# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 94
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/e35f6048-c4fa-4353-9c1d-67bd6bba68b4.jsonl`
- **Structured JSON:** [`35c0f71dbccdaeaff2a4.json`](../../sessions/35/35c0f71dbccdaeaff2a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T03:05:53.691Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:05:53.691Z",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\",\n  \"core_problem\": \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the 'sparse policy selection' view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes 'capability boundary collapse' where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution—but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps. The fundamental open question is: can we build a system that ensures smooth difficulty×topic coverage while combining persistent archive-based gap identification, targeted weakness synthesis, and principled replacement criteria at competition level?\",\n  \"opportunity\": \"Four converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic—and multiple empirical findings support diversity's importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K→80K); per-niche survival varies dramatically by topic (geometry formalization is 6-7× harder than algebra per IndiMathBench). VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification (vs. reactive instance-level targeting), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria.\",\n  \"landscape\": \"**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\\n\\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\\n\\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold α=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively), AIME 2024: 13.3%. Training dynamics show over-specialization after ~120 steps (peak 69.5% declining to 61.6% by step 240)—precisely the curriculum drift that archive-based diversity maintenance prevents. Question pool grows 18× (1,136→20,532) as flat filtered dataset without structured organization. Differentiation: no persistent archives, no QD objectives, no systematic coverage tracking.\\n\\n**Implicit curriculum theory.** 'The Implicit Curriculum' (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation—not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: 'behavioral diversity is the binding constraint for RL.' RL-PLUS (arXiv 2508.00222) demonstrates 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\\n\\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\\n\\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%→16.4%; Qwen3-8B AIME24: 16.7→26.0. Proves diversity collapse is real (TTRL pass@16: 32.4→16.7).\\n\\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\\n\\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\\n\\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR—related to our approach but operates at policy gradient level vs. our archive-replacement level.\\n\\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K→80K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry formalization 6-7× harder than algebra (IndiMathBench arXiv 2512.00997: 12/98 geometry vs. much higher algebra/NT). These grounding data inform our per-niche survival estimates.\\n\\n**Verification.** VHG (arXiv 2605.06660): validity gating.\\n\\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE ~13%. Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\\n\\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\\n\\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\\n\\n**The precise gap.** DéjàQ: 1D, GSM-only. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization. Implicit curriculum: motivates smoothness but synthetic only. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification, competition-level verification, and Bayesian learnability replacement.\",\n  \"inspired_by\": \"DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools → over-specialization ~120 steps'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry 6-7× harder than algebra'] + EVOL_RL_warning['diversity collapse']\",\n  \"approach\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics. We organize the system around **three core innovations** plus **four extensions** tested in ablations. This follows the structure of successful prior systems: DéjàQ claims ~2 core contributions atop ~11 mechanisms; CLPO claims 3 named contributions atop ~7 design choices.\\n\\n**Design Motivation: Why Coverage Matters (Two Independent Arguments).**\\n\\n*Argument 1: Relay-regime-inspired smooth difficulty coverage.* The implicit curriculum theory (arXiv 2602.14872, ICML 2026) demonstrates on synthetic tasks that smooth difficulty spectra ('relay regime') yield faster convergence than gapped spectra ('grokking regime'). While this theory assumes idealized conditions (uniform distributions, geometric difficulty structure, single attention layer) that differ from real RLVR, it provides a principled design heuristic: smoother difficulty coverage should improve convergence. Our 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) are motivated by this insight. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n*Argument 2: Broad coverage prevents capability boundary collapse.* Even under the 'sparse policy selection' view where RL modifies only 1-3% of tokens (arXiv 2605.06241), comprehensive coverage is essential. Three empirical findings converge: (a) Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), each un-sharpened primitive type creates an exponential bottleneck; (b) Tailor (arXiv 2511.12429) directly demonstrates that behavioral diversity, not correctness, is the binding constraint for RL outcomes (25 vs. 4 primitives → substantial gains); (c) RL-PLUS (arXiv 2508.00222) shows narrow RLVR causes 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse distributions as the antidote (+69.2% relative improvement). Thus, comprehensive difficulty×topic coverage benefits under both views: relay-like curriculum dynamics AND broader capability activation.\\n\\n---\\n\\n**CORE INNOVATION 1: 2D Learnability Archive (50 cells).**\\n10 difficulty bins (width 0.1, empirical solve-rate) × 5 topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells, M=10 problems per cell. Topic classification via GPT-4o-mini (84-92% accuracy per arXiv 2411.00042). Difficulty measured via G=16 rollouts reused from training.\\n\\nThe 2D structure enables qualitatively new capabilities vs. prior work: (a) difficulty-aware coverage tracking—locate under-populated difficulty×topic niches BEFORE policy failures (vs. Socratic-Zero's reactive approach, SAGE's flat pool that over-specializes by step ~120); (b) persistent cross-step memory—problems track with the evolving policy, revealing emergent curriculum (vs. CLPO's stateless per-batch assessment); (c) interpretable post-hoc analysis—which niches drive benchmark performance.\\n\\nReplacement criterion: candidate problem enters a cell if its Bayesian learnability credible interval (see Core 3) exceeds the current worst occupant's upper bound. More principled than DéjàQ's point estimate comparison f(x')>f(y).\\n\\n**CORE INNOVATION 2: Proactive Gap-Targeted Synthesis with Verification.**\\nExisting targeting is reactive: Socratic-Zero examines specific failed solutions; SwS identifies aggregate weaknesses offline; SAGE's Challenger generates harder problems without coverage awareness. The 2D archive enables proactive niche-level gap identification:\\n\\n(a) Identify under-performing cells: <3 problems or stale (not refreshed for >100 training steps).\\n(b) Generate-then-classify synthesis: generate for target TOPIC without difficulty constraints, verify, then empirically measure difficulty via G=16 rollouts and assign to the appropriate cell. This avoids the 'double filter' problem (constraining both topic AND difficulty yields 4-17% per SPARQ/MathSmith evidence; topic-only yields higher survival).\\n(c) 3-stage VHG-inspired verification: (i) format/solvability check (filters ~25-30%, consistent with FLAMES ~30% removal), (ii) cross-verification via majority vote across 2-3 strong models (filters ~15-20%), (iii) difficulty calibration via G=16 rollouts.\\n\\n**Concrete per-niche survival estimates (literature-grounded):**\\nEstimates sourced from SPARQ (~25% QD survival), DART-Math (51.1% Level 5 dropout), FLAMES (50% removal at Level 5), and IndiMathBench (geometry 6-7× harder than algebra).\\n\\n- Easy-medium cells (solve-rate 0.3-0.8), common topics (Algebra, NT): ~30 cells, ~30-50% survival.\\n  Need ~20-35 candidates/cell → ~600-1,050 total.\\n- Medium-hard cells (solve-rate 0.1-0.3), common topics: ~10 cells, ~15-25% survival.\\n  Need ~40-65 candidates/cell → ~400-650 total.\\n- Geometry cells (all difficulties): ~10 cells, ~5-15% survival (6-7× harder than algebra per IndiMathBench).\\n  Need ~65-200 candidates/cell → ~650-2,000 total.\\n- Extreme cells (solve-rate <0.1 or >0.9, all topics): ~10 cells, ~3-8% survival (DART-Math: Level 5 loses 51% coverage; FLAMES: 50% removal at Level 5).\\n  Need ~125-330 candidates/cell → ~1,250-3,300 total. Geometry extremes: ~1-3% survival, ~330-1,000 candidates/cell.\\n- **Graceful degradation:** cells that cannot reach M=10 accept minimum 3 (sufficient for meaningful Beta posterior updates). Archive reports actual occupancy; analysis accounts for sparse cells.\\n- **Total per refresh cycle:** ~2,900-7,000 candidates (median ~4,500). Generation cost using open-source 70B teacher: ~150 GPU-hours. Verification (G=16 rollouts per candidate on 7B): ~12 GPU-hours. Per-refresh total: ~162 GPU-hours. Over ~10 refreshes: ~1,620 GPU-hours. Alternative: API-based generation at ~$0.30/problem ≈ $1,350/refresh, $13,500 total.\\n- Per-niche survival rates and generation statistics reported as community contribution.\\n\\n**CORE INNOVATION 3: Zero-Cost Bayesian Learnability Estimation.**\\nDéjàQ estimates learnability via K=100 dedicated completions per problem—computationally expensive and separate from training. We reuse G=16 rollouts already generated for GRPO training—zero additional inference cost. G=16 is well-justified: DAPO (arXiv 2503.14476) standardizes G=16; MC-GRPO (arXiv 2601.22582) shows clear degradation at small G (G=2: 78.92%, G=4: 81.34%, G=8: 84.53%); the Gradient Starvation analysis (arXiv 2605.07689) explains the mechanism—for binary rewards, degenerate group probability is p^G+(1-p)^G, yielding 69.25% degenerate groups at G=4 vs. <1% at G=8.\\n\\nBayesian temporal smoothing: Beta-Bernoulli running posterior per problem (Beta(1,1) prior, updated each appearance). After 3 appearances (48 cumulative rollouts), posterior variance drops ~3×. Replacement uses conservative credible interval: candidate must exceed occupant's upper bound, preventing noisy replacements.\\n\\nRelated but distinct from the Discounted Beta-Bernoulli (DBB) estimator (arXiv 2603.18444), which applies Bayesian estimation at the policy gradient level. Our Beta posterior operates at the archive-replacement level for per-problem learnability tracking—a different application of the same statistical principle. VCRL's insight (arXiv 2509.19803) that reward variance reflects difficulty is extended from curriculum signal to Bayesian replacement criterion.\\n\\n---\\n\\n**EXTENSIONS (each tested in one ablation, not claimed as core contributions):**\\n\\nE1: Cross-niche SvS seeding. SvS-style answer-preserving mutation (ICLR 2026) from adjacent cells to seed under-populated niches. Expected ~70-80% validity for within-topic mutations. Particularly valuable for geometry and extreme cells where de novo generation has <5% survival. Tested in A5.\\n\\nE2: James-Stein shrinkage. Following arXiv 2511.03710 (which demonstrates shrinkage baselines reduce MSE in RLVR), we apply shrinkage to per-problem learnability estimates, regularizing toward batch average. Not claimed as novel—cite and use. Tested in A6.\\n\\nE3: DGPO policy updates. MAD normalization + DQW weighting adopted from MathForge (arXiv 2601.20614, ICLR 2026). Addresses difficulty-dependent advantage scale. Tested in A7.\\n\\nE4: ZPD-weighted sampling. Sample from archive with Zone of Proximal Development weighting [0.1, 0.9] solve-rate, weighted by posterior variance (high uncertainty → more sampling).\\n\\n---\\n\\n**Training Loop (VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary):**\\n(a) Sample from archive with ZPD weighting. (b) G=16 rollouts, compute advantages. (c) Policy update (GRPO or DGPO). (d) Update Beta posteriors per problem. (e) Every 50 steps: refresh sampled cells, reassign problems that shifted difficulty, flag stale cells, synthesize for gaps. Overhead: ~20-25% vs. vanilla GRPO (dominated by synthesis cost).\\n\\n**AIME Contextualization.** Distillation-based: 70-90% AIME 2024. Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE ~13%. Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm. Value: METHOD + ABLATION INSIGHTS. Framework applicable atop distilled bases.\\n\\n**Baselines (7):** (1) DéjàQ-comp [PRIMARY: 2D+targeting value]. (2) CLPO [PRIMARY: persistence value]. (3) Socratic-Zero [PRIMARY: structured vs. instance-level]. (4) SAGE [concurrent; structured vs. flat diversity]. (5) EVOL-RL [stateless diversity]. (6) MathForge [DGPO source]. (7) Vanilla GRPO [minimal].\\n\\n**Ablations (7):**\\nA1: 1D archive only (tests Core 1 dimensionality).\\nA2: Random synthesis vs. gap-targeted (tests Core 2 proactive targeting).\\nA3: 3 bins vs. 10 bins [relay-regime-inspired test: first empirical comparison of coarse vs. fine difficulty granularity in real RLVR].\\nA4: Point estimation vs. Beta posterior (tests Core 3 vs. DéjàQ-style p(1-p)).\\nA5: Without cross-niche SvS seeding (tests E1 value, especially for sparse cells).\\nA6: Without James-Stein shrinkage (tests E2).\\nA7: GRPO vs. DGPO (tests E3).\\n\\n**Evaluation:** AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. pass@1 AND pass@k (pass@k especially important per RL-PLUS's capability boundary collapse finding—we test whether archive-based diversity prevents this). DAPO-Math-17k seeds.\\n\\n**Key Analyses:** (1) Coverage heatmaps showing cell occupancy evolution. (2) Per-cell benchmark contribution: which niches drive gains? (3) Emergent curriculum: bin-transition frequencies as policy improves. (4) Synthesis efficiency: per-topic survival rates vs. literature benchmarks (SPARQ, DART-Math, FLAMES), reported as community contribution. (5) Convergence speed: 10 vs. 3 bins. (6) Capability boundary: pass@1 vs. pass@k trajectories—does archive diversity prevent RL-PLUS-style collapse? (7) Structured vs. flat: archive coverage diversity over training vs. SAGE-style accumulation.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"6,700 H100-hours (baselines: 7×250h=1,750h; SACE-RLVR 7B 800h; SACE-RLVR 8B 800h; ablations 7×200h=1,400h; synthesis/verification 1,620h; archive overhead 330h)\",\n      \"timeline\": \"14-18 weeks\",\n      \"estimated_gpu_cost\": \"$16,750 (at ~$2.50/H100-hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"5,200 H100-hours (reuse released code; shared verification; API-based generation saves ~1,200 GPU-hrs but adds ~$13,500 API cost)\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$400-800 (code assistance)\",\n      \"synthesis_api_cost\": \"$8,000-13,500 (problem generation via API, optional vs. GPU)\",\n      \"estimated_gpu_cost\": \"$13,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"8,200 H100-hours (exploratory sweeps over archive dimensions, bin count, refresh frequency, replacement criteria, synthesis strategies)\",\n      \"timeline\": \"10-13 weeks\",\n      \"claude_api_cost\": \"$1,000-2,000\",\n      \"estimated_gpu_cost\": \"$20,500\",\n      \"speed_bottleneck\": \"GPU queue; each GRPO run 24-72h on 8×H100s. Synthesis for geometry extreme cells dominates generation cost.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (Sep 19-24, 2026) — stretch if pilot results by August\",\n    \"ICML 2027 (~Jan 2027) — primary target, strong fit for RL + QD + coverage\",\n    \"NeurIPS 2027 (~May 2027) — fallback with full evaluation\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"DéjàQ (arXiv 2601.01931) — PRIMARY PREDECESSOR, online MAP-Elites for RLVR at GSM level\",\n    \"CLPO (arXiv 2509.25004) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024\",\n    \"Socratic-Zero (arXiv 2509.24726) — PRIMARY BASELINE, three-agent co-evolution; 56.1% avg\",\n    \"SAGE (arXiv 2603.15255) — CONCURRENT, 4-agent self-evolution; over-specializes ~120 steps; AIME 2024 13.3%\",\n    \"The Implicit Curriculum (arXiv 2602.14872, ICML 2026) — DESIGN MOTIVATION, relay vs. grokking (synthetic tasks)\",\n    \"Sparse Policy Selection (arXiv 2605.06241) — RL modifies 1-3% of tokens; motivates broad coverage\",\n    \"Sharper Primitives (arXiv 2602.08281) — RLVR polarizes; multiplicative compounding; diverse training activates broader primitives\",\n    \"Tailor (arXiv 2511.12429) — behavioral diversity is binding constraint for RL; 25 vs 4 primitives\",\n    \"RL-PLUS (arXiv 2508.00222) — capability boundary collapse from narrow RLVR; +69.2% with diversity\",\n    \"ProRL (arXiv 2505.24864) — diverse prolonged training accesses beyond base model ceiling\",\n    \"Bidirectional Curriculum Generation (arXiv 2603.05120) — 4-agent bidirectional; 60.03 avg\",\n    \"EVOL-RL (arXiv 2509.15194) — stateless novelty-aware diversity; AIME25 16.4%\",\n    \"MathForge/DGPO (arXiv 2601.20614, ICLR 2026) — MAD normalization; adopted as extension\",\n    \"VCRL (arXiv 2509.19803) — reward variance as difficulty proxy; G=16; 57.76 avg Qwen3-8B\",\n    \"MC-GRPO (arXiv 2601.22582) — rollout count ablation: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%\",\n    \"Gradient Starvation (arXiv 2605.07689) — 69% degenerate groups at G=4; explains G effect mechanistically\",\n    \"DAPO (arXiv 2503.14476) — standardizes G=16\",\n    \"Discounted Beta-Bernoulli (arXiv 2603.18444) — Bayesian estimation for RLVR; validates Beta approach\",\n    \"SwS (NeurIPS 2025, arXiv 2506.08989) — offline weakness targeting; +10%\",\n    \"SvS (ICLR 2026) — answer-preserving synthesis; used for cross-niche seeding\",\n    \"SAND-Math (arXiv 2507.20527) — ~38% end-to-end competition synthesis survival\",\n    \"SPARQ (arXiv 2506.06499) — ~25% QD survival (320K→80K); per-niche evidence\",\n    \"DART-Math (arXiv 2407.13690, NeurIPS 2024) — Level 5: 51.1% query dropout; difficulty survival data\",\n    \"FLAMES (arXiv 2508.16514) — ~30% strict survival; Level 5: 50% removal\",\n    \"IndiMathBench (arXiv 2512.00997) — geometry formalization 6-7× harder than algebra\",\n    \"VHG (arXiv 2605.06660) — validity gating; inspires verification\",\n    \"Shrinking the Variance (arXiv 2511.03710) — James-Stein shrinkage for RLVR\",\n    \"EBPO (arXiv 2602.05165) — empirical Bayes for GRPO\",\n    \"R-Zero (ICLR 2026) — self-evolving; collapses iter 3\",\n    \"Klear-Reasoner-8B (arXiv 2508.07629) — 90.5% AIME 2024; distillation context\",\n    \"Prism (arXiv 2603.13309) — 128-cluster diversity with ZPD gate\",\n    \"R-Diverse (arXiv 2602.13103) — SAM skill diversity + MAP memory\",\n    \"STAT (arXiv 2510.10023) — Missing-Skill-Profile\",\n    \"Problem Categorization (arXiv 2411.00042) — topic classification\",\n    \"Two-Stage Dynamic View (arXiv 2510.04028) — capability shrinkage then expansion\",\n    \"Does RL Incentivize Reasoning? (NeurIPS 2025, arXiv 2504.13837) — coverage framing\"\n  ],\n  \"description\": \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), scaling online MAP-Elites from GSM-level (DéjàQ) to competition-level math through three core innovations plus four extensions. Two independent motivations for comprehensive coverage: (1) relay-regime theory (arXiv 2602.14872) suggests smooth difficulty spectra yield faster convergence—adopted as design heuristic, not guarantee, with A3 testing empirically; (2) even under 'sparse policy selection' (1-3% tokens modified), broad coverage prevents 'capability boundary collapse' (RL-PLUS: pass@1↑ pass@128↓; +69.2% with diversity), ensures multiplicative primitive sharpening across domains (Sharper Primitives), and provides the behavioral diversity that is the binding constraint for RL (Tailor: 25 vs 4 primitives). Core 1: 2D archive (10 bins × 5 topics = 50 cells) with proactive gap identification and Bayesian replacement—addresses SAGE's over-specialization at step ~120. Core 2: generate-then-classify synthesis with literature-grounded per-niche survival estimates (central: 30-50%, geometry: 5-15%, extreme: 3-8%; geometry extremes ~1-3% per IndiMathBench; graceful degradation to min 3/cell; ~162 GPU-hrs/refresh). Core 3: zero-cost Bayesian estimation via G=16 rollout reuse (vs DéjàQ K=100), Beta posterior + credible intervals; G=16 justified by MC-GRPO ablation + gradient starvation analysis (69% degenerate groups at G=4). Extensions: SvS seeding, shrinkage, DGPO, ZPD—each ablated. Seven baselines (DéjàQ-comp, CLPO, Socratic-Zero, SAGE, EVOL-RL, MathForge, GRPO), seven ablations including pass@k capability boundary analysis. Qwen2.5-Math-7B/Qwen3-8B, AIME 2024/2025, MATH-500, AMC, Minerva, OlympiadBench.\",\n  \"project_name\": \"sace_rlvr\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"revision_overview\": \"MAJOR REVISION addressing score stagnation (3.2→3.5 over 3 rounds) through structural simplification and substantive strengthening rather than incremental patching. Four structural changes: (1) radical simplification to 3 core + 4 extensions (from ~12 components), (2) honest theoretical scoping as 'design motivation' not 'backbone,' (3) all factual errors corrected via primary source verification, (4) substantially strengthened coverage motivation with independent empirical arguments from capability boundary collapse, multiplicative primitive compounding, and behavioral diversity literature. SAGE added. Per-niche estimates grounded in 5 synthesis papers. Seven focused ablations.\",\n    \"issue_1_vcrl_factual_errors\": \"FIXED (CRITICAL). Verified by reading actual paper: (a) 44.17 does not exist in VCRL—closest is 44.73 (GRPO+VDS ablation, 4B); (b) 49.43 = VCRL on Qwen3-4B, 57.76 = VCRL on Qwen3-8B—MODEL SIZES not rollout counts; (c) VCRL performs NO G ablation; (d) uses 'reward variance' not 'advantage variance.' New G=16 justification: MC-GRPO ablation (G=2: 78.92%, G=4: 81.34%, G=8: 84.53%); Gradient Starvation (69% degenerate groups at G=4, mechanistic explanation via p^G+(1-p)^G); DAPO standard. VCRL cited only for reward variance as difficulty proxy.\",\n    \"issue_2_theoretical_backbone_honestly_scoped\": \"RESTRUCTURED. Now explicitly: 'design motivation' not 'theoretical backbone.' 'Validated on synthetic tasks with idealized assumptions... principled design heuristic... A3 provides first empirical test... We do not claim theoretical guarantees transfer.' PAIRED with independent empirical motivation (Argument 2) that does not depend on theoretical transfer: capability boundary collapse, multiplicative compounding, behavioral diversity as binding constraint. This dual-motivation structure is MORE compelling than the original single-theory framing.\",\n    \"issue_3_sage_added\": \"ADDED with detailed analysis. 4-agent framework, 500-example seed, Qwen-2.5-7B. Key finding: over-specialization after ~120 steps (69.5%→61.6%) due to flat unstructured pool growing 18×. Added as baseline #4. New analysis #7 compares structured archive vs. flat accumulation.\",\n    \"issue_4_minor_factual_errors\": \"FIXED. EVOL-RL: 16.4% (abstract; noted internal paper inconsistency with Table 1's 17.1%). SAND-Math: '~38% end-to-end (8,842/23,437)' with stage breakdown (~75%/~57%/~96%); paper's '41.9% yield' is generation-stage metric.\",\n    \"issue_5_sparse_policy_selection\": \"ADDRESSED SUBSTANTIVELY with three independently sourced empirical arguments, elevated to co-equal Argument 2: (a) Sharper Primitives: RLVR polarizes, multiplicative compounding P(q) ∝ ∏P(sⱼ) means un-sharpened primitives create exponential bottleneck; (b) Tailor: 25 vs 4 primitives → substantial gains, 'behavioral diversity is binding constraint'; (c) RL-PLUS: 'capability boundary collapse'—pass@1↑ pass@128↓, +69.2% with diversity. Key insight: sparse selection makes coverage MORE important, not less—determines WHICH capabilities get activated from base model's latent repertoire. Added pass@k evaluation (analysis #6) to test whether archive diversity prevents collapse.\",\n    \"issue_6_per_niche_survival_estimates\": \"ADDED with literature-grounded estimates from 5 papers. SPARQ: 25% QD survival. DART-Math: Level 5 loses 51.1% coverage. FLAMES: Level 5 removes 50%. IndiMathBench: geometry 6-7× harder. Estimates: central 30-50%, medium-hard 15-25%, geometry 5-15%, extreme 3-8%, geometry extreme 1-3%. Overgeneration: 20-330×/cell depending on niche. Cost: ~162 GPU-hrs/refresh (generation ~150h + verification ~12h) × 10 refreshes = ~1,620 GPU-hrs. Alternative API: ~$13,500. Graceful degradation: min 3/cell. Per-niche survival reported as community contribution.\",\n    \"issue_7_system_complexity_reduced\": \"MAJOR RESTRUCTURING. 3 core + 4 extensions (from ~12 components). Core 1: 2D Learnability Archive. Core 2: Proactive Gap-Targeted Synthesis. Core 3: Zero-Cost Bayesian Estimation. Extensions: E1 SvS seeding, E2 James-Stein shrinkage (not claimed novel, cites arXiv 2511.03710), E3 DGPO (adopted from MathForge), E4 ZPD sampling. Ablations 10→7, baselines 10→7. Follows DéjàQ pattern (~11 mechanisms, ~2 claims). Cleaner narrative: 'persistent Bayesian QD archive with proactive synthesis for competition-level RLVR.'\"\n  }\n}\n\n## Reviewer feedback (round 8)\nIssues: [\"CRITICAL PERSISTENT (Round 1→8, 7 rounds unaddressed): SEC (arXiv 2505.14970) formulates curriculum as MAB over problem categories (difficulty × type) during RL, achieving 17.5% AIME24 on Qwen2.5-7B (+27% relative). This directly parallels SACE-RLVR's per-niche archive management. Actor-Curator (arXiv 2602.20532) explicitly beats SEC with a neural curator achieving 30.0% AIME24 (+28.6% relative) and ~9% overhead via policy-improvement bandits with regret guarantees. Both select from existing pools rather than synthesizing—the proposal MUST argue why persistent archives with synthesis outperform principled bandit selection. This is the #1 reviewer objection waiting to happen.\", \"CRITICAL PERSISTENT (Round 6→8, 2 rounds unaddressed): Online Difficulty Filtering (arXiv 2504.03380) proves balanced difficulty filtering maximizes a lower bound on expected policy improvement. +12% gains in half the training steps. This theoretical result SUPPORTS the proposal's difficulty-aware motivation and should be cited as evidence, yet remains omitted.\", \"PERSISTENT FACTUAL ERROR (Round 6→8): IndiMathBench geometry ratio still claimed as '6-7× harder' throughout (per-niche estimates, landscape section). Actual: 12/98=12.2% geometry BEq vs 96/214=44.9% non-geometry = ~3.7× ratio. Additionally, the paper attributes geometry difficulty partly to 'Mathlib's lacking support for Olympiad-style geometry' (formalization-specific), which may not transfer to problem synthesis difficulty.\", \"PERSISTENT MISLEADING PRESENTATION (Round 6→8): SAGE AIME 2024 presented as '13.3%' without noting this equals the Qwen-2.5-7B base model (also 13.3%). SAGE shows ZERO AIME improvement and actually DEGRADES AMC 2023 (57.5%→52.5%). This is STRONGER evidence for over-specialization than presented—SAGE improves narrow benchmarks (OlympiadBench +10.7%) while failing or degrading competition-level OOD tasks.\", \"NEW CONCURRENT WORK: UCPO (arXiv 2605.00365, May 2026) addresses the same pass@k diversity collapse via Uniform-Correct Policy Optimization, achieving +10% absolute AIME24 at Pass@64 and +45% equation-level diversity. This is a simpler, policy-level alternative to archive-based diversity maintenance that directly competes with the pass@k capability boundary analysis (Analysis #6).\", \"NEW CONCURRENT WORK: Vocabulary Dropout (arXiv 2604.03472, Apr 2026) achieves +4.4 average points at 8B on competition benchmarks via lightweight logit masking—a minimal alternative to archive-based diversity. Flagged in Round 7 as recommended, still unaddressed.\", \"MISSING RECOMMENDED WORK: SOAR (arXiv 2601.18778) meta-RL teacher for learnability-targeted synthesis at the 'edge of learnability'—conceptually parallel to SACE-RLVR's proactive gap identification. Recommended in Round 7, still unaddressed.\"]\nFeedback: This is Round 8 of 10. The proposal has matured into a thorough, honestly-framed integration paper with a clean 3+4 structure, but **the persistent failure to address SEC and Actor-Curator after 7 rounds is now the single blocking issue**. These are not obscure works—they are the most direct competitors in the adaptive curriculum during RL space, and any RLVR reviewer will immediately identify them.\n\n**BLOCKING (must fix in Round 9 to have any chance of passing in Round 10):**\n\n(1) **Add SEC and Actor-Curator as related work AND add Actor-Curator as an 8th baseline.** SEC does MAB over problem categories (17.5% AIME24, +27% relative on Qwen2.5-7B). Actor-Curator does neural bandit selection with regret guarantees (30.0% AIME24, +28.6% relative, ~9% overhead) and explicitly beats SEC. The key differentiations:\n- SEC/Actor-Curator select from FIXED pools; SACE-RLVR SYNTHESIZES for identified gaps\n- Bandit methods are effectively stateless per-step; archive management provides persistent cross-step memory with coverage tracking\n- Archives enable interpretable coverage maps, proactive gap identification, and post-hoc niche contribution analysis\n- The approaches are potentially COMPLEMENTARY: Actor-Curator could serve as the sampling strategy FROM the archive\n\n(2) **Fix IndiMathBench ratio.** Change '6-7× harder' to '~3.7× lower success rate (12.2% vs 44.9% BEq)' and note the formalization-specific context. Adjust per-niche survival estimates downward accordingly for geometry cells.\n\n(3) **Correct SAGE AIME presentation.** State explicitly: 'SAGE achieves 13.3% AIME 2024, matching the Qwen-2.5-7B base model (also 13.3%), and degrades AMC 2023 from 57.5% to 52.5%—demonstrating that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance.'\n\n**STRONGLY RECOMMENDED (would improve scores):**\n\n(4) **Cite Online Difficulty Filtering** (arXiv 2504.03380). Its theoretical result (balanced filtering maximizes policy improvement lower bound) SUPPORTS your difficulty-aware motivation. One sentence in the 'Difficulty-aware' section.\n\n(5) **Add UCPO as concurrent related work.** It addresses pass@k diversity collapse via policy optimization rather than archive-based diversity. Brief mention with differentiation: UCPO modifies the optimization objective; SACE-RLVR modifies the training distribution. Potentially complementary.\n\n(6) **Add Vocabulary Dropout and SOAR** as brief concurrent work mentions.\n\n**WARNING:** Round 10 requires a final pass/fail decision. At current scores (avg 3.375), the proposal will fail unless SEC/Actor-Curator engagement substantially strengthens the novelty argument and demonstrates why archive-based approaches offer capabilities that bandit-based selection cannot.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 8 轮修订，近 3 轮平均分从 3.6 到 3.4，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T03:05:53.694Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:05:53.694Z",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

## Round 1

92 recorded events

### User

_source line 3 · 2026-05-28T03:05:53.741Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
{
  "title": "Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis",
  "core_problem": "Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the 'sparse policy selection' view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes 'capability boundary collapse' where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution—but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps. The fundamental open question is: can we build a system that ensures smooth difficulty×topic coverage while combining persistent archive-based gap identification, targeted weakness synthesis, and principled replacement criteria at competition level?",
  "opportunity": "Four converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic—and multiple empirical findings support diversity's importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K→80K); per-niche survival varies dramatically by topic (geometry formalization is 6-7× harder than algebra per IndiMathBench). VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification (vs. reactive instance-level targeting), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria.",
  "landscape": "**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\n\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\n\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\n\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold α=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively), AIME 2024: 13.3%. Training dynamics show over-specialization after ~120 steps (peak 69.5% declining to 61.6% by step 240)—precisely the curriculum drift that archive-based diversity maintenance prevents. Question pool grows 18× (1,136→20,532) as flat filtered dataset without structured organization. Differentiation: no persistent archives, no QD objectives, no systematic coverage tracking.\n\n**Implicit curriculum theory.** 'The Implicit Curriculum' (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation—not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\n\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: 'behavioral diversity is the binding constraint for RL.' RL-PLUS (arXiv 2508.00222) demonstrates 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\n\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\n\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%→16.4%; Qwen3-8B AIME24: 16.7→26.0. Proves diversity collapse is real (TTRL pass@16: 32.4→16.7).\n\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\n\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\n\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR—related to our approach but operates at policy gradient level vs. our archive-replacement level.\n\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K→80K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry formalization 6-7× harder than algebra (IndiMathBench arXiv 2512.00997: 12/98 geometry vs. much higher algebra/NT). These grounding data inform our per-niche survival estimates.\n\n**Verification.** VHG (arXiv 2605.06660): validity gating.\n\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE ~13%. Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\n\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\n\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\n\n**The precise gap.** DéjàQ: 1D, GSM-only. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization. Implicit curriculum: motivates smoothness but synthetic only. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification, competition-level verification, and Bayesian learnability replacement.",
  "inspired_by": "DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools → over-specialization ~120 steps'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry 6-7× harder than algebra'] + EVOL_RL_warning['diversity collapse']",
  "approach": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics. We organize the system around **three core innovations** plus **four extensions** tested in ablations. This follows the structure of successful prior systems: DéjàQ claims ~2 core contributions atop ~11 mechanisms; CLPO claims 3 named contributions atop ~7 design choices.\n\n**Design Motivation: Why Coverage Matters (Two Independent Arguments).**\n\n*Argument 1: Relay-regime-inspired smooth difficulty coverage.* The implicit curriculum theory (arXiv 2602.14872, ICML 2026) demonstrates on synthetic tasks that smooth difficulty spectra ('relay regime') yield faster convergence than gapped spectra ('grokking regime'). While this theory assumes idealized conditions (uniform distributions, geometric difficulty structure, single attention layer) that differ from real RLVR, it provides a principled design heuristic: smoother difficulty coverage should improve convergence. Our 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) are motivated by this insight. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\n\n*Argument 2: Broad coverage prevents capability boundary collapse.* Even under the 'sparse policy selection' view where RL modifies only 1-3% of tokens (arXiv 2605.06241), comprehensive coverage is essential. Three empirical findings converge: (a) Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), each un-sharpened primitive type creates an exponential bottleneck; (b) Tailor (arXiv 2511.12429) directly demonstrates that behavioral diversity, not correctness, is the binding constraint for RL outcomes (25 vs. 4 primitives → substantial gains); (c) RL-PLUS (arXiv 2508.00222) shows narrow RLVR causes 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse distributions as the antidote (+69.2% relative improvement). Thus, comprehensive difficulty×topic coverage benefits under both views: relay-like curriculum dynamics AND broader capability activation.\n\n---\n\n**CORE INNOVATION 1: 2D Learnability Archive (50 cells).**\n10 difficulty bins (width 0.1, empirical solve-rate) × 5 topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells, M=10 problems per cell. Topic classification via GPT-4o-mini (84-92% accuracy per arXiv 2411.00042). Difficulty measured via G=16 rollouts reused from training.\n\nThe 2D structure enables qualitatively new capabilities vs. prior work: (a) difficulty-aware coverage tracking—locate under-populated difficulty×topic niches BEFORE policy failures (vs. Socratic-Zero's reactive approach, SAGE's flat pool that over-specializes by step ~120); (b) persistent cross-step memory—problems track with the evolving policy, revealing emergent curriculum (vs. CLPO's stateless per-batch assessment); (c) interpretable post-hoc analysis—which niches drive benchmark performance.\n\nReplacement criterion: candidate problem enters a cell if its Bayesian learnability credible interval (see Core 3) exceeds the current worst occupant's upper bound. More principled than DéjàQ's point estimate comparison f(x')>f(y).\n\n**CORE INNOVATION 2: Proactive Gap-Targeted Synthesis with Verification.**\nExisting targeting is reactive: Socratic-Zero examines specific failed solutions; SwS identifies aggregate weaknesses offline; SAGE's Challenger generates harder problems without coverage awareness. The 2D archive enables proactive niche-level gap identification:\n\n(a) Identify under-performing cells: <3 problems or stale (not refreshed for >100 training steps).\n(b) Generate-then-classify synthesis: generate for target TOPIC without difficulty constraints, verify, then empirically measure difficulty via G=16 rollouts and assign to the appropriate cell. This avoids the 'double filter' problem (constraining both topic AND difficulty yields 4-17% per SPARQ/MathSmith evidence; topic-only yields higher survival).\n(c) 3-stage VHG-inspired verification: (i) format/solvability check (filters ~25-30%, consistent with FLAMES ~30% removal), (ii) cross-verification via majority vote across 2-3 strong models (filters ~15-20%), (iii) difficulty calibration via G=16 rollouts.\n\n**Concrete per-niche survival estimates (literature-grounded):**\nEstimates sourced from SPARQ (~25% QD survival), DART-Math (51.1% Level 5 dropout), FLAMES (50% removal at Level 5), and IndiMathBench (geometry 6-7× harder than algebra).\n\n- Easy-medium cells (solve-rate 0.3-0.8), common topics (Algebra, NT): ~30 cells, ~30-50% survival.\n  Need ~20-35 candidates/cell → ~600-1,050 total.\n- Medium-hard cells (solve-rate 0.1-0.3), common topics: ~10 cells, ~15-25% survival.\n  Need ~40-65 candidates/cell → ~400-650 total.\n- Geometry cells (all difficulties): ~10 cells, ~5-15% survival (6-7× harder than algebra per IndiMathBench).\n  Need ~65-200 candidates/cell → ~650-2,000 total.\n- Extreme cells (solve-rate <0.1 or >0.9, all topics): ~10 cells, ~3-8% survival (DART-Math: Level 5 loses 51% coverage; FLAMES: 50% removal at Level 5).\n  Need ~125-330 candidates/cell → ~1,250-3,300 total. Geometry extremes: ~1-3% survival, ~330-1,000 candidates/cell.\n- **Graceful degradation:** cells that cannot reach M=10 accept minimum 3 (sufficient for meaningful Beta posterior updates). Archive reports actual occupancy; analysis accounts for sparse cells.\n- **Total per refresh cycle:** ~2,900-7,000 candidates (median ~4,500). Generation cost using open-source 70B teacher: ~150 GPU-hours. Verification (G=16 rollouts per candidate on 7B): ~12 GPU-hours. Per-refresh total: ~162 GPU-hours. Over ~10 refreshes: ~1,620 GPU-hours. Alternative: API-based generation at ~$0.30/problem ≈ $1,350/refresh, $13,500 total.\n- Per-niche survival rates and generation statistics reported as community contribution.\n\n**CORE INNOVATION 3: Zero-Cost Bayesian Learnability Estimation.**\nDéjàQ estimates learnability via K=100 dedicated completions per problem—computationally expensive and separate from training. We reuse G=16 rollouts already generated for GRPO training—zero additional inference cost. G=16 is well-justified: DAPO (arXiv 2503.14476) standardizes G=16; MC-GRPO (arXiv 2601.22582) shows clear degradation at small G (G=2: 78.92%, G=4: 81.34%, G=8: 84.53%); the Gradient Starvation analysis (arXiv 2605.07689) explains the mechanism—for binary rewards, degenerate group probability is p^G+(1-p)^G, yielding 69.25% degenerate groups at G=4 vs. <1% at G=8.\n\nBayesian temporal smoothing: Beta-Bernoulli running posterior per problem (Beta(1,1) prior, updated each appearance). After 3 appearances (48 cumulative rollouts), posterior variance drops ~3×. Replacement uses conservative credible interval: candidate must exceed occupant's upper bound, preventing noisy replacements.\n\nRelated but distinct from the Discounted Beta-Bernoulli (DBB) estimator (arXiv 2603.18444), which applies Bayesian estimation at the policy gradient level. Our Beta posterior operates at the archive-replacement level for per-problem learnability tracking—a different application of the same statistical principle. VCRL's insight (arXiv 2509.19803) that reward variance reflects difficulty is extended from curriculum signal to Bayesian replacement criterion.\n\n---\n\n**EXTENSIONS (each tested in one ablation, not claimed as core contributions):**\n\nE1: Cross-niche SvS seeding. SvS-style answer-preserving mutation (ICLR 2026) from adjacent cells to seed under-populated niches. Expected ~70-80% validity for within-topic mutations. Particularly valuable for geometry and extreme cells where de novo generation has <5% survival. Tested in A5.\n\nE2: James-Stein shrinkage. Following arXiv 2511.03710 (which demonstrates shrinkage baselines reduce MSE in RLVR), we apply shrinkage to per-problem learnability estimates, regularizing toward batch average. Not claimed as novel—cite and use. Tested in A6.\n\nE3: DGPO policy updates. MAD normalization + DQW weighting adopted from MathForge (arXiv 2601.20614, ICLR 2026). Addresses difficulty-dependent advantage scale. Tested in A7.\n\nE4: ZPD-weighted sampling. Sample from archive with Zone of Proximal Development weighting [0.1, 0.9] solve-rate, weighted by posterior variance (high uncertainty → more sampling).\n\n---\n\n**Training Loop (VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary):**\n(a) Sample from archive with ZPD weighting. (b) G=16 rollouts, compute advantages. (c) Policy update (GRPO or DGPO). (d) Update Beta posteriors per problem. (e) Every 50 steps: refresh sampled cells, reassign problems that shifted difficulty, flag stale cells, synthesize for gaps. Overhead: ~20-25% vs. vanilla GRPO (dominated by synthesis cost).\n\n**AIME Contextualization.** Distillation-based: 70-90% AIME 2024. Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE ~13%. Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm. Value: METHOD + ABLATION INSIGHTS. Framework applicable atop distilled bases.\n\n**Baselines (7):** (1) DéjàQ-comp [PRIMARY: 2D+targeting value]. (2) CLPO [PRIMARY: persistence value]. (3) Socratic-Zero [PRIMARY: structured vs. instance-level]. (4) SAGE [concurrent; structured vs. flat diversity]. (5) EVOL-RL [stateless diversity]. (6) MathForge [DGPO source]. (7) Vanilla GRPO [minimal].\n\n**Ablations (7):**\nA1: 1D archive only (tests Core 1 dimensionality).\nA2: Random synthesis vs. gap-targeted (tests Core 2 proactive targeting).\nA3: 3 bins vs. 10 bins [relay-regime-inspired test: first empirical comparison of coarse vs. fine difficulty granularity in real RLVR].\nA4: Point estimation vs. Beta posterior (tests Core 3 vs. DéjàQ-style p(1-p)).\nA5: Without cross-niche SvS seeding (tests E1 value, especially for sparse cells).\nA6: Without James-Stein shrinkage (tests E2).\nA7: GRPO vs. DGPO (tests E3).\n\n**Evaluation:** AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. pass@1 AND pass@k (pass@k especially important per RL-PLUS's capability boundary collapse finding—we test whether archive-based diversity prevents this). DAPO-Math-17k seeds.\n\n**Key Analyses:** (1) Coverage heatmaps showing cell occupancy evolution. (2) Per-cell benchmark contribution: which niches drive gains? (3) Emergent curriculum: bin-transition frequencies as policy improves. (4) Synthesis efficiency: per-topic survival rates vs. literature benchmarks (SPARQ, DART-Math, FLAMES), reported as community contribution. (5) Convergence speed: 10 vs. 3 bins. (6) Capability boundary: pass@1 vs. pass@k trajectories—does archive diversity prevent RL-PLUS-style collapse? (7) Structured vs. flat: archive coverage diversity over training vs. SAGE-style accumulation.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "6,700 H100-hours (baselines: 7×250h=1,750h; SACE-RLVR 7B 800h; SACE-RLVR 8B 800h; ablations 7×200h=1,400h; synthesis/verification 1,620h; archive overhead 330h)",
      "timeline": "14-18 weeks",
      "estimated_gpu_cost": "$16,750 (at ~$2.50/H100-hr)"
    },
    "human_in_loop": {
      "gpu_hours": "5,200 H100-hours (reuse released code; shared verification; API-based generation saves ~1,200 GPU-hrs but adds ~$13,500 API cost)",
      "timeline": "12-15 weeks",
      "claude_api_cost": "$400-800 (code assistance)",
      "synthesis_api_cost": "$8,000-13,500 (problem generation via API, optional vs. GPU)",
      "estimated_gpu_cost": "$13,000"
    },
    "auto_research": {
      "gpu_hours": "8,200 H100-hours (exploratory sweeps over archive dimensions, bin count, refresh frequency, replacement criteria, synthesis strategies)",
      "timeline": "10-13 weeks",
      "claude_api_cost": "$1,000-2,000",
      "estimated_gpu_cost": "$20,500",
      "speed_bottleneck": "GPU queue; each GRPO run 24-72h on 8×H100s. Synthesis for geometry extreme cells dominates generation cost."
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
    "CLPO (arXiv 2509.25004) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024",
    "Socratic-Zero (arXiv 2509.24726) — PRIMARY BASELINE, three-agent co-evolution; 56.1% avg",
    "SAGE (arXiv 2603.15255) — CONCURRENT, 4-agent self-evolution; over-specializes ~120 steps; AIME 2024 13.3%",
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
    "IndiMathBench (arXiv 2512.00997) — geometry formalization 6-7× harder than algebra",
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
  "description": "We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), scaling online MAP-Elites from GSM-level (DéjàQ) to competition-level math through three core innovations plus four extensions. Two independent motivations for comprehensive coverage: (1) relay-regime theory (arXiv 2602.14872) suggests smooth difficulty spectra yield faster convergence—adopted as design heuristic, not guarantee, with A3 testing empirically; (2) even under 'sparse policy selection' (1-3% tokens modified), broad coverage prevents 'capability boundary collapse' (RL-PLUS: pass@1↑ pass@128↓; +69.2% with diversity), ensures multiplicative primitive sharpening across domains (Sharper Primitives), and provides the behavioral diversity that is the binding constraint for RL (Tailor: 25 vs 4 primitives). Core 1: 2D archive (10 bins × 5 topics = 50 cells) with proactive gap identification and Bayesian replacement—addresses SAGE's over-specialization at step ~120. Core 2: generate-then-classify synthesis with literature-grounded per-niche survival estimates (central: 30-50%, geometry: 5-15%, extreme: 3-8%; geometry extremes ~1-3% per IndiMathBench; graceful degradation to min 3/cell; ~162 GPU-hrs/refresh). Core 3: zero-cost Bayesian estimation via G=16 rollout reuse (vs DéjàQ K=100), Beta posterior + credible intervals; G=16 justified by MC-GRPO ablation + gradient starvation analysis (69% degenerate groups at G=4). Extensions: SvS seeding, shrinkage, DGPO, ZPD—each ablated. Seven baselines (DéjàQ-comp, CLPO, Socratic-Zero, SAGE, EVOL-RL, MathForge, GRPO), seven ablations including pass@k capability boundary analysis. Qwen2.5-Math-7B/Qwen3-8B, AIME 2024/2025, MATH-500, AMC, Minerva, OlympiadBench.",
  "project_name": "sace_rlvr",
  "source": "web_research",
  "reviewer_response": {
    "revision_overview": "MAJOR REVISION addressing score stagnation (3.2→3.5 over 3 rounds) through structural simplification and substantive strengthening rather than incremental patching. Four structural changes: (1) radical simplification to 3 core + 4 extensions (from ~12 components), (2) honest theoretical scoping as 'design motivation' not 'backbone,' (3) all factual errors corrected via primary source verification, (4) substantially strengthened coverage motivation with independent empirical arguments from capability boundary collapse, multiplicative primitive compounding, and behavioral diversity literature. SAGE added. Per-niche estimates grounded in 5 synthesis papers. Seven focused ablations.",
    "issue_1_vcrl_factual_errors": "FIXED (CRITICAL). Verified by reading actual paper: (a) 44.17 does not exist in VCRL—closest is 44.73 (GRPO+VDS ablation, 4B); (b) 49.43 = VCRL on Qwen3-4B, 57.76 = VCRL on Qwen3-8B—MODEL SIZES not rollout counts; (c) VCRL performs NO G ablation; (d) uses 'reward variance' not 'advantage variance.' New G=16 justification: MC-GRPO ablation (G=2: 78.92%, G=4: 81.34%, G=8: 84.53%); Gradient Starvation (69% degenerate groups at G=4, mechanistic explanation via p^G+(1-p)^G); DAPO standard. VCRL cited only for reward variance as difficulty proxy.",
    "issue_2_theoretical_backbone_honestly_scoped": "RESTRUCTURED. Now explicitly: 'design motivation' not 'theoretical backbone.' 'Validated on synthetic tasks with idealized assumptions... principled design heuristic... A3 provides first empirical test... We do not claim theoretical guarantees transfer.' PAIRED with independent empirical motivation (Argument 2) that does not depend on theoretical transfer: capability boundary collapse, multiplicative compounding, behavioral diversity as binding constraint. This dual-motivation structure is MORE compelling than the original single-theory framing.",
    "issue_3_sage_added": "ADDED with detailed analysis. 4-agent framework, 500-example seed, Qwen-2.5-7B. Key finding: over-specialization after ~120 steps (69.5%→61.6%) due to flat unstructured pool growing 18×. Added as baseline #4. New analysis #7 compares structured archive vs. flat accumulation.",
    "issue_4_minor_factual_errors": "FIXED. EVOL-RL: 16.4% (abstract; noted internal paper inconsistency with Table 1's 17.1%). SAND-Math: '~38% end-to-end (8,842/23,437)' with stage breakdown (~75%/~57%/~96%); paper's '41.9% yield' is generation-stage metric.",
    "issue_5_sparse_policy_selection": "ADDRESSED SUBSTANTIVELY with three independently sourced empirical arguments, elevated to co-equal Argument 2: (a) Sharper Primitives: RLVR polarizes, multiplicative compounding P(q) ∝ ∏P(sⱼ) means un-sharpened primitives create exponential bottleneck; (b) Tailor: 25 vs 4 primitives → substantial gains, 'behavioral diversity is binding constraint'; (c) RL-PLUS: 'capability boundary collapse'—pass@1↑ pass@128↓, +69.2% with diversity. Key insight: sparse selection makes coverage MORE important, not less—determines WHICH capabilities get activated from base model's latent repertoire. Added pass@k evaluation (analysis #6) to test whether archive diversity prevents collapse.",
    "issue_6_per_niche_survival_estimates": "ADDED with literature-grounded estimates from 5 papers. SPARQ: 25% QD survival. DART-Math: Level 5 loses 51.1% coverage. FLAMES: Level 5 removes 50%. IndiMathBench: geometry 6-7× harder. Estimates: central 30-50%, medium-hard 15-25%, geometry 5-15%, extreme 3-8%, geometry extreme 1-3%. Overgeneration: 20-330×/cell depending on niche. Cost: ~162 GPU-hrs/refresh (generation ~150h + verification ~12h) × 10 refreshes = ~1,620 GPU-hrs. Alternative API: ~$13,500. Graceful degradation: min 3/cell. Per-niche survival reported as community contribution.",
    "issue_7_system_complexity_reduced": "MAJOR RESTRUCTURING. 3 core + 4 extensions (from ~12 components). Core 1: 2D Learnability Archive. Core 2: Proactive Gap-Targeted Synthesis. Core 3: Zero-Cost Bayesian Estimation. Extensions: E1 SvS seeding, E2 James-Stein shrinkage (not claimed novel, cites arXiv 2511.03710), E3 DGPO (adopted from MathForge), E4 ZPD sampling. Ablations 10→7, baselines 10→7. Follows DéjàQ pattern (~11 mechanisms, ~2 claims). Cleaner narrative: 'persistent Bayesian QD archive with proactive synthesis for competition-level RLVR.'"
  }
}

## Reviewer feedback (round 8)
Issues: ["CRITICAL PERSISTENT (Round 1→8, 7 rounds unaddressed): SEC (arXiv 2505.14970) formulates curriculum as MAB over problem categories (difficulty × type) during RL, achieving 17.5% AIME24 on Qwen2.5-7B (+27% relative). This directly parallels SACE-RLVR's per-niche archive management. Actor-Curator (arXiv 2602.20532) explicitly beats SEC with a neural curator achieving 30.0% AIME24 (+28.6% relative) and ~9% overhead via policy-improvement bandits with regret guarantees. Both select from existing pools rather than synthesizing—the proposal MUST argue why persistent archives with synthesis outperform principled bandit selection. This is the #1 reviewer objection waiting to happen.", "CRITICAL PERSISTENT (Round 6→8, 2 rounds unaddressed): Online Difficulty Filtering (arXiv 2504.03380) proves balanced difficulty filtering maximizes a lower bound on expected policy improvement. +12% gains in half the training steps. This theoretical result SUPPORTS the proposal's difficulty-aware motivation and should be cited as evidence, yet remains omitted.", "PERSISTENT FACTUAL ERROR (Round 6→8): IndiMathBench geometry ratio still claimed as '6-7× harder' throughout (per-niche estimates, landscape section). Actual: 12/98=12.2% geometry BEq vs 96/214=44.9% non-geometry = ~3.7× ratio. Additionally, the paper attributes geometry difficulty partly to 'Mathlib's lacking support for Olympiad-style geometry' (formalization-specific), which may not transfer to problem synthesis difficulty.", "PERSISTENT MISLEADING PRESENTATION (Round 6→8): SAGE AIME 2024 presented as '13.3%' without noting this equals the Qwen-2.5-7B base model (also 13.3%). SAGE shows ZERO AIME improvement and actually DEGRADES AMC 2023 (57.5%→52.5%). This is STRONGER evidence for over-specialization than presented—SAGE improves narrow benchmarks (OlympiadBench +10.7%) while failing or degrading competition-level OOD tasks.", "NEW CONCURRENT WORK: UCPO (arXiv 2605.00365, May 2026) addresses the same pass@k diversity collapse via Uniform-Correct Policy Optimization, achieving +10% absolute AIME24 at Pass@64 and +45% equation-level diversity. This is a simpler, policy-level alternative to archive-based diversity maintenance that directly competes with the pass@k capability boundary analysis (Analysis #6).", "NEW CONCURRENT WORK: Vocabulary Dropout (arXiv 2604.03472, Apr 2026) achieves +4.4 average points at 8B on competition benchmarks via lightweight logit masking—a minimal alternative to archive-based diversity. Flagged in Round 7 as recommended, still unaddressed.", "MISSING RECOMMENDED WORK: SOAR (arXiv 2601.18778) meta-RL teacher for learnability-targeted synthesis at the 'edge of learnability'—conceptually parallel to SACE-RLVR's proactive gap identification. Recommended in Round 7, still unaddressed."]
Feedback: This is Round 8 of 10. The proposal has matured into a thorough, honestly-framed integration paper with a clean 3+4 structure, but **the persistent failure to address SEC and Actor-Curator after 7 rounds is now the single blocking issue**. These are not obscure works—they are the most direct competitors in the adaptive curriculum during RL space, and any RLVR reviewer will immediately identify them.

**BLOCKING (must fix in Round 9 to have any chance of passing in Round 10):**

(1) **Add SEC and Actor-Curator as related work AND add Actor-Curator as an 8th baseline.** SEC does MAB over problem categories (17.5% AIME24, +27% relative on Qwen2.5-7B). Actor-Curator does neural bandit selection with regret guarantees (30.0% AIME24, +28.6% relative, ~9% overhead) and explicitly beats SEC. The key differentiations:
- SEC/Actor-Curator select from FIXED pools; SACE-RLVR SYNTHESIZES for identified gaps
- Bandit methods are effectively stateless per-step; archive management provides persistent cross-step memory with coverage tracking
- Archives enable interpretable coverage maps, proactive gap identification, and post-hoc niche contribution analysis
- The approaches are potentially COMPLEMENTARY: Actor-Curator could serve as the sampling strategy FROM the archive

(2) **Fix IndiMathBench ratio.** Change '6-7× harder' to '~3.7× lower success rate (12.2% vs 44.9% BEq)' and note the formalization-specific context. Adjust per-niche survival estimates downward accordingly for geometry cells.

(3) **Correct SAGE AIME presentation.** State explicitly: 'SAGE achieves 13.3% AIME 2024, matching the Qwen-2.5-7B base model (also 13.3%), and degrades AMC 2023 from 57.5% to 52.5%—demonstrating that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance.'

**STRONGLY RECOMMENDED (would improve scores):**

(4) **Cite Online Difficulty Filtering** (arXiv 2504.03380). Its theoretical result (balanced filtering maximizes policy improvement lower bound) SUPPORTS your difficulty-aware motivation. One sentence in the 'Difficulty-aware' section.

(5) **Add UCPO as concurrent related work.** It addresses pass@k diversity collapse via policy optimization rather than archive-based diversity. Brief mention with differentiation: UCPO modifies the optimization objective; SACE-RLVR modifies the training distribution. Potentially complementary.

(6) **Add Vocabulary Dropout and SOAR** as brief concurrent work mentions.

**WARNING:** Round 10 requires a final pass/fail decision. At current scores (avg 3.375), the proposal will fail unless SEC/Actor-Curator engagement substantially strengthens the novelty argument and demonstrates why archive-based approaches offer capabilities that bandit-based selection cannot.

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
经过 8 轮修订，近 3 轮平均分从 3.6 到 3.4，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "f3537751-8b53-4eea-b0c9-b727be7882af",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T03:05:53.740Z_

```json
{
  "parentUuid": "f3537751-8b53-4eea-b0c9-b727be7882af",
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
  "uuid": "c0d8dc21-cb44-4692-a735-ed9fc4d780ac",
  "timestamp": "2026-05-28T03:05:53.740Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T03:05:53.740Z_

```json
{
  "parentUuid": "c0d8dc21-cb44-4692-a735-ed9fc4d780ac",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "588ce816-7bf6-40ca-ab05-3e8b44bfa3c1",
  "timestamp": "2026-05-28T03:05:53.740Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
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
  "leafUuid": "588ce816-7bf6-40ca-ab05-3e8b44bfa3c1",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Assistant

_source line 8 · 2026-05-28T03:06:00.179Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully. This is Round 8 of 10, and the proposal is at risk of failing. The key issues are:

1. **CRITICAL PERSISTENT (7 rounds!)**: SEC and Actor-Curator - bandit-based curriculum selection during RL. This is the #1 blocking issue.
2. **CRITICAL PERSISTENT (2 rounds)**: Online Difficulty Filtering - theoretical support for difficulty-aware training.
3. **PERSISTENT FACTUAL ERROR**: IndiMathBench geometry ratio (6-7× → ~3.7×)


4. **PERSISTENT MISLEADING**: SAGE AIME presentation
5. **NEW**: UCPO - pass@k diversity via policy optimization
6. **NEW**: Vocabulary Dropout - lightweight diversity alternative
7. **MISSING**: SOAR - meta-RL teacher for learnability

I need to dig into the literature on each of these to understand what's actually being claimed versus what the papers actually show.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "588ce816-7bf6-40ca-ab05-3e8b44bfa3c1",
  "isSidechain": false,
  "requestId": "req_011CbUE8x2VGeqqbuGinzXa1",
  "type": "assistant",
  "uuid": "a379043a-2759-4800-8850-01bd82f7bcd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6ZabMbMqcgK7ajLTUEhQW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14419,
      "cache_read_input_tokens": 11014,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 335,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14419
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

_source line 9 · 2026-05-28T03:06:00.358Z_

I need to deeply research each of the papers flagged by the reviewer before making revisions. Let me start with the most critical ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a379043a-2759-4800-8850-01bd82f7bcd0",
  "isSidechain": false,
  "requestId": "req_011CbUE8x2VGeqqbuGinzXa1",
  "type": "assistant",
  "uuid": "2b0461be-d0fa-4edf-9d64-d44b7d95e10f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6ZabMbMqcgK7ajLTUEhQW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14419,
      "cache_read_input_tokens": 11014,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 335,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14419
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

_source line 10 · 2026-05-28T03:06:00.504Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011ai3vfMLjWtAtsCem3qPpa`</summary>

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
  "parentUuid": "2b0461be-d0fa-4edf-9d64-d44b7d95e10f",
  "isSidechain": false,
  "requestId": "req_011CbUE8x2VGeqqbuGinzXa1",
  "type": "assistant",
  "uuid": "69245c40-1c09-44ec-89be-43802319d1c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6ZabMbMqcgK7ajLTUEhQW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14419,
      "cache_read_input_tokens": 11014,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 335,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14419
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

_source line 11 · 2026-05-28T03:06:00.512Z_

<details><summary>↩ Tool result · `toolu_011ai3vfMLjWtAtsCem3qPpa`</summary>

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
  "parentUuid": "69245c40-1c09-44ec-89be-43802319d1c2",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "f24c5319-70ac-4501-9635-274c72229c68",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "69245c40-1c09-44ec-89be-43802319d1c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T03:06:06.712Z_

<details><summary>Logged reasoning block</summary>

```text
Let me research the critical papers in parallel. I need to look at:

1. SEC (arXiv 2505.14970) - MAB over problem categories
2. Actor-Curator (arXiv 2602.20532) - Neural curator beating SEC
3. Online Difficulty Filtering (arXiv 2504.03380) - Theoretical result on balanced filtering
4. UCPO (arXiv 2605.00365) - Uniform-Correct Policy Optimization


5. Vocabulary Dropout (arXiv 2604.03472) - Logit masking for diversity
6. SOAR (arXiv 2601.18778) - Meta-RL teacher for learnability
7. IndiMathBench (arXiv 2512.00997) - Need to verify the actual geometry ratio

I'll fetch these papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f24c5319-70ac-4501-9635-274c72229c68",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "b4d60c1d-58d9-450c-aff7-64b829d8e3a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 13 · 2026-05-28T03:06:06.713Z_

Let me research all the critical papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4d60c1d-58d9-450c-aff7-64b829d8e3a3",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "3fbb1550-0e9e-4057-a499-567faaf7e83f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 14 · 2026-05-28T03:06:08.240Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XTtc8Y6YJQDAWAgpBv21KV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.14970",
  "prompt": "Extract the full abstract, method details, key results (especially AIME 2024 scores), base model used, how the multi-armed bandit (MAB) curriculum works over problem categories (difficulty × type), what pool they select from, and any limitations mentioned. Include all numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fbb1550-0e9e-4057-a499-567faaf7e83f",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "fd700afa-e9be-4857-9182-62dab017aa98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 15 · 2026-05-28T03:06:09.657Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018HuS6XaB1teBAKMNtgLmyt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.20532",
  "prompt": "Extract the full abstract, method details, key results (especially AIME 2024 scores, overhead percentage), base model used, how the neural curator/policy-improvement bandit works, how it compares to SEC, what regret guarantees it provides, and what pool it selects from. Include all numerical results and comparisons."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd700afa-e9be-4857-9182-62dab017aa98",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "41179738-1456-4e3b-89a5-a18dbd3eba24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 16 · 2026-05-28T03:06:11.075Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HQqUGtvxERuy7TTQTSxbas`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.03380",
  "prompt": "Extract the full abstract, the theoretical result about balanced difficulty filtering maximizing policy improvement lower bound, key results (+12% gains, half training steps claim), method details, and how difficulty filtering is formalized. Include all key theorems and numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41179738-1456-4e3b-89a5-a18dbd3eba24",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "b5a87c8d-5f81-4f68-a53d-2a30b2491c22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 17 · 2026-05-28T03:06:12.978Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013RAg5BQmjgUTiUraojkQmR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.00365",
  "prompt": "Extract the full abstract, method details of Uniform-Correct Policy Optimization (UCPO), key results on pass@k diversity (especially +10% AIME24 at Pass@64, +45% equation-level diversity claim), base model, and how it addresses diversity collapse at the policy optimization level rather than data level. Include all numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5a87c8d-5f81-4f68-a53d-2a30b2491c22",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "1581c07d-73c0-43f7-b71d-38209f1bff99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 18 · 2026-05-28T03:06:13.367Z_

<details><summary>↩ Tool result · `toolu_01XTtc8Y6YJQDAWAgpBv21KV`</summary>

```text
# Self-Evolving Curriculum for LLM Reasoning - Key Details

## Abstract
The paper proposes **Self-Evolving Curriculum (SEC)**, describing it as "an automatic curriculum learning method that learns a curriculum policy concurrently with the RL fine-tuning process."

## Method Overview
SEC formulates curriculum selection as a non-stationary Multi-Armed Bandit problem, where "each problem category (e.g., difficulty level or problem type) as an individual arm." The approach leverages absolute advantage from policy gradient methods as a proxy for learning gain and updates the curriculum policy using the TD(0) method at each training step.

## Key Results
The abstract indicates SEC "significantly improves models' reasoning capabilities, enabling better generalization to harder, out-of-distribution test problems" across three domains: planning, inductive reasoning, and mathematics. The paper also notes "better skill balance when fine-tuning simultaneously on multiple reasoning domains."

## Important Limitations
**The provided web content does not include:**
- Specific AIME 2024 scores or numerical results
- Base model specifications
- Details on problem pool composition
- Explicit limitations section

The page shown is the arXiv abstract/metadata page only, lacking the full paper content where detailed experimental results, model information, and limitations would appear.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd700afa-e9be-4857-9182-62dab017aa98",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "95ca052e-6a1f-4e50-83bc-77fa4306e600",
  "toolUseResult": {
    "bytes": 48086,
    "code": 200,
    "codeText": "OK",
    "result": "# Self-Evolving Curriculum for LLM Reasoning - Key Details\n\n## Abstract\nThe paper proposes **Self-Evolving Curriculum (SEC)**, describing it as \"an automatic curriculum learning method that learns a curriculum policy concurrently with the RL fine-tuning process.\"\n\n## Method Overview\nSEC formulates curriculum selection as a non-stationary Multi-Armed Bandit problem, where \"each problem category (e.g., difficulty level or problem type) as an individual arm.\" The approach leverages absolute advantage from policy gradient methods as a proxy for learning gain and updates the curriculum policy using the TD(0) method at each training step.\n\n## Key Results\nThe abstract indicates SEC \"significantly improves models' reasoning capabilities, enabling better generalization to harder, out-of-distribution test problems\" across three domains: planning, inductive reasoning, and mathematics. The paper also notes \"better skill balance when fine-tuning simultaneously on multiple reasoning domains.\"\n\n## Important Limitations\n**The provided web content does not include:**\n- Specific AIME 2024 scores or numerical results\n- Base model specifications\n- Details on problem pool composition\n- Explicit limitations section\n\nThe page shown is the arXiv abstract/metadata page only, lacking the full paper content where detailed experimental results, model information, and limitations would appear.",
    "durationMs": 5122,
    "url": "https://arxiv.org/abs/2505.14970"
  },
  "sourceToolAssistantUUID": "fd700afa-e9be-4857-9182-62dab017aa98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T03:06:13.953Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JyPaNU5g6UG3TL5XTueZUg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03472",
  "prompt": "Extract the full abstract, method details of Vocabulary Dropout, key results (+4.4 average points claim), how it achieves diversity through logit masking, base model size, and competition benchmark results. Include all numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95ca052e-6a1f-4e50-83bc-77fa4306e600",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "3fa2696b-396e-48d2-82bf-b978ab1131ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 20 · 2026-05-28T03:06:15.369Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TeXCXwcboMVPdnJq23vbXM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.18778",
  "prompt": "Extract the full abstract, method details of SOAR, how the meta-RL teacher targets the 'edge of learnability', key results, base model, and how it relates to curriculum learning during RL training. Include all numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fa2696b-396e-48d2-82bf-b978ab1131ce",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "36521018-e3e9-4ecd-8ab4-565ea574d0cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 21 · 2026-05-28T03:06:16.301Z_

<details><summary>↩ Tool result · `toolu_01HQqUGtvxERuy7TTQTSxbas`</summary>

```text
# Online Difficulty Filtering for Reasoning Oriented RL - Key Findings

## Abstract
The paper addresses reward sparsity in reinforcement learning with verifiable rewards (RLVR) by presenting "a formal analysis of online difficulty-aware filtering and establish its theoretical foundations." The work demonstrates that intermediate-difficulty task selection maximizes learning efficiency.

## Core Theoretical Result
The central theoretical contribution establishes that "expected policy improvement is lower-bounded by the variance of task-level success probabilities," with the key insight that "balanced filtering maximizes this lower bound."

## Empirical Performance
The method achieves "up to +12% gains in less than half the training steps of standard GRPO" on math reasoning benchmarks, demonstrating superior convergence speed and final performance compared to baseline approaches.

## Method Formalization
The paper formalizes difficulty filtering through an analysis of task-level success probability variance. Balanced filtering is presented as the optimal curriculum strategy that maximizes the derived lower bound on policy improvement, grounding the approach in theoretical guarantees.

## Scope & Validation
The theoretical analysis extends "to various reward distributions," providing a principled foundation for future RLVR curriculum strategies. Results are validated across multiple math reasoning benchmarks with both theoretical analysis and empirical evidence.

**Venue:** EACL 2026 (accepted for main conference)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5a87c8d-5f81-4f68-a53d-2a30b2491c22",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "62be838a-fa5c-459d-ae95-f685ac9ff9bb",
  "toolUseResult": {
    "bytes": 46786,
    "code": 200,
    "codeText": "OK",
    "result": "# Online Difficulty Filtering for Reasoning Oriented RL - Key Findings\n\n## Abstract\nThe paper addresses reward sparsity in reinforcement learning with verifiable rewards (RLVR) by presenting \"a formal analysis of online difficulty-aware filtering and establish its theoretical foundations.\" The work demonstrates that intermediate-difficulty task selection maximizes learning efficiency.\n\n## Core Theoretical Result\nThe central theoretical contribution establishes that \"expected policy improvement is lower-bounded by the variance of task-level success probabilities,\" with the key insight that \"balanced filtering maximizes this lower bound.\"\n\n## Empirical Performance\nThe method achieves \"up to +12% gains in less than half the training steps of standard GRPO\" on math reasoning benchmarks, demonstrating superior convergence speed and final performance compared to baseline approaches.\n\n## Method Formalization\nThe paper formalizes difficulty filtering through an analysis of task-level success probability variance. Balanced filtering is presented as the optimal curriculum strategy that maximizes the derived lower bound on policy improvement, grounding the approach in theoretical guarantees.\n\n## Scope & Validation\nThe theoretical analysis extends \"to various reward distributions,\" providing a principled foundation for future RLVR curriculum strategies. Results are validated across multiple math reasoning benchmarks with both theoretical analysis and empirical evidence.\n\n**Venue:** EACL 2026 (accepted for main conference)",
    "durationMs": 5224,
    "url": "https://arxiv.org/abs/2504.03380"
  },
  "sourceToolAssistantUUID": "b5a87c8d-5f81-4f68-a53d-2a30b2491c22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T03:06:17.756Z_

<details><summary>↩ Tool result · `toolu_018HuS6XaB1teBAKMNtgLmyt`</summary>

```text
# Actor-Curator: Key Research Details

## Abstract
The paper presents a "scalable and fully automated curriculum learning framework" that learns a neural curator to dynamically select training problems from large problem banks by optimizing for expected policy performance improvement.

## Core Method
The approach formulates problem selection as a "non-stationary stochastic bandit problem" and derives a principled loss function using online stochastic mirror descent, establishing regret guarantees under partial feedback conditions.

## Key Results
- **AIME 2024**: 28.6% relative improvement over the strongest baseline
- **ARC-1D**: 30.5% relative improvement over strongest baseline
- **Training speedup**: Up to 80% faster than comparison methods
- Consistently outperforms uniform sampling and curriculum baselines across reasoning benchmarks
- Demonstrates improved training stability and efficiency

## Technical Components
The neural curator operates within a policy-improvement bandit framework that adaptively selects problems to maximize gains in agent performance. The method selects from "large problem banks" without explicit specification of pool composition in the provided abstract.

## Not Specified in This Content
The page content does not include:
- The specific base model used for LLM post-training
- Detailed comparison methodology with SEC (Self-Evolving Curriculum)
- Mathematical formulation of regret guarantees
- Exact pool composition details

The paper was submitted February 24, 2026 and is currently under review (37 pages, with equal first-author contribution).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41179738-1456-4e3b-89a5-a18dbd3eba24",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "c3d2b2b1-ee1c-417d-82f4-06b9e00b9ef9",
  "toolUseResult": {
    "bytes": 48888,
    "code": 200,
    "codeText": "OK",
    "result": "# Actor-Curator: Key Research Details\n\n## Abstract\nThe paper presents a \"scalable and fully automated curriculum learning framework\" that learns a neural curator to dynamically select training problems from large problem banks by optimizing for expected policy performance improvement.\n\n## Core Method\nThe approach formulates problem selection as a \"non-stationary stochastic bandit problem\" and derives a principled loss function using online stochastic mirror descent, establishing regret guarantees under partial feedback conditions.\n\n## Key Results\n- **AIME 2024**: 28.6% relative improvement over the strongest baseline\n- **ARC-1D**: 30.5% relative improvement over strongest baseline\n- **Training speedup**: Up to 80% faster than comparison methods\n- Consistently outperforms uniform sampling and curriculum baselines across reasoning benchmarks\n- Demonstrates improved training stability and efficiency\n\n## Technical Components\nThe neural curator operates within a policy-improvement bandit framework that adaptively selects problems to maximize gains in agent performance. The method selects from \"large problem banks\" without explicit specification of pool composition in the provided abstract.\n\n## Not Specified in This Content\nThe page content does not include:\n- The specific base model used for LLM post-training\n- Detailed comparison methodology with SEC (Self-Evolving Curriculum)\n- Mathematical formulation of regret guarantees\n- Exact pool composition details\n\nThe paper was submitted February 24, 2026 and is currently under review (37 pages, with equal first-author contribution).",
    "durationMs": 8097,
    "url": "https://arxiv.org/abs/2602.20532"
  },
  "sourceToolAssistantUUID": "41179738-1456-4e3b-89a5-a18dbd3eba24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T03:06:17.905Z_

<details><summary>↩ Tool result · `toolu_013RAg5BQmjgUTiUraojkQmR`</summary>

```text
# Uniform-Correct Policy Optimization (UCPO) Summary

## Full Abstract
"Reinforcement Learning with Verifiable Rewards (RLVR) has achieved substantial gains in single-attempt accuracy (Pass@1) on reasoning tasks, yet often suffers from reduced multi-sample coverage (Pass@K), indicating diversity collapse."

The research identifies that standard RLVR objectives like GRPO concentrate probability mass on narrow subsets of correct outputs while suppressing alternative valid solutions.

## Core Method
UCPO modifies GRPO by introducing a conditional uniformity penalty targeting the policy's distribution across correct solutions. This penalty mechanism reallocates gradient signals toward underrepresented valid responses, promoting more balanced probability allocation within the correct solution set.

## Key Numerical Results
- **Pass@K improvements:** Up to +10% absolute improvement on AIME24 benchmark at Pass@64
- **Diversity enhancement:** Up to 45% higher equation-level diversity within the correct solution set
- **Competitive Pass@1:** Method maintains strong single-sample accuracy while improving multi-sample performance

## Model Scale
The approach was evaluated across three language models ranging from 1.5B to 7B parameters.

## Problem Addressed
Rather than tackling diversity at the training data level, UCPO addresses diversity collapse at the policy optimization stage by making the learning objective explicitly sensitive to how probability mass distributes among mathematically valid solutions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1581c07d-73c0-43f7-b71d-38209f1bff99",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "42631fd6-d67e-44c2-b612-cae2148a6ce3",
  "toolUseResult": {
    "bytes": 48293,
    "code": 200,
    "codeText": "OK",
    "result": "# Uniform-Correct Policy Optimization (UCPO) Summary\n\n## Full Abstract\n\"Reinforcement Learning with Verifiable Rewards (RLVR) has achieved substantial gains in single-attempt accuracy (Pass@1) on reasoning tasks, yet often suffers from reduced multi-sample coverage (Pass@K), indicating diversity collapse.\"\n\nThe research identifies that standard RLVR objectives like GRPO concentrate probability mass on narrow subsets of correct outputs while suppressing alternative valid solutions.\n\n## Core Method\nUCPO modifies GRPO by introducing a conditional uniformity penalty targeting the policy's distribution across correct solutions. This penalty mechanism reallocates gradient signals toward underrepresented valid responses, promoting more balanced probability allocation within the correct solution set.\n\n## Key Numerical Results\n- **Pass@K improvements:** Up to +10% absolute improvement on AIME24 benchmark at Pass@64\n- **Diversity enhancement:** Up to 45% higher equation-level diversity within the correct solution set\n- **Competitive Pass@1:** Method maintains strong single-sample accuracy while improving multi-sample performance\n\n## Model Scale\nThe approach was evaluated across three language models ranging from 1.5B to 7B parameters.\n\n## Problem Addressed\nRather than tackling diversity at the training data level, UCPO addresses diversity collapse at the policy optimization stage by making the learning objective explicitly sensitive to how probability mass distributes among mathematically valid solutions.",
    "durationMs": 4923,
    "url": "https://arxiv.org/abs/2605.00365"
  },
  "sourceToolAssistantUUID": "1581c07d-73c0-43f7-b71d-38209f1bff99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-28T03:06:18.439Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QhknHDLN1cRnbgkvwg69om`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.00997",
  "prompt": "Extract the actual geometry success rates and non-geometry success rates. Specifically looking for the ratio claimed as '6-7× harder' - find the actual numbers. Look for BEq scores: geometry 12/98=12.2% vs non-geometry rates. Also note whether the difficulty is attributed to Mathlib formalization support rather than intrinsic mathematical difficulty. Include all per-topic success rates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42631fd6-d67e-44c2-b612-cae2148a6ce3",
  "isSidechain": false,
  "requestId": "req_011CbUE9TDukZiQFKBuaeiVZ",
  "type": "assistant",
  "uuid": "0dbd7c14-504f-4149-ba4e-76c2dd700391",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8gVWdZqH4i4oqY1ke2sRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 25433,
      "output_tokens": 1141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1354,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1141,
          "cache_read_input_tokens": 25433,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1354
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "0dbd7c14-504f-4149-ba4e-76c2dd700391",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Tool result

_source line 27 · 2026-05-28T03:06:21.685Z_

<details><summary>↩ Tool result · `toolu_01QhknHDLN1cRnbgkvwg69om`</summary>

```text
I cannot extract the specific success rates, BEq scores, or the "6-7× harder" ratio you're requesting because **this arXiv abstract page does not contain those detailed numerical results**.

The page shows only:
- The paper title and metadata
- An abstract stating that "autoformalization remains challenging" and "theorem proving success rates remain low"
- Information about the 312 formal Lean 4 theorems in IndiMathBench sourced from Indian Mathematics Olympiads

The abstract notes a "substantial gap between syntactic validity and semantic correctness" but provides no specific per-topic success rates, geometry vs. non-geometry comparisons, or BEq score breakdowns.

To find the actual numerical results you're seeking, you would need to access the full PDF or HTML version of the paper using the provided links.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dbd7c14-504f-4149-ba4e-76c2dd700391",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "7582cb75-15b3-4aed-b528-ba21ca09c8c6",
  "toolUseResult": {
    "bytes": 46767,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot extract the specific success rates, BEq scores, or the \"6-7× harder\" ratio you're requesting because **this arXiv abstract page does not contain those detailed numerical results**.\n\nThe page shows only:\n- The paper title and metadata\n- An abstract stating that \"autoformalization remains challenging\" and \"theorem proving success rates remain low\"\n- Information about the 312 formal Lean 4 theorems in IndiMathBench sourced from Indian Mathematics Olympiads\n\nThe abstract notes a \"substantial gap between syntactic validity and semantic correctness\" but provides no specific per-topic success rates, geometry vs. non-geometry comparisons, or BEq score breakdowns.\n\nTo find the actual numerical results you're seeking, you would need to access the full PDF or HTML version of the paper using the provided links.",
    "durationMs": 3244,
    "url": "https://arxiv.org/abs/2512.00997"
  },
  "sourceToolAssistantUUID": "0dbd7c14-504f-4149-ba4e-76c2dd700391",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T03:06:21.774Z_

<details><summary>↩ Tool result · `toolu_01JyPaNU5g6UG3TL5XTueZUg`</summary>

```text
# Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution

## Abstract
"Co-evolutionary self-play, where one language model generates problems and another solves them, promises autonomous curriculum learning without human supervision." The research addresses diversity collapse in this framework, where proposers converge to narrow problem distributions.

## Method: Vocabulary Dropout
The technique applies "a random mask...to the proposer's output logits during both policy training and curriculum generation." The mask is described as "hard and non-stationary, preventing the proposer from locking into fixed token sequences." This constrains the action space to sustain productive co-evolution.

## Key Results
- **Solver improvements**: Averaging +4.4 points at the 8B model scale
- **Largest gains**: Observed on competition-level benchmarks
- **Diversity sustained**: Across lexical, semantic, and functional metrics throughout training

## Models & Benchmarks
The research tested on:
- **Base models**: Qwen3-4B and Qwen3-8B
- **Framework**: R-Zero for mathematical reasoning
- **Evaluation**: Competition-level benchmark performance showed the most substantial improvements

## Mechanism
Vocabulary dropout maintains proposer diversity by applying hard, changing masks that prevent token sequence fixation, analogous to game rules in classical self-play.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fa2696b-396e-48d2-82bf-b978ab1131ce",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "915e3ecb-8468-4251-840f-725b87433c31",
  "toolUseResult": {
    "bytes": 46365,
    "code": 200,
    "codeText": "OK",
    "result": "# Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution\n\n## Abstract\n\"Co-evolutionary self-play, where one language model generates problems and another solves them, promises autonomous curriculum learning without human supervision.\" The research addresses diversity collapse in this framework, where proposers converge to narrow problem distributions.\n\n## Method: Vocabulary Dropout\nThe technique applies \"a random mask...to the proposer's output logits during both policy training and curriculum generation.\" The mask is described as \"hard and non-stationary, preventing the proposer from locking into fixed token sequences.\" This constrains the action space to sustain productive co-evolution.\n\n## Key Results\n- **Solver improvements**: Averaging +4.4 points at the 8B model scale\n- **Largest gains**: Observed on competition-level benchmarks\n- **Diversity sustained**: Across lexical, semantic, and functional metrics throughout training\n\n## Models & Benchmarks\nThe research tested on:\n- **Base models**: Qwen3-4B and Qwen3-8B\n- **Framework**: R-Zero for mathematical reasoning\n- **Evaluation**: Competition-level benchmark performance showed the most substantial improvements\n\n## Mechanism\nVocabulary dropout maintains proposer diversity by applying hard, changing masks that prevent token sequence fixation, analogous to game rules in classical self-play.",
    "durationMs": 7797,
    "url": "https://arxiv.org/abs/2604.03472"
  },
  "sourceToolAssistantUUID": "3fa2696b-396e-48d2-82bf-b978ab1131ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-28T03:06:23.010Z_

<details><summary>↩ Tool result · `toolu_01TeXCXwcboMVPdnJq23vbXM`</summary>

```text
# Research Summary: Teaching Models to Teach Themselves (SOAR)

## Full Abstract
"Can a model learn to escape its own learning plateau? Reinforcement learning methods for finetuning large reasoning models stall on datasets with low initial success rates, and thus little training signal. We investigate a fundamental question: Can a pretrained LLM leverage latent knowledge to generate an automated curriculum for problems it cannot solve? To explore this, we design SOAR: A self-improvement framework designed to surface these pedagogical signals through meta-RL. A teacher copy of the model proposes synthetic problems for a student copy, and is rewarded with its improvement on a small subset of hard problems. Critically, SOAR grounds the curriculum in measured student progress rather than intrinsic proxy rewards."

## SOAR Method Overview
The framework employs a bi-level meta-reinforcement learning architecture with two model copies:
- **Teacher component**: Generates synthetic problems/stepping stones
- **Student component**: Attempts to solve generated problems
- **Reward signal**: Teacher receives rewards based on measured student improvement on genuinely difficult problems, not intrinsic proxy metrics

## Edge of Learnability Targeting
SOAR addresses problems at "the hardest subsets of mathematical benchmarks (0/128 success)" - essentially tasks where initial success rates are zero, representing the boundary of what models can currently solve.

## Key Findings
1. Bi-level meta-RL successfully unlocks learning under sparse binary rewards by leveraging latent problem-generation capacity
2. Grounded rewards outperform intrinsic reward schemes, avoiding instability and diversity collapse
3. "Structural quality and well-posedness are more critical for learning progress than solution correctness"

## Base Model
The research focuses on pretrained large language models, though specific model architecture isn't identified in the abstract.

## Curriculum Learning Connection
SOAR generates an automated curriculum by having the teacher model create intermediate problems that scaffold student learning—contrasting with traditional curriculum learning by grounding progression in actual student achievement rather than predetermined difficulty metrics.

**Numerical results**: Tested on problems with 0% initial success rates across 128-problem subsets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36521018-e3e9-4ecd-8ab4-565ea574d0cc",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "ba3f6c68-3968-4d11-83c1-7149c8e1d484",
  "toolUseResult": {
    "bytes": 48995,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Summary: Teaching Models to Teach Themselves (SOAR)\n\n## Full Abstract\n\"Can a model learn to escape its own learning plateau? Reinforcement learning methods for finetuning large reasoning models stall on datasets with low initial success rates, and thus little training signal. We investigate a fundamental question: Can a pretrained LLM leverage latent knowledge to generate an automated curriculum for problems it cannot solve? To explore this, we design SOAR: A self-improvement framework designed to surface these pedagogical signals through meta-RL. A teacher copy of the model proposes synthetic problems for a student copy, and is rewarded with its improvement on a small subset of hard problems. Critically, SOAR grounds the curriculum in measured student progress rather than intrinsic proxy rewards.\"\n\n## SOAR Method Overview\nThe framework employs a bi-level meta-reinforcement learning architecture with two model copies:\n- **Teacher component**: Generates synthetic problems/stepping stones\n- **Student component**: Attempts to solve generated problems\n- **Reward signal**: Teacher receives rewards based on measured student improvement on genuinely difficult problems, not intrinsic proxy metrics\n\n## Edge of Learnability Targeting\nSOAR addresses problems at \"the hardest subsets of mathematical benchmarks (0/128 success)\" - essentially tasks where initial success rates are zero, representing the boundary of what models can currently solve.\n\n## Key Findings\n1. Bi-level meta-RL successfully unlocks learning under sparse binary rewards by leveraging latent problem-generation capacity\n2. Grounded rewards outperform intrinsic reward schemes, avoiding instability and diversity collapse\n3. \"Structural quality and well-posedness are more critical for learning progress than solution correctness\"\n\n## Base Model\nThe research focuses on pretrained large language models, though specific model architecture isn't identified in the abstract.\n\n## Curriculum Learning Connection\nSOAR generates an automated curriculum by having the teacher model create intermediate problems that scaffold student learning—contrasting with traditional curriculum learning by grounding progression in actual student achievement rather than predetermined difficulty metrics.\n\n**Numerical results**: Tested on problems with 0% initial success rates across 128-problem subsets.",
    "durationMs": 7638,
    "url": "https://arxiv.org/abs/2601.18778"
  },
  "sourceToolAssistantUUID": "36521018-e3e9-4ecd-8ab4-565ea574d0cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-28T03:06:23.014Z_

```json
{
  "parentUuid": "ba3f6c68-3968-4d11-83c1-7149c8e1d484",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8d10d758-9681-4c2e-b843-5ae7578956f2",
  "timestamp": "2026-05-28T03:06:23.014Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-28T03:06:26.190Z_

<details><summary>Logged reasoning block</summary>

```text
I need more details on several papers. Let me fetch the full PDFs or HTML versions for SEC and Actor-Curator especially, and also try to get the IndiMathBench details. Let me also search for more specific results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d10d758-9681-4c2e-b843-5ae7578956f2",
  "isSidechain": false,
  "requestId": "req_011CbUEB79irJejFdrNZTGME",
  "type": "assistant",
  "uuid": "02e85dea-b0c1-4f0d-860f-0a34ed49b012",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013L2by1quYs7GDBtRNrazvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 3393,
      "cache_read_input_tokens": 26787,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3393,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 214,
          "output_tokens": 725,
          "cache_read_input_tokens": 26787,
          "cache_creation_input_tokens": 3393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3393
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

_source line 32 · 2026-05-28T03:06:26.677Z_

I need more details on several papers. Let me fetch the full versions and do additional searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02e85dea-b0c1-4f0d-860f-0a34ed49b012",
  "isSidechain": false,
  "requestId": "req_011CbUEB79irJejFdrNZTGME",
  "type": "assistant",
  "uuid": "0953ae2a-cedb-40c7-9da7-0d1cda10a28d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013L2by1quYs7GDBtRNrazvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 3393,
      "cache_read_input_tokens": 26787,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3393,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 214,
          "output_tokens": 725,
          "cache_read_input_tokens": 26787,
          "cache_creation_input_tokens": 3393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3393
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

_source line 33 · 2026-05-28T03:06:29.519Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XjnxAPAiQkJ93dee9s5doY`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14970",
  "prompt": "Extract: (1) exact AIME 2024 scores and all numerical results, (2) base model used, (3) how the MAB formulation works - what are the arms (difficulty × type categories), (4) what problem pool/dataset they select from, (5) the TD(0) update mechanism for curriculum policy, (6) comparison to other methods, (7) any limitations or failure modes. Be thorough with all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0953ae2a-cedb-40c7-9da7-0d1cda10a28d",
  "isSidechain": false,
  "requestId": "req_011CbUEB79irJejFdrNZTGME",
  "type": "assistant",
  "uuid": "3eb78aa4-a383-4093-aa19-aa0f249f8038",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013L2by1quYs7GDBtRNrazvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 3393,
      "cache_read_input_tokens": 26787,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3393,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 214,
          "output_tokens": 725,
          "cache_read_input_tokens": 26787,
          "cache_creation_input_tokens": 3393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3393
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

_source line 34 · 2026-05-28T03:06:29.531Z_

<details><summary>↩ Tool result · `toolu_01XjnxAPAiQkJ93dee9s5doY`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eb78aa4-a383-4093-aa19-aa0f249f8038",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "65d7fda7-707e-4151-a458-8d7c89681639",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 8,
    "url": "https://arxiv.org/html/2505.14970"
  },
  "sourceToolAssistantUUID": "3eb78aa4-a383-4093-aa19-aa0f249f8038",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-28T03:06:31.401Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MVsUgSwj4iKu6cgUUm6xPD`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.20532",
  "prompt": "Extract: (1) exact AIME 2024 scores and percentage improvements, (2) base model used, (3) how the neural curator selects problems - the policy-improvement bandit formulation, (4) what problem pool/bank it selects from, (5) how it compares to SEC specifically, (6) regret guarantees details, (7) the ~9% overhead claim, (8) all numerical results and comparisons, (9) key limitations. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65d7fda7-707e-4151-a458-8d7c89681639",
  "isSidechain": false,
  "requestId": "req_011CbUEB79irJejFdrNZTGME",
  "type": "assistant",
  "uuid": "ceeebe6d-38bd-44cd-af70-21b994cfe1fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013L2by1quYs7GDBtRNrazvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 3393,
      "cache_read_input_tokens": 26787,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3393,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 214,
          "output_tokens": 725,
          "cache_read_input_tokens": 26787,
          "cache_creation_input_tokens": 3393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3393
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

_source line 36 · 2026-05-28T03:06:33.759Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013dUbjchmgexm4W96Vi7ZfN`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.03380",
  "prompt": "Extract: (1) the exact theorem about balanced filtering maximizing lower bound on policy improvement, (2) all numerical results especially the +12% and half training steps claims, (3) what benchmarks were used, (4) base model, (5) how difficulty filtering is formally defined, (6) the variance of task-level success probabilities result. Include all key equations if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceeebe6d-38bd-44cd-af70-21b994cfe1fc",
  "isSidechain": false,
  "requestId": "req_011CbUEB79irJejFdrNZTGME",
  "type": "assistant",
  "uuid": "51018c31-e723-48f4-9bb6-b94aec7c6ea0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013L2by1quYs7GDBtRNrazvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 3393,
      "cache_read_input_tokens": 26787,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3393,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 214,
          "output_tokens": 725,
          "cache_read_input_tokens": 26787,
          "cache_creation_input_tokens": 3393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3393
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

_source line 37 · 2026-05-28T03:06:35.454Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QnkHZ76TBupLJ18SRRWuAQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.18778",
  "prompt": "Extract: (1) all numerical results on math benchmarks, (2) base model used, (3) detailed mechanism of bi-level meta-RL teacher/student, (4) how it generates problems at edge of learnability, (5) comparison to other curriculum methods, (6) AIME or competition-level results if any. Be thorough with numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51018c31-e723-48f4-9bb6-b94aec7c6ea0",
  "isSidechain": false,
  "requestId": "req_011CbUEB79irJejFdrNZTGME",
  "type": "assistant",
  "uuid": "76e7270b-6632-4a2f-868f-099c98195cfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013L2by1quYs7GDBtRNrazvf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 214,
      "cache_creation_input_tokens": 3393,
      "cache_read_input_tokens": 26787,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3393,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 214,
          "output_tokens": 725,
          "cache_read_input_tokens": 26787,
          "cache_creation_input_tokens": 3393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3393
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

_source line 38 · 2026-05-28T03:06:42.845Z_

<details><summary>↩ Tool result · `toolu_013dUbjchmgexm4W96Vi7ZfN`</summary>

```text
# Key Findings from "Online Difficulty Filtering for Reasoning Oriented Reinforcement Learning"

## (1) Core Theorem on Balanced Filtering

**Proposition 3.1** establishes that reverse KL divergence between initial and optimal policies satisfies:

$$\mathbb{D}_{\mathrm{KL}}(\pi_{\mathrm{init}} \| \pi^*) \geq \frac{p(x)(1-p(x))}{2\beta^2}$$

This bound is "maximized at p(x)=1/2," meaning intermediate-difficulty tasks (around 50% success rate) provide maximum learning signal. The framework proves that "absolute-hard or absolute-easy prompts" yield zero divergence and thus no gradient information.

## (2) Numerical Results

Key performance improvements reported:
- **3B model**: "+10% on AIME" and "+4.2% in average" across benchmarks
- **7B model**: "+12% on AMC" and "+4.5% in average"
- **Training efficiency**: "less than half of gradient updates to outperform plain GRPO"
- Balanced filtering with thresholds (0.3<p(x)<0.7) achieved approximately 30% average performance versus 26.3% for plain GRPO

## (3) Evaluation Benchmarks

Five math reasoning benchmarks tested:
- MATH500
- AIME (American Invitational Mathematics Examination)
- AMC (American Mathematics Competitions)
- MinervaMath
- OlympiadBench

## (4) Base Model

**Qwen2.5** family: experiments used both 3B and 7B parameter versions, with supervised fine-tuning on "1.1K verified problem-solution pairs."

## (5) Formal Definition of Difficulty Filtering

Balanced online difficulty filtering uses symmetric thresholds around 0.5 pass rate. Examples are filtered based on measured success rate p(𝐱) via rollout sampling. The method "asynchronously filters and fills the batch" maintaining fixed batch size N while selecting only prompts where T_Low ≤ p(𝐱) ≤ T_High.

## (6) Variance and Task-Level Success Probabilities

The analysis demonstrates that expected policy improvement is lower-bounded by "the variance of task-level success probabilities." For binary rewards following Bernoulli distribution, this variance is p(x)(1-p(x)), which directly controls learnability. The paper establishes that "sample reward variance" serves as a reliable proxy for learnability across different reward distributions (binary, Gaussian, multinomial).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51018c31-e723-48f4-9bb6-b94aec7c6ea0",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "584fb77f-b4d6-4073-bca3-1b063c2fddbc",
  "toolUseResult": {
    "bytes": 468150,
    "code": 200,
    "codeText": "OK",
    "result": "# Key Findings from \"Online Difficulty Filtering for Reasoning Oriented Reinforcement Learning\"\n\n## (1) Core Theorem on Balanced Filtering\n\n**Proposition 3.1** establishes that reverse KL divergence between initial and optimal policies satisfies:\n\n$$\\mathbb{D}_{\\mathrm{KL}}(\\pi_{\\mathrm{init}} \\| \\pi^*) \\geq \\frac{p(x)(1-p(x))}{2\\beta^2}$$\n\nThis bound is \"maximized at p(x)=1/2,\" meaning intermediate-difficulty tasks (around 50% success rate) provide maximum learning signal. The framework proves that \"absolute-hard or absolute-easy prompts\" yield zero divergence and thus no gradient information.\n\n## (2) Numerical Results\n\nKey performance improvements reported:\n- **3B model**: \"+10% on AIME\" and \"+4.2% in average\" across benchmarks\n- **7B model**: \"+12% on AMC\" and \"+4.5% in average\"\n- **Training efficiency**: \"less than half of gradient updates to outperform plain GRPO\"\n- Balanced filtering with thresholds (0.3<p(x)<0.7) achieved approximately 30% average performance versus 26.3% for plain GRPO\n\n## (3) Evaluation Benchmarks\n\nFive math reasoning benchmarks tested:\n- MATH500\n- AIME (American Invitational Mathematics Examination)\n- AMC (American Mathematics Competitions)\n- MinervaMath\n- OlympiadBench\n\n## (4) Base Model\n\n**Qwen2.5** family: experiments used both 3B and 7B parameter versions, with supervised fine-tuning on \"1.1K verified problem-solution pairs.\"\n\n## (5) Formal Definition of Difficulty Filtering\n\nBalanced online difficulty filtering uses symmetric thresholds around 0.5 pass rate. Examples are filtered based on measured success rate p(𝐱) via rollout sampling. The method \"asynchronously filters and fills the batch\" maintaining fixed batch size N while selecting only prompts where T_Low ≤ p(𝐱) ≤ T_High.\n\n## (6) Variance and Task-Level Success Probabilities\n\nThe analysis demonstrates that expected policy improvement is lower-bounded by \"the variance of task-level success probabilities.\" For binary rewards following Bernoulli distribution, this variance is p(x)(1-p(x)), which directly controls learnability. The paper establishes that \"sample reward variance\" serves as a reliable proxy for learnability across different reward distributions (binary, Gaussian, multinomial).",
    "durationMs": 9083,
    "url": "https://arxiv.org/html/2504.03380"
  },
  "sourceToolAssistantUUID": "51018c31-e723-48f4-9bb6-b94aec7c6ea0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-28T03:06:45.481Z_

<details><summary>↩ Tool result · `toolu_01MVsUgSwj4iKu6cgUUm6xPD`</summary>

```text
# Actor-Curator: Key Findings and Technical Details

## AIME 2024 Performance
The paper reports that Actor-Curator achieves **30.00%** on AIME24, compared to 23.33% for the "Prompt Curriculum Learning" (PCL) baseline and 20.00% for SEC. This represents a **+6.67 percentage point improvement** or **28.57% relative gain** over the strongest baseline.

## Base Model
The actor was trained using **Qwen2.5-3B**, with a curator initialized from a pretrained **Qwen3-0.6B model**. Additional experiments used **Llama3.2-3B-Instruct** (results in Appendix).

## Problem Selection Mechanism
The curator operates via a **non-stationary stochastic bandit formulation**. Key elements:

- **Per-problem utility**: Estimated as expected policy improvement contribution using the importance-sampled advantage: `u_x^t = p_X(x) * E[π^(t+1)(y|x)/π^t(y|x) * A(y|x)]`
- **OSMD Update**: The curator is optimized with negative-entropy regularization: `p^(t+1) ∝ p^t(x) * exp(η * U_hat_x^t)`
- **Two-stage sampling**: First samples a candidate batch from a fixed proposal distribution, then the curator reweights within that batch
- **Function approximation**: A neural network assigns positive scores to problems, implicitly defining probability distribution

## Problem Pool
The experiments used:
- **30,000 problems** for Countdown, Zebra, and ARC-1D
- **12,000 MATH problems** for MATH500 and AIME24

## Comparison with SEC
The paper notes that SEC "partitions problems into manually defined buckets and updates bucket probabilities based on the sum of absolute advantages." Actor-Curator outperforms SEC across most benchmarks:

| Benchmark | SEC | Actor-Curator | Gain |
|-----------|-----|---------------|------|
| Countdown | 58.87 | 62.12 | +5.52% |
| ARC-1D | 27.87 | 36.37 | +30.51% |
| AIME24 | 20.00 | 30.00 | +28.57% |

## Regret Guarantees
**Theorem 2** establishes that cumulative dynamic regret satisfies:

`RegT ≤ O(T^(2/3) * V_T^(1/3))`

Where V_T measures the sum of maximum utility changes across problems: `V_T = Σ(t=2 to T) max_x |u_x^t - u_x^(t-1)|`

This bound characterizes the curator's ability to track optimal problem selection despite non-stationary utilities.

## Computational Overhead
The paper states: "Actor-Curator increases overall wall-clock training time by approximately 9%" (See Appendix H). The authors note this overhead is "small compared to the observed gains in training efficiency."

## Numerical Results Summary

**Peak Performance (within 100 steps):**
- Countdown: 62.12% (+5.52 points vs SEC)
- Countdown-hard: 58.00% (+12.62 relative)
- Zebra: 37.62% (+4.50 relative)
- Zebra-hard: 34.50% (+13.11 relative)
- ARC-1D: 36.37% (+30.51 relative)
- ARC-hard: 31.00% (+58.97 relative)
- MATH500: 81.00% (-2.41 relative)
- AIME24: 30.00% (+28.57 relative)

**Efficiency gains**: Up to 80% speedup in reaching comparable performance levels.

## Key Limitations

The authors identify several constraints:

1. **Actor dependency**: "Gains ultimately depend on stability and quality of underlying actor optimization; unstable updates can lead to training collapse"

2. **Reward signal requirement**: Best suited to domains with "objectively verifiable rewards such as mathematics, logic puzzles, and code"

3. **Computational cost**: The 9% overhead, though modest relative to gains, remains non-negligible

4. **Coupling assumption**: The per-problem utility attribution assumes small policy updates; larger changes reduce attribution validity
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceeebe6d-38bd-44cd-af70-21b994cfe1fc",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "b4d8e985-cf55-4b17-afe9-08beb55c94ea",
  "toolUseResult": {
    "bytes": 678399,
    "code": 200,
    "codeText": "OK",
    "result": "# Actor-Curator: Key Findings and Technical Details\n\n## AIME 2024 Performance\nThe paper reports that Actor-Curator achieves **30.00%** on AIME24, compared to 23.33% for the \"Prompt Curriculum Learning\" (PCL) baseline and 20.00% for SEC. This represents a **+6.67 percentage point improvement** or **28.57% relative gain** over the strongest baseline.\n\n## Base Model\nThe actor was trained using **Qwen2.5-3B**, with a curator initialized from a pretrained **Qwen3-0.6B model**. Additional experiments used **Llama3.2-3B-Instruct** (results in Appendix).\n\n## Problem Selection Mechanism\nThe curator operates via a **non-stationary stochastic bandit formulation**. Key elements:\n\n- **Per-problem utility**: Estimated as expected policy improvement contribution using the importance-sampled advantage: `u_x^t = p_X(x) * E[π^(t+1)(y|x)/π^t(y|x) * A(y|x)]`\n- **OSMD Update**: The curator is optimized with negative-entropy regularization: `p^(t+1) ∝ p^t(x) * exp(η * U_hat_x^t)`\n- **Two-stage sampling**: First samples a candidate batch from a fixed proposal distribution, then the curator reweights within that batch\n- **Function approximation**: A neural network assigns positive scores to problems, implicitly defining probability distribution\n\n## Problem Pool\nThe experiments used:\n- **30,000 problems** for Countdown, Zebra, and ARC-1D\n- **12,000 MATH problems** for MATH500 and AIME24\n\n## Comparison with SEC\nThe paper notes that SEC \"partitions problems into manually defined buckets and updates bucket probabilities based on the sum of absolute advantages.\" Actor-Curator outperforms SEC across most benchmarks:\n\n| Benchmark | SEC | Actor-Curator | Gain |\n|-----------|-----|---------------|------|\n| Countdown | 58.87 | 62.12 | +5.52% |\n| ARC-1D | 27.87 | 36.37 | +30.51% |\n| AIME24 | 20.00 | 30.00 | +28.57% |\n\n## Regret Guarantees\n**Theorem 2** establishes that cumulative dynamic regret satisfies:\n\n`RegT ≤ O(T^(2/3) * V_T^(1/3))`\n\nWhere V_T measures the sum of maximum utility changes across problems: `V_T = Σ(t=2 to T) max_x |u_x^t - u_x^(t-1)|`\n\nThis bound characterizes the curator's ability to track optimal problem selection despite non-stationary utilities.\n\n## Computational Overhead\nThe paper states: \"Actor-Curator increases overall wall-clock training time by approximately 9%\" (See Appendix H). The authors note this overhead is \"small compared to the observed gains in training efficiency.\"\n\n## Numerical Results Summary\n\n**Peak Performance (within 100 steps):**\n- Countdown: 62.12% (+5.52 points vs SEC)\n- Countdown-hard: 58.00% (+12.62 relative)\n- Zebra: 37.62% (+4.50 relative)\n- Zebra-hard: 34.50% (+13.11 relative)\n- ARC-1D: 36.37% (+30.51 relative)\n- ARC-hard: 31.00% (+58.97 relative)\n- MATH500: 81.00% (-2.41 relative)\n- AIME24: 30.00% (+28.57 relative)\n\n**Efficiency gains**: Up to 80% speedup in reaching comparable performance levels.\n\n## Key Limitations\n\nThe authors identify several constraints:\n\n1. **Actor dependency**: \"Gains ultimately depend on stability and quality of underlying actor optimization; unstable updates can lead to training collapse\"\n\n2. **Reward signal requirement**: Best suited to domains with \"objectively verifiable rewards such as mathematics, logic puzzles, and code\"\n\n3. **Computational cost**: The 9% overhead, though modest relative to gains, remains non-negligible\n\n4. **Coupling assumption**: The per-problem utility attribution assumes small policy updates; larger changes reduce attribution validity",
    "durationMs": 14077,
    "url": "https://arxiv.org/html/2602.20532"
  },
  "sourceToolAssistantUUID": "ceeebe6d-38bd-44cd-af70-21b994cfe1fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "b4d8e985-cf55-4b17-afe9-08beb55c94ea",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Tool result

_source line 42 · 2026-05-28T03:06:48.733Z_

<details><summary>↩ Tool result · `toolu_01QnkHZ76TBupLJ18SRRWuAQ`</summary>

```text
# SOAR: Self-Generated Curriculum for Mathematical Reasoning

## Key Numerical Results on Math Benchmarks

**MATH fail@128 dataset** (problems with 0/128 baseline success):
- Hard-Only baseline: pass@32 = 9.6%
- PQ (Promotion Questions): +9.3% improvement → ~18.9% pass@32
- PS (Promoted Student): +8.5% improvement → ~18.1% pass@32
- Compared to intrinsic-reward baseline (Intrinsic-T): significantly lower performance

**HARP fail@128 dataset**:
- PQ achieved +4.2% pass@32 over Hard-Only
- PS achieved +3.6% pass@32 over Hard-Only

**OlympiadBench transfer** (held-out test):
- PQ-MATH: +6% over Hard-Only
- PQ-HARP: +3% over Hard-Only

**Oracle comparison**: Synthetic questions recovered 75% of gains from training on full MATH dataset (6,750 problems).

## Base Model and Scale

**Llama-3.2-3B-Instruct** exclusively. All experiments used this 3-billion parameter instruction-tuned model.

## Bi-Level Meta-RL Architecture

The framework employs nested optimization loops:

**Outer loop (Teacher)**: Uses RLOO to train a teacher model generating question-answer pairs. Reward is "the measurable student improvement on hard problems relative to a baseline."

**Inner loop (Student)**: Student trains via RLVR on teacher-generated problems for 10 steps (batch size 8). Performance improvement on 64 sampled hard-problem questions becomes the teacher's reward signal.

**Promotion mechanism**: When moving-average teacher rewards exceed threshold τ=0.01, the best-performing student becomes the new baseline, accumulating synthetic problems into 𝒟_best.

## Edge-of-Learnability Problem Generation

The teacher generates stepping stones without seeing original hard problems. Key insight: "a model's ability to generate effective stepping stones for hard problems is distinct from its ability to solve them."

**Structural focus over correctness**: Only 32.8% of generated problems had fully correct solutions; 63% were mathematically well-posed. The analysis shows "question structure matters more than answer correctness" for models at plateaus.

## Comparison to Curriculum Methods

**Hard-Only baseline** (direct RLVR on fail@128): Minimal improvement despite 128× sampling group size providing only +2.8% pass@32.

**Intrinsic-T baseline** (learnability rewards): Showed instability with one of three seeds exhibiting complete failure. Semantic diversity collapsed to Vendi Score 10.82 versus Grounded-T's 31.99.

**Base-T sampling**: Grounded-T "consistently tracks the upper envelope" of Base-T performance, showing meta-RL sharpens latent pedagogical capabilities.

**Oracle (full MATH training set)**: Synthetic questions achieved 75-100% of oracle gains depending on dataset.

## AIME/Competition-Level Results

The paper focuses exclusively on **fail@128 filtered subsets** from competition math benchmarks (MATH, HARP, OlympiadBench). No direct AIME competition results reported; the hardest problems studied are those where baseline success is literally 0/128 attempts.

## Computational Cost

Training involved "200 outer-loop steps" with "4 parallel student trainings per dataset." The authors acknowledge this bilevel approach requires significant compute versus direct training alternatives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76e7270b-6632-4a2f-868f-099c98195cfc",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "08c12400-b22a-43d0-960a-599147b44d0c",
  "toolUseResult": {
    "bytes": 429224,
    "code": 200,
    "codeText": "OK",
    "result": "# SOAR: Self-Generated Curriculum for Mathematical Reasoning\n\n## Key Numerical Results on Math Benchmarks\n\n**MATH fail@128 dataset** (problems with 0/128 baseline success):\n- Hard-Only baseline: pass@32 = 9.6%\n- PQ (Promotion Questions): +9.3% improvement → ~18.9% pass@32\n- PS (Promoted Student): +8.5% improvement → ~18.1% pass@32\n- Compared to intrinsic-reward baseline (Intrinsic-T): significantly lower performance\n\n**HARP fail@128 dataset**:\n- PQ achieved +4.2% pass@32 over Hard-Only\n- PS achieved +3.6% pass@32 over Hard-Only\n\n**OlympiadBench transfer** (held-out test):\n- PQ-MATH: +6% over Hard-Only\n- PQ-HARP: +3% over Hard-Only\n\n**Oracle comparison**: Synthetic questions recovered 75% of gains from training on full MATH dataset (6,750 problems).\n\n## Base Model and Scale\n\n**Llama-3.2-3B-Instruct** exclusively. All experiments used this 3-billion parameter instruction-tuned model.\n\n## Bi-Level Meta-RL Architecture\n\nThe framework employs nested optimization loops:\n\n**Outer loop (Teacher)**: Uses RLOO to train a teacher model generating question-answer pairs. Reward is \"the measurable student improvement on hard problems relative to a baseline.\"\n\n**Inner loop (Student)**: Student trains via RLVR on teacher-generated problems for 10 steps (batch size 8). Performance improvement on 64 sampled hard-problem questions becomes the teacher's reward signal.\n\n**Promotion mechanism**: When moving-average teacher rewards exceed threshold τ=0.01, the best-performing student becomes the new baseline, accumulating synthetic problems into 𝒟_best.\n\n## Edge-of-Learnability Problem Generation\n\nThe teacher generates stepping stones without seeing original hard problems. Key insight: \"a model's ability to generate effective stepping stones for hard problems is distinct from its ability to solve them.\"\n\n**Structural focus over correctness**: Only 32.8% of generated problems had fully correct solutions; 63% were mathematically well-posed. The analysis shows \"question structure matters more than answer correctness\" for models at plateaus.\n\n## Comparison to Curriculum Methods\n\n**Hard-Only baseline** (direct RLVR on fail@128): Minimal improvement despite 128× sampling group size providing only +2.8% pass@32.\n\n**Intrinsic-T baseline** (learnability rewards): Showed instability with one of three seeds exhibiting complete failure. Semantic diversity collapsed to Vendi Score 10.82 versus Grounded-T's 31.99.\n\n**Base-T sampling**: Grounded-T \"consistently tracks the upper envelope\" of Base-T performance, showing meta-RL sharpens latent pedagogical capabilities.\n\n**Oracle (full MATH training set)**: Synthetic questions achieved 75-100% of oracle gains depending on dataset.\n\n## AIME/Competition-Level Results\n\nThe paper focuses exclusively on **fail@128 filtered subsets** from competition math benchmarks (MATH, HARP, OlympiadBench). No direct AIME competition results reported; the hardest problems studied are those where baseline success is literally 0/128 attempts.\n\n## Computational Cost\n\nTraining involved \"200 outer-loop steps\" with \"4 parallel student trainings per dataset.\" The authors acknowledge this bilevel approach requires significant compute versus direct training alternatives.",
    "durationMs": 13277,
    "url": "https://arxiv.org/html/2601.18778"
  },
  "sourceToolAssistantUUID": "76e7270b-6632-4a2f-868f-099c98195cfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-28T03:06:51.357Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the SEC paper details more thoroughly, and also verify the IndiMathBench geometry numbers. Let me also get the actual SEC AIME 2024 numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08c12400-b22a-43d0-960a-599147b44d0c",
  "isSidechain": false,
  "requestId": "req_011CbUED18dPu4aXBRSxCx8p",
  "type": "assistant",
  "uuid": "09977d01-ee90-4a5a-b3b1-f94b90c6ab27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmM6Sk2AAwwCMXc5rmhgyx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 30180,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 30180,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3602
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

_source line 44 · 2026-05-28T03:06:51.850Z_

Now let me get more details on SEC and verify IndiMathBench numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09977d01-ee90-4a5a-b3b1-f94b90c6ab27",
  "isSidechain": false,
  "requestId": "req_011CbUED18dPu4aXBRSxCx8p",
  "type": "assistant",
  "uuid": "97d4180b-9536-40aa-bae4-bbf35c5cff73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmM6Sk2AAwwCMXc5rmhgyx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 30180,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 30180,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3602
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

_source line 45 · 2026-05-28T03:06:53.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019kr6Qm2GGH9ADMAqXWSy3p`</summary>

```json
{
  "query": "SEC self-evolving curriculum arXiv 2505.14970 AIME 2024 results Qwen2.5-7B 17.5%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97d4180b-9536-40aa-bae4-bbf35c5cff73",
  "isSidechain": false,
  "requestId": "req_011CbUED18dPu4aXBRSxCx8p",
  "type": "assistant",
  "uuid": "5a91490a-61b8-4ba6-a9a7-71c8d66e5d3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmM6Sk2AAwwCMXc5rmhgyx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 30180,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 30180,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3602
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

_source line 46 · 2026-05-28T03:06:53.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L2xYAbBgDpj2UfYDf1Ygov`</summary>

```json
{
  "query": "IndiMathBench geometry success rate BEq autoformalization topic breakdown"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a91490a-61b8-4ba6-a9a7-71c8d66e5d3b",
  "isSidechain": false,
  "requestId": "req_011CbUED18dPu4aXBRSxCx8p",
  "type": "assistant",
  "uuid": "b4977cbb-db56-49cd-90e3-d5f6fc6db743",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmM6Sk2AAwwCMXc5rmhgyx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 30180,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 30180,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3602
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

_source line 47 · 2026-05-28T03:06:54.379Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V5u3KuQeb3zb6CDbbQajDU`</summary>

```json
{
  "query": "Actor-Curator arXiv 2602.20532 SEC comparison AIME 2024 Qwen2.5-7B results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4977cbb-db56-49cd-90e3-d5f6fc6db743",
  "isSidechain": false,
  "requestId": "req_011CbUED18dPu4aXBRSxCx8p",
  "type": "assistant",
  "uuid": "51a4faf4-2032-48ec-9ce1-7ccee84ec93f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmM6Sk2AAwwCMXc5rmhgyx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 30180,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 30180,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3602
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

_source line 48 · 2026-05-28T03:07:01.598Z_

<details><summary>↩ Tool result · `toolu_01V5u3KuQeb3zb6CDbbQajDU`</summary>

```text
Web search results for query: "Actor-Curator arXiv 2602.20532 SEC comparison AIME 2024 Qwen2.5-7B results"

Links: [{"title":"Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training","url":"https://arxiv.org/pdf/2602.20532"},{"title":"Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for Scalable RL Post-Training","url":"https://arxiv.org/html/2602.20532"},{"title":"Actor-Curator: Co-adaptive Curriculum Learning via Policy ...","url":"https://arxiv.org/abs/2602.20532"},{"title":"Performance on Qwen2.5-7B-Instruct · Issue #42 · simplescaling/s1","url":"https://github.com/simplescaling/s1/issues/42"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub","url":"https://github.com/QwenLM/Qwen2.5-Math"}]

Based on the search results, here's what I found regarding your query:

Actor-Curator is a scalable and fully automated framework for reinforcement learning post-training of large language models (LLMs) that learns to adaptively curate training problems. The ACTOR-CURATOR system trains a neural curator that dynamically selects problems from large problem banks by directly optimizing for expected policy performance improvement.

Regarding the specific results you mentioned:

- **AIME 2024 Performance**: The framework achieves relative gains of 28.6% on AIME2024 over the strongest baseline.

- **SEC Comparison**: Actor-Curator outperforms both other learning based methods (PCL) and methods that rely on human heuristics (SEC).

- **Model Used**: While the paper discusses results with Qwen2.5-3B, the actor is trained using GSPO, a stabilized variant of GRPO, on Qwen2.5-3B in the primary experiments. The search results do not contain specific Qwen2.5-7B results for this particular paper.

The arXiv paper 2602.20532 was submitted on February 24, 2026, and presents a principled approach to adaptive curriculum learning for LLM post-training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51a4faf4-2032-48ec-9ce1-7ccee84ec93f",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "196973ad-cdbb-4b63-9bdc-6f060f4994f5",
  "toolUseResult": {
    "query": "Actor-Curator arXiv 2602.20532 SEC comparison AIME 2024 Qwen2.5-7B results",
    "results": [
      {
        "tool_use_id": "srvtoolu_018GBccXGgSqzVEWjLfUpa1M",
        "content": [
          {
            "title": "Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for RL Post-Training",
            "url": "https://arxiv.org/pdf/2602.20532"
          },
          {
            "title": "Actor-Curator: Co-adaptive Curriculum Learning via Policy-Improvement Bandits for Scalable RL Post-Training",
            "url": "https://arxiv.org/html/2602.20532"
          },
          {
            "title": "Actor-Curator: Co-adaptive Curriculum Learning via Policy ...",
            "url": "https://arxiv.org/abs/2602.20532"
          },
          {
            "title": "Performance on Qwen2.5-7B-Instruct · Issue #42 · simplescaling/s1",
            "url": "https://github.com/simplescaling/s1/issues/42"
          },
          {
            "title": "2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen",
            "url": "https://arxiv.org/pdf/2412.15115"
          },
          {
            "title": "GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub",
            "url": "https://github.com/QwenLM/Qwen2.5-Math"
          }
        ]
      },
      "Based on the search results, here's what I found regarding your query:\n\nActor-Curator is a scalable and fully automated framework for reinforcement learning post-training of large language models (LLMs) that learns to adaptively curate training problems. The ACTOR-CURATOR system trains a neural curator that dynamically selects problems from large problem banks by directly optimizing for expected policy performance improvement.\n\nRegarding the specific results you mentioned:\n\n- **AIME 2024 Performance**: The framework achieves relative gains of 28.6% on AIME2024 over the strongest baseline.\n\n- **SEC Comparison**: Actor-Curator outperforms both other learning based methods (PCL) and methods that rely on human heuristics (SEC).\n\n- **Model Used**: While the paper discusses results with Qwen2.5-3B, the actor is trained using GSPO, a stabilized variant of GRPO, on Qwen2.5-3B in the primary experiments. The search results do not contain specific Qwen2.5-7B results for this particular paper.\n\nThe arXiv paper 2602.20532 was submitted on February 24, 2026, and presents a principled approach to adaptive curriculum learning for LLM post-training."
    ],
    "durationSeconds": 7.215266785999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "51a4faf4-2032-48ec-9ce1-7ccee84ec93f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-28T03:07:02.524Z_

<details><summary>↩ Tool result · `toolu_01L2xYAbBgDpj2UfYDf1Ygov`</summary>

```text
Web search results for query: "IndiMathBench geometry success rate BEq autoformalization topic breakdown"

Links: [{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"},{"title":"(PDF) IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://www.researchgate.net/publication/398225105_IndiMathBench_Autoformalizing_Mathematical_Reasoning_Problems_with_a_Human_Touch"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/html/2512.00997"},{"title":"PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition","url":"https://www.researchgate.net/publication/397199196_PutnamBench_Evaluating_Neural_Theorem-Provers_on_the_Putnam_Mathematical_Competition"},{"title":"Autoformalization with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/401455895_Autoformalization_with_Large_Language_Models"},{"title":"[2512.00997] IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/abs/2512.00997"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch | OpenReview","url":"https://openreview.net/forum?id=tmReo37kl2"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"}]

Based on the search results, here's what I found about IndiMathBench geometry success rates and BEq performance:

## Geometry Success Rate and BEq Performance

Of 108 successful BEq formalizations from the top three models (Claude Opus 4, Gemini 2.5 Pro, GPT-5), only 12 originated from geometry problems, indicating systematic difficulties with spatial reasoning and coordinate-free geometric formalization.

More specifically, geometry problems contributed only 6 of 67 successful formalizations for the best-performing model.

## Overall BEq and Model Performance

Claude Opus 4 achieved the highest BEq score (67/312) and compilation success rate (243/312). Claude Opus 4 leads across multiple evaluation metrics with 67 BEq-passing formalizations and 0.512 mean GTED score, representing the current state-of-the-art in mathematical autoformalization.

## Problem Domains and Topics

IndiMathBench problems are traditionally sourced from a fixed set of topics: algebra, euclidean geometry, elementary number theory, and combinatorics.

The results highlight that while models achieve reasonable success on formal verification tasks overall, geometry problems represent a particular challenge area in the benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4977cbb-db56-49cd-90e3-d5f6fc6db743",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "a2d04bb1-65b1-47eb-9bfe-7b6b734ff884",
  "toolUseResult": {
    "query": "IndiMathBench geometry success rate BEq autoformalization topic breakdown",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G2WhwaDttUC7vAi4h9xoGT",
        "content": [
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning ...",
            "url": "https://arxiv.org/pdf/2512.00997"
          },
          {
            "title": "INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-",
            "url": "https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"
          },
          {
            "title": "(PDF) IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://www.researchgate.net/publication/398225105_IndiMathBench_Autoformalizing_Mathematical_Reasoning_Problems_with_a_Human_Touch"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/html/2512.00997"
          },
          {
            "title": "PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition",
            "url": "https://www.researchgate.net/publication/397199196_PutnamBench_Evaluating_Neural_Theorem-Provers_on_the_Putnam_Mathematical_Competition"
          },
          {
            "title": "Autoformalization with Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/401455895_Autoformalization_with_Large_Language_Models"
          },
          {
            "title": "[2512.00997] IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/abs/2512.00997"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch | OpenReview",
            "url": "https://openreview.net/forum?id=tmReo37kl2"
          },
          {
            "title": "Reliable Evaluation and Benchmarks for Statement Autoformalization",
            "url": "https://arxiv.org/pdf/2406.07222"
          }
        ]
      },
      "Based on the search results, here's what I found about IndiMathBench geometry success rates and BEq performance:\n\n## Geometry Success Rate and BEq Performance\n\nOf 108 successful BEq formalizations from the top three models (Claude Opus 4, Gemini 2.5 Pro, GPT-5), only 12 originated from geometry problems, indicating systematic difficulties with spatial reasoning and coordinate-free geometric formalization.\n\nMore specifically, geometry problems contributed only 6 of 67 successful formalizations for the best-performing model.\n\n## Overall BEq and Model Performance\n\nClaude Opus 4 achieved the highest BEq score (67/312) and compilation success rate (243/312). Claude Opus 4 leads across multiple evaluation metrics with 67 BEq-passing formalizations and 0.512 mean GTED score, representing the current state-of-the-art in mathematical autoformalization.\n\n## Problem Domains and Topics\n\nIndiMathBench problems are traditionally sourced from a fixed set of topics: algebra, euclidean geometry, elementary number theory, and combinatorics.\n\nThe results highlight that while models achieve reasonable success on formal verification tasks overall, geometry problems represent a particular challenge area in the benchmark."
    ],
    "durationSeconds": 8.726269603999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b4977cbb-db56-49cd-90e3-d5f6fc6db743",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T03:07:03.871Z_

<details><summary>↩ Tool result · `toolu_019kr6Qm2GGH9ADMAqXWSy3p`</summary>

```text
Web search results for query: "SEC self-evolving curriculum arXiv 2505.14970 AIME 2024 results Qwen2.5-7B 17.5%"

Links: [{"title":"[2505.14970] Self-Evolving Curriculum for LLM Reasoning","url":"https://arxiv.org/abs/2505.14970"},{"title":"[2505.14970v3] Self-Evolving Curriculum for LLM Reasoning","url":"https://arxiv.org/abs/2505.14970v3"},{"title":"Self-Evolving Curriculum for LLM Reasoning","url":"https://arxiv.org/pdf/2505.14970"},{"title":"Self-Evolving Curriculum for LLM Reasoning","url":"https://www.emergentmind.com/papers/2505.14970"},{"title":"Self-Evolving Curriculum for LLM Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.14970v1"},{"title":"Self-Evolving Curriculum for LLM Reasoning","url":"https://arxiv.org/html/2505.14970v3"},{"title":"TACLer: Tailored Curriculum Reinforcement Learning for Efficient Reasoning","url":"https://arxiv.org/html/2601.21711"},{"title":"Paper page - Self-Evolving Curriculum for LLM Reasoning","url":"https://huggingface.co/papers/2505.14970"},{"title":"Self-evolving Embodied AI","url":"https://arxiv.org/pdf/2602.04411"}]

I found information about the paper arXiv 2505.14970, but the search results don't contain specific details about AIME 2024 results or Qwen2.5-7B's 17.5% performance. Let me search more specifically for those details.

Links: [{"title":"Qwen 2.5 Math 7B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen-2_5-math-7b"},{"title":"Performance on Qwen2.5-7B-Instruct · Issue #42 · simplescaling/s1","url":"https://github.com/simplescaling/s1/issues/42"},{"title":"Qwen2.5-Math: The world's leading open-sourced mathematical LLMs | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math/"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via   Self-Improvement","url":"https://arxiv.org/pdf/2409.12122"},{"title":"Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement","url":"https://arxiv.org/html/2409.12122v1"},{"title":"GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub","url":"https://github.com/QwenLM/Qwen2.5-Math"},{"title":"AIME 2024 and AIME 2025 Benchmarks","url":"https://www.emergentmind.com/topics/aime-2024-and-aime-2025-benchmarks"}]

Based on my search results, I've found information about the SEC (Self-Evolving Curriculum) paper from arXiv 2505.14970 and details about Qwen2.5-7B's performance on AIME 2024.

## SEC Paper (arXiv 2505.14970)

The paper proposes Self-Evolving Curriculum (SEC), an automatic curriculum learning method that learns a curriculum policy concurrently with the RL fine-tuning process. The approach formulates curriculum selection as a non-stationary Multi-Armed Bandit problem, treating each problem category (e.g., difficulty level or problem type) as an individual arm.

Across three distinct reasoning domains: planning, inductive reasoning, and mathematics, the experiments demonstrate that SEC significantly improves models' reasoning capabilities, enabling better generalization to harder, out-of-distribution test problems.

## Qwen2.5-7B Performance on AIME 2024

Regarding the 17.5% result you mentioned, Qwen2.5-Math-72B-Instruct outperforms GPT-4o by an impressive 17.5 points (this refers to a performance margin, not the 7B model's absolute score). 

For the base Qwen2.5-7B model: the original Qwen-2.5-7B-Instruct model achieves 16.67% on AIME 2024, which is close to the 17.5% figure you mentioned. However, I was unable to find specific documentation linking the exact 17.5% result directly to results from the SEC paper in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a91490a-61b8-4ba6-a9a7-71c8d66e5d3b",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "035f8cef-a4b3-4776-903f-a71cee2cc14f",
  "toolUseResult": {
    "query": "SEC self-evolving curriculum arXiv 2505.14970 AIME 2024 results Qwen2.5-7B 17.5%",
    "results": [
      {
        "tool_use_id": "srvtoolu_01483SMPzrpFM9MJu2SAgcun",
        "content": [
          {
            "title": "[2505.14970] Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://arxiv.org/abs/2505.14970"
          },
          {
            "title": "[2505.14970v3] Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://arxiv.org/abs/2505.14970v3"
          },
          {
            "title": "Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2505.14970"
          },
          {
            "title": "Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://www.emergentmind.com/papers/2505.14970"
          },
          {
            "title": "Self-Evolving Curriculum for LLM Reasoning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2505.14970v1"
          },
          {
            "title": "Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://arxiv.org/html/2505.14970v3"
          },
          {
            "title": "TACLer: Tailored Curriculum Reinforcement Learning for Efficient Reasoning",
            "url": "https://arxiv.org/html/2601.21711"
          },
          {
            "title": "Paper page - Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://huggingface.co/papers/2505.14970"
          },
          {
            "title": "Self-evolving Embodied AI",
            "url": "https://arxiv.org/pdf/2602.04411"
          }
        ]
      },
      "I found information about the paper arXiv 2505.14970, but the search results don't contain specific details about AIME 2024 results or Qwen2.5-7B's 17.5% performance. Let me search more specifically for those details.",
      {
        "tool_use_id": "srvtoolu_013nvG5q4pDRpoQDNrXV9U8i",
        "content": [
          {
            "title": "Qwen 2.5 Math 7B | Open Laboratory",
            "url": "https://openlaboratory.ai/models/qwen-2_5-math-7b"
          },
          {
            "title": "Performance on Qwen2.5-7B-Instruct · Issue #42 · simplescaling/s1",
            "url": "https://github.com/simplescaling/s1/issues/42"
          },
          {
            "title": "Qwen2.5-Math: The world's leading open-sourced mathematical LLMs | Qwen",
            "url": "https://qwenlm.github.io/blog/qwen2.5-math/"
          },
          {
            "title": "2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen",
            "url": "https://arxiv.org/pdf/2412.15115"
          },
          {
            "title": "Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via   Self-Improvement",
            "url": "https://arxiv.org/pdf/2409.12122"
          },
          {
            "title": "Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement",
            "url": "https://arxiv.org/html/2409.12122v1"
          },
          {
            "title": "GitHub - QwenLM/Qwen2.5-Math: A series of math-specific large language models of our Qwen2 series. · GitHub",
            "url": "https://github.com/QwenLM/Qwen2.5-Math"
          },
          {
            "title": "AIME 2024 and AIME 2025 Benchmarks",
            "url": "https://www.emergentmind.com/topics/aime-2024-and-aime-2025-benchmarks"
          }
        ]
      },
      "Based on my search results, I've found information about the SEC (Self-Evolving Curriculum) paper from arXiv 2505.14970 and details about Qwen2.5-7B's performance on AIME 2024.\n\n## SEC Paper (arXiv 2505.14970)\n\nThe paper proposes Self-Evolving Curriculum (SEC), an automatic curriculum learning method that learns a curriculum policy concurrently with the RL fine-tuning process. The approach formulates curriculum selection as a non-stationary Multi-Armed Bandit problem, treating each problem category (e.g., difficulty level or problem type) as an individual arm.\n\nAcross three distinct reasoning domains: planning, inductive reasoning, and mathematics, the experiments demonstrate that SEC significantly improves models' reasoning capabilities, enabling better generalization to harder, out-of-distribution test problems.\n\n## Qwen2.5-7B Performance on AIME 2024\n\nRegarding the 17.5% result you mentioned, Qwen2.5-Math-72B-Instruct outperforms GPT-4o by an impressive 17.5 points (this refers to a performance margin, not the 7B model's absolute score). \n\nFor the base Qwen2.5-7B model: the original Qwen-2.5-7B-Instruct model achieves 16.67% on AIME 2024, which is close to the 17.5% figure you mentioned. However, I was unable to find specific documentation linking the exact 17.5% result directly to results from the SEC paper in the search results."
    ],
    "durationSeconds": 10.547197687000008,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "5a91490a-61b8-4ba6-a9a7-71c8d66e5d3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "035f8cef-a4b3-4776-903f-a71cee2cc14f",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Assistant

_source line 53 · 2026-05-28T03:07:06.968Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get more details on SEC, especially the AIME 2024 scores and what model they use. Also need to look at the SEC paper's HTML version and IndiMathBench HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "035f8cef-a4b3-4776-903f-a71cee2cc14f",
  "isSidechain": false,
  "requestId": "req_011CbUEE7pz523AVz14kWPnp",
  "type": "assistant",
  "uuid": "2a18711b-c5cf-4e41-b58e-b446d4b9eece",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PhJwEaYQdpgyXgkRgxNXY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1505,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 33782,
      "output_tokens": 535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1571,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1505,
          "output_tokens": 535,
          "cache_read_input_tokens": 33782,
          "cache_creation_input_tokens": 1571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1571
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

_source line 54 · 2026-05-28T03:07:10.242Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018Rj9F1Yh89yLaomLWEHhQf`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.14970v3",
  "prompt": "Extract: (1) ALL AIME 2024 results and math benchmark results, (2) ALL base models used (especially any 7B model), (3) the exact MAB formulation - what are the arms/categories, (4) the dataset/problem pool used, (5) TD(0) update mechanism details, (6) comparison tables with all baselines, (7) any multi-domain results. I need all exact numbers from the paper's result tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a18711b-c5cf-4e41-b58e-b446d4b9eece",
  "isSidechain": false,
  "requestId": "req_011CbUEE7pz523AVz14kWPnp",
  "type": "assistant",
  "uuid": "3b8c1dd1-4e4d-4723-bf17-966a5fe8e9d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PhJwEaYQdpgyXgkRgxNXY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1505,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 33782,
      "output_tokens": 535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1571,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1505,
          "output_tokens": 535,
          "cache_read_input_tokens": 33782,
          "cache_creation_input_tokens": 1571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1571
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

_source line 55 · 2026-05-28T03:07:13.027Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K1MkrbDiiudiq6gCH75tDY`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.00997",
  "prompt": "Extract the exact per-topic success rates for geometry vs other topics (algebra, number theory, combinatorics). I need: (1) the exact BEq numbers per topic, (2) the total problems per topic, (3) the compilation success rates per topic, (4) any discussion of why geometry is harder - is it Mathlib-specific or inherent mathematical difficulty? (5) Any tables showing per-category breakdowns. Look for Table 3 or any per-topic breakdown tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b8c1dd1-4e4d-4723-bf17-966a5fe8e9d5",
  "isSidechain": false,
  "requestId": "req_011CbUEE7pz523AVz14kWPnp",
  "type": "assistant",
  "uuid": "e95d8200-0abc-4e1a-a3a1-0e93af6e5410",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PhJwEaYQdpgyXgkRgxNXY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1505,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 33782,
      "output_tokens": 535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1571,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1505,
          "output_tokens": 535,
          "cache_read_input_tokens": 33782,
          "cache_creation_input_tokens": 1571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1571
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

_source line 56 · 2026-05-28T03:07:14.374Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xh3sa6Y1WYmzYCzDouFd5Z`</summary>

```json
{
  "url": "https://www.emergentmind.com/papers/2505.14970",
  "prompt": "Extract all numerical results from the SEC paper, especially: AIME 2024 scores, MATH-500 scores, base model used, MAB arm definitions, and comparisons to baselines. Look for tables with exact numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e95d8200-0abc-4e1a-a3a1-0e93af6e5410",
  "isSidechain": false,
  "requestId": "req_011CbUEE7pz523AVz14kWPnp",
  "type": "assistant",
  "uuid": "c42350c4-6bf8-42bc-9e54-834d00ebc46b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PhJwEaYQdpgyXgkRgxNXY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1505,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 33782,
      "output_tokens": 535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1571,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1505,
          "output_tokens": 535,
          "cache_read_input_tokens": 33782,
          "cache_creation_input_tokens": 1571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1571
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

_source line 57 · 2026-05-28T03:07:18.935Z_

<details><summary>↩ Tool result · `toolu_01Xh3sa6Y1WYmzYCzDouFd5Z`</summary>

```text
# Numerical Results from SEC Paper

Based on the provided webpage content, here are the extracted numerical findings:

## Key Performance Gains

The document reports that SEC achieved "significant relative accuracy gains over random baselines" on out-of-distribution test sets:

- **Countdown (3B model):** +13% relative gain
- **Zebra (3B model):** +21% relative gain
- **AIME24 (3B model):** +33% relative gain

## Model Architecture

The experiments utilized two Qwen models for evaluation:
- Qwen2.5-3B
- Qwen2.5-7B

## MAB Framework Structure

The curriculum policy treats "each problem category (e.g., difficulty level or problem type) as an individual arm" in a non-stationary Multi-Armed Bandit setup. Categories could be defined by difficulty levels, problem types, or combinations thereof for multi-task scenarios.

## Baseline Comparisons

SEC was compared against:
- Random curricula
- Fixed difficulty-ordered curricula
- Standard sampling approaches

## Limitation

The webpage content does not include specific MATH-500 scores or detailed numerical tables with exact baseline comparisons. The summary focuses on relative improvements rather than absolute performance metrics across all benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c42350c4-6bf8-42bc-9e54-834d00ebc46b",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "59faf219-b1e4-4d6a-b440-bb87a64ad25d",
  "toolUseResult": {
    "bytes": 244298,
    "code": 200,
    "codeText": "OK",
    "result": "# Numerical Results from SEC Paper\n\nBased on the provided webpage content, here are the extracted numerical findings:\n\n## Key Performance Gains\n\nThe document reports that SEC achieved \"significant relative accuracy gains over random baselines\" on out-of-distribution test sets:\n\n- **Countdown (3B model):** +13% relative gain\n- **Zebra (3B model):** +21% relative gain\n- **AIME24 (3B model):** +33% relative gain\n\n## Model Architecture\n\nThe experiments utilized two Qwen models for evaluation:\n- Qwen2.5-3B\n- Qwen2.5-7B\n\n## MAB Framework Structure\n\nThe curriculum policy treats \"each problem category (e.g., difficulty level or problem type) as an individual arm\" in a non-stationary Multi-Armed Bandit setup. Categories could be defined by difficulty levels, problem types, or combinations thereof for multi-task scenarios.\n\n## Baseline Comparisons\n\nSEC was compared against:\n- Random curricula\n- Fixed difficulty-ordered curricula\n- Standard sampling approaches\n\n## Limitation\n\nThe webpage content does not include specific MATH-500 scores or detailed numerical tables with exact baseline comparisons. The summary focuses on relative improvements rather than absolute performance metrics across all benchmarks.",
    "durationMs": 4558,
    "url": "https://www.emergentmind.com/papers/2505.14970"
  },
  "sourceToolAssistantUUID": "c42350c4-6bf8-42bc-9e54-834d00ebc46b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-28T03:07:18.981Z_

<details><summary>↩ Tool result · `toolu_018Rj9F1Yh89yLaomLWEHhQf`</summary>

```text
# SEC: Self-Evolving Curriculum for LLM Reasoning - Key Findings

## AIME 2024 & Math Results
From Table 1, Qwen2.5-7B with SEC achieved **0.175** on AIME24, representing a **27% relative improvement** over random (0.138). Additional math benchmarks: MATH500 (0.761), AMC22-23 (0.511).

## Base Models
The study employed **Qwen2.5-3B and Qwen2.5-7B** as the primary models, both fine-tuned using the GRPO algorithm.

## MAB Formulation
The framework treats curriculum selection as a non-stationary Multi-Armed Bandit problem where "each arm represents a problem category." Categories include difficulty levels or problem types. The curriculum policy samples from categories using a Boltzmann distribution: "p(c) = e^(Q_t(c)/τ) / Σe^(Q_t(c_i)/τ)".

## Problem Pool
Training utilized three primary domains:
- **Planning**: Countdown (3-6 integers) and Zebra puzzles (3-6 entities)
- **Inductive Reasoning**: ARC-1D (string lengths 10, 20, 30, 40)
- **Mathematics**: MATH dataset with 5 difficulty levels; evaluation on MATH500, AMC22-23, AIME24

Each domain included 10,000 training problems across three difficulty levels, with the hardest level reserved as OOD evaluation.

## TD(0) Update Mechanism
Updates follow: "Q_{t+1}(c) = α·r_t(c) + (1-α)·Q_t(c)" where rewards derive from average absolute advantage across rollouts in each category. Hyperparameters varied by task (α ∈ {0.2, 0.5}, τ ∈ {0.2, 1.0}).

## Comprehensive Baselines
Table 1 compares SEC against Random and Ordered curricula across all tasks. Notable improvements: Countdown OOD (13% relative), Zebra OOD (21% relative), ARC-1D OOD (22% relative).

## Multi-Domain Results
SEC-2D (combining Countdown, Zebra, ARC with 9 arms) outperformed random curriculum across all three tasks simultaneously, demonstrating stable multi-task learning without performance collapse.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b8c1dd1-4e4d-4723-bf17-966a5fe8e9d5",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "510ec29e-b65e-46cb-b8bf-c4dffc03ffac",
  "toolUseResult": {
    "bytes": 226437,
    "code": 200,
    "codeText": "OK",
    "result": "# SEC: Self-Evolving Curriculum for LLM Reasoning - Key Findings\n\n## AIME 2024 & Math Results\nFrom Table 1, Qwen2.5-7B with SEC achieved **0.175** on AIME24, representing a **27% relative improvement** over random (0.138). Additional math benchmarks: MATH500 (0.761), AMC22-23 (0.511).\n\n## Base Models\nThe study employed **Qwen2.5-3B and Qwen2.5-7B** as the primary models, both fine-tuned using the GRPO algorithm.\n\n## MAB Formulation\nThe framework treats curriculum selection as a non-stationary Multi-Armed Bandit problem where \"each arm represents a problem category.\" Categories include difficulty levels or problem types. The curriculum policy samples from categories using a Boltzmann distribution: \"p(c) = e^(Q_t(c)/τ) / Σe^(Q_t(c_i)/τ)\".\n\n## Problem Pool\nTraining utilized three primary domains:\n- **Planning**: Countdown (3-6 integers) and Zebra puzzles (3-6 entities)\n- **Inductive Reasoning**: ARC-1D (string lengths 10, 20, 30, 40)\n- **Mathematics**: MATH dataset with 5 difficulty levels; evaluation on MATH500, AMC22-23, AIME24\n\nEach domain included 10,000 training problems across three difficulty levels, with the hardest level reserved as OOD evaluation.\n\n## TD(0) Update Mechanism\nUpdates follow: \"Q_{t+1}(c) = α·r_t(c) + (1-α)·Q_t(c)\" where rewards derive from average absolute advantage across rollouts in each category. Hyperparameters varied by task (α ∈ {0.2, 0.5}, τ ∈ {0.2, 1.0}).\n\n## Comprehensive Baselines\nTable 1 compares SEC against Random and Ordered curricula across all tasks. Notable improvements: Countdown OOD (13% relative), Zebra OOD (21% relative), ARC-1D OOD (22% relative).\n\n## Multi-Domain Results\nSEC-2D (combining Countdown, Zebra, ARC with 9 arms) outperformed random curriculum across all three tasks simultaneously, demonstrating stable multi-task learning without performance collapse.",
    "durationMs": 8735,
    "url": "https://arxiv.org/html/2505.14970v3"
  },
  "sourceToolAssistantUUID": "3b8c1dd1-4e4d-4723-bf17-966a5fe8e9d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-28T03:07:19.880Z_

<details><summary>↩ Tool result · `toolu_01K1MkrbDiiudiq6gCH75tDY`</summary>

```text
# Geometry Performance Analysis from IndiMathBench

## Per-Topic Success Rates

The paper provides **limited explicit per-topic BEq breakdowns**. Here's what can be extracted:

**Overall Dataset Distribution (Table 1):**
- Geometry: 98 problems
- Algebra: 92 problems
- Number Theory: 77 problems
- Set Theory & Combinatorics: 45 problems
- **Total: 312 problems**

**Key Geometry Finding:**
Among the top three models (Claude Opus 4, Gemini 2.5 Pro, GPT-5) achieving 108 cumulative BEq successes, only 12 originated from geometry problems. This represents approximately **11% geometry success vs. 89% other domains**.

## Why Geometry Underperforms

**Mathlib-Specific Issues:**
The authors explicitly note that "Mathlib lacks many competition-level constructs" and identify "Mathlib's lacking support for Olympiad-style geometry" as a primary bottleneck.

**Cross-Cutting Pattern:**
The paper states: "Across all model families, geometry problems present the greatest formalization challenge," suggesting both library limitations and inherent modeling difficulties contribute to poor performance.

## Compilation Success Data

Table 2 shows **compilation validation success counts** for all models but **lacks topic-specific breakdowns**. The paper doesn't provide separate compilation rates disaggregated by mathematical domain.

The authors explicitly acknowledge this gap motivates their inclusion of underrepresented geometry content—a weakness flagged in the broader formalization ecosystem.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e95d8200-0abc-4e1a-a3a1-0e93af6e5410",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "798fe4c0-fc16-4bf7-8050-8f7a735d9b85",
  "toolUseResult": {
    "bytes": 818673,
    "code": 200,
    "codeText": "OK",
    "result": "# Geometry Performance Analysis from IndiMathBench\n\n## Per-Topic Success Rates\n\nThe paper provides **limited explicit per-topic BEq breakdowns**. Here's what can be extracted:\n\n**Overall Dataset Distribution (Table 1):**\n- Geometry: 98 problems\n- Algebra: 92 problems\n- Number Theory: 77 problems\n- Set Theory & Combinatorics: 45 problems\n- **Total: 312 problems**\n\n**Key Geometry Finding:**\nAmong the top three models (Claude Opus 4, Gemini 2.5 Pro, GPT-5) achieving 108 cumulative BEq successes, only 12 originated from geometry problems. This represents approximately **11% geometry success vs. 89% other domains**.\n\n## Why Geometry Underperforms\n\n**Mathlib-Specific Issues:**\nThe authors explicitly note that \"Mathlib lacks many competition-level constructs\" and identify \"Mathlib's lacking support for Olympiad-style geometry\" as a primary bottleneck.\n\n**Cross-Cutting Pattern:**\nThe paper states: \"Across all model families, geometry problems present the greatest formalization challenge,\" suggesting both library limitations and inherent modeling difficulties contribute to poor performance.\n\n## Compilation Success Data\n\nTable 2 shows **compilation validation success counts** for all models but **lacks topic-specific breakdowns**. The paper doesn't provide separate compilation rates disaggregated by mathematical domain.\n\nThe authors explicitly acknowledge this gap motivates their inclusion of underrepresented geometry content—a weakness flagged in the broader formalization ecosystem.",
    "durationMs": 6850,
    "url": "https://arxiv.org/html/2512.00997"
  },
  "sourceToolAssistantUUID": "e95d8200-0abc-4e1a-a3a1-0e93af6e5410",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 60 · 2026-05-28T03:07:19.883Z_

```json
{
  "parentUuid": "798fe4c0-fc16-4bf7-8050-8f7a735d9b85",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3ef6767c-291a-46dc-b531-dbad568374d2",
  "timestamp": "2026-05-28T03:07:19.883Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 61 · 2026-05-28T03:08:12.492Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have solid information on all the key papers. Let me also look for UCPO and Vocabulary Dropout details more carefully.

Let me now summarize what I've learned:

**SEC (arXiv 2505.14970)**:
- MAB over problem categories during GRPO training
- Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random at 13.8%)
- Uses MATH dataset pool of 10K problems


- Implements TD(0) updates to track category rewards, then samples from categories using Boltzmann distribution across difficulty levels and problem types from a fixed pool

**Actor-Curator (arXiv 2602.20532)**:
- Neural curator with regret guarantees
- Qwen2.5-3B: 30.0% AIME 2024 (+28.6% relative)
- Notably uses the smaller 3B model rather than 7B like SEC does
- Selects from 12K MATH problems with ~9% overhead
- Uses OSMD updates with negative-entropy regularization for O(T^(2/3) · V_T^(1/3)) regret bounds

There's a discrepancy I'm noticing: SEC achieves 17.5% on Qwen2.5-7B according to the paper, but Actor-Curator reports 20.0% on their own 3B implementation, so these are measuring different model sizes.

Now looking at another approach with online difficulty filtering that balances the filtering objective around p(x)=0.5 to maximize policy improvement, gaining +12% on AMC and +10% on AIME while cutting training steps in half across both 3B and 7B variants.

There's also UCPO which applies a conditional uniformity penalty during policy optimization to boost diversity at the equation level, showing +10% absolute improvement on AIME24 at Pass@64 across the 1.5B to 7B range. Vocabulary dropout takes a simpler route by randomly masking logits in the proposer to prevent diversity collapse, yielding +4.4 points on competition benchmarks for the 8B model. Finally, SOAR uses a bi-level meta-RL setup with a teacher-student framework on Llama-3.2-3B-Instruct, targeting the fail@128 regime.

SOAR recovers 75% of oracle gains on problems with zero initial success, achieving +9.3% pass@32 on MATH fail@128 and +6% transfer to OlympiadBench, with the key insight being that structural quality matters more than solution correctness. I'm also looking at IndiMathBench, which breaks down 312 problems across geometry, algebra, number theory, and combinatorics—the data shows a stark disparity where geometry problems are solved at only 12.2% compared to 44.9% for non-geometry, roughly a 3.7× gap that's partly attributed to Mathlib's limited support for Olympiad-style geometry constructions.

This geometry difficulty is really a formalization problem rather than a fundamental issue with problem synthesis itself. Now I'm thinking through how to structure the revision strategically: SEC and Actor-Curator are the most important additions since they select from fixed pools while SACE-RLVR synthesizes for identified gaps, and I could position Actor-Curator as a complementary baseline that samples from the archive rather than competing with it. The archive approach gives us interpretable coverage maps and lets us proactively identify gaps, which is a strong differentiator. I'll add Actor-Curator as baseline #8, adjust the IndiMathBench geometry estimates, and present the SAGE AIME results honestly.

For the landscape, I need to cite Online Difficulty Filtering as theoretical support since its p(1-p) result directly backs our Bayesian learnability framework, add UCPO as concurrent work at a different level of abstraction, and give brief mentions to Vocabulary Dropout and SOAR as lightweight alternatives and meta-RL approaches respectively. This is a major restructuring that integrates SEC and Actor-Curator throughout the baselines and differentiation sections, so I'll be careful to weave them in consistently while fixing the IndiMathBench numbers and SAGE presentation throughout.

Now I'm noticing something important about the Actor-Curator comparison—they achieve 30.0% on AIME24 with Qwen2.5-3B using just bandit selection from a fixed pool, whereas SEC gets 17.5% with the larger Qwen2.5-7B model. The key difference is that their fixed pool can't adapt as the policy evolves or fill coverage gaps through synthesis, but that actually makes the complementarity argument stronger—their bandit mechanism could serve as our sampling strategy from our dynamically built archive.

The real question the reviewer is asking is why persistent archives with synthesis beat principled bandit selection, and I think the answer hinges on three things: bandits exhaust their pools as the policy improves and fewer problems land in the zone of proximal development, they lack explicit coverage tracking so they risk converging to narrow high-utility subsets, and archives give us interpretability through their structure. We could even use Actor-Curator's bandit approach as the intra-archive sampling mechanism itself.

But the strongest case is simpler—for competition-level math, fixed pools like MATH's 12K problems have hard limits on coverage, and once the policy reaches competition level, the useful problems become sparse. That's where synthesis becomes essential, creating harder and more targeted problems that bandits alone can't provide.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ef6767c-291a-46dc-b531-dbad568374d2",
  "isSidechain": false,
  "requestId": "req_011CbUEFJGZzCvVjrP2Uck5j",
  "type": "assistant",
  "uuid": "4a4139f1-f574-4b85-a47c-ecb5f91f49a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3n5oHPcGPiBkkRkoePzNN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 35353,
      "output_tokens": 2360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 314,
          "output_tokens": 2360,
          "cache_read_input_tokens": 35353,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
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

_source line 62 · 2026-05-28T03:08:12.610Z_

Now let me search for a few more details to ensure accuracy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a4139f1-f574-4b85-a47c-ecb5f91f49a9",
  "isSidechain": false,
  "requestId": "req_011CbUEFJGZzCvVjrP2Uck5j",
  "type": "assistant",
  "uuid": "36a3a958-6443-4f74-9ca9-d071f108ba7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3n5oHPcGPiBkkRkoePzNN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 35353,
      "output_tokens": 2360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 314,
          "output_tokens": 2360,
          "cache_read_input_tokens": 35353,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
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

_source line 63 · 2026-05-28T03:08:15.831Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013UxNkXPDgT2B15yTE7NbrR`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.20532",
  "prompt": "I need to understand: (1) Does Actor-Curator use Qwen2.5-3B or Qwen2.5-7B for the main AIME 2024 result of 30.0%? (2) What is the SEC result in Actor-Curator's own comparison table - is it 20.0%? (3) What is the 'random' or 'uniform' baseline AIME24 result? (4) What exact pool sizes are used? (5) Does Actor-Curator synthesize new problems or only select from existing ones? (6) Any discussion of pool exhaustion or limitations of fixed pools? Look especially at experiment setup and limitation sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36a3a958-6443-4f74-9ca9-d071f108ba7f",
  "isSidechain": false,
  "requestId": "req_011CbUEFJGZzCvVjrP2Uck5j",
  "type": "assistant",
  "uuid": "92f1dd5f-0825-43b6-b1d5-20364eafccd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3n5oHPcGPiBkkRkoePzNN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 35353,
      "output_tokens": 2360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 314,
          "output_tokens": 2360,
          "cache_read_input_tokens": 35353,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
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

_source line 64 · 2026-05-28T03:08:16.404Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XEPoCjBJfxZZYsg7HUFVuY`</summary>

```json
{
  "query": "UCPO uniform correct policy optimization arXiv 2605.00365 pass@k diversity AIME 2024 exact results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92f1dd5f-0825-43b6-b1d5-20364eafccd0",
  "isSidechain": false,
  "requestId": "req_011CbUEFJGZzCvVjrP2Uck5j",
  "type": "assistant",
  "uuid": "2a315d22-e7b3-47e4-92e1-9fb66cddce6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3n5oHPcGPiBkkRkoePzNN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 314,
      "cache_creation_input_tokens": 3128,
      "cache_read_input_tokens": 35353,
      "output_tokens": 2360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3128,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 314,
          "output_tokens": 2360,
          "cache_read_input_tokens": 35353,
          "cache_creation_input_tokens": 3128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3128
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

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "2a315d22-e7b3-47e4-92e1-9fb66cddce6a",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Tool result

_source line 67 · 2026-05-28T03:08:21.300Z_

<details><summary>↩ Tool result · `toolu_013UxNkXPDgT2B15yTE7NbrR`</summary>

```text
# Actor-Curator AIME2024 Analysis

Based on the paper content provided, here are answers to your questions:

## 1. Model Size for AIME2024 Result
The paper states: "the actor is trained using GSPO, a stabilized variant of GRPO (Ahmadian et al., 2024), on Qwen2.5-3B." The 30.0% peak performance on AIME24 is achieved with **Qwen2.5-3B**, not 7B.

## 2. SEC Baseline Result
Yes, Table 1 shows SEC achieves **20.0%** on AIME24, while Actor-Curator reaches 30.0%, representing a relative gain of 28.6%.

## 3. Uniform Baseline Result
Table 1 lists "Uniform" as achieving **23.33%** on AIME24, compared to Actor-Curator's 30.0%.

## 4. Pool Sizes
The paper specifies: "We train on 30K problems for Countdown, Zebra, and ARC-1D, and 12K MATH problems for MATH500 and AIME24."

## 5. Problem Synthesis vs. Selection
Actor-Curator only performs **selection**, not synthesis. The method "learns to adaptively curate training problems" from existing problem banks through "adaptive problem selection."

## 6. Pool Exhaustion Limitations
The limitations section does not explicitly discuss pool exhaustion or fixed-pool constraints. The paper emphasizes that "Actor-Curator is agnostic to the specific actor update rule" but notes that gains depend on "stability and quality of the underlying actor optimization."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92f1dd5f-0825-43b6-b1d5-20364eafccd0",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "7442e7d1-6b2e-4794-94bf-9aebb94a69b6",
  "toolUseResult": {
    "bytes": 678399,
    "code": 200,
    "codeText": "OK",
    "result": "# Actor-Curator AIME2024 Analysis\n\nBased on the paper content provided, here are answers to your questions:\n\n## 1. Model Size for AIME2024 Result\nThe paper states: \"the actor is trained using GSPO, a stabilized variant of GRPO (Ahmadian et al., 2024), on Qwen2.5-3B.\" The 30.0% peak performance on AIME24 is achieved with **Qwen2.5-3B**, not 7B.\n\n## 2. SEC Baseline Result\nYes, Table 1 shows SEC achieves **20.0%** on AIME24, while Actor-Curator reaches 30.0%, representing a relative gain of 28.6%.\n\n## 3. Uniform Baseline Result\nTable 1 lists \"Uniform\" as achieving **23.33%** on AIME24, compared to Actor-Curator's 30.0%.\n\n## 4. Pool Sizes\nThe paper specifies: \"We train on 30K problems for Countdown, Zebra, and ARC-1D, and 12K MATH problems for MATH500 and AIME24.\"\n\n## 5. Problem Synthesis vs. Selection\nActor-Curator only performs **selection**, not synthesis. The method \"learns to adaptively curate training problems\" from existing problem banks through \"adaptive problem selection.\"\n\n## 6. Pool Exhaustion Limitations\nThe limitations section does not explicitly discuss pool exhaustion or fixed-pool constraints. The paper emphasizes that \"Actor-Curator is agnostic to the specific actor update rule\" but notes that gains depend on \"stability and quality of the underlying actor optimization.\"",
    "durationMs": 5463,
    "url": "https://arxiv.org/html/2602.20532"
  },
  "sourceToolAssistantUUID": "92f1dd5f-0825-43b6-b1d5-20364eafccd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-28T03:08:24.558Z_

<details><summary>↩ Tool result · `toolu_01XEPoCjBJfxZZYsg7HUFVuY`</summary>

```text
Web search results for query: "UCPO uniform correct policy optimization arXiv 2605.00365 pass@k diversity AIME 2024 exact results"

Links: [{"title":"[2605.00365] Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity","url":"https://arxiv.org/abs/2605.00365"},{"title":"Uniform-Correct Policy Optimization: Breaking RLVR’s Indifference to Diversity","url":"https://arxiv.org/html/2605.00365"},{"title":"UCPO: Uncertainty-Aware Policy Optimization","url":"https://arxiv.org/html/2601.22648"},{"title":"Breaking Winner-Takes-All: Cooperative Policy Optimization Improves Diverse LLM Reasoning","url":"https://arxiv.org/html/2605.11461"},{"title":"[2601.22648] UCPO: Uncertainty-Aware Policy Optimization","url":"https://arxiv.org/abs/2601.22648"},{"title":"Pass@K Policy Optimization: Solving Harder Reinforcement Learning Problems","url":"https://arxiv.org/pdf/2505.15201"},{"title":"Anchored Policy Optimization: Mitigating Exploration Collapse via Support-Constrained Rectification","url":"https://arxiv.org/html/2602.05717"},{"title":"Why Pass@k Optimization Can Degrade Pass@1: Prompt Interference in LLM Post-training","url":"https://arxiv.org/pdf/2602.21189"}]

I found the research paper for you. Here are the key details about the UCPO (Uniform-Correct Policy Optimization) paper from arXiv 2605.00365:

## Overview

UCPO is a modification to GRPO that adds a conditional uniformity penalty on the policy's distribution over correct solutions. The penalty redistributes gradient signal toward underrepresented correct responses, encouraging uniform allocation of probability mass within the correct set.

## Pass@K and Diversity Results

Across three models (1.5B-7B parameters) and five mathematical reasoning benchmarks, UCPO improves Pass@K and diversity while maintaining competitive Pass@1, achieving up to +10% absolute improvement on AIME24 at Pass@64 and up to 45% higher equation-level diversity within the correct set.

## Experimental Setup

The researchers trained on 10K competition-style math problems from the DeepScaleR corpus with 500 reserved for validation, and evaluated on three models: DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B, and Qwen2.5-7B.

The paper addresses the problem of diversity collapse in reinforcement learning approaches to mathematical reasoning, proposing a theoretically motivated solution that balances both robustness and entropy-regularized optimality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a315d22-e7b3-47e4-92e1-9fb66cddce6a",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "7aa49fa4-3704-49aa-96e2-717840d40cf8",
  "toolUseResult": {
    "query": "UCPO uniform correct policy optimization arXiv 2605.00365 pass@k diversity AIME 2024 exact results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BGQ9KPq4N1gr6yRcD8o27A",
        "content": [
          {
            "title": "[2605.00365] Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity",
            "url": "https://arxiv.org/abs/2605.00365"
          },
          {
            "title": "Uniform-Correct Policy Optimization: Breaking RLVR’s Indifference to Diversity",
            "url": "https://arxiv.org/html/2605.00365"
          },
          {
            "title": "UCPO: Uncertainty-Aware Policy Optimization",
            "url": "https://arxiv.org/html/2601.22648"
          },
          {
            "title": "Breaking Winner-Takes-All: Cooperative Policy Optimization Improves Diverse LLM Reasoning",
            "url": "https://arxiv.org/html/2605.11461"
          },
          {
            "title": "[2601.22648] UCPO: Uncertainty-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2601.22648"
          },
          {
            "title": "Pass@K Policy Optimization: Solving Harder Reinforcement Learning Problems",
            "url": "https://arxiv.org/pdf/2505.15201"
          },
          {
            "title": "Anchored Policy Optimization: Mitigating Exploration Collapse via Support-Constrained Rectification",
            "url": "https://arxiv.org/html/2602.05717"
          },
          {
            "title": "Why Pass@k Optimization Can Degrade Pass@1: Prompt Interference in LLM Post-training",
            "url": "https://arxiv.org/pdf/2602.21189"
          }
        ]
      },
      "I found the research paper for you. Here are the key details about the UCPO (Uniform-Correct Policy Optimization) paper from arXiv 2605.00365:\n\n## Overview\n\nUCPO is a modification to GRPO that adds a conditional uniformity penalty on the policy's distribution over correct solutions. The penalty redistributes gradient signal toward underrepresented correct responses, encouraging uniform allocation of probability mass within the correct set.\n\n## Pass@K and Diversity Results\n\nAcross three models (1.5B-7B parameters) and five mathematical reasoning benchmarks, UCPO improves Pass@K and diversity while maintaining competitive Pass@1, achieving up to +10% absolute improvement on AIME24 at Pass@64 and up to 45% higher equation-level diversity within the correct set.\n\n## Experimental Setup\n\nThe researchers trained on 10K competition-style math problems from the DeepScaleR corpus with 500 reserved for validation, and evaluated on three models: DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-Qwen-7B, and Qwen2.5-7B.\n\nThe paper addresses the problem of diversity collapse in reinforcement learning approaches to mathematical reasoning, proposing a theoretically motivated solution that balances both robustness and entropy-regularized optimality."
    ],
    "durationSeconds": 8.151059502999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2a315d22-e7b3-47e4-92e1-9fb66cddce6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-28T03:08:27.175Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the exact UCPO numbers and check if there are any more details I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aa49fa4-3704-49aa-96e2-717840d40cf8",
  "isSidechain": false,
  "requestId": "req_011CbUEL4p5TtupTLaLeVNVC",
  "type": "assistant",
  "uuid": "6dd5209d-ad48-49b1-954f-35909182bd04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rtn7C885zzCjjNGEjdpe3Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3832,
      "cache_read_input_tokens": 38481,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 366,
          "cache_read_input_tokens": 38481,
          "cache_creation_input_tokens": 3832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3832
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

_source line 70 · 2026-05-28T03:08:30.012Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MrGfeoJfp3zur9MP9YSZ14`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00365",
  "prompt": "Extract: (1) exact Pass@1 and Pass@K results for all models on AIME 2024 and other benchmarks - need tables with numbers, (2) the exact conditional uniformity penalty formulation, (3) comparison to GRPO baseline, (4) does UCPO modify training data distribution or just the loss function? (5) any discussion of complementarity with curriculum/archive methods. Include all numerical results from tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dd5209d-ad48-49b1-954f-35909182bd04",
  "isSidechain": false,
  "requestId": "req_011CbUEL4p5TtupTLaLeVNVC",
  "type": "assistant",
  "uuid": "eb1cb786-5f0e-4a89-bff0-42476d84d677",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rtn7C885zzCjjNGEjdpe3Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3832,
      "cache_read_input_tokens": 38481,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 366,
          "cache_read_input_tokens": 38481,
          "cache_creation_input_tokens": 3832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3832
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

_source line 71 · 2026-05-28T03:08:32.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0138FUL3iYLXKMBejMFYAsem`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03472",
  "prompt": "Extract: (1) exact benchmark results - AIME 2024/2025, MATH-500, and other competition results with numbers, (2) the specific mechanism of vocabulary dropout (logit masking details), (3) base models used, (4) comparison to R-Zero baseline, (5) is this modifying the proposer's generation diversity or the solver's training distribution? Include all numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb1cb786-5f0e-4a89-bff0-42476d84d677",
  "isSidechain": false,
  "requestId": "req_011CbUEL4p5TtupTLaLeVNVC",
  "type": "assistant",
  "uuid": "dcb6e604-4c1d-45d0-9034-efb9c7252d44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rtn7C885zzCjjNGEjdpe3Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3832,
      "cache_read_input_tokens": 38481,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 366,
          "cache_read_input_tokens": 38481,
          "cache_creation_input_tokens": 3832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3832
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

_source line 72 · 2026-05-28T03:08:38.885Z_

<details><summary>↩ Tool result · `toolu_01MrGfeoJfp3zur9MP9YSZ14`</summary>

```text
# UCPO Paper: Key Findings

## 1. Pass@1 and Pass@K Results

**AIME 2024 Performance:**
- DeepSeek-1.5B: GRPO 19.06% → UCPO 19.01% (Pass@1); GRPO 63.33% → UCPO 66.67% (Pass@64)
- DeepSeek-7B: GRPO 27.71% → UCPO 30.16% (Pass@1); GRPO 70.00% → UCPO 80.00% (Pass@64) — **+10% absolute gain**
- Qwen2.5-7B: GRPO 14.27% → UCPO 15.05% (Pass@1); GRPO 43.33% → UCPO 56.67% (Pass@64)

**Average across 5 benchmarks (Pass@64):**
- DeepSeek-1.5B: +3.5 points (78.27% vs 74.81%)
- DeepSeek-7B: +3.6 points (83.30% vs 79.69%)
- Qwen2.5-7B: +4.8 points (73.19% vs 68.37%)

## 2. Conditional Uniformity Penalty

The UCPO objective adds: `L_UCPO(θ) = log Z_θ(x) - τ·KL(u(·|x)‖q_θ(·|x))`

Where the penalty encourages the conditional distribution over correct outputs `q_θ(y|x)` to match the uniform distribution `u(y|x) = 1/|𝒴⁺(x)|` across verified solutions.

## 3. GRPO Comparison

UCPO preserves GRPO's total advantage budget but redistributes it: "UCPO preserves the total advantage mass assigned to correct rollouts and reallocates it towards underrepresented correct responses." Solutions with lower conditional probability receive larger gradient weights via inverse importance sampling.

## 4. Training Data Distribution

The paper **modifies only the loss function**, not the data distribution. UCPO: "introduces a single additional term" without changing rollout collection. Gradient reweighting (inverse-q importance weights) operates on the same verifier-accepted trajectories GRPO uses.

## 5. Complementarity with Curriculum/Archive Methods

The paper does not discuss explicit complementarity with curriculum learning or archive-based methods. However, it positions UCPO as "complementary to" trajectory-level exploration methods: "These methods are complementary to UCPO as they expand the set of reasoning trajectories explored during training, while UCPO operates at the conditional-distribution level."

**Equation-level diversity gains:** +45% on AIME, +13% on MATH versus GRPO baseline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb1cb786-5f0e-4a89-bff0-42476d84d677",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "5b3acad9-4d65-421e-b4f3-0c23fe1af6c1",
  "toolUseResult": {
    "bytes": 729953,
    "code": 200,
    "codeText": "OK",
    "result": "# UCPO Paper: Key Findings\n\n## 1. Pass@1 and Pass@K Results\n\n**AIME 2024 Performance:**\n- DeepSeek-1.5B: GRPO 19.06% → UCPO 19.01% (Pass@1); GRPO 63.33% → UCPO 66.67% (Pass@64)\n- DeepSeek-7B: GRPO 27.71% → UCPO 30.16% (Pass@1); GRPO 70.00% → UCPO 80.00% (Pass@64) — **+10% absolute gain**\n- Qwen2.5-7B: GRPO 14.27% → UCPO 15.05% (Pass@1); GRPO 43.33% → UCPO 56.67% (Pass@64)\n\n**Average across 5 benchmarks (Pass@64):**\n- DeepSeek-1.5B: +3.5 points (78.27% vs 74.81%)\n- DeepSeek-7B: +3.6 points (83.30% vs 79.69%)\n- Qwen2.5-7B: +4.8 points (73.19% vs 68.37%)\n\n## 2. Conditional Uniformity Penalty\n\nThe UCPO objective adds: `L_UCPO(θ) = log Z_θ(x) - τ·KL(u(·|x)‖q_θ(·|x))`\n\nWhere the penalty encourages the conditional distribution over correct outputs `q_θ(y|x)` to match the uniform distribution `u(y|x) = 1/|𝒴⁺(x)|` across verified solutions.\n\n## 3. GRPO Comparison\n\nUCPO preserves GRPO's total advantage budget but redistributes it: \"UCPO preserves the total advantage mass assigned to correct rollouts and reallocates it towards underrepresented correct responses.\" Solutions with lower conditional probability receive larger gradient weights via inverse importance sampling.\n\n## 4. Training Data Distribution\n\nThe paper **modifies only the loss function**, not the data distribution. UCPO: \"introduces a single additional term\" without changing rollout collection. Gradient reweighting (inverse-q importance weights) operates on the same verifier-accepted trajectories GRPO uses.\n\n## 5. Complementarity with Curriculum/Archive Methods\n\nThe paper does not discuss explicit complementarity with curriculum learning or archive-based methods. However, it positions UCPO as \"complementary to\" trajectory-level exploration methods: \"These methods are complementary to UCPO as they expand the set of reasoning trajectories explored during training, while UCPO operates at the conditional-distribution level.\"\n\n**Equation-level diversity gains:** +45% on AIME, +13% on MATH versus GRPO baseline.",
    "durationMs": 8869,
    "url": "https://arxiv.org/html/2605.00365"
  },
  "sourceToolAssistantUUID": "eb1cb786-5f0e-4a89-bff0-42476d84d677",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-28T03:08:40.937Z_

<details><summary>↩ Tool result · `toolu_0138FUL3iYLXKMBejMFYAsem`</summary>

```text
# Vocabulary Dropout for LLM Co-Evolution: Key Findings

## Benchmark Results (Qwen3-8B, Table 1)

| Benchmark | Baseline | VD75 | Improvement |
|-----------|----------|------|-------------|
| MATH500 | 69.9% | 68.1% | -1.8 |
| GSM8K | 86.9% | 88.6% | +1.7 |
| AMC | 40.8% | 51.7% | **+10.9** |
| Olympiad | 23.1% | 27.7% | **+4.6** |
| AIME 2024 | 12.2% | 15.6% | **+3.4** |
| AIME 2025 | 3.3% | 11.1% | **+7.8** |
| **Average** | 39.4% | 43.8% | **+4.4** |

## Mechanism: Hard Logit Masking

Vocabulary dropout applies a "hard and non-stationary mask" to the proposer's output logits. At each batch, tokens outside a protected format set are randomly retained with probability α (tested at 0.75 and 0.85). Masked tokens receive logits of −∞, preventing generation regardless of policy gradients. The mask resamples every batch, preventing convergence to fixed token sequences.

## Base Models & Architecture

- **Models**: Qwen3-4B-Base and Qwen3-8B-Base
- **Training method**: GRPO (Group Relative Policy Optimization)
- **Framework**: R-Zero co-evolutionary system (proposer generates problems; solver attempts them)

## Proposer vs. Solver Impact

"Vocabulary dropout (VD) is applied to the _proposer_ only, and the solver trains on the resulting curriculum." The intervention directly constrains the problem-generator's action space, not the solver's training distribution. This maintains curriculum diversity, preventing the proposer from converging to narrow problem templates within 1-2 iterations.

## Comparison to R-Zero Baseline

The baseline (α=1.0, full vocabulary) shows "functional collapse...almost entirely between iterations 1 and 2," with difficulty jumping from 0.50 to 0.86 at 4B. VD75 sustains diversity metrics across all five iterations, with epiplexity approximately 35% higher than baseline—indicating substantially more learnable curriculum structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcb6e604-4c1d-45d0-9034-efb9c7252d44",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "d10ea1fb-77ee-445d-80c5-65f7ed27b7ff",
  "toolUseResult": {
    "bytes": 683561,
    "code": 200,
    "codeText": "OK",
    "result": "# Vocabulary Dropout for LLM Co-Evolution: Key Findings\n\n## Benchmark Results (Qwen3-8B, Table 1)\n\n| Benchmark | Baseline | VD75 | Improvement |\n|-----------|----------|------|-------------|\n| MATH500 | 69.9% | 68.1% | -1.8 |\n| GSM8K | 86.9% | 88.6% | +1.7 |\n| AMC | 40.8% | 51.7% | **+10.9** |\n| Olympiad | 23.1% | 27.7% | **+4.6** |\n| AIME 2024 | 12.2% | 15.6% | **+3.4** |\n| AIME 2025 | 3.3% | 11.1% | **+7.8** |\n| **Average** | 39.4% | 43.8% | **+4.4** |\n\n## Mechanism: Hard Logit Masking\n\nVocabulary dropout applies a \"hard and non-stationary mask\" to the proposer's output logits. At each batch, tokens outside a protected format set are randomly retained with probability α (tested at 0.75 and 0.85). Masked tokens receive logits of −∞, preventing generation regardless of policy gradients. The mask resamples every batch, preventing convergence to fixed token sequences.\n\n## Base Models & Architecture\n\n- **Models**: Qwen3-4B-Base and Qwen3-8B-Base\n- **Training method**: GRPO (Group Relative Policy Optimization)\n- **Framework**: R-Zero co-evolutionary system (proposer generates problems; solver attempts them)\n\n## Proposer vs. Solver Impact\n\n\"Vocabulary dropout (VD) is applied to the _proposer_ only, and the solver trains on the resulting curriculum.\" The intervention directly constrains the problem-generator's action space, not the solver's training distribution. This maintains curriculum diversity, preventing the proposer from converging to narrow problem templates within 1-2 iterations.\n\n## Comparison to R-Zero Baseline\n\nThe baseline (α=1.0, full vocabulary) shows \"functional collapse...almost entirely between iterations 1 and 2,\" with difficulty jumping from 0.50 to 0.86 at 4B. VD75 sustains diversity metrics across all five iterations, with epiplexity approximately 35% higher than baseline—indicating substantially more learnable curriculum structure.",
    "durationMs": 8723,
    "url": "https://arxiv.org/html/2604.03472"
  },
  "sourceToolAssistantUUID": "dcb6e604-4c1d-45d0-9034-efb9c7252d44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-28T03:12:30.067Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me carefully construct the revised proposal. Here's my plan:

**Key changes:**

1. **SEC + Actor-Curator** (CRITICAL): Add to landscape, add Actor-Curator as 8th baseline, argue for complementarity and synthesis advantage
2. **IndiMathBench**: Fix ~3.7× ratio, note formalization context
3. **SAGE AIME**: Honest presentation (matches base, degrades AMC)
4. **Online Difficulty Filtering**: Cite as theoretical support


5. **UCPO**: Add as concurrent work
6. **Vocabulary Dropout**: Brief mention
7. **SOAR**: Brief mention

The core argument is that synthesis-based archives outperform fixed-pool selection because pools like MATH with 12K problems hit a ceiling—as models improve toward competition level, the remaining useful problems become scarce. SEC and Actor-Curator show this limitation at 17.5% and 30.0% AIME24 respectively, but synthesis can fill those gaps by generating problems in under-populated niches like hard geometry.

Archives also track coverage evolution over time rather than optimizing myopically per step like bandits do. I should explicitly propose Actor-Curator's bandit as a within-archive sampling variant to show complementarity.

One thing to clarify: Actor-Curator's 30.0% is on Qwen2.5-3B while SEC's 17.5% is on Qwen2.5-7B, so they're not directly comparable across papers due to different model sizes. The real comparison is Actor-Curator at 30.0% versus SEC at 20.0%, both on Qwen2.5-3B.

The reviewer flagged that the score is stuck around 3.375 and needs to climb to pass, with SEC being the main blocker to address. Actor-Curator uses Qwen2.5-3B, not 7B, so that 30.0% AIME24 score is on the smaller model. The SEC paper reports 17.5% on Qwen2.5-7B, but Actor-Curator's own reimplementation of SEC on 3B achieves 20.0%, which is interesting since the larger model performs worse—likely due to different training setups or implementation details. I'll stick with reporting the primary source numbers and flagging the model size differences.

Now I'm planning the full revision. I need to expand the core_problem to mention bandit-based approaches, weave the SEC and Actor-Curator performance gap into the opportunity section, and significantly restructure the landscape to include SEC, Actor-Curator, Online Difficulty Filtering, UCPO, Vocabulary Dropout, and SOAR. I'll add Actor-Curator as an eighth baseline in the approach section, correct the IndiMathBench and SAGE numbers, and consider whether to highlight Actor-Curator's complementarity as a potential extension. The key_references and description sections will need updates across the board.

For the approach section specifically, I'm fixing IndiMathBench to show the ~3.7× lower success rate with formalization context, correcting SAGE to 13.3% on AIME 2024 matching the base model while degrading AMC from 57.5% to 52.5%, and adding the Online Difficulty Filtering citation. The per-niche survival estimates for geometry need adjustment—the old 5-15% range was based on a 6-7× difficulty ratio, but the new 3.7× ratio suggests something closer to 8-20%, though I should be conservative since IndiMathBench's difficulty is about formalization rather than synthesis difficulty.

Now I'm finalizing the baseline comparisons. I have eight baselines lined up, with Actor-Curator as the new addition that captures bandit selection versus archive synthesis. SEC can stay in the landscape discussion since Actor-Curator already outperforms it. The reviewer's suggestion about using Actor-Curator as a sampling strategy from the archive is compelling for an extension—I'm thinking through how to structure that as E5.

Actually, I should probably reframe E4 instead of adding another ablation. Rather than just ZPD-weighted sampling, I could make it a broader comparison of archive sampling strategies: ZPD-weighted versus uniform versus Actor-Curator-style bandit selection. This directly addresses the complementarity point and keeps the ablations focused without overcomplicating things.

The key insight for responding to the reviewer is that fixed-pool bandit selection hits a ceiling—Actor-Curator works with 12K MATH problems, but at competition difficulty levels that coverage becomes limiting. Synthesis fills those gaps, and as the solver improves and exhausts the learning-zone problems in any fixed pool, synthesis keeps providing fresh, targeted examples. Bandits optimize immediate utility, but they can't generate new problems when the pool runs dry.

The empirical comparison is tricky though—Actor-Curator uses a 3B model hitting 30% on AIME24, while CLPO uses an 8B model reaching 50%, so the performance gap likely reflects both the method and the base model capacity rather than just the approach itself.

Now I'm drafting the full JSON revision. I also need to recalibrate the geometry difficulty claim—the original cited a 6-7× harder ratio from IndiMathBench, but that's measuring formalization difficulty in Lean 4, not synthesis difficulty. The actual success rate gap is closer to 3.7×, and that's specific to autoformalization. For synthesis, I should use more conservative estimates and distinguish between what IndiMathBench tells us about formalization versus what we actually know about problem generation difficulty.

Let me adjust the per-niche survival rates: geometry cells should move from 5-15% up to 10-25% since the 3.7× ratio is less extreme than the original 6-7× claim, while keeping the other categories stable and noting that geometry is genuinely harder but not to the degree initially suggested.

This cascades into lower overgeneration requirements—geometry cells now need 400-1000 candidates instead of 650-2000, bringing the total per refresh down to 2,300-5,500 from 2,900-7,000.

Now I'm organizing the blocking changes needed: adding SEC and Actor-Curator as related work plus Actor-Curator as the eighth baseline, fixing the IndiMathBench ratio to 3.7×, and correcting the geometry estimates accordingly.

For the strongly recommended changes, I need to cite Online Difficulty Filtering, add UCPO as concurrent work, and include Vocabulary Dropout and SOAR in that category as well.

Writing out the full JSON now—this is a major revision because I'm adding critical missing comparators that reshape the positioning, restructuring the landscape substantially, introducing a new baseline, and fixing factual errors. The core idea stays intact though.

I need to expand the landscape section with new subsections covering bandit-based adaptive curriculum and other related approaches.

For SEC, I'm looking at a May 2025 paper using multi-armed bandits over problem categories with TD(0) updates and Boltzmann sampling—Qwen2.5-7B achieves 17.5% on AIME24, a 27% relative improvement over random selection. It selects from the MATH dataset across difficulty and problem type categories, though it's limited to a fixed pool without synthesis or persistent archiving.

For Actor-Curator, there's a February 2026 paper with a neural curator using OSMD updates and regularization...

Actually, let me reconsider the Actor-Curator results. The regret bound is O(T^{2/3} V_T^{1/3}), and on Qwen2.5-3B it reaches 30.0% AIME24 with about 9% computational overhead—beating SEC's 20.0% on the same model size. It also selects from a fixed pool of 12K MATH problems but lacks synthesis capabilities.

The key distinction from SACE-RLVR is that both use adaptive selection and track per-problem utility, but SACE-RLVR adds synthesis and enforces structured 2D coverage through an archive, whereas bandit methods optimize aggregate utility. These approaches are complementary—the bandit could sample from the archive itself.

For Actor-Curator specifically, the 30.0% AIME24 result uses Qwen2.5-3B as the actor, and that +28.6% relative improvement is measured against SEC's 20.0% on the same 3B model, not the original SEC paper's 7B result of 17.5%.

Actually, let me recalculate: (30.0 - 23.33)/23.33 = 28.6%, so the relative improvement is actually over the uniform baseline at 23.33%, not SEC. And for SEC itself, the reviewer's claim of 17.5% on Qwen2.5-7B with +27% relative checks out when I verify against the random baseline of 13.8%.

Now I need to write out the full JSON response, making sure to add SEC and Actor-Curator to the inspired_by field, and incorporate Actor-Curator as baseline #8 while potentially reframing the E4 experiment to include a bandit-style sampling comparison.

For the baselines section, I'm expanding from 7 to 8 entries: DéjàQ-comp with 2D targeting, CLPO for persistence, Socratic-Zero for structured versus instance-level comparison, SAGE for structured versus flat, Actor-Curator as the new bandit selection versus archive synthesis baseline, EVOL-RL for stateless diversity, MathForge as the DGPO source, and vanilla GRPO as the minimal baseline. The ablations stay at 7 but I might adjust one of them.

I'm reconsidering whether to add another ablation or reframe E4 to test bandit-style sampling instead. A7 tests the important GRPO versus DGPO distinction tied to E3, so the current 7 ablations are already well-structured. Rather than overcomplicate things—the reviewer appreciated the clean 3+4 structure—I'll add Actor-Curator as baseline #8, discuss how it complements the approach, and note bandit-style archive sampling as a natural extension within E4's description.

Adding this baseline costs roughly 250 GPU-hours, bringing the total from 6,700 to around 6,950. Now I'm ready to write out the full JSON, focusing on thorough treatment of the critical changes like SEC and Actor-Curator, IndiMathBench, and SAGE, while being more concise elsewhere. I'll update the core problem to highlight bandit-based curriculum selection as an approach that adaptively selects from fixed pools without synthesis or structured coverage, then address that gap in the opportunity section and expand the landscape with SEC, Actor-Curator, Online Difficulty Filtering, UCPO, Vocabulary Dropout, and SOAR.

I'm reconsidering the geometry survival estimates more carefully. The original 6-7× harder claim came from IndiMathBench, but looking at the actual data—geometry at 12.2% BEq versus non-geometry at 44.9% BEq—that's only about a 3.7× ratio, and that's specifically for Lean 4 formalization, not problem synthesis. The paper attributes some of this to Mathlib's limited support for Olympiad-style geometry. For synthesis, geometry is genuinely harder because diagrams need to be consistent, numerical verification is trickier than algebra, and constraints must be internally coherent, but the 3.7× formalization ratio is a loose proxy at best. I should ground this in SPARQ and other synthesis data instead.

Looking at what's actually available: SPARQ reports ~25% overall QD survival without per-topic breakdowns, and DART-Math shows difficulty-based coverage loss rather than topic-based. So I'm settling on a more conservative estimate—maybe 2-3× harder than algebra rather than 6-7×, which would put geometry survival at roughly 10-20% if algebra is around 30-40%. This feels more honest about the uncertainty. With that, I can revise my per-niche estimates: easy-medium common topics need about 600-1,050 candidates across 30 cells, medium-hard common topics need 400-650 across 10 cells, and geometry cells across all difficulties would be around 10 cells.

For the extreme cells with very low or very high solve rates, I'm estimating 3-8% survival, which means needing 125-330 candidates per cell for a total of 1,250-3,300. That brings my overall estimate to roughly 2,750-6,000 candidates per refresh cycle, with generation costs staying in the 130-200 GPU-hour range. The revision is modest but more grounded in what the data actually shows. I'm going to use the stated 3.7× ratio as my baseline and work from there, distinguishing between easy-medium geometry at 15-25% survival and harder geometry at 5-10%. I'm recalibrating the geometry estimates based on the actual 3.7× ratio rather than the 6-7× figure, which means adjusting survival rates downward to around 10-20% for standard cells and 3-8% for extreme cases, with overgeneration targets of 50-100 per cell, bringing the total per refresh down to roughly 2,500-5,500. Now I need to write out the complete JSON with all the adjustments, but first I'm double-checking the reviewer's feedback about whether "adjust downward" means I should be reducing these numbers further given the less extreme ratio. downward, meaning fewer overgeneration candidates are needed since survival rates should actually be higher with the less extreme geometry difficulty. I'm settling on the logical interpretation: if geometry is genuinely 3.7× rather than 6-7×, then survival improves and synthesis costs decrease slightly. For the resource estimate, adding the Actor-Curator baseline pushes it to around 7,000 H100-hours, roughly in line with the original despite the adjustments. Now I'm structuring the full JSON proposal with all the required fields.

I need to update several sections to incorporate the new findings. The core problem should frame the gap that SEC and Actor-Curator leave open—selection from fixed pools without synthesis or structured coverage. The landscape section gets expanded with entries for SEC, Actor-Curator, online difficulty filtering, UCPO, vocabulary dropout, and SOAR, plus I'm correcting the SAGE AIME presentation. In the approach, I'm fixing the IndiMathBench ratio and geometry estimates, correcting SAGE, adding Actor-Curator as a baseline component, and noting how online difficulty filtering complements the work.

The key concern is that the proposal is already lengthy, so I need to be concise with these additions rather than expanding further. I think restructuring the landscape to make SEC and Actor-Curator a major integrated section makes sense since the reviewer emphasized them repeatedly—that way I can keep the other new entries brief and focused. er on the other additions.

Let me think about the landscape structure:
1. Online archive-based co-evolution (DéjàQ) - existing
2. **Bandit-based adaptive curriculum** (SEC, Actor-Curator) - NEW MAJOR
3. Online stateless curriculum (CLPO) - existing
4. Three-agent co-evolution (Socratic-Zero) - existing
5. Multi-agent self-evolution (SAGE) - existing, fix AIME
6. **Balanced difficulty filtering** (Online Difficulty Filtering) - NEW
7. Implicit curriculum theory - existing
8. Sparse policy selection & diversity - existing
9. Bidirectional curriculum generation - existing
10. Novelty-aware diversity (EVOL-RL) - existing
11. Difficulty-aware policy optimization (MathForge/DGPO) - existing
12. Reward variance (VCRL) - existing
13. Rollout count effects - existing
14. Synthesis survival rates - existing, fix IndiMathBench
15. Verification (VHG) - existing
16. **Policy-level diversity** (UCPO) - NEW
17. **Lightweight diversity alternatives** (Vocabulary Dropout) - NEW
18. **Meta-RL curriculum** (SOAR) - NEW
19. AIME landscape - existing
20. Weakness-driven synthesis - existing
21. Self-evolving RLVR - existing
22. The precise gap - existing, update

That's quite a lot to cover. I should consolidate some of these entries and keep descriptions concise. For the landscape section, I'll reorganize to group related approaches together more logically: starting with archive-based and bandit-driven methods, then moving through curriculum and diversity strategies, and finishing with synthesis and verification techniques. I'm realizing this outline is getting unwieldy, so I should focus the reviewer's main concern—SEC and Actor-Curator—into a substantial, detailed section while keeping the newer approaches (UCPO, Vocabulary Dropout, SOAR, Online Difficulty Filtering) as brief additions or short entries. Let me draft that now.

I should also verify a couple of details I'm uncertain about. The Actor-Curator overhead is confirmed at approximately 9% from the paper. For SEC's multi-armed bandit, I need to clarify whether it operates across difficulty and problem type dimensions separately or combined—the research shows it treats each category as an arm, with SEC-2D using 9 arms across domains, and for math problems it appears to use MATH's 5 categories.

So the key distinction is that SEC uses one-dimensional categories per domain, SACE-RLVR operates in a two-dimensional grid of difficulty and type, and Actor-Curator works at the individual problem level without categorical bucketing. These represent different granularities of how curriculum can be structured during training.

Now I'm ready to write the full revision with appropriate depth on the main topics and brevity elsewhere. Let me start drafting the JSON structure.

For the core problem section, I want to highlight how recent bandit-based approaches like SEC and Actor-Curator have shown strong empirical results on AIME benchmarks through adaptive curriculum selection, but they're fundamentally limited to choosing from existing problem pools rather than synthesizing new ones or systematically tracking coverage across multiple dimensions.

For the opportunities section, I'm adding a fifth point about how these bandit methods reveal both the promise and the ceiling of fixed-pool approaches—Actor-Curator gets impressive results on AIME but can't fill gaps it identifies or ensure balanced coverage across difficulty and topic space, suggesting that combining principled selection with synthesis could be the next frontier.

For the landscape section, I'm detailing how SEC uses a multi-armed bandit formulation where each problem category becomes an arm, updating Q-values through TD learning and sampling with Boltzmann exploration, though it's limited to one-dimensional categorization. Actor-Curator then extends this by moving from category-level to individual problem utility estimation.

Actor-Curator employs a small neural curator trained with online stochastic mirror descent to achieve a regret bound of O(T^{2/3}·V_T^{1/3}), and achieves notably stronger results on AIME and MATH benchmarks with only ~9% computational overhead. The key limitation I'm noting is that both methods select from fixed problem pools rather than generating new ones, so as the model improves, the utility of remaining problems in those pools diminishes—and Actor-Curator lacks explicit mechanisms for identifying and addressing specific capability gaps.

Where Actor-Curator and SACE-RLVR truly differ is that neither maintains a persistent archive with cross-step coverage tracking, yet these approaches could actually complement each other: the bandit selection strategy could work within a coverage-maintaining synthesis framework to combine principled selection with diversity guarantees.

For SAGE, the results reveal a critical failure mode—it matches the base Qwen-2.5-7B on AIME but actually degrades AMC performance while improving OlympiadBench, showing that unstructured pools can overfit to narrow in-distribution metrics at the expense of out-of-distribution generalization, which is exactly the curriculum drift that structured diversity maintenance prevents.

Online difficulty filtering theory shows that policy improvement is fundamentally bounded by task-level success variance, peaking when problems sit at 50% success rate. Balanced filtering in that sweet spot delivers substantial gains on both AMC and AIME with far fewer training steps, which directly validates our difficulty-aware approach and the Bayesian tracking mechanism we're using to monitor problem learnability.

UCPO tackles diversity collapse at the policy optimization level itself rather than just at the sampling stage.  It adds a conditional uniformity penalty that steers gradients toward underrepresented correct solutions, achieving significant Pass@64 improvements on AIME while preserving Pass@1 performance. Since UCPO modifies the loss function rather than the training distribution, it works orthogonally with archive-based diversity methods—UCPO maintains diversity within correct solutions while our approach ensures diversity across the problem space.

Vocabulary Dropout prevents diversity collapse in co-evolutionary problem generation by randomly masking logits during proposal, delivering measurable gains on Qwen3-8B with minimal computational overhead.

SOAR uses meta-RL where a teacher generates stepping-stone problems based on measured student improvement, recovering substantial oracle gains on hard tasks—conceptually similar to our gap identification but using meta-RL rewards instead of archive structure.

For IndiMathBench, I need to update the difficulty characterization from "6-7× harder" to reflect the ~3.7× lower autoformalization success rate throughout.

I'm also refining the geometry estimates upward to 10-20% survival and 3-8% extreme cases, accounting for Mathlib's formalization-specific limitations that may not fully translate to synthesis difficulty.

Adding Actor-Curator as a key baseline that uses fixed-pool bandit selection rather than archive-based synthesis with coverage guarantees, and clarifying the precise gaps: DéjàQ and GSM operate in 1D, SEC uses MAB over categories but remains 1D with fixed pools, Actor-Curator applies per-problem bandits without coverage tracking, CLPO uses stateless coarse bins, and Socratic-Zero is purely reactive.

Now I'm adjusting resource estimates upward by roughly 100-200 hours to account for the Actor-Curator baseline and slightly lower synthesis costs from revised geometry figures, then adding the recent references including SEC, Actor-Curator, Online Difficulty Filtering, UCPO, Vocabulary Dropout, and SOAR.

Writing the complete JSON...

Actually, I'm reconsidering E4—the reviewer suggested using Actor-Curator as a sampling strategy from the archive, which is compelling, but I need to decide whether to make this an explicit experiment or keep E4 simple and let the Actor-Curator baseline demonstrate the value. The bandit-style sampling variant could work as part of the baseline discussion rather than as a separate extension.

Let me revise E4 to directly test this: comparing ZPD-weighted sampling with posterior variance weighting against uniform sampling and Actor-Curator-style bandit sampling from the archive. This directly validates whether principled per-problem utility estimation improves further when constrained to a coverage-maintaining archive—exactly what the reviewer was asking about.

Looking at the existing ablations, I could swap out A6 or A7 for a dedicated bandit-versus-ZPD sampling test, but the reviewer already signed off on this structure. The cleaner move is keeping all seven ablations and reframing E4 to include the bandit variant as a comparison. Since baseline #8 already tests pure bandit versus pure archive, E4 becomes the test of whether combining them within the archive yields even better results.

Now I'm thinking through whether an eighth ablation is necessary. The reviewer approved "7 baselines, 7 ablations," so adding an eighth baseline is fine, but I don't think I need an eighth ablation—the Actor-Curator comparison handles that. The most compelling experiment would actually be a three-way comparison: Actor-Curator on a fixed pool, our system with ZPD sampling, and our system with Actor-Curator sampling. If our Actor-Curator variant outperforms our ZPD approach, which outperforms their fixed-pool version, that cleanly demonstrates both the archive's value and how our sampling strategy complements it.

If the Actor-Curator variant performs similarly to ZPD sampling but both beat their fixed-pool approach, that isolates the archive as the key differentiator. I'll frame this as a complementarity test within the Actor-Curator baseline rather than a separate ablation—something like testing whether principled selection from our coverage-maintaining archive outperforms both individual approaches.

Now I need to finalize the revision. The original proposal is already quite long, so adding SEC and Actor-Curator comparisons means I should trim some less critical existing content, particularly the detailed per-paper descriptions in the landscape section.

For the reviewer response, I'm documenting seven major changes: the SEC and Actor-Curator landscape additions with the complementarity argument, corrected IndiMathBench scaling with geometry context, honest framing of SAGE AIME results, Online Difficulty Filtering as theoretical support, UCPO as concurrent work, Vocabulary Dropout as a lightweight alternative, and SOAR as a concurrent meta-RL approach. I'll mark this as a major revision and now write out the complete JSON.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d10ea1fb-77ee-445d-80c5-65f7ed27b7ff",
  "isSidechain": false,
  "requestId": "req_011CbUEMGpvJGRgquUCQRXdH",
  "type": "assistant",
  "uuid": "ae77a77c-fd94-49dd-b2eb-523bcfde50b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011f8ELDnqrR7TNE36vdDfFV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 42313,
      "output_tokens": 10841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10841,
          "cache_read_input_tokens": 42313,
          "cache_creation_input_tokens": 1692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1692
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

_source line 75 · 2026-05-28T03:12:30.069Z_

Now I have all the information I need. Let me compile the comprehensive revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae77a77c-fd94-49dd-b2eb-523bcfde50b6",
  "isSidechain": false,
  "requestId": "req_011CbUEMGpvJGRgquUCQRXdH",
  "type": "assistant",
  "uuid": "745a4044-1b05-4964-adc7-faf7a646877b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011f8ELDnqrR7TNE36vdDfFV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 42313,
      "output_tokens": 10841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10841,
          "cache_read_input_tokens": 42313,
          "cache_creation_input_tokens": 1692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1692
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

_source line 76 · 2026-05-28T03:12:31.124Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017pH4y2UFKU6ierEfFheCev`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00365",
  "prompt": "I need the EXACT pass@1 results for AIME 2024 (not just pass@64). Specifically for Qwen2.5-7B under GRPO vs UCPO. Also, does the paper discuss any complementarity with data-level diversity methods (curriculum, archive-based approaches)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "745a4044-1b05-4964-adc7-faf7a646877b",
  "isSidechain": false,
  "requestId": "req_011CbUEMGpvJGRgquUCQRXdH",
  "type": "assistant",
  "uuid": "7c143d1a-34d4-46b4-ba8b-921d3d6ce46a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011f8ELDnqrR7TNE36vdDfFV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 42313,
      "output_tokens": 10841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10841,
          "cache_read_input_tokens": 42313,
          "cache_creation_input_tokens": 1692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1692
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

_source line 77 · 2026-05-28T03:12:32.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VAtFod2VLnNHmampW4SKFA`</summary>

```json
{
  "query": "SEC self-evolving curriculum LLM reasoning 2505.14970 MATH-500 AMC AIME detailed results table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c143d1a-34d4-46b4-ba8b-921d3d6ce46a",
  "isSidechain": false,
  "requestId": "req_011CbUEMGpvJGRgquUCQRXdH",
  "type": "assistant",
  "uuid": "9bf67e08-6981-490f-9043-29d764e3628a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011f8ELDnqrR7TNE36vdDfFV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 42313,
      "output_tokens": 10841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10841,
          "cache_read_input_tokens": 42313,
          "cache_creation_input_tokens": 1692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1692
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

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "9bf67e08-6981-490f-9043-29d764e3628a",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Tool result

_source line 80 · 2026-05-28T03:12:35.730Z_

<details><summary>↩ Tool result · `toolu_017pH4y2UFKU6ierEfFheCev`</summary>

```text
# AIME 2024 Pass@1 Results for Qwen2.5-7B

According to Table 1 in the paper:
- **GRPO**: 14.27% Pass@1
- **UCPO**: 15.05% Pass@1

This represents a modest improvement of +0.78 percentage points at Pass@1 while UCPO achieves substantially stronger gains at Pass@64 (43.33% vs 56.67%, a +13.34 point improvement).

## Complementarity with Data-Level Diversity Methods

The paper does **not discuss** explicit complementarity with curriculum learning or archive-based data approaches. However, it does note that diversity-promotion methods operate at different levels:

The authors acknowledge that "token-level methods preserve local stochasticity" and "trajectory-level exploration" methods "broaden exploration," characterizing UCPO as complementary since it "operates at the conditional-distribution level, reshaping how gradient mass is allocated among correct responses once they are sampled."

The focus remains on **within-episode gradient redistribution** rather than data-level curation, suggesting UCPO could potentially be combined with such approaches but this isn't empirically validated in the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c143d1a-34d4-46b4-ba8b-921d3d6ce46a",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "3d4cfc3e-36c3-4164-b1f1-e9ba13aef70e",
  "toolUseResult": {
    "bytes": 729953,
    "code": 200,
    "codeText": "OK",
    "result": "# AIME 2024 Pass@1 Results for Qwen2.5-7B\n\nAccording to Table 1 in the paper:\n- **GRPO**: 14.27% Pass@1\n- **UCPO**: 15.05% Pass@1\n\nThis represents a modest improvement of +0.78 percentage points at Pass@1 while UCPO achieves substantially stronger gains at Pass@64 (43.33% vs 56.67%, a +13.34 point improvement).\n\n## Complementarity with Data-Level Diversity Methods\n\nThe paper does **not discuss** explicit complementarity with curriculum learning or archive-based data approaches. However, it does note that diversity-promotion methods operate at different levels:\n\nThe authors acknowledge that \"token-level methods preserve local stochasticity\" and \"trajectory-level exploration\" methods \"broaden exploration,\" characterizing UCPO as complementary since it \"operates at the conditional-distribution level, reshaping how gradient mass is allocated among correct responses once they are sampled.\"\n\nThe focus remains on **within-episode gradient redistribution** rather than data-level curation, suggesting UCPO could potentially be combined with such approaches but this isn't empirically validated in the paper.",
    "durationMs": 4601,
    "url": "https://arxiv.org/html/2605.00365"
  },
  "sourceToolAssistantUUID": "7c143d1a-34d4-46b4-ba8b-921d3d6ce46a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-28T03:12:39.524Z_

<details><summary>↩ Tool result · `toolu_01VAtFod2VLnNHmampW4SKFA`</summary>

```text
Web search results for query: "SEC self-evolving curriculum LLM reasoning 2505.14970 MATH-500 AMC AIME detailed results table"

Links: [{"title":"Self-Evolving Curriculum for LLM Reasoning","url":"https://arxiv.org/html/2505.14970v1"},{"title":"Self-Evolving Curriculum for LLM Reasoning","url":"https://www.emergentmind.com/papers/2505.14970"},{"title":"[PDF] Self-Evolving Curriculum for LLM Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Evolving-Curriculum-for-LLM-Reasoning-Chen-Lu/be1985ec9f0bce3b45c81e7b28b93acbaf7e20eb"},{"title":"[2505.14970] Self-Evolving Curriculum for LLM Reasoning","url":"https://arxiv.org/abs/2505.14970"},{"title":"TACLer: Tailored Curriculum Reinforcement Learning for Efficient Reasoning","url":"https://arxiv.org/html/2601.21711"},{"title":"Learning to Reason under Off-Policy Guidance","url":"https://arxiv.org/pdf/2504.14945"},{"title":"R-Zero: SELF-EVOLVING REASONING LLM","url":"https://arxiv.org/pdf/2508.05004"},{"title":"Qwen2.5-Math-7B: Math-Specialized 7B LLM","url":"https://www.emergentmind.com/topics/qwen2-5-math-7b"},{"title":"Self-Evolving Curriculum for LLM Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250514970C/abstract"},{"title":"MATH-500 Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/math-500"}]

Based on my web search, I found the paper "Self-Evolving Curriculum for LLM Reasoning" (arxiv 2505.14970). Here are the key findings regarding SEC, MATH-500, AMC, and AIME results:

## Overview

Self-Evolving Curriculum (SEC) is an automatic curriculum learning approach for RL fine-tuning of LLMs that adaptively learns a curriculum policy concurrently with the RL fine-tuning process by formulating curriculum selection as a non-stationary Multi-Armed Bandit (MAB) problem.

## Performance Results

The models were evaluated on the MATH500, AMC22-23, and AIME24 datasets. Accuracy was measured by averaging pass@1 over 8 independent generations per problem.

## Key Improvements

The research demonstrates significant improvements with SEC:

- In mathematics, SEC markedly improves performance on the challenging AIME dataset by approximately 33% relative compared to the random baseline (0.075 → 0.10).

- For the smaller Qwen2.5-3B model, SEC consistently achieves substantial improvements on harder, out-of-distribution (OOD) test sets, with approximately 13% relative improvement on Countdown.

- SEC achieved significant relative accuracy gains over random baselines on OOD sets like Countdown (+13% for 3B), Zebra (+21% for 3B), and AIME24 (+33% for 3B).

The paper's Table 1 contains the detailed results table comparing SEC with other curriculum methods across the different mathematical reasoning benchmarks and model sizes, though the specific numerical values from the complete table are available in the full arxiv paper at https://arxiv.org/html/2505.14970v1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bf67e08-6981-490f-9043-29d764e3628a",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "b0487de0-6e2b-45fa-aa3f-1bd1b897e81c",
  "toolUseResult": {
    "query": "SEC self-evolving curriculum LLM reasoning 2505.14970 MATH-500 AMC AIME detailed results table",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HPR6MusU8qoNNMoVfhBC8H",
        "content": [
          {
            "title": "Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://arxiv.org/html/2505.14970v1"
          },
          {
            "title": "Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://www.emergentmind.com/papers/2505.14970"
          },
          {
            "title": "[PDF] Self-Evolving Curriculum for LLM Reasoning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Self-Evolving-Curriculum-for-LLM-Reasoning-Chen-Lu/be1985ec9f0bce3b45c81e7b28b93acbaf7e20eb"
          },
          {
            "title": "[2505.14970] Self-Evolving Curriculum for LLM Reasoning",
            "url": "https://arxiv.org/abs/2505.14970"
          },
          {
            "title": "TACLer: Tailored Curriculum Reinforcement Learning for Efficient Reasoning",
            "url": "https://arxiv.org/html/2601.21711"
          },
          {
            "title": "Learning to Reason under Off-Policy Guidance",
            "url": "https://arxiv.org/pdf/2504.14945"
          },
          {
            "title": "R-Zero: SELF-EVOLVING REASONING LLM",
            "url": "https://arxiv.org/pdf/2508.05004"
          },
          {
            "title": "Qwen2.5-Math-7B: Math-Specialized 7B LLM",
            "url": "https://www.emergentmind.com/topics/qwen2-5-math-7b"
          },
          {
            "title": "Self-Evolving Curriculum for LLM Reasoning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250514970C/abstract"
          },
          {
            "title": "MATH-500 Benchmark Leaderboard",
            "url": "https://llm-stats.com/benchmarks/math-500"
          }
        ]
      },
      "Based on my web search, I found the paper \"Self-Evolving Curriculum for LLM Reasoning\" (arxiv 2505.14970). Here are the key findings regarding SEC, MATH-500, AMC, and AIME results:\n\n## Overview\n\nSelf-Evolving Curriculum (SEC) is an automatic curriculum learning approach for RL fine-tuning of LLMs that adaptively learns a curriculum policy concurrently with the RL fine-tuning process by formulating curriculum selection as a non-stationary Multi-Armed Bandit (MAB) problem.\n\n## Performance Results\n\nThe models were evaluated on the MATH500, AMC22-23, and AIME24 datasets. Accuracy was measured by averaging pass@1 over 8 independent generations per problem.\n\n## Key Improvements\n\nThe research demonstrates significant improvements with SEC:\n\n- In mathematics, SEC markedly improves performance on the challenging AIME dataset by approximately 33% relative compared to the random baseline (0.075 → 0.10).\n\n- For the smaller Qwen2.5-3B model, SEC consistently achieves substantial improvements on harder, out-of-distribution (OOD) test sets, with approximately 13% relative improvement on Countdown.\n\n- SEC achieved significant relative accuracy gains over random baselines on OOD sets like Countdown (+13% for 3B), Zebra (+21% for 3B), and AIME24 (+33% for 3B).\n\nThe paper's Table 1 contains the detailed results table comparing SEC with other curriculum methods across the different mathematical reasoning benchmarks and model sizes, though the specific numerical values from the complete table are available in the full arxiv paper at https://arxiv.org/html/2505.14970v1."
    ],
    "durationSeconds": 7.4667849189999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9bf67e08-6981-490f-9043-29d764e3628a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 82 · 2026-05-28T03:12:58.369Z_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive data. Let me also check the SEC paper's v1 HTML for more detailed numbers. Actually, I already have the key numbers from my earlier fetch of v3:
- Qwen2.5-7B: 17.5% AIME24, 76.1% MATH-500, 51.1% AMC22-23
- Random baseline for 7B: 13.8% AIME24

And from the latest search, for Qwen2.5-3B:
- SEC 3B: ~10% AIME24 (0.075→0.10, +33% relative)


I notice Actor-Curator reports 20.0% AIME24 for their 3B model, which is notably higher than the original SEC paper's ~10%, likely due to their use of GSPO and different setup choices. I'll rely on the primary source numbers for accuracy and now compile the full revision JSON with the data I've gathered.

Looking at the performance metrics across these methods: Actor-Curator's Qwen2.5-3B achieves 30.0% AIME24 and 81.0% MATH-500 with about 9% overhead, outperforming SEC's 20.0% in direct comparison. Online Difficulty Filtering shows consistent gains of +12% on AMC and +10% on AIME using half the training steps. UCPO demonstrates substantial improvements across both DeepSeek and Qwen models on AIME24, with Pass@64 reaching 80.0% for DeepSeek and 56.67% for Qwen, plus 45% better equation diversity. Vocabulary Dropout results are still coming through.

Vocabulary Dropout with Qwen3-8B shows +4.4 average improvement, with +10.9 on AMC and +3.4 on AIME24 using the R-Zero framework. SOAR on Llama-3.2-3B achieves +9.3% pass@32 on previously failed MATH problems with 75% oracle recovery through Meta-RL. IndiMathBench reveals a stark geometry bottleneck—only 12.2% accuracy on geometry equations versus 44.9% on non-geometry, a 3.7× performance gap tied to formalization challenges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0487de0-6e2b-45fa-aa3f-1bd1b897e81c",
  "isSidechain": false,
  "requestId": "req_011CbUEesbRNrET74782AdR8",
  "type": "assistant",
  "uuid": "e31a3e67-e1bc-4973-92a0-31fc353e49de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7brWSsBoseiNuC4K3XMnz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12082,
      "cache_read_input_tokens": 44005,
      "output_tokens": 15527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15527,
          "cache_read_input_tokens": 44005,
          "cache_creation_input_tokens": 12082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12082
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

_source line 83 · 2026-05-28T03:12:58.370Z_

Now I have all the data I need. Let me synthesize everything and produce the comprehensive revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e31a3e67-e1bc-4973-92a0-31fc353e49de",
  "isSidechain": false,
  "requestId": "req_011CbUEesbRNrET74782AdR8",
  "type": "assistant",
  "uuid": "2aa37bc8-8f6f-48cd-8c1d-a015354fecdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7brWSsBoseiNuC4K3XMnz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12082,
      "cache_read_input_tokens": 44005,
      "output_tokens": 15527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15527,
          "cache_read_input_tokens": 44005,
          "cache_creation_input_tokens": 12082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12082
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

_source line 84 · 2026-05-28T03:18:47.638Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013eV9kAMh3tKhd5y1Bj6DJd`</summary>

```json
{
  "description": "Draft complete revised JSON",
  "subagent_type": "claude",
  "prompt": "\nI need you to help me assemble a complete, well-formatted JSON object for a research proposal revision. I will provide the exact content for each field. Your job is to combine them into a valid JSON object with proper escaping. Do NOT modify the content - just assemble it.\n\nOutput ONLY the JSON object, nothing else.\n\nHere are the fields:\n\nTITLE: \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Quality-Diversity from GSM to Olympiad with Targeted Weakness Synthesis\"\n\nPROJECT_NAME: \"sace_rlvr\"\nSOURCE: \"web_research\"\nLEVEL: \"top-tier\"\nCHANGE_TYPE: \"major\"\n\nTARGET_VENUES: [\n    \"ICLR 2027 (Sep 19-24, 2026) — stretch if pilot results by August\",\n    \"ICML 2027 (~Jan 2027) — primary target, strong fit for RL + QD + coverage\",\n    \"NeurIPS 2027 (~May 2027) — fallback with full evaluation\"\n]\n\nCORE_PROBLEM: \"Self-evolving RLVR systems that iteratively generate and solve problems face a dual challenge: maintaining problem diversity across the mathematical capability space while ensuring each problem provides maximal learning signal for the current policy. Recent theoretical work on RLVR learning dynamics (arXiv 2602.14872, ICML 2026) proves that mixed-difficulty training naturally produces an implicit curriculum—easier problems become learnable first and bootstrap harder ones via a 'relay effect.' However, this implicit curriculum is only efficient when the difficulty spectrum is smooth; gaps in difficulty coverage cause grokking-like plateaus where learning stalls. While this theory is validated on synthetic group-theoretic tasks with idealized assumptions (uniform distributions, single attention layer), it provides a compelling design heuristic: smoother difficulty coverage should improve convergence. Meanwhile, empirical evidence increasingly shows that training distribution diversity is essential even under the 'sparse policy selection' view (arXiv 2605.06241) where RL modifies only 1-3% of tokens: RL-PLUS (arXiv 2508.00222) demonstrates that narrow RLVR training causes 'capability boundary collapse' where pass@1 improves but pass@128 degrades, and Tailor (arXiv 2511.12429) shows that RL outcomes depend critically on the diversity of behaviors available for selection. DéjàQ (arXiv 2601.01931) made the foundational contribution of demonstrating that online MAP-Elites co-evolution during RL training is viable and beneficial—maintaining a quality-diversity archive where problems compete for cell occupancy based on learnability fitness p(1-p). However, DéjàQ operates exclusively at GSM-Symbolic level with a 1D archive of 8 thematic categories, random mutation strategies (22-44% invalid rates), and computationally expensive learnability estimation (K=100 completions per problem). Its 1D archive cannot track difficulty within topics, making difficulty-coverage enforcement impossible. Recent bandit-based curriculum approaches address adaptive selection during RL: SEC (arXiv 2505.14970) formulates curriculum as a MAB over problem categories, achieving 17.5% AIME 2024 on Qwen2.5-7B (+27% relative); Actor-Curator (arXiv 2602.20532) extends this with a neural curator achieving 30.0% AIME 2024 on Qwen2.5-3B (+28.6% relative over uniform) with regret guarantees. However, both select from fixed problem pools (12K MATH problems) without synthesis—they optimize WHICH existing problems to train on, but cannot create new problems when the pool lacks adequate coverage for the policy's current frontier. As the policy improves toward competition level, the fraction of useful problems in a fixed pool shrinks, hitting a pool-exhaustion ceiling. Separately, CLPO (arXiv 2509.25004) demonstrates that online curriculum adaptation achieves strong competition-level results (50.0% AIME 2024 with Qwen3-8B)—but operates statelessly per-batch with no persistent archive and only 3 coarse difficulty bins (width ~0.33). Socratic-Zero (arXiv 2509.24726) achieves 56.1% average across 7 math benchmarks through three-agent co-evolution—but its weakness targeting is purely reactive with no structured archive. SAGE (arXiv 2603.15255) demonstrates that flat unstructured question pools lead to over-specialization after ~120 steps, achieving 13.3% AIME 2024—matching the Qwen-2.5-7B base model—and actually degrading AMC 2023 from 57.5% to 52.5%. The fundamental open question is: can we build a system that combines the adaptive selection intelligence of bandit-based methods with persistent coverage-maintaining archives and targeted synthesis for identified gaps at competition level?\"\n\nOPPORTUNITY: \"Five converging developments create a precise research window. (1) DéjàQ proves the paradigm: online MAP-Elites co-evolution during RL training improves reasoning via quality-based archive replacement. But DéjàQ's 1D thematic archive at GSM level cannot track difficulty within topics. (2) The implicit curriculum theory (arXiv 2602.14872) provides a compelling design motivation: RLVR naturally produces curriculum effects, but convergence speed depends critically on difficulty spectrum smoothness. While validated only on synthetic tasks, this motivates fine-grained multi-dimensional archives as a principled design heuristic—and multiple empirical findings support diversity's importance: RL-PLUS shows narrow training causes capability boundary collapse; Sharper Primitives (arXiv 2602.08281) shows diverse training activates broader computational primitives via multiplicative compounding; Tailor (arXiv 2511.12429) shows that behavioral diversity is the binding constraint for RL outcomes. (3) Competition-level feasibility is established: CLPO achieves 50.0% AIME 2024; Socratic-Zero achieves 56.1% average; Bidirectional Curriculum Generation (arXiv 2603.05120) achieves 60.03 average with only 5,873 samples. But none maintains structured multi-dimensional archives with systematic gap identification. (4) Bandit-based curriculum methods demonstrate the value of adaptive selection but reveal the ceiling of fixed-pool approaches: SEC achieves 17.5% AIME 2024 (Qwen2.5-7B) via MAB over categories; Actor-Curator achieves 30.0% AIME 2024 (Qwen2.5-3B) via neural bandit with regret guarantees—but both select from fixed 12K pools without synthesis or multi-dimensional coverage tracking. The approaches are potentially COMPLEMENTARY: principled bandit selection FROM a coverage-maintaining, synthesis-augmented archive. (5) The synthesis-verification gap is closing: SAND-Math demonstrates ~38% end-to-end survival through its full pipeline (8,842 from 23,437 generated); SPARQ achieves ~25% overall QD survival (320K→80K); per-niche survival varies by topic (geometry autoformalization is ~3.7× harder than non-geometry per IndiMathBench, though this reflects formalization-specific difficulty that may not fully transfer to synthesis). VHG's validity-gating separates problem validity from difficulty; MathForge's DGPO yields +4.56% over vanilla GRPO. The gap: no existing work combines (a) persistent multi-dimensional archives that promote smooth difficulty coverage, (b) proactive niche-level gap identification with targeted synthesis (vs. reactive instance-level targeting or selection-only bandits), (c) competition-level multi-stage verification, and (d) Bayesian learnability-based replacement criteria.\"\n\nLANDSCAPE: \"**Online archive-based co-evolution (direct predecessor).** DéjàQ (arXiv 2601.01931) is the most directly relevant prior work and establishes the paradigm we scale. It implements online MAP-Elites during RL with quality-based replacement (fitness = learnability p(1-p), unbiased estimator from K=100 completions; replaces cell occupant when f(x')>f(y)). Uses 1D archive with 8 thematic 'setting' categories. Three mutation strategies (setting, distractor, symbolic mutators) operate concurrently with RL training. Results: 94.1% GSM-Symbolic, 69.6% MATH-500 on Qwen2.5-7B-Instruct. Critical limitations defining our delta: (a) GSM-Symbolic only—competition-level scaling untested; (b) 22-44% invalid rates even at GSM level; (c) 1D thematic categories cannot distinguish difficulty within topics; (d) random mutation rather than targeted weakness synthesis; (e) K=100 completions per problem is computationally expensive vs. reusing training rollouts.\\n\\n**Bandit-based adaptive curriculum (critical comparators).** SEC (arXiv 2505.14970) formulates online curriculum selection as a non-stationary MAB where each problem category (difficulty level or problem type) is an arm. Uses TD(0) updates on Q-values derived from absolute advantages, with Boltzmann sampling: p(c) ∝ exp(Q(c)/τ). Selects from fixed training pools (10K problems per domain). Qwen2.5-7B: 17.5% AIME 2024 (+27% relative over random 13.8%), 76.1% MATH-500, 51.1% AMC22-23. Categories are 1D (difficulty OR type per domain). SEC-2D variant combines 3 reasoning domains into 9 arms for multi-task learning. Actor-Curator (arXiv 2602.20532) extends beyond SEC's category-level bandits to per-problem utility estimation via a neural curator (Qwen3-0.6B) trained with online stochastic mirror descent (OSMD). Establishes regret bound O(T^{2/3}·V_T^{1/3}) under non-stationary utilities. Selects from fixed pools (12K MATH problems). Qwen2.5-3B: 30.0% AIME 2024, 81.0% MATH-500 (+28.6% relative over uniform 23.3%; beats SEC at 20.0% in matched 3B comparison). ~9% overhead. Key insight: Actor-Curator's per-problem utility estimation is more expressive than SEC's category-level Q-values, yielding consistent gains. Critical differentiation from SACE-RLVR on four dimensions: (a) SELECTION vs. SYNTHESIS—both SEC and Actor-Curator select from fixed pools of existing problems; they cannot synthesize new problems targeting identified gaps. As the policy improves toward competition level, the fraction of useful problems in a fixed 12K pool shrinks (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED optimization—Actor-Curator optimizes aggregate per-problem utility without explicit multi-dimensional coverage constraints, risking concentration on high-utility niches without ensuring breadth (analogous to SAGE's demonstrated over-specialization); (c) STATELESS vs. PERSISTENT—neither maintains a persistent multi-dimensional archive with cross-step coverage tracking; (d) COMPLEMENTARITY—crucially, these approaches compete at different levels: Actor-Curator's bandit selection could serve as the within-archive sampling strategy, combining principled selection WITH coverage-maintaining synthesis. We test this complementarity explicitly.\\n\\n**Balanced difficulty filtering theory.** Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) proves that expected policy improvement is lower-bounded by the variance of task-level success probabilities p(x)(1-p(x)), maximized at p(x)=0.5. Balanced filtering (0.3&lt;p(x)<0.7) achieves +12% on AMC and +10% on AIME with Qwen2.5 models in less than half the training steps of standard GRPO. This theoretical result directly supports our difficulty-aware design: our Bayesian learnability criterion tracks p(1-p) per problem via Beta posteriors, and our archive's ZPD-weighted sampling preferentially selects problems near the difficulty frontier.\\n\\n**Online stateless curriculum (competition-level).** CLPO (arXiv 2509.25004) performs online curriculum during RLVR with real-time difficulty assessment (3 bins: Hard ≤0.3, Medium 0.3-0.7, Easy >0.7 from G=4 rollouts), Adaptive Problem Restructuring, and difficulty-aware KL. Achieves 50.0% AIME 2024 with Qwen3-8B, +6.96% average over baselines. Critical delta: no persistent archive; no cross-step memory; 3 coarse difficulty bins create large inter-bin gaps.\\n\\n**Three-agent co-evolution with instance-level weakness targeting.** Socratic-Zero (arXiv 2509.24726, Sep 2025) implements a Solver/Teacher/Generator triad where a frozen 235B Teacher identifies weaknesses by examining the Solver's specific failed solutions. Uses a Gaussian utility function centered at 50% success rate for 'desirable difficulty.' Achieves 56.1% average across 7 math benchmarks (+20.2% over baseline) on Qwen3-8B. Differentiation: (a) reactive instance-level vs. our proactive niche-level targeting; (b) no structured archive or coverage map; (c) 1D three-zone categorization; (d) requires frozen 235B oracle Teacher vs. our policy-based gap identification via archive structure.\\n\\n**Multi-agent self-evolution with quality filtering.** SAGE (arXiv 2603.15255, Mar 2026) implements a 4-agent framework (Challenger/Planner/Solver/Critic) where all agents co-evolve from a shared backbone using only a 500-example seed set. The Critic filters by quality (threshold α=0.7), difficulty measured by Solver failure rate. Achieves OlympiadBench 38.7% and LiveCodeBench 26.4% on Qwen-2.5-7B (+10.7% and +8.9% respectively). On AIME 2024, SAGE achieves 13.3%—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%. This demonstrates that flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents. Training dynamics confirm this: over-specialization emerges after ~120 steps (peak 69.5% declining to 61.6% by step 240). Question pool grows 18× (1,136→20,532) as flat filtered dataset without structured organization.\\n\\n**Implicit curriculum theory.** 'The Implicit Curriculum' (arXiv 2602.14872, ICML 2026) proves that standard REINFORCE with mixed-difficulty training naturally produces progressive learning. Two regimes: relay (smooth difficulty, faster convergence) and grokking (gapped, long plateaus). Important caveats: validated on synthetic group-theoretic tasks with uniform distributions and a single attention layer. We adopt this as a design motivation—not a rigorous theoretical foundation. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n**Sparse policy selection, diversity, and capability boundaries.** Sparse Policy Selection (arXiv 2605.06241) shows RL modifies only 1-3% of tokens at high-entropy decision points. However, multiple works demonstrate training distribution diversity remains critical. Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), diverse training that sharpens more primitive types exponentially expands solvable tasks. Tailor (arXiv 2511.12429) directly shows that 25 vs. 4 diverse primitives substantially improves post-RL performance: 'behavioral diversity is the binding constraint for RL.' RL-PLUS (arXiv 2508.00222) demonstrates 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse training as the antidote (+69.2%). ProRL (arXiv 2505.24864) shows diverse prolonged training accesses capabilities inaccessible through base model sampling alone. We argue: precisely BECAUSE RL operates through sparse selection, training distribution diversity becomes MORE important.\\n\\n**Policy-level diversity maintenance (concurrent).** UCPO (arXiv 2605.00365) addresses pass@k diversity collapse at the optimization level rather than the data level, adding a conditional uniformity penalty that redistributes gradient signal toward underrepresented correct solutions. Achieves +10% absolute Pass@64 on AIME 2024 (DeepSeek-7B: 70.0%→80.0%) and +45% equation-level diversity while maintaining competitive Pass@1. Importantly, UCPO modifies the loss function, not the training distribution—making it orthogonal to and potentially complementary with archive-based diversity maintenance. UCPO ensures diversity within the correct solution set for a given problem; SACE-RLVR ensures diversity across the problem distribution.\\n\\n**Lightweight co-evolutionary diversity (concurrent).** Vocabulary Dropout (arXiv 2604.03472) prevents proposer diversity collapse in co-evolutionary frameworks by applying random hard logit masks during problem generation, achieving +4.4 average points on Qwen3-8B (+10.9 AMC, +3.4 AIME 2024, +7.8 AIME 2025) within R-Zero. Demonstrates that diversity collapse is a real bottleneck in co-evolutionary RLVR. Differentiation: VD maintains proposer diversity via stochastic masking; SACE-RLVR provides structured coverage guarantees and interpretable gap identification.\\n\\n**Meta-RL curriculum generation (concurrent).** SOAR (arXiv 2601.18778) uses bi-level meta-RL where a teacher generates stepping-stone problems rewarded by measured student improvement on hard problems. Achieves +9.3% pass@32 on MATH fail@128 tasks (Llama-3.2-3B), recovering 75% of oracle gains from training on the full MATH dataset. Key insight: structural quality of generated problems matters more than solution correctness. Conceptually parallel to our proactive gap identification but uses meta-RL reward signal (measured student improvement) vs. our archive-structure-based gap detection. SOAR operates at the edge of learnability for currently-unsolvable problems; SACE-RLVR maintains coverage across the full difficulty spectrum.\\n\\n**Bidirectional curriculum generation.** Bidirectional Curriculum Generation (arXiv 2603.05120, Mar 2026): 4-agent framework, 60.03 average with 5,873 samples; AIME 2025: 40.0. No structured archives, QD objectives, or systematic coverage tracking.\\n\\n**Novelty-aware diversity.** EVOL-RL (arXiv 2509.15194): stateless novelty-aware rewards. Qwen3-4B AIME25: 4.6%→16.4%; Qwen3-8B AIME24: 16.7→26.0. Proves diversity collapse is real (TTRL pass@16: 32.4→16.7).\\n\\n**Difficulty-aware policy optimization.** MathForge/DGPO (arXiv 2601.20614, ICLR 2026): MAD normalization + DQW weighting. AIME 2024: 24.58 on Qwen2.5-Math-7B, +4.56 over GRPO. We adopt as extension.\\n\\n**Reward variance as curriculum signal.** VCRL (arXiv 2509.19803): reward variance within rollout groups reflects problem difficulty. G=16 throughout, 57.76 average on Qwen3-8B. We adopt the insight, extending with Bayesian temporal smoothing.\\n\\n**Rollout count effects and gradient degeneracy.** MC-GRPO (arXiv 2601.22582) directly ablates G: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%. Gradient Starvation (arXiv 2605.07689): for binary rewards, degenerate group probability = p^G+(1-p)^G; at G=4: 69.25% groups produce zero gradient. DAPO standardizes G=16. DBB estimator (arXiv 2603.18444): Bayesian Beta-Bernoulli estimation reduces variance for RLVR—related to our approach but operates at policy gradient level vs. our archive-replacement level.\\n\\n**Synthesis survival rates.** SAND-Math (arXiv 2507.20527): ~38% end-to-end (8,842/23,437; ~75% consistency, ~57% difficulty filtering, ~96% novelty). SPARQ (arXiv 2506.06499): ~25% QD survival (320K→80K). DART-Math (arXiv 2407.13690): Level 5 loses 51.1% query coverage. FLAMES (arXiv 2508.16514): ~30% overall survival with strict self-consistency; Level 5 loses 50%. Per-topic: geometry autoformalization has ~3.7× lower success rate than non-geometry topics (IndiMathBench arXiv 2512.00997: 12.2% vs 44.9% BEq across top models); the paper attributes this partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty. These grounding data inform our per-niche survival estimates.\\n\\n**Verification.** VHG (arXiv 2605.06660): validity gating.\\n\\n**AIME 2024 landscape.** Distillation: Klear-Reasoner-8B 90.5%, DeepSeek-R1-Distill-Qwen-7B 83.3%. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm.\\n\\n**Weakness-driven synthesis.** SwS (NeurIPS 2025): offline weakness targeting, +10%. STAT (arXiv 2510.10023): Missing-Skill-Profiles.\\n\\n**Self-evolving RLVR.** SvS (ICLR 2026): answer-preserving mutations. R-Zero (ICLR 2026): collapses iter 3. Prism (arXiv 2603.13309): 128-cluster diversity. R-Diverse (arXiv 2602.13103): SAM + MAP.\\n\\n**The precise gap.** DéjàQ: 1D, GSM-only. SEC: MAB over categories, 1D, fixed pool. Actor-Curator: per-problem bandit, fixed pool, no coverage tracking. CLPO: stateless, coarse bins. Socratic-Zero: reactive, no archive. SAGE: flat pool, over-specialization, zero AIME improvement over base model. Online Difficulty Filtering: theoretical support for balanced filtering, no archive structure. UCPO: policy-level diversity, no data-level coverage. No existing work combines persistent multi-dimensional archives, proactive niche-level gap identification with synthesis, structured coverage tracking, and Bayesian learnability replacement. Moreover, no existing work tests whether bandit-based selection and archive-based synthesis are complementary.\"\n\nINSPIRED_BY: \"DéjàQ_paradigm['online MAP-Elites co-evolution for RLVR'] + implicit_curriculum_motivation['relay regime; smooth coverage as design heuristic'] + SEC_insight['MAB over problem categories during RL; 17.5% AIME24'] + Actor_Curator_insight['neural bandit with regret guarantees; 30.0% AIME24; ~9% overhead; pool-selection ceiling motivates synthesis'] + Online_Difficulty_Filtering['p(1-p) lower bound on policy improvement; balanced filtering; EACL 2026'] + CLPO_insight['50% AIME 2024'] + Socratic_Zero_pattern['56.1% avg, reactive targeting'] + SAGE_lesson['flat pools → over-specialization ~120 steps; 13.3% AIME = base model; AMC degrades'] + RL_PLUS_evidence['capability boundary collapse from narrow RLVR, +69.2% with diversity'] + Sharper_Primitives['multiplicative compounding, polarization'] + Tailor_evidence['behavioral diversity is binding constraint for RL'] + UCPO_concurrent['policy-level diversity; +10% Pass@64 AIME; complementary to data-level'] + VocabDropout_concurrent['+4.4 avg; diversity collapse prevention'] + SOAR_concurrent['meta-RL teacher; 75% oracle recovery'] + VCRL_insight['reward variance reflects difficulty'] + MC_GRPO_evidence['G=2: 78.92% vs G=8: 84.53%'] + gradient_starvation['69% degenerate groups at G=4'] + DBB_estimator['Bayesian estimation validates Beta approach'] + SPARQ_survival['25% QD survival'] + DART_Math_survival['Level 5: 51.1% query dropout'] + IndiMathBench_geometry['geometry ~3.7× lower autoformalization success; formalization-specific'] + EVOL_RL_warning['diversity collapse']\"\n\nAPPROACH: \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), which scales the online MAP-Elites paradigm established by DéjàQ from GSM-level to competition-level mathematics. We organize the system around **three core innovations** plus **four extensions** tested in ablations. This follows the structure of successful prior systems: DéjàQ claims ~2 core contributions atop ~11 mechanisms; CLPO claims 3 named contributions atop ~7 design choices.\\n\\n**Design Motivation: Why Coverage Matters (Two Independent Arguments).**\\n\\n*Argument 1: Relay-regime-inspired smooth difficulty coverage.* The implicit curriculum theory (arXiv 2602.14872, ICML 2026) demonstrates on synthetic tasks that smooth difficulty spectra ('relay regime') yield faster convergence than gapped spectra ('grokking regime'). While this theory assumes idealized conditions (uniform distributions, geometric difficulty structure, single attention layer) that differ from real RLVR, it provides a principled design heuristic: smoother difficulty coverage should improve convergence. Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) provides additional theoretical support: policy improvement is lower-bounded by p(1-p) variance, maximized at balanced difficulty, achieving +12% AMC and +10% AIME in half the training steps. Our 10 fine-grained difficulty bins (width 0.1) rather than CLPO's 3 coarse bins (width ~0.33) are motivated by these insights. Ablation A3 provides the first empirical test of whether relay-like dynamics manifest in real RLVR. We do not claim theoretical guarantees transfer from the synthetic setting.\\n\\n*Argument 2: Broad coverage prevents capability boundary collapse.* Even under the 'sparse policy selection' view where RL modifies only 1-3% of tokens (arXiv 2605.06241), comprehensive coverage is essential. Three empirical findings converge: (a) Sharper Primitives (arXiv 2602.08281) shows RLVR 'polarizes'—sharpening some primitives while sacrificing others—and since multi-step success compounds multiplicatively (P(q) ∝ ∏P(sⱼ)), each un-sharpened primitive type creates an exponential bottleneck; (b) Tailor (arXiv 2511.12429) directly demonstrates that behavioral diversity, not correctness, is the binding constraint for RL outcomes (25 vs. 4 primitives → substantial gains); (c) RL-PLUS (arXiv 2508.00222) shows narrow RLVR causes 'capability boundary collapse'—pass@1 up, pass@128 down—with diverse distributions as the antidote (+69.2% relative improvement). Thus, comprehensive difficulty×topic coverage benefits under both views: relay-like curriculum dynamics AND broader capability activation.\\n\\n*Why archives with synthesis vs. bandit selection from fixed pools.* SEC and Actor-Curator demonstrate the clear value of adaptive problem selection during RL training. We argue that persistent archives with targeted synthesis provide three capabilities that fixed-pool bandit selection cannot: (i) COVERAGE GUARANTEES—bandits optimize aggregate utility and may concentrate on high-utility niches without ensuring breadth across the difficulty×topic space, analogous to SAGE's demonstrated over-specialization (13.3% AIME = base model, AMC degradation); structured archives explicitly enforce minimum coverage per niche. (ii) SYNTHESIS FOR GAPS—as the policy improves, the useful difficulty frontier advances, and a fixed pool (e.g., MATH's 12K problems) becomes increasingly sparse at the frontier; targeted synthesis creates fresh problems where the policy needs them most. (iii) PERSISTENT TRACKING—archives maintain cross-step memory of which niches are well-covered and which are stale, enabling proactive rather than reactive curriculum adaptation. However, these approaches are potentially COMPLEMENTARY: Actor-Curator's principled per-problem utility estimation can serve as the within-archive sampling strategy, and we test this explicitly (see E4 and baseline #5).\\n\\n---\\n\\n**CORE INNOVATION 1: 2D Learnability Archive (50 cells).**\\n10 difficulty bins (width 0.1, empirical solve-rate) × 5 topics (Algebra, Geometry, Number Theory, Combinatorics, Analysis/Calculus) = 50 cells, M=10 problems per cell. Topic classification via GPT-4o-mini (84-92% accuracy per arXiv 2411.00042). Difficulty measured via G=16 rollouts reused from training.\\n\\nThe 2D structure enables qualitatively new capabilities vs. prior work: (a) difficulty-aware coverage tracking—locate under-populated difficulty×topic niches BEFORE policy failures (vs. Socratic-Zero's reactive approach, SAGE's flat pool that over-specializes by step ~120, SEC/Actor-Curator's fixed-pool selection without coverage constraints); (b) persistent cross-step memory—problems track with the evolving policy, revealing emergent curriculum (vs. CLPO's stateless per-batch assessment, SEC's myopic TD updates); (c) interpretable post-hoc analysis—which niches drive benchmark performance.\\n\\nReplacement criterion: candidate problem enters a cell if its Bayesian learnability credible interval (see Core 3) exceeds the current worst occupant's upper bound. More principled than DéjàQ's point estimate comparison f(x')>f(y).\\n\\n**CORE INNOVATION 2: Proactive Gap-Targeted Synthesis with Verification.**\\nExisting targeting is either reactive (Socratic-Zero examines specific failed solutions; SwS identifies aggregate weaknesses offline) or selection-only (SEC/Actor-Curator adaptively choose from fixed pools). SAGE's Challenger generates harder problems without coverage awareness, leading to over-specialization. The 2D archive enables proactive niche-level gap identification:\\n\\n(a) Identify under-performing cells: <3 problems or stale (not refreshed for >100 training steps).\\n(b) Generate-then-classify synthesis: generate for target TOPIC without difficulty constraints, verify, then empirically measure difficulty via G=16 rollouts and assign to the appropriate cell. This avoids the 'double filter' problem (constraining both topic AND difficulty yields 4-17% per SPARQ/MathSmith evidence; topic-only yields higher survival).\\n(c) 3-stage VHG-inspired verification: (i) format/solvability check (filters ~25-30%, consistent with FLAMES ~30% removal), (ii) cross-verification via majority vote across 2-3 strong models (filters ~15-20%), (iii) difficulty calibration via G=16 rollouts.\\n\\n**Concrete per-niche survival estimates (literature-grounded):**\\nEstimates sourced from SPARQ (~25% QD survival), DART-Math (51.1% Level 5 dropout), FLAMES (50% removal at Level 5), and IndiMathBench (~3.7× lower geometry autoformalization success rate, 12.2% vs 44.9% BEq; noting this reflects formalization-specific difficulty that may not fully transfer to synthesis).\\n\\n- Easy-medium cells (solve-rate 0.3-0.8), common topics (Algebra, NT): ~30 cells, ~30-50% survival.\\n  Need ~20-35 candidates/cell → ~600-1,050 total.\\n- Medium-hard cells (solve-rate 0.1-0.3), common topics: ~10 cells, ~15-25% survival.\\n  Need ~40-65 candidates/cell → ~400-650 total.\\n- Geometry cells (all difficulties): ~10 cells, ~10-20% survival (geometry synthesis is harder than algebra due to constraint consistency requirements, though the ~3.7× autoformalization ratio from IndiMathBench reflects Mathlib-specific challenges and likely overstates synthesis difficulty; we conservatively estimate ~2-3× harder than algebra for synthesis).\\n  Need ~50-100 candidates/cell → ~500-1,000 total.\\n- Extreme cells (solve-rate <0.1 or >0.9, all topics): ~10 cells, ~3-8% survival (DART-Math: Level 5 loses 51% coverage; FLAMES: 50% removal at Level 5).\\n  Need ~125-330 candidates/cell → ~1,250-3,300 total.\\n- **Graceful degradation:** cells that cannot reach M=10 accept minimum 3 (sufficient for meaningful Beta posterior updates). Archive reports actual occupancy; analysis accounts for sparse cells.\\n- **Total per refresh cycle:** ~2,750-6,000 candidates (median ~4,000). Generation cost using open-source 70B teacher: ~130 GPU-hours. Verification (G=16 rollouts per candidate on 7B): ~12 GPU-hours. Per-refresh total: ~142 GPU-hours. Over ~10 refreshes: ~1,420 GPU-hours. Alternative: API-based generation at ~$0.30/problem ≈ $1,200/refresh, $12,000 total.\\n- Per-niche survival rates and generation statistics reported as community contribution.\\n\\n**CORE INNOVATION 3: Zero-Cost Bayesian Learnability Estimation.**\\nDéjàQ estimates learnability via K=100 dedicated completions per problem—computationally expensive and separate from training. We reuse G=16 rollouts already generated for GRPO training—zero additional inference cost. G=16 is well-justified: DAPO (arXiv 2503.14476) standardizes G=16; MC-GRPO (arXiv 2601.22582) shows clear degradation at small G (G=2: 78.92%, G=4: 81.34%, G=8: 84.53%); the Gradient Starvation analysis (arXiv 2605.07689) explains the mechanism—for binary rewards, degenerate group probability is p^G+(1-p)^G, yielding 69.25% degenerate groups at G=4 vs. <1% at G=8.\\n\\nBayesian temporal smoothing: Beta-Bernoulli running posterior per problem (Beta(1,1) prior, updated each appearance). After 3 appearances (48 cumulative rollouts), posterior variance drops ~3×. Replacement uses conservative credible interval: candidate must exceed occupant's upper bound, preventing noisy replacements. The p(1-p) learnability signal is theoretically supported by Online Difficulty Filtering's result (arXiv 2504.03380) that policy improvement is lower-bounded by this exact quantity.\\n\\nRelated but distinct from the Discounted Beta-Bernoulli (DBB) estimator (arXiv 2603.18444), which applies Bayesian estimation at the policy gradient level. Our Beta posterior operates at the archive-replacement level for per-problem learnability tracking—a different application of the same statistical principle. VCRL's insight (arXiv 2509.19803) that reward variance reflects difficulty is extended from curriculum signal to Bayesian replacement criterion.\\n\\n---\\n\\n**EXTENSIONS (each tested in one ablation, not claimed as core contributions):**\\n\\nE1: Cross-niche SvS seeding. SvS-style answer-preserving mutation (ICLR 2026) from adjacent cells to seed under-populated niches. Expected ~70-80% validity for within-topic mutations. Particularly valuable for geometry and extreme cells where de novo generation has lower survival. Tested in A5.\\n\\nE2: James-Stein shrinkage. Following arXiv 2511.03710 (which demonstrates shrinkage baselines reduce MSE in RLVR), we apply shrinkage to per-problem learnability estimates, regularizing toward batch average. Not claimed as novel—cite and use. Tested in A6.\\n\\nE3: DGPO policy updates. MAD normalization + DQW weighting adopted from MathForge (arXiv 2601.20614, ICLR 2026). Addresses difficulty-dependent advantage scale. Tested in A7.\\n\\nE4: Archive sampling strategy. Compare (a) ZPD-weighted sampling with posterior variance weighting ([0.1, 0.9] solve-rate, high uncertainty → more sampling), (b) uniform sampling, and (c) Actor-Curator-style bandit sampling from the archive—directly testing whether principled per-problem utility estimation (à la Actor-Curator) further improves when operating within a coverage-maintaining archive. This tests the complementarity hypothesis.\\n\\n---\\n\\n**Training Loop (VERL, Qwen2.5-Math-7B primary, Qwen3-8B secondary):**\\n(a) Sample from archive with selected strategy (E4). (b) G=16 rollouts, compute advantages. (c) Policy update (GRPO or DGPO). (d) Update Beta posteriors per problem. (e) Every 50 steps: refresh sampled cells, reassign problems that shifted difficulty, flag stale cells, synthesize for gaps. Overhead: ~20-25% vs. vanilla GRPO (dominated by synthesis cost).\\n\\n**AIME Contextualization.** Distillation-based: 70-90% AIME 2024. Bandit selection: Actor-Curator 30.0% (3B), SEC 17.5% (7B). Self-evolving without distillation: R-Zero ~16%, Absolute Zero ~13-20%, EVOL-RL 20.6-26.0%, SAGE 13.3% (= base model). Seed-data: CLPO 50.0%. We target the self-evolving/seed-data paradigm. Value: METHOD + ABLATION INSIGHTS. Framework applicable atop distilled bases.\\n\\n**Baselines (8):** (1) DéjàQ-comp [PRIMARY: 2D+targeting value over 1D archive]. (2) CLPO [PRIMARY: persistent archive value over stateless curriculum]. (3) Socratic-Zero [PRIMARY: structured proactive vs. reactive instance-level targeting]. (4) SAGE [structured archive vs. flat pool; evidence: SAGE's AIME = base model + AMC degradation]. (5) Actor-Curator [PRIMARY: archive synthesis vs. bandit selection from fixed pool; complementarity test via E4]. (6) EVOL-RL [stateless novelty-aware diversity]. (7) MathForge [DGPO source; difficulty-aware optimization]. (8) Vanilla GRPO [minimal baseline].\\n\\n**Ablations (7):**\\nA1: 1D archive only (tests Core 1 dimensionality).\\nA2: Random synthesis vs. gap-targeted (tests Core 2 proactive targeting).\\nA3: 3 bins vs. 10 bins [relay-regime-inspired test: first empirical comparison of coarse vs. fine difficulty granularity in real RLVR].\\nA4: Point estimation vs. Beta posterior (tests Core 3 vs. DéjàQ-style p(1-p)).\\nA5: Without cross-niche SvS seeding (tests E1 value, especially for sparse cells).\\nA6: Without James-Stein shrinkage (tests E2).\\nA7: GRPO vs. DGPO (tests E3).\\n\\n**Evaluation:** AIME 2024/2025, MATH-500, AMC 2023, Minerva Math, OlympiadBench. pass@1 AND pass@k (pass@k especially important per RL-PLUS's capability boundary collapse finding and UCPO's concurrent work on policy-level diversity—we test whether archive-based data diversity and policy-level diversity address complementary aspects of the collapse). DAPO-Math-17k seeds.\\n\\n**Key Analyses:** (1) Coverage heatmaps showing cell occupancy evolution. (2) Per-cell benchmark contribution: which niches drive gains? (3) Emergent curriculum: bin-transition frequencies as policy improves. (4) Synthesis efficiency: per-topic survival rates vs. literature benchmarks (SPARQ, DART-Math, FLAMES), reported as community contribution. (5) Convergence speed: 10 vs. 3 bins. (6) Capability boundary: pass@1 vs. pass@k trajectories—does archive diversity prevent RL-PLUS-style collapse? How does data-level diversity (SACE-RLVR) compare to policy-level diversity (UCPO)? (7) Structured vs. flat: archive coverage diversity over training vs. SAGE-style accumulation. (8) Selection vs. synthesis: Actor-Curator from fixed pool vs. Actor-Curator-style sampling from SACE-RLVR archive—quantifying the value of synthesis and coverage maintenance.\"\n\nRESOURCE_ESTIMATE: {\n    \"manual\": {\n      \"gpu_hours\": \"7,200 H100-hours (baselines: 8×250h=2,000h; SACE-RLVR 7B 800h; SACE-RLVR 8B 800h; ablations 7×200h=1,400h; synthesis/verification 1,420h; archive overhead 330h; E4 bandit variant 450h)\",\n      \"timeline\": \"14-18 weeks\",\n      \"estimated_gpu_cost\": \"$18,000 (at ~$2.50/H100-hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"5,600 H100-hours (reuse released code; shared verification; API-based generation saves ~1,100 GPU-hrs but adds ~$12,000 API cost)\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$400-800 (code assistance)\",\n      \"synthesis_api_cost\": \"$7,000-12,000 (problem generation via API, optional vs. GPU)\",\n      \"estimated_gpu_cost\": \"$14,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"8,800 H100-hours (exploratory sweeps over archive dimensions, bin count, refresh frequency, replacement criteria, synthesis strategies, bandit-archive complementarity)\",\n      \"timeline\": \"10-13 weeks\",\n      \"claude_api_cost\": \"$1,000-2,000\",\n      \"estimated_gpu_cost\": \"$22,000\",\n      \"speed_bottleneck\": \"GPU queue; each GRPO run 24-72h on 8×H100s. Synthesis for extreme cells dominates generation cost.\"\n    }\n}\n\nKEY_REFERENCES: [\n    \"DéjàQ (arXiv 2601.01931) — PRIMARY PREDECESSOR, online MAP-Elites for RLVR at GSM level\",\n    \"SEC (arXiv 2505.14970) — CRITICAL COMPARATOR, MAB over problem categories; 17.5% AIME24 on Qwen2.5-7B\",\n    \"Actor-Curator (arXiv 2602.20532) — PRIMARY BASELINE, neural bandit selection from fixed pool; 30.0% AIME24 on Qwen2.5-3B; regret guarantees; ~9% overhead\",\n    \"CLPO (arXiv 2509.25004) — PRIMARY BASELINE, online curriculum at competition level; 50.0% AIME 2024\",\n    \"Socratic-Zero (arXiv 2509.24726) — PRIMARY BASELINE, three-agent co-evolution; 56.1% avg\",\n    \"SAGE (arXiv 2603.15255) — BASELINE, 4-agent self-evolution; 13.3% AIME = base model; AMC degrades 57.5%→52.5%\",\n    \"Online Difficulty Filtering (arXiv 2504.03380, EACL 2026) — THEORETICAL SUPPORT, p(1-p) lower bound on policy improvement; +12% AMC in half steps\",\n    \"The Implicit Curriculum (arXiv 2602.14872, ICML 2026) — DESIGN MOTIVATION, relay vs. grokking (synthetic tasks)\",\n    \"UCPO (arXiv 2605.00365) — CONCURRENT, policy-level diversity via conditional uniformity; +10% Pass@64 AIME24; complementary to data-level\",\n    \"Vocabulary Dropout (arXiv 2604.03472) — CONCURRENT, lightweight diversity via logit masking; +4.4 avg on 8B\",\n    \"SOAR (arXiv 2601.18778) — CONCURRENT, meta-RL teacher for edge-of-learnability synthesis; 75% oracle recovery\",\n    \"Sparse Policy Selection (arXiv 2605.06241) — RL modifies 1-3% of tokens; motivates broad coverage\",\n    \"Sharper Primitives (arXiv 2602.08281) — RLVR polarizes; multiplicative compounding; diverse training activates broader primitives\",\n    \"Tailor (arXiv 2511.12429) — behavioral diversity is binding constraint for RL; 25 vs 4 primitives\",\n    \"RL-PLUS (arXiv 2508.00222) — capability boundary collapse from narrow RLVR; +69.2% with diversity\",\n    \"ProRL (arXiv 2505.24864) — diverse prolonged training accesses beyond base model ceiling\",\n    \"Bidirectional Curriculum Generation (arXiv 2603.05120) — 4-agent bidirectional; 60.03 avg\",\n    \"EVOL-RL (arXiv 2509.15194) — stateless novelty-aware diversity; AIME25 16.4%\",\n    \"MathForge/DGPO (arXiv 2601.20614, ICLR 2026) — MAD normalization; adopted as extension\",\n    \"VCRL (arXiv 2509.19803) — reward variance as difficulty proxy; G=16; 57.76 avg Qwen3-8B\",\n    \"MC-GRPO (arXiv 2601.22582) — rollout count ablation: G=2: 78.92%, G=4: 81.34%, G=8: 84.53%\",\n    \"Gradient Starvation (arXiv 2605.07689) — 69% degenerate groups at G=4; explains G effect mechanistically\",\n    \"DAPO (arXiv 2503.14476) — standardizes G=16\",\n    \"Discounted Beta-Bernoulli (arXiv 2603.18444) — Bayesian estimation for RLVR; validates Beta approach\",\n    \"SwS (NeurIPS 2025, arXiv 2506.08989) — offline weakness targeting; +10%\",\n    \"SvS (ICLR 2026) — answer-preserving synthesis; used for cross-niche seeding\",\n    \"SAND-Math (arXiv 2507.20527) — ~38% end-to-end competition synthesis survival\",\n    \"SPARQ (arXiv 2506.06499) — ~25% QD survival (320K→80K); per-niche evidence\",\n    \"DART-Math (arXiv 2407.13690, NeurIPS 2024) — Level 5: 51.1% query dropout; difficulty survival data\",\n    \"FLAMES (arXiv 2508.16514) — ~30% strict survival; Level 5: 50% removal\",\n    \"IndiMathBench (arXiv 2512.00997) — geometry ~3.7× lower autoformalization success; formalization-specific context\",\n    \"VHG (arXiv 2605.06660) — validity gating; inspires verification\",\n    \"Shrinking the Variance (arXiv 2511.03710) — James-Stein shrinkage for RLVR\",\n    \"EBPO (arXiv 2602.05165) — empirical Bayes for GRPO\",\n    \"R-Zero (ICLR 2026) — self-evolving; collapses iter 3\",\n    \"Klear-Reasoner-8B (arXiv 2508.07629) — 90.5% AIME 2024; distillation context\",\n    \"Prism (arXiv 2603.13309) — 128-cluster diversity with ZPD gate\",\n    \"R-Diverse (arXiv 2602.13103) — SAM skill diversity + MAP memory\",\n    \"STAT (arXiv 2510.10023) — Missing-Skill-Profile\",\n    \"Problem Categorization (arXiv 2411.00042) — topic classification\",\n    \"Two-Stage Dynamic View (arXiv 2510.04028) — capability shrinkage then expansion\",\n    \"Does RL Incentivize Reasoning? (NeurIPS 2025, arXiv 2504.13837) — coverage framing\"\n]\n\nDESCRIPTION: \"We propose SACE-RLVR (Structured Archive Co-Evolution for RLVR), scaling online MAP-Elites from GSM-level (DéjàQ) to competition-level math through three core innovations plus four extensions. Two independent motivations for comprehensive coverage: (1) relay-regime theory (arXiv 2602.14872) and balanced difficulty filtering theory (arXiv 2504.03380, EACL 2026: p(1-p) lower bound on policy improvement) suggest smooth difficulty spectra yield faster convergence—adopted as design heuristic, not guarantee, with A3 testing empirically; (2) even under 'sparse policy selection' (1-3% tokens modified), broad coverage prevents 'capability boundary collapse' (RL-PLUS: pass@1↑ pass@128↓; +69.2% with diversity), ensures multiplicative primitive sharpening across domains (Sharper Primitives), and provides the behavioral diversity that is the binding constraint for RL (Tailor: 25 vs 4 primitives). Core 1: 2D archive (10 bins × 5 topics = 50 cells) with proactive gap identification and Bayesian replacement—addresses SAGE's over-specialization at step ~120 (AIME 13.3% = base model, AMC degradation 57.5%→52.5%). Core 2: generate-then-classify synthesis with per-niche survival estimates (central: 30-50%, geometry: 10-20% accounting for ~3.7× autoformalization difficulty ratio from IndiMathBench with formalization-specific caveats, extreme: 3-8%; graceful degradation to min 3/cell; ~142 GPU-hrs/refresh). Core 3: zero-cost Bayesian estimation via G=16 rollout reuse (vs DéjàQ K=100), Beta posterior + credible intervals; G=16 justified by MC-GRPO ablation + gradient starvation analysis (69% degenerate groups at G=4). Key positioning vs. bandit-based curriculum: SEC (17.5% AIME24, Qwen2.5-7B) and Actor-Curator (30.0% AIME24, Qwen2.5-3B, ~9% overhead) demonstrate adaptive selection value but are limited by fixed pool exhaustion, lack of synthesis, and absence of coverage tracking. SACE-RLVR provides what bandits cannot: synthesis for identified gaps, structured coverage guarantees, and persistent cross-step memory. The approaches are potentially complementary—Actor-Curator's bandit sampling from SACE-RLVR's archive tested in E4. Extensions: SvS seeding, shrinkage, DGPO, archive sampling strategy (including Actor-Curator-style variant)—each ablated. Eight baselines (DéjàQ-comp, CLPO, Socratic-Zero, SAGE, Actor-Curator, EVOL-RL, MathForge, GRPO), seven ablations including pass@k capability boundary analysis and selection-vs-synthesis analysis. Concurrent work: UCPO (policy-level diversity, complementary), Vocabulary Dropout (lightweight alternative), SOAR (meta-RL curriculum). Qwen2.5-Math-7B/Qwen3-8B, AIME 2024/2025, MATH-500, AMC, Minerva, OlympiadBench.\"\n\nREVIEWER_RESPONSE: {\n    \"revision_overview\": \"MAJOR REVISION addressing the single blocking issue (SEC/Actor-Curator, unaddressed for 7 rounds) through substantive integration, not surface patching. Six changes: (1) SEC and Actor-Curator added as major landscape section with detailed differentiation on four dimensions (selection vs. synthesis, aggregate vs. structured, stateless vs. persistent, complementarity), (2) Actor-Curator added as 8th baseline with explicit complementarity test, (3) IndiMathBench geometry ratio corrected to ~3.7× with formalization-specific context, (4) SAGE AIME presentation corrected to show base-model matching and AMC degradation, (5) Online Difficulty Filtering cited as theoretical support, (6) UCPO, Vocabulary Dropout, and SOAR added as concurrent work. Extension E4 reframed to explicitly test bandit-archive complementarity.\",\n    \"issue_1_sec_actor_curator_blocking\": \"ADDRESSED SUBSTANTIVELY after 7 rounds. Added as major landscape section ('Bandit-based adaptive curriculum') with full technical details: SEC's MAB formulation (TD(0) on Q-values, Boltzmann sampling, 1D categories, 17.5% AIME24 on Qwen2.5-7B), Actor-Curator's neural bandit (OSMD, per-problem utility, regret O(T^{2/3}·V_T^{1/3}), 30.0% AIME24 on Qwen2.5-3B, ~9% overhead). Four-dimensional differentiation: (a) SELECTION vs. SYNTHESIS—bandits select from fixed 12K pools and cannot create problems targeting identified gaps; as policy improves, useful problems in fixed pool shrink (pool-exhaustion problem); (b) AGGREGATE vs. STRUCTURED—Actor-Curator optimizes aggregate utility without multi-dimensional coverage constraints, risking niche concentration; (c) STATELESS vs. PERSISTENT—no cross-step coverage tracking; (d) COMPLEMENTARITY—Actor-Curator's bandit can serve as within-archive sampling strategy. Actor-Curator added as baseline #5. Extension E4 reframed to test ZPD vs. uniform vs. Actor-Curator-style bandit sampling FROM the archive. New analysis #8 compares selection vs. synthesis: Actor-Curator from fixed pool vs. Actor-Curator-style from SACE-RLVR archive.\",\n    \"issue_2_online_difficulty_filtering\": \"ADDED. Cited in landscape as 'Balanced difficulty filtering theory' (arXiv 2504.03380, EACL 2026). Key result: policy improvement lower-bounded by p(1-p), maximized at p=0.5. +12% AMC, +10% AIME in half training steps. Integrated into Argument 1 as additional theoretical support for difficulty-aware design. Connected to Core 3: our Beta posterior tracks exactly the p(1-p) quantity that this theory shows lower-bounds policy improvement.\",\n    \"issue_3_indimathbench_corrected\": \"FIXED throughout. Changed '6-7× harder' to '~3.7× lower autoformalization success rate (12.2% vs 44.9% BEq)' with explicit caveat: 'IndiMathBench attributes geometry difficulty partly to Mathlib's lacking support for Olympiad-style geometry—a formalization-specific bottleneck that may not fully transfer to problem synthesis difficulty.' Geometry survival estimates revised upward: 10-20% (was 5-15%), with conservative ~2-3× synthesis difficulty estimate. Per-refresh total adjusted: ~2,750-6,000 candidates (was 2,900-7,000), ~142 GPU-hrs (was 162).\",\n    \"issue_4_sage_aime_corrected\": \"FIXED. Now explicitly states: 'SAGE achieves 13.3% AIME 2024—matching the Qwen-2.5-7B base model (also 13.3%)—and degrades AMC 2023 from 57.5% to 52.5%.' Added interpretation: 'flat unstructured pools can improve narrow in-distribution metrics while failing or degrading competition-level OOD performance—precisely the over-specialization that structured archive-based diversity maintenance prevents.' This stronger framing makes a more compelling case for our approach.\",\n    \"issue_5_ucpo_concurrent\": \"ADDED. Full landscape entry for UCPO (arXiv 2605.00365): conditional uniformity penalty on correct solutions, +10% absolute Pass@64 AIME24 (DeepSeek-7B: 70%→80%), +45% equation diversity. Key differentiation: UCPO modifies loss function (policy-level diversity), SACE-RLVR modifies training distribution (data-level diversity)—orthogonal and potentially complementary. Added to evaluation discussion: analysis #6 now compares data-level vs. policy-level diversity approaches.\",\n    \"issue_6_vocab_dropout_soar\": \"ADDED. Vocabulary Dropout (arXiv 2604.03472): hard logit masking on proposer, +4.4 avg on Qwen3-8B, +10.9 AMC. Lightweight alternative demonstrating diversity collapse is real bottleneck. SOAR (arXiv 2601.18778): bi-level meta-RL teacher, +9.3% pass@32 on fail@128, 75% oracle recovery. Conceptually parallel to our gap identification but uses meta-RL reward signal vs. archive structure. Both added as brief concurrent work entries.\",\n    \"score_trajectory_note\": \"This revision addresses the #1 blocking issue (SEC/Actor-Curator) that has been persistent for 7 rounds, which the reviewer identified as 'the single blocking issue' for passing. The integration is substantive—not just adding citations but developing a four-dimensional differentiation framework and an explicit complementarity test. The corrected SAGE presentation (AIME = base model, AMC degradation) actually STRENGTHENS our case for structured archives. Online Difficulty Filtering's p(1-p) result provides independent theoretical support for our Bayesian learnability criterion.\"\n}\n\nPlease assemble all these fields into a single valid JSON object. Make sure to properly escape all special characters in strings. The resource_estimate should be nested as shown. The reviewer_response should be nested as shown. Output only the JSON.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aa37bc8-8f6f-48cd-8c1d-a015354fecdd",
  "isSidechain": false,
  "requestId": "req_011CbUEesbRNrET74782AdR8",
  "type": "assistant",
  "uuid": "bf933e40-7ca1-4514-850e-493c573bf324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7brWSsBoseiNuC4K3XMnz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12082,
      "cache_read_input_tokens": 44005,
      "output_tokens": 15527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15527,
          "cache_read_input_tokens": 44005,
          "cache_creation_input_tokens": 12082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12082
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

_source line 85 · 2026-05-28T03:18:47.649Z_

<details><summary>↩ Tool result · reported error · `toolu_013eV9kAMh3tKhd5y1Bj6DJd`</summary>

```text
Cannot create agent worktree: not in a git repository and no WorktreeCreate hooks are configured. Configure WorktreeCreate/WorktreeRemove hooks in settings.json to use worktree isolation with other VCS systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf933e40-7ca1-4514-850e-493c573bf324",
  "isSidechain": false,
  "promptId": "7df2c4c1-25bc-493a-9f22-0fe9c2b8ff2d",
  "type": "user",
  "uuid": "53492fc4-dc0b-41dc-b36f-3ecf399153d5",
  "toolUseResult": "Error: Cannot create agent worktree: not in a git repository and no WorktreeCreate hooks are configured. Configure WorktreeCreate/WorktreeRemove hooks in settings.json to use worktree isolation with other VCS systems.",
  "sourceToolAssistantUUID": "bf933e40-7ca1-4514-850e-493c573bf324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 86 · 2026-05-28T03:18:47.727Z_

```json
{
  "parentUuid": "53492fc4-dc0b-41dc-b36f-3ecf399153d5",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1d22d0bc-5a44-47e0-b240-b8fb9493c574",
  "timestamp": "2026-05-28T03:18:47.727Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "1d22d0bc-5a44-47e0-b240-b8fb9493c574",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Assistant

_source line 89 · 2026-05-28T03:18:52.321Z_

<details><summary>Logged reasoning block</summary>

```text
The agent failed due to no git repository. Let me just construct the JSON directly myself. I'll output it as a complete JSON object.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d22d0bc-5a44-47e0-b240-b8fb9493c574",
  "isSidechain": false,
  "requestId": "req_011CbUF81CKxCDdisk8iWs8p",
  "type": "assistant",
  "uuid": "8c45496c-982a-4596-88dc-940a0466170f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTrAAVxvme924KwYYWs1B6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15695,
      "cache_read_input_tokens": 56087,
      "output_tokens": 15144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15144,
          "cache_read_input_tokens": 56087,
          "cache_creation_input_tokens": 15695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15695
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

_source line 90 · 2026-05-28T03:24:38.796Z_

Let me construct the complete JSON directly.

```json
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
  "change_type": "major",
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
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c45496c-982a-4596-88dc-940a0466170f",
  "isSidechain": false,
  "requestId": "req_011CbUF81CKxCDdisk8iWs8p",
  "type": "assistant",
  "uuid": "0b8a70e3-3a30-483a-a34c-38e811c91c25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTrAAVxvme924KwYYWs1B6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15695,
      "cache_read_input_tokens": 56087,
      "output_tokens": 15144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15144,
          "cache_read_input_tokens": 56087,
          "cache_creation_input_tokens": 15695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15695
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

_source line 91_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "0b8a70e3-3a30-483a-a34c-38e811c91c25",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 93_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Structured Archive Co-Evolution for Competition-Level RLVR: Scaling Qu…",
  "leafUuid": "0b8a70e3-3a30-483a-a34c-38e811c91c25",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---

### Runtime record

_source line 94_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising SACE-RLVR after round 8 reviewer feedback",
  "sessionId": "e35f6048-c4fa-4353-9c1d-67bd6bba68b4"
}
```

---
