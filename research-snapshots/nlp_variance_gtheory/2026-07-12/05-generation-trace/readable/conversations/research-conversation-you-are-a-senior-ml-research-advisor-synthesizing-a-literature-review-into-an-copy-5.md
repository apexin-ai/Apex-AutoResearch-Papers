# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa.jsonl`
- **Structured JSON:** [`24003c03a66bb670f271.json`](../../sessions/24/24003c03a66bb670f271.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T16:34:22.968Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T16:34:22.968Z",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Research area: Synthetic Data and Self-Improvement for Mathematical Reasoning Training\n\n## Paper analyses (21 papers)\n\n[\n  {\n    \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\",\n    \"venue\": \"Nature 645, 633–638 (2025); arXiv Jan 2025\",\n    \"problem_identification\": \"Prior reasoning improvements in LLMs (CoT prompting, SFT on reasoning traces) were bottlenecked by human-annotated demonstrations — they introduce cognitive biases, cap model performance at human-level exemplars, and prevent exploration of non-human reasoning pathways. The authors identified this gap not through a literature survey but through a bold empirical hypothesis: what if SFT is actually *harmful* for reasoning because it constrains exploration? They tested this by simply removing SFT entirely and applying pure RL to a base model, which no major lab had seriously attempted at scale.\",\n    \"key_insight\": \"You don't need to teach a model HOW to reason — you only need to provide the right incentive structure (verifiable outcome rewards) and sufficient RL compute. Sophisticated reasoning behaviors like self-reflection, verification, backtracking, and dynamic strategy adaptation emerge autonomously from outcome-based RL alone, without any process supervision or human reasoning demonstrations. The 'aha moment' — where the model spontaneously starts using phrases like 'Wait, let me reconsider...' without ever being trained on such patterns — is the crystallization of this insight.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"DeepSeek-R1-Zero applies Group Relative Policy Optimization (GRPO) directly to the DeepSeek-V3-Base (671B MoE) model with only rule-based rewards: a binary accuracy reward (is the final answer correct?) and a format reward (are &lt;think>/&lt;answer> tags present?). No SFT, no neural reward model, no process reward — just outcome verification. GRPO eliminates the value model required by PPO, computing advantages via group-relative normalization of sampled rewards (sample 16 outputs per question, normalize rewards within the group). The model naturally learns to produce longer chains of thought over training (from short answers to hundreds/thousands of tokens), developing self-verification and reflection spontaneously. DeepSeek-R1 then builds a production-quality model through a four-stage pipeline: (1) cold-start SFT on a small dataset of human-edited R1-Zero reasoning traces to fix readability/language-mixing, (2) large-scale RL with reasoning + language consistency rewards, (3) rejection sampling from the RL checkpoint to curate ~800K SFT examples (600K reasoning + 200K general), and (4) a second RL stage mixing rule-based reasoning rewards with neural reward models for helpfulness/safety. Finally, reasoning capabilities are distilled to smaller models (1.5B–70B) via SFT on R1-generated traces.\",\n    \"what_makes_it_good\": \"Three things made this Nature-worthy: (1) A clean, falsifiable scientific claim — 'pure RL without SFT produces emergent reasoning' — backed by the DeepSeek-R1-Zero experiment that serves as a controlled demonstration of emergence, complete with the compelling 'aha moment' observation that resonates beyond ML; (2) State-of-the-art results that match or exceed OpenAI o1 on AIME (79.8% pass@1), MATH-500 (97.3%), Codeforces (96.3 percentile), and GPQA Diamond, proving the approach isn't just theoretically interesting but practically dominant; (3) Full open-source release of models and detailed methodology, including distilled smaller models, which generated enormous community impact and reproducibility — rare for a result of this magnitude.\",\n    \"limitations_acknowledged\": \"The authors are remarkably candid: (1) pure RL only works for tasks with reliable verifiers — reward hacking remains unsolved for open-ended tasks like writing where neural RMs must be used; (2) language mixing persists especially for non-English/Chinese queries; (3) token inefficiency from overthinking on simple problems; (4) sensitivity to prompting (few-shot degrades performance); (5) limited gains on software engineering tasks due to slow evaluation loops during RL; (6) structured output and tool use remain weak.\",\n    \"open_questions\": [\n      \"How can we extend the pure RL approach to domains without clean verifiers (creative writing, open-ended reasoning, subjective tasks)? The paper explicitly calls this out as the fundamental open challenge — reward hacking with neural RMs limits scalability of RL for non-verifiable tasks.\",\n      \"What is the theoretical mechanism behind emergence of self-reflection in RL? The paper observes the 'aha moment' but doesn't explain WHY outcome-based RL produces process-level reasoning behaviors like backtracking and verification. Is this an inevitable consequence of sufficient RL training on a capable base model, or does it require specific architectural/data prerequisites?\",\n      \"Can the cold-start / distillation loop be iterated? The paper uses R1-Zero outputs to create cold-start data for R1, which is then distilled to smaller models. Could smaller distilled models themselves be RL-trained and their outputs used to improve the next generation, creating a self-improving flywheel?\"\n    ],\n    \"building_blocks\": [\n      \"GRPO (Group Relative Policy Optimization) — PPO without value model, using group-normalized advantages\",\n      \"Rule-based binary rewards (accuracy + format) as sole RL signal for reasoning tasks\",\n      \"DeepSeek-V3-Base (671B MoE with 37B active params) as strong base model\",\n      \"Cold-start data pipeline: RL-generated traces → human editing → LLM rewriting → human verification\",\n      \"Rejection sampling from RL checkpoints for large-scale synthetic reasoning data (600K samples)\",\n      \"Language consistency reward (proportion of target-language tokens in CoT)\",\n      \"Multi-stage training pipeline: cold-start SFT → RL → rejection sampling SFT → RL with mixed rewards\",\n      \"Distillation of long-CoT reasoning to smaller models (Qwen-1.5B to Llama-70B) via SFT on R1 traces\",\n      \"DeepSeek-V3 as generative judge for validating reasoning correctness in non-rule-based domains\",\n      \"Large PPO clip ratio (ε=10) — a non-obvious hyperparameter finding crucial for long-CoT RL stability\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is the foundational reference for our research area. It demonstrates the most successful instance of self-improvement for mathematical reasoning: RL on verifiable math problems produces synthetic reasoning traces (long CoTs with self-reflection) that surpass human-written demonstrations. The rejection sampling pipeline (Section B.3.3) is essentially a synthetic data generation engine — 600K reasoning samples generated from the model's own RL-trained checkpoint. The key lesson for our area: the quality ceiling of synthetic data can be raised by RL-driven self-play against verifiers rather than by collecting better human annotations. The distillation results further show that synthetic reasoning traces from large models transfer effectively to small models, outperforming those models' own RL training.\"\n  },\n  {\n    \"title\": \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\",\n    \"venue\": \"NeurIPS 2025 (Best Paper Runner-Up); ICML 2025 AI4MATH Workshop (Best Paper)\",\n    \"problem_identification\": \"The community had a widespread, largely unchallenged belief that RLVR (Reinforcement Learning with Verifiable Rewards) enables LLMs to 'self-improve' and acquire genuinely novel reasoning abilities beyond pretraining. The authors identified this gap by asking a deceptively simple but overlooked question: if we measure reasoning *capacity* (pass@k at large k) rather than *efficiency* (pass@1), does RLVR actually expand what the model can do? This reframing exposed that prior evaluations conflated improved sampling efficiency with expanded reasoning capability — a critical distinction nobody had rigorously tested at scale.\",\n    \"key_insight\": \"RLVR does not expand reasoning capacity — it narrows the output distribution to favor already-solvable problems, improving pass@1 at the cost of pass@k at large k. The base model's reasoning boundary is an upper bound, not a starting point, for RLVR-trained models. In other words, RL sharpens the distribution but cannot create probability mass where none existed in the pretrained model.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"The authors systematically evaluate RLVR-trained models against their base counterparts using the unbiased pass@k estimator (pass@k = E[1 - C(n-c,k)/C(n,k)]) at large k values (up to k=256 or 1024), sampling n=256+ responses per problem. They test across 7 model families (Qwen2.5-7B/14B/32B, LLaMA-3.1-8B, DeepSeek-R1-Distill, Qwen2.5-VL), 6 RL algorithms (PPO, GRPO, REINFORCE++, RLOO, ReMax, DAPO), and 10+ benchmarks spanning math, coding, and visual reasoning. They introduce the 'Sampling Efficiency Gap' (ΔSE = pass@1_RL - pass@256_base) to quantify how far RL is from fully exploiting base model potential. Supporting analyses include: (1) perplexity analysis showing RLVR outputs fall within the base model's distribution, (2) coverage analysis showing base models solve a strict superset of problems solvable by RLVR models, (3) manual chain-of-thought validation ruling out random guessing, and (4) a critical contrast with distillation, which genuinely expands pass@k curves above the base model's ceiling.\",\n    \"what_makes_it_good\": \"This paper succeeds through the rare combination of a provocative, clearly stated thesis and overwhelming empirical evidence that leaves almost no room for alternative explanations. The experimental design is exceptionally thorough — varying model families, sizes, RL algorithms, task domains, and evaluation scales — making it nearly impossible to dismiss as an artifact of any single choice. The distillation comparison is a masterful rhetorical move: by showing that distillation *does* expand reasoning boundaries using the same metric, it proves their evaluation methodology can detect genuine capability expansion, which makes the RLVR null result far more convincing. Reviewers and the meta-review explicitly praised the 'masterful execution' and the authors' ability to address every concern with additional experiments.\",\n    \"limitations_acknowledged\": \"The authors acknowledge they could not evaluate proprietary frontier models (OpenAI o1, full Qwen3-235B pipeline) and that most experiments used 7B-32B scale models. They also note the field is evolving rapidly, and future RL paradigms (process rewards, multi-turn agentic RL, continual scaling) might overcome the identified limitations.\",\n    \"open_questions\": [\n      \"Can process-based rewards (rewarding intermediate reasoning steps rather than binary outcomes) break through the base model's reasoning ceiling, or will they also be bounded by pretrained knowledge — and what theoretical framework would predict this?\",\n      \"Does the finding hold for truly frontier-scale models (100B+) trained with massive RL compute budgets, or is there a scale threshold where RL begins to discover genuinely novel reasoning strategies? The Magistral results hint at a narrowing gap but don't resolve this.\",\n      \"What is the optimal hybrid strategy combining distillation (to expand the reasoning frontier) with RLVR (to improve sampling efficiency within that frontier)? Is there a principled way to interleave these phases for maximum capability?\"\n    ],\n    \"building_blocks\": [\n      \"Unbiased pass@k estimator at large k as a metric for reasoning capacity vs. efficiency\",\n      \"Sampling Efficiency Gap (ΔSE) as a diagnostic for how well RL exploits base model potential\",\n      \"Perplexity analysis of RL outputs under base model distribution to assess novelty of reasoning\",\n      \"Coverage analysis (set-theoretic comparison of solvable problem sets across models)\",\n      \"Contrast methodology: using distillation as a positive control to validate the evaluation metric\",\n      \"GRPO, DAPO, and other open-source RLVR training pipelines (verl, OpenRLHF frameworks)\",\n      \"Multi-domain benchmark suite: GSM8K, MATH500, Minerva, Olympiad, AIME24, AMC23, LiveCodeBench, HumanEval+, MBPP+, MathVista, MathVision\"\n    ],\n    \"reviewer_feedback_summary\": \"All four reviewers rated the paper 6 (Strong Accept), with the meta-review calling it 'masterfully executed.' Key praise centered on: (1) the systematic, comprehensive evaluation making results hard to dismiss, (2) importance of the negative finding for the community, and (3) rigorous supporting analyses (perplexity, manual CoT validation). Main concerns were: (a) limited model scale (mostly 7-32B, not frontier), addressed with Magistral-Medium and Tulu-3-70B results showing consistent trends; (b) novelty relative to DeepSeekMath Section 5.2.2 which had a similar observation on a single model, addressed by arguing this is the first large-scale systematic study; (c) lack of theoretical explanation for why RL fails, partially addressed by citing concurrent theoretical work bounding probability mass outside base model support; (d) terminology ('reasoning capacity/boundary') being potentially misleading, with authors agreeing to revise to 'coverage/scope.'\",\n    \"relevance_to_seed\": \"This paper is foundational for our research area because it establishes that synthetic data generated via RLVR self-improvement cannot expand a model's reasoning frontier — only distillation from a stronger teacher can. For synthetic data and self-improvement research, this means: (1) pure RL-based self-play/self-improvement has a hard ceiling set by pretraining, (2) the most promising path combines teacher distillation (to expand the frontier) with RL (to improve efficiency within it), and (3) new self-improvement paradigms must fundamentally change the exploration mechanism (e.g., multi-turn tool use, process rewards, curriculum scaling) rather than just applying standard RLVR to break through this ceiling.\"\n  },\n  {\n    \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"Prior work showed mixed results on whether test-time compute helps LLMs — sometimes it works, sometimes it doesn't. The authors identified that this inconsistency was not a fundamental limitation but rather the consequence of a missing variable: problem difficulty. Nobody had systematically studied HOW to allocate test-time compute conditioned on the hardness of the specific prompt, nor had anyone rigorously compared the exchange rate between inference-time and pretraining FLOPs. They found this gap by observing that naive uniform strategies (like best-of-N with a fixed N) waste compute on easy problems and under-invest on hard ones.\",\n    \"key_insight\": \"Test-time compute effectiveness is not a single number — it is a function of prompt difficulty, and by treating difficulty as a sufficient statistic for selecting the compute-allocation strategy (beam search vs. best-of-N vs. sequential revision), you can achieve 4x better efficiency than uniform approaches. The deeper insight is that a smaller model with an optimal test-time compute budget can match a 14x larger model on a FLOPs-matched basis, but this exchange rate is NOT 1-to-1 and breaks down on the hardest out-of-distribution problems.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"The paper establishes a unified framework decomposing test-time compute into two orthogonal axes: (1) verifier-based search (best-of-N weighted, beam search with process reward models, lookahead search) and (2) proposal distribution modification (iterative self-revision via fine-tuned revision models). They define 'compute-optimal scaling' as selecting the strategy and hyperparameters per-prompt that maximize accuracy under a fixed compute budget, using the base model's pass@1 rate (binned into 5 difficulty quantiles) as a practical proxy for question difficulty. For deployment, they replace oracle difficulty with model-predicted difficulty using averaged PRM scores. They train process reward models without human labels using Monte Carlo rollout estimates of step-level correctness, and train revision models on synthetically constructed multi-turn correction trajectories (pairing incorrect attempts with subsequent correct ones via character-edit-distance matching). The key experimental comparison is a FLOPs-matched evaluation where a small model (PaLM 2-S*) with optimal test-time compute is compared against a 14x larger model, using the ratio of inference tokens to pretraining tokens (R) to determine when each strategy dominates.\",\n    \"what_makes_it_good\": \"This paper succeeded because it reframed a confused empirical landscape into a clean optimization problem with actionable structure. Rather than proposing a single new method, it provided a principled meta-framework that explains WHEN and WHY different test-time strategies work, which is more valuable than any individual technique. The FLOPs-matched comparison between test-time compute and model scaling was a novel and compelling experimental design that gave the field a quantitative vocabulary for reasoning about the inference-vs-pretraining tradeoff — this directly enabled the 'reasoning model' paradigm (o1, etc.). Reviewers specifically praised the 'unified perspective,' 'significant practical implications,' and the thoroughness of ablations across difficulty levels.\",\n    \"limitations_acknowledged\": \"The authors acknowledged that experiments were limited to the MATH benchmark (a single domain), that the cost of difficulty estimation was not accounted for in compute budgets, that gains plateau on the hardest problems where the base model has near-zero capability, and that they did not combine PRM search with revision models (leaving a potentially powerful hybrid unexplored).\",\n    \"open_questions\": [\n      \"How does compute-optimal test-time scaling transfer to domains beyond math/code where verification is harder or impossible (e.g., creative writing, open-ended reasoning)? The authors themselves noted that most NLP benchmarks test knowledge rather than reasoning.\",\n      \"What is the optimal joint strategy when combining verifier search AND distribution revision simultaneously? The paper studied them independently but acknowledged the combination was unexplored.\",\n      \"Can the gains from compute-optimal test-time strategies be distilled back into the base model (i.e., can you train a model that implicitly allocates variable compute per-problem)? This connects directly to the subsequent development of reasoning models like o1 and R1.\"\n    ],\n    \"building_blocks\": [\n      \"Process Reward Models (PRMs) trained via Monte Carlo rollout estimation (no human labels needed)\",\n      \"Difficulty-conditioned compute allocation using pass@1 rate as proxy\",\n      \"Best-of-N weighted sampling with PRM scoring\",\n      \"Beam search with PRM reward-to-go estimates\",\n      \"Lookahead search with k-step rollouts for improved value estimation\",\n      \"Synthetic multi-turn revision trajectory construction (pairing wrong→right attempts via edit distance)\",\n      \"FLOPs-matched evaluation framework for comparing inference-time vs. pretraining compute\",\n      \"Two-fold cross-validation on difficulty bins to avoid selection bias\",\n      \"Model-predicted difficulty estimation using averaged verifier scores\",\n      \"MATH benchmark (500 test questions)\"\n    ],\n    \"reviewer_feedback_summary\": \"Scores: 8, 6, 8, 8 (mean 7.5). Reviewers unanimously praised the unified framework, systematic analysis, and practical implications. The strongest praise came for the 'insightful analysis on searching with PRMs and iterative self-refinement' (hoB2) and 'comprehensive experiments' (19PN). The primary concerns were: (1) single-dataset evaluation on MATH raising generalizability questions (all 4 reviewers), (2) whether PRM/verifier training costs should be included in compute budgets (MYbX, u4qM), (3) limited exploration of hyperparameter sensitivity and verifier quality (19PN, MYbX), and (4) some claims of test-time superiority being overstated since advantages are concentrated on easier questions (u4qM). Authors responded effectively by: adding experiments with 20% label-flip noise on verifiers showing robustness, citing two independent reproduction papers on different models/benchmarks, and modifying the title to scope claims to 'reasoning tasks.' Reviewer MYbX raised their score from 5→6 after rebuttal. The paper was described by the meta-reviewer as a 'proof-of-concept' that 'will pave the way for future studies.'\",\n    \"relevance_to_seed\": \"This paper is foundational to synthetic data and self-improvement for mathematical reasoning because it establishes the theoretical and empirical framework for WHY test-time compute works and WHEN it is cost-effective. Its specific contributions — PRM training without human labels via Monte Carlo rollouts, synthetic revision trajectory construction, and difficulty-conditioned strategy selection — are directly reusable building blocks for any self-improvement pipeline. The key lesson for our research area: the most impactful contribution was not a new model or dataset, but a new way of THINKING about the problem (compute allocation as an optimization over difficulty) that unified prior scattered results into a coherent framework.\"\n  },\n  {\n    \"title\": \"Training Language Models to Self-Correct via Reinforcement Learning (SCoRe)\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"The authors identified that intrinsic self-correction (without external feedback) is essentially broken in modern LLMs — prompting-based methods fail, and SFT-based approaches hit two specific failure modes. They found this not by theorizing, but by running careful diagnostic experiments: they measured edit distance distributions, tracked correction rates under 'fixed' vs 'self-generated' first attempts, and decomposed accuracy into i→c and c→i transitions. This empirical dissection revealed (1) distribution shift — SFT models learn to correct the *base model's* mistakes but not their own post-training mistakes — and (2) behavior collapse — models learn to produce good first answers and make minimal/no edits, a degenerate but equally optimal strategy on training data.\",\n    \"key_insight\": \"Self-correction is a 'meta-strategy' that admits a spurious shortcut: on any finite training set, 'produce the best possible first answer then change nothing' scores equally well as 'learn to actually fix mistakes.' This is directly analogous to the memorization problem in meta-learning (Yin et al., 2019). The fix requires explicitly making the shortcut less attractive: decouple the two attempts via asymmetric KL constraints (Stage I), then bias rewards toward correction *progress* rather than absolute correctness (Stage II).\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"SCoRe is a two-stage on-policy multi-turn RL method. Stage I trains an initialization that decouples attempts: it optimizes second-attempt reward while applying a strong KL penalty *only on the first attempt* to keep it close to the base model, preventing the model from coupling both turns into a single high-quality response. Stage II then jointly optimizes both attempts using REINFORCE with a shaped reward bonus b(y₂|y₁) = α·(r(y₂) - r(y₁)), which explicitly rewards transitions that flip incorrect→correct and heavily penalizes correct→incorrect transitions. Both stages use on-policy sampling to avoid distribution shift. The method uses binary correctness rewards (answer checkers for math, test cases for code) and requires no external models, teacher supervision, or human feedback — only self-generated data from the model being trained.\",\n    \"what_makes_it_good\": \"Three things made this paper exceptional: (1) Section 4 is a masterclass in diagnostic research — before proposing their method, they systematically dissect *why* SFT fails through edit distance analysis, distribution shift experiments, and behavior collapse measurements, making the subsequent method feel inevitable rather than ad-hoc. (2) The connection to meta-learning memorization is a genuinely novel conceptual bridge that reframes the problem and explains why naive RL also collapses. (3) The results are unambiguous — SCoRe achieves the first significantly positive intrinsic self-correction (Δ(t1,t2) = +4.4% on MATH vs. -11.2% for the base model), with clean ablations showing each component matters. All four reviewers gave 8/10, praising the clarity and rigor.\",\n    \"limitations_acknowledged\": \"The authors note they only trained for two turns due to infrastructure constraints, meaning additional correction rounds may not be effective. They also acknowledge that unifying Stages I and II into a single training run would be desirable, and that their results are limited to Gemini models and a small set of benchmarks (though they added Gemma 2B and additional benchmarks during rebuttal).\",\n    \"open_questions\": [\n      \"Can this approach scale to many turns of iterative self-correction (3, 5, 10 turns)? The two-turn limitation is architectural, not fundamental, and the authors' preliminary multi-turn results (Appendix A.1) show SCoRe plateaus after ~2 turns, suggesting the training distribution must match the evaluation horizon.\",\n      \"Does the two-stage design generalize to other meta-strategies beyond self-correction (e.g., self-verification, adaptive problem decomposition, backtracking search)? The memorization-in-meta-learning framing suggests a general principle for training any 'algorithmic' behavior in LLMs.\",\n      \"Can the reward shaping approach be replaced or augmented with process reward models (PRMs) that provide denser feedback on the quality of corrections, potentially enabling more fine-grained self-correction strategies?\"\n    ],\n    \"building_blocks\": [\n      \"REINFORCE with KL-divergence penalty (Ahmadian et al., 2024)\",\n      \"Multi-turn MDP formulation for LLM training (Zhou et al., 2024 - ARCHER)\",\n      \"STaR / self-training on model-generated traces (Zelikman et al., 2022)\",\n      \"Binary correctness rewards via answer checkers and test-case execution\",\n      \"Reward shaping via progress bonus (r(y₂) - r(y₁))\",\n      \"Asymmetric KL regularization across turns\",\n      \"Self-consistency decoding / majority voting (Wang et al., 2022)\",\n      \"Gemini 1.0 Pro and 1.5 Flash models\",\n      \"MATH, HumanEval, and MBPP benchmarks\",\n      \"Edit distance ratio analysis for diagnosing behavior collapse\"\n    ],\n    \"reviewer_feedback_summary\": \"All four reviewers scored 8/10. Key praise: (1) 'commendable clarity' in writing and method explanation, (2) 'very solid experiments and ablation studies,' (3) the failure-mode analysis of SFT was seen as a standalone contribution, (4) first successful reliable intrinsic self-correction approach. Key concerns: (1) reproducibility — private Gemini models limit external validation (addressed by adding Gemma 2B experiments showing 16.8%→24% improvement), (2) only two-turn training demonstrated (addressed by showing positive results extending to three turns), (3) potential that reward shaping encourages deliberately worse first attempts (addressed empirically — Accuracy@t1 actually improves), (4) limited dataset diversity with only 3 benchmarks (partially addressed by adding Functional Math and MathOdyssey evaluations). The meta-reviewer highlighted that authors 'successfully addressed concerns' during rebuttal.\",\n    \"relevance_to_seed\": \"Directly relevant to synthetic data and self-improvement for mathematical reasoning: SCoRe demonstrates that the *training paradigm* matters as much as the data — SFT on self-generated correction traces fails, but on-policy RL with careful regularization on the same task succeeds dramatically. The key transferable lesson for our research area is that teaching LLMs meta-cognitive strategies (like self-correction or verification) requires explicitly preventing behavioral shortcuts through reward design and training structure, not just generating more or better synthetic data.\"\n  },\n  {\n    \"title\": \"WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"Open-source LLMs significantly underperformed proprietary models on complex multi-step mathematical reasoning. The authors identified that prior approaches either expanded pre-training corpora or bolted on external tools (Python interpreters), but neither systematically addressed the quality and difficulty distribution of fine-tuning instructions nor combined this with process-level supervision. The key gap was that existing synthetic data methods (like MetaMathQA) augmented quantity without controlling difficulty progression, and outcome-supervised RL missed errors hidden behind correct final answers (the 'false-positive problem' where wrong reasoning yields right answers ~2.5% of the time).\",\n    \"key_insight\": \"Bidirectional instruction evolution — not just making problems harder (upward) but also deliberately creating easier variants (downward) — paired with step-level process supervision creates a far more effective training signal than either technique alone. The 'downward evolution' idea is the subtle innovation: by generating simpler problems from hard seeds, you fill gaps in the difficulty spectrum that raw dataset augmentation misses, producing a smoother curriculum. When combined with a Process-Supervised Reward Model that scores every reasoning step (not just the final answer), PPO training can simultaneously eliminate false-positive reasoning chains and reward genuine problem-solving skill across the full difficulty range.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"The method has three interlocking stages. First, Math Evol-Instruct applies GPT-4 to evolve seed problems (from GSM8k + MATH) through 5 rounds — 2 downward (simplification/topic variation) and 3 upward (adding constraints, concretizing, extending reasoning chains) — producing 448k unique instructions filtered to 418k after contamination checks. Second, two reward models are trained: an Instruction Reward Model (IRM) that scores instruction quality/difficulty using GPT-4 pairwise rankings, and a Process-Supervised Reward Model (PRM) that scores individual reasoning steps using GPT-4 step-level correctness annotations, addressing the false-positive problem where incorrect reasoning accidentally produces correct final answers. Third, PPO training optimizes the SFT-initialized model using a combined reward signal r = r^q · r^a (IRM score × minimum PRM step score), ensuring the model is simultaneously pushed toward harder, higher-quality problems and penalized for flawed intermediate reasoning. At inference, majority voting weighted by PRM scores across multiple reasoning paths provides verification.\",\n    \"what_makes_it_good\": \"Three factors earned this paper an oral. First, the empirical results are undeniable: a 7B model beating GPT-3.5-Turbo and a 70B model surpassing GPT-4-early on MATH (58.6 vs 52.6) is a headline result that proves open-source can compete. Second, the ablation study is exceptionally thorough — the authors decompose contributions of each evolution direction, each reward model, data efficiency comparisons against MetaMathQA (15-20% MATH advantage at equal sample counts), false-positive rate reduction (2.58% → 0.68%), and PRM vs ORM comparisons — making the engineering choices legible and reproducible. Third, reviewers appreciated the comprehensive rebuttal: when challenged on GPT-4 dependency, the authors demonstrated Llama-3-70B/405B as viable substitutes with quantified performance gaps (5-6%), and extended RLEIF to code reasoning (4-5% gains on HumanEval/MBPP), showing generalizability beyond math.\",\n    \"limitations_acknowledged\": \"The approach relies on GPT-4 for both instruction evolution and step-level PRM annotation, creating a dependency on proprietary models (though open-source substitutes were shown viable with a 5-6% performance gap). The evaluation focuses primarily on grade-school to high-school mathematics, with limited exploration of harder competition-level or research-level mathematical reasoning, and domain generalization beyond math and code remains unexplored.\",\n    \"open_questions\": [\n      \"Can the full pipeline become self-bootstrapping — using the trained model itself (rather than GPT-4 or any external teacher) to generate evolutions and step-level annotations, creating a true self-improvement loop?\",\n      \"How does bidirectional instruction evolution interact with scaling laws? The paper shows 5 rounds are optimal, but is this a function of the seed data size, the base model capacity, or the evolution model quality? Could more sophisticated curriculum scheduling (adaptive round allocation) yield further gains?\",\n      \"The false-positive reduction (2.58% → 0.68%) is compelling but still nonzero — can process supervision be pushed further with tree-search methods (MCTS) or verification chains, and does the remaining error rate become a bottleneck at harder difficulty levels where false-positive rates may be higher?\"\n    ],\n    \"building_blocks\": [\n      \"Evol-Instruct framework (bidirectional: upward complexity + downward simplification)\",\n      \"Process-Supervised Reward Model (PRM) with AI-generated step-level annotations\",\n      \"Instruction Reward Model (IRM) for quality/difficulty scoring\",\n      \"PPO with multiplicative reward combining IRM × PRM\",\n      \"PRM-weighted majority voting for inference-time verification\",\n      \"GSM8k and MATH as seed datasets for evolution\",\n      \"GPT-4 as evolution engine and annotation oracle (with Llama-3-70B/405B as demonstrated substitutes)\",\n      \"Contamination filtering pipeline for evolved data\",\n      \"False-positive analysis methodology for reasoning chain quality\"\n    ],\n    \"reviewer_feedback_summary\": \"All four reviewers scored 8 (one raised from 7 after rebuttal). Decision: Accept (Oral). Key praise: impressive empirical results, thorough ablations decomposing each component's contribution, and strong rebuttal addressing all concerns. Primary concerns were: (1) GPT-4 dependency for data synthesis and PRM annotation — addressed by demonstrating Llama-3-70B/405B as viable substitutes with quantified gaps; (2) limited domain scope beyond math — addressed by extending RLEIF to code (4-5% HumanEval/MBPP gains); (3) marginality of individual contributions — authors argued novelty of downward evolution concept, IRM as a new component, and being first to use AI annotation for step-level PRM data at scale; (4) presentation issues including unclear figures, unexplained table rows, and insufficient introduction of Evol-Instruct — committed to major camera-ready revision (671 lines of additional content). The area chair noted that RL contributions deserved greater emphasis and that authors' comprehensive experiments demonstrating SFT dataset superiority over alternatives were convincing.\",\n    \"relevance_to_seed\": \"This paper is a foundational contribution to synthetic data and self-improvement for math reasoning, demonstrating that the quality and difficulty distribution of synthetic data matters more than sheer quantity (15-20% MATH advantage over MetaMathQA at equal sample counts). The key transferable lesson for our research area is the bidirectional evolution principle: don't just make problems harder — also generate easier variants to fill curriculum gaps — combined with process-level (not just outcome-level) supervision. The demonstrated path from GPT-4-dependent to open-source-model-driven pipelines (with quantified degradation) provides a practical roadmap for building self-improvement systems that can eventually bootstrap without proprietary teacher models.\"\n  },\n  {\n    \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\",\n    \"venue\": \"arXiv 2024 (preprint, highly cited; GRPO adopted by DeepSeek-R1 and widely in the field)\",\n    \"problem_identification\": \"The authors identified two compounding bottlenecks that kept open-source math models far behind GPT-4: (1) existing public math corpora (OpenWebMath at 13.6B tokens, MathPile at 8.9B) were dramatically undersized because their data pipelines lacked recall — they harvested only obvious math pages and missed the long tail of math-relevant content across Common Crawl; and (2) PPO-based reinforcement learning for math reasoning was prohibitively expensive because it requires a critic/value-function model roughly the same size as the policy, doubling GPU memory. They found the gap not by theoretical analysis but by empirically probing: training a 1.3B model on every available corpus (Table 1) showed massive headroom, and profiling PPO's memory footprint revealed the critic as the bottleneck.\",\n    \"key_insight\": \"You don't need a learned value function to estimate RL baselines — if you sample a group of outputs for the same question, the group's reward statistics (mean and standard deviation) serve as a natural, zero-parameter baseline. This 'group relative' advantage estimation is not only cheaper (eliminating ~50% memory overhead) but is actually better aligned with how reward models are trained (on comparative/pairwise data), making the reward signal more informative. Simultaneously, on the data side: an iterative domain-discovery loop — where you use a classifier's collection patterns to identify math-heavy web domains, then manually annotate those domains to expand the seed set — can snowball a small seed corpus into one 7–9× larger than prior work.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"DeepSeekMath operates on three fronts. First, a data selection pipeline: starting from OpenWebMath as seed data, they train a fastText classifier (500K pos/500K neg examples), sweep 40B deduplicated Common Crawl HTML pages, then identify web domains where >10% of pages were collected as 'math-rich,' manually annotate URL patterns from those domains, add uncollected pages to the seed set, and iterate — four rounds yield 35.5M pages (120B tokens), 7× larger than Minerva's corpus, with 98% recall by iteration 3. Second, continued pre-training: they initialize from DeepSeek-Coder-Base-v1.5 7B (leveraging the empirical finding that code pre-training transfers to mathematical reasoning) and train on 500B tokens (56% math corpus, 20% code, 10% arXiv, 10% NL, 4% AlgebraicStack). Third, Group Relative Policy Optimization (GRPO): for each question, sample G=64 outputs from the current policy, compute rewards, normalize them within the group to get advantages (Â_i,t = (r_i − mean)/std), and optimize a clipped surrogate objective with an explicit KL penalty against the reference policy — no critic model needed. They also present a unified framework showing SFT, RFT, DPO, Online RFT, PPO, and GRPO as points in a space defined by three axes: data source (online vs. offline), reward type (rule-based vs. model-based), and gradient coefficient form.\",\n    \"what_makes_it_good\": \"Three things elevate this paper beyond a typical systems contribution. First, the results are undeniable: a 7B model matching Minerva 540B and reaching 51.7% on MATH (within 1.2 points of GPT-4) is a 77× parameter-efficiency gain that demands explanation. Second, the paper doesn't just report a recipe — it provides deep ablative understanding: they isolate the contribution of code pre-training vs. math data, show that arXiv papers are surprisingly ineffective, demonstrate that online RL outperforms offline methods, and reveal through Pass@K vs. Maj@K analysis that RL improves distribution robustness rather than fundamental capabilities. Third, the unified RL framework (Table connecting SFT through GRPO alon\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T16:34:22.970Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T16:34:22.970Z",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-27T16:34:23.008Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-27 (UTC).**

## Research area: Synthetic Data and Self-Improvement for Mathematical Reasoning Training

## Paper analyses (21 papers)

[
  {
    "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
    "venue": "Nature 645, 633–638 (2025); arXiv Jan 2025",
    "problem_identification": "Prior reasoning improvements in LLMs (CoT prompting, SFT on reasoning traces) were bottlenecked by human-annotated demonstrations — they introduce cognitive biases, cap model performance at human-level exemplars, and prevent exploration of non-human reasoning pathways. The authors identified this gap not through a literature survey but through a bold empirical hypothesis: what if SFT is actually *harmful* for reasoning because it constrains exploration? They tested this by simply removing SFT entirely and applying pure RL to a base model, which no major lab had seriously attempted at scale.",
    "key_insight": "You don't need to teach a model HOW to reason — you only need to provide the right incentive structure (verifiable outcome rewards) and sufficient RL compute. Sophisticated reasoning behaviors like self-reflection, verification, backtracking, and dynamic strategy adaptation emerge autonomously from outcome-based RL alone, without any process supervision or human reasoning demonstrations. The 'aha moment' — where the model spontaneously starts using phrases like 'Wait, let me reconsider...' without ever being trained on such patterns — is the crystallization of this insight.",
    "innovation_type": "simplification",
    "method_summary": "DeepSeek-R1-Zero applies Group Relative Policy Optimization (GRPO) directly to the DeepSeek-V3-Base (671B MoE) model with only rule-based rewards: a binary accuracy reward (is the final answer correct?) and a format reward (are &lt;think>/&lt;answer> tags present?). No SFT, no neural reward model, no process reward — just outcome verification. GRPO eliminates the value model required by PPO, computing advantages via group-relative normalization of sampled rewards (sample 16 outputs per question, normalize rewards within the group). The model naturally learns to produce longer chains of thought over training (from short answers to hundreds/thousands of tokens), developing self-verification and reflection spontaneously. DeepSeek-R1 then builds a production-quality model through a four-stage pipeline: (1) cold-start SFT on a small dataset of human-edited R1-Zero reasoning traces to fix readability/language-mixing, (2) large-scale RL with reasoning + language consistency rewards, (3) rejection sampling from the RL checkpoint to curate ~800K SFT examples (600K reasoning + 200K general), and (4) a second RL stage mixing rule-based reasoning rewards with neural reward models for helpfulness/safety. Finally, reasoning capabilities are distilled to smaller models (1.5B–70B) via SFT on R1-generated traces.",
    "what_makes_it_good": "Three things made this Nature-worthy: (1) A clean, falsifiable scientific claim — 'pure RL without SFT produces emergent reasoning' — backed by the DeepSeek-R1-Zero experiment that serves as a controlled demonstration of emergence, complete with the compelling 'aha moment' observation that resonates beyond ML; (2) State-of-the-art results that match or exceed OpenAI o1 on AIME (79.8% pass@1), MATH-500 (97.3%), Codeforces (96.3 percentile), and GPQA Diamond, proving the approach isn't just theoretically interesting but practically dominant; (3) Full open-source release of models and detailed methodology, including distilled smaller models, which generated enormous community impact and reproducibility — rare for a result of this magnitude.",
    "limitations_acknowledged": "The authors are remarkably candid: (1) pure RL only works for tasks with reliable verifiers — reward hacking remains unsolved for open-ended tasks like writing where neural RMs must be used; (2) language mixing persists especially for non-English/Chinese queries; (3) token inefficiency from overthinking on simple problems; (4) sensitivity to prompting (few-shot degrades performance); (5) limited gains on software engineering tasks due to slow evaluation loops during RL; (6) structured output and tool use remain weak.",
    "open_questions": [
      "How can we extend the pure RL approach to domains without clean verifiers (creative writing, open-ended reasoning, subjective tasks)? The paper explicitly calls this out as the fundamental open challenge — reward hacking with neural RMs limits scalability of RL for non-verifiable tasks.",
      "What is the theoretical mechanism behind emergence of self-reflection in RL? The paper observes the 'aha moment' but doesn't explain WHY outcome-based RL produces process-level reasoning behaviors like backtracking and verification. Is this an inevitable consequence of sufficient RL training on a capable base model, or does it require specific architectural/data prerequisites?",
      "Can the cold-start / distillation loop be iterated? The paper uses R1-Zero outputs to create cold-start data for R1, which is then distilled to smaller models. Could smaller distilled models themselves be RL-trained and their outputs used to improve the next generation, creating a self-improving flywheel?"
    ],
    "building_blocks": [
      "GRPO (Group Relative Policy Optimization) — PPO without value model, using group-normalized advantages",
      "Rule-based binary rewards (accuracy + format) as sole RL signal for reasoning tasks",
      "DeepSeek-V3-Base (671B MoE with 37B active params) as strong base model",
      "Cold-start data pipeline: RL-generated traces → human editing → LLM rewriting → human verification",
      "Rejection sampling from RL checkpoints for large-scale synthetic reasoning data (600K samples)",
      "Language consistency reward (proportion of target-language tokens in CoT)",
      "Multi-stage training pipeline: cold-start SFT → RL → rejection sampling SFT → RL with mixed rewards",
      "Distillation of long-CoT reasoning to smaller models (Qwen-1.5B to Llama-70B) via SFT on R1 traces",
      "DeepSeek-V3 as generative judge for validating reasoning correctness in non-rule-based domains",
      "Large PPO clip ratio (ε=10) — a non-obvious hyperparameter finding crucial for long-CoT RL stability"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is the foundational reference for our research area. It demonstrates the most successful instance of self-improvement for mathematical reasoning: RL on verifiable math problems produces synthetic reasoning traces (long CoTs with self-reflection) that surpass human-written demonstrations. The rejection sampling pipeline (Section B.3.3) is essentially a synthetic data generation engine — 600K reasoning samples generated from the model's own RL-trained checkpoint. The key lesson for our area: the quality ceiling of synthetic data can be raised by RL-driven self-play against verifiers rather than by collecting better human annotations. The distillation results further show that synthetic reasoning traces from large models transfer effectively to small models, outperforming those models' own RL training."
  },
  {
    "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?",
    "venue": "NeurIPS 2025 (Best Paper Runner-Up); ICML 2025 AI4MATH Workshop (Best Paper)",
    "problem_identification": "The community had a widespread, largely unchallenged belief that RLVR (Reinforcement Learning with Verifiable Rewards) enables LLMs to 'self-improve' and acquire genuinely novel reasoning abilities beyond pretraining. The authors identified this gap by asking a deceptively simple but overlooked question: if we measure reasoning *capacity* (pass@k at large k) rather than *efficiency* (pass@1), does RLVR actually expand what the model can do? This reframing exposed that prior evaluations conflated improved sampling efficiency with expanded reasoning capability — a critical distinction nobody had rigorously tested at scale.",
    "key_insight": "RLVR does not expand reasoning capacity — it narrows the output distribution to favor already-solvable problems, improving pass@1 at the cost of pass@k at large k. The base model's reasoning boundary is an upper bound, not a starting point, for RLVR-trained models. In other words, RL sharpens the distribution but cannot create probability mass where none existed in the pretrained model.",
    "innovation_type": "analysis",
    "method_summary": "The authors systematically evaluate RLVR-trained models against their base counterparts using the unbiased pass@k estimator (pass@k = E[1 - C(n-c,k)/C(n,k)]) at large k values (up to k=256 or 1024), sampling n=256+ responses per problem. They test across 7 model families (Qwen2.5-7B/14B/32B, LLaMA-3.1-8B, DeepSeek-R1-Distill, Qwen2.5-VL), 6 RL algorithms (PPO, GRPO, REINFORCE++, RLOO, ReMax, DAPO), and 10+ benchmarks spanning math, coding, and visual reasoning. They introduce the 'Sampling Efficiency Gap' (ΔSE = pass@1_RL - pass@256_base) to quantify how far RL is from fully exploiting base model potential. Supporting analyses include: (1) perplexity analysis showing RLVR outputs fall within the base model's distribution, (2) coverage analysis showing base models solve a strict superset of problems solvable by RLVR models, (3) manual chain-of-thought validation ruling out random guessing, and (4) a critical contrast with distillation, which genuinely expands pass@k curves above the base model's ceiling.",
    "what_makes_it_good": "This paper succeeds through the rare combination of a provocative, clearly stated thesis and overwhelming empirical evidence that leaves almost no room for alternative explanations. The experimental design is exceptionally thorough — varying model families, sizes, RL algorithms, task domains, and evaluation scales — making it nearly impossible to dismiss as an artifact of any single choice. The distillation comparison is a masterful rhetorical move: by showing that distillation *does* expand reasoning boundaries using the same metric, it proves their evaluation methodology can detect genuine capability expansion, which makes the RLVR null result far more convincing. Reviewers and the meta-review explicitly praised the 'masterful execution' and the authors' ability to address every concern with additional experiments.",
    "limitations_acknowledged": "The authors acknowledge they could not evaluate proprietary frontier models (OpenAI o1, full Qwen3-235B pipeline) and that most experiments used 7B-32B scale models. They also note the field is evolving rapidly, and future RL paradigms (process rewards, multi-turn agentic RL, continual scaling) might overcome the identified limitations.",
    "open_questions": [
      "Can process-based rewards (rewarding intermediate reasoning steps rather than binary outcomes) break through the base model's reasoning ceiling, or will they also be bounded by pretrained knowledge — and what theoretical framework would predict this?",
      "Does the finding hold for truly frontier-scale models (100B+) trained with massive RL compute budgets, or is there a scale threshold where RL begins to discover genuinely novel reasoning strategies? The Magistral results hint at a narrowing gap but don't resolve this.",
      "What is the optimal hybrid strategy combining distillation (to expand the reasoning frontier) with RLVR (to improve sampling efficiency within that frontier)? Is there a principled way to interleave these phases for maximum capability?"
    ],
    "building_blocks": [
      "Unbiased pass@k estimator at large k as a metric for reasoning capacity vs. efficiency",
      "Sampling Efficiency Gap (ΔSE) as a diagnostic for how well RL exploits base model potential",
      "Perplexity analysis of RL outputs under base model distribution to assess novelty of reasoning",
      "Coverage analysis (set-theoretic comparison of solvable problem sets across models)",
      "Contrast methodology: using distillation as a positive control to validate the evaluation metric",
      "GRPO, DAPO, and other open-source RLVR training pipelines (verl, OpenRLHF frameworks)",
      "Multi-domain benchmark suite: GSM8K, MATH500, Minerva, Olympiad, AIME24, AMC23, LiveCodeBench, HumanEval+, MBPP+, MathVista, MathVision"
    ],
    "reviewer_feedback_summary": "All four reviewers rated the paper 6 (Strong Accept), with the meta-review calling it 'masterfully executed.' Key praise centered on: (1) the systematic, comprehensive evaluation making results hard to dismiss, (2) importance of the negative finding for the community, and (3) rigorous supporting analyses (perplexity, manual CoT validation). Main concerns were: (a) limited model scale (mostly 7-32B, not frontier), addressed with Magistral-Medium and Tulu-3-70B results showing consistent trends; (b) novelty relative to DeepSeekMath Section 5.2.2 which had a similar observation on a single model, addressed by arguing this is the first large-scale systematic study; (c) lack of theoretical explanation for why RL fails, partially addressed by citing concurrent theoretical work bounding probability mass outside base model support; (d) terminology ('reasoning capacity/boundary') being potentially misleading, with authors agreeing to revise to 'coverage/scope.'",
    "relevance_to_seed": "This paper is foundational for our research area because it establishes that synthetic data generated via RLVR self-improvement cannot expand a model's reasoning frontier — only distillation from a stronger teacher can. For synthetic data and self-improvement research, this means: (1) pure RL-based self-play/self-improvement has a hard ceiling set by pretraining, (2) the most promising path combines teacher distillation (to expand the frontier) with RL (to improve efficiency within it), and (3) new self-improvement paradigms must fundamentally change the exploration mechanism (e.g., multi-turn tool use, process rewards, curriculum scaling) rather than just applying standard RLVR to break through this ceiling."
  },
  {
    "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "Prior work showed mixed results on whether test-time compute helps LLMs — sometimes it works, sometimes it doesn't. The authors identified that this inconsistency was not a fundamental limitation but rather the consequence of a missing variable: problem difficulty. Nobody had systematically studied HOW to allocate test-time compute conditioned on the hardness of the specific prompt, nor had anyone rigorously compared the exchange rate between inference-time and pretraining FLOPs. They found this gap by observing that naive uniform strategies (like best-of-N with a fixed N) waste compute on easy problems and under-invest on hard ones.",
    "key_insight": "Test-time compute effectiveness is not a single number — it is a function of prompt difficulty, and by treating difficulty as a sufficient statistic for selecting the compute-allocation strategy (beam search vs. best-of-N vs. sequential revision), you can achieve 4x better efficiency than uniform approaches. The deeper insight is that a smaller model with an optimal test-time compute budget can match a 14x larger model on a FLOPs-matched basis, but this exchange rate is NOT 1-to-1 and breaks down on the hardest out-of-distribution problems.",
    "innovation_type": "analysis",
    "method_summary": "The paper establishes a unified framework decomposing test-time compute into two orthogonal axes: (1) verifier-based search (best-of-N weighted, beam search with process reward models, lookahead search) and (2) proposal distribution modification (iterative self-revision via fine-tuned revision models). They define 'compute-optimal scaling' as selecting the strategy and hyperparameters per-prompt that maximize accuracy under a fixed compute budget, using the base model's pass@1 rate (binned into 5 difficulty quantiles) as a practical proxy for question difficulty. For deployment, they replace oracle difficulty with model-predicted difficulty using averaged PRM scores. They train process reward models without human labels using Monte Carlo rollout estimates of step-level correctness, and train revision models on synthetically constructed multi-turn correction trajectories (pairing incorrect attempts with subsequent correct ones via character-edit-distance matching). The key experimental comparison is a FLOPs-matched evaluation where a small model (PaLM 2-S*) with optimal test-time compute is compared against a 14x larger model, using the ratio of inference tokens to pretraining tokens (R) to determine when each strategy dominates.",
    "what_makes_it_good": "This paper succeeded because it reframed a confused empirical landscape into a clean optimization problem with actionable structure. Rather than proposing a single new method, it provided a principled meta-framework that explains WHEN and WHY different test-time strategies work, which is more valuable than any individual technique. The FLOPs-matched comparison between test-time compute and model scaling was a novel and compelling experimental design that gave the field a quantitative vocabulary for reasoning about the inference-vs-pretraining tradeoff — this directly enabled the 'reasoning model' paradigm (o1, etc.). Reviewers specifically praised the 'unified perspective,' 'significant practical implications,' and the thoroughness of ablations across difficulty levels.",
    "limitations_acknowledged": "The authors acknowledged that experiments were limited to the MATH benchmark (a single domain), that the cost of difficulty estimation was not accounted for in compute budgets, that gains plateau on the hardest problems where the base model has near-zero capability, and that they did not combine PRM search with revision models (leaving a potentially powerful hybrid unexplored).",
    "open_questions": [
      "How does compute-optimal test-time scaling transfer to domains beyond math/code where verification is harder or impossible (e.g., creative writing, open-ended reasoning)? The authors themselves noted that most NLP benchmarks test knowledge rather than reasoning.",
      "What is the optimal joint strategy when combining verifier search AND distribution revision simultaneously? The paper studied them independently but acknowledged the combination was unexplored.",
      "Can the gains from compute-optimal test-time strategies be distilled back into the base model (i.e., can you train a model that implicitly allocates variable compute per-problem)? This connects directly to the subsequent development of reasoning models like o1 and R1."
    ],
    "building_blocks": [
      "Process Reward Models (PRMs) trained via Monte Carlo rollout estimation (no human labels needed)",
      "Difficulty-conditioned compute allocation using pass@1 rate as proxy",
      "Best-of-N weighted sampling with PRM scoring",
      "Beam search with PRM reward-to-go estimates",
      "Lookahead search with k-step rollouts for improved value estimation",
      "Synthetic multi-turn revision trajectory construction (pairing wrong→right attempts via edit distance)",
      "FLOPs-matched evaluation framework for comparing inference-time vs. pretraining compute",
      "Two-fold cross-validation on difficulty bins to avoid selection bias",
      "Model-predicted difficulty estimation using averaged verifier scores",
      "MATH benchmark (500 test questions)"
    ],
    "reviewer_feedback_summary": "Scores: 8, 6, 8, 8 (mean 7.5). Reviewers unanimously praised the unified framework, systematic analysis, and practical implications. The strongest praise came for the 'insightful analysis on searching with PRMs and iterative self-refinement' (hoB2) and 'comprehensive experiments' (19PN). The primary concerns were: (1) single-dataset evaluation on MATH raising generalizability questions (all 4 reviewers), (2) whether PRM/verifier training costs should be included in compute budgets (MYbX, u4qM), (3) limited exploration of hyperparameter sensitivity and verifier quality (19PN, MYbX), and (4) some claims of test-time superiority being overstated since advantages are concentrated on easier questions (u4qM). Authors responded effectively by: adding experiments with 20% label-flip noise on verifiers showing robustness, citing two independent reproduction papers on different models/benchmarks, and modifying the title to scope claims to 'reasoning tasks.' Reviewer MYbX raised their score from 5→6 after rebuttal. The paper was described by the meta-reviewer as a 'proof-of-concept' that 'will pave the way for future studies.'",
    "relevance_to_seed": "This paper is foundational to synthetic data and self-improvement for mathematical reasoning because it establishes the theoretical and empirical framework for WHY test-time compute works and WHEN it is cost-effective. Its specific contributions — PRM training without human labels via Monte Carlo rollouts, synthetic revision trajectory construction, and difficulty-conditioned strategy selection — are directly reusable building blocks for any self-improvement pipeline. The key lesson for our research area: the most impactful contribution was not a new model or dataset, but a new way of THINKING about the problem (compute allocation as an optimization over difficulty) that unified prior scattered results into a coherent framework."
  },
  {
    "title": "Training Language Models to Self-Correct via Reinforcement Learning (SCoRe)",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "The authors identified that intrinsic self-correction (without external feedback) is essentially broken in modern LLMs — prompting-based methods fail, and SFT-based approaches hit two specific failure modes. They found this not by theorizing, but by running careful diagnostic experiments: they measured edit distance distributions, tracked correction rates under 'fixed' vs 'self-generated' first attempts, and decomposed accuracy into i→c and c→i transitions. This empirical dissection revealed (1) distribution shift — SFT models learn to correct the *base model's* mistakes but not their own post-training mistakes — and (2) behavior collapse — models learn to produce good first answers and make minimal/no edits, a degenerate but equally optimal strategy on training data.",
    "key_insight": "Self-correction is a 'meta-strategy' that admits a spurious shortcut: on any finite training set, 'produce the best possible first answer then change nothing' scores equally well as 'learn to actually fix mistakes.' This is directly analogous to the memorization problem in meta-learning (Yin et al., 2019). The fix requires explicitly making the shortcut less attractive: decouple the two attempts via asymmetric KL constraints (Stage I), then bias rewards toward correction *progress* rather than absolute correctness (Stage II).",
    "innovation_type": "combination",
    "method_summary": "SCoRe is a two-stage on-policy multi-turn RL method. Stage I trains an initialization that decouples attempts: it optimizes second-attempt reward while applying a strong KL penalty *only on the first attempt* to keep it close to the base model, preventing the model from coupling both turns into a single high-quality response. Stage II then jointly optimizes both attempts using REINFORCE with a shaped reward bonus b(y₂|y₁) = α·(r(y₂) - r(y₁)), which explicitly rewards transitions that flip incorrect→correct and heavily penalizes correct→incorrect transitions. Both stages use on-policy sampling to avoid distribution shift. The method uses binary correctness rewards (answer checkers for math, test cases for code) and requires no external models, teacher supervision, or human feedback — only self-generated data from the model being trained.",
    "what_makes_it_good": "Three things made this paper exceptional: (1) Section 4 is a masterclass in diagnostic research — before proposing their method, they systematically dissect *why* SFT fails through edit distance analysis, distribution shift experiments, and behavior collapse measurements, making the subsequent method feel inevitable rather than ad-hoc. (2) The connection to meta-learning memorization is a genuinely novel conceptual bridge that reframes the problem and explains why naive RL also collapses. (3) The results are unambiguous — SCoRe achieves the first significantly positive intrinsic self-correction (Δ(t1,t2) = +4.4% on MATH vs. -11.2% for the base model), with clean ablations showing each component matters. All four reviewers gave 8/10, praising the clarity and rigor.",
    "limitations_acknowledged": "The authors note they only trained for two turns due to infrastructure constraints, meaning additional correction rounds may not be effective. They also acknowledge that unifying Stages I and II into a single training run would be desirable, and that their results are limited to Gemini models and a small set of benchmarks (though they added Gemma 2B and additional benchmarks during rebuttal).",
    "open_questions": [
      "Can this approach scale to many turns of iterative self-correction (3, 5, 10 turns)? The two-turn limitation is architectural, not fundamental, and the authors' preliminary multi-turn results (Appendix A.1) show SCoRe plateaus after ~2 turns, suggesting the training distribution must match the evaluation horizon.",
      "Does the two-stage design generalize to other meta-strategies beyond self-correction (e.g., self-verification, adaptive problem decomposition, backtracking search)? The memorization-in-meta-learning framing suggests a general principle for training any 'algorithmic' behavior in LLMs.",
      "Can the reward shaping approach be replaced or augmented with process reward models (PRMs) that provide denser feedback on the quality of corrections, potentially enabling more fine-grained self-correction strategies?"
    ],
    "building_blocks": [
      "REINFORCE with KL-divergence penalty (Ahmadian et al., 2024)",
      "Multi-turn MDP formulation for LLM training (Zhou et al., 2024 - ARCHER)",
      "STaR / self-training on model-generated traces (Zelikman et al., 2022)",
      "Binary correctness rewards via answer checkers and test-case execution",
      "Reward shaping via progress bonus (r(y₂) - r(y₁))",
      "Asymmetric KL regularization across turns",
      "Self-consistency decoding / majority voting (Wang et al., 2022)",
      "Gemini 1.0 Pro and 1.5 Flash models",
      "MATH, HumanEval, and MBPP benchmarks",
      "Edit distance ratio analysis for diagnosing behavior collapse"
    ],
    "reviewer_feedback_summary": "All four reviewers scored 8/10. Key praise: (1) 'commendable clarity' in writing and method explanation, (2) 'very solid experiments and ablation studies,' (3) the failure-mode analysis of SFT was seen as a standalone contribution, (4) first successful reliable intrinsic self-correction approach. Key concerns: (1) reproducibility — private Gemini models limit external validation (addressed by adding Gemma 2B experiments showing 16.8%→24% improvement), (2) only two-turn training demonstrated (addressed by showing positive results extending to three turns), (3) potential that reward shaping encourages deliberately worse first attempts (addressed empirically — Accuracy@t1 actually improves), (4) limited dataset diversity with only 3 benchmarks (partially addressed by adding Functional Math and MathOdyssey evaluations). The meta-reviewer highlighted that authors 'successfully addressed concerns' during rebuttal.",
    "relevance_to_seed": "Directly relevant to synthetic data and self-improvement for mathematical reasoning: SCoRe demonstrates that the *training paradigm* matters as much as the data — SFT on self-generated correction traces fails, but on-policy RL with careful regularization on the same task succeeds dramatically. The key transferable lesson for our research area is that teaching LLMs meta-cognitive strategies (like self-correction or verification) requires explicitly preventing behavioral shortcuts through reward design and training structure, not just generating more or better synthetic data."
  },
  {
    "title": "WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "Open-source LLMs significantly underperformed proprietary models on complex multi-step mathematical reasoning. The authors identified that prior approaches either expanded pre-training corpora or bolted on external tools (Python interpreters), but neither systematically addressed the quality and difficulty distribution of fine-tuning instructions nor combined this with process-level supervision. The key gap was that existing synthetic data methods (like MetaMathQA) augmented quantity without controlling difficulty progression, and outcome-supervised RL missed errors hidden behind correct final answers (the 'false-positive problem' where wrong reasoning yields right answers ~2.5% of the time).",
    "key_insight": "Bidirectional instruction evolution — not just making problems harder (upward) but also deliberately creating easier variants (downward) — paired with step-level process supervision creates a far more effective training signal than either technique alone. The 'downward evolution' idea is the subtle innovation: by generating simpler problems from hard seeds, you fill gaps in the difficulty spectrum that raw dataset augmentation misses, producing a smoother curriculum. When combined with a Process-Supervised Reward Model that scores every reasoning step (not just the final answer), PPO training can simultaneously eliminate false-positive reasoning chains and reward genuine problem-solving skill across the full difficulty range.",
    "innovation_type": "combination",
    "method_summary": "The method has three interlocking stages. First, Math Evol-Instruct applies GPT-4 to evolve seed problems (from GSM8k + MATH) through 5 rounds — 2 downward (simplification/topic variation) and 3 upward (adding constraints, concretizing, extending reasoning chains) — producing 448k unique instructions filtered to 418k after contamination checks. Second, two reward models are trained: an Instruction Reward Model (IRM) that scores instruction quality/difficulty using GPT-4 pairwise rankings, and a Process-Supervised Reward Model (PRM) that scores individual reasoning steps using GPT-4 step-level correctness annotations, addressing the false-positive problem where incorrect reasoning accidentally produces correct final answers. Third, PPO training optimizes the SFT-initialized model using a combined reward signal r = r^q · r^a (IRM score × minimum PRM step score), ensuring the model is simultaneously pushed toward harder, higher-quality problems and penalized for flawed intermediate reasoning. At inference, majority voting weighted by PRM scores across multiple reasoning paths provides verification.",
    "what_makes_it_good": "Three factors earned this paper an oral. First, the empirical results are undeniable: a 7B model beating GPT-3.5-Turbo and a 70B model surpassing GPT-4-early on MATH (58.6 vs 52.6) is a headline result that proves open-source can compete. Second, the ablation study is exceptionally thorough — the authors decompose contributions of each evolution direction, each reward model, data efficiency comparisons against MetaMathQA (15-20% MATH advantage at equal sample counts), false-positive rate reduction (2.58% → 0.68%), and PRM vs ORM comparisons — making the engineering choices legible and reproducible. Third, reviewers appreciated the comprehensive rebuttal: when challenged on GPT-4 dependency, the authors demonstrated Llama-3-70B/405B as viable substitutes with quantified performance gaps (5-6%), and extended RLEIF to code reasoning (4-5% gains on HumanEval/MBPP), showing generalizability beyond math.",
    "limitations_acknowledged": "The approach relies on GPT-4 for both instruction evolution and step-level PRM annotation, creating a dependency on proprietary models (though open-source substitutes were shown viable with a 5-6% performance gap). The evaluation focuses primarily on grade-school to high-school mathematics, with limited exploration of harder competition-level or research-level mathematical reasoning, and domain generalization beyond math and code remains unexplored.",
    "open_questions": [
      "Can the full pipeline become self-bootstrapping — using the trained model itself (rather than GPT-4 or any external teacher) to generate evolutions and step-level annotations, creating a true self-improvement loop?",
      "How does bidirectional instruction evolution interact with scaling laws? The paper shows 5 rounds are optimal, but is this a function of the seed data size, the base model capacity, or the evolution model quality? Could more sophisticated curriculum scheduling (adaptive round allocation) yield further gains?",
      "The false-positive reduction (2.58% → 0.68%) is compelling but still nonzero — can process supervision be pushed further with tree-search methods (MCTS) or verification chains, and does the remaining error rate become a bottleneck at harder difficulty levels where false-positive rates may be higher?"
    ],
    "building_blocks": [
      "Evol-Instruct framework (bidirectional: upward complexity + downward simplification)",
      "Process-Supervised Reward Model (PRM) with AI-generated step-level annotations",
      "Instruction Reward Model (IRM) for quality/difficulty scoring",
      "PPO with multiplicative reward combining IRM × PRM",
      "PRM-weighted majority voting for inference-time verification",
      "GSM8k and MATH as seed datasets for evolution",
      "GPT-4 as evolution engine and annotation oracle (with Llama-3-70B/405B as demonstrated substitutes)",
      "Contamination filtering pipeline for evolved data",
      "False-positive analysis methodology for reasoning chain quality"
    ],
    "reviewer_feedback_summary": "All four reviewers scored 8 (one raised from 7 after rebuttal). Decision: Accept (Oral). Key praise: impressive empirical results, thorough ablations decomposing each component's contribution, and strong rebuttal addressing all concerns. Primary concerns were: (1) GPT-4 dependency for data synthesis and PRM annotation — addressed by demonstrating Llama-3-70B/405B as viable substitutes with quantified gaps; (2) limited domain scope beyond math — addressed by extending RLEIF to code (4-5% HumanEval/MBPP gains); (3) marginality of individual contributions — authors argued novelty of downward evolution concept, IRM as a new component, and being first to use AI annotation for step-level PRM data at scale; (4) presentation issues including unclear figures, unexplained table rows, and insufficient introduction of Evol-Instruct — committed to major camera-ready revision (671 lines of additional content). The area chair noted that RL contributions deserved greater emphasis and that authors' comprehensive experiments demonstrating SFT dataset superiority over alternatives were convincing.",
    "relevance_to_seed": "This paper is a foundational contribution to synthetic data and self-improvement for math reasoning, demonstrating that the quality and difficulty distribution of synthetic data matters more than sheer quantity (15-20% MATH advantage over MetaMathQA at equal sample counts). The key transferable lesson for our research area is the bidirectional evolution principle: don't just make problems harder — also generate easier variants to fill curriculum gaps — combined with process-level (not just outcome-level) supervision. The demonstrated path from GPT-4-dependent to open-source-model-driven pipelines (with quantified degradation) provides a practical roadmap for building self-improvement systems that can eventually bootstrap without proprietary teacher models."
  },
  {
    "title": "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models",
    "venue": "arXiv 2024 (preprint, highly cited; GRPO adopted by DeepSeek-R1 and widely in the field)",
    "problem_identification": "The authors identified two compounding bottlenecks that kept open-source math models far behind GPT-4: (1) existing public math corpora (OpenWebMath at 13.6B tokens, MathPile at 8.9B) were dramatically undersized because their data pipelines lacked recall — they harvested only obvious math pages and missed the long tail of math-relevant content across Common Crawl; and (2) PPO-based reinforcement learning for math reasoning was prohibitively expensive because it requires a critic/value-function model roughly the same size as the policy, doubling GPU memory. They found the gap not by theoretical analysis but by empirically probing: training a 1.3B model on every available corpus (Table 1) showed massive headroom, and profiling PPO's memory footprint revealed the critic as the bottleneck.",
    "key_insight": "You don't need a learned value function to estimate RL baselines — if you sample a group of outputs for the same question, the group's reward statistics (mean and standard deviation) serve as a natural, zero-parameter baseline. This 'group relative' advantage estimation is not only cheaper (eliminating ~50% memory overhead) but is actually better aligned with how reward models are trained (on comparative/pairwise data), making the reward signal more informative. Simultaneously, on the data side: an iterative domain-discovery loop — where you use a classifier's collection patterns to identify math-heavy web domains, then manually annotate those domains to expand the seed set — can snowball a small seed corpus into one 7–9× larger than prior work.",
    "innovation_type": "combination",
    "method_summary": "DeepSeekMath operates on three fronts. First, a data selection pipeline: starting from OpenWebMath as seed data, they train a fastText classifier (500K pos/500K neg examples), sweep 40B deduplicated Common Crawl HTML pages, then identify web domains where >10% of pages were collected as 'math-rich,' manually annotate URL patterns from those domains, add uncollected pages to the seed set, and iterate — four rounds yield 35.5M pages (120B tokens), 7× larger than Minerva's corpus, with 98% recall by iteration 3. Second, continued pre-training: they initialize from DeepSeek-Coder-Base-v1.5 7B (leveraging the empirical finding that code pre-training transfers to mathematical reasoning) and train on 500B tokens (56% math corpus, 20% code, 10% arXiv, 10% NL, 4% AlgebraicStack). Third, Group Relative Policy Optimization (GRPO): for each question, sample G=64 outputs from the current policy, compute rewards, normalize them within the group to get advantages (Â_i,t = (r_i − mean)/std), and optimize a clipped surrogate objective with an explicit KL penalty against the reference policy — no critic model needed. They also present a unified framework showing SFT, RFT, DPO, Online RFT, PPO, and GRPO as points in a space defined by three axes: data source (online vs. offline), reward type (rule-based vs. model-based), and gradient coefficient form.",
    "what_makes_it_good": "Three things elevate this paper beyond a typical systems contribution. First, the results are undeniable: a 7B model matching Minerva 540B and reaching 51.7% on MATH (within 1.2 points of GPT-4) is a 77× parameter-efficiency gain that demands explanation. Second, the paper doesn't just report a recipe — it provides deep ablative understanding: they isolate the contribution of code pre-training vs. math data, show that arXiv papers are surprisingly ineffective, demonstrate that online RL outperforms offline methods, and reveal through Pass@K vs. Maj@K analysis that RL improves distribution robustness rather than fundamental capabilities. Third, the unified RL framework (Table connecting SFT through GRPO alon
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
  "promptId": "b4d96066-8d43-4769-bfde-543f778c5234",
  "type": "user",
  "uuid": "e0e288e9-2e03-446e-a874-06d384b0f152",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T16:34:23.006Z_

```json
{
  "parentUuid": "e0e288e9-2e03-446e-a874-06d384b0f152",
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
  "uuid": "b8039d35-03f0-42af-9a13-936e9b081469",
  "timestamp": "2026-05-27T16:34:23.006Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T16:34:23.006Z_

```json
{
  "parentUuid": "b8039d35-03f0-42af-9a13-936e9b081469",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b27205a9-d4e5-4d14-8711-bbe6496c6f2b",
  "timestamp": "2026-05-27T16:34:23.006Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-27 (UTC).**  ## Research area: Synthetic Data and Self-Improvement…",
  "leafUuid": "b27205a9-d4e5-4d14-8711-bbe6496c6f2b",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize math reasoning self-improvement research strategy",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa"
}
```

---

### Assistant

_source line 8 · 2026-05-27T16:34:32.600Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 21 paper analyses into a strategic "Field Guide" for the research area of "Synthetic Data and Self-Improvement for Mathematical Reasoning Training." However, the provided text only contains detailed analyses for about 6 papers (the rest were truncated). Let me work with what I have and produce a comprehensive synthesis.

Let me catalog what I have:
1. DeepSeek-R1 - Pure RL for reasoning, emergent behaviors
2. "Does RL Really Incentivize Reasoning" - RLVR doesn't expand reasoning capacity
3. "Scaling LLM Test-Time Compute" - Compute-optimal test-time strategies


4. SCoRe - Self-correction via RL
5. WizardMath - Reinforced Evol-Instruct
6. DeepSeekMath - GRPO and math data curation

I'm identifying the core themes across these papers: reinforcement learning approaches to reasoning, the tension between compute scaling and actual reasoning improvement, and various methods for synthetic data generation and self-improvement. Now I'll structure the field guide to capture the key insights and strategic directions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b27205a9-d4e5-4d14-8711-bbe6496c6f2b",
  "isSidechain": false,
  "requestId": "req_011CbTPyrv5BYXedseed6E7z",
  "type": "assistant",
  "uuid": "7e3dca61-6e46-454e-a6de-d610cb3271b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135Bo9kC6c98hXVRqChAD6a",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11424,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8247,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 11424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11424
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

_source line 9 · 2026-05-27T16:37:33.585Z_

I'll analyze the paper corpus carefully to extract patterns and synthesize the field guide. Let me work through the analyses systematically.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Simplification by Elimination",
      "description": "Removing a component that the field assumed was necessary (e.g., removing SFT, removing the value model, removing human annotations) and showing the system works better or comparably without it. This forces the community to re-examine assumptions and often reveals that the removed component was masking a simpler, more scalable mechanism.",
      "examples": ["DeepSeek-R1 (removed SFT, showed pure RL produces emergent reasoning)", "DeepSeekMath (removed critic/value model via GRPO, showed group-relative baselines suffice)", "Scaling Test-Time Compute (showed PRMs can be trained without human labels via Monte Carlo rollouts)"],
      "success_rate": "high"
    },
    {
      "pattern": "Diagnostic-First Method Design",
      "description": "Before proposing a new method, systematically diagnosing WHY existing approaches fail through careful ablation and measurement, then designing a method that specifically addresses the diagnosed failure modes. This makes the subsequent method feel 'inevitable' rather than ad-hoc and is consistently praised by reviewers.",
      "examples": ["SCoRe (diagnosed distribution shift and behavior collapse in SFT self-correction before proposing two-stage RL)", "Does RL Really Incentivize Reasoning (diagnosed pass@k vs pass@1 conflation before concluding RLVR doesn't expand capacity)", "DeepSeekMath (diagnosed contribution of code pretraining, arXiv data, online vs offline RL before proposing GRPO)"],
      "success_rate": "high"
    },
    {
      "pattern": "Unification-as-Contribution",
      "description": "Placing disparate existing methods on a common set of axes (data source, reward type, gradient form) or a common evaluation framework, then using this unified view to identify the optimal point in the design space. The framework itself becomes the primary contribution, more durable than any single method.",
      "examples": ["Scaling Test-Time Compute (unified best-of-N, beam search, and revision into a compute-allocation framework conditioned on difficulty)", "DeepSeekMath (unified SFT, RFT, DPO, PPO, GRPO along three axes)", "Does RL Really Incentivize Reasoning (unified RLVR evaluation across 7 model families, 6 RL algorithms, 10+ benchmarks)"],
      "success_rate": "high"
    },
    {
      "pattern": "Synthetic Data Quality over Quantity",
      "description": "Demonstrating that carefully curated or structured synthetic data (via difficulty control, process supervision, or curriculum design) dramatically outperforms larger but unstructured synthetic datasets. The innovation is in the data generation pipeline, not the training algorithm.",
      "examples": ["WizardMath (15-20% MATH advantage over MetaMathQA at equal sample counts via bidirectional evolution)", "DeepSeek-R1 (600K rejection-sampled reasoning traces from RL checkpoint outperform naive SFT data)", "DeepSeekMath (iterative domain-discovery loop yielding 7x larger but higher-quality math corpus)"],
      "success_rate": "high"
    },
    {
      "pattern": "Positive Control Methodology",
      "description": "When making a negative or surprising claim, including a 'positive control' that proves the evaluation methodology CAN detect the effect if it existed, making the null result far more convincing.",
      "examples": ["Does RL Really Incentivize Reasoning (showed distillation DOES expand pass@k, proving the metric works, which makes the RLVR null result credible)"],
      "success_rate": "high"
    },
    {
      "pattern": "Multi-Stage Pipeline with Interlocking Rewards",
      "description": "Designing training pipelines where different stages address different failure modes, with reward signals that combine multiple orthogonal dimensions (accuracy × process quality, or reasoning reward + format reward + language consistency).",
      "examples": ["DeepSeek-R1 (four-stage pipeline: cold-start SFT → RL → rejection sampling SFT → mixed-reward RL)", "WizardMath (IRM × PRM multiplicative reward combining instruction quality with step-level correctness)", "SCoRe (Stage I for decoupling attempts via asymmetric KL, Stage II for joint optimization with progress bonus)"],
      "success_rate": "medium"
    },
    {
      "pattern": "RL Without Neural Reward Models",
      "description": "Using rule-based, verifier-based, or self-generated reward signals instead of learned neural reward models, avoiding reward hacking and improving training stability for tasks where ground truth verification is available.",
      "examples": ["DeepSeek-R1 (binary accuracy + format rewards only for R1-Zero)", "SCoRe (binary correctness via answer checkers and test cases)", "DeepSeekMath (GRPO with rule-based math answer verification)"],
      "success_rate": "high"
    }
  ],
  "reviewer_preferences": [
    "Comprehensive ablations that decompose each component's individual contribution — reviewers across all papers (WizardMath, SCoRe, DeepSeekMath, Scaling Test-Time Compute) specifically praised thorough ablation studies that make engineering choices legible and reproducible.",
    "Clean, falsifiable scientific claims backed by controlled experiments — DeepSeek-R1's 'pure RL produces emergent reasoning' and 'Does RL Really Incentivize Reasoning's pass@k analysis both received top scores for stating clear theses and providing overwhelming evidence.",
    "Headline quantitative results that are hard to dismiss — WizardMath's 7B beating GPT-3.5-Turbo, DeepSeekMath's 7B matching Minerva 540B, and DeepSeek-R1's matching o1 all served as 'undeniable' proof points that earned oral presentations.",
    "Addressing reproducibility concerns proactively — SCoRe's addition of Gemma 2B experiments (open-source) after concerns about private Gemini models, and WizardMath's demonstration of Llama-3-70B/405B as GPT-4 substitutes, both directly raised reviewer scores.",
    "Negative or surprising results that are supported by exhaustive evidence across multiple axes of variation (model families, algorithms, benchmarks, scales) — 'Does RL Really Incentivize Reasoning' won Best Paper Runner-Up at NeurIPS 2025 precisely because the negative finding was backed by 7 model families × 6 RL algorithms × 10+ benchmarks.",
    "Novel conceptual frameworks that explain WHEN and WHY methods work, not just THAT they work — Scaling Test-Time Compute's difficulty-conditioned allocation framework and DeepSeekMath's unified RL design space both received specific reviewer praise for providing 'unified perspectives' beyond individual techniques.",
    "Domain generalization evidence — nearly every paper received concerns about limited evaluation scope (MATH-only, math-only, etc.), and papers that proactively showed results on additional domains (WizardMath extending to code, SCoRe showing results on HumanEval/MBPP) fared better in rebuttal.",
    "Honest acknowledgment of limitations with quantified degradation — WizardMath's explicit measurement of 5-6% performance gap when replacing GPT-4 with open-source models, and DeepSeek-R1's candid list of failure modes, were seen as signs of scientific maturity rather than weaknesses."
  ],
  "field_gaps": [
    {
      "gap": "Self-improvement for tasks without clean verifiers (creative writing, open-ended reasoning, subjective evaluation)",
      "evidence": "DeepSeek-R1 explicitly calls this 'the fundamental open challenge' — reward hacking with neural RMs limits RL scalability for non-verifiable tasks. Scaling Test-Time Compute notes most NLP benchmarks test knowledge not reasoning. WizardMath's evaluation is limited to grade/high-school math.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Breaking through the base model's reasoning ceiling via self-improvement (not distillation)",
      "evidence": "'Does RL Really Incentivize Reasoning' demonstrates RLVR narrows distribution but cannot create probability mass where none existed in the pretrained model. The paper explicitly asks whether process-based rewards, multi-turn tool use, or continual scaling can overcome this. DeepSeekMath's pass@K analysis independently showed RL improves distribution robustness rather than fundamental capabilities.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Fully self-bootstrapping pipelines that eliminate dependence on proprietary teacher models",
      "evidence": "WizardMath relies on GPT-4 for both instruction evolution and step-level PRM annotation (5-6% degradation with open-source substitutes). WizardMath's open question explicitly asks: can the trained model itself replace GPT-4 in the loop? DeepSeek-R1's distillation results show smaller models trained on R1 traces, but the question of whether these can be iterated remains open.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Scaling self-correction and meta-cognitive strategies beyond 2-3 turns",
      "evidence": "SCoRe only trained for two turns and showed plateauing after ~2 turns. The authors note the training distribution must match the evaluation horizon. No paper in the corpus demonstrates effective multi-turn (5-10 round) iterative refinement with sustained improvement per turn.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Joint optimization of verifier search AND distribution revision at test time",
      "evidence": "Scaling Test-Time Compute explicitly acknowledges studying PRM-based search and revision models independently but not in combination, calling this 'a potentially powerful hybrid' left unexplored.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Theoretical understanding of WHY outcome-based RL produces process-level reasoning behaviors",
      "evidence": "DeepSeek-R1 observes the 'aha moment' (spontaneous self-reflection) but provides no mechanistic explanation. 'Does RL Really Incentivize Reasoning' reviewers noted lack of theoretical explanation for why RL fails to expand capacity. The field has compelling empirical observations but no formal theory connecting reward structure to emergent reasoning behaviors.",
      "difficulty": "high",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Process supervision at scale without expensive human or GPT-4 annotation",
      "evidence": "WizardMath's PRM relies on GPT-4 step-level annotations. Scaling Test-Time Compute's Monte Carlo rollout PRM training avoids human labels but requires many rollouts per step. No paper demonstrates a cheap, scalable process reward signal that matches human-annotation quality across diverse mathematical domains.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Optimal interleaving of distillation and RLVR phases",
      "evidence": "'Does RL Really Incentivize Reasoning' identifies the hybrid strategy — distillation to expand frontier, RLVR to improve efficiency within it — as the most promising path, but notes there is no principled framework for when to switch between phases, how much distillation data to use, or how to schedule the interleaving.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "Bidirectional Evol-Instruct (WizardMath) applied to generate curriculum data for SCoRe-style multi-turn self-correction training — evolve both the problems AND the correction trajectories across difficulty levels, then train with on-policy RL and progress-based reward shaping",
      "from_papers": ["WizardMath", "SCoRe"],
      "why_promising": "WizardMath shows curriculum-controlled synthetic data dramatically improves SFT, and SCoRe shows that self-correction requires on-policy RL with careful reward design. Combining them would let the model learn difficulty-appropriate self-correction strategies: simple error fixes for easy problems, deep reasoning revision for hard ones. Neither paper addresses the other's strength."
    },
    {
      "idea_sketch": "Difficulty-conditioned compute allocation (Scaling Test-Time Compute) applied during RL training, not just at inference — allocate more RL training compute (more rollouts, more gradient steps) to problems at the model's difficulty frontier where pass@k is moderate, and less to already-solved or unsolvable problems",
      "from_papers": ["Scaling Test-Time Compute", "DeepSeek-R1", "Does RL Really Incentivize Reasoning"],
      "why_promising": "'Does RL Really Incentivize Reasoning' shows RLVR can only improve efficiency within the base model's existing capacity. Scaling Test-Time Compute shows difficulty-conditioning is key to efficiency. Combining these insights: focus RL training compute on the 'improvable band' (problems the model sometimes solves but not reliably) rather than uniformly sampling the training distribution. This could maximize the Sampling Efficiency Gap closure from 'Does RL Really Incentivize Reasoning'."
    },
    {
      "idea_sketch": "GRPO (DeepSeekMath) combined with SCoRe's asymmetric KL and progress bonus for multi-turn self-correction without a value model — use group-relative advantages across self-correction trajectories rather than single-turn completions",
      "from_papers": ["DeepSeekMath", "SCoRe"],
      "why_promising": "SCoRe uses REINFORCE with a KL penalty (requiring a reference model), while GRPO provides a more memory-efficient framework that eliminates the value model via group-relative normalization. Applying GRPO's group-based advantage estimation to multi-turn correction trajectories could make SCoRe-style training significantly cheaper and more scalable, potentially enabling 5-10 turn correction where infrastructure constraints previously limited SCoRe to 2 turns."
    },
    {
      "idea_sketch": "Iterative self-distillation loop where a model's RL-trained checkpoint generates rejection-sampled data (DeepSeek-R1 style), which is used to expand the reasoning frontier of a fresh base model via SFT distillation ('Does RL Really Incentivize Reasoning' shows distillation genuinely expands capacity), which then undergoes another round of RL — creating an alternating distillation-RL spiral that progressively raises both the ceiling and the efficiency",
      "from_papers": ["DeepSeek-R1", "Does RL Really Incentivize Reasoning"],
      "why_promising": "DeepSeek-R1 asks whether 'smaller distilled models can be RL-trained and their outputs used to improve the next generation.' 'Does RL Really Incentivize Reasoning' provides the theoretical justification: distillation expands the frontier (what the model CAN solve) while RL improves efficiency (what it DOES solve on the first try). An explicit spiral protocol could break through the ceiling that pure RL self-improvement hits."
    },
    {
      "idea_sketch": "Monte Carlo PRM training (Scaling Test-Time Compute) used to generate step-level annotations for WizardMath's process-supervised reward model, replacing GPT-4 annotation entirely and creating a self-contained open-source pipeline for process-supervised RL on math reasoning",
      "from_papers": ["Scaling Test-Time Compute", "WizardMath"],
      "why_promising": "WizardMath's biggest limitation is GPT-4 dependency for step-level PRM annotation. Scaling Test-Time Compute independently showed PRMs can be trained without human labels via Monte Carlo rollouts. Plugging the latter's PRM training method into the former's PPO pipeline eliminates the proprietary dependency while preserving the process supervision advantage that drives WizardMath's false-positive reduction (2.58% → 0.68%)."
    },
    {
      "idea_sketch": "DeepSeekMath's iterative domain-discovery loop for web data applied to identify math-relevant training data for multimodal models — extending from text-only Common Crawl to image-text pairs, diagrams, handwritten solutions, and video lectures with mathematical content",
      "from_papers": ["DeepSeekMath"],
      "why_promising": "DeepSeekMath's data pipeline yielded a 7x improvement in math corpus size through iterative domain discovery on text. Mathematical reasoning increasingly involves visual elements (geometry diagrams, graphs, scientific figures), and no paper in the corpus addresses systematic curation of multimodal math training data. The iterative classifier-based discovery approach is domain-agnostic and could be adapted to multimodal content."
    },
    {
      "idea_sketch": "Combining DeepSeek-R1's emergent self-reflection (learned through pure RL) with Scaling Test-Time Compute's difficulty-aware strategy selection — train a model via RL that not only reasons but also learns to estimate problem difficulty and dynamically allocate its own chain-of-thought length and verification depth accordingly, internalizing the compute-optimal allocation policy",
      "from_papers": ["DeepSeek-R1", "Scaling Test-Time Compute"],
      "why_promising": "DeepSeek-R1 shows models naturally learn longer CoTs for harder problems, but this is undirected — the model sometimes overthinks easy problems (acknowledged limitation). Scaling Test-Time Compute shows difficulty-conditioned allocation is 4x more efficient than uniform allocation. Adding a difficulty-estimation reward or auxiliary loss during RL could internalize the optimal allocation strategy, creating a model that dynamically chooses how much to think based on estimated problem hardness."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "Group Relative Policy Optimization (GRPO)",
      "what_it_does": "Eliminates the value/critic model from PPO by sampling G outputs per question, computing rewards, and normalizing advantages within the group (Â = (r - mean)/std). Reduces GPU memory by ~50% and aligns advantage estimation with comparative reward model training.",
      "used_by": ["DeepSeekMath", "DeepSeek-R1"],
      "could_be_applied_to": "Multi-turn self-correction training (replacing REINFORCE in SCoRe), multi-agent debate/verification, any RL application where memory constraints limit scaling"
    },
    {
      "tool": "Rule-based binary rewards (accuracy + format)",
      "what_it_does": "Provides RL signal using only verifiable outcome correctness (answer matching) and structural format compliance (tag presence), without neural reward models. Avoids reward hacking and enables reproducible training.",
      "used_by": ["DeepSeek-R1", "SCoRe", "DeepSeekMath"],
      "could_be_applied_to": "Any domain with automated verification: formal theorem proving (Lean/Isabelle), code generation (test suites), symbolic computation, constraint satisfaction problems"
    },
    {
      "tool": "Process Reward Models via Monte Carlo rollouts",
      "what_it_does": "Trains step-level reward models without human annotations by estimating each reasoning step's value through multiple Monte Carlo rollouts from that step, computing the empirical probability of reaching a correct final answer.",
      "used_by": ["Scaling Test-Time Compute"],
      "could_be_applied_to": "Replacing GPT-4-dependent step annotation in WizardMath's pipeline, providing dense training signal for tree-search methods (MCTS), enabling process supervision in domains where human step-level annotation is infeasible"
    },
    {
      "tool": "Rejection sampling from RL checkpoints",
      "what_it_does": "Generates large quantities of synthetic training data by sampling many completions from an RL-trained model, filtering for correctness, and using the filtered outputs as SFT data for the next training stage or for distillation to smaller models.",
      "used_by": ["DeepSeek-R1 (600K reasoning samples)", "DeepSeekMath"],
      "could_be_applied_to": "Creating high-quality training data for multi-turn reasoning, generating correction trajectory pairs for self-correction training, bootstrapping new domain-specific reasoning models"
    },
    {
      "tool": "Bidirectional instruction evolution (upward + downward)",
      "what_it_does": "Augments seed problems by evolving them both toward higher difficulty (adding constraints, extending reasoning chains) AND toward lower difficulty (simplification, topic variation), creating a smooth curriculum across the full difficulty spectrum.",
      "used_by": ["WizardMath"],
      "could_be_applied_to": "Curriculum design for any reasoning domain, generating evaluation benchmarks with controlled difficulty, creating training data for difficulty-aware compute allocation systems"
    },
    {
      "tool": "Asymmetric KL regularization across turns",
      "what_it_does": "Applies strong KL penalty only on the first attempt (keeping it close to base model) while allowing freedom on subsequent attempts, preventing the degenerate strategy of producing perfect first answers with no corrections.",
      "used_by": ["SCoRe"],
      "could_be_applied_to": "Any multi-turn RL setting where later turns should adapt to earlier turns: debate protocols, iterative refinement, hierarchical planning, hypothesis-test-revise loops"
    },
    {
      "tool": "Progress-based reward shaping (r(y₂) - r(y₁))",
      "what_it_does": "Shapes rewards to explicitly incentivize improvement between attempts rather than absolute correctness, rewarding incorrect→correct transitions and penalizing correct→incorrect regressions.",
      "used_by": ["SCoRe"],
      "could_be_applied_to": "Multi-turn tool use (rewarding better tool calls over time), iterative code debugging (rewarding test-case fixes), curriculum learning (rewarding mastery progression)"
    },
    {
      "tool": "Unbiased pass@k estimator at large k",
      "what_it_does": "Estimates the probability that at least one of k sampled responses is correct using the combinatorial formula pass@k = E[1 - C(n-c,k)/C(n,k)], providing a measure of reasoning capacity (what the model CAN solve) rather than efficiency (what it typically DOES solve).",
      "used_by": ["Does RL Really Incentivize Reasoning"],
      "could_be_applied_to": "Evaluating whether ANY training intervention genuinely expands capabilities vs. merely sharpening the distribution, measuring the 'exploration potential' of a base model before committing to RL training, comparing pre-training data recipes"
    },
    {
      "tool": "FLOPs-matched evaluation framework",
      "what_it_does": "Compares different strategies (test-time compute vs. larger models, RL vs. SFT) by equalizing total FLOPs rather than comparing raw accuracy, enabling principled cost-benefit analysis of compute allocation decisions.",
      "used_by": ["Scaling Test-Time Compute"],
      "could_be_applied_to": "Evaluating synthetic data generation cost vs. additional pre-training compute, comparing RL training compute vs. distillation compute, making deployment decisions about inference-time scaling vs. model scaling"
    },
    {
      "tool": "Iterative domain-discovery for web data curation",
      "what_it_does": "Uses a classifier trained on seed domain data to sweep web corpora, identifies domains with high collection rates, manually annotates new URL patterns from those domains, and iterates — snowballing a small seed into a corpus 7-9x larger with high recall.",
      "used_by": ["DeepSeekMath"],
      "could_be_applied_to": "Curating training data for any specialized domain (scientific reasoning, legal reasoning, medical reasoning), building multimodal training corpora, identifying code repositories with mathematical content"
    },
    {
      "tool": "Cold-start data pipeline (RL traces → human editing → LLM rewriting → verification)",
      "what_it_does": "Creates high-quality seed SFT data by taking raw RL-generated reasoning traces, having humans edit for readability and correctness, then using LLMs to rewrite at scale while maintaining quality, with final human verification.",
      "used_by": ["DeepSeek-R1"],
      "could_be_applied_to": "Bootstrapping any new reasoning domain where no high-quality training data exists, creating initial SFT data for domains transitioning from rule-based to neural approaches"
    }
  ],
  "common_pitfalls": [
    "Conflating sampling efficiency (pass@1) with reasoning capacity (pass@k at large k): 'Does RL Really Incentivize Reasoning' showed this is the field's most widespread evaluation error. Always measure pass@k at large k to determine whether your intervention genuinely expands what the model can do, or merely makes it more likely to produce correct answers it could already generate.",
    "Using SFT on self-generated traces for meta-cognitive tasks (self-correction, verification): SCoRe demonstrated two specific failure modes — distribution shift (model learns to correct the BASE model's mistakes, not its own) and behavior collapse (model learns to produce perfect first answers with zero edits). Any meta-cognitive capability that admits a 'shortcut' degenerate strategy requires on-policy RL with explicit anti-shortcut mechanisms, not SFT.",
    "Assuming more synthetic data is better without controlling difficulty distribution: WizardMath's 15-20% MATH advantage over MetaMathQA at EQUAL sample counts proves that structured difficulty progression (bidirectional evolution) matters far more than dataset size. Generating 1M random augmentations is less valuable than generating 100K carefully difficulty-calibrated samples.",
    "Using PPO when GRPO suffices: For tasks with verifiable rewards where you can sample multiple outputs per question, GRPO eliminates the value model (saving ~50% GPU memory) with equal or better performance. DeepSeekMath and DeepSeek-R1 both demonstrated this. Only use PPO when you genuinely need a value function (e.g., tasks requiring credit assignment across very long episodes where group-level statistics are too noisy).",
    "Relying exclusively on GPT-4 or proprietary models for data generation without demonstrating the path to open-source self-sufficiency: Reviewers consistently flag proprietary model dependency (WizardMath received this concern from multiple reviewers). Always include experiments showing open-source model substitutes with quantified performance degradation, and ideally design pipelines that can eventually self-bootstrap.",
    "Evaluating on a single benchmark or domain: Every paper in the corpus received reviewer concerns about limited evaluation scope. SCoRe added Gemma experiments and extra benchmarks during rebuttal; WizardMath extended to code. Build multi-domain evaluation into the experimental design from the start, including at least one out-of-distribution domain.",
    "Ignoring the false-positive problem in outcome-supervised training: WizardMath found 2.58% of reasoning chains with correct final answers contain incorrect intermediate steps. For RL training, these false positives provide misleading reward signal. Process supervision (step-level rewards) or majority voting with PRM weighting can mitigate this, but outcome-only rewards cannot.",
    "Claiming 'self-improvement' without establishing the appropriate baseline: After 'Does RL Really Incentivize Reasoning,' any claim of genuine self-improvement must show capability expansion beyond what the base model can achieve with sufficient sampling (pass@k at high k). Simply showing pass@1 improvement after RL is no longer sufficient evidence for 'new reasoning capabilities.'",
    "Applying uniform test-time compute strategies: Scaling Test-Time Compute showed difficulty-conditioned allocation is 4x more efficient than uniform strategies. Best-of-N with a fixed N wastes compute on easy problems and under-invests on hard ones. Always condition compute allocation on estimated problem difficulty.",
    "Using too-small RL clip ratios for long chain-of-thought training: DeepSeek-R1 found that a large PPO clip ratio (ε=10) was crucial for long-CoT RL stability — a non-obvious hyperparameter that deviates dramatically from standard PPO practice (ε=0.2). Standard hyperparameters from short-horizon RL may be inappropriate for reasoning tasks with thousands of tokens."
  ],
  "field_trajectory": "The field is converging on three macro-directions that will define the next 12-18 months of research. First, the DISTILLATION-RL SPIRAL: the finding that RLVR cannot expand reasoning capacity beyond the base model ('Does RL Really Incentivize Reasoning') combined with DeepSeek-R1's successful distillation pipeline points toward iterative loops where distillation from stronger models expands the frontier, RL improves efficiency within it, and the improved model's outputs become distillation data for the next generation. The key research question is whether this spiral converges, diverges, or plateaus — and at what scale. Second, PROCESS-LEVEL SELF-SUPERVISION AT SCALE: the gap between outcome-based rewards (which are cheap but coarse) and process-based rewards (which are informative but expensive) is the field's central tension. Monte Carlo PRM training (Scaling Test-Time Compute), GPT-4-based step annotation (WizardMath), and emergent self-reflection (DeepSeek-R1) represent three approaches to this tension, and the winning approach will likely combine cheap automatic process rewards with RL-driven internalization of verification behaviors. Third, MULTI-TURN AGENTIC REASONING: SCoRe's self-correction, test-time compute scaling, and the acknowledged limitations of single-turn RLVR all point toward training paradigms where models learn multi-step metacognitive strategies — not just 'think harder' but 'try, verify, diagnose, revise, try again' in a loop. This connects to the broader trend of tool-augmented reasoning where models can call external verifiers (code executors, proof assistants, search engines) as part of their reasoning chain, potentially breaking through the RLVR ceiling by changing what counts as 'exploration.' The field is rapidly shifting from 'can we make LLMs reason?' (answered yes) to 'how do we make reasoning self-improving and compute-optimal?' — and the papers that will define 2026-2027 will be those that crack the self-improvement ceiling with principled theoretical frameworks, not just scaled-up engineering.",
  "meta_advice": "If you're targeting a strong 2026 publication in this area, here is what the evidence from these papers tells you. First, lead with a diagnostic insight, not a method: the highest-impact papers in this corpus (SCoRe's behavior collapse analysis, 'Does RL Really Incentivize Reasoning's pass@k reframing, Scaling Test-Time Compute's difficulty conditioning) all earned their acceptance by first identifying WHY something fails, then proposing a fix. Reviewers are saturated with new training pipelines — what they reward is a clean, falsifiable claim that reframes how the community thinks about a problem. Second, your evaluation must be exhaustive to the point of overkill: the NeurIPS Best Paper Runner-Up tested across 7 model families, 6 RL algorithms, and 10+ benchmarks specifically because a surprising finding demands overwhelming evidence. If your result is surprising, triple your evaluation budget. If it's expected, at least include 3+ model families, 2+ domains, and the pass@k metric at large k. Third, target the distillation-RL interface: the most underdeveloped high-impact area is the optimal interleaving of distillation (which genuinely expands capability) and RL (which improves efficiency). A paper that provides a principled schedule — when to distill, when to RL, how to measure when you've saturated each phase — would fill a gap explicitly identified by 'Does RL Really Incentivize Reasoning' and implicitly by DeepSeek-R1. Fourth, make your pipeline open-source-native: every paper that depended on GPT-4 faced reviewer pushback, and the trend is clearly toward self-contained systems. Design your pipeline around open-weight models from day one, even if you also show GPT-4 results as an upper bound. Fifth, connect your math reasoning contribution to at least one other domain (code, scientific reasoning, formal proof) to preempt the inevitable 'limited scope' reviewer concern. The safest bet for a high-impact paper in 2026 is to take an established technique from this corpus (GRPO, process rewards, bidirectional evolution, self-correction training) and show it works in a new setting OR to combine two techniques that haven't been combined (see the untried combinations above), with a strong diagnostic analysis explaining why the combination is non-trivial and ablations proving each component matters."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e3dca61-6e46-454e-a6de-d610cb3271b9",
  "isSidechain": false,
  "requestId": "req_011CbTPyrv5BYXedseed6E7z",
  "type": "assistant",
  "uuid": "9769394e-0812-422c-a13a-2f12382aa145",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135Bo9kC6c98hXVRqChAD6a",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11424,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8247,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 11424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11424
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-27 (UTC).**  ## Research area: Synthetic Data and Self-Improvement…",
  "leafUuid": "9769394e-0812-422c-a13a-2f12382aa145",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize math reasoning self-improvement research strategy",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-27 (UTC).**  ## Research area: Synthetic Data and Self-Improvement…",
  "leafUuid": "9769394e-0812-422c-a13a-2f12382aa145",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize math reasoning self-improvement research strategy",
  "sessionId": "b9cd3fb6-1b5f-4ad1-848e-e1e91a8ef2aa"
}
```

---
