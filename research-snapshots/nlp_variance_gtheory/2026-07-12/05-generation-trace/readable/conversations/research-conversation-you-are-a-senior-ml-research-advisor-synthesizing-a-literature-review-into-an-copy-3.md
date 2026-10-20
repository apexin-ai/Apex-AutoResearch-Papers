# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/0cad6145-8f2c-45d1-84a8-a65b48703a38.jsonl`
- **Structured JSON:** [`6931ba9915d1d35113bd.json`](../../sessions/69/6931ba9915d1d35113bd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:21:03.598Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:21:03.598Z",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Research area: Synthetic Data and Self-Improvement for Mathematical Reasoning Training\n\n## Paper analyses (19 papers)\n\n[\n  {\n    \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\",\n    \"venue\": \"Nature 2025 (volume 645, pp. 633-638) / arXiv 2501.12948\",\n    \"problem_identification\": \"Prior approaches to enhancing LLM reasoning depended on human-annotated reasoning traces (chain-of-thought demonstrations for SFT), which are expensive, introduce human cognitive biases, and fundamentally cap model performance at the level of the provided exemplars. The authors identified that this SFT-first paradigm may actually constrain the model's ability to explore novel, non-human-like reasoning pathways. They found this gap by hypothesizing — and then empirically validating — that a pre-trained base model already possesses latent reasoning capabilities that supervised demonstrations may suppress rather than unlock.\",\n    \"key_insight\": \"You don't need to teach LLMs HOW to reason through demonstrations; you only need to provide the right incentive structure (verifiable outcome rewards) and let RL discover reasoning strategies autonomously. The pre-trained model already 'knows' enough — the bottleneck is elicitation, not instruction. This reframes reasoning enhancement from an imitation problem to an exploration problem.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"The paper introduces two models. DeepSeek-R1-Zero applies Group Relative Policy Optimization (GRPO) directly to a base model (DeepSeek-V3-Base, 671B MoE) without any SFT, using only rule-based accuracy and format rewards — deliberately avoiding neural reward models due to reward hacking at scale. GRPO simplifies PPO by replacing the learned value/critic network with group-normalized advantage estimation: for each question, G=16 outputs are sampled, and advantages are computed as z-score-normalized rewards across the group. This pure-RL approach produced emergent behaviors including self-reflection, verification, and dynamic strategy adaptation (the famous 'aha moment'). DeepSeek-R1 then addresses R1-Zero's readability and language-mixing issues through a four-stage pipeline: (1) cold-start SFT on thousands of curated CoT examples to establish readable format, (2) reasoning-focused RL with language-consistency rewards, (3) rejection sampling from RL checkpoints to collect ~600K reasoning + ~200K non-reasoning samples for broad SFT, and (4) a secondary RL stage for helpfulness/harmlessness alignment. The reasoning patterns were then distilled into smaller models (1.5B–70B), where distillation outperformed applying RL directly to small models.\",\n    \"what_makes_it_good\": \"Three factors made this Nature-worthy: (1) A paradigm-challenging empirical result — pure RL without supervised reasoning data produces emergent, sophisticated reasoning behaviors that match OpenAI o1 on AIME (79.8% pass@1) and MATH-500 (97.3%), which is a genuinely surprising finding that reshapes the field's understanding of what drives reasoning in LLMs. (2) Compelling qualitative evidence — the 'aha moment' where the model spontaneously learns to say 'Wait, wait. Wait. That's an aha moment I can flag here' and reevaluate its approach is both scientifically significant and accessible to a broad audience, making it ideal for Nature's interdisciplinary readership. (3) The work was fully open-sourced (model weights, distilled variants) at a time when frontier reasoning models were closed, giving the paper outsized practical impact and earning >1000 citations within months.\",\n    \"limitations_acknowledged\": \"The authors explicitly acknowledge: (1) pure RL only works for tasks with reliable verifiable rewards — extending to creative/open-ended tasks where robust reward signals are hard to construct remains an open challenge; (2) language mixing persists in non-English/Chinese queries; (3) the model exhibits token inefficiency ('overthinking') on simple problems; (4) sensitivity to prompt formatting (few-shot prompting degrades performance); (5) process reward models (PRM) and Monte Carlo Tree Search (MCTS) were tried and failed — PRM due to difficulty defining fine-grained steps and reward hacking, MCTS due to exponential search space of token generation.\",\n    \"open_questions\": [\n      \"How can RL-based reasoning be extended to domains without clean verifiable rewards (e.g., creative writing, open-ended reasoning, scientific hypothesis generation)? The paper's own analysis suggests this is THE fundamental bottleneck — the success of pure RL is entirely predicated on having a reliable verifier.\",\n      \"What is the minimal base model capability threshold for emergent reasoning to appear under RL? The paper uses a 671B MoE model — would the 'aha moment' and self-reflection emerge in models an order of magnitude smaller, or is there a phase transition? The distillation results (where small models learn reasoning from large-model traces but not from RL alone) hint that base model scale is critical for discovery but not for execution.\",\n      \"Can the cold-start / multi-stage pipeline be replaced by curriculum design within pure RL? The paper's R1-Zero shows remarkable reasoning but poor readability — is this a fundamental trade-off between exploration freedom and output quality, or an artifact of reward design that could be solved with better format rewards?\"\n    ],\n    \"building_blocks\": [\n      \"GRPO (Group Relative Policy Optimization) — critic-free RL algorithm with group-normalized advantages\",\n      \"Rule-based reward design (accuracy + format rewards, deliberately no neural reward models)\",\n      \"DeepSeek-V3-Base (671B MoE with 37B active params) as pre-trained foundation\",\n      \"Cold-start data pipeline: R1-Zero outputs → filtering → human annotation → LLM rewriting → verification\",\n      \"Rejection sampling from RL checkpoints to create synthetic SFT data (~600K reasoning samples)\",\n      \"Language consistency reward (proportion of target-language words in CoT)\",\n      \"Multi-stage training pipeline (cold-start SFT → reasoning RL → rejection sampling SFT → alignment RL)\",\n      \"Knowledge distillation from reasoning model to smaller models (Qwen-1.5B/7B/14B/32B, Llama-8B/70B)\",\n      \"vLLM-based rollout infrastructure with expert parallelism for MoE and speculative decoding\",\n      \"DeepSeek-V3 as generative reward model (judge) for non-deterministic answers\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is foundational to synthetic data and self-improvement for mathematical reasoning: it demonstrates that RL alone (without human reasoning traces) generates synthetic reasoning trajectories that surpass human-annotated data in quality. The rejection sampling stage — where the model's own RL-trained outputs become SFT training data — is a pure self-improvement loop. The distillation results show that reasoning patterns 'discovered' by large models through self-play can be transferred to smaller models more effectively than having those small models do RL themselves, establishing a scalable synthetic-data pipeline: large model explores via RL → generates synthetic CoT data → distills to smaller models. This is directly the paradigm our research area should build on — the key lesson is that the quality of synthetic reasoning data depends more on the exploration/verification framework (RL + verifier) than on human curation.\"\n  },\n  {\n    \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\",\n    \"venue\": \"arXiv 2024 preprint (5,800+ citations; not formally peer-reviewed at a conference, but arguably more influential than most published papers — GRPO became the de facto RL algorithm for reasoning training)\",\n    \"problem_identification\": \"The authors identified two compounding bottlenecks preventing open-source models from matching proprietary ones on mathematical reasoning: (1) insufficient high-quality math pre-training data — existing corpora like OpenWebMath were 9× smaller than what was available in Common Crawl, and (2) PPO-based RL for reasoning required a separate critic model that roughly doubled GPU memory, making it impractical at scale. They found these gaps not through abstract theorizing but through systematic empirical auditing — training small 1.3B models on every available math corpus and measuring what actually moved benchmarks.\",\n    \"key_insight\": \"You don't need a learned value function to estimate advantages in RLHF — if you sample a group of outputs for the same question, the group's own reward statistics (mean, std) serve as a sufficient baseline. This eliminates the critic model entirely, cutting memory by ~50% and removing a major source of training instability, while the group-relative normalization naturally handles reward scale differences across questions.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"DeepSeekMath operates through three stages. First, a web-scale math data pipeline iteratively trains a fastText classifier seeded from OpenWebMath, then enriches it via domain-level analysis of Common Crawl (identifying math-heavy domains and adding their uncollected pages), running 4 iterations to convergence at 120B tokens (9× OpenWebMath). Second, continued pre-training on DeepSeek-Coder-Base 7B with a 56% math / 20% code / 10% arXiv / 10% NL mix for 500B tokens, followed by SFT on 776K math instruction examples. Third, GRPO: for each question, sample G=64 outputs from the current policy, score them with a reward model, compute advantages as normalized group-relative rewards Â_i = (r_i − mean(r))/std(r), and optimize a clipped surrogate objective with a KL penalty to the reference policy — no critic model needed. The paper also provides a unified framework showing SFT, RFT, DPO, and PPO as special cases of the same gradient update equation differing only in data source, reward function, and gradient coefficient.\",\n    \"what_makes_it_good\": \"Three qualities made this paper exceptionally impactful: (1) Engineering rigor married to conceptual elegance — the data pipeline is reproducible and the GRPO derivation is clean enough that anyone can implement it in 50 lines, (2) A unified theoretical framework (Table 10) that reframes SFT/RFT/DPO/PPO/GRPO as points in a single design space, giving the community a shared vocabulary and making GRPO's position self-evident rather than ad hoc, and (3) Surprising negative results presented honestly — arXiv papers providing zero benefit to math reasoning, and RL improving Maj@K but not Pass@1 — which signal intellectual integrity and provide genuine scientific insight beyond the headline numbers.\",\n    \"limitations_acknowledged\": \"The authors note weakness on geometry and formal theorem proving (triangle/ellipse problems), limited few-shot improvement capability compared to GPT-4, potential data selection bias in the pipeline, and the inherent constraint of 7B model scale. They also honestly flag that their arXiv-is-useless finding hasn't been tested at larger scales or in combination with other data.\",\n    \"open_questions\": [\n      \"Why does arXiv pre-training fail to improve math reasoning? Is it a formatting issue (LaTeX vs natural language), a distribution mismatch (research-level vs competition-level math), or does it only help at larger scales? This remains genuinely unexplained and is a rich research direction.\",\n      \"GRPO's group-relative baseline works well but is a crude estimator — can process-level reward models or learned baselines within the GRPO framework further improve sample efficiency without reintroducing the critic model's memory overhead?\",\n      \"The paper shows RL improves Maj@K but not Pass@1, suggesting it reshapes the output distribution rather than expanding capabilities. Does this mean RL's primary value is alignment (concentrating probability on correct solutions) rather than capability gain? If so, what training signal actually expands the model's mathematical frontier?\"\n    ],\n    \"building_blocks\": [\n      \"FastText classifier for web-scale data curation with iterative domain enrichment\",\n      \"GRPO algorithm (drop-in PPO replacement, ~50% memory reduction)\",\n      \"Unified RL paradigm framework (data source × reward function × gradient coefficient)\",\n      \"DeepSeekMath Corpus (120B tokens, publicly referenced pipeline)\",\n      \"Group-relative advantage estimation (no critic model needed)\",\n      \"10-gram / 3-gram benchmark decontamination protocol\",\n      \"Code pre-training as a reasoning capability catalyst\",\n      \"Multi-stage training recipe: continued pre-training → SFT → RL\",\n      \"Outcome vs process supervision comparison within GRPO\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is foundational to our research area — it established both the dominant RL algorithm (GRPO) and the dominant data curation methodology for mathematical reasoning training. For synthetic data and self-improvement, its key lesson is architectural: GRPO's group-relative scoring is itself a form of self-improvement where the model's own output distribution provides the training signal, eliminating external dependencies. Any work on synthetic data for math reasoning must either build on GRPO or explain why an alternative is better. The unified paradigm framework (Table 10) is particularly valuable as a design tool for positioning new methods in the landscape.\"\n  },\n  {\n    \"title\": \"rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking\",\n    \"venue\": \"ICML 2025 (Oral)\",\n    \"problem_identification\": \"The authors identified a three-part bottleneck in training small models for math reasoning: (1) synthetic training data suffers from undetectable intermediate-step errors even when final answers are correct, (2) process reward models require expensive human annotation and automated alternatives produce noisy scores, and (3) distillation from superior models creates a capability ceiling — hard problems the teacher can't solve are permanently excluded. They found this gap by observing that scaling up CoT data yields diminishing returns (OpenMathInstruct-2 gained only 3.9% despite 8× more data), pointing to a data quality rather than quantity problem.\",\n    \"key_insight\": \"The core insight is that MCTS rollouts with code-verified intermediate steps can simultaneously solve TWO problems at once: generating high-quality training trajectories (where every step is verified by code execution, not just the final answer) AND producing reliable Q-value signals that, when converted to preference pairs rather than used as direct reward labels, yield a process reward model accurate enough to guide subsequent rounds of even better data generation — creating a virtuous self-improvement cycle without any stronger teacher model.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"rStar-Math decomposes math problem-solving into a tree search where each node is a reasoning step paired with executable Python code — only steps whose code runs successfully are kept, filtering out intermediate errors that plague standard CoT synthesis. MCTS with UCT selection explores solution trajectories, and terminal outcomes (correct/incorrect) are back-propagated as Q-values to each step. Rather than regressing directly on noisy Q-values to train a process reward model, they construct preference pairs (high-Q correct vs. low-Q incorrect steps) and train a Process Preference Model (PPM) with Bradley-Terry pairwise ranking loss. The system self-evolves over 4 rounds: Round 1 bootstraps from a large model to get initial data, Round 2 trains the first PPM, Round 3 uses the PPM to guide MCTS (dramatically improving data quality), and Round 4 scales rollouts (64-128) to crack remaining hard problems. The policy SLM and PPM co-evolve, with each round's better policy generating better training signal for the PPM and vice versa.\",\n    \"what_makes_it_good\": \"This paper succeeds because it delivers a shocking empirical result (7B model matching o1-mini at 90% MATH) backed by a carefully ablated system where each component's contribution is isolated — the ablation showing code-augmented CoT beats rejection sampling by 5%, PPM beats ORM by 6.8%, and each self-evolution round yields measurable gains. The finding that PPM becomes the key performance determinant once the policy model is reasonably strong is a genuine architectural insight, not just an engineering trick. Reviewers gave 4-5/5 scores, praising the systematic self-evolution framework and the strong results across seven diverse benchmarks including out-of-domain tests like GaoKao.\",\n    \"limitations_acknowledged\": \"The authors acknowledge inability to handle geometry problems requiring visual understanding (8 of their unsolved AIME problems were geometry-based), and note the approach depends on domains with verifiable correctness criteria — extending to tasks requiring human judgment or mutual LLM verification remains challenging. The self-evolution process is also computationally expensive (weeks on multi-node H100/A100 clusters).\",\n    \"open_questions\": [\n      \"Can the self-evolution loop continue beyond 4 rounds, or does it hit a ceiling? The data coverage went from 60% to 90% — what happens with rounds 5-10, and is there an inherent limit set by the training problem distribution?\",\n      \"The bootstrapping Round 1 uses DeepSeek-Coder-V2-Instruct (236B) — how sensitive is the entire pipeline to this initialization? Could a weaker bootstrap (e.g., starting from the 7B model itself with random sampling) still converge, just more slowly?\",\n      \"The PPM is trained on preference pairs from MCTS Q-values, but the Q-values themselves depend on the PPM in later rounds — could this circular dependency lead to reward model collapse or systematic biases in which solution strategies are preferred?\"\n    ],\n    \"building_blocks\": [\n      \"Monte Carlo Tree Search (MCTS) with UCT for multi-step reasoning decomposition\",\n      \"Code-augmented Chain-of-Thought where each NL reasoning step has paired executable Python verification\",\n      \"Process Preference Model (PPM) trained via Bradley-Terry pairwise ranking loss on MCTS Q-value-derived preference pairs\",\n      \"Iterative self-evolution / self-play loop between policy model and reward model\",\n      \"Q-value back-propagation from terminal nodes through the search tree\",\n      \"Qwen2.5-Math and Phi3-mini as base SLMs\",\n      \"747K math problems aggregated from multiple sources as training problem set\"\n    ],\n    \"reviewer_feedback_summary\": \"Reviewers scored 4-5/5 with consensus on acceptance. Key praise: strong empirical results across diverse benchmarks, systematic ablations isolating each component's contribution, and practical significance of small models matching frontier performance. Key concerns: (1) use of 236B DeepSeek model in Round 1 seeming to contradict 'no distillation' claims — authors clarified it only provides initial formatting, not capability transfer; (2) computational cost of the pipeline (weeks of GPU time) — authors detailed that policy training is only 20 hours, with data generation being the real bottleneck at 2-3 days per round; (3) MCTS parameter sensitivity — authors provided additional experiments showing saturation beyond 32 candidate nodes and 64 rollouts. One reviewer flagged reward hacking risks, which authors addressed by noting offline MCTS updates and preference-based training mitigate typical RL exploitation.\",\n    \"relevance_to_seed\": \"This paper is a blueprint for our research area of synthetic data and self-improvement for mathematical reasoning. Its key transferable lessons are: (1) data quality via step-level code verification beats data quantity via scaling, (2) converting noisy reward signals into preference pairs is more robust than direct regression, and (3) co-evolution of the policy and reward model creates a compounding improvement loop that avoids the capability ceiling of teacher-model distillation. The specific PPM training methodology and self-evolution recipe are directly reusable building blocks for any work on iterative self-improvement.\"\n  },\n  {\n    \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"Prior work on test-time compute scaling showed conflicting results — some approaches helped on reasoning while others showed limited gains — but nobody had systematically analyzed WHY. The authors identified the gap by observing that no prior work studied the scaling behaviors of different inference methods as a function of problem difficulty. This led them to ask: given a fixed compute budget at test time, what is the optimal way to spend it, and does the answer change depending on the problem?\",\n    \"key_insight\": \"The effectiveness of test-time compute strategies is fundamentally difficulty-dependent: easy problems benefit from sequential refinement (local search), hard problems need parallel sampling (global search), and beam search can actually hurt on easy problems by exploiting verifier errors. This means a single uniform strategy wastes compute — an adaptive, difficulty-aware allocation achieves 4x efficiency gains by selecting the right strategy per problem.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"The paper frames all test-time compute through a unified proposer-verifier abstraction (analogous to MCMC with a proposal distribution and score function), then systematically studies two scaling mechanisms: (1) search against process reward models (PRMs) — comparing best-of-N weighted sampling, beam search, and lookahead search — where PRMs are trained via Monte Carlo rollouts rather than expensive human labels; and (2) iterative self-revision, where a model is fine-tuned to condition on its own prior (incorrect) attempts and improve upon them. The key methodological contribution is the compute-optimal strategy: bin problems by difficulty (estimated via averaged verifier scores at deployment), then independently select the best hyperparameters (search method, beam width, sequential-vs-parallel ratio) for each difficulty bin. This is validated against a FLOPs-matched comparison showing when test-time compute beats scaling model size by 14x.\",\n    \"what_makes_it_good\": \"The paper succeeds because it transforms a vague intuition ('more inference compute helps') into a rigorous, quantitative framework with actionable engineering guidance. Reviewers praised the unified proposer-verifier framing, the thoroughness of ablations across difficulty levels, and the provocative FLOPs-matched comparison against larger models. The paper is also strategically well-timed — it provides the foundational analysis that the entire field of 'reasoning models' (o1, etc.) would need, making it instantly high-impact.\",\n    \"limitations_acknowledged\": \"All experiments are on a single dataset (MATH) with a single model family (PaLM 2-S*), and the authors candidly state that on the hardest problems 'no method makes much meaningful progress,' limiting the generality of the test-time-beats-pretraining claim. Estimating question difficulty via 2048 samples is prohibitively expensive for deployment, creating an exploration-exploitation tradeoff the paper leaves unresolved.\",\n    \"open_questions\": [\n      \"Does the difficulty-dependent compute-optimal strategy generalize beyond math to other reasoning domains (code, science, planning), and does the optimal strategy surface change with different base model architectures and sizes?\",\n      \"Can search (PRMs) and revision be combined synergistically — e.g., tree search over revision trajectories — and would this unlock gains on the hardest problems where both individually fail?\",\n      \"How can difficulty estimation be made cheap enough for real-time deployment — can a lightweight classifier or the model's own uncertainty replace the expensive sampling-based oracle?\"\n    ],\n    \"building_blocks\": [\n      \"Process Reward Models (PRMs) trained via Monte Carlo rollouts (no human labels needed)\",\n      \"Best-of-N weighted sampling with per-step PRM score aggregation\",\n      \"Beam search and lookahead search over solution steps\",\n      \"Self-revision fine-tuning using edit-distance-correlated incorrect trajectories\",\n      \"Difficulty binning as a sufficient statistic for strategy selection\",\n      \"FLOPs-matched evaluation framework comparing inference vs. pretraining compute\",\n      \"MATH benchmark (12k train / 500 test)\",\n      \"Outcome Reward Models (ORMs) for revision selection\"\n    ],\n    \"reviewer_feedback_summary\": \"Three reviewers gave 8/10 (Accept) and one gave 6/10 (Marginally Above). Key praise: unified proposer-verifier framing, comprehensive experiments with strong ablations, significant practical implications, and insightful difficulty-dependent analysis. Key concerns: (1) all experiments on MATH only — generalizability is the #1 unresolved issue; (2) whether verifier training compute should count in the inference budget (fairness of comparison); (3) the 'compute-optimal' strategy is more proof-of-concept than deployable due to difficulty estimation cost; (4) fine-tuning alternatives not compared against pretraining scaling. Authors addressed concerns effectively — added verifier cost analysis, showed robustness to 20% noise-corrupted verifiers (91.4% accuracy on MATH-500), moved key figures from appendix to main paper, and cited follow-up reproductions on LLaMA/Qwen validating generalizability. The meta-reviewer noted strong author engagement but flagged generalizability and verifier dependency as persistent caveats.\",\n    \"relevance_to_seed\": \"This paper is directly foundational to synthetic data and self-improvement for math reasoning: the PRM training pipeline generates synthetic step-level labels via Monte Carlo rollouts (no human annotation), and the revision model is explicitly a self-improvement loop where the model learns from its own mistakes. The compute-optimal framework teaches us that self-improvement strategies must be difficulty-aware — blindly applying one synthetic data generation or self-refinement strategy across all problems wastes compute and can even hurt performance, a critical design lesson for any self-improvement training pipeline.\"\n  },\n  {\n    \"title\": \"OpenThoughts: Data Recipes for Reasoning Models\",\n    \"venue\": \"ICLR 2026 (Oral)\",\n    \"problem_identification\": \"The authors identified that while frontier reasoning models (DeepSeek-R1, o3) achieve strong results via SFT on curated reasoning data, the complete training recipes are proprietary and unexplored publicly. Prior open-source attempts made ad hoc design choices without systematic ablation, so nobody knew WHICH pipeline decisions actually matter. The gap was visible in the scatter: many projects tried to reproduce reasoning distillation but couldn't match proprietary quality, and nobody had done controlled experiments isolating each pipeline stage to understand causal contributions.\",\n    \"key_insight\": \"Decompose the data generation pipeline into 6 modular, independently testable stages (source → mix → filter questions → dedup/sample → filter answers → teacher selection) and run controlled ablations at each stage. This revealed several counterintuitive findings that challenge conventional wisdom: weaker teacher models produce better training data than stronger ones, answer verification/filtering provides zero benefit over using all samples, source quality dominates diversity (2 good sources beat 16 mixed ones), and the cheapest scaling axis is sampling multiple answers per question rather than collecting more questions.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"The authors constructed a 6-stage data generation pipeline for reasoning model training: (1) question sourcing from 62 diverse strategies (synthetic, semi-synthetic, non-synthetic) across math/code/science, (2) mixing top sources, (3) LLM-based question filtering (difficulty or response-length proxies), (4) deduplication with multiple answer sampling (up to 16× per question), (5) answer verification/filtering, and (6) teacher model selection. Each stage was ablated independently with all other stages held constant, using 31,600 datapoints per experiment across 8 benchmarks. The log-scale midpoint (31.6K) was chosen to balance signal and compute. Winning strategies from each stage were composed and scaled to 1.2M examples (OpenThoughts3), then used to SFT Qwen-2.5-7B into OpenThinker3-7B. Critically, the authors maintained held-out benchmarks (AIME 2025, HMMT, Humanity's Last Exam) never seen during pipeline development, ensuring true generalization measurement.\",\n    \"what_makes_it_good\": \"Three things elevated this paper beyond a technical report: (1) the counterintuitive findings — weaker teachers outperforming stronger ones, answer filtering being useless, quality trumping diversity — are genuinely surprising and challenge widely held assumptions, giving the paper intellectual teeth; (2) the experimental rigor of 1000+ controlled ablations with held-out evaluation creates a level of causal credibility rare in empirical ML; (3) the open-source artifact (dataset + models + code) combined with SOTA results (15-20 point improvements on AIME/GPQA at 7B scale) made it immediately useful, generating community adoption that validated the contribution beyond benchmarks.\",\n    \"limitations_acknowledged\": \"The authors explicitly note they only explored SFT and did not investigate reinforcement learning, staged SFT, or curriculum learning, which are standard components of full reasoning model training. They also acknowledge optimizing for average cross-domain performance rather than per-domain optimization, and leave open the question of what happens as student performance approaches teacher capability.\",\n    \"open_questions\": [\n      \"Why do weaker teacher models produce better training data? The authors hypothesize verbosity matters (QwQ-32B produces longer, more detailed traces than DeepSeek-R1), but the causal mechanism is unexplored — is it about reasoning granularity, error-correction patterns, or something about the capacity gap between teacher and student?\",\n      \"How do these findings change under RL training? The entire ablation study is SFT-only, yet frontier reasoning models use RL extensively. The optimal data recipe for RL reward signals may differ substantially from SFT recipes.\",\n      \"What is the scaling ceiling? Student performance plateaus as it approaches teacher capability — the 10-point gap between OpenThinker3-7B and QwQ-32B is unexplained. Can self-improvement or iterative distillation break through this ceiling without a stronger teacher?\"\n    ],\n    \"building_blocks\": [\n      \"QwQ-32B as teacher model for distillation\",\n      \"Response-length-based question filtering (proxy for difficulty)\",\n      \"16× multiple answer sampling per question for scaling\",\n      \"Exact deduplication over fuzzy/no dedup\",\n      \"LlamaFactory + DeepSpeed v3 training framework\",\n      \"CodeGolf + OpenCodeReasoning (code sources)\",\n      \"OpenMath-2-Math (math source)\",\n      \"StackExchange-Physics + OrganicChemistry-PDFs (science sources)\",\n      \"Cosine LR schedule with 0.1 warmup ratio\",\n      \"Log-scale midpoint experiment sizing (31.6K) for ablation efficiency\",\n      \"Held-out benchmark methodology for pipeline development\"\n    ],\n    \"reviewer_feedback_summary\": \"Scores: 6, 6, 6, 8 (accepted as Oral despite three 6s, suggesting AC/meta-reviewer strongly valued the contribution). PRAISE: All reviewers acknowledged exceptional experimental rigor, practical value of open-source artifacts, and importance of the problem. Reviewer 4 (score 8) specifically praised counterintuitive findings and data decontamination. CONCERNS: Three major critiques recurred — (1) feels like a technical report with limited conceptual novelty (Reviewer 2), (2) lacks deeper causal explanations for WHY things work, especially the weaker-teacher paradox (Reviewers 1, 3), and (3) unfair experimental comparisons in answer filtering (baseline trained on 63.2K vs filtered 31.6K). AUTHORS ADDRESSED: They showed compute-controlled random filtering baselines (Tables 43-45), reframed gains as 30-point over base and 8-point over SFT baselines, and offered the verbose-teacher hypothesis with token-count analysis (Section E.2). The meta-reviewer found the rebuttals convincing, noting the rebuttal 'successfully addressed methodological concerns.'\",\n    \"relevance_to_seed\": \"This paper is directly at the core of our research area — it IS the systematic investigation of synthetic data pipelines for mathematical reasoning training. Its most actionable lessons for us: (1) invest in question quality over question diversity, (2) scale through answer sampling rather than question collection, (3) use response-length as a cheap proxy for question difficulty filtering, (4) don't waste effort on answer verification — and most provocatively, (5) consider using moderately-capable verbose teachers over frontier models for distillation, as the reasoning trace quality matters more than the teacher's benchmark scores.\"\n  },\n  {\n    \"title\": \"DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"The authors performed a diagnostic analysis of existing rejection-tuned synthetic math datasets (e.g., MetaMathQA) and discovered a severe, previously unnoticed bias: vanilla rejection sampling applies equal trial budgets per query, but since harder queries have much lower success rates, the resulting datasets are dominated by easy examples — 51.1% of the hardest MATH training queries received zero correct responses, and Level-5 problems comprised only 10.5% of the final data despite being dominant in the original distribution. This was found through a straightforward but overlooked empirical analysis of dataset difficulty distributions.\",\n    \"key_insight\": \"The distribution of difficulty in synthetic training data matters as much as the volume — by simply reallocating sampling budget to give harder problems more trials (rather than improving the generator model or augmenting queries), you can create smaller but substantially more effective training datasets. The insight is that the bottleneck isn't model capability but sampling allocation policy.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"DART reframes rejection tuning as a resource allocation problem over query difficulty. First, difficulty is measured via 'fail rate' — the proportion of incorrect responses when sampling n_d responses per query from DeepSeekMath-7B-RL. Two allocation strategies are proposed: DARS-Uniform collects a fixed k_u=40 correct responses per query regardless of difficulty (equalizing representation), and DARS-Prop2Diff allocates correct responses proportionally to difficulty score with the hardest queries receiving k_p=192 responses (deliberately over-representing hard problems). Both impose a max raw sample cap n_max per query. Synthesis uses DeepSeekMath-7B-RL at temperature 1.6 with top-p=0.95, generating ~150M raw samples over 160 A100 GPU-days. The resulting datasets (~585-591k samples) are used for standard supervised fine-tuning with cosine scheduling.\",\n    \"what_makes_it_good\": \"This paper succeeds because the core contribution is both simple and surprisingly effective — it reframes an overlooked data distribution problem rather than proposing complex new architectures. The empirical gains are large and robust: +6.9 points on MATH for Llama3-8B over vanilla rejection tuning, while using only a 7B open-weight synthesizer (no GPT-4 dependency). The thorough experimental design — 6 benchmarks including 4 out-of-domain, multiple base models from 7B to 70B, detailed ablations on scaling behavior and coverage effects — demonstrates the kind of comprehensive evaluation that builds reviewer confidence.\",\n    \"limitations_acknowledged\": \"The authors acknowledge that fail rate may be suboptimal as a difficulty metric (alternatives like Elo ratings or learned difficulty scores remain unexplored), and that DART-Math is limited to natural language chain-of-thought reasoning without code execution, which is known to significantly boost math performance. They also note gains diminish for math-specialized models like DeepSeekMath.\",\n    \"open_questions\": [\n      \"What is the optimal difficulty distribution for training data — is linear proportionality to difficulty truly best, or would a learned curriculum (e.g., starting easy, gradually increasing difficulty) outperform static over-representation of hard examples?\",\n      \"How does difficulty-aware sampling interact with query augmentation techniques (e.g., rephrasing, decomposition)? The paper fixes the query set but combining DART with synthetic query generation could compound gains.\",\n      \"Can difficulty-aware allocation be made adaptive during training rather than fixed at data creation time — e.g., dynamically reweighting or resampling based on the student model's evolving competence (online difficulty-aware curriculum learning)?\"\n    ],\n    \"building_blocks\": [\n      \"Rejection sampling / rejection tuning pipeline for synthetic data\",\n      \"Fail rate as a lightweight difficulty metric (proportion of incorrect samples from a reference model)\",\n      \"DeepSeekMath-7B-RL as an open-weight synthesis model\",\n      \"MATH and GSM8K training sets as query sources\",\n      \"Temperature scaling (t=1.6) for diversity in sampling\",\n      \"DARS-Uniform and DARS-Prop2Diff allocation strategies\",\n      \"Answer-matching verification for filtering correct responses\",\n      \"Comprehensive OOD evaluation suite: CollegeMath, TheoremQA, OlympiadBench, DeepMind-Mathematics\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is directly central to our research area — it demonstrates that the data curation policy (how you allocate synthesis compute across problems of varying difficulty) is a powerful and underexplored lever for self-improvement in mathematical reasoning. The key lesson for our work is that naive rejection sampling wastes most compute on already-easy problems; any synthetic data pipeline we build should incorporate difficulty-aware allocation as a baseline, and we should investigate whether more sophisticated adaptive or curriculum-based allocation strategies can push beyond DART's static proportional approach.\"\n  },\n  {\n    \"title\": \"RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"The authors identified that training on model-generated positive synthetic data amplifies spurious correlations in intermediate reasoning steps — steps that happen to co-occur with correct final answers but are causally misleading. They found this by going beyond final-answer accuracy and examining *why* RFT scaling plateaus: positive traces contain incorrect intermediate steps undetectable by outcome-based verification (error ~ D^-0.05 on MATH), and fitting more of such data reinforces these spurious patterns rather than improving generalization. This is a gap others missed because most prior work evaluated synthetic data quality only by final-answer correctness, never dissecting step-level fidelity.\",\n    \"key_insight\": \"Incorrect model-generated solutions are not waste — they are the most informative training signal, because per-step credit assignment on negative traces reveals exactly which reasoning steps cause failure. Formally, DPO on per-step positive/negative pairs is equivalent to advantage-weighted RL, which automatically down-weights spurious steps and up-weights causally critical ones, thereby 'unlearning' the spurious correlations that positive-only training amplifies.\",\n    \"innovation_type\": \"new_formulation\",\n \n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:21:03.601Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:21:03.601Z",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-28T05:21:03.642Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-28 (UTC).**

## Research area: Synthetic Data and Self-Improvement for Mathematical Reasoning Training

## Paper analyses (19 papers)

[
  {
    "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
    "venue": "Nature 2025 (volume 645, pp. 633-638) / arXiv 2501.12948",
    "problem_identification": "Prior approaches to enhancing LLM reasoning depended on human-annotated reasoning traces (chain-of-thought demonstrations for SFT), which are expensive, introduce human cognitive biases, and fundamentally cap model performance at the level of the provided exemplars. The authors identified that this SFT-first paradigm may actually constrain the model's ability to explore novel, non-human-like reasoning pathways. They found this gap by hypothesizing — and then empirically validating — that a pre-trained base model already possesses latent reasoning capabilities that supervised demonstrations may suppress rather than unlock.",
    "key_insight": "You don't need to teach LLMs HOW to reason through demonstrations; you only need to provide the right incentive structure (verifiable outcome rewards) and let RL discover reasoning strategies autonomously. The pre-trained model already 'knows' enough — the bottleneck is elicitation, not instruction. This reframes reasoning enhancement from an imitation problem to an exploration problem.",
    "innovation_type": "simplification",
    "method_summary": "The paper introduces two models. DeepSeek-R1-Zero applies Group Relative Policy Optimization (GRPO) directly to a base model (DeepSeek-V3-Base, 671B MoE) without any SFT, using only rule-based accuracy and format rewards — deliberately avoiding neural reward models due to reward hacking at scale. GRPO simplifies PPO by replacing the learned value/critic network with group-normalized advantage estimation: for each question, G=16 outputs are sampled, and advantages are computed as z-score-normalized rewards across the group. This pure-RL approach produced emergent behaviors including self-reflection, verification, and dynamic strategy adaptation (the famous 'aha moment'). DeepSeek-R1 then addresses R1-Zero's readability and language-mixing issues through a four-stage pipeline: (1) cold-start SFT on thousands of curated CoT examples to establish readable format, (2) reasoning-focused RL with language-consistency rewards, (3) rejection sampling from RL checkpoints to collect ~600K reasoning + ~200K non-reasoning samples for broad SFT, and (4) a secondary RL stage for helpfulness/harmlessness alignment. The reasoning patterns were then distilled into smaller models (1.5B–70B), where distillation outperformed applying RL directly to small models.",
    "what_makes_it_good": "Three factors made this Nature-worthy: (1) A paradigm-challenging empirical result — pure RL without supervised reasoning data produces emergent, sophisticated reasoning behaviors that match OpenAI o1 on AIME (79.8% pass@1) and MATH-500 (97.3%), which is a genuinely surprising finding that reshapes the field's understanding of what drives reasoning in LLMs. (2) Compelling qualitative evidence — the 'aha moment' where the model spontaneously learns to say 'Wait, wait. Wait. That's an aha moment I can flag here' and reevaluate its approach is both scientifically significant and accessible to a broad audience, making it ideal for Nature's interdisciplinary readership. (3) The work was fully open-sourced (model weights, distilled variants) at a time when frontier reasoning models were closed, giving the paper outsized practical impact and earning >1000 citations within months.",
    "limitations_acknowledged": "The authors explicitly acknowledge: (1) pure RL only works for tasks with reliable verifiable rewards — extending to creative/open-ended tasks where robust reward signals are hard to construct remains an open challenge; (2) language mixing persists in non-English/Chinese queries; (3) the model exhibits token inefficiency ('overthinking') on simple problems; (4) sensitivity to prompt formatting (few-shot prompting degrades performance); (5) process reward models (PRM) and Monte Carlo Tree Search (MCTS) were tried and failed — PRM due to difficulty defining fine-grained steps and reward hacking, MCTS due to exponential search space of token generation.",
    "open_questions": [
      "How can RL-based reasoning be extended to domains without clean verifiable rewards (e.g., creative writing, open-ended reasoning, scientific hypothesis generation)? The paper's own analysis suggests this is THE fundamental bottleneck — the success of pure RL is entirely predicated on having a reliable verifier.",
      "What is the minimal base model capability threshold for emergent reasoning to appear under RL? The paper uses a 671B MoE model — would the 'aha moment' and self-reflection emerge in models an order of magnitude smaller, or is there a phase transition? The distillation results (where small models learn reasoning from large-model traces but not from RL alone) hint that base model scale is critical for discovery but not for execution.",
      "Can the cold-start / multi-stage pipeline be replaced by curriculum design within pure RL? The paper's R1-Zero shows remarkable reasoning but poor readability — is this a fundamental trade-off between exploration freedom and output quality, or an artifact of reward design that could be solved with better format rewards?"
    ],
    "building_blocks": [
      "GRPO (Group Relative Policy Optimization) — critic-free RL algorithm with group-normalized advantages",
      "Rule-based reward design (accuracy + format rewards, deliberately no neural reward models)",
      "DeepSeek-V3-Base (671B MoE with 37B active params) as pre-trained foundation",
      "Cold-start data pipeline: R1-Zero outputs → filtering → human annotation → LLM rewriting → verification",
      "Rejection sampling from RL checkpoints to create synthetic SFT data (~600K reasoning samples)",
      "Language consistency reward (proportion of target-language words in CoT)",
      "Multi-stage training pipeline (cold-start SFT → reasoning RL → rejection sampling SFT → alignment RL)",
      "Knowledge distillation from reasoning model to smaller models (Qwen-1.5B/7B/14B/32B, Llama-8B/70B)",
      "vLLM-based rollout infrastructure with expert parallelism for MoE and speculative decoding",
      "DeepSeek-V3 as generative reward model (judge) for non-deterministic answers"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is foundational to synthetic data and self-improvement for mathematical reasoning: it demonstrates that RL alone (without human reasoning traces) generates synthetic reasoning trajectories that surpass human-annotated data in quality. The rejection sampling stage — where the model's own RL-trained outputs become SFT training data — is a pure self-improvement loop. The distillation results show that reasoning patterns 'discovered' by large models through self-play can be transferred to smaller models more effectively than having those small models do RL themselves, establishing a scalable synthetic-data pipeline: large model explores via RL → generates synthetic CoT data → distills to smaller models. This is directly the paradigm our research area should build on — the key lesson is that the quality of synthetic reasoning data depends more on the exploration/verification framework (RL + verifier) than on human curation."
  },
  {
    "title": "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models",
    "venue": "arXiv 2024 preprint (5,800+ citations; not formally peer-reviewed at a conference, but arguably more influential than most published papers — GRPO became the de facto RL algorithm for reasoning training)",
    "problem_identification": "The authors identified two compounding bottlenecks preventing open-source models from matching proprietary ones on mathematical reasoning: (1) insufficient high-quality math pre-training data — existing corpora like OpenWebMath were 9× smaller than what was available in Common Crawl, and (2) PPO-based RL for reasoning required a separate critic model that roughly doubled GPU memory, making it impractical at scale. They found these gaps not through abstract theorizing but through systematic empirical auditing — training small 1.3B models on every available math corpus and measuring what actually moved benchmarks.",
    "key_insight": "You don't need a learned value function to estimate advantages in RLHF — if you sample a group of outputs for the same question, the group's own reward statistics (mean, std) serve as a sufficient baseline. This eliminates the critic model entirely, cutting memory by ~50% and removing a major source of training instability, while the group-relative normalization naturally handles reward scale differences across questions.",
    "innovation_type": "combination",
    "method_summary": "DeepSeekMath operates through three stages. First, a web-scale math data pipeline iteratively trains a fastText classifier seeded from OpenWebMath, then enriches it via domain-level analysis of Common Crawl (identifying math-heavy domains and adding their uncollected pages), running 4 iterations to convergence at 120B tokens (9× OpenWebMath). Second, continued pre-training on DeepSeek-Coder-Base 7B with a 56% math / 20% code / 10% arXiv / 10% NL mix for 500B tokens, followed by SFT on 776K math instruction examples. Third, GRPO: for each question, sample G=64 outputs from the current policy, score them with a reward model, compute advantages as normalized group-relative rewards Â_i = (r_i − mean(r))/std(r), and optimize a clipped surrogate objective with a KL penalty to the reference policy — no critic model needed. The paper also provides a unified framework showing SFT, RFT, DPO, and PPO as special cases of the same gradient update equation differing only in data source, reward function, and gradient coefficient.",
    "what_makes_it_good": "Three qualities made this paper exceptionally impactful: (1) Engineering rigor married to conceptual elegance — the data pipeline is reproducible and the GRPO derivation is clean enough that anyone can implement it in 50 lines, (2) A unified theoretical framework (Table 10) that reframes SFT/RFT/DPO/PPO/GRPO as points in a single design space, giving the community a shared vocabulary and making GRPO's position self-evident rather than ad hoc, and (3) Surprising negative results presented honestly — arXiv papers providing zero benefit to math reasoning, and RL improving Maj@K but not Pass@1 — which signal intellectual integrity and provide genuine scientific insight beyond the headline numbers.",
    "limitations_acknowledged": "The authors note weakness on geometry and formal theorem proving (triangle/ellipse problems), limited few-shot improvement capability compared to GPT-4, potential data selection bias in the pipeline, and the inherent constraint of 7B model scale. They also honestly flag that their arXiv-is-useless finding hasn't been tested at larger scales or in combination with other data.",
    "open_questions": [
      "Why does arXiv pre-training fail to improve math reasoning? Is it a formatting issue (LaTeX vs natural language), a distribution mismatch (research-level vs competition-level math), or does it only help at larger scales? This remains genuinely unexplained and is a rich research direction.",
      "GRPO's group-relative baseline works well but is a crude estimator — can process-level reward models or learned baselines within the GRPO framework further improve sample efficiency without reintroducing the critic model's memory overhead?",
      "The paper shows RL improves Maj@K but not Pass@1, suggesting it reshapes the output distribution rather than expanding capabilities. Does this mean RL's primary value is alignment (concentrating probability on correct solutions) rather than capability gain? If so, what training signal actually expands the model's mathematical frontier?"
    ],
    "building_blocks": [
      "FastText classifier for web-scale data curation with iterative domain enrichment",
      "GRPO algorithm (drop-in PPO replacement, ~50% memory reduction)",
      "Unified RL paradigm framework (data source × reward function × gradient coefficient)",
      "DeepSeekMath Corpus (120B tokens, publicly referenced pipeline)",
      "Group-relative advantage estimation (no critic model needed)",
      "10-gram / 3-gram benchmark decontamination protocol",
      "Code pre-training as a reasoning capability catalyst",
      "Multi-stage training recipe: continued pre-training → SFT → RL",
      "Outcome vs process supervision comparison within GRPO"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is foundational to our research area — it established both the dominant RL algorithm (GRPO) and the dominant data curation methodology for mathematical reasoning training. For synthetic data and self-improvement, its key lesson is architectural: GRPO's group-relative scoring is itself a form of self-improvement where the model's own output distribution provides the training signal, eliminating external dependencies. Any work on synthetic data for math reasoning must either build on GRPO or explain why an alternative is better. The unified paradigm framework (Table 10) is particularly valuable as a design tool for positioning new methods in the landscape."
  },
  {
    "title": "rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking",
    "venue": "ICML 2025 (Oral)",
    "problem_identification": "The authors identified a three-part bottleneck in training small models for math reasoning: (1) synthetic training data suffers from undetectable intermediate-step errors even when final answers are correct, (2) process reward models require expensive human annotation and automated alternatives produce noisy scores, and (3) distillation from superior models creates a capability ceiling — hard problems the teacher can't solve are permanently excluded. They found this gap by observing that scaling up CoT data yields diminishing returns (OpenMathInstruct-2 gained only 3.9% despite 8× more data), pointing to a data quality rather than quantity problem.",
    "key_insight": "The core insight is that MCTS rollouts with code-verified intermediate steps can simultaneously solve TWO problems at once: generating high-quality training trajectories (where every step is verified by code execution, not just the final answer) AND producing reliable Q-value signals that, when converted to preference pairs rather than used as direct reward labels, yield a process reward model accurate enough to guide subsequent rounds of even better data generation — creating a virtuous self-improvement cycle without any stronger teacher model.",
    "innovation_type": "combination",
    "method_summary": "rStar-Math decomposes math problem-solving into a tree search where each node is a reasoning step paired with executable Python code — only steps whose code runs successfully are kept, filtering out intermediate errors that plague standard CoT synthesis. MCTS with UCT selection explores solution trajectories, and terminal outcomes (correct/incorrect) are back-propagated as Q-values to each step. Rather than regressing directly on noisy Q-values to train a process reward model, they construct preference pairs (high-Q correct vs. low-Q incorrect steps) and train a Process Preference Model (PPM) with Bradley-Terry pairwise ranking loss. The system self-evolves over 4 rounds: Round 1 bootstraps from a large model to get initial data, Round 2 trains the first PPM, Round 3 uses the PPM to guide MCTS (dramatically improving data quality), and Round 4 scales rollouts (64-128) to crack remaining hard problems. The policy SLM and PPM co-evolve, with each round's better policy generating better training signal for the PPM and vice versa.",
    "what_makes_it_good": "This paper succeeds because it delivers a shocking empirical result (7B model matching o1-mini at 90% MATH) backed by a carefully ablated system where each component's contribution is isolated — the ablation showing code-augmented CoT beats rejection sampling by 5%, PPM beats ORM by 6.8%, and each self-evolution round yields measurable gains. The finding that PPM becomes the key performance determinant once the policy model is reasonably strong is a genuine architectural insight, not just an engineering trick. Reviewers gave 4-5/5 scores, praising the systematic self-evolution framework and the strong results across seven diverse benchmarks including out-of-domain tests like GaoKao.",
    "limitations_acknowledged": "The authors acknowledge inability to handle geometry problems requiring visual understanding (8 of their unsolved AIME problems were geometry-based), and note the approach depends on domains with verifiable correctness criteria — extending to tasks requiring human judgment or mutual LLM verification remains challenging. The self-evolution process is also computationally expensive (weeks on multi-node H100/A100 clusters).",
    "open_questions": [
      "Can the self-evolution loop continue beyond 4 rounds, or does it hit a ceiling? The data coverage went from 60% to 90% — what happens with rounds 5-10, and is there an inherent limit set by the training problem distribution?",
      "The bootstrapping Round 1 uses DeepSeek-Coder-V2-Instruct (236B) — how sensitive is the entire pipeline to this initialization? Could a weaker bootstrap (e.g., starting from the 7B model itself with random sampling) still converge, just more slowly?",
      "The PPM is trained on preference pairs from MCTS Q-values, but the Q-values themselves depend on the PPM in later rounds — could this circular dependency lead to reward model collapse or systematic biases in which solution strategies are preferred?"
    ],
    "building_blocks": [
      "Monte Carlo Tree Search (MCTS) with UCT for multi-step reasoning decomposition",
      "Code-augmented Chain-of-Thought where each NL reasoning step has paired executable Python verification",
      "Process Preference Model (PPM) trained via Bradley-Terry pairwise ranking loss on MCTS Q-value-derived preference pairs",
      "Iterative self-evolution / self-play loop between policy model and reward model",
      "Q-value back-propagation from terminal nodes through the search tree",
      "Qwen2.5-Math and Phi3-mini as base SLMs",
      "747K math problems aggregated from multiple sources as training problem set"
    ],
    "reviewer_feedback_summary": "Reviewers scored 4-5/5 with consensus on acceptance. Key praise: strong empirical results across diverse benchmarks, systematic ablations isolating each component's contribution, and practical significance of small models matching frontier performance. Key concerns: (1) use of 236B DeepSeek model in Round 1 seeming to contradict 'no distillation' claims — authors clarified it only provides initial formatting, not capability transfer; (2) computational cost of the pipeline (weeks of GPU time) — authors detailed that policy training is only 20 hours, with data generation being the real bottleneck at 2-3 days per round; (3) MCTS parameter sensitivity — authors provided additional experiments showing saturation beyond 32 candidate nodes and 64 rollouts. One reviewer flagged reward hacking risks, which authors addressed by noting offline MCTS updates and preference-based training mitigate typical RL exploitation.",
    "relevance_to_seed": "This paper is a blueprint for our research area of synthetic data and self-improvement for mathematical reasoning. Its key transferable lessons are: (1) data quality via step-level code verification beats data quantity via scaling, (2) converting noisy reward signals into preference pairs is more robust than direct regression, and (3) co-evolution of the policy and reward model creates a compounding improvement loop that avoids the capability ceiling of teacher-model distillation. The specific PPM training methodology and self-evolution recipe are directly reusable building blocks for any work on iterative self-improvement."
  },
  {
    "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "Prior work on test-time compute scaling showed conflicting results — some approaches helped on reasoning while others showed limited gains — but nobody had systematically analyzed WHY. The authors identified the gap by observing that no prior work studied the scaling behaviors of different inference methods as a function of problem difficulty. This led them to ask: given a fixed compute budget at test time, what is the optimal way to spend it, and does the answer change depending on the problem?",
    "key_insight": "The effectiveness of test-time compute strategies is fundamentally difficulty-dependent: easy problems benefit from sequential refinement (local search), hard problems need parallel sampling (global search), and beam search can actually hurt on easy problems by exploiting verifier errors. This means a single uniform strategy wastes compute — an adaptive, difficulty-aware allocation achieves 4x efficiency gains by selecting the right strategy per problem.",
    "innovation_type": "analysis",
    "method_summary": "The paper frames all test-time compute through a unified proposer-verifier abstraction (analogous to MCMC with a proposal distribution and score function), then systematically studies two scaling mechanisms: (1) search against process reward models (PRMs) — comparing best-of-N weighted sampling, beam search, and lookahead search — where PRMs are trained via Monte Carlo rollouts rather than expensive human labels; and (2) iterative self-revision, where a model is fine-tuned to condition on its own prior (incorrect) attempts and improve upon them. The key methodological contribution is the compute-optimal strategy: bin problems by difficulty (estimated via averaged verifier scores at deployment), then independently select the best hyperparameters (search method, beam width, sequential-vs-parallel ratio) for each difficulty bin. This is validated against a FLOPs-matched comparison showing when test-time compute beats scaling model size by 14x.",
    "what_makes_it_good": "The paper succeeds because it transforms a vague intuition ('more inference compute helps') into a rigorous, quantitative framework with actionable engineering guidance. Reviewers praised the unified proposer-verifier framing, the thoroughness of ablations across difficulty levels, and the provocative FLOPs-matched comparison against larger models. The paper is also strategically well-timed — it provides the foundational analysis that the entire field of 'reasoning models' (o1, etc.) would need, making it instantly high-impact.",
    "limitations_acknowledged": "All experiments are on a single dataset (MATH) with a single model family (PaLM 2-S*), and the authors candidly state that on the hardest problems 'no method makes much meaningful progress,' limiting the generality of the test-time-beats-pretraining claim. Estimating question difficulty via 2048 samples is prohibitively expensive for deployment, creating an exploration-exploitation tradeoff the paper leaves unresolved.",
    "open_questions": [
      "Does the difficulty-dependent compute-optimal strategy generalize beyond math to other reasoning domains (code, science, planning), and does the optimal strategy surface change with different base model architectures and sizes?",
      "Can search (PRMs) and revision be combined synergistically — e.g., tree search over revision trajectories — and would this unlock gains on the hardest problems where both individually fail?",
      "How can difficulty estimation be made cheap enough for real-time deployment — can a lightweight classifier or the model's own uncertainty replace the expensive sampling-based oracle?"
    ],
    "building_blocks": [
      "Process Reward Models (PRMs) trained via Monte Carlo rollouts (no human labels needed)",
      "Best-of-N weighted sampling with per-step PRM score aggregation",
      "Beam search and lookahead search over solution steps",
      "Self-revision fine-tuning using edit-distance-correlated incorrect trajectories",
      "Difficulty binning as a sufficient statistic for strategy selection",
      "FLOPs-matched evaluation framework comparing inference vs. pretraining compute",
      "MATH benchmark (12k train / 500 test)",
      "Outcome Reward Models (ORMs) for revision selection"
    ],
    "reviewer_feedback_summary": "Three reviewers gave 8/10 (Accept) and one gave 6/10 (Marginally Above). Key praise: unified proposer-verifier framing, comprehensive experiments with strong ablations, significant practical implications, and insightful difficulty-dependent analysis. Key concerns: (1) all experiments on MATH only — generalizability is the #1 unresolved issue; (2) whether verifier training compute should count in the inference budget (fairness of comparison); (3) the 'compute-optimal' strategy is more proof-of-concept than deployable due to difficulty estimation cost; (4) fine-tuning alternatives not compared against pretraining scaling. Authors addressed concerns effectively — added verifier cost analysis, showed robustness to 20% noise-corrupted verifiers (91.4% accuracy on MATH-500), moved key figures from appendix to main paper, and cited follow-up reproductions on LLaMA/Qwen validating generalizability. The meta-reviewer noted strong author engagement but flagged generalizability and verifier dependency as persistent caveats.",
    "relevance_to_seed": "This paper is directly foundational to synthetic data and self-improvement for math reasoning: the PRM training pipeline generates synthetic step-level labels via Monte Carlo rollouts (no human annotation), and the revision model is explicitly a self-improvement loop where the model learns from its own mistakes. The compute-optimal framework teaches us that self-improvement strategies must be difficulty-aware — blindly applying one synthetic data generation or self-refinement strategy across all problems wastes compute and can even hurt performance, a critical design lesson for any self-improvement training pipeline."
  },
  {
    "title": "OpenThoughts: Data Recipes for Reasoning Models",
    "venue": "ICLR 2026 (Oral)",
    "problem_identification": "The authors identified that while frontier reasoning models (DeepSeek-R1, o3) achieve strong results via SFT on curated reasoning data, the complete training recipes are proprietary and unexplored publicly. Prior open-source attempts made ad hoc design choices without systematic ablation, so nobody knew WHICH pipeline decisions actually matter. The gap was visible in the scatter: many projects tried to reproduce reasoning distillation but couldn't match proprietary quality, and nobody had done controlled experiments isolating each pipeline stage to understand causal contributions.",
    "key_insight": "Decompose the data generation pipeline into 6 modular, independently testable stages (source → mix → filter questions → dedup/sample → filter answers → teacher selection) and run controlled ablations at each stage. This revealed several counterintuitive findings that challenge conventional wisdom: weaker teacher models produce better training data than stronger ones, answer verification/filtering provides zero benefit over using all samples, source quality dominates diversity (2 good sources beat 16 mixed ones), and the cheapest scaling axis is sampling multiple answers per question rather than collecting more questions.",
    "innovation_type": "analysis",
    "method_summary": "The authors constructed a 6-stage data generation pipeline for reasoning model training: (1) question sourcing from 62 diverse strategies (synthetic, semi-synthetic, non-synthetic) across math/code/science, (2) mixing top sources, (3) LLM-based question filtering (difficulty or response-length proxies), (4) deduplication with multiple answer sampling (up to 16× per question), (5) answer verification/filtering, and (6) teacher model selection. Each stage was ablated independently with all other stages held constant, using 31,600 datapoints per experiment across 8 benchmarks. The log-scale midpoint (31.6K) was chosen to balance signal and compute. Winning strategies from each stage were composed and scaled to 1.2M examples (OpenThoughts3), then used to SFT Qwen-2.5-7B into OpenThinker3-7B. Critically, the authors maintained held-out benchmarks (AIME 2025, HMMT, Humanity's Last Exam) never seen during pipeline development, ensuring true generalization measurement.",
    "what_makes_it_good": "Three things elevated this paper beyond a technical report: (1) the counterintuitive findings — weaker teachers outperforming stronger ones, answer filtering being useless, quality trumping diversity — are genuinely surprising and challenge widely held assumptions, giving the paper intellectual teeth; (2) the experimental rigor of 1000+ controlled ablations with held-out evaluation creates a level of causal credibility rare in empirical ML; (3) the open-source artifact (dataset + models + code) combined with SOTA results (15-20 point improvements on AIME/GPQA at 7B scale) made it immediately useful, generating community adoption that validated the contribution beyond benchmarks.",
    "limitations_acknowledged": "The authors explicitly note they only explored SFT and did not investigate reinforcement learning, staged SFT, or curriculum learning, which are standard components of full reasoning model training. They also acknowledge optimizing for average cross-domain performance rather than per-domain optimization, and leave open the question of what happens as student performance approaches teacher capability.",
    "open_questions": [
      "Why do weaker teacher models produce better training data? The authors hypothesize verbosity matters (QwQ-32B produces longer, more detailed traces than DeepSeek-R1), but the causal mechanism is unexplored — is it about reasoning granularity, error-correction patterns, or something about the capacity gap between teacher and student?",
      "How do these findings change under RL training? The entire ablation study is SFT-only, yet frontier reasoning models use RL extensively. The optimal data recipe for RL reward signals may differ substantially from SFT recipes.",
      "What is the scaling ceiling? Student performance plateaus as it approaches teacher capability — the 10-point gap between OpenThinker3-7B and QwQ-32B is unexplained. Can self-improvement or iterative distillation break through this ceiling without a stronger teacher?"
    ],
    "building_blocks": [
      "QwQ-32B as teacher model for distillation",
      "Response-length-based question filtering (proxy for difficulty)",
      "16× multiple answer sampling per question for scaling",
      "Exact deduplication over fuzzy/no dedup",
      "LlamaFactory + DeepSpeed v3 training framework",
      "CodeGolf + OpenCodeReasoning (code sources)",
      "OpenMath-2-Math (math source)",
      "StackExchange-Physics + OrganicChemistry-PDFs (science sources)",
      "Cosine LR schedule with 0.1 warmup ratio",
      "Log-scale midpoint experiment sizing (31.6K) for ablation efficiency",
      "Held-out benchmark methodology for pipeline development"
    ],
    "reviewer_feedback_summary": "Scores: 6, 6, 6, 8 (accepted as Oral despite three 6s, suggesting AC/meta-reviewer strongly valued the contribution). PRAISE: All reviewers acknowledged exceptional experimental rigor, practical value of open-source artifacts, and importance of the problem. Reviewer 4 (score 8) specifically praised counterintuitive findings and data decontamination. CONCERNS: Three major critiques recurred — (1) feels like a technical report with limited conceptual novelty (Reviewer 2), (2) lacks deeper causal explanations for WHY things work, especially the weaker-teacher paradox (Reviewers 1, 3), and (3) unfair experimental comparisons in answer filtering (baseline trained on 63.2K vs filtered 31.6K). AUTHORS ADDRESSED: They showed compute-controlled random filtering baselines (Tables 43-45), reframed gains as 30-point over base and 8-point over SFT baselines, and offered the verbose-teacher hypothesis with token-count analysis (Section E.2). The meta-reviewer found the rebuttals convincing, noting the rebuttal 'successfully addressed methodological concerns.'",
    "relevance_to_seed": "This paper is directly at the core of our research area — it IS the systematic investigation of synthetic data pipelines for mathematical reasoning training. Its most actionable lessons for us: (1) invest in question quality over question diversity, (2) scale through answer sampling rather than question collection, (3) use response-length as a cheap proxy for question difficulty filtering, (4) don't waste effort on answer verification — and most provocatively, (5) consider using moderately-capable verbose teachers over frontier models for distillation, as the reasoning trace quality matters more than the teacher's benchmark scores."
  },
  {
    "title": "DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving",
    "venue": "NeurIPS 2024",
    "problem_identification": "The authors performed a diagnostic analysis of existing rejection-tuned synthetic math datasets (e.g., MetaMathQA) and discovered a severe, previously unnoticed bias: vanilla rejection sampling applies equal trial budgets per query, but since harder queries have much lower success rates, the resulting datasets are dominated by easy examples — 51.1% of the hardest MATH training queries received zero correct responses, and Level-5 problems comprised only 10.5% of the final data despite being dominant in the original distribution. This was found through a straightforward but overlooked empirical analysis of dataset difficulty distributions.",
    "key_insight": "The distribution of difficulty in synthetic training data matters as much as the volume — by simply reallocating sampling budget to give harder problems more trials (rather than improving the generator model or augmenting queries), you can create smaller but substantially more effective training datasets. The insight is that the bottleneck isn't model capability but sampling allocation policy.",
    "innovation_type": "new_formulation",
    "method_summary": "DART reframes rejection tuning as a resource allocation problem over query difficulty. First, difficulty is measured via 'fail rate' — the proportion of incorrect responses when sampling n_d responses per query from DeepSeekMath-7B-RL. Two allocation strategies are proposed: DARS-Uniform collects a fixed k_u=40 correct responses per query regardless of difficulty (equalizing representation), and DARS-Prop2Diff allocates correct responses proportionally to difficulty score with the hardest queries receiving k_p=192 responses (deliberately over-representing hard problems). Both impose a max raw sample cap n_max per query. Synthesis uses DeepSeekMath-7B-RL at temperature 1.6 with top-p=0.95, generating ~150M raw samples over 160 A100 GPU-days. The resulting datasets (~585-591k samples) are used for standard supervised fine-tuning with cosine scheduling.",
    "what_makes_it_good": "This paper succeeds because the core contribution is both simple and surprisingly effective — it reframes an overlooked data distribution problem rather than proposing complex new architectures. The empirical gains are large and robust: +6.9 points on MATH for Llama3-8B over vanilla rejection tuning, while using only a 7B open-weight synthesizer (no GPT-4 dependency). The thorough experimental design — 6 benchmarks including 4 out-of-domain, multiple base models from 7B to 70B, detailed ablations on scaling behavior and coverage effects — demonstrates the kind of comprehensive evaluation that builds reviewer confidence.",
    "limitations_acknowledged": "The authors acknowledge that fail rate may be suboptimal as a difficulty metric (alternatives like Elo ratings or learned difficulty scores remain unexplored), and that DART-Math is limited to natural language chain-of-thought reasoning without code execution, which is known to significantly boost math performance. They also note gains diminish for math-specialized models like DeepSeekMath.",
    "open_questions": [
      "What is the optimal difficulty distribution for training data — is linear proportionality to difficulty truly best, or would a learned curriculum (e.g., starting easy, gradually increasing difficulty) outperform static over-representation of hard examples?",
      "How does difficulty-aware sampling interact with query augmentation techniques (e.g., rephrasing, decomposition)? The paper fixes the query set but combining DART with synthetic query generation could compound gains.",
      "Can difficulty-aware allocation be made adaptive during training rather than fixed at data creation time — e.g., dynamically reweighting or resampling based on the student model's evolving competence (online difficulty-aware curriculum learning)?"
    ],
    "building_blocks": [
      "Rejection sampling / rejection tuning pipeline for synthetic data",
      "Fail rate as a lightweight difficulty metric (proportion of incorrect samples from a reference model)",
      "DeepSeekMath-7B-RL as an open-weight synthesis model",
      "MATH and GSM8K training sets as query sources",
      "Temperature scaling (t=1.6) for diversity in sampling",
      "DARS-Uniform and DARS-Prop2Diff allocation strategies",
      "Answer-matching verification for filtering correct responses",
      "Comprehensive OOD evaluation suite: CollegeMath, TheoremQA, OlympiadBench, DeepMind-Mathematics"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is directly central to our research area — it demonstrates that the data curation policy (how you allocate synthesis compute across problems of varying difficulty) is a powerful and underexplored lever for self-improvement in mathematical reasoning. The key lesson for our work is that naive rejection sampling wastes most compute on already-easy problems; any synthetic data pipeline we build should incorporate difficulty-aware allocation as a baseline, and we should investigate whether more sophisticated adaptive or curriculum-based allocation strategies can push beyond DART's static proportional approach."
  },
  {
    "title": "RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold",
    "venue": "NeurIPS 2024",
    "problem_identification": "The authors identified that training on model-generated positive synthetic data amplifies spurious correlations in intermediate reasoning steps — steps that happen to co-occur with correct final answers but are causally misleading. They found this by going beyond final-answer accuracy and examining *why* RFT scaling plateaus: positive traces contain incorrect intermediate steps undetectable by outcome-based verification (error ~ D^-0.05 on MATH), and fitting more of such data reinforces these spurious patterns rather than improving generalization. This is a gap others missed because most prior work evaluated synthetic data quality only by final-answer correctness, never dissecting step-level fidelity.",
    "key_insight": "Incorrect model-generated solutions are not waste — they are the most informative training signal, because per-step credit assignment on negative traces reveals exactly which reasoning steps cause failure. Formally, DPO on per-step positive/negative pairs is equivalent to advantage-weighted RL, which automatically down-weights spurious steps and up-weights causally critical ones, thereby 'unlearning' the spurious correlations that positive-only training amplifies.",
    "innovation_type": "new_formulation",
 
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
  "promptId": "bd281c73-61f2-4c2b-a6f1-b958854cf6e4",
  "type": "user",
  "uuid": "40d1fbb0-49b8-481d-b6e5-db4eaaa12958",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:21:03.640Z_

```json
{
  "parentUuid": "40d1fbb0-49b8-481d-b6e5-db4eaaa12958",
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
  "uuid": "434fe485-db46-4940-bce2-db08d2405521",
  "timestamp": "2026-05-28T05:21:03.640Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:21:03.640Z_

```json
{
  "parentUuid": "434fe485-db46-4940-bce2-db08d2405521",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f9f513ec-e25e-447d-8f62-fa1827df8744",
  "timestamp": "2026-05-28T05:21:03.640Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Synthetic Data and Self-Improvement…",
  "leafUuid": "f9f513ec-e25e-447d-8f62-fa1827df8744",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize math reasoning training literature into field guide",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38"
}
```

---

### Assistant

_source line 8 · 2026-05-28T05:21:28.495Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 19 paper analyses into a strategic "Field Guide" for research in Synthetic Data and Self-Improvement for Mathematical Reasoning Training. However, the paper analyses were truncated at paper 7. Let me work with what I have (7 detailed papers) and synthesize the patterns I can identify.

Let me carefully analyze the papers provided:

1. **DeepSeek-R1** - RL without SFT, GRPO, emergent reasoning, rejection sampling for synthetic data
2. **DeepSeekMath** - GRPO algorithm, web-scale data curation, unified RL framework


3. **rStar-Math** - MCTS + code verification, Process Preference Model, self-evolution loop
4. **Scaling Test-Time Compute** - Difficulty-dependent strategies, PRM training, compute-optimal allocation
5. **OpenThoughts** - Systematic data recipe ablation, counterintuitive findings (weaker teachers, no answer filtering)
6. **DART-Math** - Difficulty-aware rejection tuning, sampling allocation policy
7. **RL on Incorrect Synthetic Data** - Using negative traces, per-step DPO, 8x efficiency

I only have 7 papers instead of the full 19, so I'll need to work with this subset to identify the core strategic themes and patterns that emerge across these approaches.

Looking at the innovation patterns across these papers, I'm seeing several key strategies: simplification through removing unnecessary components, reframing problems in new ways like treating resource allocation or negative examples as opportunities, systematic ablation studies that reveal surprising insights, self-improvement mechanisms where models iteratively enhance themselves, and novel combinations of existing techniques. Let me structure these insights into a coherent framework.

Now I'm identifying what reviewers consistently value—counterintuitive findings backed by rigorous evidence, thorough ablations that isolate each component's contribution, open-source releases of models and code, honest reporting of failures, elegant methods that achieve outsized gains, and pipelines that others can actually reproduce. There are also clear gaps in the field: most work focuses on verifiable domains like math, we lack good ways to estimate difficulty at deployment time, the mechanism behind why weaker teachers generate better training data remains unclear, and we don't understand when self-improvement hits a ceiling. Visual reasoning and geometry are largely unexplored, and the optimal recipe for combining RL with SFT is still an open question.

I'm also noticing several untried combinations that could be promising: merging DART-Math's difficulty-aware allocation with rStar-Math's self-evolution approach, applying OpenThoughts' recipe optimization to RL training rather than just SFT, using per-step DPO on negative traces while guided by MCTS-generated data, and exploring how difficulty-dependent strategies could improve test-time performance.

The core building blocks I'm considering are GRPO for training, code-augmented chain-of-thought verification, process preference models, difficulty-aware sampling, response-length filtering, rejection sampling from RL checkpoints, and MCTS for decomposing reasoning. I'm also tracking common pitfalls: training exclusively on positive synthetic data amplifies spurious patterns, uniform sampling across difficulty levels wastes budget, answer filtering doesn't help despite what some papers suggest, chasing diversity at the expense of quality, relying on neural reward models that get hacked, and only measuring final-answer accuracy instead of intermediate steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9f513ec-e25e-447d-8f62-fa1827df8744",
  "isSidechain": false,
  "requestId": "req_011CbUQSmSfqgip8qgY3tTux",
  "type": "assistant",
  "uuid": "ad12975c-529f-4227-8f83-45dd64a4c85a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcLEdVADgdwy5xaRasJ9Lb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11130,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8788,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 11130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11130
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

_source line 9 · 2026-05-28T05:24:32.128Z_

Looking at the paper analyses, I need to carefully synthesize the patterns across all provided papers. Let me first read through the full set of analyses since the input was truncated, then build the field guide.

Given that the analyses were truncated after ~7 papers, let me work with the rich detail available in those 7 papers (DeepSeek-R1, DeepSeekMath, rStar-Math, Scaling Test-Time Compute, OpenThoughts, DART-Math, and RL on Incorrect Synthetic Data) to produce the most evidence-grounded synthesis possible.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Simplification by Component Removal",
      "description": "Identify an expensive or complex component widely assumed to be necessary (critic model, SFT stage, human annotations, neural reward models) and show empirically that removing it either maintains or improves performance. The key is pairing the removal with a clean theoretical or empirical explanation of WHY the component was unnecessary. This pattern is highly rewarded because it reduces cost, increases reproducibility, and challenges assumptions simultaneously.",
      "examples": ["DeepSeek-R1 (removes SFT stage, shows pure RL suffices)", "DeepSeekMath (removes critic model from PPO via GRPO, cutting 50% memory)", "OpenThoughts (removes answer verification/filtering, shows zero benefit)"],
      "success_rate": "high"
    },
    {
      "pattern": "Reframing the Problem Formulation",
      "description": "Take an existing pipeline component that everyone treats as fixed (e.g., 'rejection sampling is just filtering for correct answers') and reframe it as an optimization problem over a new variable (difficulty allocation, negative-trace credit assignment). The reframing itself is the contribution — it opens a new design space where simple strategies yield large gains. Works best when accompanied by a diagnostic analysis showing the hidden inefficiency in the current formulation.",
      "examples": ["DART-Math (reframes rejection tuning as a resource allocation problem over difficulty)", "RL on Incorrect Synthetic Data (reframes negative traces from waste to primary training signal)", "Scaling Test-Time Compute (reframes inference compute as difficulty-dependent strategy selection)"],
      "success_rate": "high"
    },
    {
      "pattern": "Systematic Ablation Revealing Counterintuitive Findings",
      "description": "Instead of proposing a new method, systematically ablate an existing pipeline's design choices with controlled experiments and discover that widely held assumptions are wrong. The paper's contribution is the finding, not the method. This pattern works because the community is starved for causal understanding of why things work. Requires 100+ controlled experiments and held-out evaluation to be credible.",
      "examples": ["OpenThoughts (weaker teachers > stronger teachers, answer filtering is useless, quality > diversity)", "Scaling Test-Time Compute (beam search hurts on easy problems, difficulty-dependent strategies beat uniform)"],
      "success_rate": "high"
    },
    {
      "pattern": "Self-Improvement Loop with Co-Evolving Components",
      "description": "Design a system where two or more components (typically policy model + reward/verification model) iteratively improve each other across multiple rounds. The policy generates better data for the reward model, which guides the policy to generate even better data. Critical success factor: each round must show measurable, ablatable gains, and the loop must break the capability ceiling of one-shot distillation.",
      "examples": ["rStar-Math (policy SLM and PPM co-evolve over 4 rounds, each improving the other)", "DeepSeek-R1 (RL checkpoint → rejection sampling → SFT → RL cycle)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Verification-Grounded Synthesis",
      "description": "Pair each reasoning step in synthetic data generation with an executable verification mechanism (code execution, formal proof checking, symbolic computation) to guarantee step-level correctness, bypassing the fundamental problem that outcome-correct traces can contain intermediate errors. The verification creates a quality floor that scales with compute rather than degrading.",
      "examples": ["rStar-Math (each NL reasoning step paired with executable Python verification)", "RL on Incorrect Synthetic Data (per-step credit assignment via DPO on verified step pairs)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Unified Framework Then Novel Instantiation",
      "description": "Present a theoretical framework that subsumes multiple existing methods as special cases (showing SFT, RFT, DPO, PPO as points in one design space), then propose a new point in that space justified by the framework. The framework provides intellectual credibility and the new method provides practical contribution. Particularly effective when the framework reveals that the new method occupies an obviously-good-but-unexplored region of the design space.",
      "examples": ["DeepSeekMath (unified paradigm framework in Table 10, GRPO as the natural 'missing' method)", "Scaling Test-Time Compute (proposer-verifier abstraction unifying all test-time strategies)"],
      "success_rate": "high"
    }
  ],
  "reviewer_preferences": [
    "Counterintuitive empirical findings backed by rigorous controlled experiments are the single highest-signal quality indicator. OpenThoughts got Oral at ICLR 2026 despite three 6/10 scores because the counterintuitive findings (weaker teachers beat stronger ones, answer filtering is useless) were so well-ablated that the meta-reviewer overrode moderate scores. Scaling Test-Time Compute similarly got Oral for revealing that beam search hurts on easy problems.",
    "Comprehensive ablations that isolate each component's causal contribution, not just aggregate results. rStar-Math reviewers (4-5/5) specifically praised 'systematic ablations isolating each component's contribution' — the code-augmented CoT vs rejection sampling (+5%) and PPM vs ORM (+6.8%) ablations were individually citable. Papers without per-component ablations face credibility challenges.",
    "Open-source artifacts (model weights, datasets, full training code) dramatically increase perceived impact. DeepSeek-R1 earned >1000 citations within months partly because it open-sourced weights at a time when frontier reasoning models were closed. OpenThoughts' dataset + models were immediately adopted by the community, validating contribution beyond benchmarks.",
    "Honest reporting of negative results and limitations signals intellectual integrity and provides genuine scientific value. DeepSeekMath's finding that arXiv pre-training provides zero math benefit, and DeepSeek-R1's admission that PRM and MCTS both failed, were praised rather than penalized. Papers hiding failures appear cherry-picked.",
    "FLOPs-controlled or compute-normalized comparisons rather than just accuracy tables. Scaling Test-Time Compute and DART-Math both gained credibility by showing gains hold under fair compute budgets. Reviewers increasingly flag unfair comparisons (e.g., OpenThoughts reviewer flagged 63.2K vs 31.6K baseline mismatch).",
    "Out-of-domain evaluation on held-out benchmarks not used during pipeline development. OpenThoughts maintained AIME 2025, HMMT, and Humanity's Last Exam as held-out; rStar-Math evaluated on GaoKao; DART-Math tested on CollegeMath, TheoremQA, OlympiadBench. Papers evaluating only on in-distribution benchmarks face 'overfitting to the benchmark' concerns.",
    "Simple methods that deliver large gains over complex alternatives. Reviewers reward elegance — DART-Math's core contribution is just reallocating sampling budget, yet it outperforms methods with architectural innovations. GRPO is implementable in 50 lines. Complexity without corresponding gains is penalized."
  ],
  "field_gaps": [
    {
      "gap": "Extending RL-based self-improvement beyond domains with clean verifiable rewards (creative writing, open-ended reasoning, scientific hypothesis generation)",
      "evidence": "DeepSeek-R1 explicitly identifies this as THE fundamental bottleneck — 'pure RL success is entirely predicated on having a reliable verifier.' rStar-Math acknowledges dependence on 'domains with verifiable correctness criteria.' Scaling Test-Time Compute's PRM approach also requires ground-truth labels.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Understanding WHY weaker/verbose teacher models produce better training data than stronger ones for distillation",
      "evidence": "OpenThoughts discovered this empirically (QwQ-32B > DeepSeek-R1 as teacher) and hypothesized verbosity matters, but reviewers flagged the lack of causal explanation as a primary weakness. The paper offers token-count analysis (Section E.2) but no mechanistic understanding. This is exploitable — the causal mechanism could unlock principled teacher selection.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Optimal SFT data recipes for RL — all systematic data ablation has been SFT-only",
      "evidence": "OpenThoughts explicitly acknowledges: 'we only explored SFT and did not investigate reinforcement learning.' DeepSeekMath shows RL improves Maj@K but not Pass@1, suggesting RL reshapes distributions rather than expanding capabilities. The interaction between data curation choices and downstream RL optimization is entirely unexplored in a controlled setting.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Self-improvement ceiling: when and why do iterative self-improvement loops saturate, and how to break through",
      "evidence": "rStar-Math's self-evolution went 4 rounds (60% → 90% coverage) but leaves open whether rounds 5-10 would help. OpenThoughts notes a persistent 10-point gap between student and teacher. DeepSeek-R1's distillation outperforms RL on small models, suggesting a capability floor for self-discovery. No paper has characterized the theoretical or empirical ceiling of self-improvement loops.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Adaptive difficulty-aware curriculum during training (not just at data creation time)",
      "evidence": "DART-Math uses static difficulty-proportional allocation at data creation. Scaling Test-Time Compute shows strategy should be difficulty-dependent. But no paper implements online difficulty-aware curriculum learning where the training data distribution adapts to the student model's evolving competence during training.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Cheap difficulty estimation for deployment and data curation",
      "evidence": "Scaling Test-Time Compute estimates difficulty via 2048 samples — 'prohibitively expensive for deployment.' DART-Math uses fail rate requiring n_d samples per query. OpenThoughts uses response-length as a cheap proxy. No paper has systematically compared difficulty estimators on cost-accuracy tradeoffs or developed a learned lightweight difficulty classifier.",
      "difficulty": "low",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Combining search (MCTS/beam search) with self-revision in a unified framework",
      "evidence": "Scaling Test-Time Compute explicitly asks: 'Can search (PRMs) and revision be combined synergistically — e.g., tree search over revision trajectories — and would this unlock gains on the hardest problems where both individually fail?' This was posed as an open question in an ICLR Oral and remains unanswered.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Process reward model collapse and reward hacking in multi-round self-improvement",
      "evidence": "rStar-Math's PPM is trained on MCTS Q-values that depend on the PPM in later rounds — the paper's own open question asks whether 'this circular dependency could lead to reward model collapse or systematic biases.' DeepSeek-R1 deliberately avoided neural reward models due to reward hacking at scale. No paper has characterized the failure modes of co-evolving policy-reward systems.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Geometry, visual reasoning, and multimodal mathematical problem-solving",
      "evidence": "rStar-Math notes 8 of their unsolved AIME problems were geometry-based and acknowledges 'inability to handle geometry problems requiring visual understanding.' DeepSeekMath notes weakness on geometry and formal theorem proving. This is a consistent blind spot across the field.",
      "difficulty": "high",
      "impact_if_solved": "medium"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "Difficulty-aware self-evolution: Combine DART-Math's difficulty-proportional sampling allocation with rStar-Math's iterative self-improvement loop, where each round adaptively reallocates MCTS compute budget based on the evolving policy model's per-difficulty-bin performance — spend more rollouts on problems the current model finds hard, not problems that were hard for the initial model.",
      "from_papers": ["DART-Math", "rStar-Math", "Scaling Test-Time Compute"],
      "why_promising": "DART-Math showed 6.9-point gains from static difficulty-aware allocation. rStar-Math showed each self-evolution round yields measurable gains. But rStar-Math uses uniform compute allocation across problems, and DART-Math's allocation is static. Adaptive allocation within a self-improvement loop should compound both effects — as the model improves, the difficulty frontier shifts, and compute should follow. The Scaling Test-Time Compute finding that strategy should be difficulty-dependent provides theoretical support."
    },
    {
      "idea_sketch": "Negative-trace-guided MCTS: Use RL on Incorrect Synthetic Data's per-step credit assignment on negative traces to improve rStar-Math's MCTS search policy — instead of uniform UCT exploration, bias tree expansion away from step patterns identified as causally responsible for failures in previous rounds.",
      "from_papers": ["RL on Incorrect Synthetic Data", "rStar-Math"],
      "why_promising": "rStar-Math discards incorrect MCTS trajectories after using them for Q-value estimation. RL on Incorrect Synthetic Data showed these negative traces contain the most informative training signal. Combining them means the MCTS search learns not just 'what works' but explicitly 'what to avoid,' potentially reducing the 64-128 rollouts needed per problem and making the self-evolution loop more compute-efficient."
    },
    {
      "idea_sketch": "OpenThoughts data recipes optimized for RL rather than SFT: Replicate OpenThoughts' 6-stage ablation methodology but evaluate each stage's impact on downstream RL training (GRPO) rather than SFT — testing whether the optimal data recipe changes when the data is used to initialize an RL policy vs. used as the final training signal.",
      "from_papers": ["OpenThoughts", "DeepSeekMath", "DeepSeek-R1"],
      "why_promising": "OpenThoughts' entire 1000+ ablation study is SFT-only, and they explicitly flag RL as unexplored. DeepSeek-R1 showed the cold-start SFT data crucially affects RL outcomes. DeepSeekMath showed RL reshapes distributions differently than SFT. The optimal teacher model, filtering strategy, and difficulty distribution for RL initialization likely differ from SFT — e.g., answer filtering might matter for RL even though it's useless for SFT, because RL needs a stronger initial policy to explore from."
    },
    {
      "idea_sketch": "Process Preference Models trained on code-verified step pairs + self-revision: Combine rStar-Math's code-augmented step verification with Scaling Test-Time Compute's self-revision approach — train a model to revise specific incorrect steps (identified by code execution failure) rather than regenerating entire solutions, using PPM scores to select which steps to revise first.",
      "from_papers": ["rStar-Math", "Scaling Test-Time Compute"],
      "why_promising": "Scaling Test-Time Compute shows revision works for easy-medium problems but fails on hard ones. rStar-Math's code verification can pinpoint exactly which step failed. Current revision approaches regenerate from scratch; targeted step revision guided by a PPM could be far more compute-efficient and could work on harder problems where full regeneration repeatedly fails at the same bottleneck step."
    },
    {
      "idea_sketch": "GRPO with difficulty-stratified group formation: Instead of GRPO's standard uniform sampling of G outputs per question, form groups stratified by difficulty — sample more outputs for harder questions (DART-Math's allocation) and compute group-relative advantages within difficulty-matched batches (Scaling Test-Time Compute's difficulty binning) to prevent easy-question gradients from dominating updates.",
      "from_papers": ["DeepSeekMath", "DART-Math", "Scaling Test-Time Compute"],
      "why_promising": "GRPO uses G=64 uniform samples per question, but DART-Math proved uniform allocation is severely suboptimal. In GRPO, easy questions where most samples are correct produce near-zero advantages (low signal), while hard questions where all samples fail also produce near-zero advantages (no positive examples). Difficulty-aware group sizes could ensure both easy and hard questions contribute meaningful gradient signal, directly addressing DeepSeekMath's observation that RL improves Maj@K but not Pass@1."
    },
    {
      "idea_sketch": "Weak-teacher ensemble distillation with trace-level selection: Instead of using one teacher model (OpenThoughts found QwQ-32B beats DeepSeek-R1), generate traces from multiple teachers of varying capability and select the best trace per problem per step using rStar-Math's PPM — leveraging the finding that different teachers may excel at different problem types or reasoning styles.",
      "from_papers": ["OpenThoughts", "rStar-Math"],
      "why_promising": "OpenThoughts discovered the counterintuitive weak-teacher advantage but only tested single teachers. The advantage likely varies by problem type — a weaker verbose teacher may be better for step-by-step arithmetic while a stronger concise teacher may be better for high-level strategy. Per-problem or per-step teacher selection using a PPM could capture the best of both worlds without requiring a single universally-superior teacher."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "GRPO (Group Relative Policy Optimization)",
      "what_it_does": "Critic-free RL algorithm that samples G outputs per question, computes advantages as z-score-normalized rewards within the group, and optimizes a clipped surrogate objective with KL penalty. Cuts ~50% memory vs PPO by eliminating the value/critic network.",
      "used_by": ["DeepSeek-R1", "DeepSeekMath"],
      "could_be_applied_to": "Difficulty-stratified GRPO where group size varies by problem difficulty, or GRPO with process-level rewards (per-step group-relative advantages) rather than outcome-only rewards"
    },
    {
      "tool": "Code-Augmented Chain-of-Thought Verification",
      "what_it_does": "Pairs each natural language reasoning step with executable Python code — only steps whose code runs successfully and produces consistent results are kept. Provides step-level correctness guarantees without human annotation.",
      "used_by": ["rStar-Math"],
      "could_be_applied_to": "Filtering training data in any synthetic CoT pipeline (OpenThoughts, DART-Math) at the step level rather than outcome level; generating verified step-level preference pairs for DPO training"
    },
    {
      "tool": "Process Preference Model (PPM) via Bradley-Terry on MCTS Q-values",
      "what_it_does": "Converts noisy Q-value estimates from MCTS rollouts into preference pairs (high-Q vs low-Q steps) and trains a process reward model via pairwise ranking loss, avoiding the instability of direct Q-value regression.",
      "used_by": ["rStar-Math"],
      "could_be_applied_to": "Training PRMs for Scaling Test-Time Compute's search framework without human labels; providing step-level reward signal for GRPO to enable process-level RL"
    },
    {
      "tool": "Difficulty-Aware Sampling Allocation (DARS)",
      "what_it_does": "Measures per-query difficulty via fail rate, then allocates rejection sampling budget proportionally to difficulty — harder problems get more sampling attempts, equalizing or over-representing difficult examples in the final dataset.",
      "used_by": ["DART-Math"],
      "could_be_applied_to": "Any synthetic data pipeline (OpenThoughts, rStar-Math self-evolution rounds); allocating MCTS rollout budgets per problem; allocating GRPO group sizes per question"
    },
    {
      "tool": "Response-Length-Based Question Filtering",
      "what_it_does": "Uses the length of a teacher model's response to a question as a cheap proxy for difficulty — longer responses indicate harder, more reasoning-intensive questions worth including in training data.",
      "used_by": ["OpenThoughts"],
      "could_be_applied_to": "Pre-filtering problems before expensive MCTS rollouts in rStar-Math; estimating difficulty for DART-Math's allocation without requiring multiple sample generations; routing problems to appropriate strategies in Scaling Test-Time Compute's framework"
    },
    {
      "tool": "Rejection Sampling from RL Checkpoints for SFT Data",
      "what_it_does": "Takes intermediate RL-trained model checkpoints, generates many solutions per problem, filters by correctness, and uses the resulting traces as high-quality SFT training data — creating a self-improvement loop where RL exploration generates synthetic supervised data.",
      "used_by": ["DeepSeek-R1"],
      "could_be_applied_to": "Generating SFT data for smaller student models from RL-trained teacher's exploration traces; creating curriculum data where earlier checkpoints produce easier examples and later checkpoints produce harder ones"
    },
    {
      "tool": "Per-Step Credit Assignment via DPO on Positive/Negative Trace Pairs",
      "what_it_does": "Aligns positive and negative solution traces at the step level, constructs preference pairs at each divergence point, and applies DPO — which is equivalent to advantage-weighted RL — to down-weight spurious steps and up-weight causally critical ones.",
      "used_by": ["RL on Incorrect Synthetic Data"],
      "could_be_applied_to": "Improving rStar-Math's PPM training signal; creating fine-grained reward signals for GRPO from paired correct/incorrect traces; debiasing any rejection-sampled dataset (DART-Math, OpenThoughts) at the step level"
    },
    {
      "tool": "Difficulty Binning for Strategy Selection",
      "what_it_does": "Bins problems by estimated difficulty (via averaged verifier scores), then independently selects optimal hyperparameters (search method, beam width, sequential-vs-parallel ratio) per difficulty bin — achieving 4x compute efficiency over uniform strategies.",
      "used_by": ["Scaling Test-Time Compute"],
      "could_be_applied_to": "Selecting between different synthetic data generation strategies per difficulty level (e.g., simple rejection sampling for easy problems, full MCTS for hard ones); routing problems in a self-improvement loop to appropriate compute tiers"
    },
    {
      "tool": "Multi-Round Self-Evolution with Policy-Reward Co-Training",
      "what_it_does": "Iteratively alternates between (1) using the current reward model to guide the policy's data generation via MCTS, and (2) using the policy's improved outputs to retrain the reward model — with each round producing measurably better data and models.",
      "used_by": ["rStar-Math"],
      "could_be_applied_to": "Any pipeline using both a generator and a verifier/reward model; could replace single-round rejection sampling in DART-Math or OpenThoughts with iterative refinement; could improve PRM quality in Scaling Test-Time Compute's framework"
    },
    {
      "tool": "Held-Out Benchmark Methodology for Pipeline Development",
      "what_it_does": "Maintains specific benchmarks (AIME 2025, HMMT, Humanity's Last Exam) that are never used during pipeline ablation or hyperparameter selection, only for final evaluation — preventing overfitting the pipeline to benchmark-specific patterns.",
      "used_by": ["OpenThoughts"],
      "could_be_applied_to": "Any research in this area — should be adopted as standard practice for all synthetic data and self-improvement papers to establish genuine generalization"
    }
  ],
  "common_pitfalls": [
    "Training exclusively on positive synthetic traces amplifies spurious step-level correlations. RL on Incorrect Synthetic Data demonstrated that positive-only training reinforces intermediate steps that co-occur with correct answers but are causally misleading (error ~ D^-0.05 on MATH). Any synthetic data pipeline that filters only for final-answer correctness inherits this bias. Always consider incorporating negative traces or step-level verification.",
    "Applying uniform compute/sampling budget across problems of varying difficulty. DART-Math showed vanilla rejection sampling wastes 51.1% of budget on hard problems that yield zero correct responses, while over-representing easy examples. This applies broadly: GRPO's uniform group size, MCTS's uniform rollout budget, and distillation's uniform sampling all suffer from this inefficiency.",
    "Investing in answer verification/filtering for SFT data. OpenThoughts' controlled ablation showed answer filtering provides zero benefit over using all samples — a finding many teams waste effort rediscovering. However, this was only tested for SFT; verification may matter for RL initialization or process reward model training, so context matters.",
    "Prioritizing data diversity over data quality. OpenThoughts found that 2 high-quality sources beat 16 mixed sources. The temptation to aggregate every available dataset is counterproductive — source quality dominates, and mixing in low-quality data dilutes training signal. Carefully curate few sources rather than aggregating many.",
    "Using neural reward models at scale without safeguards against reward hacking. DeepSeek-R1 deliberately avoided neural reward models and used only rule-based rewards, citing reward hacking at scale. rStar-Math mitigated this by using preference-based training and offline MCTS updates rather than online RL with a neural reward model. Naive neural reward models are a known failure mode.",
    "Evaluating synthetic data quality only by downstream task accuracy without examining step-level fidelity or difficulty distribution. RL on Incorrect Synthetic Data showed final-answer accuracy hides intermediate errors; DART-Math showed dataset difficulty distribution is a hidden confounder. Always diagnose the data itself, not just the model trained on it.",
    "Assuming stronger teacher models produce better distillation data. OpenThoughts' controlled experiment showed QwQ-32B (weaker, more verbose) outperformed DeepSeek-R1 (stronger, more concise) as a teacher. Always ablate teacher selection rather than defaulting to the strongest available model.",
    "Claiming 'no distillation' while using a large model for initialization. rStar-Math reviewers flagged the use of DeepSeek-Coder-V2-Instruct (236B) in Round 1 as potentially contradicting 'self-improvement without teacher' claims. Be precise about what components use external models and honestly characterize the degree of external dependence.",
    "Running all experiments at a single scale or on a single benchmark family. Scaling Test-Time Compute reviewers flagged MATH-only evaluation as the #1 concern. DeepSeekMath's arXiv-is-useless finding 'hasn't been tested at larger scales.' Include multiple scales, multiple benchmarks (especially OOD), and discuss which findings are scale-dependent.",
    "Presenting a complex system without ablating individual components. rStar-Math's highest reviewer praise was for isolating each component's contribution. OpenThoughts ran 1000+ controlled ablations. Papers presenting multi-stage pipelines as monolithic systems face credibility challenges — reviewers want to know which parts actually matter."
  ],
  "field_trajectory": "The field is converging on three macro-directions that will likely dominate 2026-2027 research. First, **closed-loop self-improvement systems** where the generator and verifier co-evolve without external supervision — rStar-Math demonstrated this for math via MCTS + PPM co-evolution, and DeepSeek-R1 showed RL alone can discover novel reasoning strategies. The next frontier is making these loops provably convergent and characterizing their ceilings. Expect papers that either extend self-improvement to new domains (code, science, formal proofs) or provide theoretical guarantees on when/why self-improvement saturates. Second, **compute-optimal data engineering** is emerging as a distinct research agenda — not just 'make more data' but 'allocate synthesis compute optimally across the difficulty spectrum.' DART-Math, Scaling Test-Time Compute, and OpenThoughts collectively establish that WHERE you spend compute (which problems, which strategies, which pipeline stages) matters more than HOW MUCH you spend. This will lead to adaptive, curriculum-based data generation pipelines that dynamically adjust to the student model's evolving capability. Third, **process-level supervision without human annotation** is the critical enabling technology — rStar-Math's code-verified steps, RL on Incorrect Synthetic Data's per-step credit assignment, and Scaling Test-Time Compute's Monte Carlo PRM training all attack the same problem from different angles. The eventual convergence point is likely a unified framework that provides dense, verified, step-level training signals at scale, which would unlock the next generation of reasoning models the way GRPO unlocked the current one. The field is also quietly moving away from the 'scale up the teacher' paradigm toward 'make the self-improvement loop smarter' — OpenThoughts' weak-teacher finding and rStar-Math's teacher-free later rounds both suggest that the community is beginning to value self-sufficiency over distillation.",
  "meta_advice": "If I were advising a PhD student targeting a strong 2026 venue paper in this area, here is what I would say. First, **pick a specific, well-defined bottleneck rather than building another end-to-end system.** The papers that got Orals (rStar-Math at ICML, OpenThoughts and Scaling Test-Time Compute at ICLR) succeeded not by being comprehensive but by deeply understanding one part of the pipeline — step-level verification, data recipes, or compute allocation. A paper that thoroughly ablates one understudied interaction (e.g., how data curation choices affect downstream RL, or when self-improvement loops collapse) will beat a paper that proposes a new 8-stage pipeline with marginal gains. Second, **invest 40% of your effort in diagnostic analysis and ablation, not just method development.** The highest-impact finding in OpenThoughts was 'answer filtering is useless' — a negative result from a controlled experiment. DeepSeekMath's 'arXiv doesn't help math' finding is still unexplained and citable two years later. Reviewers in this area are sophisticated enough to value understanding over performance. Third, **target the SFT-to-RL interface**, which is the largest unexplored gap. Every systematic data ablation (OpenThoughts, DART-Math) is SFT-only, and every RL paper (DeepSeek-R1, DeepSeekMath) uses ad hoc SFT initialization. A controlled study of how SFT data choices affect RL outcomes — which teacher, which difficulty distribution, which verification strategy produces the best RL starting point — would be immediately impactful because it connects the two most active sub-communities. Fourth, **always include compute-controlled baselines and out-of-domain evaluation.** Reviewers will challenge any comparison where your method uses more compute or evaluates only on in-distribution benchmarks. DART-Math's strength was showing gains hold under fair compute budgets; OpenThoughts' held-out benchmarks prevented overfitting claims. Fifth, **open-source everything** — in this specific sub-field, open artifacts (DeepSeek-R1 weights, OpenThoughts datasets, DART-Math data) generate adoption, citations, and goodwill with reviewers who explicitly praise reproducibility. A paper with SOTA results and closed data will be received worse than a paper with near-SOTA results and fully open artifacts. Finally, **the untried combinations in this field guide are genuinely open** — difficulty-aware GRPO, negative-trace-guided MCTS, RL-optimized data recipes — and any of these could yield a strong contribution because the component pieces are already validated. The risk is low and the ceiling is high."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad12975c-529f-4227-8f83-45dd64a4c85a",
  "isSidechain": false,
  "requestId": "req_011CbUQSmSfqgip8qgY3tTux",
  "type": "assistant",
  "uuid": "a38abdb8-64b0-436f-b8b5-d59b97c4561f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcLEdVADgdwy5xaRasJ9Lb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11130,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8788,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 11130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11130
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Synthetic Data and Self-Improvement…",
  "leafUuid": "a38abdb8-64b0-436f-b8b5-d59b97c4561f",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize math reasoning training literature into field guide",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Synthetic Data and Self-Improvement…",
  "leafUuid": "a38abdb8-64b0-436f-b8b5-d59b97c4561f",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize math reasoning training literature into field guide",
  "sessionId": "0cad6145-8f2c-45d1-84a8-a65b48703a38"
}
```

---
