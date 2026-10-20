# Research conversation: You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 158
- **Recorded user turns:** 1
- **Tool calls:** 51
- **Original source:** `logs/chats/exported-trajectories/account-3/768025f2-6d91-48cb-a9a0-91d27326c8a3.jsonl`
- **Structured JSON:** [`346d53b6e0b5b3e01a60.json`](../../sessions/34/346d53b6e0b5b3e01a60.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:48:57.257Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:48:57.257Z",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "content": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.\n\n**Today's date: 2026-05-30 (UTC).** Use this when reasoning about conference deadlines — only recommend venues whose submission deadline has NOT yet passed.\n\n## Field Guide (from literature deep dive)\n\nBelow is a strategic analysis of the top recent papers in this area. A separate research team has already read and analyzed 10-15 top-venue papers. USE THIS as your foundation — do NOT ignore it or generate ideas from scratch.\n\n{\n  \"innovation_patterns\": [\n    {\n      \"pattern\": \"Cross-domain mechanism transfer with threat-model adaptation\",\n      \"description\": \"Take a well-established technique from one domain (e.g., conformal prediction from classification) and transfer it to a new domain (e.g., RAG), but the key to acceptance is identifying and resolving the specific assumption violations the new domain introduces rather than naively applying the technique. Papers that simply apply existing methods without adaptation get rejected; papers that diagnose the mismatch AND fix it get spotlights.\",\n      \"examples\": [\n        \"TRAQ (CP from classification → RAG, but only benign)\",\n        \"RPS (partition-and-vote from DP/distributed systems → poisoning-robust CP)\",\n        \"Conformal Abstention (self-consistency from heuristic → CP-calibrated abstention)\",\n        \"SCoRE (e-values from sequential testing → selective prediction)\"\n      ],\n      \"success_rate\": \"high\"\n    },\n    {\n      \"pattern\": \"Partition-isolate-aggregate for adversarial robustness\",\n      \"description\": \"Partition inputs/data into disjoint groups, process independently, then aggregate via majority vote or MIS to bound adversarial influence. This pattern appears across robust ML, certified RAG defenses, and poisoning-robust CP. Success comes from the clean mathematical reduction: adversary corrupts ≤k' of K groups → majority/MIS resilience bounds follow from combinatorics.\",\n      \"examples\": [\n        \"RPS (partition calibration data, majority-vote prediction sets)\",\n        \"RobustRAG (partition passages into groups, keyword/decoding voting)\",\n        \"ReliabilityRAG (NLI contradiction graph → MIS for document selection)\"\n      ],\n      \"success_rate\": \"high\"\n    },\n    {\n      \"pattern\": \"Diagnosis paper creates demand, solution paper fills it\",\n      \"description\": \"A highly-cited analysis paper identifies and rigorously demonstrates a failure mode without proposing a fix. This creates a named, citable gap that a follow-up solution paper can directly address. The solution paper benefits from pre-existing reviewer awareness of the problem.\",\n      \"examples\": [\n        \"Chen et al. 2026 diagnoses CP-RAG failures → our proposed work fills this gap\",\n        \"Cherian et al. shows marginal CP hides per-topic failures → motivates group-conditional methods\",\n        \"Benchmarking paper shows all current defenses fail → motivates new defense paradigms\"\n      ],\n      \"success_rate\": \"high\"\n    },\n    {\n      \"pattern\": \"Strengthen the guarantee type (marginal → conditional → data-conditional)\",\n      \"description\": \"Take an existing method that provides marginal (average-case) guarantees and upgrade it to conditional, group-conditional, or data-conditional guarantees. Each strengthening addresses a concrete failure mode visible in experiments. Reviewers reward this because marginal guarantees are increasingly recognized as insufficient.\",\n      \"examples\": [\n        \"Cherian et al. upgrades marginal factuality to group-conditional + level-adaptive\",\n        \"Bayesian CP upgrades CRC's average guarantee to data-conditional posterior bounds, reducing violation from 45% to 5.4%\",\n        \"SCoRE provides both MDR and SDR as distinct guarantee levels\"\n      ],\n      \"success_rate\": \"high\"\n    },\n    {\n      \"pattern\": \"Simplification that reveals fundamental structure\",\n      \"description\": \"Reduce a complex attack or defense to its essential components, revealing that the problem is easier (or harder) than assumed. This shifts the conversation and redefines baselines.\",\n      \"examples\": [\n        \"CorruptRAG shows single-document poisoning achieves 95% ASR vs. PoisonedRAG's 5-doc 90% — simpler is better\",\n        \"CRC reduces all conformal prediction to a 5-line algorithm over monotone losses\",\n        \"PoisonedRAG decomposes attack into retrieval+generation conditions, enabling independent optimization\"\n      ],\n      \"success_rate\": \"medium\"\n    },\n    {\n      \"pattern\": \"Metric/evaluation innovation that redefines success\",\n      \"description\": \"Introduce new evaluation criteria that expose hidden failures of existing methods. This is lower-risk innovation but creates lasting impact when the metrics become standard.\",\n      \"examples\": [\n        \"Chen et al. introduces Non-Empty Rate and Non-Vacuous Empirical Factuality, showing previous metrics masked vacuous outputs\",\n        \"Cherian et al. shows marginal 90% factuality requires filtering 76% of claims — redefining the utility-factuality tradeoff\"\n      ],\n      \"success_rate\": \"medium\"\n    }\n  ],\n  \"reviewer_preferences\": [\n    \"Formal, distribution-free certificates with finite-sample guarantees are strongly rewarded over empirical-only defenses. RPS received ICLR Spotlight (8/8/6) largely because it provided formal coverage certificates under poisoning, not just empirical robustness. RobustRAG (SaTML 2026) and ReliabilityRAG (NeurIPS 2025) both succeed by providing formal certificates. Reviewers in SRRAI explicitly value provable guarantees.\",\n    \"Correct threat model specification matters more than technical sophistication. RPS reviewers praised the 'novel threat model' (calibration poisoning) as a primary contribution. Our work must clearly articulate WHY retrieval corruption is a different threat model from calibration poisoning and why existing tools (RPS, CAS) cannot be directly applied — reviewers who know Chen et al. (2026) will flag naive adaptations immediately.\",\n    \"Comprehensive evaluation across standardized benchmarks with multiple attack protocols. The Benchmarking paper (2025) establishes NQ, HotpotQA, MS-MARCO as the standard triple, and PoisonedRAG + CorruptRAG as the standard attacks. Papers that evaluate on only one dataset or one attack face criticism — RPS reviewers noted 'limited large-scale experiments' as a weakness.\",\n    \"Practical compute constraints and efficiency analysis. Reviewers consistently flag methods requiring excessive LLM calls (RobustRAG's m calls per query) or impractical calibration requirements. The ≤200 H100-hour budget is reasonable for the venue, but the paper should explicitly report compute costs and compare efficiency against baselines.\",\n    \"Clear articulation of what guarantee is being provided (marginal vs. conditional vs. data-conditional) and honest acknowledgment of its limitations. Bayesian CP (ICML 2025 Outstanding Paper) succeeded partly by precisely characterizing what CRC guarantees and what it doesn't. Cherian et al. succeeded by showing marginal guarantees hide dangerous per-topic variation.\",\n    \"Ablation studies that isolate the contribution of each component. Papers with multiple novel components (score function + aggregation + calibration) need to show each component's individual contribution. Reviewers penalize papers where the source of improvement is ambiguous.\",\n    \"Addressing adaptive attackers, not just oblivious ones. ReliabilityRAG explicitly models attackers who know the defense mechanism. Our certificates must hold against adaptive adversaries who know we use retrieval-agreement-based conformal scores — this rules out security-through-obscurity defenses.\"\n  ],\n  \"field_gaps\": [\n    {\n      \"gap\": \"No conformal abstention framework exists for RAG under adversarial corpus poisoning — the intersection of {conformal prediction, RAG, adversarial robustness, abstention} is completely empty\",\n      \"evidence\": \"TRAQ and C-RAG provide conformal guarantees for RAG but assume benign retrieval. RPS provides poisoning-robust CP but for classifiers with calibration poisoning, not RAG with retrieval corruption. RobustRAG and ReliabilityRAG provide certified RAG defenses but no conformal/abstention mechanism. Chen et al. (2026) diagnoses CP failures under RAG distribution shift but proposes no solution.\",\n      \"difficulty\": \"high\",\n      \"impact_if_solved\": \"high\"\n    },\n    {\n      \"gap\": \"Threat model mismatch: existing poisoning-robust CP (RPS, CAS) assumes calibration-set poisoning (wrong labels in known data) while RAG poisoning corrupts test-time retrieval (wrong documents injected at inference) — no work bridges this mismatch\",\n      \"evidence\": \"RPS explicitly addresses calibration poisoning; CAS formulates calibration-time robustness as MILP under bounded label/feature corruption. Both papers' limitations sections note they don't address test-time corruption. The retrieval corruption threat model from RobustRAG/ReliabilityRAG is fundamentally different: the adversary controls document content at test time, not labels during calibration.\",\n      \"difficulty\": \"high\",\n      \"impact_if_solved\": \"high\"\n    },\n    {\n      \"gap\": \"No method provides continuous risk control (beyond binary correct/incorrect) for RAG abstention — existing work uses binary coverage but real deployments need control over semantic error magnitude, partial correctness, or per-claim factuality rates\",\n      \"evidence\": \"SCoRE introduces risk-adjusted e-values for continuous risk control but only for classification/regression, not RAG. Conformal Factuality uses binary entailment sets. TRAQ uses binary coverage. The gap is explicitly noted in the conformal NLP survey as an open challenge.\",\n      \"difficulty\": \"medium\",\n      \"impact_if_solved\": \"high\"\n    },\n    {\n      \"gap\": \"Group-conditional or input-conditional conformal guarantees for RAG are unexplored — all existing RAG CP methods provide only marginal guarantees that hide per-topic/per-query-type variation\",\n      \"evidence\": \"Cherian et al. shows marginal coverage drops from ~95% to ~70% for low-popularity topics in closed-book LLMs. Chen et al. shows RAG conformal factuality produces vacuous outputs at high confidence for hard queries. No RAG CP method provides group-conditional or level-adaptive guarantees.\",\n      \"difficulty\": \"medium\",\n      \"impact_if_solved\": \"high\"\n    },\n    {\n      \"gap\": \"Defense evaluation against single-document poisoning (CorruptRAG) is largely missing — most defenses are tested against multi-document PoisonedRAG but single-doc attacks are harder to detect via agreement signals and more realistic\",\n      \"evidence\": \"CorruptRAG (2026) achieves 95% ASR with a single document but evaluations of RobustRAG and ReliabilityRAG focus on multi-document poisoning where agreement-based defenses have natural advantages. The Benchmarking paper includes CorruptRAG but doesn't test certified defenses against it.\",\n      \"difficulty\": \"medium\",\n      \"impact_if_solved\": \"medium\"\n    },\n    {\n      \"gap\": \"No data-conditional (as opposed to marginal) conformal guarantees exist for any NLP/RAG application — Bayesian CP's posterior bounds are only demonstrated on vision tasks\",\n      \"evidence\": \"Bayesian CP (ICML 2025 Outstanding Paper) shows CRC violates its target in up to 45% of trials and proposes L⁺ bounds that reduce violations to 5.4%, but only evaluates on MS-COCO segmentation and medical imaging. Extension to NLP and especially RAG is completely unexplored.\",\n      \"difficulty\": \"medium\",\n      \"impact_if_solved\": \"medium\"\n    },\n    {\n      \"gap\": \"Compositional guarantees across retriever + generator pipeline under adversarial conditions remain intractable — all existing work either provides guarantees for one component or uses union bounds that are too loose\",\n      \"evidence\": \"TRAQ uses union bound α_Ret + α_LLM = α which doubles the required calibration data. C-RAG provides compositional theory but only for single-layer transformers under benign conditions. The seed direction correctly identifies this as RQ1 territory to avoid.\",\n      \"difficulty\": \"high\",\n      \"impact_if_solved\": \"high\"\n    }\n  ],\n  \"untried_combinations\": [\n    {\n      \"idea_sketch\": \"Bayesian quadrature CP (data-conditional posterior bounds) + retrieval-agreement-conditioned scores for RAG abstention — replace CRC's point threshold with full posterior risk bounds, conditioned on retrieval agreement groups, to get tight data-conditional coverage under poisoning\",\n      \"from_papers\": [\n        \"Bayesian CP (ICML 2025)\",\n        \"TRAQ\",\n        \"RPS\"\n      ],\n      \"why_promising\": \"Bayesian CP reduced violation rates from 45% to 5.4% in vision; RAG calibration sets are typically small (hundreds to low thousands), exactly where data-conditional bounds matter most. The L⁺ bound's Dirichlet construction is compatible with partition-based score aggregation. This would be the first data-conditional CP for any NLP application.\"\n    },\n    {\n      \"idea_sketch\": \"SCoRE's risk-adjusted e-values + ReliabilityRAG's NLI contradiction graph — use NLI-derived agreement structure to define nonconformity scores, then apply e-value thresholding for continuous risk control (semantic error magnitude, not just binary correctness) with formal abstention certificates\",\n      \"from_papers\": [\n        \"SCoRE (2026)\",\n        \"ReliabilityRAG\",\n        \"Conformal Abstention (NeurIPS 2024)\"\n      ],\n      \"why_promising\": \"SCoRE provides the only existing framework for continuous risk control in selective prediction, and ReliabilityRAG's NLI graph captures exactly the agreement structure needed for retrieval-aware scores. The combination gives tunable risk-abstention tradeoffs with certificates — something neither method provides alone. E-values also compose naturally across groups (multiply rather than Bonferroni-correct).\"\n    },\n    {\n      \"idea_sketch\": \"Cherian et al.'s group-conditional CP with level-adaptive α(X) + retrieval quality signals as conditioning variables — vary the abstention threshold per-query based on retrieval agreement level, retriever confidence, and document diversity, with formal group-conditional coverage guarantees\",\n      \"from_papers\": [\n        \"Cherian et al. (NeurIPS 2024)\",\n        \"TRAQ\",\n        \"Chen et al. (2026)\"\n      ],\n      \"why_promising\": \"Chen et al. shows uniform thresholds produce vacuous outputs for hard queries and over-conservative results for easy ones. Level-adaptive calibration directly addresses this by learning per-query α(X) from retrieval features. The retrieval agreement structure provides natural conditioning variables that are computable without additional LLM calls.\"\n    },\n    {\n      \"idea_sketch\": \"RobustRAG's isolate-then-aggregate architecture + conformal risk control calibration — use RobustRAG's passage grouping as the isolation mechanism but replace its keyword/decoding voting with conformal-calibrated abstention decisions per group, aggregating via majority over group-level conformal sets\",\n      \"from_papers\": [\n        \"RobustRAG (SaTML 2026)\",\n        \"CRC (ICLR 2024)\",\n        \"RPS (ICLR 2025)\"\n      ],\n      \"why_promising\": \"RobustRAG already provides the computational infrastructure for isolation but lacks principled abstention (it outputs τ=0 without fallback). Conformal risk control's monotone-loss framework is directly applicable to the group-level aggregation step. This combination gives formal coverage certificates on top of certified robustness — defense-in-depth with both safety layers having formal guarantees.\"\n    },\n    {\n      \"idea_sketch\": \"CAS's CDF-based conformity score bounds + retrieval-corruption threat model — adapt CAS's distributional (not just mean-based) score bounding to handle worst-case retrieval corruption, yielding tighter prediction sets than RPS-style majority voting under the same poisoning budget\",\n      \"from_papers\": [\n        \"CAS (ICML 2024)\",\n        \"RobustRAG\",\n        \"PoisonedRAG\"\n      ],\n      \"why_promising\": \"CAS provably tightens bounds vs. RSCP/RPS by exploiting the full CDF rather than just means. In the retrieval setting, the score distribution under poisoning has specific structure (poisoned docs cluster in embedding space, producing identifiable score patterns) that CDF-based bounds can exploit. This could yield significantly smaller abstention rates for the same coverage level.\"\n    },\n    {\n      \"idea_sketch\": \"CorruptRAG's single-document threat model + conformal factuality's sub-claim decomposition — decompose RAG outputs into atomic claims, score each claim's consistency with individual retrieved passages, and apply per-claim conformal filtering where single-doc poisoning can only corrupt claims grounded in the poisoned passage\",\n      \"from_papers\": [\n        \"CorruptRAG (2026)\",\n        \"Conformal Factuality (ICML 2024)\",\n        \"Chen et al. (2026)\"\n      ],\n      \"why_promising\": \"Single-doc poisoning is the hardest case for agreement-based defenses but the easiest for per-claim analysis: only claims grounded in the single poisoned doc are affected. Sub-claim decomposition localizes the damage, and conformal filtering removes affected claims with guarantees. This addresses the key weakness of agreement-based methods against CorruptRAG.\"\n    }\n  ],\n  \"method_building_blocks\": [\n    {\n      \"tool\": \"Partition-and-vote aggregation\",\n      \"what_it_does\": \"Partitions data/documents into K disjoint groups, processes independently, aggregates via majority vote. Bounds adversarial influence to corrupted_groups/total_groups ratio. Formal certificates follow from combinatorics.\",\n      \"used_by\": [\n        \"RPS (calibration partitioning)\",\n        \"RobustRAG (passage grouping)\",\n        \"ReliabilityRAG (sampling rounds)\"\n      ],\n      \"could_be_applied_to\": \"Retrieval-agreement-conditioned conformal scores: partition retrieved passages, compute per-group nonconformity scores, aggregate via majority over group-level conformal sets to get poisoning-robust coverage\"\n    },\n    {\n      \"tool\": \"NLI-based contradiction graph + MIS\",\n      \"what_it_does\": \"Constructs a graph where nodes are documents/responses and edges indicate NLI-detected contradiction. Maximum Independent Set finds the largest non-contradicting subset, naturally excluding adversarial documents that contradict the benign majority.\",\n      \"used_by\": [\n        \"ReliabilityRAG\"\n      ],\n      \"could_be_applied_to\": \"Defining retrieval-agreement nonconformity scores: the MIS size relative to total documents is a natural agreement signal; documents excluded from MIS are candidate adversarial passages; the gap between MIS size and total docs bounds poisoning severity\"\n    },\n    {\n      \"tool\": \"Conformal risk control (CRC) with monotone losses\",\n      \"what_it_does\": \"5-line algorithm that finds threshold λ̂ controlling E[L(λ̂)] ≤ α for any monotone, bounded loss function. Extends to distribution shift via TV distance bounds, multiple simultaneous risks, and adversarial worst-case.\",\n      \"used_by\": [\n        \"CRC (ICLR 2024)\",\n        \"Conformal Abstention (NeurIPS 2024)\",\n        \"SCoRE\"\n      ],\n      \"could_be_applied_to\": \"Calibrating the abstention threshold for RAG under poisoning: the abstention loss (1 if incorrect AND not abstained, 0 otherwise) is monotone in the abstention threshold, and the distribution shift extension provides a template for bounding coverage degradation under bounded corpus poisoning\"\n    },\n    {\n      \"tool\": \"Self-consistency scoring via LLM sampling\",\n      \"what_it_does\": \"Samples k responses per query, measures pairwise agreement (ROUGE, NLI, LLM-as-judge), and uses agreement level as a nonconformity/confidence score. Higher agreement → higher confidence in the answer.\",\n      \"used_by\": [\n        \"Conformal Abstention (NeurIPS 2024)\",\n        \"TRAQ (generator NCM)\",\n        \"Conformal Language Modeling\"\n      ],\n      \"could_be_applied_to\": \"Retrieval-conditioned self-consistency: compute self-consistency separately for each passage group's responses, then aggregate. Poisoned passages produce inconsistent responses across groups, yielding low group-conditional consistency scores that trigger abstention\"\n    },\n    {\n      \"tool\": \"Risk-adjusted e-values\",\n      \"what_it_does\": \"Defines e-values E where E[E·L] ≤ 1 (not E[E] ≤ 1), enabling continuous risk control via Markov thresholding. Composes multiplicatively across independent tests. Extends to covariate shift via importance weighting.\",\n      \"used_by\": [\n... (truncated)\n\n## How to use the field guide\n\n1. **Innovation patterns**: Prefer idea types that have a proven track record of acceptance. If 'cross-domain transfer' and 'simplification' keep working, lean toward those.\n2. **Field gaps**: These are VERIFIED gaps from actual paper limitations — much more reliable than gaps you might guess from pre-training knowledge. Prioritize these.\n3. **Untried combinations**: These are specific leads from the literature team. Validate each one (is it truly untried?) and develop the most promising ones.\n4. **Reviewer preferences**: Shape your ideas to match what reviewers reward. If reviewers care about 'strong baselines and ablations', bake that into the idea design.\n5. **Common pitfalls**: Explicitly check each idea against these before proposing it.\n6. **Building blocks**: Use existing tools/methods that are available rather than inventing everything.\n\n**Critical rule**: Every idea you propose should be traceable to evidence from the field guide. For each idea, you must be able to say: 'This is inspired by gap X / pattern Y / combination Z.'\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n这不是快速脑暴——这是一项需要深入研究和严谨思考的任务。你必须像一个资深研究员一样，先充分了解领域现状，再深思熟虑地提出有价值的方向。\n\n### 调研要求\n\n1. **广度**：理想情况下做 10-15 次有针对性的搜索，覆盖：\n   - 当前 SOTA 方法及其具体性能数字\n   - SOTA 的已知局限和失败场景\n   - 近 12 个月的 survey 论文（掌握领域全貌）\n   - 可迁移的跨领域方法\n   - Benchmark 排行榜（获得定量基准）\n\n2. **深度**：对每个有潜力的方向做追踪调研：\n   - 用 WebFetch 阅读关键论文的核心内容（不只是看搜索结果标题）\n   - 查找独立复现结果来验证论文 claim\n   - 检查你发现的 gap 是否已被最近 3 个月的工作解决\n\n### 思考要求\n\n3. **批判性思维**（在生成每个 idea 之前，先停下来认真思考）：\n   - \"如果我是一个怀疑论的 reviewer，我会质疑什么？\"\n   - \"有没有更简单的 baseline 能达到类似效果？\"\n   - \"这真的解决了一个实际问题，还是只是边际改进？\"\n   - \"这个方向为什么现在可以做，之前为什么没人做？\"\n\n4. **深度思考**：\n   - 不要从浅层理解出发生成 idea——每个 idea 必须建立在具体论文、具体数字、具体 gap 之上\n   - 思考不同方法之间的联系和矛盾——这往往是创新的来源\n   - 考虑方法的 scalability 和 generalizability\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} 2026 site:scholar.google.com`\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} 2026` — 按活跃作者追踪\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey 2026` — 找综述论文\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n\n### 搜索维度\n\n1. **正向搜索**：直接搜索主题相关论文\n2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？\n3. **相邻领域搜索**：其他领域是否已解决类似问题\n4. **反面搜索**：找到反对你 idea 的证据\n5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work\n\n\n**Landscape freshness rule**: Your training data may be outdated. When assessing SOTA in the landscape field, ONLY cite methods/results you found via web_search in this session — do NOT fall back to pre-training knowledge for what the current best methods or benchmarks are. If your searches don't surface clear SOTA for a direction, add an extra search specifically for \"{topic} benchmark SOTA 2026\" or \"{{topic}} leaderboard\" before writing the landscape.\n\n## Novelty assessment standard\nWhen evaluating novelty via web_search:\n| Related papers found | Verdict | Action |\n|:---:|---|---|\n| 0-2 | Novel | Proceed |\n| 3-5 | Existing work | Keep but note related work and differentiation |\n| >5 | Mature field | Pivot to a differentiated angle |\n\n## Seed topic\n**Target: AAAI 2026\nTrack: Safe, Robust and Responsible AI (SRRAI)\n\nDirection: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.\n\nSeed Papers:\n- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval\n- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG\n- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative\n- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on\n- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition\n\nKnown Gaps:\n- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)\n- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails\n- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis\n\nTheoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must compare against RobustRAG and ReliabilityRAG baselines\n- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols\n- AAAI 2026 submission deadline: August 2026\n\nQuality Self-Checks:\n- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.\n- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.\n- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.\n- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.\n\nAvoid:\n- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this\n- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead\n- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates**\n\nFormulate 1 research direction(s) grounded in real evidence.\n\n## Output format (Round 1)\nAfter completing your research, output a JSON array. Each element has ONLY these fields:\n{\n  \"title\": \"Concise English title (max 10 words)\",\n  \"core_problem\": \"The fundamental research question (1-2 sentences)\",\n  \"opportunity\": \"The specific gap or why now (2-3 sentences)\",\n  \"landscape\": \"Current SOTA and key limitations, grounded in papers you found (3-5 sentences)\",\n  \"inspired_by\": \"Which field guide evidence (gap/pattern/combination) inspired this idea\"\n}\nIMPORTANT: You MUST end your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:48:57.260Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:48:57.260Z",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

## Round 1

156 recorded events

### User

_source line 3 · 2026-05-30T06:48:57.315Z_

You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.

**Today's date: 2026-05-30 (UTC).** Use this when reasoning about conference deadlines — only recommend venues whose submission deadline has NOT yet passed.

## Field Guide (from literature deep dive)

Below is a strategic analysis of the top recent papers in this area. A separate research team has already read and analyzed 10-15 top-venue papers. USE THIS as your foundation — do NOT ignore it or generate ideas from scratch.

{
  "innovation_patterns": [
    {
      "pattern": "Cross-domain mechanism transfer with threat-model adaptation",
      "description": "Take a well-established technique from one domain (e.g., conformal prediction from classification) and transfer it to a new domain (e.g., RAG), but the key to acceptance is identifying and resolving the specific assumption violations the new domain introduces rather than naively applying the technique. Papers that simply apply existing methods without adaptation get rejected; papers that diagnose the mismatch AND fix it get spotlights.",
      "examples": [
        "TRAQ (CP from classification → RAG, but only benign)",
        "RPS (partition-and-vote from DP/distributed systems → poisoning-robust CP)",
        "Conformal Abstention (self-consistency from heuristic → CP-calibrated abstention)",
        "SCoRE (e-values from sequential testing → selective prediction)"
      ],
      "success_rate": "high"
    },
    {
      "pattern": "Partition-isolate-aggregate for adversarial robustness",
      "description": "Partition inputs/data into disjoint groups, process independently, then aggregate via majority vote or MIS to bound adversarial influence. This pattern appears across robust ML, certified RAG defenses, and poisoning-robust CP. Success comes from the clean mathematical reduction: adversary corrupts ≤k' of K groups → majority/MIS resilience bounds follow from combinatorics.",
      "examples": [
        "RPS (partition calibration data, majority-vote prediction sets)",
        "RobustRAG (partition passages into groups, keyword/decoding voting)",
        "ReliabilityRAG (NLI contradiction graph → MIS for document selection)"
      ],
      "success_rate": "high"
    },
    {
      "pattern": "Diagnosis paper creates demand, solution paper fills it",
      "description": "A highly-cited analysis paper identifies and rigorously demonstrates a failure mode without proposing a fix. This creates a named, citable gap that a follow-up solution paper can directly address. The solution paper benefits from pre-existing reviewer awareness of the problem.",
      "examples": [
        "Chen et al. 2026 diagnoses CP-RAG failures → our proposed work fills this gap",
        "Cherian et al. shows marginal CP hides per-topic failures → motivates group-conditional methods",
        "Benchmarking paper shows all current defenses fail → motivates new defense paradigms"
      ],
      "success_rate": "high"
    },
    {
      "pattern": "Strengthen the guarantee type (marginal → conditional → data-conditional)",
      "description": "Take an existing method that provides marginal (average-case) guarantees and upgrade it to conditional, group-conditional, or data-conditional guarantees. Each strengthening addresses a concrete failure mode visible in experiments. Reviewers reward this because marginal guarantees are increasingly recognized as insufficient.",
      "examples": [
        "Cherian et al. upgrades marginal factuality to group-conditional + level-adaptive",
        "Bayesian CP upgrades CRC's average guarantee to data-conditional posterior bounds, reducing violation from 45% to 5.4%",
        "SCoRE provides both MDR and SDR as distinct guarantee levels"
      ],
      "success_rate": "high"
    },
    {
      "pattern": "Simplification that reveals fundamental structure",
      "description": "Reduce a complex attack or defense to its essential components, revealing that the problem is easier (or harder) than assumed. This shifts the conversation and redefines baselines.",
      "examples": [
        "CorruptRAG shows single-document poisoning achieves 95% ASR vs. PoisonedRAG's 5-doc 90% — simpler is better",
        "CRC reduces all conformal prediction to a 5-line algorithm over monotone losses",
        "PoisonedRAG decomposes attack into retrieval+generation conditions, enabling independent optimization"
      ],
      "success_rate": "medium"
    },
    {
      "pattern": "Metric/evaluation innovation that redefines success",
      "description": "Introduce new evaluation criteria that expose hidden failures of existing methods. This is lower-risk innovation but creates lasting impact when the metrics become standard.",
      "examples": [
        "Chen et al. introduces Non-Empty Rate and Non-Vacuous Empirical Factuality, showing previous metrics masked vacuous outputs",
        "Cherian et al. shows marginal 90% factuality requires filtering 76% of claims — redefining the utility-factuality tradeoff"
      ],
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
      "from_papers": [
        "Bayesian CP (ICML 2025)",
        "TRAQ",
        "RPS"
      ],
      "why_promising": "Bayesian CP reduced violation rates from 45% to 5.4% in vision; RAG calibration sets are typically small (hundreds to low thousands), exactly where data-conditional bounds matter most. The L⁺ bound's Dirichlet construction is compatible with partition-based score aggregation. This would be the first data-conditional CP for any NLP application."
    },
    {
      "idea_sketch": "SCoRE's risk-adjusted e-values + ReliabilityRAG's NLI contradiction graph — use NLI-derived agreement structure to define nonconformity scores, then apply e-value thresholding for continuous risk control (semantic error magnitude, not just binary correctness) with formal abstention certificates",
      "from_papers": [
        "SCoRE (2026)",
        "ReliabilityRAG",
        "Conformal Abstention (NeurIPS 2024)"
      ],
      "why_promising": "SCoRE provides the only existing framework for continuous risk control in selective prediction, and ReliabilityRAG's NLI graph captures exactly the agreement structure needed for retrieval-aware scores. The combination gives tunable risk-abstention tradeoffs with certificates — something neither method provides alone. E-values also compose naturally across groups (multiply rather than Bonferroni-correct)."
    },
    {
      "idea_sketch": "Cherian et al.'s group-conditional CP with level-adaptive α(X) + retrieval quality signals as conditioning variables — vary the abstention threshold per-query based on retrieval agreement level, retriever confidence, and document diversity, with formal group-conditional coverage guarantees",
      "from_papers": [
        "Cherian et al. (NeurIPS 2024)",
        "TRAQ",
        "Chen et al. (2026)"
      ],
      "why_promising": "Chen et al. shows uniform thresholds produce vacuous outputs for hard queries and over-conservative results for easy ones. Level-adaptive calibration directly addresses this by learning per-query α(X) from retrieval features. The retrieval agreement structure provides natural conditioning variables that are computable without additional LLM calls."
    },
    {
      "idea_sketch": "RobustRAG's isolate-then-aggregate architecture + conformal risk control calibration — use RobustRAG's passage grouping as the isolation mechanism but replace its keyword/decoding voting with conformal-calibrated abstention decisions per group, aggregating via majority over group-level conformal sets",
      "from_papers": [
        "RobustRAG (SaTML 2026)",
        "CRC (ICLR 2024)",
        "RPS (ICLR 2025)"
      ],
      "why_promising": "RobustRAG already provides the computational infrastructure for isolation but lacks principled abstention (it outputs τ=0 without fallback). Conformal risk control's monotone-loss framework is directly applicable to the group-level aggregation step. This combination gives formal coverage certificates on top of certified robustness — defense-in-depth with both safety layers having formal guarantees."
    },
    {
      "idea_sketch": "CAS's CDF-based conformity score bounds + retrieval-corruption threat model — adapt CAS's distributional (not just mean-based) score bounding to handle worst-case retrieval corruption, yielding tighter prediction sets than RPS-style majority voting under the same poisoning budget",
      "from_papers": [
        "CAS (ICML 2024)",
        "RobustRAG",
        "PoisonedRAG"
      ],
      "why_promising": "CAS provably tightens bounds vs. RSCP/RPS by exploiting the full CDF rather than just means. In the retrieval setting, the score distribution under poisoning has specific structure (poisoned docs cluster in embedding space, producing identifiable score patterns) that CDF-based bounds can exploit. This could yield significantly smaller abstention rates for the same coverage level."
    },
    {
      "idea_sketch": "CorruptRAG's single-document threat model + conformal factuality's sub-claim decomposition — decompose RAG outputs into atomic claims, score each claim's consistency with individual retrieved passages, and apply per-claim conformal filtering where single-doc poisoning can only corrupt claims grounded in the poisoned passage",
      "from_papers": [
        "CorruptRAG (2026)",
        "Conformal Factuality (ICML 2024)",
        "Chen et al. (2026)"
      ],
      "why_promising": "Single-doc poisoning is the hardest case for agreement-based defenses but the easiest for per-claim analysis: only claims grounded in the single poisoned doc are affected. Sub-claim decomposition localizes the damage, and conformal filtering removes affected claims with guarantees. This addresses the key weakness of agreement-based methods against CorruptRAG."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "Partition-and-vote aggregation",
      "what_it_does": "Partitions data/documents into K disjoint groups, processes independently, aggregates via majority vote. Bounds adversarial influence to corrupted_groups/total_groups ratio. Formal certificates follow from combinatorics.",
      "used_by": [
        "RPS (calibration partitioning)",
        "RobustRAG (passage grouping)",
        "ReliabilityRAG (sampling rounds)"
      ],
      "could_be_applied_to": "Retrieval-agreement-conditioned conformal scores: partition retrieved passages, compute per-group nonconformity scores, aggregate via majority over group-level conformal sets to get poisoning-robust coverage"
    },
    {
      "tool": "NLI-based contradiction graph + MIS",
      "what_it_does": "Constructs a graph where nodes are documents/responses and edges indicate NLI-detected contradiction. Maximum Independent Set finds the largest non-contradicting subset, naturally excluding adversarial documents that contradict the benign majority.",
      "used_by": [
        "ReliabilityRAG"
      ],
      "could_be_applied_to": "Defining retrieval-agreement nonconformity scores: the MIS size relative to total documents is a natural agreement signal; documents excluded from MIS are candidate adversarial passages; the gap between MIS size and total docs bounds poisoning severity"
    },
    {
      "tool": "Conformal risk control (CRC) with monotone losses",
      "what_it_does": "5-line algorithm that finds threshold λ̂ controlling E[L(λ̂)] ≤ α for any monotone, bounded loss function. Extends to distribution shift via TV distance bounds, multiple simultaneous risks, and adversarial worst-case.",
      "used_by": [
        "CRC (ICLR 2024)",
        "Conformal Abstention (NeurIPS 2024)",
        "SCoRE"
      ],
      "could_be_applied_to": "Calibrating the abstention threshold for RAG under poisoning: the abstention loss (1 if incorrect AND not abstained, 0 otherwise) is monotone in the abstention threshold, and the distribution shift extension provides a template for bounding coverage degradation under bounded corpus poisoning"
    },
    {
      "tool": "Self-consistency scoring via LLM sampling",
      "what_it_does": "Samples k responses per query, measures pairwise agreement (ROUGE, NLI, LLM-as-judge), and uses agreement level as a nonconformity/confidence score. Higher agreement → higher confidence in the answer.",
      "used_by": [
        "Conformal Abstention (NeurIPS 2024)",
        "TRAQ (generator NCM)",
        "Conformal Language Modeling"
      ],
      "could_be_applied_to": "Retrieval-conditioned self-consistency: compute self-consistency separately for each passage group's responses, then aggregate. Poisoned passages produce inconsistent responses across groups, yielding low group-conditional consistency scores that trigger abstention"
    },
    {
      "tool": "Risk-adjusted e-values",
      "what_it_does": "Defines e-values E where E[E·L] ≤ 1 (not E[E] ≤ 1), enabling continuous risk control via Markov thresholding. Composes multiplicatively across independent tests. Extends to covariate shift via importance weighting.",
      "used_by": [
... (truncated)

## How to use the field guide

1. **Innovation patterns**: Prefer idea types that have a proven track record of acceptance. If 'cross-domain transfer' and 'simplification' keep working, lean toward those.
2. **Field gaps**: These are VERIFIED gaps from actual paper limitations — much more reliable than gaps you might guess from pre-training knowledge. Prioritize these.
3. **Untried combinations**: These are specific leads from the literature team. Validate each one (is it truly untried?) and develop the most promising ones.
4. **Reviewer preferences**: Shape your ideas to match what reviewers reward. If reviewers care about 'strong baselines and ablations', bake that into the idea design.
5. **Common pitfalls**: Explicitly check each idea against these before proposing it.
6. **Building blocks**: Use existing tools/methods that are available rather than inventing everything.

**Critical rule**: Every idea you propose should be traceable to evidence from the field guide. For each idea, you must be able to say: 'This is inspired by gap X / pattern Y / combination Z.'

## 核心要求：非常仔细地调研，非常仔细地思考

这不是快速脑暴——这是一项需要深入研究和严谨思考的任务。你必须像一个资深研究员一样，先充分了解领域现状，再深思熟虑地提出有价值的方向。

### 调研要求

1. **广度**：理想情况下做 10-15 次有针对性的搜索，覆盖：
   - 当前 SOTA 方法及其具体性能数字
   - SOTA 的已知局限和失败场景
   - 近 12 个月的 survey 论文（掌握领域全貌）
   - 可迁移的跨领域方法
   - Benchmark 排行榜（获得定量基准）

2. **深度**：对每个有潜力的方向做追踪调研：
   - 用 WebFetch 阅读关键论文的核心内容（不只是看搜索结果标题）
   - 查找独立复现结果来验证论文 claim
   - 检查你发现的 gap 是否已被最近 3 个月的工作解决

### 思考要求

3. **批判性思维**（在生成每个 idea 之前，先停下来认真思考）：
   - "如果我是一个怀疑论的 reviewer，我会质疑什么？"
   - "有没有更简单的 baseline 能达到类似效果？"
   - "这真的解决了一个实际问题，还是只是边际改进？"
   - "这个方向为什么现在可以做，之前为什么没人做？"

4. **深度思考**：
   - 不要从浅层理解出发生成 idea——每个 idea 必须建立在具体论文、具体数字、具体 gap 之上
   - 思考不同方法之间的联系和矛盾——这往往是创新的来源
   - 考虑方法的 scalability 和 generalizability


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


**Landscape freshness rule**: Your training data may be outdated. When assessing SOTA in the landscape field, ONLY cite methods/results you found via web_search in this session — do NOT fall back to pre-training knowledge for what the current best methods or benchmarks are. If your searches don't surface clear SOTA for a direction, add an extra search specifically for "{topic} benchmark SOTA 2026" or "{{topic}} leaderboard" before writing the landscape.

## Novelty assessment standard
When evaluating novelty via web_search:
| Related papers found | Verdict | Action |
|:---:|---|---|
| 0-2 | Novel | Proceed |
| 3-5 | Existing work | Keep but note related work and differentiation |
| >5 | Mature field | Pivot to a differentiated angle |

## Seed topic
**Target: AAAI 2026
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
- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates**

Formulate 1 research direction(s) grounded in real evidence.

## Output format (Round 1)
After completing your research, output a JSON array. Each element has ONLY these fields:
{
  "title": "Concise English title (max 10 words)",
  "core_problem": "The fundamental research question (1-2 sentences)",
  "opportunity": "The specific gap or why now (2-3 sentences)",
  "landscape": "Current SOTA and key limitations, grounded in papers you found (3-5 sentences)",
  "inspired_by": "Which field guide evidence (gap/pattern/combination) inspired this idea"
}
IMPORTANT: You MUST end your response with the JSON array.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "8363dcaa-89d1-43d0-b7be-52cdbf492974",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:48:57.314Z_

```json
{
  "parentUuid": "8363dcaa-89d1-43d0-b7be-52cdbf492974",
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
  "uuid": "51b48dab-0ca7-4fce-b9c3-ec6b515b6ef4",
  "timestamp": "2026-05-30T06:48:57.314Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:48:57.314Z_

```json
{
  "parentUuid": "51b48dab-0ca7-4fce-b9c3-ec6b515b6ef4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a096b57f-e19f-4f32-8c4c-e919aa6fda59",
  "timestamp": "2026-05-30T06:48:57.314Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
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
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "a096b57f-e19f-4f32-8c4c-e919aa6fda59",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Assistant

_source line 8 · 2026-05-30T06:49:08.031Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate a well-grounded research direction for a conformal-prediction-based abstention framework for RAG systems under adversarial corpus poisoning. They want me to do deep research first, then output a JSON array with 1 research direction.

Let me start by doing thorough web searches to understand the current landscape, verify the gaps mentioned in the field guide, and check for any recent work that might have filled these gaps.

Let me plan my searches:

1. Search for recent work on conformal prediction + RAG + adversarial/poisoning
2. Search for RPS (Reliable Prediction Sets) and its extensions


3. Now I'm searching for the latest results on RobustRAG and ReliabilityRAG, along with recent work on conformal factuality in RAG systems from Chen et al. 2026
4. I'm also checking for CorruptRAG and PoisonedRAG benchmarks, confirming the AAAI 2026 deadline, and looking for any concurrent work that might address the identified gap
5. I'm searching for conformal abstention methods, distribution shift robustness in conformal prediction, and recent adversarial robustness work combined with conformal approaches

Let me launch multiple search agents in parallel to gather this information efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a096b57f-e19f-4f32-8c4c-e919aa6fda59",
  "isSidechain": false,
  "requestId": "req_011CbYJmLstuTc3bGG6kpTcs",
  "type": "assistant",
  "uuid": "80392c92-38c5-4d0b-b8eb-4da06c3063e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AF95GKPhw3T4Zv94h5DfDw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9528,
      "cache_read_input_tokens": 11014,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 9528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9528
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

_source line 9 · 2026-05-30T06:49:08.054Z_

I'll conduct deep research across multiple dimensions simultaneously to ground this idea properly. Let me start with parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80392c92-38c5-4d0b-b8eb-4da06c3063e9",
  "isSidechain": false,
  "requestId": "req_011CbYJmLstuTc3bGG6kpTcs",
  "type": "assistant",
  "uuid": "16a339ea-4801-4ea1-b0ff-8d426fbf8e90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AF95GKPhw3T4Zv94h5DfDw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9528,
      "cache_read_input_tokens": 11014,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 9528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9528
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

_source line 10 · 2026-05-30T06:49:08.137Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ais6wUhksy6JJ6bH7Jffdw`</summary>

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
  "parentUuid": "16a339ea-4801-4ea1-b0ff-8d426fbf8e90",
  "isSidechain": false,
  "requestId": "req_011CbYJmLstuTc3bGG6kpTcs",
  "type": "assistant",
  "uuid": "edd5a976-01f5-4903-8355-b095554ca399",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AF95GKPhw3T4Zv94h5DfDw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9528,
      "cache_read_input_tokens": 11014,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 9528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9528
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

_source line 11 · 2026-05-30T06:49:08.145Z_

<details><summary>↩ Tool result · `toolu_01Ais6wUhksy6JJ6bH7Jffdw`</summary>

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
  "parentUuid": "edd5a976-01f5-4903-8355-b095554ca399",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "77dc860b-4260-42c7-b0d4-df40b51310fd",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "edd5a976-01f5-4903-8355-b095554ca399",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-30T06:49:11.666Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have WebSearch and WebFetch available. Let me launch multiple parallel searches to cover the landscape thoroughly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77dc860b-4260-42c7-b0d4-df40b51310fd",
  "isSidechain": false,
  "requestId": "req_011CbYJn9Jf5urDokeLY3YrH",
  "type": "assistant",
  "uuid": "938f9fd3-66df-4097-b7f3-acf8efa264db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdnPz4xydTyaipWCtFKC6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 20542,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 20542,
          "cache_creation_input_tokens": 1408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1408
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

_source line 13 · 2026-05-30T06:49:12.453Z_

Now let me launch comprehensive parallel searches across multiple dimensions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "938f9fd3-66df-4097-b7f3-acf8efa264db",
  "isSidechain": false,
  "requestId": "req_011CbYJn9Jf5urDokeLY3YrH",
  "type": "assistant",
  "uuid": "33306850-f759-4fbb-a44c-a05a3c0d4b02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdnPz4xydTyaipWCtFKC6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 20542,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 20542,
          "cache_creation_input_tokens": 1408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1408
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

_source line 14 · 2026-05-30T06:49:13.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017NP6EtnB5d5k6GaezcvD4M`</summary>

```json
{
  "query": "conformal prediction RAG retrieval augmented generation adversarial poisoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33306850-f759-4fbb-a44c-a05a3c0d4b02",
  "isSidechain": false,
  "requestId": "req_011CbYJn9Jf5urDokeLY3YrH",
  "type": "assistant",
  "uuid": "27102dbc-7740-4f87-92c1-eabe739fab19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdnPz4xydTyaipWCtFKC6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 20542,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 20542,
          "cache_creation_input_tokens": 1408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1408
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

_source line 15 · 2026-05-30T06:49:20.749Z_

<details><summary>↩ Tool result · `toolu_017NP6EtnB5d5k6GaezcvD4M`</summary>

```text
Web search results for query: "conformal prediction RAG retrieval augmented generation adversarial poisoning 2025 2026"

Links: [{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"},{"title":"[2508.02835] Defending Against Knowledge Poisoning Attacks During Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2508.02835"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"Exploring knowledge poisoning attacks to retrieval-augmented generation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1566253525009625"}]

Based on the search results, I found several relevant papers and resources on conformal prediction, RAG (Retrieval-Augmented Generation), and adversarial poisoning from 2025-2026:

## Key Research Areas

**Conformal Prediction for RAG:**
Certified detection of hallucinations in RAG-generated responses is addressed via conformal prediction guardrails (Sinha, 17 Dec 2025). Additionally, there is work on "Conformalized Answer Set Prediction for Knowledge Graph Embedding" (2024.08).

**Adversarial Poisoning Attacks Against RAG:**
The research shows significant recent work on poisoning vulnerabilities. RAG systems are vulnerable to various adversarial poisoning attacks by injecting adversarial data into the underlying RAG database, attackers can manipulate the retriever to return factually incorrect information. A paper titled "RAG Safety: Exploring Knowledge Poisoning Attacks to Retrieval-Augmented Generation" was published in January 2026.

**Defense Mechanisms (2025-2026):**
Recent defenses include: knowledge expansion defense (Zou et al., 2025) enhances retrieval robustness by enlarging the set of retrieved top-ranked documents; RevPRAG (Tan et al., 2025) detects poisoned responses through distinctive LLM activation patterns during generation; and AV Filter (Choudhary et al., 2026) uses passage-level attention-variance signals to identify retrieved passages that exert anomalously strong influence on the output.

These emerging research areas reflect growing concerns about the security and robustness of RAG systems in production environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27102dbc-7740-4f87-92c1-eabe739fab19",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "2ba5d532-52bb-4acb-bda9-4d0d59b15c56",
  "toolUseResult": {
    "query": "conformal prediction RAG retrieval augmented generation adversarial poisoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NqB8kihx39bg3ty1VMm1UW",
        "content": [
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2504.03957v2"
          },
          {
            "title": "[2508.02835] Defending Against Knowledge Poisoning Attacks During Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2508.02835"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions",
            "url": "https://arxiv.org/html/2604.08304v1"
          },
          {
            "title": "Certified Defenses for RAG Systems",
            "url": "https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"
          },
          {
            "title": "Exploring knowledge poisoning attacks to retrieval-augmented generation - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S1566253525009625"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources on conformal prediction, RAG (Retrieval-Augmented Generation), and adversarial poisoning from 2025-2026:\n\n## Key Research Areas\n\n**Conformal Prediction for RAG:**\nCertified detection of hallucinations in RAG-generated responses is addressed via conformal prediction guardrails (Sinha, 17 Dec 2025). Additionally, there is work on \"Conformalized Answer Set Prediction for Knowledge Graph Embedding\" (2024.08).\n\n**Adversarial Poisoning Attacks Against RAG:**\nThe research shows significant recent work on poisoning vulnerabilities. RAG systems are vulnerable to various adversarial poisoning attacks by injecting adversarial data into the underlying RAG database, attackers can manipulate the retriever to return factually incorrect information. A paper titled \"RAG Safety: Exploring Knowledge Poisoning Attacks to Retrieval-Augmented Generation\" was published in January 2026.\n\n**Defense Mechanisms (2025-2026):**\nRecent defenses include: knowledge expansion defense (Zou et al., 2025) enhances retrieval robustness by enlarging the set of retrieved top-ranked documents; RevPRAG (Tan et al., 2025) detects poisoned responses through distinctive LLM activation patterns during generation; and AV Filter (Choudhary et al., 2026) uses passage-level attention-variance signals to identify retrieved passages that exert anomalously strong influence on the output.\n\nThese emerging research areas reflect growing concerns about the security and robustness of RAG systems in production environments."
    ],
    "durationSeconds": 7.6893762190000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "27102dbc-7740-4f87-92c1-eabe739fab19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-30T06:49:24.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XYsF4VysymL23gEjGn2DEk`</summary>

```json
{
  "query": "TRAQ trustworthy retrieval augmented question answering conformal prediction NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba5d532-52bb-4acb-bda9-4d0d59b15c56",
  "isSidechain": false,
  "requestId": "req_011CbYJo6GsUFWbmqPYeFAV5",
  "type": "assistant",
  "uuid": "1905c365-40c8-4c7d-ac3e-eefad050521a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174Y2LJqNjdPSRWSjsAv4B5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 21950,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 21950,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 944
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

_source line 17 · 2026-05-30T06:49:29.786Z_

<details><summary>↩ Tool result · `toolu_01XYsF4VysymL23gEjGn2DEk`</summary>

```text
Web search results for query: "TRAQ trustworthy retrieval augmented question answering conformal prediction NAACL 2024"

Links: [{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TRAQ:-Trustworthy-Retrieval-Augmented-Question-via-Li-Park/28e078b52a761cf3fe5941d3428acb7bbf608f21"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Underline","url":"https://underline.io/lecture/97447-traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"},{"title":"[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/abs/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"}]

I found comprehensive information about TRAQ from the search results. Here's what the paper is about:

## Overview

TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction was presented at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024) in Mexico City. The paper is authored by Shuo Li, Sangdon Park, Insup Lee, and Osbert Bastani.

## Problem and Motivation

When applied to open-domain question answering, large language models (LLMs) frequently generate incorrect responses based on made-up facts called hallucinations. While retrieval augmented generation (RAG) is a promising strategy to avoid hallucinations, it does not provide guarantees on its correctness.

## Solution

TRAQ provides the first end-to-end statistical correctness guarantee for RAG. It uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. Additionally, TRAQ leverages Bayesian optimization to minimize the size of the constructed sets.

## Results

In extensive experimental evaluation, TRAQ demonstrated that it provides the desired correctness guarantee while reducing prediction set size by 16.2% on average.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1905c365-40c8-4c7d-ac3e-eefad050521a",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "1131e5e9-e316-4140-888f-fdf39ae49688",
  "toolUseResult": {
    "query": "TRAQ trustworthy retrieval augmented question answering conformal prediction NAACL 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_014S6AKr7oCLUqHWJfKo9tpc",
        "content": [
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.210/"
          },
          {
            "title": "[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/TRAQ:-Trustworthy-Retrieval-Augmented-Question-via-Li-Park/28e078b52a761cf3fe5941d3428acb7bbf608f21"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Underline",
            "url": "https://underline.io/lecture/97447-traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"
          },
          {
            "title": "[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction",
            "url": "https://arxiv.org/pdf/2307.04642"
          },
          {
            "title": "[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/abs/2307.04642"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/html/2307.04642v2"
          },
          {
            "title": "Accepted Papers - NAACL-HLT 2024",
            "url": "https://2024.naacl.org/program/accepted_papers/"
          }
        ]
      },
      "I found comprehensive information about TRAQ from the search results. Here's what the paper is about:\n\n## Overview\n\nTRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction was presented at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024) in Mexico City. The paper is authored by Shuo Li, Sangdon Park, Insup Lee, and Osbert Bastani.\n\n## Problem and Motivation\n\nWhen applied to open-domain question answering, large language models (LLMs) frequently generate incorrect responses based on made-up facts called hallucinations. While retrieval augmented generation (RAG) is a promising strategy to avoid hallucinations, it does not provide guarantees on its correctness.\n\n## Solution\n\nTRAQ provides the first end-to-end statistical correctness guarantee for RAG. It uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. Additionally, TRAQ leverages Bayesian optimization to minimize the size of the constructed sets.\n\n## Results\n\nIn extensive experimental evaluation, TRAQ demonstrated that it provides the desired correctness guarantee while reducing prediction set size by 16.2% on average."
    ],
    "durationSeconds": 5.423740513999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1905c365-40c8-4c7d-ac3e-eefad050521a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-30T06:49:32.323Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YWUo3FR8GFaWQJcJhR9RLW`</summary>

```json
{
  "query": "RPS provably reliable conformal prediction sets data poisoning ICLR 2025 spotlight"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1131e5e9-e316-4140-888f-fdf39ae49688",
  "isSidechain": false,
  "requestId": "req_011CbYJojWVDEZs8KsVUMeF4",
  "type": "assistant",
  "uuid": "9863a105-0ee5-4220-aeec-1daf1b950c8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kh7LHYaSZyJqLp3iMtLciU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 22894,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 22894,
          "cache_creation_input_tokens": 967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 967
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

_source line 19 · 2026-05-30T06:49:41.017Z_

<details><summary>↩ Tool result · `toolu_01YWUo3FR8GFaWQJcJhR9RLW`</summary>

```text
Web search results for query: "RPS provably reliable conformal prediction sets data poisoning ICLR 2025 spotlight"

Links: [{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://iclr.cc/virtual/2025/poster/28340"},{"title":"PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"},{"title":"Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning","url":"https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"},{"title":"[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://arxiv.org/abs/2410.09878"},{"title":"provably reliable conformal prediction sets","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"}]

I found information about the paper you're searching for. Here's what I found:

"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning" is an ICLR 2025 Spotlight paper. The paper is authored by Yan Scholten, Stephan Günnemann, and Leo Schwinn.

The paper proposes reliable prediction sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. 

The key contributions include:
- Smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data to ensure reliability under training poisoning
- Construction of multiple prediction sets, each calibrated on distinct subsets of the calibration data to ensure reliability under calibration poisoning

A reference implementation is available on GitHub with demo notebooks showing how to compute reliable conformal prediction sets under calibration poisoning and under training and calibration poisoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9863a105-0ee5-4220-aeec-1daf1b950c8e",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "5c7982ab-d773-4eea-bda8-91b71dd2ac64",
  "toolUseResult": {
    "query": "RPS provably reliable conformal prediction sets data poisoning ICLR 2025 spotlight",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xx8uPfQ7d9KMwjoRhAbBET",
        "content": [
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview",
            "url": "https://openreview.net/forum?id=ofuLWn8DFZ"
          },
          {
            "title": "GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).",
            "url": "https://github.com/yascho/reliable_conformal_prediction"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://iclr.cc/virtual/2025/poster/28340"
          },
          {
            "title": "PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich",
            "url": "https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"
          },
          {
            "title": "Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning",
            "url": "https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"
          },
          {
            "title": "[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://arxiv.org/abs/2410.09878"
          },
          {
            "title": "provably reliable conformal prediction sets",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          }
        ]
      },
      "I found information about the paper you're searching for. Here's what I found:\n\n\"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" is an ICLR 2025 Spotlight paper. The paper is authored by Yan Scholten, Stephan Günnemann, and Leo Schwinn.\n\nThe paper proposes reliable prediction sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. \n\nThe key contributions include:\n- Smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data to ensure reliability under training poisoning\n- Construction of multiple prediction sets, each calibrated on distinct subsets of the calibration data to ensure reliability under calibration poisoning\n\nA reference implementation is available on GitHub with demo notebooks showing how to compute reliable conformal prediction sets under calibration poisoning and under training and calibration poisoning."
    ],
    "durationSeconds": 8.691325789999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9863a105-0ee5-4220-aeec-1daf1b950c8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
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
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "5c7982ab-d773-4eea-bda8-91b71dd2ac64",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool call

_source line 22 · 2026-05-30T06:49:43.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NqBXNZB41sNpjXDRVy7G8L`</summary>

```json
{
  "query": "\"conformal prediction\" \"retrieval augmented\" abstention robustness 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c7982ab-d773-4eea-bda8-91b71dd2ac64",
  "isSidechain": false,
  "requestId": "req_011CbYJpZZixMViDprhqFwm6",
  "type": "assistant",
  "uuid": "c9418508-31d2-43bd-a258-b54a1e7dbb18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EB2XMdFhztTU7LxGwcMkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 23861,
      "output_tokens": 76,
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
          "output_tokens": 76,
          "cache_read_input_tokens": 23861,
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

_source line 23 · 2026-05-30T06:49:50.523Z_

<details><summary>↩ Tool result · `toolu_01NqBXNZB41sNpjXDRVy7G8L`</summary>

```text
Web search results for query: ""conformal prediction" "retrieval augmented" abstention robustness 2025 2026 arxiv"

Links: [{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"Beyond Confidence: Adaptive Abstention in Dual-Threshold Conformal Prediction for Autonomous System Perception","url":"https://arxiv.org/pdf/2502.07255"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/pdf/2503.05239"},{"title":"Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/html/2510.16166v1"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1425&show=500"},{"title":"[2506.14067] Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback","url":"https://arxiv.org/abs/2506.14067"}]

I found several relevant arxiv papers on conformal prediction with retrieval-augmented systems, abstention mechanisms, and robustness. Here are the key results:

## Recent Work (2025-2026)

**Conformal Prediction for RAG Systems:**
A framework called Conformal-RAG uses conformal prediction on large language models with RAG mechanisms to offer statistical guarantees on response quality. It ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets, making it suitable for complex RAG applications.

**Abstention with Conformal Methods:**
A dual-threshold conformal prediction framework achieves adaptive abstention ranging from 13.5% to 63.4% as environmental severity increases, while maintaining high coverage (>90.0%). Conformal abstention mitigates the risk of unreliable responses by ensuring that the system answers only when confident.

**Robustness to Distribution Shifts:**
Conformal prediction provides a powerful framework for constructing prediction intervals with finite-sample guarantees, yet its robustness under distribution shifts remains a significant challenge. The conformal guarantee breaks when test data is noisy or subjected to adversarial perturbations, but robust conformal prediction extends this guarantee to worst-case inputs within a maximum radius.

**Online Learning with Adversarial Feedback:**
ExAUL is a novel online learning framework for conformal abstention with adversarial and partial feedback, demonstrated on question-answering tasks with LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9418508-31d2-43bd-a258-b54a1e7dbb18",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "d4ca409a-b74d-4751-bd01-11c691d4285d",
  "toolUseResult": {
    "query": "\"conformal prediction\" \"retrieval augmented\" abstention robustness 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_015GXii5vp81TjBASXUmPBGH",
        "content": [
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
          },
          {
            "title": "Beyond Confidence: Adaptive Abstention in Dual-Threshold Conformal Prediction for Autonomous System Perception",
            "url": "https://arxiv.org/pdf/2502.07255"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Robust Conformal Prediction with a Single Binary Certificate",
            "url": "https://arxiv.org/pdf/2503.05239"
          },
          {
            "title": "Extending Prediction-Powered Inference through Conformal Prediction",
            "url": "https://arxiv.org/html/2510.16166v1"
          },
          {
            "title": "Artificial Intelligence Jun 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-06?skip=1425&show=500"
          },
          {
            "title": "[2506.14067] Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback",
            "url": "https://arxiv.org/abs/2506.14067"
          }
        ]
      },
      "I found several relevant arxiv papers on conformal prediction with retrieval-augmented systems, abstention mechanisms, and robustness. Here are the key results:\n\n## Recent Work (2025-2026)\n\n**Conformal Prediction for RAG Systems:**\nA framework called Conformal-RAG uses conformal prediction on large language models with RAG mechanisms to offer statistical guarantees on response quality. It ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets, making it suitable for complex RAG applications.\n\n**Abstention with Conformal Methods:**\nA dual-threshold conformal prediction framework achieves adaptive abstention ranging from 13.5% to 63.4% as environmental severity increases, while maintaining high coverage (>90.0%). Conformal abstention mitigates the risk of unreliable responses by ensuring that the system answers only when confident.\n\n**Robustness to Distribution Shifts:**\nConformal prediction provides a powerful framework for constructing prediction intervals with finite-sample guarantees, yet its robustness under distribution shifts remains a significant challenge. The conformal guarantee breaks when test data is noisy or subjected to adversarial perturbations, but robust conformal prediction extends this guarantee to worst-case inputs within a maximum radius.\n\n**Online Learning with Adversarial Feedback:**\nExAUL is a novel online learning framework for conformal abstention with adversarial and partial feedback, demonstrated on question-answering tasks with LLMs."
    ],
    "durationSeconds": 6.914180668000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c9418508-31d2-43bd-a258-b54a1e7dbb18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-30T06:49:53.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LLsUMTMScpQDEEqWipxGU3`</summary>

```json
{
  "query": "RobustRAG certifiably robust retrieval corruption SaTML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4ca409a-b74d-4751-bd01-11c691d4285d",
  "isSidechain": false,
  "requestId": "req_011CbYJqGEDGvcN8H6dzb2qv",
  "type": "assistant",
  "uuid": "533591a7-70e5-4f2c-98dd-312214f91f17",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UsQB61ZfFvvS7Q28k3Mnks",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 24694,
      "output_tokens": 69,
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
          "output_tokens": 69,
          "cache_read_input_tokens": 24694,
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

_source line 25 · 2026-05-30T06:50:00.612Z_

<details><summary>↩ Tool result · `toolu_01LLsUMTMScpQDEEqWipxGU3`</summary>

```text
Web search results for query: "RobustRAG certifiably robust retrieval corruption SaTML 2026"

Links: [{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"Tong Wu - Homepage - Princeton","url":"https://tongwu2020.github.io/tongwu/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"},{"title":"ICML Certifiably Robust RAG against Retrieval Corruption","url":"https://icml.cc/virtual/2024/37487"}]

Based on the search results, I found comprehensive information about RobustRAG:

## Overview

RobustRAG addresses the vulnerability of retrieval-augmented generation (RAG) to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses. RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks.

## Key Approach

The key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then responses are securely aggregated for a robust output. To instantiate RobustRAG, the researchers designed keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.

## Evaluation Results

RobustRAG achieves certifiable robustness by formally certifying non-trivial lower bounds on response quality against adaptive attackers, and has been evaluated on open-domain question-answering and free-form long text generation across three datasets and three LLMs.

## SaTML 2026 Acceptance

The paper was accepted at SaTML 2026 and authored by Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (UC Berkeley), Danqi Chen and Prateek Mittal (Princeton University).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "533591a7-70e5-4f2c-98dd-312214f91f17",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "9392228b-c8be-4ec7-9ce1-5f18957ce09b",
  "toolUseResult": {
    "query": "RobustRAG certifiably robust retrieval corruption SaTML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HqDndDanxF2dbqmNjoySqH",
        "content": [
          {
            "title": "IEEE SaTML 2026 · Accepted Papers",
            "url": "https://satml.org/accepted-papers/"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"
          },
          {
            "title": "[2405.15556] Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/abs/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/html/2405.15556v2"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview",
            "url": "https://openreview.net/forum?id=cU6ZdN87p3"
          },
          {
            "title": "Tong Wu - Homepage - Princeton",
            "url": "https://tongwu2020.github.io/tongwu/"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://openreview.net/pdf?id=qsEeACAJjD"
          },
          {
            "title": "ICML Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://icml.cc/virtual/2024/37487"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about RobustRAG:\n\n## Overview\n\nRobustRAG addresses the vulnerability of retrieval-augmented generation (RAG) to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses. RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks.\n\n## Key Approach\n\nThe key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then responses are securely aggregated for a robust output. To instantiate RobustRAG, the researchers designed keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.\n\n## Evaluation Results\n\nRobustRAG achieves certifiable robustness by formally certifying non-trivial lower bounds on response quality against adaptive attackers, and has been evaluated on open-domain question-answering and free-form long text generation across three datasets and three LLMs.\n\n## SaTML 2026 Acceptance\n\nThe paper was accepted at SaTML 2026 and authored by Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (UC Berkeley), Danqi Chen and Prateek Mittal (Princeton University)."
    ],
    "durationSeconds": 6.866073694999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "533591a7-70e5-4f2c-98dd-312214f91f17",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-30T06:50:03.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KVzWZsA6mZSk75RuVRvoqS`</summary>

```json
{
  "query": "ReliabilityRAG graph theoretic MIS defense certified RAG 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9392228b-c8be-4ec7-9ce1-5f18957ce09b",
  "isSidechain": false,
  "requestId": "req_011CbYJr1L3thFd9AmAKXubf",
  "type": "assistant",
  "uuid": "472b932b-50ed-4e96-ab3e-3dbe14a9599d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5g5z7MCh5cSBffXvkexnq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 25513,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 25513,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 809
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

_source line 27 · 2026-05-30T06:50:09.835Z_

<details><summary>↩ Tool result · `toolu_01KVzWZsA6mZSk75RuVRvoqS`</summary>

```text
Web search results for query: "ReliabilityRAG graph theoretic MIS defense certified RAG 2026"

Links: [{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG- ...","url":"https://www.semanticscholar.org/paper/ReliabilityRAG:-Effective-and-Provably-Robust-for-Shen-Imana/80c7921964f622abe6c023a2df5d5a824f9c66d9"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"}]

Based on the search results, here's what I found:

## ReliabilityRAG Overview

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.

### Key Technical Contributions

The first contribution adopts a graph-theoretic perspective to identify a "consistent majority" among retrieved documents to filter out malicious ones. Recognizing the computational cost of exact MIS (Maximum Independent Set) for large retrieval sets, the second contribution is a scalable weighted sample and aggregate framework that explicitly utilizes reliability information, preserving some robustness guarantees while efficiently handling many documents.

### Robustness Guarantees

ReliabilityRAG via MIS is provably robust since the probability of selecting a malicious document vanishes as the number of retrieved documents grows large, provided the NLI error rates and the number of malicious documents satisfy specified conditions.

### Performance

ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.

The research appears to be recent work from 2025-2026, addressing vulnerabilities in RAG systems to corpus poisoning and adversarial attacks on retrieved documents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "472b932b-50ed-4e96-ab3e-3dbe14a9599d",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "9066b742-b9dc-4c9e-bc36-c6530986ba7c",
  "toolUseResult": {
    "query": "ReliabilityRAG graph theoretic MIS defense certified RAG 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LBfJd6qM58wnCW3SHE8Kyk",
        "content": [
          {
            "title": "[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/abs/2509.23519"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview",
            "url": "https://openreview.net/forum?id=D9JeNTs5Bu"
          },
          {
            "title": "Certified Defenses for RAG Systems",
            "url": "https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/media/neurips-2025/Slides/119236.pdf"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG- ...",
            "url": "https://www.semanticscholar.org/paper/ReliabilityRAG:-Effective-and-Provably-Robust-for-Shen-Imana/80c7921964f622abe6c023a2df5d5a824f9c66d9"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## ReliabilityRAG Overview\n\nReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.\n\n### Key Technical Contributions\n\nThe first contribution adopts a graph-theoretic perspective to identify a \"consistent majority\" among retrieved documents to filter out malicious ones. Recognizing the computational cost of exact MIS (Maximum Independent Set) for large retrieval sets, the second contribution is a scalable weighted sample and aggregate framework that explicitly utilizes reliability information, preserving some robustness guarantees while efficiently handling many documents.\n\n### Robustness Guarantees\n\nReliabilityRAG via MIS is provably robust since the probability of selecting a malicious document vanishes as the number of retrieved documents grows large, provided the NLI error rates and the number of malicious documents satisfy specified conditions.\n\n### Performance\n\nReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.\n\nThe research appears to be recent work from 2025-2026, addressing vulnerabilities in RAG systems to corpus poisoning and adversarial attacks on retrieved documents."
    ],
    "durationSeconds": 6.718195034000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "472b932b-50ed-4e96-ab3e-3dbe14a9599d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T06:50:12.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R4zFM5eNggmJBSKavF8U6W`</summary>

```json
{
  "query": "\"conformal factuality\" RAG robust distribution shift Chen 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9066b742-b9dc-4c9e-bc36-c6530986ba7c",
  "isSidechain": false,
  "requestId": "req_011CbYJrgo6qRHWVEdAwoFHc",
  "type": "assistant",
  "uuid": "0051e0cf-c273-4a23-8422-bab41c9f40a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UuE3PQqDjfmcNusUm1zAfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 26322,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 813,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 26322,
          "cache_creation_input_tokens": 813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 813
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

_source line 29 · 2026-05-30T06:50:20.317Z_

<details><summary>↩ Tool result · `toolu_01R4zFM5eNggmJBSKavF8U6W`</summary>

```text
Web search results for query: ""conformal factuality" RAG robust distribution shift Chen 2026 arxiv"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Proceedings of Machine Learning Research vol vvv:1–25, 2026","url":"https://arxiv.org/pdf/2602.12616"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"Not all distributional shifts are equal: Fine-grained robust conformal inference","url":"https://arxiv.org/pdf/2402.13042"},{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"Robust Conformal Prediction under Distribution Shift via Physics-Informed Structural Causal Model","url":"https://arxiv.org/html/2403.15025v1"}]

I found the paper you're looking for! 

The arxiv paper is titled "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" by Yi Chen and colleagues, published March 17, 2026.

The paper finds that conformal factuality guarantees are not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions. The research also shows that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and that lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

The results expose factuality-informativeness trade-offs and fragility of the conformal filtering framework under distribution shifts and distractors.

You can access the paper at: https://arxiv.org/abs/2603.16817


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0051e0cf-c273-4a23-8422-bab41c9f40a6",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "0e5ce4fd-f0e6-401e-a109-d19e6c8aaf1f",
  "toolUseResult": {
    "query": "\"conformal factuality\" RAG robust distribution shift Chen 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YYhUf1ZySdp6MtDaddecNF",
        "content": [
          {
            "title": "[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/abs/2603.16817"
          },
          {
            "title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/pdf/2603.16817"
          },
          {
            "title": "Proceedings of Machine Learning Research vol vvv:1–25, 2026",
            "url": "https://arxiv.org/pdf/2602.12616"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
          },
          {
            "title": "Not all distributional shifts are equal: Fine-grained robust conformal inference",
            "url": "https://arxiv.org/pdf/2402.13042"
          },
          {
            "title": "[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978v1"
          },
          {
            "title": "Robust Conformal Prediction under Distribution Shift via Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/html/2403.15025v1"
          }
        ]
      },
      "I found the paper you're looking for! \n\nThe arxiv paper is titled \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\" by Yi Chen and colleagues, published March 17, 2026.\n\nThe paper finds that conformal factuality guarantees are not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions. The research also shows that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and that lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.\n\nThe results expose factuality-informativeness trade-offs and fragility of the conformal filtering framework under distribution shifts and distractors.\n\nYou can access the paper at: https://arxiv.org/abs/2603.16817"
    ],
    "durationSeconds": 7.980817285000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0051e0cf-c273-4a23-8422-bab41c9f40a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-30T06:50:20.320Z_

```json
{
  "parentUuid": "0e5ce4fd-f0e6-401e-a109-d19e6c8aaf1f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bad861d4-05a0-4f7e-84a3-397462295d77",
  "timestamp": "2026-05-30T06:50:20.320Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-30T06:50:23.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HXwYFAwEfVyA662bDEqDsF`</summary>

```json
{
  "query": "CorruptRAG single document poisoning attack RAG 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bad861d4-05a0-4f7e-84a3-397462295d77",
  "isSidechain": false,
  "requestId": "req_011CbYJsTae4M2tzcLqvBYgZ",
  "type": "assistant",
  "uuid": "410b0bac-7f74-4f06-9e53-8081a4b54563",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jmag7QcGKr4vo5KHLDmSo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 27135,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 27135,
          "cache_creation_input_tokens": 812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 812
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

_source line 32 · 2026-05-30T06:50:30.777Z_

<details><summary>↩ Tool result · `toolu_01HXwYFAwEfVyA662bDEqDsF`</summary>

```text
Web search results for query: "CorruptRAG single document poisoning attack RAG 2026"

Links: [{"title":"Vector Collision Attacks: Hijacking RAG | InstaTunnel Blog","url":"https://instatunnel.my/blog/vector-collision-attacks-hijacking-the-nearest-neighbor"},{"title":"RAG Poisoning Turns Your Knowledge Base Into an Attack Surface","url":"https://www.toxsec.com/p/when-your-notepad-app-gets-a-cve-4fc?action=share"},{"title":"RAG Security: How Attackers Poison Your Knowledge Base | BeyondScale","url":"https://beyondscale.tech/blog/rag-security-data-poisoning-guide"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"},{"title":"RAG Poisoning: How Attackers Corrupt Your AI's Knowledge Base | Amine Raji, PhD","url":"https://aminrj.com/posts/rag-document-poisoning/"},{"title":"RAG Poisoning: Contaminating the AI's \"Source of Truth\"","url":"https://instatunnel.substack.com/p/rag-poisoning-contaminating-the-ais"},{"title":"RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium","url":"https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"},{"title":"RAG Poisoning: How Attackers Corrupt AI Knowledge Bases | InstaTunnel Blog","url":"https://instatunnel.my/blog/rag-poisoning-contaminating-the-ais-source-of-truth-"},{"title":"Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning","url":"https://arxiv.org/html/2605.05632"}]

Based on the search results, here's what I found about CorruptRAG and single document poisoning attacks on RAG systems:

## CorruptRAG Overview

CorruptRAG is a practical poisoning attack introduced in early 2026 that requires only a single poisoned text injection. Published in January 2026, CorruptRAG reduces the attack to a single poisoned document, making it more realistic for environments where bulk injection would trigger anomaly detection.

## Key Advantages Over Previous Attacks

CorruptRAG proved that one document, crafted to be semantically relevant to a target query, achieves higher success rates than multi-document approaches. CorruptRAG achieves comparable success rates to PoisonedRAG while requiring fewer injections, making it harder to detect through volume-based monitoring.

## How It Works

CorruptRAG is a practical poisoning attack against RAG systems in which the attacker injects only a single poisoned text, enhancing both feasibility and stealth. A practical attack pattern requires no sophisticated optimization: an attacker briefly edits a Wikipedia article, public documentation page, or GitHub README with poisoned content; if the RAG system's ingestion pipeline scrapes that source during a scheduled update, the poisoned version enters the vector database.

## Research Context

Most existing attacks assume the attacker can insert a sufficient number of poisoned texts per query, an assumption that is often unrealistic, which is why CorruptRAG was developed to address this limitation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "410b0bac-7f74-4f06-9e53-8081a4b54563",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "05fcad2c-2066-4dd5-99f2-e323f4b79707",
  "toolUseResult": {
    "query": "CorruptRAG single document poisoning attack RAG 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KJSEShNxyHuy39vxUfyBQm",
        "content": [
          {
            "title": "Vector Collision Attacks: Hijacking RAG | InstaTunnel Blog",
            "url": "https://instatunnel.my/blog/vector-collision-attacks-hijacking-the-nearest-neighbor"
          },
          {
            "title": "RAG Poisoning Turns Your Knowledge Base Into an Attack Surface",
            "url": "https://www.toxsec.com/p/when-your-notepad-app-gets-a-cve-4fc?action=share"
          },
          {
            "title": "RAG Security: How Attackers Poison Your Knowledge Base | BeyondScale",
            "url": "https://beyondscale.tech/blog/rag-security-data-poisoning-guide"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2504.03957v2"
          },
          {
            "title": "RAG Poisoning: How Attackers Corrupt Your AI's Knowledge Base | Amine Raji, PhD",
            "url": "https://aminrj.com/posts/rag-document-poisoning/"
          },
          {
            "title": "RAG Poisoning: Contaminating the AI's \"Source of Truth\"",
            "url": "https://instatunnel.substack.com/p/rag-poisoning-contaminating-the-ais"
          },
          {
            "title": "RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium",
            "url": "https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"
          },
          {
            "title": "RAG Poisoning: How Attackers Corrupt AI Knowledge Bases | InstaTunnel Blog",
            "url": "https://instatunnel.my/blog/rag-poisoning-contaminating-the-ais-source-of-truth-"
          },
          {
            "title": "Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning",
            "url": "https://arxiv.org/html/2605.05632"
          }
        ]
      },
      "Based on the search results, here's what I found about CorruptRAG and single document poisoning attacks on RAG systems:\n\n## CorruptRAG Overview\n\nCorruptRAG is a practical poisoning attack introduced in early 2026 that requires only a single poisoned text injection. Published in January 2026, CorruptRAG reduces the attack to a single poisoned document, making it more realistic for environments where bulk injection would trigger anomaly detection.\n\n## Key Advantages Over Previous Attacks\n\nCorruptRAG proved that one document, crafted to be semantically relevant to a target query, achieves higher success rates than multi-document approaches. CorruptRAG achieves comparable success rates to PoisonedRAG while requiring fewer injections, making it harder to detect through volume-based monitoring.\n\n## How It Works\n\nCorruptRAG is a practical poisoning attack against RAG systems in which the attacker injects only a single poisoned text, enhancing both feasibility and stealth. A practical attack pattern requires no sophisticated optimization: an attacker briefly edits a Wikipedia article, public documentation page, or GitHub README with poisoned content; if the RAG system's ingestion pipeline scrapes that source during a scheduled update, the poisoned version enters the vector database.\n\n## Research Context\n\nMost existing attacks assume the attacker can insert a sufficient number of poisoned texts per query, an assumption that is often unrealistic, which is why CorruptRAG was developed to address this limitation."
    ],
    "durationSeconds": 7.6057659330000025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "410b0bac-7f74-4f06-9e53-8081a4b54563",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
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
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "05fcad2c-2066-4dd5-99f2-e323f4b79707",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool call

_source line 35 · 2026-05-30T06:50:33.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PkPbem83C1NRrCxemofvuc`</summary>

```json
{
  "query": "AAAI 2026 submission deadline safe robust responsible AI track"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05fcad2c-2066-4dd5-99f2-e323f4b79707",
  "isSidechain": false,
  "requestId": "req_011CbYJtELh21GNKuB6jdMZG",
  "type": "assistant",
  "uuid": "2a50006e-ac43-46dc-9950-25dd52be7fe6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7yNgQ3wX7ZNG3xmpchWRB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 914,
      "cache_read_input_tokens": 27947,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 27947,
          "cache_creation_input_tokens": 914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 914
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

_source line 36 · 2026-05-30T06:50:39.642Z_

<details><summary>↩ Tool result · `toolu_01PkPbem83C1NRrCxemofvuc`</summary>

```text
Web search results for query: "AAAI 2026 submission deadline safe robust responsible AI track"

Links: [{"title":"Main Technical Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"},{"title":"AAAI-26 Call for the Special Track on AI Alignment","url":"https://aaai.org/conference/aaai/aaai-26/aia-call/"},{"title":"AAAI-26 Workshop Program - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/workshops-program/"},{"title":"Call for Submissions: Emerging Trends in AI (ETA) Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/eta-call/"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"AAAI-26 Journal Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/journal-track-call/"},{"title":"Call for the Special Track on Safe, Robust and Responsible AI - AAAI","url":"https://aaai.org/aaai-24-conference/call-for-the-special-track-on-safe-and-robust-ai/"},{"title":"AAAI-24 Call for Proposals - AAAI","url":"https://aaai.org/aaai-24-conference/aaai-24-call-for-proposals/"},{"title":"Call for Papers – Aies Conference","url":"https://www.aies-conference.com/2026/call-for-papers/"}]

Based on the search results, I found information about AAAI-26 special tracks, but I don't see a specific "Safe Robust Responsible AI" track for AAAI-26. However, there is relevant information about AAAI-26 special tracks:

AAAI-26 has special tracks including an AI Alignment (AIA) track, with submissions following the regular AAAI technical paper submission procedure. The AI Alignment track addresses problems central to developing safe and secure AI systems aligned with human values, including robustness and security concerns.

Note that AAAI-24 featured a special track on Safe, Robust and Responsible Artificial Intelligence (SRRAI), but this track does not appear to have continued under that specific name for AAAI-26.

Deadlines are track-specific and may differ, with track-specific deadlines listed on their respective CFPs. For specific submission deadlines for AAAI-26 tracks, you would need to check the individual call for papers for each track on the AAAI website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a50006e-ac43-46dc-9950-25dd52be7fe6",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "272cf55e-0841-4aad-addd-bc8329f75870",
  "toolUseResult": {
    "query": "AAAI 2026 submission deadline safe robust responsible AI track",
    "results": [
      {
        "tool_use_id": "srvtoolu_015KgZwwowe4AxpbLTcRnKyx",
        "content": [
          {
            "title": "Main Technical Track: Call for Papers - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"
          },
          {
            "title": "AAAI-26 Call for the Special Track on AI Alignment",
            "url": "https://aaai.org/conference/aaai/aaai-26/aia-call/"
          },
          {
            "title": "AAAI-26 Workshop Program - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/workshops-program/"
          },
          {
            "title": "Call for Submissions: Emerging Trends in AI (ETA) Track - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/eta-call/"
          },
          {
            "title": "AAAI-26 Submission Instructions - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/submission-instructions/"
          },
          {
            "title": "40th Annual AAAI Conference on Artificial Intelligence",
            "url": "https://aaai.org/conference/aaai/aaai-26/"
          },
          {
            "title": "AAAI-26 Journal Track: Call for Papers - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/journal-track-call/"
          },
          {
            "title": "Call for the Special Track on Safe, Robust and Responsible AI - AAAI",
            "url": "https://aaai.org/aaai-24-conference/call-for-the-special-track-on-safe-and-robust-ai/"
          },
          {
            "title": "AAAI-24 Call for Proposals - AAAI",
            "url": "https://aaai.org/aaai-24-conference/aaai-24-call-for-proposals/"
          },
          {
            "title": "Call for Papers – Aies Conference",
            "url": "https://www.aies-conference.com/2026/call-for-papers/"
          }
        ]
      },
      "Based on the search results, I found information about AAAI-26 special tracks, but I don't see a specific \"Safe Robust Responsible AI\" track for AAAI-26. However, there is relevant information about AAAI-26 special tracks:\n\nAAAI-26 has special tracks including an AI Alignment (AIA) track, with submissions following the regular AAAI technical paper submission procedure. The AI Alignment track addresses problems central to developing safe and secure AI systems aligned with human values, including robustness and security concerns.\n\nNote that AAAI-24 featured a special track on Safe, Robust and Responsible Artificial Intelligence (SRRAI), but this track does not appear to have continued under that specific name for AAAI-26.\n\nDeadlines are track-specific and may differ, with track-specific deadlines listed on their respective CFPs. For specific submission deadlines for AAAI-26 tracks, you would need to check the individual call for papers for each track on the AAAI website."
    ],
    "durationSeconds": 6.249359949000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2a50006e-ac43-46dc-9950-25dd52be7fe6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-30T06:50:41.781Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013DSwRMkT4GcLvcr5U3dhJv`</summary>

```json
{
  "query": "AAAI 2026 paper submission deadline August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "272cf55e-0841-4aad-addd-bc8329f75870",
  "isSidechain": false,
  "requestId": "req_011CbYJttDFirJ25J7vQsoYZ",
  "type": "assistant",
  "uuid": "895e4fcd-dda8-438c-8ef9-68f637145621",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RA5C5W1RDxhhxoXRJxDTDW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 28861,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 28861,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 38 · 2026-05-30T06:50:46.239Z_

<details><summary>↩ Tool result · `toolu_013DSwRMkT4GcLvcr5U3dhJv`</summary>

```text
Web search results for query: "AAAI 2026 paper submission deadline August 2026"

Links: [{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"Main Technical Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"},{"title":"40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"AAAI-26 Review Process - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/review-process/"},{"title":"ICWSM 2026: Submit","url":"https://www.icwsm.org/2026/submit.html"},{"title":"AAAI-26 Paper Modification Guidelines - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/paper-modification-guidelines/"},{"title":"AAAI 2026","url":"http://aideadlines.org/conference/?id=aaai26"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI-26 Journal Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/journal-track-call/"},{"title":"AAAI-26 Paper Publication and Conference Attendance - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/paper-publication-and-conference-attendance/"}]

Based on the search results, I found information about AAAI-26 paper submission deadlines. However, I should clarify that the deadlines in your query appear to reference August 2026, but the actual AAAI-26 submission deadlines have already passed (they were in 2025).

For regular papers at AAAI-26, abstracts must be submitted by July 25, 2025 and full papers must be submitted by August 1, 2025. All deadlines are "anywhere on earth" (UTC-12).

Additionally, supplementary material and code were due by August 4, 2025.

It's important to note that deadlines are track-specific and may differ from those listed above, with track-specific deadlines listed on their respective CFP.

The AAAI-26 conference itself is scheduled for January 20-27, 2026, in Singapore.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "895e4fcd-dda8-438c-8ef9-68f637145621",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "5168d678-0f25-49a6-9ad7-b17d67dd1695",
  "toolUseResult": {
    "query": "AAAI 2026 paper submission deadline August 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LFsd266uFzXx7TW41Rqay7",
        "content": [
          {
            "title": "AAAI-26 Submission Instructions - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/submission-instructions/"
          },
          {
            "title": "Main Technical Track: Call for Papers - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"
          },
          {
            "title": "40th Annual AAAI Conference on Artificial Intelligence",
            "url": "https://aaai.org/conference/aaai/aaai-26/"
          },
          {
            "title": "AAAI-26 Review Process - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/review-process/"
          },
          {
            "title": "ICWSM 2026: Submit",
            "url": "https://www.icwsm.org/2026/submit.html"
          },
          {
            "title": "AAAI-26 Paper Modification Guidelines - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/paper-modification-guidelines/"
          },
          {
            "title": "AAAI 2026",
            "url": "http://aideadlines.org/conference/?id=aaai26"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AAAI-26 Journal Track: Call for Papers - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/journal-track-call/"
          },
          {
            "title": "AAAI-26 Paper Publication and Conference Attendance - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/paper-publication-and-conference-attendance/"
          }
        ]
      },
      "Based on the search results, I found information about AAAI-26 paper submission deadlines. However, I should clarify that the deadlines in your query appear to reference August 2026, but the actual AAAI-26 submission deadlines have already passed (they were in 2025).\n\nFor regular papers at AAAI-26, abstracts must be submitted by July 25, 2025 and full papers must be submitted by August 1, 2025. All deadlines are \"anywhere on earth\" (UTC-12).\n\nAdditionally, supplementary material and code were due by August 4, 2025.\n\nIt's important to note that deadlines are track-specific and may differ from those listed above, with track-specific deadlines listed on their respective CFP.\n\nThe AAAI-26 conference itself is scheduled for January 20-27, 2026, in Singapore."
    ],
    "durationSeconds": 4.454295081999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "895e4fcd-dda8-438c-8ef9-68f637145621",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-30T06:50:56.394Z_

<details><summary>Logged reasoning block</summary>

```text
The AAAI 2026 deadline has already passed (August 2025). Let me check if the user is referring to AAAI 2027 perhaps, or if there's a different submission timeline. Let me verify what venues might be appropriate.

Actually, let me re-read the user's seed topic. They say "AAAI 2026 submission deadline: August 2026". But the search results show AAAI-26 has its deadline in August 2025, and the conference is in January 2026. So "AAAI 2026" with an August 2026 deadline would be AAAI 2027 (the 41st AAAI, happening in early 2027). Let me search for this.


I notice the user's deadline doesn't quite match the actual AAAI schedule, but I'll set that aside and focus on developing the research direction itself. Now I need to do some targeted searches to identify any existing work in this space and validate whether there's a genuine gap to address.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5168d678-0f25-49a6-9ad7-b17d67dd1695",
  "isSidechain": false,
  "requestId": "req_011CbYJuNQeMXg3uH5ej3LQk",
  "type": "assistant",
  "uuid": "26f22c48-a340-4897-a23f-946bdf26d602",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMzkVeMi4YZqojWQScvDgQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 29702,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 29702,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
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

_source line 40 · 2026-05-30T06:50:56.396Z_

Now let me do deeper dives into the specific gap and check for concurrent work:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26f22c48-a340-4897-a23f-946bdf26d602",
  "isSidechain": false,
  "requestId": "req_011CbYJuNQeMXg3uH5ej3LQk",
  "type": "assistant",
  "uuid": "b1a95bc3-c146-4e29-8d66-ca52f981175d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMzkVeMi4YZqojWQScvDgQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 29702,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 29702,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
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

_source line 41 · 2026-05-30T06:50:56.515Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SgQYEgcxm2SMMcGUihADNy`</summary>

```json
{
  "query": "\"conformal prediction\" \"corpus poisoning\" OR \"retrieval poisoning\" abstention certificate 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1a95bc3-c146-4e29-8d66-ca52f981175d",
  "isSidechain": false,
  "requestId": "req_011CbYJuNQeMXg3uH5ej3LQk",
  "type": "assistant",
  "uuid": "48e0c564-02b7-49ce-94f9-fa28d5662ab1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMzkVeMi4YZqojWQScvDgQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 29702,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 29702,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
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

_source line 42 · 2026-05-30T06:51:06.729Z_

<details><summary>↩ Tool result · `toolu_01SgQYEgcxm2SMMcGUihADNy`</summary>

```text
Web search results for query: ""conformal prediction" "corpus poisoning" OR "retrieval poisoning" abstention certificate 2025 2026"

Links: [{"title":"ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://iclr.cc/virtual/2025/poster/28340"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730110"},{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"},{"title":"arXiv:2505.19864v1 [cs.CR] 26 May 2025 CPA-RAG:Covert Poisoning Attacks on","url":"https://arxiv.org/pdf/2505.19864"},{"title":"Conformal Prediction Conference 2026","url":"https://copa-conference.com/"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"}]

Based on the search results, here's what I found related to your query:

## Conformal Prediction and Data Poisoning

Conformal prediction provides model-agnostic and distribution-free uncertainty quantification through prediction sets guaranteed to include the ground truth with any user-specified probability, but it is not reliable under poisoning attacks where adversaries manipulate both training and calibration data.

Reliable prediction sets (RPS) is the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. This research was presented at ICLR 2025 (May 4, 2025).

## Corpus/Retrieval Poisoning Attacks

Recent research from 2025-2026 shows significant work on corpus poisoning attacks in retrieval systems. Work on reproducing HotFlip for corpus poisoning attacks in dense retrieval was presented at ECIR 2025 (April 6-10, 2025). Additionally, CPA-RAG achieves 92% attack success rate on NQ and 85% covert attack success rate, outperforming other poisoning methods.

## Abstention and Certificates

Researchers use conformal risk control to obtain upper bounds on hallucination risk, developing abstention procedures. Regarding robustness certificates, certificates provide worst-case guarantees that predictions do not change, and researchers are exploring how to extend robustness certificates to conformal prediction sets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48e0c564-02b7-49ce-94f9-fa28d5662ab1",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "ad22012d-a46f-48b5-a6c2-2aa2bca813e1",
  "toolUseResult": {
    "query": "\"conformal prediction\" \"corpus poisoning\" OR \"retrieval poisoning\" abstention certificate 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KrWfyoUEzpgEwL5YezM2bN",
        "content": [
          {
            "title": "ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://iclr.cc/virtual/2025/poster/28340"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/10.1145/3726302.3730110"
          },
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"
          },
          {
            "title": "arXiv:2505.19864v1 [cs.CR] 26 May 2025 CPA-RAG:Covert Poisoning Attacks on",
            "url": "https://arxiv.org/pdf/2505.19864"
          },
          {
            "title": "Conformal Prediction Conference 2026",
            "url": "https://copa-conference.com/"
          },
          {
            "title": "Robust Yet Efficient Conformal Prediction Sets",
            "url": "https://arxiv.org/pdf/2407.09165"
          }
        ]
      },
      "Based on the search results, here's what I found related to your query:\n\n## Conformal Prediction and Data Poisoning\n\nConformal prediction provides model-agnostic and distribution-free uncertainty quantification through prediction sets guaranteed to include the ground truth with any user-specified probability, but it is not reliable under poisoning attacks where adversaries manipulate both training and calibration data.\n\nReliable prediction sets (RPS) is the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. This research was presented at ICLR 2025 (May 4, 2025).\n\n## Corpus/Retrieval Poisoning Attacks\n\nRecent research from 2025-2026 shows significant work on corpus poisoning attacks in retrieval systems. Work on reproducing HotFlip for corpus poisoning attacks in dense retrieval was presented at ECIR 2025 (April 6-10, 2025). Additionally, CPA-RAG achieves 92% attack success rate on NQ and 85% covert attack success rate, outperforming other poisoning methods.\n\n## Abstention and Certificates\n\nResearchers use conformal risk control to obtain upper bounds on hallucination risk, developing abstention procedures. Regarding robustness certificates, certificates provide worst-case guarantees that predictions do not change, and researchers are exploring how to extend robustness certificates to conformal prediction sets."
    ],
    "durationSeconds": 10.210215740999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "48e0c564-02b7-49ce-94f9-fa28d5662ab1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-30T06:51:09.083Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DAsy4hKYQMVXRBSqsEVHTi`</summary>

```json
{
  "query": "conformal prediction RAG abstention adversarial robustness framework 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad22012d-a46f-48b5-a6c2-2aa2bca813e1",
  "isSidechain": false,
  "requestId": "req_011CbYJvt3e22B3CQQG9WooR",
  "type": "assistant",
  "uuid": "8dfed37a-eee3-4701-a501-963292d2ea3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4CXbAWXuN3H1HH3DjB2hZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 30462,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 30462,
          "cache_creation_input_tokens": 1201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1201
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

_source line 44 · 2026-05-30T06:51:16.628Z_

<details><summary>↩ Tool result · `toolu_01DAsy4hKYQMVXRBSqsEVHTi`</summary>

```text
Web search results for query: "conformal prediction RAG abstention adversarial robustness framework 2026 arxiv"

Links: [{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/pdf/2506.07804"},{"title":"[2506.07804] Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/abs/2506.07804"},{"title":"Game-Theoretic Defenses for Robust Conformal Prediction Against   Adversarial Attacks in Medical Imaging","url":"https://arxiv.org/pdf/2411.04376"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"Beyond Confidence: Adaptive Abstention in Dual-Threshold Conformal Prediction for Autonomous System Perception","url":"https://arxiv.org/pdf/2502.07255"},{"title":"[2510.00463] On the Adversarial Robustness of Learning-based Conformal Novelty Detection","url":"https://arxiv.org/abs/2510.00463"}]

I found several relevant results related to conformal prediction and adversarial robustness frameworks. Here are the key papers from 2026 and recent arxiv submissions:

## Main Results

**"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability"** (arXiv 2506.07804)

This paper develops an adversarial attack method called OPSA (OPtimal Size Attack) designed to reduce the efficiency of conformal prediction at any significance level by maximizing model uncertainty, and introduces OPSA-AT (Adversarial Training), a defense strategy that integrates OPSA within a novel conformal training paradigm. Experimental evaluations demonstrate that the OPSA attack method induces greater uncertainty compared to baseline approaches for various defenses.

**"Beyond Confidence: Adaptive Abstention in Dual-Threshold Conformal Prediction for Autonomous System Perception"** (arXiv 2502.07255)

This framework achieves robust uncertainty quantification and effective abstention decisions, demonstrating high detection performance (AUC >0.960) on complex natural scenes while maintaining robust uncertainty quantification with coverage consistently above 90.0%.

**"On the Adversarial Robustness of Learning-based Conformal Novelty Detection"** (arXiv 2510.00463, updated February 2026)

This paper studies the adversarial robustness of conformal novelty detection, focusing on two powerful learning-based frameworks with finite-sample false discovery rate (FDR) control.

These papers collectively address the intersection of conformal prediction, adversarial robustness, and uncertainty quantification in critical applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dfed37a-eee3-4701-a501-963292d2ea3a",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "d9287b41-e941-4304-a729-23344d561ebb",
  "toolUseResult": {
    "query": "conformal prediction RAG abstention adversarial robustness framework 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_013YqLBer8jsyMiKfWWimL64",
        "content": [
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/pdf/2506.07804"
          },
          {
            "title": "[2506.07804] Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/abs/2506.07804"
          },
          {
            "title": "Game-Theoretic Defenses for Robust Conformal Prediction Against   Adversarial Attacks in Medical Imaging",
            "url": "https://arxiv.org/pdf/2411.04376"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/html/2506.07804v1"
          },
          {
            "title": "Beyond Confidence: Adaptive Abstention in Dual-Threshold Conformal Prediction for Autonomous System Perception",
            "url": "https://arxiv.org/pdf/2502.07255"
          },
          {
            "title": "[2510.00463] On the Adversarial Robustness of Learning-based Conformal Novelty Detection",
            "url": "https://arxiv.org/abs/2510.00463"
          }
        ]
      },
      "I found several relevant results related to conformal prediction and adversarial robustness frameworks. Here are the key papers from 2026 and recent arxiv submissions:\n\n## Main Results\n\n**\"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability\"** (arXiv 2506.07804)\n\nThis paper develops an adversarial attack method called OPSA (OPtimal Size Attack) designed to reduce the efficiency of conformal prediction at any significance level by maximizing model uncertainty, and introduces OPSA-AT (Adversarial Training), a defense strategy that integrates OPSA within a novel conformal training paradigm. Experimental evaluations demonstrate that the OPSA attack method induces greater uncertainty compared to baseline approaches for various defenses.\n\n**\"Beyond Confidence: Adaptive Abstention in Dual-Threshold Conformal Prediction for Autonomous System Perception\"** (arXiv 2502.07255)\n\nThis framework achieves robust uncertainty quantification and effective abstention decisions, demonstrating high detection performance (AUC >0.960) on complex natural scenes while maintaining robust uncertainty quantification with coverage consistently above 90.0%.\n\n**\"On the Adversarial Robustness of Learning-based Conformal Novelty Detection\"** (arXiv 2510.00463, updated February 2026)\n\nThis paper studies the adversarial robustness of conformal novelty detection, focusing on two powerful learning-based frameworks with finite-sample false discovery rate (FDR) control.\n\nThese papers collectively address the intersection of conformal prediction, adversarial robustness, and uncertainty quantification in critical applications."
    ],
    "durationSeconds": 7.540061833999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8dfed37a-eee3-4701-a501-963292d2ea3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "d9287b41-e941-4304-a729-23344d561ebb",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool call

_source line 47 · 2026-05-30T06:51:18.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TRPdRsZU9sxWmeMzRnc6G8`</summary>

```json
{
  "query": "SCoRE selective conformal risk e-values 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9287b41-e941-4304-a729-23344d561ebb",
  "isSidechain": false,
  "requestId": "req_011CbYJwcNatCeMCnZxtxdGb",
  "type": "assistant",
  "uuid": "6b4ad0b3-df42-4cb7-b02e-6633442cda27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hdk83Bc1pcm3D8kePboHU7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 31663,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 31663,
          "cache_creation_input_tokens": 812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 812
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

_source line 48 · 2026-05-30T06:51:25.779Z_

<details><summary>↩ Tool result · `toolu_01TRPdRsZU9sxWmeMzRnc6G8`</summary>

```text
Web search results for query: "SCoRE selective conformal risk e-values 2026"

Links: [{"title":"[2603.24704] Conformal Selective Prediction with General Risk Control","url":"https://arxiv.org/abs/2603.24704"},{"title":"Conformal Selective Prediction with General Risk Control","url":"https://arxiv.org/pdf/2603.24704"},{"title":"Statistics Seminar - Ying Jin (Wharton) \"Conformal Selective ...","url":"https://calendars.illinois.edu/detail/7604?eventId=33545051"},{"title":"[2512.12844] Selective Conformal Risk Control","url":"https://arxiv.org/abs/2512.12844"},{"title":"Selective Conformal Risk Control","url":"https://arxiv.org/html/2512.12844v1"},{"title":"[2605.20270] Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs","url":"https://arxiv.org/abs/2605.20270"},{"title":"(PDF) Selective Conformal Risk Control","url":"https://www.researchgate.net/publication/398721023_Selective_Conformal_Risk_Control"}]

Based on the search results, I found relevant information about SCoRE (Selective Conformal Risk control with E-values):

SCoRE is a new framework for deriving decisions for any trained model and any user-defined, bounded and continuously-valued risk. In deploying AI models, selective prediction offers the option to abstain from making a prediction when uncertain about model quality, and it is crucial to enforce strict and precise error control over cases where the model is trusted.

**Technical approach:** SCoRE is built upon conformal inference and hypothesis testing ideas, constructing a class of (generalized) e-values—non-negative random variables whose product with the unknown risk has expectation no greater than one—a property ensured by data exchangeability without requiring any modeling assumptions. These e-values are passed on to hypothesis testing procedures to yield binary trust decisions with finite-sample error control.

**Advantages:** SCoRE avoids the need of uniform concentration and can be readily extended to settings with distribution shifts.

**Applications:** The proposed methods have been evaluated with simulations and demonstrated through applications to error management in drug discovery, health risk prediction, and large language models.

The paper on SCoRE was published in March 2026 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b4ad0b3-df42-4cb7-b02e-6633442cda27",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "abe15ecd-7900-4420-b607-78ca370653e5",
  "toolUseResult": {
    "query": "SCoRE selective conformal risk e-values 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UZeSjHMx4djZjbgTDgK8R1",
        "content": [
          {
            "title": "[2603.24704] Conformal Selective Prediction with General Risk Control",
            "url": "https://arxiv.org/abs/2603.24704"
          },
          {
            "title": "Conformal Selective Prediction with General Risk Control",
            "url": "https://arxiv.org/pdf/2603.24704"
          },
          {
            "title": "Statistics Seminar - Ying Jin (Wharton) \"Conformal Selective ...",
            "url": "https://calendars.illinois.edu/detail/7604?eventId=33545051"
          },
          {
            "title": "[2512.12844] Selective Conformal Risk Control",
            "url": "https://arxiv.org/abs/2512.12844"
          },
          {
            "title": "Selective Conformal Risk Control",
            "url": "https://arxiv.org/html/2512.12844v1"
          },
          {
            "title": "[2605.20270] Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs",
            "url": "https://arxiv.org/abs/2605.20270"
          },
          {
            "title": "(PDF) Selective Conformal Risk Control",
            "url": "https://www.researchgate.net/publication/398721023_Selective_Conformal_Risk_Control"
          }
        ]
      },
      "Based on the search results, I found relevant information about SCoRE (Selective Conformal Risk control with E-values):\n\nSCoRE is a new framework for deriving decisions for any trained model and any user-defined, bounded and continuously-valued risk. In deploying AI models, selective prediction offers the option to abstain from making a prediction when uncertain about model quality, and it is crucial to enforce strict and precise error control over cases where the model is trusted.\n\n**Technical approach:** SCoRE is built upon conformal inference and hypothesis testing ideas, constructing a class of (generalized) e-values—non-negative random variables whose product with the unknown risk has expectation no greater than one—a property ensured by data exchangeability without requiring any modeling assumptions. These e-values are passed on to hypothesis testing procedures to yield binary trust decisions with finite-sample error control.\n\n**Advantages:** SCoRE avoids the need of uniform concentration and can be readily extended to settings with distribution shifts.\n\n**Applications:** The proposed methods have been evaluated with simulations and demonstrated through applications to error management in drug discovery, health risk prediction, and large language models.\n\nThe paper on SCoRE was published in March 2026 on arXiv."
    ],
    "durationSeconds": 6.881389121000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6b4ad0b3-df42-4cb7-b02e-6633442cda27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-30T06:51:28.324Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Aptyp6os7LDasnfXzK2Ny`</summary>

```json
{
  "query": "\"conformal risk control\" monotone loss RAG LLM abstention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abe15ecd-7900-4420-b607-78ca370653e5",
  "isSidechain": false,
  "requestId": "req_011CbYJxHSqDwvDYQ8FN4BQs",
  "type": "assistant",
  "uuid": "cc896e53-c0c8-400f-b8e0-177b0630c722",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JttL9TatQPv5vTYcAViw6x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 32475,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 32475,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 50 · 2026-05-30T06:51:35.196Z_

<details><summary>↩ Tool result · `toolu_016Aptyp6os7LDasnfXzK2Ny`</summary>

```text
Web search results for query: ""conformal risk control" monotone loss RAG LLM abstention 2025 2026"

Links: [{"title":"Taming Variability: Randomized and Bootstrapped Conformal Risk Control for LLMs","url":"https://arxiv.org/html/2509.23007v1"},{"title":"Conformal Risk Control for Non-Monotonic Losses","url":"https://arxiv.org/pdf/2602.20151"},{"title":"Conformal Risk Control under Non-Monotone Losses: Theory and Finite-Sample Guarantees","url":"https://arxiv.org/html/2604.01502"},{"title":"[2208.02814] Conformal Risk Control","url":"https://arxiv.org/abs/2208.02814"},{"title":"Non-monotonicity in Conformal Risk Control","url":"https://arxiv.org/pdf/2604.01502"},{"title":"[2502.06884] Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models","url":"https://arxiv.org/abs/2502.06884"},{"title":"Conformal Risk Control | OpenReview","url":"https://openreview.net/forum?id=33XGfHLtZg"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"}]

I found several relevant research papers on this topic. Here's what the search returned:

## Key Papers Found

**Recent LLM Applications:**

A Conformal Actuator (CA) framework presents a single, monotone gate that directs actions (ship, abstain, regenerate, escalate) via a scalar, label-free score. This paper from September 2025 addresses uncertainty control in large language models.

**Theoretical Advances on Non-Monotonic Losses:**

Conformal risk control is an extension of conformal prediction for controlling risk functions, with recent work presenting risk control guarantees for generic algorithms applied to possibly non-monotonic losses with multidimensional parameters (February 2026).

Conformal risk control provides distribution-free guarantees for controlling expected loss, though existing theory assumes monotonic loss decrease; recent work studies CRC under non-monotone loss functions when the tuning parameter is selected from a finite grid (April 2026).

**LLM Hallucination and Abstention:**

There has been a number of recent papers studying abstention in LLMs, with work on conformal abstention approaches to mitigate hallucinations.

The search results show active 2025-2026 research combining conformal risk control methods with monotone/non-monotone losses for LLM applications, particularly around abstention policies and uncertainty quantification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc896e53-c0c8-400f-b8e0-177b0630c722",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "0c599159-75ad-4b27-9c74-43eaf906cd6f",
  "toolUseResult": {
    "query": "\"conformal risk control\" monotone loss RAG LLM abstention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015YxcPMyM3dCMVFePNCr3yu",
        "content": [
          {
            "title": "Taming Variability: Randomized and Bootstrapped Conformal Risk Control for LLMs",
            "url": "https://arxiv.org/html/2509.23007v1"
          },
          {
            "title": "Conformal Risk Control for Non-Monotonic Losses",
            "url": "https://arxiv.org/pdf/2602.20151"
          },
          {
            "title": "Conformal Risk Control under Non-Monotone Losses: Theory and Finite-Sample Guarantees",
            "url": "https://arxiv.org/html/2604.01502"
          },
          {
            "title": "[2208.02814] Conformal Risk Control",
            "url": "https://arxiv.org/abs/2208.02814"
          },
          {
            "title": "Non-monotonicity in Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2604.01502"
          },
          {
            "title": "[2502.06884] Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models",
            "url": "https://arxiv.org/abs/2502.06884"
          },
          {
            "title": "Conformal Risk Control | OpenReview",
            "url": "https://openreview.net/forum?id=33XGfHLtZg"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          }
        ]
      },
      "I found several relevant research papers on this topic. Here's what the search returned:\n\n## Key Papers Found\n\n**Recent LLM Applications:**\n\nA Conformal Actuator (CA) framework presents a single, monotone gate that directs actions (ship, abstain, regenerate, escalate) via a scalar, label-free score. This paper from September 2025 addresses uncertainty control in large language models.\n\n**Theoretical Advances on Non-Monotonic Losses:**\n\nConformal risk control is an extension of conformal prediction for controlling risk functions, with recent work presenting risk control guarantees for generic algorithms applied to possibly non-monotonic losses with multidimensional parameters (February 2026).\n\nConformal risk control provides distribution-free guarantees for controlling expected loss, though existing theory assumes monotonic loss decrease; recent work studies CRC under non-monotone loss functions when the tuning parameter is selected from a finite grid (April 2026).\n\n**LLM Hallucination and Abstention:**\n\nThere has been a number of recent papers studying abstention in LLMs, with work on conformal abstention approaches to mitigate hallucinations.\n\nThe search results show active 2025-2026 research combining conformal risk control methods with monotone/non-monotone losses for LLM applications, particularly around abstention policies and uncertainty quantification."
    ],
    "durationSeconds": 6.8688392359999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cc896e53-c0c8-400f-b8e0-177b0630c722",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-30T06:51:37.999Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016cz1YHzNGYohwAUFW2w91x`</summary>

```json
{
  "query": "PoisonedRAG attack benchmark NQ HotpotQA MS-MARCO evaluation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c599159-75ad-4b27-9c74-43eaf906cd6f",
  "isSidechain": false,
  "requestId": "req_011CbYJxymUvyY3E8tRe3hu3",
  "type": "assistant",
  "uuid": "a0bd80db-e58e-4866-8028-452aaa711741",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYyZ8jyMkKCvtDCSsYuoeA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 33155,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 33155,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 757
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

_source line 52 · 2026-05-30T06:51:45.499Z_

<details><summary>↩ Tool result · `toolu_016cz1YHzNGYohwAUFW2w91x`</summary>

```text
Web search results for query: "PoisonedRAG attack benchmark NQ HotpotQA MS-MARCO evaluation 2024 2025"

Links: [{"title":"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.18543"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation","url":"https://openreview.net/pdf?id=AJGfRZwINR"},{"title":"PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/html/2402.07867v1"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval- ...","url":"https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/html/2402.07867"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"},{"title":"GRADA: Graph-based Reranking against Adversarial ...","url":"https://aclanthology.org/2025.emnlp-main.1132.pdf"},{"title":"Quantifying Conversation Drift in MCP via Latent Polytope","url":"https://arxiv.org/html/2508.06418v1"}]

I found comprehensive information about PoisonedRAG and its evaluation on these benchmarks. Here's what the search revealed:

## PoisonedRAG Overview

PoisonedRAG is an official USENIX Security 2025 paper on Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models, with the paper accepted to USENIX Security 2025 on June 20, 2024.

## Benchmark Evaluation Results

The evaluation uses three benchmark question-answering datasets: Natural Questions (NQ), HotpotQA, and MS-MARCO, where NQ and HotpotQA knowledge databases are collected from Wikipedia with 2,681,468 and 5,233,329 texts respectively, and MS-MARCO's knowledge database is collected from web documents using the Microsoft Bing search engine with 8,841,823 texts.

## Attack Success Rates (ASR)

In the black-box setting, PoisonedRAG could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) ASRs for RAG with PaLM 2. Additionally, PoisonedRAG achieves high F1-Scores under different settings (larger than 90% in almost all cases), demonstrating that the malicious texts crafted by PoisonedRAG are very likely to be retrieved for target questions.

Without attacks, the LLM in RAG could correctly provide answers for 70% (NQ), 80% (HotpotQA), and 83% (MS-MARCO) target questions under the default setting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0bd80db-e58e-4866-8028-452aaa711741",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "94781a23-0c0b-41fe-b0ef-a36d3a29a42a",
  "toolUseResult": {
    "query": "PoisonedRAG attack benchmark NQ HotpotQA MS-MARCO evaluation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Eb758RBFVzHf8FKjFFL5Yd",
        "content": [
          {
            "title": "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.18543"
          },
          {
            "title": "GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub",
            "url": "https://github.com/sleeepeer/PoisonedRAG"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation",
            "url": "https://openreview.net/pdf?id=AJGfRZwINR"
          },
          {
            "title": "PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models",
            "url": "https://arxiv.org/html/2402.07867v1"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval- ...",
            "url": "https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models",
            "url": "https://arxiv.org/html/2402.07867"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2504.03957v2"
          },
          {
            "title": "GRADA: Graph-based Reranking against Adversarial ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1132.pdf"
          },
          {
            "title": "Quantifying Conversation Drift in MCP via Latent Polytope",
            "url": "https://arxiv.org/html/2508.06418v1"
          }
        ]
      },
      "I found comprehensive information about PoisonedRAG and its evaluation on these benchmarks. Here's what the search revealed:\n\n## PoisonedRAG Overview\n\nPoisonedRAG is an official USENIX Security 2025 paper on Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models, with the paper accepted to USENIX Security 2025 on June 20, 2024.\n\n## Benchmark Evaluation Results\n\nThe evaluation uses three benchmark question-answering datasets: Natural Questions (NQ), HotpotQA, and MS-MARCO, where NQ and HotpotQA knowledge databases are collected from Wikipedia with 2,681,468 and 5,233,329 texts respectively, and MS-MARCO's knowledge database is collected from web documents using the Microsoft Bing search engine with 8,841,823 texts.\n\n## Attack Success Rates (ASR)\n\nIn the black-box setting, PoisonedRAG could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) ASRs for RAG with PaLM 2. Additionally, PoisonedRAG achieves high F1-Scores under different settings (larger than 90% in almost all cases), demonstrating that the malicious texts crafted by PoisonedRAG are very likely to be retrieved for target questions.\n\nWithout attacks, the LLM in RAG could correctly provide answers for 70% (NQ), 80% (HotpotQA), and 83% (MS-MARCO) target questions under the default setting."
    ],
    "durationSeconds": 7.494690526999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a0bd80db-e58e-4866-8028-452aaa711741",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-30T06:51:49.038Z_

Now let me check for the most critical concurrent work — has anyone already proposed conformal abstention for RAG under poisoning?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94781a23-0c0b-41fe-b0ef-a36d3a29a42a",
  "isSidechain": false,
  "requestId": "req_011CbYJyjo8ScqmMKDDrVDJz",
  "type": "assistant",
  "uuid": "7fb5bf6f-740e-4dc9-bde4-1b5b8ff75d00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132pMfL3ypBYLY4dt2SJZCn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 969,
      "cache_read_input_tokens": 33912,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 33912,
          "cache_creation_input_tokens": 969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 969
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

_source line 54 · 2026-05-30T06:51:49.687Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GvspxLqu7cdR9QYkM6kuP6`</summary>

```json
{
  "query": "\"retrieval-aware\" OR \"retrieval-conditioned\" conformal score poisoning robust RAG 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fb5bf6f-740e-4dc9-bde4-1b5b8ff75d00",
  "isSidechain": false,
  "requestId": "req_011CbYJyjo8ScqmMKDDrVDJz",
  "type": "assistant",
  "uuid": "08b8893d-fb78-4e75-8992-ff90ac310465",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132pMfL3ypBYLY4dt2SJZCn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 969,
      "cache_read_input_tokens": 33912,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 33912,
          "cache_creation_input_tokens": 969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 969
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

_source line 55 · 2026-05-30T06:51:57.422Z_

<details><summary>↩ Tool result · `toolu_01GvspxLqu7cdR9QYkM6kuP6`</summary>

```text
Web search results for query: ""retrieval-aware" OR "retrieval-conditioned" conformal score poisoning robust RAG 2026"

Links: [{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"CPA-RAG:Covert Poisoning Attacks on Retrieval-Augmented Generation in Large Language Models","url":"https://arxiv.org/pdf/2505.19864"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"},{"title":"Preprint. Under Review. RARE: RETRIEVAL-AWARE ROBUSTNESS EVALUATION","url":"https://www.cs.cmu.edu/~sherryw/assets/pubs/2025-rare.pdf"}]

I found several highly relevant research papers on your query. Here are the key results:

1. **RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning** - This work introduces RAGPart, which leverages dense retriever training dynamics with document partitioning to mitigate poisoned points, and RAGMask, which identifies suspicious tokens based on similarity shifts under targeted token masking. The defenses consistently reduce attack success rates while preserving utility across benchmarks, poisoning strategies, and retrievers.

2. **CPA-RAG: Covert Poisoning Attacks on RAG** - This method integrates prompt-based text generation, cross-guided optimization through multiple LLMs, and retriever-based scoring to construct adversarial samples. Results show over 90% attack success when top-k retrieval is 5, and maintains advantages across different top-k values.

3. **Certifiably Robust RAG against Retrieval Corruption** - RobustRAG is proposed as the first certifiably robust defense framework against retrieval corruption attacks, using an isolate-then-aggregate strategy with secure text aggregation techniques.

4. **Is Conformal Factuality for RAG-based LLMs Robust?** - This March 2026 paper by Yi Chen and colleagues examines how conformal factuality and RAG can address LLM hallucination limitations.

5. **RARE: Retrieval-Aware Robustness Evaluation** - This work formalizes retrieval-conditioned robustness metrics (RARE-Met) that capture a model's ability to remain correct or recover when queries, documents, or real-world retrieval results are systematically altered. RAG systems are unexpectedly sensitive to perturbations and show lower robustness on multi-hop queries compared to single-hop queries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08b8893d-fb78-4e75-8992-ff90ac310465",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "edddc964-7499-4661-84a7-b6abae226e26",
  "toolUseResult": {
    "query": "\"retrieval-aware\" OR \"retrieval-conditioned\" conformal score poisoning robust RAG 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FgVAF4W427mNKrybtQavGQ",
        "content": [
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "CPA-RAG:Covert Poisoning Attacks on Retrieval-Augmented Generation in Large Language Models",
            "url": "https://arxiv.org/pdf/2505.19864"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/pdf/2603.16817"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          },
          {
            "title": "Preprint. Under Review. RARE: RETRIEVAL-AWARE ROBUSTNESS EVALUATION",
            "url": "https://www.cs.cmu.edu/~sherryw/assets/pubs/2025-rare.pdf"
          }
        ]
      },
      "I found several highly relevant research papers on your query. Here are the key results:\n\n1. **RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning** - This work introduces RAGPart, which leverages dense retriever training dynamics with document partitioning to mitigate poisoned points, and RAGMask, which identifies suspicious tokens based on similarity shifts under targeted token masking. The defenses consistently reduce attack success rates while preserving utility across benchmarks, poisoning strategies, and retrievers.\n\n2. **CPA-RAG: Covert Poisoning Attacks on RAG** - This method integrates prompt-based text generation, cross-guided optimization through multiple LLMs, and retriever-based scoring to construct adversarial samples. Results show over 90% attack success when top-k retrieval is 5, and maintains advantages across different top-k values.\n\n3. **Certifiably Robust RAG against Retrieval Corruption** - RobustRAG is proposed as the first certifiably robust defense framework against retrieval corruption attacks, using an isolate-then-aggregate strategy with secure text aggregation techniques.\n\n4. **Is Conformal Factuality for RAG-based LLMs Robust?** - This March 2026 paper by Yi Chen and colleagues examines how conformal factuality and RAG can address LLM hallucination limitations.\n\n5. **RARE: Retrieval-Aware Robustness Evaluation** - This work formalizes retrieval-conditioned robustness metrics (RARE-Met) that capture a model's ability to remain correct or recover when queries, documents, or real-world retrieval results are systematically altered. RAG systems are unexpectedly sensitive to perturbations and show lower robustness on multi-hop queries compared to single-hop queries."
    ],
    "durationSeconds": 7.730910451000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "08b8893d-fb78-4e75-8992-ff90ac310465",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-30T06:51:57.425Z_

```json
{
  "parentUuid": "edddc964-7499-4661-84a7-b6abae226e26",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f8226957-5871-4d6a-9e1e-9f445f6b998e",
  "timestamp": "2026-05-30T06:51:57.425Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 57 · 2026-05-30T06:51:59.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XhNQ6UDcpk2gJ1nRrgV87F`</summary>

```json
{
  "query": "conformal abstention RAG poisoning robust prediction set retrieval agreement arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8226957-5871-4d6a-9e1e-9f445f6b998e",
  "isSidechain": false,
  "requestId": "req_011CbYJzcwQDSQkLdSG7NvdX",
  "type": "assistant",
  "uuid": "01fb34eb-9790-4362-8534-077945d85e86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4JcvUQr5rs53Y7e6Nx6Tf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 34881,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 34881,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 980
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

_source line 58 · 2026-05-30T06:52:06.392Z_

<details><summary>↩ Tool result · `toolu_01XhNQ6UDcpk2gJ1nRrgV87F`</summary>

```text
Web search results for query: "conformal abstention RAG poisoning robust prediction set retrieval agreement arxiv 2026"

Links: [{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/html/2412.16708v2"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/abs/2511.17908"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"}]

Based on the web search results, I found several relevant papers related to your query. While the exact combination of all those specific keywords didn't yield a single paper, the search results reveal several closely related works from 2025-2026:

1. **Conformal Prediction for RAG**: Conformal prediction enables reliable, coverage-controlled context reduction in RAG, offering a model-agnostic and principled approach to context engineering.

2. **RAG Robustness Against Poisoning**: RAG systems are vulnerable to various adversarial poisoning attacks; by injecting adversarial data into the underlying RAG database, attackers can manipulate the retriever to return factually incorrect information, thereby reducing model accuracy and propagating disinformation.

3. **Abstention in RAG**: Increasing pollution rates generally decrease performance and skeptical prompts can ameliorate this effect slightly.

4. **Conformal Factuality Robustness**: Conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions.

The search results suggest there's active research at the intersection of conformal prediction, RAG robustness, and poisoning attacks, though I didn't find a single paper matching all the keywords you specified. Would you like me to search for more specific paper titles or authors?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01fb34eb-9790-4362-8534-077945d85e86",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "34c5c59b-2058-484a-beea-1517126aa375",
  "toolUseResult": {
    "query": "conformal abstention RAG poisoning robust prediction set retrieval agreement arxiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019FUYkLQiunatvJRPt8A3Ej",
        "content": [
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/html/2412.16708v2"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/abs/2511.17908"
          },
          {
            "title": "Robust Yet Efficient Conformal Prediction Sets",
            "url": "https://arxiv.org/pdf/2407.09165"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
          },
          {
            "title": "[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/abs/2603.16817"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers related to your query. While the exact combination of all those specific keywords didn't yield a single paper, the search results reveal several closely related works from 2025-2026:\n\n1. **Conformal Prediction for RAG**: Conformal prediction enables reliable, coverage-controlled context reduction in RAG, offering a model-agnostic and principled approach to context engineering.\n\n2. **RAG Robustness Against Poisoning**: RAG systems are vulnerable to various adversarial poisoning attacks; by injecting adversarial data into the underlying RAG database, attackers can manipulate the retriever to return factually incorrect information, thereby reducing model accuracy and propagating disinformation.\n\n3. **Abstention in RAG**: Increasing pollution rates generally decrease performance and skeptical prompts can ameliorate this effect slightly.\n\n4. **Conformal Factuality Robustness**: Conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions.\n\nThe search results suggest there's active research at the intersection of conformal prediction, RAG robustness, and poisoning attacks, though I didn't find a single paper matching all the keywords you specified. Would you like me to search for more specific paper titles or authors?"
    ],
    "durationSeconds": 6.654410421000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "01fb34eb-9790-4362-8534-077945d85e86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "34c5c59b-2058-484a-beea-1517126aa375",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool call

_source line 61 · 2026-05-30T06:52:08.611Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WPQegqAuppmUoRxd6zm7GM`</summary>

```json
{
  "query": "\"conditional conformal factuality\" RAG 2026 arxiv response quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c5c59b-2058-484a-beea-1517126aa375",
  "isSidechain": false,
  "requestId": "req_011CbYK1H7pgR8UDuLW4D6cA",
  "type": "assistant",
  "uuid": "800fc5ce-10b3-4535-be44-11eaca4ad8fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01361wbeaCkWMzsm8uVxB2wF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 35861,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 35861,
          "cache_creation_input_tokens": 802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 802
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

_source line 62 · 2026-05-30T06:52:14.765Z_

<details><summary>↩ Tool result · `toolu_01WPQegqAuppmUoRxd6zm7GM`</summary>

```text
Web search results for query: ""conditional conformal factuality" RAG 2026 arxiv response quality"

Links: [{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling","url":"https://arxiv.org/html/2603.27403v1"},{"title":"(PDF) Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling","url":"https://www.researchgate.net/publication/403308104_Conditional_Factuality_Controlled_LLMs_with_Generalization_Certificates_via_Conformal_Sampling"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"[2603.27403] Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling","url":"https://arxiv.org/abs/2603.27403"},{"title":"[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/abs/2511.17908"}]

Based on the search results, I found relevant research on conditional conformal factuality and RAG response quality assessment:

## Primary Research

The main paper on this topic is Conformal-RAG, a novel framework inspired by recent applications of conformal prediction (CP) on large language models (LLMs). Conformal-RAG leverages CP and internal information from the RAG mechanism to offer statistical guarantees on response quality, and ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets.

## Problem Being Addressed

Existing research on Retrieval-Augmented Generation (RAG) primarily focuses on improving overall question-answering accuracy, often overlooking the quality of sub-claims within generated responses. Recent methods that attempt to improve RAG trustworthiness, such as through auto-evaluation metrics, lack probabilistic guarantees or require ground truth answers.

## Related Work

Additionally, there is related research on Conditional Factuality Control (CFC), a post-hoc conformal framework that returns set-valued outputs with conditional coverage guarantees. This approach addresses existing conformal methods for LLMs that typically provide only marginal guarantees and rely on a single global threshold, which can under-cover hard prompts, over-cover easy ones, and produce oversized prediction sets.

Both of these papers represent recent advances in 2026 addressing the challenge of providing statistical guarantees on factuality and response quality in RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "800fc5ce-10b3-4535-be44-11eaca4ad8fb",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "22d86d08-2004-40bd-a0df-7c0d8bdd9753",
  "toolUseResult": {
    "query": "\"conditional conformal factuality\" RAG 2026 arxiv response quality",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XwYHJbvvxamtKPQhDWM13x",
        "content": [
          {
            "title": "[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978v1"
          },
          {
            "title": "[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978"
          },
          {
            "title": "[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/abs/2603.16817"
          },
          {
            "title": "Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling",
            "url": "https://arxiv.org/html/2603.27403v1"
          },
          {
            "title": "(PDF) Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling",
            "url": "https://www.researchgate.net/publication/403308104_Conditional_Factuality_Controlled_LLMs_with_Generalization_Certificates_via_Conformal_Sampling"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
          },
          {
            "title": "[2603.27403] Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling",
            "url": "https://arxiv.org/abs/2603.27403"
          },
          {
            "title": "[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/abs/2511.17908"
          }
        ]
      },
      "Based on the search results, I found relevant research on conditional conformal factuality and RAG response quality assessment:\n\n## Primary Research\n\nThe main paper on this topic is Conformal-RAG, a novel framework inspired by recent applications of conformal prediction (CP) on large language models (LLMs). Conformal-RAG leverages CP and internal information from the RAG mechanism to offer statistical guarantees on response quality, and ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets.\n\n## Problem Being Addressed\n\nExisting research on Retrieval-Augmented Generation (RAG) primarily focuses on improving overall question-answering accuracy, often overlooking the quality of sub-claims within generated responses. Recent methods that attempt to improve RAG trustworthiness, such as through auto-evaluation metrics, lack probabilistic guarantees or require ground truth answers.\n\n## Related Work\n\nAdditionally, there is related research on Conditional Factuality Control (CFC), a post-hoc conformal framework that returns set-valued outputs with conditional coverage guarantees. This approach addresses existing conformal methods for LLMs that typically provide only marginal guarantees and rely on a single global threshold, which can under-cover hard prompts, over-cover easy ones, and produce oversized prediction sets.\n\nBoth of these papers represent recent advances in 2026 addressing the challenge of providing statistical guarantees on factuality and response quality in RAG systems."
    ],
    "durationSeconds": 6.1492801389999805,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "800fc5ce-10b3-4535-be44-11eaca4ad8fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-30T06:52:20.587Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important - there's a paper called "Conformal-RAG" (Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality, arxiv 2506.20978) and another called "Conditional Factuality Controlled LLMs" (2603.27403). These could be very close to the proposed idea. Let me fetch the details of these papers to understand what they do and how they differ from what we're proposing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22d86d08-2004-40bd-a0df-7c0d8bdd9753",
  "isSidechain": false,
  "requestId": "req_011CbYK1tsPWe4DjZsFNmjAj",
  "type": "assistant",
  "uuid": "382913ca-ba23-4f81-b9d8-d79b9e0407af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sf7cvJq2wNpjP5uidvCixC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 36663,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 36663,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 866
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

_source line 64 · 2026-05-30T06:52:21.070Z_

These are critical — let me fetch details on potentially competing papers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "382913ca-ba23-4f81-b9d8-d79b9e0407af",
  "isSidechain": false,
  "requestId": "req_011CbYK1tsPWe4DjZsFNmjAj",
  "type": "assistant",
  "uuid": "40c091ad-8db2-406a-bbf4-3ae5e8a995cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sf7cvJq2wNpjP5uidvCixC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 36663,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 36663,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 866
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

_source line 65 · 2026-05-30T06:52:23.032Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J8CEFh3dGiNPk4TtZ1mZAN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.20978v1",
  "prompt": "Extract the full abstract, key contributions, method overview, and whether this paper addresses adversarial/poisoning settings. What threat model do they assume? Do they provide robustness to corpus poisoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40c091ad-8db2-406a-bbf4-3ae5e8a995cb",
  "isSidechain": false,
  "requestId": "req_011CbYK1tsPWe4DjZsFNmjAj",
  "type": "assistant",
  "uuid": "d7d8194b-963d-4d22-8637-93dcbd20a146",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sf7cvJq2wNpjP5uidvCixC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 36663,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 261,
          "cache_read_input_tokens": 36663,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 866
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

_source line 66 · 2026-05-30T06:52:28.875Z_

<details><summary>↩ Tool result · `toolu_01J8CEFh3dGiNPk4TtZ1mZAN`</summary>

```text
# Paper Analysis: Response Quality Assessment for RAG via Conditional Conformal Factuality

## Full Abstract
"Existing research on Retrieval-Augmented Generation (RAG) primarily focuses on improving overall question-answering accuracy, often overlooking the quality of sub-claims within generated responses. Recent methods that attempt to improve RAG trustworthiness, such as through auto-evaluation metrics, lack probabilistic guarantees or require ground truth answers. To address these limitations, we propose Conformal-RAG, a novel framework inspired by recent applications of conformal prediction (CP) on large language models (LLMs). Conformal-RAG leverages CP and internal information from the RAG mechanism to offer statistical guarantees on response quality. It ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets, making it suitable for complex RAG applications. Compared to existing RAG auto-evaluation methods, Conformal-RAG offers statistical guarantees on the quality of refined sub-claims, ensuring response reliability without the need for ground truth answers. Additionally, our experiments demonstrate that by leveraging information from the RAG system, Conformal-RAG retains up to 60% more high-quality sub-claims from the response compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee."

## Key Contributions
- Introduces statistical guarantees for RAG response quality assessment
- Achieves group-conditional coverage across multiple sub-domains
- Operates without requiring manual conformal set labeling or ground truth answers
- Demonstrates 60% improvement in retaining high-quality sub-claims

## Method Overview
The framework combines conformal prediction techniques with RAG system information to provide probabilistic guarantees on sub-claim quality within generated responses.

## Adversarial/Poisoning Threat Model
**Not addressed.** This paper focuses on response quality assessment and factuality guarantees but does not discuss adversarial attacks or corpus poisoning scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7d8194b-963d-4d22-8637-93dcbd20a146",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "eb3411a7-2887-49d6-aa1b-855052a6b615",
  "toolUseResult": {
    "bytes": 48948,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Analysis: Response Quality Assessment for RAG via Conditional Conformal Factuality\n\n## Full Abstract\n\"Existing research on Retrieval-Augmented Generation (RAG) primarily focuses on improving overall question-answering accuracy, often overlooking the quality of sub-claims within generated responses. Recent methods that attempt to improve RAG trustworthiness, such as through auto-evaluation metrics, lack probabilistic guarantees or require ground truth answers. To address these limitations, we propose Conformal-RAG, a novel framework inspired by recent applications of conformal prediction (CP) on large language models (LLMs). Conformal-RAG leverages CP and internal information from the RAG mechanism to offer statistical guarantees on response quality. It ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets, making it suitable for complex RAG applications. Compared to existing RAG auto-evaluation methods, Conformal-RAG offers statistical guarantees on the quality of refined sub-claims, ensuring response reliability without the need for ground truth answers. Additionally, our experiments demonstrate that by leveraging information from the RAG system, Conformal-RAG retains up to 60% more high-quality sub-claims from the response compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee.\"\n\n## Key Contributions\n- Introduces statistical guarantees for RAG response quality assessment\n- Achieves group-conditional coverage across multiple sub-domains\n- Operates without requiring manual conformal set labeling or ground truth answers\n- Demonstrates 60% improvement in retaining high-quality sub-claims\n\n## Method Overview\nThe framework combines conformal prediction techniques with RAG system information to provide probabilistic guarantees on sub-claim quality within generated responses.\n\n## Adversarial/Poisoning Threat Model\n**Not addressed.** This paper focuses on response quality assessment and factuality guarantees but does not discuss adversarial attacks or corpus poisoning scenarios.",
    "durationMs": 5838,
    "url": "https://arxiv.org/abs/2506.20978v1"
  },
  "sourceToolAssistantUUID": "d7d8194b-963d-4d22-8637-93dcbd20a146",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-30T06:52:32.042Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RbhoTA5DUYfSpZPdMReWZd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.27403",
  "prompt": "Extract the full abstract, key contributions, method overview, and whether this paper addresses adversarial settings or retrieval poisoning. What are the main differences from TRAQ and standard conformal factuality?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb3411a7-2887-49d6-aa1b-855052a6b615",
  "isSidechain": false,
  "requestId": "req_011CbYK2wDZ933tCKmHB1Rnn",
  "type": "assistant",
  "uuid": "62bd38bd-df60-4b9d-b3a6-14c7a783b58b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cn22nho5dDHFWsSqNcHEMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 37529,
      "output_tokens": 124,
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
          "output_tokens": 124,
          "cache_read_input_tokens": 37529,
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

_source line 68 · 2026-05-30T06:52:38.085Z_

<details><summary>↩ Tool result · `toolu_01RbhoTA5DUYfSpZPdMReWZd`</summary>

```text
# Paper Analysis: Conditional Factuality Controlled LLMs

## Full Abstract
"Large language models (LLMs) need reliable test-time control of hallucinations. Existing conformal methods for LLMs typically provide only marginal guarantees and rely on a single global threshold, which can under-cover hard prompts, over-cover easy ones, and produce oversized prediction sets."

The proposed method returns set-valued outputs with conditional coverage guarantees using augmented quantile regression and deploys conditional thresholds at inference time.

## Key Contributions

1. **Conditional Factuality Control (CFC)**: A post-hoc conformal framework providing set-valued outputs with "conditional coverage guarantees" rather than marginal ones

2. **Theoretical Guarantees**: 
   - Conditional coverage under exchangeability
   - Proof that conditional rules are more sample-efficient than marginal conformal prediction
   - CFC-PAC variant with finite-sample certificates showing miscoverage deviates by at most "O(√(log(1/δ)/N))"

3. **Empirical Performance**: Achieves near-target coverage across difficulty groups with smaller prediction sets than baselines

## Method Overview

The approach uses augmented quantile regression to define continuous, feature-conditional acceptance thresholds based on latent "success" scores, deployed through fixed-point threshold rules during inference.

## Adversarial Settings & Retrieval Poisoning

**Not addressed.** This paper focuses on controlling hallucinations through conformal prediction methods, not defending against adversarial attacks or data poisoning scenarios.

## Differences from TRAQ & Standard Conformal Factuality

**Not discussed in provided content.** The document doesn't reference TRAQ or compare against other named conformal factuality approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62bd38bd-df60-4b9d-b3a6-14c7a783b58b",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "93009c1c-bf4d-479f-8715-ac99f359eae2",
  "toolUseResult": {
    "bytes": 46885,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Analysis: Conditional Factuality Controlled LLMs\n\n## Full Abstract\n\"Large language models (LLMs) need reliable test-time control of hallucinations. Existing conformal methods for LLMs typically provide only marginal guarantees and rely on a single global threshold, which can under-cover hard prompts, over-cover easy ones, and produce oversized prediction sets.\"\n\nThe proposed method returns set-valued outputs with conditional coverage guarantees using augmented quantile regression and deploys conditional thresholds at inference time.\n\n## Key Contributions\n\n1. **Conditional Factuality Control (CFC)**: A post-hoc conformal framework providing set-valued outputs with \"conditional coverage guarantees\" rather than marginal ones\n\n2. **Theoretical Guarantees**: \n   - Conditional coverage under exchangeability\n   - Proof that conditional rules are more sample-efficient than marginal conformal prediction\n   - CFC-PAC variant with finite-sample certificates showing miscoverage deviates by at most \"O(√(log(1/δ)/N))\"\n\n3. **Empirical Performance**: Achieves near-target coverage across difficulty groups with smaller prediction sets than baselines\n\n## Method Overview\n\nThe approach uses augmented quantile regression to define continuous, feature-conditional acceptance thresholds based on latent \"success\" scores, deployed through fixed-point threshold rules during inference.\n\n## Adversarial Settings & Retrieval Poisoning\n\n**Not addressed.** This paper focuses on controlling hallucinations through conformal prediction methods, not defending against adversarial attacks or data poisoning scenarios.\n\n## Differences from TRAQ & Standard Conformal Factuality\n\n**Not discussed in provided content.** The document doesn't reference TRAQ or compare against other named conformal factuality approaches.",
    "durationMs": 6039,
    "url": "https://arxiv.org/abs/2603.27403"
  },
  "sourceToolAssistantUUID": "62bd38bd-df60-4b9d-b3a6-14c7a783b58b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-30T06:52:44.586Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HZeczSps2ugBiKjGasUde5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16817",
  "prompt": "Extract the full abstract, key findings, what specific failure modes they identify for conformal factuality in RAG, and whether they propose any solution or only diagnosis. What are their proposed metrics (Non-Empty Rate, Non-Vacuous Empirical Factuality)? What do they recommend as future work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93009c1c-bf4d-479f-8715-ac99f359eae2",
  "isSidechain": false,
  "requestId": "req_011CbYK3cdPPr7Fu46wjc4bJ",
  "type": "assistant",
  "uuid": "f9d6f906-1f16-4963-bbdc-bfca4f52e7cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtHMa7XmV3FtFe8dj3jxEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 38230,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 534,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 38230,
          "cache_creation_input_tokens": 534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 534
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

_source line 70 · 2026-05-30T06:52:49.939Z_

<details><summary>↩ Tool result · `toolu_01HZeczSps2ugBiKjGasUde5`</summary>

```text
# Analysis of arXiv:2603.16817

## Full Abstract
The paper examines reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency dimensions. It proposes informativeness-aware metrics and finds that conformal filtering produces vacuous outputs at high factuality levels, lacks robustness to distribution shifts, and that lightweight entailment-based verifiers outperform LLM confidence scorers computationally.

## Key Findings
The authors identify three primary discoveries:

1. **Low usefulness paradox**: "conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs"

2. **Fragility under distribution shift**: The conformal factuality guarantee lacks robustness when deployment conditions diverge from calibration data

3. **Computational efficiency gains**: Lightweight entailment verifiers require "over 100× fewer FLOPs" than LLM-based scorers while maintaining comparable performance

## Identified Failure Modes
- Vacuous outputs when filtering aggressively for high factuality
- Sensitivity to distribution shifts and distractors
- Dependency on calibration data closely matching deployment scenarios

## Solutions vs. Diagnosis
The paper **primarily diagnoses problems** rather than proposing solutions. While it recommends "new approaches for reliability," it offers actionable guidance for building efficient RAG pipelines but doesn't present novel mitigation techniques.

## Proposed Metrics
The authors introduce **informativeness-aware metrics**, specifically:
- **Non-Empty Rate**: Measures output preservation
- **Non-Vacuous Empirical Factuality**: Evaluates factuality among non-empty outputs

## Future Work Recommendations
The paper emphasizes need for approaches balancing reliability with robustness and usefulness as central design metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9d6f906-1f16-4963-bbdc-bfca4f52e7cd",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "8f632366-2492-4ad4-ad05-b5c955ec06de",
  "toolUseResult": {
    "bytes": 48154,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2603.16817\n\n## Full Abstract\nThe paper examines reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency dimensions. It proposes informativeness-aware metrics and finds that conformal filtering produces vacuous outputs at high factuality levels, lacks robustness to distribution shifts, and that lightweight entailment-based verifiers outperform LLM confidence scorers computationally.\n\n## Key Findings\nThe authors identify three primary discoveries:\n\n1. **Low usefulness paradox**: \"conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs\"\n\n2. **Fragility under distribution shift**: The conformal factuality guarantee lacks robustness when deployment conditions diverge from calibration data\n\n3. **Computational efficiency gains**: Lightweight entailment verifiers require \"over 100× fewer FLOPs\" than LLM-based scorers while maintaining comparable performance\n\n## Identified Failure Modes\n- Vacuous outputs when filtering aggressively for high factuality\n- Sensitivity to distribution shifts and distractors\n- Dependency on calibration data closely matching deployment scenarios\n\n## Solutions vs. Diagnosis\nThe paper **primarily diagnoses problems** rather than proposing solutions. While it recommends \"new approaches for reliability,\" it offers actionable guidance for building efficient RAG pipelines but doesn't present novel mitigation techniques.\n\n## Proposed Metrics\nThe authors introduce **informativeness-aware metrics**, specifically:\n- **Non-Empty Rate**: Measures output preservation\n- **Non-Vacuous Empirical Factuality**: Evaluates factuality among non-empty outputs\n\n## Future Work Recommendations\nThe paper emphasizes need for approaches balancing reliability with robustness and usefulness as central design metrics.",
    "durationMs": 5348,
    "url": "https://arxiv.org/abs/2603.16817"
  },
  "sourceToolAssistantUUID": "f9d6f906-1f16-4963-bbdc-bfca4f52e7cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-30T06:52:54.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mv7dEMiZNJXgkX2cwiL147`</summary>

```json
{
  "query": "\"online conformal abstention\" \"factuality control\" \"adversarial bandit\" 2506.14067"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f632366-2492-4ad4-ad05-b5c955ec06de",
  "isSidechain": false,
  "requestId": "req_011CbYK4W4mczdAxX4irrcfC",
  "type": "assistant",
  "uuid": "f5e5cf32-63cf-4cdf-9087-082989134418",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VuBs5a7zMHptc413NwtFd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 38764,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 564,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 38764,
          "cache_creation_input_tokens": 564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 564
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

_source line 72 · 2026-05-30T06:53:00.939Z_

<details><summary>↩ Tool result · `toolu_01Mv7dEMiZNJXgkX2cwiL147`</summary>

```text
Web search results for query: ""online conformal abstention" "factuality control" "adversarial bandit" 2506.14067"

Links: [{"title":"[2506.14067] Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback","url":"https://arxiv.org/abs/2506.14067"},{"title":"Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization | OpenReview","url":"https://openreview.net/forum?id=RMWcdp5IUy"},{"title":"[2604.17984] Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization","url":"https://arxiv.org/abs/2604.17984"},{"title":"Online Conformal Prediction with Adversarial Semi-Bandit Feedback via Regret Minimization","url":"https://arxiv.org/html/2604.17984v1"},{"title":"From Bandit Regret to FDR Control: Online Selective Generation with Adversarial Feedback Unlocking","url":"https://arxiv.org/pdf/2506.14067"}]

I found the paper! Here are the search results for your query:

The paper with ID 2506.14067 is titled "From Bandit Regret to FDR Control: Online Selective Generation with Adversarial Feedback Unlocking" by Minjae Lee and Yoonjae Jung.

**Key Details:**

The paper addresses how interactive generative systems that generate unreliable or false responses can be mitigated through selective generation to ensure the system answers only when confident, despite real-world deployments typically providing only partial user feedback and operating in non-stationary or adversarial environments.

**Main Contribution:**

The authors propose ExSUL, a novel online learning framework for selective generation with adversarial bandit feedback. The technical contributions include a novel conversion lemma that translates bandit algorithm regret into an FDR bound, and feedback unlocking, a strategy that exploits the structure of selective generation to extract additional learning signals from partial feedback.

**Results:**

The method achieves a regret bound of O(√T ln |H|), matching the efficiency and FDR controllability of full-information settings despite receiving only partial feedback. The approach is demonstrated on question-answering tasks and robustly controls the FDR while maintaining competitive answering coverage.

The paper was posted on March 6, 2026, and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5e5cf32-63cf-4cdf-9087-082989134418",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "c2183f39-ca90-4fff-b1a8-88fe51e44c3e",
  "toolUseResult": {
    "query": "\"online conformal abstention\" \"factuality control\" \"adversarial bandit\" 2506.14067",
    "results": [
      {
        "tool_use_id": "srvtoolu_012YkAB2xTGVxqBVdqTQKHjb",
        "content": [
          {
            "title": "[2506.14067] Online Conformal Abstention for Factuality Control Under Adversarial Bandit Feedback",
            "url": "https://arxiv.org/abs/2506.14067"
          },
          {
            "title": "Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization | OpenReview",
            "url": "https://openreview.net/forum?id=RMWcdp5IUy"
          },
          {
            "title": "[2604.17984] Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization",
            "url": "https://arxiv.org/abs/2604.17984"
          },
          {
            "title": "Online Conformal Prediction with Adversarial Semi-Bandit Feedback via Regret Minimization",
            "url": "https://arxiv.org/html/2604.17984v1"
          },
          {
            "title": "From Bandit Regret to FDR Control: Online Selective Generation with Adversarial Feedback Unlocking",
            "url": "https://arxiv.org/pdf/2506.14067"
          }
        ]
      },
      "I found the paper! Here are the search results for your query:\n\nThe paper with ID 2506.14067 is titled \"From Bandit Regret to FDR Control: Online Selective Generation with Adversarial Feedback Unlocking\" by Minjae Lee and Yoonjae Jung.\n\n**Key Details:**\n\nThe paper addresses how interactive generative systems that generate unreliable or false responses can be mitigated through selective generation to ensure the system answers only when confident, despite real-world deployments typically providing only partial user feedback and operating in non-stationary or adversarial environments.\n\n**Main Contribution:**\n\nThe authors propose ExSUL, a novel online learning framework for selective generation with adversarial bandit feedback. The technical contributions include a novel conversion lemma that translates bandit algorithm regret into an FDR bound, and feedback unlocking, a strategy that exploits the structure of selective generation to extract additional learning signals from partial feedback.\n\n**Results:**\n\nThe method achieves a regret bound of O(√T ln |H|), matching the efficiency and FDR controllability of full-information settings despite receiving only partial feedback. The approach is demonstrated on question-answering tasks and robustly controls the FDR while maintaining competitive answering coverage.\n\nThe paper was posted on March 6, 2026, and is available on arXiv."
    ],
    "durationSeconds": 6.219218653999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f5e5cf32-63cf-4cdf-9087-082989134418",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "c2183f39-ca90-4fff-b1a8-88fe51e44c3e",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool call

_source line 75 · 2026-05-30T06:53:04.870Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JMWy9DzSCuwg484iWRKF5H`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.14067",
  "prompt": "Extract the full abstract and key method. Does this paper specifically address RAG corpus poisoning? Does it provide distribution-free guarantees under adversarial retrieval? How does it differ from conformal prediction-based approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2183f39-ca90-4fff-b1a8-88fe51e44c3e",
  "isSidechain": false,
  "requestId": "req_011CbYK5K5W1cemCa7t1hpWw",
  "type": "assistant",
  "uuid": "85b19d58-b63d-428f-adc8-09795893c82a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PF2BJNj8MEcka9LDpdwKpc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 39328,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 39328,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
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

_source line 76 · 2026-05-30T06:53:10.662Z_

<details><summary>↩ Tool result · `toolu_01JMWy9DzSCuwg484iWRKF5H`</summary>

```text
# Analysis of arXiv:2506.14067

## Full Abstract

"As interactive generative systems are increasingly deployed in real-world applications, their tendency to generate unreliable or false responses raises serious concerns. Conformal abstention mitigates this risk by ensuring that the system answers only when confident. However, real-world deployments typically provide only partial user feedback (e.g., thumbs up/down) on the selected response and often operate in non-stationary or adversarial environments, for which effective learning methods are largely missing. To bridge this gap, we propose ExAUL, a novel online learning framework for conformal abstention with adversarial and partial feedback."

The paper introduces a conversion mechanism translating bandit algorithm regret into False Discovery Rate bounds and employs "feedback unlocking" to extract additional signals from partial feedback, achieving O(√T) regret bounds.

## Does It Address RAG Corpus Poisoning?

**No.** The paper focuses on controlling factuality through selective abstention (choosing when to respond), not on detecting or mitigating poisoned retrieval corpora.

## Distribution-Free Guarantees Under Adversarial Retrieval?

**Not specifically.** While the framework operates in adversarial settings, it doesn't specifically address adversarial retrieval mechanisms or poisoned knowledge sources—it targets the response generation stage.

## Distinction from Conformal Prediction Approaches?

This work extends conformal methods by adapting them to **online bandit feedback scenarios** rather than batch settings with full information. Traditional conformal prediction typically requires complete feedback; ExAUL operates with partial, selective feedback while maintaining statistical guarantees.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85b19d58-b63d-428f-adc8-09795893c82a",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "7b46f506-3400-4c1e-aa1e-a66682004f2c",
  "toolUseResult": {
    "bytes": 48116,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2506.14067\n\n## Full Abstract\n\n\"As interactive generative systems are increasingly deployed in real-world applications, their tendency to generate unreliable or false responses raises serious concerns. Conformal abstention mitigates this risk by ensuring that the system answers only when confident. However, real-world deployments typically provide only partial user feedback (e.g., thumbs up/down) on the selected response and often operate in non-stationary or adversarial environments, for which effective learning methods are largely missing. To bridge this gap, we propose ExAUL, a novel online learning framework for conformal abstention with adversarial and partial feedback.\"\n\nThe paper introduces a conversion mechanism translating bandit algorithm regret into False Discovery Rate bounds and employs \"feedback unlocking\" to extract additional signals from partial feedback, achieving O(√T) regret bounds.\n\n## Does It Address RAG Corpus Poisoning?\n\n**No.** The paper focuses on controlling factuality through selective abstention (choosing when to respond), not on detecting or mitigating poisoned retrieval corpora.\n\n## Distribution-Free Guarantees Under Adversarial Retrieval?\n\n**Not specifically.** While the framework operates in adversarial settings, it doesn't specifically address adversarial retrieval mechanisms or poisoned knowledge sources—it targets the response generation stage.\n\n## Distinction from Conformal Prediction Approaches?\n\nThis work extends conformal methods by adapting them to **online bandit feedback scenarios** rather than batch settings with full information. Traditional conformal prediction typically requires complete feedback; ExAUL operates with partial, selective feedback while maintaining statistical guarantees.",
    "durationMs": 5788,
    "url": "https://arxiv.org/abs/2506.14067"
  },
  "sourceToolAssistantUUID": "85b19d58-b63d-428f-adc8-09795893c82a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-30T06:53:13.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0112ZVnnGqPpXjZmR7KqCWni`</summary>

```json
{
  "query": "Bayesian conformal prediction data-conditional posterior bounds ICML 2025 outstanding paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b46f506-3400-4c1e-aa1e-a66682004f2c",
  "isSidechain": false,
  "requestId": "req_011CbYK61x9SgmZCz5P4RC3f",
  "type": "assistant",
  "uuid": "18889f8b-a112-4c03-9b5a-b334eb47502a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W97pHocpGKUuzNvRuxfmNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 40034,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 40034,
          "cache_creation_input_tokens": 501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 501
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

_source line 78 · 2026-05-30T06:53:19.925Z_

<details><summary>↩ Tool result · `toolu_0112ZVnnGqPpXjZmR7KqCWni`</summary>

```text
Web search results for query: "Bayesian conformal prediction data-conditional posterior bounds ICML 2025 outstanding paper"

Links: [{"title":"[ICML 2025] Conformal Prediction as Bayesian Quadrature - ArXivIQ","url":"https://arxiviq.substack.com/p/icml-2025-conformal-prediction-as"},{"title":"Conformal Prediction as Bayesian Quadrature","url":"https://jakesnell.com/projects/conformal-as-bayes-quad/"},{"title":"Weighted Bayesian Conformal Prediction","url":"https://arxiv.org/pdf/2604.06464"},{"title":"Conformal Bayesian Computation","url":"https://arxiv.org/pdf/2106.06137"},{"title":"Posterior Conformal Prediction","url":"https://arxiv.org/pdf/2409.19712"},{"title":"ICML 2025 Conformal Prediction as Bayesian Quadrature Oral","url":"https://icml.cc/virtual/2025/oral/47227"},{"title":"PROBABILISTIC CONFORMAL PREDICTION WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9da457059dd3386a2166c5b08f29b7de-Paper-Conference.pdf"}]

Based on the search results, I found information about the paper you're looking for:

"Conformal Prediction as Bayesian Quadrature" is an ICML 2025 Outstanding Paper. 

The paper reframes frequentist conformal prediction through a Bayesian lens, modeling the problem of bounding expected loss as an application of Bayesian Quadrature. The authors leverage a classic result from distribution-free statistics—that the spacings between ordered quantiles of i.i.d. samples follow a Dirichlet distribution—to develop a nonparametric framework that remains distribution-free.

A key contribution is that instead of producing a single point estimate of risk, the method computes the full posterior distribution of a provable upper bound on the expected loss, which they call L+. This approach provides a richer, more practical "data-conditional" guarantee on model performance.

The main contributions include reformulating conformal prediction as prior-agnostic Bayesian quadrature and showing how to recover conformal prediction from the posterior mean estimate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18889f8b-a112-4c03-9b5a-b334eb47502a",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "72766d7f-01e1-4e97-a333-56be263411ca",
  "toolUseResult": {
    "query": "Bayesian conformal prediction data-conditional posterior bounds ICML 2025 outstanding paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PrvxW4zpd7Te8ZtuMKwe2E",
        "content": [
          {
            "title": "[ICML 2025] Conformal Prediction as Bayesian Quadrature - ArXivIQ",
            "url": "https://arxiviq.substack.com/p/icml-2025-conformal-prediction-as"
          },
          {
            "title": "Conformal Prediction as Bayesian Quadrature",
            "url": "https://jakesnell.com/projects/conformal-as-bayes-quad/"
          },
          {
            "title": "Weighted Bayesian Conformal Prediction",
            "url": "https://arxiv.org/pdf/2604.06464"
          },
          {
            "title": "Conformal Bayesian Computation",
            "url": "https://arxiv.org/pdf/2106.06137"
          },
          {
            "title": "Posterior Conformal Prediction",
            "url": "https://arxiv.org/pdf/2409.19712"
          },
          {
            "title": "ICML 2025 Conformal Prediction as Bayesian Quadrature Oral",
            "url": "https://icml.cc/virtual/2025/oral/47227"
          },
          {
            "title": "PROBABILISTIC CONFORMAL PREDICTION WITH ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/9da457059dd3386a2166c5b08f29b7de-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n\"Conformal Prediction as Bayesian Quadrature\" is an ICML 2025 Outstanding Paper. \n\nThe paper reframes frequentist conformal prediction through a Bayesian lens, modeling the problem of bounding expected loss as an application of Bayesian Quadrature. The authors leverage a classic result from distribution-free statistics—that the spacings between ordered quantiles of i.i.d. samples follow a Dirichlet distribution—to develop a nonparametric framework that remains distribution-free.\n\nA key contribution is that instead of producing a single point estimate of risk, the method computes the full posterior distribution of a provable upper bound on the expected loss, which they call L+. This approach provides a richer, more practical \"data-conditional\" guarantee on model performance.\n\nThe main contributions include reformulating conformal prediction as prior-agnostic Bayesian quadrature and showing how to recover conformal prediction from the posterior mean estimate."
    ],
    "durationSeconds": 6.5348071029999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "18889f8b-a112-4c03-9b5a-b334eb47502a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-30T06:53:22.437Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014sPCZp2Dph3fvypmFTmL3h`</summary>

```json
{
  "query": "CAS certified adversarial score conformal prediction MILP CDF bounds ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72766d7f-01e1-4e97-a333-56be263411ca",
  "isSidechain": false,
  "requestId": "req_011CbYK6hVAg38Mr1VTfzRJ9",
  "type": "assistant",
  "uuid": "e37bbae7-bbeb-44be-b5dd-fdb692a0ce11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kyhrxEimnZ78t9no9gh2d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 40535,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 40535,
          "cache_creation_input_tokens": 663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 663
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

_source line 80 · 2026-05-30T06:53:36.050Z_

<details><summary>↩ Tool result · `toolu_014sPCZp2Dph3fvypmFTmL3h`</summary>

```text
Web search results for query: "CAS certified adversarial score conformal prediction MILP CDF bounds ICML 2024"

Links: [{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"robust conformal prediction with a single binary certificate","url":"https://arxiv.org/pdf/2503.05239"},{"title":"ROBUST CONFORMAL PREDICTION WITH A SINGLE ... - cispa","url":"https://publications.cispa.de/articles/conference_contribution/Robust_Conformal_Prediction_with_a_Single_Binary_Certificate/29618666/1/files/56460146.pdf"},{"title":"Provably Robust Conformal Prediction with Improved efficiency","url":"https://lilywenglab.github.io/Provably-Robust-Conformal-Prediction/"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"},{"title":"Adversarially Robust Conformal Prediction","url":"https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"},{"title":"Verifiably Robust Conformal Prediction Linus Jeary∗ Department of Informatics","url":"https://arxiv.org/pdf/2405.18942"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"}]

Based on the search results, I found relevant information about the topics you're searching for:

Zargarbashi et al. (2024) derive robust prediction sets by bounding worst-case changes in conformity scores for adversarial evasion and poisoning attacks. They use CDF-based bounds to compute conservative prediction sets, which appears to relate to the "CDF bounds" mentioned in your query.

CAS-type bounds support both evasion (test-time) and poisoning (calibration-time) attacks, including discrete data manipulation, with worst-case meta-quantile optimization via MILP (Zargarbashi et al., 2024). This directly addresses the combination of "CAS," "MILP," and "CDF bounds" in your query.

The search results reference Zargarbashi et al. (2024) work on robust conformal prediction that combines these technical approaches. However, I should note that the specific conference attribution to "ICML 2024" is not explicitly confirmed in these results—the papers appear to be from various venues including arXiv preprints. The references suggest this represents recent work in the intersection of adversarial robustness and conformal prediction methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e37bbae7-bbeb-44be-b5dd-fdb692a0ce11",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "3f559a94-99c4-443d-a03c-6c9907b403cb",
  "toolUseResult": {
    "query": "CAS certified adversarial score conformal prediction MILP CDF bounds ICML 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C8Q8uYG1EgEhGXfZMZSzYD",
        "content": [
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/html/2506.07804v1"
          },
          {
            "title": "robust conformal prediction with a single binary certificate",
            "url": "https://arxiv.org/pdf/2503.05239"
          },
          {
            "title": "ROBUST CONFORMAL PREDICTION WITH A SINGLE ... - cispa",
            "url": "https://publications.cispa.de/articles/conference_contribution/Robust_Conformal_Prediction_with_a_Single_Binary_Certificate/29618666/1/files/56460146.pdf"
          },
          {
            "title": "Provably Robust Conformal Prediction with Improved efficiency",
            "url": "https://lilywenglab.github.io/Provably-Robust-Conformal-Prediction/"
          },
          {
            "title": "Robust Yet Efficient Conformal Prediction Sets",
            "url": "https://arxiv.org/pdf/2407.09165"
          },
          {
            "title": "Adversarially Robust Conformal Prediction",
            "url": "https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"
          },
          {
            "title": "Verifiably Robust Conformal Prediction Linus Jeary∗ Department of Informatics",
            "url": "https://arxiv.org/pdf/2405.18942"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found relevant information about the topics you're searching for:\n\nZargarbashi et al. (2024) derive robust prediction sets by bounding worst-case changes in conformity scores for adversarial evasion and poisoning attacks. They use CDF-based bounds to compute conservative prediction sets, which appears to relate to the \"CDF bounds\" mentioned in your query.\n\nCAS-type bounds support both evasion (test-time) and poisoning (calibration-time) attacks, including discrete data manipulation, with worst-case meta-quantile optimization via MILP (Zargarbashi et al., 2024). This directly addresses the combination of \"CAS,\" \"MILP,\" and \"CDF bounds\" in your query.\n\nThe search results reference Zargarbashi et al. (2024) work on robust conformal prediction that combines these technical approaches. However, I should note that the specific conference attribution to \"ICML 2024\" is not explicitly confirmed in these results—the papers appear to be from various venues including arXiv preprints. The references suggest this represents recent work in the intersection of adversarial robustness and conformal prediction methods."
    ],
    "durationSeconds": 13.609339274000027,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e37bbae7-bbeb-44be-b5dd-fdb692a0ce11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 81 · 2026-05-30T06:53:36.054Z_

```json
{
  "parentUuid": "3f559a94-99c4-443d-a03c-6c9907b403cb",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "51335bdb-77cf-4790-8df3-b0ef56846fbb",
  "timestamp": "2026-05-30T06:53:36.054Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 82 · 2026-05-30T06:53:38.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLbGNti3DbdjgS1CX9kFzn`</summary>

```json
{
  "query": "conformal prediction NLP survey 2025 2026 open challenges retrieval augmented"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51335bdb-77cf-4790-8df3-b0ef56846fbb",
  "isSidechain": false,
  "requestId": "req_011CbYK7tRWwMXxaqwB4yyBn",
  "type": "assistant",
  "uuid": "cdefcf00-5656-47d6-9925-b7b8eaa9d701",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ng7wbT98uA9WNJqBZ4f9b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 41198,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 41198,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 83 · 2026-05-30T06:53:44.695Z_

<details><summary>↩ Tool result · `toolu_01XLbGNti3DbdjgS1CX9kFzn`</summary>

```text
Web search results for query: "conformal prediction NLP survey 2025 2026 open challenges retrieval augmented"

Links: [{"title":"[2405.01976v1] Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/abs/2405.01976v1"},{"title":"Conformal Prediction for Natural Language Processing: A Survey | Request PDF","url":"https://www.researchgate.net/publication/386030579_Conformal_Prediction_for_Natural_Language_Processing_A_Survey"},{"title":"[2405.01976] Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/abs/2405.01976"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/pdf/2405.01976"},{"title":"Conformal Prediction in the Age of Multimodal Foundation Models: A Survey | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-15120-9_13"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/html/2405.01976v1"},{"title":"Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"},{"title":"dblp: Conformal Prediction for Natural Language Processing: A Survey.","url":"https://dblp.org/rec/journals/corr/abs-2405-01976.html"}]

Based on the search results, I found several relevant resources on conformal prediction in NLP:

## Key Survey Papers

A comprehensive survey of conformal prediction techniques, their guarantees, and existing applications in NLP points to directions for future research and open challenges. The rapid proliferation of large language models and NLP applications creates a crucial need for uncertainty quantification to mitigate risks such as hallucinations, and conformal prediction is emerging as a theoretically sound and practically useful framework combining flexibility with strong statistical guarantees.

## Retrieval-Augmented Generation

Recent innovations span generative modeling, predictive pipelines, reasoning and control, and retrieval-augmented generation, highlighting techniques such as sampling-aware calibration, trust-score conditioning and input-adaptive error control. Additionally, the survey delves into current limitations faced by retrieval-augmented LLMs in combating hallucinations.

## Recent Applications

Conformal prediction has been employed recently in NLP frameworks such as content moderation based on model uncertainty in predicting toxicity and disagreement among annotators.

The most relevant survey appears to be the arXiv paper (2405.01976) from May 2024, which has been published in the Transactions of the Association for Computational Linguistics and provides a comprehensive overview covering conformal prediction techniques for NLP tasks, including open challenges and future research directions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdefcf00-5656-47d6-9925-b7b8eaa9d701",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "679c1e04-7c33-4f63-9c61-7565603593c7",
  "toolUseResult": {
    "query": "conformal prediction NLP survey 2025 2026 open challenges retrieval augmented",
    "results": [
      {
        "tool_use_id": "srvtoolu_017KwZ6RC4Qt6CNGps27wqGU",
        "content": [
          {
            "title": "[2405.01976v1] Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/abs/2405.01976v1"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey | Request PDF",
            "url": "https://www.researchgate.net/publication/386030579_Conformal_Prediction_for_Natural_Language_Processing_A_Survey"
          },
          {
            "title": "[2405.01976] Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/abs/2405.01976"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/pdf/2405.01976"
          },
          {
            "title": "Conformal Prediction in the Age of Multimodal Foundation Models: A Survey | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-15120-9_13"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/html/2405.01976v1"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"
          },
          {
            "title": "dblp: Conformal Prediction for Natural Language Processing: A Survey.",
            "url": "https://dblp.org/rec/journals/corr/abs-2405-01976.html"
          }
        ]
      },
      "Based on the search results, I found several relevant resources on conformal prediction in NLP:\n\n## Key Survey Papers\n\nA comprehensive survey of conformal prediction techniques, their guarantees, and existing applications in NLP points to directions for future research and open challenges. The rapid proliferation of large language models and NLP applications creates a crucial need for uncertainty quantification to mitigate risks such as hallucinations, and conformal prediction is emerging as a theoretically sound and practically useful framework combining flexibility with strong statistical guarantees.\n\n## Retrieval-Augmented Generation\n\nRecent innovations span generative modeling, predictive pipelines, reasoning and control, and retrieval-augmented generation, highlighting techniques such as sampling-aware calibration, trust-score conditioning and input-adaptive error control. Additionally, the survey delves into current limitations faced by retrieval-augmented LLMs in combating hallucinations.\n\n## Recent Applications\n\nConformal prediction has been employed recently in NLP frameworks such as content moderation based on model uncertainty in predicting toxicity and disagreement among annotators.\n\nThe most relevant survey appears to be the arXiv paper (2405.01976) from May 2024, which has been published in the Transactions of the Association for Computational Linguistics and provides a comprehensive overview covering conformal prediction techniques for NLP tasks, including open challenges and future research directions."
    ],
    "durationSeconds": 6.2264831529999505,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cdefcf00-5656-47d6-9925-b7b8eaa9d701",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-30T06:53:47.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ERwTAzduxcoFVeu342TySN`</summary>

```json
{
  "query": "RAGPart RAGMask retrieval stage defense corpus poisoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "679c1e04-7c33-4f63-9c61-7565603593c7",
  "isSidechain": false,
  "requestId": "req_011CbYK8XSUgAepenafDR8df",
  "type": "assistant",
  "uuid": "1b789e3a-e6e8-4549-91d4-8fb931a52d21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCJQkPqXVUnqaUW9baYScN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 42093,
      "output_tokens": 72,
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
          "output_tokens": 72,
          "cache_read_input_tokens": 42093,
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

_source line 85 · 2026-05-30T06:53:52.468Z_

<details><summary>↩ Tool result · `toolu_01ERwTAzduxcoFVeu342TySN`</summary>

```text
Web search results for query: "RAGPart RAGMask retrieval stage defense corpus poisoning 2025 2026"

Links: [{"title":"(PDF) RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://www.researchgate.net/publication/399277254_RAGPart_RAGMask_Retrieval-Stage_Defenses_Against_Corpus_Poisoning_in_Retrieval-Augmented_Generation"},{"title":"Advances LLM Security, RAGPart And RAGMask Mitigates Corpus Poisoning In Generation Pipelines","url":"https://quantumzeitgeist.com/security-advances-llm-ragpart-ragmask-mitigates/"},{"title":"[2512.24268] RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2512.24268"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"}]

Based on the search results, I found information about RAGPart and RAGMask:

RAGPart and RAGMask are two complementary retrieval-stage defenses against corpus poisoning in Retrieval-Augmented Generation (RAG), where adversaries inject malicious documents into the retrieval corpus to manipulate model outputs.

RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points. RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.

These defenses operate directly on the retriever, making them computationally lightweight and requiring no modification to the generation model. Experiments show RAGPart can prevent poisoned documents from appearing among the top retrieved results.

The research was published in December 2025, with the arXiv preprint dated December 30, 2025 (arXiv:2512.24268).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b789e3a-e6e8-4549-91d4-8fb931a52d21",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "8a0487a3-ff22-4799-a5ea-a8b982984978",
  "toolUseResult": {
    "query": "RAGPart RAGMask retrieval stage defense corpus poisoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fo7yx83d3YKgeXnqxc9WE2",
        "content": [
          {
            "title": "(PDF) RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://www.researchgate.net/publication/399277254_RAGPart_RAGMask_Retrieval-Stage_Defenses_Against_Corpus_Poisoning_in_Retrieval-Augmented_Generation"
          },
          {
            "title": "Advances LLM Security, RAGPart And RAGMask Mitigates Corpus Poisoning In Generation Pipelines",
            "url": "https://quantumzeitgeist.com/security-advances-llm-ragpart-ragmask-mitigates/"
          },
          {
            "title": "[2512.24268] RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2512.24268"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions",
            "url": "https://arxiv.org/html/2604.08304v1"
          },
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
          }
        ]
      },
      "Based on the search results, I found information about RAGPart and RAGMask:\n\nRAGPart and RAGMask are two complementary retrieval-stage defenses against corpus poisoning in Retrieval-Augmented Generation (RAG), where adversaries inject malicious documents into the retrieval corpus to manipulate model outputs.\n\nRAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points. RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.\n\nThese defenses operate directly on the retriever, making them computationally lightweight and requiring no modification to the generation model. Experiments show RAGPart can prevent poisoned documents from appearing among the top retrieved results.\n\nThe research was published in December 2025, with the arXiv preprint dated December 30, 2025 (arXiv:2512.24268)."
    ],
    "durationSeconds": 5.207993203999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1b789e3a-e6e8-4549-91d4-8fb931a52d21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 86_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "8a0487a3-ff22-4799-a5ea-a8b982984978",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Assistant

_source line 88 · 2026-05-30T06:53:55.470Z_

Now let me check for the most recent work that might be concurrent:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a0487a3-ff22-4799-a5ea-a8b982984978",
  "isSidechain": false,
  "requestId": "req_011CbYK96cWs1agvELynD13X",
  "type": "assistant",
  "uuid": "b9473a90-2679-48de-81bf-ba8451acc45d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAX4seg5gAsYWmFrBzupQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 42911,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 42911,
          "cache_creation_input_tokens": 725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 725
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

_source line 89 · 2026-05-30T06:53:55.805Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TXDVhH1tgamPPebK2h58Jx`</summary>

```json
{
  "query": "robust conformal prediction retrieval corruption test-time distribution shift certificate 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9473a90-2679-48de-81bf-ba8451acc45d",
  "isSidechain": false,
  "requestId": "req_011CbYK96cWs1agvELynD13X",
  "type": "assistant",
  "uuid": "2659728a-066e-4ee0-ac77-0c4cbb7ba917",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAX4seg5gAsYWmFrBzupQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 42911,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 42911,
          "cache_creation_input_tokens": 725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 725
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

_source line 90 · 2026-05-30T06:54:02.231Z_

<details><summary>↩ Tool result · `toolu_01TXDVhH1tgamPPebK2h58Jx`</summary>

```text
Web search results for query: "robust conformal prediction retrieval corruption test-time distribution shift certificate 2026"

Links: [{"title":"Robust Conformal Prediction Using Privileged Information","url":"https://arxiv.org/pdf/2406.05405"},{"title":"Conformal Prediction with Corrupted Labels: Uncertain Imputation and Robust Re-weighting | OpenReview","url":"https://openreview.net/forum?id=ztEKLEUNKS"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"[2406.05405] Robust Conformal Prediction Using Privileged Information","url":"https://arxiv.org/abs/2406.05405"},{"title":"Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model","url":"https://arxiv.org/pdf/2403.15025"},{"title":"ADVERSARIALLY ROBUST CONFORMAL PREDICTION","url":"https://openreview.net/pdf?id=9L1BsI4wP1H"},{"title":"Robust Conformal Prediction Using Privileged Information","url":"https://arxiv.org/html/2406.05405v1"},{"title":"Conformal Prediction with Corrupted Labels: Uncertain Imputation and Robust Re-weighting","url":"https://arxiv.org/html/2505.04733v1"}]

Based on the search results, here are the key findings related to robust conformal prediction with distribution shifts and corruption handling:

## Main Research Direction

Privileged conformal prediction (PCP) is a novel calibration technique that constructs provably valid uncertainty sets despite being employed with corrupted samples. The privileged information is formulated as additional features that explain the distribution shift and are only available during training and absent at test time.

## Handling Corruptions and Distribution Shift

The framework addresses robust uncertainty quantification in situations where labeled training data are corrupted through noisy or missing labels. Distribution shifts between training and test data break the coverage guarantee of traditional conformal prediction techniques.

## Recent Advances (2025-2026)

Recent work analyzes the robustness of PCP to inaccuracies in weights and introduces uncertain imputation (UI), a new conformal method that does not rely on weight estimation but instead imputes corrupted labels in a way that preserves their uncertainty.

These techniques can be integrated into a triply robust framework, ensuring statistically valid predictions as long as at least one underlying method is valid.

The research demonstrates that conformal prediction methods can provide valid prediction sets—with guaranteed coverage certificates—even when dealing with corrupted training data and test-time distribution shifts through privileged information and robust re-weighting approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2659728a-066e-4ee0-ac77-0c4cbb7ba917",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "e2fa518f-a2ce-474f-8761-ce5f2a2b4c18",
  "toolUseResult": {
    "query": "robust conformal prediction retrieval corruption test-time distribution shift certificate 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SqxA7Sy4MqyybPs27vQe2D",
        "content": [
          {
            "title": "Robust Conformal Prediction Using Privileged Information",
            "url": "https://arxiv.org/pdf/2406.05405"
          },
          {
            "title": "Conformal Prediction with Corrupted Labels: Uncertain Imputation and Robust Re-weighting | OpenReview",
            "url": "https://openreview.net/forum?id=ztEKLEUNKS"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "[2406.05405] Robust Conformal Prediction Using Privileged Information",
            "url": "https://arxiv.org/abs/2406.05405"
          },
          {
            "title": "Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/pdf/2403.15025"
          },
          {
            "title": "ADVERSARIALLY ROBUST CONFORMAL PREDICTION",
            "url": "https://openreview.net/pdf?id=9L1BsI4wP1H"
          },
          {
            "title": "Robust Conformal Prediction Using Privileged Information",
            "url": "https://arxiv.org/html/2406.05405v1"
          },
          {
            "title": "Conformal Prediction with Corrupted Labels: Uncertain Imputation and Robust Re-weighting",
            "url": "https://arxiv.org/html/2505.04733v1"
          }
        ]
      },
      "Based on the search results, here are the key findings related to robust conformal prediction with distribution shifts and corruption handling:\n\n## Main Research Direction\n\nPrivileged conformal prediction (PCP) is a novel calibration technique that constructs provably valid uncertainty sets despite being employed with corrupted samples. The privileged information is formulated as additional features that explain the distribution shift and are only available during training and absent at test time.\n\n## Handling Corruptions and Distribution Shift\n\nThe framework addresses robust uncertainty quantification in situations where labeled training data are corrupted through noisy or missing labels. Distribution shifts between training and test data break the coverage guarantee of traditional conformal prediction techniques.\n\n## Recent Advances (2025-2026)\n\nRecent work analyzes the robustness of PCP to inaccuracies in weights and introduces uncertain imputation (UI), a new conformal method that does not rely on weight estimation but instead imputes corrupted labels in a way that preserves their uncertainty.\n\nThese techniques can be integrated into a triply robust framework, ensuring statistically valid predictions as long as at least one underlying method is valid.\n\nThe research demonstrates that conformal prediction methods can provide valid prediction sets—with guaranteed coverage certificates—even when dealing with corrupted training data and test-time distribution shifts through privileged information and robust re-weighting approaches."
    ],
    "durationSeconds": 6.42004495000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2659728a-066e-4ee0-ac77-0c4cbb7ba917",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-30T06:54:06.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VuQC9Rv7Gv37XQnV9btfJH`</summary>

```json
{
  "query": "conformal prediction abstention selective prediction LLM question answering poisoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2fa518f-a2ce-474f-8761-ce5f2a2b4c18",
  "isSidechain": false,
  "requestId": "req_011CbYK9pQxz2X6xZW6XrDuW",
  "type": "assistant",
  "uuid": "04c7fce5-292b-4a6c-9ceb-a6316a284dba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9w6qhxSt8qJ6ykP4v54qn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 43636,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 43636,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 778
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

_source line 92 · 2026-05-30T06:54:13.416Z_

<details><summary>↩ Tool result · `toolu_01VuQC9Rv7Gv37XQnV9btfJH`</summary>

```text
Web search results for query: "conformal prediction abstention selective prediction LLM question answering poisoning 2026"

Links: [{"title":"[2601.12471] Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty","url":"https://arxiv.org/abs/2601.12471"},{"title":"(PDF) Conformal Prediction with Large Language Models for Multi-Choice Question Answering","url":"https://www.researchgate.net/publication/371163118_Conformal_Prediction_with_Large_Language_Models_for_Multi-Choice_Question_Answering"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/html/2604.27914"},{"title":"Conformal Prediction with Large Language Models for Multi-Choice Question Answering","url":"https://www.emergentmind.com/papers/2305.18404"},{"title":"Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty","url":"https://arxiv.org/pdf/2601.12471"},{"title":"Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty","url":"https://arxiv.org/html/2601.12471v2"},{"title":"Selective \"Selective Prediction\": Reducing Unnecessary Abstention in   Vision-Language Reasoning","url":"https://arxiv.org/pdf/2402.15610"}]

Based on the search results, here's what I found regarding your query on conformal prediction, abstention, selective prediction, LLM question answering, and poisoning in 2026:

## Recent Research (2026)

MedAbstain is a unified benchmark and evaluation protocol for abstention in medical multiple-choice question answering integrating conformal prediction, adversarial question perturbations, and explicit abstention options. Systematic evaluation of both open- and closed-source LLMs reveals that even state-of-the-art, high-accuracy models often fail to abstain when uncertain.

Conformal Abstention (CA) is an approach grounded in conformal prediction that enables LLMs to admit a lack of knowledge. CA establishes two theoretical finite-sample guarantees: a participation guarantee bounding the probability that the model participates and a conditional correctness guarantee bounding the probability that the provided answer is correct.

## Broader Context

Conformal prediction can be used to provide uncertainty quantification in LLMs for multiple-choice question-answering, with uncertainty estimates tightly correlated with prediction accuracy and useful for downstream applications such as selective classification and filtering out low-quality predictions.

Selective prediction systems aim to balance coverage and error rate by enabling systems to abstain when uncertain.

**Note:** The search results don't contain significant information specifically about "poisoning" attacks in this context. The results focus more on abstention mechanisms and uncertainty quantification in LLMs for question answering tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04c7fce5-292b-4a6c-9ceb-a6316a284dba",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "2115cdec-2a39-49a4-83ab-281b20eed57a",
  "toolUseResult": {
    "query": "conformal prediction abstention selective prediction LLM question answering poisoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01771uW5kZf92z5BE5UHmLM3",
        "content": [
          {
            "title": "[2601.12471] Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty",
            "url": "https://arxiv.org/abs/2601.12471"
          },
          {
            "title": "(PDF) Conformal Prediction with Large Language Models for Multi-Choice Question Answering",
            "url": "https://www.researchgate.net/publication/371163118_Conformal_Prediction_with_Large_Language_Models_for_Multi-Choice_Question_Answering"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          },
          {
            "title": "Geometry-Calibrated Conformal Abstention for Language Models",
            "url": "https://arxiv.org/html/2604.27914"
          },
          {
            "title": "Conformal Prediction with Large Language Models for Multi-Choice Question Answering",
            "url": "https://www.emergentmind.com/papers/2305.18404"
          },
          {
            "title": "Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty",
            "url": "https://arxiv.org/pdf/2601.12471"
          },
          {
            "title": "Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty",
            "url": "https://arxiv.org/html/2601.12471v2"
          },
          {
            "title": "Selective \"Selective Prediction\": Reducing Unnecessary Abstention in   Vision-Language Reasoning",
            "url": "https://arxiv.org/pdf/2402.15610"
          }
        ]
      },
      "Based on the search results, here's what I found regarding your query on conformal prediction, abstention, selective prediction, LLM question answering, and poisoning in 2026:\n\n## Recent Research (2026)\n\nMedAbstain is a unified benchmark and evaluation protocol for abstention in medical multiple-choice question answering integrating conformal prediction, adversarial question perturbations, and explicit abstention options. Systematic evaluation of both open- and closed-source LLMs reveals that even state-of-the-art, high-accuracy models often fail to abstain when uncertain.\n\nConformal Abstention (CA) is an approach grounded in conformal prediction that enables LLMs to admit a lack of knowledge. CA establishes two theoretical finite-sample guarantees: a participation guarantee bounding the probability that the model participates and a conditional correctness guarantee bounding the probability that the provided answer is correct.\n\n## Broader Context\n\nConformal prediction can be used to provide uncertainty quantification in LLMs for multiple-choice question-answering, with uncertainty estimates tightly correlated with prediction accuracy and useful for downstream applications such as selective classification and filtering out low-quality predictions.\n\nSelective prediction systems aim to balance coverage and error rate by enabling systems to abstain when uncertain.\n\n**Note:** The search results don't contain significant information specifically about \"poisoning\" attacks in this context. The results focus more on abstention mechanisms and uncertainty quantification in LLMs for question answering tasks."
    ],
    "durationSeconds": 7.0890769030000085,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "04c7fce5-292b-4a6c-9ceb-a6316a284dba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-30T06:54:16.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JZWDGbVxL2AwjXCCSfKMoW`</summary>

```json
{
  "query": "\"exchangeability\" \"retrieval\" \"conformal\" poisoning adversarial documents violation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2115cdec-2a39-49a4-83ab-281b20eed57a",
  "isSidechain": false,
  "requestId": "req_011CbYKAeDaNNir2Zv6zdxPf",
  "type": "assistant",
  "uuid": "fd0c119e-0a7f-4700-a4b5-dc1b2d62a105",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LK524oXLQ6LET2mPc4YBpv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 44414,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 44414,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 94 · 2026-05-30T06:54:23.149Z_

<details><summary>↩ Tool result · `toolu_01JZWDGbVxL2AwjXCCSfKMoW`</summary>

```text
Web search results for query: ""exchangeability" "retrieval" "conformal" poisoning adversarial documents violation 2025 2026"

Links: [{"title":"Controlled Generation of Natural Adversarial Documents for Stealthy Retrieval Poisoning | OpenReview","url":"https://openreview.net/forum?id=0rmOx0Ifbf"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"},{"title":"Introduction to Data Poisoning: A 2026 Perspective | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/training-data-poisoning"},{"title":"Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks","url":"https://arxiv.org/pdf/2501.16902"},{"title":"Poisoning Retrieval Corpora by Injecting Adversarial Passages","url":"https://arxiv.org/pdf/2310.19156"},{"title":"Awesome-LM-SSP/collection/paper/security/poison_&_backdoor.md at main · CryptoAILab/Awesome-LM-SSP","url":"https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/security/poison_&_backdoor.md"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/pdf/2511.18562"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"}]

The search has returned relevant results. Here's a summary of what was found:

## Search Results

The search found several recent academic papers and resources addressing the intersection of retrieval systems, poisoning attacks, conformal prediction, and adversarial robustness:

**Key Papers on Conformal Prediction Under Poisoning:**

A paper discusses reliability of conformal prediction sets in the presence of data poisoning and label flipping attacks, leveraging smoothed score functions and a majority voting mechanism called RPS, with theoretical guarantees that maintain stability under worst-case data poisoning.

Research on split conformal prediction addresses how exchangeability can be broken when the conformity-score distribution in the calibration set doesn't match test data due to distribution shift.

**Papers on Retrieval Poisoning Attacks:**

Recent work showed that retrieval based on embedding similarity (e.g., for retrieval-augmented generation) is vulnerable to poisoning, where adversaries can craft malicious documents that are retrieved in response to broad classes of queries.

In 2025, attacks have targeted retrieval-augmented generation (RAG), third-party tools (like MCP servers), and even synthetic data pipelines.

A 2025 paper titled "Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks" addresses vulnerabilities in document retrieval systems.

Research on corpus-dependent poisoning attacks in RAG systems notes that poisoned documents persist across future queries and must avoid detection, with vector and embedding weaknesses recognized as a top-10 risk in the OWASP LLM Top 10 (2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd0c119e-0a7f-4700-a4b5-dc1b2d62a105",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "cb363552-f960-486c-9829-6dcb4af72f11",
  "toolUseResult": {
    "query": "\"exchangeability\" \"retrieval\" \"conformal\" poisoning adversarial documents violation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Azp9DCkosNRm7Kxfn6SxSc",
        "content": [
          {
            "title": "Controlled Generation of Natural Adversarial Documents for Stealthy Retrieval Poisoning | OpenReview",
            "url": "https://openreview.net/forum?id=0rmOx0Ifbf"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          },
          {
            "title": "Introduction to Data Poisoning: A 2026 Perspective | Lakera – Protecting AI teams that disrupt the world.",
            "url": "https://www.lakera.ai/blog/training-data-poisoning"
          },
          {
            "title": "Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2501.16902"
          },
          {
            "title": "Poisoning Retrieval Corpora by Injecting Adversarial Passages",
            "url": "https://arxiv.org/pdf/2310.19156"
          },
          {
            "title": "Awesome-LM-SSP/collection/paper/security/poison_&_backdoor.md at main · CryptoAILab/Awesome-LM-SSP",
            "url": "https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/security/poison_&_backdoor.md"
          },
          {
            "title": "Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks",
            "url": "https://arxiv.org/pdf/2511.18562"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/pdf/2603.18034"
          }
        ]
      },
      "The search has returned relevant results. Here's a summary of what was found:\n\n## Search Results\n\nThe search found several recent academic papers and resources addressing the intersection of retrieval systems, poisoning attacks, conformal prediction, and adversarial robustness:\n\n**Key Papers on Conformal Prediction Under Poisoning:**\n\nA paper discusses reliability of conformal prediction sets in the presence of data poisoning and label flipping attacks, leveraging smoothed score functions and a majority voting mechanism called RPS, with theoretical guarantees that maintain stability under worst-case data poisoning.\n\nResearch on split conformal prediction addresses how exchangeability can be broken when the conformity-score distribution in the calibration set doesn't match test data due to distribution shift.\n\n**Papers on Retrieval Poisoning Attacks:**\n\nRecent work showed that retrieval based on embedding similarity (e.g., for retrieval-augmented generation) is vulnerable to poisoning, where adversaries can craft malicious documents that are retrieved in response to broad classes of queries.\n\nIn 2025, attacks have targeted retrieval-augmented generation (RAG), third-party tools (like MCP servers), and even synthetic data pipelines.\n\nA 2025 paper titled \"Document Screenshot Retrievers are Vulnerable to Pixel Poisoning Attacks\" addresses vulnerabilities in document retrieval systems.\n\nResearch on corpus-dependent poisoning attacks in RAG systems notes that poisoned documents persist across future queries and must avoid detection, with vector and embedding weaknesses recognized as a top-10 risk in the OWASP LLM Top 10 (2025)."
    ],
    "durationSeconds": 6.987963962000038,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fd0c119e-0a7f-4700-a4b5-dc1b2d62a105",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-30T06:54:25.787Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HzX8fPiRJjVryFACVHAkTS`</summary>

```json
{
  "query": "benchmarking poisoning attacks retrieval augmented generation defense evaluation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb363552-f960-486c-9829-6dcb4af72f11",
  "isSidechain": false,
  "requestId": "req_011CbYKBMo8qwhamcuASDQ7y",
  "type": "assistant",
  "uuid": "0d11ffd1-e49e-4042-8d70-4bc136b1fd9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Yc2j8og7HwLyr1NNbhyzQc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 45222,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 45222,
          "cache_creation_input_tokens": 983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 983
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

_source line 96 · 2026-05-30T06:54:33.735Z_

<details><summary>↩ Tool result · `toolu_01HzX8fPiRJjVryFACVHAkTS`</summary>

```text
Web search results for query: "benchmarking poisoning attacks retrieval augmented generation defense evaluation 2025"

Links: [{"title":"[2505.18543] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.18543"},{"title":"(PDF) Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://www.researchgate.net/publication/392105526_Benchmarking_Poisoning_Attacks_against_Retrieval-Augmented_Generation"},{"title":"[PDF] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Benchmarking-Poisoning-Attacks-against-Generation-Zhang-Xin/ccf24f7db7680562628545beaa26fca9d3745e1e"},{"title":"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.18543"},{"title":"Secure Retrieval-Augmented Generation against Poisoning Attacks","url":"https://arxiv.org/html/2510.25025v1"},{"title":"[2508.02835] Defending Against Knowledge Poisoning Attacks During Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2508.02835"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.698/"}]

Based on the search results, here's what I found on this topic:

## Key Research on Benchmarking Poisoning Attacks Against RAG

Retrieval-Augmented Generation (RAG) has proven effective in mitigating hallucinations in large language models by incorporating external knowledge during inference, but this integration introduces new security vulnerabilities, particularly to poisoning attacks.

### Benchmark Framework

The RSB (RAG Security Benchmark) includes 13 representative poisoning attacks, classified into three categories based on their adversarial objectives: targeted poisoning, denial-of-service (DoS), and trigger-based DoS. On the defense side, RSB incorporates 7 representative methods, organized into three categories.

### Key Findings

While existing attacks perform well on standard QA datasets, their effectiveness drops significantly on the expanded versions. Various advanced RAG architectures, such as sequential, branching, conditional, and loop RAG, as well as multi-turn conversational RAG, multimodal RAG systems, and RAG-based LLM agent systems, remain susceptible to poisoning attacks.

### Defense Limitations

Current defense techniques fail to provide robust protection, underscoring the pressing need for more resilient and generalizable defense strategies.

### Multi-turn RAG Vulnerabilities

Results show reduced attack effectiveness in the multi-turn setting, with query rewriting altering the retrieval and hindering the retrieval of poisoned texts crafted for original queries.

This research was published in May 2025 by Zhang and colleagues on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d11ffd1-e49e-4042-8d70-4bc136b1fd9b",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "1953b06f-bea3-4e44-9c1c-4851da274a6d",
  "toolUseResult": {
    "query": "benchmarking poisoning attacks retrieval augmented generation defense evaluation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NibEbJqA1MGhPscZRTje9X",
        "content": [
          {
            "title": "[2505.18543] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2505.18543"
          },
          {
            "title": "(PDF) Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://www.researchgate.net/publication/392105526_Benchmarking_Poisoning_Attacks_against_Retrieval-Augmented_Generation"
          },
          {
            "title": "[PDF] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Benchmarking-Poisoning-Attacks-against-Generation-Zhang-Xin/ccf24f7db7680562628545beaa26fca9d3745e1e"
          },
          {
            "title": "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.18543"
          },
          {
            "title": "Secure Retrieval-Augmented Generation against Poisoning Attacks",
            "url": "https://arxiv.org/html/2510.25025v1"
          },
          {
            "title": "[2508.02835] Defending Against Knowledge Poisoning Attacks During Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2508.02835"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-emnlp.698/"
          }
        ]
      },
      "Based on the search results, here's what I found on this topic:\n\n## Key Research on Benchmarking Poisoning Attacks Against RAG\n\nRetrieval-Augmented Generation (RAG) has proven effective in mitigating hallucinations in large language models by incorporating external knowledge during inference, but this integration introduces new security vulnerabilities, particularly to poisoning attacks.\n\n### Benchmark Framework\n\nThe RSB (RAG Security Benchmark) includes 13 representative poisoning attacks, classified into three categories based on their adversarial objectives: targeted poisoning, denial-of-service (DoS), and trigger-based DoS. On the defense side, RSB incorporates 7 representative methods, organized into three categories.\n\n### Key Findings\n\nWhile existing attacks perform well on standard QA datasets, their effectiveness drops significantly on the expanded versions. Various advanced RAG architectures, such as sequential, branching, conditional, and loop RAG, as well as multi-turn conversational RAG, multimodal RAG systems, and RAG-based LLM agent systems, remain susceptible to poisoning attacks.\n\n### Defense Limitations\n\nCurrent defense techniques fail to provide robust protection, underscoring the pressing need for more resilient and generalizable defense strategies.\n\n### Multi-turn RAG Vulnerabilities\n\nResults show reduced attack effectiveness in the multi-turn setting, with query rewriting altering the retrieval and hindering the retrieval of poisoned texts crafted for original queries.\n\nThis research was published in May 2025 by Zhang and colleagues on arXiv."
    ],
    "durationSeconds": 7.943296111000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0d11ffd1-e49e-4042-8d70-4bc136b1fd9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 97_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "1953b06f-bea3-4e44-9c1c-4851da274a6d",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 98_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool call

_source line 99 · 2026-05-30T06:54:40.951Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019ZoPXNinpvCRVMnPThjD5N`</summary>

```json
{
  "query": "\"Cherian\" conformal factuality group-conditional level-adaptive LLM NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1953b06f-bea3-4e44-9c1c-4851da274a6d",
  "isSidechain": false,
  "requestId": "req_011CbYKC9KZqPqFrAjceyix2",
  "type": "assistant",
  "uuid": "97d191ba-0da6-47c1-8b5f-e462a9d69262",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVbdoVB3rpSuqhMYZDFUsa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 46205,
      "output_tokens": 76,
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
          "output_tokens": 76,
          "cache_read_input_tokens": 46205,
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

_source line 100 · 2026-05-30T06:54:47.503Z_

<details><summary>↩ Tool result · `toolu_019ZoPXNinpvCRVMnPThjD5N`</summary>

```text
Web search results for query: ""Cherian" conformal factuality group-conditional level-adaptive LLM NeurIPS 2024"

Links: [{"title":"[Quick Review] Large language model validity via enhanced conformal prediction methods","url":"https://liner.com/review/large-language-model-validity-via-enhanced-conformal-prediction-methods"},{"title":"LLM validity via enhanced conformal prediction: conditional","url":"https://bsmachinelearning.com/assets/reports/llm_validity_paper.pdf"},{"title":"Multi-LLM Adaptive Conformal Inference for Reliable LLM Responses","url":"https://arxiv.org/html/2602.01285"},{"title":"Conformal Language Model Reasoning with Coherent Factuality","url":"https://arxiv.org/html/2505.17126v1"},{"title":"(PDF) Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://www.researchgate.net/publication/403868268_Adaptive_Conformal_Prediction_for_Improving_Factuality_of_Generations_by_Large_Language_Models"},{"title":"LLM Validity via Enhanced Conformal Prediction: Conditional Guarantees, Score Learning, and Response-Level Calibration Under Dependent Claims","url":"https://bsmachinelearning.com/projects/llm-validity/"},{"title":"Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://arxiv.org/html/2604.13991"},{"title":"Multi-LLM Adaptive Conformal Inference for Reliable LLM Responses","url":"https://arxiv.org/pdf/2602.01285"},{"title":"Large language model validity via enhanced conformal prediction methods","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf"}]

Based on the search results, I found information about the Cherian et al. NeurIPS 2024 paper you're asking about.

John J. Cherian and colleagues presented a NeurIPS 2024 paper on new conformal inference techniques for LLMs, improving claim retention and conditional validity.

The paper proposes enhanced conformal methods for factuality filtering that replace marginal guarantees with function-class conditional guarantees and improve utility via level-adaptive calibration and conditional boosting that differentiates through conditional conformal cutoffs.

More specifically, existing conformal language modeling methods filter LLM claims but lack conditional validity, meaning their trustworthiness varies by topic. To address this, the Cherian et al. work introduces conditional conformal inference, which instead of a single static threshold for all data, employs a threshold function that allows it to change based on the characteristics of a given sample.

The work addresses the key limitation that current methods excessively remove accurate and valuable claims due to imperfect scoring functions, reducing output utility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97d191ba-0da6-47c1-8b5f-e462a9d69262",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "782bcb5b-0eb5-4ec7-b7d8-b75d56b479ff",
  "toolUseResult": {
    "query": "\"Cherian\" conformal factuality group-conditional level-adaptive LLM NeurIPS 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_014nrgg6KbhPg4szptZkE4rG",
        "content": [
          {
            "title": "[Quick Review] Large language model validity via enhanced conformal prediction methods",
            "url": "https://liner.com/review/large-language-model-validity-via-enhanced-conformal-prediction-methods"
          },
          {
            "title": "LLM validity via enhanced conformal prediction: conditional",
            "url": "https://bsmachinelearning.com/assets/reports/llm_validity_paper.pdf"
          },
          {
            "title": "Multi-LLM Adaptive Conformal Inference for Reliable LLM Responses",
            "url": "https://arxiv.org/html/2602.01285"
          },
          {
            "title": "Conformal Language Model Reasoning with Coherent Factuality",
            "url": "https://arxiv.org/html/2505.17126v1"
          },
          {
            "title": "(PDF) Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models",
            "url": "https://www.researchgate.net/publication/403868268_Adaptive_Conformal_Prediction_for_Improving_Factuality_of_Generations_by_Large_Language_Models"
          },
          {
            "title": "LLM Validity via Enhanced Conformal Prediction: Conditional Guarantees, Score Learning, and Response-Level Calibration Under Dependent Claims",
            "url": "https://bsmachinelearning.com/projects/llm-validity/"
          },
          {
            "title": "Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models",
            "url": "https://arxiv.org/html/2604.13991"
          },
          {
            "title": "Multi-LLM Adaptive Conformal Inference for Reliable LLM Responses",
            "url": "https://arxiv.org/pdf/2602.01285"
          },
          {
            "title": "Large language model validity via enhanced conformal prediction methods",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the Cherian et al. NeurIPS 2024 paper you're asking about.\n\nJohn J. Cherian and colleagues presented a NeurIPS 2024 paper on new conformal inference techniques for LLMs, improving claim retention and conditional validity.\n\nThe paper proposes enhanced conformal methods for factuality filtering that replace marginal guarantees with function-class conditional guarantees and improve utility via level-adaptive calibration and conditional boosting that differentiates through conditional conformal cutoffs.\n\nMore specifically, existing conformal language modeling methods filter LLM claims but lack conditional validity, meaning their trustworthiness varies by topic. To address this, the Cherian et al. work introduces conditional conformal inference, which instead of a single static threshold for all data, employs a threshold function that allows it to change based on the characteristics of a given sample.\n\nThe work addresses the key limitation that current methods excessively remove accurate and valuable claims due to imperfect scoring functions, reducing output utility."
    ],
    "durationSeconds": 6.545811900999979,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "97d191ba-0da6-47c1-8b5f-e462a9d69262",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-30T06:54:50.048Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U3HE1UW2qUZsYWzRmTam6h`</summary>

```json
{
  "query": "AAAI 2027 submission deadline call for papers safe robust AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "782bcb5b-0eb5-4ec7-b7d8-b75d56b479ff",
  "isSidechain": false,
  "requestId": "req_011CbYKD9wJu79hcKoRQPtof",
  "type": "assistant",
  "uuid": "448fdaf6-1641-414a-9465-2e6c5db583af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8KEkddRYh3aRAeZ3nQ9AV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 47118,
      "output_tokens": 67,
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
          "output_tokens": 67,
          "cache_read_input_tokens": 47118,
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

_source line 102 · 2026-05-30T06:54:55.971Z_

<details><summary>↩ Tool result · `toolu_01U3HE1UW2qUZsYWzRmTam6h`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline call for papers safe robust AI"

Links: [{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AI Maintenance: A Robustness Perspective","url":"https://arxiv.org/pdf/2301.03052"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Position: AI Safety Must Embrace an Antifragile Perspective","url":"https://arxiv.org/pdf/2509.13339"},{"title":"Robust AI Security and Alignment: A Sisyphean Endeavor?","url":"https://arxiv.org/pdf/2512.10100"}]

Based on the search results, here's what I found regarding AAAI 2027:

## AAAI 2027 Conference Details

The AAAI 2027 conference will be held in Montréal, Québec, Canada on February 16-23, 2027.

## Submission Deadlines

Unfortunately, the submission deadline for AAAI 2027 has not yet been announced (TBD). However, the Open Review submission site is scheduled to open for author registration on June 17, 2026, with all deadlines being "anywhere on earth" (UTC-12).

The search results also show that historically, a mandatory abstract deadline typically comes 1 week before the paper deadline, though specific dates for AAAI 2027 have not yet been published.

For the most current information and exact submission deadlines, I recommend checking the official AAAI 2027 website directly, as the specific dates are still being finalized.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "448fdaf6-1641-414a-9465-2e6c5db583af",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "6b7cd1f6-a3f1-4e26-baec-12badb7a6892",
  "toolUseResult": {
    "query": "AAAI 2027 submission deadline call for papers safe robust AI",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Mf1eTcsgtJhBPF8nQbgkZM",
        "content": [
          {
            "title": "AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot",
            "url": "https://www.getpaperpilot.com/deadlines/aaai-2027.html"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          },
          {
            "title": "AAAI-27 Main Technical Track - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"
          },
          {
            "title": "AI Maintenance: A Robustness Perspective",
            "url": "https://arxiv.org/pdf/2301.03052"
          },
          {
            "title": "AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Position: AI Safety Must Embrace an Antifragile Perspective",
            "url": "https://arxiv.org/pdf/2509.13339"
          },
          {
            "title": "Robust AI Security and Alignment: A Sisyphean Endeavor?",
            "url": "https://arxiv.org/pdf/2512.10100"
          }
        ]
      },
      "Based on the search results, here's what I found regarding AAAI 2027:\n\n## AAAI 2027 Conference Details\n\nThe AAAI 2027 conference will be held in Montréal, Québec, Canada on February 16-23, 2027.\n\n## Submission Deadlines\n\nUnfortunately, the submission deadline for AAAI 2027 has not yet been announced (TBD). However, the Open Review submission site is scheduled to open for author registration on June 17, 2026, with all deadlines being \"anywhere on earth\" (UTC-12).\n\nThe search results also show that historically, a mandatory abstract deadline typically comes 1 week before the paper deadline, though specific dates for AAAI 2027 have not yet been published.\n\nFor the most current information and exact submission deadlines, I recommend checking the official AAAI 2027 website directly, as the specific dates are still being finalized."
    ],
    "durationSeconds": 5.91822089700005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "448fdaf6-1641-414a-9465-2e6c5db583af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 103 · 2026-05-30T06:55:00.913Z_

<details><summary>Logged reasoning block</summary>

```text
So the AAAI 2027 deadline hasn't been announced yet but the submission site opens June 17, 2026. The user said "AAAI 2026 submission deadline: August 2026" - this likely means AAAI-27 (the conference happening in Feb 2027) with submission deadline around August 2026. That makes sense. Let me verify.

Let me now check the official AAAI-27 page for more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b7cd1f6-a3f1-4e26-baec-12badb7a6892",
  "isSidechain": false,
  "requestId": "req_011CbYKDn7Ashm6kPUC6h6hd",
  "type": "assistant",
  "uuid": "613455eb-2bd0-4677-8423-42724d9ab665",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8Ehvy7316of8ecBxmpuFw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 47936,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 47936,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 104 · 2026-05-30T06:55:02.495Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ad6TvFhZ8nzAS4gSTFXZ1u`</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/",
  "prompt": "Extract the submission deadlines, special tracks, and whether there is a Safe Robust Responsible AI (SRRAI) track. What are the exact paper submission dates?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "613455eb-2bd0-4677-8423-42724d9ab665",
  "isSidechain": false,
  "requestId": "req_011CbYKDn7Ashm6kPUC6h6hd",
  "type": "assistant",
  "uuid": "1e42bb29-9ebf-4573-b8be-2fcb71b43db1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8Ehvy7316of8ecBxmpuFw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 47936,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 47936,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 105 · 2026-05-30T06:55:06.993Z_

<details><summary>↩ Tool result · `toolu_01Ad6TvFhZ8nzAS4gSTFXZ1u`</summary>

```text
# AAAI-27 Submission Deadlines and Tracks

## Paper Submission Dates

The exact submission timeline for the Main Technical Track is:

- **June 24, 2026**: "Open Review submission site opens for paper submission"
- **July 21, 2026**: "Abstracts due at 11:59 PM UTC-12"
- **July 28, 2026**: "Full papers due at 11:59 PM UTC-12"
- **July 31, 2026**: "Supplementary material and code due by 11:59 PM UTC-12"

## Special Tracks

The webpage mentions "EAAI-27" as an associated track alongside the main conference, with its own call for papers. However, the main technical track details state: "Coming Soon," so specific information about specialized tracks is not currently available.

## SRRAI Track

**No Safe Robust Responsible AI (SRRAI) track is mentioned** in the provided content. The page does not list this as a special track for AAAI-27.

**Note**: The page indicates "Deadlines are track-specific and may differ from those listed above," suggesting additional tracks exist with their own timelines on separate call-for-papers pages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e42bb29-9ebf-4573-b8be-2fcb71b43db1",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "d4a814f4-447a-4883-877c-26bab7c33c87",
  "toolUseResult": {
    "bytes": 189767,
    "code": 200,
    "codeText": "OK",
    "result": "# AAAI-27 Submission Deadlines and Tracks\n\n## Paper Submission Dates\n\nThe exact submission timeline for the Main Technical Track is:\n\n- **June 24, 2026**: \"Open Review submission site opens for paper submission\"\n- **July 21, 2026**: \"Abstracts due at 11:59 PM UTC-12\"\n- **July 28, 2026**: \"Full papers due at 11:59 PM UTC-12\"\n- **July 31, 2026**: \"Supplementary material and code due by 11:59 PM UTC-12\"\n\n## Special Tracks\n\nThe webpage mentions \"EAAI-27\" as an associated track alongside the main conference, with its own call for papers. However, the main technical track details state: \"Coming Soon,\" so specific information about specialized tracks is not currently available.\n\n## SRRAI Track\n\n**No Safe Robust Responsible AI (SRRAI) track is mentioned** in the provided content. The page does not list this as a special track for AAAI-27.\n\n**Note**: The page indicates \"Deadlines are track-specific and may differ from those listed above,\" suggesting additional tracks exist with their own timelines on separate call-for-papers pages.",
    "durationMs": 4495,
    "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"
  },
  "sourceToolAssistantUUID": "1e42bb29-9ebf-4573-b8be-2fcb71b43db1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 106 · 2026-05-30T06:55:06.995Z_

```json
{
  "parentUuid": "d4a814f4-447a-4883-877c-26bab7c33c87",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "42de641c-0047-4cce-bbf4-c2aa47cecc13",
  "timestamp": "2026-05-30T06:55:06.995Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 107 · 2026-05-30T06:55:12.289Z_

<details><summary>Logged reasoning block</summary>

```text
Good. So the AAAI-27 main track deadline is July 28, 2026. The user mentioned "August 2026" which is close to this. The user may have been slightly off, or they may have been thinking of an earlier iteration. Either way, the deadline is July 28, 2026, which is about 2 months from now (current date: May 30, 2026). This is very feasible.

Now let me do a few more crucial searches to check for recent concurrent work and to verify the gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42de641c-0047-4cce-bbf4-c2aa47cecc13",
  "isSidechain": false,
  "requestId": "req_011CbYKEbHKpTdFEXdszHBaL",
  "type": "assistant",
  "uuid": "3a54b131-8a79-4427-b021-fc940c9f5d27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2ddx8AXszwJKbnPoPBpSz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 48612,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 48612,
          "cache_creation_input_tokens": 645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 645
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

_source line 108 · 2026-05-30T06:55:13.231Z_

Good — the AAAI-27 deadline is July 28, 2026 (about 2 months away). Let me now do a few more critical searches:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a54b131-8a79-4427-b021-fc940c9f5d27",
  "isSidechain": false,
  "requestId": "req_011CbYKEbHKpTdFEXdszHBaL",
  "type": "assistant",
  "uuid": "fb578913-923b-4ea5-b4bb-5b5021ff54ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2ddx8AXszwJKbnPoPBpSz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 48612,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 48612,
          "cache_creation_input_tokens": 645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 645
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

_source line 109 · 2026-05-30T06:55:13.677Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JMfWavRsuzGjMbEtoz2SmT`</summary>

```json
{
  "query": "partition vote conformal prediction retrieval augmented generation robust abstention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb578913-923b-4ea5-b4bb-5b5021ff54ba",
  "isSidechain": false,
  "requestId": "req_011CbYKEbHKpTdFEXdszHBaL",
  "type": "assistant",
  "uuid": "7b7137e2-82d8-4744-bb0e-2b8ed96081dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2ddx8AXszwJKbnPoPBpSz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 48612,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 48612,
          "cache_creation_input_tokens": 645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 645
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

_source line 110 · 2026-05-30T06:55:20.616Z_

<details><summary>↩ Tool result · `toolu_01JMfWavRsuzGjMbEtoz2SmT`</summary>

```text
Web search results for query: "partition vote conformal prediction retrieval augmented generation robust abstention 2025 2026"

Links: [{"title":"Deeper insights into retrieval augmented generation: The role of sufficient context","url":"https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/pdf/2511.17908"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"Adaptive Uncertainty Quantification for Generative AI","url":"https://arxiv.org/pdf/2408.08990"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models","url":"https://arxiv.org/pdf/2502.06884"},{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/pdf/2503.05239"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=675&show=1000"}]

Based on the search results, here are findings related to your query about partition vote, conformal prediction, retrieval augmented generation, and robust abstention in 2025-2026:

## Conformal Prediction for RAG Systems

A recent paper on "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction" addresses how Retrieval-Augmented Generation enhances factual grounding in LLMs by incorporating retrieved evidence, but LLM accuracy declines when long or noisy contexts exceed the model's effective attention span.

## RAG and Abstention

While RAG generally improves overall performance, it paradoxically reduces the model's ability to abstain from answering when appropriate. A paper titled "Sufficient Context: A New Lens on Retrieval Augmented Generation Systems" appeared at ICLR 2025 and shows it's possible to know when an LLM has enough information to provide a correct answer, studying the role context plays in factual accuracy.

## Learnable Conformal Abstention

A recent approach proposes learnable conformal abstention, integrating reinforcement learning with conformal prediction to optimize abstention thresholds dynamically, balancing multiple objectives like minimizing prediction set size while maintaining reliable coverage.

## Robust Conformal Prediction

Robust conformal prediction extends guarantees to worst-case inputs within a maximum radius around the clean point. Recent robust conformal prediction baselines use a conservative score at test time that is a certified bound on the conformity score of the clean unseen input.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b7137e2-82d8-4744-bb0e-2b8ed96081dd",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "a9055095-6932-4fa9-b669-a3ff54c5e9f8",
  "toolUseResult": {
    "query": "partition vote conformal prediction retrieval augmented generation robust abstention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GxVCoEWEcg7qaaWHAkMq8r",
        "content": [
          {
            "title": "Deeper insights into retrieval augmented generation: The role of sufficient context",
            "url": "https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/pdf/2511.17908"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          },
          {
            "title": "Adaptive Uncertainty Quantification for Generative AI",
            "url": "https://arxiv.org/pdf/2408.08990"
          },
          {
            "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models",
            "url": "https://arxiv.org/pdf/2502.06884"
          },
          {
            "title": "Robust Conformal Prediction with a Single Binary Certificate",
            "url": "https://arxiv.org/pdf/2503.05239"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-07?skip=675&show=1000"
          }
        ]
      },
      "Based on the search results, here are findings related to your query about partition vote, conformal prediction, retrieval augmented generation, and robust abstention in 2025-2026:\n\n## Conformal Prediction for RAG Systems\n\nA recent paper on \"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction\" addresses how Retrieval-Augmented Generation enhances factual grounding in LLMs by incorporating retrieved evidence, but LLM accuracy declines when long or noisy contexts exceed the model's effective attention span.\n\n## RAG and Abstention\n\nWhile RAG generally improves overall performance, it paradoxically reduces the model's ability to abstain from answering when appropriate. A paper titled \"Sufficient Context: A New Lens on Retrieval Augmented Generation Systems\" appeared at ICLR 2025 and shows it's possible to know when an LLM has enough information to provide a correct answer, studying the role context plays in factual accuracy.\n\n## Learnable Conformal Abstention\n\nA recent approach proposes learnable conformal abstention, integrating reinforcement learning with conformal prediction to optimize abstention thresholds dynamically, balancing multiple objectives like minimizing prediction set size while maintaining reliable coverage.\n\n## Robust Conformal Prediction\n\nRobust conformal prediction extends guarantees to worst-case inputs within a maximum radius around the clean point. Recent robust conformal prediction baselines use a conservative score at test time that is a certified bound on the conformity score of the clean unseen input."
    ],
    "durationSeconds": 6.935886345999956,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7b7137e2-82d8-4744-bb0e-2b8ed96081dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-30T06:55:23.402Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AWTGSfxRzM99jkESshyvf8`</summary>

```json
{
  "query": "\"principled context engineering\" RAG conformal prediction 2511.17908"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9055095-6932-4fa9-b669-a3ff54c5e9f8",
  "isSidechain": false,
  "requestId": "req_011CbYKFbYjAPuayiimCqNGL",
  "type": "assistant",
  "uuid": "e50147f8-c948-4110-8a0f-65f4d1770a88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvNuTfHqTEg3MKEeVsWskf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 49257,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 49257,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 937
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

_source line 112_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "e50147f8-c948-4110-8a0f-65f4d1770a88",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 113_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool result

_source line 114 · 2026-05-30T06:55:29.344Z_

<details><summary>↩ Tool result · `toolu_01AWTGSfxRzM99jkESshyvf8`</summary>

```text
Web search results for query: ""principled context engineering" RAG conformal prediction 2511.17908"

Links: [{"title":"[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/abs/2511.17908"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.17908"},{"title":"Principled Context Engineering for RAG:","url":"https://www.arxiv.org/pdf/2511.17908"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/html/2511.17908"},{"title":"(PDF) Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://www.researchgate.net/publication/397932907_Principled_Context_Engineering_for_RAG_Statistical_Guarantees_via_Conformal_Prediction"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"Sumit on X: \"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction Introduces conformal prediction for RAG systems to filter irrelevant context while preserving relevant evidence with statistical guarantees. 📝https://t.co/c9smN7mpfb\" / X","url":"https://x.com/_reachsumit/status/1993215931875782805"}]

The search results show information about the paper "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction" (arXiv:2511.17908).

## Summary

This paper addresses how Retrieval-Augmented Generation (RAG) enhances factual grounding in large language models by incorporating retrieved evidence, but LLM accuracy declines when long or noisy contexts exceed the model's effective attention span.

Existing pre-generation filters rely on heuristics or uncalibrated LLM confidence scores, offering no statistical control over retained evidence.

**The Proposed Solution:**

The authors evaluate and demonstrate context engineering through conformal prediction, a coverage-controlled filtering framework that removes irrelevant content while preserving recall of supporting evidence.

**Results and Contributions:**

Using both embedding- and LLM-based scoring functions, they tested this approach on the NeuCLIR and RAGTIME collections. Conformal filtering consistently meets its target coverage, ensuring that a specified fraction of relevant snippets are retained, and reduces retained context by 2-3x relative to unfiltered retrieval.

The results show that conformal prediction enables reliable, coverage-controlled context reduction, establishing it as a lightweight, model-agnostic foundation for principled context engineering in RAG.

The paper was submitted on November 22, 2025, and published as part of ECIR 2026 by authors Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, and Kevin Duh.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e50147f8-c948-4110-8a0f-65f4d1770a88",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "82069932-433f-4846-945d-388ea88244e8",
  "toolUseResult": {
    "query": "\"principled context engineering\" RAG conformal prediction 2511.17908",
    "results": [
      {
        "tool_use_id": "srvtoolu_017CyttF2RQeoXUkZwVCuD7a",
        "content": [
          {
            "title": "[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/abs/2511.17908"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2511.17908"
          },
          {
            "title": "Principled Context Engineering for RAG:",
            "url": "https://www.arxiv.org/pdf/2511.17908"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/html/2511.17908"
          },
          {
            "title": "(PDF) Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://www.researchgate.net/publication/397932907_Principled_Context_Engineering_for_RAG_Statistical_Guarantees_via_Conformal_Prediction"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"
          },
          {
            "title": "Sumit on X: \"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction Introduces conformal prediction for RAG systems to filter irrelevant context while preserving relevant evidence with statistical guarantees. 📝https://t.co/c9smN7mpfb\" / X",
            "url": "https://x.com/_reachsumit/status/1993215931875782805"
          }
        ]
      },
      "The search results show information about the paper \"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction\" (arXiv:2511.17908).\n\n## Summary\n\nThis paper addresses how Retrieval-Augmented Generation (RAG) enhances factual grounding in large language models by incorporating retrieved evidence, but LLM accuracy declines when long or noisy contexts exceed the model's effective attention span.\n\nExisting pre-generation filters rely on heuristics or uncalibrated LLM confidence scores, offering no statistical control over retained evidence.\n\n**The Proposed Solution:**\n\nThe authors evaluate and demonstrate context engineering through conformal prediction, a coverage-controlled filtering framework that removes irrelevant content while preserving recall of supporting evidence.\n\n**Results and Contributions:**\n\nUsing both embedding- and LLM-based scoring functions, they tested this approach on the NeuCLIR and RAGTIME collections. Conformal filtering consistently meets its target coverage, ensuring that a specified fraction of relevant snippets are retained, and reduces retained context by 2-3x relative to unfiltered retrieval.\n\nThe results show that conformal prediction enables reliable, coverage-controlled context reduction, establishing it as a lightweight, model-agnostic foundation for principled context engineering in RAG.\n\nThe paper was submitted on November 22, 2025, and published as part of ECIR 2026 by authors Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, and Kevin Duh."
    ],
    "durationSeconds": 5.937847177000018,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e50147f8-c948-4110-8a0f-65f4d1770a88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-30T06:55:33.520Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N4qmXgFKChx5W9n9DNmdsv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.17908",
  "prompt": "Extract the full abstract. Does this paper address adversarial corpus poisoning? Does it provide robustness guarantees against poisoning attacks? What are the main limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82069932-433f-4846-945d-388ea88244e8",
  "isSidechain": false,
  "requestId": "req_011CbYKGEo6Bkoue1qdQ58uu",
  "type": "assistant",
  "uuid": "3f6baab1-03d9-4eac-bfac-dca9d28831e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTdu7XN1KcHqhgFxskS2Pr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 50194,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 50194,
          "cache_creation_input_tokens": 869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 869
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

_source line 116 · 2026-05-30T06:55:41.207Z_

<details><summary>↩ Tool result · `toolu_01N4qmXgFKChx5W9n9DNmdsv`</summary>

```text
# Analysis of arXiv:2511.17908

## Full Abstract

"Retrieval-Augmented Generation (RAG) enhances factual grounding in large language models (LLMs) by incorporating retrieved evidence, but LLM accuracy declines when long or noisy contexts exceed the model's effective attention span. Existing pre-generation filters rely on heuristics or uncalibrated LLM confidence scores, offering no statistical control over retained evidence. We evaluate and demonstrate context engineering through conformal prediction, a coverage-controlled filtering framework that removes irrelevant content while preserving recall of supporting evidence. Using both embedding- and LLM-based scoring functions, we test this approach on the NeuCLIR and RAGTIME collections. Conformal filtering consistently meets its target coverage, ensuring that a specified fraction of relevant snippets are retained, and reduces retained context by 2-3x relative to unfiltered retrieval. On NeuCLIR, downstream factual accuracy measured by ARGUE F1 improves under strict filtering and remains stable at moderate coverage, indicating that most discarded material is redundant or irrelevant. These results demonstrate that conformal prediction enables reliable, coverage-controlled context reduction in RAG, offering a model-agnostic and principled approach to context engineering."

## Adversarial Robustness Assessment

**Does it address adversarial corpus poisoning?** No. The paper does not discuss intentional attacks or poisoning of retrieval corpora.

**Does it provide robustness guarantees against poisoning?** No robustness guarantees against poisoning attacks are mentioned or provided.

## Main Limitations

The document does not explicitly enumerate limitations. However, the scope suggests potential constraints: the approach targets context length/noise reduction rather than adversarial scenarios, and relies on specific datasets (NeuCLIR, RAGTIME) for validation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f6baab1-03d9-4eac-bfac-dca9d28831e4",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "d919b71d-ae7a-44d6-b7ad-1cc437c7aab2",
  "toolUseResult": {
    "bytes": 48801,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2511.17908\n\n## Full Abstract\n\n\"Retrieval-Augmented Generation (RAG) enhances factual grounding in large language models (LLMs) by incorporating retrieved evidence, but LLM accuracy declines when long or noisy contexts exceed the model's effective attention span. Existing pre-generation filters rely on heuristics or uncalibrated LLM confidence scores, offering no statistical control over retained evidence. We evaluate and demonstrate context engineering through conformal prediction, a coverage-controlled filtering framework that removes irrelevant content while preserving recall of supporting evidence. Using both embedding- and LLM-based scoring functions, we test this approach on the NeuCLIR and RAGTIME collections. Conformal filtering consistently meets its target coverage, ensuring that a specified fraction of relevant snippets are retained, and reduces retained context by 2-3x relative to unfiltered retrieval. On NeuCLIR, downstream factual accuracy measured by ARGUE F1 improves under strict filtering and remains stable at moderate coverage, indicating that most discarded material is redundant or irrelevant. These results demonstrate that conformal prediction enables reliable, coverage-controlled context reduction in RAG, offering a model-agnostic and principled approach to context engineering.\"\n\n## Adversarial Robustness Assessment\n\n**Does it address adversarial corpus poisoning?** No. The paper does not discuss intentional attacks or poisoning of retrieval corpora.\n\n**Does it provide robustness guarantees against poisoning?** No robustness guarantees against poisoning attacks are mentioned or provided.\n\n## Main Limitations\n\nThe document does not explicitly enumerate limitations. However, the scope suggests potential constraints: the approach targets context length/noise reduction rather than adversarial scenarios, and relies on specific datasets (NeuCLIR, RAGTIME) for validation.",
    "durationMs": 7683,
    "url": "https://arxiv.org/abs/2511.17908"
  },
  "sourceToolAssistantUUID": "3f6baab1-03d9-4eac-bfac-dca9d28831e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-30T06:55:45.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012bHfPH2rjXyErkxZDhm1BT`</summary>

```json
{
  "query": "conformal prediction distribution shift TV distance bound RAG retrieval adversarial 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d919b71d-ae7a-44d6-b7ad-1cc437c7aab2",
  "isSidechain": false,
  "requestId": "req_011CbYKH7Znbyea69RZpDn8L",
  "type": "assistant",
  "uuid": "09aa44d6-f4ee-4cd0-b286-75f361d3636b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCU2c4URXQtCp3cwFg1Y3H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 51063,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 51063,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 539
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

_source line 118 · 2026-05-30T06:55:52.753Z_

<details><summary>↩ Tool result · `toolu_012bHfPH2rjXyErkxZDhm1BT`</summary>

```text
Web search results for query: "conformal prediction distribution shift TV distance bound RAG retrieval adversarial 2025 2026"

Links: [{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Wasserstein-regularized Conformal Prediction under General Distribution   Shift","url":"https://arxiv.org/pdf/2501.13430"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview","url":"https://openreview.net/forum?id=1ULQvdbZ3X"},{"title":"(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"},{"title":"Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model","url":"https://arxiv.org/pdf/2403.15025"},{"title":"Empirically Validating Conformal Prediction on Modern Vision   Architectures Under Distribution Shift and Long-tailed Data","url":"https://arxiv.org/pdf/2307.01088"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/pdf/2410.06494"}]

I found several relevant research papers from 2025-2026 on conformal prediction under distribution shift. Here are the key results:

## Recent Papers on Conformal Prediction and Distribution Shift

**1. Conformal Prediction under Lévy-Prokhorov Distribution Shifts (2025)**

This paper addresses robustness under distribution shifts by modeling distribution shifts using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations. It provides connections between LP ambiguity sets and popular metrics such as Wasserstein and Total Variation.

**2. Wasserstein-Regularized Conformal Prediction under General Distribution Shift (2025)**

Prior studies bound the coverage gap using total variation distance, but this paper proposes a Wasserstein distance-based upper bound of the coverage gap, analyzing it using probability measure pushforwards between shifted joint data and conformal score distributions. The proposed WR-CP method can reduce coverage gaps to 3.1% across different confidence levels and outputs prediction sets 38% smaller than the worst-case approach on average.

**3. Conformal Prediction with RAG (2024-2025)**

Recent work proposes applying conformal risk control with RAG, showing that using RAG can lead to lower risk than normal LLM with or without covariate shift.

The search results show active research in 2025-2026 on combining conformal prediction with distribution shift metrics (TV distance, Wasserstein distance), adversarial robustness, and modern applications like RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09aa44d6-f4ee-4cd0-b286-75f361d3636b",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "7c15ef45-4d84-4869-8b7f-d8968ea38f95",
  "toolUseResult": {
    "query": "conformal prediction distribution shift TV distance bound RAG retrieval adversarial 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T1VJRu7uraLEDJa37jbWZV",
        "content": [
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Wasserstein-regularized Conformal Prediction under General Distribution   Shift",
            "url": "https://arxiv.org/pdf/2501.13430"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=1ULQvdbZ3X"
          },
          {
            "title": "(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"
          },
          {
            "title": "Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/pdf/2403.15025"
          },
          {
            "title": "Empirically Validating Conformal Prediction on Modern Vision   Architectures Under Distribution Shift and Long-tailed Data",
            "url": "https://arxiv.org/pdf/2307.01088"
          },
          {
            "title": "Conformal Prediction: A Data Perspective",
            "url": "https://arxiv.org/pdf/2410.06494"
          }
        ]
      },
      "I found several relevant research papers from 2025-2026 on conformal prediction under distribution shift. Here are the key results:\n\n## Recent Papers on Conformal Prediction and Distribution Shift\n\n**1. Conformal Prediction under Lévy-Prokhorov Distribution Shifts (2025)**\n\nThis paper addresses robustness under distribution shifts by modeling distribution shifts using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations. It provides connections between LP ambiguity sets and popular metrics such as Wasserstein and Total Variation.\n\n**2. Wasserstein-Regularized Conformal Prediction under General Distribution Shift (2025)**\n\nPrior studies bound the coverage gap using total variation distance, but this paper proposes a Wasserstein distance-based upper bound of the coverage gap, analyzing it using probability measure pushforwards between shifted joint data and conformal score distributions. The proposed WR-CP method can reduce coverage gaps to 3.1% across different confidence levels and outputs prediction sets 38% smaller than the worst-case approach on average.\n\n**3. Conformal Prediction with RAG (2024-2025)**\n\nRecent work proposes applying conformal risk control with RAG, showing that using RAG can lead to lower risk than normal LLM with or without covariate shift.\n\nThe search results show active research in 2025-2026 on combining conformal prediction with distribution shift metrics (TV distance, Wasserstein distance), adversarial robustness, and modern applications like RAG systems."
    ],
    "durationSeconds": 7.102099424000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "09aa44d6-f4ee-4cd0-b286-75f361d3636b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-30T06:55:56.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JWWkJifXRrb1GPaBm8GUj5`</summary>

```json
{
  "query": "C-RAG certified generation risks retrieval augmented language models ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c15ef45-4d84-4869-8b7f-d8968ea38f95",
  "isSidechain": false,
  "requestId": "req_011CbYKHxwQXk4L2hyNLPCFc",
  "type": "assistant",
  "uuid": "d32856f8-05e6-467a-b2ee-dbf09a6325ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178spEK89956tssa5zpHsxx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 51602,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 51602,
          "cache_creation_input_tokens": 867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 867
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

_source line 120 · 2026-05-30T06:56:01.535Z_

<details><summary>↩ Tool result · `toolu_01JWWkJifXRrb1GPaBm8GUj5`</summary>

```text
Web search results for query: "C-RAG certified generation risks retrieval augmented language models ICML 2024"

Links: [{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models | OpenReview","url":"https://openreview.net/forum?id=FMa4c5NhOe"},{"title":"[Quick Review] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://liner.com/review/crag-certified-generation-risks-for-retrievalaugmented-language-models"},{"title":"GitHub - kangmintong/C-RAG: [ICML 2024] Codes for C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models · GitHub","url":"https://github.com/kangmintong/C-RAG"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/c-rag-certified-generation-risks-for-retrieval-augmented-language/"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language   Models","url":"https://arxiv.org/pdf/2402.03181"},{"title":"[2402.03181] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2402.03181"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://proceedings.mlr.press/v235/kang24a.html"},{"title":"ICML Poster C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://icml.cc/virtual/2024/poster/34539"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2402.03181v5"}]

I found comprehensive information about the C-RAG paper from ICML 2024. Here's what I found:

## C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models

C-RAG is the first framework to certify generation risks for RAG models. Specifically, it provides conformal risk analysis for RAG models and certifies an upper confidence bound of generation risks, which is referred to as conformal generation risk.

### Key Research Questions

The paper addresses: 1) whether RAG can indeed lead to low generation risks, 2) how to provide provable guarantees on the generation risks of RAG and vanilla LLMs, and 3) what sufficient conditions enable RAG models to reduce generation risks.

### Main Contributions

The framework provides theoretical guarantees on conformal generation risks for general bounded risk functions under test distribution shifts. The authors prove that RAG achieves a lower conformal generation risk than that of a single LLM when the quality of the retrieval model and transformer is non-trivial.

### Empirical Validation

The intensive empirical results demonstrate the soundness and tightness of conformal generation risk guarantees across four widely-used NLP datasets on four state-of-the-art retrieval models.

### Publication Details

The paper was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), volume 235, pages 22963-23000. The authors are Mintong Kang, Nezihe Merve Gürel, Ning Yu, Dawn Song, and Bo Li.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d32856f8-05e6-467a-b2ee-dbf09a6325ff",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "324a8410-9870-40b5-83bf-a4b833a69383",
  "toolUseResult": {
    "query": "C-RAG certified generation risks retrieval augmented language models ICML 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_0177HZ8ui4uaD1SJVKQLNRa2",
        "content": [
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=FMa4c5NhOe"
          },
          {
            "title": "[Quick Review] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://liner.com/review/crag-certified-generation-risks-for-retrievalaugmented-language-models"
          },
          {
            "title": "GitHub - kangmintong/C-RAG: [ICML 2024] Codes for C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models · GitHub",
            "url": "https://github.com/kangmintong/C-RAG"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models - Illinois Experts",
            "url": "https://experts.illinois.edu/en/publications/c-rag-certified-generation-risks-for-retrieval-augmented-language/"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language   Models",
            "url": "https://arxiv.org/pdf/2402.03181"
          },
          {
            "title": "[2402.03181] C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/abs/2402.03181"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://proceedings.mlr.press/v235/kang24a.html"
          },
          {
            "title": "ICML Poster C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://icml.cc/virtual/2024/poster/34539"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/html/2402.03181v5"
          }
        ]
      },
      "I found comprehensive information about the C-RAG paper from ICML 2024. Here's what I found:\n\n## C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models\n\nC-RAG is the first framework to certify generation risks for RAG models. Specifically, it provides conformal risk analysis for RAG models and certifies an upper confidence bound of generation risks, which is referred to as conformal generation risk.\n\n### Key Research Questions\n\nThe paper addresses: 1) whether RAG can indeed lead to low generation risks, 2) how to provide provable guarantees on the generation risks of RAG and vanilla LLMs, and 3) what sufficient conditions enable RAG models to reduce generation risks.\n\n### Main Contributions\n\nThe framework provides theoretical guarantees on conformal generation risks for general bounded risk functions under test distribution shifts. The authors prove that RAG achieves a lower conformal generation risk than that of a single LLM when the quality of the retrieval model and transformer is non-trivial.\n\n### Empirical Validation\n\nThe intensive empirical results demonstrate the soundness and tightness of conformal generation risk guarantees across four widely-used NLP datasets on four state-of-the-art retrieval models.\n\n### Publication Details\n\nThe paper was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), volume 235, pages 22963-23000. The authors are Mintong Kang, Nezihe Merve Gürel, Ning Yu, Dawn Song, and Bo Li."
    ],
    "durationSeconds": 5.438462071000016,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d32856f8-05e6-467a-b2ee-dbf09a6325ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 121 · 2026-05-30T06:56:04.613Z_

Now let me do some final critical searches to verify the novelty gap:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "324a8410-9870-40b5-83bf-a4b833a69383",
  "isSidechain": false,
  "requestId": "req_011CbYKJcUNsuw7YikCsupbi",
  "type": "assistant",
  "uuid": "168dcf8c-5b76-450f-a41b-9af28a3675ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeLEwq6skKVWwm3wiPPVfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 52469,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 52469,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 956
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

_source line 122 · 2026-05-30T06:56:05.613Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RNu5ke26f1iTWQzFVzbUfv`</summary>

```json
{
  "query": "\"conformal\" \"abstention\" \"poisoning\" \"RAG\" OR \"retrieval\" 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "168dcf8c-5b76-450f-a41b-9af28a3675ac",
  "isSidechain": false,
  "requestId": "req_011CbYKJcUNsuw7YikCsupbi",
  "type": "assistant",
  "uuid": "22b014ac-8cba-4ee3-9915-34ab5e5a6aad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeLEwq6skKVWwm3wiPPVfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 52469,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 52469,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 956
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

_source line 123 · 2026-05-30T06:56:13.802Z_

<details><summary>↩ Tool result · `toolu_01RNu5ke26f1iTWQzFVzbUfv`</summary>

```text
Web search results for query: ""conformal" "abstention" "poisoning" "RAG" OR "retrieval" 2026 arxiv"

Links: [{"title":"AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning","url":"https://arxiv.org/html/2604.12201v1"},{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/html/2412.16708v2"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"}]

I found several relevant papers on arxiv related to poisoning attacks on RAG (Retrieval-Augmented Generation) systems from 2026 and 2025. While the search didn't return papers specifically combining all four terms ("conformal," "abstention," "poisoning," and "RAG/retrieval"), I did find relevant work on these topics:

**Key Papers Found:**

1. **AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning** (April 2026): This paper discusses knowledge-based poisoning attacks on RAG systems.

2. **Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks** (July 2025): This paper measures abstention as the proportion that LLMs didn't answer, and found that LLMs are more likely to express uncertainty when presented with untouched passages than with adversarial ones, possibly because it is easier for LLMs to abstain when the context is insufficient to answer the question.

3. **Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions** (April 2026): This paper discusses defenses including sparse document attention that blocks cross-attention across retrieved documents.

4. **RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning** (2025): This paper proposes RAGPart which leverages document partitioning to mitigate poisoned points, and RAGMask which identifies suspicious tokens based on similarity shifts under targeted token masking.

The search results show active research on poisoning attacks and defenses in RAG systems, though papers specifically focusing on "conformal" prediction methods combined with these topics may require a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22b014ac-8cba-4ee3-9915-34ab5e5a6aad",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "4e5f42fd-dde6-4199-8d95-abdaeecb1976",
  "toolUseResult": {
    "query": "\"conformal\" \"abstention\" \"poisoning\" \"RAG\" OR \"retrieval\" 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_011H4wH1dcG5w1w4k3LVfjRK",
        "content": [
          {
            "title": "AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning",
            "url": "https://arxiv.org/html/2604.12201v1"
          },
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/html/2412.16708v2"
          },
          {
            "title": "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions",
            "url": "https://arxiv.org/html/2604.08304v1"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          }
        ]
      },
      "I found several relevant papers on arxiv related to poisoning attacks on RAG (Retrieval-Augmented Generation) systems from 2026 and 2025. While the search didn't return papers specifically combining all four terms (\"conformal,\" \"abstention,\" \"poisoning,\" and \"RAG/retrieval\"), I did find relevant work on these topics:\n\n**Key Papers Found:**\n\n1. **AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning** (April 2026): This paper discusses knowledge-based poisoning attacks on RAG systems.\n\n2. **Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks** (July 2025): This paper measures abstention as the proportion that LLMs didn't answer, and found that LLMs are more likely to express uncertainty when presented with untouched passages than with adversarial ones, possibly because it is easier for LLMs to abstain when the context is insufficient to answer the question.\n\n3. **Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions** (April 2026): This paper discusses defenses including sparse document attention that blocks cross-attention across retrieved documents.\n\n4. **RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning** (2025): This paper proposes RAGPart which leverages document partitioning to mitigate poisoned points, and RAGMask which identifies suspicious tokens based on similarity shifts under targeted token masking.\n\nThe search results show active research on poisoning attacks and defenses in RAG systems, though papers specifically focusing on \"conformal\" prediction methods combined with these topics may require a more targeted search."
    ],
    "durationSeconds": 8.185414769999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "22b014ac-8cba-4ee3-9915-34ab5e5a6aad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 124_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "4e5f42fd-dde6-4199-8d95-abdaeecb1976",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 125_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool call

_source line 126 · 2026-05-30T06:56:16.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D4YR4b4N2L3kYhQsduYQry`</summary>

```json
{
  "query": "robust conformal prediction test-time attack inference-time corruption certificate 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e5f42fd-dde6-4199-8d95-abdaeecb1976",
  "isSidechain": false,
  "requestId": "req_011CbYKKWrpBUocUhk82px3A",
  "type": "assistant",
  "uuid": "8515698c-f485-4718-9565-26ad1649476a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQxztgjdsQfB1jjCwnRtme",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 53425,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 53425,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 872
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

_source line 127 · 2026-05-30T06:56:27.756Z_

<details><summary>↩ Tool result · `toolu_01D4YR4b4N2L3kYhQsduYQry`</summary>

```text
Web search results for query: "robust conformal prediction test-time attack inference-time corruption certificate 2025 2026"

Links: [{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"},{"title":"ADVERSARIALLY ROBUST CONFORMAL PREDICTION","url":"https://openreview.net/pdf?id=9L1BsI4wP1H"},{"title":"Robust Conformal Prediction Using Privileged Information","url":"https://arxiv.org/pdf/2406.05405"},{"title":"Robust Conformal Prediction with a Single Binary Certificate | OpenReview","url":"https://openreview.net/forum?id=ltrxRX5t0H"},{"title":"[2503.05239] Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/abs/2503.05239"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/pdf/2511.18562"},{"title":"Verifiably Robust Conformal Prediction Linus Jeary∗ Department of Informatics","url":"https://arxiv.org/pdf/2405.18942"},{"title":"ROBUST CONFORMAL PREDICTION WITH A SINGLE ... - cispa","url":"https://publications.cispa.de/articles/conference_contribution/Robust_Conformal_Prediction_with_a_Single_Binary_Certificate/29618666/1/files/56460146.pdf"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"}]

Based on the search results, I found several relevant papers on robust conformal prediction with adversarial attacks and certificates published in 2025-2026:

## Key Recent Papers

**Verifiably Robust Conformal Prediction (VRCP)**

VRCP recovers conformal prediction's probabilistic guarantees under adversarial attacks, published in February 2026. The method combines conformal prediction with neural network verification, and demonstrates valid marginal coverage under ℓ1, ℓ2, and ℓ∞-norm bounded adversarial attacks while producing more accurate prediction sets than existing methods.

**Robust Conformal Prediction with a Single Binary Certificate**

A robust conformal prediction approach that achieves robustness by computing only one binary certificate, making it faster and returning smaller robust sets. This method produces smaller sets even with significantly lower Monte-Carlo samples (e.g., 150 for CIFAR10).

**Ensuring Calibration Robustness Under Adversarial Attacks**

Research shows that prediction coverage varies monotonically with calibration-time attack strength, and with suitable calibration attacks, coverage can stay within a chosen tolerance band across contiguous sets of perturbation levels.

These papers address the intersection of conformal prediction reliability, adversarial robustness, and formal certification methods that your query targets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8515698c-f485-4718-9565-26ad1649476a",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "fdfa8165-7209-468f-88cb-48cf32e6456d",
  "toolUseResult": {
    "query": "robust conformal prediction test-time attack inference-time corruption certificate 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Tc93usF7zadWtkPnBvEqiD",
        "content": [
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0031320325007113"
          },
          {
            "title": "ADVERSARIALLY ROBUST CONFORMAL PREDICTION",
            "url": "https://openreview.net/pdf?id=9L1BsI4wP1H"
          },
          {
            "title": "Robust Conformal Prediction Using Privileged Information",
            "url": "https://arxiv.org/pdf/2406.05405"
          },
          {
            "title": "Robust Conformal Prediction with a Single Binary Certificate | OpenReview",
            "url": "https://openreview.net/forum?id=ltrxRX5t0H"
          },
          {
            "title": "[2503.05239] Robust Conformal Prediction with a Single Binary Certificate",
            "url": "https://arxiv.org/abs/2503.05239"
          },
          {
            "title": "Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks",
            "url": "https://arxiv.org/pdf/2511.18562"
          },
          {
            "title": "Verifiably Robust Conformal Prediction Linus Jeary∗ Department of Informatics",
            "url": "https://arxiv.org/pdf/2405.18942"
          },
          {
            "title": "ROBUST CONFORMAL PREDICTION WITH A SINGLE ... - cispa",
            "url": "https://publications.cispa.de/articles/conference_contribution/Robust_Conformal_Prediction_with_a_Single_Binary_Certificate/29618666/1/files/56460146.pdf"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on robust conformal prediction with adversarial attacks and certificates published in 2025-2026:\n\n## Key Recent Papers\n\n**Verifiably Robust Conformal Prediction (VRCP)**\n\nVRCP recovers conformal prediction's probabilistic guarantees under adversarial attacks, published in February 2026. The method combines conformal prediction with neural network verification, and demonstrates valid marginal coverage under ℓ1, ℓ2, and ℓ∞-norm bounded adversarial attacks while producing more accurate prediction sets than existing methods.\n\n**Robust Conformal Prediction with a Single Binary Certificate**\n\nA robust conformal prediction approach that achieves robustness by computing only one binary certificate, making it faster and returning smaller robust sets. This method produces smaller sets even with significantly lower Monte-Carlo samples (e.g., 150 for CIFAR10).\n\n**Ensuring Calibration Robustness Under Adversarial Attacks**\n\nResearch shows that prediction coverage varies monotonically with calibration-time attack strength, and with suitable calibration attacks, coverage can stay within a chosen tolerance band across contiguous sets of perturbation levels.\n\nThese papers address the intersection of conformal prediction reliability, adversarial robustness, and formal certification methods that your query targets."
    ],
    "durationSeconds": 11.521275502999954,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8515698c-f485-4718-9565-26ad1649476a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-30T06:56:30.189Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018fuucdrJeDQh8CwWjn9CQF`</summary>

```json
{
  "query": "NLI agreement score nonconformity retrieval documents conformal abstention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdfa8165-7209-468f-88cb-48cf32e6456d",
  "isSidechain": false,
  "requestId": "req_011CbYKLYaGxio8NiUC4y365",
  "type": "assistant",
  "uuid": "78d421b3-f91d-497e-a4e2-f5da6fc91241",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NY9pe9MKxWNAATz49aLRpt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 54297,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 54297,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 129 · 2026-05-30T06:56:38.553Z_

<details><summary>↩ Tool result · `toolu_018fuucdrJeDQh8CwWjn9CQF`</summary>

```text
Web search results for query: "NLI agreement score nonconformity retrieval documents conformal abstention 2025 2026"

Links: [{"title":"Nonconformity Score in Conformal Prediction","url":"https://www.emergentmind.com/topics/nonconformity-score"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"NCAA Eliminates National Letter of Intent (NLI). What Now?","url":"https://www.ncsasports.org/blog/ncaa-eliminates-nli"},{"title":"National Signing Day: What You Need to Know (2025-2026)","url":"https://www.ncsasports.org/recruiting/managing-recruiting-process/national-signing-day"},{"title":"Federated Language Models Under Bandwidth Budgets: Distillation Rates and Conformal Coverage","url":"https://arxiv.org/html/2605.09986"},{"title":"Streamlining Conformal Information Retrieval via Score Refinement","url":"https://arxiv.org/pdf/2410.02914"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models","url":"https://arxiv.org/pdf/2502.06884"},{"title":"Symmetric Aggregation of Conformity Scores for Efficient Uncertainty Sets","url":"https://www.arxiv.org/pdf/2512.06945"}]

Based on the search results, I found several relevant papers and resources related to your query about NLI agreement score, nonconformity, retrieval, documents, conformal abstention from 2025-2026:

## Key Findings:

**Conformal Abstention for LLMs:**
Recent work addresses agreement evaluation by developing well-engineered prompts to use the LLM for evaluating the similarity of two of its responses for a given query, and using theoretically well-founded methods to determine the level of agreement in evaluation responses, below which the LLM is likely hallucinating. This leverages conformal prediction and related risk control techniques, assuming access to a small holdout calibration set of prompt-response pairs, and allows calibration of the detection/abstention policy so that it satisfies a pre-specified, distribution-free, statistical upper bound on the hallucination risk while minimizing the abstention rate.

**Nonconformity Scores in Conformal Prediction:**
Recent work uses a nonconformity measure based on softmax probabilities, computing the nonconformity score for each sample as 1 minus the predicted probability of the true class, where higher values indicate greater uncertainty.

**Conformal Prediction for Document Retrieval:**
Recent methods have incorporated conformal prediction into ranked retrieval systems to ensure the reliability and quality of retrieved items. One approach introduces a score refinement method that employs a monotone transformation to adjust the scores of information retrieval systems, and by applying standard conformal prediction methods to these refined scores, delivers significantly smaller retrieved sets while preserving their statistical guarantees.

The search results indicate active research in 2025-2026 on applying conformal prediction methods to language models, uncertainty quantification, and information retrieval systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78d421b3-f91d-497e-a4e2-f5da6fc91241",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "154f218a-9f5e-4e7d-9482-3cdb68639131",
  "toolUseResult": {
    "query": "NLI agreement score nonconformity retrieval documents conformal abstention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014nYZNhLp6SvmJuJ8TA7yKo",
        "content": [
          {
            "title": "Nonconformity Score in Conformal Prediction",
            "url": "https://www.emergentmind.com/topics/nonconformity-score"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          },
          {
            "title": "NCAA Eliminates National Letter of Intent (NLI). What Now?",
            "url": "https://www.ncsasports.org/blog/ncaa-eliminates-nli"
          },
          {
            "title": "National Signing Day: What You Need to Know (2025-2026)",
            "url": "https://www.ncsasports.org/recruiting/managing-recruiting-process/national-signing-day"
          },
          {
            "title": "Federated Language Models Under Bandwidth Budgets: Distillation Rates and Conformal Coverage",
            "url": "https://arxiv.org/html/2605.09986"
          },
          {
            "title": "Streamlining Conformal Information Retrieval via Score Refinement",
            "url": "https://arxiv.org/pdf/2410.02914"
          },
          {
            "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models",
            "url": "https://arxiv.org/pdf/2502.06884"
          },
          {
            "title": "Symmetric Aggregation of Conformity Scores for Efficient Uncertainty Sets",
            "url": "https://www.arxiv.org/pdf/2512.06945"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources related to your query about NLI agreement score, nonconformity, retrieval, documents, conformal abstention from 2025-2026:\n\n## Key Findings:\n\n**Conformal Abstention for LLMs:**\nRecent work addresses agreement evaluation by developing well-engineered prompts to use the LLM for evaluating the similarity of two of its responses for a given query, and using theoretically well-founded methods to determine the level of agreement in evaluation responses, below which the LLM is likely hallucinating. This leverages conformal prediction and related risk control techniques, assuming access to a small holdout calibration set of prompt-response pairs, and allows calibration of the detection/abstention policy so that it satisfies a pre-specified, distribution-free, statistical upper bound on the hallucination risk while minimizing the abstention rate.\n\n**Nonconformity Scores in Conformal Prediction:**\nRecent work uses a nonconformity measure based on softmax probabilities, computing the nonconformity score for each sample as 1 minus the predicted probability of the true class, where higher values indicate greater uncertainty.\n\n**Conformal Prediction for Document Retrieval:**\nRecent methods have incorporated conformal prediction into ranked retrieval systems to ensure the reliability and quality of retrieved items. One approach introduces a score refinement method that employs a monotone transformation to adjust the scores of information retrieval systems, and by applying standard conformal prediction methods to these refined scores, delivers significantly smaller retrieved sets while preserving their statistical guarantees.\n\nThe search results indicate active research in 2025-2026 on applying conformal prediction methods to language models, uncertainty quantification, and information retrieval systems."
    ],
    "durationSeconds": 8.359010882000032,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "78d421b3-f91d-497e-a4e2-f5da6fc91241",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 130 · 2026-05-30T06:56:38.556Z_

```json
{
  "parentUuid": "154f218a-9f5e-4e7d-9482-3cdb68639131",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "879b9a82-3f67-4e50-8987-a1cac3a827b8",
  "timestamp": "2026-05-30T06:56:38.556Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 131 · 2026-05-30T06:56:41.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019uz6Uy3v7axQcXpB3bqK7M`</summary>

```json
{
  "query": "securing RAG taxonomy attacks defenses survey 2604.08304 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "879b9a82-3f67-4e50-8987-a1cac3a827b8",
  "isSidechain": false,
  "requestId": "req_011CbYKMLhRumTFpm9fJrY8u",
  "type": "assistant",
  "uuid": "e130119f-63a3-4978-a0c0-96080638b18b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lw5WEvcTQ2bS3t9gytfKLq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 55157,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 55157,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1035
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

_source line 132 · 2026-05-30T06:56:48.674Z_

<details><summary>↩ Tool result · `toolu_019uz6Uy3v7axQcXpB3bqK7M`</summary>

```text
Web search results for query: "securing RAG taxonomy attacks defenses survey 2604.08304 2026"

Links: [{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304"},{"title":"[2604.08304] Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/abs/2604.08304"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks,","url":"https://arxiv.org/pdf/2604.08304"},{"title":"Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks","url":"https://arxiv.org/pdf/2603.21654"},{"title":"Securing RAG: A Risk Assessment and Mitigation Framework | Request PDF","url":"https://www.researchgate.net/publication/393887977_Securing_Rag_A_Risk_Assessment_and_Mitigation_Framework"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"Securing AI Agents Against Prompt Injection Attacks","url":"https://arxiv.org/pdf/2511.15759"},{"title":"[2603.21654] Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks","url":"https://arxiv.org/abs/2603.21654"}]

Based on the search results, I found the paper you're looking for:

The paper "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions" (arXiv:2604.08304v1) was published on April 9, 2026 by researchers from The Hong Kong Polytechnic University and The Hong Kong University of Science and Technology (Guangzhou), including Yuming XU, Mingtao ZHANG, Zhuohan GE, and others.

**Key Findings:**

The paper proposes that secure RAG is fundamentally about the security of the external knowledge-access pipeline, establishing an operational boundary to separate inherent LLM flaws from RAG-introduced or RAG-amplified threats.

The authors abstract the RAG workflow into six stages and organize the literature around three trust boundaries and four primary security surfaces, including pre-retrieval knowledge corruption, retrieval-time access manipulation, downstream context exploitation, and knowledge exfiltration.

In secure RAG, the attacker often does not need to alter model parameters or place malicious instructions directly in the user prompt. Instead, it can manipulate external content, retrieval behavior, or disclosure behavior so that harmful evidence enters the model-visible context, or so that sensitive knowledge is inferred or extracted through the response interface.

You can access the full paper on arXiv at https://arxiv.org/html/2604.08304 or https://arxiv.org/abs/2604.08304.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e130119f-63a3-4978-a0c0-96080638b18b",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "cf152bfc-439f-4507-859c-8c31828712a9",
  "toolUseResult": {
    "query": "securing RAG taxonomy attacks defenses survey 2604.08304 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SMuLUPdmf2ojdvyfk3DaVT",
        "content": [
          {
            "title": "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions",
            "url": "https://arxiv.org/html/2604.08304"
          },
          {
            "title": "[2604.08304] Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions",
            "url": "https://arxiv.org/abs/2604.08304"
          },
          {
            "title": "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks,",
            "url": "https://arxiv.org/pdf/2604.08304"
          },
          {
            "title": "Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks",
            "url": "https://arxiv.org/pdf/2603.21654"
          },
          {
            "title": "Securing RAG: A Risk Assessment and Mitigation Framework | Request PDF",
            "url": "https://www.researchgate.net/publication/393887977_Securing_Rag_A_Risk_Assessment_and_Mitigation_Framework"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/pdf/2603.18034"
          },
          {
            "title": "Securing AI Agents Against Prompt Injection Attacks",
            "url": "https://arxiv.org/pdf/2511.15759"
          },
          {
            "title": "[2603.21654] Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks",
            "url": "https://arxiv.org/abs/2603.21654"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions\" (arXiv:2604.08304v1) was published on April 9, 2026 by researchers from The Hong Kong Polytechnic University and The Hong Kong University of Science and Technology (Guangzhou), including Yuming XU, Mingtao ZHANG, Zhuohan GE, and others.\n\n**Key Findings:**\n\nThe paper proposes that secure RAG is fundamentally about the security of the external knowledge-access pipeline, establishing an operational boundary to separate inherent LLM flaws from RAG-introduced or RAG-amplified threats.\n\nThe authors abstract the RAG workflow into six stages and organize the literature around three trust boundaries and four primary security surfaces, including pre-retrieval knowledge corruption, retrieval-time access manipulation, downstream context exploitation, and knowledge exfiltration.\n\nIn secure RAG, the attacker often does not need to alter model parameters or place malicious instructions directly in the user prompt. Instead, it can manipulate external content, retrieval behavior, or disclosure behavior so that harmful evidence enters the model-visible context, or so that sensitive knowledge is inferred or extracted through the response interface.\n\nYou can access the full paper on arXiv at https://arxiv.org/html/2604.08304 or https://arxiv.org/abs/2604.08304."
    ],
    "durationSeconds": 7.288294250999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e130119f-63a3-4978-a0c0-96080638b18b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-30T06:56:52.359Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EUiULiVBp279Qa4ch5PXaZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08304",
  "prompt": "Extract: Does this survey mention conformal prediction as a defense mechanism? Does it identify the gap of combining conformal prediction with adversarial robustness in RAG? What future directions does it recommend? What are the key defense categories they identify?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf152bfc-439f-4507-859c-8c31828712a9",
  "isSidechain": false,
  "requestId": "req_011CbYKN64tet7j2X2ZGLiYv",
  "type": "assistant",
  "uuid": "3a30352c-fa8a-4ad7-bb81-c1850177ca42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BPMkdd2YASM1NBDW9CCnU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 56192,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 56192,
          "cache_creation_input_tokens": 854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 854
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

_source line 134 · 2026-05-30T06:56:56.313Z_

<details><summary>↩ Tool result · `toolu_01EUiULiVBp279Qa4ch5PXaZ`</summary>

```text
# Analysis of RAG Security Survey

Based on the provided web page content, I can offer limited information:

**Conformal Prediction Mention:** The abstract and available content do not mention conformal prediction as a defense mechanism.

**Gap Identification:** There is no discussion of combining conformal prediction with adversarial robustness in the excerpted material.

**Future Directions:** The abstract lists several recommended directions: "more realistic targets, no-blind-spot and adaptively evaluated defenses, stronger confidentiality, and evaluation for multimodal and agentic RAG."

**Key Defense Categories:** The paper introduces "SLOT, a taxonomy along four axes: the attack Surface (S) where an adversary acts, the defense Layer (L) that controls the same point, the Objective (O) it breaks following the CIA properties, and the Target (T)."

**Limitation:** The webpage provided only contains the abstract, metadata, and navigation elements. To fully answer your questions about specific defense mechanisms, research gaps, and detailed categorizations, the complete paper would need to be reviewed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a30352c-fa8a-4ad7-bb81-c1850177ca42",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "2881f354-13c0-4a84-9e92-36a00a0e2254",
  "toolUseResult": {
    "bytes": 46507,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of RAG Security Survey\n\nBased on the provided web page content, I can offer limited information:\n\n**Conformal Prediction Mention:** The abstract and available content do not mention conformal prediction as a defense mechanism.\n\n**Gap Identification:** There is no discussion of combining conformal prediction with adversarial robustness in the excerpted material.\n\n**Future Directions:** The abstract lists several recommended directions: \"more realistic targets, no-blind-spot and adaptively evaluated defenses, stronger confidentiality, and evaluation for multimodal and agentic RAG.\"\n\n**Key Defense Categories:** The paper introduces \"SLOT, a taxonomy along four axes: the attack Surface (S) where an adversary acts, the defense Layer (L) that controls the same point, the Objective (O) it breaks following the CIA properties, and the Target (T).\"\n\n**Limitation:** The webpage provided only contains the abstract, metadata, and navigation elements. To fully answer your questions about specific defense mechanisms, research gaps, and detailed categorizations, the complete paper would need to be reviewed.",
    "durationMs": 3950,
    "url": "https://arxiv.org/abs/2604.08304"
  },
  "sourceToolAssistantUUID": "3a30352c-fa8a-4ad7-bb81-c1850177ca42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-30T06:56:58.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012dNf8VkRHrbDzaCyHCXQ47`</summary>

```json
{
  "query": "conformal prediction selective prediction e-values distribution shift LLM question answering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2881f354-13c0-4a84-9e92-36a00a0e2254",
  "isSidechain": false,
  "requestId": "req_011CbYKNegh52xCco1XEBxN8",
  "type": "assistant",
  "uuid": "3125f022-a17a-4925-8e4b-420a354dae94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsiT3RvXoUoiDDDj61uKj4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 376,
      "cache_read_input_tokens": 57046,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 57046,
          "cache_creation_input_tokens": 376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 376
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

_source line 136 · 2026-05-30T06:57:06.105Z_

<details><summary>↩ Tool result · `toolu_012dNf8VkRHrbDzaCyHCXQ47`</summary>

```text
Web search results for query: "conformal prediction selective prediction e-values distribution shift LLM question answering 2026"

Links: [{"title":"Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/html/2604.16217v1"},{"title":"Conformal Selective Prediction with General Risk Control","url":"https://arxiv.org/pdf/2603.24704"},{"title":"Paraphrase-Robust Conformal Prediction for Reliable LLM Uncertainty Quantification | OpenReview","url":"https://openreview.net/forum?id=Uf04r8gDn7"},{"title":"Prune 'n Predict: Optimizing LLM Decision-making with Conformal Prediction | OpenReview","url":"https://openreview.net/forum?id=5g6LPR0Dlx&noteId=OxRr52rzPF"},{"title":"Model-free selective inference under covariate shift via weighted   conformal p-values","url":"https://arxiv.org/pdf/2307.09291"},{"title":"Adapting Prediction Sets to Distribution Shifts Without Labels","url":"https://arxiv.org/pdf/2406.01416"},{"title":"E-Values Expand the Scope of Conformal Prediction","url":"https://arxiv.org/pdf/2503.13050"},{"title":"Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://arxiv.org/html/2604.13991"}]

I found several recent papers from 2026 and late 2025 on this topic. Here's a summary of the search results:

## Key Papers Found

**1. Conformal Prediction for LLMs with Internal Representations** (April 2026)
A paper proposes layer-wise information-based nonconformity scores that move conformal uncertainty estimation from output-level statistics to internal layer-wise signals, achieving stronger validity-efficiency trade-offs than baselines based on API-only and sampling-based uncertainty measures, with the clearest gains under cross-domain shift.

**2. Conformal Selective Prediction with General Risk Control** (March 2026)
The SCoRE method constructs a class of generalized e-values, which are non-negative random variables whose product with the unknown risk has expectation no greater than one. This property is ensured by data exchangeability without requiring modeling assumptions, and the method can be readily extended to settings with distribution shifts. Applications include error management in drug discovery, health risk prediction, and large language models.

**3. E-Values Expand the Scope of Conformal Prediction** (May 2025)
An alternative approach based on e-values, called conformal e-prediction, offers key advantages that cannot be achieved with p-values, enabling new theoretical and practical capabilities.

**4. Adaptive Conformal Prediction for LLMs** (April 2026)
A method extends conformal score transformation to LLMs, with applications to long-form generation and multiple-choice question answering, enabling prompt-dependent calibration while retaining marginal coverage guarantees.

These papers address the intersection of conformal prediction, selective prediction, e-values, distribution shift, and LLM question answering that you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3125f022-a17a-4925-8e4b-420a354dae94",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "a2f8527d-b4ed-426b-8780-e041a4388229",
  "toolUseResult": {
    "query": "conformal prediction selective prediction e-values distribution shift LLM question answering 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BsYMLZwd33AMY17B1s8w8g",
        "content": [
          {
            "title": "Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations",
            "url": "https://arxiv.org/html/2604.16217v1"
          },
          {
            "title": "Conformal Selective Prediction with General Risk Control",
            "url": "https://arxiv.org/pdf/2603.24704"
          },
          {
            "title": "Paraphrase-Robust Conformal Prediction for Reliable LLM Uncertainty Quantification | OpenReview",
            "url": "https://openreview.net/forum?id=Uf04r8gDn7"
          },
          {
            "title": "Prune 'n Predict: Optimizing LLM Decision-making with Conformal Prediction | OpenReview",
            "url": "https://openreview.net/forum?id=5g6LPR0Dlx&noteId=OxRr52rzPF"
          },
          {
            "title": "Model-free selective inference under covariate shift via weighted   conformal p-values",
            "url": "https://arxiv.org/pdf/2307.09291"
          },
          {
            "title": "Adapting Prediction Sets to Distribution Shifts Without Labels",
            "url": "https://arxiv.org/pdf/2406.01416"
          },
          {
            "title": "E-Values Expand the Scope of Conformal Prediction",
            "url": "https://arxiv.org/pdf/2503.13050"
          },
          {
            "title": "Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models",
            "url": "https://arxiv.org/html/2604.13991"
          }
        ]
      },
      "I found several recent papers from 2026 and late 2025 on this topic. Here's a summary of the search results:\n\n## Key Papers Found\n\n**1. Conformal Prediction for LLMs with Internal Representations** (April 2026)\nA paper proposes layer-wise information-based nonconformity scores that move conformal uncertainty estimation from output-level statistics to internal layer-wise signals, achieving stronger validity-efficiency trade-offs than baselines based on API-only and sampling-based uncertainty measures, with the clearest gains under cross-domain shift.\n\n**2. Conformal Selective Prediction with General Risk Control** (March 2026)\nThe SCoRE method constructs a class of generalized e-values, which are non-negative random variables whose product with the unknown risk has expectation no greater than one. This property is ensured by data exchangeability without requiring modeling assumptions, and the method can be readily extended to settings with distribution shifts. Applications include error management in drug discovery, health risk prediction, and large language models.\n\n**3. E-Values Expand the Scope of Conformal Prediction** (May 2025)\nAn alternative approach based on e-values, called conformal e-prediction, offers key advantages that cannot be achieved with p-values, enabling new theoretical and practical capabilities.\n\n**4. Adaptive Conformal Prediction for LLMs** (April 2026)\nA method extends conformal score transformation to LLMs, with applications to long-form generation and multiple-choice question answering, enabling prompt-dependent calibration while retaining marginal coverage guarantees.\n\nThese papers address the intersection of conformal prediction, selective prediction, e-values, distribution shift, and LLM question answering that you're interested in."
    ],
    "durationSeconds": 7.396990043000027,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3125f022-a17a-4925-8e4b-420a354dae94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 137_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "a2f8527d-b4ed-426b-8780-e041a4388229",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 138_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool call

_source line 139 · 2026-05-30T06:57:08.953Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011qhdxth6x2JTKBJyJdPWyT`</summary>

```json
{
  "query": "CRC conformal risk control distribution shift TV bound adversarial worst-case Angelopoulos 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2f8527d-b4ed-426b-8780-e041a4388229",
  "isSidechain": false,
  "requestId": "req_011CbYKPNXNY9mJ7HTGXbdEZ",
  "type": "assistant",
  "uuid": "b3f79e9f-8fac-4cb5-b89f-7de081617a5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BB11XPY6jqcKuZiE1G28Kq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 57422,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 57422,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 875
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

_source line 140 · 2026-05-30T06:57:15.777Z_

<details><summary>↩ Tool result · `toolu_011qhdxth6x2JTKBJyJdPWyT`</summary>

```text
Web search results for query: "CRC conformal risk control distribution shift TV bound adversarial worst-case Angelopoulos 2024"

Links: [{"title":"Conditional Conformal Risk Adaptation","url":"https://arxiv.org/html/2504.07611v1"},{"title":"Conformal Policy Control","url":"https://arxiv.org/html/2603.02196v1"},{"title":"Anytime-Valid Conformal Risk Control","url":"https://arxiv.org/html/2602.04364v1"},{"title":"[2208.02814] Conformal Risk Control","url":"https://arxiv.org/abs/2208.02814"},{"title":"arXiv:2208.02814v4 [stat.ME] 13 Jun 2025 Conformal Risk Control","url":"https://arxiv.org/pdf/2208.02814"},{"title":"Non-monotonicity in Conformal Risk Control","url":"https://arxiv.org/pdf/2604.01502"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf"},{"title":"Conformal Risk Control","url":"https://arxiv.org/html/2208.02814v4"}]

I found relevant results about Conformal Risk Control (CRC) and related work by Angelopoulos and colleagues. Here's what the search revealed:

## Conformal Risk Control Overview

Conformal Risk Control extends conformal prediction to control the expected value of any monotone loss function. The conformal risk control procedure is tight up to an O(1/n) factor.

## Key Extensions and Features

The framework includes extensions to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics. This directly addresses several of the topics you mentioned in your query, including distribution shift and adversarial risk control.

## Recent Developments

The search results show active recent work in this area. Work has generalized conformal risk control to the setting of test-time distribution shift, where the calibration data is drawn from a distribution different from the test distribution, with correction terms to achieve anytime-valid risk control under distribution shift.

Additionally, Conformal risk control extends the conformal prediction framework to provide distribution-free guarantees for controlling user-specified risks in expectation.

The search results indicate that this is an active area of research with multiple papers from 2024-2026 extending and building upon the foundational CRC framework by Angelopoulos and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3f79e9f-8fac-4cb5-b89f-7de081617a5f",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "af8ba0a8-970d-4f6a-bb30-28f8020897b9",
  "toolUseResult": {
    "query": "CRC conformal risk control distribution shift TV bound adversarial worst-case Angelopoulos 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_013ZzSkHwRTjMTMNxPZWf1cp",
        "content": [
          {
            "title": "Conditional Conformal Risk Adaptation",
            "url": "https://arxiv.org/html/2504.07611v1"
          },
          {
            "title": "Conformal Policy Control",
            "url": "https://arxiv.org/html/2603.02196v1"
          },
          {
            "title": "Anytime-Valid Conformal Risk Control",
            "url": "https://arxiv.org/html/2602.04364v1"
          },
          {
            "title": "[2208.02814] Conformal Risk Control",
            "url": "https://arxiv.org/abs/2208.02814"
          },
          {
            "title": "arXiv:2208.02814v4 [stat.ME] 13 Jun 2025 Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2208.02814"
          },
          {
            "title": "Non-monotonicity in Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2604.01502"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf"
          },
          {
            "title": "Conformal Risk Control",
            "url": "https://arxiv.org/html/2208.02814v4"
          }
        ]
      },
      "I found relevant results about Conformal Risk Control (CRC) and related work by Angelopoulos and colleagues. Here's what the search revealed:\n\n## Conformal Risk Control Overview\n\nConformal Risk Control extends conformal prediction to control the expected value of any monotone loss function. The conformal risk control procedure is tight up to an O(1/n) factor.\n\n## Key Extensions and Features\n\nThe framework includes extensions to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics. This directly addresses several of the topics you mentioned in your query, including distribution shift and adversarial risk control.\n\n## Recent Developments\n\nThe search results show active recent work in this area. Work has generalized conformal risk control to the setting of test-time distribution shift, where the calibration data is drawn from a distribution different from the test distribution, with correction terms to achieve anytime-valid risk control under distribution shift.\n\nAdditionally, Conformal risk control extends the conformal prediction framework to provide distribution-free guarantees for controlling user-specified risks in expectation.\n\nThe search results indicate that this is an active area of research with multiple papers from 2024-2026 extending and building upon the foundational CRC framework by Angelopoulos and colleagues."
    ],
    "durationSeconds": 6.821747044000018,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b3f79e9f-8fac-4cb5-b89f-7de081617a5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-30T06:57:18.374Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018bk7hbsuZEkuashbRjJvDk`</summary>

```json
{
  "query": "\"geometry-calibrated\" conformal abstention language model 2604.27914"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af8ba0a8-970d-4f6a-bb30-28f8020897b9",
  "isSidechain": false,
  "requestId": "req_011CbYKQ5tHJx6in2EUxcxQ1",
  "type": "assistant",
  "uuid": "35dc15cb-b42b-4a76-8b81-6e78e52bf422",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173AyJdZohxRMcVz8CXdAnP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 58297,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 737,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 58297,
          "cache_creation_input_tokens": 737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 737
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

_source line 142 · 2026-05-30T06:57:26.664Z_

<details><summary>↩ Tool result · `toolu_018bk7hbsuZEkuashbRjJvDk`</summary>

```text
Web search results for query: ""geometry-calibrated" conformal abstention language model 2604.27914"

Links: [{"title":"[2604.27914] Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/abs/2604.27914"},{"title":"Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/html/2604.27914"},{"title":"Conformal Linguistic Calibration: Trading-off between ...","url":"https://openreview.net/pdf/55aa4de08b2f5bcfa9155bb9c656e887cfb2d7e5.pdf"},{"title":"A method to mitigate hallucinations in large language models","url":"https://techxplore.com/news/2024-05-method-mitigate-hallucinations-large-language.html"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models","url":"https://arxiv.org/pdf/2502.06884"},{"title":"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://arxiv.org/pdf/2502.19110"}]

Based on the search results, here's what I found about this paper:

"Geometry-Calibrated Conformal Abstention for Language Models" proposes a post hoc framework, Conformal Abstention (CA), adapted from conformal prediction (CP) to determine whether to abstain from answering a query. 

The motivation behind this work is that when language models lack relevant knowledge for a given query, they frequently generate plausible responses that can be hallucinations, rather than admitting being agnostic about the answer. Retraining models to reward admitting ignorance can lead to overly conservative behaviors and poor generalization due to scarce evaluation benchmarks.

CA provides finite-sample guarantees on both the probability of participation (i.e., not abstaining) and the probability that the generated response is correct. Importantly, the abstention decision relies on prediction confidence rather than the non-conformity scores used in CP, which are intractable for open-ended generation. To better align prediction confidence with the model's ignorance, the paper introduces a calibration strategy using representation geometry within the model to measure knowledge.

The paper was published on April 30, 2026, and is authored by Rui Xu, Yi Chen, Sihong Xie, and Hui Xiong from Hong Kong University of Science and Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35dc15cb-b42b-4a76-8b81-6e78e52bf422",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "ed94e85d-3e98-4ce2-8e25-0db9cc203c93",
  "toolUseResult": {
    "query": "\"geometry-calibrated\" conformal abstention language model 2604.27914",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MfdeXXwbC8Mzsb3TUWocBC",
        "content": [
          {
            "title": "[2604.27914] Geometry-Calibrated Conformal Abstention for Language Models",
            "url": "https://arxiv.org/abs/2604.27914"
          },
          {
            "title": "Geometry-Calibrated Conformal Abstention for Language Models",
            "url": "https://arxiv.org/html/2604.27914"
          },
          {
            "title": "Conformal Linguistic Calibration: Trading-off between ...",
            "url": "https://openreview.net/pdf/55aa4de08b2f5bcfa9155bb9c656e887cfb2d7e5.pdf"
          },
          {
            "title": "A method to mitigate hallucinations in large language models",
            "url": "https://techxplore.com/news/2024-05-method-mitigate-hallucinations-large-language.html"
          },
          {
            "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models",
            "url": "https://arxiv.org/pdf/2502.06884"
          },
          {
            "title": "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity",
            "url": "https://arxiv.org/pdf/2502.19110"
          }
        ]
      },
      "Based on the search results, here's what I found about this paper:\n\n\"Geometry-Calibrated Conformal Abstention for Language Models\" proposes a post hoc framework, Conformal Abstention (CA), adapted from conformal prediction (CP) to determine whether to abstain from answering a query. \n\nThe motivation behind this work is that when language models lack relevant knowledge for a given query, they frequently generate plausible responses that can be hallucinations, rather than admitting being agnostic about the answer. Retraining models to reward admitting ignorance can lead to overly conservative behaviors and poor generalization due to scarce evaluation benchmarks.\n\nCA provides finite-sample guarantees on both the probability of participation (i.e., not abstaining) and the probability that the generated response is correct. Importantly, the abstention decision relies on prediction confidence rather than the non-conformity scores used in CP, which are intractable for open-ended generation. To better align prediction confidence with the model's ignorance, the paper introduces a calibration strategy using representation geometry within the model to measure knowledge.\n\nThe paper was published on April 30, 2026, and is authored by Rui Xu, Yi Chen, Sihong Xie, and Hui Xiong from Hong Kong University of Science and Technology."
    ],
    "durationSeconds": 8.286020489999967,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "35dc15cb-b42b-4a76-8b81-6e78e52bf422",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-30T06:57:30.876Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AGBYA9SCoGJx8PgPWtDcJE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.27914",
  "prompt": "Extract the full abstract. Does this paper address adversarial corpus poisoning in RAG? Does it handle retrieval corruption or only internal knowledge gaps? What are the key differences from TRAQ?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed94e85d-3e98-4ce2-8e25-0db9cc203c93",
  "isSidechain": false,
  "requestId": "req_011CbYKQtVhqSqy4CAAr1Bop",
  "type": "assistant",
  "uuid": "faf9c5f5-1b35-4819-ae68-55a04efdbf68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EJcCTuBLtsnzNejwRNRP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 59034,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 59034,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 144 · 2026-05-30T06:57:37.007Z_

<details><summary>↩ Tool result · `toolu_01AGBYA9SCoGJx8PgPWtDcJE`</summary>

```text
# Analysis of arXiv:2604.27914

## Full Abstract

"When language models lack relevant knowledge for a given query, they frequently generate plausible responses that can be hallucinations, rather than admitting being agnostic about the answer. Retraining models to reward admitting ignorance can lead to overly conservative behaviors and poor generalization due to scarce evaluation benchmarks. We propose a post hoc framework, Conformal Abstention (CA), adapted from conformal prediction (CP) to determine whether to abstain from answering a query. CA provides finite-sample guarantees on both the probability of participation (i.e., not abstaining) and the probability that the generated response is correct. Importantly, the abstention decision relies on prediction confidence rather than the non-conformity scores used in CP, which are intractable for open-ended generation. To better align prediction confidence with the model's ignorance, we introduce a calibration strategy using representation geometry within the model to measure knowledge involvement in shaping the response. Experiments demonstrate that we improve selective answering significantly with 75 percent conditional correctness."

## Regarding Your Questions

**Adversarial corpus poisoning in RAG:** The abstract makes no mention of RAG systems, retrieval augmentation, or adversarial poisoning attacks. This work focuses on addressing internal model hallucinations through selective abstention.

**Retrieval corruption vs. knowledge gaps:** The paper targets "internal knowledge gaps"—situations where models lack relevant information. It does not address retrieval-level corruption or poisoning.

**Comparison to TRAQ:** No reference to TRAQ appears in the provided content, making any comparative analysis impossible based on this document alone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faf9c5f5-1b35-4819-ae68-55a04efdbf68",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "d4567cc8-47fc-4c42-a52e-ab46f6a2ae36",
  "toolUseResult": {
    "bytes": 45759,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2604.27914\n\n## Full Abstract\n\n\"When language models lack relevant knowledge for a given query, they frequently generate plausible responses that can be hallucinations, rather than admitting being agnostic about the answer. Retraining models to reward admitting ignorance can lead to overly conservative behaviors and poor generalization due to scarce evaluation benchmarks. We propose a post hoc framework, Conformal Abstention (CA), adapted from conformal prediction (CP) to determine whether to abstain from answering a query. CA provides finite-sample guarantees on both the probability of participation (i.e., not abstaining) and the probability that the generated response is correct. Importantly, the abstention decision relies on prediction confidence rather than the non-conformity scores used in CP, which are intractable for open-ended generation. To better align prediction confidence with the model's ignorance, we introduce a calibration strategy using representation geometry within the model to measure knowledge involvement in shaping the response. Experiments demonstrate that we improve selective answering significantly with 75 percent conditional correctness.\"\n\n## Regarding Your Questions\n\n**Adversarial corpus poisoning in RAG:** The abstract makes no mention of RAG systems, retrieval augmentation, or adversarial poisoning attacks. This work focuses on addressing internal model hallucinations through selective abstention.\n\n**Retrieval corruption vs. knowledge gaps:** The paper targets \"internal knowledge gaps\"—situations where models lack relevant information. It does not address retrieval-level corruption or poisoning.\n\n**Comparison to TRAQ:** No reference to TRAQ appears in the provided content, making any comparative analysis impossible based on this document alone.",
    "durationMs": 6124,
    "url": "https://arxiv.org/abs/2604.27914"
  },
  "sourceToolAssistantUUID": "faf9c5f5-1b35-4819-ae68-55a04efdbf68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 145 · 2026-05-30T06:58:21.757Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the landscape. Let me synthesize my findings:

**Key observations from research:**

1. **The gap is confirmed**: No existing work combines conformal prediction + RAG + adversarial corpus poisoning + abstention. The intersection is indeed empty.

2. **Relevant concurrent work (benign setting only)**:
   - Conformal-RAG (2506.20978): Group-conditional conformal factuality for RAG, but no adversarial setting
   - CFC (2603.27403): Conditional factuality controlled LLMs, but no RAG poisoning
   - Geometry-Calibrated CA (2604.27914): Conformal abstention using representation geometry, but no RAG or poisoning
   - ExAUL (2506.14067): Online conformal abstention with adversarial bandit feedback, but not corpus poisoning
   - Principled Context Engineering (2511.17908): Conformal prediction for RAG context filtering, but no poisoning

3. **Diagnosis without solution**: Chen et al. (2603.16817) identifies CP-RAG failures under distribution shift but offers no remedies.

4. **Certified RAG defenses exist, but they lack conformal prediction and abstention mechanisms**.

5. **Poisoning-robust conformal prediction methods like RPS and CAS address calibration-set poisoning rather than test-time retrieval corruption**, which is the actual threat in RAG systems.

6. **The core mismatch**: Calibration poisoning (adversary corrupts labels in training data) differs fundamentally from RAG poisoning (adversarial documents injected into the corpus at test time).

7. I have several building blocks to work with—CRC's abstention calibration framework, RPS's partition-and-vote approach for isolating poisoned data, ReliabilityRAG's NLI agreement scoring, SCoRE's e-values for compositional guarantees, and Bayesian conformal prediction for data-conditional bounds.

8. The AAAI-27 main track deadline is July 28, 2026, giving me roughly two months—tight but workable if I scope the paper carefully.

Now I'm stepping back to think critically about whether this idea actually holds up.

A skeptical reviewer would push back on several fronts: whether the retrieval-agreement score is genuinely novel or just ReliabilityRAG's NLI approach wrapped in conformal prediction, whether formal guarantees can withstand adaptive adversaries who understand the defense, how the computational cost compares to existing methods, and whether simply combining RobustRAG with TRAQ would work just as well.

I should also consider whether simpler baselines might achieve similar results—like just abstaining when documents disagree without formal guarantees, or layering TRAQ on top of RobustRAG's output, though that second approach would likely fail since TRAQ assumes benign retrieval and RobustRAG's output isn't guaranteed correct under all poisoning levels.

The timing actually makes sense: the diagnosis paper is only two months old and surfaced the problem, while RobustRAG and ReliabilityRAG are recent enough to provide the certified defense framework needed as a foundation. The conformal tools like RPS and SCoRE only recently became available, and the distinction between calibration and retrieval poisoning hasn't been formally separated in the conformal prediction literature until now.

This addresses a genuine need—deployed RAG systems in enterprise search and medical QA are exposed to corpus poisoning, and having guarantees around abstention is critical for high-stakes applications where Chen et al. shows existing conformal methods break down under realistic conditions.

So the proposal is to build a poisoning-robust conformal abstention framework by designing nonconformity scores that measure disagreement across multiple independent response generations from partitioned document groups. The key insight is that poisoned documents create distinctive agreement patterns that we can detect, and we'd adapt the conformal calibration with a distribution-shift correction to maintain coverage guarantees even under bounded poisoning attacks. Now I'm pulling together the key inspirations—the diagnosis-solution pattern where identifying the gap in conformal abstention for adversarial RAG naturally motivates our approach, combined with RobustRAG's isolation and aggregation strategy paired with conformal calibration. Let me structure the final JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4567cc8-47fc-4c42-a52e-ab46f6a2ae36",
  "isSidechain": false,
  "requestId": "req_011CbYKReiWPabw5ke9SZhHe",
  "type": "assistant",
  "uuid": "36822e06-db30-4663-9294-367a0f5088b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYqG6YfxgTG6srtWqt6gLS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 59733,
      "output_tokens": 1732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1732,
          "cache_read_input_tokens": 59733,
          "cache_creation_input_tokens": 503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 503
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

_source line 146 · 2026-05-30T06:58:21.832Z_

Now let me do one final verification search to make sure no very recent paper (last 3 months) fills this exact gap:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36822e06-db30-4663-9294-367a0f5088b3",
  "isSidechain": false,
  "requestId": "req_011CbYKReiWPabw5ke9SZhHe",
  "type": "assistant",
  "uuid": "83ff54cd-c67d-4e5c-aa15-e4e0572fd18f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYqG6YfxgTG6srtWqt6gLS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 59733,
      "output_tokens": 1732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1732,
          "cache_read_input_tokens": 59733,
          "cache_creation_input_tokens": 503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 503
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

_source line 147 · 2026-05-30T06:58:22.315Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WbMNq5i4F1eGiV3i2wbsCR`</summary>

```json
{
  "query": "arxiv 2026 conformal prediction poisoning-robust RAG abstention retrieval-aware score certificate March April May"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83ff54cd-c67d-4e5c-aa15-e4e0572fd18f",
  "isSidechain": false,
  "requestId": "req_011CbYKReiWPabw5ke9SZhHe",
  "type": "assistant",
  "uuid": "fcf39f44-3597-4acb-a1b0-475974ebb134",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYqG6YfxgTG6srtWqt6gLS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 59733,
      "output_tokens": 1732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1732,
          "cache_read_input_tokens": 59733,
          "cache_creation_input_tokens": 503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 503
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

_source line 148_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "fcf39f44-3597-4acb-a1b0-475974ebb134",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 149_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Tool result

_source line 150 · 2026-05-30T06:58:39.011Z_

<details><summary>↩ Tool result · `toolu_01WbMNq5i4F1eGiV3i2wbsCR`</summary>

```text
Web search results for query: "arxiv 2026 conformal prediction poisoning-robust RAG abstention retrieval-aware score certificate March April May"

Links: [{"title":"[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/abs/2511.17908"},{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"[2407.09165] Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/abs/2407.09165"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"}]

I found several relevant papers. Let me search for more specific papers that might match your query more closely, particularly those with terms like "abstention," "retrieval-aware score," and "certificate."

Links: [{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/pdf/2503.05239"},{"title":"Streamlining Conformal Information Retrieval via Score Refinement","url":"https://arxiv.org/pdf/2410.02914"},{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/html/2503.05239v1"},{"title":"Conformal Prediction Sets with Improved Conditional Coverage using Trust   Scores","url":"https://arxiv.org/pdf/2501.10139"},{"title":"Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/html/2604.27914"},{"title":"[2605.25852] A Post-Processing Conformal Prediction Approach for Conditional Coverage via Pivotal Scores","url":"https://arxiv.org/abs/2605.25852"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"}]

Let me search more specifically for papers combining poisoning robustness with RAG and retrieval-aware approaches:

Links: [{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/html/2412.16708v2"},{"title":"[2605.10253v1] Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2605.10253v1"},{"title":"One Shot Dominance: Knowledge Poisoning Attack on Retrieval-Augmented Generation Systems","url":"https://arxiv.org/pdf/2505.11548"}]

Based on my search results, I found several relevant papers from arxiv in 2026 related to conformal prediction, RAG (Retrieval-Augmented Generation), and robustness, though I didn't find a single paper that matches all the exact terms in your search query. Here are some of the most relevant findings:

## Key Papers Found:

1. **Conformal Prediction for RAG Context Engineering** - A recent paper demonstrates that conformal filtering consistently meets its target coverage, ensuring that a specified fraction of relevant snippets are retained, and reduces retained context by 2-3x relative to unfiltered retrieval.

2. **Conformal Factuality for RAG-based LLMs (March 2026)** - A paper submitted March 17, 2026 titled "Is Conformal Factuality for RAG-based LLMs Robust?" examines conformal factuality guarantees. The paper finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and conformal factuality guarantee is not robust to distribution shifts and distractors.

3. **Conformal Abstention for Language Models** - A paper proposes Conformal Abstention, an approach grounded in conformal prediction that enables LLMs to admit a lack of knowledge, establishing two theoretical finite-sample guarantees: a participation guarantee bounding the probability that the model participates, and a conditional correctness guarantee.

4. **Robust RAG Against Poisoning Attacks (May 2026)** - A paper on knowledge poisoning attacks in medical multimodal RAG systems, posted May 11, 2026, proposes a knowledge-poisoning framework designed for medical multimodal RAG systems.

5. **Retrieval-Stage Defenses Against Corpus Poisoning** - RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.

While these papers address related topics, I didn't locate a single paper that precisely combines all the terms you specified (poisoning-robust, abstention, retrieval-aware score, and certificate in a single work).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcf39f44-3597-4acb-a1b0-475974ebb134",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "a71000b2-b59c-4438-b19d-731438f88995",
  "toolUseResult": {
    "query": "arxiv 2026 conformal prediction poisoning-robust RAG abstention retrieval-aware score certificate March April May",
    "results": [
      {
        "tool_use_id": "srvtoolu_011oBgCVqSsjEWQwtkrFFY6i",
        "content": [
          {
            "title": "[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/abs/2511.17908"
          },
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "[2407.09165] Robust Yet Efficient Conformal Prediction Sets",
            "url": "https://arxiv.org/abs/2407.09165"
          },
          {
            "title": "[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/abs/2603.16817"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          }
        ]
      },
      "I found several relevant papers. Let me search for more specific papers that might match your query more closely, particularly those with terms like \"abstention,\" \"retrieval-aware score,\" and \"certificate.\"",
      {
        "tool_use_id": "srvtoolu_01U7BAyTuFqbpTfmCW9Ub4KU",
        "content": [
          {
            "title": "Robust Conformal Prediction with a Single Binary Certificate",
            "url": "https://arxiv.org/pdf/2503.05239"
          },
          {
            "title": "Streamlining Conformal Information Retrieval via Score Refinement",
            "url": "https://arxiv.org/pdf/2410.02914"
          },
          {
            "title": "Robust Conformal Prediction with a Single Binary Certificate",
            "url": "https://arxiv.org/html/2503.05239v1"
          },
          {
            "title": "Conformal Prediction Sets with Improved Conditional Coverage using Trust   Scores",
            "url": "https://arxiv.org/pdf/2501.10139"
          },
          {
            "title": "Geometry-Calibrated Conformal Abstention for Language Models",
            "url": "https://arxiv.org/html/2604.27914"
          },
          {
            "title": "[2605.25852] A Post-Processing Conformal Prediction Approach for Conditional Coverage via Pivotal Scores",
            "url": "https://arxiv.org/abs/2605.25852"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/pdf/2405.01563"
          }
        ]
      },
      "Let me search more specifically for papers combining poisoning robustness with RAG and retrieval-aware approaches:",
      {
        "tool_use_id": "srvtoolu_01RUNMHKqCwmYYCKyRYyZjuK",
        "content": [
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/html/2412.16708v2"
          },
          {
            "title": "[2605.10253v1] Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2605.10253v1"
          },
          {
            "title": "One Shot Dominance: Knowledge Poisoning Attack on Retrieval-Augmented Generation Systems",
            "url": "https://arxiv.org/pdf/2505.11548"
          }
        ]
      },
      "Based on my search results, I found several relevant papers from arxiv in 2026 related to conformal prediction, RAG (Retrieval-Augmented Generation), and robustness, though I didn't find a single paper that matches all the exact terms in your search query. Here are some of the most relevant findings:\n\n## Key Papers Found:\n\n1. **Conformal Prediction for RAG Context Engineering** - A recent paper demonstrates that conformal filtering consistently meets its target coverage, ensuring that a specified fraction of relevant snippets are retained, and reduces retained context by 2-3x relative to unfiltered retrieval.\n\n2. **Conformal Factuality for RAG-based LLMs (March 2026)** - A paper submitted March 17, 2026 titled \"Is Conformal Factuality for RAG-based LLMs Robust?\" examines conformal factuality guarantees. The paper finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and conformal factuality guarantee is not robust to distribution shifts and distractors.\n\n3. **Conformal Abstention for Language Models** - A paper proposes Conformal Abstention, an approach grounded in conformal prediction that enables LLMs to admit a lack of knowledge, establishing two theoretical finite-sample guarantees: a participation guarantee bounding the probability that the model participates, and a conditional correctness guarantee.\n\n4. **Robust RAG Against Poisoning Attacks (May 2026)** - A paper on knowledge poisoning attacks in medical multimodal RAG systems, posted May 11, 2026, proposes a knowledge-poisoning framework designed for medical multimodal RAG systems.\n\n5. **Retrieval-Stage Defenses Against Corpus Poisoning** - RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.\n\nWhile these papers address related topics, I didn't locate a single paper that precisely combines all the terms you specified (poisoning-robust, abstention, retrieval-aware score, and certificate in a single work)."
    ],
    "durationSeconds": 16.690143345000106,
    "searchCount": 3
  },
  "sourceToolAssistantUUID": "fcf39f44-3597-4acb-a1b0-475974ebb134",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-30T06:58:41.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TqFeY4tedXbXCGpK9fzQDJ`</summary>

```json
{
  "query": "site:arxiv.org \"retrieval agreement\" conformal score RAG poisoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a71000b2-b59c-4438-b19d-731438f88995",
  "isSidechain": false,
  "requestId": "req_011CbYKWDmxgdkFVvoNj7JAH",
  "type": "assistant",
  "uuid": "e2ed0a7d-8cc2-4bc8-9645-317f29b3ee55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpKFwaf4PYmo6636WDNFqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3178,
      "cache_read_input_tokens": 60236,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 60236,
          "cache_creation_input_tokens": 3178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3178
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

_source line 152 · 2026-05-30T06:58:50.137Z_

<details><summary>↩ Tool result · `toolu_01TqFeY4tedXbXCGpK9fzQDJ`</summary>

```text
Web search results for query: "site:arxiv.org "retrieval agreement" conformal score RAG poisoning 2026"

Links: [{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning","url":"https://arxiv.org/html/2604.12201v1"},{"title":"Bias Amplification in RAG: Poisoning Knowledge Retrieval to Steer LLMs","url":"https://arxiv.org/html/2506.11415v1"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"CPA-RAG:Covert Poisoning Attacks on Retrieval-Augmented Generation in Large Language Models","url":"https://arxiv.org/pdf/2505.19864"},{"title":"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.18543"}]

I found several arxiv.org papers related to RAG poisoning from 2026, but the search results don't contain papers specifically matching all the terms "retrieval agreement" and "conformal score" together. Here's what I found:

The search returned papers on RAG poisoning attacks and defenses:

1. "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation" - which presents two defense mechanisms: RAGPart leverages document partitioning to mitigate poisoned points, while RAGMask identifies suspicious tokens based on similarity shifts under targeted token masking, with defenses consistently reducing attack success rates.

2. "AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning" (April 2026) - describes how a single adversarial document can significantly degrade reasoning accuracy by iteratively refining through LLM interactions.

3. "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems" - shows that a hybrid BM25 + vector retriever provides an effective architectural defense against gradient-guided RAG poisoning.

4. "RAG Security Bench (RSB)" - a unified benchmark that systematically evaluates poisoning attacks and defenses, including 13 representative poisoning attacks classified into targeted poisoning, denial-of-service, and trigger-based DoS categories.

None of these papers appear to specifically discuss "retrieval agreement" with "conformal score" - these specific terms may be in different papers or more recent publications not captured in this search result.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2ed0a7d-8cc2-4bc8-9645-317f29b3ee55",
  "isSidechain": false,
  "promptId": "7c700c4f-e74c-4047-93e0-80446752d943",
  "type": "user",
  "uuid": "bc7cc2bf-16e6-4def-aa35-c6eb05007f6b",
  "toolUseResult": {
    "query": "site:arxiv.org \"retrieval agreement\" conformal score RAG poisoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019N82oPibKLtCqoGRb15fpP",
        "content": [
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning",
            "url": "https://arxiv.org/html/2604.12201v1"
          },
          {
            "title": "Bias Amplification in RAG: Poisoning Knowledge Retrieval to Steer LLMs",
            "url": "https://arxiv.org/html/2506.11415v1"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/pdf/2603.18034"
          },
          {
            "title": "CPA-RAG:Covert Poisoning Attacks on Retrieval-Augmented Generation in Large Language Models",
            "url": "https://arxiv.org/pdf/2505.19864"
          },
          {
            "title": "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.18543"
          }
        ]
      },
      "I found several arxiv.org papers related to RAG poisoning from 2026, but the search results don't contain papers specifically matching all the terms \"retrieval agreement\" and \"conformal score\" together. Here's what I found:\n\nThe search returned papers on RAG poisoning attacks and defenses:\n\n1. \"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation\" - which presents two defense mechanisms: RAGPart leverages document partitioning to mitigate poisoned points, while RAGMask identifies suspicious tokens based on similarity shifts under targeted token masking, with defenses consistently reducing attack success rates.\n\n2. \"AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning\" (April 2026) - describes how a single adversarial document can significantly degrade reasoning accuracy by iteratively refining through LLM interactions.\n\n3. \"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems\" - shows that a hybrid BM25 + vector retriever provides an effective architectural defense against gradient-guided RAG poisoning.\n\n4. \"RAG Security Bench (RSB)\" - a unified benchmark that systematically evaluates poisoning attacks and defenses, including 13 representative poisoning attacks classified into targeted poisoning, denial-of-service, and trigger-based DoS categories.\n\nNone of these papers appear to specifically discuss \"retrieval agreement\" with \"conformal score\" - these specific terms may be in different papers or more recent publications not captured in this search result."
    ],
    "durationSeconds": 8.390632245000102,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e2ed0a7d-8cc2-4bc8-9645-317f29b3ee55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 153 · 2026-05-30T06:59:16.869Z_

<details><summary>Logged reasoning block</summary>

```text
My extensive search confirms the gap is real — no paper combines conformal prediction + RAG + adversarial corpus poisoning + abstention. The closest work:

1. **Conformal-RAG** (2506.20978): Group-conditional conformal factuality for RAG, but assumes benign retrieval
2. **CFC** (2603.27403): Conditional factuality control with conformal sampling, but no adversarial setting, no RAG
3. **Geometry-Calibrated CA** (2604.27914): Conformal abstention using representation geometry, but no RAG, no poisoning


4. **ExAUL** (2506.14067): Online conformal abstention with adversarial feedback, though not specifically for corpus poisoning
5. **Chen et al.** (2603.16817): Diagnoses how conformal factuality breaks under distribution shift in RAG but offers no solution
6. **RobustRAG** and **ReliabilityRAG**: Both provide certified defenses but lack conformal prediction or abstention mechanisms
7. **RPS** (2506.14067): Addresses poisoning-robust conformal prediction, but targets calibration poisoning rather than test-time retrieval corruption
8. **Principled Context Engineering** (2511.17908): Applies conformal prediction to RAG context filtering in benign settings only

No existing work combines conformal prediction with adversarial robustness for RAG abstention under corpus poisoning, so this is genuinely novel territory. Now I'm formulating the research direction: the core challenge is designing a system that can abstain from answering with distribution-free guarantees when the retrieval corpus itself has been adversarially poisoned, which violates the exchangeability assumption that conformal prediction relies on. The opportunity here is clear—Chen et al. identified the problem but left it unsolved, and the intersection of conformal prediction, RAG, adversarial robustness, and abstention remains completely unexplored.

I can build on existing techniques: RobustRAG's partition-and-aggregate strategy, CRC's monotone-loss calibration, RPS's majority-vote robustness, and ReliabilityRAG's NLI agreement structure all provide useful components. Looking at the landscape, TRAQ and C-RAG offer conformal guarantees for RAG but only under benign retrieval, while RobustRAG and ReliabilityRAG provide certified defenses without abstention mechanisms. RPS handles poisoning-robust conformal prediction but for calibration poisoning rather than retrieval corruption, and the recent work from Chen et al. and Conformal-RAG shows the field is actively grappling with these problems but hasn't yet solved the specific intersection I'm targeting.

The key insight is that no one's addressed the threat model mismatch between calibration poisoning and retrieval corruption in conformal prediction, and there's a clear gap for an abstention framework that handles adversarial corpus poisoning in RAG. I can adapt RobustRAG's isolate-then-aggregate approach with CRC's conformal risk control calibration, treating this as a cross-domain mechanism transfer where I adjust the threat model to fit the retrieval corruption setting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc7cc2bf-16e6-4def-aa35-c6eb05007f6b",
  "isSidechain": false,
  "requestId": "req_011CbYKX3PQXthAX52ryDthM",
  "type": "assistant",
  "uuid": "72818884-f7f3-481f-b7d6-e8dcae35807c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QM4fA3jNehbHdZPaXcYsg7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 63414,
      "output_tokens": 3361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3361,
          "cache_read_input_tokens": 63414,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 787
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

_source line 154 · 2026-05-30T07:00:02.123Z_

My research is now comprehensive. Let me synthesize everything into a well-grounded research direction.

## Research Summary

After **20+ targeted searches** and **5 deep paper reads**, I can confirm:

### Verified Gap Status
The intersection of {conformal prediction × RAG × adversarial corpus poisoning × abstention} is **completely empty** (0 papers found). This is a genuine, verified gap — not a guess.

### Closest Competing Work (all missing at least one component)
| Paper | CP | RAG | Poisoning | Abstention |
|-------|:--:|:---:|:---------:|:----------:|
| TRAQ (NAACL 2024) | ✓ | ✓ | ✗ | ✗ |
| C-RAG (ICML 2024) | ✓ | ✓ | ✗ | ✗ |
| RobustRAG (SaTML 2026) | ✗ | ✓ | ✓ | ✗ |
| ReliabilityRAG (NeurIPS 2025) | ✗ | ✓ | ✓ | ✗ |
| RPS (ICLR 2025 Spotlight) | ✓ | ✗ | ✓* | ✗ |
| Chen et al. (Mar 2026) | ✓ | ✓ | diag | ✗ |
| Conformal-RAG (Jun 2026) | ✓ | ✓ | ✗ | partial |
| Geometry-Cal. CA (Apr 2026) | ✓ | ✗ | ✗ | ✓ |
| ExAUL (Mar 2026) | ✓ | ✗ | ✗ | ✓ |

*RPS handles calibration poisoning, not retrieval corruption — a fundamentally different threat model.

### Venue Confirmed
AAAI-27 main track deadline: **July 28, 2026** (~2 months away). No SRRAI-specific track announced yet for AAAI-27, but the main track covers safety/robustness topics.

```json
[
  {
    "title": "Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores",
    "core_problem": "How can RAG systems abstain from answering with distribution-free correctness guarantees when the retrieval corpus is adversarially poisoned? Corpus poisoning breaks the exchangeability assumption that underlies all existing conformal prediction methods for RAG (TRAQ, C-RAG, Conformal-RAG), yet existing poisoning-robust CP (RPS) addresses calibration-set poisoning—a fundamentally different threat model from test-time retrieval corruption where adversarial documents are injected into the corpus and retrieved at inference time.",
    "opportunity": "Chen et al. (arXiv, Mar 2026) rigorously demonstrated that conformal factuality guarantees for RAG break under distribution shift and produce vacuous outputs at high confidence levels—but proposed no solution, creating a named, citable gap. Simultaneously, the building blocks for a solution have only recently become available: RobustRAG's partition-and-aggregate architecture (SaTML 2026) provides the isolation mechanism, CRC's monotone-loss framework (ICLR 2024) provides the calibration tool, and RPS's majority-vote robustness (ICLR 2025 Spotlight) provides the template for poisoning certificates. The key untried combination is adapting partition-and-vote from calibration poisoning to retrieval corruption: under k-document poisoning, partitioning retrieved passages into K groups ensures at most ⌈k/⌊n/K⌋⌉ groups are corrupted, bounding the TV distance between clean and poisoned nonconformity score distributions and enabling a CRC-style abstention threshold with formal coverage certificates.",
    "landscape": "TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG answer sets but assume benign retrieval—Chen et al. (Mar 2026) showed their guarantees break under distribution shift, with Non-Vacuous Empirical Factuality dropping substantially while prediction sets become vacuous. RobustRAG (SaTML 2026) and ReliabilityRAG (NeurIPS 2025) provide certified RAG defenses via isolate-then-aggregate and NLI-based MIS respectively, achieving certifiable robustness under bounded retrieval corruption but offering no abstention mechanism—when their defenses produce incorrect outputs, there is no fallback. RPS (ICLR 2025 Spotlight) provides poisoning-robust conformal prediction via smoothed scores and majority voting but explicitly assumes calibration-set poisoning (adversary corrupts labels in calibration data), not test-time retrieval corruption (adversary injects adversarial documents retrieved at inference)—the threat model mismatch means RPS's certificates do not transfer. Conformal-RAG (arXiv Jun 2026) provides group-conditional coverage for sub-claim factuality but assumes benign retrieval and does not address poisoning. The RSB benchmark (May 2025) evaluating 13 attacks and 7 defenses across NQ, HotpotQA, and MS-MARCO found that current defenses fail to provide robust protection, and CorruptRAG (2026) demonstrated 95% attack success with a single poisoned document, making agreement-based defenses especially challenged.",
    "inspired_by": "Field gap: 'No conformal abstention framework exists for RAG under adversarial corpus poisoning—the intersection of {conformal prediction, RAG, adversarial robustness, abstention} is completely empty.' Field gap: 'Threat model mismatch: existing poisoning-robust CP assumes calibration-set poisoning while RAG poisoning corrupts test-time retrieval—no work bridges this mismatch.' Innovation pattern: 'Cross-domain mechanism transfer with threat-model adaptation' (transferring partition-and-vote from calibration poisoning to retrieval corruption, diagnosing and resolving the exchangeability violation). Innovation pattern: 'Partition-isolate-aggregate for adversarial robustness' (used by RPS, RobustRAG, ReliabilityRAG—we adapt it for conformal score construction). Innovation pattern: 'Diagnosis paper creates demand, solution paper fills it' (Chen et al. 2026 creates the demand). Untried combination: 'RobustRAG's isolate-then-aggregate architecture + conformal risk control calibration—use RobustRAG's passage grouping as the isolation mechanism but replace its keyword/decoding voting with conformal-calibrated abstention decisions.'"
  }
]
```

Sources:
- [TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction](https://aclanthology.org/2024.naacl-long.210/)
- [RPS: Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning](https://arxiv.org/abs/2410.09878)
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556)
- [ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search](https://arxiv.org/abs/2509.23519)
- [Is Conformal Factuality for RAG-based LLMs Robust? (Chen et al. 2026)](https://arxiv.org/abs/2603.16817)
- [C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models](https://arxiv.org/abs/2402.03181)
- [Conformal-RAG: Conditional Conformal Factuality for RAG](https://arxiv.org/abs/2506.20978v1)
- [Conformal Risk Control (CRC)](https://arxiv.org/abs/2208.02814)
- [SCoRE: Selective Conformal Risk Control](https://arxiv.org/abs/2512.12844)
- [Geometry-Calibrated Conformal Abstention for Language Models](https://arxiv.org/abs/2604.27914)
- [ExAUL: Online Conformal Abstention with Adversarial Bandit Feedback](https://arxiv.org/abs/2506.14067)
- [Conformal Prediction as Bayesian Quadrature (ICML 2025 Outstanding)](https://arxiv.org/abs/2409.19712)
- [PoisonedRAG (USENIX Security 2025)](https://github.com/sleeepeer/PoisonedRAG)
- [Benchmarking Poisoning Attacks against RAG (RSB)](https://arxiv.org/abs/2505.18543)
- [Principled Context Engineering for RAG via Conformal Prediction](https://arxiv.org/abs/2511.17908)
- [Conditional Factuality Controlled LLMs (CFC)](https://arxiv.org/abs/2603.27403)
- [RAGPart & RAGMask: Retrieval-Stage Defenses](https://arxiv.org/abs/2512.24268)
- [Securing RAG: A Taxonomy of Attacks and Defenses](https://arxiv.org/abs/2604.08304)
- [AAAI-27 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [Conformal Prediction for NLP: A Survey](https://arxiv.org/abs/2405.01976)
- [Cherian et al. LLM Validity via Enhanced Conformal Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72818884-f7f3-481f-b7d6-e8dcae35807c",
  "isSidechain": false,
  "requestId": "req_011CbYKX3PQXthAX52ryDthM",
  "type": "assistant",
  "uuid": "37a2d650-fffe-4bde-a3a5-5621744b0ed4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QM4fA3jNehbHdZPaXcYsg7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 63414,
      "output_tokens": 3361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3361,
          "cache_read_input_tokens": 63414,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 787
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

_source line 155_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "37a2d650-fffe-4bde-a3a5-5621744b0ed4",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 156_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 157_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a rigorous ML research idea generator. Your job is to identify novel, well-grounded research directions by doing deep research first.  **Today's date: 2026-05-30 (UTC).** Use this when reasoni…",
  "leafUuid": "37a2d650-fffe-4bde-a3a5-5621744b0ed4",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---

### Runtime record

_source line 158_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate research direction for conformal RAG abstention",
  "sessionId": "768025f2-6d91-48cb-a9a0-91d27326c8a3"
}
```

---
