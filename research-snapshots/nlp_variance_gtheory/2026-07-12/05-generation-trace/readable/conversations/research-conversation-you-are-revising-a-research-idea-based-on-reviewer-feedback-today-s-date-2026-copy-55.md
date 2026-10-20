# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/3a999b40-0a1d-4b1d-a15f-656fc61cd73d.jsonl`
- **Structured JSON:** [`eb742414d25fb9693d6a.json`](../../sessions/eb/eb742414d25fb9693d6a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T03:37:23.899Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:37:23.899Z",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\",\n  \"core_problem\": \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the 'sparse policy selection' view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes 'capability boundary collapse' where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Recent bandit-based curriculum approaches address adaptive selection during RL: SEC (arXiv 2505.14970) formulates curriculum as a MAB over problem categories, achieving 17.5% AIME 2024 on Qwen2.5-7B (+27% relative); Actor-Curator (arXiv 2602.20532) extends this with a neural curator achieving 30.0% AIME 2024 on Qwen2.5-3B (+28.6% relative over uniform) with regret guarantees. However, both select from fixed problem pools (12K MATH problems) without synthesis—they optimize WHICH existing problems to train on, but cannot create new problems when the pool lacks adequate coverage for the policy's current frontier. As the policy improves toward competition level, the fraction of useful problems in a fixed pool shrinks, hitting a pool-exhaustion ceiling. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution—but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps, achieving 13.3% AIME 2024—matching the Qwen-2.5-7B base model—and actually degrading AMC 2023 from 57.5% to 52.5%. The fundamental open question is: can we build a system that combines the adaptive selection intelligence of bandit-based methods with persistent coverage-maintaining archives and targeted synthesis for identified gaps at competition level?\",\n  \"opportunity\": \"Five converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic—and multiple empirical findings support diversity's importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) Bandit-based curriculum methods demonstrate the value of adaptive selection but reveal the ceiling of fixed-pool approaches: SEC achieves 17.5% AIME 2024 (Qwen2.5-7B) via MAB over categories; Actor-Curator achieves 30.0% AIME 2024 (Qwen2.5-3B) via neural bandit with regret guarantees—but both select from fixed 12K pools without synthesis or multi-dimensional coverage tracking. The approaches are potentially COMPLEMENTARY: principled bandit selection FROM a coverage-maintaining, synthesis-augmented archive. (5) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K→80K); per-niche survival varies by topic (geometry autoformalization is ~3.7× harder than non-geometry per IndiMathBench, though this reflects formalization-specific difficulty that may not fully transfer to synthesis). VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification with targeted synthesis (vs. reactive instance-level targeting or selection-only bandits), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria.\",\n  \"landscape\": \"**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\\n\\n**Bandit-based adaptive curriculum (critical comparators).** SEC (arXiv 2505.14970) formulates online curriculum selection as a non-stationary MAB where each problem category (difficulty level or problem type) is an arm. Uses TD(0) updates on Q-values derived from absolute advantages, with Boltzmann sampling: p(c) ∝ exp(Q(c)/τ). Selects from fixed training pools (10K problems per domain). Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random 13.8%), 76.1% MATH-500, 51.1% AMC22-23. Categories are 1D (difficulty OR type per domain). SEC-2D variant combines 3 reasoning domains into 9 arms for multi-task learning. Actor-Curator (arXiv 2602.20532) extends beyond SEC's category-level bandits to per-problem utility estimation via a neural curator (Qwen3-0.6B) trained with online stochastic mirror descent (OSMD). Establishes regret bound O(T^{2/3}·V_T^{1/3}) under non-stationary utilities. Selects from fixed pools (12K MATH problems). Qwen2.5-3B: 30.0% AIME 2024, 81.0% MATH-500 (+28.6% relative over uniform 23.3%; beats SEC at 20.0% in matched 3B comparison). ~9% overhead. Key insight: Actor-Curator's per-problem utility estimation is more expressive than SEC's category-level Q-values, yielding consistent gains. Critical differentiation from SACE-RLVR on four dimensions: (a) SELECTION vs. SYNTHESIS—both SEC and Actor-Curator select from fixed pools of existing problems; they cannot synthesize new problems targeting identified gaps. As the policy improves toward competition level, the fraction of useful problems in a fixed 12K pool shrinks (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED optimization—Actor-Curator optimizes aggregate per-problem utility without explicit multi-dimensional coverage constraints, risking concentration on high-utility niches without ensuring breadth (analogous to SAGE's demonstrated over-specialization); (c) STATELESS vs. PERSISTENT—neither maintains a persistent multi-dimensional archive with cross-step coverage tracking; (d) COMPLEMENTARITY—crucially, these approaches compete at different levels: Actor-Curator's bandit selection could serve as the within-archive sampling strategy, combining principled selection WITH coverage-maintaining synthesis. We test this complementarity explicitly.\\n\\n**Balanced difficulty filtering theory.** Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) proves that expected policy improvement is lower-bounded by the variance of task-level success probabilities p(x)(1-p(x)), maximized at p(x)=0.5. Balanced filtering (0.3&lt;p(x)<0.7) achieves +12% on AMC and +10% on AIME with Qwen2.5 models in less than half the training steps of standard GRPO. This theoretical result directly supports our difficulty-aware design: our Bayesian learnability criterion tracks p(1-p) per problem via Beta posteriors, and our archive's ZPD-weighted sampling preferentially selects problems near the difficulty frontier.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\\n\\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\\n\\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold α=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively). On AIME 2024, SAGE achieves 13.3%—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%. This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents. Training dynamics confirm this: over-specialization emerges after ~120 steps (peak 69.5% declining to 61.6% by step 240). Question pool grows 18× (1,136→20,532) as flat filtered dataset without structured organization.\\n\\n**Implicit curriculum theory.** 'The Implicit Curriculum' (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation—not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: 'behavioral diversity is the binding constraint for RL.' RL-PLUS (arXiv 2508.00222) demonstrates 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\\n\\n**Policy-level diversity maintenance (concurrent).** UCPO (arXiv 2605.00365) addresses pass@k diversity collapse at the optimization level rather than the data level, adding a conditional uniformity penalty that redistributes gradient signal toward underrepresented correct solutions. Achieves +10% absolute Pass@64 on AIME 2024 (DeepSeek-7B: 70.0%→80.0%) and +45% equation-level diversity while maintaining competitive Pass@1. Importantly, UCPO modifies the loss function, not the training distribution—making it orthogonal to and potentially complementary with archive-based diversity maintenance. UCPO ensures diversity within the correct solution set for a given problem; SACE-RLVR ensures diversity across the problem distribution.\\n\\n**Lightweight co-evolutionary diversity (concurrent).** Vocabulary Dropout (arXiv 2604.03472) prevents proposer diversity collapse in co-evolutionary frameworks by applying random hard logit masks during problem generation, achieving +4.4 average points on Qwen3-8B (+10.9 AMC, +3.4 AIME 2024, +7.8 AIME 2025) within R-Zero. Demonstrates that diversity collapse is a real bottleneck in co-evolutionary RLVR. Differentiation: VD maintains proposer diversity via stochastic masking; SACE-RLVR provides structured coverage guarantees and interpretable gap identification.\\n\\n**Meta-RL curriculum generation (concurrent).** SOAR (arXiv 2601.18778) uses bi-level meta-RL where a teacher generates stepping-stone problems rewarded by measured student improvement on hard problems. Achieves +9.3% pass@32 on MATH fail@128 tasks (Llama-3.2-3B), recovering 75% of oracle gains from training on the full MATH dataset. Key insight: structural quality of generated problems matters more than solution correctness. Conceptually parallel to our proactive gap identification but uses meta-RL reward signal (measured student improvement) vs. our archive-structure-based gap detection. SOAR operates at the edge of learnability for currently-unsolvable problems; SACE-RLVR maintains coverage across the full difficulty spectrum.\\n\\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\\n\\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%→16.4%; Qwen3-8B AIME24: 16.7→26.0. Proves diversity collapse is real (TTRL pass@16: 32.4→16.7).\\n\\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\\n\\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\\n\\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR—related to our approach but operates at policy gradient level vs. our archive-replacement level.\\n\\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K→80K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry autoformalization has ~3.7× lower success rate than non-geometry (IndiMathBench arXiv 2512.00997: 12.2% vs 44.9% BEq across top models); the paper attributes this partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty. These grounding data inform our per-niche survival estimates.\\n\\n**Verification.** VHG (arXiv 2605.06660): validity gating.\\n\\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\\n\\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\\n\\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\\n\\n**The precise gap.** DéjàQ: 1D, GSM-only. SEC: MAB over categories, 1D, fixed pool. Actor-Curator: per-problem bandit, fixed pool, no coverage tracking. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization, zero AIME improvement over base model. Online Difficulty Filtering: theoretical support for balanced filtering, no archive structure. UCPO: policy-level diversity, no data-level coverage. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification with synthesis, structured coverage tracking, and Bayesian learnability replacement. Moreover, no existing work tests whether bandit-based selection and archive-based synthesis are complementary.\",\n  \"inspired_by\": \"DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + SEC_insight['MAB over problem categories during RL; 17.5% AIME24'] + Actor_Curator_insight['neural bandit with regret guarantees; 30.0% AIME24; ~9% overhead; pool-selection ceiling motivates synthesis'] + Online_Difficulty_Filtering['p(1-p) lower bound on policy improvement; balanced filtering; EACL 2026'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools → over-specialization ~120 steps; 13.3% AIME = base model; AMC degrades'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + UCPO_concurrent['policy-level diversity; +10% Pass@64 AIME; complementary to data-level'] + VocabDropout_concurrent['+4.4 avg; diversity collapse prevention'] + SOAR_concurrent['meta-RL teacher; 75% oracle recovery'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry ~3.7× lower autoformalization success; formalization-specific'] + EVOL_RL_warning['diversity collapse']\",\n  \"approach\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics. We organize the system around **three core innovations** plus **four extensions** tested in ablations. This follows the structure of successful prior systems: DéjàQ claims ~2 core contributions atop ~11 mechanisms; CLPO claims 3 named contributions atop ~7 design choices.\\n\\n**Design Motivation: Why Coverage Matters (Two Independent Arguments).**\\n\\n*Argument 1: Relay-regime-inspired smooth difficulty coverage.* The implicit curriculum theory (arXiv 2602.14872, ICML 2026) demonstrates on synthetic tasks that smooth difficulty spectra ('relay regime') yield faster convergence than gapped spectra ('grokking regime'). While this theory assumes idealized conditions (uniform distributions, geometric difficulty structure, single attention layer) that differ from real RLVR, it provides a principled design heuristic: smoother difficulty coverage should improve convergence. Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) provides additional theoretical support: policy improvement is lower-bounded by p(1-p) variance, maximized at balanced difficulty, achieving +12% AMC and +10% AIME in half the training steps. Our 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) are motivated by these insights. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n*Argument 2: Broad coverage prevents capability boundary collapse.* Even under the 'sparse policy selection' view where RL modifies only 1-3% of tokens (arXiv 2605.06241), comprehensive coverage is essential. Three empirical findings converge: (a) Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), each un-sharpened primitive type creates an exponential bottleneck; (b) Tailor (arXiv 2511.12429) directly demonstrates that behavioral diversity, not correctness, is the binding constraint for RL outcomes (25 vs. 4 primitives → substantial gains); (c) RL-PLUS (arXiv 2508.00222) shows narrow RLVR causes 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse distributions as the antidote (+69.2% relative improvement). Thus, comprehensive difficulty×topic coverage benefits under both views: relay-like curriculum dynamics AND broader capability activation.\\n\\n*Why archives with synthesis vs. bandit selection from fixed pools.* SEC and Actor-Curator demonstrate the clear value of adaptive problem selection during RL training. We argue that persistent archives with targeted synthesis provide three capabilities that fixed-pool bandit selection cannot: (i) COVERAGE GUARANTEES—bandits optimize aggregate utility and may concentrate on high-utility niches without ensuring breadth across the difficulty×topic space, analogous to SAGE's demonstrated over-specialization (13.3% AIME = base model, AMC degradation); structured archives explicitly enforce minimum coverage per niche. (ii) SYNTHESIS FOR GAPS—as the policy improves, the useful difficulty frontier advances, and a fixed pool (e.g., MATH's 12K problems) becomes increasingly sparse at the frontier; targeted synthesis creates fresh problems where the policy needs them most. (iii) PERSISTENT TRACKING—archives maintain cross-step memory of which niches are well-covered and which are stale, enabling proactive rather than reactive curriculum adaptation. However, these approaches are potentially COMPLEMENTARY: Actor-Curator's principled per-problem utility estimation can serve as the within-archive sampling strategy, and we test this explicitly (see E4 and baseline #5).\\n\\n---\\n\\n**CORE INNOVATION 1: 2D Learnability Archive (50 cells).**\\n10 difficulty bins (width 0.1, empirical solve-rate) × 5 topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells, M=10 problems per cell. Topic classification via GPT-4o-mini (84-92% accuracy per arXiv 2411.00042). Difficulty measured via G=16 rollouts reused from training.\\n\\nThe 2D structure enables qualitatively new capabilities vs. prior work: (a) difficulty-aware coverage tracking—locate under-populated difficulty×topic niches BEFORE policy failures (vs. Socratic-Zero's reactive approach, SAGE's flat pool that over-specializes by step ~120, SEC/Actor-Curator's fixed-pool selection without coverage constraints); (b) persistent cross-step memory—problems track with the evolving policy, revealing emergent curriculum (vs. CLPO's stateless per-batch assessment, SEC's myopic TD updates); (c) interpretable post-hoc analysis—which niches drive benchmark performance.\\n\\nReplacement criterion: candidate problem enters a cell if its Bayesian learnability credible interval (see Core 3) exceeds the current worst occupant's upper bound. More principled than DéjàQ's point estimate comparison f(x')>f(y).\\n\\n**CORE INNOVATION 2: Proactive Gap-Targeted Synthesis with Verification.**\\nExisting targeting is either reactive (Socratic-Zero examines specific failed solutions; SwS identifies aggregate weaknesses offline) or selection-only (SEC/Actor-Curator adaptively choose from fixed pools). SAGE's Challenger generates harder problems without coverage awareness, leading to over-specialization. The 2D archive enables proactive niche-level gap identification:\\n\\n(a) Identify under-performing cells: <3 problems or stale (not refreshed for >100 training steps).\\n(b) Generate-then-classify synthesis: generate for target TOPIC without difficulty constraints, verify, then empirically measure difficulty via G=16 rollouts and assign to the appropriate cell. This avoids the 'double filter' problem (constraining both topic AND difficulty yields 4-17% per SPARQ/MathSmith evidence; topic-only yields higher survival).\\n(c) 3-stage VHG-inspired verification: (i) format/solvability check (filters ~25-30%, consistent with FLAMES ~30% removal), (ii) cross-verification via majority vote across 2-3 strong models (filters ~15-20%), (iii) difficulty calibration via G=16 rollouts.\\n\\n**Concrete per-niche survival estimates (literature-grounded):**\\nEstimates sourced from SPARQ (~25% QD survival), DART-Math (51.1% Level 5 dropout), FLAMES (50% removal at Level 5), and IndiMathBench (~3.7× lower geometry autoformalization success rate, 12.2% vs 44.9% BEq; noting this reflects formalization-specific difficulty in Lean 4 that may not fully transfer to problem synthesis—we conservatively estimate geometry synthesis is ~2-3× harder than algebra).\\n\\n- Easy-medium cells (solve-rate 0.3-0.8), common topics (Algebra, NT): ~30 cells, ~30-50% survival.\\n  Need ~20-35 candidates/cell → ~600-1,050 total.\\n- Medium-hard cells (solve-rate 0.1-0.3), common topics: ~10 cells, ~15-25% survival.\\n  Need ~40-65 candidates/cell → ~400-650 total.\\n- Geometry cells (all difficulties): ~10 cells, ~10-20% survival (geometry synthesis is harder than algebra due to constraint consistency requirements; conservatively ~2-3× harder based on adjusted IndiMathBench ratio with formalization-specific caveats).\\n  Need ~50-100 candidates/cell → ~500-1,000 total.\\n- Extreme cells (solve-rate <0.1 or >0.9, all topics): ~10 cells, ~3-8% survival (DART-Math: Level 5 loses 51% coverage; FLAMES: 50% removal at Level 5).\\n  Need ~125-330 candidates/cell → ~1,250-3,300 total.\\n- **Graceful degradation:** cells that cannot reach M=10 accept minimum 3 (sufficient for meaningful Beta posterior updates). Archive reports actual occupancy; analysis accounts for sparse cells.\\n- **Total per refresh cycle:** ~2,750-6,000 candidates (median ~4,000). Generation cost using open-source 70B teacher: ~130 GPU-hours. Verification (G=16 rollouts per candidate on 7B): ~12 GPU-hours. Per-refresh total: ~142 GPU-hours. Over ~10 refreshes: ~1,420 GPU-hours. Alternative: API-based generation at ~$0.30/problem ≈ $1,200/refresh, $12,000 total.\\n- Per-niche survival rates and generation statistics reported as community contribution.\\n\\n**CORE INNOVATION 3: Zero-Cost Bayesian Learnability Estimation.**\\nDéjàQ estimates learnability via K=100 dedicated completions per problem—computationally expensive and separate from training. We reuse G=16 rollouts already generated for GRPO training—zero additional inference cost. G=16 is well-justified: DAPO (arXiv 2503.14476) standardizes G=16; MC-GRPO (arXiv 2601.22582) shows clear degradation at small G (G=2: 78.92%, G=4: 81.34%, G=8: 84.53%); the Gradient Starvation analysis (arXiv 2605.07689) explains the mechanism—for binary rewards, degenerate group probability is p^G+(1-p)^G, yielding 69.25% degenerate groups at G=4 vs. <1% at G=8.\\n\\nBayesian temporal smoothing: Beta-Bernoulli running posterior per problem (Beta(1,1) prior, updated each appearance). After 3 appearances (48 cumulative rollouts), posterior variance drops ~3×. Replacement uses conservative credible interval: candidate must exceed occupant's upper bound, preventing noisy replacements. The p(1-p) learnability signal is theoretically supported by Online Difficulty Filtering's result (arXiv 2504.03380) that policy improvement is lower-bounded by this exact quantity.\\n\\nRelated but distinct from the Discounted Beta-Bernoulli (DBB) estimator (arXiv 2603.18444), which applies Bayesian estimation at the policy gradient level. Our Beta posterior operates at the archive-replacement level for per-problem learnability tracking—a different application of the same statistical principle. VCRL's insight (arXiv 2509.19803) that reward variance reflects difficulty is extended from curriculum signal to Bayesian replacement criterion.\\n\\n---\\n\\n**EXTENSIONS (each tested in one ablation, not claimed as core contributions):**\\n\\nE1: Cross-niche SvS seeding. SvS-style answer-preserving mutation (ICLR 2026) from adjacent cells to seed under-populated niches. Expected ~70-80% validity for within-topic mutations. Particularly valuable for geometry and extreme cells where de novo generation has lower survival. Tested in A5.\\n\\nE2: James-Stein shrinkage. Following arXiv 2511.03710 (which demonstrates shrinkage baselines reduce MSE in RLVR), we apply shrinkage to per-problem learnability estimates, regularizing toward batch average. Not claimed as novel—cite and use. Tested in A6.\\n\\nE3: DGPO policy updates. MAD normalization + DQW weighting adopted from MathForge (arXiv 2601.20614, ICLR 2026). Addresses difficulty-dependent advantage scale. Tested in A7.\\n\\nE4: Archive sampling strategy. Compare (a) ZPD-weighted sampling with posterior variance weighting ([0.1, 0.9] solve-rate, high uncertainty → more sampling), (b) uniform sampling, and (c) Actor-Curator-style bandit sampling from the archive—directly testing whether principled per-problem utility estimation (à la Actor-Curator) further improves when operating within a coverage-maintaining archive. This tests the complementarity hypothesis: if (c) outperforms both Actor-Curator from a fixed pool and (a) from the archive, it validates that bandit selection and archive synthesis address orthogonal bottlenecks.\\n\\n---\\n\\n**Training Loop (VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary):**\\n(a) Sample from archive with selected strategy (E4). (b) G=16 rollouts, compute advantages. (c) Policy update (GRPO or DGPO). (d) Update Beta posteriors per problem. (e) Every 50 steps: refresh sampled cells, reassign problems that shifted difficulty, flag stale cells, synthesize for gaps. Overhead: ~20-25% vs. vanilla GRPO (dominated by synthesis cost).\\n\\n**AIME Contextualization.** Distillation-based: 70-90% AIME 2024. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm. Value: METHOD + ABLATION INSIGHTS. Framework applicable atop distilled bases.\\n\\n**Baselines (8):** (1) DéjàQ-comp [PRIMARY: 2D+targeting value over 1D archive]. (2) CLPO [PRIMARY: persistent archive value over stateless curriculum]. (3) Socratic-Zero [PRIMARY: structured proactive vs. reactive instance-level targeting]. (4) SAGE [structured archive vs. flat pool; evidence: SAGE's AIME = base model + AMC degradation]. (5) Actor-Curator [PRIMARY: archive synthesis vs. bandit selection from fixed pool; complementarity test via E4]. (6) EVOL-RL [stateless novelty-aware diversity]. (7) MathForge [DGPO source; difficulty-aware optimization]. (8) Vanilla GRPO [minimal baseline].\\n\\n**Ablations (7):**\\nA1: 1D archive only (tests Core 1 dimensionality).\\nA2: Random synthesis vs. gap-targeted (tests Core 2 proactive targeting).\\nA3: 3 bins vs. 10 bins [relay-regime-inspired test: first empirical comparison of coarse vs. fine difficulty granularity in real RLVR].\\nA4: Point estimation vs. Beta posterior (tests Core 3 vs. DéjàQ-style p(1-p)).\\nA5: Without cross-niche SvS seeding (tests E1 value, especially for sparse cells).\\nA6: Without James-Stein shrinkage (tests E2).\\nA7: GRPO vs. DGPO (tests E3).\\n\\n**Evaluation:** AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. pass@1 AND pass@k (pass@k especially important per RL-PLUS's capability boundary collapse finding and UCPO's concurrent work on policy-level diversity—we test whether archive-based data diversity and policy-level diversity address complementary aspects of the collapse). DAPO-Math-17k seeds.\\n\\n**Key Analyses:** (1) Coverage heatmaps showing cell occupancy evolution. (2) Per-cell benchmark contribution: which niches drive gains? (3) Emergent curriculum: bin-transition frequencies as policy improves. (4) Synthesis efficiency: per-topic survival rates vs. literature benchmarks (SPARQ, DART-Math, FLAMES), reported as community contribution. (5) Convergence speed: 10 vs. 3 bins. (6) Capability boundary: pass@1 vs. pass@k trajectories—does archive diversity prevent RL-PLUS-style collapse? How does data-level diversity (SACE-RLVR) compare to policy-level diversity (UCPO)? (7) Structured vs. flat: archive coverage diversity over training vs. SAGE-style accumulation. (8) Selection vs. synthesis: Actor-Curator from fixed pool vs. Actor-Curator-style sampling from SACE-RLVR archive—quantifying the value of synthesis and coverage maintenance.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"7,200 H100-hours (baselines: 8×250h=2,000h; SACE-RLVR 7B 800h; SACE-RLVR 8B 800h; ablations 7×200h=1,400h; synthesis/verification 1,420h; archive overhead 330h; E4 bandit variant 450h)\",\n      \"timeline\": \"14-18 weeks\",\n      \"estimated_gpu_cost\": \"$18,000 (at ~$2.50/H100-hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"5,600 H100-hours (reuse released code; shared verification; API-based generation saves ~1,100 GPU-hrs but adds ~$12,000 API cost)\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$400-800 (code assistance)\",\n      \"synthesis_api_cost\": \"$7,000-12,000 (problem generation via API, optional vs. GPU)\",\n      \"estimated_gpu_cost\": \"$14,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"8,800 H100-hours (exploratory sweeps over archive dimensions, bin count, refresh frequency, replacement criteria, synthesis strategies, bandit-archive complementarity)\",\n      \"timeline\": \"10-13 weeks\",\n      \"claude_api_cost\": \"$1,000-2,000\",\n      \"estimated_gpu_cost\": \"$22,000\",\n      \"speed_bottleneck\": \"GPU queue; each GRPO run 24-72h on 8×H100s. Synthesis for extreme cells dominates generation cost.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (Sep 19-24, 2026) — stretch if pilot results by August\",\n    \"ICML 2027 (~Jan 2027) — primary target, strong fit for RL + QD + coverage\",\n    \"NeurIPS 2027 (~May 2027) — fallback with full evaluation\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"DéjàQ (arXiv 2601.01931) — PRIMARY PREDECESSOR, online MAP-Elites for RLVR at GSM level\",\n    \"SEC (arXiv 2505.14970) — CRITICAL COMPARATOR, MAB over problem categories; 17.5% AIME24 on Qwen2.5-7B; TD(0) updates\",\n    \"Actor-Curator (arXiv 2602.20532) — PRIMARY BASELINE, neural bandit selection from fixed pool; 30.0% AIME24 on Qwen2.5-3B; regret O(T^{2/3}·V_T^{1/3}); ~9% overhead\",\n    \"Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) — THEORETICAL SUPPORT, p(1-p) lower bound on policy improvement; +12% AMC in half steps\",\n    \"CLPO (arXiv 2509.25004) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024\",\n    \"Socratic-Zero (arXiv 2509.24726) — PRIMARY BASELINE, three-agent co-evolution; 56.1% avg\",\n    \"SAGE (arXiv 2603.15255) — BASELINE, 4-agent self-evolution; 13.3% AIME = base model; AMC degrades 57.5%→52.5%\",\n    \"UCPO (arXiv 2605.00365) — CONCURRENT, policy-level diversity via conditional uniformity; +10% Pass@64 AIME24; complementary to data-level\",\n    \"Vocabulary Dropout (arXiv 2604.03472) — CONCURRENT, lightweight diversity via logit masking; +4.4 avg on 8B\",\n    \"SOAR (arXiv 2601.18778) — CONCURRENT, meta-RL teacher for edge-of-learnability synthesis; 75% oracle recovery\",\n    \"The Implicit Curriculum (arXiv 2602.14872, ICML 2026) — DESIGN MOTIVATION, relay vs. grokking (synthetic tasks)\",\n    \"Sparse Policy Selection (arXiv 2605.06241) — RL modifies 1-3% of tokens; motivates broad coverage\",\n    \"Sharper Primitives (arXiv 2602.08281) — RLVR polarizes; multiplicative compounding; diverse training activates broader primitives\",\n    \"Tailor (arXiv 2511.12429) — behavioral diversity is binding constraint for RL; 25 vs 4 primitives\",\n    \"RL-PLUS (arXiv 2508.00222) — capability boundary collapse from narrow RLVR; +69.2% with diversity\",\n    \"ProRL (arXiv 2505.24864) — diverse prolonged training accesses beyond base model ceiling\",\n    \"Bidirectional Curriculum Generation (arXiv 2603.05120) — 4-agent bidirectional; 60.03 avg\",\n    \"EVOL-RL (arXiv 2509.15194) — stateless novelty-aware diversity; AIME25 16.4%\",\n    \"MathForge/DGPO (arXiv 2601.20614, ICLR 2026) — MAD normalization; adopted as extension\",\n    \"VCRL (arXiv 2509.19803) — reward variance as difficulty proxy; G=16; 57.76 avg Qwen3-8B\",\n    \"MC-GRPO (arXiv 2601.22582) — rollout count ablation: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%\",\n    \"Gradient Starvation (arXiv 2605.07689) — 69% degenerate groups at G=4; explains G effect mechanistically\",\n    \"DAPO (arXiv 2503.14476) — standardizes G=16\",\n    \"Discounted Beta-Bernoulli (arXiv 2603.18444) — Bayesian estimation for RLVR; validates Beta approach\",\n    \"SwS (NeurIPS 2025, arXiv 2506.08989) — offline weakness targeting; +10%\",\n    \"SvS (ICLR 2026) — answer-preserving synthesis; used for cross-niche seeding\",\n    \"SAND-Math (arXiv 2507.20527) — ~38% end-to-end competition synthesis survival\",\n    \"SPARQ (arXiv 2506.06499) — ~25% QD survival (320K→80K); per-niche evidence\",\n    \"DART-Math (arXiv 2407.13690, NeurIPS 2024) — Level 5: 51.1% query dropout; difficulty survival data\",\n    \"FLAMES (arXiv 2508.16514) — ~30% strict survival; Level 5: 50% removal\",\n    \"IndiMathBench (arXiv 2512.00997) — geometry ~3.7× lower autoformalization success; formalization-specific context\",\n    \"VHG (arXiv 2605.06660) — validity gating; inspires verification\",\n    \"Shrinking the Variance (arXiv 2511.03710) — James-Stein shrinkage for RLVR\",\n    \"EBPO (arXiv 2602.05165) — empirical Bayes for GRPO\",\n    \"R-Zero (ICLR 2026) — self-evolving; collapses iter 3\",\n    \"Klear-Reasoner-8B (arXiv 2508.07629) — 90.5% AIME 2024; distillation context\",\n    \"Prism (arXiv 2603.13309) — 128-cluster diversity with ZPD gate\",\n    \"R-Diverse (arXiv 2602.13103) — SAM skill diversity + MAP memory\",\n    \"STAT (arXiv 2510.10023) — Missing-Skill-Profile\",\n    \"Problem Categorization (arXiv 2411.00042) — topic classification\",\n    \"Two-Stage Dynamic View (arXiv 2510.04028) — capability shrinkage then expansion\",\n    \"Does RL Incentivize Reasoning? (NeurIPS 2025, arXiv 2504.13837) — coverage framing\"\n  ],\n  \"description\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), scaling online MAP-Elites from GSM-level (DéjàQ) to competition-level math through three core innovations plus four extensions. Two independent motivations for comprehensive coverage: (1) relay-regime theory (arXiv 2602.14872) and balanced difficulty filtering theory (arXiv 2504.03380, EACL 2026: p(1-p) lower bound on policy improvement) suggest smooth difficulty spectra yield faster convergence—adopted as design heuristic, not guarantee, with A3 testing empirically; (2) even under 'sparse policy selection' (1-3% tokens modified), broad coverage prevents 'capability boundary collapse' (RL-PLUS: pass@1↑ pass@128↓; +69.2% with diversity), ensures multiplicative primitive sharpening across domains (Sharper Primitives), and provides the behavioral diversity that is the binding constraint for RL (Tailor: 25 vs 4 primitives). Core 1: 2D archive (10 bins × 5 topics = 50 cells) with proactive gap identification and Bayesian replacement—addresses SAGE's over-specialization at step ~120 (AIME 13.3% = base model, AMC degradation 57.5%→52.5%). Core 2: generate-then-classify synthesis with per-niche survival estimates (central: 30-50%, geometry: 10-20% accounting for ~3.7× autoformalization difficulty ratio from IndiMathBench with formalization-specific caveats, extreme: 3-8%; graceful degradation to min 3/cell; ~142 GPU-hrs/refresh). Core 3: zero-cost Bayesian estimation via G=16 rollout reuse (vs DéjàQ K=100), Beta posterior + credible intervals; G=16 justified by MC-GRPO ablation + gradient starvation analysis (69% degenerate groups at G=4). Key positioning vs. bandit-based curriculum: SEC (17.5% AIME24, Qwen2.5-7B) and Actor-Curator (30.0% AIME24, Qwen2.5-3B, ~9% overhead) demonstrate adaptive selection value but are limited by fixed pool exhaustion, lack of synthesis, and absence of coverage tracking. SACE-RLVR provides what bandits cannot: synthesis for identified gaps, structured coverage guarantees, and persistent cross-step memory. The approaches are potentially complementary—Actor-Curator's bandit sampling from SACE-RLVR's archive tested in E4 and Analysis #8. Extensions: SvS seeding, shrinkage, DGPO, archive sampling strategy (including Actor-Curator-style variant)—each ablated. Eight baselines (DéjàQ-comp, CLPO, Socratic-Zero, SAGE, Actor-Curator, EVOL-RL, MathForge, GRPO), seven ablations including pass@k capability boundary analysis and selection-vs-synthesis analysis. Concurrent work positioned: UCPO (policy-level diversity, complementary), Vocabulary Dropout (lightweight alternative), SOAR (meta-RL curriculum). Qwen2.5-Math-7B/Qwen3-8B, AIME 2024/2025, MATH-500, AMC, Minerva, OlympiadBench.\",\n  \"project_name\": \"sace_rlvr\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"revision_overview\": \"MAJOR REVISION addressing the single blocking issue (SEC/Actor-Curator, unaddressed for 7 rounds) through substantive integration, not surface patching. Six structural changes: (1) SEC and Actor-Curator added as major landscape section with detailed four-dimensional differentiation (selection vs. synthesis, aggregate vs. structured, stateless vs. persistent, complementarity), (2) Actor-Curator added as 8th baseline with explicit complementarity test, (3) IndiMathBench geometry ratio corrected to ~3.7× with formalization-specific context, (4) SAGE AIME presentation corrected to show base-model matching and AMC degradation, (5) Online Difficulty Filtering cited as theoretical support for p(1-p) learnability criterion, (6) UCPO, Vocabulary Dropout, and SOAR added as concurrent work. Extension E4 reframed to explicitly test bandit-archive complementarity hypothesis.\",\n    \"issue_1_sec_actor_curator_blocking\": \"ADDRESSED SUBSTANTIVELY after 7 rounds. Added as major landscape section ('Bandit-based adaptive curriculum') with full technical details: SEC's MAB formulation (TD(0) on Q-values, Boltzmann sampling, 1D categories, 17.5% AIME24 on Qwen2.5-7B, 76.1% MATH-500, 51.1% AMC22-23), Actor-Curator's neural bandit (OSMD, per-problem utility via Qwen3-0.6B curator, regret O(T^{2/3}·V_T^{1/3}), 30.0% AIME24 on Qwen2.5-3B, 81.0% MATH-500, ~9% overhead). Four-dimensional differentiation: (a) SELECTION vs. SYNTHESIS—bandits select from fixed 12K pools and cannot create problems targeting identified gaps; pool-exhaustion problem as policy improves; (b) AGGREGATE vs. STRUCTURED—Actor-Curator optimizes aggregate per-problem utility without multi-dimensional coverage constraints, risking niche concentration (analogous to SAGE's over-specialization); (c) STATELESS vs. PERSISTENT—no cross-step coverage tracking or emergent curriculum visualization; (d) COMPLEMENTARITY—Actor-Curator's bandit can serve as within-archive sampling strategy. Actor-Curator added as baseline #5. Extension E4 reframed to compare ZPD, uniform, and Actor-Curator-style bandit sampling FROM the archive. New analysis #8 directly quantifies selection-vs-synthesis value: Actor-Curator from fixed pool vs. Actor-Curator-style from SACE-RLVR archive. Added 'Why archives with synthesis vs. bandit selection' subsection in approach with three-capability argument (coverage guarantees, synthesis for gaps, persistent tracking). Core problem and opportunity sections updated to integrate bandit-based approaches as part of the research landscape.\",\n    \"issue_2_online_difficulty_filtering\": \"ADDED. Cited in landscape as 'Balanced difficulty filtering theory' (arXiv 2504.03380, EACL 2026). Key result: expected policy improvement lower-bounded by p(x)(1-p(x)), maximized at p(x)=0.5. Achieves +12% AMC and +10% AIME in half training steps with Qwen2.5 models. Integrated into three locations: (1) Argument 1 in approach as additional theoretical support alongside implicit curriculum theory; (2) Core 3 discussion noting our Beta posterior tracks exactly the p(1-p) quantity this theory shows lower-bounds policy improvement; (3) dedicated landscape entry connecting to our archive's ZPD-weighted sampling.\",\n    \"issue_3_indimathbench_corrected\": \"FIXED throughout all occurrences. Changed '6-7× harder' to '~3.7× lower autoformalization success rate (12.2% vs 44.9% BEq across top models)' with explicit caveat: 'IndiMathBench attributes geometry difficulty partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty.' Geometry synthesis difficulty conservatively re-estimated as ~2-3× harder than algebra. Survival estimates adjusted: geometry cells 10-20% (was 5-15%), need 50-100 candidates/cell (was 65-200). Per-refresh total revised to ~2,750-6,000 candidates (was 2,900-7,000), ~142 GPU-hrs (was 162). Total synthesis cost over 10 refreshes: ~1,420 GPU-hrs (was 1,620).\",\n    \"issue_4_sage_aime_corrected\": \"FIXED. Now explicitly states: 'On AIME 2024, SAGE achieves 13.3%—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%.' Interpretation strengthened: 'This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents.' This corrected framing is STRONGER evidence for our approach than the original presentation.\",\n    \"issue_5_ucpo_concurrent\": \"ADDED. Full landscape entry: UCPO (arXiv 2605.00365) adds conditional uniformity penalty redistributing gradient toward underrepresented correct solutions. DeepSeek-7B AIME24: Pass@1 27.71%→30.16%, Pass@64 70.0%→80.0% (+10% absolute). +45% equation-level diversity. Qwen2.5-7B AIME24: Pass@64 43.33%→56.67%. Key differentiation: UCPO modifies loss function (policy-level), SACE-RLVR modifies training distribution (data-level)—orthogonal and potentially complementary. Analysis #6 updated to compare data-level vs. policy-level diversity approaches.\",\n    \"issue_6_vocab_dropout_soar\": \"ADDED. Vocabulary Dropout (arXiv 2604.03472): hard logit masking on proposer in R-Zero, +4.4 avg on Qwen3-8B (+10.9 AMC, +3.4 AIME24, +7.8 AIME25). Demonstrates diversity collapse is real bottleneck. Differentiation: stochastic masking vs. structured coverage. SOAR (arXiv 2601.18778): bi-level meta-RL teacher/student on Llama-3.2-3B, +9.3% pass@32 on MATH fail@128, recovers 75% oracle gains. Key insight: structural quality > solution correctness. Differentiation: meta-RL reward signal vs. archive-structure gap detection; SOAR targets edge of learnability, SACE-RLVR maintains full-spectrum coverage.\",\n    \"score_trajectory_note\": \"This revision addresses the #1 blocking issue (SEC/Actor-Curator, 7 rounds persistent) through substantive integration, not surface citation. The four-dimensional differentiation (selection/synthesis, aggregate/structured, stateless/persistent, complementarity) provides a rigorous argument for why archives with synthesis offer capabilities that bandit selection cannot. The complementarity test (E4 and Analysis #8) turns a potential weakness into a strength: rather than competing with bandits, SACE-RLVR subsumes them. The corrected SAGE presentation (AIME = base, AMC degradation) actually strengthens the case for structured archives. Online Difficulty Filtering's p(1-p) result independently validates our Bayesian learnability criterion. All six recommended concurrent works now integrated.\"\n  }\n}\n\n## Reviewer feedback (round 9)\nIssues: [\"MISSING WORK: CurES (arXiv 2510.01037, Mar 2026 revision) uses Beta(α,β) per-problem posteriors with Bayesian updates for RLVR curriculum selection, derives optimal sampling distribution based on p(1-p), achieves +4.82 over GRPO on 7B (24.58% AIME24). This directly overlaps with Core Innovation 3's 'Zero-Cost Bayesian Learnability Estimation' — CurES applies the SAME statistical framework (Beta posteriors + p(1-p) signal) for problem selection in RLVR. While CurES selects from fixed pools (vs SACE-RLVR's archive replacement), claiming Beta posteriors as a 'core innovation' without acknowledging CurES is a significant omission that weakens Core 3's novelty.\", \"MISSING WORK: InSight (arXiv 2603.01907, Mar 2026) models data outcomes using Bayesian latent success rates for RLVR data selection, with mutual information-based acquisition scores. Related to Core 3's Bayesian approach, achieving ~2.2× training acceleration.\", \"NOVELTY PRESSURE ON CORE 3: The proposal already cites DBB (arXiv 2603.18444) for Bayesian estimation at the policy gradient level. With CurES using Beta posteriors at the curriculum level and Online Difficulty Filtering providing the p(1-p) theory, Core 3's novelty reduces to: applying Beta posteriors specifically for ARCHIVE REPLACEMENT with credible interval comparison (vs point estimates). This is a valid but narrow contribution that may not warrant 'core innovation' status.\", \"INTERESTING CONTEXT: At the 3B scale, SEC (20.0%) actually UNDERPERFORMS uniform sampling (23.33%) on AIME24, while Actor-Curator (30.0%) beats both. This suggests category-level bandits can fail without coverage guarantees — the proposal could use this data point to strengthen the archives-over-bandits argument.\", \"VENUE TIMELINE: ICLR 2027 deadline ~Sep 24, 2026. With 14-18 week timeline starting late May 2026, earliest completion is mid-September — making ICLR 2027 nearly impossible, not merely a 'stretch.' The proposal honestly labels it 'stretch' but should consider removing it to avoid credibility concerns.\"]\nFeedback: **This is Round 9 of 10. Round 10 requires a final pass/fail decision. Current average: 3.875 < 4.0 threshold. Here is exactly what is needed:**\n\n**(1) Add CurES (arXiv 2510.01037) — CRITICAL for Round 10.** CurES uses the EXACT same statistical mechanism as Core 3: Beta(α,β) per problem, Bayesian posterior updates with new rollouts, p(1-p)-based sampling distribution. The proposal cites DBB (gradient level) and Online Difficulty Filtering (theory), but misses CurES (curriculum level) — the most directly comparable prior art for Core 3. Add CurES to the landscape section with differentiation: CurES uses Beta posteriors for SAMPLING from fixed pools (which problem to train on?); SACE-RLVR uses them for REPLACEMENT in evolving archives (should this new problem replace the worst occupant?). CurES uses point estimates for sampling probabilities; SACE-RLVR uses credible intervals for replacement decisions. The 'zero-cost' aspect (reusing G=16 training rollouts vs dedicated evaluation) remains valid regardless.\n\n**(2) Reframe Core 3's novelty claim.** Given CurES + DBB + Online Difficulty Filtering, 'Zero-Cost Bayesian Learnability Estimation' should not be positioned as though Beta posteriors in RLVR are novel. Reframe: 'We apply established Beta-Bernoulli estimation (cf. CurES, DBB) to a new decision problem — archive replacement via credible interval comparison — at zero additional inference cost by reusing training rollouts.' This is more honest and equally compelling.\n\n**(3) Optional but recommended:** Note that SEC underperforms uniform at 3B (20.0% vs 23.33%) — this strengthens your argument that category-level bandits without coverage guarantees can fail, providing concrete evidence for the archives-over-bandits thesis.\n\n**Round 10 outlook:** If CurES is addressed and Core 3 reframed, I would lean toward 'pass' — the proposal has exceptional clarity and thoroughness, the complementarity test is genuinely novel, and the remaining novelty (2D archive + gap-targeted synthesis + credible-interval replacement + bandit-archive complementarity) is sufficient for a well-executed integration paper at top venues. The novelty score is the bottleneck at 3.5; with honest reframing it could reach 3.75, and with the clarity bonus (4.5) the overall quality is competitive.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T03:37:23.902Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:37:23.902Z",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

## Round 1

67 recorded events

### User

_source line 3 · 2026-05-28T03:37:23.944Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
{
  "title": "Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis",
  "core_problem": "Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the 'sparse policy selection' view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes 'capability boundary collapse' where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Recent bandit-based curriculum approaches address adaptive selection during RL: SEC (arXiv 2505.14970) formulates curriculum as a MAB over problem categories, achieving 17.5% AIME 2024 on Qwen2.5-7B (+27% relative); Actor-Curator (arXiv 2602.20532) extends this with a neural curator achieving 30.0% AIME 2024 on Qwen2.5-3B (+28.6% relative over uniform) with regret guarantees. However, both select from fixed problem pools (12K MATH problems) without synthesis—they optimize WHICH existing problems to train on, but cannot create new problems when the pool lacks adequate coverage for the policy's current frontier. As the policy improves toward competition level, the fraction of useful problems in a fixed pool shrinks, hitting a pool-exhaustion ceiling. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution—but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps, achieving 13.3% AIME 2024—matching the Qwen-2.5-7B base model—and actually degrading AMC 2023 from 57.5% to 52.5%. The fundamental open question is: can we build a system that combines the adaptive selection intelligence of bandit-based methods with persistent coverage-maintaining archives and targeted synthesis for identified gaps at competition level?",
  "opportunity": "Five converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic—and multiple empirical findings support diversity's importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) Bandit-based curriculum methods demonstrate the value of adaptive selection but reveal the ceiling of fixed-pool approaches: SEC achieves 17.5% AIME 2024 (Qwen2.5-7B) via MAB over categories; Actor-Curator achieves 30.0% AIME 2024 (Qwen2.5-3B) via neural bandit with regret guarantees—but both select from fixed 12K pools without synthesis or multi-dimensional coverage tracking. The approaches are potentially COMPLEMENTARY: principled bandit selection FROM a coverage-maintaining, synthesis-augmented archive. (5) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K→80K); per-niche survival varies by topic (geometry autoformalization is ~3.7× harder than non-geometry per IndiMathBench, though this reflects formalization-specific difficulty that may not fully transfer to synthesis). VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification with targeted synthesis (vs. reactive instance-level targeting or selection-only bandits), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria.",
  "landscape": "**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\n\n**Bandit-based adaptive curriculum (critical comparators).** SEC (arXiv 2505.14970) formulates online curriculum selection as a non-stationary MAB where each problem category (difficulty level or problem type) is an arm. Uses TD(0) updates on Q-values derived from absolute advantages, with Boltzmann sampling: p(c) ∝ exp(Q(c)/τ). Selects from fixed training pools (10K problems per domain). Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random 13.8%), 76.1% MATH-500, 51.1% AMC22-23. Categories are 1D (difficulty OR type per domain). SEC-2D variant combines 3 reasoning domains into 9 arms for multi-task learning. Actor-Curator (arXiv 2602.20532) extends beyond SEC's category-level bandits to per-problem utility estimation via a neural curator (Qwen3-0.6B) trained with online stochastic mirror descent (OSMD). Establishes regret bound O(T^{2/3}·V_T^{1/3}) under non-stationary utilities. Selects from fixed pools (12K MATH problems). Qwen2.5-3B: 30.0% AIME 2024, 81.0% MATH-500 (+28.6% relative over uniform 23.3%; beats SEC at 20.0% in matched 3B comparison). ~9% overhead. Key insight: Actor-Curator's per-problem utility estimation is more expressive than SEC's category-level Q-values, yielding consistent gains. Critical differentiation from SACE-RLVR on four dimensions: (a) SELECTION vs. SYNTHESIS—both SEC and Actor-Curator select from fixed pools of existing problems; they cannot synthesize new problems targeting identified gaps. As the policy improves toward competition level, the fraction of useful problems in a fixed 12K pool shrinks (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED optimization—Actor-Curator optimizes aggregate per-problem utility without explicit multi-dimensional coverage constraints, risking concentration on high-utility niches without ensuring breadth (analogous to SAGE's demonstrated over-specialization); (c) STATELESS vs. PERSISTENT—neither maintains a persistent multi-dimensional archive with cross-step coverage tracking; (d) COMPLEMENTARITY—crucially, these approaches compete at different levels: Actor-Curator's bandit selection could serve as the within-archive sampling strategy, combining principled selection WITH coverage-maintaining synthesis. We test this complementarity explicitly.\n\n**Balanced difficulty filtering theory.** Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) proves that expected policy improvement is lower-bounded by the variance of task-level success probabilities p(x)(1-p(x)), maximized at p(x)=0.5. Balanced filtering (0.3&lt;p(x)<0.7) achieves +12% on AMC and +10% on AIME with Qwen2.5 models in less than half the training steps of standard GRPO. This theoretical result directly supports our difficulty-aware design: our Bayesian learnability criterion tracks p(1-p) per problem via Beta posteriors, and our archive's ZPD-weighted sampling preferentially selects problems near the difficulty frontier.\n\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\n\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\n\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold α=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively). On AIME 2024, SAGE achieves 13.3%—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%. This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents. Training dynamics confirm this: over-specialization emerges after ~120 steps (peak 69.5% declining to 61.6% by step 240). Question pool grows 18× (1,136→20,532) as flat filtered dataset without structured organization.\n\n**Implicit curriculum theory.** 'The Implicit Curriculum' (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation—not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\n\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: 'behavioral diversity is the binding constraint for RL.' RL-PLUS (arXiv 2508.00222) demonstrates 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\n\n**Policy-level diversity maintenance (concurrent).** UCPO (arXiv 2605.00365) addresses pass@k diversity collapse at the optimization level rather than the data level, adding a conditional uniformity penalty that redistributes gradient signal toward underrepresented correct solutions. Achieves +10% absolute Pass@64 on AIME 2024 (DeepSeek-7B: 70.0%→80.0%) and +45% equation-level diversity while maintaining competitive Pass@1. Importantly, UCPO modifies the loss function, not the training distribution—making it orthogonal to and potentially complementary with archive-based diversity maintenance. UCPO ensures diversity within the correct solution set for a given problem; SACE-RLVR ensures diversity across the problem distribution.\n\n**Lightweight co-evolutionary diversity (concurrent).** Vocabulary Dropout (arXiv 2604.03472) prevents proposer diversity collapse in co-evolutionary frameworks by applying random hard logit masks during problem generation, achieving +4.4 average points on Qwen3-8B (+10.9 AMC, +3.4 AIME 2024, +7.8 AIME 2025) within R-Zero. Demonstrates that diversity collapse is a real bottleneck in co-evolutionary RLVR. Differentiation: VD maintains proposer diversity via stochastic masking; SACE-RLVR provides structured coverage guarantees and interpretable gap identification.\n\n**Meta-RL curriculum generation (concurrent).** SOAR (arXiv 2601.18778) uses bi-level meta-RL where a teacher generates stepping-stone problems rewarded by measured student improvement on hard problems. Achieves +9.3% pass@32 on MATH fail@128 tasks (Llama-3.2-3B), recovering 75% of oracle gains from training on the full MATH dataset. Key insight: structural quality of generated problems matters more than solution correctness. Conceptually parallel to our proactive gap identification but uses meta-RL reward signal (measured student improvement) vs. our archive-structure-based gap detection. SOAR operates at the edge of learnability for currently-unsolvable problems; SACE-RLVR maintains coverage across the full difficulty spectrum.\n\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\n\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%→16.4%; Qwen3-8B AIME24: 16.7→26.0. Proves diversity collapse is real (TTRL pass@16: 32.4→16.7).\n\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\n\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\n\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR—related to our approach but operates at policy gradient level vs. our archive-replacement level.\n\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K→80K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry autoformalization has ~3.7× lower success rate than non-geometry (IndiMathBench arXiv 2512.00997: 12.2% vs 44.9% BEq across top models); the paper attributes this partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty. These grounding data inform our per-niche survival estimates.\n\n**Verification.** VHG (arXiv 2605.06660): validity gating.\n\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\n\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\n\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\n\n**The precise gap.** DéjàQ: 1D, GSM-only. SEC: MAB over categories, 1D, fixed pool. Actor-Curator: per-problem bandit, fixed pool, no coverage tracking. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization, zero AIME improvement over base model. Online Difficulty Filtering: theoretical support for balanced filtering, no archive structure. UCPO: policy-level diversity, no data-level coverage. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification with synthesis, structured coverage tracking, and Bayesian learnability replacement. Moreover, no existing work tests whether bandit-based selection and archive-based synthesis are complementary.",
  "inspired_by": "DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + SEC_insight['MAB over problem categories during RL; 17.5% AIME24'] + Actor_Curator_insight['neural bandit with regret guarantees; 30.0% AIME24; ~9% overhead; pool-selection ceiling motivates synthesis'] + Online_Difficulty_Filtering['p(1-p) lower bound on policy improvement; balanced filtering; EACL 2026'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools → over-specialization ~120 steps; 13.3% AIME = base model; AMC degrades'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + UCPO_concurrent['policy-level diversity; +10% Pass@64 AIME; complementary to data-level'] + VocabDropout_concurrent['+4.4 avg; diversity collapse prevention'] + SOAR_concurrent['meta-RL teacher; 75% oracle recovery'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry ~3.7× lower autoformalization success; formalization-specific'] + EVOL_RL_warning['diversity collapse']",
  "approach": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics. We organize the system around **three core innovations** plus **four extensions** tested in ablations. This follows the structure of successful prior systems: DéjàQ claims ~2 core contributions atop ~11 mechanisms; CLPO claims 3 named contributions atop ~7 design choices.\n\n**Design Motivation: Why Coverage Matters (Two Independent Arguments).**\n\n*Argument 1: Relay-regime-inspired smooth difficulty coverage.* The implicit curriculum theory (arXiv 2602.14872, ICML 2026) demonstrates on synthetic tasks that smooth difficulty spectra ('relay regime') yield faster convergence than gapped spectra ('grokking regime'). While this theory assumes idealized conditions (uniform distributions, geometric difficulty structure, single attention layer) that differ from real RLVR, it provides a principled design heuristic: smoother difficulty coverage should improve convergence. Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) provides additional theoretical support: policy improvement is lower-bounded by p(1-p) variance, maximized at balanced difficulty, achieving +12% AMC and +10% AIME in half the training steps. Our 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) are motivated by these insights. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\n\n*Argument 2: Broad coverage prevents capability boundary collapse.* Even under the 'sparse policy selection' view where RL modifies only 1-3% of tokens (arXiv 2605.06241), comprehensive coverage is essential. Three empirical findings converge: (a) Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), each un-sharpened primitive type creates an exponential bottleneck; (b) Tailor (arXiv 2511.12429) directly demonstrates that behavioral diversity, not correctness, is the binding constraint for RL outcomes (25 vs. 4 primitives → substantial gains); (c) RL-PLUS (arXiv 2508.00222) shows narrow RLVR causes 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse distributions as the antidote (+69.2% relative improvement). Thus, comprehensive difficulty×topic coverage benefits under both views: relay-like curriculum dynamics AND broader capability activation.\n\n*Why archives with synthesis vs. bandit selection from fixed pools.* SEC and Actor-Curator demonstrate the clear value of adaptive problem selection during RL training. We argue that persistent archives with targeted synthesis provide three capabilities that fixed-pool bandit selection cannot: (i) COVERAGE GUARANTEES—bandits optimize aggregate utility and may concentrate on high-utility niches without ensuring breadth across the difficulty×topic space, analogous to SAGE's demonstrated over-specialization (13.3% AIME = base model, AMC degradation); structured archives explicitly enforce minimum coverage per niche. (ii) SYNTHESIS FOR GAPS—as the policy improves, the useful difficulty frontier advances, and a fixed pool (e.g., MATH's 12K problems) becomes increasingly sparse at the frontier; targeted synthesis creates fresh problems where the policy needs them most. (iii) PERSISTENT TRACKING—archives maintain cross-step memory of which niches are well-covered and which are stale, enabling proactive rather than reactive curriculum adaptation. However, these approaches are potentially COMPLEMENTARY: Actor-Curator's principled per-problem utility estimation can serve as the within-archive sampling strategy, and we test this explicitly (see E4 and baseline #5).\n\n---\n\n**CORE INNOVATION 1: 2D Learnability Archive (50 cells).**\n10 difficulty bins (width 0.1, empirical solve-rate) × 5 topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells, M=10 problems per cell. Topic classification via GPT-4o-mini (84-92% accuracy per arXiv 2411.00042). Difficulty measured via G=16 rollouts reused from training.\n\nThe 2D structure enables qualitatively new capabilities vs. prior work: (a) difficulty-aware coverage tracking—locate under-populated difficulty×topic niches BEFORE policy failures (vs. Socratic-Zero's reactive approach, SAGE's flat pool that over-specializes by step ~120, SEC/Actor-Curator's fixed-pool selection without coverage constraints); (b) persistent cross-step memory—problems track with the evolving policy, revealing emergent curriculum (vs. CLPO's stateless per-batch assessment, SEC's myopic TD updates); (c) interpretable post-hoc analysis—which niches drive benchmark performance.\n\nReplacement criterion: candidate problem enters a cell if its Bayesian learnability credible interval (see Core 3) exceeds the current worst occupant's upper bound. More principled than DéjàQ's point estimate comparison f(x')>f(y).\n\n**CORE INNOVATION 2: Proactive Gap-Targeted Synthesis with Verification.**\nExisting targeting is either reactive (Socratic-Zero examines specific failed solutions; SwS identifies aggregate weaknesses offline) or selection-only (SEC/Actor-Curator adaptively choose from fixed pools). SAGE's Challenger generates harder problems without coverage awareness, leading to over-specialization. The 2D archive enables proactive niche-level gap identification:\n\n(a) Identify under-performing cells: <3 problems or stale (not refreshed for >100 training steps).\n(b) Generate-then-classify synthesis: generate for target TOPIC without difficulty constraints, verify, then empirically measure difficulty via G=16 rollouts and assign to the appropriate cell. This avoids the 'double filter' problem (constraining both topic AND difficulty yields 4-17% per SPARQ/MathSmith evidence; topic-only yields higher survival).\n(c) 3-stage VHG-inspired verification: (i) format/solvability check (filters ~25-30%, consistent with FLAMES ~30% removal), (ii) cross-verification via majority vote across 2-3 strong models (filters ~15-20%), (iii) difficulty calibration via G=16 rollouts.\n\n**Concrete per-niche survival estimates (literature-grounded):**\nEstimates sourced from SPARQ (~25% QD survival), DART-Math (51.1% Level 5 dropout), FLAMES (50% removal at Level 5), and IndiMathBench (~3.7× lower geometry autoformalization success rate, 12.2% vs 44.9% BEq; noting this reflects formalization-specific difficulty in Lean 4 that may not fully transfer to problem synthesis—we conservatively estimate geometry synthesis is ~2-3× harder than algebra).\n\n- Easy-medium cells (solve-rate 0.3-0.8), common topics (Algebra, NT): ~30 cells, ~30-50% survival.\n  Need ~20-35 candidates/cell → ~600-1,050 total.\n- Medium-hard cells (solve-rate 0.1-0.3), common topics: ~10 cells, ~15-25% survival.\n  Need ~40-65 candidates/cell → ~400-650 total.\n- Geometry cells (all difficulties): ~10 cells, ~10-20% survival (geometry synthesis is harder than algebra due to constraint consistency requirements; conservatively ~2-3× harder based on adjusted IndiMathBench ratio with formalization-specific caveats).\n  Need ~50-100 candidates/cell → ~500-1,000 total.\n- Extreme cells (solve-rate <0.1 or >0.9, all topics): ~10 cells, ~3-8% survival (DART-Math: Level 5 loses 51% coverage; FLAMES: 50% removal at Level 5).\n  Need ~125-330 candidates/cell → ~1,250-3,300 total.\n- **Graceful degradation:** cells that cannot reach M=10 accept minimum 3 (sufficient for meaningful Beta posterior updates). Archive reports actual occupancy; analysis accounts for sparse cells.\n- **Total per refresh cycle:** ~2,750-6,000 candidates (median ~4,000). Generation cost using open-source 70B teacher: ~130 GPU-hours. Verification (G=16 rollouts per candidate on 7B): ~12 GPU-hours. Per-refresh total: ~142 GPU-hours. Over ~10 refreshes: ~1,420 GPU-hours. Alternative: API-based generation at ~$0.30/problem ≈ $1,200/refresh, $12,000 total.\n- Per-niche survival rates and generation statistics reported as community contribution.\n\n**CORE INNOVATION 3: Zero-Cost Bayesian Learnability Estimation.**\nDéjàQ estimates learnability via K=100 dedicated completions per problem—computationally expensive and separate from training. We reuse G=16 rollouts already generated for GRPO training—zero additional inference cost. G=16 is well-justified: DAPO (arXiv 2503.14476) standardizes G=16; MC-GRPO (arXiv 2601.22582) shows clear degradation at small G (G=2: 78.92%, G=4: 81.34%, G=8: 84.53%); the Gradient Starvation analysis (arXiv 2605.07689) explains the mechanism—for binary rewards, degenerate group probability is p^G+(1-p)^G, yielding 69.25% degenerate groups at G=4 vs. <1% at G=8.\n\nBayesian temporal smoothing: Beta-Bernoulli running posterior per problem (Beta(1,1) prior, updated each appearance). After 3 appearances (48 cumulative rollouts), posterior variance drops ~3×. Replacement uses conservative credible interval: candidate must exceed occupant's upper bound, preventing noisy replacements. The p(1-p) learnability signal is theoretically supported by Online Difficulty Filtering's result (arXiv 2504.03380) that policy improvement is lower-bounded by this exact quantity.\n\nRelated but distinct from the Discounted Beta-Bernoulli (DBB) estimator (arXiv 2603.18444), which applies Bayesian estimation at the policy gradient level. Our Beta posterior operates at the archive-replacement level for per-problem learnability tracking—a different application of the same statistical principle. VCRL's insight (arXiv 2509.19803) that reward variance reflects difficulty is extended from curriculum signal to Bayesian replacement criterion.\n\n---\n\n**EXTENSIONS (each tested in one ablation, not claimed as core contributions):**\n\nE1: Cross-niche SvS seeding. SvS-style answer-preserving mutation (ICLR 2026) from adjacent cells to seed under-populated niches. Expected ~70-80% validity for within-topic mutations. Particularly valuable for geometry and extreme cells where de novo generation has lower survival. Tested in A5.\n\nE2: James-Stein shrinkage. Following arXiv 2511.03710 (which demonstrates shrinkage baselines reduce MSE in RLVR), we apply shrinkage to per-problem learnability estimates, regularizing toward batch average. Not claimed as novel—cite and use. Tested in A6.\n\nE3: DGPO policy updates. MAD normalization + DQW weighting adopted from MathForge (arXiv 2601.20614, ICLR 2026). Addresses difficulty-dependent advantage scale. Tested in A7.\n\nE4: Archive sampling strategy. Compare (a) ZPD-weighted sampling with posterior variance weighting ([0.1, 0.9] solve-rate, high uncertainty → more sampling), (b) uniform sampling, and (c) Actor-Curator-style bandit sampling from the archive—directly testing whether principled per-problem utility estimation (à la Actor-Curator) further improves when operating within a coverage-maintaining archive. This tests the complementarity hypothesis: if (c) outperforms both Actor-Curator from a fixed pool and (a) from the archive, it validates that bandit selection and archive synthesis address orthogonal bottlenecks.\n\n---\n\n**Training Loop (VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary):**\n(a) Sample from archive with selected strategy (E4). (b) G=16 rollouts, compute advantages. (c) Policy update (GRPO or DGPO). (d) Update Beta posteriors per problem. (e) Every 50 steps: refresh sampled cells, reassign problems that shifted difficulty, flag stale cells, synthesize for gaps. Overhead: ~20-25% vs. vanilla GRPO (dominated by synthesis cost).\n\n**AIME Contextualization.** Distillation-based: 70-90% AIME 2024. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm. Value: METHOD + ABLATION INSIGHTS. Framework applicable atop distilled bases.\n\n**Baselines (8):** (1) DéjàQ-comp [PRIMARY: 2D+targeting value over 1D archive]. (2) CLPO [PRIMARY: persistent archive value over stateless curriculum]. (3) Socratic-Zero [PRIMARY: structured proactive vs. reactive instance-level targeting]. (4) SAGE [structured archive vs. flat pool; evidence: SAGE's AIME = base model + AMC degradation]. (5) Actor-Curator [PRIMARY: archive synthesis vs. bandit selection from fixed pool; complementarity test via E4]. (6) EVOL-RL [stateless novelty-aware diversity]. (7) MathForge [DGPO source; difficulty-aware optimization]. (8) Vanilla GRPO [minimal baseline].\n\n**Ablations (7):**\nA1: 1D archive only (tests Core 1 dimensionality).\nA2: Random synthesis vs. gap-targeted (tests Core 2 proactive targeting).\nA3: 3 bins vs. 10 bins [relay-regime-inspired test: first empirical comparison of coarse vs. fine difficulty granularity in real RLVR].\nA4: Point estimation vs. Beta posterior (tests Core 3 vs. DéjàQ-style p(1-p)).\nA5: Without cross-niche SvS seeding (tests E1 value, especially for sparse cells).\nA6: Without James-Stein shrinkage (tests E2).\nA7: GRPO vs. DGPO (tests E3).\n\n**Evaluation:** AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. pass@1 AND pass@k (pass@k especially important per RL-PLUS's capability boundary collapse finding and UCPO's concurrent work on policy-level diversity—we test whether archive-based data diversity and policy-level diversity address complementary aspects of the collapse). DAPO-Math-17k seeds.\n\n**Key Analyses:** (1) Coverage heatmaps showing cell occupancy evolution. (2) Per-cell benchmark contribution: which niches drive gains? (3) Emergent curriculum: bin-transition frequencies as policy improves. (4) Synthesis efficiency: per-topic survival rates vs. literature benchmarks (SPARQ, DART-Math, FLAMES), reported as community contribution. (5) Convergence speed: 10 vs. 3 bins. (6) Capability boundary: pass@1 vs. pass@k trajectories—does archive diversity prevent RL-PLUS-style collapse? How does data-level diversity (SACE-RLVR) compare to policy-level diversity (UCPO)? (7) Structured vs. flat: archive coverage diversity over training vs. SAGE-style accumulation. (8) Selection vs. synthesis: Actor-Curator from fixed pool vs. Actor-Curator-style sampling from SACE-RLVR archive—quantifying the value of synthesis and coverage maintenance.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "7,200 H100-hours (baselines: 8×250h=2,000h; SACE-RLVR 7B 800h; SACE-RLVR 8B 800h; ablations 7×200h=1,400h; synthesis/verification 1,420h; archive overhead 330h; E4 bandit variant 450h)",
      "timeline": "14-18 weeks",
      "estimated_gpu_cost": "$18,000 (at ~$2.50/H100-hr)"
    },
    "human_in_loop": {
      "gpu_hours": "5,600 H100-hours (reuse released code; shared verification; API-based generation saves ~1,100 GPU-hrs but adds ~$12,000 API cost)",
      "timeline": "12-15 weeks",
      "claude_api_cost": "$400-800 (code assistance)",
      "synthesis_api_cost": "$7,000-12,000 (problem generation via API, optional vs. GPU)",
      "estimated_gpu_cost": "$14,000"
    },
    "auto_research": {
      "gpu_hours": "8,800 H100-hours (exploratory sweeps over archive dimensions, bin count, refresh frequency, replacement criteria, synthesis strategies, bandit-archive complementarity)",
      "timeline": "10-13 weeks",
      "claude_api_cost": "$1,000-2,000",
      "estimated_gpu_cost": "$22,000",
      "speed_bottleneck": "GPU queue; each GRPO run 24-72h on 8×H100s. Synthesis for extreme cells dominates generation cost."
    }
  },
  "target_venues": [
    "ICLR 2027 (Sep 19-24, 2026) — stretch if pilot results by August",
    "ICML 2027 (~Jan 2027) — primary target, strong fit for RL + QD + coverage",
    "NeurIPS 2027 (~May 2027) — fallback with full evaluation"
  ],
  "level": "top-tier",
  "key_references": [
    "DéjàQ (arXiv 2601.01931) — PRIMARY PREDECESSOR, online MAP-Elites for RLVR at GSM level",
    "SEC (arXiv 2505.14970) — CRITICAL COMPARATOR, MAB over problem categories; 17.5% AIME24 on Qwen2.5-7B; TD(0) updates",
    "Actor-Curator (arXiv 2602.20532) — PRIMARY BASELINE, neural bandit selection from fixed pool; 30.0% AIME24 on Qwen2.5-3B; regret O(T^{2/3}·V_T^{1/3}); ~9% overhead",
    "Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) — THEORETICAL SUPPORT, p(1-p) lower bound on policy improvement; +12% AMC in half steps",
    "CLPO (arXiv 2509.25004) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024",
    "Socratic-Zero (arXiv 2509.24726) — PRIMARY BASELINE, three-agent co-evolution; 56.1% avg",
    "SAGE (arXiv 2603.15255) — BASELINE, 4-agent self-evolution; 13.3% AIME = base model; AMC degrades 57.5%→52.5%",
    "UCPO (arXiv 2605.00365) — CONCURRENT, policy-level diversity via conditional uniformity; +10% Pass@64 AIME24; complementary to data-level",
    "Vocabulary Dropout (arXiv 2604.03472) — CONCURRENT, lightweight diversity via logit masking; +4.4 avg on 8B",
    "SOAR (arXiv 2601.18778) — CONCURRENT, meta-RL teacher for edge-of-learnability synthesis; 75% oracle recovery",
    "The Implicit Curriculum (arXiv 2602.14872, ICML 2026) — DESIGN MOTIVATION, relay vs. grokking (synthetic tasks)",
    "Sparse Policy Selection (arXiv 2605.06241) — RL modifies 1-3% of tokens; motivates broad coverage",
    "Sharper Primitives (arXiv 2602.08281) — RLVR polarizes; multiplicative compounding; diverse training activates broader primitives",
    "Tailor (arXiv 2511.12429) — behavioral diversity is binding constraint for RL; 25 vs 4 primitives",
    "RL-PLUS (arXiv 2508.00222) — capability boundary collapse from narrow RLVR; +69.2% with diversity",
    "ProRL (arXiv 2505.24864) — diverse prolonged training accesses beyond base model ceiling",
    "Bidirectional Curriculum Generation (arXiv 2603.05120) — 4-agent bidirectional; 60.03 avg",
    "EVOL-RL (arXiv 2509.15194) — stateless novelty-aware diversity; AIME25 16.4%",
    "MathForge/DGPO (arXiv 2601.20614, ICLR 2026) — MAD normalization; adopted as extension",
    "VCRL (arXiv 2509.19803) — reward variance as difficulty proxy; G=16; 57.76 avg Qwen3-8B",
    "MC-GRPO (arXiv 2601.22582) — rollout count ablation: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%",
    "Gradient Starvation (arXiv 2605.07689) — 69% degenerate groups at G=4; explains G effect mechanistically",
    "DAPO (arXiv 2503.14476) — standardizes G=16",
    "Discounted Beta-Bernoulli (arXiv 2603.18444) — Bayesian estimation for RLVR; validates Beta approach",
    "SwS (NeurIPS 2025, arXiv 2506.08989) — offline weakness targeting; +10%",
    "SvS (ICLR 2026) — answer-preserving synthesis; used for cross-niche seeding",
    "SAND-Math (arXiv 2507.20527) — ~38% end-to-end competition synthesis survival",
    "SPARQ (arXiv 2506.06499) — ~25% QD survival (320K→80K); per-niche evidence",
    "DART-Math (arXiv 2407.13690, NeurIPS 2024) — Level 5: 51.1% query dropout; difficulty survival data",
    "FLAMES (arXiv 2508.16514) — ~30% strict survival; Level 5: 50% removal",
    "IndiMathBench (arXiv 2512.00997) — geometry ~3.7× lower autoformalization success; formalization-specific context",
    "VHG (arXiv 2605.06660) — validity gating; inspires verification",
    "Shrinking the Variance (arXiv 2511.03710) — James-Stein shrinkage for RLVR",
    "EBPO (arXiv 2602.05165) — empirical Bayes for GRPO",
    "R-Zero (ICLR 2026) — self-evolving; collapses iter 3",
    "Klear-Reasoner-8B (arXiv 2508.07629) — 90.5% AIME 2024; distillation context",
    "Prism (arXiv 2603.13309) — 128-cluster diversity with ZPD gate",
    "R-Diverse (arXiv 2602.13103) — SAM skill diversity + MAP memory",
    "STAT (arXiv 2510.10023) — Missing-Skill-Profile",
    "Problem Categorization (arXiv 2411.00042) — topic classification",
    "Two-Stage Dynamic View (arXiv 2510.04028) — capability shrinkage then expansion",
    "Does RL Incentivize Reasoning? (NeurIPS 2025, arXiv 2504.13837) — coverage framing"
  ],
  "description": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), scaling online MAP-Elites from GSM-level (DéjàQ) to competition-level math through three core innovations plus four extensions. Two independent motivations for comprehensive coverage: (1) relay-regime theory (arXiv 2602.14872) and balanced difficulty filtering theory (arXiv 2504.03380, EACL 2026: p(1-p) lower bound on policy improvement) suggest smooth difficulty spectra yield faster convergence—adopted as design heuristic, not guarantee, with A3 testing empirically; (2) even under 'sparse policy selection' (1-3% tokens modified), broad coverage prevents 'capability boundary collapse' (RL-PLUS: pass@1↑ pass@128↓; +69.2% with diversity), ensures multiplicative primitive sharpening across domains (Sharper Primitives), and provides the behavioral diversity that is the binding constraint for RL (Tailor: 25 vs 4 primitives). Core 1: 2D archive (10 bins × 5 topics = 50 cells) with proactive gap identification and Bayesian replacement—addresses SAGE's over-specialization at step ~120 (AIME 13.3% = base model, AMC degradation 57.5%→52.5%). Core 2: generate-then-classify synthesis with per-niche survival estimates (central: 30-50%, geometry: 10-20% accounting for ~3.7× autoformalization difficulty ratio from IndiMathBench with formalization-specific caveats, extreme: 3-8%; graceful degradation to min 3/cell; ~142 GPU-hrs/refresh). Core 3: zero-cost Bayesian estimation via G=16 rollout reuse (vs DéjàQ K=100), Beta posterior + credible intervals; G=16 justified by MC-GRPO ablation + gradient starvation analysis (69% degenerate groups at G=4). Key positioning vs. bandit-based curriculum: SEC (17.5% AIME24, Qwen2.5-7B) and Actor-Curator (30.0% AIME24, Qwen2.5-3B, ~9% overhead) demonstrate adaptive selection value but are limited by fixed pool exhaustion, lack of synthesis, and absence of coverage tracking. SACE-RLVR provides what bandits cannot: synthesis for identified gaps, structured coverage guarantees, and persistent cross-step memory. The approaches are potentially complementary—Actor-Curator's bandit sampling from SACE-RLVR's archive tested in E4 and Analysis #8. Extensions: SvS seeding, shrinkage, DGPO, archive sampling strategy (including Actor-Curator-style variant)—each ablated. Eight baselines (DéjàQ-comp, CLPO, Socratic-Zero, SAGE, Actor-Curator, EVOL-RL, MathForge, GRPO), seven ablations including pass@k capability boundary analysis and selection-vs-synthesis analysis. Concurrent work positioned: UCPO (policy-level diversity, complementary), Vocabulary Dropout (lightweight alternative), SOAR (meta-RL curriculum). Qwen2.5-Math-7B/Qwen3-8B, AIME 2024/2025, MATH-500, AMC, Minerva, OlympiadBench.",
  "project_name": "sace_rlvr",
  "source": "web_research",
  "reviewer_response": {
    "revision_overview": "MAJOR REVISION addressing the single blocking issue (SEC/Actor-Curator, unaddressed for 7 rounds) through substantive integration, not surface patching. Six structural changes: (1) SEC and Actor-Curator added as major landscape section with detailed four-dimensional differentiation (selection vs. synthesis, aggregate vs. structured, stateless vs. persistent, complementarity), (2) Actor-Curator added as 8th baseline with explicit complementarity test, (3) IndiMathBench geometry ratio corrected to ~3.7× with formalization-specific context, (4) SAGE AIME presentation corrected to show base-model matching and AMC degradation, (5) Online Difficulty Filtering cited as theoretical support for p(1-p) learnability criterion, (6) UCPO, Vocabulary Dropout, and SOAR added as concurrent work. Extension E4 reframed to explicitly test bandit-archive complementarity hypothesis.",
    "issue_1_sec_actor_curator_blocking": "ADDRESSED SUBSTANTIVELY after 7 rounds. Added as major landscape section ('Bandit-based adaptive curriculum') with full technical details: SEC's MAB formulation (TD(0) on Q-values, Boltzmann sampling, 1D categories, 17.5% AIME24 on Qwen2.5-7B, 76.1% MATH-500, 51.1% AMC22-23), Actor-Curator's neural bandit (OSMD, per-problem utility via Qwen3-0.6B curator, regret O(T^{2/3}·V_T^{1/3}), 30.0% AIME24 on Qwen2.5-3B, 81.0% MATH-500, ~9% overhead). Four-dimensional differentiation: (a) SELECTION vs. SYNTHESIS—bandits select from fixed 12K pools and cannot create problems targeting identified gaps; pool-exhaustion problem as policy improves; (b) AGGREGATE vs. STRUCTURED—Actor-Curator optimizes aggregate per-problem utility without multi-dimensional coverage constraints, risking niche concentration (analogous to SAGE's over-specialization); (c) STATELESS vs. PERSISTENT—no cross-step coverage tracking or emergent curriculum visualization; (d) COMPLEMENTARITY—Actor-Curator's bandit can serve as within-archive sampling strategy. Actor-Curator added as baseline #5. Extension E4 reframed to compare ZPD, uniform, and Actor-Curator-style bandit sampling FROM the archive. New analysis #8 directly quantifies selection-vs-synthesis value: Actor-Curator from fixed pool vs. Actor-Curator-style from SACE-RLVR archive. Added 'Why archives with synthesis vs. bandit selection' subsection in approach with three-capability argument (coverage guarantees, synthesis for gaps, persistent tracking). Core problem and opportunity sections updated to integrate bandit-based approaches as part of the research landscape.",
    "issue_2_online_difficulty_filtering": "ADDED. Cited in landscape as 'Balanced difficulty filtering theory' (arXiv 2504.03380, EACL 2026). Key result: expected policy improvement lower-bounded by p(x)(1-p(x)), maximized at p(x)=0.5. Achieves +12% AMC and +10% AIME in half training steps with Qwen2.5 models. Integrated into three locations: (1) Argument 1 in approach as additional theoretical support alongside implicit curriculum theory; (2) Core 3 discussion noting our Beta posterior tracks exactly the p(1-p) quantity this theory shows lower-bounds policy improvement; (3) dedicated landscape entry connecting to our archive's ZPD-weighted sampling.",
    "issue_3_indimathbench_corrected": "FIXED throughout all occurrences. Changed '6-7× harder' to '~3.7× lower autoformalization success rate (12.2% vs 44.9% BEq across top models)' with explicit caveat: 'IndiMathBench attributes geometry difficulty partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty.' Geometry synthesis difficulty conservatively re-estimated as ~2-3× harder than algebra. Survival estimates adjusted: geometry cells 10-20% (was 5-15%), need 50-100 candidates/cell (was 65-200). Per-refresh total revised to ~2,750-6,000 candidates (was 2,900-7,000), ~142 GPU-hrs (was 162). Total synthesis cost over 10 refreshes: ~1,420 GPU-hrs (was 1,620).",
    "issue_4_sage_aime_corrected": "FIXED. Now explicitly states: 'On AIME 2024, SAGE achieves 13.3%—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%.' Interpretation strengthened: 'This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents.' This corrected framing is STRONGER evidence for our approach than the original presentation.",
    "issue_5_ucpo_concurrent": "ADDED. Full landscape entry: UCPO (arXiv 2605.00365) adds conditional uniformity penalty redistributing gradient toward underrepresented correct solutions. DeepSeek-7B AIME24: Pass@1 27.71%→30.16%, Pass@64 70.0%→80.0% (+10% absolute). +45% equation-level diversity. Qwen2.5-7B AIME24: Pass@64 43.33%→56.67%. Key differentiation: UCPO modifies loss function (policy-level), SACE-RLVR modifies training distribution (data-level)—orthogonal and potentially complementary. Analysis #6 updated to compare data-level vs. policy-level diversity approaches.",
    "issue_6_vocab_dropout_soar": "ADDED. Vocabulary Dropout (arXiv 2604.03472): hard logit masking on proposer in R-Zero, +4.4 avg on Qwen3-8B (+10.9 AMC, +3.4 AIME24, +7.8 AIME25). Demonstrates diversity collapse is real bottleneck. Differentiation: stochastic masking vs. structured coverage. SOAR (arXiv 2601.18778): bi-level meta-RL teacher/student on Llama-3.2-3B, +9.3% pass@32 on MATH fail@128, recovers 75% oracle gains. Key insight: structural quality > solution correctness. Differentiation: meta-RL reward signal vs. archive-structure gap detection; SOAR targets edge of learnability, SACE-RLVR maintains full-spectrum coverage.",
    "score_trajectory_note": "This revision addresses the #1 blocking issue (SEC/Actor-Curator, 7 rounds persistent) through substantive integration, not surface citation. The four-dimensional differentiation (selection/synthesis, aggregate/structured, stateless/persistent, complementarity) provides a rigorous argument for why archives with synthesis offer capabilities that bandit selection cannot. The complementarity test (E4 and Analysis #8) turns a potential weakness into a strength: rather than competing with bandits, SACE-RLVR subsumes them. The corrected SAGE presentation (AIME = base, AMC degradation) actually strengthens the case for structured archives. Online Difficulty Filtering's p(1-p) result independently validates our Bayesian learnability criterion. All six recommended concurrent works now integrated."
  }
}

## Reviewer feedback (round 9)
Issues: ["MISSING WORK: CurES (arXiv 2510.01037, Mar 2026 revision) uses Beta(α,β) per-problem posteriors with Bayesian updates for RLVR curriculum selection, derives optimal sampling distribution based on p(1-p), achieves +4.82 over GRPO on 7B (24.58% AIME24). This directly overlaps with Core Innovation 3's 'Zero-Cost Bayesian Learnability Estimation' — CurES applies the SAME statistical framework (Beta posteriors + p(1-p) signal) for problem selection in RLVR. While CurES selects from fixed pools (vs SACE-RLVR's archive replacement), claiming Beta posteriors as a 'core innovation' without acknowledging CurES is a significant omission that weakens Core 3's novelty.", "MISSING WORK: InSight (arXiv 2603.01907, Mar 2026) models data outcomes using Bayesian latent success rates for RLVR data selection, with mutual information-based acquisition scores. Related to Core 3's Bayesian approach, achieving ~2.2× training acceleration.", "NOVELTY PRESSURE ON CORE 3: The proposal already cites DBB (arXiv 2603.18444) for Bayesian estimation at the policy gradient level. With CurES using Beta posteriors at the curriculum level and Online Difficulty Filtering providing the p(1-p) theory, Core 3's novelty reduces to: applying Beta posteriors specifically for ARCHIVE REPLACEMENT with credible interval comparison (vs point estimates). This is a valid but narrow contribution that may not warrant 'core innovation' status.", "INTERESTING CONTEXT: At the 3B scale, SEC (20.0%) actually UNDERPERFORMS uniform sampling (23.33%) on AIME24, while Actor-Curator (30.0%) beats both. This suggests category-level bandits can fail without coverage guarantees — the proposal could use this data point to strengthen the archives-over-bandits argument.", "VENUE TIMELINE: ICLR 2027 deadline ~Sep 24, 2026. With 14-18 week timeline starting late May 2026, earliest completion is mid-September — making ICLR 2027 nearly impossible, not merely a 'stretch.' The proposal honestly labels it 'stretch' but should consider removing it to avoid credibility concerns."]
Feedback: **This is Round 9 of 10. Round 10 requires a final pass/fail decision. Current average: 3.875 < 4.0 threshold. Here is exactly what is needed:**

**(1) Add CurES (arXiv 2510.01037) — CRITICAL for Round 10.** CurES uses the EXACT same statistical mechanism as Core 3: Beta(α,β) per problem, Bayesian posterior updates with new rollouts, p(1-p)-based sampling distribution. The proposal cites DBB (gradient level) and Online Difficulty Filtering (theory), but misses CurES (curriculum level) — the most directly comparable prior art for Core 3. Add CurES to the landscape section with differentiation: CurES uses Beta posteriors for SAMPLING from fixed pools (which problem to train on?); SACE-RLVR uses them for REPLACEMENT in evolving archives (should this new problem replace the worst occupant?). CurES uses point estimates for sampling probabilities; SACE-RLVR uses credible intervals for replacement decisions. The 'zero-cost' aspect (reusing G=16 training rollouts vs dedicated evaluation) remains valid regardless.

**(2) Reframe Core 3's novelty claim.** Given CurES + DBB + Online Difficulty Filtering, 'Zero-Cost Bayesian Learnability Estimation' should not be positioned as though Beta posteriors in RLVR are novel. Reframe: 'We apply established Beta-Bernoulli estimation (cf. CurES, DBB) to a new decision problem — archive replacement via credible interval comparison — at zero additional inference cost by reusing training rollouts.' This is more honest and equally compelling.

**(3) Optional but recommended:** Note that SEC underperforms uniform at 3B (20.0% vs 23.33%) — this strengthens your argument that category-level bandits without coverage guarantees can fail, providing concrete evidence for the archives-over-bandits thesis.

**Round 10 outlook:** If CurES is addressed and Core 3 reframed, I would lean toward 'pass' — the proposal has exceptional clarity and thoroughness, the complementarity test is genuinely novel, and the remaining novelty (2D archive + gap-targeted synthesis + credible-interval replacement + bandit-archive complementarity) is sufficient for a well-executed integration paper at top venues. The novelty score is the bottleneck at 3.5; with honest reframing it could reach 3.75, and with the clarity bonus (4.5) the overall quality is competitive.

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "38797e77-eaee-49b5-bbe3-23068fecf684",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T03:37:23.942Z_

```json
{
  "parentUuid": "38797e77-eaee-49b5-bbe3-23068fecf684",
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
  "uuid": "8ec73140-3c60-47c6-afd3-75b3ab4ca4be",
  "timestamp": "2026-05-28T03:37:23.942Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T03:37:23.942Z_

```json
{
  "parentUuid": "8ec73140-3c60-47c6-afd3-75b3ab4ca4be",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1bc01697-a8a1-465d-8f03-3f370b68a89a",
  "timestamp": "2026-05-28T03:37:23.942Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
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
  "leafUuid": "1bc01697-a8a1-465d-8f03-3f370b68a89a",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise RLVR archive approach for CurES acknowledgment",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Assistant

_source line 8 · 2026-05-28T03:37:31.797Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully:

1. **CurES (arXiv 2510.01037)** - CRITICAL missing work that uses Beta posteriors + p(1-p) for RLVR curriculum selection. This directly overlaps with Core 3.
2. **InSight (arXiv 2603.01907)** - Another Bayesian approach for RLVR data selection.
3. **Novelty pressure on Core 3** - Need to reframe from "novel innovation" to "novel application of established technique."


4. **SEC underperforms at 3B** - This is a useful data point that strengthens the argument.
5. **Venue timeline** - ICLR 2027 is unrealistic, so I should remove it.

I need to dig into CurES and InSight to understand their approaches, then revise accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bc01697-a8a1-465d-8f03-3f370b68a89a",
  "isSidechain": false,
  "requestId": "req_011CbUGYHXscF8wEPfFH2Hn9",
  "type": "assistant",
  "uuid": "adaaacba-dd61-4284-9edf-d57a15fb0bf0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUdQDo34dtEfASsKhEvpQW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18112,
      "cache_read_input_tokens": 11014,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 18112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18112
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

_source line 9 · 2026-05-28T03:37:31.896Z_

I need to research the critical missing papers (CurES and InSight) before revising. Let me do deep searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adaaacba-dd61-4284-9edf-d57a15fb0bf0",
  "isSidechain": false,
  "requestId": "req_011CbUGYHXscF8wEPfFH2Hn9",
  "type": "assistant",
  "uuid": "b961e28c-f780-4bd4-8101-a7b99c8db0bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUdQDo34dtEfASsKhEvpQW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18112,
      "cache_read_input_tokens": 11014,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 18112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18112
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

_source line 10 · 2026-05-28T03:37:32.405Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AwFSPKnXNq8yc3s5Hbacy9`</summary>

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
  "parentUuid": "b961e28c-f780-4bd4-8101-a7b99c8db0bf",
  "isSidechain": false,
  "requestId": "req_011CbUGYHXscF8wEPfFH2Hn9",
  "type": "assistant",
  "uuid": "267e4501-d17c-4376-ad74-a80c4b7db142",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUdQDo34dtEfASsKhEvpQW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18112,
      "cache_read_input_tokens": 11014,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 18112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18112
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

_source line 11 · 2026-05-28T03:37:32.412Z_

<details><summary>↩ Tool result · `toolu_01AwFSPKnXNq8yc3s5Hbacy9`</summary>

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
  "parentUuid": "267e4501-d17c-4376-ad74-a80c4b7db142",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "6c16d5b9-0e6f-4b2f-b05e-77226968af48",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "267e4501-d17c-4376-ad74-a80c4b7db142",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T03:37:45.627Z_

Now let me research CurES and InSight in parallel with multiple search strategies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c16d5b9-0e6f-4b2f-b05e-77226968af48",
  "isSidechain": false,
  "requestId": "req_011CbUGYuy7jqh4jYu7c61UX",
  "type": "assistant",
  "uuid": "5d981b0d-f36e-43ae-9ff5-fa369ca34c11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016keS841jwoGLM1QR8jAVqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 29126,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 29126,
          "cache_creation_input_tokens": 1337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1337
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

_source line 13 · 2026-05-28T03:37:46.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XUDZfUCRgdSrFc7qmfdC5`</summary>

```json
{
  "query": "CurES arXiv 2510.01037 Beta posterior Bayesian RLVR curriculum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d981b0d-f36e-43ae-9ff5-fa369ca34c11",
  "isSidechain": false,
  "requestId": "req_011CbUGYuy7jqh4jYu7c61UX",
  "type": "assistant",
  "uuid": "b53b373c-9466-4598-9b08-46338ec5df09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016keS841jwoGLM1QR8jAVqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 29126,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 29126,
          "cache_creation_input_tokens": 1337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1337
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

_source line 14 · 2026-05-28T03:37:53.147Z_

<details><summary>↩ Tool result · `toolu_012XUDZfUCRgdSrFc7qmfdC5`</summary>

```text
Web search results for query: "CurES arXiv 2510.01037 Beta posterior Bayesian RLVR curriculum"

Links: [{"title":"CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs","url":"https://arxiv.org/html/2510.01037"},{"title":"CurES: From Gradient Analysis to Efficient Curriculum ...","url":"https://www.arxiv.org/pdf/2510.01037"},{"title":"[2510.01037] CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs","url":"https://arxiv.org/abs/2510.01037"},{"title":"Paper page - CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs","url":"https://huggingface.co/papers/2510.01037"},{"title":"PuzzleCraft: Exploration-Aware Curriculum Learning for Puzzle-Based RLVR in VLMs","url":"https://arxiv.org/pdf/2512.14944"},{"title":"Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/pdf/2603.18444"}]

Based on the search results, here's what I found about CurES (arXiv 2510.01037):

## Overview

CurES is a theoretically grounded curriculum learning algorithm for RLVR (Reinforcement Learning with Verifiable Reward). The approach adaptively prioritizes training prompts of optimal difficulty and dynamically allocates rollout budgets.

## Key Technical Components

**Bayesian Beta Posterior Approach**: The method models the success rate of each prompt instance with a Beta distribution, which naturally incorporates prior information and posterior updates as new rollouts are observed.

**Gradient Analysis Foundation**: The theoretical analysis identifies two key factors influencing training efficiency: the selection of training prompts and the allocation of rollout quantities across different prompts. The sampling distribution of prompts dictates the convergence rate of gradient descent, while the allocation of the rollout quantity influences the consistency and stability of overall gradient updates.

## Performance Results

CurES outperforms Group Relative Policy Optimization (GRPO) by +3.30 points and +4.82 points with 1.5B and 7B models, respectively, and exceeds the best prior sample efficient methods by +2.12 points on average across eight math reasoning benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b53b373c-9466-4598-9b08-46338ec5df09",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "5151c550-6db3-4d5e-a7a9-c907e551cd36",
  "toolUseResult": {
    "query": "CurES arXiv 2510.01037 Beta posterior Bayesian RLVR curriculum",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FsKBMHbAM6KakZs2wavios",
        "content": [
          {
            "title": "CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs",
            "url": "https://arxiv.org/html/2510.01037"
          },
          {
            "title": "CurES: From Gradient Analysis to Efficient Curriculum ...",
            "url": "https://www.arxiv.org/pdf/2510.01037"
          },
          {
            "title": "[2510.01037] CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs",
            "url": "https://arxiv.org/abs/2510.01037"
          },
          {
            "title": "Paper page - CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs",
            "url": "https://huggingface.co/papers/2510.01037"
          },
          {
            "title": "PuzzleCraft: Exploration-Aware Curriculum Learning for Puzzle-Based RLVR in VLMs",
            "url": "https://arxiv.org/pdf/2512.14944"
          },
          {
            "title": "Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards",
            "url": "https://arxiv.org/pdf/2603.18444"
          }
        ]
      },
      "Based on the search results, here's what I found about CurES (arXiv 2510.01037):\n\n## Overview\n\nCurES is a theoretically grounded curriculum learning algorithm for RLVR (Reinforcement Learning with Verifiable Reward). The approach adaptively prioritizes training prompts of optimal difficulty and dynamically allocates rollout budgets.\n\n## Key Technical Components\n\n**Bayesian Beta Posterior Approach**: The method models the success rate of each prompt instance with a Beta distribution, which naturally incorporates prior information and posterior updates as new rollouts are observed.\n\n**Gradient Analysis Foundation**: The theoretical analysis identifies two key factors influencing training efficiency: the selection of training prompts and the allocation of rollout quantities across different prompts. The sampling distribution of prompts dictates the convergence rate of gradient descent, while the allocation of the rollout quantity influences the consistency and stability of overall gradient updates.\n\n## Performance Results\n\nCurES outperforms Group Relative Policy Optimization (GRPO) by +3.30 points and +4.82 points with 1.5B and 7B models, respectively, and exceeds the best prior sample efficient methods by +2.12 points on average across eight math reasoning benchmarks."
    ],
    "durationSeconds": 6.983969902000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b53b373c-9466-4598-9b08-46338ec5df09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T03:37:55.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QYa77GjSDjgtKmeQx8PWZ5`</summary>

```json
{
  "query": "InSight arXiv 2603.01907 Bayesian latent success RLVR data selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5151c550-6db3-4d5e-a7a9-c907e551cd36",
  "isSidechain": false,
  "requestId": "req_011CbUGaSPEbXVx2tNagMsV9",
  "type": "assistant",
  "uuid": "877610ce-3e30-44b6-8a02-9b9dee1e86d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rh6Rh4ByThF57qcZQNAcAz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 30463,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 30463,
          "cache_creation_input_tokens": 712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 712
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

_source line 16 · 2026-05-28T03:38:02.882Z_

<details><summary>↩ Tool result · `toolu_01QYa77GjSDjgtKmeQx8PWZ5`</summary>

```text
Web search results for query: "InSight arXiv 2603.01907 Bayesian latent success RLVR data selection"

Links: [{"title":"[2603.01907] Efficient RLVR Training via Weighted Mutual Information Data Selection","url":"https://arxiv.org/abs/2603.01907"},{"title":"Efficient RLVR Training via Weighted Mutual Information Data Selection","url":"https://arxiv.org/html/2603.01907"},{"title":"Paper page - Efficient RLVR Training via Weighted Mutual Information Data Selection","url":"https://huggingface.co/papers/2603.01907"},{"title":"Data-Efficient RLVR via Off-Policy Influence Guidance","url":"https://arxiv.org/pdf/2510.26491"},{"title":"Learn More with Less: Uncertainty Consistency Guided Query Selection for RLVR","url":"https://arxiv.org/pdf/2601.22595"},{"title":"Open-Medical-R1: How to Choose Data for RLVR Training at Medicine Domain","url":"https://arxiv.org/pdf/2504.13950"},{"title":"Beyond Variance: Prompt-Efficient RLVR via Rare-Event Amplification and Bidirectional Pairing","url":"https://arxiv.org/pdf/2602.03452"}]

Based on the search results, here's what I found about arXiv paper 2603.01907:

InSight is an INformation-guided data SamplInG metHod for RL Training, grounded in a weighted mutual information objective. By modeling data outcomes with Bayesian latent success rates, the method shows that expected uncertainty reduction decomposes into complementary difficulty- and evidence-dependent components, revealing a fundamental limitation of difficulty-only selection.

The paper addresses the problem that reinforcement learning plays a central role in improving the reasoning and alignment of large language models, yet its efficiency critically depends on how training data are selected. Existing online selection strategies predominantly rely on difficulty-based heuristics, favouring datapoints with intermediate success rates, implicitly equating difficulty with informativeness and neglecting epistemic uncertainty arising from limited evidence.

The paper was published on March 2, 2026, and is authored by Xinyu Zhou, Boyu Zhu, Haotian Zhang, Huiming Wang, and Zhijiang Guo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "877610ce-3e30-44b6-8a02-9b9dee1e86d7",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "62490ed2-3691-4b70-8d5b-3b92cd64cf8c",
  "toolUseResult": {
    "query": "InSight arXiv 2603.01907 Bayesian latent success RLVR data selection",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AL1A5P5KnavSoeHSi2Agzq",
        "content": [
          {
            "title": "[2603.01907] Efficient RLVR Training via Weighted Mutual Information Data Selection",
            "url": "https://arxiv.org/abs/2603.01907"
          },
          {
            "title": "Efficient RLVR Training via Weighted Mutual Information Data Selection",
            "url": "https://arxiv.org/html/2603.01907"
          },
          {
            "title": "Paper page - Efficient RLVR Training via Weighted Mutual Information Data Selection",
            "url": "https://huggingface.co/papers/2603.01907"
          },
          {
            "title": "Data-Efficient RLVR via Off-Policy Influence Guidance",
            "url": "https://arxiv.org/pdf/2510.26491"
          },
          {
            "title": "Learn More with Less: Uncertainty Consistency Guided Query Selection for RLVR",
            "url": "https://arxiv.org/pdf/2601.22595"
          },
          {
            "title": "Open-Medical-R1: How to Choose Data for RLVR Training at Medicine Domain",
            "url": "https://arxiv.org/pdf/2504.13950"
          },
          {
            "title": "Beyond Variance: Prompt-Efficient RLVR via Rare-Event Amplification and Bidirectional Pairing",
            "url": "https://arxiv.org/pdf/2602.03452"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2603.01907:\n\nInSight is an INformation-guided data SamplInG metHod for RL Training, grounded in a weighted mutual information objective. By modeling data outcomes with Bayesian latent success rates, the method shows that expected uncertainty reduction decomposes into complementary difficulty- and evidence-dependent components, revealing a fundamental limitation of difficulty-only selection.\n\nThe paper addresses the problem that reinforcement learning plays a central role in improving the reasoning and alignment of large language models, yet its efficiency critically depends on how training data are selected. Existing online selection strategies predominantly rely on difficulty-based heuristics, favouring datapoints with intermediate success rates, implicitly equating difficulty with informativeness and neglecting epistemic uncertainty arising from limited evidence.\n\nThe paper was published on March 2, 2026, and is authored by Xinyu Zhou, Boyu Zhu, Haotian Zhang, Huiming Wang, and Zhijiang Guo."
    ],
    "durationSeconds": 7.303096678000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "877610ce-3e30-44b6-8a02-9b9dee1e86d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T03:38:08.847Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BsQrQBm5hpMcUouhXu3gJB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.01037",
  "prompt": "Extract ALL technical details about CurES: 1) How exactly does it use Beta(α,β) posteriors? What are the prior parameters? How are they updated? 2) What is the exact sampling distribution derived from p(1-p)? 3) What is the rollout budget allocation mechanism? 4) What are the EXACT benchmark results, especially AIME 2024, MATH-500? 5) What base models are used? 6) What training data/pool size? 7) How does it differ from standard GRPO? 8) What is the paper's revision history (original date vs revisions)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62490ed2-3691-4b70-8d5b-3b92cd64cf8c",
  "isSidechain": false,
  "requestId": "req_011CbUGb9v4ef6B1GFjpJZgx",
  "type": "assistant",
  "uuid": "f30e178b-8304-4646-b270-a0d82845a661",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EteF6sh9GbcH9HPqDFY2Ym",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 31175,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 31175,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

_source line 18 · 2026-05-28T03:38:13.644Z_

<details><summary>↩ Tool result · `toolu_01BsQrQBm5hpMcUouhXu3gJB`</summary>

```text
# CurES Technical Details - Limited Information Available

Based on the arXiv abstract provided, I can only offer partial details, as the full paper content is not included:

## Available Information:

**Revision History:**
- Original submission: October 1, 2025
- Latest revision (v2): March 23, 2026

**Base Models:**
The abstract mentions experiments with "1.5B and 7B models" but doesn't specify architecture names.

**Performance Claims:**
The abstract states CurES "outperforms Group Relative Policy Optimization (GRPO) by +3.30 points and +4.82 points" for the respective model sizes, and "exceeds the best prior sample efficient methods by +2.12 points on average across eight math reasoning benchmarks."

Specific benchmark results for AIME 2024 and MATH-500 are not detailed in this excerpt.

## Information NOT in Provided Content:

The abstract does not contain specifics regarding:
- Beta(α,β) posterior mechanics or prior parameters
- The exact sampling distribution formula from p(1-p)
- Rollout budget allocation mechanism details
- Training data pool sizes
- Detailed architectural differences from GRPO

**Note:** To access these technical specifications, you would need to review the full paper PDF (available via the provided link) or the HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f30e178b-8304-4646-b270-a0d82845a661",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "a5f45d3f-71c1-43ed-9a2b-a7e4bf933401",
  "toolUseResult": {
    "bytes": 49104,
    "code": 200,
    "codeText": "OK",
    "result": "# CurES Technical Details - Limited Information Available\n\nBased on the arXiv abstract provided, I can only offer partial details, as the full paper content is not included:\n\n## Available Information:\n\n**Revision History:**\n- Original submission: October 1, 2025\n- Latest revision (v2): March 23, 2026\n\n**Base Models:**\nThe abstract mentions experiments with \"1.5B and 7B models\" but doesn't specify architecture names.\n\n**Performance Claims:**\nThe abstract states CurES \"outperforms Group Relative Policy Optimization (GRPO) by +3.30 points and +4.82 points\" for the respective model sizes, and \"exceeds the best prior sample efficient methods by +2.12 points on average across eight math reasoning benchmarks.\"\n\nSpecific benchmark results for AIME 2024 and MATH-500 are not detailed in this excerpt.\n\n## Information NOT in Provided Content:\n\nThe abstract does not contain specifics regarding:\n- Beta(α,β) posterior mechanics or prior parameters\n- The exact sampling distribution formula from p(1-p)\n- Rollout budget allocation mechanism details\n- Training data pool sizes\n- Detailed architectural differences from GRPO\n\n**Note:** To access these technical specifications, you would need to review the full paper PDF (available via the provided link) or the HTML version.",
    "durationMs": 4793,
    "url": "https://arxiv.org/abs/2510.01037"
  },
  "sourceToolAssistantUUID": "f30e178b-8304-4646-b270-a0d82845a661",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T03:38:22.293Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ch2vADW26pbrdP1SCnfxCL`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.01037",
  "prompt": "Extract ALL technical details about CurES: 1) How exactly does it use Beta(α,β) posteriors? What are the prior parameters? How are they updated? 2) What is the exact optimal sampling distribution? Is it proportional to p(1-p)? 3) What is the rollout budget allocation mechanism? 4) What are the EXACT benchmark results - especially AIME 2024, MATH-500, AMC scores? 5) What base models (Qwen2.5-Math-1.5B, 7B)? 6) What training data pool? 7) Does it select from a FIXED pool or synthesize new problems? 8) How does credible interval or point estimate factor in? 9) What is the \"zero additional cost\" claim - does it reuse training rollouts? 10) Section-by-section summary of the method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5f45d3f-71c1-43ed-9a2b-a7e4bf933401",
  "isSidechain": false,
  "requestId": "req_011CbUGbwuXbQ8Fz3bXvjd9C",
  "type": "assistant",
  "uuid": "095366f7-b6f2-4904-ba4e-8024350bedd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AGeJcnzyVphwDcnZiBdJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 31849,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 31849,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 537
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

_source line 20 · 2026-05-28T03:38:35.562Z_

<details><summary>↩ Tool result · `toolu_01Ch2vADW26pbrdP1SCnfxCL`</summary>

````text
# CurES: Technical Details Extraction

## 1) Beta Posterior Updates

CurES models prompt success probability as **Beta(α₀(xᵢ), β₀(xᵢ))**, where parameters represent "counts of correct and incorrect answers during sampling."

**Update mechanism:**
- Initialize with small batch (N' rollouts)
- At step t, after nᵢ samples with s correct answers:
  - αₜ(xᵢ) = αₜ₋₁(xᵢ) + s
  - βₜ(xᵢ) = βₜ₋₁(xᵢ) + (nᵢ - s)
- Point estimate uses "the mean of the Beta distribution"

## 2) Optimal Sampling Distribution

**Exact formula (Eq. 14):**
```
ρ*(x) = exp(√[p(x)(1-p(x))]/τ) / Σ exp(√[p(x')(1-p(x'))]/τ)
```

Yes, proportional to √[p(1-p)], where τ = α/√(2δ) (hyperparameter). This maximizes the theoretical convergence bound subject to entropy constraints.

## 3) Rollout Budget Allocation

**Formula (Eq. 20):**
```
nᵢ = (σᵢ / Σⱼσⱼ) × N
σᵢ = √[Tr(Variance of policy gradients given xᵢ)]
```

Allocates more rollouts to prompts with higher gradient variance, particularly "moderately difficult prompts" per experimental findings.

## 4) Exact Benchmark Results

**Qwen2.5-Math-1.5B:**
- MATH500: 77.20% (CurES-GRPO)
- GSM8K: 85.97%
- AIME24: 13.33% (averaged over 16 runs)
- AIME25: 10.42%
- AMC23: 52.19%

**Qwen2.5-Math-7B:**
- MATH500: 84.80%
- GSM8K: 92.27%
- AIME24: 24.58%
- AIME25: 15.21%
- AMC23: 64.38%

Outperforms GRPO by "+3.30 points and +4.82 points" on respective model scales.

## 5) Base Models

- **Qwen2.5-Math-1.5B** (1.5 billion parameters)
- **Qwen2.5-Math-7B** (7 billion parameters)

Both initialized from Qwen2.5-Math models.

## 6) Training Data Pool

**Numina-Math dataset**, partitioned into 15 non-overlapping subsets. Training uses "Reinforcement Learning with Verifiable Reward (RLVR)" where correctness is "objectively defined" through programmatic verification.

## 7) Pool Selection vs. Synthesis

CurES **selects from a fixed pool**—"we divide the dataset into T non-overlapped subsets and perform iterative training." No synthesis of new problems.

## 8) Credible Interval vs. Point Estimate

Uses **point estimate only**: "To reduce randomness, we use the mean of the Beta distribution to estimate prompt difficulty." No explicit credible interval incorporation for sampling decisions.

## 9) "Zero Additional Cost" Mechanism

Not explicitly claimed as zero-cost. However, parameter estimation reuses training rollouts: N' = 4 rollouts per prompt for initial estimates, then training phase uses N = 8×1024 total budget. Distribution reset per iteration "alleviates distribution shift without introducing significant computational overhead."

## 10) Section-by-Section Summary

**§4.1:** Derives that loss convergence is bounded by √[p(x)(1-p(x))], proving prompt difficulty controls optimization potential. Entropy-maximized sampling yields softmax distribution over difficulty.

**§4.2:** Minimizes variance of practical gradient updates under fixed rollout budget N. Optimal allocation proportional to √[gradient variance], decomposed into correct/incorrect outcome branches.

**§4.3:** Implements Bayesian Beta-Binomial conjugacy for online difficulty estimation. Two-phase training: lightweight parameter stage (N' rollouts), then large-scale stage with variance-based allocation.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "095366f7-b6f2-4904-ba4e-8024350bedd3",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "2e5b905c-67a0-4964-8273-856bc5e74174",
  "toolUseResult": {
    "bytes": 612111,
    "code": 200,
    "codeText": "OK",
    "result": "# CurES: Technical Details Extraction\n\n## 1) Beta Posterior Updates\n\nCurES models prompt success probability as **Beta(α₀(xᵢ), β₀(xᵢ))**, where parameters represent \"counts of correct and incorrect answers during sampling.\"\n\n**Update mechanism:**\n- Initialize with small batch (N' rollouts)\n- At step t, after nᵢ samples with s correct answers:\n  - αₜ(xᵢ) = αₜ₋₁(xᵢ) + s\n  - βₜ(xᵢ) = βₜ₋₁(xᵢ) + (nᵢ - s)\n- Point estimate uses \"the mean of the Beta distribution\"\n\n## 2) Optimal Sampling Distribution\n\n**Exact formula (Eq. 14):**\n```\nρ*(x) = exp(√[p(x)(1-p(x))]/τ) / Σ exp(√[p(x')(1-p(x'))]/τ)\n```\n\nYes, proportional to √[p(1-p)], where τ = α/√(2δ) (hyperparameter). This maximizes the theoretical convergence bound subject to entropy constraints.\n\n## 3) Rollout Budget Allocation\n\n**Formula (Eq. 20):**\n```\nnᵢ = (σᵢ / Σⱼσⱼ) × N\nσᵢ = √[Tr(Variance of policy gradients given xᵢ)]\n```\n\nAllocates more rollouts to prompts with higher gradient variance, particularly \"moderately difficult prompts\" per experimental findings.\n\n## 4) Exact Benchmark Results\n\n**Qwen2.5-Math-1.5B:**\n- MATH500: 77.20% (CurES-GRPO)\n- GSM8K: 85.97%\n- AIME24: 13.33% (averaged over 16 runs)\n- AIME25: 10.42%\n- AMC23: 52.19%\n\n**Qwen2.5-Math-7B:**\n- MATH500: 84.80%\n- GSM8K: 92.27%\n- AIME24: 24.58%\n- AIME25: 15.21%\n- AMC23: 64.38%\n\nOutperforms GRPO by \"+3.30 points and +4.82 points\" on respective model scales.\n\n## 5) Base Models\n\n- **Qwen2.5-Math-1.5B** (1.5 billion parameters)\n- **Qwen2.5-Math-7B** (7 billion parameters)\n\nBoth initialized from Qwen2.5-Math models.\n\n## 6) Training Data Pool\n\n**Numina-Math dataset**, partitioned into 15 non-overlapping subsets. Training uses \"Reinforcement Learning with Verifiable Reward (RLVR)\" where correctness is \"objectively defined\" through programmatic verification.\n\n## 7) Pool Selection vs. Synthesis\n\nCurES **selects from a fixed pool**—\"we divide the dataset into T non-overlapped subsets and perform iterative training.\" No synthesis of new problems.\n\n## 8) Credible Interval vs. Point Estimate\n\nUses **point estimate only**: \"To reduce randomness, we use the mean of the Beta distribution to estimate prompt difficulty.\" No explicit credible interval incorporation for sampling decisions.\n\n## 9) \"Zero Additional Cost\" Mechanism\n\nNot explicitly claimed as zero-cost. However, parameter estimation reuses training rollouts: N' = 4 rollouts per prompt for initial estimates, then training phase uses N = 8×1024 total budget. Distribution reset per iteration \"alleviates distribution shift without introducing significant computational overhead.\"\n\n## 10) Section-by-Section Summary\n\n**§4.1:** Derives that loss convergence is bounded by √[p(x)(1-p(x))], proving prompt difficulty controls optimization potential. Entropy-maximized sampling yields softmax distribution over difficulty.\n\n**§4.2:** Minimizes variance of practical gradient updates under fixed rollout budget N. Optimal allocation proportional to √[gradient variance], decomposed into correct/incorrect outcome branches.\n\n**§4.3:** Implements Bayesian Beta-Binomial conjugacy for online difficulty estimation. Two-phase training: lightweight parameter stage (N' rollouts), then large-scale stage with variance-based allocation.",
    "durationMs": 13265,
    "url": "https://arxiv.org/html/2510.01037"
  },
  "sourceToolAssistantUUID": "095366f7-b6f2-4904-ba4e-8024350bedd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "2e5b905c-67a0-4964-8273-856bc5e74174",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise RLVR archive approach for CurES acknowledgment",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Tool call

_source line 23 · 2026-05-28T03:38:46.167Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NjG7u1baqF25BsQ67YNg1j`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.01907",
  "prompt": "Extract ALL technical details about InSight: 1) How does it model Bayesian latent success rates? What distribution? 2) What is the mutual information objective? 3) How does it decompose into difficulty-dependent and evidence-dependent components? 4) What are exact benchmark results (AIME 2024, MATH-500, etc.)? 5) What base models? 6) Does it use Beta posteriors? 7) How does it compare to CurES? 8) What is the ~2.2× training acceleration claim? 9) Fixed pool or synthesis? 10) Key differentiation from difficulty-only methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e5b905c-67a0-4964-8273-856bc5e74174",
  "isSidechain": false,
  "requestId": "req_011CbUGdZd9FfRTTBJepzg9w",
  "type": "assistant",
  "uuid": "4d28ec6c-bce7-4bb2-b305-ac657758110c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bo8MMtqFfEGS5Xho45JBaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 32386,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 32386,
          "cache_creation_input_tokens": 1358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1358
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

_source line 24 · 2026-05-28T03:38:58.518Z_

<details><summary>↩ Tool result · `toolu_01NjG7u1baqF25BsQ67YNg1j`</summary>

```text
# InSight: Technical Details Extraction

## 1. Bayesian Latent Success Rate Modeling
InSight models each datapoint's unknown success rate **ϕ_τ^t ∈ [0,1]** using a **Beta distribution prior**: "ϕ_τ^0 ∼ Beta(α_τ^0, β_τ^0)" initialized to uniform Beta(1,1). Rewards follow Bernoulli(ϕ_τ^t), with posterior updates: "ϕ_τ^t|ℋ_t ∼ Beta(α_τ^t + S_τ^t, β_τ^t + K − S_τ^t)" where S_τ^t is success count across K rollouts.

## 2. Mutual Information Objective
The core acquisition metric combines: **A(τ) = w(ϕ̄_τ) · I(R_{1:K}; Φ_τ)**, where mutual information captures "expected reduction in uncertainty about Φ_τ caused by observing the reward." This measures epistemic exploration value independent of sampled outcomes.

## 3. Decomposition Components
Expected variance reduction decomposes as: "Δ V(τ) = ϕ̄_τ(1−ϕ̄_τ)/(n+1)^2" where the numerator represents **aleatoric (outcome variability)** and denominator reflects **epistemic decay with evidence n=α+β accumulation**.

## 4. Exact Benchmark Results
**Planning & Mathematics (Qwen3-4B):**
- AIME24: 53.75 (+2.30 vs. Random)
- AMC23: 79.00 (+0.99)
- MATH500: 91.22 (tied)
- Average gain: +1.30

**General Reasoning (Qwen3-4B):** +0.48 average across MMLU/GPQA

## 5. Base Models Evaluated
- Qwen3-0.6B, Qwen3-1.7B, Qwen3-4B
- DeepSeek-R1-Distill-Qwen-7B

## 6. Beta Posteriors
Yes, conjugate Beta-Bernoulli framework with "temporal discounting": "α_τ^{t+1} = λα_τ^t + (1−λ)α_τ^0 + S_τ^t" (λ=1.0 default).

## 7. Comparison to CurES
Not mentioned. Compared against **MoPPS** (difficulty-only SOTA), Inverse-Evidence, Expected-Difficulty, and Dynamic Sampling baselines.

## 8. ~2.2× Acceleration Claim
Achieved on Countdown task: "up to ∼2.2x, ∼1.5x, and ∼1.6x speedups" across model scales by reaching competitive performance in fewer training steps.

## 9. Fixed Pool vs. Synthesis
**Fixed pool**: Training uses static DeepScaler (~40K math problems) and WebInstruct-verified datasets. No data synthesis described.

## 10. Key Differentiation
Difficulty-only methods ignore evidence accumulation. InSight's weighted function "w(ϕ̄_τ) = (ϕ̄_τ(1−ϕ̄_τ)) · exp(−η(ϕ̄_τ−μ)²)" uses **mean posterior beliefs rather than noisy samples**, enabling principled uncertainty quantification as training progresses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d28ec6c-bce7-4bb2-b305-ac657758110c",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "4cc13ce4-b622-4d5e-bbd3-2873202423db",
  "toolUseResult": {
    "bytes": 358028,
    "code": 200,
    "codeText": "OK",
    "result": "# InSight: Technical Details Extraction\n\n## 1. Bayesian Latent Success Rate Modeling\nInSight models each datapoint's unknown success rate **ϕ_τ^t ∈ [0,1]** using a **Beta distribution prior**: \"ϕ_τ^0 ∼ Beta(α_τ^0, β_τ^0)\" initialized to uniform Beta(1,1). Rewards follow Bernoulli(ϕ_τ^t), with posterior updates: \"ϕ_τ^t|ℋ_t ∼ Beta(α_τ^t + S_τ^t, β_τ^t + K − S_τ^t)\" where S_τ^t is success count across K rollouts.\n\n## 2. Mutual Information Objective\nThe core acquisition metric combines: **A(τ) = w(ϕ̄_τ) · I(R_{1:K}; Φ_τ)**, where mutual information captures \"expected reduction in uncertainty about Φ_τ caused by observing the reward.\" This measures epistemic exploration value independent of sampled outcomes.\n\n## 3. Decomposition Components\nExpected variance reduction decomposes as: \"Δ V(τ) = ϕ̄_τ(1−ϕ̄_τ)/(n+1)^2\" where the numerator represents **aleatoric (outcome variability)** and denominator reflects **epistemic decay with evidence n=α+β accumulation**.\n\n## 4. Exact Benchmark Results\n**Planning & Mathematics (Qwen3-4B):**\n- AIME24: 53.75 (+2.30 vs. Random)\n- AMC23: 79.00 (+0.99)\n- MATH500: 91.22 (tied)\n- Average gain: +1.30\n\n**General Reasoning (Qwen3-4B):** +0.48 average across MMLU/GPQA\n\n## 5. Base Models Evaluated\n- Qwen3-0.6B, Qwen3-1.7B, Qwen3-4B\n- DeepSeek-R1-Distill-Qwen-7B\n\n## 6. Beta Posteriors\nYes, conjugate Beta-Bernoulli framework with \"temporal discounting\": \"α_τ^{t+1} = λα_τ^t + (1−λ)α_τ^0 + S_τ^t\" (λ=1.0 default).\n\n## 7. Comparison to CurES\nNot mentioned. Compared against **MoPPS** (difficulty-only SOTA), Inverse-Evidence, Expected-Difficulty, and Dynamic Sampling baselines.\n\n## 8. ~2.2× Acceleration Claim\nAchieved on Countdown task: \"up to ∼2.2x, ∼1.5x, and ∼1.6x speedups\" across model scales by reaching competitive performance in fewer training steps.\n\n## 9. Fixed Pool vs. Synthesis\n**Fixed pool**: Training uses static DeepScaler (~40K math problems) and WebInstruct-verified datasets. No data synthesis described.\n\n## 10. Key Differentiation\nDifficulty-only methods ignore evidence accumulation. InSight's weighted function \"w(ϕ̄_τ) = (ϕ̄_τ(1−ϕ̄_τ)) · exp(−η(ϕ̄_τ−μ)²)\" uses **mean posterior beliefs rather than noisy samples**, enabling principled uncertainty quantification as training progresses.",
    "durationMs": 12347,
    "url": "https://arxiv.org/html/2603.01907"
  },
  "sourceToolAssistantUUID": "4d28ec6c-bce7-4bb2-b305-ac657758110c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T03:39:01.840Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AFjcLUyusz6S6qUaAZpkXk`</summary>

```json
{
  "query": "SEC Actor-Curator AIME 2024 3B scale comparison uniform sampling underperforms"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cc13ce4-b622-4d5e-bbd3-2873202423db",
  "isSidechain": false,
  "requestId": "req_011CbUGfFs7LVvnxB1XvpCQm",
  "type": "assistant",
  "uuid": "fb4b0009-57a7-4287-87bd-36dde4459499",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KPgk3HmBs7Gx33e5znr2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1116,
      "cache_read_input_tokens": 33744,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1116,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 33744,
          "cache_creation_input_tokens": 1116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1116
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

_source line 26 · 2026-05-28T03:39:19.704Z_

<details><summary>↩ Tool result · `toolu_01AFjcLUyusz6S6qUaAZpkXk`</summary>

```text
Web search results for query: "SEC Actor-Curator AIME 2024 3B scale comparison uniform sampling underperforms"

Links: [{"title":"AIME24: Math Reasoning Benchmark","url":"https://www.emergentmind.com/topics/aime24"},{"title":"Flexible, efficient and scalable sampling","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7543006"},{"title":"Maxwell-Jia/AIME_2024 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Maxwell-Jia/AIME_2024"},{"title":"HuggingFaceH4/aime_2024 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceH4/aime_2024"},{"title":"AIME 2024 and 2025 (part 1) - independent eval results · Issue #3 · rllm-org/rllm","url":"https://github.com/agentica-project/deepscaler/issues/3"},{"title":"AIME Benchmarks: Math & AI Evaluation","url":"https://www.emergentmind.com/topics/aime-benchmarks"},{"title":"2024 AIME I - AoPS Wiki","url":"https://artofproblemsolving.com/wiki/index.php/2024_AIME_I"},{"title":"R\\'enyi-infinity constrained sampling with $d^3$ membership queries","url":"https://arxiv.org/pdf/2407.12967"}]

The search results don't contain specific information about "SEC Actor-Curator" with AIME 2024 3B scale comparison or uniform sampling underperformance. Let me try a more targeted search:

Links: [{"title":"Explaining Off-Policy Actor-Critic From A Bias-Variance Perspective","url":"https://arxiv.org/pdf/2110.02421"},{"title":"Actor Prioritized Experience Replay","url":"https://arxiv.org/pdf/2209.00532"},{"title":"Uniform Sampling of Steady States in Metabolic Networks: Heterogeneous Scales and Rounding | PLOS One","url":"https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0122670"},{"title":"Uniform Sampling - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/computer-science/uniform-sampling"},{"title":"Reproducible scaling laws for contrastive language-image learning","url":"https://arxiv.org/html/2212.07143"},{"title":"Actor-Critics Can Achieve Optimal Sample Efficiency","url":"https://arxiv.org/pdf/2505.03710"}]

Let me try a more specific search with different terms:

Links: [{"title":"From Abstract to Contextual: What LLMs Still Cannot Do in Mathematics","url":"https://arxiv.org/pdf/2601.23048"},{"title":"AIME 2025 Benchmark: An Analysis of AI Math Reasoning","url":"https://intuitionlabs.ai/pdfs/aime-2025-benchmark-an-analysis-of-ai-math-reasoning.pdf"},{"title":"AgentMath: Empowering Mathematical Reasoning for Large Language Models via Tool-Augmented Agent","url":"https://arxiv.org/pdf/2512.20745"},{"title":"SIGMA: Search-Augmented On-Demand Knowledge Integration for Agentic Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.27568"},{"title":"rStar2-Agent: Agentic Reasoning Technical Report","url":"https://arxiv.org/pdf/2508.20722"}]

Let me try one more specific search focusing on the exact terminology:

Links: [{"title":"Active Sampling for Pairwise Comparisons via Approximate Message Passing   and Information Gain Maximization","url":"https://arxiv.org/pdf/2004.05691"},{"title":"How do you evaluate and compare the performance of different actor-critic methods?","url":"https://www.linkedin.com/advice/1/how-do-you-evaluate-compare-performance-different"},{"title":"Nested versus independent sampling: Solving the mystery of contradictory species-area relationships","url":"https://www.biorxiv.org/content/10.1101/2020.08.19.257337.full.pdf"},{"title":"Automating Model Comparison in Factor Graphs","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10453220/"},{"title":"Adaptive comparison matrix: An efficient method for psychological scaling of large stimulus sets","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7259756/"},{"title":"Sampling of actor in NeuRD · Issue #737 · google-deepmind/open_spiel","url":"https://github.com/google-deepmind/open_spiel/issues/737"}]

I've completed several web searches using various search queries related to "SEC Actor-Curator AIME 2024 3B scale comparison uniform sampling underperforms," but unfortunately, the search results do not contain information about this specific topic or research.

The searches returned results related to:
- General AIME 2024 benchmarking and mathematical reasoning for LLMs
- Actor-critic algorithms in reinforcement learning
- Sampling methods in various contexts
- General model comparison and scaling studies

However, none of these results specifically address "SEC Actor-Curator" or the particular comparison you're asking about regarding 3B scale models and uniform sampling performance on AIME 2024.

It's possible that:
1. This may be from a very recent research paper or preprint not yet widely indexed
2. The terminology or specific naming convention may be different from what appears in public search results
3. This could be from a technical report or internal documentation not widely available online

If you have access to the original source material or can provide additional context (such as author names, publication venue, or a direct link), I'd be happy to help you find more information about it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb4b0009-57a7-4287-87bd-36dde4459499",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "55b5ef89-15df-48f3-b77e-36599de708bc",
  "toolUseResult": {
    "query": "SEC Actor-Curator AIME 2024 3B scale comparison uniform sampling underperforms",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TXWrC2u3FJ59cnws4Smc4b",
        "content": [
          {
            "title": "AIME24: Math Reasoning Benchmark",
            "url": "https://www.emergentmind.com/topics/aime24"
          },
          {
            "title": "Flexible, efficient and scalable sampling",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7543006"
          },
          {
            "title": "Maxwell-Jia/AIME_2024 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/Maxwell-Jia/AIME_2024"
          },
          {
            "title": "HuggingFaceH4/aime_2024 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/HuggingFaceH4/aime_2024"
          },
          {
            "title": "AIME 2024 and 2025 (part 1) - independent eval results · Issue #3 · rllm-org/rllm",
            "url": "https://github.com/agentica-project/deepscaler/issues/3"
          },
          {
            "title": "AIME Benchmarks: Math & AI Evaluation",
            "url": "https://www.emergentmind.com/topics/aime-benchmarks"
          },
          {
            "title": "2024 AIME I - AoPS Wiki",
            "url": "https://artofproblemsolving.com/wiki/index.php/2024_AIME_I"
          },
          {
            "title": "R\\'enyi-infinity constrained sampling with $d^3$ membership queries",
            "url": "https://arxiv.org/pdf/2407.12967"
          }
        ]
      },
      "The search results don't contain specific information about \"SEC Actor-Curator\" with AIME 2024 3B scale comparison or uniform sampling underperformance. Let me try a more targeted search:",
      {
        "tool_use_id": "srvtoolu_0179EjMHTAC8sxngMRh7VPj6",
        "content": [
          {
            "title": "Explaining Off-Policy Actor-Critic From A Bias-Variance Perspective",
            "url": "https://arxiv.org/pdf/2110.02421"
          },
          {
            "title": "Actor Prioritized Experience Replay",
            "url": "https://arxiv.org/pdf/2209.00532"
          },
          {
            "title": "Uniform Sampling of Steady States in Metabolic Networks: Heterogeneous Scales and Rounding | PLOS One",
            "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0122670"
          },
          {
            "title": "Uniform Sampling - an overview | ScienceDirect Topics",
            "url": "https://www.sciencedirect.com/topics/computer-science/uniform-sampling"
          },
          {
            "title": "Reproducible scaling laws for contrastive language-image learning",
            "url": "https://arxiv.org/html/2212.07143"
          },
          {
            "title": "Actor-Critics Can Achieve Optimal Sample Efficiency",
            "url": "https://arxiv.org/pdf/2505.03710"
          }
        ]
      },
      "Let me try a more specific search with different terms:",
      {
        "tool_use_id": "srvtoolu_01BSFnACUwp1uu9oKA61tQQt",
        "content": [
          {
            "title": "From Abstract to Contextual: What LLMs Still Cannot Do in Mathematics",
            "url": "https://arxiv.org/pdf/2601.23048"
          },
          {
            "title": "AIME 2025 Benchmark: An Analysis of AI Math Reasoning",
            "url": "https://intuitionlabs.ai/pdfs/aime-2025-benchmark-an-analysis-of-ai-math-reasoning.pdf"
          },
          {
            "title": "AgentMath: Empowering Mathematical Reasoning for Large Language Models via Tool-Augmented Agent",
            "url": "https://arxiv.org/pdf/2512.20745"
          },
          {
            "title": "SIGMA: Search-Augmented On-Demand Knowledge Integration for Agentic Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2510.27568"
          },
          {
            "title": "rStar2-Agent: Agentic Reasoning Technical Report",
            "url": "https://arxiv.org/pdf/2508.20722"
          }
        ]
      },
      "Let me try one more specific search focusing on the exact terminology:",
      {
        "tool_use_id": "srvtoolu_019gKJc32KC4YmE27B467MtG",
        "content": [
          {
            "title": "Active Sampling for Pairwise Comparisons via Approximate Message Passing   and Information Gain Maximization",
            "url": "https://arxiv.org/pdf/2004.05691"
          },
          {
            "title": "How do you evaluate and compare the performance of different actor-critic methods?",
            "url": "https://www.linkedin.com/advice/1/how-do-you-evaluate-compare-performance-different"
          },
          {
            "title": "Nested versus independent sampling: Solving the mystery of contradictory species-area relationships",
            "url": "https://www.biorxiv.org/content/10.1101/2020.08.19.257337.full.pdf"
          },
          {
            "title": "Automating Model Comparison in Factor Graphs",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10453220/"
          },
          {
            "title": "Adaptive comparison matrix: An efficient method for psychological scaling of large stimulus sets",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7259756/"
          },
          {
            "title": "Sampling of actor in NeuRD · Issue #737 · google-deepmind/open_spiel",
            "url": "https://github.com/google-deepmind/open_spiel/issues/737"
          }
        ]
      },
      "I've completed several web searches using various search queries related to \"SEC Actor-Curator AIME 2024 3B scale comparison uniform sampling underperforms,\" but unfortunately, the search results do not contain information about this specific topic or research.\n\nThe searches returned results related to:\n- General AIME 2024 benchmarking and mathematical reasoning for LLMs\n- Actor-critic algorithms in reinforcement learning\n- Sampling methods in various contexts\n- General model comparison and scaling studies\n\nHowever, none of these results specifically address \"SEC Actor-Curator\" or the particular comparison you're asking about regarding 3B scale models and uniform sampling performance on AIME 2024.\n\nIt's possible that:\n1. This may be from a very recent research paper or preprint not yet widely indexed\n2. The terminology or specific naming convention may be different from what appears in public search results\n3. This could be from a technical report or internal documentation not widely available online\n\nIf you have access to the original source material or can provide additional context (such as author names, publication venue, or a direct link), I'd be happy to help you find more information about it."
    ],
    "durationSeconds": 17.85986937300001,
    "searchCount": 4
  },
  "sourceToolAssistantUUID": "fb4b0009-57a7-4287-87bd-36dde4459499",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T03:39:24.641Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gx8JFD17CGSb5Fw1kfzasJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.20532",
  "prompt": "Find the specific comparison between SEC and Actor-Curator at the 3B model scale. Look for tables showing SEC performance at 3B on AIME 2024, and specifically whether SEC underperforms uniform sampling at 3B. I need the exact numbers: SEC 3B AIME24 score, uniform 3B AIME24 score, Actor-Curator 3B AIME24 score. Also look for any discussion about why SEC fails at smaller scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55b5ef89-15df-48f3-b77e-36599de708bc",
  "isSidechain": false,
  "requestId": "req_011CbUGgpMVqrQ6JuG5xz1NJ",
  "type": "assistant",
  "uuid": "dea6e445-290e-4b98-ade5-aae4ad103674",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CkQy7Cyo56cx5zyrokdwz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 34860,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 34860,
          "cache_creation_input_tokens": 1589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1589
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

_source line 28 · 2026-05-28T03:39:29.469Z_

<details><summary>↩ Tool result · `toolu_01Gx8JFD17CGSb5Fw1kfzasJ`</summary>

```text
# SEC Performance vs Actor-Curator at 3B Scale

Based on the provided document, **Table 1 presents results exclusively for Qwen2.5-3B**, showing:

- **Uniform sampling (AIME24)**: 20.00
- **SEC (AIME24)**: 20.00
- **Actor-Curator (AIME24)**: 30.00

Notably, SEC achieves identical performance to uniform sampling on AIME24 at the 3B scale, suggesting it provides no advantage over baseline random selection on this challenging benchmark.

The document does not explicitly discuss why SEC underperforms at smaller model scales. However, the paper indicates that "Actor-Curator consistently outperforms all baselines" and notes particularly large gains on harder tasks. The results hint that SEC's heuristic approach based on absolute advantage may not effectively capture the nuanced learning dynamics necessary for complex reasoning problems, especially with constrained model capacity.

Extended results with alternative models (Llama3.2-3B-instruct) are referenced in Table 4 but not detailed in the main text excerpt provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dea6e445-290e-4b98-ade5-aae4ad103674",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "dac30197-e8e1-4e12-a616-b3c8bd38e3f0",
  "toolUseResult": {
    "bytes": 678399,
    "code": 200,
    "codeText": "OK",
    "result": "# SEC Performance vs Actor-Curator at 3B Scale\n\nBased on the provided document, **Table 1 presents results exclusively for Qwen2.5-3B**, showing:\n\n- **Uniform sampling (AIME24)**: 20.00\n- **SEC (AIME24)**: 20.00\n- **Actor-Curator (AIME24)**: 30.00\n\nNotably, SEC achieves identical performance to uniform sampling on AIME24 at the 3B scale, suggesting it provides no advantage over baseline random selection on this challenging benchmark.\n\nThe document does not explicitly discuss why SEC underperforms at smaller model scales. However, the paper indicates that \"Actor-Curator consistently outperforms all baselines\" and notes particularly large gains on harder tasks. The results hint that SEC's heuristic approach based on absolute advantage may not effectively capture the nuanced learning dynamics necessary for complex reasoning problems, especially with constrained model capacity.\n\nExtended results with alternative models (Llama3.2-3B-instruct) are referenced in Table 4 but not detailed in the main text excerpt provided.",
    "durationMs": 4824,
    "url": "https://arxiv.org/html/2602.20532"
  },
  "sourceToolAssistantUUID": "dea6e445-290e-4b98-ade5-aae4ad103674",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-28T03:39:29.474Z_

```json
{
  "parentUuid": "dac30197-e8e1-4e12-a616-b3c8bd38e3f0",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c6a7e4b8-db88-49ee-aecd-5db1a1bc8765",
  "timestamp": "2026-05-28T03:39:29.474Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-28T03:39:32.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LbYbNdrxafSG8mj4CWb62P`</summary>

```json
{
  "query": "CurES curriculum RLVR Beta posterior AIME 2024 24.58 Qwen2.5-Math-7B detailed results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6a7e4b8-db88-49ee-aecd-5db1a1bc8765",
  "isSidechain": false,
  "requestId": "req_011CbUGhY6j3NRcFt58Aeup9",
  "type": "assistant",
  "uuid": "e9b54f5f-4016-46c2-b008-36ac6cd23040",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzRBrLP4pfiTtV6Q8ek26Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 36449,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 36449,
          "cache_creation_input_tokens": 544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 544
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

_source line 31 · 2026-05-28T03:39:39.863Z_

<details><summary>↩ Tool result · `toolu_01LbYbNdrxafSG8mj4CWb62P`</summary>

```text
Web search results for query: "CurES curriculum RLVR Beta posterior AIME 2024 24.58 Qwen2.5-Math-7B detailed results"

Links: [{"title":"CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs","url":"https://arxiv.org/html/2510.01037"},{"title":"CurES: From Gradient Analysis to Efficient Curriculum ...","url":"https://www.arxiv.org/pdf/2510.01037"},{"title":"Qwen 2.5 Math 7B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen-2_5-math-7b"},{"title":"Qwen-2.5-Math-7B: Mathematical Reasoning Model","url":"https://www.emergentmind.com/topics/qwen-2-5-math-7b"},{"title":"Qwen/Qwen2.5-Math-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-7B"},{"title":"GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub","url":"https://github.com/QwenLM/Qwen2.5-Math"},{"title":"RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning","url":"https://arxiv.org/pdf/2507.07451"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=autocurriculum+RL"},{"title":"DRIVE: Data Curation Best Practices for Reinforcement Learning with Verifiable Reward in Competitive Code Generation","url":"https://arxiv.org/pdf/2511.06307"}]

Based on the search results, I found detailed information about the CurES curriculum and its performance with Qwen2.5-Math-7B. Here are the key findings:

## CurES Overview

CurES is an efficient training method that accelerates convergence and employs Bayesian posterior estimation to minimize computational overhead.

## Performance Results

Experiments demonstrate that CurES outperforms Group Relative Policy Optimization (GRPO) by +3.30 points and +4.82 points with 1.5B and 7B models, respectively, and exceeds the best prior sample efficient methods by +2.12 points on average across eight math reasoning benchmarks.

## Training Configuration

The method employs VERL as the training framework and initializes policy using Qwen2.5-Math models (1.5B and 7B parameters), utilizing Numina-Math for training data, partitioned into 15 subsets. GRPO (Shao et al., 2024) and REINFORCE++ (RPP) are employed as advantage estimators for all methods.

## RLVR Context

Reinforcement Learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for reasoning tasks of Large Language Models.

The search results show that CurES represents a significant advancement in curriculum learning for mathematical reasoning, with notable improvements over baseline methods on Qwen2.5-Math-7B when evaluated on various math benchmarks including AIME 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9b54f5f-4016-46c2-b008-36ac6cd23040",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "04a58b3d-3bcf-4943-b73c-6ae6ba66b0ed",
  "toolUseResult": {
    "query": "CurES curriculum RLVR Beta posterior AIME 2024 24.58 Qwen2.5-Math-7B detailed results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BWWucZakueVEPPqJyZnwrb",
        "content": [
          {
            "title": "CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs",
            "url": "https://arxiv.org/html/2510.01037"
          },
          {
            "title": "CurES: From Gradient Analysis to Efficient Curriculum ...",
            "url": "https://www.arxiv.org/pdf/2510.01037"
          },
          {
            "title": "Qwen 2.5 Math 7B | Open Laboratory",
            "url": "https://openlaboratory.ai/models/qwen-2_5-math-7b"
          },
          {
            "title": "Qwen-2.5-Math-7B: Mathematical Reasoning Model",
            "url": "https://www.emergentmind.com/topics/qwen-2-5-math-7b"
          },
          {
            "title": "Qwen/Qwen2.5-Math-7B · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen2.5-Math-7B"
          },
          {
            "title": "GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub",
            "url": "https://github.com/QwenLM/Qwen2.5-Math"
          },
          {
            "title": "RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2507.07451"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=autocurriculum+RL"
          },
          {
            "title": "DRIVE: Data Curation Best Practices for Reinforcement Learning with Verifiable Reward in Competitive Code Generation",
            "url": "https://arxiv.org/pdf/2511.06307"
          }
        ]
      },
      "Based on the search results, I found detailed information about the CurES curriculum and its performance with Qwen2.5-Math-7B. Here are the key findings:\n\n## CurES Overview\n\nCurES is an efficient training method that accelerates convergence and employs Bayesian posterior estimation to minimize computational overhead.\n\n## Performance Results\n\nExperiments demonstrate that CurES outperforms Group Relative Policy Optimization (GRPO) by +3.30 points and +4.82 points with 1.5B and 7B models, respectively, and exceeds the best prior sample efficient methods by +2.12 points on average across eight math reasoning benchmarks.\n\n## Training Configuration\n\nThe method employs VERL as the training framework and initializes policy using Qwen2.5-Math models (1.5B and 7B parameters), utilizing Numina-Math for training data, partitioned into 15 subsets. GRPO (Shao et al., 2024) and REINFORCE++ (RPP) are employed as advantage estimators for all methods.\n\n## RLVR Context\n\nReinforcement Learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for reasoning tasks of Large Language Models.\n\nThe search results show that CurES represents a significant advancement in curriculum learning for mathematical reasoning, with notable improvements over baseline methods on Qwen2.5-Math-7B when evaluated on various math benchmarks including AIME 2024."
    ],
    "durationSeconds": 7.4462820739999875,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e9b54f5f-4016-46c2-b008-36ac6cd23040",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-28T03:39:45.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Giedqcww922uY46wWohiU2`</summary>

```json
{
  "query": "\"CurES\" \"optimal sampling\" \"p(1-p)\" \"rollout allocation\" gradient variance RLVR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04a58b3d-3bcf-4943-b73c-6ae6ba66b0ed",
  "isSidechain": false,
  "requestId": "req_011CbUGiJVCLg6NPqURyPNZF",
  "type": "assistant",
  "uuid": "52122c8e-112a-4bb0-832e-959ea562b193",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfXgBf3VvS1X2LqF95YgHm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 36993,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 36993,
          "cache_creation_input_tokens": 911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 911
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
  "leafUuid": "52122c8e-112a-4bb0-832e-959ea562b193",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise RLVR archive approach for CurES acknowledgment",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Tool result

_source line 35 · 2026-05-28T03:39:52.322Z_

<details><summary>↩ Tool result · `toolu_01Giedqcww922uY46wWohiU2`</summary>

```text
Web search results for query: ""CurES" "optimal sampling" "p(1-p)" "rollout allocation" gradient variance RLVR 2026"

Links: [{"title":"Preprint, Work in Progress CURES: FROM GRADIENT ANALYSIS TO EFFICIENT","url":"https://www.arxiv.org/pdf/2510.01037"},{"title":"Published as a conference paper at ICLR 2026 ADAPTIVE ROLLOUT ALLOCATION FOR","url":"https://openreview.net/pdf/6ee2f705eef5b4d7169297beb7748db19ab85413.pdf"},{"title":"CURES:FROM GRADIENT ANALYSIS TO EFFICIENT ...","url":"https://openreview.net/pdf/41b6c16003459422965bfdffce5d80e9f6e3e87e.pdf"},{"title":"CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs","url":"https://arxiv.org/html/2510.01037v1"},{"title":"adaptive rollout allocation for online re","url":"https://arxiv.org/pdf/2602.01601"},{"title":"Improving Sampling Efficiency in RLVR through Adaptive ...","url":"https://arxiv.org/pdf/2509.25808"},{"title":"Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse","url":"https://arxiv.org/html/2509.25808v1"},{"title":"LLM RLVR: Optimizing with Verifiable Rewards","url":"https://www.emergentmind.com/topics/llm-rlvr"}]

Based on the search results, I found relevant information about your query:

## CurES Overview

CurES is a theoretically grounded curriculum learning algorithm for RLVR that adaptively prioritizes training prompts of optimal difficulty and dynamically allocates rollout budgets by linking gradient efficiency to accuracy.

## Key Technical Components

**Bayesian Framework**: The algorithmic design leverages a Bayesian framework to track prompt difficulty in a lightweight yet adaptive manner, specifically modeling the success rate of each prompt instance with a Beta distribution, which naturally incorporates prior information and posterior updates as new rollouts are observed.

**Sampling and Allocation**: Combined with the derived sampling distribution and variance-based rollout quantity allocation, this Bayesian mechanism ensures that both question selection and sample budgeting adapt dynamically to the evolving policy.

## Gradient Variance Analysis

The work addresses a critical issue in RLVR: analyzing the variance of the gradient estimator arising from sampling rollouts in RLVR algorithms such as GRPO and RLOO. This variance analysis directly connects to the optimal rollout allocation strategy used in CurES.

The search results indicate this is a recent advancement in RLVR (Reinforcement Learning with Verifiable Reward) research, focusing on improving training efficiency for reasoning-focused large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52122c8e-112a-4bb0-832e-959ea562b193",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "5f7862b4-3469-4bb8-b0ba-1f0b04579a78",
  "toolUseResult": {
    "query": "\"CurES\" \"optimal sampling\" \"p(1-p)\" \"rollout allocation\" gradient variance RLVR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FFJj7yQFTHcUjPVKkkfCYh",
        "content": [
          {
            "title": "Preprint, Work in Progress CURES: FROM GRADIENT ANALYSIS TO EFFICIENT",
            "url": "https://www.arxiv.org/pdf/2510.01037"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 ADAPTIVE ROLLOUT ALLOCATION FOR",
            "url": "https://openreview.net/pdf/6ee2f705eef5b4d7169297beb7748db19ab85413.pdf"
          },
          {
            "title": "CURES:FROM GRADIENT ANALYSIS TO EFFICIENT ...",
            "url": "https://openreview.net/pdf/41b6c16003459422965bfdffce5d80e9f6e3e87e.pdf"
          },
          {
            "title": "CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs",
            "url": "https://arxiv.org/html/2510.01037v1"
          },
          {
            "title": "adaptive rollout allocation for online re",
            "url": "https://arxiv.org/pdf/2602.01601"
          },
          {
            "title": "Improving Sampling Efficiency in RLVR through Adaptive ...",
            "url": "https://arxiv.org/pdf/2509.25808"
          },
          {
            "title": "Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse",
            "url": "https://arxiv.org/html/2509.25808v1"
          },
          {
            "title": "LLM RLVR: Optimizing with Verifiable Rewards",
            "url": "https://www.emergentmind.com/topics/llm-rlvr"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\n## CurES Overview\n\nCurES is a theoretically grounded curriculum learning algorithm for RLVR that adaptively prioritizes training prompts of optimal difficulty and dynamically allocates rollout budgets by linking gradient efficiency to accuracy.\n\n## Key Technical Components\n\n**Bayesian Framework**: The algorithmic design leverages a Bayesian framework to track prompt difficulty in a lightweight yet adaptive manner, specifically modeling the success rate of each prompt instance with a Beta distribution, which naturally incorporates prior information and posterior updates as new rollouts are observed.\n\n**Sampling and Allocation**: Combined with the derived sampling distribution and variance-based rollout quantity allocation, this Bayesian mechanism ensures that both question selection and sample budgeting adapt dynamically to the evolving policy.\n\n## Gradient Variance Analysis\n\nThe work addresses a critical issue in RLVR: analyzing the variance of the gradient estimator arising from sampling rollouts in RLVR algorithms such as GRPO and RLOO. This variance analysis directly connects to the optimal rollout allocation strategy used in CurES.\n\nThe search results indicate this is a recent advancement in RLVR (Reinforcement Learning with Verifiable Reward) research, focusing on improving training efficiency for reasoning-focused large language models."
    ],
    "durationSeconds": 6.866660891999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "52122c8e-112a-4bb0-832e-959ea562b193",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-28T03:39:54.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015vgaqHMYARFnM15TdjPmfC`</summary>

```json
{
  "query": "SEC AIME 2024 Qwen2.5-3B 20% uniform sampling category bandit underperform"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f7862b4-3469-4bb8-b0ba-1f0b04579a78",
  "isSidechain": false,
  "requestId": "req_011CbUGjDnCurJnkCiustbDe",
  "type": "assistant",
  "uuid": "c6f0e2de-dd6a-414d-9265-f16a2a10ce52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZnawukuYfdHWhUhZhL1wb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 37904,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 37904,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
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

_source line 37 · 2026-05-28T03:40:00.750Z_

<details><summary>↩ Tool result · `toolu_015vgaqHMYARFnM15TdjPmfC`</summary>

```text
Web search results for query: "SEC AIME 2024 Qwen2.5-3B 20% uniform sampling category bandit underperform"

Links: [{"title":"Qwen/Qwen2.5-3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-3B-Instruct"},{"title":"On Universally Optimal Algorithms for A/B Testing","url":"https://arxiv.org/pdf/2308.12000"},{"title":"Stochastic Optimization with Bandit Sampling","url":"https://arxiv.org/pdf/1708.02544"},{"title":"An Asymptotically Optimal Policy for Uniform Bandits of Unknown Support","url":"https://arxiv.org/pdf/1505.01918"},{"title":"Multi-Agent Thompson Sampling for Bandit Applications with Sparse Neighbourhood Structures","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7174305/"},{"title":"Asymptotically Optimal Sequential Experimentation Under Generalized   Ranking","url":"https://arxiv.org/pdf/1510.02041"}]

The search results don't contain information specifically about SEC AIME 2024 (Secondary Mathematical Olympiad) with Qwen2.5-3B performance metrics, uniform sampling, category bandits, or underperformance comparisons. 

The results returned academic papers about multi-armed bandits and sampling strategies in general optimization contexts, as well as information about the Qwen2.5 model itself, but nothing matching the specific technical evaluation you're asking about.

This appears to be a very specific technical evaluation or benchmark result that may not be widely indexed on the web, or it could be referring to an internal evaluation, recent technical report, or specialized benchmark that hasn't been published in accessible web sources yet. You might want to try:

1. Checking arXiv directly for recent papers on Qwen2.5 evaluations
2. Looking at Qwen's official GitHub repositories or documentation
3. Searching for specific research papers or benchmarks that include this comparison

Is there a more specific source or publication you're looking for?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6f0e2de-dd6a-414d-9265-f16a2a10ce52",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "e37f1411-338c-4903-b0ee-d9da7cfcd042",
  "toolUseResult": {
    "query": "SEC AIME 2024 Qwen2.5-3B 20% uniform sampling category bandit underperform",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P8zZPNjz51TaFQXUjGLMN6",
        "content": [
          {
            "title": "Qwen/Qwen2.5-3B-Instruct · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen2.5-3B-Instruct"
          },
          {
            "title": "On Universally Optimal Algorithms for A/B Testing",
            "url": "https://arxiv.org/pdf/2308.12000"
          },
          {
            "title": "Stochastic Optimization with Bandit Sampling",
            "url": "https://arxiv.org/pdf/1708.02544"
          },
          {
            "title": "An Asymptotically Optimal Policy for Uniform Bandits of Unknown Support",
            "url": "https://arxiv.org/pdf/1505.01918"
          },
          {
            "title": "Multi-Agent Thompson Sampling for Bandit Applications with Sparse Neighbourhood Structures",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7174305/"
          },
          {
            "title": "Asymptotically Optimal Sequential Experimentation Under Generalized   Ranking",
            "url": "https://arxiv.org/pdf/1510.02041"
          }
        ]
      },
      "The search results don't contain information specifically about SEC AIME 2024 (Secondary Mathematical Olympiad) with Qwen2.5-3B performance metrics, uniform sampling, category bandits, or underperformance comparisons. \n\nThe results returned academic papers about multi-armed bandits and sampling strategies in general optimization contexts, as well as information about the Qwen2.5 model itself, but nothing matching the specific technical evaluation you're asking about.\n\nThis appears to be a very specific technical evaluation or benchmark result that may not be widely indexed on the web, or it could be referring to an internal evaluation, recent technical report, or specialized benchmark that hasn't been published in accessible web sources yet. You might want to try:\n\n1. Checking arXiv directly for recent papers on Qwen2.5 evaluations\n2. Looking at Qwen's official GitHub repositories or documentation\n3. Searching for specific research papers or benchmarks that include this comparison\n\nIs there a more specific source or publication you're looking for?"
    ],
    "durationSeconds": 5.908028053000017,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c6f0e2de-dd6a-414d-9265-f16a2a10ce52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-28T03:40:28.246Z_

<details><summary>Logged reasoning block</summary>

```text
I now have enough information about CurES and InSight. Let me also verify the SEC 3B data point from the Actor-Curator paper. The WebFetch already confirmed:
- Uniform sampling (AIME24) at 3B: 20.00
- SEC (AIME24) at 3B: 20.00
- Actor-Curator (AIME24) at 3B: 30.00

Actually wait - the reviewer said SEC underperforms uniform at 3B (20.0% vs 23.33%). But the Actor-Curator paper table shows Uniform=20.00 and SEC=20.00. 

There's a discrepancy here - the reviewer claims uniform sampling achieves 23.33% at 3B, but my data shows 20.00%. Let me trace back to the original source to see if there's a different metric or configuration being used, since the Actor-Curator paper clearly states Qwen2.5-3B reaches 30.0% with their method. I'm noticing the reviewer's claim about SEC underperforming uniform sampling doesn't match what I found in the paper's Table 1, where both showed 20.0% on AIME24. The "+28.6% relative" figure seems to refer to the overall average rather than AIME24 specifically, so there might be different metrics or tables at play here. Let me verify the exact numbers from the Actor-Curator paper before drawing conclusions about the comparison. The discrepancy might stem from different experimental setups across tables, so I should verify the paper directly rather than relying on potentially conflicting numbers from different sources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e37f1411-338c-4903-b0ee-d9da7cfcd042",
  "isSidechain": false,
  "requestId": "req_011CbUGjqmumVgy1fxeFBtBs",
  "type": "assistant",
  "uuid": "b283373c-6fad-43e4-af7d-26e2994c721e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiVtpvWovb3nXSTNpKPebo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 38714,
      "output_tokens": 1204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1204,
          "cache_read_input_tokens": 38714,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
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

_source line 39 · 2026-05-28T03:40:30.088Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018cJsfpBbwabSPk121fwDej`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.20532",
  "prompt": "Find ALL tables in this paper. I need the exact AIME 2024 numbers for Qwen2.5-3B across all methods. Specifically: 1) What is the uniform baseline AIME24 score at 3B? 2) What is SEC's AIME24 score at 3B? 3) Does SEC underperform uniform on AIME24 at 3B? 4) What is Actor-Curator's AIME24 score at 3B? Look at ALL tables including supplementary ones. Report exact numbers from each table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b283373c-6fad-43e4-af7d-26e2994c721e",
  "isSidechain": false,
  "requestId": "req_011CbUGjqmumVgy1fxeFBtBs",
  "type": "assistant",
  "uuid": "e6ae2c45-d326-4f64-9a5b-1dcbd370d465",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiVtpvWovb3nXSTNpKPebo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 38714,
      "output_tokens": 1204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1204,
          "cache_read_input_tokens": 38714,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
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

_source line 40 · 2026-05-28T03:40:33.927Z_

<details><summary>↩ Tool result · `toolu_018cJsfpBbwabSPk121fwDej`</summary>

```text
Based on the provided content, I can find AIME24 results for Qwen2.5-3B in **Table 1** only:

**Table 1 - AIME24 Results (Qwen2.5-3B):**

1. **Uniform baseline**: 20.00
2. **SEC**: 23.33
3. **Does SEC underperform uniform?** No. SEC matches the PCL baseline at 23.33, outperforming uniform's 20.00
4. **Actor-Curator**: 30.00

The paper states Actor-Curator achieves "+6.67 +28.57%" improvement, meaning 6.67 absolute points and 28.57% relative gain over the 23.33 baseline (SEC/PCL).

I reviewed the entire document and only Table 1 contains explicit AIME24 numerical results for this model size. The supplementary materials referenced (Appendix J) are mentioned but their full content isn't provided in the excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6ae2c45-d326-4f64-9a5b-1dcbd370d465",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "a6d91d13-a133-4710-86af-674f26a0665d",
  "toolUseResult": {
    "bytes": 678399,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided content, I can find AIME24 results for Qwen2.5-3B in **Table 1** only:\n\n**Table 1 - AIME24 Results (Qwen2.5-3B):**\n\n1. **Uniform baseline**: 20.00\n2. **SEC**: 23.33\n3. **Does SEC underperform uniform?** No. SEC matches the PCL baseline at 23.33, outperforming uniform's 20.00\n4. **Actor-Curator**: 30.00\n\nThe paper states Actor-Curator achieves \"+6.67 +28.57%\" improvement, meaning 6.67 absolute points and 28.57% relative gain over the 23.33 baseline (SEC/PCL).\n\nI reviewed the entire document and only Table 1 contains explicit AIME24 numerical results for this model size. The supplementary materials referenced (Appendix J) are mentioned but their full content isn't provided in the excerpt.",
    "durationMs": 3834,
    "url": "https://arxiv.org/html/2602.20532"
  },
  "sourceToolAssistantUUID": "e6ae2c45-d326-4f64-9a5b-1dcbd370d465",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-28T03:41:23.631Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting - so from the Actor-Curator paper Table 1:
- Uniform AIME24 3B: 20.00
- SEC AIME24 3B: 23.33
- Actor-Curator AIME24 3B: 30.00

So SEC actually outperforms uniform (23.33 > 20.00), not underperforms. The reviewer was wrong about this specific claim! The "+28.57% relative" is relative to SEC/PCL baseline of 23.33.

Wait, but the reviewer said "SEC (20.0%) actually UNDERPERFORMS uniform sampling (23.33%)". 

That's backwards from what the table shows. SEC beats uniform by a clear margin - 23.33 versus 20.00. The reviewer definitely confused the numbers here. The reviewer's numbers appear to be reversed—looking at the actual table data, uniform is 20.0% and SEC is 23.33%, so SEC actually outperforms uniform, not the other way around. I should address this diplomatically in my response, noting the correct performance gap while acknowledging the broader point about diminishing returns as complexity increases.

Now I need to revise the paper with several key updates: adding CurES and InSight to the related work landscape, reframing Core 3 as an established technique applied to a novel problem rather than claiming novel posteriors, and removing the ICLR 2027 stretch target. The critical distinction is that CurES uses Beta posteriors for sampling from a fixed pool, while Core 3 applies them to the archive replacement decision problem—these are meaningfully different applications.

Constructing the revised JSON... SACE-RLVR achieves zero additional cost by reusing the same 16 training rollouts and operates with an evolving archive rather than a fixed pool. For InSight, I'm looking at how it combines Beta posteriors with mutual information decomposition to separate difficulty-dependent uncertainty from evidence-dependent uncertainty, achieving 2.2× training acceleration on Countdown and 53.75% on AIME24 with Qwen3-4B, though it uses a fixed pool from DeepScaler with temporal discounting applied to the Beta parameters. The key distinction for Core 3 is that we're not introducing Beta-Bernoulli estimation itself—that's CurES's contribution—but rather applying the established approach specifically for replacement decisions in the archive.

The actual novelty lies in three places: using credible intervals instead of point estimates for deciding which problems to replace, achieving zero inference overhead through rollout reuse, and applying this to archive management rather than sampling or gradient estimation. Looking at the SEC 3B data from Actor-Curator's Table 1, SEC reaches 23.33% on AIME24 compared to uniform's 20%, a modest 3.33 percentage point gain, whereas Actor-Curator achieves 30%—so while SEC does improve over uniform, the gap is much smaller than what the per-problem approach delivers.

The reviewer's recommendation to highlight this data point is worth taking seriously, even though their specific numbers appear reversed. I can note the correct figures while still making the substantive point about bandits' limitations: at 3B scale, category-level methods like SEC show diminishing returns compared to fine-grained per-problem selection, especially as problems get harder.

For the revision itself, I'm focusing on five key updates: incorporating CurES and InSight into the related work landscape, reframing how I present Core 3's novelty, using the accurate SEC numbers to strengthen the differentiation argument, adjusting the venue timeline to prioritize ICML 2027 with NeurIPS 2027 as backup, and updating any downstream sections that reference these changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d91d13-a133-4710-86af-674f26a0665d",
  "isSidechain": false,
  "requestId": "req_011CbUGnHhgameR6EUsJTTuv",
  "type": "assistant",
  "uuid": "cd6984f1-56ba-45c7-91e0-5ff6ca7cf0d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017REAY4MhUbpaDiaDxJ5W6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 39343,
      "output_tokens": 2108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2108,
          "cache_read_input_tokens": 39343,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1446
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

_source line 42 · 2026-05-28T03:41:23.816Z_

Now I have thorough research on all the key papers. Let me verify one more data point about CurES's publication status:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd6984f1-56ba-45c7-91e0-5ff6ca7cf0d5",
  "isSidechain": false,
  "requestId": "req_011CbUGnHhgameR6EUsJTTuv",
  "type": "assistant",
  "uuid": "0f4c94b7-c479-4ae6-9f70-e5dee830e2d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017REAY4MhUbpaDiaDxJ5W6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 39343,
      "output_tokens": 2108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2108,
          "cache_read_input_tokens": 39343,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1446
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

_source line 43 · 2026-05-28T03:41:24.386Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WqEB4gFueUVHodLpVD8Ttc`</summary>

```json
{
  "query": "CurES arXiv 2510.01037 ICLR 2026 accepted openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f4c94b7-c479-4ae6-9f70-e5dee830e2d4",
  "isSidechain": false,
  "requestId": "req_011CbUGnHhgameR6EUsJTTuv",
  "type": "assistant",
  "uuid": "b5f29955-03aa-415f-9891-4c153ecaf54c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017REAY4MhUbpaDiaDxJ5W6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 39343,
      "output_tokens": 2108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2108,
          "cache_read_input_tokens": 39343,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1446
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "b5f29955-03aa-415f-9891-4c153ecaf54c",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise RLVR archive approach for CurES acknowledgment",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Tool result

_source line 46 · 2026-05-28T03:41:31.311Z_

<details><summary>↩ Tool result · `toolu_01WqEB4gFueUVHodLpVD8Ttc`</summary>

```text
Web search results for query: "CurES arXiv 2510.01037 ICLR 2026 accepted openreview"

Links: [{"title":"[2510.01037] CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs","url":"https://arxiv.org/abs/2510.01037"},{"title":"CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs","url":"https://arxiv.org/html/2510.01037"},{"title":"Preprint, Work in Progress CURES: FROM GRADIENT ANALYSIS TO EFFICIENT","url":"https://www.arxiv.org/pdf/2510.01037"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"The dynamic interplay between in-context and in-weight learning in humans and neural networks","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10896373/"},{"title":"Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"},{"title":"Demonstrations, CoT, and Prompting: A Theoretical Analysis of ICL","url":"https://arxiv.org/pdf/2603.19611"},{"title":"Vision-Language Models vs Autonomous AI Agents for Anterior Capsular Radial Folds: A Diagnostic Study","url":"https://www.medrxiv.org/content/10.64898/2026.01.15.26344200.full.pdf"}]

Based on the search results, I found information about the CurES paper with arXiv ID 2510.01037:

CurES is a paper titled "From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs" that focuses on how curriculum learning plays a crucial role in enhancing the training efficiency of large language models on reasoning tasks.

The paper approaches the problem from the perspective of reinforcement learning gradient optimization, identifying two key factors influencing training efficiency: the selection of training prompts and the allocation of rollout quantities across different prompts. The theoretical analysis reveals that the sampling distribution of prompts dictates the convergence rate of gradient descent, while the allocation of the rollout quantity influences the consistency and stability of overall gradient updates.

The paper was submitted on October 1, 2025 and last revised on March 23, 2026, with authors including Yongcheng Zeng, Zexu Sun, Bokai Ji, and others from institutions including the Chinese Academy of Sciences, Baidu Inc., University College London, and Renmin University of China.

However, the search results do not contain specific information about whether this paper was accepted to ICLR 2026 or its OpenReview status. To get that information, you may want to check the OpenReview website directly or the ICLR 2026 conference page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5f29955-03aa-415f-9891-4c153ecaf54c",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "897f9cbe-8e87-4a03-8a83-534a92a73b4b",
  "toolUseResult": {
    "query": "CurES arXiv 2510.01037 ICLR 2026 accepted openreview",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UtN1raoM3iGh6p92L5BMsc",
        "content": [
          {
            "title": "[2510.01037] CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs",
            "url": "https://arxiv.org/abs/2510.01037"
          },
          {
            "title": "CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs",
            "url": "https://arxiv.org/html/2510.01037"
          },
          {
            "title": "Preprint, Work in Progress CURES: FROM GRADIENT ANALYSIS TO EFFICIENT",
            "url": "https://www.arxiv.org/pdf/2510.01037"
          },
          {
            "title": "ICLR 2026 Call for Papers",
            "url": "https://iclr.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "The dynamic interplay between in-context and in-weight learning in humans and neural networks",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10896373/"
          },
          {
            "title": "Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews",
            "url": "https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"
          },
          {
            "title": "Demonstrations, CoT, and Prompting: A Theoretical Analysis of ICL",
            "url": "https://arxiv.org/pdf/2603.19611"
          },
          {
            "title": "Vision-Language Models vs Autonomous AI Agents for Anterior Capsular Radial Folds: A Diagnostic Study",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.15.26344200.full.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the CurES paper with arXiv ID 2510.01037:\n\nCurES is a paper titled \"From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs\" that focuses on how curriculum learning plays a crucial role in enhancing the training efficiency of large language models on reasoning tasks.\n\nThe paper approaches the problem from the perspective of reinforcement learning gradient optimization, identifying two key factors influencing training efficiency: the selection of training prompts and the allocation of rollout quantities across different prompts. The theoretical analysis reveals that the sampling distribution of prompts dictates the convergence rate of gradient descent, while the allocation of the rollout quantity influences the consistency and stability of overall gradient updates.\n\nThe paper was submitted on October 1, 2025 and last revised on March 23, 2026, with authors including Yongcheng Zeng, Zexu Sun, Bokai Ji, and others from institutions including the Chinese Academy of Sciences, Baidu Inc., University College London, and Renmin University of China.\n\nHowever, the search results do not contain specific information about whether this paper was accepted to ICLR 2026 or its OpenReview status. To get that information, you may want to check the OpenReview website directly or the ICLR 2026 conference page."
    ],
    "durationSeconds": 6.9194411629999815,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b5f29955-03aa-415f-9891-4c153ecaf54c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-28T03:41:38.545Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UvKPk9kWHsG4ragZUL4dRz`</summary>

```json
{
  "url": "https://openreview.net/pdf/41b6c16003459422965bfdffce5d80e9f6e3e87e.pdf",
  "prompt": "What venue/conference is this paper submitted to or published at? Is it ICLR 2026? Look for any header, watermark, or venue indication. Also extract any additional technical details about CurES not found in the arXiv version - specifically about rollout reuse, Beta prior initialization, and comparison to other Bayesian methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "897f9cbe-8e87-4a03-8a83-534a92a73b4b",
  "isSidechain": false,
  "requestId": "req_011CbUGrXE8m7LLUUfvLa94H",
  "type": "assistant",
  "uuid": "e9e5e72b-d000-481f-a408-88e4d28fcd46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vv1Uqb6Gooe4uTMR8DXcU7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2857,
      "cache_read_input_tokens": 40789,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 40789,
          "cache_creation_input_tokens": 2857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2857
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

_source line 48 · 2026-05-28T03:41:38.922Z_

<details><summary>↩ Tool result · `toolu_01UvKPk9kWHsG4ragZUL4dRz`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9e5e72b-d000-481f-a408-88e4d28fcd46",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "8784a6d2-0f4f-4c54-ab64-68a5e90c4faa",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 374,
    "url": "https://openreview.net/pdf/41b6c16003459422965bfdffce5d80e9f6e3e87e.pdf"
  },
  "sourceToolAssistantUUID": "e9e5e72b-d000-481f-a408-88e4d28fcd46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-28T03:41:41.592Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Enzk8rBbSzSzwm9pzWmMhQ`</summary>

```json
{
  "query": "InSight \"2603.01907\" Bayesian RLVR weighted mutual information data selection training acceleration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8784a6d2-0f4f-4c54-ab64-68a5e90c4faa",
  "isSidechain": false,
  "requestId": "req_011CbUGs5XLswLuPuZfi6ixD",
  "type": "assistant",
  "uuid": "c73c3b70-a838-41e2-aea4-e9fe2606ce98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Wr8V6ajiA6PSiJ4HtWRPU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 43646,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 43646,
          "cache_creation_input_tokens": 243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 243
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

_source line 50 · 2026-05-28T03:41:49.502Z_

<details><summary>↩ Tool result · `toolu_01Enzk8rBbSzSzwm9pzWmMhQ`</summary>

```text
Web search results for query: "InSight "2603.01907" Bayesian RLVR weighted mutual information data selection training acceleration"

Links: [{"title":"[2603.01907] Efficient RLVR Training via Weighted Mutual Information Data Selection","url":"https://arxiv.org/abs/2603.01907"},{"title":"Paper page - Efficient RLVR Training via Weighted Mutual Information Data Selection","url":"https://huggingface.co/papers/2603.01907"},{"title":"Efficient RLVR Training via Weighted Mutual Information Data Selection","url":"https://arxiv.org/html/2603.01907"},{"title":"Data-Efficient RLVR via Off-Policy Influence Guidance","url":"https://arxiv.org/pdf/2510.26491"},{"title":"Towards Accelerated Model Training via Bayesian Data Selection","url":"https://arxiv.org/pdf/2308.10544"},{"title":"Robust Feature Selection by Mutual Information Distributions","url":"https://arxiv.org/pdf/cs/0206006"}]

Based on the search results, I found the paper you're looking for:

## InSight: Efficient RLVR Training via Weighted Mutual Information Data Selection

InSight is an INformation-guided data SamplInG metHod for RL Training, grounded in a weighted mutual information objective.

**Key Technical Approach:**

By modeling data outcomes with Bayesian latent success rates, the method shows that expected uncertainty reduction decomposes into complementary difficulty- and evidence-dependent components, revealing a fundamental limitation of difficulty-only selection. InSight constructs a stable acquisition score based on the mean belief of datapoints' success rather than noisy sampled outcomes, and naturally extends to multi-rollout settings common in reinforcement learning with verifiable rewards (RLVR).

**Performance Results:**

Extensive experiments demonstrate up to ~2.2x acceleration, with negligible additional computational overhead.

**Context:**

Reinforcement learning plays a central role in improving the reasoning and alignment of large language models, yet its efficiency critically depends on how training data are selected. Existing online selection strategies predominantly rely on difficulty-based heuristics, favouring datapoints with intermediate success rates, implicitly equating difficulty with informativeness and neglecting epistemic uncertainty arising from limited evidence.

The paper was published on March 2, 2026 (arXiv:2603.01907).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c73c3b70-a838-41e2-aea4-e9fe2606ce98",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "69af2cca-e353-4a03-a6e5-db1c16ae6ca5",
  "toolUseResult": {
    "query": "InSight \"2603.01907\" Bayesian RLVR weighted mutual information data selection training acceleration",
    "results": [
      {
        "tool_use_id": "srvtoolu_018sTRmE2aGja761QV4fCMv4",
        "content": [
          {
            "title": "[2603.01907] Efficient RLVR Training via Weighted Mutual Information Data Selection",
            "url": "https://arxiv.org/abs/2603.01907"
          },
          {
            "title": "Paper page - Efficient RLVR Training via Weighted Mutual Information Data Selection",
            "url": "https://huggingface.co/papers/2603.01907"
          },
          {
            "title": "Efficient RLVR Training via Weighted Mutual Information Data Selection",
            "url": "https://arxiv.org/html/2603.01907"
          },
          {
            "title": "Data-Efficient RLVR via Off-Policy Influence Guidance",
            "url": "https://arxiv.org/pdf/2510.26491"
          },
          {
            "title": "Towards Accelerated Model Training via Bayesian Data Selection",
            "url": "https://arxiv.org/pdf/2308.10544"
          },
          {
            "title": "Robust Feature Selection by Mutual Information Distributions",
            "url": "https://arxiv.org/pdf/cs/0206006"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## InSight: Efficient RLVR Training via Weighted Mutual Information Data Selection\n\nInSight is an INformation-guided data SamplInG metHod for RL Training, grounded in a weighted mutual information objective.\n\n**Key Technical Approach:**\n\nBy modeling data outcomes with Bayesian latent success rates, the method shows that expected uncertainty reduction decomposes into complementary difficulty- and evidence-dependent components, revealing a fundamental limitation of difficulty-only selection. InSight constructs a stable acquisition score based on the mean belief of datapoints' success rather than noisy sampled outcomes, and naturally extends to multi-rollout settings common in reinforcement learning with verifiable rewards (RLVR).\n\n**Performance Results:**\n\nExtensive experiments demonstrate up to ~2.2x acceleration, with negligible additional computational overhead.\n\n**Context:**\n\nReinforcement learning plays a central role in improving the reasoning and alignment of large language models, yet its efficiency critically depends on how training data are selected. Existing online selection strategies predominantly rely on difficulty-based heuristics, favouring datapoints with intermediate success rates, implicitly equating difficulty with informativeness and neglecting epistemic uncertainty arising from limited evidence.\n\nThe paper was published on March 2, 2026 (arXiv:2603.01907)."
    ],
    "durationSeconds": 7.904990634999965,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c73c3b70-a838-41e2-aea4-e9fe2606ce98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-28T03:42:09.814Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me carefully construct the revised JSON. Here's my plan:

1. **CurES** - Add as a major landscape entry with detailed differentiation
2. **InSight** - Add as a related work
3. **Reframe Core 3** - From "novel" to "established technique, novel application"
4. **SEC 3B data** - Use the CORRECT data (SEC 23.33 > Uniform 20.00, not the reviewer's incorrect claim)
5. **Venue timeline** - Remove ICLR 2027


6. **CurES technical details** - Bayesian posterior updates with Beta distributions, optimal sampling based on entropy, point estimates from Beta means. Qwen2.5-Math-7B achieves 24.58% on AIME24 and 84.80% on MATH-500 using a fixed pool from Numina-Math with 15 partitions and VERL framework, with versions released October 2025 and March 2026.
7. **InSight approach** - Combines Beta posteriors with mutual information decomposition and temporal discounting, achieving 53.75% on AIME24.
8. **Qwen3-4B results** - Shows up to 2.2× speedup with a fixed pool from DeepScaler (~40K examples).
9. **SEC baseline comparison** - At 3B parameters, SEC reaches 23.33% on AIME24 (not the 20.0% the reviewer cited), while uniform sampling gets 20.00% and Actor-Curator achieves 30.00%.

Now I'm refocusing the paper's framing—this is a "minor" change where I'm adding these missing works and repositioning our contribution. The core insight is that while Bayesian estimation itself is well-established, our innovation lies in how we apply it to this specific problem. I need to update the core problem statement to situate CurES and InSight within the Bayesian estimation context, reframe the opportunity to emphasize our novel application, expand the landscape section with these new entries, and adjust how I present Core 3 to reflect this positioning.

I should also remove ICLR 2027 from the target venues and make sure the reviewer response documents all these changes comprehensively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69af2cca-e353-4a03-a6e5-db1c16ae6ca5",
  "isSidechain": false,
  "requestId": "req_011CbUGsrmQdgTLDB2RADSo1",
  "type": "assistant",
  "uuid": "bec1e75f-1e11-46db-b53a-630c572a4fb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m71C6wfAEZb8D7zLh8LkB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 43889,
      "output_tokens": 9009,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9009,
          "cache_read_input_tokens": 43889,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 52 · 2026-05-28T03:42:11.987Z_

Now I have comprehensive research on all critical papers. Let me synthesize the findings and construct the complete revision.

Key research findings:
- **CurES**: Beta(α,β) posteriors with point estimates (Beta mean), optimal sampling ∝ exp(√[p(1-p)]/τ), fixed pool (Numina-Math), AIME24 24.58% on Qwen2.5-Math-7B, +4.82 over GRPO
- **InSight**: Beta posteriors + mutual information decomposition into difficulty + evidence components, ~2.2× acceleration, AIME24 53.75 on Qwen3-4B
- **SEC 3B correction**: Actor-Curator Table 1 shows Uniform=20.00, SEC=23.33, Actor-Curator=30.00 — SEC actually outperforms uniform at 3B (reviewer's claim was inverted)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bec1e75f-1e11-46db-b53a-630c572a4fb5",
  "isSidechain": false,
  "requestId": "req_011CbUGsrmQdgTLDB2RADSo1",
  "type": "assistant",
  "uuid": "a1d73344-1e00-4bc5-a8b5-764667ee30bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m71C6wfAEZb8D7zLh8LkB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 43889,
      "output_tokens": 9009,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9009,
          "cache_read_input_tokens": 43889,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 53 · 2026-05-28T03:45:54.839Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014yMsoZy9eQUQx63cXtQnrP`</summary>

````json
{
  "description": "Construct complete revised JSON",
  "prompt": "You are helping revise a research idea JSON document. I will give you the complete context and you must output the COMPLETE revised JSON.\n\n## Research Context\n\nThis is Round 9 of 10 for a research proposal called SACE-RLVR (Structured Archive Co-Evolution for RLVR). The reviewer has identified critical missing works and a needed reframing. Here is exactly what needs to change:\n\n### Change 1: Add CurES (arXiv 2510.01037) to landscape — CRITICAL\n\nCurES (\"From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs\", Oct 2025, revised Mar 2026) is the most directly comparable prior art for Core 3's Bayesian estimation approach. Technical details:\n\n- Models per-problem success rate with Beta(α,β) posterior, updated as α += successes, β += failures from rollouts\n- Derives optimal sampling distribution ∝ exp(√[p(1-p)]/τ) via gradient convergence analysis\n- Uses POINT ESTIMATES (Beta mean) for sampling probability computation\n- Two-phase: parameter estimation phase (N'=4 rollouts per prompt), then training phase with variance-based rollout allocation\n- Fixed pool: Numina-Math dataset partitioned into 15 subsets\n- Results: Qwen2.5-Math-7B: AIME24 24.58%, MATH-500 84.80%, AMC23 64.38%, +4.82 over GRPO\n- Also: Qwen2.5-Math-1.5B: AIME24 13.33%, MATH-500 77.20%, +3.30 over GRPO\n- Uses VERL training framework\n\nDifferentiation from SACE-RLVR Core 3:\n- CurES: Beta posteriors for SAMPLING (which problem to train on) from fixed pool → SACE-RLVR: Beta posteriors for REPLACEMENT (should this new problem replace an existing archive occupant)\n- CurES: Point estimates (Beta mean) → SACE-RLVR: Credible intervals for replacement\n- CurES: Fixed pool selection → SACE-RLVR: Evolving archive with synthesis\n- CurES: Separate estimation phase → SACE-RLVR: Zero additional cost via G=16 training rollout reuse\n\n### Change 2: Add InSight (arXiv 2603.01907) to landscape\n\nInSight (\"Efficient RLVR Training via Weighted Mutual Information Data Selection\", Mar 2026):\n- Models Bayesian latent success rates with Beta(α,β), prior Beta(1,1)\n- Key innovation: weighted mutual information objective decomposing into difficulty-dependent (aleatoric) + evidence-dependent (epistemic) components\n- Shows difficulty-only selection (like p(1-p)) is fundamentally limited — epistemic uncertainty matters too\n- Temporal discounting on Beta parameters: α_{t+1} = λα_t + (1-λ)α_0 + S_t\n- Results: AIME24 53.75 on Qwen3-4B (+2.30 vs random), up to ~2.2× training acceleration on Countdown\n- Fixed pool (DeepScaler ~40K)\n- Differentiation: InSight extends Bayesian RLVR estimation with epistemic uncertainty; SACE-RLVR applies Bayesian estimation to archive replacement (different decision problem)\n\n### Change 3: Reframe Core 3's novelty claim\n\nOLD framing: \"Zero-Cost Bayesian Learnability Estimation\" positioned as if Beta posteriors in RLVR are novel\nNEW framing: \"Zero-Cost Bayesian Learnability for Archive Replacement\" — applies ESTABLISHED Beta-Bernoulli estimation (cf. CurES for sampling, InSight for mutual-information-based selection, DBB for gradient estimation) to a NEW DECISION PROBLEM: archive replacement via credible interval comparison, at zero additional inference cost. The novelty is:\n(a) The decision problem: replacement in evolving archives (not sampling from fixed pools or gradient estimation)\n(b) Credible intervals for replacement (not point estimates for sampling)\n(c) Zero-cost via G=16 training rollout reuse (vs CurES's separate estimation phase, DéjàQ's K=100 dedicated completions)\n\n### Change 4: SEC 3B data — IMPORTANT CORRECTION\n\nThe reviewer suggested noting that \"SEC (20.0%) underperforms uniform (23.33%) at 3B.\" However, my research shows this is INVERTED. From Actor-Curator's Table 1 at Qwen2.5-3B:\n- Uniform: 20.00% AIME24\n- SEC: 23.33% AIME24  \n- Actor-Curator: 30.00% AIME24\n\nSo SEC modestly outperforms uniform (+3.33 absolute, +16.7% relative), while Actor-Curator substantially outperforms both (+10.0 over uniform, +50% relative). The valid point is: SEC's category-level approach yields only modest gains over uniform on AIME24 at 3B, while Actor-Curator's per-problem utility estimation yields much larger gains — supporting the argument that coarser-grained approaches offer diminishing returns for harder competition-level problems. But I should use the CORRECT numbers, not the reviewer's inverted claim.\n\n### Change 5: Remove ICLR 2027 venue target\n\nWith 14-18 week timeline starting late May 2026, earliest completion is mid-September — ICLR 2027 deadline ~Sep 24, 2026 is nearly impossible. Remove to avoid credibility concerns.\n\n### Additional updates needed throughout:\n- core_problem: mention CurES/InSight establishing Bayesian estimation in RLVR\n- opportunity: note that Bayesian estimation is now established; our contribution is the archive-replacement application + credible intervals + zero cost\n- landscape: add CurES and InSight sections, update references to Core 3\n- approach: reframe Core 3\n- description: update summary\n- key_references: add CurES, InSight\n- target_venues: remove ICLR 2027\n- inspired_by: add CurES and InSight\n- reviewer_response: document all changes for round 9\n\nHere is the COMPLETE original JSON that you must revise. Output the COMPLETE revised JSON with ALL fields:\n\n```json\n{\n  \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\",\n  \"core_problem\": \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the 'sparse policy selection' view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes 'capability boundary collapse' where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Recent bandit-based curriculum approaches address adaptive selection during RL: SEC (arXiv 2505.14970) formulates curriculum as a MAB over problem categories, achieving 17.5% AIME 2024 on Qwen2.5-7B (+27% relative); Actor-Curator (arXiv 2602.20532) extends this with a neural curator achieving 30.0% AIME 2024 on Qwen2.5-3B (+28.6% relative over uniform) with regret guarantees. However, both select from fixed problem pools (12K MATH problems) without synthesis—they optimize WHICH existing problems to train on, but cannot create new problems when the pool lacks adequate coverage for the policy's current frontier. As the policy improves toward competition level, the fraction of useful problems in a fixed pool shrinks, hitting a pool-exhaustion ceiling. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution—but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps, achieving 13.3% AIME 2024—matching the Qwen-2.5-7B base model—and actually degrading AMC 2023 from 57.5% to 52.5%. The fundamental open question is: can we build a system that combines the adaptive selection intelligence of bandit-based methods with persistent coverage-maintaining archives and targeted synthesis for identified gaps at competition level?\",\n  \"opportunity\": \"Five converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic—and multiple empirical findings support diversity's importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) Bandit-based curriculum methods demonstrate the value of adaptive selection but reveal the ceiling of fixed-pool approaches: SEC achieves 17.5% AIME 2024 (Qwen2.5-7B) via MAB over categories; Actor-Curator achieves 30.0% AIME 2024 (Qwen2.5-3B) via neural bandit with regret guarantees—but both select from fixed 12K pools without synthesis or multi-dimensional coverage tracking. The approaches are potentially COMPLEMENTARY: principled bandit selection FROM a coverage-maintaining, synthesis-augmented archive. (5) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K→80K); per-niche survival varies by topic (geometry autoformalization is ~3.7× harder than non-geometry per IndiMathBench, though this reflects formalization-specific difficulty that may not fully transfer to synthesis). VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification with targeted synthesis (vs. reactive instance-level targeting or selection-only bandits), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria.\",\n  \"landscape\": \"**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\\n\\n**Bandit-based adaptive curriculum (critical comparators).** SEC (arXiv 2505.14970) formulates online curriculum selection as a non-stationary MAB where each problem category (difficulty level or problem type) is an arm. Uses TD(0) updates on Q-values derived from absolute advantages, with Boltzmann sampling: p(c) ∝ exp(Q(c)/τ). Selects from fixed training pools (10K problems per domain). Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random 13.8%), 76.1% MATH-500, 51.1% AMC22-23. Categories are 1D (difficulty OR type per domain). SEC-2D variant combines 3 reasoning domains into 9 arms for multi-task learning. Actor-Curator (arXiv 2602.20532) extends beyond SEC's category-level bandits to per-problem utility estimation via a neural curator (Qwen3-0.6B) trained with online stochastic mirror descent (OSMD). Establishes regret bound O(T^{2/3}·V_T^{1/3}) under non-stationary utilities. Selects from fixed pools (12K MATH problems). Qwen2.5-3B: 30.0% AIME 2024, 81.0% MATH-500 (+28.6% relative over uniform 23.3%; beats SEC at 20.0% in matched 3B comparison). ~9% overhead. Key insight: Actor-Curator's per-problem utility estimation is more expressive than SEC's category-level Q-values, yielding consistent gains. Critical differentiation from SACE-RLVR on four dimensions: (a) SELECTION vs. SYNTHESIS—both SEC and Actor-Curator select from fixed pools of existing problems; they cannot synthesize new problems targeting identified gaps. As the policy improves toward competition level, the fraction of useful problems in a fixed 12K pool shrinks (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED optimization—Actor-Curator optimizes aggregate per-problem utility without explicit multi-dimensional coverage constraints, risking concentration on high-utility niches without ensuring breadth (analogous to SAGE's demonstrated over-specialization); (c) STATELESS vs. PERSISTENT—neither maintains a persistent multi-dimensional archive with cross-step coverage tracking; (d) COMPLEMENTARITY—crucially, these approaches compete at different levels: Actor-Curator's bandit selection could serve as the within-archive sampling strategy, combining principled selection WITH coverage-maintaining synthesis. We test this complementarity explicitly.\\n\\n**Balanced difficulty filtering theory.** Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) proves that expected policy improvement is lower-bounded by the variance of task-level success probabilities p(x)(1-p(x)), maximized at p(x)=0.5. Balanced filtering (0.3&lt;p(x)<0.7) achieves +12% on AMC and +10% on AIME with Qwen2.5 models in less than half the training steps of standard GRPO. This theoretical result directly supports our difficulty-aware design: our Bayesian learnability criterion tracks p(1-p) per problem via Beta posteriors, and our archive's ZPD-weighted sampling preferentially selects problems near the difficulty frontier.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\\n\\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\\n\\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold α=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively). On AIME 2024, SAGE achieves 13.3%—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%. This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents. Training dynamics confirm this: over-specialization emerges after ~120 steps (peak 69.5% declining to 61.6% by step 240). Question pool grows 18× (1,136→20,532) as flat filtered dataset without structured organization.\\n\\n**Implicit curriculum theory.** 'The Implicit Curriculum' (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation—not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: 'behavioral diversity is the binding constraint for RL.' RL-PLUS (arXiv 2508.00222) demonstrates 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\\n\\n**Policy-level diversity maintenance (concurrent).** UCPO (arXiv 2605.00365) addresses pass@k diversity collapse at the optimization level rather than the data level, adding a conditional uniformity penalty that redistributes gradient signal toward underrepresented correct solutions. Achieves +10% absolute Pass@64 on AIME 2024 (DeepSeek-7B: 70.0%→80.0%) and +45% equation-level diversity while maintaining competitive Pass@1. Importantly, UCPO modifies the loss function, not the training distribution—making it orthogonal to and potentially complementary with archive-based diversity maintenance. UCPO ensures diversity within the correct solution set for a given problem; SACE-RLVR ensures diversity across the problem distribution.\\n\\n**Lightweight co-evolutionary diversity (concurrent).** Vocabulary Dropout (arXiv 2604.03472) prevents proposer diversity collapse in co-evolutionary frameworks by applying random hard logit masks during problem generation, achieving +4.4 average points on Qwen3-8B (+10.9 AMC, +3.4 AIME 2024, +7.8 AIME 2025) within R-Zero. Demonstrates that diversity collapse is a real bottleneck in co-evolutionary RLVR. Differentiation: VD maintains proposer diversity via stochastic masking; SACE-RLVR provides structured coverage guarantees and interpretable gap identification.\\n\\n**Meta-RL curriculum generation (concurrent).** SOAR (arXiv 2601.18778) uses bi-level meta-RL where a teacher generates stepping-stone problems rewarded by measured student improvement on hard problems. Achieves +9.3% pass@32 on MATH fail@128 tasks (Llama-3.2-3B), recovering 75% of oracle gains from training on the full MATH dataset. Key insight: structural quality of generated problems matters more than solution correctness. Conceptually parallel to our proactive gap identification but uses meta-RL reward signal (measured student improvement) vs. our archive-structure-based gap detection. SOAR operates at the edge of learnability for currently-unsolvable problems; SACE-RLVR maintains coverage across the full difficulty spectrum.\\n\\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\\n\\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%→16.4%; Qwen3-8B AIME24: 16.7→26.0. Proves diversity collapse is real (TTRL pass@16: 32.4→16.7).\\n\\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\\n\\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\\n\\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR—related to our approach but operates at policy gradient level vs. our archive-replacement level.\\n\\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K→80K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry autoformalization has ~3.7× lower success rate than non-geometry (IndiMathBench arXiv 2512.00997: 12.2% vs 44.9% BEq across top models); the paper attributes this partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty. These grounding data inform our per-niche survival estimates.\\n\\n**Verification.** VHG (arXiv 2605.06660): validity gating.\\n\\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\\n\\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\\n\\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\\n\\n**The precise gap.** DéjàQ: 1D, GSM-only. SEC: MAB over categories, 1D, fixed pool. Actor-Curator: per-problem bandit, fixed pool, no coverage tracking. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization, zero AIME improvement over base model. Online Difficulty Filtering: theoretical support for balanced filtering, no archive structure. UCPO: policy-level diversity, no data-level coverage. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification with synthesis, structured coverage tracking, and Bayesian learnability replacement. Moreover, no existing work tests whether bandit-based selection and archive-based synthesis are complementary.\",\n  \"inspired_by\": \"DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + SEC_insight['MAB over problem categories during RL; 17.5% AIME24'] + Actor_Curator_insight['neural bandit with regret guarantees; 30.0% AIME24; ~9% overhead; pool-selection ceiling motivates synthesis'] + Online_Difficulty_Filtering['p(1-p) lower bound on policy improvement; balanced filtering; EACL 2026'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools → over-specialization ~120 steps; 13.3% AIME = base model; AMC degrades'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + UCPO_concurrent['policy-level diversity; +10% Pass@64 AIME; complementary to data-level'] + VocabDropout_concurrent['+4.4 avg; diversity collapse prevention'] + SOAR_concurrent['meta-RL teacher; 75% oracle recovery'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry ~3.7× lower autoformalization success; formalization-specific'] + EVOL_RL_warning['diversity collapse']\",\n  \"approach\": \"[KEEP ORIGINAL APPROACH TEXT BUT MAKE THESE SPECIFIC CHANGES TO CORE 3]\",\n  \"resource_estimate\": \"[KEEP ORIGINAL]\",\n  \"target_venues\": \"[REMOVE ICLR 2027]\",\n  \"level\": \"top-tier\",\n  \"key_references\": \"[ADD CurES AND InSight]\",\n  \"description\": \"[UPDATE SUMMARY]\",\n  \"project_name\": \"sace_rlvr\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": \"[UPDATE FOR ROUND 9]\"\n}\n```\n\nNow, I will write the COMPLETE JSON below. Make EVERY field complete — do not use placeholders or \"[KEEP ORIGINAL]\". I need you to output the actual full text for every single field, modifying where needed per the changes above and keeping the rest intact.\n\nCRITICAL RULES:\n1. The JSON must be valid — escape all quotes inside strings, use \\n for newlines\n2. Every field must be complete, not truncated\n3. The approach field must have the FULL text with Core 3 reframed\n4. The landscape must include the new CurES and InSight sections\n5. The core_problem must reference CurES/InSight in the Bayesian context\n6. Add \"change_type\": \"minor\" field\n7. For the SEC 3B data point, use CORRECT numbers: Uniform=20.00, SEC=23.33, Actor-Curator=30.00. The reviewer's claim that SEC underperforms uniform was inverted. The correct observation is that SEC's category-level gains are MODEST (+3.33 absolute) compared to Actor-Curator's substantial gains (+10.0 absolute), supporting the argument that coarser approaches offer diminishing returns for harder problems.\n8. In the bandit landscape section, fix the line \"beats SEC at 20.0% in matched 3B comparison\" — this should say something like \"SEC achieves 23.33% while uniform achieves only 20.00%; Actor-Curator's per-problem utility yields much larger gains than SEC's category-level approach\"\n\nOutput ONLY the JSON object, nothing else.\n",
  "model": "opus"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1d73344-1e00-4bc5-a8b5-764667ee30bf",
  "isSidechain": false,
  "requestId": "req_011CbUGsrmQdgTLDB2RADSo1",
  "type": "assistant",
  "uuid": "8402397b-19f7-46a5-8e64-fefd13923e69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m71C6wfAEZb8D7zLh8LkB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 43889,
      "output_tokens": 9009,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9009,
          "cache_read_input_tokens": 43889,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "8402397b-19f7-46a5-8e64-fefd13923e69",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise RLVR archive approach for CurES acknowledgment",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Tool result

_source line 56 · 2026-05-28T04:02:10.217Z_

<details><summary>↩ Tool result · `toolu_014yMsoZy9eQUQx63cXtQnrP`</summary>

````text
The environment won't let me run Python to validate. Let me just output the complete JSON directly as my response, which is what the user asked for.

Here is the complete revised JSON:

```json
{
  "title": "Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis",
  "change_type": "minor",
  "core_problem": "Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum\u2014easier problems become learnable first and bootstrap harder ones via a \u2018relay effect.\u2019 However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the \u2018sparse policy selection\u2019 view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes \u2018capability boundary collapse\u2019 where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. D\u00e9j\u00e0Q (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial\u2014maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, D\u00e9j\u00e0Q operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Recent bandit-based curriculum approaches address adaptive selection during RL: SEC (arXiv 2505.14970) formulates curriculum as a MAB over problem categories, achieving 17.5% AIME 2024 on Qwen2.5-7B (+27% relative); Actor-Curator (arXiv 2602.20532) extends this with a neural curator achieving 30.0% AIME 2024 on Qwen2.5-3B (+28.6% relative over uniform) with regret guarantees. However, both select from fixed problem pools (12K MATH problems) without synthesis\u2014they optimize WHICH existing problems to train on, but cannot create new problems when the pool lacks adequate coverage for the policy\u2019s current frontier. As the policy improves toward competition level, the fraction of useful problems in a fixed pool shrinks, hitting a pool-exhaustion ceiling. Bayesian estimation of per-problem learnability is now an established technique in RLVR curriculum design: CurES (arXiv 2510.01037) models per-problem success rates with Beta(\u03b1,\u03b2) posteriors and derives optimal sampling distributions via gradient convergence analysis; InSight (arXiv 2603.01907) extends this with weighted mutual information decomposing into difficulty-dependent and epistemic components; DBB (arXiv 2603.18444) applies Beta-Bernoulli estimation to policy gradient variance reduction. However, all these apply Bayesian estimation to problem SELECTION from fixed pools or gradient estimation\u2014none applies it to the fundamentally different decision problem of archive REPLACEMENT in evolving archives with synthesis. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)\u2014but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution\u2014but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps, achieving 13.3% AIME 2024\u2014matching the Qwen-2.5-7B base model\u2014and actually degrading AMC 2023 from 57.5% to 52.5%. The fundamental open question is: can we build a system that combines the adaptive selection intelligence of bandit-based methods with persistent coverage-maintaining archives and targeted synthesis for identified gaps at competition level?",
  "opportunity": "Five converging developments create a precise research window. (1) D\u00e9j\u00e0Q proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But D\u00e9j\u00e0Q\u2019s 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic\u2014and multiple empirical findings support diversity\u2019s importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) Bandit-based curriculum methods demonstrate the value of adaptive selection but reveal the ceiling of fixed-pool approaches: SEC achieves 17.5% AIME 2024 (Qwen2.5-7B) via MAB over categories; Actor-Curator achieves 30.0% AIME 2024 (Qwen2.5-3B) via neural bandit with regret guarantees\u2014but both select from fixed 12K pools without synthesis or multi-dimensional coverage tracking. The approaches are potentially COMPLEMENTARY: principled bandit selection FROM a coverage-maintaining, synthesis-augmented archive. (5) Bayesian estimation of per-problem learnability is now established in RLVR: CurES derives optimal sampling distributions from Beta posteriors via gradient convergence analysis; InSight extends this with mutual-information-based selection decomposing epistemic and aleatoric uncertainty; DBB applies Beta-Bernoulli estimation to gradient variance reduction. Our contribution applies this established estimation technique to a new decision problem\u2014archive replacement via credible interval comparison\u2014at zero additional inference cost by reusing G=16 training rollouts, rather than requiring separate estimation phases (CurES) or dedicated completions (D\u00e9j\u00e0Q K=100). (6) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K\u219280K); per-niche survival varies by topic (geometry autoformalization is ~3.7\u00d7 harder than non-geometry per IndiMathBench, though this reflects formalization-specific difficulty that may not fully transfer to synthesis). VHG\u2019s validity-gating separates problem validity from difficulty; MathForge\u2019s DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification with targeted synthesis (vs. reactive instance-level targeting or selection-only bandits), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria applied to evolving archives rather than fixed-pool selection.",
  "landscape": "**Online archive-based co-evolution (direct predecessor).** D\u00e9j\u00e0Q (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic \u2018setting\u2019 categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only\u2014competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\n\n**Bandit-based adaptive curriculum (critical comparators).** SEC (arXiv 2505.14970) formulates online curriculum selection as a non-stationary MAB where each problem category (difficulty level or problem type) is an arm. Uses TD(0) updates on Q-values derived from absolute advantages, with Boltzmann sampling: p(c) \u221d exp(Q(c)/\u03c4). Selects from fixed training pools (10K problems per domain). Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random 13.8%), 76.1% MATH-500, 51.1% AMC22-23. Categories are 1D (difficulty OR type per domain). SEC-2D variant combines 3 reasoning domains into 9 arms for multi-task learning. Actor-Curator (arXiv 2602.20532) extends beyond SEC\u2019s category-level bandits to per-problem utility estimation via a neural curator (Qwen3-0.6B) trained with online stochastic mirror descent (OSMD). Establishes regret bound O(T^{2/3}\u00b7V_T^{1/3}) under non-stationary utilities. Selects from fixed pools (12K MATH problems). Qwen2.5-3B: 30.0% AIME 2024, 81.0% MATH-500 (+28.6% relative over uniform 23.3%; in the matched 3B comparison, SEC achieves 23.33% while uniform achieves only 20.00%\u2014SEC\u2019s category-level approach yields only modest gains over uniform (+3.33 absolute, +16.7% relative), while Actor-Curator\u2019s per-problem utility estimation yields much larger gains (+10.0 absolute over uniform, +50% relative), supporting the argument that coarser-grained category-level approaches offer diminishing returns for harder competition-level problems). ~9% overhead. Key insight: Actor-Curator\u2019s per-problem utility estimation is more expressive than SEC\u2019s category-level Q-values, yielding consistent gains. Critical differentiation from SACE-RLVR on four dimensions: (a) SELECTION vs. SYNTHESIS\u2014both SEC and Actor-Curator select from fixed pools of existing problems; they cannot synthesize new problems targeting identified gaps. As the policy improves toward competition level, the fraction of useful problems in a fixed 12K pool shrinks (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED optimization\u2014Actor-Curator optimizes aggregate per-problem utility without explicit multi-dimensional coverage constraints, risking concentration on high-utility niches without ensuring breadth (analogous to SAGE\u2019s demonstrated over-specialization); (c) STATELESS vs. PERSISTENT\u2014neither maintains a persistent multi-dimensional archive with cross-step coverage tracking; (d) COMPLEMENTARITY\u2014crucially, these approaches compete at different levels: Actor-Curator\u2019s bandit selection could serve as the within-archive sampling strategy, combining principled selection WITH coverage-maintaining synthesis. We test this complementarity explicitly.\n\n**Bayesian learnability estimation in RLVR (critical context for Core 3).** CurES (arXiv 2510.01037, Oct 2025, revised Mar 2026) is the most directly comparable prior art for Bayesian estimation in RLVR curriculum design. Models per-problem success rate with Beta(\u03b1,\u03b2) posterior, updated as \u03b1 += successes, \u03b2 += failures from rollouts. Derives optimal sampling distribution \u221d exp(\u221a[p(1-p)]/\u03c4) via gradient convergence analysis. Uses point estimates (Beta mean) for sampling probability computation. Two-phase: parameter estimation phase (N'=4 rollouts per prompt), then training phase with variance-based rollout allocation. Fixed pool: Numina-Math dataset partitioned into 15 subsets. Results: Qwen2.5-Math-7B: AIME24 24.58%, MATH-500 84.80%, AMC23 64.38%, +4.82 over GRPO; Qwen2.5-Math-1.5B: AIME24 13.33%, MATH-500 77.20%, +3.30 over GRPO. Uses VERL training framework. Critical differentiation from SACE-RLVR Core 3: (a) CurES uses Beta posteriors for SAMPLING (which problem to train on) from a fixed pool \u2192 SACE-RLVR uses Beta posteriors for REPLACEMENT (should this new problem replace an existing archive occupant)\u2014a fundamentally different decision problem; (b) CurES uses point estimates (Beta mean) \u2192 SACE-RLVR uses credible intervals for replacement decisions; (c) CurES operates on a fixed pool \u2192 SACE-RLVR operates on an evolving archive with synthesis; (d) CurES requires a separate estimation phase (N'=4 dedicated rollouts per prompt) \u2192 SACE-RLVR achieves zero additional cost via G=16 training rollout reuse.\n\nInSight (arXiv 2603.01907, Mar 2026) extends Bayesian RLVR estimation with weighted mutual information for data selection. Models Bayesian latent success rates with Beta(\u03b1,\u03b2), prior Beta(1,1). Key innovation: weighted mutual information objective decomposing into difficulty-dependent (aleatoric) + evidence-dependent (epistemic) components. Demonstrates that difficulty-only selection (like p(1-p)) is fundamentally limited\u2014epistemic uncertainty matters too. Temporal discounting on Beta parameters: \u03b1_{t+1} = \u03bb\u03b1_t + (1-\u03bb)\u03b1_0 + S_t. Results: AIME24 53.75 on Qwen3-4B (+2.30 vs random), up to ~2.2\u00d7 training acceleration on Countdown. Fixed pool (DeepScaler ~40K). Differentiation: InSight extends Bayesian RLVR estimation with epistemic uncertainty for problem selection from fixed pools; SACE-RLVR applies Bayesian estimation to archive replacement (different decision problem) in evolving archives with synthesis.\n\n**Balanced difficulty filtering theory.** Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) proves that expected policy improvement is lower-bounded by the variance of task-level success probabilities p(x)(1-p(x)), maximized at p(x)=0.5. Balanced filtering (0.3&lt;p(x)<0.7) achieves +12% on AMC and +10% on AIME with Qwen2.5 models in less than half the training steps of standard GRPO. This theoretical result directly supports our difficulty-aware design: our Bayesian learnability criterion tracks p(1-p) per problem via Beta posteriors, and our archive\u2019s ZPD-weighted sampling preferentially selects problems near the difficulty frontier.\n\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard \u22640.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\n\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver\u2019s specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for \u2018desirable difficulty.\u2019 Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\n\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold \u03b1=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively). On AIME 2024, SAGE achieves 13.3%\u2014matching the Qwen-2.5-7B base model (also 13.3%)\u2014and degrades AMC 2023 from 57.5% to 52.5%. This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance\u2014precisely the over-specialization that structured archive-based diversity maintenance prevents. Training dynamics confirm this: over-specialization emerges after ~120 steps (peak 69.5% declining to 61.6% by step 240). Question pool grows 18\u00d7 (1,136\u219220,532) as flat filtered dataset without structured organization.\n\n**Implicit curriculum theory.** \u2018The Implicit Curriculum\u2019 (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation\u2014not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\n\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR \u2018polarizes\u2019\u2014sharpening some primitives while sacrificing others\u2014and since multi-step success compounds multiplicatively (P(q) \u221d \u220fP(s\u2c7c)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: \u2018behavioral diversity is the binding constraint for RL.\u2019 RL-PLUS (arXiv 2508.00222) demonstrates \u2018capability boundary collapse\u2019\u2014pass@1 up, pass@128 down\u2014with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\n\n**Policy-level diversity maintenance (concurrent).** UCPO (arXiv 2605.00365) addresses pass@k diversity collapse at the optimization level rather than the data level, adding a conditional uniformity penalty that redistributes gradient signal toward underrepresented correct solutions. Achieves +10% absolute Pass@64 on AIME 2024 (DeepSeek-7B: 70.0%\u219280.0%) and +45% equation-level diversity while maintaining competitive Pass@1. Importantly, UCPO modifies the loss function, not the training distribution\u2014making it orthogonal to and potentially complementary with archive-based diversity maintenance. UCPO ensures diversity within the correct solution set for a given problem; SACE-RLVR ensures diversity across the problem distribution.\n\n**Lightweight co-evolutionary diversity (concurrent).** Vocabulary Dropout (arXiv 2604.03472) prevents proposer diversity collapse in co-evolutionary frameworks by applying random hard logit masks during problem generation, achieving +4.4 average points on Qwen3-8B (+10.9 AMC, +3.4 AIME 2024, +7.8 AIME 2025) within R-Zero. Demonstrates that diversity collapse is a real bottleneck in co-evolutionary RLVR. Differentiation: VD maintains proposer diversity via stochastic masking; SACE-RLVR provides structured coverage guarantees and interpretable gap identification.\n\n**Meta-RL curriculum generation (concurrent).** SOAR (arXiv 2601.18778) uses bi-level meta-RL where a teacher generates stepping-stone problems rewarded by measured student improvement on hard problems. Achieves +9.3% pass@32 on MATH fail@128 tasks (Llama-3.2-3B), recovering 75% of oracle gains from training on the full MATH dataset. Key insight: structural quality of generated problems matters more than solution correctness. Conceptually parallel to our proactive gap identification but uses meta-RL reward signal (measured student improvement) vs. our archive-structure-based gap detection. SOAR operates at the edge of learnability for currently-unsolvable problems; SACE-RLVR maintains coverage across the full difficulty spectrum.\n\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\n\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%\u219216.4%; Qwen3-8B AIME24: 16.7\u219226.0. Proves diversity collapse is real (TTRL pass@16: 32.4\u219216.7).\n\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\n\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\n\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR\u2014related to our approach but operates at policy gradient level vs. our archive-replacement level.\n\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K\u219280K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry autoformalization has ~3.7\u00d7 lower success rate than non-geometry (IndiMathBench arXiv 2512.00997: 12.2% vs 44.9% BEq across top models); the paper attributes this partly to Mathlib\u2019s lacking support for Olympiad-style geometry\u2014a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty. These grounding data inform our per-niche survival estimates.\n\n**Verification.** VHG (arXiv 2605.06660): validity gating.\n\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Bayesian curriculum: CurES 24.58% (7B-Math), InSight 53.75% (Qwen3-4B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\n\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\n\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\n\n**The precise gap.** D\u00e9j\u00e0Q: 1D, GSM-only. SEC: MAB over categories, 1D, fixed pool. Actor-Curator: per-problem bandit, fixed pool, no coverage tracking. CurES: Beta posteriors for sampling from fixed pool, point estimates, separate estimation phase. InSight: Beta posteriors with mutual information for selection from fixed pool. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization, zero AIME improvement over base model. Online Difficulty Filtering: theoretical support for balanced filtering, no archive structure. UCPO: policy-level diversity, no data-level coverage. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification with synthesis, structured coverage tracking, and Bayesian learnability replacement applied to evolving archives (rather than fixed-pool selection). Moreover, no existing work tests whether bandit-based selection and archive-based synthesis are complementary.",
  "inspired_by": "D\u00e9j\u00e0Q_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + SEC_insight['MAB over problem categories during RL; 17.5% AIME24'] + Actor_Curator_insight['neural bandit with regret guarantees; 30.0% AIME24; ~9% overhead; pool-selection ceiling motivates synthesis'] + CurES_insight['Beta posteriors for sampling; gradient convergence analysis; +4.82 over GRPO; establishes Bayesian estimation in RLVR'] + InSight_insight['weighted mutual information; epistemic + aleatoric decomposition; temporal discounting; extends Bayesian RLVR estimation'] + Online_Difficulty_Filtering['p(1-p) lower bound on policy improvement; balanced filtering; EACL 2026'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools \u2192 over-specialization ~120 steps; 13.3% AIME = base model; AMC degrades'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + UCPO_concurrent['policy-level diversity; +10% Pass@64 AIME; complementary to data-level'] + VocabDropout_concurrent['+4.4 avg; diversity collapse prevention'] + SOAR_concurrent['meta-RL teacher; 75% oracle recovery'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry ~3.7\u00d7 lower autoformalization success; formalization-specific'] + EVOL_RL_warning['diversity collapse']",
  "approach": "SACE-RLVR integrates three tightly-coupled cores into a unified online co-evolutionary RLVR system.\n\n**Core 1: Multi-Dimensional MAP-Elites Archive with ZPD-Weighted Sampling.** We extend D\u00e9j\u00e0Q\u2019s 1D thematic archive to a 2D archive indexed by (topic, difficulty), with ~8 topic categories and ~5 difficulty levels yielding ~40 niches. Each niche stores the top-K (K=3) problems ranked by Bayesian learnability (see Core 3). The difficulty dimension is estimated from rollout success rates during training (aligned with CLPO\u2019s online assessment but with finer granularity: 5 bins vs. 3). Archive initialization uses a seed dataset of ~2K competition-level problems (e.g., from MATH Level 4-5, AMC, AIME). During training, batch construction uses ZPD-weighted sampling: each niche\u2019s sampling weight is proportional to its aggregate learnability score, biased toward the zone of proximal development (p \u2208 [0.2, 0.8]) where learning signal is strongest per the Online Difficulty Filtering lower bound. Coverage enforcement ensures each topic receives minimum representation per epoch, preventing the over-specialization demonstrated by SAGE. The archive evolves continuously as Core 2 proposes candidates and Core 3 adjudicates replacement.\n\n**Core 2: Proactive Niche-Level Gap Identification and Targeted Synthesis.** Rather than D\u00e9j\u00e0Q\u2019s random mutation or Socratic-Zero\u2019s reactive instance-level targeting, we implement proactive gap identification at the niche level. After each training epoch, we compute a coverage map: for each niche (topic, difficulty), we track occupancy count, average learnability, and learnability trend (improving/declining/stagnant). Gap identification triggers synthesis when: (a) a niche is empty or under-occupied (coverage gap); (b) all problems in a niche have learnability below threshold (the policy has \u2018graduated\u2019 and needs harder problems); (c) learnability is declining across a difficulty band (potential relay-effect blockage). Synthesis uses the policy model itself with structured prompts specifying the target topic, difficulty level, and (for weakness targeting) specific error patterns extracted from failed rollouts in adjacent niches. Multi-stage verification follows: (1) format/solvability check via symbolic solver where applicable (SymPy, Lean4 for formalizable subsets); (2) difficulty calibration via G=4 quick rollouts; (3) novelty check against archive occupants via embedding similarity. We target ~30% end-to-end survival rate informed by SAND-Math (~38%) and SPARQ (~25%), with per-topic variation (geometry expected ~15% vs. algebra ~40% based on IndiMathBench difficulty ratios, adjusted for synthesis vs. formalization). Invalid problems are discarded without penalty; valid problems proceed to Core 3 for replacement adjudication.\n\n**Core 3: Zero-Cost Bayesian Learnability for Archive Replacement.** This core applies established Beta-Bernoulli estimation\u2014as used by CurES for sampling (arXiv 2510.01037), InSight for mutual-information-based selection (arXiv 2603.01907), and DBB for gradient estimation (arXiv 2603.18444)\u2014to a new decision problem: archive replacement in evolving archives. For each problem x in the archive, we maintain a Beta(\u03b1_x, \u03b2_x) posterior over its true success rate, initialized with prior Beta(1,1). Each time x appears in a training batch with G=16 rollouts, we observe k successes out of G attempts and update: \u03b1_x += k, \u03b2_x += (G-k). The key insight enabling zero additional cost: we reuse the G=16 rollouts already required for GRPO training\u2014no separate estimation phase is needed (unlike CurES\u2019s dedicated N\u2019=4 estimation rollouts per prompt, or D\u00e9j\u00e0Q\u2019s K=100 dedicated completions). Learnability is computed as the posterior mean of p(1-p): E[p(1-p)] = \u03b1\u03b2/[(\u03b1+\u03b2)^2(\u03b1+\u03b2+1)]. The novelty of Core 3 lies not in the Beta-Bernoulli estimation itself (which is now established in RLVR via CurES, InSight, and DBB), but in three aspects: (a) The decision problem: replacement in evolving archives rather than sampling from fixed pools or gradient estimation. When a candidate problem x\u2019 is proposed for a niche occupied by x, we compare credible intervals: x\u2019 replaces x if the lower bound of x\u2019\u2019s 80% credible interval for learnability exceeds the upper bound of x\u2019s interval, providing conservative replacement that accounts for estimation uncertainty. (b) Credible intervals rather than point estimates: CurES uses point estimates (Beta mean) for sampling probabilities; we use full posterior credible intervals to make replacement decisions that appropriately account for uncertainty\u2014a new problem with few observations should not displace a well-characterized occupant based on a noisy point estimate. (c) Zero additional inference cost: by reusing G=16 training rollouts, we avoid CurES\u2019s separate estimation phase and D\u00e9j\u00e0Q\u2019s K=100 dedicated completions. Temporal discounting (inspired by InSight\u2019s \u03bb-discounting on Beta parameters) prevents stale estimates: \u03b1_x \u2192 \u03bb\u03b1_x + (1-\u03bb), \u03b2_x \u2192 \u03bb\u03b2_x + (1-\u03bb) with \u03bb=0.95, ensuring the posterior adapts as the policy evolves.\n\n**Integration and training loop.** Each training step: (1) Sample a batch from the archive using ZPD-weighted niche sampling; (2) Run G=16 GRPO rollouts; (3) Update Beta posteriors for all sampled problems (zero cost\u2014reuses rollouts from step 2); (4) Compute GRPO policy gradient with DGPO weighting (MathForge); (5) Every N steps, run gap identification and trigger synthesis for identified gaps; (6) Adjudicate replacement for synthesis candidates and any archive occupants whose learnability has dropped below threshold. The system maintains a coverage dashboard tracking per-niche occupancy, learnability distributions, and difficulty spectrum smoothness.\n\n**Ablation design.** A1: Archive dimensionality (1D topic-only vs. 2D topic\u00d7difficulty vs. flat pool). A2: Synthesis targeting (proactive niche-level vs. random mutation vs. no synthesis). A3: Difficulty spectrum smoothness (does smoother coverage correlate with faster convergence, testing the relay-effect hypothesis from implicit curriculum theory?). A4: Bayesian replacement via credible intervals vs. point-estimate replacement vs. D\u00e9j\u00e0Q\u2019s direct fitness comparison. A5: Bandit complementarity (uniform archive sampling vs. SEC-style MAB vs. Actor-Curator-style neural bandit over archive niches). A6: G=16 rollout reuse vs. dedicated estimation rollouts (testing zero-cost claim).\n\n**Extensions.** E1: DGPO integration (MathForge\u2019s difficulty-aware weighting). E2: UCPO integration (policy-level diversity maintenance, orthogonal to data-level). E3: Vocabulary Dropout for synthesis diversity. E4: Actor-Curator as within-archive sampling strategy.",
  "resource_estimate": "Base model: Qwen2.5-7B (primary) and Qwen2.5-3B (scaling comparison). Training: 8\u00d7A100 80GB GPUs, ~500 GRPO steps with G=16 rollouts. Estimated training time: ~72-96 hours for main run, ~200 hours total including ablations. Synthesis overhead: ~15-20% of training compute (amortized over gap identification intervals of N=50 steps). Verification overhead: ~5-10% (symbolic checking is fast; difficulty calibration G=4 rollouts are the bottleneck). Archive maintenance: negligible (<1% of compute). Total compute budget: ~2,000-3,000 A100-hours including all ablations and baselines. Key infrastructure: VERL or OpenRLHF training framework, SymPy for symbolic verification, embedding model for novelty checking. Timeline: 14-18 weeks. Weeks 1-3: infrastructure (archive data structures, GRPO training loop, synthesis pipeline). Weeks 4-6: Core 1+3 implementation and validation on MATH-500. Weeks 7-9: Core 2 synthesis pipeline with verification. Weeks 10-12: full system integration and main experiments. Weeks 13-15: ablation studies. Weeks 16-18: analysis, writing, submission preparation.",
  "target_venues": ["NeurIPS 2027", "ICML 2027"],
  "level": "top-tier",
  "key_references": [
    "D\u00e9j\u00e0Q (arXiv 2601.01931) - online MAP-Elites co-evolution for RLVR",
    "The Implicit Curriculum (arXiv 2602.14872, ICML 2026) - relay vs grokking regimes",
    "SEC (arXiv 2505.14970) - MAB over problem categories for RLVR curriculum",
    "Actor-Curator (arXiv 2602.20532) - neural bandit with regret guarantees for RLVR",
    "CurES (arXiv 2510.01037) - Beta posteriors for sampling; gradient convergence analysis for RLVR curriculum",
    "InSight (arXiv 2603.01907) - weighted mutual information with epistemic+aleatoric decomposition for RLVR data selection",
    "Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) - p(1-p) lower bound",
    "CLPO (arXiv 2509.25004) - online curriculum, 50% AIME 2024",
    "Socratic-Zero (arXiv 2509.24726) - three-agent co-evolution",
    "SAGE (arXiv 2603.15255) - flat pools lead to over-specialization",
    "RL-PLUS (arXiv 2508.00222) - capability boundary collapse",
    "Sharper Primitives (arXiv 2602.08281) - multiplicative compounding",
    "Tailor (arXiv 2511.12429) - behavioral diversity as binding constraint",
    "Sparse Policy Selection (arXiv 2605.06241) - RL modifies 1-3% of tokens",
    "UCPO (arXiv 2605.00365) - policy-level diversity maintenance",
    "Vocabulary Dropout (arXiv 2604.03472) - diversity collapse prevention",
    "SOAR (arXiv 2601.18778) - meta-RL curriculum generation",
    "MathForge/DGPO (arXiv 2601.20614, ICLR 2026) - difficulty-aware optimization",
    "VCRL (arXiv 2509.19803) - reward variance as curriculum signal",
    "MC-GRPO (arXiv 2601.22582) - rollout count ablation",
    "Gradient Starvation (arXiv 2605.07689) - gradient degeneracy analysis",
    "DBB (arXiv 2603.18444) - Bayesian Beta-Bernoulli for RLVR gradients",
    "SAND-Math (arXiv 2507.20527) - synthesis survival rates",
    "SPARQ (arXiv 2506.06499) - QD survival rates",
    "VHG (arXiv 2605.06660) - validity gating",
    "EVOL-RL (arXiv 2509.15194) - novelty-aware diversity",
    "Bidirectional Curriculum Generation (arXiv 2603.05120) - 4-agent framework",
    "DART-Math (arXiv 2407.13690) - query coverage dropout",
    "FLAMES (arXiv 2508.16514) - self-consistency filtering",
    "IndiMathBench (arXiv 2512.00997) - geometry difficulty baseline",
    "SwS (NeurIPS 2025) - offline weakness targeting",
    "STAT (arXiv 2510.10023) - Missing-Skill-Profiles",
    "R-Zero (ICLR 2026) - self-evolving RLVR",
    "SvS (ICLR 2026) - answer-preserving mutations",
    "Prism (arXiv 2603.13309) - 128-cluster diversity",
    "R-Diverse (arXiv 2602.13103) - SAM + MAP",
    "ProRL (arXiv 2505.24864) - diverse prolonged training",
    "DAPO - standardizes G=16"
  ],
  "description": "SACE-RLVR scales D\u00e9j\u00e0Q\u2019s online MAP-Elites co-evolution from GSM-level to competition-level math reasoning through three integrated cores: (1) a 2D topic\u00d7difficulty archive (~40 niches) with ZPD-weighted sampling ensuring smooth difficulty coverage motivated by implicit curriculum theory; (2) proactive niche-level gap identification triggering targeted synthesis with multi-stage verification; and (3) zero-cost Bayesian learnability estimation for archive replacement, applying established Beta-Bernoulli estimation (cf. CurES for sampling, InSight for mutual-information selection, DBB for gradients) to a new decision problem\u2014archive replacement via credible interval comparison\u2014at zero additional inference cost by reusing G=16 training rollouts. The system addresses the pool-exhaustion ceiling of fixed-pool bandit methods (SEC, Actor-Curator) and the over-specialization of unstructured self-evolving approaches (SAGE), while explicitly testing complementarity between bandit-based selection and archive-based synthesis. Key ablations isolate archive dimensionality, synthesis targeting strategy, difficulty spectrum smoothness effects, Bayesian credible-interval vs. point-estimate replacement, and bandit integration.",
  "project_name": "sace_rlvr",
  "source": "web_research",
  "reviewer_response": "Round 9 response: Five substantive changes implemented based on reviewer feedback.\n\n(1) CRITICAL ADDITION - CurES (arXiv 2510.01037): Added as the most directly comparable prior art for Core 3\u2019s Bayesian estimation. CurES models per-problem success rates with Beta posteriors and derives optimal sampling distributions via gradient convergence analysis. Full technical details added to landscape section under new \u2018Bayesian learnability estimation in RLVR\u2019 subsection. Key differentiation established on four dimensions: CurES uses Beta posteriors for SAMPLING from fixed pools (point estimates, separate estimation phase) vs. SACE-RLVR uses Beta posteriors for REPLACEMENT in evolving archives (credible intervals, zero-cost via training rollout reuse). Added to core_problem, opportunity, landscape, inspired_by, key_references, and description.\n\n(2) ADDITION - InSight (arXiv 2603.01907): Added as extending Bayesian RLVR estimation with weighted mutual information decomposing into epistemic and aleatoric components. Shows difficulty-only selection is fundamentally limited. Differentiated: InSight extends Bayesian estimation for fixed-pool selection; SACE-RLVR applies it to archive replacement (different decision problem). Added to landscape (under same Bayesian subsection), inspired_by, key_references.\n\n(3) CORE 3 REFRAMING: Renamed from \u2018Zero-Cost Bayesian Learnability Estimation\u2019 to \u2018Zero-Cost Bayesian Learnability for Archive Replacement.\u2019 Now explicitly acknowledges that Beta-Bernoulli estimation in RLVR is established (CurES, InSight, DBB) and positions Core 3\u2019s novelty as: (a) the decision problem (replacement in evolving archives, not sampling from fixed pools); (b) credible intervals for replacement (not point estimates for sampling); (c) zero-cost via G=16 training rollout reuse (vs. CurES\u2019s separate estimation phase, D\u00e9j\u00e0Q\u2019s K=100 dedicated completions). Updated throughout approach, core_problem, opportunity, description.\n\n(4) SEC 3B DATA CORRECTION: Fixed inverted claim about SEC vs. uniform at 3B scale. Correct numbers from Actor-Curator Table 1: Uniform=20.00%, SEC=23.33%, Actor-Curator=30.00% on AIME24 at Qwen2.5-3B. SEC modestly outperforms uniform (+3.33 absolute, +16.7% relative), while Actor-Curator substantially outperforms both (+10.0 over uniform, +50% relative). The valid analytical point is preserved with correct data: coarser-grained category-level approaches (SEC) yield only modest gains over uniform for harder competition-level problems, while per-problem utility estimation (Actor-Curator) yields much larger gains\u2014supporting the argument for finer-grained approaches.\n\n(5) VENUE TARGET UPDATED: Removed ICLR 2027 (deadline ~Sep 24, 2026 is nearly impossible with 14-18 week timeline starting late May 2026). Retained NeurIPS 2027 and ICML 2027 as realistic targets.\n\n(6) Added change_type field set to \u2018minor\u2019 per reviewer guidance.\n\nAdditional updates: AIME 2024 landscape in landscape section updated to include CurES and InSight results. Gap statement updated to enumerate CurES and InSight as existing Bayesian approaches that do not address archive replacement. Opportunity section restructured from 5 to 6 converging developments, with point (5) now covering established Bayesian estimation as context for our archive-replacement application."
}
```

The complete revised JSON has been produced with all five changes implemented:

1. **CurES added** -- New "Bayesian learnability estimation in RLVR" subsection in landscape with full technical details; referenced in core_problem, opportunity, approach (Core 3), inspired_by, key_references, description, and AIME 2024 landscape.

2. **InSight added** -- Included alongside CurES in the same new landscape subsection; added to inspired_by, key_references, and gap statement.

3. **Core 3 reframed** -- Renamed to "Zero-Cost Bayesian Learnability for Archive Replacement"; explicitly acknowledges CurES/InSight/DBB as establishing Beta-Bernoulli in RLVR; novelty repositioned around (a) the replacement decision problem, (b) credible intervals vs. point estimates, (c) zero-cost rollout reuse.

4. **SEC 3B data corrected** -- The Actor-Curator landscape entry now uses the correct numbers (Uniform=20.00%, SEC=23.33%, Actor-Curator=30.00%) with the valid analytical point that SEC's category-level approach yields only modest gains (+3.33 absolute) vs. Actor-Curator's much larger gains (+10.0 absolute).

5. **ICLR 2027 removed** -- target_venues now contains only NeurIPS 2027 and ICML 2027.

6. **change_type: "minor" added** as requested.

7. **Opportunity restructured** from 5 to 6 converging developments, with point (5) covering established Bayesian estimation and point (6) covering synthesis-verification gap.

agentId: a76f998b25cc34244 (use SendMessage with to: 'a76f998b25cc34244' to continue this agent)
&lt;usage>total_tokens: 58201
tool_uses: 9
duration_ms: 975370&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8402397b-19f7-46a5-8e64-fefd13923e69",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "0e1674fe-9ace-41f5-9573-95588f45171d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping revise a research idea JSON document. I will give you the complete context and you must output the COMPLETE revised JSON.\n\n## Research Context\n\nThis is Round 9 of 10 for a research proposal called SACE-RLVR (Structured Archive Co-Evolution for RLVR). The reviewer has identified critical missing works and a needed reframing. Here is exactly what needs to change:\n\n### Change 1: Add CurES (arXiv 2510.01037) to landscape — CRITICAL\n\nCurES (\"From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs\", Oct 2025, revised Mar 2026) is the most directly comparable prior art for Core 3's Bayesian estimation approach. Technical details:\n\n- Models per-problem success rate with Beta(α,β) posterior, updated as α += successes, β += failures from rollouts\n- Derives optimal sampling distribution ∝ exp(√[p(1-p)]/τ) via gradient convergence analysis\n- Uses POINT ESTIMATES (Beta mean) for sampling probability computation\n- Two-phase: parameter estimation phase (N'=4 rollouts per prompt), then training phase with variance-based rollout allocation\n- Fixed pool: Numina-Math dataset partitioned into 15 subsets\n- Results: Qwen2.5-Math-7B: AIME24 24.58%, MATH-500 84.80%, AMC23 64.38%, +4.82 over GRPO\n- Also: Qwen2.5-Math-1.5B: AIME24 13.33%, MATH-500 77.20%, +3.30 over GRPO\n- Uses VERL training framework\n\nDifferentiation from SACE-RLVR Core 3:\n- CurES: Beta posteriors for SAMPLING (which problem to train on) from fixed pool → SACE-RLVR: Beta posteriors for REPLACEMENT (should this new problem replace an existing archive occupant)\n- CurES: Point estimates (Beta mean) → SACE-RLVR: Credible intervals for replacement\n- CurES: Fixed pool selection → SACE-RLVR: Evolving archive with synthesis\n- CurES: Separate estimation phase → SACE-RLVR: Zero additional cost via G=16 training rollout reuse\n\n### Change 2: Add InSight (arXiv 2603.01907) to landscape\n\nInSight (\"Efficient RLVR Training via Weighted Mutual Information Data Selection\", Mar 2026):\n- Models Bayesian latent success rates with Beta(α,β), prior Beta(1,1)\n- Key innovation: weighted mutual information objective decomposing into difficulty-dependent (aleatoric) + evidence-dependent (epistemic) components\n- Shows difficulty-only selection (like p(1-p)) is fundamentally limited — epistemic uncertainty matters too\n- Temporal discounting on Beta parameters: α_{t+1} = λα_t + (1-λ)α_0 + S_t\n- Results: AIME24 53.75 on Qwen3-4B (+2.30 vs random), up to ~2.2× training acceleration on Countdown\n- Fixed pool (DeepScaler ~40K)\n- Differentiation: InSight extends Bayesian RLVR estimation with epistemic uncertainty; SACE-RLVR applies Bayesian estimation to archive replacement (different decision problem)\n\n### Change 3: Reframe Core 3's novelty claim\n\nOLD framing: \"Zero-Cost Bayesian Learnability Estimation\" positioned as if Beta posteriors in RLVR are novel\nNEW framing: \"Zero-Cost Bayesian Learnability for Archive Replacement\" — applies ESTABLISHED Beta-Bernoulli estimation (cf. CurES for sampling, InSight for mutual-information-based selection, DBB for gradient estimation) to a NEW DECISION PROBLEM: archive replacement via credible interval comparison, at zero additional inference cost. The novelty is:\n(a) The decision problem: replacement in evolving archives (not sampling from fixed pools or gradient estimation)\n(b) Credible intervals for replacement (not point estimates for sampling)\n(c) Zero-cost via G=16 training rollout reuse (vs CurES's separate estimation phase, DéjàQ's K=100 dedicated completions)\n\n### Change 4: SEC 3B data — IMPORTANT CORRECTION\n\nThe reviewer suggested noting that \"SEC (20.0%) underperforms uniform (23.33%) at 3B.\" However, my research shows this is INVERTED. From Actor-Curator's Table 1 at Qwen2.5-3B:\n- Uniform: 20.00% AIME24\n- SEC: 23.33% AIME24  \n- Actor-Curator: 30.00% AIME24\n\nSo SEC modestly outperforms uniform (+3.33 absolute, +16.7% relative), while Actor-Curator substantially outperforms both (+10.0 over uniform, +50% relative). The valid point is: SEC's category-level approach yields only modest gains over uniform on AIME24 at 3B, while Actor-Curator's per-problem utility estimation yields much larger gains — supporting the argument that coarser-grained approaches offer diminishing returns for harder competition-level problems. But I should use the CORRECT numbers, not the reviewer's inverted claim.\n\n### Change 5: Remove ICLR 2027 venue target\n\nWith 14-18 week timeline starting late May 2026, earliest completion is mid-September — ICLR 2027 deadline ~Sep 24, 2026 is nearly impossible. Remove to avoid credibility concerns.\n\n### Additional updates needed throughout:\n- core_problem: mention CurES/InSight establishing Bayesian estimation in RLVR\n- opportunity: note that Bayesian estimation is now established; our contribution is the archive-replacement application + credible intervals + zero cost\n- landscape: add CurES and InSight sections, update references to Core 3\n- approach: reframe Core 3\n- description: update summary\n- key_references: add CurES, InSight\n- target_venues: remove ICLR 2027\n- inspired_by: add CurES and InSight\n- reviewer_response: document all changes for round 9\n\nHere is the COMPLETE original JSON that you must revise. Output the COMPLETE revised JSON with ALL fields:\n\n```json\n{\n  \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\",\n  \"core_problem\": \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the 'sparse policy selection' view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes 'capability boundary collapse' where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Recent bandit-based curriculum approaches address adaptive selection during RL: SEC (arXiv 2505.14970) formulates curriculum as a MAB over problem categories, achieving 17.5% AIME 2024 on Qwen2.5-7B (+27% relative); Actor-Curator (arXiv 2602.20532) extends this with a neural curator achieving 30.0% AIME 2024 on Qwen2.5-3B (+28.6% relative over uniform) with regret guarantees. However, both select from fixed problem pools (12K MATH problems) without synthesis—they optimize WHICH existing problems to train on, but cannot create new problems when the pool lacks adequate coverage for the policy's current frontier. As the policy improves toward competition level, the fraction of useful problems in a fixed pool shrinks, hitting a pool-exhaustion ceiling. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution—but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps, achieving 13.3% AIME 2024—matching the Qwen-2.5-7B base model—and actually degrading AMC 2023 from 57.5% to 52.5%. The fundamental open question is: can we build a system that combines the adaptive selection intelligence of bandit-based methods with persistent coverage-maintaining archives and targeted synthesis for identified gaps at competition level?\",\n  \"opportunity\": \"Five converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic—and multiple empirical findings support diversity's importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) Bandit-based curriculum methods demonstrate the value of adaptive selection but reveal the ceiling of fixed-pool approaches: SEC achieves 17.5% AIME 2024 (Qwen2.5-7B) via MAB over categories; Actor-Curator achieves 30.0% AIME 2024 (Qwen2.5-3B) via neural bandit with regret guarantees—but both select from fixed 12K pools without synthesis or multi-dimensional coverage tracking. The approaches are potentially COMPLEMENTARY: principled bandit selection FROM a coverage-maintaining, synthesis-augmented archive. (5) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K→80K); per-niche survival varies by topic (geometry autoformalization is ~3.7× harder than non-geometry per IndiMathBench, though this reflects formalization-specific difficulty that may not fully transfer to synthesis). VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification with targeted synthesis (vs. reactive instance-level targeting or selection-only bandits), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria.\",\n  \"landscape\": \"**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\\n\\n**Bandit-based adaptive curriculum (critical comparators).** SEC (arXiv 2505.14970) formulates online curriculum selection as a non-stationary MAB where each problem category (difficulty level or problem type) is an arm. Uses TD(0) updates on Q-values derived from absolute advantages, with Boltzmann sampling: p(c) ∝ exp(Q(c)/τ). Selects from fixed training pools (10K problems per domain). Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random 13.8%), 76.1% MATH-500, 51.1% AMC22-23. Categories are 1D (difficulty OR type per domain). SEC-2D variant combines 3 reasoning domains into 9 arms for multi-task learning. Actor-Curator (arXiv 2602.20532) extends beyond SEC's category-level bandits to per-problem utility estimation via a neural curator (Qwen3-0.6B) trained with online stochastic mirror descent (OSMD). Establishes regret bound O(T^{2/3}·V_T^{1/3}) under non-stationary utilities. Selects from fixed pools (12K MATH problems). Qwen2.5-3B: 30.0% AIME 2024, 81.0% MATH-500 (+28.6% relative over uniform 23.3%; beats SEC at 20.0% in matched 3B comparison). ~9% overhead. Key insight: Actor-Curator's per-problem utility estimation is more expressive than SEC's category-level Q-values, yielding consistent gains. Critical differentiation from SACE-RLVR on four dimensions: (a) SELECTION vs. SYNTHESIS—both SEC and Actor-Curator select from fixed pools of existing problems; they cannot synthesize new problems targeting identified gaps. As the policy improves toward competition level, the fraction of useful problems in a fixed 12K pool shrinks (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED optimization—Actor-Curator optimizes aggregate per-problem utility without explicit multi-dimensional coverage constraints, risking concentration on high-utility niches without ensuring breadth (analogous to SAGE's demonstrated over-specialization); (c) STATELESS vs. PERSISTENT—neither maintains a persistent multi-dimensional archive with cross-step coverage tracking; (d) COMPLEMENTARITY—crucially, these approaches compete at different levels: Actor-Curator's bandit selection could serve as the within-archive sampling strategy, combining principled selection WITH coverage-maintaining synthesis. We test this complementarity explicitly.\\n\\n**Balanced difficulty filtering theory.** Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) proves that expected policy improvement is lower-bounded by the variance of task-level success probabilities p(x)(1-p(x)), maximized at p(x)=0.5. Balanced filtering (0.3&lt;p(x)<0.7) achieves +12% on AMC and +10% on AIME with Qwen2.5 models in less than half the training steps of standard GRPO. This theoretical result directly supports our difficulty-aware design: our Bayesian learnability criterion tracks p(1-p) per problem via Beta posteriors, and our archive's ZPD-weighted sampling preferentially selects problems near the difficulty frontier.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\\n\\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\\n\\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold α=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively). On AIME 2024, SAGE achieves 13.3%—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%. This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents. Training dynamics confirm this: over-specialization emerges after ~120 steps (peak 69.5% declining to 61.6% by step 240). Question pool grows 18× (1,136→20,532) as flat filtered dataset without structured organization.\\n\\n**Implicit curriculum theory.** 'The Implicit Curriculum' (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation—not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: 'behavioral diversity is the binding constraint for RL.' RL-PLUS (arXiv 2508.00222) demonstrates 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\\n\\n**Policy-level diversity maintenance (concurrent).** UCPO (arXiv 2605.00365) addresses pass@k diversity collapse at the optimization level rather than the data level, adding a conditional uniformity penalty that redistributes gradient signal toward underrepresented correct solutions. Achieves +10% absolute Pass@64 on AIME 2024 (DeepSeek-7B: 70.0%→80.0%) and +45% equation-level diversity while maintaining competitive Pass@1. Importantly, UCPO modifies the loss function, not the training distribution—making it orthogonal to and potentially complementary with archive-based diversity maintenance. UCPO ensures diversity within the correct solution set for a given problem; SACE-RLVR ensures diversity across the problem distribution.\\n\\n**Lightweight co-evolutionary diversity (concurrent).** Vocabulary Dropout (arXiv 2604.03472) prevents proposer diversity collapse in co-evolutionary frameworks by applying random hard logit masks during problem generation, achieving +4.4 average points on Qwen3-8B (+10.9 AMC, +3.4 AIME 2024, +7.8 AIME 2025) within R-Zero. Demonstrates that diversity collapse is a real bottleneck in co-evolutionary RLVR. Differentiation: VD maintains proposer diversity via stochastic masking; SACE-RLVR provides structured coverage guarantees and interpretable gap identification.\\n\\n**Meta-RL curriculum generation (concurrent).** SOAR (arXiv 2601.18778) uses bi-level meta-RL where a teacher generates stepping-stone problems rewarded by measured student improvement on hard problems. Achieves +9.3% pass@32 on MATH fail@128 tasks (Llama-3.2-3B), recovering 75% of oracle gains from training on the full MATH dataset. Key insight: structural quality of generated problems matters more than solution correctness. Conceptually parallel to our proactive gap identification but uses meta-RL reward signal (measured student improvement) vs. our archive-structure-based gap detection. SOAR operates at the edge of learnability for currently-unsolvable problems; SACE-RLVR maintains coverage across the full difficulty spectrum.\\n\\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\\n\\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%→16.4%; Qwen3-8B AIME24: 16.7→26.0. Proves diversity collapse is real (TTRL pass@16: 32.4→16.7).\\n\\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\\n\\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\\n\\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR—related to our approach but operates at policy gradient level vs. our archive-replacement level.\\n\\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K→80K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry autoformalization has ~3.7× lower success rate than non-geometry (IndiMathBench arXiv 2512.00997: 12.2% vs 44.9% BEq across top models); the paper attributes this partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty. These grounding data inform our per-niche survival estimates.\\n\\n**Verification.** VHG (arXiv 2605.06660): validity gating.\\n\\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\\n\\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\\n\\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\\n\\n**The precise gap.** DéjàQ: 1D, GSM-only. SEC: MAB over categories, 1D, fixed pool. Actor-Curator: per-problem bandit, fixed pool, no coverage tracking. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization, zero AIME improvement over base model. Online Difficulty Filtering: theoretical support for balanced filtering, no archive structure. UCPO: policy-level diversity, no data-level coverage. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification with synthesis, structured coverage tracking, and Bayesian learnability replacement. Moreover, no existing work tests whether bandit-based selection and archive-based synthesis are complementary.\",\n  \"inspired_by\": \"DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + SEC_insight['MAB over problem categories during RL; 17.5% AIME24'] + Actor_Curator_insight['neural bandit with regret guarantees; 30.0% AIME24; ~9% overhead; pool-selection ceiling motivates synthesis'] + Online_Difficulty_Filtering['p(1-p) lower bound on policy improvement; balanced filtering; EACL 2026'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools → over-specialization ~120 steps; 13.3% AIME = base model; AMC degrades'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + UCPO_concurrent['policy-level diversity; +10% Pass@64 AIME; complementary to data-level'] + VocabDropout_concurrent['+4.4 avg; diversity collapse prevention'] + SOAR_concurrent['meta-RL teacher; 75% oracle recovery'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry ~3.7× lower autoformalization success; formalization-specific'] + EVOL_RL_warning['diversity collapse']\",\n  \"approach\": \"[KEEP ORIGINAL APPROACH TEXT BUT MAKE THESE SPECIFIC CHANGES TO CORE 3]\",\n  \"resource_estimate\": \"[KEEP ORIGINAL]\",\n  \"target_venues\": \"[REMOVE ICLR 2027]\",\n  \"level\": \"top-tier\",\n  \"key_references\": \"[ADD CurES AND InSight]\",\n  \"description\": \"[UPDATE SUMMARY]\",\n  \"project_name\": \"sace_rlvr\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": \"[UPDATE FOR ROUND 9]\"\n}\n```\n\nNow, I will write the COMPLETE JSON below. Make EVERY field complete — do not use placeholders or \"[KEEP ORIGINAL]\". I need you to output the actual full text for every single field, modifying where needed per the changes above and keeping the rest intact.\n\nCRITICAL RULES:\n1. The JSON must be valid — escape all quotes inside strings, use \\n for newlines\n2. Every field must be complete, not truncated\n3. The approach field must have the FULL text with Core 3 reframed\n4. The landscape must include the new CurES and InSight sections\n5. The core_problem must reference CurES/InSight in the Bayesian context\n6. Add \"change_type\": \"minor\" field\n7. For the SEC 3B data point, use CORRECT numbers: Uniform=20.00, SEC=23.33, Actor-Curator=30.00. The reviewer's claim that SEC underperforms uniform was inverted. The correct observation is that SEC's category-level gains are MODEST (+3.33 absolute) compared to Actor-Curator's substantial gains (+10.0 absolute), supporting the argument that coarser approaches offer diminishing returns for harder problems.\n8. In the bandit landscape section, fix the line \"beats SEC at 20.0% in matched 3B comparison\" — this should say something like \"SEC achieves 23.33% while uniform achieves only 20.00%; Actor-Curator's per-problem utility yields much larger gains than SEC's category-level approach\"\n\nOutput ONLY the JSON object, nothing else.\n",
    "agentId": "a76f998b25cc34244",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "The environment won't let me run Python to validate. Let me just output the complete JSON directly as my response, which is what the user asked for.\n\nHere is the complete revised JSON:\n\n```json\n{\n  \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\",\n  \"change_type\": \"minor\",\n  \"core_problem\": \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum\\u2014easier problems become learnable first and bootstrap harder ones via a \\u2018relay effect.\\u2019 However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the \\u2018sparse policy selection\\u2019 view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes \\u2018capability boundary collapse\\u2019 where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. D\\u00e9j\\u00e0Q (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial\\u2014maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, D\\u00e9j\\u00e0Q operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Recent bandit-based curriculum approaches address adaptive selection during RL: SEC (arXiv 2505.14970) formulates curriculum as a MAB over problem categories, achieving 17.5% AIME 2024 on Qwen2.5-7B (+27% relative); Actor-Curator (arXiv 2602.20532) extends this with a neural curator achieving 30.0% AIME 2024 on Qwen2.5-3B (+28.6% relative over uniform) with regret guarantees. However, both select from fixed problem pools (12K MATH problems) without synthesis\\u2014they optimize WHICH existing problems to train on, but cannot create new problems when the pool lacks adequate coverage for the policy\\u2019s current frontier. As the policy improves toward competition level, the fraction of useful problems in a fixed pool shrinks, hitting a pool-exhaustion ceiling. Bayesian estimation of per-problem learnability is now an established technique in RLVR curriculum design: CurES (arXiv 2510.01037) models per-problem success rates with Beta(\\u03b1,\\u03b2) posteriors and derives optimal sampling distributions via gradient convergence analysis; InSight (arXiv 2603.01907) extends this with weighted mutual information decomposing into difficulty-dependent and epistemic components; DBB (arXiv 2603.18444) applies Beta-Bernoulli estimation to policy gradient variance reduction. However, all these apply Bayesian estimation to problem SELECTION from fixed pools or gradient estimation\\u2014none applies it to the fundamentally different decision problem of archive REPLACEMENT in evolving archives with synthesis. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)\\u2014but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution\\u2014but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps, achieving 13.3% AIME 2024\\u2014matching the Qwen-2.5-7B base model\\u2014and actually degrading AMC 2023 from 57.5% to 52.5%. The fundamental open question is: can we build a system that combines the adaptive selection intelligence of bandit-based methods with persistent coverage-maintaining archives and targeted synthesis for identified gaps at competition level?\",\n  \"opportunity\": \"Five converging developments create a precise research window. (1) D\\u00e9j\\u00e0Q proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But D\\u00e9j\\u00e0Q\\u2019s 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic\\u2014and multiple empirical findings support diversity\\u2019s importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) Bandit-based curriculum methods demonstrate the value of adaptive selection but reveal the ceiling of fixed-pool approaches: SEC achieves 17.5% AIME 2024 (Qwen2.5-7B) via MAB over categories; Actor-Curator achieves 30.0% AIME 2024 (Qwen2.5-3B) via neural bandit with regret guarantees\\u2014but both select from fixed 12K pools without synthesis or multi-dimensional coverage tracking. The approaches are potentially COMPLEMENTARY: principled bandit selection FROM a coverage-maintaining, synthesis-augmented archive. (5) Bayesian estimation of per-problem learnability is now established in RLVR: CurES derives optimal sampling distributions from Beta posteriors via gradient convergence analysis; InSight extends this with mutual-information-based selection decomposing epistemic and aleatoric uncertainty; DBB applies Beta-Bernoulli estimation to gradient variance reduction. Our contribution applies this established estimation technique to a new decision problem\\u2014archive replacement via credible interval comparison\\u2014at zero additional inference cost by reusing G=16 training rollouts, rather than requiring separate estimation phases (CurES) or dedicated completions (D\\u00e9j\\u00e0Q K=100). (6) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K\\u219280K); per-niche survival varies by topic (geometry autoformalization is ~3.7\\u00d7 harder than non-geometry per IndiMathBench, though this reflects formalization-specific difficulty that may not fully transfer to synthesis). VHG\\u2019s validity-gating separates problem validity from difficulty; MathForge\\u2019s DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification with targeted synthesis (vs. reactive instance-level targeting or selection-only bandits), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria applied to evolving archives rather than fixed-pool selection.\",\n  \"landscape\": \"**Online archive-based co-evolution (direct predecessor).** D\\u00e9j\\u00e0Q (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic \\u2018setting\\u2019 categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only\\u2014competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\\n\\n**Bandit-based adaptive curriculum (critical comparators).** SEC (arXiv 2505.14970) formulates online curriculum selection as a non-stationary MAB where each problem category (difficulty level or problem type) is an arm. Uses TD(0) updates on Q-values derived from absolute advantages, with Boltzmann sampling: p(c) \\u221d exp(Q(c)/\\u03c4). Selects from fixed training pools (10K problems per domain). Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random 13.8%), 76.1% MATH-500, 51.1% AMC22-23. Categories are 1D (difficulty OR type per domain). SEC-2D variant combines 3 reasoning domains into 9 arms for multi-task learning. Actor-Curator (arXiv 2602.20532) extends beyond SEC\\u2019s category-level bandits to per-problem utility estimation via a neural curator (Qwen3-0.6B) trained with online stochastic mirror descent (OSMD). Establishes regret bound O(T^{2/3}\\u00b7V_T^{1/3}) under non-stationary utilities. Selects from fixed pools (12K MATH problems). Qwen2.5-3B: 30.0% AIME 2024, 81.0% MATH-500 (+28.6% relative over uniform 23.3%; in the matched 3B comparison, SEC achieves 23.33% while uniform achieves only 20.00%\\u2014SEC\\u2019s category-level approach yields only modest gains over uniform (+3.33 absolute, +16.7% relative), while Actor-Curator\\u2019s per-problem utility estimation yields much larger gains (+10.0 absolute over uniform, +50% relative), supporting the argument that coarser-grained category-level approaches offer diminishing returns for harder competition-level problems). ~9% overhead. Key insight: Actor-Curator\\u2019s per-problem utility estimation is more expressive than SEC\\u2019s category-level Q-values, yielding consistent gains. Critical differentiation from SACE-RLVR on four dimensions: (a) SELECTION vs. SYNTHESIS\\u2014both SEC and Actor-Curator select from fixed pools of existing problems; they cannot synthesize new problems targeting identified gaps. As the policy improves toward competition level, the fraction of useful problems in a fixed 12K pool shrinks (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED optimization\\u2014Actor-Curator optimizes aggregate per-problem utility without explicit multi-dimensional coverage constraints, risking concentration on high-utility niches without ensuring breadth (analogous to SAGE\\u2019s demonstrated over-specialization); (c) STATELESS vs. PERSISTENT\\u2014neither maintains a persistent multi-dimensional archive with cross-step coverage tracking; (d) COMPLEMENTARITY\\u2014crucially, these approaches compete at different levels: Actor-Curator\\u2019s bandit selection could serve as the within-archive sampling strategy, combining principled selection WITH coverage-maintaining synthesis. We test this complementarity explicitly.\\n\\n**Bayesian learnability estimation in RLVR (critical context for Core 3).** CurES (arXiv 2510.01037, Oct 2025, revised Mar 2026) is the most directly comparable prior art for Bayesian estimation in RLVR curriculum design. Models per-problem success rate with Beta(\\u03b1,\\u03b2) posterior, updated as \\u03b1 += successes, \\u03b2 += failures from rollouts. Derives optimal sampling distribution \\u221d exp(\\u221a[p(1-p)]/\\u03c4) via gradient convergence analysis. Uses point estimates (Beta mean) for sampling probability computation. Two-phase: parameter estimation phase (N'=4 rollouts per prompt), then training phase with variance-based rollout allocation. Fixed pool: Numina-Math dataset partitioned into 15 subsets. Results: Qwen2.5-Math-7B: AIME24 24.58%, MATH-500 84.80%, AMC23 64.38%, +4.82 over GRPO; Qwen2.5-Math-1.5B: AIME24 13.33%, MATH-500 77.20%, +3.30 over GRPO. Uses VERL training framework. Critical differentiation from SACE-RLVR Core 3: (a) CurES uses Beta posteriors for SAMPLING (which problem to train on) from a fixed pool \\u2192 SACE-RLVR uses Beta posteriors for REPLACEMENT (should this new problem replace an existing archive occupant)\\u2014a fundamentally different decision problem; (b) CurES uses point estimates (Beta mean) \\u2192 SACE-RLVR uses credible intervals for replacement decisions; (c) CurES operates on a fixed pool \\u2192 SACE-RLVR operates on an evolving archive with synthesis; (d) CurES requires a separate estimation phase (N'=4 dedicated rollouts per prompt) \\u2192 SACE-RLVR achieves zero additional cost via G=16 training rollout reuse.\\n\\nInSight (arXiv 2603.01907, Mar 2026) extends Bayesian RLVR estimation with weighted mutual information for data selection. Models Bayesian latent success rates with Beta(\\u03b1,\\u03b2), prior Beta(1,1). Key innovation: weighted mutual information objective decomposing into difficulty-dependent (aleatoric) + evidence-dependent (epistemic) components. Demonstrates that difficulty-only selection (like p(1-p)) is fundamentally limited\\u2014epistemic uncertainty matters too. Temporal discounting on Beta parameters: \\u03b1_{t+1} = \\u03bb\\u03b1_t + (1-\\u03bb)\\u03b1_0 + S_t. Results: AIME24 53.75 on Qwen3-4B (+2.30 vs random), up to ~2.2\\u00d7 training acceleration on Countdown. Fixed pool (DeepScaler ~40K). Differentiation: InSight extends Bayesian RLVR estimation with epistemic uncertainty for problem selection from fixed pools; SACE-RLVR applies Bayesian estimation to archive replacement (different decision problem) in evolving archives with synthesis.\\n\\n**Balanced difficulty filtering theory.** Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) proves that expected policy improvement is lower-bounded by the variance of task-level success probabilities p(x)(1-p(x)), maximized at p(x)=0.5. Balanced filtering (0.3&lt;p(x)<0.7) achieves +12% on AMC and +10% on AIME with Qwen2.5 models in less than half the training steps of standard GRPO. This theoretical result directly supports our difficulty-aware design: our Bayesian learnability criterion tracks p(1-p) per problem via Beta posteriors, and our archive\\u2019s ZPD-weighted sampling preferentially selects problems near the difficulty frontier.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard \\u22640.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\\n\\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver\\u2019s specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for \\u2018desirable difficulty.\\u2019 Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\\n\\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold \\u03b1=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively). On AIME 2024, SAGE achieves 13.3%\\u2014matching the Qwen-2.5-7B base model (also 13.3%)\\u2014and degrades AMC 2023 from 57.5% to 52.5%. This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance\\u2014precisely the over-specialization that structured archive-based diversity maintenance prevents. Training dynamics confirm this: over-specialization emerges after ~120 steps (peak 69.5% declining to 61.6% by step 240). Question pool grows 18\\u00d7 (1,136\\u219220,532) as flat filtered dataset without structured organization.\\n\\n**Implicit curriculum theory.** \\u2018The Implicit Curriculum\\u2019 (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation\\u2014not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR \\u2018polarizes\\u2019\\u2014sharpening some primitives while sacrificing others\\u2014and since multi-step success compounds multiplicatively (P(q) \\u221d \\u220fP(s\\u2c7c)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: \\u2018behavioral diversity is the binding constraint for RL.\\u2019 RL-PLUS (arXiv 2508.00222) demonstrates \\u2018capability boundary collapse\\u2019\\u2014pass@1 up, pass@128 down\\u2014with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\\n\\n**Policy-level diversity maintenance (concurrent).** UCPO (arXiv 2605.00365) addresses pass@k diversity collapse at the optimization level rather than the data level, adding a conditional uniformity penalty that redistributes gradient signal toward underrepresented correct solutions. Achieves +10% absolute Pass@64 on AIME 2024 (DeepSeek-7B: 70.0%\\u219280.0%) and +45% equation-level diversity while maintaining competitive Pass@1. Importantly, UCPO modifies the loss function, not the training distribution\\u2014making it orthogonal to and potentially complementary with archive-based diversity maintenance. UCPO ensures diversity within the correct solution set for a given problem; SACE-RLVR ensures diversity across the problem distribution.\\n\\n**Lightweight co-evolutionary diversity (concurrent).** Vocabulary Dropout (arXiv 2604.03472) prevents proposer diversity collapse in co-evolutionary frameworks by applying random hard logit masks during problem generation, achieving +4.4 average points on Qwen3-8B (+10.9 AMC, +3.4 AIME 2024, +7.8 AIME 2025) within R-Zero. Demonstrates that diversity collapse is a real bottleneck in co-evolutionary RLVR. Differentiation: VD maintains proposer diversity via stochastic masking; SACE-RLVR provides structured coverage guarantees and interpretable gap identification.\\n\\n**Meta-RL curriculum generation (concurrent).** SOAR (arXiv 2601.18778) uses bi-level meta-RL where a teacher generates stepping-stone problems rewarded by measured student improvement on hard problems. Achieves +9.3% pass@32 on MATH fail@128 tasks (Llama-3.2-3B), recovering 75% of oracle gains from training on the full MATH dataset. Key insight: structural quality of generated problems matters more than solution correctness. Conceptually parallel to our proactive gap identification but uses meta-RL reward signal (measured student improvement) vs. our archive-structure-based gap detection. SOAR operates at the edge of learnability for currently-unsolvable problems; SACE-RLVR maintains coverage across the full difficulty spectrum.\\n\\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\\n\\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%\\u219216.4%; Qwen3-8B AIME24: 16.7\\u219226.0. Proves diversity collapse is real (TTRL pass@16: 32.4\\u219216.7).\\n\\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\\n\\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\\n\\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR\\u2014related to our approach but operates at policy gradient level vs. our archive-replacement level.\\n\\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K\\u219280K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry autoformalization has ~3.7\\u00d7 lower success rate than non-geometry (IndiMathBench arXiv 2512.00997: 12.2% vs 44.9% BEq across top models); the paper attributes this partly to Mathlib\\u2019s lacking support for Olympiad-style geometry\\u2014a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty. These grounding data inform our per-niche survival estimates.\\n\\n**Verification.** VHG (arXiv 2605.06660): validity gating.\\n\\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Bayesian curriculum: CurES 24.58% (7B-Math), InSight 53.75% (Qwen3-4B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\\n\\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\\n\\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\\n\\n**The precise gap.** D\\u00e9j\\u00e0Q: 1D, GSM-only. SEC: MAB over categories, 1D, fixed pool. Actor-Curator: per-problem bandit, fixed pool, no coverage tracking. CurES: Beta posteriors for sampling from fixed pool, point estimates, separate estimation phase. InSight: Beta posteriors with mutual information for selection from fixed pool. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization, zero AIME improvement over base model. Online Difficulty Filtering: theoretical support for balanced filtering, no archive structure. UCPO: policy-level diversity, no data-level coverage. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification with synthesis, structured coverage tracking, and Bayesian learnability replacement applied to evolving archives (rather than fixed-pool selection). Moreover, no existing work tests whether bandit-based selection and archive-based synthesis are complementary.\",\n  \"inspired_by\": \"D\\u00e9j\\u00e0Q_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + SEC_insight['MAB over problem categories during RL; 17.5% AIME24'] + Actor_Curator_insight['neural bandit with regret guarantees; 30.0% AIME24; ~9% overhead; pool-selection ceiling motivates synthesis'] + CurES_insight['Beta posteriors for sampling; gradient convergence analysis; +4.82 over GRPO; establishes Bayesian estimation in RLVR'] + InSight_insight['weighted mutual information; epistemic + aleatoric decomposition; temporal discounting; extends Bayesian RLVR estimation'] + Online_Difficulty_Filtering['p(1-p) lower bound on policy improvement; balanced filtering; EACL 2026'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools \\u2192 over-specialization ~120 steps; 13.3% AIME = base model; AMC degrades'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + UCPO_concurrent['policy-level diversity; +10% Pass@64 AIME; complementary to data-level'] + VocabDropout_concurrent['+4.4 avg; diversity collapse prevention'] + SOAR_concurrent['meta-RL teacher; 75% oracle recovery'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry ~3.7\\u00d7 lower autoformalization success; formalization-specific'] + EVOL_RL_warning['diversity collapse']\",\n  \"approach\": \"SACE-RLVR integrates three tightly-coupled cores into a unified online co-evolutionary RLVR system.\\n\\n**Core 1: Multi-Dimensional MAP-Elites Archive with ZPD-Weighted Sampling.** We extend D\\u00e9j\\u00e0Q\\u2019s 1D thematic archive to a 2D archive indexed by (topic, difficulty), with ~8 topic categories and ~5 difficulty levels yielding ~40 niches. Each niche stores the top-K (K=3) problems ranked by Bayesian learnability (see Core 3). The difficulty dimension is estimated from rollout success rates during training (aligned with CLPO\\u2019s online assessment but with finer granularity: 5 bins vs. 3). Archive initialization uses a seed dataset of ~2K competition-level problems (e.g., from MATH Level 4-5, AMC, AIME). During training, batch construction uses ZPD-weighted sampling: each niche\\u2019s sampling weight is proportional to its aggregate learnability score, biased toward the zone of proximal development (p \\u2208 [0.2, 0.8]) where learning signal is strongest per the Online Difficulty Filtering lower bound. Coverage enforcement ensures each topic receives minimum representation per epoch, preventing the over-specialization demonstrated by SAGE. The archive evolves continuously as Core 2 proposes candidates and Core 3 adjudicates replacement.\\n\\n**Core 2: Proactive Niche-Level Gap Identification and Targeted Synthesis.** Rather than D\\u00e9j\\u00e0Q\\u2019s random mutation or Socratic-Zero\\u2019s reactive instance-level targeting, we implement proactive gap identification at the niche level. After each training epoch, we compute a coverage map: for each niche (topic, difficulty), we track occupancy count, average learnability, and learnability trend (improving/declining/stagnant). Gap identification triggers synthesis when: (a) a niche is empty or under-occupied (coverage gap); (b) all problems in a niche have learnability below threshold (the policy has \\u2018graduated\\u2019 and needs harder problems); (c) learnability is declining across a difficulty band (potential relay-effect blockage). Synthesis uses the policy model itself with structured prompts specifying the target topic, difficulty level, and (for weakness targeting) specific error patterns extracted from failed rollouts in adjacent niches. Multi-stage verification follows: (1) format/solvability check via symbolic solver where applicable (SymPy, Lean4 for formalizable subsets); (2) difficulty calibration via G=4 quick rollouts; (3) novelty check against archive occupants via embedding similarity. We target ~30% end-to-end survival rate informed by SAND-Math (~38%) and SPARQ (~25%), with per-topic variation (geometry expected ~15% vs. algebra ~40% based on IndiMathBench difficulty ratios, adjusted for synthesis vs. formalization). Invalid problems are discarded without penalty; valid problems proceed to Core 3 for replacement adjudication.\\n\\n**Core 3: Zero-Cost Bayesian Learnability for Archive Replacement.** This core applies established Beta-Bernoulli estimation\\u2014as used by CurES for sampling (arXiv 2510.01037), InSight for mutual-information-based selection (arXiv 2603.01907), and DBB for gradient estimation (arXiv 2603.18444)\\u2014to a new decision problem: archive replacement in evolving archives. For each problem x in the archive, we maintain a Beta(\\u03b1_x, \\u03b2_x) posterior over its true success rate, initialized with prior Beta(1,1). Each time x appears in a training batch with G=16 rollouts, we observe k successes out of G attempts and update: \\u03b1_x += k, \\u03b2_x += (G-k). The key insight enabling zero additional cost: we reuse the G=16 rollouts already required for GRPO training\\u2014no separate estimation phase is needed (unlike CurES\\u2019s dedicated N\\u2019=4 estimation rollouts per prompt, or D\\u00e9j\\u00e0Q\\u2019s K=100 dedicated completions). Learnability is computed as the posterior mean of p(1-p): E[p(1-p)] = \\u03b1\\u03b2/[(\\u03b1+\\u03b2)^2(\\u03b1+\\u03b2+1)]. The novelty of Core 3 lies not in the Beta-Bernoulli estimation itself (which is now established in RLVR via CurES, InSight, and DBB), but in three aspects: (a) The decision problem: replacement in evolving archives rather than sampling from fixed pools or gradient estimation. When a candidate problem x\\u2019 is proposed for a niche occupied by x, we compare credible intervals: x\\u2019 replaces x if the lower bound of x\\u2019\\u2019s 80% credible interval for learnability exceeds the upper bound of x\\u2019s interval, providing conservative replacement that accounts for estimation uncertainty. (b) Credible intervals rather than point estimates: CurES uses point estimates (Beta mean) for sampling probabilities; we use full posterior credible intervals to make replacement decisions that appropriately account for uncertainty\\u2014a new problem with few observations should not displace a well-characterized occupant based on a noisy point estimate. (c) Zero additional inference cost: by reusing G=16 training rollouts, we avoid CurES\\u2019s separate estimation phase and D\\u00e9j\\u00e0Q\\u2019s K=100 dedicated completions. Temporal discounting (inspired by InSight\\u2019s \\u03bb-discounting on Beta parameters) prevents stale estimates: \\u03b1_x \\u2192 \\u03bb\\u03b1_x + (1-\\u03bb), \\u03b2_x \\u2192 \\u03bb\\u03b2_x + (1-\\u03bb) with \\u03bb=0.95, ensuring the posterior adapts as the policy evolves.\\n\\n**Integration and training loop.** Each training step: (1) Sample a batch from the archive using ZPD-weighted niche sampling; (2) Run G=16 GRPO rollouts; (3) Update Beta posteriors for all sampled problems (zero cost\\u2014reuses rollouts from step 2); (4) Compute GRPO policy gradient with DGPO weighting (MathForge); (5) Every N steps, run gap identification and trigger synthesis for identified gaps; (6) Adjudicate replacement for synthesis candidates and any archive occupants whose learnability has dropped below threshold. The system maintains a coverage dashboard tracking per-niche occupancy, learnability distributions, and difficulty spectrum smoothness.\\n\\n**Ablation design.** A1: Archive dimensionality (1D topic-only vs. 2D topic\\u00d7difficulty vs. flat pool). A2: Synthesis targeting (proactive niche-level vs. random mutation vs. no synthesis). A3: Difficulty spectrum smoothness (does smoother coverage correlate with faster convergence, testing the relay-effect hypothesis from implicit curriculum theory?). A4: Bayesian replacement via credible intervals vs. point-estimate replacement vs. D\\u00e9j\\u00e0Q\\u2019s direct fitness comparison. A5: Bandit complementarity (uniform archive sampling vs. SEC-style MAB vs. Actor-Curator-style neural bandit over archive niches). A6: G=16 rollout reuse vs. dedicated estimation rollouts (testing zero-cost claim).\\n\\n**Extensions.** E1: DGPO integration (MathForge\\u2019s difficulty-aware weighting). E2: UCPO integration (policy-level diversity maintenance, orthogonal to data-level). E3: Vocabulary Dropout for synthesis diversity. E4: Actor-Curator as within-archive sampling strategy.\",\n  \"resource_estimate\": \"Base model: Qwen2.5-7B (primary) and Qwen2.5-3B (scaling comparison). Training: 8\\u00d7A100 80GB GPUs, ~500 GRPO steps with G=16 rollouts. Estimated training time: ~72-96 hours for main run, ~200 hours total including ablations. Synthesis overhead: ~15-20% of training compute (amortized over gap identification intervals of N=50 steps). Verification overhead: ~5-10% (symbolic checking is fast; difficulty calibration G=4 rollouts are the bottleneck). Archive maintenance: negligible (<1% of compute). Total compute budget: ~2,000-3,000 A100-hours including all ablations and baselines. Key infrastructure: VERL or OpenRLHF training framework, SymPy for symbolic verification, embedding model for novelty checking. Timeline: 14-18 weeks. Weeks 1-3: infrastructure (archive data structures, GRPO training loop, synthesis pipeline). Weeks 4-6: Core 1+3 implementation and validation on MATH-500. Weeks 7-9: Core 2 synthesis pipeline with verification. Weeks 10-12: full system integration and main experiments. Weeks 13-15: ablation studies. Weeks 16-18: analysis, writing, submission preparation.\",\n  \"target_venues\": [\"NeurIPS 2027\", \"ICML 2027\"],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"D\\u00e9j\\u00e0Q (arXiv 2601.01931) - online MAP-Elites co-evolution for RLVR\",\n    \"The Implicit Curriculum (arXiv 2602.14872, ICML 2026) - relay vs grokking regimes\",\n    \"SEC (arXiv 2505.14970) - MAB over problem categories for RLVR curriculum\",\n    \"Actor-Curator (arXiv 2602.20532) - neural bandit with regret guarantees for RLVR\",\n    \"CurES (arXiv 2510.01037) - Beta posteriors for sampling; gradient convergence analysis for RLVR curriculum\",\n    \"InSight (arXiv 2603.01907) - weighted mutual information with epistemic+aleatoric decomposition for RLVR data selection\",\n    \"Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) - p(1-p) lower bound\",\n    \"CLPO (arXiv 2509.25004) - online curriculum, 50% AIME 2024\",\n    \"Socratic-Zero (arXiv 2509.24726) - three-agent co-evolution\",\n    \"SAGE (arXiv 2603.15255) - flat pools lead to over-specialization\",\n    \"RL-PLUS (arXiv 2508.00222) - capability boundary collapse\",\n    \"Sharper Primitives (arXiv 2602.08281) - multiplicative compounding\",\n    \"Tailor (arXiv 2511.12429) - behavioral diversity as binding constraint\",\n    \"Sparse Policy Selection (arXiv 2605.06241) - RL modifies 1-3% of tokens\",\n    \"UCPO (arXiv 2605.00365) - policy-level diversity maintenance\",\n    \"Vocabulary Dropout (arXiv 2604.03472) - diversity collapse prevention\",\n    \"SOAR (arXiv 2601.18778) - meta-RL curriculum generation\",\n    \"MathForge/DGPO (arXiv 2601.20614, ICLR 2026) - difficulty-aware optimization\",\n    \"VCRL (arXiv 2509.19803) - reward variance as curriculum signal\",\n    \"MC-GRPO (arXiv 2601.22582) - rollout count ablation\",\n    \"Gradient Starvation (arXiv 2605.07689) - gradient degeneracy analysis\",\n    \"DBB (arXiv 2603.18444) - Bayesian Beta-Bernoulli for RLVR gradients\",\n    \"SAND-Math (arXiv 2507.20527) - synthesis survival rates\",\n    \"SPARQ (arXiv 2506.06499) - QD survival rates\",\n    \"VHG (arXiv 2605.06660) - validity gating\",\n    \"EVOL-RL (arXiv 2509.15194) - novelty-aware diversity\",\n    \"Bidirectional Curriculum Generation (arXiv 2603.05120) - 4-agent framework\",\n    \"DART-Math (arXiv 2407.13690) - query coverage dropout\",\n    \"FLAMES (arXiv 2508.16514) - self-consistency filtering\",\n    \"IndiMathBench (arXiv 2512.00997) - geometry difficulty baseline\",\n    \"SwS (NeurIPS 2025) - offline weakness targeting\",\n    \"STAT (arXiv 2510.10023) - Missing-Skill-Profiles\",\n    \"R-Zero (ICLR 2026) - self-evolving RLVR\",\n    \"SvS (ICLR 2026) - answer-preserving mutations\",\n    \"Prism (arXiv 2603.13309) - 128-cluster diversity\",\n    \"R-Diverse (arXiv 2602.13103) - SAM + MAP\",\n    \"ProRL (arXiv 2505.24864) - diverse prolonged training\",\n    \"DAPO - standardizes G=16\"\n  ],\n  \"description\": \"SACE-RLVR scales D\\u00e9j\\u00e0Q\\u2019s online MAP-Elites co-evolution from GSM-level to competition-level math reasoning through three integrated cores: (1) a 2D topic\\u00d7difficulty archive (~40 niches) with ZPD-weighted sampling ensuring smooth difficulty coverage motivated by implicit curriculum theory; (2) proactive niche-level gap identification triggering targeted synthesis with multi-stage verification; and (3) zero-cost Bayesian learnability estimation for archive replacement, applying established Beta-Bernoulli estimation (cf. CurES for sampling, InSight for mutual-information selection, DBB for gradients) to a new decision problem\\u2014archive replacement via credible interval comparison\\u2014at zero additional inference cost by reusing G=16 training rollouts. The system addresses the pool-exhaustion ceiling of fixed-pool bandit methods (SEC, Actor-Curator) and the over-specialization of unstructured self-evolving approaches (SAGE), while explicitly testing complementarity between bandit-based selection and archive-based synthesis. Key ablations isolate archive dimensionality, synthesis targeting strategy, difficulty spectrum smoothness effects, Bayesian credible-interval vs. point-estimate replacement, and bandit integration.\",\n  \"project_name\": \"sace_rlvr\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": \"Round 9 response: Five substantive changes implemented based on reviewer feedback.\\n\\n(1) CRITICAL ADDITION - CurES (arXiv 2510.01037): Added as the most directly comparable prior art for Core 3\\u2019s Bayesian estimation. CurES models per-problem success rates with Beta posteriors and derives optimal sampling distributions via gradient convergence analysis. Full technical details added to landscape section under new \\u2018Bayesian learnability estimation in RLVR\\u2019 subsection. Key differentiation established on four dimensions: CurES uses Beta posteriors for SAMPLING from fixed pools (point estimates, separate estimation phase) vs. SACE-RLVR uses Beta posteriors for REPLACEMENT in evolving archives (credible intervals, zero-cost via training rollout reuse). Added to core_problem, opportunity, landscape, inspired_by, key_references, and description.\\n\\n(2) ADDITION - InSight (arXiv 2603.01907): Added as extending Bayesian RLVR estimation with weighted mutual information decomposing into epistemic and aleatoric components. Shows difficulty-only selection is fundamentally limited. Differentiated: InSight extends Bayesian estimation for fixed-pool selection; SACE-RLVR applies it to archive replacement (different decision problem). Added to landscape (under same Bayesian subsection), inspired_by, key_references.\\n\\n(3) CORE 3 REFRAMING: Renamed from \\u2018Zero-Cost Bayesian Learnability Estimation\\u2019 to \\u2018Zero-Cost Bayesian Learnability for Archive Replacement.\\u2019 Now explicitly acknowledges that Beta-Bernoulli estimation in RLVR is established (CurES, InSight, DBB) and positions Core 3\\u2019s novelty as: (a) the decision problem (replacement in evolving archives, not sampling from fixed pools); (b) credible intervals for replacement (not point estimates for sampling); (c) zero-cost via G=16 training rollout reuse (vs. CurES\\u2019s separate estimation phase, D\\u00e9j\\u00e0Q\\u2019s K=100 dedicated completions). Updated throughout approach, core_problem, opportunity, description.\\n\\n(4) SEC 3B DATA CORRECTION: Fixed inverted claim about SEC vs. uniform at 3B scale. Correct numbers from Actor-Curator Table 1: Uniform=20.00%, SEC=23.33%, Actor-Curator=30.00% on AIME24 at Qwen2.5-3B. SEC modestly outperforms uniform (+3.33 absolute, +16.7% relative), while Actor-Curator substantially outperforms both (+10.0 over uniform, +50% relative). The valid analytical point is preserved with correct data: coarser-grained category-level approaches (SEC) yield only modest gains over uniform for harder competition-level problems, while per-problem utility estimation (Actor-Curator) yields much larger gains\\u2014supporting the argument for finer-grained approaches.\\n\\n(5) VENUE TARGET UPDATED: Removed ICLR 2027 (deadline ~Sep 24, 2026 is nearly impossible with 14-18 week timeline starting late May 2026). Retained NeurIPS 2027 and ICML 2027 as realistic targets.\\n\\n(6) Added change_type field set to \\u2018minor\\u2019 per reviewer guidance.\\n\\nAdditional updates: AIME 2024 landscape in landscape section updated to include CurES and InSight results. Gap statement updated to enumerate CurES and InSight as existing Bayesian approaches that do not address archive replacement. Opportunity section restructured from 5 to 6 converging developments, with point (5) now covering established Bayesian estimation as context for our archive-replacement application.\"\n}\n```\n\nThe complete revised JSON has been produced with all five changes implemented:\n\n1. **CurES added** -- New \"Bayesian learnability estimation in RLVR\" subsection in landscape with full technical details; referenced in core_problem, opportunity, approach (Core 3), inspired_by, key_references, description, and AIME 2024 landscape.\n\n2. **InSight added** -- Included alongside CurES in the same new landscape subsection; added to inspired_by, key_references, and gap statement.\n\n3. **Core 3 reframed** -- Renamed to \"Zero-Cost Bayesian Learnability for Archive Replacement\"; explicitly acknowledges CurES/InSight/DBB as establishing Beta-Bernoulli in RLVR; novelty repositioned around (a) the replacement decision problem, (b) credible intervals vs. point estimates, (c) zero-cost rollout reuse.\n\n4. **SEC 3B data corrected** -- The Actor-Curator landscape entry now uses the correct numbers (Uniform=20.00%, SEC=23.33%, Actor-Curator=30.00%) with the valid analytical point that SEC's category-level approach yields only modest gains (+3.33 absolute) vs. Actor-Curator's much larger gains (+10.0 absolute).\n\n5. **ICLR 2027 removed** -- target_venues now contains only NeurIPS 2027 and ICML 2027.\n\n6. **change_type: \"minor\" added** as requested.\n\n7. **Opportunity restructured** from 5 to 6 converging developments, with point (5) covering established Bayesian estimation and point (6) covering synthesis-verification gap."
      }
    ],
    "totalDurationMs": 975370,
    "totalTokens": 58201,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 45236,
      "output_tokens": 12874,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 90
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12874,
          "cache_read_input_tokens": 45236,
          "cache_creation_input_tokens": 90,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 90,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 3,
      "bashCount": 4,
      "editFileCount": 2,
      "linesAdded": 113,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "8402397b-19f7-46a5-8e64-fefd13923e69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 57 · 2026-05-28T04:02:10.226Z_

```json
{
  "parentUuid": "0e1674fe-9ace-41f5-9573-95588f45171d",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0e9c985f-12a8-4122-8f9a-9eed7cb60592",
  "timestamp": "2026-05-28T04:02:10.226Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "0e9c985f-12a8-4122-8f9a-9eed7cb60592",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise RLVR archive approach for CurES acknowledgment",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Assistant

_source line 60 · 2026-05-28T04:02:35.158Z_

<details><summary>Logged reasoning block</summary>

```text
The agent has produced a comprehensive revised JSON. Let me review it carefully to make sure all the changes are correct and complete, and that nothing critical was missed or introduced incorrectly.

Let me check each change:

1. **CurES added** - Yes, added in landscape, core_problem, opportunity, approach, inspired_by, key_references, description ✓
2. **InSight added** - Yes, added similarly ✓
3. **Core 3 reframed** - Yes, renamed and repositioned ✓


4. **SEC 3B data corrected** - Yes, correct numbers used ✓
5. **ICLR 2027 removed** - Yes ✓
6. **change_type: "minor"** - Yes ✓

But I'm noticing some significant divergence from the original structure. The `approach` field has been substantially simplified compared to the original's detailed breakdown across Core 1, Core 2, Core 3, Extensions E1-E4, Training Loop, Baselines, Ablations, Evaluation, and Key Analyses. The `resource_estimate` has also been restructured considerably from its original format.

Looking at what the agent produced, I can see the `approach` was shortened and reorganized, the `resource_estimate` was flattened from a structured object with `manual`, `human_in_loop`, and `auto_research` sub-objects into plain text, and the `target_venues` lost their descriptive text. I need to reconstruct the full JSON carefully, preserving the original's detailed structure while incorporating the specific changes requested—particularly the new sections on CurES, InSight, and Core 3 updates.

Going through each field systematically: the title and change_type stay as is, but the core_problem needs CurES and InSight context woven in. The opportunity section needs to expand from 5 to 6 points with Bayesian estimation. The landscape requires adding CurES and InSight sections, correcting the SEC 3B numbers, and updating the gap statement and AIME landscape. I need to add CurES and InSight to inspired_by, and most importantly, restore the full original detail in approach while reframing only the Core 3 section—the agent oversimplified this significantly. The resource_estimate needs to return to its original structured format with the three sub-objects.

Now I'm constructing the complete JSON output, merging the agent's solid work on new sections with the original's granular detail where it matters most.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e9c985f-12a8-4122-8f9a-9eed7cb60592",
  "isSidechain": false,
  "requestId": "req_011CbUJRqwZHLqV2EPNh1cLS",
  "type": "assistant",
  "uuid": "8f857240-2408-4c34-b9d8-fa5d012e8ed6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhWgjTmSVbag6GF5entABj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22059,
      "cache_read_input_tokens": 44567,
      "output_tokens": 1716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1716,
          "cache_read_input_tokens": 44567,
          "cache_creation_input_tokens": 22059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22059
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

_source line 61 · 2026-05-28T04:02:35.783Z_

I need to verify the agent's output carefully — it appears to have significantly simplified the `approach` and `resource_estimate` fields compared to the original. Let me check and fix these critical sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f857240-2408-4c34-b9d8-fa5d012e8ed6",
  "isSidechain": false,
  "requestId": "req_011CbUJRqwZHLqV2EPNh1cLS",
  "type": "assistant",
  "uuid": "e1d11d42-58da-4d0f-b355-ff6db875c1f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhWgjTmSVbag6GF5entABj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22059,
      "cache_read_input_tokens": 44567,
      "output_tokens": 1716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1716,
          "cache_read_input_tokens": 44567,
          "cache_creation_input_tokens": 22059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22059
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

_source line 62 · 2026-05-28T04:02:57.000Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KVyEoT4RSzDK6oLb47KNF8`</summary>

```json
{
  "description": "Verify approach completeness",
  "prompt": "I have an original research proposal `approach` field that is very detailed (about 5000 words) and a revised version that appears to have been shortened to about 2000 words, losing critical details about baselines, ablation specifics, evaluation benchmarks, key analyses, extensions, training loop details, per-niche survival estimates, and resource breakdowns.\n\nI need you to tell me: given the following original approach text, what specific sections/details would be lost if I used the shortened version? Just list the missing sections/details concisely.\n\nORIGINAL APPROACH (abbreviated section headers):\n- Design Motivation: Why Coverage Matters (Two Independent Arguments)\n  - Argument 1: Relay-regime-inspired smooth difficulty coverage\n  - Argument 2: Broad coverage prevents capability boundary collapse\n  - Why archives with synthesis vs. bandit selection from fixed pools\n- CORE INNOVATION 1: 2D Learnability Archive (50 cells) - 10 difficulty bins × 5 topics, M=10 problems per cell, topic classification, replacement criterion\n- CORE INNOVATION 2: Proactive Gap-Targeted Synthesis with Verification - 3-stage VHG-inspired verification, detailed per-niche survival estimates (Easy-medium ~30-50%, Medium-hard ~15-25%, Geometry ~10-20%, Extreme ~3-8%), graceful degradation, total per refresh cycle ~2,750-6,000 candidates, ~142 GPU-hrs\n- CORE INNOVATION 3: Zero-Cost Bayesian Learnability Estimation - G=16 justification, Beta-Bernoulli, VCRL insight\n- EXTENSIONS (E1-E4): Cross-niche SvS seeding, James-Stein shrinkage, DGPO policy updates, Archive sampling strategy including Actor-Curator-style variant\n- Training Loop: VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary, 5-step loop, 50-step refresh, ~20-25% overhead\n- AIME Contextualization\n- Baselines (8): DéjàQ-comp, CLPO, Socratic-Zero, SAGE, Actor-Curator, EVOL-RL, MathForge, GRPO\n- Ablations (7): A1-A7 with specific descriptions\n- Evaluation: AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench, pass@1 AND pass@k\n- Key Analyses (8): Coverage heatmaps, per-cell benchmark contribution, emergent curriculum, synthesis efficiency, convergence speed, capability boundary, structured vs flat, selection vs synthesis\n\nPlease list the sections/details that would be lost in the shortened version. Report in under 300 words.\n",
  "model": "haiku"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1d11d42-58da-4d0f-b355-ff6db875c1f3",
  "isSidechain": false,
  "requestId": "req_011CbUJRqwZHLqV2EPNh1cLS",
  "type": "assistant",
  "uuid": "9340f2ae-0ca9-40a7-b472-70ddfe8d2900",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhWgjTmSVbag6GF5entABj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22059,
      "cache_read_input_tokens": 44567,
      "output_tokens": 1716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1716,
          "cache_read_input_tokens": 44567,
          "cache_creation_input_tokens": 22059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22059
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

_source line 63 · 2026-05-28T04:03:00.087Z_

<details><summary>↩ Tool result · `toolu_01KVyEoT4RSzDK6oLb47KNF8`</summary>

```text
I'd be happy to help identify what would be lost, but I need to see both versions of the approach text to make a precise comparison. Could you provide:

1. The original full approach text (the ~5000 word version)
2. The shortened approach text (the ~2000 word version)

Once I have both documents, I can systematically compare them and identify exactly which sections, quantitative details, and analyses are missing in the shortened version.

You can either:
- Paste them directly in your next message
- Provide file paths if they're stored locally
- Share the relevant text in any format you have available

agentId: aa3c4ad436115de96 (use SendMessage with to: 'aa3c4ad436115de96' to continue this agent)
&lt;usage>total_tokens: 18386
tool_uses: 0
duration_ms: 3082&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9340f2ae-0ca9-40a7-b472-70ddfe8d2900",
  "isSidechain": false,
  "promptId": "fdf615fd-4027-45f0-aece-84d06b280be4",
  "type": "user",
  "uuid": "84d11516-92a4-4e48-838d-f22144c9eb16",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I have an original research proposal `approach` field that is very detailed (about 5000 words) and a revised version that appears to have been shortened to about 2000 words, losing critical details about baselines, ablation specifics, evaluation benchmarks, key analyses, extensions, training loop details, per-niche survival estimates, and resource breakdowns.\n\nI need you to tell me: given the following original approach text, what specific sections/details would be lost if I used the shortened version? Just list the missing sections/details concisely.\n\nORIGINAL APPROACH (abbreviated section headers):\n- Design Motivation: Why Coverage Matters (Two Independent Arguments)\n  - Argument 1: Relay-regime-inspired smooth difficulty coverage\n  - Argument 2: Broad coverage prevents capability boundary collapse\n  - Why archives with synthesis vs. bandit selection from fixed pools\n- CORE INNOVATION 1: 2D Learnability Archive (50 cells) - 10 difficulty bins × 5 topics, M=10 problems per cell, topic classification, replacement criterion\n- CORE INNOVATION 2: Proactive Gap-Targeted Synthesis with Verification - 3-stage VHG-inspired verification, detailed per-niche survival estimates (Easy-medium ~30-50%, Medium-hard ~15-25%, Geometry ~10-20%, Extreme ~3-8%), graceful degradation, total per refresh cycle ~2,750-6,000 candidates, ~142 GPU-hrs\n- CORE INNOVATION 3: Zero-Cost Bayesian Learnability Estimation - G=16 justification, Beta-Bernoulli, VCRL insight\n- EXTENSIONS (E1-E4): Cross-niche SvS seeding, James-Stein shrinkage, DGPO policy updates, Archive sampling strategy including Actor-Curator-style variant\n- Training Loop: VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary, 5-step loop, 50-step refresh, ~20-25% overhead\n- AIME Contextualization\n- Baselines (8): DéjàQ-comp, CLPO, Socratic-Zero, SAGE, Actor-Curator, EVOL-RL, MathForge, GRPO\n- Ablations (7): A1-A7 with specific descriptions\n- Evaluation: AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench, pass@1 AND pass@k\n- Key Analyses (8): Coverage heatmaps, per-cell benchmark contribution, emergent curriculum, synthesis efficiency, convergence speed, capability boundary, structured vs flat, selection vs synthesis\n\nPlease list the sections/details that would be lost in the shortened version. Report in under 300 words.\n",
    "agentId": "aa3c4ad436115de96",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I'd be happy to help identify what would be lost, but I need to see both versions of the approach text to make a precise comparison. Could you provide:\n\n1. The original full approach text (the ~5000 word version)\n2. The shortened approach text (the ~2000 word version)\n\nOnce I have both documents, I can systematically compare them and identify exactly which sections, quantitative details, and analyses are missing in the shortened version.\n\nYou can either:\n- Paste them directly in your next message\n- Provide file paths if they're stored locally\n- Share the relevant text in any format you have available"
      }
    ],
    "totalDurationMs": 3082,
    "totalTokens": 18386,
    "totalToolUseCount": 0,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18245,
      "cache_read_input_tokens": 0,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18245
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 139,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18245,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  },
  "sourceToolAssistantUUID": "9340f2ae-0ca9-40a7-b472-70ddfe8d2900",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-28T04:03:58.022Z_

<details><summary>Logged reasoning block</summary>

```text
The agent couldn't help since it didn't have the actual texts. Let me just construct the final JSON myself, carefully preserving the original's detail while making only the specific changes needed. I know exactly what needs to change:

1. `core_problem`: Add CurES/InSight mention in Bayesian context
2. `opportunity`: Restructure from 5→6 points, add Bayesian estimation context
3. `landscape`: Add CurES/InSight sections, fix SEC 3B numbers, update gap/AIME sections


4. `inspired_by`: Add CurES/InSight entries
5. `approach`: Reframe Core 3 ONLY, keep everything else
6. `resource_estimate`: Keep original structure
7. `target_venues`: Remove ICLR 2027
8. `key_references`: Add CurES, InSight
9. `description`: Update summary
10. `reviewer_response`: New for round 9
11. `change_type`: Add "minor"

Now I'll build out the complete JSON with all these targeted modifications. this as a properly formatted JSON. Let me construct it carefully, making targeted edits to the original text.

For the approach field, the key change is to Core Innovation 3. The original says we estimate learnability through K=100 dedicated completions per problem, which is computationally expensive. Instead, I'm reusing the G=16 rollouts already generated during GRPO training—zero additional inference cost. G=16 is well-justified by prior work: DAPO standardizes this value, MC-GRPO shows clear performance degradation below it, and the gradient starvation analysis explains why—at G=4 we get 69.25% degenerate groups versus less than 1% at G=8.

I'm also incorporating Bayesian temporal smoothing with a Beta-Bernoulli running posterior per problem that updates with each appearance, causing posterior variance to drop roughly threefold after just 3 appearances. The replacement strategy uses a conservative credible interval where candidates must exceed the occupant's upper bound, which prevents noisy replacements. This p(1-p) learnability signal is theoretically grounded in Online Difficulty Filtering's result showing policy improvement is lower-bounded by exactly this quantity. I'm seeing that CurES, InSight, and DBB have all established Beta-Bernoulli posteriors in RLVR, but they apply these techniques to problem selection and gradient estimation rather than archive replacement decisions. My approach differs by using credible intervals to decide which solutions to keep, reusing rollouts from the selection process to avoid computational overhead, and incorporating temporal discounting similar to InSight's difficulty weighting. We apply this established statistical framework to a fundamentally different decision problem: archive replacement in evolving archives.

For each problem x in the archive, we maintain a Beta(α_x, β_x) posterior over its true success rate, initialized with prior Beta(1,1). Each time x appears in a training batch with G=16 rollouts, we observe k successes and update: α_x += k, β_x += (G-k). We reuse the G=16 rollouts already generated for GRPO training—zero additional inference cost (unlike CurES's dedicated N'=4 estimation rollouts per prompt, or DéjàQ's K=100 dedicated completions). G=16 is well-justified: DAPO standardizes G=16; MC-GRPO shows clear degradation at smaller G values due to gradient starvation—at G=4, degenerate groups occur 69.25% of the time versus less than 1% at G=8.

After just 3 appearances totaling 48 cumulative rollouts, posterior variance drops roughly threefold, and the p(1-p) learnability signal is theoretically grounded in Online Difficulty Filtering's result that policy improvement is lower-bounded by this exact quantity. The novelty here isn't the Beta-Bernoulli estimation itself—that's now standard across RLVR methods like CurES, InSight, and DBB—but rather how we apply it: the specific decision problem of archive replacement, and how we leverage the existing rollout budget. replacement in evolving archives rather than sampling from fixed pools or gradient estimation. When a candidate problem x' is proposed for a cell occupied by x, we compare credible intervals: x' replaces x only if the lower bound of x''s 80% credible interval for learnability p(1-p) exceeds the upper bound of x's interval. This is more principled than DéjàQ's point estimate comparison f(x')>f(y). We use full posterior credible intervals instead of point estimates, which prevents noisy replacements of well-characterized occupants by poorly-observed newcomers. By reusing the same G=16 training rollouts, we avoid CurES's separate estimation phase and DéjàQ's K=100 dedicated completions. Temporal discounting inspired by InSight's approach prevents stale estimates as the policy evolves, and we extend VCRL's insight that reward variance reflects difficulty from a curriculum signal into our Bayesian replacement criterion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84d11516-92a4-4e48-838d-f22144c9eb16",
  "isSidechain": false,
  "requestId": "req_011CbUJVXCJcynpvS8z1HHpW",
  "type": "assistant",
  "uuid": "ed4a28b0-0628-4cf1-b9ba-7fbf0e64e075",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYuYojGsrmWe1VdfS8Gpcf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1932,
      "cache_read_input_tokens": 66626,
      "output_tokens": 19706,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19706,
          "cache_read_input_tokens": 66626,
          "cache_creation_input_tokens": 1932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1932
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

_source line 65 · 2026-05-28T04:11:30.325Z_

The agent couldn't compare without both texts. I already know exactly what needs to change — the agent's revision oversimplified the approach and resource_estimate. Let me construct the proper final JSON myself, preserving all original detail while making only the targeted changes needed for the reviewer's feedback.

Here is the complete revised JSON with all fields:

```json
{
  "title": "Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis",
  "change_type": "minor",
  "core_problem": "Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the 'sparse policy selection' view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes 'capability boundary collapse' where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Recent bandit-based curriculum approaches address adaptive selection during RL: SEC (arXiv 2505.14970) formulates curriculum as a MAB over problem categories, achieving 17.5% AIME 2024 on Qwen2.5-7B (+27% relative); Actor-Curator (arXiv 2602.20532) extends this with a neural curator achieving 30.0% AIME 2024 on Qwen2.5-3B (+28.6% relative over uniform) with regret guarantees. However, both select from fixed problem pools (12K MATH problems) without synthesis—they optimize WHICH existing problems to train on, but cannot create new problems when the pool lacks adequate coverage for the policy's current frontier. As the policy improves toward competition level, the fraction of useful problems in a fixed pool shrinks, hitting a pool-exhaustion ceiling. Bayesian estimation of per-problem learnability is now an established technique in RLVR curriculum design: CurES (arXiv 2510.01037) models per-problem success rates with Beta(α,β) posteriors and derives optimal sampling distributions via gradient convergence analysis (+4.82 over GRPO on 7B); InSight (arXiv 2603.01907) extends this with weighted mutual information decomposing into difficulty-dependent and epistemic components (~2.2× training acceleration); DBB (arXiv 2603.18444) applies Beta-Bernoulli estimation to policy gradient variance reduction. However, all three apply Bayesian estimation to problem SELECTION from fixed pools or gradient estimation—none applies it to the fundamentally different decision problem of archive REPLACEMENT in evolving archives with synthesis. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution—but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps, achieving 13.3% AIME 2024—matching the Qwen-2.5-7B base model—and actually degrading AMC 2023 from 57.5% to 52.5%. The fundamental open question is: can we build a system that combines the adaptive selection intelligence of bandit-based methods with persistent coverage-maintaining archives and targeted synthesis for identified gaps at competition level?",
  "opportunity": "Six converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic—and multiple empirical findings support diversity's importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) Bandit-based curriculum methods demonstrate the value of adaptive selection but reveal the ceiling of fixed-pool approaches: SEC achieves 17.5% AIME 2024 (Qwen2.5-7B) via MAB over categories; Actor-Curator achieves 30.0% AIME 2024 (Qwen2.5-3B) via neural bandit with regret guarantees—but both select from fixed 12K pools without synthesis or multi-dimensional coverage tracking. Notably, at the 3B scale SEC's category-level approach yields only modest gains over uniform (+3.33 absolute on AIME24, from 20.0% to 23.33%), while Actor-Curator's per-problem utility estimation yields much larger gains (+10.0 absolute to 30.0%), suggesting coarser-grained approaches offer diminishing returns for harder problems. The approaches are potentially COMPLEMENTARY: principled bandit selection FROM a coverage-maintaining, synthesis-augmented archive. (5) Bayesian estimation of per-problem learnability is now established in RLVR: CurES (arXiv 2510.01037) derives optimal sampling distributions from Beta posteriors via gradient convergence analysis (+4.82 over GRPO on 7B); InSight (arXiv 2603.01907) extends this with mutual-information-based selection decomposing epistemic and aleatoric uncertainty (~2.2× acceleration); DBB (arXiv 2603.18444) applies Beta-Bernoulli estimation to gradient variance reduction. Our contribution applies this established estimation technique to a new decision problem—archive replacement via credible interval comparison—at zero additional inference cost by reusing G=16 training rollouts, rather than requiring separate estimation phases (CurES) or dedicated completions (DéjàQ K=100). (6) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K→80K); per-niche survival varies by topic (geometry autoformalization is ~3.7× harder than non-geometry per IndiMathBench, though this reflects formalization-specific difficulty that may not fully transfer to synthesis). VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification with targeted synthesis (vs. reactive instance-level targeting or selection-only bandits), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria applied to evolving archives rather than fixed-pool selection.",
  "landscape": "**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\n\n**Bandit-based adaptive curriculum (critical comparators).** SEC (arXiv 2505.14970) formulates online curriculum selection as a non-stationary MAB where each problem category (difficulty level or problem type) is an arm. Uses TD(0) updates on Q-values derived from absolute advantages, with Boltzmann sampling: p(c) ∝ exp(Q(c)/τ). Selects from fixed training pools (10K problems per domain). Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random 13.8%), 76.1% MATH-500, 51.1% AMC22-23. Categories are 1D (difficulty OR type per domain). SEC-2D variant combines 3 reasoning domains into 9 arms for multi-task learning. Actor-Curator (arXiv 2602.20532) extends beyond SEC's category-level bandits to per-problem utility estimation via a neural curator (Qwen3-0.6B) trained with online stochastic mirror descent (OSMD). Establishes regret bound O(T^{2/3}·V_T^{1/3}) under non-stationary utilities. Selects from fixed pools (12K MATH problems). Qwen2.5-3B: 30.0% AIME 2024, 81.0% MATH-500 (+50% relative over uniform 20.0%; in the matched 3B comparison, SEC achieves 23.33% while uniform achieves only 20.00%—SEC's category-level approach yields only modest gains over uniform (+3.33 absolute, +16.7% relative on AIME24), while Actor-Curator's per-problem utility estimation yields much larger gains (+10.0 absolute over uniform, +50% relative), supporting the argument that coarser-grained category-level approaches offer diminishing returns for harder competition-level problems). ~9% overhead. Key insight: Actor-Curator's per-problem utility estimation is more expressive than SEC's category-level Q-values, yielding consistent gains. Critical differentiation from SACE-RLVR on four dimensions: (a) SELECTION vs. SYNTHESIS—both SEC and Actor-Curator select from fixed pools of existing problems; they cannot synthesize new problems targeting identified gaps. As the policy improves toward competition level, the fraction of useful problems in a fixed 12K pool shrinks (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED optimization—Actor-Curator optimizes aggregate per-problem utility without explicit multi-dimensional coverage constraints, risking concentration on high-utility niches without ensuring breadth (analogous to SAGE's demonstrated over-specialization); (c) STATELESS vs. PERSISTENT—neither maintains a persistent multi-dimensional archive with cross-step coverage tracking; (d) COMPLEMENTARITY—crucially, these approaches compete at different levels: Actor-Curator's bandit selection could serve as the within-archive sampling strategy, combining principled selection WITH coverage-maintaining synthesis. We test this complementarity explicitly.\n\n**Bayesian learnability estimation in RLVR (critical context for Core 3).** CurES (arXiv 2510.01037, Oct 2025, revised Mar 2026) is the most directly comparable prior art for Bayesian estimation in RLVR curriculum design. Models per-problem success rate with Beta(α,β) posterior, updated as α += successes, β += failures from rollouts. Derives optimal sampling distribution ∝ exp(√[p(1-p)]/τ) via gradient convergence analysis, linking the p(1-p) learnability signal to gradient descent convergence rate. Uses point estimates (Beta mean) for sampling probability computation. Two-phase: parameter estimation phase (N'=4 rollouts per prompt), then training phase with variance-based rollout allocation proportional to √[gradient variance]. Fixed pool: Numina-Math dataset partitioned into 15 subsets. Results: Qwen2.5-Math-7B: AIME24 24.58%, MATH-500 84.80%, AMC23 64.38%, +4.82 over GRPO; Qwen2.5-Math-1.5B: AIME24 13.33%, MATH-500 77.20%, +3.30 over GRPO. Uses VERL training framework. Critical differentiation from SACE-RLVR Core 3 on four dimensions: (a) DECISION PROBLEM—CurES uses Beta posteriors for SAMPLING (which problem to train on next?) from a fixed pool → SACE-RLVR uses Beta posteriors for REPLACEMENT (should this new problem replace an existing archive occupant?)—a fundamentally different decision problem; (b) ESTIMATION TYPE—CurES uses point estimates (Beta mean) for sampling probabilities → SACE-RLVR uses credible intervals for replacement decisions, providing conservative replacement that accounts for estimation uncertainty; (c) POOL TYPE—CurES operates on a fixed pool (Numina-Math, 15 partitions) → SACE-RLVR operates on an evolving archive with targeted synthesis; (d) COST—CurES requires a separate estimation phase (N'=4 dedicated rollouts per prompt) → SACE-RLVR achieves zero additional cost via G=16 training rollout reuse.\n\nInSight (arXiv 2603.01907, Mar 2026) extends Bayesian RLVR estimation with weighted mutual information for data selection. Models Bayesian latent success rates with Beta(α,β), prior Beta(1,1). Key innovation: weighted mutual information objective A(τ) = w(ϕ̄_τ) · I(R_{1:K}; Φ_τ), decomposing expected uncertainty reduction into difficulty-dependent (aleatoric: ϕ̄(1-ϕ̄)) and evidence-dependent (epistemic: 1/(n+1)²) components. Demonstrates that difficulty-only selection (like pure p(1-p)) is fundamentally limited—epistemic uncertainty from limited evidence matters too. Temporal discounting on Beta parameters: α_{t+1} = λα_t + (1-λ)α_0 + S_t (λ=1.0 default). Results: AIME24 53.75 on Qwen3-4B (+2.30 vs random), up to ~2.2× training acceleration on Countdown. Fixed pool (DeepScaler ~40K). Differentiation: InSight extends Bayesian RLVR estimation with epistemic uncertainty for problem selection from fixed pools; SACE-RLVR applies Bayesian estimation to archive replacement (different decision problem) in evolving archives with synthesis. InSight's temporal discounting insight is adopted for our Beta parameter decay.\n\n**Balanced difficulty filtering theory.** Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) proves that expected policy improvement is lower-bounded by the variance of task-level success probabilities p(x)(1-p(x)), maximized at p(x)=0.5. Balanced filtering (0.3&lt;p(x)<0.7) achieves +12% on AMC and +10% on AIME with Qwen2.5 models in less than half the training steps of standard GRPO. This theoretical result directly supports our difficulty-aware design: our Bayesian learnability criterion tracks p(1-p) per problem via Beta posteriors, and our archive's ZPD-weighted sampling preferentially selects problems near the difficulty frontier.\n\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\n\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\n\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold α=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively). On AIME 2024, SAGE achieves 13.3%—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%. This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents. Training dynamics confirm this: over-specialization emerges after ~120 steps (peak 69.5% declining to 61.6% by step 240). Question pool grows 18× (1,136→20,532) as flat filtered dataset without structured organization.\n\n**Implicit curriculum theory.** 'The Implicit Curriculum' (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation—not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\n\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: 'behavioral diversity is the binding constraint for RL.' RL-PLUS (arXiv 2508.00222) demonstrates 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\n\n**Policy-level diversity maintenance (concurrent).** UCPO (arXiv 2605.00365) addresses pass@k diversity collapse at the optimization level rather than the data level, adding a conditional uniformity penalty that redistributes gradient signal toward underrepresented correct solutions. Achieves +10% absolute Pass@64 on AIME 2024 (DeepSeek-7B: 70.0%→80.0%) and +45% equation-level diversity while maintaining competitive Pass@1. Importantly, UCPO modifies the loss function, not the training distribution—making it orthogonal to and potentially complementary with archive-based diversity maintenance. UCPO ensures diversity within the correct solution set for a given problem; SACE-RLVR ensures diversity across the problem distribution.\n\n**Lightweight co-evolutionary diversity (concurrent).** Vocabulary Dropout (arXiv 2604.03472) prevents proposer diversity collapse in co-evolutionary frameworks by applying random hard logit masks during problem generation, achieving +4.4 average points on Qwen3-8B (+10.9 AMC, +3.4 AIME 2024, +7.8 AIME 2025) within R-Zero. Demonstrates that diversity collapse is a real bottleneck in co-evolutionary RLVR. Differentiation: VD maintains proposer diversity via stochastic masking; SACE-RLVR provides structured coverage guarantees and interpretable gap identification.\n\n**Meta-RL curriculum generation (concurrent).** SOAR (arXiv 2601.18778) uses bi-level meta-RL where a teacher generates stepping-stone problems rewarded by measured student improvement on hard problems. Achieves +9.3% pass@32 on MATH fail@128 tasks (Llama-3.2-3B), recovering 75% of oracle gains from training on the full MATH dataset. Key insight: structural quality of generated problems matters more than solution correctness. Conceptually parallel to our proactive gap identification but uses meta-RL reward signal (measured student improvement) vs. our archive-structure-based gap detection. SOAR operates at the edge of learnability for currently-unsolvable problems; SACE-RLVR maintains coverage across the full difficulty spectrum.\n\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\n\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%→16.4%; Qwen3-8B AIME24: 16.7→26.0. Proves diversity collapse is real (TTRL pass@16: 32.4→16.7).\n\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\n\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\n\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR—applies Bayesian estimation at the policy gradient level. Our Beta posterior operates at the archive-replacement level for per-problem learnability tracking—a different application of the same statistical principle, alongside CurES (sampling level) and InSight (selection level).\n\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K→80K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry autoformalization has ~3.7× lower success rate than non-geometry (IndiMathBench arXiv 2512.00997: 12.2% vs 44.9% BEq across top models); the paper attributes this partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty. These grounding data inform our per-niche survival estimates.\n\n**Verification.** VHG (arXiv 2605.06660): validity gating.\n\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Bayesian curriculum: CurES 24.58% (7B-Math), InSight 53.75% (Qwen3-4B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\n\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\n\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\n\n**The precise gap.** DéjàQ: 1D, GSM-only. SEC: MAB over categories, 1D, fixed pool. Actor-Curator: per-problem bandit, fixed pool, no coverage tracking. CurES: Beta posteriors for sampling from fixed pool, point estimates, separate estimation phase. InSight: Beta posteriors with mutual information for selection from fixed pool, epistemic decomposition. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization, zero AIME improvement over base model. Online Difficulty Filtering: theoretical support for balanced filtering, no archive structure. UCPO: policy-level diversity, no data-level coverage. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification with synthesis, structured coverage tracking, and Bayesian learnability replacement applied to evolving archives (rather than fixed-pool selection or gradient estimation). Moreover, no existing work tests whether bandit-based selection and archive-based synthesis are complementary.",
  "inspired_by": "DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + SEC_insight['MAB over problem categories during RL; 17.5% AIME24'] + Actor_Curator_insight['neural bandit with regret guarantees; 30.0% AIME24; ~9% overhead; pool-selection ceiling motivates synthesis'] + CurES_insight['Beta posteriors for sampling; gradient convergence analysis; +4.82 over GRPO; establishes Bayesian estimation in RLVR curriculum'] + InSight_insight['weighted mutual information; epistemic+aleatoric decomposition; temporal discounting; extends Bayesian RLVR estimation'] + Online_Difficulty_Filtering['p(1-p) lower bound on policy improvement; balanced filtering; EACL 2026'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools → over-specialization ~120 steps; 13.3% AIME = base model; AMC degrades'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + UCPO_concurrent['policy-level diversity; +10% Pass@64 AIME; complementary to data-level'] + VocabDropout_concurrent['+4.4 avg; diversity collapse prevention'] + SOAR_concurrent['meta-RL teacher; 75% oracle recovery'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry ~3.7× lower autoformalization success; formalization-specific'] + EVOL_RL_warning['diversity collapse']",
  "approach": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics. We organize the system around **three core innovations** plus **four extensions** tested in ablations. This follows the structure of successful prior systems: DéjàQ claims ~2 core contributions atop ~11 mechanisms; CLPO claims 3 named contributions atop ~7 design choices.\n\n**Design Motivation: Why Coverage Matters (Two Independent Arguments).**\n\n*Argument 1: Relay-regime-inspired smooth difficulty coverage.* The implicit curriculum theory (arXiv 2602.14872, ICML 2026) demonstrates on synthetic tasks that smooth difficulty spectra ('relay regime') yield faster convergence than gapped spectra ('grokking regime'). While this theory assumes idealized conditions (uniform distributions, geometric difficulty structure, single attention layer) that differ from real RLVR, it provides a principled design heuristic: smoother difficulty coverage should improve convergence. Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) provides additional theoretical support: policy improvement is lower-bounded by p(1-p) variance, maximized at balanced difficulty, achieving +12% AMC and +10% AIME in half the training steps. Our 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) are motivated by these insights. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\n\n*Argument 2: Broad coverage prevents capability boundary collapse.* Even under the 'sparse policy selection' view where RL modifies only 1-3% of tokens (arXiv 2605.06241), comprehensive coverage is essential. Three empirical findings converge: (a) Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), each un-sharpened primitive type creates an exponential bottleneck; (b) Tailor (arXiv 2511.12429) directly demonstrates that behavioral diversity, not correctness, is the binding constraint for RL outcomes (25 vs. 4 primitives → substantial gains); (c) RL-PLUS (arXiv 2508.00222) shows narrow RLVR causes 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse distributions as the antidote (+69.2% relative improvement). Thus, comprehensive difficulty×topic coverage benefits under both views: relay-like curriculum dynamics AND broader capability activation.\n\n*Why archives with synthesis vs. bandit selection from fixed pools.* SEC and Actor-Curator demonstrate the clear value of adaptive problem selection during RL training. We argue that persistent archives with targeted synthesis provide three capabilities that fixed-pool bandit selection cannot: (i) COVERAGE GUARANTEES—bandits optimize aggregate utility and may concentrate on high-utility niches without ensuring breadth across the difficulty×topic space, analogous to SAGE's demonstrated over-specialization (13.3% AIME = base model, AMC degradation); structured archives explicitly enforce minimum coverage per niche. (ii) SYNTHESIS FOR GAPS—as the policy improves, the useful difficulty frontier advances, and a fixed pool (e.g., MATH's 12K problems) becomes increasingly sparse at the frontier; targeted synthesis creates fresh problems where the policy needs them most. (iii) PERSISTENT TRACKING—archives maintain cross-step memory of which niches are well-covered and which are stale, enabling proactive rather than reactive curriculum adaptation. However, these approaches are potentially COMPLEMENTARY: Actor-Curator's principled per-problem utility estimation can serve as the within-archive sampling strategy, and we test this explicitly (see E4 and baseline #5).\n\n---\n\n**CORE INNOVATION 1: 2D Learnability Archive (50 cells).**\n10 difficulty bins (width 0.1, empirical solve-rate) × 5 topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells, M=10 problems per cell. Topic classification via GPT-4o-mini (84-92% accuracy per arXiv 2411.00042). Difficulty measured via G=16 rollouts reused from training.\n\nThe 2D structure enables qualitatively new capabilities vs. prior work: (a) difficulty-aware coverage tracking—locate under-populated difficulty×topic niches BEFORE policy failures (vs. Socratic-Zero's reactive approach, SAGE's flat pool that over-specializes by step ~120, SEC/Actor-Curator's fixed-pool selection without coverage constraints); (b) persistent cross-step memory—problems track with the evolving policy, revealing emergent curriculum (vs. CLPO's stateless per-batch assessment, SEC's myopic TD updates); (c) interpretable post-hoc analysis—which niches drive benchmark performance.\n\nReplacement criterion: candidate problem enters a cell if its Bayesian learnability credible interval (see Core 3) exceeds the current worst occupant's upper bound. More principled than DéjàQ's point estimate comparison f(x')>f(y).\n\n**CORE INNOVATION 2: Proactive Gap-Targeted Synthesis with Verification.**\nExisting targeting is either reactive (Socratic-Zero examines specific failed solutions; SwS identifies aggregate weaknesses offline) or selection-only (SEC/Actor-Curator adaptively choose from fixed pools). SAGE's Challenger generates harder problems without coverage awareness, leading to over-specialization. The 2D archive enables proactive niche-level gap identification:\n\n(a) Identify under-performing cells: <3 problems or stale (not refreshed for >100 training steps).\n(b) Generate-then-classify synthesis: generate for target TOPIC without difficulty constraints, verify, then empirically measure difficulty via G=16 rollouts and assign to the appropriate cell. This avoids the 'double filter' problem (constraining both topic AND difficulty yields 4-17% per SPARQ/MathSmith evidence; topic-only yields higher survival).\n(c) 3-stage VHG-inspired verification: (i) format/solvability check (filters ~25-30%, consistent with FLAMES ~30% removal), (ii) cross-verification via majority vote across 2-3 strong models (filters ~15-20%), (iii) difficulty calibration via G=16 rollouts.\n\n**Concrete per-niche survival estimates (literature-grounded):**\nEstimates sourced from SPARQ (~25% QD survival), DART-Math (51.1% Level 5 dropout), FLAMES (50% removal at Level 5), and IndiMathBench (~3.7× lower geometry autoformalization success rate, 12.2% vs 44.9% BEq; noting this reflects formalization-specific difficulty in Lean 4 that may not fully transfer to problem synthesis—we conservatively estimate geometry synthesis is ~2-3× harder than algebra).\n\n- Easy-medium cells (solve-rate 0.3-0.8), common topics (Algebra, NT): ~30 cells, ~30-50% survival.\n  Need ~20-35 candidates/cell → ~600-1,050 total.\n- Medium-hard cells (solve-rate 0.1-0.3), common topics: ~10 cells, ~15-25% survival.\n  Need ~40-65 candidates/cell → ~400-650 total.\n- Geometry cells (all difficulties): ~10 cells, ~10-20% survival (geometry synthesis is harder than algebra due to constraint consistency requirements; conservatively ~2-3× harder based on adjusted IndiMathBench ratio with formalization-specific caveats).\n  Need ~50-100 candidates/cell → ~500-1,000 total.\n- Extreme cells (solve-rate <0.1 or >0.9, all topics): ~10 cells, ~3-8% survival (DART-Math: Level 5 loses 51% coverage; FLAMES: 50% removal at Level 5).\n  Need ~125-330 candidates/cell → ~1,250-3,300 total.\n- **Graceful degradation:** cells that cannot reach M=10 accept minimum 3 (sufficient for meaningful Beta posterior updates). Archive reports actual occupancy; analysis accounts for sparse cells.\n- **Total per refresh cycle:** ~2,750-6,000 candidates (median ~4,000). Generation cost using open-source 70B teacher: ~130 GPU-hours. Verification (G=16 rollouts per candidate on 7B): ~12 GPU-hours. Per-refresh total: ~142 GPU-hours. Over ~10 refreshes: ~1,420 GPU-hours. Alternative: API-based generation at ~$0.30/problem ≈ $1,200/refresh, $12,000 total.\n- Per-niche survival rates and generation statistics reported as community contribution.\n\n**CORE INNOVATION 3: Zero-Cost Bayesian Learnability for Archive Replacement.**\nBeta-Bernoulli estimation is now an established technique in RLVR curriculum design: CurES (arXiv 2510.01037) models per-problem success rates with Beta(α,β) posteriors and derives optimal sampling distributions ∝ exp(√[p(1-p)]/τ) via gradient convergence analysis (+4.82 over GRPO on 7B); InSight (arXiv 2603.01907) extends this with weighted mutual information decomposing into difficulty-dependent (aleatoric) and evidence-dependent (epistemic) components (~2.2× training acceleration); DBB (arXiv 2603.18444) applies Beta-Bernoulli estimation to policy gradient variance reduction. All three apply Bayesian estimation to problem SELECTION from fixed pools or gradient estimation. We apply this established statistical framework to a fundamentally different decision problem: archive REPLACEMENT in evolving archives.\n\nFor each problem x in the archive, we maintain a Beta(α_x, β_x) posterior over its true success rate, initialized with prior Beta(1,1). Each time x appears in a training batch with G=16 rollouts, we observe k successes and update: α_x += k, β_x += (G-k). We reuse the G=16 rollouts already generated for GRPO training—zero additional inference cost (unlike CurES's dedicated N'=4 estimation rollouts per prompt, or DéjàQ's K=100 dedicated completions). G=16 is well-justified: DAPO (arXiv 2503.14476) standardizes G=16; MC-GRPO (arXiv 2601.22582) shows clear degradation at small G (G=2: 78.92%, G=4: 81.34%, G=8: 84.53%); the Gradient Starvation analysis (arXiv 2605.07689) explains the mechanism—for binary rewards, degenerate group probability is p^G+(1-p)^G, yielding 69.25% degenerate groups at G=4 vs. <1% at G=8.\n\nAfter 3 appearances (48 cumulative rollouts), posterior variance drops ~3×. The p(1-p) learnability signal is theoretically supported by Online Difficulty Filtering's result (arXiv 2504.03380) that policy improvement is lower-bounded by this exact quantity.\n\nThe novelty of Core 3 lies not in the Beta-Bernoulli estimation itself (now established in RLVR via CurES, InSight, DBB), but in three aspects: (a) The decision problem: replacement in evolving archives rather than sampling from fixed pools or gradient estimation. When a candidate problem x' is proposed for a cell occupied by x, we compare credible intervals: x' replaces x only if the lower bound of x''s 80% credible interval for learnability p(1-p) exceeds the upper bound of x's interval. This is more principled than DéjàQ's point estimate comparison f(x')>f(y). (b) Credible intervals rather than point estimates: CurES uses point estimates (Beta mean) for sampling probabilities; we use full posterior credible intervals for replacement decisions, preventing noisy replacement of well-characterized occupants by poorly-observed newcomers. (c) Zero additional inference cost: by reusing G=16 training rollouts, we avoid CurES's separate estimation phase and DéjàQ's K=100 dedicated completions. Temporal discounting (inspired by InSight's λ-discounting on Beta parameters) prevents stale estimates as the policy evolves. VCRL's insight (arXiv 2509.19803) that reward variance reflects difficulty is extended from curriculum signal to Bayesian replacement criterion.\n\n---\n\n**EXTENSIONS (each tested in one ablation, not claimed as core contributions):**\n\nE1: Cross-niche SvS seeding. SvS-style answer-preserving mutation (ICLR 2026) from adjacent cells to seed under-populated niches. Expected ~70-80% validity for within-topic mutations. Particularly valuable for geometry and extreme cells where de novo generation has lower survival. Tested in A5.\n\nE2: James-Stein shrinkage. Following arXiv 2511.03710 (which demonstrates shrinkage baselines reduce MSE in RLVR), we apply shrinkage to per-problem learnability estimates, regularizing toward batch average. Not claimed as novel—cite and use. Tested in A6.\n\nE3: DGPO policy updates. MAD normalization + DQW weighting adopted from MathForge (arXiv 2601.20614, ICLR 2026). Addresses difficulty-dependent advantage scale. Tested in A7.\n\nE4: Archive sampling strategy. Compare (a) ZPD-weighted sampling with posterior variance weighting ([0.1, 0.9] solve-rate, high uncertainty → more sampling), (b) uniform sampling, and (c) Actor-Curator-style bandit sampling from the archive—directly testing whether principled per-problem utility estimation (à la Actor-Curator) further improves when operating within a coverage-maintaining archive. This tests the complementarity hypothesis: if (c) outperforms both Actor-Curator from a fixed pool and (a) from the archive, it validates that bandit selection and archive synthesis address orthogonal bottlenecks.\n\n---\n\n**Training Loop (VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary):**\n(a) Sample from archive with selected strategy (E4). (b) G=16 rollouts, compute advantages. (c) Policy update (GRPO or DGPO). (d) Update Beta posteriors per problem. (e) Every 50 steps: refresh sampled cells, reassign problems that shifted difficulty, flag stale cells, synthesize for gaps. Overhead: ~20-25% vs. vanilla GRPO (dominated by synthesis cost).\n\n**AIME Contextualization.** Distillation-based: 70-90% AIME 2024. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Bayesian curriculum: CurES 24.58% (7B-Math). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm. Value: METHOD + ABLATION INSIGHTS. Framework applicable atop distilled bases.\n\n**Baselines (8):** (1) DéjàQ-comp [PRIMARY: 2D+targeting value over 1D archive]. (2) CLPO [PRIMARY: persistent archive value over stateless curriculum]. (3) Socratic-Zero [PRIMARY: structured proactive vs. reactive instance-level targeting]. (4) SAGE [structured archive vs. flat pool; evidence: SAGE's AIME = base model + AMC degradation]. (5) Actor-Curator [PRIMARY: archive synthesis vs. bandit selection from fixed pool; complementarity test via E4]. (6) EVOL-RL [stateless novelty-aware diversity]. (7) MathForge [DGPO source; difficulty-aware optimization]. (8) Vanilla GRPO [minimal baseline].\n\n**Ablations (7):**\nA1: 1D archive only (tests Core 1 dimensionality).\nA2: Random synthesis vs. gap-targeted (tests Core 2 proactive targeting).\nA3: 3 bins vs. 10 bins [relay-regime-inspired test: first empirical comparison of coarse vs. fine difficulty granularity in real RLVR].\nA4: Point estimation vs. Beta posterior with credible intervals (tests Core 3 vs. DéjàQ-style point-estimate comparison and CurES-style point-estimate sampling).\nA5: Without cross-niche SvS seeding (tests E1 value, especially for sparse cells).\nA6: Without James-Stein shrinkage (tests E2).\nA7: GRPO vs. DGPO (tests E3).\n\n**Evaluation:** AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. pass@1 AND pass@k (pass@k especially important per RL-PLUS's capability boundary collapse finding and UCPO's concurrent work on policy-level diversity—we test whether archive-based data diversity and policy-level diversity address complementary aspects of the collapse). DAPO-Math-17k seeds.\n\n**Key Analyses:** (1) Coverage heatmaps showing cell occupancy evolution. (2) Per-cell benchmark contribution: which niches drive gains? (3) Emergent curriculum: bin-transition frequencies as policy improves. (4) Synthesis efficiency: per-topic survival rates vs. literature benchmarks (SPARQ, DART-Math, FLAMES), reported as community contribution. (5) Convergence speed: 10 vs. 3 bins. (6) Capability boundary: pass@1 vs. pass@k trajectories—does archive diversity prevent RL-PLUS-style collapse? How does data-level diversity (SACE-RLVR) compare to policy-level diversity (UCPO)? (7) Structured vs. flat: archive coverage diversity over training vs. SAGE-style accumulation. (8) Selection vs. synthesis: Actor-Curator from fixed pool vs. Actor-Curator-style sampling from SACE-RLVR archive—quantifying the value of synthesis and coverage maintenance.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "7,200 H100-hours (baselines: 8×250h=2,000h; SACE-RLVR 7B 800h; SACE-RLVR 8B 800h; ablations 7×200h=1,400h; synthesis/verification 1,420h; archive overhead 330h; E4 bandit variant 450h)",
      "timeline": "14-18 weeks",
      "estimated_gpu_cost": "$18,000 (at ~$2.50/H100-hr)"
    },
    "human_in_loop": {
      "gpu_hours": "5,600 H100-hours (reuse released code; shared verification; API-based generation saves ~1,100 GPU-hrs but adds ~$12,000 API cost)",
      "timeline": "12-15 weeks",
      "claude_api_cost": "$400-800 (code assistance)",
      "synthesis_api_cost": "$7,000-12,000 (problem generation via API, optional vs. GPU)",
      "estimated_gpu_cost": "$14,000"
    },
    "auto_research": {
      "gpu_hours": "8,800 H100-hours (exploratory sweeps over archive dimensions, bin count, refresh frequency, replacement criteria, synthesis strategies, bandit-archive complementarity)",
      "timeline": "10-13 weeks",
      "claude_api_cost": "$1,000-2,000",
      "estimated_gpu_cost": "$22,000",
      "speed_bottleneck": "GPU queue; each GRPO run 24-72h on 8×H100s. Synthesis for extreme cells dominates generation cost."
    }
  },
  "target_venues": [
    "ICML 2027 (~Jan 2027) — primary target, strong fit for RL + QD + coverage",
    "NeurIPS 2027 (~May 2027) — fallback with full evaluation"
  ],
  "level": "top-tier",
  "key_references": [
    "DéjàQ (arXiv 2601.01931) — PRIMARY PREDECESSOR, online MAP-Elites for RLVR at GSM level",
    "SEC (arXiv 2505.14970) — CRITICAL COMPARATOR, MAB over problem categories; 17.5% AIME24 on Qwen2.5-7B; TD(0) updates",
    "Actor-Curator (arXiv 2602.20532) — PRIMARY BASELINE, neural bandit selection from fixed pool; 30.0% AIME24 on Qwen2.5-3B; regret O(T^{2/3}·V_T^{1/3}); ~9% overhead",
    "CurES (arXiv 2510.01037) — CRITICAL CONTEXT FOR CORE 3, Beta posteriors for sampling; optimal distribution ∝ exp(√[p(1-p)]/τ); +4.82 over GRPO on 7B; establishes Bayesian estimation in RLVR curriculum",
    "InSight (arXiv 2603.01907) — CRITICAL CONTEXT FOR CORE 3, weighted mutual information with epistemic+aleatoric decomposition; ~2.2× acceleration; extends Bayesian RLVR estimation",
    "Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) — THEORETICAL SUPPORT, p(1-p) lower bound on policy improvement; +12% AMC in half steps",
    "CLPO (arXiv 2509.25004) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024",
    "Socratic-Zero (arXiv 2509.24726) — PRIMARY BASELINE, three-agent co-evolution; 56.1% avg",
    "SAGE (arXiv 2603.15255) — BASELINE, 4-agent self-evolution; 13.3% AIME = base model; AMC degrades 57.5%→52.5%",
    "UCPO (arXiv 2605.00365) — CONCURRENT, policy-level diversity via conditional uniformity; +10% Pass@64 AIME24; complementary to data-level",
    "Vocabulary Dropout (arXiv 2604.03472) — CONCURRENT, lightweight diversity via logit masking; +4.4 avg on 8B",
    "SOAR (arXiv 2601.18778) — CONCURRENT, meta-RL teacher for edge-of-learnability synthesis; 75% oracle recovery",
    "The Implicit Curriculum (arXiv 2602.14872, ICML 2026) — DESIGN MOTIVATION, relay vs. grokking (synthetic tasks)",
    "Sparse Policy Selection (arXiv 2605.06241) — RL modifies 1-3% of tokens; motivates broad coverage",
    "Sharper Primitives (arXiv 2602.08281) — RLVR polarizes; multiplicative compounding; diverse training activates broader primitives",
    "Tailor (arXiv 2511.12429) — behavioral diversity is binding constraint for RL; 25 vs 4 primitives",
    "RL-PLUS (arXiv 2508.00222) — capability boundary collapse from narrow RLVR; +69.2% with diversity",
    "ProRL (arXiv 2505.24864) — diverse prolonged training accesses beyond base model ceiling",
    "Bidirectional Curriculum Generation (arXiv 2603.05120) — 4-agent bidirectional; 60.03 avg",
    "EVOL-RL (arXiv 2509.15194) — stateless novelty-aware diversity; AIME25 16.4%",
    "MathForge/DGPO (arXiv 2601.20614, ICLR 2026) — MAD normalization; adopted as extension",
    "VCRL (arXiv 2509.19803) — reward variance as difficulty proxy; G=16; 57.76 avg Qwen3-8B",
    "MC-GRPO (arXiv 2601.22582) — rollout count ablation: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%",
    "Gradient Starvation (arXiv 2605.07689) — 69% degenerate groups at G=4; explains G effect mechanistically",
    "DAPO (arXiv 2503.14476) — standardizes G=16",
    "Discounted Beta-Bernoulli (arXiv 2603.18444) — Bayesian estimation for RLVR gradients; validates Beta approach",
    "SwS (NeurIPS 2025, arXiv 2506.08989) — offline weakness targeting; +10%",
    "SvS (ICLR 2026) — answer-preserving synthesis; used for cross-niche seeding",
    "SAND-Math (arXiv 2507.20527) — ~38% end-to-end competition synthesis survival",
    "SPARQ (arXiv 2506.06499) — ~25% QD survival (320K→80K); per-niche evidence",
    "DART-Math (arXiv 2407.13690, NeurIPS 2024) — Level 5: 51.1% query dropout; difficulty survival data",
    "FLAMES (arXiv 2508.16514) — ~30% strict survival; Level 5: 50% removal",
    "IndiMathBench (arXiv 2512.00997) — geometry ~3.7× lower autoformalization success; formalization-specific context",
    "VHG (arXiv 2605.06660) — validity gating; inspires verification",
    "Shrinking the Variance (arXiv 2511.03710) — James-Stein shrinkage for RLVR",
    "EBPO (arXiv 2602.05165) — empirical Bayes for GRPO",
    "R-Zero (ICLR 2026) — self-evolving; collapses iter 3",
    "Klear-Reasoner-8B (arXiv 2508.07629) — 90.5% AIME 2024; distillation context",
    "Prism (arXiv 2603.13309) — 128-cluster diversity with ZPD gate",
    "R-Diverse (arXiv 2602.13103) — SAM skill diversity + MAP memory",
    "STAT (arXiv 2510.10023) — Missing-Skill-Profile",
    "Problem Categorization (arXiv 2411.00042) — topic classification",
    "Two-Stage Dynamic View (arXiv 2510.04028) — capability shrinkage then expansion",
    "Does RL Incentivize Reasoning? (NeurIPS 2025, arXiv 2504.13837) — coverage framing"
  ],
  "description": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), scaling online MAP-Elites from GSM-level (DéjàQ) to competition-level math through three core innovations plus four extensions. Two independent motivations for comprehensive coverage: (1) relay-regime theory (arXiv 2602.14872) and balanced difficulty filtering theory (arXiv 2504.03380, EACL 2026: p(1-p) lower bound on policy improvement) suggest smooth difficulty spectra yield faster convergence—adopted as design heuristic, not guarantee, with A3 testing empirically; (2) even under 'sparse policy selection' (1-3% tokens modified), broad coverage prevents 'capability boundary collapse' (RL-PLUS: pass@1↑ pass@128↓; +69.2% with diversity), ensures multiplicative primitive sharpening across domains (Sharper Primitives), and provides the behavioral diversity that is the binding constraint for RL (Tailor: 25 vs 4 primitives). Core 1: 2D archive (10 bins × 5 topics = 50 cells) with proactive gap identification and Bayesian replacement—addresses SAGE's over-specialization at step ~120 (AIME 13.3% = base model, AMC degradation 57.5%→52.5%). Core 2: generate-then-classify synthesis with per-niche survival estimates (central: 30-50%, geometry: 10-20% accounting for ~3.7× autoformalization difficulty ratio from IndiMathBench with formalization-specific caveats, extreme: 3-8%; graceful degradation to min 3/cell; ~142 GPU-hrs/refresh). Core 3: zero-cost Bayesian learnability for archive replacement, applying established Beta-Bernoulli estimation (cf. CurES for sampling from fixed pools, InSight for mutual-information-based selection, DBB for gradient estimation) to a new decision problem—archive replacement via credible interval comparison—at zero additional inference cost by reusing G=16 training rollouts (vs. CurES's separate estimation phase, DéjàQ's K=100 dedicated completions); G=16 justified by MC-GRPO ablation + gradient starvation analysis (69% degenerate groups at G=4). Key positioning vs. bandit-based curriculum: SEC (17.5% AIME24, Qwen2.5-7B) and Actor-Curator (30.0% AIME24, Qwen2.5-3B, ~9% overhead) demonstrate adaptive selection value but are limited by fixed pool exhaustion, lack of synthesis, and absence of coverage tracking; at 3B scale SEC's category-level gains over uniform are modest (+3.33 absolute on AIME24) while Actor-Curator's per-problem approach yields much larger gains (+10.0 absolute), supporting finer-grained approaches. SACE-RLVR provides what bandits cannot: synthesis for identified gaps, structured coverage guarantees, and persistent cross-step memory. The approaches are potentially complementary—Actor-Curator's bandit sampling from SACE-RLVR's archive tested in E4 and Analysis #8. Extensions: SvS seeding, shrinkage, DGPO, archive sampling strategy (including Actor-Curator-style variant)—each ablated. Eight baselines (DéjàQ-comp, CLPO, Socratic-Zero, SAGE, Actor-Curator, EVOL-RL, MathForge, GRPO), seven ablations including pass@k capability boundary analysis and selection-vs-synthesis analysis. Concurrent work positioned: UCPO (policy-level diversity, complementary), Vocabulary Dropout (lightweight alternative), SOAR (meta-RL curriculum). Qwen2.5-Math-7B/Qwen3-8B, AIME 2024/2025, MATH-500, AMC, Minerva, OlympiadBench.",
  "project_name": "sace_rlvr",
  "source": "web_research",
  "reviewer_response": {
    "revision_overview": "MINOR REVISION addressing the final critical gap (CurES/InSight) and reframing Core 3's novelty claim for Round 10 readiness. Five changes: (1) CurES added as critical context for Core 3 with four-dimensional differentiation, (2) InSight added as extending Bayesian RLVR estimation, (3) Core 3 reframed from 'novel Beta posteriors' to 'established technique applied to new decision problem', (4) SEC 3B data corrected with accurate numbers, (5) ICLR 2027 venue target removed.",
    "issue_1_cures_critical": "ADDRESSED. CurES (arXiv 2510.01037) added as the most directly comparable prior art for Core 3. Full technical details in new 'Bayesian learnability estimation in RLVR' landscape subsection: Beta(α,β) posteriors, optimal sampling ∝ exp(√[p(1-p)]/τ) via gradient convergence analysis, point estimates (Beta mean), two-phase estimation (N'=4 dedicated rollouts per prompt), fixed pool (Numina-Math, 15 partitions), Qwen2.5-Math-7B: AIME24 24.58%, MATH-500 84.80%, +4.82 over GRPO. Four-dimensional differentiation: (a) DECISION PROBLEM—CurES uses Beta posteriors for SAMPLING (which problem to train on) from fixed pool vs. SACE-RLVR uses for REPLACEMENT (should this problem replace an archive occupant); (b) ESTIMATION TYPE—CurES uses point estimates (Beta mean) vs. SACE-RLVR uses credible intervals for conservative replacement; (c) POOL TYPE—CurES fixed pool vs. SACE-RLVR evolving archive with synthesis; (d) COST—CurES requires separate estimation phase vs. SACE-RLVR zero additional cost via G=16 training rollout reuse. Integrated into core_problem, opportunity, landscape, approach (Core 3), AIME landscape, gap statement, inspired_by, key_references, and description.",
    "issue_2_insight": "ADDRESSED. InSight (arXiv 2603.01907) added alongside CurES in the Bayesian estimation landscape subsection. Key details: Beta(α,β) posterior with Beta(1,1) prior, weighted mutual information objective A(τ) = w(ϕ̄_τ) · I(R_{1:K}; Φ_τ), decomposition into difficulty-dependent (aleatoric: ϕ̄(1-ϕ̄)) and evidence-dependent (epistemic: 1/(n+1)²) components, temporal discounting (α_{t+1} = λα_t + (1-λ)α_0 + S_t), AIME24 53.75 on Qwen3-4B, ~2.2× training acceleration. Differentiation: InSight extends Bayesian RLVR estimation with epistemic uncertainty for selection from fixed pools; SACE-RLVR applies Bayesian estimation to archive replacement (different decision problem). InSight's temporal discounting adopted for our Beta parameter decay. Added to landscape, opportunity, core_problem, inspired_by, key_references.",
    "issue_3_core3_reframing": "ADDRESSED. Core 3 renamed from 'Zero-Cost Bayesian Learnability Estimation' to 'Zero-Cost Bayesian Learnability for Archive Replacement.' Now explicitly opens by acknowledging that Beta-Bernoulli estimation is an established technique in RLVR (CurES for sampling, InSight for MI-based selection, DBB for gradient estimation). Novelty repositioned around three specific aspects: (a) the decision problem (archive replacement in evolving archives, not sampling from fixed pools or gradient estimation); (b) credible intervals for replacement decisions (not point estimates for sampling); (c) zero additional inference cost via G=16 training rollout reuse (vs. CurES's separate estimation phase, DéjàQ's K=100 dedicated completions). Ablation A4 updated to reference CurES-style point estimation as comparison. This framing is more honest and equally compelling—the novelty is the application context and decision framework, not the statistical technique itself.",
    "issue_4_sec_3b_data": "ADDRESSED WITH CORRECTION. The reviewer suggested that 'SEC (20.0%) actually UNDERPERFORMS uniform sampling (23.33%)' at 3B scale. Verification against Actor-Curator's Table 1 (arXiv 2602.20532) reveals the numbers are inverted: Uniform=20.00%, SEC=23.33%, Actor-Curator=30.00% on AIME24 at Qwen2.5-3B. SEC modestly outperforms uniform (+3.33 absolute, +16.7% relative), while Actor-Curator substantially outperforms both (+10.0 over uniform, +50% relative). The corrected data still supports the broader analytical point: SEC's category-level approach yields only modest gains over uniform for harder competition-level problems, while Actor-Curator's per-problem utility estimation yields much larger gains, supporting the argument for finer-grained approaches and the limitations of coarse category-level bandits. Updated in landscape bandit section and opportunity section with correct numbers.",
    "issue_5_venue_timeline": "ADDRESSED. Removed ICLR 2027 (deadline ~Sep 24, 2026; with 14-18 week timeline starting late May 2026, earliest completion is mid-September—making ICLR 2027 nearly impossible). Retained ICML 2027 (~Jan 2027) as primary target and NeurIPS 2027 (~May 2027) as fallback with full evaluation."
  }
}
```

## Summary of Changes (Round 9 → Round 10)

### Critical Changes:

1. **CurES (arXiv 2510.01037) — CRITICAL ADDITION**: Added as the most directly comparable prior art for Core 3. Full technical details (Beta posteriors, optimal sampling ∝ exp(√[p(1-p)]/τ), point estimates, two-phase estimation, AIME24 24.58% on 7B). Four-dimensional differentiation: decision problem (sampling vs. replacement), estimation type (point vs. credible intervals), pool type (fixed vs. evolving archive), cost (separate phase vs. zero-cost rollout reuse). Integrated across all relevant sections.

2. **InSight (arXiv 2603.01907) — ADDITION**: Added alongside CurES. Key detail: mutual information decomposition revealing that difficulty-only selection (p(1-p)) is fundamentally limited — epistemic uncertainty matters too. Temporal discounting adopted for our Beta decay.

3. **Core 3 REFRAMED**: Renamed to "Zero-Cost Bayesian Learnability for **Archive Replacement**." Now opens by explicitly acknowledging CurES/InSight/DBB as establishing Beta posteriors in RLVR. Novelty repositioned to: (a) new decision problem (archive replacement), (b) credible intervals (not point estimates), (c) zero-cost rollout reuse.

4. **SEC 3B data CORRECTED**: Reviewer's claim that SEC underperforms uniform at 3B was inverted. Correct numbers from Actor-Curator Table 1: Uniform=20.00%, SEC=23.33%, Actor-Curator=30.00%. The valid analytical point is preserved: SEC's category-level gains are modest (+3.33) vs. Actor-Curator's substantial gains (+10.0).

5. **ICLR 2027 REMOVED** from venue targets — timeline makes it nearly impossible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed4a28b0-0628-4cf1-b9ba-7fbf0e64e075",
  "isSidechain": false,
  "requestId": "req_011CbUJVXCJcynpvS8z1HHpW",
  "type": "assistant",
  "uuid": "1f1106d1-e4c2-46b2-9106-10e9bf358843",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYuYojGsrmWe1VdfS8Gpcf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1932,
      "cache_read_input_tokens": 66626,
      "output_tokens": 19706,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19706,
          "cache_read_input_tokens": 66626,
          "cache_creation_input_tokens": 1932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1932
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

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "1f1106d1-e4c2-46b2-9106-10e9bf358843",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise RLVR archive approach for CurES acknowledgment",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "1f1106d1-e4c2-46b2-9106-10e9bf358843",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise RLVR archive approach for CurES acknowledgment",
  "sessionId": "3a999b40-0a1d-4b1d-a15f-656fc61cd73d"
}
```

---
