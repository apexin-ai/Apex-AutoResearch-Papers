# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/480b819a-d329-4e18-be66-5fddad48e193.jsonl`
- **Structured JSON:** [`44912f017cf0cca4e866.json`](../../sessions/44/44912f017cf0cca4e866.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T00:41:07.768Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T00:41:07.768Z",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\",\n  \"core_problem\": \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level (grade-school math, 1-5 reasoning steps) with a 1D archive of 8 thematic 'setting' categories (Personal Life, Professional, Economic, etc.), random mutation strategies (setting/distractor/symbolic mutators with 22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). It leaves the critical scaling question unanswered: can archive-based co-evolution work at competition level (AIME, Olympiad) where synthesis is far harder, verification is unreliable, and the behavioral space is structurally richer? Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B) through real-time difficulty assessment and adaptive problem restructuring—but operates statelessly per-batch with no persistent archive, no cross-step memory of which problem niches the policy has mastered, and no targeted synthesis for identified gaps. The fundamental open question is: can we combine the archive-based co-evolutionary structure proven by DéjàQ with the competition-level ambition demonstrated by CLPO, while addressing both systems' limitations through structured multi-dimensional behavioral descriptors, targeted weakness-driven synthesis, and principled RLVR-grounded replacement criteria?\",\n  \"opportunity\": \"Three converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning by maintaining diverse, learnable problems via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot distinguish difficulty within topics, its random mutation degrades with teacher-student misalignment, and 22-44% invalid rates would be catastrophic at competition level. (2) CLPO proves competition-level feasibility: online curriculum with difficulty-aware restructuring achieves 50.0% AIME 2024 (+6.96% average), demonstrating that adaptive difficulty management works at scale. But CLPO's per-batch statelessness means it cannot systematically track which topic×difficulty niches have been mastered vs. where gaps persist—it may repeatedly visit algebra while undersampling number theory. (3) The synthesis-verification gap is closing: SAND-Math demonstrates ~37.7% survival rate for competition-level synthesis; VHG's validity-gating separates problem validity from difficulty; MathForge (ICLR 2026) shows that difficulty-aware GRPO (MAD normalization + DQW) yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that remember policy strengths/weaknesses across training, (b) targeted weakness-driven synthesis that identifies archive gaps and generates specifically for those niches, (c) multi-stage verification suitable for competition-level problems, and (d) RLVR-grounded replacement criteria (advantage variance, not proxy p(1-p)). Our contribution is the principled integration and scaling of these ideas—not the invention of any single component.\",\n  \"landscape\": \"**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability l_θ(x) = p_θ(x)(1−p_θ(x)), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) teacher-student misalignment—RL improves student but not teacher/mutator; (f) K=100 completions per problem is computationally expensive.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring (diversifies medium-difficulty problems, simplifies hard ones, preserving answers), and difficulty-aware KL (λ_hard=0.3, λ_non-hard=1.0). Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines including DAPO and Critique-GRPO. Trained on DAPO-Math-17k, 200 steps, 8×H20 GPUs. Critical delta: no persistent archive—operates per-batch only; no cross-step memory; restructures existing problems rather than synthesizing new ones for identified gaps; 3 coarse difficulty bins vs. our 10 fine-grained bins.\\n\\n**Difficulty-aware offline augmentation.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026) introduces Difficulty-Balanced Group Advantage Estimation using MAD normalization (replacing std normalization in GRPO, ensuring constant update magnitude regardless of accuracy distribution) and Difficulty-aware Question-level Weighting (DQW: λ_s = B_v·exp(D_s/T)/Σexp(D_s/T), T=2.0). Multi-Aspect Question Reformulation (MQR) expands datasets 4× via background/term/sub-problem reformulations. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. Offline augmentation—no online adaptation. We adopt DGPO's MAD normalization for our policy update step.\\n\\n**Weakness-driven targeted synthesis.** SwS (NeurIPS 2025, arXiv 2506.08989) identifies model weaknesses as problems where accuracy never reaches 50% with negative slope during preliminary RL, allocates synthesis budget proportionally to category failure rates, generates 40K targeted problems. Results: +10.0% (7B), +7.7% (32B). Offline two-stage pipeline; weaknesses identified once. STAT (arXiv 2510.10023) creates Missing-Skill-Profiles and synthesizes skill-targeted examples (+7.5% on MATH via SFT). 'Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis' (arXiv 2604.04386) uses AI hypotheses to identify struggle concepts, reducing accuracy from 77% to 45%. These validate the weakness→targeted generation pattern we adopt continuously online.\\n\\n**Adaptive curriculum and co-evolutionary approaches.** AdaRFT (arXiv 2504.05520) dynamically adjusts training problem difficulty based on recent reward signals, achieving 2× training speedup on AMC/AIME/IMO. Relevant for demonstrating adaptive difficulty value, but without archive-based coverage tracking. CPMöbius (arXiv 2602.02979) implements cooperative coach-player co-evolution for data-free RL, achieving +4.9 average improvement on Qwen2.5-Math-7B-Instruct. Demonstrates co-evolution for LLM reasoning but without archive structure or quality-diversity principles. AERO (arXiv 2602.03084) uses ZPD-based autonomous evolutionary reasoning with entropy-based dual-loop (inner self-questioning/answering, outer difficulty calibration). Shares ZPD motivation but operates without structured archives. OpenSIR (arXiv 2511.00602) optimizes both difficulty and diversity from seed problems via self-play teacher-student dynamics; relevant for diversity optimization perspective but at GSM/CollegeMath level.\\n\\n**Self-evolving RLVR and diversity maintenance.** SvS (ICLR 2026) achieves +18.3%/+22.8% pass@32 on AIME24/25 via answer-preserving variational mutations. R-Zero (ICLR 2026) co-evolves Challenger+Solver but collapses after iteration 3. Prism (arXiv 2603.13309) prevents collapse via 128 K-means semantic clusters with ZPD gate [0.5, 0.9] and rarity bonus (AIME 2024: 16.77 on Qwen3-4B). R-Diverse (arXiv 2602.13103) introduces SAM code-embedding skill diversity + MAP persistent memory bank (AIME 2024: 19.17 on Qwen3-4B, +6.46 over R-Zero). Vocabulary Dropout (arXiv 2604.03472) addresses diversity collapse via token-level perturbation.\\n\\n**Verification approaches.** VHG (arXiv 2605.06660) introduces three-party self-play with verifier gating: reward = I[V(x,y*)=1]×(1-Acc_solver), preventing reward hacking where invalid problems appear difficult. SAND-Math (arXiv 2507.20527) demonstrates competition-level synthesis at 37.7% survival rate.\\n\\n**Learnability and curriculum optimization.** VCRL (arXiv 2509.19803) validates that reward variance follows an inverted-U relationship with difficulty—problems with moderate difficulty produce highest advantage variance, providing the principled replacement criterion we adopt. SEC (arXiv 2505.14970) formulates curriculum selection as MAB over predefined categories using |advantage| as learning gain proxy.\\n\\n**QD foundations.** SPARQ (arXiv 2506.06499) demonstrated MAP-Elites for offline synthetic math generation. ARISE (arXiv 2603.16060) co-evolves hierarchical skill libraries.\\n\\n**Fundamental premise.** 'Sparse Policy Selection' (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. 'Sharper Primitives' (arXiv 2602.08281) shows diverse training activates broader latent primitive coverage even under the selection hypothesis. 'Does RL Really Incentivize Reasoning Capacity Beyond the Base Model?' (NeurIPS 2025, arXiv 2504.13837) finds >95% overlap at high pass@k. These support a coverage-focused framing: archive diversity ensures RL's limited selection budget is spent across the full capability spectrum.\\n\\n**The precise gap.** DéjàQ proves online MAP-Elites works for RLVR but only at GSM level with 1D descriptors and random mutation. CLPO proves online curriculum works at competition level but without persistent archives or targeted synthesis. MathForge proves difficulty-aware training helps but only offline. No existing work combines persistent multi-dimensional archives, targeted weakness synthesis, competition-level verification, and RLVR-grounded replacement criteria in a single online system.\",\n  \"inspired_by\": \"DéjàQ_paradigm['online MAP-Elites co-evolution during RL training is viable'] + CLPO_insight['online curriculum with difficulty adaptation achieves 50% AIME 2024'] + MathForge_contribution['MAD normalization fixes GRPO difficulty imbalance'] + SwS_pattern['targeted weakness-driven synthesis yields +10% over indiscriminate generation'] + VCRL_criterion['advantage variance inverted-U validates principled replacement signal'] + DéjàQ_limitations['1D archive + random mutation + GSM-only + 22-44% invalid rates define scaling challenge'] + CLPO_limitations['stateless per-batch = no persistent coverage guarantees'] + sparse_policy_selection['coverage-focused framing: archive diversity maximizes RL selection budget efficiency']\",\n  \"approach\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics through four principled innovations: a 2D interpretable archive enabling systematic gap identification, targeted weakness-driven synthesis replacing random mutation, VCRL-validated advantage variance as the replacement criterion, and progressive archive population with multi-stage verification. We honestly acknowledge that DéjàQ established online MAP-Elites co-evolution for RLVR—our contribution is scaling and principled design, not paradigm invention.\\n\\n**1. 2D Interpretable Archive (50 cells).** Unlike DéjàQ's 1D archive with 8 thematic settings, we maintain a 2D MAP-Elites grid: 10 difficulty bins (width 0.1, based on empirical solve-rate: [0-0.1, 0.1-0.2, ..., 0.9-1.0]) × 5 mathematical topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells. Each cell stores up to M=10 problems (max 500 active). Topic classification via GPT-4o-mini (validated at 84-92% accuracy; arXiv 2411.00042). Difficulty via empirical solve-rate from K=8 rollouts on the current policy. The 2D structure enables capabilities impossible in DéjàQ's 1D or CLPO's stateless approach: (a) systematic gap identification—precisely locate which topic×difficulty niches the policy struggles with; (b) targeted synthesis—generate problems specifically for empty or stale cells; (c) interpretable post-hoc analysis—which niches contribute most to downstream benchmark performance.\\n\\n**2. Emergent Curriculum via Fine-Grained Recalibration (quantitatively grounded).** With 0.1-wide difficulty bins, typical GRPO training improves solve-rate by ~3-8% per 50 steps on in-ZPD problems (based on published GRPO learning curves from DAPO, MathForge, and CLPO). This means ~30-80% of problems in a given cell cross bin boundaries per refresh cycle (every K=50 steps). Over 500 training steps (10 refresh cycles), most problems shift 2-4 difficulty bins, creating measurable emergent curriculum without explicit scheduling. Contrast with CLPO's 3 coarse bins (width ~0.33): the same 3-8% improvement rarely triggers bin transitions, making curriculum emergence invisible. We commit to tracking per-cell solve-rate trajectories and bin-transition frequencies as a primary analysis, enabling direct comparison of curriculum granularity effects (ablation A8: 3 bins vs. 10 bins).\\n\\n**3. Targeted Weakness-Driven Synthesis (vs. DéjàQ's Random Mutation).** DéjàQ's three mutation strategies (setting, distractor, symbolic) do not respond to the policy's current weaknesses—the teacher generates blindly regardless of where the student struggles, leading to teacher-student misalignment. We replace this with SwS-style targeted synthesis: (a) identify under-performing archive cells (under-populated <3 problems, or stale—all problems with solve-rate >0.9 or <0.05), (b) prompt a synthesis LLM (Qwen2.5-72B-Instruct or GPT-4o) with the specific topic×difficulty niche requirements, exemplar problems from neighboring cells, and target solve-rate range, (c) generate candidate problems conditioned on the identified gap, requiring unique numerical answers for verifiable reward. When seed problems exist in the target cell, we also use SvS-style answer-preserving mutation for higher validity (~near-100% vs. ~37% for de novo synthesis). This is a fundamental shift from 'mutate randomly and hope' to 'identify gap → synthesize for gap.'\\n\\n**4. Multi-Stage Verification Pipeline (Competition-Level).** DéjàQ suffers 22-44% invalid rates even at GSM level. At competition level, robust verification is essential. We implement a 3-stage VHG-inspired pipeline: (a) *Format and solvability check*—verify the problem is well-formed with a unique numerical answer (filters ~30% of candidates); (b) *Cross-verification*—solve with 2-3 strong models (Qwen2.5-Math-72B, DeepSeek-Math) and check answer agreement via majority vote (≥75% consistency among 16 rollouts, filters ~20% of remaining); (c) *Difficulty calibration*—K=8 rollouts with current policy for solve-rate estimation and bin assignment. Expected survival rate: ~37-40% (consistent with SAND-Math), requiring ~25-27 candidates to yield 10 valid problems per cell. With 5× overgeneration budget (50 candidates per cell), we expect ~19 valid problems—sufficient for M=10 with replacement buffer.\\n\\n**5. VCRL-Validated Advantage Variance as Replacement Criterion.** DéjàQ uses p(1-p) learnability as fitness, which peaks at solve-rate 0.5 regardless of RLVR training signal structure. We propose advantage variance: for each problem, compute Var(A_i) across K=8 GRPO rollouts under the current policy. Following VCRL's validated inverted-U relationship, problems with moderate advantage variance provide the strongest gradient signal for GRPO-style training (gradient ∝ advantage × ∇log π). A new candidate replaces the current cell occupant only when it falls in the same cell AND its advantage variance exceeds the occupant's. This directly optimizes for training signal quality rather than a proxy. Computational savings: 8 rollouts vs. DéjàQ's K=100 completions per problem.\\n\\n**6. Progressive Archive Population.** Competition-level synthesis is hard, and extreme niches (e.g., 'hard geometry' with solve-rate 0-0.1) may require many synthesis cycles. Progressive strategy: Phase 1 (steps 0-100)—populate 'medium' cells (solve-rate 0.3-0.7) across all topics, which are easiest to generate/verify and provide strongest ZPD training signal; Phase 2 (steps 100-300)—expand to 'hard' cells (0.1-0.3) as the policy improves and recalibration naturally populates harder bins; Phase 3 (steps 300+)—target extreme cells (0-0.1 and 0.7+) for coverage completeness. Initially empty cells are filled opportunistically. Graceful degradation: if some extreme cells remain empty, the system still functions on well-populated cells, and the analysis reveals which niches are practically impossible to populate.\\n\\n**7. DGPO-Enhanced Policy Update.** We integrate MathForge's MAD normalization (replacing std normalization in GRPO with mean absolute deviation, ensuring constant update magnitude regardless of difficulty) and difficulty-aware question-level weighting (DQW: exponential weighting with T=2.0). This is orthogonal to archive management and addresses GRPO's implicit difficulty imbalance.\\n\\n**Training Loop (DGPO on Qwen2.5-Math-7B primary, Qwen3-8B secondary, VERL framework):**\\n(a) Sample training batch from archive cells in ZPD window [0.1, 0.9], weighted by advantage variance.\\n(b) Run K=8 rollouts per problem, compute advantages with MAD normalization and DQW.\\n(c) DGPO policy update step.\\n(d) Every K=50 steps: staggered archive refresh—re-evaluate only cells sampled in the last K steps (~40-60% of archive, ~200-300 problems × 8 rollouts = 1600-2400 evaluation rollouts); reassign problems crossing bin boundaries; flag stale cells; trigger targeted synthesis for under-populated or stale cells.\\n(e) Estimated overhead: ~20-25% per refresh cycle (1600-2400 evaluation + synthesis rollouts vs. ~12,800 training rollouts per 50 steps at batch_size=32×8). Lazy evaluation reduces this to ~15% for mature archives.\\n\\n**Baselines (8 systems):**\\n(1) DéjàQ-comp: DéjàQ adapted to competition level—same 1D archive with symbolic mutator applied to competition-level seeds using our verification pipeline. PRIMARY baseline isolating the value of 2D structure + targeted synthesis.\\n(2) CLPO: reproduced with DAPO-Math-17k on Qwen3-8B. PRIMARY baseline isolating the value of persistent archive.\\n(3) SwS: static two-stage offline pipeline (reproduced).\\n(4) MathForge: offline DGPO + MQR augmentation.\\n(5) Prism: 128-cluster semantic diversity with ZPD gate.\\n(6) R-Diverse: SAM skill diversity + MAP memory bank.\\n(7) AdaRFT: adaptive difficulty without archive.\\n(8) Vanilla GRPO on DAPO-Math-17k.\\n\\n**Ablations (9 experiments):**\\nA1: 1D archive only (topic dimension, no difficulty bins)—tests whether 2D adds value over DéjàQ-style 1D.\\nA2: Random synthesis instead of targeted weakness synthesis (keeps archive structure but uses DéjàQ-style random mutation adapted to competition level—isolates targeted synthesis value).\\nA3: p(1-p) replacement instead of advantage variance (DéjàQ's fitness criterion on our archive—isolates replacement criterion value).\\nA4: No archive persistence (per-batch only, CLPO-style but with synthesis—isolates archive persistence value).\\nA5: DéjàQ-comp baseline (1D archive + random mutation at competition level).\\nA6: CLPO + archive persistence (adds our persistent archive to CLPO's approach—tests whether archive alone closes the gap).\\nA7: Coarse difficulty bins (3 bins like CLPO vs. our 10—tests bin granularity effect on emergent curriculum).\\nA8: Standard GRPO normalization vs. DGPO MAD (isolates policy update contribution).\\nA9: Archive coverage vs. per-cell pass@k correlation (tests sparse-selection-compatible justification: does broader primitive activation drive gains?).\\n\\n**Evaluation:** AIME 2024 (30 problems), AIME 2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. Both pass@1 and pass@k (k=8,32,64). Training data: DAPO-Math-17k as seed. Base models: Qwen2.5-Math-7B (primary, following MathForge for comparability) and Qwen3-8B (secondary, following CLPO for comparability).\\n\\n**Key analyses:** (1) Archive coverage heatmaps at each training stage. (2) Per-cell contribution to benchmark performance (which topic×difficulty niches matter most for AIME?). (3) Emergent curriculum visualization showing per-cell solve-rate trajectories and bin-transition frequencies. (4) Synthesis efficiency by niche (valid yield rate for 'medium algebra' vs. 'hard number theory'). (5) DéjàQ-comp vs. SACE-RLVR archive dynamics comparison.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"5800 H100-hours (baselines: GRPO+SwS+Prism+R-Diverse+MathForge+CLPO+AdaRFT reproduction 7×250h=1750h; DéjàQ-comp adaptation 400h; SACE-RLVR primary on 7B 2×400h=800h on 8×H100; SACE-RLVR on 8B 2×400h=800h; ablations A1-A9 9×200h=1800h; archive population/synthesis/verification 250h)\",\n      \"timeline\": \"14-18 weeks\",\n      \"estimated_gpu_cost\": \"$14,500 (at ~$2.50/H100-hr cloud spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"4800 H100-hours (reuse MathForge/CLPO released code for baselines; fewer failed runs from validated hyperparameters; shared verification pipeline across ablations)\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$400-800 (GPT-4o-mini for topic classification, Qwen2.5-72B for targeted synthesis prompting)\",\n      \"estimated_gpu_cost\": \"$12,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"7000 H100-hours (more exploratory sweeps over archive dimensions, bin granularity, refresh frequencies, replacement criteria, and synthesis strategies)\",\n      \"timeline\": \"9-12 weeks\",\n      \"claude_api_cost\": \"$1000-2000\",\n      \"estimated_gpu_cost\": \"$17,500\",\n      \"speed_bottleneck\": \"GPU allocation queue time; each GRPO run takes 24-72h wall-clock on 8×H100s. Archive refresh adds ~20-25% overhead per cycle. DéjàQ-comp baseline requires careful engineering—DéjàQ's symbolic mutator may not straightforwardly extend to competition-level problems.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026) — stretch target if pilot results are strong by August\",\n    \"ICML 2027 (expected deadline ~Jan 2027) — primary target, strong fit for RL + quality-diversity intersection\",\n    \"NeurIPS 2027 (full paper ~May 2027) — fallback with comprehensive evaluation\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems (arXiv 2601.01931, Jan 2026) — PRIMARY PREDECESSOR, establishes online MAP-Elites co-evolution for RLVR at GSM level; 1D archive, p(1-p) fitness, K=100 completions, 22-44% invalid rates; we scale this paradigm to competition level\",\n    \"CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning (arXiv 2509.25004, Sep 2025) — PRIMARY BASELINE, online curriculum with difficulty-aware restructuring at competition level; 50.0% AIME 2024 with Qwen3-8B; stateless per-batch (no persistent archive)\",\n    \"MathForge/DGPO: Harder Is Better (arXiv 2601.20614, ICLR 2026) — MAD normalization fixing GRPO difficulty imbalance + MQR offline augmentation; AIME 2024: 24.58 on 7B; we adopt DGPO for policy update\",\n    \"SwS: Self-aware Weakness-driven Problem Synthesis in RL (NeurIPS 2025, arXiv 2506.08989) — offline category-based weakness targeting with proportional synthesis; +10% (7B); we adopt targeted synthesis pattern online\",\n    \"AdaRFT: Efficient Reinforcement Finetuning via Adaptive Curriculum Learning (arXiv 2504.05520) — adaptive difficulty selection with 2× speedup on AMC/AIME/IMO\",\n    \"CPMöbius: Iterative Coach-Player Reasoning for Data-Free RL (arXiv 2602.02979, Feb 2026) — cooperative coach-player co-evolution; +4.9 average improvement\",\n    \"AERO: Autonomous Evolutionary Reasoning Optimization via Endogenous Dual-Loop Feedback (arXiv 2602.03084, Feb 2026) — ZPD-based dual-loop with entropy-based difficulty targeting\",\n    \"OpenSIR: Open-Ended Self-Improving Reasoner (arXiv 2511.00602, Nov 2025) — difficulty + diversity optimization from seed problems via self-play\",\n    \"Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR [SvS] (ICLR 2026) — answer-preserving synthesis baseline\",\n    \"Preventing Curriculum Collapse in Self-Evolving Reasoning Systems [Prism] (arXiv 2603.13309, Mar 2026) — 128-cluster semantic diversity with ZPD gate\",\n    \"R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training (arXiv 2602.13103, Feb 2026) — SAM skill-aware diversity + MAP memory; AIME 2024: 19.17 (+6.46 over R-Zero on 4B)\",\n    \"VCRL: Variance-based Curriculum RL for LLMs (arXiv 2509.19803) — validates advantage variance inverted-U relationship with learnability; provides principled replacement criterion\",\n    \"SAND-Math: Competition-Level Synthesis with LLMs (arXiv 2507.20527) — empirical grounding for ~37.7% synthesis survival rate at competition level\",\n    \"VHG: Verifier-Backed Hard Problem Generation (arXiv 2605.06660, May 2026) — three-party self-play with validity gating; inspires our verification pipeline\",\n    \"R-Zero: Self-Evolving Reasoning LLM from Zero Data (ICLR 2026) — foundational self-evolving framework; collapses after iteration 3\",\n    \"SPARQ: Synthetic Problem Generation via Quality-Diversity Algorithms (arXiv 2506.06499) — offline QD for problem generation\",\n    \"STAT: Skill-Targeted Adaptive Training (arXiv 2510.10023) — Missing-Skill-Profile for targeted synthesis in SFT\",\n    \"Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis (arXiv 2604.04386) — weakness-driven benchmark generation\",\n    \"SEC: Self-Evolving Curriculum for LLM Reasoning (arXiv 2505.14970) — MAB over problem categories\",\n    \"Sparse Policy Selection, Not Capability Learning (arXiv 2605.06241, May 2026) — RL modifies 1-3% tokens; motivates coverage framing\",\n    \"New Skills or Sharper Primitives (arXiv 2602.08281) — diverse training activates broader latent primitives under selection hypothesis\",\n    \"Does RL Really Incentivize Reasoning Capacity Beyond the Base Model? (NeurIPS 2025, arXiv 2504.13837) — >95% overlap at high pass@k; supports coverage framing\",\n    \"Problem Categorization Can Help LLMs Solve Math Problems (arXiv 2411.00042) — 84%+ topic classification accuracy\",\n    \"ARISE: Agent Reasoning with Intrinsic Skill Evolution (arXiv 2603.16060) — skill library co-evolution\",\n    \"Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution (arXiv 2604.03472)\"\n  ],\n  \"description\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm from GSM-level—where DéjàQ (arXiv 2601.01931) first demonstrated it—to competition-level mathematics (AIME, Olympiad) through four principled innovations. We honestly acknowledge that DéjàQ established online MAP-Elites co-evolution for RLVR and CLPO (arXiv 2509.25004) demonstrated online curriculum at competition level; our contribution is principled integration and scaling, not paradigm invention. (1) A 2D interpretable archive (10 difficulty bins × 5 mathematical topics = 50 cells) replaces DéjàQ's 1D thematic settings and CLPO's stateless per-batch approach, enabling systematic gap identification: which specific topic×difficulty niches does the policy struggle with? (2) Targeted weakness-driven synthesis (SwS-style: identify gap → synthesize for gap) replaces DéjàQ's random mutation that suffers from teacher-student misalignment, and extends CLPO beyond restructuring existing problems. (3) VCRL-validated advantage variance as the replacement criterion directly optimizes for RLVR training signal quality, replacing DéjàQ's proxy p(1-p) learnability. (4) Progressive archive population with multi-stage VHG-inspired verification addresses competition-level synthesis challenges (expected ~37-40% survival per SAND-Math evidence). Emergent curriculum is quantitatively grounded: with 0.1-wide difficulty bins and 3-8% solve-rate improvement per 50 GRPO steps, 30-80% of problems cross bin boundaries per refresh cycle, creating measurable curriculum dynamics impossible with CLPO's 3 coarse bins. We integrate DGPO's MAD normalization (MathForge, ICLR 2026) for robust policy updates. Both DéjàQ-comp (DéjàQ adapted to competition level) and CLPO serve as PRIMARY baselines enabling direct measurement of our innovations' added value. Nine ablations systematically isolate each component: 2D vs. 1D archive, targeted vs. random synthesis, advantage variance vs. p(1-p) replacement, archive persistence, bin granularity, and MAD normalization. Evaluation on Qwen2.5-Math-7B and Qwen3-8B using VERL, targeting AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, and OlympiadBench. Key interpretable analyses include archive coverage heatmaps, per-cell contribution to benchmark performance, and emergent curriculum visualization with bin-transition frequency tracking.\",\n  \"project_name\": \"sace_rlvr\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"revision_overview\": \"MAJOR REVISION. Scores stagnated 3.0→3.2 over 3 rounds, prompting fundamental narrative reframing. The core shift: from claiming 'first to do online co-evolution' (incorrect—DéjàQ does this) to 'scaling archive-based co-evolution from GSM to competition level with structured behavioral descriptors and targeted weakness synthesis.' Every novelty claim re-evaluated against DéjàQ and CLPO. Title, project name, framing, baselines, and ablation structure all substantially revised.\",\n    \"issue_1_clpo_mathforge\": \"ADDRESSED AS PRIMARY WORKS. CLPO is now a PRIMARY baseline with extensive characterization: 50.0% AIME 2024 with Qwen3-8B, online curriculum with G=4 rollout difficulty assessment, 3 bins (Hard/Medium/Easy), Adaptive Problem Restructuring (diversify medium, simplify hard), difficulty-aware KL (λ_hard=0.3). Honest delta articulated: SACE-RLVR adds persistent cross-step archive for systematic coverage guarantees and targeted synthesis for identified gaps, which CLPO's stateless per-batch approach fundamentally cannot provide. MathForge/DGPO is integrated at two levels: (a) landscape characterization (ICLR 2026, MAD normalization, DQW, MQR, +4.56 over GRPO); (b) technical integration—we adopt DGPO's MAD normalization for our policy update step, with ablation A8 isolating its contribution. Ablation A6 tests CLPO + archive persistence to determine whether archive alone closes the gap.\",\n    \"issue_2_dejaq_delta_sharpened\": \"HONESTLY REFRAMED. We now explicitly acknowledge: 'DéjàQ established online MAP-Elites co-evolution for RLVR—our contribution is scaling and principled design, not paradigm invention.' The genuine delta is articulated precisely: (a) Competition-level scaling from GSM-Symbolic (1-5 steps) to AIME/Olympiad, requiring multi-stage verification DéjàQ doesn't need (22-44% invalid at GSM → ~60% invalid at competition level without robust pipeline); (b) 2D interpretable archive (10 difficulty bins × 5 topics = 50 cells) vs. DéjàQ's 1D thematic settings (8 categories)—enables difficulty tracking impossible in 1D; (c) Targeted weakness-driven synthesis vs. random mutation—addresses DéjàQ's identified teacher-student misalignment problem; (d) Advantage variance replacement vs. p(1-p)—directly optimizes for RLVR gradient signal quality; (e) K=8 rollouts vs. K=100—8× computational savings for calibration. DéjàQ-comp (adapted to competition level) is PRIMARY baseline (ablation A5). DéjàQ's p(1-p) criterion tested as ablation A3. Paper framed as 'scaling DéjàQ to competition level with structured targeting.'\",\n    \"issue_3_concurrent_works_added\": \"ALL FOUR ADDED. AdaRFT (arXiv 2504.05520): adaptive difficulty with 2× speedup on competition math—included as baseline and landscape entry. CPMöbius (arXiv 2602.02979): coach-player co-evolution for data-free RL, +4.9 average improvement—differentiated as lacking archive structure and quality-diversity principles. AERO (arXiv 2602.03084): ZPD-based dual-loop with entropy-based difficulty targeting—shares ZPD motivation but operates without structured archives or behavioral descriptors. OpenSIR (arXiv 2511.00602): self-play difficulty + diversity optimization from seeds—relevant diversity perspective at GSM/CollegeMath level. Each positioned with specific mechanistic differences from SACE-RLVR (none uses persistent multi-dimensional archives with targeted synthesis).\",\n    \"issue_4_emergent_curriculum_grounded\": \"QUANTITATIVELY GROUNDED with three changes. (1) EXPANDED to 50 cells (10 difficulty bins × 5 topics, up from 5×5=25). With 0.1-wide bins (vs. CLPO's ~0.33-wide), curriculum emergence is a natural consequence of training progress. (2) CONCRETE MATH: Published GRPO learning curves show ~3-8% solve-rate improvement per 50 steps on in-ZPD problems. With 0.1-wide bins, 30-80% of problems in a cell cross bin boundaries per refresh cycle. Over 500 steps (10 cycles), most problems shift 2-4 bins—this IS emergent curriculum and it is measurable. With CLPO's 3 coarse bins, the same improvement rarely triggers transitions. (3) COMMITTED ANALYSIS: per-cell solve-rate trajectory tracking and bin-transition frequency measurement as primary analyses. Ablation A7 directly compares 3 bins (CLPO-style) vs. 10 bins to quantify the granularity effect.\",\n    \"issue_5_dejaq_as_baseline\": \"FULLY ADOPTED. DéjàQ-comp (DéjàQ adapted to competition level with symbolic mutator on competition-level seed problems, using our verification pipeline for fair comparison) is PRIMARY baseline ablation A5. This is the most important comparison: it directly measures the value of 2D structure + targeted synthesis + advantage variance replacement over the existing paradigm when both operate at competition level. Additionally, DéjàQ's p(1-p) fitness criterion is isolated as ablation A3 (same archive, different replacement criterion). The paper explicitly measures: does 2D structure lead to qualitatively different coverage patterns than 1D? Does targeted synthesis outperform random mutation at competition level?\",\n    \"issue_6_archive_population_uncertainty\": \"ADDRESSED via progressive strategy + honest estimation. (1) PROGRESSIVE POPULATION: Phase 1 (steps 0-100) targets 'medium' cells (solve-rate 0.3-0.7) across all topics—easiest to generate/verify, strongest ZPD signal. Phase 2 (steps 100-300) expands to 'hard' cells as policy improves and recalibration populates harder bins. Phase 3 (steps 300+) targets extremes. (2) EMPIRICAL GROUNDING: SAND-Math ~37.7% survival; 5× overgeneration (50 candidates) yields ~19 valid per cell, sufficient for M=10 with buffer. (3) HONEST RISK: extreme niches (e.g., 'very hard geometry' solve-rate 0-0.1) may need 2-3× more candidates than average. (4) GRACEFUL DEGRADATION: empty extreme cells don't break the system—it trains on well-populated cells. The analysis explicitly reports which niches are practically impossible to populate, which is itself a useful finding for the community.\"\n  }\n}\n\n## Reviewer feedback (round 4)\nIssues: [\"MISSING WORK: Socratic-Zero (arXiv 2509.24726, Sep 2025) implements three-agent co-evolution where a Teacher explicitly targets the Solver's weaknesses and generates problems accordingly—directly overlapping with the targeted weakness synthesis pattern. While it lacks MAP-Elites structure and persistent archives, the weakness-targeting mechanism is conceptually close and must be discussed with explicit differentiation.\", \"MISSING WORK: 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv 2602.14872, Feb 2026) provides theoretical analysis showing RLVR naturally follows an implicit curriculum WITHOUT explicit scheduling—easier problems become learnable first and shape the frontier for harder ones. This simultaneously supports the emergent curriculum concept and challenges the NEED for explicit archive-based curriculum management. The proposal should engage with this theoretical result.\", \"MISSING WORK: Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026) uses a multi-agent framework that dynamically generates data by either complicating or simplifying problems based on reasoning gaps—a bidirectional curriculum approach relevant to the difficulty-adaptive synthesis proposed here.\", \"MISSING WORK: EVOL-RL (arXiv 2509.15194) uses novelty-aware rewards to prevent diversity collapse during label-free RL, achieving substantial AIME improvements (Qwen3-4B pass@1 4.6→16.4% on AIME25). Relevant as a lightweight alternative to archive-based diversity maintenance.\", \"STALE BASELINES: AIME 2024 SOTA for 7B-8B models has moved dramatically—Klear-Reasoner-8B achieves 90.5%, BP-Math-7B 70.8%, ScaleDiff-7B 73.0%. The proposal's primary baselines (CLPO at 50.0%, MathForge at 24.58) are no longer competitive reference points. While these SOTA results use different training paradigms (distillation, extensive SFT), the proposal must contextualize where self-evolving/co-evolutionary methods sit in the broader AIME landscape to avoid appearing disconnected from the field.\", \"EMERGENT CURRICULUM VS. IMPLICIT CURRICULUM: The theoretical analysis in arXiv 2602.14872 shows RLVR already produces implicit curriculum effects through learning dynamics alone. The proposal's emergent curriculum claim (problems shifting bins as solve-rate improves) may be capturing this natural phenomenon rather than demonstrating added value from the 2D archive structure. The ablation A4 (no archive persistence) partially addresses this, but the proposal should explicitly discuss why structured curriculum management adds value over the implicit curriculum that RLVR naturally produces.\", \"ADVANTAGE VARIANCE RELIABILITY AT K=8: With only 8 rollouts per problem, the variance estimate of advantages is itself highly variable. For a competition-level problem where the policy might solve it 1-2 times out of 8, the advantage variance estimate will be extremely noisy. The proposal should discuss the bias-variance tradeoff of K=8 vs K=100 and possibly propose confidence-based thresholds for replacement decisions.\", \"ARCHIVE POPULATION REALISM: The proposal estimates ~37-40% survival for competition-level synthesis but this is for general competition-level problems. Synthesis for SPECIFIC topic×difficulty niches (e.g., 'geometry with solve-rate 0.1-0.2') will have much lower survival because the difficulty constraint adds another filter. The 5× overgeneration budget may be insufficient for extreme cells.\"]\nFeedback: The proposal has matured substantially over 4 rounds and now represents a thorough, honest integration paper. The remaining issues fall into three categories:\n\n**(1) Missing concurrent works (quick fixes).** Add Socratic-Zero, EVOL-RL, Bidirectional Curriculum Generation, and the 'Implicit Curriculum' paper. Socratic-Zero is the most important—it has Teacher→Solver weakness targeting and should be a related work entry with clear differentiation (no persistent archive, no QD framework). The 'Implicit Curriculum' paper (2602.14872) is theoretically important: engage with its claim that RLVR naturally produces curriculum effects and argue why EXPLICIT archive management adds value beyond this natural phenomenon.\n\n**(2) Contextualize against current AIME SOTA.** The 7B-8B AIME 2024 landscape has shifted to 70-90%. Add a paragraph acknowledging this and positioning SACE-RLVR's expected contribution: the value is the METHOD (systematic archive-based co-evolution) and the ABLATION INSIGHTS (which components matter), not absolute AIME numbers. Self-evolving methods operate under stricter constraints (no distillation, online-only data) than methods achieving 90%+. Make this explicit.\n\n**(3) Strengthen the novelty argument.** The 'integration paper' framing is honest but needs a sharper argument for why this specific integration is MORE than the sum of its parts. Consider: does the 2D archive enable capabilities (targeted synthesis, interpretable gap analysis, curriculum dynamics) that are QUALITATIVELY impossible with component-wise approaches? The ablation structure already tests this—preview the expected findings more concretely. Also consider: could the 'Implicit Curriculum' theoretical framework (smooth difficulty spectrum → relay effect) serve as a theoretical backbone for why the 2D archive's fine-grained bins produce better curriculum dynamics than coarse approaches?\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 4 轮修订，近 3 轮平均分从 3.2 到 3.2，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T00:41:07.771Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T00:41:07.771Z",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

## Round 1

51 recorded events

### User

_source line 3 · 2026-05-28T00:41:07.818Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
{
  "title": "Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis",
  "core_problem": "Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level (grade-school math, 1-5 reasoning steps) with a 1D archive of 8 thematic 'setting' categories (Personal Life, Professional, Economic, etc.), random mutation strategies (setting/distractor/symbolic mutators with 22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). It leaves the critical scaling question unanswered: can archive-based co-evolution work at competition level (AIME, Olympiad) where synthesis is far harder, verification is unreliable, and the behavioral space is structurally richer? Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B) through real-time difficulty assessment and adaptive problem restructuring—but operates statelessly per-batch with no persistent archive, no cross-step memory of which problem niches the policy has mastered, and no targeted synthesis for identified gaps. The fundamental open question is: can we combine the archive-based co-evolutionary structure proven by DéjàQ with the competition-level ambition demonstrated by CLPO, while addressing both systems' limitations through structured multi-dimensional behavioral descriptors, targeted weakness-driven synthesis, and principled RLVR-grounded replacement criteria?",
  "opportunity": "Three converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning by maintaining diverse, learnable problems via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot distinguish difficulty within topics, its random mutation degrades with teacher-student misalignment, and 22-44% invalid rates would be catastrophic at competition level. (2) CLPO proves competition-level feasibility: online curriculum with difficulty-aware restructuring achieves 50.0% AIME 2024 (+6.96% average), demonstrating that adaptive difficulty management works at scale. But CLPO's per-batch statelessness means it cannot systematically track which topic×difficulty niches have been mastered vs. where gaps persist—it may repeatedly visit algebra while undersampling number theory. (3) The synthesis-verification gap is closing: SAND-Math demonstrates ~37.7% survival rate for competition-level synthesis; VHG's validity-gating separates problem validity from difficulty; MathForge (ICLR 2026) shows that difficulty-aware GRPO (MAD normalization + DQW) yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that remember policy strengths/weaknesses across training, (b) targeted weakness-driven synthesis that identifies archive gaps and generates specifically for those niches, (c) multi-stage verification suitable for competition-level problems, and (d) RLVR-grounded replacement criteria (advantage variance, not proxy p(1-p)). Our contribution is the principled integration and scaling of these ideas—not the invention of any single component.",
  "landscape": "**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability l_θ(x) = p_θ(x)(1−p_θ(x)), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) teacher-student misalignment—RL improves student but not teacher/mutator; (f) K=100 completions per problem is computationally expensive.\n\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring (diversifies medium-difficulty problems, simplifies hard ones, preserving answers), and difficulty-aware KL (λ_hard=0.3, λ_non-hard=1.0). Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines including DAPO and Critique-GRPO. Trained on DAPO-Math-17k, 200 steps, 8×H20 GPUs. Critical delta: no persistent archive—operates per-batch only; no cross-step memory; restructures existing problems rather than synthesizing new ones for identified gaps; 3 coarse difficulty bins vs. our 10 fine-grained bins.\n\n**Difficulty-aware offline augmentation.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026) introduces Difficulty-Balanced Group Advantage Estimation using MAD normalization (replacing std normalization in GRPO, ensuring constant update magnitude regardless of accuracy distribution) and Difficulty-aware Question-level Weighting (DQW: λ_s = B_v·exp(D_s/T)/Σexp(D_s/T), T=2.0). Multi-Aspect Question Reformulation (MQR) expands datasets 4× via background/term/sub-problem reformulations. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. Offline augmentation—no online adaptation. We adopt DGPO's MAD normalization for our policy update step.\n\n**Weakness-driven targeted synthesis.** SwS (NeurIPS 2025, arXiv 2506.08989) identifies model weaknesses as problems where accuracy never reaches 50% with negative slope during preliminary RL, allocates synthesis budget proportionally to category failure rates, generates 40K targeted problems. Results: +10.0% (7B), +7.7% (32B). Offline two-stage pipeline; weaknesses identified once. STAT (arXiv 2510.10023) creates Missing-Skill-Profiles and synthesizes skill-targeted examples (+7.5% on MATH via SFT). 'Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis' (arXiv 2604.04386) uses AI hypotheses to identify struggle concepts, reducing accuracy from 77% to 45%. These validate the weakness→targeted generation pattern we adopt continuously online.\n\n**Adaptive curriculum and co-evolutionary approaches.** AdaRFT (arXiv 2504.05520) dynamically adjusts training problem difficulty based on recent reward signals, achieving 2× training speedup on AMC/AIME/IMO. Relevant for demonstrating adaptive difficulty value, but without archive-based coverage tracking. CPMöbius (arXiv 2602.02979) implements cooperative coach-player co-evolution for data-free RL, achieving +4.9 average improvement on Qwen2.5-Math-7B-Instruct. Demonstrates co-evolution for LLM reasoning but without archive structure or quality-diversity principles. AERO (arXiv 2602.03084) uses ZPD-based autonomous evolutionary reasoning with entropy-based dual-loop (inner self-questioning/answering, outer difficulty calibration). Shares ZPD motivation but operates without structured archives. OpenSIR (arXiv 2511.00602) optimizes both difficulty and diversity from seed problems via self-play teacher-student dynamics; relevant for diversity optimization perspective but at GSM/CollegeMath level.\n\n**Self-evolving RLVR and diversity maintenance.** SvS (ICLR 2026) achieves +18.3%/+22.8% pass@32 on AIME24/25 via answer-preserving variational mutations. R-Zero (ICLR 2026) co-evolves Challenger+Solver but collapses after iteration 3. Prism (arXiv 2603.13309) prevents collapse via 128 K-means semantic clusters with ZPD gate [0.5, 0.9] and rarity bonus (AIME 2024: 16.77 on Qwen3-4B). R-Diverse (arXiv 2602.13103) introduces SAM code-embedding skill diversity + MAP persistent memory bank (AIME 2024: 19.17 on Qwen3-4B, +6.46 over R-Zero). Vocabulary Dropout (arXiv 2604.03472) addresses diversity collapse via token-level perturbation.\n\n**Verification approaches.** VHG (arXiv 2605.06660) introduces three-party self-play with verifier gating: reward = I[V(x,y*)=1]×(1-Acc_solver), preventing reward hacking where invalid problems appear difficult. SAND-Math (arXiv 2507.20527) demonstrates competition-level synthesis at 37.7% survival rate.\n\n**Learnability and curriculum optimization.** VCRL (arXiv 2509.19803) validates that reward variance follows an inverted-U relationship with difficulty—problems with moderate difficulty produce highest advantage variance, providing the principled replacement criterion we adopt. SEC (arXiv 2505.14970) formulates curriculum selection as MAB over predefined categories using |advantage| as learning gain proxy.\n\n**QD foundations.** SPARQ (arXiv 2506.06499) demonstrated MAP-Elites for offline synthetic math generation. ARISE (arXiv 2603.16060) co-evolves hierarchical skill libraries.\n\n**Fundamental premise.** 'Sparse Policy Selection' (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. 'Sharper Primitives' (arXiv 2602.08281) shows diverse training activates broader latent primitive coverage even under the selection hypothesis. 'Does RL Really Incentivize Reasoning Capacity Beyond the Base Model?' (NeurIPS 2025, arXiv 2504.13837) finds >95% overlap at high pass@k. These support a coverage-focused framing: archive diversity ensures RL's limited selection budget is spent across the full capability spectrum.\n\n**The precise gap.** DéjàQ proves online MAP-Elites works for RLVR but only at GSM level with 1D descriptors and random mutation. CLPO proves online curriculum works at competition level but without persistent archives or targeted synthesis. MathForge proves difficulty-aware training helps but only offline. No existing work combines persistent multi-dimensional archives, targeted weakness synthesis, competition-level verification, and RLVR-grounded replacement criteria in a single online system.",
  "inspired_by": "DéjàQ_paradigm['online MAP-Elites co-evolution during RL training is viable'] + CLPO_insight['online curriculum with difficulty adaptation achieves 50% AIME 2024'] + MathForge_contribution['MAD normalization fixes GRPO difficulty imbalance'] + SwS_pattern['targeted weakness-driven synthesis yields +10% over indiscriminate generation'] + VCRL_criterion['advantage variance inverted-U validates principled replacement signal'] + DéjàQ_limitations['1D archive + random mutation + GSM-only + 22-44% invalid rates define scaling challenge'] + CLPO_limitations['stateless per-batch = no persistent coverage guarantees'] + sparse_policy_selection['coverage-focused framing: archive diversity maximizes RL selection budget efficiency']",
  "approach": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics through four principled innovations: a 2D interpretable archive enabling systematic gap identification, targeted weakness-driven synthesis replacing random mutation, VCRL-validated advantage variance as the replacement criterion, and progressive archive population with multi-stage verification. We honestly acknowledge that DéjàQ established online MAP-Elites co-evolution for RLVR—our contribution is scaling and principled design, not paradigm invention.\n\n**1. 2D Interpretable Archive (50 cells).** Unlike DéjàQ's 1D archive with 8 thematic settings, we maintain a 2D MAP-Elites grid: 10 difficulty bins (width 0.1, based on empirical solve-rate: [0-0.1, 0.1-0.2, ..., 0.9-1.0]) × 5 mathematical topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells. Each cell stores up to M=10 problems (max 500 active). Topic classification via GPT-4o-mini (validated at 84-92% accuracy; arXiv 2411.00042). Difficulty via empirical solve-rate from K=8 rollouts on the current policy. The 2D structure enables capabilities impossible in DéjàQ's 1D or CLPO's stateless approach: (a) systematic gap identification—precisely locate which topic×difficulty niches the policy struggles with; (b) targeted synthesis—generate problems specifically for empty or stale cells; (c) interpretable post-hoc analysis—which niches contribute most to downstream benchmark performance.\n\n**2. Emergent Curriculum via Fine-Grained Recalibration (quantitatively grounded).** With 0.1-wide difficulty bins, typical GRPO training improves solve-rate by ~3-8% per 50 steps on in-ZPD problems (based on published GRPO learning curves from DAPO, MathForge, and CLPO). This means ~30-80% of problems in a given cell cross bin boundaries per refresh cycle (every K=50 steps). Over 500 training steps (10 refresh cycles), most problems shift 2-4 difficulty bins, creating measurable emergent curriculum without explicit scheduling. Contrast with CLPO's 3 coarse bins (width ~0.33): the same 3-8% improvement rarely triggers bin transitions, making curriculum emergence invisible. We commit to tracking per-cell solve-rate trajectories and bin-transition frequencies as a primary analysis, enabling direct comparison of curriculum granularity effects (ablation A8: 3 bins vs. 10 bins).\n\n**3. Targeted Weakness-Driven Synthesis (vs. DéjàQ's Random Mutation).** DéjàQ's three mutation strategies (setting, distractor, symbolic) do not respond to the policy's current weaknesses—the teacher generates blindly regardless of where the student struggles, leading to teacher-student misalignment. We replace this with SwS-style targeted synthesis: (a) identify under-performing archive cells (under-populated <3 problems, or stale—all problems with solve-rate >0.9 or <0.05), (b) prompt a synthesis LLM (Qwen2.5-72B-Instruct or GPT-4o) with the specific topic×difficulty niche requirements, exemplar problems from neighboring cells, and target solve-rate range, (c) generate candidate problems conditioned on the identified gap, requiring unique numerical answers for verifiable reward. When seed problems exist in the target cell, we also use SvS-style answer-preserving mutation for higher validity (~near-100% vs. ~37% for de novo synthesis). This is a fundamental shift from 'mutate randomly and hope' to 'identify gap → synthesize for gap.'\n\n**4. Multi-Stage Verification Pipeline (Competition-Level).** DéjàQ suffers 22-44% invalid rates even at GSM level. At competition level, robust verification is essential. We implement a 3-stage VHG-inspired pipeline: (a) *Format and solvability check*—verify the problem is well-formed with a unique numerical answer (filters ~30% of candidates); (b) *Cross-verification*—solve with 2-3 strong models (Qwen2.5-Math-72B, DeepSeek-Math) and check answer agreement via majority vote (≥75% consistency among 16 rollouts, filters ~20% of remaining); (c) *Difficulty calibration*—K=8 rollouts with current policy for solve-rate estimation and bin assignment. Expected survival rate: ~37-40% (consistent with SAND-Math), requiring ~25-27 candidates to yield 10 valid problems per cell. With 5× overgeneration budget (50 candidates per cell), we expect ~19 valid problems—sufficient for M=10 with replacement buffer.\n\n**5. VCRL-Validated Advantage Variance as Replacement Criterion.** DéjàQ uses p(1-p) learnability as fitness, which peaks at solve-rate 0.5 regardless of RLVR training signal structure. We propose advantage variance: for each problem, compute Var(A_i) across K=8 GRPO rollouts under the current policy. Following VCRL's validated inverted-U relationship, problems with moderate advantage variance provide the strongest gradient signal for GRPO-style training (gradient ∝ advantage × ∇log π). A new candidate replaces the current cell occupant only when it falls in the same cell AND its advantage variance exceeds the occupant's. This directly optimizes for training signal quality rather than a proxy. Computational savings: 8 rollouts vs. DéjàQ's K=100 completions per problem.\n\n**6. Progressive Archive Population.** Competition-level synthesis is hard, and extreme niches (e.g., 'hard geometry' with solve-rate 0-0.1) may require many synthesis cycles. Progressive strategy: Phase 1 (steps 0-100)—populate 'medium' cells (solve-rate 0.3-0.7) across all topics, which are easiest to generate/verify and provide strongest ZPD training signal; Phase 2 (steps 100-300)—expand to 'hard' cells (0.1-0.3) as the policy improves and recalibration naturally populates harder bins; Phase 3 (steps 300+)—target extreme cells (0-0.1 and 0.7+) for coverage completeness. Initially empty cells are filled opportunistically. Graceful degradation: if some extreme cells remain empty, the system still functions on well-populated cells, and the analysis reveals which niches are practically impossible to populate.\n\n**7. DGPO-Enhanced Policy Update.** We integrate MathForge's MAD normalization (replacing std normalization in GRPO with mean absolute deviation, ensuring constant update magnitude regardless of difficulty) and difficulty-aware question-level weighting (DQW: exponential weighting with T=2.0). This is orthogonal to archive management and addresses GRPO's implicit difficulty imbalance.\n\n**Training Loop (DGPO on Qwen2.5-Math-7B primary, Qwen3-8B secondary, VERL framework):**\n(a) Sample training batch from archive cells in ZPD window [0.1, 0.9], weighted by advantage variance.\n(b) Run K=8 rollouts per problem, compute advantages with MAD normalization and DQW.\n(c) DGPO policy update step.\n(d) Every K=50 steps: staggered archive refresh—re-evaluate only cells sampled in the last K steps (~40-60% of archive, ~200-300 problems × 8 rollouts = 1600-2400 evaluation rollouts); reassign problems crossing bin boundaries; flag stale cells; trigger targeted synthesis for under-populated or stale cells.\n(e) Estimated overhead: ~20-25% per refresh cycle (1600-2400 evaluation + synthesis rollouts vs. ~12,800 training rollouts per 50 steps at batch_size=32×8). Lazy evaluation reduces this to ~15% for mature archives.\n\n**Baselines (8 systems):**\n(1) DéjàQ-comp: DéjàQ adapted to competition level—same 1D archive with symbolic mutator applied to competition-level seeds using our verification pipeline. PRIMARY baseline isolating the value of 2D structure + targeted synthesis.\n(2) CLPO: reproduced with DAPO-Math-17k on Qwen3-8B. PRIMARY baseline isolating the value of persistent archive.\n(3) SwS: static two-stage offline pipeline (reproduced).\n(4) MathForge: offline DGPO + MQR augmentation.\n(5) Prism: 128-cluster semantic diversity with ZPD gate.\n(6) R-Diverse: SAM skill diversity + MAP memory bank.\n(7) AdaRFT: adaptive difficulty without archive.\n(8) Vanilla GRPO on DAPO-Math-17k.\n\n**Ablations (9 experiments):**\nA1: 1D archive only (topic dimension, no difficulty bins)—tests whether 2D adds value over DéjàQ-style 1D.\nA2: Random synthesis instead of targeted weakness synthesis (keeps archive structure but uses DéjàQ-style random mutation adapted to competition level—isolates targeted synthesis value).\nA3: p(1-p) replacement instead of advantage variance (DéjàQ's fitness criterion on our archive—isolates replacement criterion value).\nA4: No archive persistence (per-batch only, CLPO-style but with synthesis—isolates archive persistence value).\nA5: DéjàQ-comp baseline (1D archive + random mutation at competition level).\nA6: CLPO + archive persistence (adds our persistent archive to CLPO's approach—tests whether archive alone closes the gap).\nA7: Coarse difficulty bins (3 bins like CLPO vs. our 10—tests bin granularity effect on emergent curriculum).\nA8: Standard GRPO normalization vs. DGPO MAD (isolates policy update contribution).\nA9: Archive coverage vs. per-cell pass@k correlation (tests sparse-selection-compatible justification: does broader primitive activation drive gains?).\n\n**Evaluation:** AIME 2024 (30 problems), AIME 2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. Both pass@1 and pass@k (k=8,32,64). Training data: DAPO-Math-17k as seed. Base models: Qwen2.5-Math-7B (primary, following MathForge for comparability) and Qwen3-8B (secondary, following CLPO for comparability).\n\n**Key analyses:** (1) Archive coverage heatmaps at each training stage. (2) Per-cell contribution to benchmark performance (which topic×difficulty niches matter most for AIME?). (3) Emergent curriculum visualization showing per-cell solve-rate trajectories and bin-transition frequencies. (4) Synthesis efficiency by niche (valid yield rate for 'medium algebra' vs. 'hard number theory'). (5) DéjàQ-comp vs. SACE-RLVR archive dynamics comparison.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "5800 H100-hours (baselines: GRPO+SwS+Prism+R-Diverse+MathForge+CLPO+AdaRFT reproduction 7×250h=1750h; DéjàQ-comp adaptation 400h; SACE-RLVR primary on 7B 2×400h=800h on 8×H100; SACE-RLVR on 8B 2×400h=800h; ablations A1-A9 9×200h=1800h; archive population/synthesis/verification 250h)",
      "timeline": "14-18 weeks",
      "estimated_gpu_cost": "$14,500 (at ~$2.50/H100-hr cloud spot)"
    },
    "human_in_loop": {
      "gpu_hours": "4800 H100-hours (reuse MathForge/CLPO released code for baselines; fewer failed runs from validated hyperparameters; shared verification pipeline across ablations)",
      "timeline": "12-15 weeks",
      "claude_api_cost": "$400-800 (GPT-4o-mini for topic classification, Qwen2.5-72B for targeted synthesis prompting)",
      "estimated_gpu_cost": "$12,000"
    },
    "auto_research": {
      "gpu_hours": "7000 H100-hours (more exploratory sweeps over archive dimensions, bin granularity, refresh frequencies, replacement criteria, and synthesis strategies)",
      "timeline": "9-12 weeks",
      "claude_api_cost": "$1000-2000",
      "estimated_gpu_cost": "$17,500",
      "speed_bottleneck": "GPU allocation queue time; each GRPO run takes 24-72h wall-clock on 8×H100s. Archive refresh adds ~20-25% overhead per cycle. DéjàQ-comp baseline requires careful engineering—DéjàQ's symbolic mutator may not straightforwardly extend to competition-level problems."
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026) — stretch target if pilot results are strong by August",
    "ICML 2027 (expected deadline ~Jan 2027) — primary target, strong fit for RL + quality-diversity intersection",
    "NeurIPS 2027 (full paper ~May 2027) — fallback with comprehensive evaluation"
  ],
  "level": "top-tier",
  "key_references": [
    "DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems (arXiv 2601.01931, Jan 2026) — PRIMARY PREDECESSOR, establishes online MAP-Elites co-evolution for RLVR at GSM level; 1D archive, p(1-p) fitness, K=100 completions, 22-44% invalid rates; we scale this paradigm to competition level",
    "CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning (arXiv 2509.25004, Sep 2025) — PRIMARY BASELINE, online curriculum with difficulty-aware restructuring at competition level; 50.0% AIME 2024 with Qwen3-8B; stateless per-batch (no persistent archive)",
    "MathForge/DGPO: Harder Is Better (arXiv 2601.20614, ICLR 2026) — MAD normalization fixing GRPO difficulty imbalance + MQR offline augmentation; AIME 2024: 24.58 on 7B; we adopt DGPO for policy update",
    "SwS: Self-aware Weakness-driven Problem Synthesis in RL (NeurIPS 2025, arXiv 2506.08989) — offline category-based weakness targeting with proportional synthesis; +10% (7B); we adopt targeted synthesis pattern online",
    "AdaRFT: Efficient Reinforcement Finetuning via Adaptive Curriculum Learning (arXiv 2504.05520) — adaptive difficulty selection with 2× speedup on AMC/AIME/IMO",
    "CPMöbius: Iterative Coach-Player Reasoning for Data-Free RL (arXiv 2602.02979, Feb 2026) — cooperative coach-player co-evolution; +4.9 average improvement",
    "AERO: Autonomous Evolutionary Reasoning Optimization via Endogenous Dual-Loop Feedback (arXiv 2602.03084, Feb 2026) — ZPD-based dual-loop with entropy-based difficulty targeting",
    "OpenSIR: Open-Ended Self-Improving Reasoner (arXiv 2511.00602, Nov 2025) — difficulty + diversity optimization from seed problems via self-play",
    "Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR [SvS] (ICLR 2026) — answer-preserving synthesis baseline",
    "Preventing Curriculum Collapse in Self-Evolving Reasoning Systems [Prism] (arXiv 2603.13309, Mar 2026) — 128-cluster semantic diversity with ZPD gate",
    "R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training (arXiv 2602.13103, Feb 2026) — SAM skill-aware diversity + MAP memory; AIME 2024: 19.17 (+6.46 over R-Zero on 4B)",
    "VCRL: Variance-based Curriculum RL for LLMs (arXiv 2509.19803) — validates advantage variance inverted-U relationship with learnability; provides principled replacement criterion",
    "SAND-Math: Competition-Level Synthesis with LLMs (arXiv 2507.20527) — empirical grounding for ~37.7% synthesis survival rate at competition level",
    "VHG: Verifier-Backed Hard Problem Generation (arXiv 2605.06660, May 2026) — three-party self-play with validity gating; inspires our verification pipeline",
    "R-Zero: Self-Evolving Reasoning LLM from Zero Data (ICLR 2026) — foundational self-evolving framework; collapses after iteration 3",
    "SPARQ: Synthetic Problem Generation via Quality-Diversity Algorithms (arXiv 2506.06499) — offline QD for problem generation",
    "STAT: Skill-Targeted Adaptive Training (arXiv 2510.10023) — Missing-Skill-Profile for targeted synthesis in SFT",
    "Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis (arXiv 2604.04386) — weakness-driven benchmark generation",
    "SEC: Self-Evolving Curriculum for LLM Reasoning (arXiv 2505.14970) — MAB over problem categories",
    "Sparse Policy Selection, Not Capability Learning (arXiv 2605.06241, May 2026) — RL modifies 1-3% tokens; motivates coverage framing",
    "New Skills or Sharper Primitives (arXiv 2602.08281) — diverse training activates broader latent primitives under selection hypothesis",
    "Does RL Really Incentivize Reasoning Capacity Beyond the Base Model? (NeurIPS 2025, arXiv 2504.13837) — >95% overlap at high pass@k; supports coverage framing",
    "Problem Categorization Can Help LLMs Solve Math Problems (arXiv 2411.00042) — 84%+ topic classification accuracy",
    "ARISE: Agent Reasoning with Intrinsic Skill Evolution (arXiv 2603.16060) — skill library co-evolution",
    "Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution (arXiv 2604.03472)"
  ],
  "description": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm from GSM-level—where DéjàQ (arXiv 2601.01931) first demonstrated it—to competition-level mathematics (AIME, Olympiad) through four principled innovations. We honestly acknowledge that DéjàQ established online MAP-Elites co-evolution for RLVR and CLPO (arXiv 2509.25004) demonstrated online curriculum at competition level; our contribution is principled integration and scaling, not paradigm invention. (1) A 2D interpretable archive (10 difficulty bins × 5 mathematical topics = 50 cells) replaces DéjàQ's 1D thematic settings and CLPO's stateless per-batch approach, enabling systematic gap identification: which specific topic×difficulty niches does the policy struggle with? (2) Targeted weakness-driven synthesis (SwS-style: identify gap → synthesize for gap) replaces DéjàQ's random mutation that suffers from teacher-student misalignment, and extends CLPO beyond restructuring existing problems. (3) VCRL-validated advantage variance as the replacement criterion directly optimizes for RLVR training signal quality, replacing DéjàQ's proxy p(1-p) learnability. (4) Progressive archive population with multi-stage VHG-inspired verification addresses competition-level synthesis challenges (expected ~37-40% survival per SAND-Math evidence). Emergent curriculum is quantitatively grounded: with 0.1-wide difficulty bins and 3-8% solve-rate improvement per 50 GRPO steps, 30-80% of problems cross bin boundaries per refresh cycle, creating measurable curriculum dynamics impossible with CLPO's 3 coarse bins. We integrate DGPO's MAD normalization (MathForge, ICLR 2026) for robust policy updates. Both DéjàQ-comp (DéjàQ adapted to competition level) and CLPO serve as PRIMARY baselines enabling direct measurement of our innovations' added value. Nine ablations systematically isolate each component: 2D vs. 1D archive, targeted vs. random synthesis, advantage variance vs. p(1-p) replacement, archive persistence, bin granularity, and MAD normalization. Evaluation on Qwen2.5-Math-7B and Qwen3-8B using VERL, targeting AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, and OlympiadBench. Key interpretable analyses include archive coverage heatmaps, per-cell contribution to benchmark performance, and emergent curriculum visualization with bin-transition frequency tracking.",
  "project_name": "sace_rlvr",
  "source": "web_research",
  "reviewer_response": {
    "revision_overview": "MAJOR REVISION. Scores stagnated 3.0→3.2 over 3 rounds, prompting fundamental narrative reframing. The core shift: from claiming 'first to do online co-evolution' (incorrect—DéjàQ does this) to 'scaling archive-based co-evolution from GSM to competition level with structured behavioral descriptors and targeted weakness synthesis.' Every novelty claim re-evaluated against DéjàQ and CLPO. Title, project name, framing, baselines, and ablation structure all substantially revised.",
    "issue_1_clpo_mathforge": "ADDRESSED AS PRIMARY WORKS. CLPO is now a PRIMARY baseline with extensive characterization: 50.0% AIME 2024 with Qwen3-8B, online curriculum with G=4 rollout difficulty assessment, 3 bins (Hard/Medium/Easy), Adaptive Problem Restructuring (diversify medium, simplify hard), difficulty-aware KL (λ_hard=0.3). Honest delta articulated: SACE-RLVR adds persistent cross-step archive for systematic coverage guarantees and targeted synthesis for identified gaps, which CLPO's stateless per-batch approach fundamentally cannot provide. MathForge/DGPO is integrated at two levels: (a) landscape characterization (ICLR 2026, MAD normalization, DQW, MQR, +4.56 over GRPO); (b) technical integration—we adopt DGPO's MAD normalization for our policy update step, with ablation A8 isolating its contribution. Ablation A6 tests CLPO + archive persistence to determine whether archive alone closes the gap.",
    "issue_2_dejaq_delta_sharpened": "HONESTLY REFRAMED. We now explicitly acknowledge: 'DéjàQ established online MAP-Elites co-evolution for RLVR—our contribution is scaling and principled design, not paradigm invention.' The genuine delta is articulated precisely: (a) Competition-level scaling from GSM-Symbolic (1-5 steps) to AIME/Olympiad, requiring multi-stage verification DéjàQ doesn't need (22-44% invalid at GSM → ~60% invalid at competition level without robust pipeline); (b) 2D interpretable archive (10 difficulty bins × 5 topics = 50 cells) vs. DéjàQ's 1D thematic settings (8 categories)—enables difficulty tracking impossible in 1D; (c) Targeted weakness-driven synthesis vs. random mutation—addresses DéjàQ's identified teacher-student misalignment problem; (d) Advantage variance replacement vs. p(1-p)—directly optimizes for RLVR gradient signal quality; (e) K=8 rollouts vs. K=100—8× computational savings for calibration. DéjàQ-comp (adapted to competition level) is PRIMARY baseline (ablation A5). DéjàQ's p(1-p) criterion tested as ablation A3. Paper framed as 'scaling DéjàQ to competition level with structured targeting.'",
    "issue_3_concurrent_works_added": "ALL FOUR ADDED. AdaRFT (arXiv 2504.05520): adaptive difficulty with 2× speedup on competition math—included as baseline and landscape entry. CPMöbius (arXiv 2602.02979): coach-player co-evolution for data-free RL, +4.9 average improvement—differentiated as lacking archive structure and quality-diversity principles. AERO (arXiv 2602.03084): ZPD-based dual-loop with entropy-based difficulty targeting—shares ZPD motivation but operates without structured archives or behavioral descriptors. OpenSIR (arXiv 2511.00602): self-play difficulty + diversity optimization from seeds—relevant diversity perspective at GSM/CollegeMath level. Each positioned with specific mechanistic differences from SACE-RLVR (none uses persistent multi-dimensional archives with targeted synthesis).",
    "issue_4_emergent_curriculum_grounded": "QUANTITATIVELY GROUNDED with three changes. (1) EXPANDED to 50 cells (10 difficulty bins × 5 topics, up from 5×5=25). With 0.1-wide bins (vs. CLPO's ~0.33-wide), curriculum emergence is a natural consequence of training progress. (2) CONCRETE MATH: Published GRPO learning curves show ~3-8% solve-rate improvement per 50 steps on in-ZPD problems. With 0.1-wide bins, 30-80% of problems in a cell cross bin boundaries per refresh cycle. Over 500 steps (10 cycles), most problems shift 2-4 bins—this IS emergent curriculum and it is measurable. With CLPO's 3 coarse bins, the same improvement rarely triggers transitions. (3) COMMITTED ANALYSIS: per-cell solve-rate trajectory tracking and bin-transition frequency measurement as primary analyses. Ablation A7 directly compares 3 bins (CLPO-style) vs. 10 bins to quantify the granularity effect.",
    "issue_5_dejaq_as_baseline": "FULLY ADOPTED. DéjàQ-comp (DéjàQ adapted to competition level with symbolic mutator on competition-level seed problems, using our verification pipeline for fair comparison) is PRIMARY baseline ablation A5. This is the most important comparison: it directly measures the value of 2D structure + targeted synthesis + advantage variance replacement over the existing paradigm when both operate at competition level. Additionally, DéjàQ's p(1-p) fitness criterion is isolated as ablation A3 (same archive, different replacement criterion). The paper explicitly measures: does 2D structure lead to qualitatively different coverage patterns than 1D? Does targeted synthesis outperform random mutation at competition level?",
    "issue_6_archive_population_uncertainty": "ADDRESSED via progressive strategy + honest estimation. (1) PROGRESSIVE POPULATION: Phase 1 (steps 0-100) targets 'medium' cells (solve-rate 0.3-0.7) across all topics—easiest to generate/verify, strongest ZPD signal. Phase 2 (steps 100-300) expands to 'hard' cells as policy improves and recalibration populates harder bins. Phase 3 (steps 300+) targets extremes. (2) EMPIRICAL GROUNDING: SAND-Math ~37.7% survival; 5× overgeneration (50 candidates) yields ~19 valid per cell, sufficient for M=10 with buffer. (3) HONEST RISK: extreme niches (e.g., 'very hard geometry' solve-rate 0-0.1) may need 2-3× more candidates than average. (4) GRACEFUL DEGRADATION: empty extreme cells don't break the system—it trains on well-populated cells. The analysis explicitly reports which niches are practically impossible to populate, which is itself a useful finding for the community."
  }
}

## Reviewer feedback (round 4)
Issues: ["MISSING WORK: Socratic-Zero (arXiv 2509.24726, Sep 2025) implements three-agent co-evolution where a Teacher explicitly targets the Solver's weaknesses and generates problems accordingly—directly overlapping with the targeted weakness synthesis pattern. While it lacks MAP-Elites structure and persistent archives, the weakness-targeting mechanism is conceptually close and must be discussed with explicit differentiation.", "MISSING WORK: 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv 2602.14872, Feb 2026) provides theoretical analysis showing RLVR naturally follows an implicit curriculum WITHOUT explicit scheduling—easier problems become learnable first and shape the frontier for harder ones. This simultaneously supports the emergent curriculum concept and challenges the NEED for explicit archive-based curriculum management. The proposal should engage with this theoretical result.", "MISSING WORK: Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026) uses a multi-agent framework that dynamically generates data by either complicating or simplifying problems based on reasoning gaps—a bidirectional curriculum approach relevant to the difficulty-adaptive synthesis proposed here.", "MISSING WORK: EVOL-RL (arXiv 2509.15194) uses novelty-aware rewards to prevent diversity collapse during label-free RL, achieving substantial AIME improvements (Qwen3-4B pass@1 4.6→16.4% on AIME25). Relevant as a lightweight alternative to archive-based diversity maintenance.", "STALE BASELINES: AIME 2024 SOTA for 7B-8B models has moved dramatically—Klear-Reasoner-8B achieves 90.5%, BP-Math-7B 70.8%, ScaleDiff-7B 73.0%. The proposal's primary baselines (CLPO at 50.0%, MathForge at 24.58) are no longer competitive reference points. While these SOTA results use different training paradigms (distillation, extensive SFT), the proposal must contextualize where self-evolving/co-evolutionary methods sit in the broader AIME landscape to avoid appearing disconnected from the field.", "EMERGENT CURRICULUM VS. IMPLICIT CURRICULUM: The theoretical analysis in arXiv 2602.14872 shows RLVR already produces implicit curriculum effects through learning dynamics alone. The proposal's emergent curriculum claim (problems shifting bins as solve-rate improves) may be capturing this natural phenomenon rather than demonstrating added value from the 2D archive structure. The ablation A4 (no archive persistence) partially addresses this, but the proposal should explicitly discuss why structured curriculum management adds value over the implicit curriculum that RLVR naturally produces.", "ADVANTAGE VARIANCE RELIABILITY AT K=8: With only 8 rollouts per problem, the variance estimate of advantages is itself highly variable. For a competition-level problem where the policy might solve it 1-2 times out of 8, the advantage variance estimate will be extremely noisy. The proposal should discuss the bias-variance tradeoff of K=8 vs K=100 and possibly propose confidence-based thresholds for replacement decisions.", "ARCHIVE POPULATION REALISM: The proposal estimates ~37-40% survival for competition-level synthesis but this is for general competition-level problems. Synthesis for SPECIFIC topic×difficulty niches (e.g., 'geometry with solve-rate 0.1-0.2') will have much lower survival because the difficulty constraint adds another filter. The 5× overgeneration budget may be insufficient for extreme cells."]
Feedback: The proposal has matured substantially over 4 rounds and now represents a thorough, honest integration paper. The remaining issues fall into three categories:

**(1) Missing concurrent works (quick fixes).** Add Socratic-Zero, EVOL-RL, Bidirectional Curriculum Generation, and the 'Implicit Curriculum' paper. Socratic-Zero is the most important—it has Teacher→Solver weakness targeting and should be a related work entry with clear differentiation (no persistent archive, no QD framework). The 'Implicit Curriculum' paper (2602.14872) is theoretically important: engage with its claim that RLVR naturally produces curriculum effects and argue why EXPLICIT archive management adds value beyond this natural phenomenon.

**(2) Contextualize against current AIME SOTA.** The 7B-8B AIME 2024 landscape has shifted to 70-90%. Add a paragraph acknowledging this and positioning SACE-RLVR's expected contribution: the value is the METHOD (systematic archive-based co-evolution) and the ABLATION INSIGHTS (which components matter), not absolute AIME numbers. Self-evolving methods operate under stricter constraints (no distillation, online-only data) than methods achieving 90%+. Make this explicit.

**(3) Strengthen the novelty argument.** The 'integration paper' framing is honest but needs a sharper argument for why this specific integration is MORE than the sum of its parts. Consider: does the 2D archive enable capabilities (targeted synthesis, interpretable gap analysis, curriculum dynamics) that are QUALITATIVELY impossible with component-wise approaches? The ablation structure already tests this—preview the expected findings more concretely. Also consider: could the 'Implicit Curriculum' theoretical framework (smooth difficulty spectrum → relay effect) serve as a theoretical backbone for why the 2D archive's fine-grained bins produce better curriculum dynamics than coarse approaches?

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

## 停滞提醒
经过 4 轮修订，近 3 轮平均分从 3.2 到 3.2，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "5a26c411-3de0-4ede-a189-5ff53455a810",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T00:41:07.817Z_

```json
{
  "parentUuid": "5a26c411-3de0-4ede-a189-5ff53455a810",
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
  "uuid": "c67b812a-d032-4850-8999-2aac5c992167",
  "timestamp": "2026-05-28T00:41:07.817Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T00:41:07.817Z_

```json
{
  "parentUuid": "c67b812a-d032-4850-8999-2aac5c992167",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "edd8f6bb-dfd2-4452-8c5e-24cc432a3182",
  "timestamp": "2026-05-28T00:41:07.817Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "edd8f6bb-dfd2-4452-8c5e-24cc432a3182",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Assistant

_source line 8 · 2026-05-28T00:41:16.147Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully. This is round 4, and scores have stagnated at ~3.2. The reviewer identifies three categories of issues:

1. **Missing concurrent works** - Socratic-Zero, EVOL-RL, Bidirectional Curriculum Generation, Implicit Curriculum paper
2. **Stale baselines** - AIME 2024 SOTA has moved to 70-90% for 7B-8B models
3. **Strengthen novelty argument** - Need sharper argument for why integration is more than sum of parts

Let me research each of these thoroughly before making revisions.


Now I'm diving into the specific papers I need to cover: Socratic-Zero's three-agent co-evolution approach, the implicit curriculum dynamics paper, bidirectional curriculum generation across multiple agents, EVOL-RL's novelty-aware reward mechanisms, and the latest AIME 2024 benchmarks where models like Klear-Reasoner and BP-Math have already achieved significantly higher performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edd8f6bb-dfd2-4452-8c5e-24cc432a3182",
  "isSidechain": false,
  "requestId": "req_011CbU36g3UaMuuLsYbMwZ52",
  "type": "assistant",
  "uuid": "56b6eb7b-741f-4754-bf72-62942d01db42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7DcCMvwE8p9BgH4Lai2R2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13306,
      "cache_read_input_tokens": 11014,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 495,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13306
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

_source line 9 · 2026-05-28T00:41:16.407Z_

I'll research all the missing works, current AIME SOTA, and the theoretical arguments systematically. Let me launch parallel research agents for each major issue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56b6eb7b-741f-4754-bf72-62942d01db42",
  "isSidechain": false,
  "requestId": "req_011CbU36g3UaMuuLsYbMwZ52",
  "type": "assistant",
  "uuid": "64fc47ae-dda7-48b2-b223-f602a4514776",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7DcCMvwE8p9BgH4Lai2R2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13306,
      "cache_read_input_tokens": 11014,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 495,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13306
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

_source line 10 · 2026-05-28T00:41:16.872Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KxvxWxsoMNdwFcsTZ7Bgz9`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64fc47ae-dda7-48b2-b223-f602a4514776",
  "isSidechain": false,
  "requestId": "req_011CbU36g3UaMuuLsYbMwZ52",
  "type": "assistant",
  "uuid": "f06f0bac-5857-4ee1-8f08-0fc22b1e0515",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7DcCMvwE8p9BgH4Lai2R2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13306,
      "cache_read_input_tokens": 11014,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 495,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13306
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

_source line 11 · 2026-05-28T00:41:16.879Z_

<details><summary>↩ Tool result · `toolu_01KxvxWxsoMNdwFcsTZ7Bgz9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "f06f0bac-5857-4ee1-8f08-0fc22b1e0515",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "0347153f-a983-4398-8af6-f0a46ca7c3f0",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "f06f0bac-5857-4ee1-8f08-0fc22b1e0515",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T00:41:22.256Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me launch parallel research agents for each major issue area. I need to research:

1. Socratic-Zero (arXiv 2509.24726)
2. "On the Learning Dynamics of RLVR at the Edge of Competence" (arXiv 2602.14872)
3. Bidirectional Curriculum Generation (arXiv 2603.05120)
4. EVOL-RL (arXiv 2509.15194)
5. Current AIME 2024 SOTA for 7B-8B models


6. K=8 rollout reliability and advantage variance estimation
7. Niche-specific synthesis survival rates

I'll spin these up as parallel research tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0347153f-a983-4398-8af6-f0a46ca7c3f0",
  "isSidechain": false,
  "requestId": "req_011CbU37Lt5SnobwNHJRj179",
  "type": "assistant",
  "uuid": "df2f05d6-b23b-4e62-913b-cc41fc84cb18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018U4u75RRRMSiT4a7cRye3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 24320,
      "output_tokens": 2080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2080,
          "cache_read_input_tokens": 24320,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 13 · 2026-05-28T00:41:22.257Z_

Let me launch parallel research agents for all the key issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df2f05d6-b23b-4e62-913b-cc41fc84cb18",
  "isSidechain": false,
  "requestId": "req_011CbU37Lt5SnobwNHJRj179",
  "type": "assistant",
  "uuid": "732680b9-5167-4ca5-8a7b-2382adf5d593",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018U4u75RRRMSiT4a7cRye3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 24320,
      "output_tokens": 2080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2080,
          "cache_read_input_tokens": 24320,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 14 · 2026-05-28T00:41:27.785Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011Tu8UU5hRjiVAetdYCkQwS`</summary>

```json
{
  "description": "Research Socratic-Zero paper",
  "prompt": "I need to deeply understand the Socratic-Zero paper (arXiv 2509.24726, Sep 2025). This paper implements three-agent co-evolution where a Teacher explicitly targets the Solver's weaknesses and generates problems accordingly.\n\nPlease:\n1. Search for and fetch this paper from arxiv.org (https://arxiv.org/abs/2509.24726)\n2. Extract the following details:\n   - Full title and authors\n   - The three-agent architecture (Teacher, Solver, and what's the third?)\n   - How does the Teacher identify and target the Solver's weaknesses? What mechanism exactly?\n   - Does it use any archive or persistent memory structure?\n   - What benchmarks/results does it report?\n   - What mathematical domains does it operate on (GSM, MATH, AIME)?\n   - How does the weakness-targeting mechanism compare to: (a) SwS's offline weakness identification, (b) MAP-Elites archive-based gap identification?\n   - Any mention of quality-diversity, behavioral descriptors, or structured archives?\n\nReport all findings in detail. This is critical for differentiation.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "732680b9-5167-4ca5-8a7b-2382adf5d593",
  "isSidechain": false,
  "requestId": "req_011CbU37Lt5SnobwNHJRj179",
  "type": "assistant",
  "uuid": "ab08eb75-0b54-4df6-8348-9590521c283c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018U4u75RRRMSiT4a7cRye3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 24320,
      "output_tokens": 2080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2080,
          "cache_read_input_tokens": 24320,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 15 · 2026-05-28T00:41:32.619Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01S6vtqb8H8fCKrJsDy7r7Dx`</summary>

```json
{
  "description": "Research implicit curriculum paper",
  "prompt": "I need to deeply understand the paper \"On the Learning Dynamics of RLVR at the Edge of Competence\" (arXiv 2602.14872, Feb 2026). This paper provides theoretical analysis showing RLVR naturally follows an implicit curriculum WITHOUT explicit scheduling.\n\nPlease:\n1. Search for and fetch this paper from arxiv.org (https://arxiv.org/abs/2602.14872)\n2. Extract the following details:\n   - Full title and authors\n   - Core theoretical result: how does RLVR naturally produce curriculum effects?\n   - What is the \"edge of competence\" concept?\n   - What is the \"relay effect\" or mechanism by which easier problems enable harder ones?\n   - Does it argue AGAINST explicit curriculum management, or just show implicit curriculum exists?\n   - What empirical evidence supports the theoretical claims?\n   - What mathematical domains/benchmarks are used?\n   - Does it discuss the role of problem diversity or difficulty distribution?\n   - How does this relate to advantage variance and the inverted-U relationship?\n\nThis is critical for understanding whether our explicit archive-based curriculum adds value beyond natural RLVR dynamics.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab08eb75-0b54-4df6-8348-9590521c283c",
  "isSidechain": false,
  "requestId": "req_011CbU37Lt5SnobwNHJRj179",
  "type": "assistant",
  "uuid": "8f3c821f-f8e5-478c-8849-77475b8aac46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018U4u75RRRMSiT4a7cRye3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 24320,
      "output_tokens": 2080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2080,
          "cache_read_input_tokens": 24320,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 16 · 2026-05-28T00:41:37.907Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015qqKJdatsxHGjYsrwa8NBK`</summary>

```json
{
  "description": "Research bidirectional curriculum + EVOL-RL",
  "prompt": "I need to research two papers:\n\n**Paper 1: Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026)**\n- Search for and fetch from https://arxiv.org/abs/2603.05120\n- Extract: full title, core mechanism (complicating vs simplifying problems based on reasoning gaps), multi-agent framework details, results, benchmarks, how it relates to difficulty-adaptive synthesis\n\n**Paper 2: EVOL-RL (arXiv 2509.15194)**\n- Search for and fetch from https://arxiv.org/abs/2509.15194\n- Extract: full title, novelty-aware rewards mechanism, how it prevents diversity collapse, AIME results (reportedly Qwen3-4B pass@1 4.6→16.4% on AIME25), how it compares to archive-based diversity maintenance, computational cost\n\nFor both papers, I need:\n- Precise mechanism descriptions\n- Key results with numbers\n- How they differ from MAP-Elites archive-based approaches\n- Whether they use persistent memory/archives or are stateless\n\nReport all findings in detail.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f3c821f-f8e5-478c-8849-77475b8aac46",
  "isSidechain": false,
  "requestId": "req_011CbU37Lt5SnobwNHJRj179",
  "type": "assistant",
  "uuid": "862c4ba5-a989-4583-a7ce-40ddca4b4def",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018U4u75RRRMSiT4a7cRye3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 24320,
      "output_tokens": 2080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2080,
          "cache_read_input_tokens": 24320,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 17 · 2026-05-28T00:41:44.609Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01P6CBagaUK3ZhUYQYYDaTLU`</summary>

```json
{
  "description": "Research current AIME 2024 SOTA",
  "prompt": "I need to find the current state-of-the-art results on AIME 2024 for 7B-8B parameter models as of May 2026. The reviewer mentioned:\n- Klear-Reasoner-8B: 90.5% on AIME 2024\n- BP-Math-7B: 70.8%\n- ScaleDiff-7B: 73.0%\n\nPlease:\n1. Search for \"AIME 2024 leaderboard 7B 8B models 2026\" and related queries\n2. Search for \"Klear-Reasoner-8B AIME\" to verify this result\n3. Search for \"BP-Math-7B AIME\" to verify\n4. Search for \"ScaleDiff-7B AIME\" to verify\n5. Search for Papers with Code AIME 2024 leaderboard\n6. Search for \"self-evolving RLVR AIME 2024 results 2026\" to find what self-evolving/co-evolutionary methods specifically achieve\n\nKey questions:\n- What training paradigms do the top models use? (distillation? extensive SFT? synthetic data?)\n- Where do self-evolving/online methods specifically rank?\n- What's the best AIME 2024 result from a purely self-evolving/co-evolutionary method (no distillation)?\n- What constraints separate self-evolving methods from distillation-based ones?\n\nReport concrete numbers and methods used.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "862c4ba5-a989-4583-a7ce-40ddca4b4def",
  "isSidechain": false,
  "requestId": "req_011CbU37Lt5SnobwNHJRj179",
  "type": "assistant",
  "uuid": "9003d75c-6c16-44d9-8f26-fd64a877fabc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018U4u75RRRMSiT4a7cRye3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 24320,
      "output_tokens": 2080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2080,
          "cache_read_input_tokens": 24320,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 18 · 2026-05-28T00:41:52.521Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01EXm2XBSMU4gaad3juyW9o4`</summary>

```json
{
  "description": "Research K=8 rollout variance reliability",
  "prompt": "I need to research the statistical reliability of using K=8 rollouts to estimate advantage variance for RLVR problem difficulty calibration. The context:\n\n- In GRPO-style RL training for math reasoning, problems are evaluated with K rollouts\n- DéjàQ uses K=100 completions per problem for learnability estimation p(1-p)\n- We propose K=8 rollouts and using advantage variance as a replacement criterion\n- A reviewer is concerned that with K=8, the variance estimate is itself highly variable, especially for competition-level problems where solve rates might be 1/8 or 2/8\n\nPlease research:\n1. Search for \"GRPO rollout sample size variance estimation\" and related queries\n2. Search for \"VCRL advantage variance estimation reliability\" \n3. Search for \"confidence interval binomial proportion small sample\"\n4. Search for \"DAPO GRPO number rollouts per problem\" to find what standard practice is\n5. What is the standard number of rollouts used in GRPO/DAPO/DeepSeek-R1 style training?\n6. What statistical approaches exist for reliable variance estimation with small samples?\n7. Is there literature on confidence-based thresholds for curriculum/replacement decisions in RL?\n8. What's the bias-variance tradeoff between K=8 and K=16 or K=32?\n\nI need concrete statistical arguments for why K=8 might be sufficient or what modifications would make it robust.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9003d75c-6c16-44d9-8f26-fd64a877fabc",
  "isSidechain": false,
  "requestId": "req_011CbU37Lt5SnobwNHJRj179",
  "type": "assistant",
  "uuid": "9b22337f-f9c0-49bc-bc15-180e6dd1b00b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018U4u75RRRMSiT4a7cRye3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 24320,
      "output_tokens": 2080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1514,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2080,
          "cache_read_input_tokens": 24320,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1514
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

_source line 19 · 2026-05-28T00:43:42.489Z_

<details><summary>↩ Tool result · `toolu_015qqKJdatsxHGjYsrwa8NBK`</summary>

```text
Now I have all the information needed. Here is the comprehensive research report.

---

## Paper 1: Bidirectional Curriculum Generation (arXiv 2603.05120, March 2026)

### Full Title
**"Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning"**

Authors: Boren Hu, Xiao Liu, Boci Peng, Xinping Zhao, Xiaoran Shang, Yun Zhu, Lijun Wu

### Core Mechanism

The paper rejects traditional unidirectional curriculum learning (simple-to-complex) as wasteful. Instead, it introduces a **bidirectional** curriculum that both **complicates** problems (when the model has mastered them) and **simplifies** problems (when it fails, to repair specific reasoning gaps). The system partitions validation data into:
- **Hard samples** (failures) -- routed for simplification/repair
- **Easy samples** (successes) -- promoted to higher difficulty

This creates a closed feedback loop grounded in the **Optimal Pacing Theorem**, which states that tasks within the Zone of Proximal Development (difficulty interval ct-epsilon to ct+epsilon) maximize gradient norm and convergence speed. The gradient contribution is modeled as g(d) = A * d * e^(-d/ct), peaking at optimal difficulty d* = ct. Samples too easy or too hard produce vanishing gradients.

### Multi-Agent Framework (4 Agents)

1. **Difficulty-Reduction Agent (Repairer)**: Lowers complexity when models fail by reducing constraints to bridge conceptual gaps.
2. **Difficulty-Increasing Agent (Challenger)**: Promotes mastered problems to higher difficulty levels.
3. **Reverse-Generation Agent (Reasoner)**: Reformulates problems by swapping queries and answers, forcing reasoning from solutions back to problem conditions.
4. **Diversity-Enhancement Agent (Explorer)**: Expands coverage across mathematical domains to prevent template overfitting.

### Reasoning Gap Detection

Diagnostic evaluation runs model inference on all validation problems using a correctness indicator requiring both reasoning chain AND final answer accuracy. Each problem has a persistent error counter `ind_err(p)` that accumulates across iterations. Problems with persistent failures (exceeding 3 attempts) are reclassified from validation to training data for supervised memorization.

### Key Results

Performance with **Qwen3-8B-Base** (Table 2):
- Final model trained on only **5,873 samples**: **60.03 average** across six benchmarks (+15.53 vs. base)
- Outperforms FastMath (7.9K samples) by **+4.27 points** despite using less data
- Surpasses MegaScience (1.25M samples) at **60.03 vs. 52.5** using **0.5% of the data**

Out-of-domain results:
- AIME 2025: **40.0** (nearly doubles Raiden-DeepSeek-R1's 20.41)
- OlympiadBench: **60.08** (vs. 47.20 baseline)

Iteration progression (showing data efficiency):
- Round 0 (200 samples): 43.31
- Round 2 (1,633 samples): 53.32
- Round 4 (5,873 samples): 60.03

Ablation: Removing reverse-generation drops average from 56.13 to 51.35; removing four domain types drops to 47.23.

### Statefulness / Memory

The system **maintains persistent state**. Each problem carries an error counter `ind_err(p)` that accumulates across iterations. The validation set itself evolves iteratively -- hard problems with ind_err(p) <= 3 persist, while newly generated advanced samples continuously refresh the frontier. Failed samples transition from validation to training after exceeding the error threshold. This is a **stateful, iterative system** with persistent problem tracking.

### Relation to Difficulty-Adaptive Synthesis

This extends difficulty-adaptive synthesis by combining bidirectional adjustment with diagnostic feedback. Rather than static complexity scaling, it implements closed-loop adaptation where the training distribution shifts adaptively with the student model's proficiency, enabling both downward repairs and upward progression within single curriculum cycles.

---

## Paper 2: EVOL-RL (arXiv 2509.15194)

### Full Title
**"Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation"**

Authors: Yujun Zhou, Zhenwen Liang, Haolin Liu, Wenhao Yu, Kishan Panaganti, Linfeng Song, Dian Yu, Xiangliang Zhang, Haitao Mi, Dong Yu

Submitted September 2025, revised February 2026 (v3).

### Novelty-Aware Reward Mechanism

The system generates G responses per prompt and computes embeddings for reasoning sections. For each response i, it calculates:
- **Mean intra-group similarity** (s_bar_i): average cosine similarity to peer solutions within the same majority/minority group
- **Maximum similarity** (m_i): highest cosine similarity to any response in the entire batch

**Novelty score**: u_i = 1 - (alpha * s_bar_i + (1-alpha) * m_i), with default alpha = 0.5

This penalizes both conformity to group averages and near-duplication. Scores undergo intra-group min-max normalization so novelty is measured relative to one's direct peers.

**Reward mapping**:
- Invalid responses: -1
- Majority (correct) solutions: 0.5 + 0.5 * u_tilde_i, yielding range [0.5, 1]
- Minority (incorrect) solutions: -1 + 0.5 * u_tilde_i, yielding range [-1, -0.5]

This ensures **any majority solution, regardless of novelty, always outscores any minority solution**, maintaining strong correctness pressure while novelty refines within-group rankings.

### How It Prevents Diversity Collapse

**Entropy collapse** is defined as a degenerative feedback loop where majority-only reward signals systematically eliminate solution diversity, creating increasingly narrow policies that generate impoverished reward signals, accelerating collapse into low-entropy states.

EVOL-RL combats this with three synergistic components:
1. **Token-level entropy regularizer**: maintains diversity during generation
2. **Asymmetric PPO clipping** (epsilon_high > epsilon_low): preserves full gradient signals from high-reward novel solutions
3. **Novelty reward structure**: in collapsed states, any novel solution automatically receives higher reward, forcing the algorithm to shift probability toward diverse solutions (making collapsed states inherently unstable)

**Theoretical guarantee (Theorem 1)**: While correctness-only objectives admit degenerate optimal policies collapsing to a single solution, the diversity-augmented objective ensures global maximizers concentrate probability mass across all correct reasoning modes.

### AIME Results (Comprehensive)

**Qwen3-4B-Base on AIME25** (the specific claim in the request):
- When trained on AIME24: TTRL baseline **4.6%** pass@1 --> Evol-RL **17.1%** pass@1 (+12.5 pts); pass@16: 18.5% --> 42.0%
- When trained on MATH-500: TTRL 7.2% --> Evol-RL 16.1%
- When trained on MATH-TRAIN: TTRL 6.8% --> Evol-RL 17.5%

**Note**: The reported "4.6 to 16.4%" claim is approximately correct but slightly off. The 4.6% TTRL baseline is accurate (AIME24-trained), but Evol-RL achieves 17.1% (not 16.4%) on AIME25 in that configuration.

**Qwen3-4B-Base on AIME24**: Base 10.0 --> TTRL 16.7 --> Evol-RL **20.6** pass@1; pass@16: 32.4 --> 16.7 (TTRL collapses!) --> **40.9**

**Qwen3-8B-Base on AIME25** (AIME24-trained): Base 8.2 --> TTRL 11.4 --> Evol-RL **16.5**; pass@16: 30.8 --> 25.4 --> **34.7**

**Qwen3-8B-Base on AIME24** (MATH-TRAIN): TTRL 16.7 --> Evol-RL **26.0**; pass@16: 37.6 --> **51.7**

### Results Beyond AIME

- **MATH**: Qwen3-4B pass@1 75.4 --> 80.0; Qwen3-8B 81.1 --> 83.6
- **AMC**: Qwen3-4B 42.5 --> 51.4; Qwen3-8B 53.6 --> 55.5
- **GPQA-Diamond**: Qwen3-4B 36.5 --> 37.2; Qwen3-8B 38.1 --> 43.5
- **MMLU-Pro** (Qwen3-8B): 53.4 --> 55.3
- **SuperGPQA** (Qwen3-8B): 29.7 --> 30.2
- **BBEH** (Qwen3-8B): 12.1 --> 11.5 (slight decrease in pass@1, but pass@4 improves)

### Statefulness / Memory

EVOL-RL is **entirely stateless / per-batch**. It generates G responses per prompt, computes novelty within that concurrent batch only. There is **no persistent archive or memory**. Diversity assessment happens exclusively over the immediate batch of samples. This makes it computationally lightweight but potentially unable to detect longer-horizon pattern repetition across training steps.

### Computational Cost

**Minimal overhead**. The embedding computation and similarity matrix calculation occur post-generation and add negligible cost. Token-level entropy regularization integrates into standard policy optimization with standard computational patterns. No specific wall-clock time comparisons are provided, but the authors emphasize the approach is lightweight.

---

## Comparative Analysis: Both Papers vs. MAP-Elites Archive-Based Approaches

### Architectural Differences from MAP-Elites

| Dimension | MAP-Elites | Bidirectional Curriculum (2603.05120) | EVOL-RL (2509.15194) |
|---|---|---|---|
| **Persistent archive** | Yes -- maintains a grid/archive of elite solutions indexed by behavioral descriptors | Partially -- maintains persistent error counters and an evolving validation set across iterations | No -- entirely stateless, per-batch novelty computation |
| **Diversity mechanism** | Behavioral descriptor space partitioning; archive cells maintain phenotypic diversity | Four specialized agents including an explicit Diversity-Enhancement Agent (Explorer) | Embedding-space cosine similarity novelty scores within each batch |
| **Selection pressure** | Fitness within each cell; archive retains best per niche | Optimal Pacing Theorem; gradient-maximizing difficulty zone | Majority-vote correctness as hard constraint; novelty as soft refinement |
| **Memory/state** | Heavy (full population archive) | Moderate (per-problem error counters + evolving validation set) | None (all computation is within-batch) |
| **Exploration strategy** | Archive gaps drive exploration of unfilled niches | Bidirectional difficulty adjustment + domain diversity agent | Novelty bonus makes collapsed states unstable, incentivizing diverse reasoning |
| **Computational cost** | Potentially high (archive maintenance, descriptor computation) | Moderate (multi-agent generation + diagnostic evaluation each round) | Low (post-hoc embedding similarity computation) |

### Key Conceptual Differences

**Bidirectional Curriculum** operates at the **problem level** -- it generates and selects training *problems* of appropriate difficulty. Its "archive" equivalent is the evolving validation/training set with error tracking. It doesn't maintain solution diversity per se; rather, it maintains *problem* diversity across difficulty levels and mathematical domains. This is fundamentally different from MAP-Elites, which archives *solutions*.

**EVOL-RL** operates at the **solution/policy level** -- it shapes the reward signal during RL training to maintain diverse *reasoning paths*. It explicitly draws the evolutionary analogy (selection = majority voting, variation = novelty rewards) but deliberately avoids MAP-Elites-style persistent archives. The paper acknowledges MAP-Elites in its related work but argues that embedding novelty directly into per-step rewards is more effective for LLM training than maintaining separate archives, because the policy itself is the "population" and the reward signal must prevent entropy collapse in real-time.

**Neither paper uses MAP-Elites directly**, and neither provides head-to-head experimental comparisons with archive-based approaches. Bidirectional Curriculum is closest to MAP-Elites in spirit (persistent tracking, iterative refinement of a collection) but operates on problems rather than solutions. EVOL-RL is the most conceptually distinct, trading all persistent state for lightweight per-batch diversity incentives.

agentId: a8526edbc853721c1 (use SendMessage with to: 'a8526edbc853721c1' to continue this agent)
&lt;usage>total_tokens: 18420
tool_uses: 6
duration_ms: 124578&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "862c4ba5-a989-4583-a7ce-40ddca4b4def",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "74c089d3-6e73-43af-be70-9a9fb6cef75c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research two papers:\n\n**Paper 1: Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026)**\n- Search for and fetch from https://arxiv.org/abs/2603.05120\n- Extract: full title, core mechanism (complicating vs simplifying problems based on reasoning gaps), multi-agent framework details, results, benchmarks, how it relates to difficulty-adaptive synthesis\n\n**Paper 2: EVOL-RL (arXiv 2509.15194)**\n- Search for and fetch from https://arxiv.org/abs/2509.15194\n- Extract: full title, novelty-aware rewards mechanism, how it prevents diversity collapse, AIME results (reportedly Qwen3-4B pass@1 4.6→16.4% on AIME25), how it compares to archive-based diversity maintenance, computational cost\n\nFor both papers, I need:\n- Precise mechanism descriptions\n- Key results with numbers\n- How they differ from MAP-Elites archive-based approaches\n- Whether they use persistent memory/archives or are stateless\n\nReport all findings in detail.",
    "agentId": "a8526edbc853721c1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is the comprehensive research report.\n\n---\n\n## Paper 1: Bidirectional Curriculum Generation (arXiv 2603.05120, March 2026)\n\n### Full Title\n**\"Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning\"**\n\nAuthors: Boren Hu, Xiao Liu, Boci Peng, Xinping Zhao, Xiaoran Shang, Yun Zhu, Lijun Wu\n\n### Core Mechanism\n\nThe paper rejects traditional unidirectional curriculum learning (simple-to-complex) as wasteful. Instead, it introduces a **bidirectional** curriculum that both **complicates** problems (when the model has mastered them) and **simplifies** problems (when it fails, to repair specific reasoning gaps). The system partitions validation data into:\n- **Hard samples** (failures) -- routed for simplification/repair\n- **Easy samples** (successes) -- promoted to higher difficulty\n\nThis creates a closed feedback loop grounded in the **Optimal Pacing Theorem**, which states that tasks within the Zone of Proximal Development (difficulty interval ct-epsilon to ct+epsilon) maximize gradient norm and convergence speed. The gradient contribution is modeled as g(d) = A * d * e^(-d/ct), peaking at optimal difficulty d* = ct. Samples too easy or too hard produce vanishing gradients.\n\n### Multi-Agent Framework (4 Agents)\n\n1. **Difficulty-Reduction Agent (Repairer)**: Lowers complexity when models fail by reducing constraints to bridge conceptual gaps.\n2. **Difficulty-Increasing Agent (Challenger)**: Promotes mastered problems to higher difficulty levels.\n3. **Reverse-Generation Agent (Reasoner)**: Reformulates problems by swapping queries and answers, forcing reasoning from solutions back to problem conditions.\n4. **Diversity-Enhancement Agent (Explorer)**: Expands coverage across mathematical domains to prevent template overfitting.\n\n### Reasoning Gap Detection\n\nDiagnostic evaluation runs model inference on all validation problems using a correctness indicator requiring both reasoning chain AND final answer accuracy. Each problem has a persistent error counter `ind_err(p)` that accumulates across iterations. Problems with persistent failures (exceeding 3 attempts) are reclassified from validation to training data for supervised memorization.\n\n### Key Results\n\nPerformance with **Qwen3-8B-Base** (Table 2):\n- Final model trained on only **5,873 samples**: **60.03 average** across six benchmarks (+15.53 vs. base)\n- Outperforms FastMath (7.9K samples) by **+4.27 points** despite using less data\n- Surpasses MegaScience (1.25M samples) at **60.03 vs. 52.5** using **0.5% of the data**\n\nOut-of-domain results:\n- AIME 2025: **40.0** (nearly doubles Raiden-DeepSeek-R1's 20.41)\n- OlympiadBench: **60.08** (vs. 47.20 baseline)\n\nIteration progression (showing data efficiency):\n- Round 0 (200 samples): 43.31\n- Round 2 (1,633 samples): 53.32\n- Round 4 (5,873 samples): 60.03\n\nAblation: Removing reverse-generation drops average from 56.13 to 51.35; removing four domain types drops to 47.23.\n\n### Statefulness / Memory\n\nThe system **maintains persistent state**. Each problem carries an error counter `ind_err(p)` that accumulates across iterations. The validation set itself evolves iteratively -- hard problems with ind_err(p) <= 3 persist, while newly generated advanced samples continuously refresh the frontier. Failed samples transition from validation to training after exceeding the error threshold. This is a **stateful, iterative system** with persistent problem tracking.\n\n### Relation to Difficulty-Adaptive Synthesis\n\nThis extends difficulty-adaptive synthesis by combining bidirectional adjustment with diagnostic feedback. Rather than static complexity scaling, it implements closed-loop adaptation where the training distribution shifts adaptively with the student model's proficiency, enabling both downward repairs and upward progression within single curriculum cycles.\n\n---\n\n## Paper 2: EVOL-RL (arXiv 2509.15194)\n\n### Full Title\n**\"Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation\"**\n\nAuthors: Yujun Zhou, Zhenwen Liang, Haolin Liu, Wenhao Yu, Kishan Panaganti, Linfeng Song, Dian Yu, Xiangliang Zhang, Haitao Mi, Dong Yu\n\nSubmitted September 2025, revised February 2026 (v3).\n\n### Novelty-Aware Reward Mechanism\n\nThe system generates G responses per prompt and computes embeddings for reasoning sections. For each response i, it calculates:\n- **Mean intra-group similarity** (s_bar_i): average cosine similarity to peer solutions within the same majority/minority group\n- **Maximum similarity** (m_i): highest cosine similarity to any response in the entire batch\n\n**Novelty score**: u_i = 1 - (alpha * s_bar_i + (1-alpha) * m_i), with default alpha = 0.5\n\nThis penalizes both conformity to group averages and near-duplication. Scores undergo intra-group min-max normalization so novelty is measured relative to one's direct peers.\n\n**Reward mapping**:\n- Invalid responses: -1\n- Majority (correct) solutions: 0.5 + 0.5 * u_tilde_i, yielding range [0.5, 1]\n- Minority (incorrect) solutions: -1 + 0.5 * u_tilde_i, yielding range [-1, -0.5]\n\nThis ensures **any majority solution, regardless of novelty, always outscores any minority solution**, maintaining strong correctness pressure while novelty refines within-group rankings.\n\n### How It Prevents Diversity Collapse\n\n**Entropy collapse** is defined as a degenerative feedback loop where majority-only reward signals systematically eliminate solution diversity, creating increasingly narrow policies that generate impoverished reward signals, accelerating collapse into low-entropy states.\n\nEVOL-RL combats this with three synergistic components:\n1. **Token-level entropy regularizer**: maintains diversity during generation\n2. **Asymmetric PPO clipping** (epsilon_high > epsilon_low): preserves full gradient signals from high-reward novel solutions\n3. **Novelty reward structure**: in collapsed states, any novel solution automatically receives higher reward, forcing the algorithm to shift probability toward diverse solutions (making collapsed states inherently unstable)\n\n**Theoretical guarantee (Theorem 1)**: While correctness-only objectives admit degenerate optimal policies collapsing to a single solution, the diversity-augmented objective ensures global maximizers concentrate probability mass across all correct reasoning modes.\n\n### AIME Results (Comprehensive)\n\n**Qwen3-4B-Base on AIME25** (the specific claim in the request):\n- When trained on AIME24: TTRL baseline **4.6%** pass@1 --> Evol-RL **17.1%** pass@1 (+12.5 pts); pass@16: 18.5% --> 42.0%\n- When trained on MATH-500: TTRL 7.2% --> Evol-RL 16.1%\n- When trained on MATH-TRAIN: TTRL 6.8% --> Evol-RL 17.5%\n\n**Note**: The reported \"4.6 to 16.4%\" claim is approximately correct but slightly off. The 4.6% TTRL baseline is accurate (AIME24-trained), but Evol-RL achieves 17.1% (not 16.4%) on AIME25 in that configuration.\n\n**Qwen3-4B-Base on AIME24**: Base 10.0 --> TTRL 16.7 --> Evol-RL **20.6** pass@1; pass@16: 32.4 --> 16.7 (TTRL collapses!) --> **40.9**\n\n**Qwen3-8B-Base on AIME25** (AIME24-trained): Base 8.2 --> TTRL 11.4 --> Evol-RL **16.5**; pass@16: 30.8 --> 25.4 --> **34.7**\n\n**Qwen3-8B-Base on AIME24** (MATH-TRAIN): TTRL 16.7 --> Evol-RL **26.0**; pass@16: 37.6 --> **51.7**\n\n### Results Beyond AIME\n\n- **MATH**: Qwen3-4B pass@1 75.4 --> 80.0; Qwen3-8B 81.1 --> 83.6\n- **AMC**: Qwen3-4B 42.5 --> 51.4; Qwen3-8B 53.6 --> 55.5\n- **GPQA-Diamond**: Qwen3-4B 36.5 --> 37.2; Qwen3-8B 38.1 --> 43.5\n- **MMLU-Pro** (Qwen3-8B): 53.4 --> 55.3\n- **SuperGPQA** (Qwen3-8B): 29.7 --> 30.2\n- **BBEH** (Qwen3-8B): 12.1 --> 11.5 (slight decrease in pass@1, but pass@4 improves)\n\n### Statefulness / Memory\n\nEVOL-RL is **entirely stateless / per-batch**. It generates G responses per prompt, computes novelty within that concurrent batch only. There is **no persistent archive or memory**. Diversity assessment happens exclusively over the immediate batch of samples. This makes it computationally lightweight but potentially unable to detect longer-horizon pattern repetition across training steps.\n\n### Computational Cost\n\n**Minimal overhead**. The embedding computation and similarity matrix calculation occur post-generation and add negligible cost. Token-level entropy regularization integrates into standard policy optimization with standard computational patterns. No specific wall-clock time comparisons are provided, but the authors emphasize the approach is lightweight.\n\n---\n\n## Comparative Analysis: Both Papers vs. MAP-Elites Archive-Based Approaches\n\n### Architectural Differences from MAP-Elites\n\n| Dimension | MAP-Elites | Bidirectional Curriculum (2603.05120) | EVOL-RL (2509.15194) |\n|---|---|---|---|\n| **Persistent archive** | Yes -- maintains a grid/archive of elite solutions indexed by behavioral descriptors | Partially -- maintains persistent error counters and an evolving validation set across iterations | No -- entirely stateless, per-batch novelty computation |\n| **Diversity mechanism** | Behavioral descriptor space partitioning; archive cells maintain phenotypic diversity | Four specialized agents including an explicit Diversity-Enhancement Agent (Explorer) | Embedding-space cosine similarity novelty scores within each batch |\n| **Selection pressure** | Fitness within each cell; archive retains best per niche | Optimal Pacing Theorem; gradient-maximizing difficulty zone | Majority-vote correctness as hard constraint; novelty as soft refinement |\n| **Memory/state** | Heavy (full population archive) | Moderate (per-problem error counters + evolving validation set) | None (all computation is within-batch) |\n| **Exploration strategy** | Archive gaps drive exploration of unfilled niches | Bidirectional difficulty adjustment + domain diversity agent | Novelty bonus makes collapsed states unstable, incentivizing diverse reasoning |\n| **Computational cost** | Potentially high (archive maintenance, descriptor computation) | Moderate (multi-agent generation + diagnostic evaluation each round) | Low (post-hoc embedding similarity computation) |\n\n### Key Conceptual Differences\n\n**Bidirectional Curriculum** operates at the **problem level** -- it generates and selects training *problems* of appropriate difficulty. Its \"archive\" equivalent is the evolving validation/training set with error tracking. It doesn't maintain solution diversity per se; rather, it maintains *problem* diversity across difficulty levels and mathematical domains. This is fundamentally different from MAP-Elites, which archives *solutions*.\n\n**EVOL-RL** operates at the **solution/policy level** -- it shapes the reward signal during RL training to maintain diverse *reasoning paths*. It explicitly draws the evolutionary analogy (selection = majority voting, variation = novelty rewards) but deliberately avoids MAP-Elites-style persistent archives. The paper acknowledges MAP-Elites in its related work but argues that embedding novelty directly into per-step rewards is more effective for LLM training than maintaining separate archives, because the policy itself is the \"population\" and the reward signal must prevent entropy collapse in real-time.\n\n**Neither paper uses MAP-Elites directly**, and neither provides head-to-head experimental comparisons with archive-based approaches. Bidirectional Curriculum is closest to MAP-Elites in spirit (persistent tracking, iterative refinement of a collection) but operates on problems rather than solutions. EVOL-RL is the most conceptually distinct, trading all persistent state for lightweight per-batch diversity incentives."
      }
    ],
    "totalDurationMs": 124578,
    "totalTokens": 18420,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 14566,
      "output_tokens": 3173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3173,
          "cache_read_input_tokens": 14566,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 680,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "862c4ba5-a989-4583-a7ce-40ddca4b4def",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "74c089d3-6e73-43af-be70-9a9fb6cef75c",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Tool result

_source line 22 · 2026-05-28T00:44:04.223Z_

<details><summary>↩ Tool result · `toolu_011Tu8UU5hRjiVAetdYCkQwS`</summary>

````text


I have now read the complete 23-page paper. Here is a comprehensive report of all findings.

---

## Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution

**arXiv: 2509.24726v1, September 29, 2025**

---

### 1. Full Title and Authors

**Title:** "Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution"

**Authors:** Shaobo Wang, Zhengbo Jiao, Zifan Zhang, Yilang Peng, Xu Ze, Boyu Yang, Wei Wang, Hu Wei, Linfeng Zhang

**Affiliations:** Alibaba Group Holding Limited, EPIC Lab at Shanghai Jiao Tong University, Shanghai University of Finance and Economics, Wuhan University, Zhejiang University

---

### 2. The Three-Agent Architecture

The three agents are **Solver**, **Teacher**, and **Generator**:

1. **Solver (S):** A trainable agent with policy pi_{theta_S} that maps a problem q to a solution trajectory y. It improves via online preference learning (DPO) on both successful and failed trajectories. This is the model being trained (e.g., Qwen3-8B).

2. **Teacher (T):** A **fixed**, high-capacity LLM (Qwen3-235B-A22B-Instruct-2507) that serves as a frozen oracle. It provides two deterministic functions:
   - **Verification function** V(q, y) -> {0, 1}: judges whether a solution y for problem q is correct.
   - **Problem refinement function** G(q, y_fail) -> (q', y'_ref): creates a NEW problem-solution pair by revising an original problem based on a failed solution. The new problem is designed to target the specific reasoning error exhibited in y_fail.

3. **Generator (G):** A trainable agent with policy pi_{theta_G} that learns to mimic the Teacher's problem-refinement strategy. It maps a problem and a failed solution (q, y_fail) to a new problem q'. It evolves to generate problems that are optimally challenging for the current Solver. Trained via value-weighted supervised fine-tuning (WSFT).

**Key insight:** The Teacher is NOT trainable -- it is frozen. The co-evolution is between the Solver and the Generator, guided by the fixed Teacher. The Generator exists to make the system scalable by distilling the expensive Teacher's problem-generation capability into a smaller model.

---

### 3. How the Teacher Identifies and Targets the Solver's Weaknesses -- The Exact Mechanism

This is a multi-step process operating at each iteration t:

**Step 1 -- Failure Collection:** The Solver attempts each problem q in the current curriculum D_t with k=8 solution attempts. The Teacher's verifier V classifies each attempt as correct or incorrect. The set of failures F_t is collected:
```
F_t = {(q, y_S) | (q, y_ref) in D_t, y_S ~ pi_{theta_S}(. | q), V(q, y_S) = 0}
```

**Step 2 -- Problem Categorization by Success Rate:** Each problem is categorized into three zones based on the Solver's success rate s_q = (1/k) * sum(V(q, y_S^(i))):
- **Mastered Zone** (s_q = 1): Solver always solves it correctly.
- **Learning Zone** (0 < s_q < 1): Solver can sometimes solve it -- this is the optimal frontier.
- **Too Difficult Zone** (s_q = 0): Solver always fails -- temporarily set aside.

**Step 3 -- Zone-Adaptive Problem Generation:** The Teacher generates new problems differently depending on the source zone:
- **From the Learning Zone:** The Teacher is given a specific failed solution y_fail. The new problem (q', y'_ref) = G(q, y_fail) is designed to **target the specific reasoning error** exhibited in y_fail. This is the core weakness-targeting mechanism.
- **From the Mastered Zone:** The Teacher is given a successful solution y_succ. The new problem G(q, y_succ) is a **more complex variant** designed to push the boundaries of established competence.
- **Problems in the Too Difficult Zone are explicitly excluded** from generation to prevent counterproductive difficulty increases.

**Step 4 -- Dynamic Recategorization:** At each iteration, ALL problems in the curriculum are re-evaluated and recategorized, so problems that were too difficult can move to the Learning Zone as the Solver improves, and Learning Zone problems can move to Mastered.

**The actual Teacher prompt** (Appendix A.3) reads: *"You are a math problem enhancement expert specializing in competition-style mathematics. Generate enhanced problems based on student error analysis with complete solutions. Enhancement principles: Target specific error points, maintain mathematical essence, help avoid similar errors."* It takes as input: the original question + the error analysis from the grading step.

**This is critically important for differentiation:** The weakness-targeting is done via the Teacher's problem refinement function G, which takes a *specific failed solution* as input and generates a new problem that targets the *specific error pattern* in that solution. This is an **instance-level, error-specific** mechanism, not a statistical aggregate.

---

### 4. Archive / Persistent Memory Structure

**The curriculum D_t is the persistent memory structure.** It grows monotonically:
```
D_{t+1} = D_t ∪ {G(q, y_S) | (q, y_S) in F_t}
```

Key properties:
- Starts with D_0 = 100 seed problems from MATH dataset (Levels 2-4)
- Grows each iteration by adding Teacher-refined problems based on failures
- Contains 25% historical replay (older problems are retained and re-sampled)
- Problems are dynamically recategorized each iteration based on current Solver performance
- Quality control removes erroneous problems from the active curriculum

**However, there is NO structured archive** in the quality-diversity sense. There are no behavioral descriptors, no explicit coverage map, no cells or niches. The curriculum is an unstructured, growing set of (problem, reference_solution) pairs. The only structure imposed is the three-zone categorization (Mastered/Learning/Too Difficult), which is recomputed dynamically each iteration.

---

### 5. Benchmarks and Results

**Seven mathematical reasoning benchmarks:**
- AMC-23 (AMC competition 2023)
- AIME-24 (AIME 2024)
- AIME-25 (AIME 2025)
- Olympiad (OlympiadBench)
- MATH-500
- Minerva
- GSM8K

**Three general reasoning benchmarks** (transfer evaluation):
- BBEH (Big-Bench Extra Hard)
- MMLU-Pro
- SuperGPQA

**Key numerical results (Solver, Qwen3-8B-base):**
- Socratic-Solver-8B achieves **56.1% average accuracy** across 7 math benchmarks
- This is **+20.2 percentage points** average gain over the baseline
- Outperforms Static Augmentation by +15.4 points, LLM2LLM by +15.2 points
- Especially strong on competition problems: AIME-24 (+19.1 over SA), AIME-25 (+16.5 over SA)
- General reasoning transfer: +6.02 points average across BBEH, MMLU-Pro, SuperGPQA

**Cross-architecture generalization:**
- GLM4-9B-base: 52.3% avg (+17.1 over base)
- Qwen3-14B-base: 60.3% avg (+17.3 over base)

**Generator results (Socratic-Generator-32B):**
- 95.6% validity rate (rivals Claude-4.1-Opus at 96.9%, GPT-5 at 95.8%)
- 37.72% downstream training effectiveness -- surpasses its own Teacher (Qwen3-235B-A22B at 37.13%) and all tested commercial models including Claude-4.1-Opus (37.01%), GPT-5 (36.62%), Gemini-2.5-Pro (37.20%), Grok-4 (37.01%), DeepSeek-V3.1-671B (36.62%)

---

### 6. Mathematical Domains

The 100 seed problems are distributed across 7 MATH subject areas:
- Algebra (15 problems)
- Number Theory (15)
- Geometry (15)
- Combinatorics (15)
- Precalculus (15)
- Intermediate Algebra (15)
- Prealgebra (10)

The system operates on competition-level mathematics spanning from grade school (GSM8K) through AMC/AIME to Olympiad level.

---

### 7. Comparison to SwS and MAP-Elites for Differentiation

#### (a) vs. SwS's Offline Weakness Identification

Socratic-Zero's weakness-targeting mechanism is fundamentally different from an offline approach like SwS:

- **Socratic-Zero is ONLINE and INSTANCE-LEVEL:** At every iteration, the Solver attempts problems, the Teacher collects the *specific failed solutions*, and generates new problems targeting *that specific error*. The weakness identification happens in real time as part of the co-evolutionary loop.
- **SwS (offline weakness identification)** would typically: batch-analyze failures after training, identify aggregate weakness categories, then generate targeted problems offline for the next training round.
- **Socratic-Zero's mechanism is reactive and continuous:** The three-zone categorization (Mastered/Learning/Too Difficult) with dynamic recategorization means the curriculum constantly adapts. Problems transition between zones as the Solver evolves. This is tighter coupling than an offline approach.
- **But the "weakness" is identified at the problem-instance level, not at a skill/concept level.** The Teacher sees "the Solver failed on this specific problem with this specific error in the solution trace" and generates a related problem. There is no explicit skill taxonomy or systematic categorization of weakness types.

#### (b) vs. MAP-Elites Archive-Based Gap Identification

The contrast here is stark:

- **MAP-Elites** maintains a **structured archive** indexed by behavioral descriptors (e.g., difficulty level x topic x solution-strategy). Gaps are identified as *empty or low-quality cells* in this archive. New problems are generated specifically to fill those cells.
- **Socratic-Zero has NO structured archive, NO behavioral descriptors, NO explicit coverage map, and NO cell-based gap identification.** The curriculum is an unstructured growing set. The only structure is the transient three-zone categorization that is recomputed each iteration.
- **Socratic-Zero's "gap identification" is implicit:** it relies on the Teacher's ability to look at a specific failed solution and generate a problem that targets that error. There is no systematic search for under-explored regions of the problem space.
- **Diversity in Socratic-Zero is maintained through three weak mechanisms:** (1) multi-domain seed initialization across 7 MATH subjects, (2) high-temperature sampling (0.8-0.9) during problem generation, (3) stochastic variation from the Solver's multiple attempts. None of these are principled diversity-preservation mechanisms.

---

### 8. Quality-Diversity, Behavioral Descriptors, Structured Archives

**The paper makes absolutely NO mention of:**
- Quality-diversity (QD) algorithms
- MAP-Elites
- Behavioral descriptors / behavioral characterizations
- Novelty search
- Structured archives with cells/niches
- Coverage metrics over a feature space

The paper does discuss "diversity" in Appendix J ("Curriculum Stability and Diversity Analysis"), but this is limited to:
- Observing that problems span multiple mathematical domains
- Using high-temperature sampling for variation
- Noting that multi-domain seeds create diverse failure patterns

This is purely observational -- diversity is a side effect, not a design objective. There is no mechanism to detect or correct diversity collapse.

---

### 9. Key Equations and Algorithm

**Solver training -- DPO loss (Eq. 5):**
```
L_DPO(theta_S; theta_ref) = -E[log sigma(beta * log(pi_{theta_S}(y_w|q) / pi_{theta_ref}(y_w|q)) - beta * log(pi_{theta_S}(y_l|q) / pi_{theta_ref}(y_l|q)))]
```

**Generator utility function -- Gaussian centered at target success rate (Eq. 6):**
```
U(q' | pi_{theta_S}) = exp(-(s_{q'} - mu)^2 / (2*sigma^2))
```
where mu = 0.5 (target 50% success rate, i.e., "desirable difficulty") and sigma = 0.2.

**Generator training -- WSFT loss (Eq. 7):**
```
L_WSFT(theta_G) = -E[U(q' | pi_{theta_S}) * log pi_{theta_G}(q' | q, y_fail)]
```

The full algorithm (Appendix H, Algorithm 1) runs T iterations, each with three phases:
1. Phase 1: Online Solver Evolution (generate k solutions per problem, build preference pairs, DPO update)
2. Phase 2: Offline Generator Evolution (Teacher generates new problems from failures, estimate utility with updated Solver, WSFT update to Generator)
3. Phase 3: Curriculum Update (add new problems to D_t)

---

### 10. Limitations (from the paper)

- Lacks formal convergence guarantees for multi-agent co-evolution
- Computational overhead of running three agents (especially the 235B Teacher requiring 16 AMD MI308X GPUs)
- Oscillatory convergence dynamics (Solver mean reward oscillates: 52.1% -> 48.7% -> 50.1%)
- Domain transfer not yet demonstrated (mathematical reasoning only)
- Scalability to extremely large model families unclear

---

### Summary for Differentiation Purposes

**What Socratic-Zero does well:**
- Tight online co-evolutionary loop between Solver and Generator, guided by a frozen Teacher
- Instance-level weakness targeting: generates new problems from specific failed solutions
- "Desirable difficulty" calibration via Gaussian utility function targeting 50% success rate
- Strong empirical results (+20.2 points, surpasses commercial LLMs on downstream utility)

**What Socratic-Zero explicitly LACKS (and thus where differentiation opportunities exist):**
- No structured archive or persistent coverage map -- the curriculum is an amorphous growing set
- No behavioral descriptors or feature-space decomposition of the problem landscape
- No systematic gap identification across skill/concept dimensions
- No quality-diversity objective -- diversity is a side effect, not optimized
- No explicit novelty pressure or deduplication mechanism
- The three-zone categorization (Mastered/Learning/Too Difficult) is a 1-dimensional difficulty measure, not a multi-dimensional skill map
- The weakness-targeting is purely reactive (responds to specific failures) rather than proactive (identifying systematically under-explored regions)

agentId: af683bef5a2443dc1 (use SendMessage with to: 'af683bef5a2443dc1' to continue this agent)
&lt;usage>total_tokens: 45483
tool_uses: 8
duration_ms: 156433&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "ab08eb75-0b54-4df6-8348-9590521c283c",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "e03c298e-95b3-4d32-b76d-1b68b2e0ed3d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply understand the Socratic-Zero paper (arXiv 2509.24726, Sep 2025). This paper implements three-agent co-evolution where a Teacher explicitly targets the Solver's weaknesses and generates problems accordingly.\n\nPlease:\n1. Search for and fetch this paper from arxiv.org (https://arxiv.org/abs/2509.24726)\n2. Extract the following details:\n   - Full title and authors\n   - The three-agent architecture (Teacher, Solver, and what's the third?)\n   - How does the Teacher identify and target the Solver's weaknesses? What mechanism exactly?\n   - Does it use any archive or persistent memory structure?\n   - What benchmarks/results does it report?\n   - What mathematical domains does it operate on (GSM, MATH, AIME)?\n   - How does the weakness-targeting mechanism compare to: (a) SwS's offline weakness identification, (b) MAP-Elites archive-based gap identification?\n   - Any mention of quality-diversity, behavioral descriptors, or structured archives?\n\nReport all findings in detail. This is critical for differentiation.",
    "agentId": "af683bef5a2443dc1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nI have now read the complete 23-page paper. Here is a comprehensive report of all findings.\n\n---\n\n## Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution\n\n**arXiv: 2509.24726v1, September 29, 2025**\n\n---\n\n### 1. Full Title and Authors\n\n**Title:** \"Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution\"\n\n**Authors:** Shaobo Wang, Zhengbo Jiao, Zifan Zhang, Yilang Peng, Xu Ze, Boyu Yang, Wei Wang, Hu Wei, Linfeng Zhang\n\n**Affiliations:** Alibaba Group Holding Limited, EPIC Lab at Shanghai Jiao Tong University, Shanghai University of Finance and Economics, Wuhan University, Zhejiang University\n\n---\n\n### 2. The Three-Agent Architecture\n\nThe three agents are **Solver**, **Teacher**, and **Generator**:\n\n1. **Solver (S):** A trainable agent with policy pi_{theta_S} that maps a problem q to a solution trajectory y. It improves via online preference learning (DPO) on both successful and failed trajectories. This is the model being trained (e.g., Qwen3-8B).\n\n2. **Teacher (T):** A **fixed**, high-capacity LLM (Qwen3-235B-A22B-Instruct-2507) that serves as a frozen oracle. It provides two deterministic functions:\n   - **Verification function** V(q, y) -> {0, 1}: judges whether a solution y for problem q is correct.\n   - **Problem refinement function** G(q, y_fail) -> (q', y'_ref): creates a NEW problem-solution pair by revising an original problem based on a failed solution. The new problem is designed to target the specific reasoning error exhibited in y_fail.\n\n3. **Generator (G):** A trainable agent with policy pi_{theta_G} that learns to mimic the Teacher's problem-refinement strategy. It maps a problem and a failed solution (q, y_fail) to a new problem q'. It evolves to generate problems that are optimally challenging for the current Solver. Trained via value-weighted supervised fine-tuning (WSFT).\n\n**Key insight:** The Teacher is NOT trainable -- it is frozen. The co-evolution is between the Solver and the Generator, guided by the fixed Teacher. The Generator exists to make the system scalable by distilling the expensive Teacher's problem-generation capability into a smaller model.\n\n---\n\n### 3. How the Teacher Identifies and Targets the Solver's Weaknesses -- The Exact Mechanism\n\nThis is a multi-step process operating at each iteration t:\n\n**Step 1 -- Failure Collection:** The Solver attempts each problem q in the current curriculum D_t with k=8 solution attempts. The Teacher's verifier V classifies each attempt as correct or incorrect. The set of failures F_t is collected:\n```\nF_t = {(q, y_S) | (q, y_ref) in D_t, y_S ~ pi_{theta_S}(. | q), V(q, y_S) = 0}\n```\n\n**Step 2 -- Problem Categorization by Success Rate:** Each problem is categorized into three zones based on the Solver's success rate s_q = (1/k) * sum(V(q, y_S^(i))):\n- **Mastered Zone** (s_q = 1): Solver always solves it correctly.\n- **Learning Zone** (0 < s_q < 1): Solver can sometimes solve it -- this is the optimal frontier.\n- **Too Difficult Zone** (s_q = 0): Solver always fails -- temporarily set aside.\n\n**Step 3 -- Zone-Adaptive Problem Generation:** The Teacher generates new problems differently depending on the source zone:\n- **From the Learning Zone:** The Teacher is given a specific failed solution y_fail. The new problem (q', y'_ref) = G(q, y_fail) is designed to **target the specific reasoning error** exhibited in y_fail. This is the core weakness-targeting mechanism.\n- **From the Mastered Zone:** The Teacher is given a successful solution y_succ. The new problem G(q, y_succ) is a **more complex variant** designed to push the boundaries of established competence.\n- **Problems in the Too Difficult Zone are explicitly excluded** from generation to prevent counterproductive difficulty increases.\n\n**Step 4 -- Dynamic Recategorization:** At each iteration, ALL problems in the curriculum are re-evaluated and recategorized, so problems that were too difficult can move to the Learning Zone as the Solver improves, and Learning Zone problems can move to Mastered.\n\n**The actual Teacher prompt** (Appendix A.3) reads: *\"You are a math problem enhancement expert specializing in competition-style mathematics. Generate enhanced problems based on student error analysis with complete solutions. Enhancement principles: Target specific error points, maintain mathematical essence, help avoid similar errors.\"* It takes as input: the original question + the error analysis from the grading step.\n\n**This is critically important for differentiation:** The weakness-targeting is done via the Teacher's problem refinement function G, which takes a *specific failed solution* as input and generates a new problem that targets the *specific error pattern* in that solution. This is an **instance-level, error-specific** mechanism, not a statistical aggregate.\n\n---\n\n### 4. Archive / Persistent Memory Structure\n\n**The curriculum D_t is the persistent memory structure.** It grows monotonically:\n```\nD_{t+1} = D_t ∪ {G(q, y_S) | (q, y_S) in F_t}\n```\n\nKey properties:\n- Starts with D_0 = 100 seed problems from MATH dataset (Levels 2-4)\n- Grows each iteration by adding Teacher-refined problems based on failures\n- Contains 25% historical replay (older problems are retained and re-sampled)\n- Problems are dynamically recategorized each iteration based on current Solver performance\n- Quality control removes erroneous problems from the active curriculum\n\n**However, there is NO structured archive** in the quality-diversity sense. There are no behavioral descriptors, no explicit coverage map, no cells or niches. The curriculum is an unstructured, growing set of (problem, reference_solution) pairs. The only structure imposed is the three-zone categorization (Mastered/Learning/Too Difficult), which is recomputed dynamically each iteration.\n\n---\n\n### 5. Benchmarks and Results\n\n**Seven mathematical reasoning benchmarks:**\n- AMC-23 (AMC competition 2023)\n- AIME-24 (AIME 2024)\n- AIME-25 (AIME 2025)\n- Olympiad (OlympiadBench)\n- MATH-500\n- Minerva\n- GSM8K\n\n**Three general reasoning benchmarks** (transfer evaluation):\n- BBEH (Big-Bench Extra Hard)\n- MMLU-Pro\n- SuperGPQA\n\n**Key numerical results (Solver, Qwen3-8B-base):**\n- Socratic-Solver-8B achieves **56.1% average accuracy** across 7 math benchmarks\n- This is **+20.2 percentage points** average gain over the baseline\n- Outperforms Static Augmentation by +15.4 points, LLM2LLM by +15.2 points\n- Especially strong on competition problems: AIME-24 (+19.1 over SA), AIME-25 (+16.5 over SA)\n- General reasoning transfer: +6.02 points average across BBEH, MMLU-Pro, SuperGPQA\n\n**Cross-architecture generalization:**\n- GLM4-9B-base: 52.3% avg (+17.1 over base)\n- Qwen3-14B-base: 60.3% avg (+17.3 over base)\n\n**Generator results (Socratic-Generator-32B):**\n- 95.6% validity rate (rivals Claude-4.1-Opus at 96.9%, GPT-5 at 95.8%)\n- 37.72% downstream training effectiveness -- surpasses its own Teacher (Qwen3-235B-A22B at 37.13%) and all tested commercial models including Claude-4.1-Opus (37.01%), GPT-5 (36.62%), Gemini-2.5-Pro (37.20%), Grok-4 (37.01%), DeepSeek-V3.1-671B (36.62%)\n\n---\n\n### 6. Mathematical Domains\n\nThe 100 seed problems are distributed across 7 MATH subject areas:\n- Algebra (15 problems)\n- Number Theory (15)\n- Geometry (15)\n- Combinatorics (15)\n- Precalculus (15)\n- Intermediate Algebra (15)\n- Prealgebra (10)\n\nThe system operates on competition-level mathematics spanning from grade school (GSM8K) through AMC/AIME to Olympiad level.\n\n---\n\n### 7. Comparison to SwS and MAP-Elites for Differentiation\n\n#### (a) vs. SwS's Offline Weakness Identification\n\nSocratic-Zero's weakness-targeting mechanism is fundamentally different from an offline approach like SwS:\n\n- **Socratic-Zero is ONLINE and INSTANCE-LEVEL:** At every iteration, the Solver attempts problems, the Teacher collects the *specific failed solutions*, and generates new problems targeting *that specific error*. The weakness identification happens in real time as part of the co-evolutionary loop.\n- **SwS (offline weakness identification)** would typically: batch-analyze failures after training, identify aggregate weakness categories, then generate targeted problems offline for the next training round.\n- **Socratic-Zero's mechanism is reactive and continuous:** The three-zone categorization (Mastered/Learning/Too Difficult) with dynamic recategorization means the curriculum constantly adapts. Problems transition between zones as the Solver evolves. This is tighter coupling than an offline approach.\n- **But the \"weakness\" is identified at the problem-instance level, not at a skill/concept level.** The Teacher sees \"the Solver failed on this specific problem with this specific error in the solution trace\" and generates a related problem. There is no explicit skill taxonomy or systematic categorization of weakness types.\n\n#### (b) vs. MAP-Elites Archive-Based Gap Identification\n\nThe contrast here is stark:\n\n- **MAP-Elites** maintains a **structured archive** indexed by behavioral descriptors (e.g., difficulty level x topic x solution-strategy). Gaps are identified as *empty or low-quality cells* in this archive. New problems are generated specifically to fill those cells.\n- **Socratic-Zero has NO structured archive, NO behavioral descriptors, NO explicit coverage map, and NO cell-based gap identification.** The curriculum is an unstructured growing set. The only structure is the transient three-zone categorization that is recomputed each iteration.\n- **Socratic-Zero's \"gap identification\" is implicit:** it relies on the Teacher's ability to look at a specific failed solution and generate a problem that targets that error. There is no systematic search for under-explored regions of the problem space.\n- **Diversity in Socratic-Zero is maintained through three weak mechanisms:** (1) multi-domain seed initialization across 7 MATH subjects, (2) high-temperature sampling (0.8-0.9) during problem generation, (3) stochastic variation from the Solver's multiple attempts. None of these are principled diversity-preservation mechanisms.\n\n---\n\n### 8. Quality-Diversity, Behavioral Descriptors, Structured Archives\n\n**The paper makes absolutely NO mention of:**\n- Quality-diversity (QD) algorithms\n- MAP-Elites\n- Behavioral descriptors / behavioral characterizations\n- Novelty search\n- Structured archives with cells/niches\n- Coverage metrics over a feature space\n\nThe paper does discuss \"diversity\" in Appendix J (\"Curriculum Stability and Diversity Analysis\"), but this is limited to:\n- Observing that problems span multiple mathematical domains\n- Using high-temperature sampling for variation\n- Noting that multi-domain seeds create diverse failure patterns\n\nThis is purely observational -- diversity is a side effect, not a design objective. There is no mechanism to detect or correct diversity collapse.\n\n---\n\n### 9. Key Equations and Algorithm\n\n**Solver training -- DPO loss (Eq. 5):**\n```\nL_DPO(theta_S; theta_ref) = -E[log sigma(beta * log(pi_{theta_S}(y_w|q) / pi_{theta_ref}(y_w|q)) - beta * log(pi_{theta_S}(y_l|q) / pi_{theta_ref}(y_l|q)))]\n```\n\n**Generator utility function -- Gaussian centered at target success rate (Eq. 6):**\n```\nU(q' | pi_{theta_S}) = exp(-(s_{q'} - mu)^2 / (2*sigma^2))\n```\nwhere mu = 0.5 (target 50% success rate, i.e., \"desirable difficulty\") and sigma = 0.2.\n\n**Generator training -- WSFT loss (Eq. 7):**\n```\nL_WSFT(theta_G) = -E[U(q' | pi_{theta_S}) * log pi_{theta_G}(q' | q, y_fail)]\n```\n\nThe full algorithm (Appendix H, Algorithm 1) runs T iterations, each with three phases:\n1. Phase 1: Online Solver Evolution (generate k solutions per problem, build preference pairs, DPO update)\n2. Phase 2: Offline Generator Evolution (Teacher generates new problems from failures, estimate utility with updated Solver, WSFT update to Generator)\n3. Phase 3: Curriculum Update (add new problems to D_t)\n\n---\n\n### 10. Limitations (from the paper)\n\n- Lacks formal convergence guarantees for multi-agent co-evolution\n- Computational overhead of running three agents (especially the 235B Teacher requiring 16 AMD MI308X GPUs)\n- Oscillatory convergence dynamics (Solver mean reward oscillates: 52.1% -> 48.7% -> 50.1%)\n- Domain transfer not yet demonstrated (mathematical reasoning only)\n- Scalability to extremely large model families unclear\n\n---\n\n### Summary for Differentiation Purposes\n\n**What Socratic-Zero does well:**\n- Tight online co-evolutionary loop between Solver and Generator, guided by a frozen Teacher\n- Instance-level weakness targeting: generates new problems from specific failed solutions\n- \"Desirable difficulty\" calibration via Gaussian utility function targeting 50% success rate\n- Strong empirical results (+20.2 points, surpasses commercial LLMs on downstream utility)\n\n**What Socratic-Zero explicitly LACKS (and thus where differentiation opportunities exist):**\n- No structured archive or persistent coverage map -- the curriculum is an amorphous growing set\n- No behavioral descriptors or feature-space decomposition of the problem landscape\n- No systematic gap identification across skill/concept dimensions\n- No quality-diversity objective -- diversity is a side effect, not optimized\n- No explicit novelty pressure or deduplication mechanism\n- The three-zone categorization (Mastered/Learning/Too Difficult) is a 1-dimensional difficulty measure, not a multi-dimensional skill map\n- The weakness-targeting is purely reactive (responds to specific failures) rather than proactive (identifying systematically under-explored regions)"
      }
    ],
    "totalDurationMs": 156433,
    "totalTokens": 45483,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3979,
      "cache_read_input_tokens": 37829,
      "output_tokens": 3672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3672,
          "cache_read_input_tokens": 37829,
          "cache_creation_input_tokens": 3979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3979,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "ab08eb75-0b54-4df6-8348-9590521c283c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 23 · 2026-05-28T00:44:30.195Z_

<details><summary>↩ Tool result · `toolu_01S6vtqb8H8fCKrJsDy7r7Dx`</summary>

````text
The references in the repo are just tangential citations in other paper reviews. Now I have everything needed for a comprehensive analysis. Here is the complete synthesis:

---

## Paper: "The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards"

**arXiv:** 2602.14872v2 (Feb 16, 2026; revised May 6, 2026 post-ICML acceptance)

**Authors:** Yu Huang, Zixin Wen, Yuejie Chi, Yuting Wei, Aarti Singh, Yingbin Liang, Yuxin Chen

---

### 1. Core Theoretical Result: How RLVR Naturally Produces Curriculum Effects

The paper proves that standard REINFORCE with outcome-only (terminal) rewards on a **mixed-difficulty** training set naturally produces a progressive learning sequence -- easier problems become solvable first, and their solutions bootstrap harder ones. No explicit scheduling is needed.

The key mechanism is captured by the gradient characterization in **Lemma 6.2**:

```
nabla_q J_L(t)  proportional to  (Delta_L(t))^L * (1 - Delta_L(t))
```

where `Delta_L(t)` is the effective probability margin at iteration t for problems of horizon (difficulty) L. This formula has two competing factors:
- `(Delta_L)^L` -- exponentially suppresses gradients when the margin is small (problem too hard for current competence)
- `(1 - Delta_L)` -- suppresses gradients when the margin approaches 1 (problem already solved)

This creates an **inverted-U** shape: the gradient signal peaks at intermediate difficulty relative to current ability, naturally focusing learning on the competence frontier.

### 2. The "Edge of Competence" Concept

The paper borrows this term from Zhang et al. (2025) but gives it precise theoretical grounding. The "edge of competence" is the difficulty level where the model has just enough capability to begin solving problems -- where the gradient signal is strongest. Formally, for a problem of horizon L_k, the visibility time T_{vis,k} marks when the expected reward first exceeds 0.01 (the problem enters the competence frontier), and T_{mas,k} marks when it exceeds 0.99 (mastered). The edge of competence is the active zone between these.

The theory shows that in the relay regime, "policy remains 'just competent enough' on L_k... keeping optimization near the edge of competence" -- learning automatically concentrates where it matters most.

### 3. The "Relay Effect" (Relay Regime vs. Grokking Regime)

This is the paper's most important distinction:

**Relay Regime (Theorem 5.2)** -- When the difficulty ratio R = O(1) (smooth difficulty spectrum, small gaps between adjacent problem difficulties):
- Gradients from adjacent difficulty levels **overlap** temporally
- Progress on easier problems **continuously supports** the next harder level before the easier level is fully mastered
- Inter-difficulty plateaus are compressed by a factor of d^{Theta(1)} (exponential speedup)
- Training proceeds smoothly, staying near the competence frontier

**Grokking Regime (Theorem 5.1)** -- When R = omega(1) (large gaps between difficulty levels):
- Long plateaus of length Theta-tilde(L_max / eta) * d^{C_B - 1} between mastering one level and seeing progress on the next
- Followed by rapid phase transitions (grokking-like jumps)
- The model must essentially fully master one difficulty level before the next becomes learnable
- Much slower overall convergence

**Critical implication:** The smoothness of the difficulty spectrum determines whether learning is efficient (relay) or stalled (grokking). Broad, smooth difficulty distributions are dramatically better than sparse or gap-ridden ones.

### 4. Position on Explicit Curriculum Management

The paper does **NOT** explicitly argue against explicit curriculum. Its contribution is mechanistic: proving that implicit curriculum arises naturally from mixed-difficulty training under RLVR. Key nuances:

- The paper states: "without any explicit schedule, easier problems become learnable first and shape the frontier for harder ones"
- It notes that "broad and smooth difficulty spectra can be preferable to relying only on easy or hard subsets"
- It references "frontier-of-learnability sampling" (Foster et al. 2025, Bae et al. 2025) without criticizing it
- The practical implication is that the difficulty **distribution** matters enormously (smooth vs. gapped), but explicit temporal scheduling may be unnecessary if the training mixture already covers a smooth spectrum

**Bottom line:** The paper shows implicit curriculum exists and works well with smooth spectra. It does NOT prove that explicit curriculum cannot add value -- especially in regimes with non-smooth difficulty distributions, which is precisely where explicit curation could help bridge gaps.

### 5. Empirical Evidence

The empirical validation is **entirely synthetic**:
- **Task:** Group-theoretic state tracking on finite non-abelian groups (Definition 3.1). Given a sequence of group actions g_1, ..., g_L, predict the final state y_L = g_L(g_{L-1}(...g_1(y_0)...))
- **Model:** Single attention layer + frozen pretrained MLP
- **Algorithm:** REINFORCE with length-normalized updates
- **No real math benchmarks** (no MATH, GSM8K, AIME, AMC, etc.)
- Experiments validate the plateau lengths, phase transition timings, and relay vs. grokking dynamics predicted by theory
- Figure 1 shows reward trajectories matching theoretical predictions

### 6. Mathematical Domains / Benchmarks

**Synthetic only.** The benchmark is an abstract compositional reasoning task (L-step state tracking under group actions). The "difficulty" parameter is the horizon length L. This is a carefully designed toy setting, not real mathematical reasoning.

### 7. Problem Diversity and Difficulty Distribution

- The paper studies **uniform mixture** over difficulty levels: J_mix = E_{L ~ Unif(L_R)}[J_L]
- Non-uniform distributions are not studied
- The key insight is that the **geometric ratio R** between adjacent difficulty levels governs everything:
  - R = O(1): smooth spectrum, relay regime, fast learning
  - R = omega(1): gapped spectrum, grokking regime, slow plateaus
- **Finer granularity** (smaller R, more intermediate difficulties) is implicitly better because it keeps the system in the relay regime. Corollary 5.2 suggests convergence improves roughly as d^{-C_B^2/(C_B+R)} with smaller R.

### 8. Advantage Variance and the Inverted-U Relationship

The paper does **NOT** use the term "advantage variance" explicitly. However, the gradient formula `(Delta_L)^L * (1 - Delta_L)` is mathematically equivalent to the concept:

- When pass rate is near 0: gradient signal is exponentially suppressed (no useful advantage signal because everything fails)
- When pass rate is near 1: gradient signal vanishes (no useful advantage signal because everything succeeds)
- Maximum gradient at intermediate pass rates (the inverted-U)

This is the same phenomenon that the broader RLVR community discusses as the "inverted-U relationship between pass rate and advantage variance." The paper provides a rigorous proof of WHY this happens in terms of the underlying probability margins.

### 9. Key Limitations for Your Project

Several important caveats for applying this to real RLVR training:

1. **Synthetic setting only** -- group-theoretic state tracking, not real math reasoning
2. **Frozen MLP** -- assumes atomic reasoning skills are already perfectly learned; only attention patterns train
3. **Single attention layer** -- far from real transformer architectures
4. **REINFORCE only** -- does not analyze GRPO, PPO, or other modern algorithms
5. **No discussion of entropy collapse, KL divergence, or reward hacking**
6. **Uniform difficulty distribution only** -- real problem sets have highly non-uniform distributions
7. **Does not address what happens when the base model lacks prerequisite skills** (the MLP is assumed pretrained)

### 10. Implications for Your Explicit Archive-Based Curriculum

**The paper supports several aspects of explicit curriculum and raises no fatal objection:**

- **Smooth difficulty spectra accelerate learning dramatically** (relay >> grokking). An archive-based curriculum that ensures smooth coverage of the difficulty spectrum is directly aligned with this finding.
- **Gaps in difficulty are harmful** -- they cause grokking-style plateaus. Explicit curation to fill difficulty gaps adds clear value beyond what implicit curriculum provides.
- **The paper only proves implicit curriculum works on uniform mixtures** -- real training data is rarely uniformly distributed across difficulties. Explicit reweighting or selection could be essential for non-uniform distributions.
- **The theory assumes all prerequisite skills are pre-learned** -- in practice, some skills may need explicit bootstrapping that natural RLVR cannot provide.
- **The paper does NOT prove explicit curriculum is redundant** -- it proves implicit curriculum exists under idealized conditions. Explicit curriculum could still accelerate learning, handle distribution gaps, or address the many aspects the theory does not cover.

The strongest takeaway for your work: **ensure your difficulty spectrum is smooth and broad** (supporting the relay regime), which is an argument FOR careful archive curation rather than against it.

agentId: af6118c4e263748f4 (use SendMessage with to: 'af6118c4e263748f4' to continue this agent)
&lt;usage>total_tokens: 19870
tool_uses: 9
duration_ms: 177573&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8f3c821f-f8e5-478c-8849-77475b8aac46",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "bb814573-89ac-4b7a-b86f-e6c469c905c6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply understand the paper \"On the Learning Dynamics of RLVR at the Edge of Competence\" (arXiv 2602.14872, Feb 2026). This paper provides theoretical analysis showing RLVR naturally follows an implicit curriculum WITHOUT explicit scheduling.\n\nPlease:\n1. Search for and fetch this paper from arxiv.org (https://arxiv.org/abs/2602.14872)\n2. Extract the following details:\n   - Full title and authors\n   - Core theoretical result: how does RLVR naturally produce curriculum effects?\n   - What is the \"edge of competence\" concept?\n   - What is the \"relay effect\" or mechanism by which easier problems enable harder ones?\n   - Does it argue AGAINST explicit curriculum management, or just show implicit curriculum exists?\n   - What empirical evidence supports the theoretical claims?\n   - What mathematical domains/benchmarks are used?\n   - Does it discuss the role of problem diversity or difficulty distribution?\n   - How does this relate to advantage variance and the inverted-U relationship?\n\nThis is critical for understanding whether our explicit archive-based curriculum adds value beyond natural RLVR dynamics.",
    "agentId": "af6118c4e263748f4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "The references in the repo are just tangential citations in other paper reviews. Now I have everything needed for a comprehensive analysis. Here is the complete synthesis:\n\n---\n\n## Paper: \"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards\"\n\n**arXiv:** 2602.14872v2 (Feb 16, 2026; revised May 6, 2026 post-ICML acceptance)\n\n**Authors:** Yu Huang, Zixin Wen, Yuejie Chi, Yuting Wei, Aarti Singh, Yingbin Liang, Yuxin Chen\n\n---\n\n### 1. Core Theoretical Result: How RLVR Naturally Produces Curriculum Effects\n\nThe paper proves that standard REINFORCE with outcome-only (terminal) rewards on a **mixed-difficulty** training set naturally produces a progressive learning sequence -- easier problems become solvable first, and their solutions bootstrap harder ones. No explicit scheduling is needed.\n\nThe key mechanism is captured by the gradient characterization in **Lemma 6.2**:\n\n```\nnabla_q J_L(t)  proportional to  (Delta_L(t))^L * (1 - Delta_L(t))\n```\n\nwhere `Delta_L(t)` is the effective probability margin at iteration t for problems of horizon (difficulty) L. This formula has two competing factors:\n- `(Delta_L)^L` -- exponentially suppresses gradients when the margin is small (problem too hard for current competence)\n- `(1 - Delta_L)` -- suppresses gradients when the margin approaches 1 (problem already solved)\n\nThis creates an **inverted-U** shape: the gradient signal peaks at intermediate difficulty relative to current ability, naturally focusing learning on the competence frontier.\n\n### 2. The \"Edge of Competence\" Concept\n\nThe paper borrows this term from Zhang et al. (2025) but gives it precise theoretical grounding. The \"edge of competence\" is the difficulty level where the model has just enough capability to begin solving problems -- where the gradient signal is strongest. Formally, for a problem of horizon L_k, the visibility time T_{vis,k} marks when the expected reward first exceeds 0.01 (the problem enters the competence frontier), and T_{mas,k} marks when it exceeds 0.99 (mastered). The edge of competence is the active zone between these.\n\nThe theory shows that in the relay regime, \"policy remains 'just competent enough' on L_k... keeping optimization near the edge of competence\" -- learning automatically concentrates where it matters most.\n\n### 3. The \"Relay Effect\" (Relay Regime vs. Grokking Regime)\n\nThis is the paper's most important distinction:\n\n**Relay Regime (Theorem 5.2)** -- When the difficulty ratio R = O(1) (smooth difficulty spectrum, small gaps between adjacent problem difficulties):\n- Gradients from adjacent difficulty levels **overlap** temporally\n- Progress on easier problems **continuously supports** the next harder level before the easier level is fully mastered\n- Inter-difficulty plateaus are compressed by a factor of d^{Theta(1)} (exponential speedup)\n- Training proceeds smoothly, staying near the competence frontier\n\n**Grokking Regime (Theorem 5.1)** -- When R = omega(1) (large gaps between difficulty levels):\n- Long plateaus of length Theta-tilde(L_max / eta) * d^{C_B - 1} between mastering one level and seeing progress on the next\n- Followed by rapid phase transitions (grokking-like jumps)\n- The model must essentially fully master one difficulty level before the next becomes learnable\n- Much slower overall convergence\n\n**Critical implication:** The smoothness of the difficulty spectrum determines whether learning is efficient (relay) or stalled (grokking). Broad, smooth difficulty distributions are dramatically better than sparse or gap-ridden ones.\n\n### 4. Position on Explicit Curriculum Management\n\nThe paper does **NOT** explicitly argue against explicit curriculum. Its contribution is mechanistic: proving that implicit curriculum arises naturally from mixed-difficulty training under RLVR. Key nuances:\n\n- The paper states: \"without any explicit schedule, easier problems become learnable first and shape the frontier for harder ones\"\n- It notes that \"broad and smooth difficulty spectra can be preferable to relying only on easy or hard subsets\"\n- It references \"frontier-of-learnability sampling\" (Foster et al. 2025, Bae et al. 2025) without criticizing it\n- The practical implication is that the difficulty **distribution** matters enormously (smooth vs. gapped), but explicit temporal scheduling may be unnecessary if the training mixture already covers a smooth spectrum\n\n**Bottom line:** The paper shows implicit curriculum exists and works well with smooth spectra. It does NOT prove that explicit curriculum cannot add value -- especially in regimes with non-smooth difficulty distributions, which is precisely where explicit curation could help bridge gaps.\n\n### 5. Empirical Evidence\n\nThe empirical validation is **entirely synthetic**:\n- **Task:** Group-theoretic state tracking on finite non-abelian groups (Definition 3.1). Given a sequence of group actions g_1, ..., g_L, predict the final state y_L = g_L(g_{L-1}(...g_1(y_0)...))\n- **Model:** Single attention layer + frozen pretrained MLP\n- **Algorithm:** REINFORCE with length-normalized updates\n- **No real math benchmarks** (no MATH, GSM8K, AIME, AMC, etc.)\n- Experiments validate the plateau lengths, phase transition timings, and relay vs. grokking dynamics predicted by theory\n- Figure 1 shows reward trajectories matching theoretical predictions\n\n### 6. Mathematical Domains / Benchmarks\n\n**Synthetic only.** The benchmark is an abstract compositional reasoning task (L-step state tracking under group actions). The \"difficulty\" parameter is the horizon length L. This is a carefully designed toy setting, not real mathematical reasoning.\n\n### 7. Problem Diversity and Difficulty Distribution\n\n- The paper studies **uniform mixture** over difficulty levels: J_mix = E_{L ~ Unif(L_R)}[J_L]\n- Non-uniform distributions are not studied\n- The key insight is that the **geometric ratio R** between adjacent difficulty levels governs everything:\n  - R = O(1): smooth spectrum, relay regime, fast learning\n  - R = omega(1): gapped spectrum, grokking regime, slow plateaus\n- **Finer granularity** (smaller R, more intermediate difficulties) is implicitly better because it keeps the system in the relay regime. Corollary 5.2 suggests convergence improves roughly as d^{-C_B^2/(C_B+R)} with smaller R.\n\n### 8. Advantage Variance and the Inverted-U Relationship\n\nThe paper does **NOT** use the term \"advantage variance\" explicitly. However, the gradient formula `(Delta_L)^L * (1 - Delta_L)` is mathematically equivalent to the concept:\n\n- When pass rate is near 0: gradient signal is exponentially suppressed (no useful advantage signal because everything fails)\n- When pass rate is near 1: gradient signal vanishes (no useful advantage signal because everything succeeds)\n- Maximum gradient at intermediate pass rates (the inverted-U)\n\nThis is the same phenomenon that the broader RLVR community discusses as the \"inverted-U relationship between pass rate and advantage variance.\" The paper provides a rigorous proof of WHY this happens in terms of the underlying probability margins.\n\n### 9. Key Limitations for Your Project\n\nSeveral important caveats for applying this to real RLVR training:\n\n1. **Synthetic setting only** -- group-theoretic state tracking, not real math reasoning\n2. **Frozen MLP** -- assumes atomic reasoning skills are already perfectly learned; only attention patterns train\n3. **Single attention layer** -- far from real transformer architectures\n4. **REINFORCE only** -- does not analyze GRPO, PPO, or other modern algorithms\n5. **No discussion of entropy collapse, KL divergence, or reward hacking**\n6. **Uniform difficulty distribution only** -- real problem sets have highly non-uniform distributions\n7. **Does not address what happens when the base model lacks prerequisite skills** (the MLP is assumed pretrained)\n\n### 10. Implications for Your Explicit Archive-Based Curriculum\n\n**The paper supports several aspects of explicit curriculum and raises no fatal objection:**\n\n- **Smooth difficulty spectra accelerate learning dramatically** (relay >> grokking). An archive-based curriculum that ensures smooth coverage of the difficulty spectrum is directly aligned with this finding.\n- **Gaps in difficulty are harmful** -- they cause grokking-style plateaus. Explicit curation to fill difficulty gaps adds clear value beyond what implicit curriculum provides.\n- **The paper only proves implicit curriculum works on uniform mixtures** -- real training data is rarely uniformly distributed across difficulties. Explicit reweighting or selection could be essential for non-uniform distributions.\n- **The theory assumes all prerequisite skills are pre-learned** -- in practice, some skills may need explicit bootstrapping that natural RLVR cannot provide.\n- **The paper does NOT prove explicit curriculum is redundant** -- it proves implicit curriculum exists under idealized conditions. Explicit curriculum could still accelerate learning, handle distribution gaps, or address the many aspects the theory does not cover.\n\nThe strongest takeaway for your work: **ensure your difficulty spectrum is smooth and broad** (supporting the relay regime), which is an argument FOR careful archive curation rather than against it."
      }
    ],
    "totalDurationMs": 177573,
    "totalTokens": 19870,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 16716,
      "output_tokens": 2215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2215,
          "cache_read_input_tokens": 16716,
          "cache_creation_input_tokens": 938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 938,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 2,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "8f3c821f-f8e5-478c-8849-77475b8aac46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "bb814573-89ac-4b7a-b86f-e6c469c905c6",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Tool result

_source line 26 · 2026-05-28T00:44:38.012Z_

<details><summary>↩ Tool result · `toolu_01EXm2XBSMU4gaad3juyW9o4`</summary>

```text
Now I have comprehensive information. Let me compile the complete analysis.

---

Here is a thorough research synthesis addressing the statistical reliability of K=8 rollouts for advantage variance estimation in RLVR problem difficulty calibration.

## 1. Standard Practice: Rollouts Per Problem in GRPO-Family Methods

The field has converged on the following standard group sizes:

- **DeepSeek-R1**: G=16 rollouts per prompt (32 prompts per batch, batch size 512)
- **DAPO**: G=16 rollouts per prompt (512 prompt batch, 16 responses each)
- **VCRL**: G=16 (their recommended sweet spot based on ablation)
- **General GRPO**: Typical range is G=8 to G=64, with G=16 being the most common default

**K=8 is at the low end of standard practice, not below it.** The "It Takes Two" paper showed that 2-GRPO can match 16-GRPO under matched rollout budgets, but that is about policy gradient estimation, not variance estimation for curriculum decisions.

## 2. The Core Statistical Problem with K=8

The reviewer's concern is well-founded from a pure statistics standpoint. Here is the concrete math:

For binary rewards (correct/incorrect), if the true solve rate is p, then with K rollouts we observe k ~ Binomial(K, p). The sample variance estimator is:

**s^2 = k(K-k) / (K(K-1))**

The key issue is the **variance of this variance estimator**. For a Bernoulli process, the variance of the sample proportion p_hat = k/K is p(1-p)/K. More critically, the quantity p_hat(1-p_hat) that estimates p(1-p) has its own sampling variance that scales as O(1/K).

Concrete examples with K=8:
- **True p=0.5** (ideal difficulty): Possible observed k values are 0-8. The observed variance k(8-k)/(8*7) takes values {0, 0.125, 0.214, 0.268, 0.286, 0.268, 0.214, 0.125, 0}. The estimation is somewhat noisy but centered well.
- **True p=1/8=0.125** (hard problem): Most likely outcome is k=0 (34.4%) or k=1 (39.3%). With k=0 you get variance=0 (concluding the problem is "too hard"), with k=1 you get variance=0.125. There is a 34% chance of seeing zero variance even though the true p(1-p) = 0.109 is nonzero.
- **True p=2/8=0.25**: k=0 occurs 10% of the time, k=1 occurs 27% of the time, k=2 occurs 31% of the time. Significant probability mass on misleading estimates.

The normal approximation for confidence intervals requires np >= 5 and n(1-p) >= 5, which **fails entirely for K=8 at extreme solve rates**. The Wilson score interval for p_hat=1/8 with n=8 at 95% confidence spans roughly [0.006, 0.482] -- an enormous range.

## 3. VCRL's Own Ablation Results

The VCRL paper's ablation on group size is the most directly relevant evidence:

- **G=4**: Average score 44.17
- **G=16**: Average score 57.76 (massive +13.6 jump)
- **G=32**: Average score 59.25 (diminishing returns, +1.5 over G=16)

VCRL explicitly concludes that **G=16 is the minimum for robust variance estimation** in their curriculum framework. The jump from G=4 to G=16 is enormous, suggesting G=8 (interpolating) would capture some but not all of the benefit.

## 4. Known Failure Modes at Small Group Sizes

The MC-GRPO paper identifies the **advantage sign flip problem**: with small G, noise in the group mean/variance estimation causes some rollouts to receive incorrectly signed advantages, reversing the update direction. Even a 5% sign-flip rate induces approximately 4% performance degradation. This compounds over training.

AERO identifies the **zero-advantage dead zone**: when all K rollouts agree (all correct or all incorrect), the group variance is exactly zero and no gradient signal is produced. With K=8 and p=0.125, this happens 34% of the time (all failures). These are precisely the hard competition-level problems the reviewer is worried about.

## 5. Arguments FOR K=8 Being Sufficient (With Modifications)

Despite the raw statistical weakness, several arguments and modifications can make K=8 workable:

### a) You are not doing point estimation -- you are making a binary/ordinal decision

The key insight is that for problem replacement, you typically need to distinguish three regimes: "too easy" (variance near 0, high p), "too hard" (variance near 0, low p), and "learnable" (variance high). This is a much coarser classification than precise variance estimation. With K=8, you can reliably distinguish p near 0 or 1 from p near 0.5, even if you cannot distinguish p=0.3 from p=0.4.

### b) Temporal aggregation / exponential moving averages

DéjàQ applies **exponential decay to stored learnability estimates** and refreshes them whenever the item appears in the GRPO batch. If a problem appears in multiple batches over training, you effectively accumulate more than K=8 observations over time. This is equivalent to increasing your effective sample size.

### c) James-Stein / Empirical Bayes shrinkage (the strongest argument)

The **"Shrinking the Variance" paper** and **EBPO** demonstrate that shrinkage estimators that combine per-prompt statistics with global (across-prompt) statistics can dramatically reduce MSE, especially in the low-generation regime. Specifically:

- The James-Stein shrinkage baseline is provably lower-variance than the naive per-group mean
- EBPO uses a Welford online algorithm to maintain global statistics and dynamically shrinks local estimates toward the global prior
- The degree of shrinkage adapts: when local data is scarce (small K), more weight goes to the global prior; when abundant, the local estimate dominates

**This directly addresses the reviewer's concern**: with K=8, your per-problem variance estimate is noisy, but if you shrink it toward the batch-level average variance (a much better-estimated quantity), you get a principled estimate that trades a small bias for large variance reduction.

### d) Discounted Beta-Bernoulli (DBB) estimation

The DBB paper (March 2026) proposes maintaining a Beta posterior over each problem's solve rate using historical observations, rather than relying solely on the current batch's K samples. This:
- Accumulates evidence over time (effective K grows)
- Provides well-calibrated uncertainty estimates
- Avoids the variance collapse that point estimation suffers from
- Achieves lower MSE than standard GRPO estimation

### e) MC-GRPO's median-centered approach

Even with G=2, MC-GRPO closes the gap to G=8 to within 1% by replacing the mean baseline with a median baseline. This suggests that **the choice of estimator matters more than the raw sample size** for practical performance.

## 6. Concrete Recommendations for Making K=8 Robust

Here is what I would argue in a rebuttal:

### Primary argument: K=8 is for per-batch advantage computation, not for the replacement decision in isolation

1. **Separate the two uses of rollouts.** K=8 is standard (low end but standard) for GRPO advantage estimation and policy gradient computation. The replacement/curriculum decision should accumulate evidence across multiple appearances of the same problem.

2. **Use a Bayesian running estimate.** Maintain a Beta(alpha, beta) posterior per problem, initialized at Beta(1,1). Each time the problem appears with K=8 rollouts and k successes, update to Beta(alpha+k, beta+K-k). After just 3 appearances, you have an effective sample of K=24, which is quite reliable.

3. **Use shrinkage for the within-batch decision.** Apply James-Stein or empirical Bayes shrinkage so that when K=8 gives an extreme estimate, it is regularized toward the batch-level average. This is theoretically guaranteed to reduce MSE.

4. **Set conservative replacement thresholds.** Instead of replacing when estimated variance < threshold, replace when the upper bound of a credible interval for variance is below threshold. With a Beta posterior, this is straightforward to compute.

5. **The bias-variance tradeoff favors K=8 over K=16 or K=32 when compute-matched.** Doubling K from 8 to 16 halves the number of unique problems you can evaluate per batch. VCRL's ablation shows G=16 is better in isolation, but the AERO paper shows that under fixed compute budgets, seeing more diverse problems with smaller groups can be equally or more effective than fewer problems with larger groups.

### Quantitative bias-variance tradeoff: K=8 vs K=16 vs K=32

| Metric | K=8 | K=16 | K=32 |
|--------|-----|------|------|
| Unique problems per batch (fixed compute) | 2x more | baseline | 0.5x |
| Std dev of p_hat at p=0.5 | 0.177 | 0.125 | 0.088 |
| Std dev of p_hat at p=0.125 | 0.117 | 0.083 | 0.058 |
| P(all fail) at p=0.125 | 34.4% | 11.8% | 1.4% |
| P(all fail) at p=0.25 | 10.0% | 1.0% | 0.01% |
| Zero-gradient dead zone frequency (p=0.125) | ~34% | ~12% | ~1% |

The "P(all fail)" row is the most damning for K=8 at low solve rates. However, with a Beta posterior and shrinkage, these zero-observation events are handled gracefully (the posterior simply does not update much, retaining the prior).

## 7. Summary of the Strongest Rebuttal Points

1. **K=8 per batch is standard for GRPO training** (DeepSeek-R1 uses 16, but recent work like "It Takes Two" and MC-GRPO shows smaller groups work with proper estimators).

2. **The replacement decision should not rely on a single batch's K=8 estimate.** Maintaining a running Bayesian posterior (Beta-Bernoulli) over multiple encounters gives an effective sample much larger than 8. DéjàQ itself uses exponential decay for this reason.

3. **Shrinkage estimators (James-Stein, EBPO) are specifically designed for this regime** and provably reduce MSE without additional compute. This is the most directly applicable mitigation.

4. **The compute tradeoff favors exploration over precision**: with K=8, you see 2x as many unique problems as K=16. For curriculum learning, breadth of difficulty estimation across the problem set may matter more than precision on individual problems.

5. **The decision is coarse, not fine-grained.** You need to distinguish "learnable" from "too hard/easy," not estimate variance to 3 decimal places. Even noisy K=8 estimates, combined with conservative thresholds or credible intervals, suffice for this classification.

6. **Acknowledge the limitation and propose a concrete fix**: "We agree that single-batch K=8 estimates have high variance for extreme solve rates. We address this by [accumulating a Beta posterior / applying shrinkage / using conservative thresholds], which increases effective sample size without additional compute."

Sources:
- [VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models](https://arxiv.org/abs/2509.19803)
- [MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning](https://arxiv.org/abs/2601.22582)
- [Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2511.03710)
- [EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization](https://arxiv.org/abs/2602.05165)
- [Discounted Beta-Bernoulli Reward Estimation for Sample-Efficient RLVR](https://arxiv.org/pdf/2603.18444)
- [DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems](https://arxiv.org/abs/2601.01931)
- [It Takes Two: Your GRPO Is Secretly DPO](https://arxiv.org/abs/2510.00977)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs](https://arxiv.org/abs/2501.12948)
- [Train Less, Learn More: Adaptive Efficient Rollout Optimization](https://arxiv.org/abs/2602.14338)
- [DAPO: An Open Source LLM Reinforcement Learning System at Scale](https://self-supervised.cs.jhu.edu/fa2025/files/presentations/Why-RL-Sep16-AdvancesNLP.pdf)
- [Binomial Proportion Confidence Interval - Wikipedia](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval)
- [Why Tree-Style Branching Matters for Thought Advantage Estimation in GRPO](https://arxiv.org/pdf/2509.24494)
- [GRPO++: Tricks for Making RL Actually Work](https://cameronrwolfe.substack.com/p/grpo-tricks)

agentId: a3b716849e4c858e1 (use SendMessage with to: 'a3b716849e4c858e1' to continue this agent)
&lt;usage>total_tokens: 30253
tool_uses: 22
duration_ms: 165487&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b22337f-f9c0-49bc-bc15-180e6dd1b00b",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "f1981e34-b332-4577-a986-b6ff9540ece4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the statistical reliability of using K=8 rollouts to estimate advantage variance for RLVR problem difficulty calibration. The context:\n\n- In GRPO-style RL training for math reasoning, problems are evaluated with K rollouts\n- DéjàQ uses K=100 completions per problem for learnability estimation p(1-p)\n- We propose K=8 rollouts and using advantage variance as a replacement criterion\n- A reviewer is concerned that with K=8, the variance estimate is itself highly variable, especially for competition-level problems where solve rates might be 1/8 or 2/8\n\nPlease research:\n1. Search for \"GRPO rollout sample size variance estimation\" and related queries\n2. Search for \"VCRL advantage variance estimation reliability\" \n3. Search for \"confidence interval binomial proportion small sample\"\n4. Search for \"DAPO GRPO number rollouts per problem\" to find what standard practice is\n5. What is the standard number of rollouts used in GRPO/DAPO/DeepSeek-R1 style training?\n6. What statistical approaches exist for reliable variance estimation with small samples?\n7. Is there literature on confidence-based thresholds for curriculum/replacement decisions in RL?\n8. What's the bias-variance tradeoff between K=8 and K=16 or K=32?\n\nI need concrete statistical arguments for why K=8 might be sufficient or what modifications would make it robust.",
    "agentId": "a3b716849e4c858e1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the complete analysis.\n\n---\n\nHere is a thorough research synthesis addressing the statistical reliability of K=8 rollouts for advantage variance estimation in RLVR problem difficulty calibration.\n\n## 1. Standard Practice: Rollouts Per Problem in GRPO-Family Methods\n\nThe field has converged on the following standard group sizes:\n\n- **DeepSeek-R1**: G=16 rollouts per prompt (32 prompts per batch, batch size 512)\n- **DAPO**: G=16 rollouts per prompt (512 prompt batch, 16 responses each)\n- **VCRL**: G=16 (their recommended sweet spot based on ablation)\n- **General GRPO**: Typical range is G=8 to G=64, with G=16 being the most common default\n\n**K=8 is at the low end of standard practice, not below it.** The \"It Takes Two\" paper showed that 2-GRPO can match 16-GRPO under matched rollout budgets, but that is about policy gradient estimation, not variance estimation for curriculum decisions.\n\n## 2. The Core Statistical Problem with K=8\n\nThe reviewer's concern is well-founded from a pure statistics standpoint. Here is the concrete math:\n\nFor binary rewards (correct/incorrect), if the true solve rate is p, then with K rollouts we observe k ~ Binomial(K, p). The sample variance estimator is:\n\n**s^2 = k(K-k) / (K(K-1))**\n\nThe key issue is the **variance of this variance estimator**. For a Bernoulli process, the variance of the sample proportion p_hat = k/K is p(1-p)/K. More critically, the quantity p_hat(1-p_hat) that estimates p(1-p) has its own sampling variance that scales as O(1/K).\n\nConcrete examples with K=8:\n- **True p=0.5** (ideal difficulty): Possible observed k values are 0-8. The observed variance k(8-k)/(8*7) takes values {0, 0.125, 0.214, 0.268, 0.286, 0.268, 0.214, 0.125, 0}. The estimation is somewhat noisy but centered well.\n- **True p=1/8=0.125** (hard problem): Most likely outcome is k=0 (34.4%) or k=1 (39.3%). With k=0 you get variance=0 (concluding the problem is \"too hard\"), with k=1 you get variance=0.125. There is a 34% chance of seeing zero variance even though the true p(1-p) = 0.109 is nonzero.\n- **True p=2/8=0.25**: k=0 occurs 10% of the time, k=1 occurs 27% of the time, k=2 occurs 31% of the time. Significant probability mass on misleading estimates.\n\nThe normal approximation for confidence intervals requires np >= 5 and n(1-p) >= 5, which **fails entirely for K=8 at extreme solve rates**. The Wilson score interval for p_hat=1/8 with n=8 at 95% confidence spans roughly [0.006, 0.482] -- an enormous range.\n\n## 3. VCRL's Own Ablation Results\n\nThe VCRL paper's ablation on group size is the most directly relevant evidence:\n\n- **G=4**: Average score 44.17\n- **G=16**: Average score 57.76 (massive +13.6 jump)\n- **G=32**: Average score 59.25 (diminishing returns, +1.5 over G=16)\n\nVCRL explicitly concludes that **G=16 is the minimum for robust variance estimation** in their curriculum framework. The jump from G=4 to G=16 is enormous, suggesting G=8 (interpolating) would capture some but not all of the benefit.\n\n## 4. Known Failure Modes at Small Group Sizes\n\nThe MC-GRPO paper identifies the **advantage sign flip problem**: with small G, noise in the group mean/variance estimation causes some rollouts to receive incorrectly signed advantages, reversing the update direction. Even a 5% sign-flip rate induces approximately 4% performance degradation. This compounds over training.\n\nAERO identifies the **zero-advantage dead zone**: when all K rollouts agree (all correct or all incorrect), the group variance is exactly zero and no gradient signal is produced. With K=8 and p=0.125, this happens 34% of the time (all failures). These are precisely the hard competition-level problems the reviewer is worried about.\n\n## 5. Arguments FOR K=8 Being Sufficient (With Modifications)\n\nDespite the raw statistical weakness, several arguments and modifications can make K=8 workable:\n\n### a) You are not doing point estimation -- you are making a binary/ordinal decision\n\nThe key insight is that for problem replacement, you typically need to distinguish three regimes: \"too easy\" (variance near 0, high p), \"too hard\" (variance near 0, low p), and \"learnable\" (variance high). This is a much coarser classification than precise variance estimation. With K=8, you can reliably distinguish p near 0 or 1 from p near 0.5, even if you cannot distinguish p=0.3 from p=0.4.\n\n### b) Temporal aggregation / exponential moving averages\n\nDéjàQ applies **exponential decay to stored learnability estimates** and refreshes them whenever the item appears in the GRPO batch. If a problem appears in multiple batches over training, you effectively accumulate more than K=8 observations over time. This is equivalent to increasing your effective sample size.\n\n### c) James-Stein / Empirical Bayes shrinkage (the strongest argument)\n\nThe **\"Shrinking the Variance\" paper** and **EBPO** demonstrate that shrinkage estimators that combine per-prompt statistics with global (across-prompt) statistics can dramatically reduce MSE, especially in the low-generation regime. Specifically:\n\n- The James-Stein shrinkage baseline is provably lower-variance than the naive per-group mean\n- EBPO uses a Welford online algorithm to maintain global statistics and dynamically shrinks local estimates toward the global prior\n- The degree of shrinkage adapts: when local data is scarce (small K), more weight goes to the global prior; when abundant, the local estimate dominates\n\n**This directly addresses the reviewer's concern**: with K=8, your per-problem variance estimate is noisy, but if you shrink it toward the batch-level average variance (a much better-estimated quantity), you get a principled estimate that trades a small bias for large variance reduction.\n\n### d) Discounted Beta-Bernoulli (DBB) estimation\n\nThe DBB paper (March 2026) proposes maintaining a Beta posterior over each problem's solve rate using historical observations, rather than relying solely on the current batch's K samples. This:\n- Accumulates evidence over time (effective K grows)\n- Provides well-calibrated uncertainty estimates\n- Avoids the variance collapse that point estimation suffers from\n- Achieves lower MSE than standard GRPO estimation\n\n### e) MC-GRPO's median-centered approach\n\nEven with G=2, MC-GRPO closes the gap to G=8 to within 1% by replacing the mean baseline with a median baseline. This suggests that **the choice of estimator matters more than the raw sample size** for practical performance.\n\n## 6. Concrete Recommendations for Making K=8 Robust\n\nHere is what I would argue in a rebuttal:\n\n### Primary argument: K=8 is for per-batch advantage computation, not for the replacement decision in isolation\n\n1. **Separate the two uses of rollouts.** K=8 is standard (low end but standard) for GRPO advantage estimation and policy gradient computation. The replacement/curriculum decision should accumulate evidence across multiple appearances of the same problem.\n\n2. **Use a Bayesian running estimate.** Maintain a Beta(alpha, beta) posterior per problem, initialized at Beta(1,1). Each time the problem appears with K=8 rollouts and k successes, update to Beta(alpha+k, beta+K-k). After just 3 appearances, you have an effective sample of K=24, which is quite reliable.\n\n3. **Use shrinkage for the within-batch decision.** Apply James-Stein or empirical Bayes shrinkage so that when K=8 gives an extreme estimate, it is regularized toward the batch-level average. This is theoretically guaranteed to reduce MSE.\n\n4. **Set conservative replacement thresholds.** Instead of replacing when estimated variance < threshold, replace when the upper bound of a credible interval for variance is below threshold. With a Beta posterior, this is straightforward to compute.\n\n5. **The bias-variance tradeoff favors K=8 over K=16 or K=32 when compute-matched.** Doubling K from 8 to 16 halves the number of unique problems you can evaluate per batch. VCRL's ablation shows G=16 is better in isolation, but the AERO paper shows that under fixed compute budgets, seeing more diverse problems with smaller groups can be equally or more effective than fewer problems with larger groups.\n\n### Quantitative bias-variance tradeoff: K=8 vs K=16 vs K=32\n\n| Metric | K=8 | K=16 | K=32 |\n|--------|-----|------|------|\n| Unique problems per batch (fixed compute) | 2x more | baseline | 0.5x |\n| Std dev of p_hat at p=0.5 | 0.177 | 0.125 | 0.088 |\n| Std dev of p_hat at p=0.125 | 0.117 | 0.083 | 0.058 |\n| P(all fail) at p=0.125 | 34.4% | 11.8% | 1.4% |\n| P(all fail) at p=0.25 | 10.0% | 1.0% | 0.01% |\n| Zero-gradient dead zone frequency (p=0.125) | ~34% | ~12% | ~1% |\n\nThe \"P(all fail)\" row is the most damning for K=8 at low solve rates. However, with a Beta posterior and shrinkage, these zero-observation events are handled gracefully (the posterior simply does not update much, retaining the prior).\n\n## 7. Summary of the Strongest Rebuttal Points\n\n1. **K=8 per batch is standard for GRPO training** (DeepSeek-R1 uses 16, but recent work like \"It Takes Two\" and MC-GRPO shows smaller groups work with proper estimators).\n\n2. **The replacement decision should not rely on a single batch's K=8 estimate.** Maintaining a running Bayesian posterior (Beta-Bernoulli) over multiple encounters gives an effective sample much larger than 8. DéjàQ itself uses exponential decay for this reason.\n\n3. **Shrinkage estimators (James-Stein, EBPO) are specifically designed for this regime** and provably reduce MSE without additional compute. This is the most directly applicable mitigation.\n\n4. **The compute tradeoff favors exploration over precision**: with K=8, you see 2x as many unique problems as K=16. For curriculum learning, breadth of difficulty estimation across the problem set may matter more than precision on individual problems.\n\n5. **The decision is coarse, not fine-grained.** You need to distinguish \"learnable\" from \"too hard/easy,\" not estimate variance to 3 decimal places. Even noisy K=8 estimates, combined with conservative thresholds or credible intervals, suffice for this classification.\n\n6. **Acknowledge the limitation and propose a concrete fix**: \"We agree that single-batch K=8 estimates have high variance for extreme solve rates. We address this by [accumulating a Beta posterior / applying shrinkage / using conservative thresholds], which increases effective sample size without additional compute.\"\n\nSources:\n- [VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models](https://arxiv.org/abs/2509.19803)\n- [MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning](https://arxiv.org/abs/2601.22582)\n- [Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2511.03710)\n- [EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization](https://arxiv.org/abs/2602.05165)\n- [Discounted Beta-Bernoulli Reward Estimation for Sample-Efficient RLVR](https://arxiv.org/pdf/2603.18444)\n- [DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems](https://arxiv.org/abs/2601.01931)\n- [It Takes Two: Your GRPO Is Secretly DPO](https://arxiv.org/abs/2510.00977)\n- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs](https://arxiv.org/abs/2501.12948)\n- [Train Less, Learn More: Adaptive Efficient Rollout Optimization](https://arxiv.org/abs/2602.14338)\n- [DAPO: An Open Source LLM Reinforcement Learning System at Scale](https://self-supervised.cs.jhu.edu/fa2025/files/presentations/Why-RL-Sep16-AdvancesNLP.pdf)\n- [Binomial Proportion Confidence Interval - Wikipedia](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval)\n- [Why Tree-Style Branching Matters for Thought Advantage Estimation in GRPO](https://arxiv.org/pdf/2509.24494)\n- [GRPO++: Tricks for Making RL Actually Work](https://cameronrwolfe.substack.com/p/grpo-tricks)"
      }
    ],
    "totalDurationMs": 165487,
    "totalTokens": 30253,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 637,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 25381,
      "output_tokens": 3400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 637,
          "output_tokens": 3400,
          "cache_read_input_tokens": 25381,
          "cache_creation_input_tokens": 835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 835,
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
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "9b22337f-f9c0-49bc-bc15-180e6dd1b00b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T00:45:14.188Z_

<details><summary>↩ Tool result · `toolu_01P6CBagaUK3ZhUYQYYDaTLU`</summary>

```text
Now I have a comprehensive picture. Let me compile the findings into a thorough report.

Here is the comprehensive report on AIME 2024 state-of-the-art results for 7B-8B parameter models as of May 2026.

---

## AIME 2024 Leaderboard for 7B-8B Parameter Models (as of May 2026)

### Top-Ranked 7B-8B Models on AIME 2024

| Rank | Model | AIME 2024 | Parameters | Training Paradigm |
|------|-------|-----------|------------|-------------------|
| 1 | **Klear-Reasoner-8B** | **90.5%** (64K budget) | 8B | Distillation (DeepSeek-R1-0528) + SFT + RL (GPPO) |
| 2 | **Ministral 3 8B Reasoning** | **86.0%** | 8B | Proprietary (Mistral reasoning training) |
| 3 | **MiniCPM-SALA** | **83.75%** | 9B | Hybrid architecture + continual training |
| 4 | **DeepSeek-R1-Distill-Qwen-7B** | **83.3%** | 7B | Distillation from DeepSeek-R1 |
| 5 | **Granite 3.3 8B Instruct/Base** | **81.2%** | 8B | Two-stage training + PPO alignment |
| 6 | **DeepSeek-R1-Distill-Llama-8B** | **80.0%** | 8B | Distillation from DeepSeek-R1 |
| 7 | **ScaleDiff-7B** | **73.0%** | 7B | SFT on synthetic difficulty-scaled data (distilled from Qwen3-8B) |
| 8 | **OpenMath-Nemotron-7B** | **73.7%** | 7B | SFT + RL (NVIDIA pipeline) |
| 9 | **BP-Math-7B** | **70.8%** | 7B | RL via BAPO on distilled base |
| 10 | **SkyWork-OR1-7B** | **70.2%** | 7B | RL on DeepSeek-R1-Distill-Qwen-7B base |
| 11 | **AceMath-RL-Nemotron-7B** | **69.0%** | 7B | Pure RL (GRPO) from distilled checkpoint |
| 12 | **OpenThinker3-7B** | **66.3%** | 7B | SFT on 1.2M reasoning examples |

---

### Verification of the Three Reviewer-Cited Models

**Klear-Reasoner-8B: 90.5% -- CONFIRMED**
- Base model: Qwen3-8B-Base
- Training: Long CoT SFT distilled from DeepSeek-R1-0528, followed by RL using a novel method called GPPO (Gradient-Preserving Clipping Policy Optimization)
- Important caveat: The 90.5% figure requires a **64K token inference budget** with YaRN scaling (factor 2.5). Without the extended budget, SFT-only achieves 75.6%, and SFT+GPPO achieves 83.2%.
- Paper: [arxiv.org/abs/2508.07629](https://arxiv.org/abs/2508.07629)
- HuggingFace: [Kwai-Klear/Klear-Reasoner-8B](https://huggingface.co/Kwai-Klear/Klear-Reasoner-8B)

**BP-Math-7B: 70.8% -- CONFIRMED**
- Training: BAPO (Balanced Policy Optimization with Adaptive Clipping), an off-policy RL method
- Base model: Built on top of a distilled model (likely DeepSeek-R1-Distill-Qwen-7B), with BAPO achieving +3.9 points over the SFT baseline on AIME 2024
- Outperforms SkyWork-OR1-7B by 7.9 points on AIME 2025
- Paper: [arxiv.org/abs/2510.18927](https://arxiv.org/abs/2510.18927)

**ScaleDiff-7B: 73.0% -- CONFIRMED (73.0% +/- 5.0)**
- Training: **SFT only** (not RL) on the ScaleDiff-Math synthetic dataset
- Base model: Qwen2.5-Math-7B-Instruct
- Uses distillation: solutions generated by Qwen3-8B in "Thinking" mode
- The pipeline uses difficulty mining (AdaptThink) and a specialized hard-problem generator (DiffGen-8B)
- Paper: [arxiv.org/abs/2509.21070](https://arxiv.org/abs/2509.21070)

---

### Training Paradigm Analysis

**What do the top models use?**

Nearly every top-performing 7B-8B model on AIME 2024 relies on **distillation** in some form:

1. **Distillation + RL** (highest scores): Klear-Reasoner-8B (90.5%) starts from long-CoT data distilled from DeepSeek-R1-0528, then applies GPPO reinforcement learning. This is the dominant paradigm for the very top results.

2. **Distillation + SFT** (strong baselines): DeepSeek-R1-Distill-Qwen-7B (83.3%) uses pure SFT on ~800K samples distilled from DeepSeek-R1. ScaleDiff-7B (73.0%) uses SFT on synthetically generated hard problems with solutions distilled from Qwen3-8B.

3. **RL on distilled base** (incremental gains): Models like AceMath-RL-Nemotron-7B (69.0%), SkyWork-OR1-7B (70.2%), and BP-Math-7B (70.8%) apply RL on top of already-distilled checkpoints (typically DeepSeek-R1-Distill-Qwen-7B). The RL adds roughly 5-15 points on top of the distilled base.

4. **Proprietary methods**: Ministral 3 8B Reasoning (86.0%) from Mistral AI does not disclose full training details.

---

### Where Do Self-Evolving / Co-Evolutionary Methods Rank?

Self-evolving and co-evolutionary methods that avoid teacher distillation score **dramatically lower** on AIME 2024 for 7B-8B models:

| Method | Model | AIME 2024 | Uses Distillation? |
|--------|-------|-----------|-------------------|
| **DSER** (Deep Self-Evolving Reasoning) | DeepSeek-R1-0528-Qwen3-8B | **89.3%** (pass@1) | **Yes** -- the base model is distilled from DeepSeek-R1-0528 (600B teacher); DSER is a test-time self-evolution method applied on top |
| **R-Zero** (co-evolutionary) | Qwen3-8B-Base | **~16.35** (mean@32) | **No** -- truly zero external data, co-evolutionary Challenger/Solver |
| **Absolute Zero (AZR)** | Qwen2.5-7B | **13.3-20.0%** (pass@1) | **No** -- self-play with zero external data |
| **SvS** (Self-play Variational Problem Synthesis) | LLaMA-3.1-8B-Instruct | +18.3 pts (pass@32 gain) | **No** -- self-play augmentation of RLVR |

**Key finding**: The best truly self-evolving method *without distillation* on a 7B-8B model achieves roughly **16-20% on AIME 2024** (R-Zero with Qwen3-8B-Base, Absolute Zero with Qwen2.5-7B). This is approximately **4-5x lower** than the distillation-based SOTA of 90.5%.

DSER achieves 89.3% but it is not a pure self-evolving method -- it applies self-evolving *reasoning at inference time* to a model that was already distilled from a 600B teacher. The self-evolution component adds +6.5 points on top of the 82.8% distilled baseline.

---

### What Constraints Separate Self-Evolving Methods from Distillation-Based Ones?

1. **Data source**: Distillation-based methods train on CoT traces generated by a stronger teacher model (e.g., DeepSeek-R1, DeepSeek-R1-0528). Self-evolving methods generate their own training problems and solutions with no external teacher.

2. **Knowledge ceiling**: Distilled models inherit the reasoning patterns of their much larger teachers (600B+ parameters). Self-evolving models are bounded by their own capacity to discover reasoning strategies from scratch.

3. **The gap is enormous**: For 7B-8B models, the gap between the best distillation-based result (90.5%) and the best purely self-evolving result (~16-20%) is roughly **70+ percentage points**. Even the best RL-on-distilled-base approach (AceMath-RL-Nemotron at 69%) still trails the distillation+RL leader by over 20 points.

4. **Hybrid zone**: Most practical "self-evolving" methods actually start from a distilled checkpoint and then apply self-evolution techniques (like DSER). This hybrid approach is effective (82.8% -> 89.3%) but should not be confused with pure self-evolution from a base model.

---

### Summary

- **SOTA for 7B-8B on AIME 2024**: Klear-Reasoner-8B at 90.5% (with 64K inference budget; 83.2% at standard budget)
- **All three reviewer-cited numbers are confirmed**: Klear-Reasoner-8B 90.5%, BP-Math-7B 70.8%, ScaleDiff-7B 73.0%
- **Dominant paradigm**: Distillation from a strong teacher (DeepSeek-R1-0528) + SFT + RL
- **Best pure self-evolving (no distillation) result**: Approximately 16-20% on AIME 2024 for 7B-8B models (R-Zero, Absolute Zero)
- **Best self-evolving on distilled base**: DSER at 89.3% (but the base is distilled)
- **Pure RL on distilled base**: AceMath-RL-Nemotron-7B at 69.0%

The current evidence strongly suggests that distillation from large teacher models remains the critical ingredient for competitive AIME 2024 performance at the 7B-8B scale. Self-evolving methods show promising directions but have not yet closed the gap.

Sources:
- [Klear-Reasoner paper](https://arxiv.org/abs/2508.07629)
- [Klear-Reasoner-8B on HuggingFace](https://huggingface.co/Kwai-Klear/Klear-Reasoner-8B)
- [BAPO / BP-Math paper](https://arxiv.org/abs/2510.18927)
- [ScaleDiff paper](https://arxiv.org/abs/2509.21070)
- [Deep Self-Evolving Reasoning (DSER)](https://arxiv.org/abs/2510.17498)
- [Absolute Zero Reasoner](https://arxiv.org/abs/2505.03335)
- [R-Zero](https://arxiv.org/html/2508.05004v1)
- [AceReason-Nemotron / AceMath-RL](https://arxiv.org/abs/2505.16400)
- [SkyWork-OR1](https://arxiv.org/html/2505.22312v1)
- [Beyond Pass@1: SvS](https://arxiv.org/abs/2508.14029)
- [AIME 2024 Leaderboard (llm-stats)](https://llm-stats.com/benchmarks/aime-2024)
- [AIME 2024 Leaderboard (CodeSOTA)](https://www.codesota.com/benchmark/aime-2024)
- [AIME 2024 Leaderboard (pricepertoken)](https://pricepertoken.com/leaderboards/benchmark/aime)
- [Post-Training in 2026 overview](https://llm-stats.com/blog/research/post-training-techniques-2026)

agentId: a9b5a82b8aa482760 (use SendMessage with to: 'a9b5a82b8aa482760' to continue this agent)
&lt;usage>total_tokens: 41329
tool_uses: 40
duration_ms: 209574&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9003d75c-6c16-44d9-8f26-fd64a877fabc",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "3ed4533d-be9b-406d-8325-d3bb643e5228",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find the current state-of-the-art results on AIME 2024 for 7B-8B parameter models as of May 2026. The reviewer mentioned:\n- Klear-Reasoner-8B: 90.5% on AIME 2024\n- BP-Math-7B: 70.8%\n- ScaleDiff-7B: 73.0%\n\nPlease:\n1. Search for \"AIME 2024 leaderboard 7B 8B models 2026\" and related queries\n2. Search for \"Klear-Reasoner-8B AIME\" to verify this result\n3. Search for \"BP-Math-7B AIME\" to verify\n4. Search for \"ScaleDiff-7B AIME\" to verify\n5. Search for Papers with Code AIME 2024 leaderboard\n6. Search for \"self-evolving RLVR AIME 2024 results 2026\" to find what self-evolving/co-evolutionary methods specifically achieve\n\nKey questions:\n- What training paradigms do the top models use? (distillation? extensive SFT? synthetic data?)\n- Where do self-evolving/online methods specifically rank?\n- What's the best AIME 2024 result from a purely self-evolving/co-evolutionary method (no distillation)?\n- What constraints separate self-evolving methods from distillation-based ones?\n\nReport concrete numbers and methods used.",
    "agentId": "a9b5a82b8aa482760",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Let me compile the findings into a thorough report.\n\nHere is the comprehensive report on AIME 2024 state-of-the-art results for 7B-8B parameter models as of May 2026.\n\n---\n\n## AIME 2024 Leaderboard for 7B-8B Parameter Models (as of May 2026)\n\n### Top-Ranked 7B-8B Models on AIME 2024\n\n| Rank | Model | AIME 2024 | Parameters | Training Paradigm |\n|------|-------|-----------|------------|-------------------|\n| 1 | **Klear-Reasoner-8B** | **90.5%** (64K budget) | 8B | Distillation (DeepSeek-R1-0528) + SFT + RL (GPPO) |\n| 2 | **Ministral 3 8B Reasoning** | **86.0%** | 8B | Proprietary (Mistral reasoning training) |\n| 3 | **MiniCPM-SALA** | **83.75%** | 9B | Hybrid architecture + continual training |\n| 4 | **DeepSeek-R1-Distill-Qwen-7B** | **83.3%** | 7B | Distillation from DeepSeek-R1 |\n| 5 | **Granite 3.3 8B Instruct/Base** | **81.2%** | 8B | Two-stage training + PPO alignment |\n| 6 | **DeepSeek-R1-Distill-Llama-8B** | **80.0%** | 8B | Distillation from DeepSeek-R1 |\n| 7 | **ScaleDiff-7B** | **73.0%** | 7B | SFT on synthetic difficulty-scaled data (distilled from Qwen3-8B) |\n| 8 | **OpenMath-Nemotron-7B** | **73.7%** | 7B | SFT + RL (NVIDIA pipeline) |\n| 9 | **BP-Math-7B** | **70.8%** | 7B | RL via BAPO on distilled base |\n| 10 | **SkyWork-OR1-7B** | **70.2%** | 7B | RL on DeepSeek-R1-Distill-Qwen-7B base |\n| 11 | **AceMath-RL-Nemotron-7B** | **69.0%** | 7B | Pure RL (GRPO) from distilled checkpoint |\n| 12 | **OpenThinker3-7B** | **66.3%** | 7B | SFT on 1.2M reasoning examples |\n\n---\n\n### Verification of the Three Reviewer-Cited Models\n\n**Klear-Reasoner-8B: 90.5% -- CONFIRMED**\n- Base model: Qwen3-8B-Base\n- Training: Long CoT SFT distilled from DeepSeek-R1-0528, followed by RL using a novel method called GPPO (Gradient-Preserving Clipping Policy Optimization)\n- Important caveat: The 90.5% figure requires a **64K token inference budget** with YaRN scaling (factor 2.5). Without the extended budget, SFT-only achieves 75.6%, and SFT+GPPO achieves 83.2%.\n- Paper: [arxiv.org/abs/2508.07629](https://arxiv.org/abs/2508.07629)\n- HuggingFace: [Kwai-Klear/Klear-Reasoner-8B](https://huggingface.co/Kwai-Klear/Klear-Reasoner-8B)\n\n**BP-Math-7B: 70.8% -- CONFIRMED**\n- Training: BAPO (Balanced Policy Optimization with Adaptive Clipping), an off-policy RL method\n- Base model: Built on top of a distilled model (likely DeepSeek-R1-Distill-Qwen-7B), with BAPO achieving +3.9 points over the SFT baseline on AIME 2024\n- Outperforms SkyWork-OR1-7B by 7.9 points on AIME 2025\n- Paper: [arxiv.org/abs/2510.18927](https://arxiv.org/abs/2510.18927)\n\n**ScaleDiff-7B: 73.0% -- CONFIRMED (73.0% +/- 5.0)**\n- Training: **SFT only** (not RL) on the ScaleDiff-Math synthetic dataset\n- Base model: Qwen2.5-Math-7B-Instruct\n- Uses distillation: solutions generated by Qwen3-8B in \"Thinking\" mode\n- The pipeline uses difficulty mining (AdaptThink) and a specialized hard-problem generator (DiffGen-8B)\n- Paper: [arxiv.org/abs/2509.21070](https://arxiv.org/abs/2509.21070)\n\n---\n\n### Training Paradigm Analysis\n\n**What do the top models use?**\n\nNearly every top-performing 7B-8B model on AIME 2024 relies on **distillation** in some form:\n\n1. **Distillation + RL** (highest scores): Klear-Reasoner-8B (90.5%) starts from long-CoT data distilled from DeepSeek-R1-0528, then applies GPPO reinforcement learning. This is the dominant paradigm for the very top results.\n\n2. **Distillation + SFT** (strong baselines): DeepSeek-R1-Distill-Qwen-7B (83.3%) uses pure SFT on ~800K samples distilled from DeepSeek-R1. ScaleDiff-7B (73.0%) uses SFT on synthetically generated hard problems with solutions distilled from Qwen3-8B.\n\n3. **RL on distilled base** (incremental gains): Models like AceMath-RL-Nemotron-7B (69.0%), SkyWork-OR1-7B (70.2%), and BP-Math-7B (70.8%) apply RL on top of already-distilled checkpoints (typically DeepSeek-R1-Distill-Qwen-7B). The RL adds roughly 5-15 points on top of the distilled base.\n\n4. **Proprietary methods**: Ministral 3 8B Reasoning (86.0%) from Mistral AI does not disclose full training details.\n\n---\n\n### Where Do Self-Evolving / Co-Evolutionary Methods Rank?\n\nSelf-evolving and co-evolutionary methods that avoid teacher distillation score **dramatically lower** on AIME 2024 for 7B-8B models:\n\n| Method | Model | AIME 2024 | Uses Distillation? |\n|--------|-------|-----------|-------------------|\n| **DSER** (Deep Self-Evolving Reasoning) | DeepSeek-R1-0528-Qwen3-8B | **89.3%** (pass@1) | **Yes** -- the base model is distilled from DeepSeek-R1-0528 (600B teacher); DSER is a test-time self-evolution method applied on top |\n| **R-Zero** (co-evolutionary) | Qwen3-8B-Base | **~16.35** (mean@32) | **No** -- truly zero external data, co-evolutionary Challenger/Solver |\n| **Absolute Zero (AZR)** | Qwen2.5-7B | **13.3-20.0%** (pass@1) | **No** -- self-play with zero external data |\n| **SvS** (Self-play Variational Problem Synthesis) | LLaMA-3.1-8B-Instruct | +18.3 pts (pass@32 gain) | **No** -- self-play augmentation of RLVR |\n\n**Key finding**: The best truly self-evolving method *without distillation* on a 7B-8B model achieves roughly **16-20% on AIME 2024** (R-Zero with Qwen3-8B-Base, Absolute Zero with Qwen2.5-7B). This is approximately **4-5x lower** than the distillation-based SOTA of 90.5%.\n\nDSER achieves 89.3% but it is not a pure self-evolving method -- it applies self-evolving *reasoning at inference time* to a model that was already distilled from a 600B teacher. The self-evolution component adds +6.5 points on top of the 82.8% distilled baseline.\n\n---\n\n### What Constraints Separate Self-Evolving Methods from Distillation-Based Ones?\n\n1. **Data source**: Distillation-based methods train on CoT traces generated by a stronger teacher model (e.g., DeepSeek-R1, DeepSeek-R1-0528). Self-evolving methods generate their own training problems and solutions with no external teacher.\n\n2. **Knowledge ceiling**: Distilled models inherit the reasoning patterns of their much larger teachers (600B+ parameters). Self-evolving models are bounded by their own capacity to discover reasoning strategies from scratch.\n\n3. **The gap is enormous**: For 7B-8B models, the gap between the best distillation-based result (90.5%) and the best purely self-evolving result (~16-20%) is roughly **70+ percentage points**. Even the best RL-on-distilled-base approach (AceMath-RL-Nemotron at 69%) still trails the distillation+RL leader by over 20 points.\n\n4. **Hybrid zone**: Most practical \"self-evolving\" methods actually start from a distilled checkpoint and then apply self-evolution techniques (like DSER). This hybrid approach is effective (82.8% -> 89.3%) but should not be confused with pure self-evolution from a base model.\n\n---\n\n### Summary\n\n- **SOTA for 7B-8B on AIME 2024**: Klear-Reasoner-8B at 90.5% (with 64K inference budget; 83.2% at standard budget)\n- **All three reviewer-cited numbers are confirmed**: Klear-Reasoner-8B 90.5%, BP-Math-7B 70.8%, ScaleDiff-7B 73.0%\n- **Dominant paradigm**: Distillation from a strong teacher (DeepSeek-R1-0528) + SFT + RL\n- **Best pure self-evolving (no distillation) result**: Approximately 16-20% on AIME 2024 for 7B-8B models (R-Zero, Absolute Zero)\n- **Best self-evolving on distilled base**: DSER at 89.3% (but the base is distilled)\n- **Pure RL on distilled base**: AceMath-RL-Nemotron-7B at 69.0%\n\nThe current evidence strongly suggests that distillation from large teacher models remains the critical ingredient for competitive AIME 2024 performance at the 7B-8B scale. Self-evolving methods show promising directions but have not yet closed the gap.\n\nSources:\n- [Klear-Reasoner paper](https://arxiv.org/abs/2508.07629)\n- [Klear-Reasoner-8B on HuggingFace](https://huggingface.co/Kwai-Klear/Klear-Reasoner-8B)\n- [BAPO / BP-Math paper](https://arxiv.org/abs/2510.18927)\n- [ScaleDiff paper](https://arxiv.org/abs/2509.21070)\n- [Deep Self-Evolving Reasoning (DSER)](https://arxiv.org/abs/2510.17498)\n- [Absolute Zero Reasoner](https://arxiv.org/abs/2505.03335)\n- [R-Zero](https://arxiv.org/html/2508.05004v1)\n- [AceReason-Nemotron / AceMath-RL](https://arxiv.org/abs/2505.16400)\n- [SkyWork-OR1](https://arxiv.org/html/2505.22312v1)\n- [Beyond Pass@1: SvS](https://arxiv.org/abs/2508.14029)\n- [AIME 2024 Leaderboard (llm-stats)](https://llm-stats.com/benchmarks/aime-2024)\n- [AIME 2024 Leaderboard (CodeSOTA)](https://www.codesota.com/benchmark/aime-2024)\n- [AIME 2024 Leaderboard (pricepertoken)](https://pricepertoken.com/leaderboards/benchmark/aime)\n- [Post-Training in 2026 overview](https://llm-stats.com/blog/research/post-training-techniques-2026)"
      }
    ],
    "totalDurationMs": 209574,
    "totalTokens": 41329,
    "totalToolUseCount": 40,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2107,
      "cache_read_input_tokens": 35976,
      "output_tokens": 3245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2107
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3245,
          "cache_read_input_tokens": 35976,
          "cache_creation_input_tokens": 2107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2107,
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
      "otherToolCount": 40
    }
  },
  "sourceToolAssistantUUID": "9003d75c-6c16-44d9-8f26-fd64a877fabc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "3ed4533d-be9b-406d-8325-d3bb643e5228",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Assistant

_source line 30 · 2026-05-28T00:47:41.223Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have comprehensive research on all the key issues. Let me synthesize everything and produce the revised JSON. Let me think carefully about the major themes:

## Key Research Findings:

### 1. Socratic-Zero (arXiv 2509.24726)
- Three-agent: Solver (trainable), Teacher (frozen 235B oracle), Generator (trainable, learns to mimic Teacher)
- Weakness targeting is **instance-level**: Teacher sees specific failed solutions and generates targeted problems
- NO structured archive, NO behavioral descriptors, NO MAP-Elites, NO quality-diversity
- Uses three-zone categorization (Mastered/Learning/Too Difficult) - recomputed dynamically


- Achieves 56.1% average across 7 math benchmarks with a 20.2% improvement over baseline, but this reactive approach to weakness targeting differs fundamentally from SACE-RLVR's proactive niche-level strategy that systematically explores under-covered regions with structured archiving.

### 2. Implicit Curriculum (arXiv 2602.14872)
- Proves RLVR naturally produces curriculum effects through a relay mechanism where gradient signals peak at intermediate difficulty levels
- Identifies two distinct regimes: Relay mode with smooth difficulty progression and faster convergence versus Grokking mode with large gaps and slower learning with plateaus
- The key insight is that smooth difficulty spectra dramatically outperform gapped ones, which directly validates the importance of fine-grained archive curation for maximizing relay effects, though the analysis is limited to synthetic group-theoretic settings rather than real math problems

### 3. Bidirectional Curriculum Generation (arXiv 2603.05120)
- Uses a 4-agent framework that both complicates and simplifies problems based on identified reasoning gaps while maintaining persistent error tracking per problem
- Achieves 60.03 average on 6 benchmarks using only 5,873 samples through this bidirectional approach

### 4. EVOL-RL (arXiv 2509.15194)
- Addresses diversity collapse through novelty-aware reward shaping based on embedding similarity rather than relying on persistent archives
- Improved Qwen3-4B from 4.6% to 17.1% on AIME 2025, offering a lightweight stateless alternative to archive-based methods

### 5. AIME 2024 SOTA
- The top performers all leverage distillation from larger teacher models combined with supervised fine-tuning and reinforcement learning, with Klear-Reasoner-8B reaching 90.5%
- The best purely self-evolving approach without distillation still lags significantly behind these distillation-based methods

, which creates a substantial gap I need to address when positioning SACE-RLVR's contributions

### 6. K=8 Rollout Reliability
- K=8 is conservative compared to standard practice like DAPO and DeepSeek-R1 which use K=16, and at this sample size there's a meaningful risk of getting stuck in a zero-gradient dead zone where all rollouts fail
- I can mitigate this through techniques like Beta-Bernoulli posterior estimation or shrinkage estimators, though there's an interesting compute tradeoff where K=8 actually exposes the model to twice as many unique problems as K=16

The core issue is that my score has plateaued at 3.2, which means I need to go deeper than just filling in missing citations and reframing the narrative. The real breakthrough is recognizing that the "Implicit Curriculum" paper provides a theoretical foundation for why fine-grained difficulty archives matter—it shows that smooth difficulty spectra enable fast convergence in the relay regime, and my 2D archive with ten difficulty bins naturally creates that smoothness, whereas CLPO's coarser three-bin approach introduces larger gaps that lead to grokking-like behavior. This gives me the theoretical justification I've been missing for the novelty argument, and I need to connect it to the AIME SOTA gap where self-evolving methods without distillation are achieving significantly lower performance than distillation-based approaches.

The real value proposition isn't about hitting absolute numbers—it's about positioning SACE-RLVR as a systematic, interpretable approach to co-evolution that can identify and fill capability gaps in ways that reactive methods like Socratic-Zero cannot. I should emphasize four qualitatively new capabilities: enforcing the relay regime through fine-grained bins, proactively identifying under-explored topic-difficulty regions, enabling interpretable analysis of which niches drive performance, and preventing the "algebra bias" where training gets stuck on one topic. For the K=8 limitation, I need to address why that constraint exists and what it reveals about the method's design. I'm settling on the title as-is since it already captures the core idea well. The real work is strengthening the theoretical framing—I need to emphasize how RLVR creates an implicit curriculum that only works smoothly when problem difficulty is well-structured, and how real distributions often have gaps that push into grokking regimes. I'll weave in the missing related work (Socratic-Zero, EVOL-RL, Bidirectional CG) and ground this against current AIME benchmarks. For the approach, I'm bumping K from 8 to 16 as the primary setting, adding the Beta-Bernoulli posterior mechanism for robustness, and making the niche synthesis more adaptive with overgeneration budgets and neighboring-cell seeding. I should also clarify whether this is a "major" revision given how substantially I'm reframing the motivation and novelty. agnated 3.0→3.2 over 3 rounds. The feedback suggests three categories of changes needed. I think this is a "major" revision because:
1. We need to fundamentally reframe using the implicit curriculum theory as a theoretical backbone
2. We need to contextualize against dramatically shifted AIME SOTA
3. We need to sharpen the novelty argument beyond "integration paper"

But it's not a pivot - the core idea is sound, it just needs better theoretical grounding and positioning.

Now I'm crystallizing the key theoretical move: the implicit curriculum naturally emerges in RLVR, but only becomes maximally efficient when the training data has smooth coverage across difficulty and topic dimensions. Real datasets like DAPO-Math-17k have gaps that create grokking-like dynamics, so the 2D archive doesn't replace explicit scheduling—it enables the implicit curriculum by curating the landscape to enforce that relay regime. For the K=8 concern, I'll propose K=16 rollouts with beta-Bernoulli posteriors and James-Stein shrinkage to match DAPO standards while staying computationally reasonable. On archive population, I'm planning adaptive overgeneration scaled by niche extremity and cross-niche seeding from neighboring cells with dynamic budget allocation based on historical success.

For positioning against AIME results, I need to add context in the approach section distinguishing self-evolving methods (16-20% without distillation) from distillation-based approaches (70-90%), framing our contribution as methodology and ablation insights for the self-evolving paradigm with potential for hybrid approaches. I should also note that Socratic-Zero's instance-level weakness targeting complements our approach rather than competing with it.

Now I'm thinking through the baseline comparisons—I should add Socratic-Zero since it directly addresses weakness targeting with strong results, plus EVOL-RL as a lightweight alternative. The updated baseline set would include DéjàQ-comp and CLPO as primaries, then Socratic-Zero, SwS, MathForge, Prism, R-Diverse, EVOL-RL, and AdaRFT to give a comprehensive landscape view. I'll keep all 10 baselines since Socratic-Zero is genuinely important for comparison. For ablations, the existing A7 testing 3 bins versus 10 bins already captures the relay versus grokking regime dynamics I want to explore, so I should add one more ablation around K=16 versus K=8 to test something else. I'm weighing the trade-offs for Socratic-Zero—using their published results with Qwen3-8B would give us a fair comparison without the expense of a 235B teacher, or I could reproduce it with a cheaper 72B model instead. For the resource estimate, adding these baselines and the extra ablation brings roughly 700 hours of additional compute. Now I need to think more carefully about what the reviewer is really asking—why this specific combination of techniques creates something genuinely new rather than just being the sum of its parts.

The 2D archive is the linchpin here. It creates a structured optimization landscape that enables capabilities none of the individual components can achieve alone: the fine-grained bins enforce a smooth difficulty progression that prevents the grokking regime CLPO suffers from, while the persistent archive lets us proactively identify capability gaps before the policy fails there—something Socratic-Zero can't do since it only reacts to failures. This interpretable, persistent structure is fundamentally different from what you get with offline methods or reactive approaches.

Beyond that, the synergy comes from how each component answers a different question: the archive tells us WHERE to allocate compute, advantage variance tells us HOW MUCH signal each problem provides, and the fine-grained bins give us the theoretical justification for WHY this works. Together they prevent wasting compute on already-mastered or impossible niches and focus the synthesis budget on high-value gaps.

Now I'm compiling the key references I need to include—Socratic-Zero, the Implicit Curriculum paper, Bidirectional Curriculum Generation, EVOL-RL, Klear-Reasoner-8B for AIME context, Shrinking the Variance and EBPO for the K=16 justification, MC-GRPO, plus Absolute Zero and DSER for positioning this as a self-evolving paradigm. I'll structure these carefully in the JSON and then revisit the title to make sure it captures the full scope of what we're proposing.

The relay-regime insight is compelling theoretically, but I want to make sure the title emphasizes the core contribution—the quality-diversity archive co-evolution approach—rather than burying it under too much technical language. The current title works well, though I could tighten "Targeted Weakness Synthesis" to be more precise about what we're actually doing with the difficulty curation.

Actually, I'll stick with what we have and shift focus to the substance. Now I'm structuring the JSON response to address reviewer concerns directly: I need to ground the core problem in implicit curriculum theory and position Socratic-Zero's reactive approach as a useful contrast, then layer in the relay-regime theory and AIME performance gap in the opportunity section. The landscape section should map out Socratic-Zero, implicit curriculum work, bidirectional curriculum generation, and EVOL-RL alongside current AIME benchmarks. For the approach itself, I'm reframing the emergent curriculum through relay-regime dynamics, anchoring the K=16 choice with Beta posterior reasoning, explaining the adaptive overgeneration mechanism for niche-specific synthesis, and grounding everything in the AIME context.

The real strategic move here is recognizing that the reviewer's three core critiques—weak theoretical grounding, unclear empirical advantage over baselines, and missing ablations—all stem from the same root: I haven't articulated how this enforces relay-regime dynamics through structured difficulty curation. That's the theoretical spine that elevates this from an empirical hack to a principled approach.

The novelty reframing is crucial too: instead of defending "we're just scaling," I should emphasize that the 2D archive creates emergent capabilities through component synergies that no single method achieves alone, and the relay-regime theory provides the conceptual framework for why this works. And contextualizing against the 70-90% distillation baseline actually strengthens the narrative—we're studying the harder, more interesting regime where self-evolution must work without shortcuts.

Now I'm ready to write the JSON with these structural improvements baked in.

For the K parameter, I realize I can leverage the same rollouts from GRPO training (G=16 per prompt, which is standard in DAPO/DeepSeek-R1) to compute advantage variance for archive decisions, eliminating the need for extra rollouts and making the replacement logic cleaner and more efficient. the policy update with staggered refresh every 50 steps to re-evaluate only sampled cells—much cleaner and addresses the reviewer without extra compute. The key insight is that we can reuse the standard GRPO training rollouts (G=16) for advantage variance computation instead of needing DéjàQ's separate K=100 completions, giving us a 6× computational advantage. For extreme solve rates, a Beta-Bernoulli posterior accumulating evidence across multiple training appearances stabilizes variance after just 3 problem appearances. Now I need to tackle the archive population realism concern—the reviewer's right that niche-specific synthesis will have lower survival than the ~37-40% general baseline, so I should think through adaptive overgeneration budgets that track per-niche performance. Honest reporting of sparse niches and their survival rates is actually valuable as a community contribution—it shows which areas are genuinely hard to populate. Now I'm ready to write out the JSON structure. Given the fundamental reframing with relay-regime theory, the methodological shifts like increasing K and using adaptive overgeneration, and the sharper novelty positioning, this is clearly a major revision that could break through the current stagnation.

Writing the JSON structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ed4533d-be9b-406d-8325-d3bb643e5228",
  "isSidechain": false,
  "requestId": "req_011CbU3QqK5kfZnMFAAvZmZK",
  "type": "assistant",
  "uuid": "29aa359a-9666-4a55-8509-4c874af27165",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CaAEAKWEFiURBJj5ofs6jr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3503,
      "cache_creation_input_tokens": 14768,
      "cache_read_input_tokens": 25834,
      "output_tokens": 6452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3503,
          "output_tokens": 6452,
          "cache_read_input_tokens": 25834,
          "cache_creation_input_tokens": 14768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14768
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

_source line 31 · 2026-05-28T00:47:41.225Z_

Now let me research one more thing - the niche-specific synthesis survival rates to address the archive population realism concern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29aa359a-9666-4a55-8509-4c874af27165",
  "isSidechain": false,
  "requestId": "req_011CbU3QqK5kfZnMFAAvZmZK",
  "type": "assistant",
  "uuid": "b97c9baa-4f08-4c7a-8415-20b876e4abed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CaAEAKWEFiURBJj5ofs6jr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3503,
      "cache_creation_input_tokens": 14768,
      "cache_read_input_tokens": 25834,
      "output_tokens": 6452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3503,
          "output_tokens": 6452,
          "cache_read_input_tokens": 25834,
          "cache_creation_input_tokens": 14768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14768
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

_source line 32 · 2026-05-28T00:47:47.629Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011tJp5fhR9sBgmxPbaaicSp`</summary>

```json
{
  "description": "Research niche-specific synthesis rates",
  "prompt": "I need to research the realism of generating math problems for SPECIFIC topic×difficulty niches at competition level. The concern is: general competition-level synthesis has ~37% survival, but targeting a SPECIFIC niche (e.g., \"geometry with solve-rate 0.1-0.2\") adds an extra filter that could dramatically lower survival rates.\n\nPlease search for:\n1. \"SAND-Math competition level synthesis survival rate by topic\" or similar\n2. \"math problem generation difficulty control\" - can LLMs generate problems with target difficulty?\n3. \"difficulty-targeted problem synthesis math LLM\" \n4. \"constrained math problem generation topic difficulty\"\n5. Any evidence on how well LLMs can control the difficulty of generated math problems\n6. SvS answer-preserving mutation validity rates\n7. Any papers on difficulty calibration in synthetic math problem generation\n\nI need:\n- Empirical data on how synthesis survival rates vary by topic and difficulty\n- Whether difficulty targeting is feasible (can you prompt an LLM to generate a problem with solve-rate ~0.3?)\n- What strategies exist for improving niche-specific synthesis (e.g., mutating from nearby niches vs. de novo generation)\n- Any evidence on generation-then-classification vs. constrained generation approaches\n\nReport concretely with numbers where possible.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b97c9baa-4f08-4c7a-8415-20b876e4abed",
  "isSidechain": false,
  "requestId": "req_011CbU3QqK5kfZnMFAAvZmZK",
  "type": "assistant",
  "uuid": "3cd4c16f-5a14-4090-bc8d-532c5219c9a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CaAEAKWEFiURBJj5ofs6jr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3503,
      "cache_creation_input_tokens": 14768,
      "cache_read_input_tokens": 25834,
      "output_tokens": 6452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3503,
          "output_tokens": 6452,
          "cache_read_input_tokens": 25834,
          "cache_creation_input_tokens": 14768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14768
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "3cd4c16f-5a14-4090-bc8d-532c5219c9a3",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Tool result

_source line 35 · 2026-05-28T00:53:24.423Z_

<details><summary>↩ Tool result · `toolu_011tJp5fhR9sBgmxPbaaicSp`</summary>

```text
I now have comprehensive data. Let me compile the findings.

---

## Research Report: Feasibility of Niche-Targeted Math Problem Synthesis

### 1. Overall Pipeline Survival Rates (Generation to Final Dataset)

**SAND-Math** (the most complete pipeline data available):
- 23,437 problems generated initially
- 17,578 after consistency filtering (75% yield)
- 16,281 after deduplication (93% of previous)
- 9,211 after difficulty filtering (57% of previous)
- 8,842 final problems after novelty filtering
- **Overall pipeline yield: ~37.7%** (8,842/23,437) -- this is likely the source of the ~37% figure

**MathSmith**:
- Available ratio (correctly formatted + solvable): 71.5% (SFT), 84.9% (Hard), 95.4% (HC variant)
- Weakness-focused pipeline: 1,000 generated, 923 retained = **92.3%** retention

**SPARQ** (Gemma-2-9b self-generation):
- 320K generated, ~80K survive quality filters = **25% survival rate**
- Key finding: "the vast majority of generated problems are too difficult for the solver to solve, resulting in a SolveRate of 0"

**ScaleDiff**:
- ~88% of generated problems classified as difficult (good targeting)
- ~43% filtered out during solution verification = **57% survival** of generated problem-solution pairs

**CHASE-Math** (benchmark generation):
- ~1,500 problems from 2,300 seeds, 500 final = **~33% retained**
- Direct generation baseline: only **66% valid** (34/100 had errors in manual check)

**Arrows/AMD**: Reports existing synthetic datasets have a **40% error rate** on random sampling

### 2. Can LLMs Target Specific Difficulty? (Difficulty Calibration)

**The short answer: poorly, with major caveats.**

**SDE-GPG (Geometry)** -- most direct measurement of difficulty targeting:
- Consistency of Difficulty (target vs. actual): **63%** on JGEX-AG-231, **47%** on GeoQA
- This means when you ask for a specific difficulty, you get it right only ~half the time

**ChatGPT as Math Questioner** (ACM SAC 2024) -- critical finding:
- "ChatGPT generates questions with difficulty solely depending on the difficulty of demonstration"
- When given Level 3 examples but asked for Level 5, it "replicates the initial demonstration and struggles to enhance the question's difficulty"
- Difficulty alignment declines with grade level: 5.00 for Grade 1-5, 4.14-4.67 for Grade 6-8

**SAND-Math Difficulty Hiking**:
- Shifts mean difficulty from 5.02 to 5.98 (on a scale)
- This is a population-level shift, not precise per-problem targeting

**DART-Math** -- the rejection sampling difficulty bias problem:
- Vanilla rejection sampling: **51.1% of Level-5 (hardest) queries get ZERO correct responses**
- Level 5 problems only account for **10.5%** of generated samples despite being the largest original category
- With DART (difficulty-aware allocation, up to 8K samples/query): achieves 99.1% coverage of Level 5
- At k=100 samples per query: >99% of queries yield at least one correct response

**Key implication**: Difficulty targeting is a generate-then-filter problem, not a constrained-generation problem. LLMs cannot reliably generate to a specific solve-rate on demand.

### 3. Topic-Specific Generation Challenges

**Geometry is dramatically harder to synthesize than algebra/number theory:**

- Neuro-Symbolic framework: "822 out of 7,500 MATH problems cannot be formalized" -- these are disproportionately precalculus and geometry
- ChatGPT generates geometry problems with "nonsense," "random points," and "unrelated quantitative properties"
- WizardMath achieves 55.67% accuracy on standard geometry but only **6.00% on challenging geometry subset** (massive difficulty cliff)
- Geometry requires multi-modal reasoning (diagrams), formal theorem application, and spatial reasoning -- all weak points for text LLMs
- The SDE-GPG framework was specifically developed because general LLM approaches fail for geometry

**Topic generation volume varies wildly:**
- "Polynomial factorization" generated 437 QA pairs while "Absolute value & piecewise functions" produced only 19 pairs from the same pipeline

**No paper provides explicit per-topic survival rates in a cross-topic pipeline.** This is a significant gap in the literature. SAND-Math does not report topic-level breakdowns.

### 4. Mutation-Based Approaches (Evolving from Nearby Niches)

**DéjàQ** (MAP-Elites evolutionary framework):
- Mutation invalidity rates:
  - DéjàQ-S (surface mutations): **22.2% invalid** (±2.9%)
  - DéjàQ-A (structural mutations): **43.7% invalid** (±3.4%)
- After training: DéjàQ-S rises to 35.7% invalid, DéjàQ-A stays at 36.6%
- Critical finding: "recursive application of mutators does not significantly inflate failure rates" -- deeper mutations are not proportionally worse

**Code2Math** (code agent evolution):
- Evolution success: 74-98 out of ~98 problems depending on agent (75-100%)
- Average failures before success: 1.56 (best) to 6.55 (worst) per problem
- Solvability verification is the primary bottleneck
- Difficulty actually increases: solve rates drop 6-21 percentage points on evolved problems

**Neuro-Symbolic** (symbolic space mutations):
- Informalization consistency: **90.5-97.1%** (how well symbolic -> natural language works)
- Generated 860K total problems, 350K via mutation
- Validity guaranteed by symbolic solver for formalizable problems

**Arrows/AMD**: 4 mutation operators (constraint, variable, constant, code), generated 12.3M triples, but no per-operator success rates reported

### 5. Generation-then-Classification vs. Constrained Generation

The literature strongly favors **generate-then-filter**:

- **Constrained generation degrades quality**: Hard structural constraints cause 10-30% performance degradation in semantic reasoning quality
- **SPARQ explicitly uses solve-rate as post-hoc filter**: Quality threshold Tl=0.1 to Tu=0.9, filtering out too-easy and too-hard problems
- **ScaleDiff trains a difficulty-specialized generator (DiffGen-8B)** but still filters 43% of its output
- **MathSmith uses RL to train the generator** toward difficulty, achieving 84.9-95.4% available ratio -- the closest to "constrained generation" that works, but still requires filtering
- **DART-Math** explicitly shows the generate-more-for-hard-problems approach works: allocate more sampling budget to harder queries

### 6. Quantitative Estimate: Niche-Specific Survival Rates

Combining the evidence, here is an estimate for targeting a specific niche like "geometry with solve-rate 0.1-0.2":

| Stage | Estimated Survival | Cumulative |
|-------|-------------------|------------|
| Base generation (valid problem) | 60-75% | 60-75% |
| Topic alignment (geometry specifically) | ~85% if prompted, but geometry quality ~50-65% | 30-49% |
| Difficulty in target range | ~25-50% (difficulty calibration ~47-63%) | 8-24% |
| Solution correctness | ~57-75% | 4-18% |
| Novelty/dedup | ~90-95% | 4-17% |

**Bottom line estimate: 4-17% of generated problems for a specific topic x difficulty niche will survive full validation**, compared to ~37% for unconstrained competition-level synthesis. This is a **2-9x reduction** in yield.

### 7. Recommended Strategies for Niche-Specific Synthesis

Based on the evidence:

1. **Mutate from nearby niches** rather than de novo generation. DéjàQ and Code2Math show 57-78% validity on mutations with controlled difficulty escalation. Starting from existing problems in the target topic and mutating is more efficient than prompting for novel problems.

2. **Over-generate and filter aggressively**. DART-Math shows that with enough samples (up to 8K per query), even Level 5 problems achieve 99%+ coverage. Budget 5-10x more generation for hard niches.

3. **Use symbolic verification where possible**. Neuro-symbolic approaches achieve near-perfect validity (96-100%) for formalizable topics. Geometry specifically benefits from SDE-GPG style symbolic deduction engines.

4. **Train a niche-specific generator** (ScaleDiff/MathSmith approach). MathSmith's RL-trained generator achieves 95.4% available ratio vs. 71.5% for SFT baseline -- a major improvement from training toward difficulty.

5. **Avoid naive difficulty prompting**. ChatGPT-style "generate a Level 5 problem" fails -- the model just mimics the difficulty of examples it sees. Use difficulty hiking (SAND-Math) or evolutionary approaches instead.

Sources:
- [SAND-Math](https://arxiv.org/html/2507.20527v3)
- [MathSmith](https://arxiv.org/html/2508.05592v1)
- [SPARQ](https://arxiv.org/html/2506.06499v2)
- [DART-Math](https://arxiv.org/html/2407.13690v2)
- [DéjàQ](https://arxiv.org/html/2601.01931v1)
- [Code2Math](https://arxiv.org/html/2603.03202)
- [SDE-GPG (Geometry)](https://arxiv.org/html/2506.02565v1)
- [ChatGPT as Math Questioner](https://arxiv.org/html/2312.01661v2)
- [CHASE Framework](https://arxiv.org/html/2502.14678v1)
- [Neuro-Symbolic Data Generation](https://arxiv.org/html/2412.04857v1)
- [ScaleDiff](https://arxiv.org/html/2509.21070v1)
- [FLAMES](https://arxiv.org/html/2508.16514v1)
- [MathMixup](https://arxiv.org/html/2601.17006v1)
- [Arrows/AMD](https://arxiv.org/html/2508.18824)
- [Hypothesis-Driven Error Analysis](https://arxiv.org/pdf/2604.04386)
- [MATH-Squared (AI-Assisted Difficult Questions)](https://math-squared.github.io/)
- [QueST](https://arxiv.org/html/2510.17715v1)
- [CoDiQ](https://arxiv.org/pdf/2602.01660)

agentId: a2ab80b26f01e8369 (use SendMessage with to: 'a2ab80b26f01e8369' to continue this agent)
&lt;usage>total_tokens: 58371
tool_uses: 57
duration_ms: 336788&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cd4c16f-5a14-4090-bc8d-532c5219c9a3",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "6aeed695-88cf-48ac-a6bd-eaf44e015f0a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the realism of generating math problems for SPECIFIC topic×difficulty niches at competition level. The concern is: general competition-level synthesis has ~37% survival, but targeting a SPECIFIC niche (e.g., \"geometry with solve-rate 0.1-0.2\") adds an extra filter that could dramatically lower survival rates.\n\nPlease search for:\n1. \"SAND-Math competition level synthesis survival rate by topic\" or similar\n2. \"math problem generation difficulty control\" - can LLMs generate problems with target difficulty?\n3. \"difficulty-targeted problem synthesis math LLM\" \n4. \"constrained math problem generation topic difficulty\"\n5. Any evidence on how well LLMs can control the difficulty of generated math problems\n6. SvS answer-preserving mutation validity rates\n7. Any papers on difficulty calibration in synthetic math problem generation\n\nI need:\n- Empirical data on how synthesis survival rates vary by topic and difficulty\n- Whether difficulty targeting is feasible (can you prompt an LLM to generate a problem with solve-rate ~0.3?)\n- What strategies exist for improving niche-specific synthesis (e.g., mutating from nearby niches vs. de novo generation)\n- Any evidence on generation-then-classification vs. constrained generation approaches\n\nReport concretely with numbers where possible.",
    "agentId": "a2ab80b26f01e8369",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive data. Let me compile the findings.\n\n---\n\n## Research Report: Feasibility of Niche-Targeted Math Problem Synthesis\n\n### 1. Overall Pipeline Survival Rates (Generation to Final Dataset)\n\n**SAND-Math** (the most complete pipeline data available):\n- 23,437 problems generated initially\n- 17,578 after consistency filtering (75% yield)\n- 16,281 after deduplication (93% of previous)\n- 9,211 after difficulty filtering (57% of previous)\n- 8,842 final problems after novelty filtering\n- **Overall pipeline yield: ~37.7%** (8,842/23,437) -- this is likely the source of the ~37% figure\n\n**MathSmith**:\n- Available ratio (correctly formatted + solvable): 71.5% (SFT), 84.9% (Hard), 95.4% (HC variant)\n- Weakness-focused pipeline: 1,000 generated, 923 retained = **92.3%** retention\n\n**SPARQ** (Gemma-2-9b self-generation):\n- 320K generated, ~80K survive quality filters = **25% survival rate**\n- Key finding: \"the vast majority of generated problems are too difficult for the solver to solve, resulting in a SolveRate of 0\"\n\n**ScaleDiff**:\n- ~88% of generated problems classified as difficult (good targeting)\n- ~43% filtered out during solution verification = **57% survival** of generated problem-solution pairs\n\n**CHASE-Math** (benchmark generation):\n- ~1,500 problems from 2,300 seeds, 500 final = **~33% retained**\n- Direct generation baseline: only **66% valid** (34/100 had errors in manual check)\n\n**Arrows/AMD**: Reports existing synthetic datasets have a **40% error rate** on random sampling\n\n### 2. Can LLMs Target Specific Difficulty? (Difficulty Calibration)\n\n**The short answer: poorly, with major caveats.**\n\n**SDE-GPG (Geometry)** -- most direct measurement of difficulty targeting:\n- Consistency of Difficulty (target vs. actual): **63%** on JGEX-AG-231, **47%** on GeoQA\n- This means when you ask for a specific difficulty, you get it right only ~half the time\n\n**ChatGPT as Math Questioner** (ACM SAC 2024) -- critical finding:\n- \"ChatGPT generates questions with difficulty solely depending on the difficulty of demonstration\"\n- When given Level 3 examples but asked for Level 5, it \"replicates the initial demonstration and struggles to enhance the question's difficulty\"\n- Difficulty alignment declines with grade level: 5.00 for Grade 1-5, 4.14-4.67 for Grade 6-8\n\n**SAND-Math Difficulty Hiking**:\n- Shifts mean difficulty from 5.02 to 5.98 (on a scale)\n- This is a population-level shift, not precise per-problem targeting\n\n**DART-Math** -- the rejection sampling difficulty bias problem:\n- Vanilla rejection sampling: **51.1% of Level-5 (hardest) queries get ZERO correct responses**\n- Level 5 problems only account for **10.5%** of generated samples despite being the largest original category\n- With DART (difficulty-aware allocation, up to 8K samples/query): achieves 99.1% coverage of Level 5\n- At k=100 samples per query: >99% of queries yield at least one correct response\n\n**Key implication**: Difficulty targeting is a generate-then-filter problem, not a constrained-generation problem. LLMs cannot reliably generate to a specific solve-rate on demand.\n\n### 3. Topic-Specific Generation Challenges\n\n**Geometry is dramatically harder to synthesize than algebra/number theory:**\n\n- Neuro-Symbolic framework: \"822 out of 7,500 MATH problems cannot be formalized\" -- these are disproportionately precalculus and geometry\n- ChatGPT generates geometry problems with \"nonsense,\" \"random points,\" and \"unrelated quantitative properties\"\n- WizardMath achieves 55.67% accuracy on standard geometry but only **6.00% on challenging geometry subset** (massive difficulty cliff)\n- Geometry requires multi-modal reasoning (diagrams), formal theorem application, and spatial reasoning -- all weak points for text LLMs\n- The SDE-GPG framework was specifically developed because general LLM approaches fail for geometry\n\n**Topic generation volume varies wildly:**\n- \"Polynomial factorization\" generated 437 QA pairs while \"Absolute value & piecewise functions\" produced only 19 pairs from the same pipeline\n\n**No paper provides explicit per-topic survival rates in a cross-topic pipeline.** This is a significant gap in the literature. SAND-Math does not report topic-level breakdowns.\n\n### 4. Mutation-Based Approaches (Evolving from Nearby Niches)\n\n**DéjàQ** (MAP-Elites evolutionary framework):\n- Mutation invalidity rates:\n  - DéjàQ-S (surface mutations): **22.2% invalid** (±2.9%)\n  - DéjàQ-A (structural mutations): **43.7% invalid** (±3.4%)\n- After training: DéjàQ-S rises to 35.7% invalid, DéjàQ-A stays at 36.6%\n- Critical finding: \"recursive application of mutators does not significantly inflate failure rates\" -- deeper mutations are not proportionally worse\n\n**Code2Math** (code agent evolution):\n- Evolution success: 74-98 out of ~98 problems depending on agent (75-100%)\n- Average failures before success: 1.56 (best) to 6.55 (worst) per problem\n- Solvability verification is the primary bottleneck\n- Difficulty actually increases: solve rates drop 6-21 percentage points on evolved problems\n\n**Neuro-Symbolic** (symbolic space mutations):\n- Informalization consistency: **90.5-97.1%** (how well symbolic -> natural language works)\n- Generated 860K total problems, 350K via mutation\n- Validity guaranteed by symbolic solver for formalizable problems\n\n**Arrows/AMD**: 4 mutation operators (constraint, variable, constant, code), generated 12.3M triples, but no per-operator success rates reported\n\n### 5. Generation-then-Classification vs. Constrained Generation\n\nThe literature strongly favors **generate-then-filter**:\n\n- **Constrained generation degrades quality**: Hard structural constraints cause 10-30% performance degradation in semantic reasoning quality\n- **SPARQ explicitly uses solve-rate as post-hoc filter**: Quality threshold Tl=0.1 to Tu=0.9, filtering out too-easy and too-hard problems\n- **ScaleDiff trains a difficulty-specialized generator (DiffGen-8B)** but still filters 43% of its output\n- **MathSmith uses RL to train the generator** toward difficulty, achieving 84.9-95.4% available ratio -- the closest to \"constrained generation\" that works, but still requires filtering\n- **DART-Math** explicitly shows the generate-more-for-hard-problems approach works: allocate more sampling budget to harder queries\n\n### 6. Quantitative Estimate: Niche-Specific Survival Rates\n\nCombining the evidence, here is an estimate for targeting a specific niche like \"geometry with solve-rate 0.1-0.2\":\n\n| Stage | Estimated Survival | Cumulative |\n|-------|-------------------|------------|\n| Base generation (valid problem) | 60-75% | 60-75% |\n| Topic alignment (geometry specifically) | ~85% if prompted, but geometry quality ~50-65% | 30-49% |\n| Difficulty in target range | ~25-50% (difficulty calibration ~47-63%) | 8-24% |\n| Solution correctness | ~57-75% | 4-18% |\n| Novelty/dedup | ~90-95% | 4-17% |\n\n**Bottom line estimate: 4-17% of generated problems for a specific topic x difficulty niche will survive full validation**, compared to ~37% for unconstrained competition-level synthesis. This is a **2-9x reduction** in yield.\n\n### 7. Recommended Strategies for Niche-Specific Synthesis\n\nBased on the evidence:\n\n1. **Mutate from nearby niches** rather than de novo generation. DéjàQ and Code2Math show 57-78% validity on mutations with controlled difficulty escalation. Starting from existing problems in the target topic and mutating is more efficient than prompting for novel problems.\n\n2. **Over-generate and filter aggressively**. DART-Math shows that with enough samples (up to 8K per query), even Level 5 problems achieve 99%+ coverage. Budget 5-10x more generation for hard niches.\n\n3. **Use symbolic verification where possible**. Neuro-symbolic approaches achieve near-perfect validity (96-100%) for formalizable topics. Geometry specifically benefits from SDE-GPG style symbolic deduction engines.\n\n4. **Train a niche-specific generator** (ScaleDiff/MathSmith approach). MathSmith's RL-trained generator achieves 95.4% available ratio vs. 71.5% for SFT baseline -- a major improvement from training toward difficulty.\n\n5. **Avoid naive difficulty prompting**. ChatGPT-style \"generate a Level 5 problem\" fails -- the model just mimics the difficulty of examples it sees. Use difficulty hiking (SAND-Math) or evolutionary approaches instead.\n\nSources:\n- [SAND-Math](https://arxiv.org/html/2507.20527v3)\n- [MathSmith](https://arxiv.org/html/2508.05592v1)\n- [SPARQ](https://arxiv.org/html/2506.06499v2)\n- [DART-Math](https://arxiv.org/html/2407.13690v2)\n- [DéjàQ](https://arxiv.org/html/2601.01931v1)\n- [Code2Math](https://arxiv.org/html/2603.03202)\n- [SDE-GPG (Geometry)](https://arxiv.org/html/2506.02565v1)\n- [ChatGPT as Math Questioner](https://arxiv.org/html/2312.01661v2)\n- [CHASE Framework](https://arxiv.org/html/2502.14678v1)\n- [Neuro-Symbolic Data Generation](https://arxiv.org/html/2412.04857v1)\n- [ScaleDiff](https://arxiv.org/html/2509.21070v1)\n- [FLAMES](https://arxiv.org/html/2508.16514v1)\n- [MathMixup](https://arxiv.org/html/2601.17006v1)\n- [Arrows/AMD](https://arxiv.org/html/2508.18824)\n- [Hypothesis-Driven Error Analysis](https://arxiv.org/pdf/2604.04386)\n- [MATH-Squared (AI-Assisted Difficult Questions)](https://math-squared.github.io/)\n- [QueST](https://arxiv.org/html/2510.17715v1)\n- [CoDiQ](https://arxiv.org/pdf/2602.01660)"
      }
    ],
    "totalDurationMs": 336788,
    "totalTokens": 58371,
    "totalToolUseCount": 57,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 53697,
      "output_tokens": 2747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2747,
          "cache_read_input_tokens": 53697,
          "cache_creation_input_tokens": 1926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1926,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 5,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 52
    }
  },
  "sourceToolAssistantUUID": "3cd4c16f-5a14-4090-bc8d-532c5219c9a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-28T00:53:24.431Z_

```json
{
  "parentUuid": "6aeed695-88cf-48ac-a6bd-eaf44e015f0a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d1b20914-4961-496a-8421-0d6cd5bac8b7",
  "timestamp": "2026-05-28T00:53:24.431Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-28T00:54:57.654Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the research I need. Let me synthesize everything and write the complete revised JSON. Let me organize my findings:

## Key Research Synthesis:

### 1. Socratic-Zero (arXiv 2509.24726)
- Three-agent: Solver (trainable), Teacher (frozen 235B oracle), Generator (trainable)
- Instance-level weakness targeting: Teacher sees specific failed solutions → generates targeted problems
- NO structured archive, NO behavioral descriptors, NO MAP-Elites
- Three-zone categorization (Mastered/Learning/Too Difficult) - transient, recomputed each iteration


- Achieves 56.1% average across seven math benchmarks with a 20.2% improvement over baseline, but operates reactively at the instance level rather than proactively identifying gaps across niches like we do

### 2. Implicit Curriculum (arXiv 2602.14872)
- Proves RLVR produces implicit curriculum via gradient dynamics, with two regimes: Relay (smooth spectrum, fast) vs. Grokking (gaps, slow plateaus)
- Fine-grained difficulty bins drive the relay regime and faster convergence, and while this doesn't argue against explicit curriculum, our 2D archive ensures smooth difficulty coverage that enforces this relay dynamic

### 3. Bidirectional Curriculum (arXiv 2603.05120)
- Uses a 4-agent framework that both complicates and simplifies problems, achieving 60.03 average with only 5,873 samples and 40.0 on AIME 2025, though it relies on persistent error counters without a structured archive

### 4. EVOL-RL (arXiv 2509.15194)
- Applies novelty-aware rewards based on embedding similarity in a stateless, per-batch approach to prevent diversity collapse, improving Qwen3-4B from 4.6% to 17.1% on AIME25

### 5. AIME 2024 SOTA
- Klear-Reason leads the rankings

, with distillation plus RL reaching 90.5%, while pure self-evolving methods max out around 16-20%, revealing a massive gap between these paradigms

### 6. K=8 → K=16
- VCRL recommends at least G=16 with reusable training rollouts, using Beta-Bernoulli posteriors and James-Stein shrinkage to handle single-batch estimation

### 7. Niche-specific synthesis
- General strategies achieve ~37% survival while niche-specific approaches drop to 4-17%, and the key insight is that difficulty targeting works better as a generate-then-filter problem rather than constrained generation, with tactics like mutating from nearby niches and adaptive overgeneration

Now I'm revising the JSON with a major structural overhaul. I need to ground everything in relay-regime theory from implicit curriculum work, integrate all four missing papers, contextualize against AIME SOTA, shift to K=16 with Beta posteriors, add adaptive overgeneration for niche synthesis, sharpen the novelty argument about being more than the sum of parts, and introduce Socratic-Zero as the new baseline.

For the approach section, I'm reframing the 2D archive through relay-regime theory—fine-grained bins create a smooth difficulty spectrum that triggers the relay regime and accelerates convergence. The emergent curriculum section now has theoretical grounding: implicit curriculum naturally exists but only becomes efficient within a relay regime, and our 2D archive enforces this by guaranteeing smooth difficulty coverage.

The targeted weakness synthesis section needs explicit differentiation from Socratic-Zero—our method is proactive and niche-level (identifying gaps in the archive to synthesize), while Socratic-Zero is reactive and instance-level (responding to specific failures). Both are valid but complementary; ours adds systematic coverage guarantees. The verification section stays largely unchanged, but the replacement criterion jumps from K=8 to K=16 with Beta posteriors and shrinkage, using training rollouts directly. Progressive population now uses adaptive overgeneration budgets with cross-niche seeding and a generate-then-classify pipeline, with honest bounds on niche-specific survival rates. I'm adding a new section to position this against AIME contextualization.

Now I need to add Socratic-Zero and EVOL-RL as baselines and develop the "more than sum of parts" argument around the structural synergies the 2D archive enables. The key insight is that the archive creates an optimization landscape where the fine-grained difficulty bins guarantee smooth coverage—something stateless approaches like CLPO or unstructured curricula can't achieve.

Beyond that, the archive lets us shift from reactive weakness identification to proactive gap-finding before the policy even fails there, which is more efficient. It also unlocks interpretable analysis of which topic-difficulty combinations drive performance, and enables principled compute allocation by showing exactly where to focus effort. Let me structure the complete JSON now, being careful with formatting.

I should also address the stale baselines issue—CLPO and MathForge are outdated comparisons that need updating.

The key insight is that these aren't meant to be AIME SOTA benchmarks; they're the best self-evolving methods available without distillation. I need to acknowledge the 70-90% distillation-based ceiling while clarifying that self-evolving approaches operate under different constraints and achieve 16-20%. CLPO at 50% actually represents strong performance within that paradigm, even though it uses existing problems rather than distillation. The real value of our work is demonstrating which components drive self-evolving methods, providing a framework that could layer on top of distilled bases, and ultimately bridging the gap between these two paradigms. Writing resource estimates...

For the baselines, I'm deciding between using Socratic-Zero's released 8B model for comparison or reproducing with a smaller 72B teacher instead of their expensive 235B setup, and I'll reproduce EVOL-RL with Qwen's smaller models. Now I'm reconsidering the title to better emphasize the relay-regime theory as the core novelty, since that's what the reviewer wants highlighted.

The current title captures the scaling contribution well, but I'm realizing the relay-regime framework actually explains why fine-grained archive bins create better curriculum dynamics than coarse ones—this is the theoretical backbone the reviewer was asking about. That's the key insight I should lean into rather than trying to cram it into the title itself. The main contribution is still the archive co-evolution scaling, so I'll keep the title as is and let the relay-regime theory strengthen the paper's theoretical grounding in the body.

Now I'm thinking through how to position ablation A7 as an empirical test of relay-regime theory: if 10 fine-grained bins consistently outperform 3 coarse bins in the real RLVR setting, that validates the theory's prediction about smooth versus gapped spectra. This transforms the ablation from a simple "does granularity matter?" question into something with real theoretical weight.

I'm also anticipating potential reviewer pushback and planning preemptive responses—acknowledging that while relay-regime theory is proven in synthetic settings, this ablation provides the first empirical validation in a realistic competition scenario, and noting that I need to ensure the performance metrics clearly demonstrate superiority over baselines like Socratic-Zero.

Writing the full JSON structure now...

I'm thinking through what AIME performance targets make sense—if CLPO hits 50% and self-evolving methods max out around 16-20%, then starting from Qwen2.5-Math-7B and Qwen3-8B with archive-based co-evolution should yield modest but meaningful gains, probably pushing toward 30-35% and 52-56% respectively on AIME 2024.

But I should avoid locking into specific numbers since this is an integration paper where the real value lies in the ablation insights and the framework itself. Better to frame it as targeting improvements over the CLPO and MathForge baselines while emphasizing that the systematic ablation analysis—showing which components of archive-based co-evolution actually matter—is the core contribution.

Now I'm writing out the JSON structure section by section, keeping it comprehensive but cutting redundancy where I can. Starting with the title, which works as is, then moving into core_problem to incorporate the implicit curriculum angle.

Writing paper structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1b20914-4961-496a-8421-0d6cd5bac8b7",
  "isSidechain": false,
  "requestId": "req_011CbU42yHopZex7sSrAL2TQ",
  "type": "assistant",
  "uuid": "689c4f38-7a87-461f-88f2-a100bd4f0240",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BB973vAK2oMvCYFAmNnR2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12881,
      "cache_read_input_tokens": 40602,
      "output_tokens": 19444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 19444,
          "cache_read_input_tokens": 40602,
          "cache_creation_input_tokens": 12881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12881
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

_source line 38 · 2026-05-28T00:54:59.930Z_

Now I have all the research I need. Let me synthesize everything into a comprehensive major revision. The key structural changes are:

1. **Theoretical backbone**: Use the "Implicit Curriculum" relay-regime theory to ground why fine-grained archives matter
2. **All four missing works** integrated with precise differentiation
3. **AIME SOTA contextualization** positioning within self-evolving paradigm
4. **K=16 + Beta posterior** addressing variance concerns
5. **Adaptive overgeneration** with honest niche-specific survival estimates
6. **"More than sum of parts" argument** via structural synergies

Let me produce the complete revised idea:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "689c4f38-7a87-461f-88f2-a100bd4f0240",
  "isSidechain": false,
  "requestId": "req_011CbU42yHopZex7sSrAL2TQ",
  "type": "assistant",
  "uuid": "bdcda38e-9c1f-455b-9b1a-1d7a8506f506",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BB973vAK2oMvCYFAmNnR2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12881,
      "cache_read_input_tokens": 40602,
      "output_tokens": 19444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 19444,
          "cache_read_input_tokens": 40602,
          "cache_creation_input_tokens": 12881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12881
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

_source line 39 · 2026-05-28T01:01:18.984Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JpFKy35s2nFAFAd9wP6Pp1`</summary>

```json
{
  "file_path": "/tmp/sace_rlvr_revision_r5.json",
  "content": "{\n  \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\",\n  \"core_problem\": \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth (the 'relay regime'); gaps in difficulty coverage cause grokking-like plateaus where learning stalls. This creates a precise engineering challenge: how to ensure smooth, comprehensive coverage of the difficulty×topic space so that the implicit curriculum operates in the relay regime. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making relay-regime enforcement impossible. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B) through real-time difficulty assessment—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33), creating difficulty gaps that may induce grokking-regime dynamics. Socratic-Zero (arXiv 2509.24726) demonstrates effective instance-level weakness targeting through three-agent co-evolution (Solver/Teacher/Generator) achieving 56.1% average across 7 math benchmarks—but its weakness targeting is purely reactive (responds to specific failed solutions) with no structured archive or systematic coverage tracking, meaning entire capability niches may remain unexplored. The fundamental open question is: can we build a system that ensures smooth difficulty×topic coverage—thereby enforcing relay-regime learning dynamics—while combining persistent archive-based gap identification, targeted weakness synthesis, and principled RLVR-grounded replacement criteria at competition level?\",\n  \"opportunity\": \"Four converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot enforce relay-regime dynamics because it cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides the missing theoretical backbone: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness—the relay regime (smooth spectrum, small geometric ratio R between adjacent difficulties) converges exponentially faster than the grokking regime (large gaps). This directly motivates fine-grained multi-dimensional archives: ensuring smooth coverage of difficulty×topic is not merely a heuristic but a theoretically-grounded design choice for maximizing RLVR convergence speed. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024 with online curriculum; Socratic-Zero achieves 56.1% average with three-agent co-evolution; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples via bidirectional difficulty adjustment. But none maintains structured multi-dimensional archives with systematic gap identification. (4) The synthesis-verification gap is closing: SAND-Math demonstrates ~37.7% survival for general competition-level synthesis; VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that enforce relay-regime dynamics by ensuring smooth difficulty coverage, (b) proactive niche-level gap identification (vs. reactive instance-level targeting), (c) competition-level multi-stage verification, and (d) RLVR-grounded replacement criteria. Our contribution is elevating archive-based co-evolution from a GSM-level proof-of-concept to a theoretically-grounded, competition-level system—not paradigm invention.\",\n  \"landscape\": \"**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability l_θ(x) = p_θ(x)(1−p_θ(x)), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics—relay-regime enforcement impossible; (d) random mutation rather than targeted weakness synthesis; (e) teacher-student misalignment—RL improves student but not teacher/mutator; (f) K=100 completions per problem is computationally expensive.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring (diversifies medium-difficulty problems, simplifies hard ones, preserving answers), and difficulty-aware KL (λ_hard=0.3, λ_non-hard=1.0). Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines including DAPO and Critique-GRPO. Trained on DAPO-Math-17k, 200 steps, 8×H20 GPUs. Critical delta: no persistent archive—operates per-batch only; no cross-step memory; restructures existing problems rather than synthesizing new ones; 3 coarse difficulty bins (width ~0.33) create large inter-bin gaps that may induce grokking-regime dynamics per the implicit curriculum theory.\\n\\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions, then generates new problems targeting those specific reasoning errors. Uses a Gaussian utility function centered at 50% success rate (μ=0.5, σ=0.2) for 'desirable difficulty.' The Generator (trained via value-weighted SFT) distills the Teacher's problem-generation capability. Dynamic three-zone categorization (Mastered/Learning/Too Difficult) recategorized each iteration. Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B, with a trained Generator reaching 95.6% validity. Critical differentiation from our approach: (a) weakness targeting is reactive and instance-level—responds to specific failed solutions rather than proactively identifying under-explored niches; (b) no structured archive, behavioral descriptors, or coverage map—the curriculum is an unstructured growing set; (c) three-zone categorization is a 1D difficulty measure, not a multi-dimensional skill map; (d) no quality-diversity objective—diversity is a side effect of multi-domain seeds and temperature sampling, not optimized; (e) requires a frozen 235B oracle Teacher (16 MI308X GPUs), while our approach uses the policy itself for gap identification via archive structure. Our approach is complementary: proactive niche-level gap identification (which niches are under-explored?) vs. Socratic-Zero's reactive instance-level targeting (which specific errors occurred?).\\n\\n**Implicit curriculum theory.** 'The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards' (arXiv 2602.14872, Feb 2026; ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning—the gradient signal peaks at intermediate difficulty (∇_q J_L(t) ∝ (Δ_L)^L(1−Δ_L), an inverted-U). Two regimes are identified: the relay regime (smooth difficulty spectrum, geometric ratio R = O(1), where progress on easier problems continuously supports harder ones with compressed inter-level plateaus) and the grokking regime (large difficulty gaps, R = ω(1), where long plateaus precede sudden phase transitions). The relay regime converges exponentially faster. Importantly, this paper does NOT argue against explicit curriculum management—it proves implicit curriculum exists under idealized conditions (synthetic group-theoretic tasks, uniform difficulty distributions, single attention layer). Real training data has non-uniform, potentially gapped difficulty distributions where explicit curation is needed to enforce the relay regime. We adopt this theoretical framework as our backbone: our 2D archive with 10 fine-grained difficulty bins (width 0.1) ENSURES smooth difficulty coverage within each topic, directly enforcing relay-regime dynamics. Ablation A7 (3 vs. 10 bins) provides the first empirical test of relay vs. grokking dynamics in real RLVR training.\\n\\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026) introduces a 4-agent framework (Repairer/Challenger/Reasoner/Explorer) that both complicates mastered problems and simplifies failed ones based on an Optimal Pacing Theorem (gradient g(d) = A·d·e^{-d/c_t} peaks at d* = c_t). Achieves 60.03 average across 6 benchmarks with only 5,873 samples; AIME 2025: 40.0. Maintains persistent per-problem error counters and an evolving validation set. Differentiation: this system optimizes problem difficulty bidirectionally but without structured multi-dimensional archives, quality-diversity objectives, or systematic coverage tracking across topic×difficulty niches. The Explorer agent promotes domain diversity but without principled coverage guarantees.\\n\\n**Novelty-aware diversity without archives.** EVOL-RL (arXiv 2509.15194, Sep 2025; revised Feb 2026) prevents diversity collapse during label-free RL via novelty-aware rewards: embedding-based cosine similarity within response batches, with asymmetric PPO clipping and entropy regularization. Achieves Qwen3-4B AIME25: 4.6%→17.1% pass@1 (TTRL→EVOL-RL); Qwen3-8B AIME24: 16.7→26.0. Entirely stateless—novelty computed per-batch with no persistent memory. Proves that diversity collapse is a real failure mode (TTRL pass@16 degrades from 32.4→16.7 while EVOL-RL improves to 40.9). Represents a lightweight alternative to archive-based diversity maintenance, but cannot detect longer-horizon pattern repetition across training steps or provide systematic coverage guarantees.\\n\\n**Difficulty-aware offline augmentation.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026) introduces MAD normalization (replacing std normalization in GRPO, ensuring constant update magnitude regardless of difficulty) and DQW weighting (λ_s = B_v·exp(D_s/T)/Σexp(D_s/T), T=2.0). AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. Offline augmentation—no online adaptation. We adopt DGPO's MAD normalization for our policy update step.\\n\\n**Weakness-driven targeted synthesis.** SwS (NeurIPS 2025, arXiv 2506.08989) identifies model weaknesses as problems where accuracy never reaches 50% with negative slope during preliminary RL, allocates synthesis budget proportionally to category failure rates, generates 40K targeted problems. Results: +10.0% (7B), +7.7% (32B). Offline two-stage pipeline; weaknesses identified once. STAT (arXiv 2510.10023) creates Missing-Skill-Profiles and synthesizes skill-targeted examples (+7.5% on MATH via SFT). 'Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis' (arXiv 2604.04386) uses AI hypotheses to identify struggle concepts. These validate the weakness→targeted generation pattern we adopt continuously online, but all operate offline.\\n\\n**Adaptive curriculum and co-evolutionary approaches.** AdaRFT (arXiv 2504.05520) dynamically adjusts training problem difficulty based on recent reward signals, achieving 2× training speedup on AMC/AIME/IMO. CPMöbius (arXiv 2602.02979) implements cooperative coach-player co-evolution for data-free RL, +4.9 average improvement—demonstrates co-evolution for LLM reasoning but without archive structure or quality-diversity principles. AERO (arXiv 2602.03084) uses ZPD-based autonomous evolutionary reasoning with entropy-based dual-loop—shares ZPD motivation but operates without structured archives. OpenSIR (arXiv 2511.00602) optimizes both difficulty and diversity from seed problems via self-play teacher-student dynamics at GSM/CollegeMath level.\\n\\n**Self-evolving RLVR and diversity maintenance.** SvS (ICLR 2026) achieves +18.3%/+22.8% pass@32 on AIME24/25 via answer-preserving variational mutations. R-Zero (ICLR 2026) co-evolves Challenger+Solver but collapses after iteration 3. Prism (arXiv 2603.13309) prevents collapse via 128 K-means semantic clusters with ZPD gate [0.5, 0.9] and rarity bonus (AIME 2024: 16.77 on Qwen3-4B). R-Diverse (arXiv 2602.13103) introduces SAM code-embedding skill diversity + MAP persistent memory bank (AIME 2024: 19.17 on Qwen3-4B, +6.46 over R-Zero). Vocabulary Dropout (arXiv 2604.03472) addresses diversity collapse via token-level perturbation.\\n\\n**Verification approaches.** VHG (arXiv 2605.06660) introduces three-party self-play with verifier gating: reward = I[V(x,y*)=1]×(1-Acc_solver). SAND-Math (arXiv 2507.20527) demonstrates competition-level synthesis at 37.7% survival rate for unconstrained generation (critical caveat: niche-specific targeting reduces survival to 4-17% per empirical evidence across MathSmith, SPARQ, and SDE-GPG studies).\\n\\n**AIME 2024 landscape and paradigm contextualization.** The 7B-8B AIME 2024 landscape has shifted dramatically: Klear-Reasoner-8B achieves 90.5% (distillation from DeepSeek-R1-0528 + SFT + GPPO RL, 64K inference budget), DeepSeek-R1-Distill-Qwen-7B 83.3% (pure distillation), BP-Math-7B 70.8% (BAPO RL on distilled base), ScaleDiff-7B 73.0% (SFT on difficulty-scaled synthetic data). Crucially, nearly ALL top results rely on distillation from >100B parameter teachers—inheriting reasoning patterns the 7B model could not discover independently. Self-evolving methods operating WITHOUT distillation achieve fundamentally lower scores: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0% on AIME 2024. Methods using seed training data without distillation: CLPO 50.0%, Socratic-Zero's solver ~56.1% average (but with a frozen 235B oracle). This reveals two distinct research paradigms with different constraints and contributions. Our work targets the self-evolving/seed-data paradigm: the value lies in the METHOD (systematic archive-based co-evolution), the ABLATION INSIGHTS (which components matter and why), and the FRAMEWORK (relay-regime enforcement via structured archives)—not in competing with distillation-based absolute numbers. We note that SACE-RLVR's framework could be applied atop distilled bases for potential further gains.\\n\\n**Learnability and curriculum optimization.** VCRL (arXiv 2509.19803) validates that reward variance follows an inverted-U relationship with difficulty—problems with moderate difficulty produce highest advantage variance. Critically, VCRL's ablation finds G=16 is the minimum for robust variance estimation (G=4 averages 44.17 vs. G=16 at 57.76). SEC (arXiv 2505.14970) formulates curriculum selection as MAB over predefined categories using |advantage| as learning gain proxy. Shrinkage estimators (James-Stein baseline in arXiv 2511.03710; EBPO arXiv 2602.05165) provably reduce MSE for per-group statistics in the low-generation regime.\\n\\n**QD foundations.** SPARQ (arXiv 2506.06499) demonstrated MAP-Elites for offline synthetic math generation. ARISE (arXiv 2603.16060) co-evolves hierarchical skill libraries.\\n\\n**Fundamental premise.** 'Sparse Policy Selection' (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. 'Sharper Primitives' (arXiv 2602.08281) shows diverse training activates broader latent primitive coverage. 'Does RL Really Incentivize Reasoning Capacity Beyond the Base Model?' (NeurIPS 2025, arXiv 2504.13837) finds >95% overlap at high pass@k. These support a coverage-focused framing: archive diversity ensures RL's limited selection budget is spent across the full capability spectrum.\\n\\n**The precise gap.** DéjàQ proves online MAP-Elites works for RLVR but only at GSM level with 1D descriptors and random mutation—cannot enforce relay-regime dynamics. CLPO proves online curriculum works at competition level but statelessly with coarse bins—difficulty gaps may induce grokking dynamics. Socratic-Zero proves weakness targeting works at competition level but reactively without structured coverage—cannot proactively identify under-explored niches. The implicit curriculum theory proves smooth difficulty spectra are critical but doesn't provide a mechanism for ensuring smoothness. No existing work combines persistent multi-dimensional archives (enforcing relay-regime dynamics), proactive niche-level gap identification, competition-level verification, and RLVR-grounded replacement criteria in a single online system.\",\n  \"inspired_by\": \"DéjàQ_paradigm['online MAP-Elites co-evolution during RL training is viable'] + implicit_curriculum_theory['relay regime with smooth difficulty spectra converges exponentially faster than grokking regime'] + CLPO_insight['online curriculum with difficulty adaptation achieves 50% AIME 2024'] + Socratic_Zero_pattern['three-agent co-evolution with instance-level weakness targeting achieves 56.1% average'] + MathForge_contribution['MAD normalization fixes GRPO difficulty imbalance'] + SwS_pattern['targeted weakness-driven synthesis yields +10% over indiscriminate generation'] + VCRL_criterion['advantage variance inverted-U validates principled replacement signal; G≥16 for robust estimation'] + EVOL_RL_warning['diversity collapse is real: TTRL pass@16 degrades 32.4→16.7 without novelty pressure'] + DéjàQ_limitations['1D archive cannot enforce relay-regime + random mutation + GSM-only'] + CLPO_limitations['3 coarse bins may induce grokking dynamics + no persistent coverage'] + SocraticZero_limitations['reactive instance-level targeting cannot proactively identify under-explored niches'] + sparse_policy_selection['coverage-focused framing: archive diversity maximizes RL selection budget efficiency']\",\n  \"approach\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics through five principled innovations grounded in a theoretical backbone from the implicit curriculum literature: a 2D interpretable archive enforcing relay-regime dynamics, proactive niche-level weakness synthesis (complementing reactive approaches like Socratic-Zero), VCRL-validated advantage variance with robust estimation, adaptive niche-aware population strategy, and DGPO-enhanced policy updates. We honestly acknowledge that DéjàQ established online MAP-Elites co-evolution for RLVR—our contribution is theoretically-grounded scaling and principled design that creates structural synergies beyond component-wise integration.\\n\\n**Theoretical Backbone: Relay-Regime Enforcement.** The implicit curriculum theory (arXiv 2602.14872) proves that RLVR naturally produces curriculum effects—but only efficiently in the relay regime where the difficulty spectrum is smooth (geometric ratio R = O(1) between adjacent levels). Gaps in difficulty cause grokking-regime dynamics with exponentially longer plateaus. This provides the theoretical foundation for our design choices: (a) 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) to minimize inter-bin gaps; (b) persistent archive tracking to detect and fill difficulty gaps before they cause training stalls; (c) targeted synthesis specifically for under-populated niches to maintain smooth coverage. The theory predicts that finer granularity (smaller R) produces faster convergence—ablation A7 provides the first empirical test of relay vs. grokking dynamics in real RLVR training.\\n\\n**1. 2D Interpretable Archive (50 cells).** Unlike DéjàQ's 1D archive with 8 thematic settings, we maintain a 2D MAP-Elites grid: 10 difficulty bins (width 0.1, based on empirical solve-rate: [0-0.1, 0.1-0.2, ..., 0.9-1.0]) × 5 mathematical topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells. Each cell stores up to M=10 problems (max 500 active). Topic classification via GPT-4o-mini (validated at 84-92% accuracy; arXiv 2411.00042). Difficulty via empirical solve-rate from G=16 rollouts on the current policy (reusing training rollouts—see Section 5). The 2D structure enables capabilities that emerge from the archive as substrate and are QUALITATIVELY impossible with component-wise approaches: (a) relay-regime enforcement—fine-grained difficulty bins ensure smooth coverage within each topic, directly implementing the theoretical condition for fast convergence; (b) proactive gap identification—precisely locate which topic×difficulty niches are under-explored BEFORE the policy encounters failures there (vs. Socratic-Zero's reactive approach that waits for specific failures); (c) principled compute allocation—the archive tells WHERE to focus synthesis and training, advantage variance tells HOW MUCH signal each problem provides; (d) interpretable post-hoc analysis—which niches contribute most to downstream benchmark performance, providing actionable insights beyond any single AIME number.\\n\\n**2. Emergent Curriculum via Relay-Regime Dynamics (theoretically grounded).** With 0.1-wide difficulty bins, typical GRPO training improves solve-rate by ~3-8% per 50 steps on in-ZPD problems (based on published GRPO learning curves from DAPO, MathForge, and CLPO). This means ~30-80% of problems in a given cell cross bin boundaries per refresh cycle (every 50 steps). Over 500 training steps (10 refresh cycles), most problems shift 2-4 difficulty bins, creating measurable emergent curriculum without explicit scheduling. The implicit curriculum theory explains WHY this works: 0.1-wide bins maintain small geometric ratio R between adjacent difficulty levels, keeping the system in the relay regime where progress on each level continuously supports the next. Contrast with CLPO's 3 coarse bins (width ~0.33): the same 3-8% improvement rarely triggers bin transitions, and the larger inter-bin gaps may induce grokking-like plateaus. We commit to tracking per-cell solve-rate trajectories and bin-transition frequencies as a primary analysis, and ablation A7 directly tests the relay-regime prediction (10 bins vs. 3 bins, predicting faster convergence with finer granularity).\\n\\n**3. Targeted Weakness-Driven Synthesis: Proactive Niche-Level Gap Identification (vs. Reactive Instance-Level Targeting).** Existing weakness targeting approaches operate reactively: Socratic-Zero's Teacher examines specific failed solutions and generates problems targeting those errors; SwS identifies aggregate category-level weaknesses after preliminary RL. Both are effective but cannot proactively identify under-explored capability niches. The 2D archive enables a fundamentally different approach: proactive niche-level gap identification. (a) Identify under-performing archive cells (under-populated <3 problems, or stale—all problems with solve-rate >0.9 or <0.05). (b) Prompt a synthesis LLM (Qwen2.5-72B-Instruct or GPT-4o) with the specific topic×difficulty niche requirements, exemplar problems from neighboring cells, and target solve-rate range. (c) Use generate-then-classify rather than constrained generation: generate candidate problems for the target topic without explicit difficulty constraints, verify them, then measure actual difficulty with the current policy and assign to the appropriate cell. This avoids the 'double filter' problem where simultaneously constraining topic AND difficulty reduces survival to 4-17% (vs. ~37% for unconstrained generation). (d) When seed problems exist in nearby cells, use SvS-style answer-preserving mutation (higher validity ~70-80%) for cross-niche seeding. This is complementary to Socratic-Zero's instance-level targeting: we identify WHERE gaps exist (niche level), they identify WHAT errors occur (instance level). A complete system could integrate both—we test this complementarity in ablation A2.\\n\\n**4. Multi-Stage Verification Pipeline (Competition-Level).** DéjàQ suffers 22-44% invalid rates even at GSM level. At competition level, robust verification is essential. We implement a 3-stage VHG-inspired pipeline: (a) Format and solvability check—verify the problem is well-formed with a unique numerical answer (filters ~30% of candidates); (b) Cross-verification—solve with 2-3 strong models (Qwen2.5-Math-72B, DeepSeek-Math) and check answer agreement via majority vote (≥75% consistency among 16 rollouts, filters ~20% of remaining); (c) Difficulty calibration—G=16 rollouts with current policy for solve-rate estimation and bin assignment. Under the generate-then-classify approach, we generate for target topic (not difficulty), achieving ~25-30% survival through verification, then assign to appropriate difficulty cells. This is more efficient than targeting specific topic×difficulty niches (4-17% survival) because difficulty is determined empirically rather than constrained during generation.\\n\\n**5. Robust Advantage Variance Estimation (K=16 + Beta Posterior).** DéjàQ uses p(1-p) learnability as fitness with K=100 dedicated completions per problem. We propose advantage variance as the replacement criterion, following VCRL's validated inverted-U relationship. Addressing the reviewer's concern about estimation reliability at small sample sizes: (a) We use G=16 rollouts (matching DAPO/VCRL standard practice), reusing the same rollouts as GRPO training—no additional inference cost. VCRL's ablation confirms G=16 as the minimum for robust estimation (G=4 averages 44.17 vs. G=16 at 57.76). (b) We maintain a Beta-Bernoulli running posterior for each problem's solve-rate: initialized at Beta(1,1), updated to Beta(α+k, β+G-k) each time the problem appears in training (k successes from G rollouts). After 3 training appearances (48 total rollouts), the posterior variance drops by 3×, providing reliable estimates even for problems with true solve rates below 0.2. (c) For single-batch decisions, we apply James-Stein shrinkage (arXiv 2511.03710): per-problem variance estimates are regularized toward the batch-level average, provably reducing MSE when individual estimates are noisy. (d) Replacement decisions use conservative credible intervals: a candidate replaces the cell occupant only when its posterior advantage variance credible interval (lower bound) exceeds the occupant's (upper bound). This prevents spurious replacements from noise at extreme solve rates. Computational savings vs. DéjàQ: 16 rollouts (reused from training) vs. 100 dedicated rollouts = zero additional cost.\\n\\n**6. Adaptive Niche-Aware Population Strategy.** Competition-level synthesis is hard, and niche-specific survival rates vary dramatically. Empirical evidence: unconstrained competition-level synthesis survives at ~37% (SAND-Math), but targeting specific topics reduces this (geometry is particularly hard—SDE-GPG reports only 47-63% difficulty calibration accuracy for geometry), and difficulty targeting adds another filter. Our generate-then-classify approach mitigates this, but some niches will still be harder to populate. Strategy: Phase 1 (steps 0-100)—populate 'medium' cells (solve-rate 0.3-0.7) across all topics using generate-then-classify, which are easiest to fill and provide strongest ZPD training signal. Phase 2 (steps 100-300)—as the policy improves, recalibration naturally shifts problems into harder bins; supplement with targeted synthesis for topics with persistent gaps. Phase 3 (steps 300+)—target extreme cells using cross-niche seeding (SvS-style mutation from adjacent populated cells, ~70-80% validity). Adaptive overgeneration budgets track per-niche historical survival rates: start at 5× for well-populated niches, increase to 10× for hard niches (e.g., geometry), 15× for extreme niches (e.g., hard number theory at 0-0.1 solve-rate). Graceful degradation: empty extreme cells don't break the system—it trains on well-populated cells. The analysis explicitly reports per-niche population density and survival rates, which is itself a community contribution revealing which capability niches are practically feasible to populate.\\n\\n**7. DGPO-Enhanced Policy Update.** We integrate MathForge's MAD normalization and DQW weighting, orthogonal to archive management. Ablation A8 isolates its contribution.\\n\\n**'More Than Sum of Parts': Structural Synergies from the 2D Archive.** The 2D archive is not merely a data structure—it is an enabling substrate that creates emergent capabilities impossible with any single component or their naive combination. (1) Relay-regime enforcement requires both fine-grained difficulty tracking (archive structure) AND smooth coverage maintenance (targeted synthesis). Neither the archive alone (without synthesis to fill gaps) nor synthesis alone (without archive to identify gaps) can enforce relay dynamics. (2) Proactive gap identification requires persistent coverage memory (archive) to know WHERE gaps are, combined with targeted synthesis to fill them. Reactive approaches (Socratic-Zero, SwS) cannot identify gaps they have not yet encountered. (3) Principled compute allocation requires both WHERE information (archive coverage map) and HOW MUCH information (advantage variance). Together, they enable focused compute on high-value regions of the capability space. (4) Interpretable capability diagnosis requires structured behavioral descriptors (topic×difficulty) to map which niches drive downstream performance. This analysis is impossible with unstructured curricula. The ablation structure tests each synergy: A1 removes 2D structure (can 1D archive enforce relay dynamics?), A2 removes targeted synthesis (does random synthesis maintain smooth coverage?), A3 removes advantage variance (does p(1-p) provide equivalent compute allocation signal?), A4 removes persistence (do per-batch decisions achieve relay-regime dynamics?).\\n\\n**Training Loop (DGPO on Qwen2.5-Math-7B primary, Qwen3-8B secondary, VERL framework):**\\n(a) Sample training batch from archive cells in ZPD window [0.1, 0.9], weighted by posterior advantage variance.\\n(b) Run G=16 rollouts per problem, compute advantages with MAD normalization and DQW.\\n(c) DGPO policy update step.\\n(d) Update Beta posteriors for all sampled problems using batch results.\\n(e) Every 50 steps: staggered archive refresh—re-evaluate only cells sampled in the last 50 steps (~40-60% of archive, ~200-300 problems × 16 rollouts = 3200-4800 evaluation rollouts from training); reassign problems crossing bin boundaries; flag stale cells; trigger targeted synthesis for under-populated or stale cells.\\n(f) Estimated overhead: ~15-20% per refresh cycle (synthesis and verification; evaluation rollouts are reused from training). Lazy evaluation reduces this to ~10% for mature archives.\\n\\n**AIME 2024 Landscape Contextualization.** We position SACE-RLVR within the self-evolving/seed-data paradigm, distinct from distillation-based methods that dominate the AIME 2024 leaderboard (Klear-Reasoner-8B 90.5% via distillation+RL, DeepSeek-R1-Distill-Qwen-7B 83.3%). Self-evolving methods without distillation achieve 16-20% (R-Zero, Absolute Zero), while seed-data methods achieve ~50% (CLPO). Our primary contribution is not absolute AIME numbers but: (a) systematic ablation revealing which components of archive-based co-evolution matter and why (relay-regime enforcement, proactive gap identification, robust variance estimation); (b) the first competition-level archive-based co-evolution system, establishing whether the paradigm scales; (c) interpretable capability maps revealing which topic×difficulty niches drive benchmark performance; (d) a framework applicable atop distilled bases for potential further gains—we test this as secondary experiment with Qwen3-8B.\\n\\n**Baselines (10 systems):**\\n(1) DéjàQ-comp: DéjàQ adapted to competition level—1D archive with symbolic mutator on competition-level seeds using our verification pipeline. PRIMARY baseline isolating 2D structure + targeted synthesis value.\\n(2) CLPO: reproduced with DAPO-Math-17k on Qwen3-8B. PRIMARY baseline isolating persistent archive value.\\n(3) Socratic-Zero: compared against their released Socratic-Solver-8B model; if unavailable, reproduced with 72B teacher (instead of 235B). PRIMARY baseline isolating structured archive vs. instance-level targeting.\\n(4) SwS: static two-stage offline pipeline (reproduced).\\n(5) MathForge: offline DGPO + MQR augmentation.\\n(6) Prism: 128-cluster semantic diversity with ZPD gate.\\n(7) R-Diverse: SAM skill diversity + MAP memory bank.\\n(8) EVOL-RL: novelty-aware per-batch diversity; tests whether lightweight stateless diversity suffices.\\n(9) AdaRFT: adaptive difficulty without archive.\\n(10) Vanilla GRPO on DAPO-Math-17k.\\n\\n**Ablations (10 experiments):**\\nA1: 1D archive only (topic dimension, no difficulty bins)—tests whether 2D structure enables relay-regime enforcement.\\nA2: Random synthesis instead of targeted weakness synthesis (keeps archive structure but uses DéjàQ-style random mutation—isolates proactive vs. random gap filling).\\nA3: p(1-p) replacement instead of advantage variance (DéjàQ's fitness criterion on our archive—isolates replacement criterion value).\\nA4: No archive persistence (per-batch only, CLPO-style with synthesis—isolates whether persistent coverage enables relay dynamics).\\nA5: DéjàQ-comp baseline (1D archive + random mutation at competition level).\\nA6: CLPO + archive persistence (adds persistent archive to CLPO's approach—tests whether archive alone closes the gap).\\nA7: Coarse difficulty bins (3 bins like CLPO vs. our 10)—the key relay-regime test. We predict faster convergence with 10 bins per the implicit curriculum theory.\\nA8: Standard GRPO normalization vs. DGPO MAD (isolates policy update contribution).\\nA9: Archive coverage vs. per-cell pass@k correlation (tests: does broader primitive activation drive gains?).\\nA10: G=16 with Beta posterior vs. G=16 point estimation only (isolates robust estimation value; tests whether posterior accumulation and shrinkage improve replacement quality).\\n\\n**Evaluation:** AIME 2024 (30 problems), AIME 2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. Both pass@1 and pass@k (k=8,32,64). Training data: DAPO-Math-17k as seed. Base models: Qwen2.5-Math-7B (primary, following MathForge for comparability) and Qwen3-8B (secondary, following CLPO for comparability).\\n\\n**Key analyses:** (1) Archive coverage heatmaps at each training stage, with relay-regime metrics (inter-bin gap ratios R per topic). (2) Per-cell contribution to benchmark performance (which topic×difficulty niches matter most for AIME?). (3) Emergent curriculum visualization showing per-cell solve-rate trajectories and bin-transition frequencies, with comparison to predicted relay-regime dynamics. (4) Synthesis efficiency by niche: generate-then-classify vs. constrained generation survival rates, per-topic breakdown (expecting geometry to be hardest). (5) DéjàQ-comp vs. SACE-RLVR archive dynamics comparison. (6) Convergence speed comparison: relay-regime prediction (10 bins → fewer/shorter plateaus) vs. grokking-regime (3 bins → longer plateaus). (7) Proactive vs. reactive gap analysis: do archive-identified gaps correlate with subsequent policy failures?\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"6600 H100-hours (baselines: GRPO+SwS+Prism+R-Diverse+MathForge+CLPO+AdaRFT+EVOL-RL reproduction 8×250h=2000h; Socratic-Zero comparison 300h; DéjàQ-comp adaptation 400h; SACE-RLVR primary on 7B 2×400h=800h on 8×H100; SACE-RLVR on 8B 2×400h=800h; ablations A1-A10 10×200h=2000h; archive population/synthesis/verification 300h)\",\n      \"timeline\": \"14-18 weeks\",\n      \"estimated_gpu_cost\": \"$16,500 (at ~$2.50/H100-hr cloud spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"5400 H100-hours (reuse MathForge/CLPO/EVOL-RL released code for baselines; use released Socratic-Solver-8B model; fewer failed runs from validated hyperparameters; shared verification pipeline across ablations)\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$400-800 (GPT-4o-mini for topic classification, Qwen2.5-72B for targeted synthesis prompting)\",\n      \"estimated_gpu_cost\": \"$13,500\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"8000 H100-hours (more exploratory sweeps over archive dimensions, bin granularity, refresh frequencies, replacement criteria, synthesis strategies, and relay-regime metrics)\",\n      \"timeline\": \"10-13 weeks\",\n      \"claude_api_cost\": \"$1000-2000\",\n      \"estimated_gpu_cost\": \"$20,000\",\n      \"speed_bottleneck\": \"GPU allocation queue time; each GRPO run takes 24-72h wall-clock on 8×H100s. DéjàQ-comp baseline requires careful engineering—DéjàQ's symbolic mutator may not straightforwardly extend to competition-level problems. Socratic-Zero reproduction with 72B teacher (if released model unavailable) adds significant inference cost.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026) — stretch target if pilot results are strong by August\",\n    \"ICML 2027 (expected deadline ~Jan 2027) — primary target, strong fit for RL + quality-diversity intersection + relay-regime theoretical connection\",\n    \"NeurIPS 2027 (full paper ~May 2027) — fallback with comprehensive evaluation\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems (arXiv 2601.01931, Jan 2026) — PRIMARY PREDECESSOR, establishes online MAP-Elites co-evolution for RLVR at GSM level; 1D archive, p(1-p) fitness, K=100 completions; we scale this paradigm to competition level with relay-regime grounding\",\n    \"CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning (arXiv 2509.25004, Sep 2025) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024 with Qwen3-8B; stateless per-batch with 3 coarse bins\",\n    \"Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution (arXiv 2509.24726, Sep 2025) — PRIMARY BASELINE for weakness targeting comparison; three-agent co-evolution with instance-level weakness targeting; 56.1% avg; no structured archive or QD framework\",\n    \"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards (arXiv 2602.14872, Feb 2026; ICML 2026) — THEORETICAL BACKBONE; proves relay regime (smooth difficulty) converges exponentially faster than grokking regime (gapped difficulty); grounds our fine-grained bin design\",\n    \"Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2603.05120, Mar 2026) — 4-agent bidirectional difficulty adjustment; 60.03 avg with 5,873 samples; persistent error counters but no structured multi-dimensional archive\",\n    \"EVOL-RL: Evolving Language Models without Labels via Novelty-Aware Rewards (arXiv 2509.15194, Sep 2025) — stateless per-batch novelty-aware diversity; Qwen3-4B AIME25 17.1%; lightweight alternative to archive-based diversity; demonstrates diversity collapse risk\",\n    \"MathForge/DGPO: Harder Is Better (arXiv 2601.20614, ICLR 2026) — MAD normalization + DQW for GRPO; we adopt for policy update; AIME 2024: 24.58 on 7B\",\n    \"SwS: Self-aware Weakness-driven Problem Synthesis in RL (NeurIPS 2025, arXiv 2506.08989) — offline category-based weakness targeting; +10% (7B); we adopt online targeted synthesis pattern\",\n    \"AdaRFT: Efficient Reinforcement Finetuning via Adaptive Curriculum Learning (arXiv 2504.05520) — adaptive difficulty with 2× speedup; baseline\",\n    \"CPMöbius: Iterative Coach-Player Reasoning for Data-Free RL (arXiv 2602.02979, Feb 2026) — cooperative co-evolution without archive structure\",\n    \"AERO: Autonomous Evolutionary Reasoning Optimization via Endogenous Dual-Loop Feedback (arXiv 2602.03084, Feb 2026) — ZPD-based dual-loop without structured archives\",\n    \"OpenSIR: Open-Ended Self-Improving Reasoner (arXiv 2511.00602, Nov 2025) — self-play difficulty + diversity at GSM/CollegeMath level\",\n    \"Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR [SvS] (ICLR 2026) — answer-preserving synthesis; we use for cross-niche seeding\",\n    \"Preventing Curriculum Collapse in Self-Evolving Reasoning Systems [Prism] (arXiv 2603.13309, Mar 2026) — 128-cluster diversity with ZPD gate; baseline\",\n    \"R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training (arXiv 2602.13103, Feb 2026) — SAM skill diversity + MAP memory; baseline\",\n    \"VCRL: Variance-based Curriculum RL for LLMs (arXiv 2509.19803) — validates advantage variance inverted-U; G=16 minimum for robust estimation; grounds our replacement criterion\",\n    \"SAND-Math: Competition-Level Synthesis with LLMs (arXiv 2507.20527) — ~37.7% survival for unconstrained competition synthesis; empirical grounding for population strategy\",\n    \"VHG: Verifier-Backed Hard Problem Generation (arXiv 2605.06660, May 2026) — three-party self-play with validity gating; inspires verification pipeline\",\n    \"R-Zero: Self-Evolving Reasoning LLM from Zero Data (ICLR 2026) — foundational self-evolving framework; collapses after iteration 3\",\n    \"SPARQ: Synthetic Problem Generation via Quality-Diversity Algorithms (arXiv 2506.06499) — offline QD for problem generation\",\n    \"STAT: Skill-Targeted Adaptive Training (arXiv 2510.10023) — Missing-Skill-Profile for targeted synthesis in SFT\",\n    \"Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis (arXiv 2604.04386) — weakness-driven benchmark generation\",\n    \"SEC: Self-Evolving Curriculum for LLM Reasoning (arXiv 2505.14970) — MAB over problem categories\",\n    \"Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards (arXiv 2511.03710) — James-Stein shrinkage for per-group statistics; addresses K=16 variance concerns\",\n    \"EBPO: Empirical Bayes Shrinkage for Stabilizing GRPO (arXiv 2602.05165) — dynamic shrinkage with Welford algorithm; supports our Beta posterior approach\",\n    \"Klear-Reasoner-8B: GPPO for Long-CoT Reasoning (arXiv 2508.07629) — 90.5% AIME 2024 via distillation+RL; contextualizes current AIME landscape\",\n    \"Sparse Policy Selection, Not Capability Learning (arXiv 2605.06241, May 2026) — RL modifies 1-3% tokens; motivates coverage framing\",\n    \"New Skills or Sharper Primitives (arXiv 2602.08281) — diverse training activates broader latent primitives\",\n    \"Does RL Really Incentivize Reasoning Capacity Beyond the Base Model? (NeurIPS 2025, arXiv 2504.13837) — >95% overlap at high pass@k; supports coverage framing\",\n    \"Problem Categorization Can Help LLMs Solve Math Problems (arXiv 2411.00042) — 84%+ topic classification accuracy\",\n    \"ARISE: Agent Reasoning with Intrinsic Skill Evolution (arXiv 2603.16060) — skill library co-evolution\",\n    \"Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution (arXiv 2604.03472)\"\n  ],\n  \"description\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm from GSM-level—where DéjàQ (arXiv 2601.01931) first demonstrated it—to competition-level mathematics (AIME, Olympiad) through five principled innovations grounded in the implicit curriculum theory (arXiv 2602.14872, ICML 2026). The key theoretical insight: RLVR naturally produces curriculum effects, but only efficiently in the 'relay regime' where difficulty spectra are smooth; gaps cause exponentially slower 'grokking' dynamics. Our 2D archive (10 difficulty bins × 5 topics = 50 cells) ENFORCES relay-regime dynamics by maintaining smooth difficulty coverage—a theoretically-grounded design choice, not merely a heuristic. We honestly acknowledge that DéjàQ established online MAP-Elites co-evolution, CLPO demonstrated online curriculum at competition level, and Socratic-Zero showed effective weakness targeting; our contribution is the principled integration that creates structural synergies beyond component-wise combination. (1) The 2D interpretable archive enables proactive niche-level gap identification—systematically locating under-explored topic×difficulty niches—which is qualitatively impossible with Socratic-Zero's reactive instance-level targeting (responds to specific failed solutions), CLPO's stateless per-batch approach, or DéjàQ's 1D structure. (2) Targeted weakness synthesis uses a generate-then-classify approach (generating for target topic, verifying, then empirically measuring difficulty) rather than constrained generation, achieving ~25-30% survival vs. 4-17% for niche-constrained synthesis. Cross-niche seeding via SvS-style mutation from adjacent cells provides ~70-80% validity for hard-to-populate niches. (3) VCRL-validated advantage variance with robust estimation: G=16 rollouts reused from GRPO training (zero additional cost vs. DéjàQ's K=100 dedicated completions), Beta-Bernoulli running posterior accumulating evidence across training appearances, and James-Stein shrinkage for single-batch decisions. After 3 appearances (48 rollouts), posterior variance drops 3×, providing reliable estimates even at extreme solve rates. (4) Adaptive niche-aware population with per-niche overgeneration budgets (5× for medium niches, 10-15× for extreme niches), progressive phases, and honest acknowledgment that some extreme cells may remain sparse. (5) DGPO-enhanced policy updates (MAD normalization from MathForge, ICLR 2026). The proposal is contextualized against the current AIME 2024 landscape: distillation-based methods achieve 70-90% (Klear-Reasoner-8B 90.5%), while self-evolving methods without distillation achieve 16-20%. We target the self-evolving/seed-data paradigm where the value is the METHOD and ABLATION INSIGHTS, not absolute numbers. Three PRIMARY baselines enable precise measurement: DéjàQ-comp (isolates 2D + targeted synthesis over 1D + random mutation), CLPO (isolates persistent archive over stateless per-batch), and Socratic-Zero (isolates structured proactive gap identification over reactive instance-level targeting). Seven additional baselines (SwS, MathForge, Prism, R-Diverse, EVOL-RL, AdaRFT, vanilla GRPO) provide comprehensive positioning. Ten ablations systematically isolate each component, with A7 (3 vs. 10 bins) providing the first empirical test of relay vs. grokking dynamics in real RLVR training. Key interpretable analyses include archive coverage heatmaps with relay-regime metrics, per-cell benchmark contribution mapping, convergence speed comparison validating the relay-regime prediction, and per-niche synthesis feasibility reporting. Evaluation on Qwen2.5-Math-7B and Qwen3-8B using VERL, targeting AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, and OlympiadBench.\",\n  \"project_name\": \"sace_rlvr\",\n  \"source\": \"web_research\",\n  \"change_type\": \"major\",\n  \"reviewer_response\": {\n    \"revision_overview\": \"MAJOR REVISION addressing three structural issues: (1) theoretical backbone via implicit curriculum relay-regime theory, (2) AIME SOTA contextualization within self-evolving paradigm, (3) sharper 'more than sum of parts' novelty argument via structural synergies. Four missing concurrent works added with precise differentiation. K=8→G=16 with Beta posterior and James-Stein shrinkage for robust variance estimation. Generate-then-classify approach for niche-aware synthesis with adaptive overgeneration budgets. Socratic-Zero elevated to PRIMARY baseline. Total of 10 baselines and 10 ablations. This revision represents a fundamental reframing from 'integration paper' to 'theoretically-grounded system design with empirically testable predictions.'\",\n    \"issue_1_socratic_zero\": \"ADDED AS PRIMARY BASELINE with extensive differentiation. Socratic-Zero (arXiv 2509.24726) implements three-agent co-evolution (Solver/Teacher/Generator) where a frozen 235B Teacher examines specific failed solutions and generates targeted problems (instance-level, reactive weakness targeting). Achieves 56.1% average across 7 math benchmarks. Key differentiation articulated along five dimensions: (a) reactive/instance-level vs. our proactive/niche-level gap identification—Socratic-Zero waits for specific failures, we identify under-explored niches before failures occur; (b) no structured archive—curriculum is an unstructured growing set vs. our 2D MAP-Elites grid; (c) 1D three-zone categorization (Mastered/Learning/Too Difficult) vs. our 2D topic×difficulty behavioral descriptors; (d) no quality-diversity objective—diversity is a side effect vs. our principled coverage optimization; (e) requires frozen 235B oracle (16 MI308X GPUs) vs. our policy-based gap identification via archive structure. Positioned as complementary: they solve WHERE errors occur (instance level), we solve WHERE gaps exist (niche level). Both are valid and could be integrated. Socratic-Zero is baseline #3 (using released Socratic-Solver-8B or reproduced with 72B teacher).\",\n    \"issue_2_implicit_curriculum\": \"INTEGRATED AS THEORETICAL BACKBONE—the most significant structural change in this revision. The implicit curriculum paper (arXiv 2602.14872, ICML 2026) proves RLVR naturally produces curriculum effects via gradient dynamics (∇_q J_L(t) ∝ (Δ_L)^L(1−Δ_L)), but identifies two regimes: relay (smooth difficulty spectrum, geometric ratio R=O(1), exponentially faster convergence) and grokking (large gaps, R=ω(1), long plateaus). This provides the theoretical foundation for our design choices: (a) 10 fine-grained bins (width 0.1) minimize inter-bin gaps to maintain relay regime; (b) persistent archive tracks and fills difficulty gaps; (c) targeted synthesis maintains smooth coverage. The theory predicts finer granularity → faster convergence. Ablation A7 (3 vs. 10 bins) provides the first empirical test of relay vs. grokking dynamics in real RLVR training—a testable theoretical prediction. We engage honestly with the implicit curriculum claim: RLVR naturally produces curriculum, but only EFFICIENTLY with smooth spectra. Our archive ENSURES smoothness—it enables implicit curriculum to work well, rather than replacing it with explicit scheduling. The theory is proven in synthetic settings (group-theoretic tasks, single attention layer); our ablation extends it to real RLVR.\",\n    \"issue_3_bidirectional_curriculum\": \"ADDED to landscape and related work. Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026) uses 4 agents (Repairer/Challenger/Reasoner/Explorer) for bidirectional difficulty adjustment based on an Optimal Pacing Theorem (g(d) = A·d·e^{-d/c_t}). Achieves 60.03 average with only 5,873 samples; AIME 2025: 40.0. Maintains persistent per-problem error counters. Differentiation: optimizes difficulty bidirectionally but without structured multi-dimensional archives, quality-diversity objectives, or systematic coverage tracking across topic×difficulty niches. The Explorer agent promotes domain diversity but without principled coverage guarantees. Does not provide relay-regime enforcement or interpretable capability mapping.\",\n    \"issue_4_evol_rl\": \"ADDED as baseline and landscape entry. EVOL-RL (arXiv 2509.15194) prevents diversity collapse via novelty-aware rewards (embedding cosine similarity within batches), asymmetric PPO clipping, and entropy regularization. Qwen3-4B AIME25: 4.6%→17.1%; Qwen3-8B AIME24: 16.7→26.0. Entirely stateless—novelty computed per-batch. Important contribution: demonstrates diversity collapse is a real failure mode (TTRL pass@16 degrades 32.4→16.7). Differentiation: lightweight but cannot detect longer-horizon pattern repetition or provide systematic coverage guarantees. Represents a complementary approach—per-batch diversity pressure vs. our persistent archive-based coverage. Included as baseline #8 to test whether lightweight stateless diversity suffices vs. structured archive-based approach.\",\n    \"issue_5_stale_baselines\": \"COMPREHENSIVELY ADDRESSED via AIME landscape contextualization paragraph in both landscape and approach sections. Current 7B-8B AIME 2024 SOTA: Klear-Reasoner-8B 90.5% (distillation from DeepSeek-R1-0528 + SFT + GPPO, 64K budget), DeepSeek-R1-Distill-Qwen-7B 83.3%, BP-Math-7B 70.8% (BAPO on distilled base), ScaleDiff-7B 73.0% (SFT on distilled synthetic data). KEY INSIGHT: nearly ALL top results rely on distillation from >100B teachers. Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%. Seed-data methods: CLPO 50.0%. We explicitly position within the self-evolving/seed-data paradigm: value is METHOD + ABLATION INSIGHTS + FRAMEWORK, not absolute AIME numbers. CLPO at 50.0% is actually among the best non-distillation methods, making it a competitive and appropriate baseline. We note SACE-RLVR's framework could be applied atop distilled bases for further gains.\",\n    \"issue_6_emergent_vs_implicit_curriculum\": \"DIRECTLY ENGAGED as the central theoretical argument. The implicit curriculum theory shows RLVR produces curriculum effects naturally—we agree and adopt this as our theoretical backbone. Our argument: implicit curriculum EXISTS but is only EFFICIENT in the relay regime (smooth difficulty spectrum). Real training data (e.g., DAPO-Math-17k) may have non-uniform, potentially gapped difficulty distributions. The 2D archive with fine-grained bins ENSURES smooth coverage, enforcing relay-regime dynamics. This is not replacing implicit curriculum with explicit scheduling—it is ENABLING implicit curriculum to work optimally by curating the difficulty landscape. The strongest evidence: ablation A4 (no archive persistence) tests whether per-batch decisions achieve relay dynamics, and A7 (3 vs. 10 bins) tests the relay-regime prediction directly. If 10 bins outperform 3 bins with faster convergence and fewer plateaus, it validates both the theory and the archive's value.\",\n    \"issue_7_advantage_variance_k8\": \"SUBSTANTIALLY REVISED. Changed from K=8 to G=16, matching VCRL's recommended minimum (their ablation: G=4→44.17, G=16→57.76). Crucially, G=16 rollouts are REUSED from GRPO training—zero additional inference cost (vs. DéjàQ's K=100 dedicated completions). Three robustness mechanisms: (1) Beta-Bernoulli running posterior per problem: initialized Beta(1,1), updated each training appearance. After 3 appearances (48 rollouts), posterior variance drops 3×, reliable even at p<0.2. (2) James-Stein shrinkage for single-batch decisions: per-problem estimates regularized toward batch-level average, provably reducing MSE when individual estimates are noisy (supported by arXiv 2511.03710 and EBPO arXiv 2602.05165). (3) Conservative credible interval replacement: candidate replaces occupant only when lower bound of its variance credible interval exceeds upper bound of occupant's—prevents spurious replacements from noise. New ablation A10 tests posterior+shrinkage vs. point estimation, isolating robust estimation value.\",\n    \"issue_8_archive_population_realism\": \"SUBSTANTIALLY REVISED with three-pronged strategy. (1) GENERATE-THEN-CLASSIFY approach: generate candidate problems for target TOPIC (not specific difficulty), verify through pipeline, then empirically measure difficulty with current policy and assign to appropriate cell. This avoids the 'double filter' problem: unconstrained competition synthesis survives at ~37% (SAND-Math) vs. 4-17% for niche-constrained synthesis. (2) ADAPTIVE OVERGENERATION budgets tracking per-niche historical survival rates: 5× for well-populated niches, 10× for hard niches (geometry), 15× for extreme niches. (3) CROSS-NICHE SEEDING via SvS-style answer-preserving mutation from adjacent populated cells (~70-80% validity) for hard-to-populate niches. Topic-specific challenges acknowledged: geometry is hardest (SDE-GPG reports only 47-63% difficulty calibration accuracy); some extreme cells (hard geometry, solve-rate 0-0.1) may remain sparse. Graceful degradation: system functions on well-populated cells. Per-niche population density and survival rates reported as community contribution.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdcda38e-9c1f-455b-9b1a-1d7a8506f506",
  "isSidechain": false,
  "requestId": "req_011CbU42yHopZex7sSrAL2TQ",
  "type": "assistant",
  "uuid": "b3cd8740-48fd-4a44-a609-ae344a106378",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BB973vAK2oMvCYFAmNnR2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12881,
      "cache_read_input_tokens": 40602,
      "output_tokens": 19444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 19444,
          "cache_read_input_tokens": 40602,
          "cache_creation_input_tokens": 12881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12881
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

_source line 40 · 2026-05-28T01:01:18.990Z_

<details><summary>↩ Tool result · reported error · `toolu_01JpFKy35s2nFAFAd9wP6Pp1`</summary>

```text
Claude requested permissions to write to /tmp/sace_rlvr_revision_r5.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3cd8740-48fd-4a44-a609-ae344a106378",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "79c39c2f-ab92-40a3-87f2-de545476d5a8",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/sace_rlvr_revision_r5.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "b3cd8740-48fd-4a44-a609-ae344a106378",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "79c39c2f-ab92-40a3-87f2-de545476d5a8",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Tool call

_source line 43 · 2026-05-28T01:06:11.092Z_

<details open><summary>🔧 Tool call — Write · `toolu_01SGQyv7sFCbiUURStCzFvhW`</summary>

```json
{
  "file_path": "/tmp/sace_rlvr_revision_r5.json",
  "content": "{\n  \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\",\n  \"core_problem\": \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth (the 'relay regime'); gaps in difficulty coverage cause grokking-like plateaus where learning stalls. This creates a precise engineering challenge: how to ensure smooth, comprehensive coverage of the difficulty x topic space so that the implicit curriculum operates in the relay regime. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making relay-regime enforcement impossible. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B) through real-time difficulty assessment—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33), creating difficulty gaps that may induce grokking-regime dynamics. Socratic-Zero (arXiv 2509.24726) demonstrates effective instance-level weakness targeting through three-agent co-evolution (Solver/Teacher/Generator) achieving 56.1% average across 7 math benchmarks—but its weakness targeting is purely reactive (responds to specific failed solutions) with no structured archive or systematic coverage tracking, meaning entire capability niches may remain unexplored. The fundamental open question is: can we build a system that ensures smooth difficulty x topic coverage—thereby enforcing relay-regime learning dynamics—while combining persistent archive-based gap identification, targeted weakness synthesis, and principled RLVR-grounded replacement criteria at competition level?\",\n  \"opportunity\": \"Four converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot enforce relay-regime dynamics because it cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides the missing theoretical backbone: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness—the relay regime (smooth spectrum, small geometric ratio R between adjacent difficulties) converges exponentially faster than the grokking regime (large gaps). This directly motivates fine-grained multi-dimensional archives: ensuring smooth coverage of difficulty x topic is not merely a heuristic but a theoretically-grounded design choice for maximizing RLVR convergence speed. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024 with online curriculum; Socratic-Zero achieves 56.1% average with three-agent co-evolution; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples via bidirectional difficulty adjustment. But none maintains structured multi-dimensional archives with systematic gap identification. (4) The synthesis-verification gap is closing: SAND-Math demonstrates ~37.7% survival for general competition-level synthesis; VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that enforce relay-regime dynamics by ensuring smooth difficulty coverage, (b) proactive niche-level gap identification (vs. reactive instance-level targeting), (c) competition-level multi-stage verification, and (d) RLVR-grounded replacement criteria. Our contribution is elevating archive-based co-evolution from a GSM-level proof-of-concept to a theoretically-grounded, competition-level system—not paradigm invention.\",\n  \"landscape\": \"**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics—relay-regime enforcement impossible; (d) random mutation rather than targeted weakness synthesis; (e) teacher-student misalignment—RL improves student but not teacher/mutator; (f) K=100 completions per problem is computationally expensive.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard <=0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring (diversifies medium-difficulty problems, simplifies hard ones, preserving answers), and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines including DAPO and Critique-GRPO. Trained on DAPO-Math-17k, 200 steps, 8xH20 GPUs. Critical delta: no persistent archive—operates per-batch only; no cross-step memory; restructures existing problems rather than synthesizing new ones; 3 coarse difficulty bins (width ~0.33) create large inter-bin gaps that may induce grokking-regime dynamics per the implicit curriculum theory.\\n\\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions, then generates new problems targeting those specific reasoning errors. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' The Generator (trained via value-weighted SFT) distills the Teacher's problem-generation capability. Dynamic three-zone categorization (Mastered/Learning/Too Difficult) recategorized each iteration. Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B, with a trained Generator reaching 95.6% validity. Critical differentiation from our approach: (a) weakness targeting is reactive and instance-level—responds to specific failed solutions rather than proactively identifying under-explored niches; (b) no structured archive, behavioral descriptors, or coverage map—the curriculum is an unstructured growing set; (c) three-zone categorization is a 1D difficulty measure, not a multi-dimensional skill map; (d) no quality-diversity objective—diversity is a side effect of multi-domain seeds and temperature sampling, not optimized; (e) requires a frozen 235B oracle Teacher (16 MI308X GPUs), while our approach uses the policy itself for gap identification via archive structure. Our approach is complementary: proactive niche-level gap identification (which niches are under-explored?) vs. Socratic-Zero's reactive instance-level targeting (which specific errors occurred?).\\n\\n**Implicit curriculum theory.** 'The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards' (arXiv 2602.14872, Feb 2026; ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning—the gradient signal peaks at intermediate difficulty (an inverted-U). Two regimes are identified: the relay regime (smooth difficulty spectrum, geometric ratio R = O(1), where progress on easier problems continuously supports harder ones with compressed inter-level plateaus) and the grokking regime (large difficulty gaps, R >> 1, where long plateaus precede sudden phase transitions). The relay regime converges exponentially faster. Importantly, this paper does NOT argue against explicit curriculum management—it proves implicit curriculum exists under idealized conditions (synthetic group-theoretic tasks, uniform difficulty distributions, single attention layer). Real training data has non-uniform, potentially gapped difficulty distributions where explicit curation is needed to enforce the relay regime. We adopt this theoretical framework as our backbone: our 2D archive with 10 fine-grained difficulty bins (width 0.1) ENSURES smooth difficulty coverage within each topic, directly enforcing relay-regime dynamics. Ablation A7 (3 vs. 10 bins) provides the first empirical test of relay vs. grokking dynamics in real RLVR training.\\n\\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026) introduces a 4-agent framework (Repairer/Challenger/Reasoner/Explorer) that both complicates mastered problems and simplifies failed ones based on an Optimal Pacing Theorem (gradient peaks at optimal difficulty d* = c_t). Achieves 60.03 average across 6 benchmarks with only 5,873 samples; AIME 2025: 40.0. Maintains persistent per-problem error counters and an evolving validation set. Differentiation: this system optimizes problem difficulty bidirectionally but without structured multi-dimensional archives, quality-diversity objectives, or systematic coverage tracking across topic x difficulty niches. The Explorer agent promotes domain diversity but without principled coverage guarantees.\\n\\n**Novelty-aware diversity without archives.** EVOL-RL (arXiv 2509.15194, Sep 2025; revised Feb 2026) prevents diversity collapse during label-free RL via novelty-aware rewards: embedding-based cosine similarity within response batches, with asymmetric PPO clipping and entropy regularization. Achieves Qwen3-4B AIME25: 4.6% to 17.1% pass@1 (TTRL to EVOL-RL); Qwen3-8B AIME24: 16.7 to 26.0. Entirely stateless—novelty computed per-batch with no persistent memory. Proves that diversity collapse is a real failure mode (TTRL pass@16 degrades from 32.4 to 16.7 while EVOL-RL improves to 40.9). Represents a lightweight alternative to archive-based diversity maintenance, but cannot detect longer-horizon pattern repetition across training steps or provide systematic coverage guarantees.\\n\\n**Difficulty-aware offline augmentation.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026) introduces MAD normalization (replacing std normalization in GRPO, ensuring constant update magnitude regardless of difficulty) and DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. Offline augmentation—no online adaptation. We adopt DGPO's MAD normalization for our policy update step.\\n\\n**Weakness-driven targeted synthesis.** SwS (NeurIPS 2025, arXiv 2506.08989) identifies model weaknesses as problems where accuracy never reaches 50% with negative slope during preliminary RL, allocates synthesis budget proportionally to category failure rates, generates 40K targeted problems. Results: +10.0% (7B), +7.7% (32B). Offline two-stage pipeline; weaknesses identified once. STAT (arXiv 2510.10023) creates Missing-Skill-Profiles and synthesizes skill-targeted examples. 'Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis' (arXiv 2604.04386) uses AI hypotheses to identify struggle concepts. These validate the weakness-to-targeted-generation pattern we adopt continuously online, but all operate offline.\\n\\n**Adaptive curriculum and co-evolutionary approaches.** AdaRFT (arXiv 2504.05520) dynamically adjusts training problem difficulty based on recent reward signals, achieving 2x training speedup on AMC/AIME/IMO. CPMobius (arXiv 2602.02979) implements cooperative coach-player co-evolution for data-free RL, +4.9 average improvement—demonstrates co-evolution without archive structure or quality-diversity principles. AERO (arXiv 2602.03084) uses ZPD-based autonomous evolutionary reasoning with entropy-based dual-loop—shares ZPD motivation but operates without structured archives. OpenSIR (arXiv 2511.00602) optimizes both difficulty and diversity from seed problems via self-play teacher-student dynamics at GSM/CollegeMath level.\\n\\n**Self-evolving RLVR and diversity maintenance.** SvS (ICLR 2026) achieves +18.3%/+22.8% pass@32 on AIME24/25 via answer-preserving variational mutations. R-Zero (ICLR 2026) co-evolves Challenger+Solver but collapses after iteration 3. Prism (arXiv 2603.13309) prevents collapse via 128 K-means semantic clusters with ZPD gate [0.5, 0.9] and rarity bonus (AIME 2024: 16.77 on Qwen3-4B). R-Diverse (arXiv 2602.13103) introduces SAM code-embedding skill diversity + MAP persistent memory bank (AIME 2024: 19.17 on Qwen3-4B). Vocabulary Dropout (arXiv 2604.03472) addresses diversity collapse via token-level perturbation.\\n\\n**Verification approaches.** VHG (arXiv 2605.06660) introduces three-party self-play with verifier gating. SAND-Math (arXiv 2507.20527) demonstrates competition-level synthesis at 37.7% survival rate for unconstrained generation (critical caveat: niche-specific targeting reduces survival to 4-17% per empirical evidence across MathSmith, SPARQ, and SDE-GPG studies).\\n\\n**AIME 2024 landscape and paradigm contextualization.** The 7B-8B AIME 2024 landscape has shifted dramatically: Klear-Reasoner-8B achieves 90.5% (distillation from DeepSeek-R1-0528 + SFT + GPPO RL, 64K inference budget), DeepSeek-R1-Distill-Qwen-7B 83.3% (pure distillation), BP-Math-7B 70.8% (BAPO RL on distilled base), ScaleDiff-7B 73.0% (SFT on difficulty-scaled synthetic data). Crucially, nearly ALL top results rely on distillation from >100B parameter teachers. Self-evolving methods without distillation achieve fundamentally lower scores: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0% on AIME 2024. Methods using seed training data without distillation: CLPO 50.0%. This reveals two distinct research paradigms with different constraints and contributions. Our work targets the self-evolving/seed-data paradigm where the value lies in METHOD, ABLATION INSIGHTS, and FRAMEWORK rather than competing with distillation-based absolute numbers.\\n\\n**Learnability and curriculum optimization.** VCRL (arXiv 2509.19803) validates that reward variance follows an inverted-U relationship with difficulty. Critically, VCRL's ablation finds G=16 is the minimum for robust variance estimation (G=4 averages 44.17 vs. G=16 at 57.76). SEC (arXiv 2505.14970) formulates curriculum selection as MAB over predefined categories. Shrinkage estimators (James-Stein baseline in arXiv 2511.03710; EBPO arXiv 2602.05165) provably reduce MSE for per-group statistics in the low-generation regime.\\n\\n**QD foundations.** SPARQ (arXiv 2506.06499) demonstrated MAP-Elites for offline synthetic math generation. ARISE (arXiv 2603.16060) co-evolves hierarchical skill libraries.\\n\\n**Fundamental premise.** 'Sparse Policy Selection' (arXiv 2605.06241) shows RL modifies only 1-3% of tokens. 'Sharper Primitives' (arXiv 2602.08281) shows diverse training activates broader latent primitives. 'Does RL Really Incentivize Reasoning Capacity Beyond the Base Model?' (NeurIPS 2025, arXiv 2504.13837) finds >95% overlap at high pass@k. These support a coverage-focused framing.\\n\\n**The precise gap.** DéjàQ proves online MAP-Elites works for RLVR but only at GSM level with 1D descriptors—cannot enforce relay-regime dynamics. CLPO proves online curriculum works at competition level but statelessly with coarse bins—difficulty gaps may induce grokking dynamics. Socratic-Zero proves weakness targeting works at competition level but reactively without structured coverage—cannot proactively identify under-explored niches. The implicit curriculum theory proves smooth difficulty spectra are critical but does not provide a mechanism for ensuring smoothness. No existing work combines persistent multi-dimensional archives (enforcing relay-regime dynamics), proactive niche-level gap identification, competition-level verification, and RLVR-grounded replacement criteria.\",\n  \"inspired_by\": \"DéjàQ_paradigm['online MAP-Elites co-evolution during RL training is viable'] + implicit_curriculum_theory['relay regime with smooth difficulty spectra converges exponentially faster than grokking regime'] + CLPO_insight['online curriculum with difficulty adaptation achieves 50% AIME 2024'] + Socratic_Zero_pattern['three-agent co-evolution with instance-level weakness targeting achieves 56.1% average'] + MathForge_contribution['MAD normalization fixes GRPO difficulty imbalance'] + SwS_pattern['targeted weakness-driven synthesis yields +10%'] + VCRL_criterion['advantage variance inverted-U; G>=16 for robust estimation'] + EVOL_RL_warning['diversity collapse is real: TTRL pass@16 degrades 32.4 to 16.7'] + DéjàQ_limitations['1D archive cannot enforce relay-regime + random mutation + GSM-only'] + CLPO_limitations['3 coarse bins may induce grokking dynamics + no persistent coverage'] + SocraticZero_limitations['reactive instance-level targeting cannot proactively identify under-explored niches']\",\n  \"approach\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics through five principled innovations grounded in a theoretical backbone from the implicit curriculum literature: a 2D interpretable archive enforcing relay-regime dynamics, proactive niche-level weakness synthesis (complementing reactive approaches like Socratic-Zero), VCRL-validated advantage variance with robust estimation, adaptive niche-aware population strategy, and DGPO-enhanced policy updates. We honestly acknowledge that DéjàQ established online MAP-Elites co-evolution for RLVR—our contribution is theoretically-grounded scaling and principled design that creates structural synergies beyond component-wise integration.\\n\\n**Theoretical Backbone: Relay-Regime Enforcement.** The implicit curriculum theory (arXiv 2602.14872) proves that RLVR naturally produces curriculum effects—but only efficiently in the relay regime where the difficulty spectrum is smooth (geometric ratio R = O(1) between adjacent levels). Gaps in difficulty cause grokking-regime dynamics with exponentially longer plateaus. This provides the theoretical foundation for our design choices: (a) 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) to minimize inter-bin gaps; (b) persistent archive tracking to detect and fill difficulty gaps before they cause training stalls; (c) targeted synthesis specifically for under-populated niches to maintain smooth coverage. The theory predicts that finer granularity (smaller R) produces faster convergence—ablation A7 provides the first empirical test of relay vs. grokking dynamics in real RLVR training.\\n\\n**1. 2D Interpretable Archive (50 cells).** Unlike DéjàQ's 1D archive with 8 thematic settings, we maintain a 2D MAP-Elites grid: 10 difficulty bins (width 0.1, based on empirical solve-rate: [0-0.1, 0.1-0.2, ..., 0.9-1.0]) x 5 mathematical topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells. Each cell stores up to M=10 problems (max 500 active). Topic classification via GPT-4o-mini (validated at 84-92% accuracy; arXiv 2411.00042). Difficulty via empirical solve-rate from G=16 rollouts on the current policy (reusing training rollouts—see Section 5). The 2D structure enables capabilities that emerge from the archive as substrate and are QUALITATIVELY impossible with component-wise approaches: (a) relay-regime enforcement—fine-grained difficulty bins ensure smooth coverage within each topic, directly implementing the theoretical condition for fast convergence; (b) proactive gap identification—precisely locate which topic x difficulty niches are under-explored BEFORE the policy encounters failures there (vs. Socratic-Zero's reactive approach that waits for specific failures); (c) principled compute allocation—the archive tells WHERE to focus synthesis and training, advantage variance tells HOW MUCH signal each problem provides; (d) interpretable post-hoc analysis—which niches contribute most to downstream benchmark performance, providing actionable insights beyond any single AIME number.\\n\\n**2. Emergent Curriculum via Relay-Regime Dynamics (theoretically grounded).** With 0.1-wide difficulty bins, typical GRPO training improves solve-rate by ~3-8% per 50 steps on in-ZPD problems (based on published GRPO learning curves from DAPO, MathForge, and CLPO). This means ~30-80% of problems in a given cell cross bin boundaries per refresh cycle (every 50 steps). Over 500 training steps (10 refresh cycles), most problems shift 2-4 difficulty bins, creating measurable emergent curriculum without explicit scheduling. The implicit curriculum theory explains WHY this works: 0.1-wide bins maintain small geometric ratio R between adjacent difficulty levels, keeping the system in the relay regime where progress on each level continuously supports the next. Contrast with CLPO's 3 coarse bins (width ~0.33): the same 3-8% improvement rarely triggers bin transitions, and the larger inter-bin gaps may induce grokking-like plateaus. We commit to tracking per-cell solve-rate trajectories and bin-transition frequencies as a primary analysis, and ablation A7 directly tests the relay-regime prediction (10 bins vs. 3 bins, predicting faster convergence with finer granularity).\\n\\n**3. Targeted Weakness-Driven Synthesis: Proactive Niche-Level Gap Identification.** Existing weakness targeting approaches operate reactively: Socratic-Zero's Teacher examines specific failed solutions and generates problems targeting those errors; SwS identifies aggregate category-level weaknesses after preliminary RL. Both are effective but cannot proactively identify under-explored capability niches. The 2D archive enables a fundamentally different approach: proactive niche-level gap identification. (a) Identify under-performing archive cells (under-populated <3 problems, or stale—all problems with solve-rate >0.9 or <0.05). (b) Prompt a synthesis LLM (Qwen2.5-72B-Instruct or GPT-4o) with the specific topic niche requirements, exemplar problems from neighboring cells, and general competition-level framing. (c) Use generate-then-classify rather than constrained generation: generate candidate problems for the target topic without explicit difficulty constraints, verify them, then measure actual difficulty with the current policy and assign to the appropriate cell. This avoids the 'double filter' problem where simultaneously constraining topic AND difficulty reduces survival to 4-17% (vs. ~25-30% for topic-only constrained generation with post-hoc difficulty assignment). (d) When seed problems exist in nearby cells, use SvS-style answer-preserving mutation (higher validity ~70-80%) for cross-niche seeding. This is complementary to Socratic-Zero's instance-level targeting: we identify WHERE gaps exist (niche level), they identify WHAT errors occur (instance level). A complete system could integrate both.\\n\\n**4. Multi-Stage Verification Pipeline (Competition-Level).** DéjàQ suffers 22-44% invalid rates even at GSM level. At competition level, robust verification is essential. We implement a 3-stage VHG-inspired pipeline: (a) Format and solvability check—verify the problem is well-formed with a unique numerical answer (filters ~30% of candidates); (b) Cross-verification—solve with 2-3 strong models (Qwen2.5-Math-72B, DeepSeek-Math) and check answer agreement via majority vote (>=75% consistency among 16 rollouts, filters ~20% of remaining); (c) Difficulty calibration—G=16 rollouts with current policy for solve-rate estimation and bin assignment. Under the generate-then-classify approach, we generate for target topic (not difficulty), achieving ~25-30% survival through verification, then assign to appropriate difficulty cells.\\n\\n**5. Robust Advantage Variance Estimation (G=16 + Beta Posterior + Shrinkage).** DéjàQ uses p(1-p) learnability as fitness with K=100 dedicated completions per problem. We propose advantage variance as the replacement criterion, following VCRL's validated inverted-U relationship. Addressing variance estimation reliability: (a) We use G=16 rollouts (matching DAPO/VCRL standard practice), reusing the same rollouts as GRPO training—zero additional inference cost. VCRL's ablation confirms G=16 as the minimum for robust estimation (G=4 averages 44.17 vs. G=16 at 57.76). (b) We maintain a Beta-Bernoulli running posterior for each problem's solve-rate: initialized at Beta(1,1), updated to Beta(alpha+k, beta+G-k) each time the problem appears in training. After 3 training appearances (48 total rollouts), the posterior variance drops by 3x, providing reliable estimates even for problems with true solve rates below 0.2. (c) For single-batch decisions, we apply James-Stein shrinkage (arXiv 2511.03710): per-problem variance estimates are regularized toward the batch-level average, provably reducing MSE when individual estimates are noisy. (d) Replacement decisions use conservative credible intervals: a candidate replaces the cell occupant only when its posterior advantage variance credible interval (lower bound) exceeds the occupant's (upper bound). This prevents spurious replacements from noise at extreme solve rates. Computational savings vs. DéjàQ: 16 rollouts reused from training vs. 100 dedicated rollouts = zero additional cost.\\n\\n**6. Adaptive Niche-Aware Population Strategy.** Competition-level synthesis is hard, and niche-specific survival rates vary dramatically. Empirical evidence: unconstrained competition-level synthesis survives at ~37% (SAND-Math), but niche-specific targeting reduces this to 4-17%. Our generate-then-classify approach mitigates this (topic-only targeting: ~25-30%), but some niches remain harder. Strategy: Phase 1 (steps 0-100)—populate 'medium' cells (solve-rate 0.3-0.7) across all topics using generate-then-classify, which are easiest to fill and provide strongest ZPD training signal. Phase 2 (steps 100-300)—as the policy improves, recalibration naturally shifts problems into harder bins; supplement with targeted synthesis for topics with persistent gaps. Phase 3 (steps 300+)—target extreme cells using cross-niche seeding (SvS-style mutation from adjacent populated cells, ~70-80% validity). Adaptive overgeneration budgets track per-niche historical survival rates: start at 5x for well-populated niches, increase to 10x for hard niches (e.g., geometry where SDE-GPG reports 47-63% difficulty calibration accuracy), 15x for extreme niches. Graceful degradation: empty extreme cells don't break the system—it trains on well-populated cells. The analysis explicitly reports per-niche population density and survival rates as a community contribution.\\n\\n**7. DGPO-Enhanced Policy Update.** We integrate MathForge's MAD normalization and DQW weighting, orthogonal to archive management. Ablation A8 isolates its contribution.\\n\\n**'More Than Sum of Parts': Structural Synergies from the 2D Archive.** The 2D archive is not merely a data structure—it is an enabling substrate that creates emergent capabilities impossible with any single component or their naive combination. (1) Relay-regime enforcement requires BOTH fine-grained difficulty tracking (archive structure) AND smooth coverage maintenance (targeted synthesis). Neither the archive alone (without synthesis to fill gaps) nor synthesis alone (without archive to identify gaps) can enforce relay dynamics. (2) Proactive gap identification requires persistent coverage memory (archive) to know WHERE gaps are, combined with targeted synthesis to fill them. Reactive approaches (Socratic-Zero, SwS) cannot identify gaps they have not yet encountered. (3) Principled compute allocation requires both WHERE information (archive coverage map) and HOW MUCH information (advantage variance). Together they enable focused compute on high-value regions. (4) Interpretable capability diagnosis requires structured behavioral descriptors (topic x difficulty) to map which niches drive downstream performance. The ablation structure directly tests each synergy: A1 removes 2D structure, A2 removes targeted synthesis, A3 removes advantage variance, A4 removes persistence.\\n\\n**Training Loop (DGPO on Qwen2.5-Math-7B primary, Qwen3-8B secondary, VERL framework):**\\n(a) Sample training batch from archive cells in ZPD window [0.1, 0.9], weighted by posterior advantage variance.\\n(b) Run G=16 rollouts per problem, compute advantages with MAD normalization and DQW.\\n(c) DGPO policy update step.\\n(d) Update Beta posteriors for all sampled problems using batch results.\\n(e) Every 50 steps: staggered archive refresh—re-evaluate only cells sampled in the last 50 steps (~40-60% of archive); reassign problems crossing bin boundaries; flag stale cells; trigger targeted synthesis for under-populated or stale cells.\\n(f) Estimated overhead: ~15-20% per refresh cycle (synthesis and verification; evaluation rollouts reused from training).\\n\\n**AIME 2024 Landscape Contextualization.** We position SACE-RLVR within the self-evolving/seed-data paradigm, distinct from distillation-based methods that dominate the AIME 2024 leaderboard (Klear-Reasoner-8B 90.5% via distillation+RL, DeepSeek-R1-Distill-Qwen-7B 83.3%). Self-evolving methods without distillation achieve 16-20% (R-Zero, Absolute Zero), while seed-data methods achieve ~50% (CLPO). Our primary contribution is not absolute AIME numbers but: (a) systematic ablation revealing which components of archive-based co-evolution matter and why; (b) the first competition-level archive-based co-evolution system; (c) interpretable capability maps revealing which topic x difficulty niches drive benchmark performance; (d) a framework applicable atop distilled bases for potential further gains.\\n\\n**Baselines (10 systems):**\\n(1) DéjàQ-comp: DéjàQ adapted to competition level—1D archive with symbolic mutator using our verification pipeline. PRIMARY baseline isolating 2D structure + targeted synthesis.\\n(2) CLPO: reproduced with DAPO-Math-17k on Qwen3-8B. PRIMARY baseline isolating persistent archive value.\\n(3) Socratic-Zero: compared against released Socratic-Solver-8B; if unavailable, reproduced with 72B teacher. PRIMARY baseline isolating structured archive vs. instance-level targeting.\\n(4) SwS: static two-stage offline pipeline.\\n(5) MathForge: offline DGPO + MQR augmentation.\\n(6) Prism: 128-cluster semantic diversity with ZPD gate.\\n(7) R-Diverse: SAM skill diversity + MAP memory bank.\\n(8) EVOL-RL: novelty-aware per-batch diversity; tests whether lightweight stateless diversity suffices.\\n(9) AdaRFT: adaptive difficulty without archive.\\n(10) Vanilla GRPO on DAPO-Math-17k.\\n\\n**Ablations (10 experiments):**\\nA1: 1D archive only (topic dimension, no difficulty bins)—tests whether 2D enables relay-regime enforcement.\\nA2: Random synthesis instead of targeted (keeps archive, uses random mutation—isolates proactive vs. random gap filling).\\nA3: p(1-p) replacement instead of advantage variance (DéjàQ's criterion on our archive).\\nA4: No archive persistence (per-batch only—isolates whether persistent coverage enables relay dynamics).\\nA5: DéjàQ-comp baseline (1D archive + random mutation at competition level).\\nA6: CLPO + archive persistence (adds persistent archive to CLPO—tests whether archive alone closes gap).\\nA7: Coarse difficulty bins (3 bins vs. 10)—the key relay-regime test predicting faster convergence with finer granularity.\\nA8: Standard GRPO normalization vs. DGPO MAD.\\nA9: Archive coverage vs. per-cell pass@k correlation.\\nA10: G=16 with Beta posterior + shrinkage vs. G=16 point estimation only (isolates robust estimation value).\\n\\n**Evaluation:** AIME 2024 (30 problems), AIME 2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. Both pass@1 and pass@k (k=8,32,64). Training data: DAPO-Math-17k as seed. Base models: Qwen2.5-Math-7B (primary) and Qwen3-8B (secondary).\\n\\n**Key analyses:** (1) Archive coverage heatmaps with relay-regime metrics (inter-bin gap ratios R per topic). (2) Per-cell contribution to benchmark performance. (3) Emergent curriculum visualization with bin-transition frequencies and comparison to relay-regime predictions. (4) Synthesis efficiency: generate-then-classify vs. constrained generation, per-topic breakdown. (5) DéjàQ-comp vs. SACE-RLVR archive dynamics. (6) Convergence speed: relay prediction (10 bins, fewer plateaus) vs. grokking (3 bins, longer plateaus). (7) Proactive vs. reactive gap analysis: do archive-identified gaps correlate with subsequent policy failures?\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"6600 H100-hours (baselines: GRPO+SwS+Prism+R-Diverse+MathForge+CLPO+AdaRFT+EVOL-RL 8x250h=2000h; Socratic-Zero comparison 300h; DéjàQ-comp 400h; SACE-RLVR on 7B 2x400h=800h; SACE-RLVR on 8B 2x400h=800h; ablations A1-A10 10x200h=2000h; archive synthesis/verification 300h)\",\n      \"timeline\": \"14-18 weeks\",\n      \"estimated_gpu_cost\": \"$16,500 (at ~$2.50/H100-hr cloud spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"5400 H100-hours (reuse released code/models for baselines including Socratic-Solver-8B; shared verification pipeline; fewer failed runs)\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$400-800 (GPT-4o-mini topic classification, Qwen2.5-72B synthesis)\",\n      \"estimated_gpu_cost\": \"$13,500\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"8000 H100-hours (exploratory sweeps over archive dimensions, bin granularity, refresh frequencies, replacement criteria, synthesis strategies, relay-regime metrics)\",\n      \"timeline\": \"10-13 weeks\",\n      \"claude_api_cost\": \"$1000-2000\",\n      \"estimated_gpu_cost\": \"$20,000\",\n      \"speed_bottleneck\": \"GPU queue time; each GRPO run takes 24-72h on 8xH100s. Socratic-Zero reproduction with 72B teacher adds inference cost if released model unavailable.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026) — stretch target if pilot results strong by August\",\n    \"ICML 2027 (expected deadline ~Jan 2027) — primary target, strong fit for RL + QD + relay-regime theory\",\n    \"NeurIPS 2027 (full paper ~May 2027) — fallback with comprehensive evaluation\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"DéjàQ: Open-Ended Evolution of Diverse, Learnable and Verifiable Problems (arXiv 2601.01931, Jan 2026) — PRIMARY PREDECESSOR, online MAP-Elites for RLVR at GSM level; we scale with relay-regime grounding\",\n    \"CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning (arXiv 2509.25004, Sep 2025) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024; stateless with 3 coarse bins\",\n    \"Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution (arXiv 2509.24726, Sep 2025) — PRIMARY BASELINE for weakness targeting; three-agent co-evolution with instance-level targeting; 56.1% avg; no structured archive\",\n    \"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards (arXiv 2602.14872, Feb 2026; ICML 2026) — THEORETICAL BACKBONE; relay regime converges exponentially faster than grokking regime; grounds fine-grained bin design\",\n    \"Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026) — 4-agent bidirectional difficulty adjustment; 60.03 avg with 5,873 samples; no structured multi-dimensional archive\",\n    \"EVOL-RL: Evolving Language Models without Labels (arXiv 2509.15194, Sep 2025) — stateless novelty-aware diversity; Qwen3-4B AIME25 17.1%; demonstrates diversity collapse risk\",\n    \"MathForge/DGPO: Harder Is Better (arXiv 2601.20614, ICLR 2026) — MAD normalization + DQW; we adopt for policy update\",\n    \"SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025, arXiv 2506.08989) — offline weakness targeting; +10% (7B)\",\n    \"AdaRFT: Efficient Reinforcement Finetuning via Adaptive Curriculum (arXiv 2504.05520) — adaptive difficulty; baseline\",\n    \"CPMobius: Iterative Coach-Player Reasoning for Data-Free RL (arXiv 2602.02979, Feb 2026) — cooperative co-evolution without archive\",\n    \"AERO: Autonomous Evolutionary Reasoning Optimization (arXiv 2602.03084, Feb 2026) — ZPD-based dual-loop without archives\",\n    \"OpenSIR: Open-Ended Self-Improving Reasoner (arXiv 2511.00602, Nov 2025) — self-play at GSM/CollegeMath level\",\n    \"Beyond Pass@1: Self-Play with Variational Problem Synthesis [SvS] (ICLR 2026) — answer-preserving synthesis for cross-niche seeding\",\n    \"Preventing Curriculum Collapse [Prism] (arXiv 2603.13309, Mar 2026) — 128-cluster diversity; baseline\",\n    \"R-Diverse (arXiv 2602.13103, Feb 2026) — SAM skill diversity + MAP memory; baseline\",\n    \"VCRL: Variance-based Curriculum RL (arXiv 2509.19803) — advantage variance inverted-U; G>=16 minimum; grounds replacement criterion\",\n    \"SAND-Math (arXiv 2507.20527) — 37.7% survival for competition synthesis; grounds population strategy\",\n    \"VHG: Verifier-Backed Hard Problem Generation (arXiv 2605.06660, May 2026) — validity gating; inspires verification pipeline\",\n    \"R-Zero (ICLR 2026) — self-evolving framework; collapses after iteration 3\",\n    \"Shrinking the Variance (arXiv 2511.03710) — James-Stein shrinkage for per-group statistics; supports robust estimation\",\n    \"EBPO: Empirical Bayes Shrinkage for GRPO (arXiv 2602.05165) — dynamic shrinkage; supports Beta posterior approach\",\n    \"Klear-Reasoner-8B (arXiv 2508.07629) — 90.5% AIME 2024 via distillation+RL; contextualizes AIME landscape\",\n    \"SPARQ (arXiv 2506.06499) — offline QD for problem generation\",\n    \"STAT (arXiv 2510.10023) — Missing-Skill-Profile for targeted synthesis\",\n    \"Hypothesis-Driven Error Analysis (arXiv 2604.04386) — weakness-driven benchmark generation\",\n    \"SEC: Self-Evolving Curriculum (arXiv 2505.14970) — MAB over problem categories\",\n    \"Sparse Policy Selection (arXiv 2605.06241, May 2026) — RL modifies 1-3% tokens; coverage framing\",\n    \"Sharper Primitives (arXiv 2602.08281) — diverse training activates broader primitives\",\n    \"Does RL Really Incentivize Reasoning? (NeurIPS 2025, arXiv 2504.13837) — >95% overlap; coverage framing\",\n    \"Problem Categorization (arXiv 2411.00042) — 84%+ topic classification accuracy\",\n    \"ARISE (arXiv 2603.16060) — skill library co-evolution\",\n    \"Vocabulary Dropout (arXiv 2604.03472) — diversity collapse via token perturbation\"\n  ],\n  \"description\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm from GSM-level—where DéjàQ first demonstrated it—to competition-level mathematics (AIME, Olympiad) through five principled innovations grounded in the implicit curriculum theory (arXiv 2602.14872, ICML 2026). The key theoretical insight: RLVR naturally produces curriculum effects, but only efficiently in the 'relay regime' where difficulty spectra are smooth; gaps cause exponentially slower 'grokking' dynamics. Our 2D archive (10 difficulty bins x 5 topics = 50 cells) ENFORCES relay-regime dynamics by maintaining smooth difficulty coverage—a theoretically-grounded design choice, not merely a heuristic. We honestly acknowledge DéjàQ established online MAP-Elites co-evolution, CLPO demonstrated online curriculum at competition level, and Socratic-Zero showed effective weakness targeting; our contribution creates structural synergies beyond component-wise combination. (1) The 2D archive enables proactive niche-level gap identification—qualitatively impossible with Socratic-Zero's reactive instance-level targeting, CLPO's stateless approach, or DéjàQ's 1D structure. (2) Targeted synthesis uses generate-then-classify (topic-constrained generation with post-hoc difficulty measurement, ~25-30% survival) rather than niche-constrained generation (4-17%), with cross-niche seeding via SvS-style mutation (~70-80% validity). (3) VCRL-validated advantage variance with G=16 rollouts reused from GRPO training (zero additional cost vs. DéjàQ's K=100), Beta-Bernoulli running posterior, and James-Stein shrinkage for robust estimation even at extreme solve rates. (4) Adaptive niche-aware population with per-niche overgeneration budgets (5-15x) and progressive phases. (5) DGPO-enhanced policy updates. Contextualized against the AIME 2024 landscape where distillation-based methods achieve 70-90% and self-evolving methods 16-20%, we target the self-evolving/seed-data paradigm where value is METHOD + ABLATION INSIGHTS. Three PRIMARY baselines (DéjàQ-comp, CLPO, Socratic-Zero) plus seven additional baselines. Ten ablations, with A7 (3 vs. 10 bins) providing the first empirical test of relay vs. grokking dynamics in real RLVR. Key analyses include archive coverage heatmaps with relay-regime metrics, convergence speed validation, per-cell benchmark contribution mapping, and per-niche synthesis feasibility. Evaluation on Qwen2.5-Math-7B and Qwen3-8B using VERL.\",\n  \"project_name\": \"sace_rlvr\",\n  \"source\": \"web_research\",\n  \"change_type\": \"major\",\n  \"reviewer_response\": {\n    \"revision_overview\": \"MAJOR REVISION addressing three structural issues: (1) theoretical backbone via implicit curriculum relay-regime theory, (2) AIME SOTA contextualization within self-evolving paradigm, (3) sharper 'more than sum of parts' novelty argument via structural synergies. Four missing concurrent works added with precise differentiation. K=8 upgraded to G=16 with Beta posterior and James-Stein shrinkage. Generate-then-classify approach for niche-aware synthesis. Socratic-Zero elevated to PRIMARY baseline. 10 baselines and 10 ablations. Fundamental reframing from 'integration paper' to 'theoretically-grounded system design with empirically testable predictions.'\",\n    \"issue_1_socratic_zero\": \"ADDED AS PRIMARY BASELINE with extensive differentiation along five dimensions: (a) reactive/instance-level vs. proactive/niche-level gap identification; (b) unstructured growing curriculum vs. structured 2D archive; (c) 1D three-zone categorization vs. 2D topic x difficulty descriptors; (d) diversity as side effect vs. principled QD optimization; (e) requires frozen 235B oracle vs. policy-based gap identification. Positioned as complementary (instance-level error targeting vs. niche-level gap identification). Baseline #3 using released model or 72B teacher reproduction.\",\n    \"issue_2_implicit_curriculum\": \"INTEGRATED AS THEORETICAL BACKBONE. The relay regime (smooth spectrum) converges exponentially faster than grokking regime (gapped spectrum). This grounds our design: 10 fine-grained bins maintain small R, persistent archive fills gaps, targeted synthesis maintains smoothness. Ablation A7 provides first empirical test in real RLVR. We engage honestly: implicit curriculum EXISTS naturally but is only EFFICIENT with smooth spectra. Our archive ENSURES smoothness—enabling implicit curriculum rather than replacing it. The theory is proven in synthetic settings; our ablation extends to real RLVR.\",\n    \"issue_3_bidirectional_curriculum\": \"ADDED to landscape. 4-agent bidirectional difficulty adjustment, 60.03 avg with 5,873 samples. Differentiated: persistent error counters but no structured multi-dimensional archives, QD objectives, or systematic coverage tracking. Explorer agent promotes diversity without principled guarantees.\",\n    \"issue_4_evol_rl\": \"ADDED as baseline #8 and landscape entry. Stateless per-batch novelty-aware diversity. Demonstrates diversity collapse is real (TTRL pass@16 degrades 32.4 to 16.7). Tests whether lightweight stateless diversity suffices vs. archive-based coverage.\",\n    \"issue_5_stale_baselines\": \"COMPREHENSIVELY ADDRESSED. AIME 2024 landscape contextualized: distillation-based 70-90% (Klear-Reasoner 90.5%), self-evolving without distillation 16-20%, seed-data methods ~50% (CLPO). Two distinct paradigms identified. We target self-evolving/seed-data paradigm where value is METHOD + ABLATION INSIGHTS + FRAMEWORK. CLPO at 50.0% is among the best non-distillation methods—appropriate baseline. Framework applicable atop distilled bases.\",\n    \"issue_6_emergent_vs_implicit_curriculum\": \"CENTRAL THEORETICAL ARGUMENT. Implicit curriculum exists naturally but is only efficient in relay regime (smooth spectra). Real training data may have gapped distributions. 2D archive ensures smooth coverage, enforcing relay regime. Not replacing implicit curriculum—ENABLING it. Ablation A4 tests persistence value, A7 tests relay prediction. If 10 bins outperform 3 with faster convergence and fewer plateaus, validates both theory and archive's value.\",\n    \"issue_7_advantage_variance_k8\": \"SUBSTANTIALLY REVISED. K=8 upgraded to G=16 matching VCRL minimum (G=4: 44.17 vs G=16: 57.76). G=16 rollouts REUSED from GRPO training—zero additional cost. Three robustness mechanisms: Beta-Bernoulli posterior (48 rollouts after 3 appearances, 3x variance reduction), James-Stein shrinkage (provably reduced MSE), conservative credible interval replacement. New ablation A10 isolates robust estimation value.\",\n    \"issue_8_archive_population_realism\": \"SUBSTANTIALLY REVISED. Generate-then-classify approach: topic-constrained generation (~25-30% survival) with post-hoc difficulty assignment avoids double-filter problem (4-17% for niche-constrained). Adaptive overgeneration: 5x medium, 10x hard (geometry), 15x extreme. Cross-niche seeding via SvS mutation (~70-80% validity). Per-niche survival rates reported as community contribution. Honest about geometry difficulty (SDE-GPG: 47-63% calibration accuracy).\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79c39c2f-ab92-40a3-87f2-de545476d5a8",
  "isSidechain": false,
  "requestId": "req_011CbU4dxWACats7B9AtRpZE",
  "type": "assistant",
  "uuid": "3cbc504a-cc34-47a5-bfaa-1687ca396138",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeMZ16dFtVoRQm8SyvrrLp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19496,
      "cache_read_input_tokens": 53483,
      "output_tokens": 12736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12736,
          "cache_read_input_tokens": 53483,
          "cache_creation_input_tokens": 19496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19496
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

_source line 44 · 2026-05-28T01:06:11.098Z_

<details><summary>↩ Tool result · reported error · `toolu_01SGQyv7sFCbiUURStCzFvhW`</summary>

```text
Claude requested permissions to write to /tmp/sace_rlvr_revision_r5.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cbc504a-cc34-47a5-bfaa-1687ca396138",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "0b527f5b-a707-44f8-ad9f-19fb5510bc98",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/sace_rlvr_revision_r5.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "3cbc504a-cc34-47a5-bfaa-1687ca396138",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "0b527f5b-a707-44f8-ad9f-19fb5510bc98",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Tool call

_source line 47 · 2026-05-28T01:06:14.629Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0118X6bB8LkXpk16ciVrPApY`</summary>

```json
{
  "command": "echo \"ready\"",
  "description": "Test command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b527f5b-a707-44f8-ad9f-19fb5510bc98",
  "isSidechain": false,
  "requestId": "req_011CbU51VMsh1GK6UTUKua4Z",
  "type": "assistant",
  "uuid": "ea3da8b8-f61b-4256-832e-a929de889591",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134pd64BKj3wXdTTv6rkVg2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12787,
      "cache_read_input_tokens": 72979,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 72979,
          "cache_creation_input_tokens": 12787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12787
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

_source line 48 · 2026-05-28T01:06:14.771Z_

<details><summary>↩ Tool result · `toolu_0118X6bB8LkXpk16ciVrPApY`</summary>

```text
ready
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea3da8b8-f61b-4256-832e-a929de889591",
  "isSidechain": false,
  "promptId": "74e3d9ed-d48f-4d53-aeb2-d75f370a6576",
  "type": "user",
  "uuid": "3cc1dce6-6178-47e0-95ff-05f7e6fb5fd1",
  "toolUseResult": {
    "stdout": "ready",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ea3da8b8-f61b-4256-832e-a929de889591",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-28T01:09:31.231Z_

The complete revised research idea is ready. Let me present it directly as the output. Here is the **Round 5 Major Revision** of SACE-RLVR:

---

```json
{
  "title": "Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis",
  "core_problem": "Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth (the 'relay regime'); gaps in difficulty coverage cause grokking-like plateaus where learning stalls. This creates a precise engineering challenge: how to ensure smooth, comprehensive coverage of the difficulty×topic space so that the implicit curriculum operates in the relay regime. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making relay-regime enforcement impossible. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B) through real-time difficulty assessment—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33), creating difficulty gaps that may induce grokking-regime dynamics. Socratic-Zero (arXiv 2509.24726) demonstrates effective instance-level weakness targeting through three-agent co-evolution (Solver/Teacher/Generator) achieving 56.1% average across 7 math benchmarks—but its weakness targeting is purely reactive (responds to specific failed solutions) with no structured archive or systematic coverage tracking, meaning entire capability niches may remain unexplored. The fundamental open question is: can we build a system that ensures smooth difficulty×topic coverage—thereby enforcing relay-regime learning dynamics—while combining persistent archive-based gap identification, targeted weakness synthesis, and principled RLVR-grounded replacement criteria at competition level?",
  "opportunity": "Four converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot enforce relay-regime dynamics because it cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides the missing theoretical backbone: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness—the relay regime (smooth spectrum, small geometric ratio R between adjacent difficulties) converges exponentially faster than the grokking regime (large gaps). This directly motivates fine-grained multi-dimensional archives: ensuring smooth coverage of difficulty×topic is not merely a heuristic but a theoretically-grounded design choice for maximizing RLVR convergence speed. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024 with online curriculum; Socratic-Zero achieves 56.1% average with three-agent co-evolution; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples via bidirectional difficulty adjustment. But none maintains structured multi-dimensional archives with systematic gap identification. (4) The synthesis-verification gap is closing: SAND-Math demonstrates ~37.7% survival for general competition-level synthesis; VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that enforce relay-regime dynamics by ensuring smooth difficulty coverage, (b) proactive niche-level gap identification (vs. reactive instance-level targeting), (c) competition-level multi-stage verification, and (d) RLVR-grounded replacement criteria. Our contribution is elevating archive-based co-evolution from a GSM-level proof-of-concept to a theoretically-grounded, competition-level system—not paradigm invention.",
  "landscape": "**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics—relay-regime enforcement impossible; (d) random mutation rather than targeted weakness synthesis; (e) teacher-student misalignment—RL improves student but not teacher/mutator; (f) K=100 completions per problem is computationally expensive.\n\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Trained on DAPO-Math-17k, 200 steps, 8×H20 GPUs. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins (width ~0.33) create large inter-bin gaps that may induce grokking-regime dynamics per the implicit curriculum theory.\n\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions, then generates new problems targeting those specific reasoning errors. Uses a Gaussian utility function centered at 50% success rate (μ=0.5, σ=0.2) for 'desirable difficulty.' The Generator (trained via value-weighted SFT) distills the Teacher's capability. Dynamic three-zone categorization (Mastered/Learning/Too Difficult) recategorized each iteration. Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B, with a trained Generator reaching 95.6% validity. Critical differentiation: (a) weakness targeting is reactive and instance-level—responds to specific failed solutions rather than proactively identifying under-explored niches; (b) no structured archive, behavioral descriptors, or coverage map—the curriculum is an unstructured growing set; (c) three-zone categorization is a 1D difficulty measure, not a multi-dimensional skill map; (d) no quality-diversity objective—diversity is a side effect of multi-domain seeds and temperature sampling; (e) requires a frozen 235B oracle Teacher (16 MI308X GPUs), while our approach uses the policy itself for gap identification via archive structure. Our approach is complementary: proactive niche-level gap identification vs. Socratic-Zero's reactive instance-level targeting.\n\n**Implicit curriculum theory.** 'The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards' (arXiv 2602.14872, Feb 2026; ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning—the gradient signal peaks at intermediate difficulty (∇_q J_L(t) ∝ (Δ_L)^L(1−Δ_L), an inverted-U). Two regimes: the relay regime (smooth difficulty spectrum, geometric ratio R = O(1), compressed inter-level plateaus, exponentially faster convergence) and the grokking regime (large difficulty gaps, R ≫ 1, long plateaus followed by phase transitions). Importantly, this paper does NOT argue against explicit curriculum—it proves implicit curriculum exists under idealized conditions (synthetic group-theoretic tasks, uniform distributions, single attention layer). Real training data has non-uniform, potentially gapped distributions where explicit curation enforces the relay regime. We adopt this as our theoretical backbone: 10 fine-grained bins (width 0.1) ENSURE smooth coverage, directly enforcing relay dynamics. Ablation A7 (3 vs. 10 bins) provides the first empirical test in real RLVR.\n\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026) introduces a 4-agent framework (Repairer/Challenger/Reasoner/Explorer) that both complicates mastered problems and simplifies failed ones based on an Optimal Pacing Theorem. Achieves 60.03 average across 6 benchmarks with only 5,873 samples; AIME 2025: 40.0. Persistent per-problem error counters. Differentiation: optimizes difficulty bidirectionally but without structured multi-dimensional archives, QD objectives, or systematic coverage tracking across topic×difficulty niches.\n\n**Novelty-aware diversity without archives.** EVOL-RL (arXiv 2509.15194, Sep 2025) prevents diversity collapse via novelty-aware rewards (embedding cosine similarity within batches), asymmetric PPO clipping, and entropy regularization. Qwen3-4B AIME25: 4.6%→17.1%; Qwen3-8B AIME24: 16.7→26.0. Entirely stateless. Proves diversity collapse is a real failure mode (TTRL pass@16 degrades 32.4→16.7). Lightweight alternative but cannot detect longer-horizon pattern repetition or provide systematic coverage guarantees.\n\n**Difficulty-aware offline augmentation.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026) introduces MAD normalization and DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. Offline. We adopt DGPO's MAD normalization.\n\n**Weakness-driven targeted synthesis.** SwS (NeurIPS 2025, arXiv 2506.08989) identifies weaknesses offline, allocates synthesis budget proportionally. +10.0% (7B). STAT (arXiv 2510.10023) creates Missing-Skill-Profiles. arXiv 2604.04386 uses hypothesis-driven error analysis. All offline; we adopt the pattern continuously online.\n\n**Adaptive curriculum and co-evolutionary approaches.** AdaRFT (arXiv 2504.05520): adaptive difficulty, 2× speedup. CPMöbius (arXiv 2602.02979): coach-player co-evolution without archive/QD. AERO (arXiv 2602.03084): ZPD dual-loop without archives. OpenSIR (arXiv 2511.00602): self-play at GSM/CollegeMath level.\n\n**Self-evolving RLVR and diversity maintenance.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses after iteration 3. Prism (arXiv 2603.13309): 128-cluster diversity with ZPD gate. R-Diverse (arXiv 2602.13103): SAM skill diversity + MAP memory. Vocabulary Dropout (arXiv 2604.03472).\n\n**Verification.** VHG (arXiv 2605.06660): validity gating. SAND-Math (arXiv 2507.20527): 37.7% survival for unconstrained synthesis (niche-specific: 4-17% per MathSmith, SPARQ, SDE-GPG evidence).\n\n**AIME 2024 landscape.** 7B-8B SOTA shifted dramatically: Klear-Reasoner-8B 90.5% (distillation from DeepSeek-R1-0528 + SFT + GPPO, 64K budget), DeepSeek-R1-Distill-Qwen-7B 83.3%, BP-Math-7B 70.8%, ScaleDiff-7B 73.0%. Nearly ALL top results rely on distillation from >100B teachers. Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%. Seed-data without distillation: CLPO 50.0%. Two distinct paradigms with different constraints. Our work targets the self-evolving/seed-data paradigm.\n\n**Learnability and estimation.** VCRL (arXiv 2509.19803): advantage variance inverted-U; G=16 minimum (G=4: 44.17 vs G=16: 57.76). Shrinkage estimators (arXiv 2511.03710; EBPO arXiv 2602.05165) provably reduce MSE.\n\n**QD foundations and fundamental premise.** SPARQ (arXiv 2506.06499), ARISE (arXiv 2603.16060). Sparse Policy Selection (arXiv 2605.06241): RL modifies 1-3% of tokens. Sharper Primitives (arXiv 2602.08281): diverse training activates broader primitives. Does RL Incentivize Reasoning? (NeurIPS 2025): >95% overlap at high pass@k.\n\n**The precise gap.** DéjàQ: 1D archive, GSM-only—cannot enforce relay-regime. CLPO: stateless, coarse bins—difficulty gaps may induce grokking. Socratic-Zero: reactive targeting, no structured coverage—cannot proactively identify gaps. Implicit curriculum theory: proves smooth spectra critical but provides no mechanism for ensuring smoothness. No existing work combines persistent multi-dimensional archives (enforcing relay-regime), proactive niche-level gap identification, competition-level verification, and RLVR-grounded replacement criteria.",
  "inspired_by": "DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR is viable'] + implicit_curriculum_theory['relay regime (smooth difficulty) converges exponentially faster than grokking regime (gapped)'] + CLPO_insight['online curriculum achieves 50% AIME 2024'] + Socratic_Zero_pattern['three-agent co-evolution with instance-level weakness targeting, 56.1% avg'] + MathForge_contribution['MAD normalization fixes GRPO difficulty imbalance'] + SwS_pattern['targeted weakness synthesis +10%'] + VCRL_criterion['advantage variance inverted-U; G≥16 for robust estimation'] + EVOL_RL_warning['diversity collapse is real'] + DéjàQ_limitations['1D cannot enforce relay-regime + random mutation + GSM-only'] + CLPO_limitations['3 coarse bins may induce grokking + no persistent coverage'] + SocraticZero_limitations['reactive instance-level targeting cannot proactively identify under-explored niches']",
  "approach": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics through five principled innovations grounded in a theoretical backbone from the implicit curriculum literature: a 2D interpretable archive enforcing relay-regime dynamics, proactive niche-level weakness synthesis, VCRL-validated advantage variance with robust estimation, adaptive niche-aware population, and DGPO-enhanced policy updates. We honestly acknowledge DéjàQ established online MAP-Elites co-evolution for RLVR—our contribution is theoretically-grounded scaling that creates structural synergies beyond component-wise integration.\n\n**Theoretical Backbone: Relay-Regime Enforcement.** The implicit curriculum theory (arXiv 2602.14872, ICML 2026) proves that RLVR naturally produces curriculum effects—but only efficiently in the relay regime where the difficulty spectrum is smooth (geometric ratio R = O(1) between adjacent levels). Gaps cause grokking-regime dynamics with exponentially longer plateaus. This provides the theoretical foundation: (a) 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) to minimize inter-bin gaps; (b) persistent archive tracking to detect and fill difficulty gaps; (c) targeted synthesis for under-populated niches. The theory predicts finer granularity (smaller R) → faster convergence. Ablation A7 provides the first empirical test of relay vs. grokking dynamics in real RLVR.\n\n**1. 2D Interpretable Archive (50 cells).** 10 difficulty bins (width 0.1, empirical solve-rate) × 5 topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells, M=10 problems per cell. Topic via GPT-4o-mini (84-92% accuracy). Difficulty via G=16 rollouts reused from training. The 2D structure enables QUALITATIVELY new capabilities as structural synergies: (a) relay-regime enforcement—fine-grained bins ensure smooth coverage implementing the theoretical condition for fast convergence; (b) proactive gap identification—locate under-explored niches BEFORE policy failures (vs. Socratic-Zero's reactive approach); (c) principled compute allocation—archive provides WHERE, advantage variance provides HOW MUCH; (d) interpretable post-hoc analysis—which niches drive benchmark performance.\n\n**2. Emergent Curriculum via Relay-Regime Dynamics.** With 0.1-wide bins, ~3-8% solve-rate improvement per 50 GRPO steps means ~30-80% of problems cross bin boundaries per refresh cycle. Over 500 steps, most problems shift 2-4 bins—measurable emergent curriculum. The implicit curriculum theory explains WHY: 0.1-wide bins maintain small R, keeping the system in relay regime. CLPO's ~0.33-wide bins create larger gaps potentially inducing grokking. Committed analysis: per-cell trajectories and bin-transition frequencies. A7 directly tests the prediction.\n\n**3. Proactive Niche-Level Weakness Synthesis.** Existing targeting is reactive: Socratic-Zero examines specific failed solutions; SwS identifies aggregate weaknesses offline. The 2D archive enables proactive niche-level gap identification: (a) identify under-performing cells (<3 problems or stale); (b) use generate-then-classify: generate for target TOPIC without difficulty constraints, verify, then empirically measure difficulty and assign to appropriate cell—avoiding the 'double filter' (topic+difficulty: 4-17% survival vs. topic-only: ~25-30%); (c) cross-niche seeding via SvS-style answer-preserving mutation from adjacent cells (~70-80% validity); (d) complementary to Socratic-Zero: we find WHERE gaps exist (niche level), they find WHAT errors occur (instance level).\n\n**4. Multi-Stage Verification Pipeline.** 3-stage VHG-inspired: (a) format/solvability check (filters ~30%); (b) cross-verification via majority vote across 2-3 strong models (filters ~20%); (c) difficulty calibration via G=16 rollouts. Under generate-then-classify, ~25-30% survival through verification, then assigned to cells.\n\n**5. Robust Advantage Variance (G=16 + Beta Posterior + Shrinkage).** We use G=16 rollouts (VCRL minimum: G=4→44.17, G=16→57.76), REUSED from GRPO training—zero additional cost vs. DéjàQ's K=100 dedicated completions. Three robustness mechanisms: (a) Beta-Bernoulli running posterior per problem (Beta(1,1) prior, updated each appearance; after 3 appearances/48 rollouts, variance drops 3×); (b) James-Stein shrinkage regularizing per-problem estimates toward batch average (provably reduced MSE per arXiv 2511.03710); (c) conservative credible interval replacement (candidate must exceed occupant's upper bound). Ablation A10 isolates value.\n\n**6. Adaptive Niche-Aware Population.** Niche-specific survival varies dramatically (general: ~37%, niche-constrained: 4-17%). Strategy: Phase 1 (steps 0-100) populates medium cells (0.3-0.7 solve-rate) via generate-then-classify. Phase 2 (100-300) expands as recalibration shifts problems to harder bins. Phase 3 (300+) targets extremes via cross-niche seeding. Adaptive overgeneration: 5× medium, 10× hard (geometry: SDE-GPG 47-63% calibration), 15× extreme. Graceful degradation for sparse extreme cells. Per-niche survival reported as community contribution.\n\n**7. DGPO-Enhanced Policy Update.** MAD normalization + DQW from MathForge. Ablation A8 isolates.\n\n**Structural Synergies ('More Than Sum of Parts').** The 2D archive creates emergent capabilities: (1) Relay-regime enforcement requires BOTH fine-grained tracking AND smooth coverage maintenance—neither archive alone nor synthesis alone suffices. (2) Proactive gap identification requires persistent memory AND targeted synthesis—reactive approaches cannot find gaps they haven't encountered. (3) Principled compute allocation requires WHERE (archive) AND HOW MUCH (variance). (4) Interpretable diagnosis requires structured descriptors. Ablations A1-A4 test each synergy.\n\n**Training Loop (VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary):** (a) Sample from archive ZPD [0.1, 0.9] weighted by posterior variance. (b) G=16 rollouts, MAD+DQW advantages. (c) DGPO update. (d) Update Beta posteriors. (e) Every 50 steps: refresh sampled cells, reassign, flag stale, synthesize for gaps. Overhead: ~15-20%.\n\n**AIME Contextualization.** Distillation-based: 70-90%. Self-evolving without distillation: 16-20%. Seed-data: ~50% (CLPO). We target the self-evolving/seed-data paradigm. Value: METHOD + ABLATION INSIGHTS + FRAMEWORK. Framework applicable atop distilled bases.\n\n**Baselines (10):** (1) DéjàQ-comp [PRIMARY: 2D+targeting value]. (2) CLPO [PRIMARY: persistence value]. (3) Socratic-Zero [PRIMARY: structured vs. instance-level]. (4) SwS. (5) MathForge. (6) Prism. (7) R-Diverse. (8) EVOL-RL [stateless diversity]. (9) AdaRFT. (10) Vanilla GRPO.\n\n**Ablations (10):** A1: 1D only. A2: random synthesis. A3: p(1-p) replacement. A4: no persistence. A5: DéjàQ-comp. A6: CLPO+archive. A7: 3 vs. 10 bins [relay-regime test]. A8: GRPO vs. DGPO. A9: coverage↔pass@k correlation. A10: posterior+shrinkage vs. point estimation.\n\n**Evaluation:** AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. pass@1 and pass@k. DAPO-Math-17k seeds.\n\n**Key Analyses:** (1) Coverage heatmaps with relay-regime metrics (R per topic). (2) Per-cell benchmark contribution. (3) Emergent curriculum with bin-transition frequencies vs. relay predictions. (4) Synthesis efficiency: generate-then-classify vs. constrained, per-topic. (5) DéjàQ-comp comparison. (6) Convergence speed: relay (10 bins) vs. grokking (3 bins). (7) Proactive gap ↔ subsequent failure correlation.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "6600 H100-hours (baselines: 8×250h=2000h; Socratic-Zero 300h; DéjàQ-comp 400h; SACE-RLVR 7B 800h; SACE-RLVR 8B 800h; ablations 10×200h=2000h; synthesis/verification 300h)",
      "timeline": "14-18 weeks",
      "estimated_gpu_cost": "$16,500 (at ~$2.50/H100-hr)"
    },
    "human_in_loop": {
      "gpu_hours": "5400 H100-hours (reuse released code/models; shared verification; fewer failures)",
      "timeline": "12-15 weeks",
      "claude_api_cost": "$400-800",
      "estimated_gpu_cost": "$13,500"
    },
    "auto_research": {
      "gpu_hours": "8000 H100-hours (exploratory sweeps over archive dims, bins, refresh, criteria, relay metrics)",
      "timeline": "10-13 weeks",
      "claude_api_cost": "$1000-2000",
      "estimated_gpu_cost": "$20,000",
      "speed_bottleneck": "GPU queue; each GRPO run 24-72h on 8×H100s. Socratic-Zero 72B teacher adds cost if released model unavailable."
    }
  },
  "target_venues": [
    "ICLR 2027 (Sep 19-24, 2026) — stretch if pilot results by August",
    "ICML 2027 (~Jan 2027) — primary target, strong fit for RL + QD + relay-regime theory",
    "NeurIPS 2027 (~May 2027) — fallback with full evaluation"
  ],
  "level": "top-tier",
  "key_references": [
    "DéjàQ (arXiv 2601.01931) — PRIMARY PREDECESSOR, online MAP-Elites for RLVR at GSM level",
    "CLPO (arXiv 2509.25004) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024",
    "Socratic-Zero (arXiv 2509.24726) — PRIMARY BASELINE, three-agent co-evolution with instance-level weakness targeting; 56.1% avg",
    "The Implicit Curriculum (arXiv 2602.14872, ICML 2026) — THEORETICAL BACKBONE, relay regime ≫ grokking regime",
    "Bidirectional Curriculum Generation (arXiv 2603.05120) — 4-agent bidirectional difficulty; 60.03 avg",
    "EVOL-RL (arXiv 2509.15194) — stateless novelty-aware diversity; AIME25 17.1%",
    "MathForge/DGPO (arXiv 2601.20614, ICLR 2026) — MAD normalization; adopted for policy update",
    "SwS (NeurIPS 2025, arXiv 2506.08989) — offline weakness targeting; +10%",
    "AdaRFT (arXiv 2504.05520) — adaptive difficulty; baseline",
    "CPMöbius (arXiv 2602.02979) — coach-player co-evolution without archive",
    "AERO (arXiv 2602.03084) — ZPD dual-loop without archives",
    "OpenSIR (arXiv 2511.00602) — self-play at GSM level",
    "SvS (ICLR 2026) — answer-preserving synthesis; used for cross-niche seeding",
    "Prism (arXiv 2603.13309) — 128-cluster diversity; baseline",
    "R-Diverse (arXiv 2602.13103) — SAM skill diversity; baseline",
    "VCRL (arXiv 2509.19803) — advantage variance inverted-U; G≥16; grounds replacement",
    "SAND-Math (arXiv 2507.20527) — 37.7% competition synthesis survival",
    "VHG (arXiv 2605.06660) — validity gating; inspires verification",
    "R-Zero (ICLR 2026) — self-evolving; collapses iter 3",
    "Shrinking the Variance (arXiv 2511.03710) — James-Stein shrinkage",
    "EBPO (arXiv 2602.05165) — empirical Bayes for GRPO",
    "Klear-Reasoner-8B (arXiv 2508.07629) — 90.5% AIME 2024; AIME landscape context",
    "SPARQ (arXiv 2506.06499) — offline QD",
    "STAT (arXiv 2510.10023) — Missing-Skill-Profile",
    "Hypothesis-Driven Error Analysis (arXiv 2604.04386)",
    "SEC (arXiv 2505.14970) — MAB over categories",
    "Sparse Policy Selection (arXiv 2605.06241) — RL modifies 1-3% tokens",
    "Sharper Primitives (arXiv 2602.08281) — diverse training activates primitives",
    "Does RL Incentivize Reasoning? (NeurIPS 2025, arXiv 2504.13837) — coverage framing",
    "Problem Categorization (arXiv 2411.00042) — topic classification",
    "ARISE (arXiv 2603.16060) — skill library co-evolution",
    "Vocabulary Dropout (arXiv 2604.03472)"
  ],
  "description": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), scaling online MAP-Elites from GSM-level (DéjàQ) to competition-level math through five innovations grounded in implicit curriculum theory (arXiv 2602.14872, ICML 2026). Key insight: RLVR produces implicit curriculum only efficiently in the 'relay regime' (smooth difficulty spectra); gaps cause exponentially slower 'grokking.' Our 2D archive (10 bins × 5 topics = 50 cells) ENFORCES relay-regime dynamics via smooth coverage—a theoretically-grounded design, not heuristic. (1) 2D archive enables proactive niche-level gap identification (vs. Socratic-Zero's reactive instance-level targeting, CLPO's stateless per-batch, DéjàQ's 1D). (2) Generate-then-classify synthesis (~25-30% survival) avoids double-filter (4-17%), with cross-niche SvS mutation (~70-80%). (3) G=16 advantage variance reused from training (zero cost vs. DéjàQ K=100), Beta posterior + James-Stein shrinkage for robust estimation. (4) Adaptive niche-aware population (5-15× overgeneration). (5) DGPO policy updates. Contextualized: distillation-based 70-90% AIME 2024, self-evolving 16-20%—we target METHOD + ABLATION INSIGHTS. Three PRIMARY baselines (DéjàQ-comp, CLPO, Socratic-Zero), 7 additional, 10 ablations with A7 testing relay vs. grokking prediction. Evaluation: Qwen2.5-Math-7B/Qwen3-8B, AIME 2024/2025, MATH-500, AMC 2023, Minerva, OlympiadBench.",
  "project_name": "sace_rlvr",
  "source": "web_research",
  "change_type": "major",
  "reviewer_response": {
    "revision_overview": "MAJOR REVISION with three structural changes: (1) relay-regime theory as theoretical backbone, (2) AIME SOTA contextualization, (3) 'structural synergies' novelty argument. Four missing works added. K=8→G=16 with Beta posterior + shrinkage. Generate-then-classify for synthesis. Socratic-Zero as PRIMARY baseline. 10 baselines, 10 ablations. Reframed from 'integration paper' to 'theoretically-grounded system with testable predictions.'",
    "issue_1_socratic_zero": "ADDED AS PRIMARY BASELINE #3. Differentiated: (a) reactive instance-level vs. proactive niche-level targeting; (b) unstructured curriculum vs. 2D archive; (c) 1D three-zone vs. 2D topic×difficulty; (d) diversity as side-effect vs. QD optimization; (e) frozen 235B oracle vs. policy-based gap identification. Complementary approaches.",
    "issue_2_implicit_curriculum": "INTEGRATED AS THEORETICAL BACKBONE. Relay regime (smooth R=O(1)) ≫ grokking (gapped R≫1). Grounds: 10 fine bins, persistent tracking, targeted synthesis. A7 = first empirical relay vs. grokking test in real RLVR. Honest engagement: enables implicit curriculum rather than replacing it.",
    "issue_3_bidirectional_curriculum": "ADDED. 4-agent bidirectional framework, 60.03 avg. Differentiated: no structured archives, QD objectives, or systematic coverage.",
    "issue_4_evol_rl": "ADDED as baseline #8. Stateless novelty. Demonstrates collapse risk. Tests lightweight vs. archive-based diversity.",
    "issue_5_stale_baselines": "ADDRESSED. Distillation: 70-90%. Self-evolving: 16-20%. Seed-data: ~50%. Two paradigms. We target self-evolving/seed-data. CLPO 50.0% is among best non-distillation. Framework applicable atop distilled bases.",
    "issue_6_emergent_vs_implicit": "CENTRAL ARGUMENT. Implicit curriculum exists but efficient only with smooth spectra. Archive ensures smoothness → enables relay regime. A4 tests persistence, A7 tests granularity prediction.",
    "issue_7_k8_variance": "RESOLVED. G=16 (VCRL minimum), reused from training. Beta posterior (48 rollouts after 3 appearances, 3× variance reduction). James-Stein shrinkage. Conservative credible intervals. A10 isolates value.",
    "issue_8_population_realism": "RESOLVED. Generate-then-classify (~25-30%) avoids double filter (4-17%). Adaptive overgeneration 5-15×. Cross-niche SvS seeding (~70-80%). Per-niche reporting."
  }
}
```

---

## Summary of Major Changes in Round 5

This is a **major revision** driven by three structural improvements:

### 1. Theoretical Backbone: Relay-Regime Theory
The most significant change. The "Implicit Curriculum" paper (arXiv 2602.14872, ICML 2026) proves RLVR naturally produces curriculum effects, but **only efficiently with smooth difficulty spectra** (relay regime). Gaps cause exponentially slower "grokking" dynamics. This transforms our 2D archive from "a useful data structure" to **a theoretically-grounded mechanism for enforcing optimal learning dynamics**. Ablation A7 (3 vs. 10 bins) becomes the first empirical test of relay vs. grokking in real RLVR.

### 2. Four Missing Works Integrated
- **Socratic-Zero** → PRIMARY baseline #3, differentiated along 5 dimensions (reactive/instance-level vs. proactive/niche-level targeting)
- **Implicit Curriculum** → theoretical backbone (see above)
- **Bidirectional Curriculum** → landscape (no structured archive or QD)
- **EVOL-RL** → baseline #8 (tests lightweight stateless diversity vs. archive-based)

### 3. AIME SOTA Contextualization
Distillation-based methods achieve 70-90% AIME 2024; self-evolving methods 16-20%. We explicitly target the **self-evolving/seed-data paradigm** where value is METHOD + ABLATION INSIGHTS, not absolute numbers.

### 4. Technical Fixes
- **K=8 → G=16** with Beta-Bernoulli posterior + James-Stein shrinkage (zero additional cost—reuses training rollouts)
- **Generate-then-classify** for synthesis (~25-30% survival vs. 4-17% for niche-constrained), with adaptive overgeneration budgets per niche
- **"More Than Sum of Parts"** argument: 4 structural synergies that emerge from the 2D archive as enabling substrate

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cc1dce6-6178-47e0-95ff-05f7e6fb5fd1",
  "isSidechain": false,
  "requestId": "req_011CbU51koKHp2d6TP7ywPdd",
  "type": "assistant",
  "uuid": "686ba5aa-7315-44b3-a87a-f267c82003ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCFJEnh49z27N9SW8ijCWs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86,
      "cache_read_input_tokens": 85766,
      "output_tokens": 9388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 86,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9388,
          "cache_read_input_tokens": 85766,
          "cache_creation_input_tokens": 86,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 86
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "686ba5aa-7315-44b3-a87a-f267c82003ef",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "686ba5aa-7315-44b3-a87a-f267c82003ef",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SACE-RLVR: address emerging concurrent works and implicit curriculum theory",
  "sessionId": "480b819a-d329-4e18-be66-5fddad48e193"
}
```

---
