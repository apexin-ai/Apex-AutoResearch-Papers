# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/d6a46929-f053-493c-8f7d-5f148e2920f7.jsonl`
- **Structured JSON:** [`cc26d0fd87ac115fc70c.json`](../../sessions/cc/cc26d0fd87ac115fc70c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T05:38:41.400Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T05:38:41.400Z",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Machine Learning — Learning from Limited/Structured Data\n\nDirection: Use OMEGA's templated skill structure to construct a mathematical skill dependency DAG, identify under-covered compositional frontiers (novel but adjacent k-skill combinations), and synthesize targeted training data at those frontiers. The hypothesis is that systematic coverage of the compositional frontier — not random augmentation or generic RL — is required to break the scale-invariant +6% compositional ceiling. Evaluate whether skill-graph-guided data synthesis enables compositional generalization where scaling, RL, and curriculum learning all fail.\n\nSeed Papers:\n- OMEGA (Sun et al., NeurIPS 2025) — Primary benchmark: defines the +6% compositional ceiling across 40 templated generators, 6 math domains. Provides the skill taxonomy and evaluation infrastructure.\n- MASS: Mathematical Data Selection via Skill Graphs (ICML 2025) — Demonstrates skill graphs improve math data selection efficiency by 50-70%. Validates the skill-graph approach in math but does NOT target compositional generalization.\n- STEPS: Skill Taxonomy Guided Data Synthesis (arXiv Jan 2026) — Information-theoretic framework for compositional data synthesis via skill taxonomies. Validated on instruction-following, NOT math. Our direct methodological ancestor.\n- Scaling Can Lead to Compositional Generalization (Redhardt et al., NeurIPS 2025 Spotlight) — Proves coverage of task space enables generalization. Theoretical basis for why frontier-targeted synthesis should work, but provides no practical method for achieving coverage in math.\n- Can Models Learn Skill Composition from Examples? (Zhao & Kaur, NeurIPS 2024) — Shows k-skill fine-tuning generalizes to (k+1)-skill if data design is careful. Validates the data design matters, but uses manual composition.\n\nKnown Gaps:\n- MASS uses skill graphs for pretraining data selection efficiency, not for compositional frontier identification — nobody has used skill DAGs to find and fill gaps in compositional coverage.\n- STEPS targets instruction-following composition, not mathematical reasoning — the math-specific instantiation (skill extraction from OMEGA templates, mathematical coherence filtering) is untested.\n- No published method has been evaluated on OMEGA's compositional axis with targeted data interventions; all existing OMEGA results use RL or prompting.\n\nTheoretical Anchor: Redhardt et al. (NeurIPS 2025) prove that compositional generalization emerges when training distribution covers the compositional task space. OMEGA shows current training data does NOT cover the compositional frontier. STEPS' information-theoretic framework (maximizing marginal structural information in skill hierarchies) provides the selection principle. Together: coverage + information-maximizing selection over skill DAG = compositional generalization.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated 50-80 H100-hours for Qwen-7B fine-tuning + data generation)\n\nQuality Self-Checks:\n- [x] Core insight: Compositional generalization requires explicit coverage of the skill-composition frontier; random augmentation and RL cannot discover this structure.\n- [x] Why not obvious: MASS (skill graphs for math) and STEPS (taxonomy synthesis for composition) exist independently; nobody has combined them because MASS targets efficiency and STEPS targets instruction-following — the math-composition intersection requires domain-specific skill extraction from OMEGA templates.\n- [ ] Baseline fear test: CONCERN — a simple baseline of training on randomly sampled k-skill compositions (without the skill DAG structure) might achieve 60-80% of the improvement. The ablation comparing random vs. frontier-guided composition is the make-or-break experiment.\n- [x] Information exploited: The skill dependency structure encoded in OMEGA's 40 templated generators — specifically, which atomic skills are prerequisites for which compositions and which k-tuples are absent from training distributions.\n\nAvoid:\n- Framing as 'yet another data augmentation paper' — the contribution is the compositional frontier identification via skill DAGs, not the augmentation itself.\n- Overclaiming that this solves transformative generalization — OMEGA's transformative axis (novel strategies) is a fundamentally harder problem that skill-graph coverage cannot address.\n- Ignoring MASS as related work — MASS must be prominently cited and differentiated, or reviewers who know ICML 2025 will flag the omission.\n- Testing only on OMEGA — include MathTrap (EMNLP 2024) and AgentCoMa (2025) as secondary benchmarks to demonstrate the improvement is not benchmark-specific.\n\n## Paper analyses (18 papers)\n\n[\n  {\n    \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\",\n    \"venue\": \"Nature 2025\",\n    \"problem_identification\": \"Existing reasoning-capable LLMs depended on expensive human-annotated chain-of-thought data and fragile neural reward models prone to reward hacking at scale. They identified this by observing that process reward models are ill-defined for general reasoning and that Monte Carlo Tree Search fails in token-level search spaces.\",\n    \"key_insight\": \"Pure RL with only rule-based verifiable rewards (binary correctness + format compliance) — no SFT, no neural reward model — is sufficient to elicit sophisticated reasoning behaviors including self-verification and adaptive problem-solving.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"GRPO (Group Relative Policy Optimization) eliminates PPO's critic model by normalizing advantages relative to a group of G sampled completions per question: A_i = (r_i - mean(r)) / std(r). The full pipeline is four-stage: cold-start SFT on minimal CoT examples → reasoning-oriented RL with rule-based rewards → rejection sampling SFT (~800K samples) → all-scenario RL for alignment. Distillation into 1.5B–70B models uses 800K curated R1 outputs without RL on the student.\",\n    \"limitations_and_open_questions\": \"Distilled models show severe compositional degradation: 1.5B loses ~25 points on MATH and collapses on formal logic. Critics (oat-zero, Thoughtology) argue RL amplifies pre-existing base model patterns rather than inducing genuine novel reasoning — self-reflection exists at 'epoch 0' in most architectures.\",\n    \"building_blocks\": [\n      \"GRPO algorithm\",\n      \"Rule-based verifiable rewards\",\n      \"Cold-start SFT methodology\",\n      \"Distillation pipeline for reasoning models\",\n      \"DeepSeek-R1 distilled model family\"\n    ],\n    \"relevance_to_seed\": \"Defines the RL reasoning paradigm our method complements — distilled models' compositional degradation directly motivates skill-graph-guided data synthesis as an alternative to pure RL for compositional generalization.\"\n  },\n  {\n    \"title\": \"A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Prior theory established either sufficient or necessary conditions for compositional generalization but never both simultaneously — Wiedemer et al. (NeurIPS 2023) gave sufficient-only conditions, while Lippl & Stachenfeld showed fundamental limitations of kernel-theoretic approaches. Li identified the need for a complete characterization by observing the field lacked a unified diagnostic framework.\",\n    \"key_insight\": \"Compositional generalization requires an indivisible triple: the model's computational graph must align with the true compositional DAG, component mappings must be unambiguous on training data, AND components must encode minimally sufficient information — removing any one condition causes complete failure.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Formalizes compositional structure as a reference graph set (DAG of deterministic components) and requires structural isomorphism between model and reference graphs. Proves sufficiency via bottom-up structural induction over the DAG using a bijection lemma: unambiguous + minimized representation yields bijective component mappings. Achieves minimization via information bottleneck regularization (Gaussian noise injection + L2 penalty). Validates on XOR composition task showing each condition is independently essential.\",\n    \"limitations_and_open_questions\": \"The framework assumes compositional structure is known a priori — structural alignment cannot be learned from data alone. Validation is limited to synthetic XOR tasks; scaling to realistic mathematical reasoning with deep DAGs remains undemonstrated.\",\n    \"building_blocks\": [\n      \"Three-condition theoretical framework\",\n      \"Component-level coverage criterion (Definition 4)\",\n      \"Information bottleneck for minimized representation\",\n      \"Structural alignment as architectural design principle\"\n    ],\n    \"relevance_to_seed\": \"Provides the theoretical foundation for why skill-graph-guided coverage works: the component-level coverage criterion (all test component inputs seen in training) is precisely what frontier-targeted synthesis achieves over the skill DAG.\"\n  },\n  {\n    \"title\": \"ScaleQuest: Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch\",\n    \"venue\": \"ACL 2025\",\n    \"problem_identification\": \"Question-driven synthesis (WizardMath, MetaMath) is bounded by seed diversity, while knowledge-driven synthesis (KPMath, MathScale) requires expensive GPT-4 APIs. The authors observed the field was optimizing answer quality while treating the question distribution as fixed — questions, not answers, were the scaling bottleneck.\",\n    \"key_insight\": \"Instruction-tuned models possess latent question-generation capability from causal LM pretraining that can be cheaply activated via question-only fine-tuning (QFT), without needing seed questions, knowledge graphs, or proprietary models at generation time.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"QFT fine-tunes on ~15K problem texts (solutions stripped, EOS appended) for 1 epoch to activate question generation. QPO then applies DPO-style preference optimization using improved questions (from Llama-70B) as preferred vs. originals as dispreferred. A three-stage filter (language, solvability via model evaluation, difficulty scoring) removes ~48% of raw output. Final pipeline: 1M questions at $680 total, with responses scored by InternLM2-7B-Reward.\",\n    \"limitations_and_open_questions\": \"No analysis of compositional skill coverage — diversity is measured by topic embedding spread, not by systematic skill combination coverage. QPO still requires a 70B model for preference pairs, undermining the 'from scratch' framing. Effectiveness on models larger than 7B is untested.\",\n    \"building_blocks\": [\n      \"QFT activation technique\",\n      \"QPO for question preference optimization\",\n      \"Difficulty scoring via fail-rate regression\",\n      \"Cost-effective 7B-only synthesis pipeline\"\n    ],\n    \"relevance_to_seed\": \"Key baseline/competitor — achieves diversity through distributional sampling rather than structured skill coverage, making it the natural 'random augmentation' control against which frontier-guided synthesis must demonstrate clear compositional gains.\"\n  },\n  {\n    \"title\": \"MathCAMPS: Fine-grained Synthesis of Mathematical Problems From Human Curricula\",\n    \"venue\": \"ICLR 2025 (rejected, scores 5/6/6/6; revised for COLM 2025)\",\n    \"problem_identification\": \"Static benchmarks (GSM8K, MATH) face contamination opacity and aggregate metrics that mask dramatic per-skill variation. They identified this by noting that models with identical overall accuracy show 36% gaps on specific skills (e.g., Claude Opus vs. Sonnet on fraction addition).\",\n    \"key_insight\": \"Human educational curricula (Common Core Standards) already encode a hierarchical skill taxonomy that can be mechanized as attribute grammars to produce unlimited, provably-valid, contamination-free problems at arbitrary skill granularity.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"44 Common Core K-8 standards are encoded as non-terminals in an attribute grammar with 66 parameterized filters enforcing standard-specific constraints. Rejection sampling produces symbolic problems solved by SymPy, translated to natural language via GPT-4o few-shot prompting with 188 narrative themes. Cycle-consistency validation (back-translate and re-solve) achieves 97.7% faithfulness. Follow-up questions (counterfactual + incremental) probe compositional robustness.\",\n    \"limitations_and_open_questions\": \"Covers only 44/229 K-8 standards (19.2%) — too easy for frontier models. Reviewers criticized the GSM8K-only comparison and K-8 scope limitation. Critically, standards are treated independently with no inter-skill dependency modeling, leaving the compositional frontier unexplored.\",\n    \"building_blocks\": [\n      \"Attribute grammar encoding of math skills\",\n      \"Cycle-consistency validation pipeline\",\n      \"Skill-specific failure analysis methodology\",\n      \"Follow-up question generation (counterfactual/incremental)\"\n    ],\n    \"relevance_to_seed\": \"Most methodologically similar predecessor — the grammar-based skill encoding is a more rigorous alternative to embedding-based skill extraction, and the skill-specific failure findings validate that compositional frontiers exist, but the lack of inter-skill DAG modeling is exactly the gap our approach fills.\"\n  },\n  {\n    \"title\": \"OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data\",\n    \"venue\": \"NeurIPS 2024 MATH-AI Workshop / ICLR 2025 Poster\",\n    \"problem_identification\": \"Open-source math instruction data lagged behind proprietary datasets, and their predecessor OpenMathInstruct-1 had zero question diversity beyond MATH/GSM8K seeds. They diagnosed this through systematic ablations revealing that solution diversity yields diminishing returns while question diversity does not saturate.\",\n    \"key_insight\": \"Question diversity dominates solution diversity for sustained scaling of math SFT performance, and excessively verbose chain-of-thought solutions are actively harmful — their concise 'OpenMath CoT' format outperforms verbose alternatives by 3.9% absolute while being 40% shorter.\",\n    \"innovation_type\": \"scaling\",\n    \"method_summary\": \"Two-stage pipeline using Llama-3.1-405B-Instruct: (1) solution augmentation via few-shot prompting with answer-matching retention, (2) question augmentation via 5-shot prompting with subject-specific exemplars, validated by 32-sample majority voting. LLM-based decontamination catches paraphrased test items missed by n-gram methods. Yields 14M pairs (~600K unique questions) under CC-BY-4.0.\",\n    \"limitations_and_open_questions\": \"All questions derive from MATH/GSM8K distributions — augmentation generates 'similar' problems, not compositionally novel ones. The 70B model actually regressed on GSM8K and AIME without majority voting, suggesting the data composition favors smaller models. No skill-level coverage analysis exists.\",\n    \"building_blocks\": [\n      \"14M open-source math instruction dataset\",\n      \"Question augmentation via few-shot prompting\",\n      \"LLM-based decontamination pipeline\",\n      \"Empirical finding: concise > verbose solutions for SFT\"\n    ],\n    \"relevance_to_seed\": \"Provides the baseline data infrastructure — skill-graph-guided selection (à la MASS) could be applied directly to OpenMathInstruct-2's 600K questions to identify compositional frontier gaps, making it the natural corpus for our data selection experiments.\"\n  },\n  {\n    \"title\": \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\",\n    \"venue\": \"NeurIPS 2025 (Oral / Best Paper Runner-up, perfect 6/6/6/6 scores)\",\n    \"problem_identification\": \"The field assumed RLVR creates new reasoning capabilities in LLMs, but no rigorous study had tested whether RL-trained models can solve problems their base models fundamentally cannot. The authors identified this gap by shifting from pass@1 (sampling efficiency) to pass@k at large k (reasoning boundary).\",\n    \"key_insight\": \"RLVR does not expand the reasoning frontier—it merely biases the sampling distribution toward already-existing rewarded paths, making the base model a hard upper bound on reasoning capability.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Used pass@k (k up to 1024) as a boundary probe across 6 RL algorithms (PPO, GRPO, Reinforce++, RLOO, ReMax, DAPO), 3 model families (Qwen2.5, LLaMA-3.1, DeepSeek-R1), and math/code/vision tasks. At large k, base models match or exceed RL-trained variants (e.g., 9% higher on Minerva-32B at k=128). On AIME24, 0% of problems were solved exclusively by RL models vs. 13.3% exclusively by base. Perplexity analysis confirmed RL outputs already lie in the base model's distribution. Distillation, by contrast, genuinely introduced new reasoning paths.\",\n    \"limitations_and_open_questions\": \"Analysis uses finite k—theoretically, RL could locate astronomically low-probability paths. Restricted to single-turn tasks with binary rewards on open-weight models; proprietary systems (o1) remain a black box.\",\n    \"building_blocks\": [\n      \"pass@k as reasoning boundary metric\",\n      \"coverage analysis methodology for RL vs base models\",\n      \"distillation as capability expansion baseline\"\n    ],\n    \"relevance_to_seed\": \"Directly motivates our data-centric approach: if RL cannot create new reasoning patterns (only redistribute existing ones), then compositional generalization requires injecting new compositional training data—exactly what skill-graph-guided frontier synthesis provides.\"\n  },\n  {\n    \"title\": \"Exploring the Compositional Deficiency of Large Language Models in Mathematical Reasoning Through Trap Problems\",\n    \"venue\": \"EMNLP 2024\",\n    \"problem_identification\": \"No benchmark existed to isolate compositional failure in math reasoning from general math difficulty. The authors realized that inserting logical traps into known-solvable problems creates a clean test: models possess both component skills (math solving + trap detection) but fail to compose them.\",\n    \"key_insight\": \"LLMs possess all requisite component knowledge yet fail to spontaneously compose it for novel combinations—compositional deficiency is structural, not a knowledge gap.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Constructed MathTrap by embedding 5 trap types (concept undefined 16%, missing condition 6%, direct contradiction 24%, indirect contradiction 38%, common-sense violation 15%) into MATH/GSM8K problems. Each item is a triplet: original problem, conceptual trap test, and composed trap problem. GPT-4 drops from 70.3% to 36.0% on trap problems (51.2% ratio); Claude-3.5 drops to 25.9% ratio; humans maintain 85.9% ratio. Fine-tuning on 1K trap examples improves trap accuracy but degrades original accuracy, revealing a composition-forgetting tradeoff.\",\n    \"limitations_and_open_questions\": \"Small dataset (155 private triplets); trap insertion is semi-manual limiting scalability. Does fine-tuning on compositional traps generalize to other composition types, or is it trap-type-specific?\",\n    \"building_blocks\": [\n      \"MathTrap benchmark for compositional math evaluation\",\n      \"triplet evaluation design (original/component/composed)\",\n      \"taxonomy of 5 mathematical trap types\"\n    ],\n    \"relevance_to_seed\": \"MathTrap serves as our secondary evaluation benchmark, providing direct evidence of compositional deficiency in math. The composition-forgetting tradeoff during fine-tuning motivates our structured frontier-coverage approach over naive augmentation.\"\n  },\n  {\n    \"title\": \"DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"Discovered severe easy-query bias in math SFT datasets: 51.1% of the hardest MATH queries received zero synthetic responses in standard rejection sampling, while easy queries were massively over-represented. This was identified through systematic fail-rate analysis of existing rejection tuning pipelines.\",\n    \"key_insight\": \"Data difficulty distribution matters more than data volume—allocating synthesis trials proportionally to query difficulty yields better models from smaller datasets than uniform sampling from larger ones.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Proposed two Difficulty-Aware Rejection Sampling strategies: DARS-Uniform (equalizes correct responses per query at k_u=40) and DARS-Prop2Diff (allocates up to k_p=192 responses for hardest queries). Uses fail-rate from n_d samples as an automatic difficulty metric. All synthesis uses open-source DeepSeekMath-7B-RL (no GPT-4). ~590K examples from GSM8K/MATH training queries. Llama3-8B gains +6.9% on MATH (39.7→46.6%) and +4-5 points on out-of-domain benchmarks, matching models trained on 4× more data.\",\n    \"limitations_and_open_questions\": \"Difficulty is defined per-query, not per-skill-composition—DART cannot distinguish whether a hard problem is hard because of novel skill combinations vs. inherent single-skill complexity. Does difficulty-awareness compose with compositional coverage?\",\n    \"building_blocks\": [\n      \"fail-rate as automatic difficulty metric\",\n      \"DARS-Uniform and DARS-Prop2Diff sampling strategies\",\n      \"demonstration that open-source-only synthesis can match proprietary pipelines\"\n    ],\n    \"relevance_to_seed\": \"Validates the principle that targeted data curation outperforms volume. Our approach extends this from difficulty-awareness to composition-awareness: rather than asking 'how hard is this query?', we ask 'which skill compositions are under-covered?' DART's methodology could be combined with our frontier sampling.\"\n  },\n  {\n    \"title\": \"RV-Syn: Rational and Verifiable Mathematical Reasoning Data Synthesis based on Structured Function Library\",\n    \"venue\": \"EACL 2026\",\n    \"problem_identification\": \"Existing math data synthesis methods either lack solution verifiability (LLM-generated solutions may be wrong) or fail to capture the logical structure of problems (random augmentation doesn't control skill composition). The gap: no method jointly ensures correctness via execution and controls compositional structure via explicit function graphs.\",\n    \"key_insight\": \"Decomposing math problems into executable computational graphs of typed functions enables synthesis that is simultaneously verifiable (graphs execute to ground truth) and compositionally controllable (novel function combinations produce novel problems).\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Three-stage pipeline: (1) Decompose seed problems into Python function sequences, merge redundant functions (~28% reduction) via AST+semantic similarity, and organize into a graph with co-occurrence and topic edges. (2) Sample function subsets via three strategies (co-occurrence, topic-based, edgeless) to balance familiarity and novelty, then compose into computational graphs. (3) Execute graphs for ground-truth answers, back-translate into NL problems via LLM, and filter by answer-match verification. Achieves 6.3% SOTA gain on LLaMA-3-8B with 50K data (vs. competitors' 100K), 0.9% problem error rate vs. 4.9-10.6% for baselines.\",\n    \"limitations_and_open_questions\": \"Function library is derived from seed problems, potentially limiting coverage to seed-distribution skills. The edgeless sampling strategy (novel combinations) is not systematically guided by a coverage criterion—how much of the compositional frontier does it actually cover?\",\n    \"building_blocks\": [\n      \"structured function library from seed decomposition\",\n      \"computational graph as verifiable solution representation\",\n      \"three-strategy sampling (co-occurrence/topic/edgeless) for composition control\",\n      \"back-translation from graphs to NL problems\"\n    ],\n    \"relevance_to_seed\": \"RV-Syn's function library is structurally analogous to OMEGA's skill templates, and its graph-based composition mirrors our proposed skill-DAG-guided synthesis. Key difference: RV-Syn samples compositions without explicit frontier identification—adding our coverage-maximizing selection over the function graph would directly extend their approach.\"\n  },\n  {\n    \"title\": \"Skill-it! A Data-Driven Skills Framework for Understanding and Training Language Models\",\n    \"venue\": \"NeurIPS 2023 (Spotlight)\",\n    \"problem_identification\": \"Training data selection treated all skills as independent, ignoring that skills have prerequisite dependencies (learning skill B is easier after mastering skill A). No framework existed to discover and exploit these orderings for data-efficient LLM training.\",\n    \"key_insight\": \"Language models follow a natural skill acquisition order analogous to human learning—formalizing and exploiting prerequisite relationships between skills via a learned skill graph enables dramatically more data-efficient training.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Defines skills as data partitions with associated loss functions. Constructs a skill graph by measuring how training on skill A's data reduces loss on skill B (prerequisite edges). The SKILL-IT online algorithm iteratively adjusts the training data mixture based on: (1) current per-skill evaluation loss and (2) adjacency structure from the skill graph, upweighting prerequisites of underperforming skills. On LEGO synthetic data: +36.5 accuracy points over random sampling. On Natural Instructions fine-tuning: 13.6% validation loss reduction. On RedPajama 1B-token pretraining: outperforms 3B-token random baseline on LM Eval Harness.\",\n    \"limitations_and_open_questions\": \"Skill definitions require human specification or clustering—automatic skill discovery at scale is unaddressed. The skill graph captures prerequisites but not compositional relationships (A+B→C). Does the framework extend from single-skill ordering to multi-skill composition?\",\n    \"building_blocks\": [\n      \"skill graph construction via cross-skill loss reduction\",\n      \"online data mixture algorithm exploiting prerequisite structure\",\n      \"formalization of ordered skill sets for LLMs\"\n    ],\n    \"relevance_to_seed\": \"Conceptual ancestor of our approach: Skill-it proved that skill DAGs improve training efficiency, but targets single-skill ordering, not compositional frontier coverage. Our work extends the skill graph from prerequisite ordering to compositional frontier identification—from 'what order to learn skills' to 'which skill combinations are missing.'\"\n  },\n  {\n    \"title\": \"How Does RL Post-training Induce Skill Composition? A Case Study on Countdown\",\n    \"venue\": \"NeurIPS 2025 Workshops (Efficient Reasoning Spotlight, MATH-AI Poster)\",\n    \"problem_identification\": \"Prior work conflated compositional generalization with length generalization in RL-trained LLMs; no study had decomposed *what structures* RL learns and in what order. The authors identified this gap by noting that pass@k metrics obscure structural mastery patterns.\",\n    \"key_insight\": \"RL induces a structure-dependent learning hierarchy — balanced expression trees are mastered before unbalanced ones — due to a 'lookahead bottleneck' where autoregressive models must commit to root operators before generating complex right subtrees.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Solutions to Countdown (find arithmetic expressions evaluating to a target) are parsed into canonical binary expression trees, classified by shape signatures ([left_size]∘[right_size]). Models (Qwen-2.5 1.5B–7B) are trained via GRPO on n∈{3,4} with balanced pattern sampling, then evaluated OOD on n∈{5,6} and held-out tree shapes. Key ablations compare RL vs. SFT learning dynamics, GRPO vs. PPO, and the effect of withholding entire pattern families during training.\",\n    \"limitations_and_open_questions\": \"Validated only on Countdown — transferability to multi-step mathematical reasoning, theorem proving, or realistic compositional tasks is unknown. No curriculum or data design intervention was tested, leaving open whether structure-aware training data could accelerate or reorder the hierarchy.\",\n    \"building_blocks\": [\n      \"Expression-tree decomposition of solutions into compositional skill atoms\",\n      \"Shape-signature taxonomy for classifying compositional complexity\",\n      \"Balanced pattern sampling methodology to remove distributional confounds\",\n      \"Evidence that RL produces genuine compositional reuse (not memorization)\"\n    ],\n    \"relevance_to_seed\": \"Directly validates our hypothesis that compositional structure matters more than scale — their finding that certain tree shapes resist learning even with RL motivates targeted data synthesis at those specific compositional frontiers rather than relying on RL alone.\"\n  },\n  {\n    \"title\": \"MathGAP: Out-of-Distribution Evaluation on Problems with Arbitrarily Complex Proofs\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"Existing math benchmarks conflate data contamination with generalization failure and lack systematic control over proof complexity. The authors formalized the gap: no evaluation framework independently varies depth, width, shape, and ordering of mathematical proof structures.\",\n    \"key_insight\": \"Performance degradation is governed by proof tree *structure* (nonlinear >> linear, deep >> shallow) rather than surface features, and nonlinear proofs approach zero accuracy even for frontier models — revealing that compositional proof reasoning, not arithmetic, is the bottleneck.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"MathGAP generates problems via a three-step pipeline: (1) top-down recursive proof tree sampling with controlled depth/width/shape parameters using five logical form predicates, (2) template-based conversion of leaf axioms to natural language sentences, (3) post-order traversal to produce chain-of-thought traces. Evaluated on Mixtral-8x7B, Llama3-8B/70B, GPT-3.5/4o, o1-preview, and DeepSeek-R1 across ~400-problem test sets per configuration.\",\n    \"limitations_and_open_questions\": \"Limited to arithmetic word problems with fixed logical form predicates — unclear if the framework extends to algebraic, geometric, or multi-domain math. The template-based NL generation may introduce artifacts that models exploit rather than reason through.\",\n    \"building_blocks\": [\n      \"Parameterized proof tree generation with independent depth/width/shape control\",\n      \"Methodology for contamination-free OOD evaluation\",\n      \"Quantitative evidence that nonlinear proof structures are the hardest compositional axis\",\n      \"Complementary evaluation framework for measuring compositional math generalization\"\n    ],\n    \"relevance_to_seed\": \"Provides a complementary evaluation methodology to OMEGA — while OMEGA measures compositional generalization via skill combinations, MathGAP measures it via proof tree complexity, enabling us to validate that skill-DAG-guided synthesis improves generalization along both axes.\"\n  },\n  {\n    \"title\": \"SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"Open-source RL replication efforts concentrated on math/code, leaving general logical reasoning under-resourced due to the difficulty of collecting diverse, *verifiable* reasoning data. The authors identified that logical reasoning is a foundational building block that transfers cross-domain but lacked a scalable synthesis pipeline.\",\n    \"key_insight\": \"Structured synthetic logical reasoning data with rule-based verification enables RL training that transfers to unseen mathematical domains — logic-only training improves AIME by ~10 points, suggesting shared abstract reasoning mechanisms exploitable via data mixing.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"35 diverse logic tasks (puzzles, constraint satisfaction, deduction) are implemented as programmatic generators with task-specific difficulty parameters calibrated to a dual-bound (lower: pass rate 0–0.5 for base models; upper: pass@10 > 0 for frontier models). Each task has a dedicated rule-based verifier providing binary rewards. Models (Qwen2.5-7B/32B) are trained via GRPO with data mixing strategies (logic+math, logic+code, all three). SynLogic-Hard uses all 35 tasks; SynLogic-Easy excludes 8 tasks beyond 7B capacity.\",\n    \"limitations_and_open_questions\": \"Reviewer scores were borderline (5/4/4/4/4 on 6-point NeurIPS scale). The difficulty calibration is model-dependent and may not generalize. Cross-domain transfer is demonstrated but the mechanism (shared reasoning primitives vs. longer CoT) is not disentangled. No evaluation on compositional generalization specifically.\",\n    \"building_blocks\": [\n      \"Dual-bound difficulty calibration methodology\",\n      \"Rule-based verification for RL reward across 35 task types\",\n      \"Evidence that logic+math data mixing improves sample efficiency\",\n      \"Open-source synthesis pipeline and dataset\"\n    ],\n    \"relevance_to_seed\": \"Validates that structured synthetic data with verifiable rewards and controllable difficulty improves generalization across domains — our approach applies the same principle (structured generation + verification) but targets the compositional skill frontier specifically rather than broad logical reasoning coverage.\"\n  },\n  {\n    \"title\": \"Key-Point-Driven Data Synthesis with its Enhancement on Mathematical Reasoning\",\n    \"venue\": \"AAAI 2025\",\n    \"problem_identification\": \"Math reasoning training data is scarce and existing synthesis methods either rephrase seed problems (limited novelty) or generate from knowledge bases (distribution mismatch). The authors identified that grounding synthesis in extracted 'key points' — essential theorems/methods — preserves authentic data distributions while enabling novel question generation.\",\n    \"key_insight\": \"Decomposing math problems into topic + key-point pairs and using a topic co-occurrence probability matrix to sample multi-topic combinations generates genuinely novel problems that remain distributionally aligned with authentic data — a middle ground between augmentation and unconstrained generation.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"GPT-4 extracts topics and key points from seed problems (GSM8K, MATH), which are deduplicated via embedding similarity. A Topic Co-occurrence Probability Matrix (TCPM) guides sampling of 2–3 topic combinations. GPT-4 generates novel questions conditioned on sampled topics, key points, and exemplar practices. Quality control uses GPT-4 scoring (≥0.85 threshold, ~51% pass rate) and consensus voting over 10 nucleus-sampled solutions verified via SymPy equivalence. Produces KPMath (800K+) and KPMath-Plus (1.576M total).\",\n    \"limitations_and_open_questions\": \"Heavy reliance on GPT-4 for extraction, generation, and scoring creates cost barriers and potential capability ceiling. The TCPM captures co-occurrence but not prerequisite/dependency structure — key points are treated as flat, not hierarchical. No evaluation of compositional generalization or OOD performance.\",\n    \"building_blocks\": [\n      \"Key-point extraction as a structured skill decomposition analog\",\n      \"Topic co-occurrence probability matrix for principled combination sampling\",\n      \"Consensus voting with symbolic equivalence checking for quality filtering\",\n      \"Demonstrated scalability to 800K+ high-quality math QA pairs\"\n    ],\n    \"relevance_to_seed\": \"The key-point extraction pipeline is a direct methodological precursor to our skill extraction from OMEGA templates — but KPDDS uses flat co-occurrence rather than a dependency DAG, and targets training data volume rather than compositional frontier coverage, precisely the gap our approach fills.\"\n  },\n  {\n    \"title\": \"Compositional Generalization from Learned Skills via CoT Training: A Theoretical and Structural Analysis for Reasoning\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"No mechanistic explanation existed for WHY CoT training enables compositional generalization — prior work showed CoT helps but treated it as a black box. Yao et al. identified this gap by noting the disconnect between empirical CoT success and the absence of circuit-level or distributional analysis of how composition emerges.\",\n    \"key_insight\": \"CoT training creates a two-stage compositional circuit where shallow layers resolve intermediate entities (first hop), freeing deeper layers to specialize in subsequent reasoning steps — the number of internal circuit stages directly corresponds to explicit reasoning steps during training.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Uses synthetic multi-hop fact completion (entities, relations, 2-hop compositions) with controlled ID/OOD splits to isolate compositional generalization. Employs logit lens and causal tracing to identify a two-stage circuit: Stage 1 retrieves bridge entities at layers 3-5, Stage 2 processes autoregressively at layer 8. Parameter λ controls multi-hop/single-hop ratio; noise analysis (ξ=0.05→97.8% OOD, ξ=0.4→49.1%) quantifies robustness. Validated on Llama2-7B with Wikidata two-hop queries via LoRA.\",\n    \"limitations_and_open_questions\": \"Models trained on 2-hop CoT cannot generalize to 3-hop — the circuit structure is fixed to training-time depth. Synthetic triplet setup is far simpler than real math composition; unclear if the same circuit pattern holds for mathematical skill composition with heterogeneous skill types.\",\n    \"building_blocks\": [\n      \"Logit lens / causal tracing methodology for analyzing compositional circuits\",\n      \"ID/OOD decomposition framework with λ-controlled distributional shifts\",\n      \"Noise robustness analysis protocol for CoT intermediate steps\"\n    ],\n    \"relevance_to_seed\": \"Provides theoretical grounding that CoT-based training enables compositional generalization through learned circuits — directly supports our hypothesis that models CAN compose skills if trained with proper compositional coverage, and explains WHY frontier-targeted data (covering the compositional space) should work mechanistically.\"\n  },\n  {\n    \"title\": \"AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Existing compositional reasoning benchmarks test multi-step reasoning of the SAME type (e.g., multi-hop math); no benchmark measured the compositionality gap when mixing DIFFERENT reasoning types (commonsense + math) in realistic agentic scenarios.\",\n    \"key_insight\": \"The compositional failure is cross-type, not just cross-step: LLMs solve commonsense and math independently but lose ~30% accuracy when combining them, even when each isolated step succeeds — revealing a type-composition gap distinct from depth-composition gaps.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Constructs tasks across 5 real-world domains (house working, web shopping, science experiments, smart assistant, travel agent) where each requires both a commonsense step and a math step. Evaluates 61 LLMs using three metrics: all-steps-correct (isolated), composition accuracy, and the gap between them. Includes interpretability analysis via neuron patterns, attention maps, and membership inference to diagnose failure modes.\",\n    \"limitations_and_open_questions\": \"Limited to binary composition (commonsense + math); doesn't test k>2 skill compositions or compositions within math subtypes. As a secondary benchmark for our work, the commonsense component may not directly reflect pure mathematical compositional generalization — the gap may conflate cross-type integration difficulty with genuine compositional failure.\",\n    \"building_blocks\": [\n      \"Compositionality gap metric (isolated vs. composed accuracy)\",\n      \"Multi-domain agentic task templates combining heterogeneous reasoning\",\n      \"61-model evaluation infrastructure with interpretability diagnostics\"\n    ],\n    \"relevance_to_seed\": \"Serves as a secondary evaluation benchmark demonstrating that compositional failures persist across 61 LLMs and are not benchmark-specific — validates our core premise that composition is systematically hard, though the commonsense+math axis is orthogonal to OMEGA's intra-mathematical composition.\"\n  },\n  {\n    \"title\": \"MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy\",\n    \"venue\": \"AAAI 2026\",\n    \"problem_identification\": \"Existing math data synthesis either mutates existing problems (risking contamination and limited novelty) or uses unconstrained generation (producing trivial/unsolvable problems). MathSmith identified that the key bottleneck is generating genuinely NOVEL hard problems with guaranteed solvability.\",\n    \"key_insight\": \"Concept-pair sampling from PlanetMath (11K concepts) combined with RL-optimized difficulty strategies creates a generate-from-scratch pipeline that decouples problem novelty from existing problem sets, using answer consistency across multiple teacher samples as a solvability filter.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Samples concept-explanation pairs from PlanetMath, applies ≥2 of 9 difficulty strategies (multi-step reasoning, cross-topic integration, implicit logic, distractors, abstract modeling, multiple solution paths, advanced manipulation, extreme conditions, non-standard representation) as soft constraints. Uses GRPO to optimize composite reward: r_structure (format validity α=0.7 + step count α=0.3) + r_reasoning (complexity via CoT length β=0.7 + answer consistency via K=5 majority voting β=0.3). Three-stage pipeline: SFT → Hard → HC, achieving 95.4% usability ratio.\",\n    \"limitations_and_open_questions\": \"Difficulty is proxied by CoT length, which conflates verbosity with genuine reasoning depth. The concept-pair approach targets individual problem hardness, NOT compositional coverage — there's no mechanism to identify which concept COMBINATIONS are underrepresented. This is the critical gap our skill-DAG approach fills.\",\n    \"building_blocks\": [\n      \"PlanetMath concept-pair extraction pipeline (11K concepts)\",\n      \"9 difficulty strategy taxonomy as generation constraints\",\n      \"Multi-objective RL reward combining structural validity, complexity, and consistency\",\n      \"GRPO-based policy optimization for math problem generation\"\n    ],\n    \"relevance_to_seed\": \"Directly competing approach at same venue (AAAI 2026) — MathSmith targets problem DIFFICULTY via RL while our approach targets compositional COVERAGE via skill DAGs. Key differentiation: MathSmith's concept pairs lack dependency structure and don't identify frontier compositions; our method is complementary (could use MathSmith's generation pipeline to synthesize problems AT identified frontier nodes).\"\n  },\n  {\n    \"title\": \"More Data or Better Data? A Critical Analysis of Data Selection and Synthesis for Mathematical Reasoning\",\n    \"venue\": \"EMNLP 2025 (Industry Track)\",\n    \"problem_identification\": \"Despite proliferation of math data construction methods, no unified comparison existed under realistic deployment conditions — each method was evaluated in isolation with different models, metrics, and mixing strategies, making actionable guidance impossible.\",\n    \"key_insight\": \"Data structure (interpretable formatting, LaTeX, clear definitions) and source quality (distillation from reasoning models like QwQ-32B) consistently dominate data volume — rule-based scaling and retrieval augmentation provide negligible gains, while distilled data yields +8.96 MATH accuracy.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Evaluates open-source datasets (web-scraped, curated, specialized) and synthesis techniques (prompt-based reformatting, model distillation, weakness-guided augmentation, textbook extraction) under a unified annealing pipeline mixing new data at 20% with baseline data. Tests on DeepSeek-V2-Lite and Qwen2.5-3B across MMLU, GSM8K, MATH, MathBench, and HumanEval. Key quantitative findings: Math-Cosmo (structured formatting) +1.72 MATH, NaturalReasoning-QwQ (distillation) +1.92 MATH, OpenR1-Math-220K (scaled distillation) +8.96 MATH.\",\n    \"limitations_and_open_questions\": \"Analysis is limited to small models (3B-16B) in an industrial annealing setup — un\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T05:38:41.403Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T05:38:41.403Z",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-29T05:38:41.417Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-29 (UTC).**

## Research area: Target: AAAI 2026
Track: Machine Learning — Learning from Limited/Structured Data

Direction: Use OMEGA's templated skill structure to construct a mathematical skill dependency DAG, identify under-covered compositional frontiers (novel but adjacent k-skill combinations), and synthesize targeted training data at those frontiers. The hypothesis is that systematic coverage of the compositional frontier — not random augmentation or generic RL — is required to break the scale-invariant +6% compositional ceiling. Evaluate whether skill-graph-guided data synthesis enables compositional generalization where scaling, RL, and curriculum learning all fail.

Seed Papers:
- OMEGA (Sun et al., NeurIPS 2025) — Primary benchmark: defines the +6% compositional ceiling across 40 templated generators, 6 math domains. Provides the skill taxonomy and evaluation infrastructure.
- MASS: Mathematical Data Selection via Skill Graphs (ICML 2025) — Demonstrates skill graphs improve math data selection efficiency by 50-70%. Validates the skill-graph approach in math but does NOT target compositional generalization.
- STEPS: Skill Taxonomy Guided Data Synthesis (arXiv Jan 2026) — Information-theoretic framework for compositional data synthesis via skill taxonomies. Validated on instruction-following, NOT math. Our direct methodological ancestor.
- Scaling Can Lead to Compositional Generalization (Redhardt et al., NeurIPS 2025 Spotlight) — Proves coverage of task space enables generalization. Theoretical basis for why frontier-targeted synthesis should work, but provides no practical method for achieving coverage in math.
- Can Models Learn Skill Composition from Examples? (Zhao & Kaur, NeurIPS 2024) — Shows k-skill fine-tuning generalizes to (k+1)-skill if data design is careful. Validates the data design matters, but uses manual composition.

Known Gaps:
- MASS uses skill graphs for pretraining data selection efficiency, not for compositional frontier identification — nobody has used skill DAGs to find and fill gaps in compositional coverage.
- STEPS targets instruction-following composition, not mathematical reasoning — the math-specific instantiation (skill extraction from OMEGA templates, mathematical coherence filtering) is untested.
- No published method has been evaluated on OMEGA's compositional axis with targeted data interventions; all existing OMEGA results use RL or prompting.

Theoretical Anchor: Redhardt et al. (NeurIPS 2025) prove that compositional generalization emerges when training distribution covers the compositional task space. OMEGA shows current training data does NOT cover the compositional frontier. STEPS' information-theoretic framework (maximizing marginal structural information in skill hierarchies) provides the selection principle. Together: coverage + information-maximizing selection over skill DAG = compositional generalization.

Constraints:
- Compute: ≤200 H100-hours (estimated 50-80 H100-hours for Qwen-7B fine-tuning + data generation)

Quality Self-Checks:
- [x] Core insight: Compositional generalization requires explicit coverage of the skill-composition frontier; random augmentation and RL cannot discover this structure.
- [x] Why not obvious: MASS (skill graphs for math) and STEPS (taxonomy synthesis for composition) exist independently; nobody has combined them because MASS targets efficiency and STEPS targets instruction-following — the math-composition intersection requires domain-specific skill extraction from OMEGA templates.
- [ ] Baseline fear test: CONCERN — a simple baseline of training on randomly sampled k-skill compositions (without the skill DAG structure) might achieve 60-80% of the improvement. The ablation comparing random vs. frontier-guided composition is the make-or-break experiment.
- [x] Information exploited: The skill dependency structure encoded in OMEGA's 40 templated generators — specifically, which atomic skills are prerequisites for which compositions and which k-tuples are absent from training distributions.

Avoid:
- Framing as 'yet another data augmentation paper' — the contribution is the compositional frontier identification via skill DAGs, not the augmentation itself.
- Overclaiming that this solves transformative generalization — OMEGA's transformative axis (novel strategies) is a fundamentally harder problem that skill-graph coverage cannot address.
- Ignoring MASS as related work — MASS must be prominently cited and differentiated, or reviewers who know ICML 2025 will flag the omission.
- Testing only on OMEGA — include MathTrap (EMNLP 2024) and AgentCoMa (2025) as secondary benchmarks to demonstrate the improvement is not benchmark-specific.

## Paper analyses (18 papers)

[
  {
    "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
    "venue": "Nature 2025",
    "problem_identification": "Existing reasoning-capable LLMs depended on expensive human-annotated chain-of-thought data and fragile neural reward models prone to reward hacking at scale. They identified this by observing that process reward models are ill-defined for general reasoning and that Monte Carlo Tree Search fails in token-level search spaces.",
    "key_insight": "Pure RL with only rule-based verifiable rewards (binary correctness + format compliance) — no SFT, no neural reward model — is sufficient to elicit sophisticated reasoning behaviors including self-verification and adaptive problem-solving.",
    "innovation_type": "simplification",
    "method_summary": "GRPO (Group Relative Policy Optimization) eliminates PPO's critic model by normalizing advantages relative to a group of G sampled completions per question: A_i = (r_i - mean(r)) / std(r). The full pipeline is four-stage: cold-start SFT on minimal CoT examples → reasoning-oriented RL with rule-based rewards → rejection sampling SFT (~800K samples) → all-scenario RL for alignment. Distillation into 1.5B–70B models uses 800K curated R1 outputs without RL on the student.",
    "limitations_and_open_questions": "Distilled models show severe compositional degradation: 1.5B loses ~25 points on MATH and collapses on formal logic. Critics (oat-zero, Thoughtology) argue RL amplifies pre-existing base model patterns rather than inducing genuine novel reasoning — self-reflection exists at 'epoch 0' in most architectures.",
    "building_blocks": [
      "GRPO algorithm",
      "Rule-based verifiable rewards",
      "Cold-start SFT methodology",
      "Distillation pipeline for reasoning models",
      "DeepSeek-R1 distilled model family"
    ],
    "relevance_to_seed": "Defines the RL reasoning paradigm our method complements — distilled models' compositional degradation directly motivates skill-graph-guided data synthesis as an alternative to pure RL for compositional generalization."
  },
  {
    "title": "A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition",
    "venue": "arXiv 2025",
    "problem_identification": "Prior theory established either sufficient or necessary conditions for compositional generalization but never both simultaneously — Wiedemer et al. (NeurIPS 2023) gave sufficient-only conditions, while Lippl & Stachenfeld showed fundamental limitations of kernel-theoretic approaches. Li identified the need for a complete characterization by observing the field lacked a unified diagnostic framework.",
    "key_insight": "Compositional generalization requires an indivisible triple: the model's computational graph must align with the true compositional DAG, component mappings must be unambiguous on training data, AND components must encode minimally sufficient information — removing any one condition causes complete failure.",
    "innovation_type": "new_formulation",
    "method_summary": "Formalizes compositional structure as a reference graph set (DAG of deterministic components) and requires structural isomorphism between model and reference graphs. Proves sufficiency via bottom-up structural induction over the DAG using a bijection lemma: unambiguous + minimized representation yields bijective component mappings. Achieves minimization via information bottleneck regularization (Gaussian noise injection + L2 penalty). Validates on XOR composition task showing each condition is independently essential.",
    "limitations_and_open_questions": "The framework assumes compositional structure is known a priori — structural alignment cannot be learned from data alone. Validation is limited to synthetic XOR tasks; scaling to realistic mathematical reasoning with deep DAGs remains undemonstrated.",
    "building_blocks": [
      "Three-condition theoretical framework",
      "Component-level coverage criterion (Definition 4)",
      "Information bottleneck for minimized representation",
      "Structural alignment as architectural design principle"
    ],
    "relevance_to_seed": "Provides the theoretical foundation for why skill-graph-guided coverage works: the component-level coverage criterion (all test component inputs seen in training) is precisely what frontier-targeted synthesis achieves over the skill DAG."
  },
  {
    "title": "ScaleQuest: Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch",
    "venue": "ACL 2025",
    "problem_identification": "Question-driven synthesis (WizardMath, MetaMath) is bounded by seed diversity, while knowledge-driven synthesis (KPMath, MathScale) requires expensive GPT-4 APIs. The authors observed the field was optimizing answer quality while treating the question distribution as fixed — questions, not answers, were the scaling bottleneck.",
    "key_insight": "Instruction-tuned models possess latent question-generation capability from causal LM pretraining that can be cheaply activated via question-only fine-tuning (QFT), without needing seed questions, knowledge graphs, or proprietary models at generation time.",
    "innovation_type": "combination",
    "method_summary": "QFT fine-tunes on ~15K problem texts (solutions stripped, EOS appended) for 1 epoch to activate question generation. QPO then applies DPO-style preference optimization using improved questions (from Llama-70B) as preferred vs. originals as dispreferred. A three-stage filter (language, solvability via model evaluation, difficulty scoring) removes ~48% of raw output. Final pipeline: 1M questions at $680 total, with responses scored by InternLM2-7B-Reward.",
    "limitations_and_open_questions": "No analysis of compositional skill coverage — diversity is measured by topic embedding spread, not by systematic skill combination coverage. QPO still requires a 70B model for preference pairs, undermining the 'from scratch' framing. Effectiveness on models larger than 7B is untested.",
    "building_blocks": [
      "QFT activation technique",
      "QPO for question preference optimization",
      "Difficulty scoring via fail-rate regression",
      "Cost-effective 7B-only synthesis pipeline"
    ],
    "relevance_to_seed": "Key baseline/competitor — achieves diversity through distributional sampling rather than structured skill coverage, making it the natural 'random augmentation' control against which frontier-guided synthesis must demonstrate clear compositional gains."
  },
  {
    "title": "MathCAMPS: Fine-grained Synthesis of Mathematical Problems From Human Curricula",
    "venue": "ICLR 2025 (rejected, scores 5/6/6/6; revised for COLM 2025)",
    "problem_identification": "Static benchmarks (GSM8K, MATH) face contamination opacity and aggregate metrics that mask dramatic per-skill variation. They identified this by noting that models with identical overall accuracy show 36% gaps on specific skills (e.g., Claude Opus vs. Sonnet on fraction addition).",
    "key_insight": "Human educational curricula (Common Core Standards) already encode a hierarchical skill taxonomy that can be mechanized as attribute grammars to produce unlimited, provably-valid, contamination-free problems at arbitrary skill granularity.",
    "innovation_type": "new_benchmark",
    "method_summary": "44 Common Core K-8 standards are encoded as non-terminals in an attribute grammar with 66 parameterized filters enforcing standard-specific constraints. Rejection sampling produces symbolic problems solved by SymPy, translated to natural language via GPT-4o few-shot prompting with 188 narrative themes. Cycle-consistency validation (back-translate and re-solve) achieves 97.7% faithfulness. Follow-up questions (counterfactual + incremental) probe compositional robustness.",
    "limitations_and_open_questions": "Covers only 44/229 K-8 standards (19.2%) — too easy for frontier models. Reviewers criticized the GSM8K-only comparison and K-8 scope limitation. Critically, standards are treated independently with no inter-skill dependency modeling, leaving the compositional frontier unexplored.",
    "building_blocks": [
      "Attribute grammar encoding of math skills",
      "Cycle-consistency validation pipeline",
      "Skill-specific failure analysis methodology",
      "Follow-up question generation (counterfactual/incremental)"
    ],
    "relevance_to_seed": "Most methodologically similar predecessor — the grammar-based skill encoding is a more rigorous alternative to embedding-based skill extraction, and the skill-specific failure findings validate that compositional frontiers exist, but the lack of inter-skill DAG modeling is exactly the gap our approach fills."
  },
  {
    "title": "OpenMathInstruct-2: Accelerating AI for Math with Massive Open-Source Instruction Data",
    "venue": "NeurIPS 2024 MATH-AI Workshop / ICLR 2025 Poster",
    "problem_identification": "Open-source math instruction data lagged behind proprietary datasets, and their predecessor OpenMathInstruct-1 had zero question diversity beyond MATH/GSM8K seeds. They diagnosed this through systematic ablations revealing that solution diversity yields diminishing returns while question diversity does not saturate.",
    "key_insight": "Question diversity dominates solution diversity for sustained scaling of math SFT performance, and excessively verbose chain-of-thought solutions are actively harmful — their concise 'OpenMath CoT' format outperforms verbose alternatives by 3.9% absolute while being 40% shorter.",
    "innovation_type": "scaling",
    "method_summary": "Two-stage pipeline using Llama-3.1-405B-Instruct: (1) solution augmentation via few-shot prompting with answer-matching retention, (2) question augmentation via 5-shot prompting with subject-specific exemplars, validated by 32-sample majority voting. LLM-based decontamination catches paraphrased test items missed by n-gram methods. Yields 14M pairs (~600K unique questions) under CC-BY-4.0.",
    "limitations_and_open_questions": "All questions derive from MATH/GSM8K distributions — augmentation generates 'similar' problems, not compositionally novel ones. The 70B model actually regressed on GSM8K and AIME without majority voting, suggesting the data composition favors smaller models. No skill-level coverage analysis exists.",
    "building_blocks": [
      "14M open-source math instruction dataset",
      "Question augmentation via few-shot prompting",
      "LLM-based decontamination pipeline",
      "Empirical finding: concise > verbose solutions for SFT"
    ],
    "relevance_to_seed": "Provides the baseline data infrastructure — skill-graph-guided selection (à la MASS) could be applied directly to OpenMathInstruct-2's 600K questions to identify compositional frontier gaps, making it the natural corpus for our data selection experiments."
  },
  {
    "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?",
    "venue": "NeurIPS 2025 (Oral / Best Paper Runner-up, perfect 6/6/6/6 scores)",
    "problem_identification": "The field assumed RLVR creates new reasoning capabilities in LLMs, but no rigorous study had tested whether RL-trained models can solve problems their base models fundamentally cannot. The authors identified this gap by shifting from pass@1 (sampling efficiency) to pass@k at large k (reasoning boundary).",
    "key_insight": "RLVR does not expand the reasoning frontier—it merely biases the sampling distribution toward already-existing rewarded paths, making the base model a hard upper bound on reasoning capability.",
    "innovation_type": "analysis",
    "method_summary": "Used pass@k (k up to 1024) as a boundary probe across 6 RL algorithms (PPO, GRPO, Reinforce++, RLOO, ReMax, DAPO), 3 model families (Qwen2.5, LLaMA-3.1, DeepSeek-R1), and math/code/vision tasks. At large k, base models match or exceed RL-trained variants (e.g., 9% higher on Minerva-32B at k=128). On AIME24, 0% of problems were solved exclusively by RL models vs. 13.3% exclusively by base. Perplexity analysis confirmed RL outputs already lie in the base model's distribution. Distillation, by contrast, genuinely introduced new reasoning paths.",
    "limitations_and_open_questions": "Analysis uses finite k—theoretically, RL could locate astronomically low-probability paths. Restricted to single-turn tasks with binary rewards on open-weight models; proprietary systems (o1) remain a black box.",
    "building_blocks": [
      "pass@k as reasoning boundary metric",
      "coverage analysis methodology for RL vs base models",
      "distillation as capability expansion baseline"
    ],
    "relevance_to_seed": "Directly motivates our data-centric approach: if RL cannot create new reasoning patterns (only redistribute existing ones), then compositional generalization requires injecting new compositional training data—exactly what skill-graph-guided frontier synthesis provides."
  },
  {
    "title": "Exploring the Compositional Deficiency of Large Language Models in Mathematical Reasoning Through Trap Problems",
    "venue": "EMNLP 2024",
    "problem_identification": "No benchmark existed to isolate compositional failure in math reasoning from general math difficulty. The authors realized that inserting logical traps into known-solvable problems creates a clean test: models possess both component skills (math solving + trap detection) but fail to compose them.",
    "key_insight": "LLMs possess all requisite component knowledge yet fail to spontaneously compose it for novel combinations—compositional deficiency is structural, not a knowledge gap.",
    "innovation_type": "new_benchmark",
    "method_summary": "Constructed MathTrap by embedding 5 trap types (concept undefined 16%, missing condition 6%, direct contradiction 24%, indirect contradiction 38%, common-sense violation 15%) into MATH/GSM8K problems. Each item is a triplet: original problem, conceptual trap test, and composed trap problem. GPT-4 drops from 70.3% to 36.0% on trap problems (51.2% ratio); Claude-3.5 drops to 25.9% ratio; humans maintain 85.9% ratio. Fine-tuning on 1K trap examples improves trap accuracy but degrades original accuracy, revealing a composition-forgetting tradeoff.",
    "limitations_and_open_questions": "Small dataset (155 private triplets); trap insertion is semi-manual limiting scalability. Does fine-tuning on compositional traps generalize to other composition types, or is it trap-type-specific?",
    "building_blocks": [
      "MathTrap benchmark for compositional math evaluation",
      "triplet evaluation design (original/component/composed)",
      "taxonomy of 5 mathematical trap types"
    ],
    "relevance_to_seed": "MathTrap serves as our secondary evaluation benchmark, providing direct evidence of compositional deficiency in math. The composition-forgetting tradeoff during fine-tuning motivates our structured frontier-coverage approach over naive augmentation."
  },
  {
    "title": "DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving",
    "venue": "NeurIPS 2024",
    "problem_identification": "Discovered severe easy-query bias in math SFT datasets: 51.1% of the hardest MATH queries received zero synthetic responses in standard rejection sampling, while easy queries were massively over-represented. This was identified through systematic fail-rate analysis of existing rejection tuning pipelines.",
    "key_insight": "Data difficulty distribution matters more than data volume—allocating synthesis trials proportionally to query difficulty yields better models from smaller datasets than uniform sampling from larger ones.",
    "innovation_type": "new_technique",
    "method_summary": "Proposed two Difficulty-Aware Rejection Sampling strategies: DARS-Uniform (equalizes correct responses per query at k_u=40) and DARS-Prop2Diff (allocates up to k_p=192 responses for hardest queries). Uses fail-rate from n_d samples as an automatic difficulty metric. All synthesis uses open-source DeepSeekMath-7B-RL (no GPT-4). ~590K examples from GSM8K/MATH training queries. Llama3-8B gains +6.9% on MATH (39.7→46.6%) and +4-5 points on out-of-domain benchmarks, matching models trained on 4× more data.",
    "limitations_and_open_questions": "Difficulty is defined per-query, not per-skill-composition—DART cannot distinguish whether a hard problem is hard because of novel skill combinations vs. inherent single-skill complexity. Does difficulty-awareness compose with compositional coverage?",
    "building_blocks": [
      "fail-rate as automatic difficulty metric",
      "DARS-Uniform and DARS-Prop2Diff sampling strategies",
      "demonstration that open-source-only synthesis can match proprietary pipelines"
    ],
    "relevance_to_seed": "Validates the principle that targeted data curation outperforms volume. Our approach extends this from difficulty-awareness to composition-awareness: rather than asking 'how hard is this query?', we ask 'which skill compositions are under-covered?' DART's methodology could be combined with our frontier sampling."
  },
  {
    "title": "RV-Syn: Rational and Verifiable Mathematical Reasoning Data Synthesis based on Structured Function Library",
    "venue": "EACL 2026",
    "problem_identification": "Existing math data synthesis methods either lack solution verifiability (LLM-generated solutions may be wrong) or fail to capture the logical structure of problems (random augmentation doesn't control skill composition). The gap: no method jointly ensures correctness via execution and controls compositional structure via explicit function graphs.",
    "key_insight": "Decomposing math problems into executable computational graphs of typed functions enables synthesis that is simultaneously verifiable (graphs execute to ground truth) and compositionally controllable (novel function combinations produce novel problems).",
    "innovation_type": "combination",
    "method_summary": "Three-stage pipeline: (1) Decompose seed problems into Python function sequences, merge redundant functions (~28% reduction) via AST+semantic similarity, and organize into a graph with co-occurrence and topic edges. (2) Sample function subsets via three strategies (co-occurrence, topic-based, edgeless) to balance familiarity and novelty, then compose into computational graphs. (3) Execute graphs for ground-truth answers, back-translate into NL problems via LLM, and filter by answer-match verification. Achieves 6.3% SOTA gain on LLaMA-3-8B with 50K data (vs. competitors' 100K), 0.9% problem error rate vs. 4.9-10.6% for baselines.",
    "limitations_and_open_questions": "Function library is derived from seed problems, potentially limiting coverage to seed-distribution skills. The edgeless sampling strategy (novel combinations) is not systematically guided by a coverage criterion—how much of the compositional frontier does it actually cover?",
    "building_blocks": [
      "structured function library from seed decomposition",
      "computational graph as verifiable solution representation",
      "three-strategy sampling (co-occurrence/topic/edgeless) for composition control",
      "back-translation from graphs to NL problems"
    ],
    "relevance_to_seed": "RV-Syn's function library is structurally analogous to OMEGA's skill templates, and its graph-based composition mirrors our proposed skill-DAG-guided synthesis. Key difference: RV-Syn samples compositions without explicit frontier identification—adding our coverage-maximizing selection over the function graph would directly extend their approach."
  },
  {
    "title": "Skill-it! A Data-Driven Skills Framework for Understanding and Training Language Models",
    "venue": "NeurIPS 2023 (Spotlight)",
    "problem_identification": "Training data selection treated all skills as independent, ignoring that skills have prerequisite dependencies (learning skill B is easier after mastering skill A). No framework existed to discover and exploit these orderings for data-efficient LLM training.",
    "key_insight": "Language models follow a natural skill acquisition order analogous to human learning—formalizing and exploiting prerequisite relationships between skills via a learned skill graph enables dramatically more data-efficient training.",
    "innovation_type": "new_formulation",
    "method_summary": "Defines skills as data partitions with associated loss functions. Constructs a skill graph by measuring how training on skill A's data reduces loss on skill B (prerequisite edges). The SKILL-IT online algorithm iteratively adjusts the training data mixture based on: (1) current per-skill evaluation loss and (2) adjacency structure from the skill graph, upweighting prerequisites of underperforming skills. On LEGO synthetic data: +36.5 accuracy points over random sampling. On Natural Instructions fine-tuning: 13.6% validation loss reduction. On RedPajama 1B-token pretraining: outperforms 3B-token random baseline on LM Eval Harness.",
    "limitations_and_open_questions": "Skill definitions require human specification or clustering—automatic skill discovery at scale is unaddressed. The skill graph captures prerequisites but not compositional relationships (A+B→C). Does the framework extend from single-skill ordering to multi-skill composition?",
    "building_blocks": [
      "skill graph construction via cross-skill loss reduction",
      "online data mixture algorithm exploiting prerequisite structure",
      "formalization of ordered skill sets for LLMs"
    ],
    "relevance_to_seed": "Conceptual ancestor of our approach: Skill-it proved that skill DAGs improve training efficiency, but targets single-skill ordering, not compositional frontier coverage. Our work extends the skill graph from prerequisite ordering to compositional frontier identification—from 'what order to learn skills' to 'which skill combinations are missing.'"
  },
  {
    "title": "How Does RL Post-training Induce Skill Composition? A Case Study on Countdown",
    "venue": "NeurIPS 2025 Workshops (Efficient Reasoning Spotlight, MATH-AI Poster)",
    "problem_identification": "Prior work conflated compositional generalization with length generalization in RL-trained LLMs; no study had decomposed *what structures* RL learns and in what order. The authors identified this gap by noting that pass@k metrics obscure structural mastery patterns.",
    "key_insight": "RL induces a structure-dependent learning hierarchy — balanced expression trees are mastered before unbalanced ones — due to a 'lookahead bottleneck' where autoregressive models must commit to root operators before generating complex right subtrees.",
    "innovation_type": "analysis",
    "method_summary": "Solutions to Countdown (find arithmetic expressions evaluating to a target) are parsed into canonical binary expression trees, classified by shape signatures ([left_size]∘[right_size]). Models (Qwen-2.5 1.5B–7B) are trained via GRPO on n∈{3,4} with balanced pattern sampling, then evaluated OOD on n∈{5,6} and held-out tree shapes. Key ablations compare RL vs. SFT learning dynamics, GRPO vs. PPO, and the effect of withholding entire pattern families during training.",
    "limitations_and_open_questions": "Validated only on Countdown — transferability to multi-step mathematical reasoning, theorem proving, or realistic compositional tasks is unknown. No curriculum or data design intervention was tested, leaving open whether structure-aware training data could accelerate or reorder the hierarchy.",
    "building_blocks": [
      "Expression-tree decomposition of solutions into compositional skill atoms",
      "Shape-signature taxonomy for classifying compositional complexity",
      "Balanced pattern sampling methodology to remove distributional confounds",
      "Evidence that RL produces genuine compositional reuse (not memorization)"
    ],
    "relevance_to_seed": "Directly validates our hypothesis that compositional structure matters more than scale — their finding that certain tree shapes resist learning even with RL motivates targeted data synthesis at those specific compositional frontiers rather than relying on RL alone."
  },
  {
    "title": "MathGAP: Out-of-Distribution Evaluation on Problems with Arbitrarily Complex Proofs",
    "venue": "ICLR 2025",
    "problem_identification": "Existing math benchmarks conflate data contamination with generalization failure and lack systematic control over proof complexity. The authors formalized the gap: no evaluation framework independently varies depth, width, shape, and ordering of mathematical proof structures.",
    "key_insight": "Performance degradation is governed by proof tree *structure* (nonlinear >> linear, deep >> shallow) rather than surface features, and nonlinear proofs approach zero accuracy even for frontier models — revealing that compositional proof reasoning, not arithmetic, is the bottleneck.",
    "innovation_type": "new_benchmark",
    "method_summary": "MathGAP generates problems via a three-step pipeline: (1) top-down recursive proof tree sampling with controlled depth/width/shape parameters using five logical form predicates, (2) template-based conversion of leaf axioms to natural language sentences, (3) post-order traversal to produce chain-of-thought traces. Evaluated on Mixtral-8x7B, Llama3-8B/70B, GPT-3.5/4o, o1-preview, and DeepSeek-R1 across ~400-problem test sets per configuration.",
    "limitations_and_open_questions": "Limited to arithmetic word problems with fixed logical form predicates — unclear if the framework extends to algebraic, geometric, or multi-domain math. The template-based NL generation may introduce artifacts that models exploit rather than reason through.",
    "building_blocks": [
      "Parameterized proof tree generation with independent depth/width/shape control",
      "Methodology for contamination-free OOD evaluation",
      "Quantitative evidence that nonlinear proof structures are the hardest compositional axis",
      "Complementary evaluation framework for measuring compositional math generalization"
    ],
    "relevance_to_seed": "Provides a complementary evaluation methodology to OMEGA — while OMEGA measures compositional generalization via skill combinations, MathGAP measures it via proof tree complexity, enabling us to validate that skill-DAG-guided synthesis improves generalization along both axes."
  },
  {
    "title": "SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond",
    "venue": "NeurIPS 2025",
    "problem_identification": "Open-source RL replication efforts concentrated on math/code, leaving general logical reasoning under-resourced due to the difficulty of collecting diverse, *verifiable* reasoning data. The authors identified that logical reasoning is a foundational building block that transfers cross-domain but lacked a scalable synthesis pipeline.",
    "key_insight": "Structured synthetic logical reasoning data with rule-based verification enables RL training that transfers to unseen mathematical domains — logic-only training improves AIME by ~10 points, suggesting shared abstract reasoning mechanisms exploitable via data mixing.",
    "innovation_type": "combination",
    "method_summary": "35 diverse logic tasks (puzzles, constraint satisfaction, deduction) are implemented as programmatic generators with task-specific difficulty parameters calibrated to a dual-bound (lower: pass rate 0–0.5 for base models; upper: pass@10 > 0 for frontier models). Each task has a dedicated rule-based verifier providing binary rewards. Models (Qwen2.5-7B/32B) are trained via GRPO with data mixing strategies (logic+math, logic+code, all three). SynLogic-Hard uses all 35 tasks; SynLogic-Easy excludes 8 tasks beyond 7B capacity.",
    "limitations_and_open_questions": "Reviewer scores were borderline (5/4/4/4/4 on 6-point NeurIPS scale). The difficulty calibration is model-dependent and may not generalize. Cross-domain transfer is demonstrated but the mechanism (shared reasoning primitives vs. longer CoT) is not disentangled. No evaluation on compositional generalization specifically.",
    "building_blocks": [
      "Dual-bound difficulty calibration methodology",
      "Rule-based verification for RL reward across 35 task types",
      "Evidence that logic+math data mixing improves sample efficiency",
      "Open-source synthesis pipeline and dataset"
    ],
    "relevance_to_seed": "Validates that structured synthetic data with verifiable rewards and controllable difficulty improves generalization across domains — our approach applies the same principle (structured generation + verification) but targets the compositional skill frontier specifically rather than broad logical reasoning coverage."
  },
  {
    "title": "Key-Point-Driven Data Synthesis with its Enhancement on Mathematical Reasoning",
    "venue": "AAAI 2025",
    "problem_identification": "Math reasoning training data is scarce and existing synthesis methods either rephrase seed problems (limited novelty) or generate from knowledge bases (distribution mismatch). The authors identified that grounding synthesis in extracted 'key points' — essential theorems/methods — preserves authentic data distributions while enabling novel question generation.",
    "key_insight": "Decomposing math problems into topic + key-point pairs and using a topic co-occurrence probability matrix to sample multi-topic combinations generates genuinely novel problems that remain distributionally aligned with authentic data — a middle ground between augmentation and unconstrained generation.",
    "innovation_type": "new_technique",
    "method_summary": "GPT-4 extracts topics and key points from seed problems (GSM8K, MATH), which are deduplicated via embedding similarity. A Topic Co-occurrence Probability Matrix (TCPM) guides sampling of 2–3 topic combinations. GPT-4 generates novel questions conditioned on sampled topics, key points, and exemplar practices. Quality control uses GPT-4 scoring (≥0.85 threshold, ~51% pass rate) and consensus voting over 10 nucleus-sampled solutions verified via SymPy equivalence. Produces KPMath (800K+) and KPMath-Plus (1.576M total).",
    "limitations_and_open_questions": "Heavy reliance on GPT-4 for extraction, generation, and scoring creates cost barriers and potential capability ceiling. The TCPM captures co-occurrence but not prerequisite/dependency structure — key points are treated as flat, not hierarchical. No evaluation of compositional generalization or OOD performance.",
    "building_blocks": [
      "Key-point extraction as a structured skill decomposition analog",
      "Topic co-occurrence probability matrix for principled combination sampling",
      "Consensus voting with symbolic equivalence checking for quality filtering",
      "Demonstrated scalability to 800K+ high-quality math QA pairs"
    ],
    "relevance_to_seed": "The key-point extraction pipeline is a direct methodological precursor to our skill extraction from OMEGA templates — but KPDDS uses flat co-occurrence rather than a dependency DAG, and targets training data volume rather than compositional frontier coverage, precisely the gap our approach fills."
  },
  {
    "title": "Compositional Generalization from Learned Skills via CoT Training: A Theoretical and Structural Analysis for Reasoning",
    "venue": "ICLR 2026",
    "problem_identification": "No mechanistic explanation existed for WHY CoT training enables compositional generalization — prior work showed CoT helps but treated it as a black box. Yao et al. identified this gap by noting the disconnect between empirical CoT success and the absence of circuit-level or distributional analysis of how composition emerges.",
    "key_insight": "CoT training creates a two-stage compositional circuit where shallow layers resolve intermediate entities (first hop), freeing deeper layers to specialize in subsequent reasoning steps — the number of internal circuit stages directly corresponds to explicit reasoning steps during training.",
    "innovation_type": "analysis",
    "method_summary": "Uses synthetic multi-hop fact completion (entities, relations, 2-hop compositions) with controlled ID/OOD splits to isolate compositional generalization. Employs logit lens and causal tracing to identify a two-stage circuit: Stage 1 retrieves bridge entities at layers 3-5, Stage 2 processes autoregressively at layer 8. Parameter λ controls multi-hop/single-hop ratio; noise analysis (ξ=0.05→97.8% OOD, ξ=0.4→49.1%) quantifies robustness. Validated on Llama2-7B with Wikidata two-hop queries via LoRA.",
    "limitations_and_open_questions": "Models trained on 2-hop CoT cannot generalize to 3-hop — the circuit structure is fixed to training-time depth. Synthetic triplet setup is far simpler than real math composition; unclear if the same circuit pattern holds for mathematical skill composition with heterogeneous skill types.",
    "building_blocks": [
      "Logit lens / causal tracing methodology for analyzing compositional circuits",
      "ID/OOD decomposition framework with λ-controlled distributional shifts",
      "Noise robustness analysis protocol for CoT intermediate steps"
    ],
    "relevance_to_seed": "Provides theoretical grounding that CoT-based training enables compositional generalization through learned circuits — directly supports our hypothesis that models CAN compose skills if trained with proper compositional coverage, and explains WHY frontier-targeted data (covering the compositional space) should work mechanistically."
  },
  {
    "title": "AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios",
    "venue": "arXiv 2025",
    "problem_identification": "Existing compositional reasoning benchmarks test multi-step reasoning of the SAME type (e.g., multi-hop math); no benchmark measured the compositionality gap when mixing DIFFERENT reasoning types (commonsense + math) in realistic agentic scenarios.",
    "key_insight": "The compositional failure is cross-type, not just cross-step: LLMs solve commonsense and math independently but lose ~30% accuracy when combining them, even when each isolated step succeeds — revealing a type-composition gap distinct from depth-composition gaps.",
    "innovation_type": "new_benchmark",
    "method_summary": "Constructs tasks across 5 real-world domains (house working, web shopping, science experiments, smart assistant, travel agent) where each requires both a commonsense step and a math step. Evaluates 61 LLMs using three metrics: all-steps-correct (isolated), composition accuracy, and the gap between them. Includes interpretability analysis via neuron patterns, attention maps, and membership inference to diagnose failure modes.",
    "limitations_and_open_questions": "Limited to binary composition (commonsense + math); doesn't test k>2 skill compositions or compositions within math subtypes. As a secondary benchmark for our work, the commonsense component may not directly reflect pure mathematical compositional generalization — the gap may conflate cross-type integration difficulty with genuine compositional failure.",
    "building_blocks": [
      "Compositionality gap metric (isolated vs. composed accuracy)",
      "Multi-domain agentic task templates combining heterogeneous reasoning",
      "61-model evaluation infrastructure with interpretability diagnostics"
    ],
    "relevance_to_seed": "Serves as a secondary evaluation benchmark demonstrating that compositional failures persist across 61 LLMs and are not benchmark-specific — validates our core premise that composition is systematically hard, though the commonsense+math axis is orthogonal to OMEGA's intra-mathematical composition."
  },
  {
    "title": "MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy",
    "venue": "AAAI 2026",
    "problem_identification": "Existing math data synthesis either mutates existing problems (risking contamination and limited novelty) or uses unconstrained generation (producing trivial/unsolvable problems). MathSmith identified that the key bottleneck is generating genuinely NOVEL hard problems with guaranteed solvability.",
    "key_insight": "Concept-pair sampling from PlanetMath (11K concepts) combined with RL-optimized difficulty strategies creates a generate-from-scratch pipeline that decouples problem novelty from existing problem sets, using answer consistency across multiple teacher samples as a solvability filter.",
    "innovation_type": "new_technique",
    "method_summary": "Samples concept-explanation pairs from PlanetMath, applies ≥2 of 9 difficulty strategies (multi-step reasoning, cross-topic integration, implicit logic, distractors, abstract modeling, multiple solution paths, advanced manipulation, extreme conditions, non-standard representation) as soft constraints. Uses GRPO to optimize composite reward: r_structure (format validity α=0.7 + step count α=0.3) + r_reasoning (complexity via CoT length β=0.7 + answer consistency via K=5 majority voting β=0.3). Three-stage pipeline: SFT → Hard → HC, achieving 95.4% usability ratio.",
    "limitations_and_open_questions": "Difficulty is proxied by CoT length, which conflates verbosity with genuine reasoning depth. The concept-pair approach targets individual problem hardness, NOT compositional coverage — there's no mechanism to identify which concept COMBINATIONS are underrepresented. This is the critical gap our skill-DAG approach fills.",
    "building_blocks": [
      "PlanetMath concept-pair extraction pipeline (11K concepts)",
      "9 difficulty strategy taxonomy as generation constraints",
      "Multi-objective RL reward combining structural validity, complexity, and consistency",
      "GRPO-based policy optimization for math problem generation"
    ],
    "relevance_to_seed": "Directly competing approach at same venue (AAAI 2026) — MathSmith targets problem DIFFICULTY via RL while our approach targets compositional COVERAGE via skill DAGs. Key differentiation: MathSmith's concept pairs lack dependency structure and don't identify frontier compositions; our method is complementary (could use MathSmith's generation pipeline to synthesize problems AT identified frontier nodes)."
  },
  {
    "title": "More Data or Better Data? A Critical Analysis of Data Selection and Synthesis for Mathematical Reasoning",
    "venue": "EMNLP 2025 (Industry Track)",
    "problem_identification": "Despite proliferation of math data construction methods, no unified comparison existed under realistic deployment conditions — each method was evaluated in isolation with different models, metrics, and mixing strategies, making actionable guidance impossible.",
    "key_insight": "Data structure (interpretable formatting, LaTeX, clear definitions) and source quality (distillation from reasoning models like QwQ-32B) consistently dominate data volume — rule-based scaling and retrieval augmentation provide negligible gains, while distilled data yields +8.96 MATH accuracy.",
    "innovation_type": "analysis",
    "method_summary": "Evaluates open-source datasets (web-scraped, curated, specialized) and synthesis techniques (prompt-based reformatting, model distillation, weakness-guided augmentation, textbook extraction) under a unified annealing pipeline mixing new data at 20% with baseline data. Tests on DeepSeek-V2-Lite and Qwen2.5-3B across MMLU, GSM8K, MATH, MathBench, and HumanEval. Key quantitative findings: Math-Cosmo (structured formatting) +1.72 MATH, NaturalReasoning-QwQ (distillation) +1.92 MATH, OpenR1-Math-220K (scaled distillation) +8.96 MATH.",
    "limitations_and_open_questions": "Analysis is limited to small models (3B-16B) in an industrial annealing setup — un
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
  "promptId": "28475c01-8228-490c-89ce-bf301410a04b",
  "type": "user",
  "uuid": "859a51dc-0e90-4901-b3f3-bc9b2d5f7336",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T05:38:41.415Z_

```json
{
  "parentUuid": "859a51dc-0e90-4901-b3f3-bc9b2d5f7336",
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
  "uuid": "722e82b7-4e02-48d8-9efd-014beb8843c9",
  "timestamp": "2026-05-29T05:38:41.415Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T05:38:41.416Z_

```json
{
  "parentUuid": "722e82b7-4e02-48d8-9efd-014beb8843c9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5c46ed98-80f4-4a7d-9c39-e3b6590074b6",
  "timestamp": "2026-05-29T05:38:41.416Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "5c46ed98-80f4-4a7d-9c39-e3b6590074b6",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize compositional frontier research strategy for AAAI 2026",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7"
}
```

---

### Assistant

_source line 8 · 2026-05-29T05:39:04.293Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 18 paper analyses into a strategic "Field Guide" for a researcher working on compositional generalization in mathematical reasoning, specifically targeting AAAI 2026. Let me carefully analyze the papers and produce a comprehensive, evidence-based JSON output.

Let me think through each section:

**Innovation Patterns:**
1. Structured data > more data (DART-Math, OpenMathInstruct-2, EMNLP 2025 analysis)
2. Skill/concept decomposition + recombination (KPDDS, RV-Syn, MathCAMPS, Skill-it)


3. Verifiable synthetic generation with formal guarantees (RV-Syn, SynLogic, MathSmith)
4. Papers that challenge foundational assumptions with empirical evidence (oat-zero on RL limits, Yao et al. on CoT circuits)
5. Streamlining complex training pipelines toward elegance (DeepSeek-R1's GRPO approach)
6. Benchmarks that expose systematic weaknesses (MathTrap, MathGAP, AgentCoMa, OMEGA)

**Reviewer Preferences:**
- Rigorous ablations with clean results (DART-Math, oat-zero achieved perfect scores)
- Challenging conventional wisdom backed by solid evidence (oat-zero's RL findings)
- Controlled experimental design

, open-source implementations, and clear positioning against prior work

**Field Gaps:**
The major untapped opportunities are combining skill DAGs with compositional frontier identification for math problems, bridging MASS-style skill graphs to data synthesis, scaling automatic skill discovery beyond current limitations, evaluating compositions beyond pairs, and developing training curricula that respect problem structure.

**Untried Combinations:**
I'm seeing potential in mixing OMEGA templates with STEPS and MASS skill graphs, pairing RV-Syn's computational graphs with frontier identification, guiding MathSmith's RL generation through skill-DAG coverage, and leveraging DART-Math's difficulty awareness for compositional coverage.

**Method Building Blocks:**
GRPO, skill graphs, attribute grammars, computational graphs, and fail-rate difficulty metrics provide the foundation.

**Common Pitfalls:**
Avoid framing this as incremental data augmentation—the novelty lies in the structural and compositional insights.

I also need to be careful not to skip random baseline comparisons, avoid testing on just one benchmark, and keep difficulty metrics separate from compositional complexity, which are distinct dimensions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c46ed98-80f4-4a7d-9c39-e3b6590074b6",
  "isSidechain": false,
  "requestId": "req_011CbWKbf28sF5KBp6quoPMS",
  "type": "assistant",
  "uuid": "2f605c3a-a644-4d51-98dc-927138e997d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKNV8NyTRP1YgrmB6iv72D",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12620,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8184,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12620
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

_source line 9 · 2026-05-29T05:42:05.084Z_

I'll analyze the 18 papers systematically to synthesize the field guide. Let me think through the patterns carefully before producing the output.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Structured Coverage Over Scale",
      "description": "Papers that demonstrate targeted, structure-aware data curation outperforms brute-force scaling consistently achieve strong results. The key move is identifying a structural axis (difficulty, skill, proof depth) and showing that systematic coverage along that axis yields disproportionate gains per data point compared to uniform or random sampling.",
      "examples": ["DART-Math (NeurIPS 2024)", "Skill-it (NeurIPS 2023 Spotlight)", "MASS (ICML 2025)", "OpenMathInstruct-2 (ICLR 2025)", "EMNLP 2025 Data Analysis"],
      "success_rate": "high"
    },
    {
      "pattern": "Assumption-Shattering Analysis with Rigorous Methodology",
      "description": "Papers that challenge widely-held field assumptions using clean experimental methodology — especially pass@k boundary probing, controlled ablations, and mechanistic interpretability — receive the highest review scores. The critical ingredient is a tight experimental design that leaves no room for alternative explanations.",
      "examples": ["Does RL Really Incentivize Reasoning (NeurIPS 2025 Oral, 6/6/6/6)", "Yao et al. CoT Circuits (ICLR 2026)", "RL Skill Composition on Countdown (NeurIPS 2025 Workshops)"],
      "success_rate": "high"
    },
    {
      "pattern": "Verifiable Synthetic Generation via Executable Representations",
      "description": "Representing math problems as executable structures (computational graphs, attribute grammars, programmatic generators) that produce ground-truth answers by construction, then back-translating to natural language. This sidesteps the LLM-generated-solution reliability problem and enables compositional control.",
      "examples": ["RV-Syn (EACL 2026)", "MathCAMPS (ICLR 2025 rejected/COLM 2025)", "SynLogic (NeurIPS 2025)", "MathGAP (ICLR 2025)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Concept/Skill Decomposition + Principled Recombination",
      "description": "Decomposing the problem space into atomic units (skills, key points, functions, concepts) and then recombining them via a structured sampling mechanism (co-occurrence matrix, graph, DAG). The innovation delta comes from HOW recombination is guided — flat co-occurrence (KPDDS), random graph sampling (RV-Syn), or prerequisite ordering (Skill-it) — each leaving room for more principled alternatives.",
      "examples": ["KPDDS (AAAI 2025)", "RV-Syn (EACL 2026)", "Skill-it (NeurIPS 2023)", "MathSmith (AAAI 2026)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Simplification of Complex Pipelines",
      "description": "Removing expensive components (neural reward models, GPT-4 dependencies, process supervision) and showing that simpler alternatives (rule-based rewards, open-source-only synthesis, binary correctness signals) match or exceed performance. Reviewers reward this when the ablation is clean and the cost reduction is dramatic.",
      "examples": ["DeepSeek-R1 (Nature 2025)", "DART-Math (NeurIPS 2024)", "ScaleQuest (ACL 2025)"],
      "success_rate": "high"
    },
    {
      "pattern": "Benchmark-as-Diagnostic Revealing Hidden Failures",
      "description": "Constructing evaluation frameworks with fine-grained structural control (skill decomposition, proof tree parameterization, trap insertion) that expose systematic failures invisible in aggregate metrics. The highest-impact benchmarks don't just measure performance — they diagnose WHY models fail along specific structural axes.",
      "examples": ["MathTrap (EMNLP 2024)", "MathGAP (ICLR 2025)", "AgentCoMa (2025)", "MathCAMPS (ICLR 2025 rej.)"],
      "success_rate": "medium"
    }
  ],
  "reviewer_preferences": [
    "Clean ablation structure that isolates each claimed contribution: the oat-zero paper (NeurIPS 2025 Oral, perfect 6/6/6/6) succeeded because pass@k at large k cleanly isolates the RL-vs-base-model reasoning boundary — reviewers reward experimental designs where the conclusion is unambiguous from the data.",
    "Open-source reproducibility with concrete compute budgets: DART-Math, ScaleQuest, and SynLogic all provide open datasets and detail exact compute costs ($680 for ScaleQuest, 590K examples for DART-Math). Papers hiding behind GPT-4 dependencies (KPDDS) face reviewer skepticism about reproducibility and cost barriers.",
    "Differentiation from the most obvious related work, especially recent high-profile papers: MathCAMPS was rejected partly for insufficient comparison scope (GSM8K-only). For AAAI 2026, failure to prominently differentiate from MASS (ICML 2025) and MathSmith (same venue) will trigger immediate reviewer flags.",
    "Quantitative evidence that structural/compositional axes matter independently of difficulty: MathGAP's finding that nonlinear proofs approach zero accuracy even for frontier models, and MathTrap's 51.2% compositional ratio for GPT-4, are the kind of specific, surprising numbers reviewers cite in acceptance arguments.",
    "Practical impact at realistic scale — reviewers penalize methods that only work at 70B+ or require proprietary APIs: DART-Math's demonstration that open-source-only synthesis matches proprietary pipelines, and ScaleQuest's 7B-only pipeline, set the bar. Methods requiring 405B or GPT-4 in the critical path need strong justification.",
    "Negative results and honest limitation sections earn reviewer trust: the oat-zero paper's acknowledgment that finite-k analysis cannot rule out astronomically-low-probability RL paths, and Yao et al.'s admission that 2-hop circuits don't generalize to 3-hop, both turned potential weaknesses into credibility signals.",
    "Out-of-domain generalization evidence beyond the primary benchmark: DART-Math gains +4-5 points on OOD benchmarks, SynLogic's logic-only training improves AIME by ~10 points. Papers evaluated on a single benchmark (MathCAMPS on GSM8K-only) are consistently penalized."
  ],
  "field_gaps": [
    {
      "gap": "No method uses skill dependency DAGs to identify AND fill compositional coverage gaps in mathematical training data — MASS uses skill graphs for selection efficiency, STEPS uses skill taxonomies for instruction-following, but nobody has combined DAG-guided frontier identification with targeted math data synthesis.",
      "evidence": "MASS (ICML 2025) explicitly targets efficiency not composition; STEPS (arXiv Jan 2026) validates on instruction-following not math; Skill-it (NeurIPS 2023) captures prerequisites but not compositional relationships; RV-Syn (EACL 2026) samples compositions without explicit frontier identification.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Automatic skill discovery and taxonomy construction at scale remains unsolved — every existing approach requires either human-defined skill taxonomies (MathCAMPS's Common Core standards), seed-problem decomposition (RV-Syn's function library), or LLM-extracted key points (KPDDS) with no principled coverage guarantees.",
      "evidence": "Skill-it (NeurIPS 2023) lists automatic skill discovery as a key limitation; MathCAMPS covers only 44/229 K-8 standards; KPDDS's GPT-4-extracted key points have no coverage guarantee over the actual skill space.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No empirical study has tested whether RL's compositional limitations (demonstrated on Countdown by the NeurIPS 2025 workshop paper) persist when the BASE model has been pre-trained with compositionally-complete data — the oat-zero finding that RL cannot exceed the base model's reasoning boundary implies the bottleneck is upstream data, but nobody has closed the loop experimentally.",
      "evidence": "oat-zero (NeurIPS 2025 Oral) shows RL is bounded by base model; RL Skill Composition on Countdown shows structure-dependent learning hierarchy in RL; DeepSeek-R1 distilled models show compositional degradation. None test RL on compositionally-enriched base models.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "The composition-forgetting tradeoff during fine-tuning (training on compositional data degrades single-skill performance) has been observed but not solved — MathTrap shows fine-tuning on trap examples improves trap accuracy but degrades original accuracy, and no curriculum or regularization strategy has been proposed to prevent this.",
      "evidence": "MathTrap (EMNLP 2024) directly observes composition-forgetting; Yao et al. (ICLR 2026) show CoT circuits are fixed to training-time depth, suggesting fine-tuning for deeper composition may overwrite shallower circuits.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "k>2 compositional evaluation is essentially absent — AgentCoMa tests binary composition (commonsense + math), MathTrap tests binary composition (math + trap detection), and even MathGAP primarily controls depth rather than combinatorial width of distinct skill types. No benchmark systematically evaluates k=3,4,5+ skill compositions.",
      "evidence": "AgentCoMa (2025) explicitly notes limitation to binary composition; Zhao & Kaur (NeurIPS 2024) manually compose k-skill but only up to k+1; OMEGA provides the infrastructure but no published results systematically evaluate across k values.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Difficulty calibration conflates single-skill complexity with compositional complexity — DART-Math's fail-rate, MathSmith's CoT-length proxy, and ScaleQuest's difficulty scoring all measure aggregate difficulty without distinguishing whether a problem is hard because of a single difficult skill or because of novel skill combination.",
      "evidence": "DART-Math (NeurIPS 2024) explicitly notes difficulty is defined per-query not per-skill-composition; MathSmith (AAAI 2026) proxies difficulty by CoT length which conflates verbosity with reasoning depth; ScaleQuest uses topic embedding spread which is orthogonal to compositional coverage.",
      "difficulty": "low",
      "impact_if_solved": "medium"
    },
    {
      "gap": "No unified theoretical framework connects Li's necessary-and-sufficient conditions for compositional generalization (structural alignment + unambiguity + minimality) with practical training data design — the theory says WHAT is needed but not HOW to construct training data that satisfies all three conditions.",
      "evidence": "Li (arXiv 2025) validates only on synthetic XOR tasks; the component-level coverage criterion (Definition 4) is precisely what frontier-targeted synthesis should achieve, but no empirical work has tested this connection. Redhardt et al. (NeurIPS 2025) prove coverage suffices but provide no practical method.",
      "difficulty": "high",
      "impact_if_solved": "high"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "OMEGA's templated skill taxonomy as a DAG + STEPS' information-theoretic frontier selection + MASS's skill-graph construction methodology → skill-DAG-guided compositional data synthesis for mathematical reasoning. Extract skills from OMEGA's 40 generators, build a dependency DAG using MASS's cross-skill loss reduction method, identify under-covered k-tuples via STEPS' marginal structural information criterion, and synthesize targeted problems at those frontiers.",
      "from_papers": ["OMEGA (NeurIPS 2025)", "MASS (ICML 2025)", "STEPS (arXiv Jan 2026)", "Skill-it (NeurIPS 2023)"],
      "why_promising": "Each component is independently validated: MASS proves skill graphs improve math data efficiency by 50-70%, STEPS proves information-theoretic selection improves compositional generalization, OMEGA provides the evaluation infrastructure and skill taxonomy. The combination is non-obvious because MASS targets efficiency, STEPS targets instruction-following, and nobody has worked at the math-composition intersection. This is the proposed paper's core contribution."
    },
    {
      "idea_sketch": "RV-Syn's computational graph synthesis + skill-DAG frontier identification → verifiable compositional frontier synthesis. Use RV-Syn's function decomposition and executable graph pipeline, but replace their three sampling strategies (co-occurrence/topic/edgeless) with frontier-guided sampling that specifically targets under-covered function combinations identified by the skill DAG.",
      "from_papers": ["RV-Syn (EACL 2026)", "MASS (ICML 2025)", "OMEGA (NeurIPS 2025)"],
      "why_promising": "RV-Syn already proves that computational graph composition produces verifiable problems with controllable structure (0.9% error rate vs. 4.9-10.6% for baselines), but lacks principled coverage guidance. Adding frontier identification to their pipeline is a clean, high-value extension — the generation infrastructure exists, only the selection principle is missing."
    },
    {
      "idea_sketch": "DART-Math's difficulty-aware rejection tuning + compositional coverage awareness → a data selection strategy that jointly optimizes for BOTH difficulty AND compositional frontier coverage. Instead of DARS-Uniform/DARS-Prop2Diff which allocate by single-query difficulty, allocate synthesis budget proportionally to (difficulty × compositional novelty), where novelty is measured by distance to the nearest covered k-tuple in the skill DAG.",
      "from_papers": ["DART-Math (NeurIPS 2024)", "MASS (ICML 2025)", "OMEGA (NeurIPS 2025)"],
      "why_promising": "DART-Math proves difficulty-awareness alone yields +6.9% MATH gains from smaller datasets, and compositional coverage should be orthogonal — a problem can be easy but compositionally novel, or hard but compositionally redundant. Joint optimization should capture gains from both axes."
    },
    {
      "idea_sketch": "MathSmith's RL-optimized problem generation + skill-DAG frontier nodes as generation targets → RL-guided synthesis that optimizes for compositional coverage rather than difficulty. Replace MathSmith's PlanetMath concept-pair sampling with OMEGA-derived skill-tuple sampling, and modify the GRPO reward to include a coverage bonus for generating problems in under-represented compositional regions.",
      "from_papers": ["MathSmith (AAAI 2026)", "OMEGA (NeurIPS 2025)", "MASS (ICML 2025)"],
      "why_promising": "MathSmith's generation pipeline produces 95.4% usable problems, but concept pairs lack dependency structure and don't identify frontier compositions. This combination is especially important for venue positioning — at AAAI 2026, differentiating from MathSmith by showing coverage-guided generation > difficulty-guided generation on OMEGA's compositional axis would be a decisive comparison."
    },
    {
      "idea_sketch": "Li's theoretical framework (structural alignment + unambiguity + minimality) + MathGAP's parameterized proof tree generation → empirical validation of the three-condition theory on realistic mathematical reasoning tasks by synthesizing training data that systematically satisfies or violates each condition.",
      "from_papers": ["Li (arXiv 2025)", "MathGAP (ICLR 2025)", "Yao et al. (ICLR 2026)"],
      "why_promising": "Li's theory is validated only on XOR; MathGAP's parameterized generation provides the first realistic testbed where structural alignment can be independently controlled. This would be the first empirical bridge between compositional generalization theory and mathematical reasoning practice."
    },
    {
      "idea_sketch": "SynLogic's logic task generators as auxiliary compositional training + math skill-DAG-guided synthesis → a mixed-domain training regime that uses logic tasks to build compositional circuitry (per Yao et al.'s mechanistic findings) and math frontier data to specialize that circuitry for mathematical composition.",
      "from_papers": ["SynLogic (NeurIPS 2025)", "Yao et al. (ICLR 2026)", "OMEGA (NeurIPS 2025)"],
      "why_promising": "SynLogic shows logic-only training improves AIME by ~10 points (suggesting shared abstract reasoning mechanisms), and Yao et al. show CoT training creates compositional circuits. Combining logic training (for general compositional circuits) with targeted math frontier data (for domain-specific composition) could exploit both mechanisms — nobody has tested this specific mixing strategy."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "GRPO (Group Relative Policy Optimization)",
      "what_it_does": "Eliminates PPO's critic model by normalizing advantages relative to a group of G sampled completions per question: A_i = (r_i - mean(r)) / std(r). Simpler, cheaper, and empirically competitive with PPO for reasoning tasks.",
      "used_by": ["DeepSeek-R1", "MathSmith", "SynLogic", "RL Skill Composition on Countdown"],
      "could_be_applied_to": "RL fine-tuning stage after SFT on frontier-synthesized data — use GRPO with compositional coverage rewards to further refine models beyond what SFT achieves."
    },
    {
      "tool": "Skill graph construction via cross-skill loss reduction",
      "what_it_does": "Measures how training on skill A's data reduces loss on skill B, creating directed edges that encode prerequisite relationships. Produces a DAG of skill dependencies that can guide training data ordering and mixture optimization.",
      "used_by": ["Skill-it", "MASS"],
      "could_be_applied_to": "Constructing the skill dependency DAG from OMEGA's 40 templated generators — train on each generator's data individually and measure cross-generator loss reduction to discover mathematical skill prerequisites automatically."
    },
    {
      "tool": "Computational graph synthesis with back-translation",
      "what_it_does": "Decomposes math problems into executable function sequences, composes novel function subsets into computational graphs that execute to ground-truth answers, then back-translates into natural language problems. Achieves <1% problem error rate.",
      "used_by": ["RV-Syn"],
      "could_be_applied_to": "Generating verifiable problems at identified compositional frontier nodes — once the skill DAG identifies under-covered k-tuples, computational graph composition of corresponding functions produces problems with guaranteed correctness."
    },
    {
      "tool": "Attribute grammar encoding of math skills",
      "what_it_does": "Encodes math skills as non-terminals in an attribute grammar with parameterized filters enforcing skill-specific constraints. Enables programmatic generation of unlimited problems at arbitrary skill granularity with provable validity.",
      "used_by": ["MathCAMPS"],
      "could_be_applied_to": "Formalizing OMEGA's 40 templated generators as attribute grammar productions — this would enable principled composition of generators (combining non-terminals) to produce multi-skill problems with formal guarantees about which skills are exercised."
    },
    {
      "tool": "Fail-rate as automatic difficulty/coverage metric",
      "what_it_does": "Samples n responses from a model and measures the proportion that fail, providing a cheap, model-specific difficulty estimate. Can be adapted from per-query difficulty to per-skill-combination difficulty.",
      "used_by": ["DART-Math", "SynLogic (dual-bound calibration)"],
      "could_be_applied_to": "Measuring which skill compositions are under-covered by computing fail-rates per k-tuple rather than per query — high fail-rate on a specific skill combination indicates a compositional frontier that targeted synthesis should address."
    },
    {
      "tool": "pass@k as reasoning boundary metric",
      "what_it_does": "Evaluates whether a model CAN solve a problem at large sampling budgets (k up to 1024), separating the question 'does the model possess this capability?' from 'does the model reliably produce it?'",
      "used_by": ["oat-zero (NeurIPS 2025 Oral)"],
      "could_be_applied_to": "Evaluating whether frontier-synthesized training data genuinely expands the reasoning boundary (new problems solvable at pass@k that were previously unsolvable) vs. merely improving sampling efficiency on already-solvable problems."
    },
    {
      "tool": "Topic Co-occurrence Probability Matrix (TCPM)",
      "what_it_does": "Builds a matrix of empirical co-occurrence probabilities between skill/topic categories from a corpus of math problems, then samples multi-topic combinations according to this matrix to generate novel but distributionally-aligned problems.",
      "used_by": ["KPDDS (AAAI 2025)"],
      "could_be_applied_to": "Baseline comparison — TCPM represents 'flat' co-occurrence sampling without dependency structure, making it the natural control against DAG-guided frontier sampling. Showing DAG > TCPM on compositional generalization would cleanly isolate the value of dependency structure."
    },
    {
      "tool": "Cycle-consistency validation",
      "what_it_does": "Back-translates generated natural language problems to symbolic form and re-solves, checking that the answer matches the original. Achieves 97.7% faithfulness on MathCAMPS.",
      "used_by": ["MathCAMPS"],
      "could_be_applied_to": "Quality filtering of frontier-synthesized problems — after generating NL problems from compositional graph executions, cycle-consistency ensures the NL problem faithfully represents the intended skill composition."
    },
    {
      "tool": "Compositionality gap metric",
      "what_it_does": "Measures the delta between isolated single-skill accuracy and composed multi-skill accuracy on matched problem pairs, directly quantifying compositional failure independent of absolute performance.",
      "used_by": ["AgentCoMa", "MathTrap"],
      "could_be_applied_to": "Primary evaluation metric for our method — measuring whether skill-DAG-guided synthesis specifically closes the compositionality gap (not just overall accuracy) on OMEGA's compositional axis."
    },
    {
      "tool": "QFT (Question-only Fine-Tuning) for activating question generation",
      "what_it_does": "Fine-tunes on problem texts only (solutions stripped) for 1 epoch to activate latent question-generation capability in instruction-tuned models, enabling cheap synthesis without seed questions or proprietary APIs.",
      "used_by": ["ScaleQuest"],
      "could_be_applied_to": "Generating candidate problems at frontier skill combinations — QFT a model on OMEGA problems filtered to specific skill tuples, then sample to produce novel problems in those compositional regions at minimal cost."
    }
  ],
  "common_pitfalls": [
    "Framing compositional data synthesis as 'data augmentation': MathCAMPS was rejected (5/6/6/6 at ICLR) partly because reviewers saw grammar-based generation as sophisticated augmentation rather than a fundamentally new capability. The contribution must be framed as compositional frontier identification and coverage — the synthesis is the delivery mechanism, not the insight.",
    "Conflating difficulty with compositional complexity: DART-Math's fail-rate, MathSmith's CoT-length proxy, and ScaleQuest's embedding-spread diversity all measure axes orthogonal to compositional coverage. A problem requiring advanced calculus (high difficulty, single skill) is categorically different from one requiring basic algebra + basic geometry + basic probability (low difficulty per skill, novel 3-skill composition). Reviewers who know OMEGA will catch this conflation immediately.",
    "Ignoring the 'random composition baseline' ablation: The seed paper's own quality self-check flags this — if randomly sampling k-skill compositions (without DAG structure) achieves 60-80% of the improvement, the paper is dead. This ablation must be prominent, run early, and ideally show a substantial gap. Historical precedent: Skill-it showed +36.5 points over random on LEGO, setting the expected bar for DAG-over-random gains.",
    "Testing on a single benchmark: MathCAMPS was penalized for GSM8K-only evaluation. DART-Math succeeded partly because it showed +4-5 OOD gains. For AAAI 2026, OMEGA alone is insufficient — MathTrap (EMNLP 2024) and AgentCoMa (2025) should serve as secondary benchmarks, and MathGAP (ICLR 2025) as an optional structural generalization probe.",
    "Relying on GPT-4/proprietary models in the critical synthesis path: KPDDS's heavy GPT-4 dependence limits reproducibility and faces reviewer pushback. ScaleQuest and DART-Math prove that 7B open-source models can drive the entire pipeline. Use Qwen-7B or similar for generation, with GPT-4 only for optional quality validation.",
    "Overclaiming compositional generalization solves 'reasoning': The oat-zero paper and Yao et al. both show fundamental limits — RL cannot exceed base model boundaries, and CoT circuits are fixed to training-time depth. Claims must be scoped to OMEGA's compositional axis specifically, explicitly excluding the transformative axis (novel strategies) which requires different mechanisms entirely.",
    "Ignoring MathSmith as same-venue competition: MathSmith (AAAI 2026) uses concept-pair sampling from PlanetMath with GRPO — it's the most direct competitor and likely shares reviewers. The paper must explicitly differentiate: MathSmith optimizes problem difficulty, we optimize compositional coverage. Ideally, run MathSmith as a baseline and show it fails on OMEGA's compositional axis despite producing hard problems.",
    "Underspecifying the skill extraction step: Moving from OMEGA's 40 templated generators to a skill DAG requires a concrete, reproducible methodology. Vague descriptions of 'extracting skills from templates' will draw reviewer requests for algorithmic detail. The extraction pipeline (whether grammar-based à la MathCAMPS, function-decomposition à la RV-Syn, or embedding-based à la MASS) must be fully specified with coverage statistics.",
    "Neglecting the composition-forgetting tradeoff: MathTrap showed that training on compositional data degrades single-skill performance. If frontier-synthesized training improves compositional accuracy but regresses on single-skill MATH problems, the net result may be ambiguous. Report both metrics and consider data mixing strategies (à la SynLogic's logic+math mixing) to mitigate."
  ],
  "field_trajectory": "The field is converging on three macro-directions that will define 2026-2027 research. First, the 'RL ceiling' discovery (oat-zero, NeurIPS 2025 Oral) is redirecting attention from post-training RL back to pre-training and SFT data design — if RL merely redistributes existing capability, the frontier is in what data the base model ingests, not how it's reinforced. This makes data-centric approaches to compositional generalization (our direction) timely and high-impact. Second, the field is moving from 'more data' to 'structured data' — OpenMathInstruct-2 showed question diversity dominates solution diversity, DART-Math showed difficulty-targeted selection outperforms 4x volume, and the EMNLP 2025 analysis confirmed that data structure dominates data quantity. The natural next step is moving from single-axis structuring (difficulty OR diversity OR coverage) to multi-axis structuring (difficulty × compositional coverage × skill dependency), which nobody has attempted. Third, verifiable synthesis pipelines (RV-Syn, SynLogic, MathCAMPS) are establishing a new quality standard where synthetic data is correct by construction rather than filtered post-hoc — this will become table stakes by 2027, and methods that generate unverifiable problems will face increasing reviewer skepticism. The specific intersection we target — skill-DAG-guided compositional frontier synthesis with verifiable generation — sits at the convergence of all three trends, which is why the timing is right for AAAI 2026.",
  "meta_advice": "If you're writing this paper for AAAI 2026, here is what will make or break it. First, run the random-composition baseline on day one — if randomly sampling k-skill compositions from OMEGA's generators closes 80%+ of the gap that DAG-guided selection achieves, pivot immediately. Skill-it showed a 36.5-point gap between graph-guided and random selection on LEGO; you need a comparable gap on OMEGA. Second, your strongest reviewer-convincing move is the 'compositional frontier map' — a visualization showing which k-tuples of OMEGA skills are covered vs. uncovered in standard training data (OpenMathInstruct-2's 600K questions), with model accuracy overlaid. This makes the gap viscerally obvious and is the kind of figure that lands in acceptance arguments. Third, differentiate aggressively from MathSmith (same venue): run MathSmith as a baseline and show it generates hard problems that are compositionally redundant — high difficulty, low frontier coverage, no compositional generalization gain on OMEGA. This positions your work as solving an orthogonal problem, not competing on the same axis. Fourth, keep the method modular: skill extraction from OMEGA templates (Section 3.1), DAG construction via cross-skill loss reduction (Section 3.2), frontier identification via information-theoretic selection (Section 3.3), and verifiable problem synthesis at frontier nodes (Section 3.4). Each component should have its own ablation. Reviewers reward clean modularity because it enables future work. Fifth, stay within compute budget by using Qwen-7B throughout and targeting 50K-100K frontier-synthesized problems (DART-Math proved 590K is overkill when selection is principled; RV-Syn got SOTA with 50K). Report exact H100-hours. Sixth, include MathTrap and AgentCoMa as secondary benchmarks to preempt the 'benchmark-specific improvement' criticism — even small consistent gains across three benchmarks are more convincing than a large gain on one. Finally, the honest limitations section should acknowledge three things: (1) OMEGA's 40 generators define a finite skill space that may not cover all mathematical composition, (2) the composition-forgetting tradeoff (per MathTrap) may limit net improvement without mixing strategies, and (3) this addresses OMEGA's compositional axis but explicitly not the transformative axis. Reviewers trust papers that know their boundaries."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f605c3a-a644-4d51-98dc-927138e997d6",
  "isSidechain": false,
  "requestId": "req_011CbWKbf28sF5KBp6quoPMS",
  "type": "assistant",
  "uuid": "703459d5-0644-49cc-8ad4-dd605dec9095",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKNV8NyTRP1YgrmB6iv72D",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12620,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8184,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12620
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "703459d5-0644-49cc-8ad4-dd605dec9095",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize compositional frontier research strategy for AAAI 2026",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "703459d5-0644-49cc-8ad4-dd605dec9095",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize compositional frontier research strategy for AAAI 2026",
  "sessionId": "d6a46929-f053-493c-8f7d-5f148e2920f7"
}
```

---
