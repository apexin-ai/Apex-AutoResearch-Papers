# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Model Uncertainty vs. User Trust 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1.jsonl`
- **Structured JSON:** [`fe04ec3837d0e3115f80.json`](../../sessions/fe/fe04ec3837d0e3115f80.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:45:32.377Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:45:32.377Z",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Making\n\n## Description\nWe propose the first head-to-head comparison of model uncertainty and user trust as gating signals for adaptive dual explanation presentation in LLM-assisted decision-making. Building on three convergent findings—that dual explanations are the only explanation type genuinely reducing overreliance (2605.10930), that trust-gated counter-explanations cut inappropriate reliance by 38% but require obtrusive self-reports and accuracy feedback (Adjust for Trust, IUI 2026), and that displaying uncertainty directly to users backfires by increasing algorithm aversion (Bo et al., CHI 2025)—we test whether automatic model uncertainty can serve as a practical, first-interaction-ready *backend* gating signal that selects explanation type without burdening users. The system uses a validated hybrid uncertainty estimator (semantic entropy + Probability of Correctness probe over Qwen3-30B-A3B's shared residual stream representations, addressing both the 'confidently wrong' regime identified by 2603.21172 and MoE-specific probing considerations) to selectively trigger dual explanations when model error is likely. The uncertainty threshold is set via Youden's J-optimal cutpoint with cross-validated calibration, and triggering rates are verified against the trust-gated condition in a pilot study. A preregistered between-subjects study (N≈560, Prolific) compares four conditions across 30 general-knowledge questions: no explanation, always-on dual explanation, trust-gated dual explanation (replicating the Adjust for Trust mechanism with trust ≥ 8 threshold), and uncertainty-gated dual explanation. We measure overreliance reduction, discrimination accuracy, appropriate reliance ratio, cognitive load, and satisfaction. The central hypothesis (H2) tests non-inferiority of uncertainty-gating via TOST with a pre-registered equivalence margin of Cohen's d = 0.35 (≈7 percentage points on overreliance rate), justified by cost-benefit SESOI reasoning: below this threshold, uncertainty-gating's deployment advantages (no surveys, no feedback dependency, first-interaction readiness) outweigh any effectiveness loss. Power analysis confirms N=140/group provides 80% power for TOST at d = 0.35 (Lakens, 2017). Analysis uses GLMMs with crossed random effects for participants and items (Baayen et al., 2008; Westfall et al., 2014) to account for question-specific variance. Unlike prior adaptive approaches that require learned user models from prior interactions (Li et al., CHI 2025), our uncertainty-gated condition requires no user state measurement and works from the first interaction. Uniquely, we include a fairness analysis—motivated by 'Unequal Uncertainty' (2508.07872)—examining whether uncertainty-gated interventions trigger disproportionately across demographic groups. We explicitly acknowledge the ecological validity limitation that accuracy feedback (provided for comparability) is rarely available in deployment, and argue—supported by Okamura & Yamada (CHI 2024)—that uncertainty-gating's relative advantage is likely *larger* in practice because trust calibration degrades without feedback while uncertainty-gating is feedback-independent. This work bridges uncertainty quantification in NLP with adaptive explanation design in HCI, offering both a principled comparison of gating strategies and a deployable framework that requires no user state measurement.\n\n## Core Problem\nWhich gating signal—model uncertainty (automatic, available from first interaction) or user trust (self-reported, requiring repeated measurement)—better governs when to present dual explanations for reducing LLM overreliance, and does uncertainty-based gating introduce demographic fairness risks through differential triggering?\n\n## Opportunity\nTwo recent lines of work create a convergent opportunity. First, the 'false trust' study (2605.10930, May 2026) establishes that dual explanations (pro + contra arguments) are the *only* explanation type that genuinely improves users' ability to distinguish correct from incorrect LLM outputs—all other types merely increase acceptance. Second, 'Adjust for Trust' (2502.13321, IUI 2026) demonstrates that adaptively triggering counter-explanations based on user trust reduces inappropriate reliance by up to 38%. However, their approach requires obtrusive trust self-reports after every decision and real-time accuracy feedback—conditions rarely met in deployment. Their own analysis reveals that predicting trust from behavioral signals alone achieves F1 ≤ 0.5, making passive trust detection impractical, and they explicitly acknowledge that 'a key assumption of our setup does not hold in most real-world settings: that both parties have access to real-time feedback about decision accuracy.' Model uncertainty offers a complementary gating signal: it is computed automatically, requires no user input, works from the first interaction, and—critically—does not depend on accuracy feedback for calibration. Yet no work has empirically compared these two gating strategies. Meanwhile, 'The Persuasion Paradox' (2604.03237) shows that explanation effectiveness is strongly task-dependent—explanations help for language-based reasoning (72.5% accuracy vs. 48.5% baseline on LSAT) but hurt for visual reasoning—suggesting that uncertainty-gated explanation switching is most valuable precisely for the knowledge QA domain where explanations are effective. Critically, 'To Rely or Not to Rely?' (2412.15584, CHI 2025) finds that *displaying* uncertainty to users (via token-level probability highlighting) actually backfires—increasing algorithm aversion without improving appropriate reliance. This counter-evidence is important because it shows that uncertainty information is counterproductive when presented directly to users, but it does not indict using uncertainty as a *backend gating signal* to select which explanation type to present. Indeed, it strengthens the case for our approach: rather than burdening users with uncertainty visualization, we use uncertainty behind the scenes to select the more effective dual explanation format when model error is likely. The missing piece remains a head-to-head comparison that determines when model uncertainty outperforms, matches, or falls short of trust-based gating, while also measuring the fairness implications that 'Unequal Uncertainty' (2508.07872) warns about.\n\n## Landscape\nThe false trust paper (2605.10930, May 2026) establishes dual explanations as uniquely effective but tested them uniformly. 'Adjust for Trust' (2502.13321, IUI 2026) is the closest prior work on gating strategy: it gates between supporting and counter-explanations based on self-reported user trust (11-point scale, 0-10), achieving 38% reduction in inappropriate reliance and 20% accuracy improvement across science QA and medical diagnosis with 30 trials per participant. Critically, their trust measurement requires accuracy feedback after each trial and explicit trust surveys—conditions that limit deployment scalability. Their trust threshold (≥8 on 0-10 scale for counter-explanations) was set by visual inspection of reliance curves, not formal optimization. Their attempt to predict trust from interaction features yielded F1 ≤ 0.5. 'From Text to Trust' (Li et al., 2502.11919, CHI 2025) is the closest prior work on adaptive explanation selection: they use a dynamic programming framework with a learned human behavior model to selectively decide which LLM-generated feature analyses to present for tabular AI predictions (income, recidivism; N=447 and N=397, 15 trials per participant), significantly improving appropriate reliance versus always-on and control conditions. However, their approach differs from ours in three key respects: (1) it requires prior interaction data to train the behavior model (cold-start problem), (2) it operates on tabular feature-level analyses rather than natural-language dual explanations, and (3) their gating is based on predicted utility of each analysis rather than on model uncertainty or user trust as explicit signals. Our work complements theirs by comparing two deployment-practical gating signals (model uncertainty and self-reported trust) for a different intervention type (dual pro/contra explanations) in knowledge QA. 'To Rely or Not to Rely?' (Bo et al., 2412.15584, CHI 2025) benchmarks three reliance interventions on N=400 participants across LSAT and image estimation (only 4 trials per participant): Reliance Disclaimer (static warning text), Uncertainty Highlighting (red/pink token-level probability visualization), and Implicit Answer (removing explicit answer statements). Their central finding is sobering: while interventions reduce over-reliance, they generally fail to improve *appropriate* reliance—only Reliance Disclaimer improves the Appropriate Reliance Ratio, and only on LSAT (ARR=1.62 vs. 1.17 control, p=.04). Uncertainty Highlighting specifically backfired, significantly reducing perceived accuracy and helpfulness and increasing algorithm aversion rather than calibrating reliance. This is critical counter-evidence that our approach must address. The key distinction is mechanistic: Bo et al.'s Uncertainty Highlighting *displays* uncertainty information to users, imposing cognitive burden and triggering aversion. Our uncertainty-gated approach uses uncertainty as a *backend signal* to select explanation type—users never see uncertainty scores; they see adaptively selected explanation content. Furthermore, their interventions (disclaimer, highlighting, implicit answer) are simpler cognitive forcing mechanisms, whereas our dual explanation (pro + contra arguments) is the only format shown to genuinely improve discrimination ability (2605.10930). 'Selectively Providing Reliance Calibration Cues' (2302.09995) predicts human reliance behavior to selectively present calibration cues, but uses a learned user model rather than model uncertainty and does not switch explanation types. 'The Persuasion Paradox' (2604.03237) finds that uncertainty-based selective automation outperforms explanations for visual reasoning, but their own results show LLM explanations dramatically improve performance on language-based tasks (LSAT: 72.5% vs. 48.5%), supporting explanation-type switching for knowledge QA. 'Contrastive Explanations That Anticipate Misconceptions' (2410.04253, CHI 2025) generates explanations addressing the gap between AI and user reasoning (N=628, improves decision skills), but applies them uniformly without selective gating. 'Don't Just Translate, Agitate' (2504.12424) proposes LLMs as devil's advocates for XAI but is a position paper without empirical evaluation. 'Why Not Both?' (Frontiers 2025) shows explanations and uncertainty estimates serve complementary roles—uncertainty improves accuracy while explanations improve understanding—supporting the value of combining both signals. 'Unequal Uncertainty' (2508.07872) provides the first socio-technical and legal analysis of uncertainty-gated interventions, showing they can disproportionately affect underrepresented groups through differential triggering rates, creating fairness and legal risks under UK Equality Act 2010. 'Entropy Alone is Insufficient' (2603.21172) demonstrates that semantic entropy has a 'confidently wrong regime' and combining it with a Probability of Correctness probe substantially improves reliability. 'Revisiting Uncertainty Estimation' (2505.23854) shows LLMs have better calibration on reasoning tasks than knowledge-heavy ones across 80 models, and that good calibration does not guarantee effective error ranking—necessitating explicit validation for our QA domain. 'LLMs Should Express Uncertainty Explicitly' (2604.05306) proposes verbalized confidence and reasoning-time uncertainty markers, achieving improved calibration. 'Dissenting Explanations' (AAAI 2024) leverages model multiplicity for disagreeing explanations but applies them uniformly. Partial explanations (de Jong et al., PACM HCI 2025) reduce overreliance through cognitive forcing but do not modulate explanation type. 'Framework for Machine Evaluation of Reasoning Completeness' (Patil, 2510.21884) introduces the RACE framework evaluating alignment between LLM explanations and interpretable feature importance, finding a 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues—relevant context for understanding how explanation quality may covary with model correctness. Multi-AI panel work (2603.22152) finds single dissent reduces conformity while broad disagreement confuses. Uncertainty Gating for Cost-Aware XAI (2603.29915) uses epistemic uncertainty to gate explanation methods for ML classifiers, not human overreliance; notably, they use percentile-based thresholds calibrated per dataset across ν ∈ {0.1, 0.3, 0.5, 0.7, 0.9}. No existing work directly compares model uncertainty and user trust as competing gating signals for adaptive explanation presentation in LLM-assisted decision-making.\n\n## Approach\nThe study proceeds in two phases. **Phase 1: Uncertainty Signal Validation.** Before any human-subjects work, we validate the gating signal on our specific task. Using Qwen3-30B-A3B—a Mixture-of-Experts model with 30.5B total parameters but only 3.3B activated per token (128 experts/layer, 8 selected per token)—we generate answers to 200 candidate general-knowledge questions and compute semantic entropy over 10 sampled completions per question. Semantic entropy operates on output-level semantics (clustering sampled completions by meaning), so it is unaffected by MoE routing variability. Following 'Entropy Alone is Insufficient' (2603.21172), we also train a lightweight Probability of Correctness (PC) probe on Qwen3-30B-A3B's hidden-state activations using a held-out set. For the PC probe specifically, we address MoE-specific considerations: we probe the shared residual stream representations (post-attention, pre-MoE routing) rather than post-expert states, avoiding the routing variability where different tokens activate different expert subsets. We validate probe stability by measuring variance across multiple forward passes on identical inputs, since MoE routing is deterministic for greedy decoding but may vary under sampling. Alternatively, we can adopt the Semantic Entropy Probes approach (Kossen et al., 2024), which approximates semantic entropy from single-generation hidden states, eliminating the need for multiple samples entirely. We combine semantic entropy and PC probe scores via logistic regression to produce a hybrid uncertainty signal. We require AUROC ≥ 0.75 for distinguishing correct from incorrect answers before proceeding; if this threshold is not met, we evaluate alternative models (Llama-4-Scout-17B, Mixtral-8x22B) or uncertainty methods (semantic energy, verbalized confidence per 2604.05306). **Threshold calibration:** The uncertainty gating threshold is set at the Youden's J optimal cutpoint (maximizing sensitivity + specificity − 1) on Phase 1 validation data, with bootstrap 95% CI for the cutpoint to quantify threshold uncertainty. Cross-validation (leave-20%-out) prevents overfitting on the 200-question set. From validated questions, we select 30 for the main study (15 where the model is correct, 15 where it is incorrect, balanced across uncertainty levels and topic domains). The increase from 20 to 30 items matches the 'Adjust for Trust' protocol (30 trials per participant) and provides sufficient levels for stable item-level random effects estimation in the GLMM analysis (Westfall, Kenny, & Judd, 2014, show that with ≤8 items, maximal attainable power is <0.5 regardless of participant N; 30 items is well above this threshold and above the ≥5-level minimum recommended by Gelman & Hill, 2006). **Phase 2: Comparative User Study.** A preregistered between-subjects study (N≈560, 140 per condition) on Prolific with four conditions: (1) **No explanation**—LLM answer only; (2) **Always-on dual explanation**—every answer includes structured pro and contra arguments (replicating the effective condition from 2605.10930); (3) **Trust-gated dual explanation**—participants report trust on an 11-point scale (0-10) after each of the 30 trials; when trust exceeds 8 (adopting the 'Adjust for Trust' threshold, which was empirically calibrated against reliance behavior), the next trial presents dual explanation, otherwise single explanation; (4) **Uncertainty-gated dual explanation**—when the hybrid uncertainty signal exceeds the Youden's J-optimal threshold from Phase 1, dual explanation is presented; otherwise single explanation. **Triggering rate calibration:** In the pilot study (N=60, 15 per condition), we compare empirical triggering rates between Conditions 3 and 4. If rates differ by >15 percentage points, we adjust the uncertainty threshold to the percentile that approximately matches the trust-gated triggering rate, reporting both Youden-optimal and rate-matched thresholds as sensitivity analyses. This ensures condition comparability while preserving transparency about any threshold adjustment. Crucially, unlike the Uncertainty Highlighting intervention in Bo et al. (2412.15584) which *displays* token-level probability information to users (and backfired by increasing algorithm aversion), our uncertainty-gated condition uses uncertainty purely as a backend signal—participants see only the selected explanation format, never the uncertainty estimate itself. This design choice is directly informed by Bo et al.'s finding that user-facing uncertainty visualization is counterproductive. All conditions receive accuracy feedback after each trial (following 'Adjust for Trust' protocol, ensuring comparability). Dual explanations are generated via Claude API with structured prompting (pro: 3-4 sentences supporting the answer; contra: 2-3 sentences presenting the strongest counter-argument and alternative answer), with human review for quality. **Measures**: Primary—overreliance rate (accepting incorrect AI answers), discrimination accuracy (AUROC of accept/reject decisions vs. correctness), appropriate reliance (composite of over- and under-reliance, following the Appropriate Reliance Ratio from Bo et al., 2412.15584). Secondary—cognitive load (NASA-TLX), task completion time, subjective satisfaction (7-point Likert), perceived AI competence. **Analysis plan**: Generalized linear mixed model (GLMM) with a logit link for trial-level accept/reject decisions, including crossed random intercepts for participants and items (questions), and random slopes for condition by item to capture differential treatment effects across questions (following Baayen, Davidson, & Bates, 2008; Westfall, Kenny, & Judd, 2014). Fixed effects: condition (4 levels), item correctness (correct/incorrect), and their interaction. Participant-level covariates: age, education, domain knowledge (pre-test). This approach accounts for item-level variance (question difficulty, topic familiarity) that would otherwise inflate Type I error if items were treated as fixed (Judd, Westfall, & Kenny, 2012). **Equivalence testing specification (H2)**: We use Two One-Sided Tests (TOST; Lakens, 2017) with a pre-registered equivalence margin of Cohen's d = 0.35, justified by cost-benefit SESOI reasoning (Lakens, Scheel, & Isager, 2018): this represents the maximum effectiveness difference at which uncertainty-gating's deployment advantages—no user surveys, no accuracy feedback dependency, first-interaction readiness—still outweigh the performance loss versus trust-gating. In raw terms, d = 0.35 corresponds to approximately 7 percentage points on overreliance rate (assuming participant-level SD ≈ 0.20), meaning we accept non-inferiority if uncertainty-gating's overreliance rate is no more than 7pp higher than trust-gating's. As sensitivity analyses, we also report equivalence tests at d = 0.25 (stricter) and d = 0.50 (more lenient) to demonstrate robustness to margin specification. **Power analysis**: For H2 (TOST non-inferiority, d = 0.35 bounds, α = 0.05): N = 140 per group provides ~80% power (computed via TOSTER::power_t_TOST; consistent with Lakens, 2017, Table 1: d = 0.30 requires N = 191/group, d = 0.40 requires N = 108/group, interpolating to ~140 for d = 0.35). For H1 and H3 (superiority tests, expected d ≈ 0.50 based on 'Adjust for Trust' effect sizes): N = 140 per group provides >95% power. Total sample: N = 560 (140 per condition). **Fairness analysis** (RQ3, addressing 'Unequal Uncertainty'): We collect demographic data (gender, race/ethnicity, education, English proficiency) and analyze whether uncertainty-gated dual explanations trigger at different rates for questions where demographic knowledge gaps exist, whether differential triggering correlates with demographics, and whether any differential triggering translates to differential overreliance reduction. **Key hypotheses**: H1—Conditions 3 and 4 both reduce overreliance compared to Condition 1; H2—Condition 4 (uncertainty-gated) achieves non-inferior overreliance reduction compared to Condition 3 (trust-gated), tested via TOST with equivalence margin d = 0.35; H3—Condition 4 produces lower cognitive load and higher satisfaction than Condition 2 (always-on dual); H4—Condition 4 incurs no measurement burden (no trust surveys), making it more practical; H5—Uncertainty-gated triggering rates do not differ significantly across demographic groups (fairness hypothesis, tested as a secondary analysis with appropriate corrections for multiple comparisons). **Ecological validity limitation**: Accuracy feedback after every trial, while necessary for the trust-gated condition (Condition 3) and provided to all conditions for comparability, is rarely available in real-world deployment. The 'Adjust for Trust' authors explicitly acknowledge this limitation. Okamura and Yamada (CHI 2024, arXiv 2111.08222) demonstrate that outcome feedback substantially improves trust calibration, while interpretability alone does not—implying that trust-gating's effectiveness degrades in feedback-free settings. Critically, uncertainty-gating is feedback-independent: the model computes uncertainty from its own outputs regardless of whether users receive outcome information. This means our study likely *underestimates* uncertainty-gating's relative advantage over trust-gating in deployment, because the experimental feedback supports trust calibration that would be absent in practice. We discuss this asymmetry as a key deployment implication: in feedback-scarce environments (the norm for most LLM-assisted decisions), uncertainty-gating may be the *only* viable adaptive strategy, as trust-gating without feedback relies on potentially miscalibrated self-reports that the 'Adjust for Trust' authors themselves note may reflect 'potentially incorrect perceptions of expertise.' A follow-up study varying feedback availability (present vs. absent) across both gating conditions would directly quantify this interaction and is identified as priority future work.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '300-400 (Qwen3-30B-A3B hosting for Phase 1 validation: ~2K questions × 10 samples + PC probe training on shared residual stream representations; Phase 2: ~10K inference calls × 10 samples for pilot + main study on A100-80GB; note Qwen3-30B-A3B activates only 3.3B parameters per token, reducing per-inference cost vs. dense 30B models)', 'timeline': '5-7 months (Month 1: system build + Phase 1 uncertainty validation + threshold calibration; Month 2: IRB submission + pilot design; Month 3: IRB approval + pilot N=60 + triggering rate calibration; Month 4: pilot analysis + main study refinement; Month 5: main study N≈560; Month 6-7: analysis + writing; aggressive 4.5-month variant possible if IRB uses expedited review for minimal-risk online study)', 'estimated_gpu_cost': '$700-1000 (A100 at ~$3/hr; MoE efficiency reduces per-inference cost)'}, 'human_in_loop': {'gpu_hours': '200-300 (Claude API generates candidate explanations and counter-arguments; GPU only for Qwen3-30B-A3B uncertainty estimation and PC probe training)', 'timeline': '4.5-6 months (Claude accelerates explanation generation, stimulus quality control, statistical modeling, and fairness analysis code)', 'claude_api_cost': '$600-900 (explanation generation for 200 candidate + 30 final questions × 4 conditions × multiple pilot rounds, plus analysis assistance)', 'estimated_gpu_cost': '$500-750'}, 'auto_research': {'gpu_hours': '200-300', 'timeline': '4.5-6 months minimum', 'claude_api_cost': '$900-1400 (automated stimulus optimization, power analysis simulation, equivalence testing code, fairness analysis, draft writing)', 'estimated_gpu_cost': '$500-750', 'speed_bottleneck': 'IRB approval (4-8 weeks, expedited review possible for minimal-risk online survey) and Prolific data collection (~2-3 weeks for N=560) are non-automatable; participant compensation ~$6,200-7,000 (560 participants × ~40 min average session × $12/hr Prolific recommended minimum + 33.3% Prolific academic service fee + ~10% buffer for rejections/replacements; Condition 3 sessions may extend to ~45 min due to trust surveys after each of 30 trials); trust measurement in Condition 3 requires interactive protocol that may extend session duration'}}\n\n## Inspired By\nThe 'Adjust for Trust' finding that trust-gated counter-explanations reduce overreliance by 38%—combined with their own limitation that trust cannot be reliably predicted from behavior (F1 ≤ 0.5) and their acknowledgment that accuracy feedback is unavailable in most deployment settings—directly motivates testing model uncertainty as a practical alternative gating signal. The convergence of (1) dual explanations as uniquely effective (2605.10930), (2) adaptive gating as effective but trust-measurement-limited (2502.13321), (3) adaptive explanation selection as effective but requiring learned user models (2502.11919), (4) 'Entropy Alone is Insufficient' showing hybrid uncertainty signals improve reliability (2603.21172), (5) uncertainty *display* backfiring while the underlying signal remains informative (2412.15584), and (6) 'Unequal Uncertainty' raising fairness concerns about uncertainty-gated interventions (2508.07872) creates a well-motivated research question that no single prior paper addresses.\n\n## Target Venues\n- CHI 2027 (paper deadline Sep 10, 2026 — aggressive but achievable with 4.5-month timeline if Phase 1 validates quickly and IRB uses expedited review; flagship HCI venue, strong fit for adaptive AI-assisted decision-making comparison study; revise-and-resubmit process available)\n- CSCW 2027 (rolling submission from Jan 2027 — comfortable primary target if CHI 2027 timeline proves too tight; strongest fit for adaptive AI-assisted decision-making with fairness analysis; 3-4 month review cycle)\n- FAccT 2027 (estimated deadline ~Jan 2027 — fairness analysis of uncertainty-gated interventions is strong fit; equity framing as secondary contribution)\n- CHI 2028 (paper deadline ~Sep 2027 — safe fallback if earlier venues require major revision)\n\n## Key References\n- Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (IUI 2026, arXiv 2502.13321) — *primary point of differentiation*: trust-gated adaptive counter-explanations, 38% reduction in inappropriate reliance, 30 trials/participant, trust ≥ 8 threshold; our Condition 3 replicates their mechanism\n- Evaluating the False Trust engendered by LLM Explanations (arXiv 2605.10930, May 2026) — establishes dual explanations as uniquely effective; motivates explanation type selection\n- From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis (Li et al., CHI 2025, arXiv 2502.11919) — dynamic programming framework with learned human behavior model for selectively presenting LLM-generated feature analyses (N=447, N=397, 15 trials/participant); improves appropriate reliance on tabular AI tasks; differs from our work in requiring prior interaction data, operating on feature-level analyses rather than dual explanations, and using predicted utility rather than model uncertainty or trust as gating signal\n- To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models (Bo et al., CHI 2025, arXiv 2412.15584) — benchmarks three reliance interventions (Reliance Disclaimer, Uncertainty Highlighting, Implicit Answer) on N=400 (only 4 trials/participant); finds interventions generally fail to improve appropriate reliance; Uncertainty Highlighting specifically backfires by increasing algorithm aversion; *critical counter-evidence* that motivates our backend-gating design: we use uncertainty to select explanation type, never displaying it to users; Appropriate Reliance Ratio adopted as primary metric\n- The Persuasion Paradox: When LLM Explanations Fail to Improve Human-AI Team Performance (arXiv 2604.03237) — shows explanation effectiveness is task-dependent; supports explanation switching for language-based QA while selective automation is better for visual tasks\n- Selectively Providing Reliance Calibration Cues With Reliance Prediction (arXiv 2302.09995) — selective intervention via predicted reliance behavior; differs in gating signal (user model vs. model uncertainty) and intervention type (calibration cues vs. explanation switching)\n- Contrastive Explanations That Anticipate Human Misconceptions (CHI 2025, arXiv 2410.04253) — human-centered contrastive explanations improve decision skills (N=628); applied uniformly, not selectively gated\n- Don't Just Translate, Agitate: Using LLMs as Devil's Advocates for AI Explanations (arXiv 2504.12424) — position paper proposing LLMs as constructive agitators; no empirical evaluation\n- Why Not Both? Complementing Explanations with Uncertainty (Frontiers in Computer Science 2025) — shows explanations and uncertainty serve complementary roles; supports combining both signals\n- Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI (arXiv 2508.07872) — fairness risks of uncertainty-gated interventions; directly motivates our RQ3 fairness analysis\n- Entropy Alone is Insufficient for Safe Selective Prediction in LLMs (arXiv 2603.21172) — demonstrates 'confidently wrong' regime of semantic entropy; motivates our hybrid SE + PC probe approach\n- Revisiting Uncertainty Estimation and Calibration of Large Language Models (arXiv 2505.23854) — shows calibration varies across 80 models, worse on knowledge vs. reasoning tasks; motivates Phase 1 validation\n- LLMs Should Express Uncertainty Explicitly (arXiv 2604.05306) — verbalized confidence and reasoning-time uncertainty markers improve calibration; alternative uncertainty elicitation if SE fails validation\n- To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance (CSCW 2021) — establishes effectiveness-usability tradeoff in CFF interventions\n- An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, January 2026) — Assumption CFF reduces overreliance but decreases satisfaction\n- Cognitive Forcing for Better Decision-Making: Reducing Overreliance Through Partial Explanations (PACM HCI 2025) — partial explanations as cognitive forcing; no uncertainty-based modulation\n- Dissenting Explanations: Leveraging Disagreement to Reduce Model Overreliance (AAAI 2024) — model multiplicity for disagreeing explanations; applied uniformly without selective gating\n- More Isn't Always Better: Balancing Decision Accuracy and Conformity Pressures in Multi-AI Advice (arXiv 2603.22152) — single dissent reduces conformity; supports targeted rather than blanket counter-argumentation\n- Uncertainty Gating for Cost-Aware Explainable AI (arXiv 2603.29915) — uses epistemic uncertainty to gate explanation methods for ML classifiers with percentile-based thresholds; analogous mechanism but entirely different application domain\n- Framework for Machine Evaluation of Reasoning Completeness in Large Language Models for Classification Tasks (Patil, arXiv 2510.21884) — RACE framework evaluating explanation-feature alignment; finds 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues; relevant context for understanding explanation quality covariation with model correctness\n- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (Kossen et al., arXiv 2406.15927) — approximates semantic entropy from single-generation hidden states, reducing computational overhead to near zero; potential efficiency improvement for Phase 1 uncertainty estimation\n- Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (Lakens, 2017, Social Psychological and Personality Science) — TOST procedure and power analysis tables; our equivalence margin and power calculations follow this framework\n- Equivalence Testing for Psychological Research: A Tutorial (Lakens, Scheel, & Isager, 2018, AMPPS) — SESOI justification approaches including cost-benefit analysis; grounds our d = 0.35 margin choice\n- Statistical Power and Optimal Design in Experiments in Which Samples of Participants Respond to Samples of Stimuli (Westfall, Kenny, & Judd, 2014, JEP:General) — power analysis for crossed random effects designs; shows ≤8 items cap maximal power at <0.5; motivates our 30-item stimulus set\n- Mixed-Effects Modeling with Crossed Random Effects for Subjects and Items (Baayen, Davidson, & Bates, 2008, J Memory & Language) — methodological foundation for our GLMM analysis plan with crossed random effects for participants and items\n- Adaptive Trust Calibration for Human-AI Collaboration (Okamura & Yamada, CHI 2024, arXiv 2111.08222) — directly compares feedback vs. no-feedback conditions; shows outcome feedback substantially improves trust calibration while interpretability alone does not; grounds our ecological validity discussion\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:45:32.383Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:45:32.383Z",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

## Round 1

51 recorded events

### User

_source line 3 · 2026-05-20T04:45:32.398Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Making

## Description
We propose the first head-to-head comparison of model uncertainty and user trust as gating signals for adaptive dual explanation presentation in LLM-assisted decision-making. Building on three convergent findings—that dual explanations are the only explanation type genuinely reducing overreliance (2605.10930), that trust-gated counter-explanations cut inappropriate reliance by 38% but require obtrusive self-reports and accuracy feedback (Adjust for Trust, IUI 2026), and that displaying uncertainty directly to users backfires by increasing algorithm aversion (Bo et al., CHI 2025)—we test whether automatic model uncertainty can serve as a practical, first-interaction-ready *backend* gating signal that selects explanation type without burdening users. The system uses a validated hybrid uncertainty estimator (semantic entropy + Probability of Correctness probe over Qwen3-30B-A3B's shared residual stream representations, addressing both the 'confidently wrong' regime identified by 2603.21172 and MoE-specific probing considerations) to selectively trigger dual explanations when model error is likely. The uncertainty threshold is set via Youden's J-optimal cutpoint with cross-validated calibration, and triggering rates are verified against the trust-gated condition in a pilot study. A preregistered between-subjects study (N≈560, Prolific) compares four conditions across 30 general-knowledge questions: no explanation, always-on dual explanation, trust-gated dual explanation (replicating the Adjust for Trust mechanism with trust ≥ 8 threshold), and uncertainty-gated dual explanation. We measure overreliance reduction, discrimination accuracy, appropriate reliance ratio, cognitive load, and satisfaction. The central hypothesis (H2) tests non-inferiority of uncertainty-gating via TOST with a pre-registered equivalence margin of Cohen's d = 0.35 (≈7 percentage points on overreliance rate), justified by cost-benefit SESOI reasoning: below this threshold, uncertainty-gating's deployment advantages (no surveys, no feedback dependency, first-interaction readiness) outweigh any effectiveness loss. Power analysis confirms N=140/group provides 80% power for TOST at d = 0.35 (Lakens, 2017). Analysis uses GLMMs with crossed random effects for participants and items (Baayen et al., 2008; Westfall et al., 2014) to account for question-specific variance. Unlike prior adaptive approaches that require learned user models from prior interactions (Li et al., CHI 2025), our uncertainty-gated condition requires no user state measurement and works from the first interaction. Uniquely, we include a fairness analysis—motivated by 'Unequal Uncertainty' (2508.07872)—examining whether uncertainty-gated interventions trigger disproportionately across demographic groups. We explicitly acknowledge the ecological validity limitation that accuracy feedback (provided for comparability) is rarely available in deployment, and argue—supported by Okamura & Yamada (CHI 2024)—that uncertainty-gating's relative advantage is likely *larger* in practice because trust calibration degrades without feedback while uncertainty-gating is feedback-independent. This work bridges uncertainty quantification in NLP with adaptive explanation design in HCI, offering both a principled comparison of gating strategies and a deployable framework that requires no user state measurement.

## Core Problem
Which gating signal—model uncertainty (automatic, available from first interaction) or user trust (self-reported, requiring repeated measurement)—better governs when to present dual explanations for reducing LLM overreliance, and does uncertainty-based gating introduce demographic fairness risks through differential triggering?

## Opportunity
Two recent lines of work create a convergent opportunity. First, the 'false trust' study (2605.10930, May 2026) establishes that dual explanations (pro + contra arguments) are the *only* explanation type that genuinely improves users' ability to distinguish correct from incorrect LLM outputs—all other types merely increase acceptance. Second, 'Adjust for Trust' (2502.13321, IUI 2026) demonstrates that adaptively triggering counter-explanations based on user trust reduces inappropriate reliance by up to 38%. However, their approach requires obtrusive trust self-reports after every decision and real-time accuracy feedback—conditions rarely met in deployment. Their own analysis reveals that predicting trust from behavioral signals alone achieves F1 ≤ 0.5, making passive trust detection impractical, and they explicitly acknowledge that 'a key assumption of our setup does not hold in most real-world settings: that both parties have access to real-time feedback about decision accuracy.' Model uncertainty offers a complementary gating signal: it is computed automatically, requires no user input, works from the first interaction, and—critically—does not depend on accuracy feedback for calibration. Yet no work has empirically compared these two gating strategies. Meanwhile, 'The Persuasion Paradox' (2604.03237) shows that explanation effectiveness is strongly task-dependent—explanations help for language-based reasoning (72.5% accuracy vs. 48.5% baseline on LSAT) but hurt for visual reasoning—suggesting that uncertainty-gated explanation switching is most valuable precisely for the knowledge QA domain where explanations are effective. Critically, 'To Rely or Not to Rely?' (2412.15584, CHI 2025) finds that *displaying* uncertainty to users (via token-level probability highlighting) actually backfires—increasing algorithm aversion without improving appropriate reliance. This counter-evidence is important because it shows that uncertainty information is counterproductive when presented directly to users, but it does not indict using uncertainty as a *backend gating signal* to select which explanation type to present. Indeed, it strengthens the case for our approach: rather than burdening users with uncertainty visualization, we use uncertainty behind the scenes to select the more effective dual explanation format when model error is likely. The missing piece remains a head-to-head comparison that determines when model uncertainty outperforms, matches, or falls short of trust-based gating, while also measuring the fairness implications that 'Unequal Uncertainty' (2508.07872) warns about.

## Landscape
The false trust paper (2605.10930, May 2026) establishes dual explanations as uniquely effective but tested them uniformly. 'Adjust for Trust' (2502.13321, IUI 2026) is the closest prior work on gating strategy: it gates between supporting and counter-explanations based on self-reported user trust (11-point scale, 0-10), achieving 38% reduction in inappropriate reliance and 20% accuracy improvement across science QA and medical diagnosis with 30 trials per participant. Critically, their trust measurement requires accuracy feedback after each trial and explicit trust surveys—conditions that limit deployment scalability. Their trust threshold (≥8 on 0-10 scale for counter-explanations) was set by visual inspection of reliance curves, not formal optimization. Their attempt to predict trust from interaction features yielded F1 ≤ 0.5. 'From Text to Trust' (Li et al., 2502.11919, CHI 2025) is the closest prior work on adaptive explanation selection: they use a dynamic programming framework with a learned human behavior model to selectively decide which LLM-generated feature analyses to present for tabular AI predictions (income, recidivism; N=447 and N=397, 15 trials per participant), significantly improving appropriate reliance versus always-on and control conditions. However, their approach differs from ours in three key respects: (1) it requires prior interaction data to train the behavior model (cold-start problem), (2) it operates on tabular feature-level analyses rather than natural-language dual explanations, and (3) their gating is based on predicted utility of each analysis rather than on model uncertainty or user trust as explicit signals. Our work complements theirs by comparing two deployment-practical gating signals (model uncertainty and self-reported trust) for a different intervention type (dual pro/contra explanations) in knowledge QA. 'To Rely or Not to Rely?' (Bo et al., 2412.15584, CHI 2025) benchmarks three reliance interventions on N=400 participants across LSAT and image estimation (only 4 trials per participant): Reliance Disclaimer (static warning text), Uncertainty Highlighting (red/pink token-level probability visualization), and Implicit Answer (removing explicit answer statements). Their central finding is sobering: while interventions reduce over-reliance, they generally fail to improve *appropriate* reliance—only Reliance Disclaimer improves the Appropriate Reliance Ratio, and only on LSAT (ARR=1.62 vs. 1.17 control, p=.04). Uncertainty Highlighting specifically backfired, significantly reducing perceived accuracy and helpfulness and increasing algorithm aversion rather than calibrating reliance. This is critical counter-evidence that our approach must address. The key distinction is mechanistic: Bo et al.'s Uncertainty Highlighting *displays* uncertainty information to users, imposing cognitive burden and triggering aversion. Our uncertainty-gated approach uses uncertainty as a *backend signal* to select explanation type—users never see uncertainty scores; they see adaptively selected explanation content. Furthermore, their interventions (disclaimer, highlighting, implicit answer) are simpler cognitive forcing mechanisms, whereas our dual explanation (pro + contra arguments) is the only format shown to genuinely improve discrimination ability (2605.10930). 'Selectively Providing Reliance Calibration Cues' (2302.09995) predicts human reliance behavior to selectively present calibration cues, but uses a learned user model rather than model uncertainty and does not switch explanation types. 'The Persuasion Paradox' (2604.03237) finds that uncertainty-based selective automation outperforms explanations for visual reasoning, but their own results show LLM explanations dramatically improve performance on language-based tasks (LSAT: 72.5% vs. 48.5%), supporting explanation-type switching for knowledge QA. 'Contrastive Explanations That Anticipate Misconceptions' (2410.04253, CHI 2025) generates explanations addressing the gap between AI and user reasoning (N=628, improves decision skills), but applies them uniformly without selective gating. 'Don't Just Translate, Agitate' (2504.12424) proposes LLMs as devil's advocates for XAI but is a position paper without empirical evaluation. 'Why Not Both?' (Frontiers 2025) shows explanations and uncertainty estimates serve complementary roles—uncertainty improves accuracy while explanations improve understanding—supporting the value of combining both signals. 'Unequal Uncertainty' (2508.07872) provides the first socio-technical and legal analysis of uncertainty-gated interventions, showing they can disproportionately affect underrepresented groups through differential triggering rates, creating fairness and legal risks under UK Equality Act 2010. 'Entropy Alone is Insufficient' (2603.21172) demonstrates that semantic entropy has a 'confidently wrong regime' and combining it with a Probability of Correctness probe substantially improves reliability. 'Revisiting Uncertainty Estimation' (2505.23854) shows LLMs have better calibration on reasoning tasks than knowledge-heavy ones across 80 models, and that good calibration does not guarantee effective error ranking—necessitating explicit validation for our QA domain. 'LLMs Should Express Uncertainty Explicitly' (2604.05306) proposes verbalized confidence and reasoning-time uncertainty markers, achieving improved calibration. 'Dissenting Explanations' (AAAI 2024) leverages model multiplicity for disagreeing explanations but applies them uniformly. Partial explanations (de Jong et al., PACM HCI 2025) reduce overreliance through cognitive forcing but do not modulate explanation type. 'Framework for Machine Evaluation of Reasoning Completeness' (Patil, 2510.21884) introduces the RACE framework evaluating alignment between LLM explanations and interpretable feature importance, finding a 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues—relevant context for understanding how explanation quality may covary with model correctness. Multi-AI panel work (2603.22152) finds single dissent reduces conformity while broad disagreement confuses. Uncertainty Gating for Cost-Aware XAI (2603.29915) uses epistemic uncertainty to gate explanation methods for ML classifiers, not human overreliance; notably, they use percentile-based thresholds calibrated per dataset across ν ∈ {0.1, 0.3, 0.5, 0.7, 0.9}. No existing work directly compares model uncertainty and user trust as competing gating signals for adaptive explanation presentation in LLM-assisted decision-making.

## Approach
The study proceeds in two phases. **Phase 1: Uncertainty Signal Validation.** Before any human-subjects work, we validate the gating signal on our specific task. Using Qwen3-30B-A3B—a Mixture-of-Experts model with 30.5B total parameters but only 3.3B activated per token (128 experts/layer, 8 selected per token)—we generate answers to 200 candidate general-knowledge questions and compute semantic entropy over 10 sampled completions per question. Semantic entropy operates on output-level semantics (clustering sampled completions by meaning), so it is unaffected by MoE routing variability. Following 'Entropy Alone is Insufficient' (2603.21172), we also train a lightweight Probability of Correctness (PC) probe on Qwen3-30B-A3B's hidden-state activations using a held-out set. For the PC probe specifically, we address MoE-specific considerations: we probe the shared residual stream representations (post-attention, pre-MoE routing) rather than post-expert states, avoiding the routing variability where different tokens activate different expert subsets. We validate probe stability by measuring variance across multiple forward passes on identical inputs, since MoE routing is deterministic for greedy decoding but may vary under sampling. Alternatively, we can adopt the Semantic Entropy Probes approach (Kossen et al., 2024), which approximates semantic entropy from single-generation hidden states, eliminating the need for multiple samples entirely. We combine semantic entropy and PC probe scores via logistic regression to produce a hybrid uncertainty signal. We require AUROC ≥ 0.75 for distinguishing correct from incorrect answers before proceeding; if this threshold is not met, we evaluate alternative models (Llama-4-Scout-17B, Mixtral-8x22B) or uncertainty methods (semantic energy, verbalized confidence per 2604.05306). **Threshold calibration:** The uncertainty gating threshold is set at the Youden's J optimal cutpoint (maximizing sensitivity + specificity − 1) on Phase 1 validation data, with bootstrap 95% CI for the cutpoint to quantify threshold uncertainty. Cross-validation (leave-20%-out) prevents overfitting on the 200-question set. From validated questions, we select 30 for the main study (15 where the model is correct, 15 where it is incorrect, balanced across uncertainty levels and topic domains). The increase from 20 to 30 items matches the 'Adjust for Trust' protocol (30 trials per participant) and provides sufficient levels for stable item-level random effects estimation in the GLMM analysis (Westfall, Kenny, & Judd, 2014, show that with ≤8 items, maximal attainable power is <0.5 regardless of participant N; 30 items is well above this threshold and above the ≥5-level minimum recommended by Gelman & Hill, 2006). **Phase 2: Comparative User Study.** A preregistered between-subjects study (N≈560, 140 per condition) on Prolific with four conditions: (1) **No explanation**—LLM answer only; (2) **Always-on dual explanation**—every answer includes structured pro and contra arguments (replicating the effective condition from 2605.10930); (3) **Trust-gated dual explanation**—participants report trust on an 11-point scale (0-10) after each of the 30 trials; when trust exceeds 8 (adopting the 'Adjust for Trust' threshold, which was empirically calibrated against reliance behavior), the next trial presents dual explanation, otherwise single explanation; (4) **Uncertainty-gated dual explanation**—when the hybrid uncertainty signal exceeds the Youden's J-optimal threshold from Phase 1, dual explanation is presented; otherwise single explanation. **Triggering rate calibration:** In the pilot study (N=60, 15 per condition), we compare empirical triggering rates between Conditions 3 and 4. If rates differ by >15 percentage points, we adjust the uncertainty threshold to the percentile that approximately matches the trust-gated triggering rate, reporting both Youden-optimal and rate-matched thresholds as sensitivity analyses. This ensures condition comparability while preserving transparency about any threshold adjustment. Crucially, unlike the Uncertainty Highlighting intervention in Bo et al. (2412.15584) which *displays* token-level probability information to users (and backfired by increasing algorithm aversion), our uncertainty-gated condition uses uncertainty purely as a backend signal—participants see only the selected explanation format, never the uncertainty estimate itself. This design choice is directly informed by Bo et al.'s finding that user-facing uncertainty visualization is counterproductive. All conditions receive accuracy feedback after each trial (following 'Adjust for Trust' protocol, ensuring comparability). Dual explanations are generated via Claude API with structured prompting (pro: 3-4 sentences supporting the answer; contra: 2-3 sentences presenting the strongest counter-argument and alternative answer), with human review for quality. **Measures**: Primary—overreliance rate (accepting incorrect AI answers), discrimination accuracy (AUROC of accept/reject decisions vs. correctness), appropriate reliance (composite of over- and under-reliance, following the Appropriate Reliance Ratio from Bo et al., 2412.15584). Secondary—cognitive load (NASA-TLX), task completion time, subjective satisfaction (7-point Likert), perceived AI competence. **Analysis plan**: Generalized linear mixed model (GLMM) with a logit link for trial-level accept/reject decisions, including crossed random intercepts for participants and items (questions), and random slopes for condition by item to capture differential treatment effects across questions (following Baayen, Davidson, & Bates, 2008; Westfall, Kenny, & Judd, 2014). Fixed effects: condition (4 levels), item correctness (correct/incorrect), and their interaction. Participant-level covariates: age, education, domain knowledge (pre-test). This approach accounts for item-level variance (question difficulty, topic familiarity) that would otherwise inflate Type I error if items were treated as fixed (Judd, Westfall, & Kenny, 2012). **Equivalence testing specification (H2)**: We use Two One-Sided Tests (TOST; Lakens, 2017) with a pre-registered equivalence margin of Cohen's d = 0.35, justified by cost-benefit SESOI reasoning (Lakens, Scheel, & Isager, 2018): this represents the maximum effectiveness difference at which uncertainty-gating's deployment advantages—no user surveys, no accuracy feedback dependency, first-interaction readiness—still outweigh the performance loss versus trust-gating. In raw terms, d = 0.35 corresponds to approximately 7 percentage points on overreliance rate (assuming participant-level SD ≈ 0.20), meaning we accept non-inferiority if uncertainty-gating's overreliance rate is no more than 7pp higher than trust-gating's. As sensitivity analyses, we also report equivalence tests at d = 0.25 (stricter) and d = 0.50 (more lenient) to demonstrate robustness to margin specification. **Power analysis**: For H2 (TOST non-inferiority, d = 0.35 bounds, α = 0.05): N = 140 per group provides ~80% power (computed via TOSTER::power_t_TOST; consistent with Lakens, 2017, Table 1: d = 0.30 requires N = 191/group, d = 0.40 requires N = 108/group, interpolating to ~140 for d = 0.35). For H1 and H3 (superiority tests, expected d ≈ 0.50 based on 'Adjust for Trust' effect sizes): N = 140 per group provides >95% power. Total sample: N = 560 (140 per condition). **Fairness analysis** (RQ3, addressing 'Unequal Uncertainty'): We collect demographic data (gender, race/ethnicity, education, English proficiency) and analyze whether uncertainty-gated dual explanations trigger at different rates for questions where demographic knowledge gaps exist, whether differential triggering correlates with demographics, and whether any differential triggering translates to differential overreliance reduction. **Key hypotheses**: H1—Conditions 3 and 4 both reduce overreliance compared to Condition 1; H2—Condition 4 (uncertainty-gated) achieves non-inferior overreliance reduction compared to Condition 3 (trust-gated), tested via TOST with equivalence margin d = 0.35; H3—Condition 4 produces lower cognitive load and higher satisfaction than Condition 2 (always-on dual); H4—Condition 4 incurs no measurement burden (no trust surveys), making it more practical; H5—Uncertainty-gated triggering rates do not differ significantly across demographic groups (fairness hypothesis, tested as a secondary analysis with appropriate corrections for multiple comparisons). **Ecological validity limitation**: Accuracy feedback after every trial, while necessary for the trust-gated condition (Condition 3) and provided to all conditions for comparability, is rarely available in real-world deployment. The 'Adjust for Trust' authors explicitly acknowledge this limitation. Okamura and Yamada (CHI 2024, arXiv 2111.08222) demonstrate that outcome feedback substantially improves trust calibration, while interpretability alone does not—implying that trust-gating's effectiveness degrades in feedback-free settings. Critically, uncertainty-gating is feedback-independent: the model computes uncertainty from its own outputs regardless of whether users receive outcome information. This means our study likely *underestimates* uncertainty-gating's relative advantage over trust-gating in deployment, because the experimental feedback supports trust calibration that would be absent in practice. We discuss this asymmetry as a key deployment implication: in feedback-scarce environments (the norm for most LLM-assisted decisions), uncertainty-gating may be the *only* viable adaptive strategy, as trust-gating without feedback relies on potentially miscalibrated self-reports that the 'Adjust for Trust' authors themselves note may reflect 'potentially incorrect perceptions of expertise.' A follow-up study varying feedback availability (present vs. absent) across both gating conditions would directly quantify this interaction and is identified as priority future work.

## Resource Estimate
{'manual': {'gpu_hours': '300-400 (Qwen3-30B-A3B hosting for Phase 1 validation: ~2K questions × 10 samples + PC probe training on shared residual stream representations; Phase 2: ~10K inference calls × 10 samples for pilot + main study on A100-80GB; note Qwen3-30B-A3B activates only 3.3B parameters per token, reducing per-inference cost vs. dense 30B models)', 'timeline': '5-7 months (Month 1: system build + Phase 1 uncertainty validation + threshold calibration; Month 2: IRB submission + pilot design; Month 3: IRB approval + pilot N=60 + triggering rate calibration; Month 4: pilot analysis + main study refinement; Month 5: main study N≈560; Month 6-7: analysis + writing; aggressive 4.5-month variant possible if IRB uses expedited review for minimal-risk online study)', 'estimated_gpu_cost': '$700-1000 (A100 at ~$3/hr; MoE efficiency reduces per-inference cost)'}, 'human_in_loop': {'gpu_hours': '200-300 (Claude API generates candidate explanations and counter-arguments; GPU only for Qwen3-30B-A3B uncertainty estimation and PC probe training)', 'timeline': '4.5-6 months (Claude accelerates explanation generation, stimulus quality control, statistical modeling, and fairness analysis code)', 'claude_api_cost': '$600-900 (explanation generation for 200 candidate + 30 final questions × 4 conditions × multiple pilot rounds, plus analysis assistance)', 'estimated_gpu_cost': '$500-750'}, 'auto_research': {'gpu_hours': '200-300', 'timeline': '4.5-6 months minimum', 'claude_api_cost': '$900-1400 (automated stimulus optimization, power analysis simulation, equivalence testing code, fairness analysis, draft writing)', 'estimated_gpu_cost': '$500-750', 'speed_bottleneck': 'IRB approval (4-8 weeks, expedited review possible for minimal-risk online survey) and Prolific data collection (~2-3 weeks for N=560) are non-automatable; participant compensation ~$6,200-7,000 (560 participants × ~40 min average session × $12/hr Prolific recommended minimum + 33.3% Prolific academic service fee + ~10% buffer for rejections/replacements; Condition 3 sessions may extend to ~45 min due to trust surveys after each of 30 trials); trust measurement in Condition 3 requires interactive protocol that may extend session duration'}}

## Inspired By
The 'Adjust for Trust' finding that trust-gated counter-explanations reduce overreliance by 38%—combined with their own limitation that trust cannot be reliably predicted from behavior (F1 ≤ 0.5) and their acknowledgment that accuracy feedback is unavailable in most deployment settings—directly motivates testing model uncertainty as a practical alternative gating signal. The convergence of (1) dual explanations as uniquely effective (2605.10930), (2) adaptive gating as effective but trust-measurement-limited (2502.13321), (3) adaptive explanation selection as effective but requiring learned user models (2502.11919), (4) 'Entropy Alone is Insufficient' showing hybrid uncertainty signals improve reliability (2603.21172), (5) uncertainty *display* backfiring while the underlying signal remains informative (2412.15584), and (6) 'Unequal Uncertainty' raising fairness concerns about uncertainty-gated interventions (2508.07872) creates a well-motivated research question that no single prior paper addresses.

## Target Venues
- CHI 2027 (paper deadline Sep 10, 2026 — aggressive but achievable with 4.5-month timeline if Phase 1 validates quickly and IRB uses expedited review; flagship HCI venue, strong fit for adaptive AI-assisted decision-making comparison study; revise-and-resubmit process available)
- CSCW 2027 (rolling submission from Jan 2027 — comfortable primary target if CHI 2027 timeline proves too tight; strongest fit for adaptive AI-assisted decision-making with fairness analysis; 3-4 month review cycle)
- FAccT 2027 (estimated deadline ~Jan 2027 — fairness analysis of uncertainty-gated interventions is strong fit; equity framing as secondary contribution)
- CHI 2028 (paper deadline ~Sep 2027 — safe fallback if earlier venues require major revision)

## Key References
- Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (IUI 2026, arXiv 2502.13321) — *primary point of differentiation*: trust-gated adaptive counter-explanations, 38% reduction in inappropriate reliance, 30 trials/participant, trust ≥ 8 threshold; our Condition 3 replicates their mechanism
- Evaluating the False Trust engendered by LLM Explanations (arXiv 2605.10930, May 2026) — establishes dual explanations as uniquely effective; motivates explanation type selection
- From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis (Li et al., CHI 2025, arXiv 2502.11919) — dynamic programming framework with learned human behavior model for selectively presenting LLM-generated feature analyses (N=447, N=397, 15 trials/participant); improves appropriate reliance on tabular AI tasks; differs from our work in requiring prior interaction data, operating on feature-level analyses rather than dual explanations, and using predicted utility rather than model uncertainty or trust as gating signal
- To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models (Bo et al., CHI 2025, arXiv 2412.15584) — benchmarks three reliance interventions (Reliance Disclaimer, Uncertainty Highlighting, Implicit Answer) on N=400 (only 4 trials/participant); finds interventions generally fail to improve appropriate reliance; Uncertainty Highlighting specifically backfires by increasing algorithm aversion; *critical counter-evidence* that motivates our backend-gating design: we use uncertainty to select explanation type, never displaying it to users; Appropriate Reliance Ratio adopted as primary metric
- The Persuasion Paradox: When LLM Explanations Fail to Improve Human-AI Team Performance (arXiv 2604.03237) — shows explanation effectiveness is task-dependent; supports explanation switching for language-based QA while selective automation is better for visual tasks
- Selectively Providing Reliance Calibration Cues With Reliance Prediction (arXiv 2302.09995) — selective intervention via predicted reliance behavior; differs in gating signal (user model vs. model uncertainty) and intervention type (calibration cues vs. explanation switching)
- Contrastive Explanations That Anticipate Human Misconceptions (CHI 2025, arXiv 2410.04253) — human-centered contrastive explanations improve decision skills (N=628); applied uniformly, not selectively gated
- Don't Just Translate, Agitate: Using LLMs as Devil's Advocates for AI Explanations (arXiv 2504.12424) — position paper proposing LLMs as constructive agitators; no empirical evaluation
- Why Not Both? Complementing Explanations with Uncertainty (Frontiers in Computer Science 2025) — shows explanations and uncertainty serve complementary roles; supports combining both signals
- Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI (arXiv 2508.07872) — fairness risks of uncertainty-gated interventions; directly motivates our RQ3 fairness analysis
- Entropy Alone is Insufficient for Safe Selective Prediction in LLMs (arXiv 2603.21172) — demonstrates 'confidently wrong' regime of semantic entropy; motivates our hybrid SE + PC probe approach
- Revisiting Uncertainty Estimation and Calibration of Large Language Models (arXiv 2505.23854) — shows calibration varies across 80 models, worse on knowledge vs. reasoning tasks; motivates Phase 1 validation
- LLMs Should Express Uncertainty Explicitly (arXiv 2604.05306) — verbalized confidence and reasoning-time uncertainty markers improve calibration; alternative uncertainty elicitation if SE fails validation
- To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance (CSCW 2021) — establishes effectiveness-usability tradeoff in CFF interventions
- An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, January 2026) — Assumption CFF reduces overreliance but decreases satisfaction
- Cognitive Forcing for Better Decision-Making: Reducing Overreliance Through Partial Explanations (PACM HCI 2025) — partial explanations as cognitive forcing; no uncertainty-based modulation
- Dissenting Explanations: Leveraging Disagreement to Reduce Model Overreliance (AAAI 2024) — model multiplicity for disagreeing explanations; applied uniformly without selective gating
- More Isn't Always Better: Balancing Decision Accuracy and Conformity Pressures in Multi-AI Advice (arXiv 2603.22152) — single dissent reduces conformity; supports targeted rather than blanket counter-argumentation
- Uncertainty Gating for Cost-Aware Explainable AI (arXiv 2603.29915) — uses epistemic uncertainty to gate explanation methods for ML classifiers with percentile-based thresholds; analogous mechanism but entirely different application domain
- Framework for Machine Evaluation of Reasoning Completeness in Large Language Models for Classification Tasks (Patil, arXiv 2510.21884) — RACE framework evaluating explanation-feature alignment; finds 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues; relevant context for understanding explanation quality covariation with model correctness
- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (Kossen et al., arXiv 2406.15927) — approximates semantic entropy from single-generation hidden states, reducing computational overhead to near zero; potential efficiency improvement for Phase 1 uncertainty estimation
- Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (Lakens, 2017, Social Psychological and Personality Science) — TOST procedure and power analysis tables; our equivalence margin and power calculations follow this framework
- Equivalence Testing for Psychological Research: A Tutorial (Lakens, Scheel, & Isager, 2018, AMPPS) — SESOI justification approaches including cost-benefit analysis; grounds our d = 0.35 margin choice
- Statistical Power and Optimal Design in Experiments in Which Samples of Participants Respond to Samples of Stimuli (Westfall, Kenny, & Judd, 2014, JEP:General) — power analysis for crossed random effects designs; shows ≤8 items cap maximal power at <0.5; motivates our 30-item stimulus set
- Mixed-Effects Modeling with Crossed Random Effects for Subjects and Items (Baayen, Davidson, & Bates, 2008, J Memory & Language) — methodological foundation for our GLMM analysis plan with crossed random effects for participants and items
- Adaptive Trust Calibration for Human-AI Collaboration (Okamura & Yamada, CHI 2024, arXiv 2111.08222) — directly compares feedback vs. no-feedback conditions; shows outcome feedback substantially improves trust calibration while interpretability alone does not; grounds our ecological validity discussion


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "bcb2531d-0daa-4fdf-ad5b-25f4dee31f37",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:45:32.395Z_

```json
{
  "parentUuid": "bcb2531d-0daa-4fdf-ad5b-25f4dee31f37",
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
  "uuid": "62cafdcf-0cd0-48ae-900b-fcdf27137fde",
  "timestamp": "2026-05-20T04:45:32.395Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:45:32.396Z_

```json
{
  "parentUuid": "62cafdcf-0cd0-48ae-900b-fcdf27137fde",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6bd9d37b-ff21-41d9-ba8d-44e2854b5d26",
  "timestamp": "2026-05-20T04:45:32.396Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "6bd9d37b-ff21-41d9-ba8d-44e2854b5d26",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Model uncertainty vs. user trust for adaptive AI explanations",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:45:42.931Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed research proposal that I need to evaluate as the "入口评审 agent" (Entry Triage Agent). Let me first understand the proposal, then conduct web searches to understand the field, and finally provide my assessment.

The proposal is about comparing model uncertainty vs. user trust as gating signals for when to present dual explanations (pro + contra arguments) in LLM-assisted decision-making. The core idea is that:

1. Dual explanations (showing both supporting and opposing arguments) are the only explanation type that genuinely reduces overreliance on LLMs
2. Trust-gated approaches work but require obtrusive self-reports and accuracy feedback


3. Model uncertainty could serve as an automatic, deployment-ready alternative gating signal
4. They want to do a head-to-head comparison of these two gating strategies

Now I need to search for relevant papers and understand the current landscape in this area before evaluating the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bd9d37b-ff21-41d9-ba8d-44e2854b5d26",
  "isSidechain": false,
  "requestId": "req_011CbDDGLZLaF6RSL77VUH1e",
  "type": "assistant",
  "uuid": "fd73a49b-04f3-4e3a-b76d-f5d4a56caf62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Um9XxG2j9UEjDTJtuVgPn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9663,
      "cache_read_input_tokens": 14333,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 312,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 9663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9663
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

_source line 9 · 2026-05-20T04:45:42.934Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019kh6EDqRYcLxLRfpj8Phy7`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd73a49b-04f3-4e3a-b76d-f5d4a56caf62",
  "isSidechain": false,
  "requestId": "req_011CbDDGLZLaF6RSL77VUH1e",
  "type": "assistant",
  "uuid": "8b53a5e8-acb8-497b-9892-60913aebff07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Um9XxG2j9UEjDTJtuVgPn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9663,
      "cache_read_input_tokens": 14333,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 312,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 9663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9663
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

_source line 10 · 2026-05-20T04:45:42.943Z_

<details><summary>↩ Tool result · `toolu_019kh6EDqRYcLxLRfpj8Phy7`</summary>

````text
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
  "parentUuid": "8b53a5e8-acb8-497b-9892-60913aebff07",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "7c090971-450d-408c-813e-cd0081f55074",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "8b53a5e8-acb8-497b-9892-60913aebff07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T04:45:47.342Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required web searches to understand the field before making any assessment. I need to search for:

1. The key papers cited in this proposal to verify they exist and understand them
2. The current state of adaptive explanation / overreliance reduction in LLM-assisted decision-making
3. Any competing or overlapping work that might threaten novelty

Let me do multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c090971-450d-408c-813e-cd0081f55074",
  "isSidechain": false,
  "requestId": "req_011CbDDH7hD6L4HJRVnitnHj",
  "type": "assistant",
  "uuid": "80e219f8-7f37-467c-8993-67748e51da36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDmpeYrDZ9kWXbhTPWaSmW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23996,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 12 · 2026-05-20T04:45:48.289Z_

Let me conduct the required field research before making any assessment. I'll run multiple targeted searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80e219f8-7f37-467c-8993-67748e51da36",
  "isSidechain": false,
  "requestId": "req_011CbDDH7hD6L4HJRVnitnHj",
  "type": "assistant",
  "uuid": "f3adfdb9-1cd0-4050-a9e4-19b669e83d41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDmpeYrDZ9kWXbhTPWaSmW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23996,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 13 · 2026-05-20T04:45:48.767Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fq2ZygKuppxeB6zQ8STuCu`</summary>

```json
{
  "query": "adaptive dual explanations LLM overreliance reduction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3adfdb9-1cd0-4050-a9e4-19b669e83d41",
  "isSidechain": false,
  "requestId": "req_011CbDDH7hD6L4HJRVnitnHj",
  "type": "assistant",
  "uuid": "cccfb075-23c0-456f-831e-8e1e0c34027d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDmpeYrDZ9kWXbhTPWaSmW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23996,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 14 · 2026-05-20T04:45:49.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Mq2K77H36xT1tLBo6xo3M`</summary>

```json
{
  "query": "arXiv 2605.10930 false trust LLM explanations dual explanations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cccfb075-23c0-456f-831e-8e1e0c34027d",
  "isSidechain": false,
  "requestId": "req_011CbDDH7hD6L4HJRVnitnHj",
  "type": "assistant",
  "uuid": "2334929f-7fbc-42fb-8ec0-9d269147d6e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDmpeYrDZ9kWXbhTPWaSmW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23996,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 15 · 2026-05-20T04:45:50.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FqrvNbCjYKCK7TSg4HWykS`</summary>

```json
{
  "query": "arXiv 2502.13321 \"Adjust for Trust\" IUI 2026 trust-gated counter-explanations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2334929f-7fbc-42fb-8ec0-9d269147d6e3",
  "isSidechain": false,
  "requestId": "req_011CbDDH7hD6L4HJRVnitnHj",
  "type": "assistant",
  "uuid": "be61cf7b-1f77-450f-82a6-e0bf49628b5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDmpeYrDZ9kWXbhTPWaSmW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23996,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 16 · 2026-05-20T04:45:51.548Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015FAmkUp9v27gAtdTEdX4zU`</summary>

```json
{
  "query": "model uncertainty gating signal explanation selection human-AI decision making 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be61cf7b-1f77-450f-82a6-e0bf49628b5c",
  "isSidechain": false,
  "requestId": "req_011CbDDH7hD6L4HJRVnitnHj",
  "type": "assistant",
  "uuid": "3697d67b-d082-406b-bc72-84051ebca580",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDmpeYrDZ9kWXbhTPWaSmW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 23996,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 17 · 2026-05-20T04:45:56.048Z_

<details><summary>↩ Tool result · `toolu_01Fq2ZygKuppxeB6zQ8STuCu`</summary>

```text
Web search results for query: "adaptive dual explanations LLM overreliance reduction 2025 2026"

Links: [{"title":"LLM Overreliance: What It Is and How to Prevent | Cobalt","url":"https://www.cobalt.io/learning-center/llm-overreliance-overview"},{"title":"Measuring and mitigating overreliance is necessary for building human-compatible AI","url":"https://arxiv.org/html/2509.08010v1"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Large Language Models Help Humans Verify Truthfulness -- Except When   They Are Convincingly Wrong","url":"https://arxiv.org/pdf/2310.12558"},{"title":"Know Your Mistakes: Towards Preventing Overreliance on Task-Oriented Conversational AI Through Accountability Modeling","url":"https://arxiv.org/pdf/2501.10316"},{"title":"[2509.08010] Measuring and mitigating overreliance is necessary for building human-compatible AI","url":"https://arxiv.org/abs/2509.08010"},{"title":"Fostering Appropriate Reliance on Large Language Models: The Role of   Explanations, Sources, and Inconsistencies","url":"https://arxiv.org/pdf/2502.08554"},{"title":"Top LLM Trends 2025: What's the Future of LLMs","url":"https://www.turing.com/resources/top-llm-trends"}]

Based on the search results, here's what I found regarding adaptive dual explanations and LLM overreliance reduction in 2025-2026:

## Adaptive Explanations for Overreliance Reduction

Adaptive explanations can tailor explanations of model outputs by task context or other strategies such as levels of confidence, for example, explaining alternative predictions when AI confidence falls below certain thresholds, or only explaining top predictions when confidence is high.

## Contrastive Explanation Approach

Research has explored using contrastive or dual explanations to address overreliance. To reduce over-reliance on LLMs, researchers asked LLMs to provide contrastive information—explain both why a claim is true and false, and then presented both sides of the explanation to users, which mitigates users' over-reliance on LLMs.

## 2025-2026 Outlook

A 2025 research paper titled "Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies" was presented at CHI Conference in April-May 2025 in Yokohama, Japan, indicating active research in this area.

The broader context shows that LLM overreliance is recognized as one of the most significant risks in the Open Worldwide Application Security Project (OWASP) Top 10 list for large language model applications and generative AI vulnerabilities, making this an important focus area for AI researchers and practitioners.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cccfb075-23c0-456f-831e-8e1e0c34027d",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "240937aa-a24d-4994-bff9-5fc37b11a0c0",
  "toolUseResult": {
    "query": "adaptive dual explanations LLM overreliance reduction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014kVje6t4Z8jM62Pe2GhfNM",
        "content": [
          {
            "title": "LLM Overreliance: What It Is and How to Prevent | Cobalt",
            "url": "https://www.cobalt.io/learning-center/llm-overreliance-overview"
          },
          {
            "title": "Measuring and mitigating overreliance is necessary for building human-compatible AI",
            "url": "https://arxiv.org/html/2509.08010v1"
          },
          {
            "title": "The State Of LLMs 2025: Progress, Progress, and Predictions",
            "url": "https://magazine.sebastianraschka.com/p/state-of-llms-2025"
          },
          {
            "title": "Large Language Models Help Humans Verify Truthfulness -- Except When   They Are Convincingly Wrong",
            "url": "https://arxiv.org/pdf/2310.12558"
          },
          {
            "title": "Know Your Mistakes: Towards Preventing Overreliance on Task-Oriented Conversational AI Through Accountability Modeling",
            "url": "https://arxiv.org/pdf/2501.10316"
          },
          {
            "title": "[2509.08010] Measuring and mitigating overreliance is necessary for building human-compatible AI",
            "url": "https://arxiv.org/abs/2509.08010"
          },
          {
            "title": "Fostering Appropriate Reliance on Large Language Models: The Role of   Explanations, Sources, and Inconsistencies",
            "url": "https://arxiv.org/pdf/2502.08554"
          },
          {
            "title": "Top LLM Trends 2025: What's the Future of LLMs",
            "url": "https://www.turing.com/resources/top-llm-trends"
          }
        ]
      },
      "Based on the search results, here's what I found regarding adaptive dual explanations and LLM overreliance reduction in 2025-2026:\n\n## Adaptive Explanations for Overreliance Reduction\n\nAdaptive explanations can tailor explanations of model outputs by task context or other strategies such as levels of confidence, for example, explaining alternative predictions when AI confidence falls below certain thresholds, or only explaining top predictions when confidence is high.\n\n## Contrastive Explanation Approach\n\nResearch has explored using contrastive or dual explanations to address overreliance. To reduce over-reliance on LLMs, researchers asked LLMs to provide contrastive information—explain both why a claim is true and false, and then presented both sides of the explanation to users, which mitigates users' over-reliance on LLMs.\n\n## 2025-2026 Outlook\n\nA 2025 research paper titled \"Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies\" was presented at CHI Conference in April-May 2025 in Yokohama, Japan, indicating active research in this area.\n\nThe broader context shows that LLM overreliance is recognized as one of the most significant risks in the Open Worldwide Application Security Project (OWASP) Top 10 list for large language model applications and generative AI vulnerabilities, making this an important focus area for AI researchers and practitioners."
    ],
    "durationSeconds": 7.272673972000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cccfb075-23c0-456f-831e-8e1e0c34027d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T04:45:56.579Z_

<details><summary>↩ Tool result · `toolu_012Mq2K77H36xT1tLBo6xo3M`</summary>

```text
Web search results for query: "arXiv 2605.10930 false trust LLM explanations dual explanations"

Links: [{"title":"[2605.10930] Evaluating the False Trust engendered by LLM Explanations","url":"https://arxiv.org/abs/2605.10930"},{"title":"From Deception to Detection: The Dual Roles of Large Language Models in Fake News","url":"https://arxiv.org/html/2409.17416v1"},{"title":"When AI Persuades: Adversarial Explanation Attacks on Human Trust in AI-Assisted Decision Making","url":"https://arxiv.org/html/2602.04003v1"},{"title":"LLM-Generated Black-box Explanations Can Be Adversarially Helpful","url":"https://arxiv.org/pdf/2405.06800"},{"title":"Can LLMs Produce Faithful Explanations For Fact-checking? Towards   Faithful Explainable Fact-Checking via Multi-Agent Debate","url":"https://arxiv.org/pdf/2402.07401"},{"title":"Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations","url":"https://arxiv.org/pdf/2504.14150"},{"title":"Truthful or Fabricated? Using Causal Attribution to Mitigate Reward Hacking in Explanations","url":"https://arxiv.org/pdf/2504.05294"}]

Based on the search results, here's what I found about arXiv paper 2605.10930:

## Overview

The paper conducts a between-subject user study analyzing the false trust engendered by commonly used LLM explanations - reasoning traces, their summaries and post-hoc explanations.

## Key Findings

The research finds that reasoning traces and post-hoc explanations are persuasive but not informative: they increase user acceptance of LLM predictions regardless of their correctness.

## Dual Explanations

The paper introduces an important innovation in its experimental design: it tests a contrastive dual explanation setting where arguments for and against the AI's answer are presented. Notably, dual explanation is the only condition that genuinely improves users' ability to distinguish correct from incorrect AI outputs.

## Context

The reasoning traces are neither faithful representations of the model's computations nor necessarily semantically meaningful, yet are often interpreted as provenance explanations. The research addresses whether explanations or reasoning traces help users identify when the AI is incorrect, or whether they simply persuade users to trust the AI regardless.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2334929f-7fbc-42fb-8ec0-9d269147d6e3",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "96b4f950-1225-4618-8d88-af30382318e3",
  "toolUseResult": {
    "query": "arXiv 2605.10930 false trust LLM explanations dual explanations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BuSMTCq25RqMNu66SXNCnQ",
        "content": [
          {
            "title": "[2605.10930] Evaluating the False Trust engendered by LLM Explanations",
            "url": "https://arxiv.org/abs/2605.10930"
          },
          {
            "title": "From Deception to Detection: The Dual Roles of Large Language Models in Fake News",
            "url": "https://arxiv.org/html/2409.17416v1"
          },
          {
            "title": "When AI Persuades: Adversarial Explanation Attacks on Human Trust in AI-Assisted Decision Making",
            "url": "https://arxiv.org/html/2602.04003v1"
          },
          {
            "title": "LLM-Generated Black-box Explanations Can Be Adversarially Helpful",
            "url": "https://arxiv.org/pdf/2405.06800"
          },
          {
            "title": "Can LLMs Produce Faithful Explanations For Fact-checking? Towards   Faithful Explainable Fact-Checking via Multi-Agent Debate",
            "url": "https://arxiv.org/pdf/2402.07401"
          },
          {
            "title": "Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations",
            "url": "https://arxiv.org/pdf/2504.14150"
          },
          {
            "title": "Truthful or Fabricated? Using Causal Attribution to Mitigate Reward Hacking in Explanations",
            "url": "https://arxiv.org/pdf/2504.05294"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2605.10930:\n\n## Overview\n\nThe paper conducts a between-subject user study analyzing the false trust engendered by commonly used LLM explanations - reasoning traces, their summaries and post-hoc explanations.\n\n## Key Findings\n\nThe research finds that reasoning traces and post-hoc explanations are persuasive but not informative: they increase user acceptance of LLM predictions regardless of their correctness.\n\n## Dual Explanations\n\nThe paper introduces an important innovation in its experimental design: it tests a contrastive dual explanation setting where arguments for and against the AI's answer are presented. Notably, dual explanation is the only condition that genuinely improves users' ability to distinguish correct from incorrect AI outputs.\n\n## Context\n\nThe reasoning traces are neither faithful representations of the model's computations nor necessarily semantically meaningful, yet are often interpreted as provenance explanations. The research addresses whether explanations or reasoning traces help users identify when the AI is incorrect, or whether they simply persuade users to trust the AI regardless."
    ],
    "durationSeconds": 6.827275741999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2334929f-7fbc-42fb-8ec0-9d269147d6e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T04:45:57.460Z_

<details><summary>↩ Tool result · `toolu_01FqrvNbCjYKCK7TSg4HWykS`</summary>

```text
Web search results for query: "arXiv 2502.13321 "Adjust for Trust" IUI 2026 trust-gated counter-explanations"

Links: [{"title":"[2502.13321] Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://arxiv.org/abs/2502.13321"},{"title":"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://arxiv.org/html/2502.13321"},{"title":"(PDF) Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://www.researchgate.net/publication/389167262_Adjust_for_Trust_Mitigating_Trust-Induced_Inappropriate_Reliance_on_AI_Assistance"},{"title":"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250213321S/abstract"},{"title":"The Effects of Presenting AI Uncertainty Information on Pharmacists’ Trust in Automated Pill Recognition Technology: Exploratory Mixed Subjects Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11862782/"},{"title":"Adjust for Trust:","url":"https://arxiv.org/pdf/2502.13321"},{"title":"Determinants of Laypersons’ Trust in Medical Decision Aids: Randomized Controlled Trial","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9115664/"},{"title":"First impressions of a financial AI assistant: differences between high trust and low trust users","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10579608/"},{"title":"Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.","url":"https://arxiv.org/html/2311.11489"}]

I found the paper you were looking for! Here are the key details:

**Title:** "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance"

**arXiv ID:** 2502.13321

**Authors:** Tejas Srinivasan and Jesse Thomason

**Publication:** The paper is published at the 31st International Conference on Intelligent User Interfaces (IUI '26), March 23–26, 2026, in Paphos, Cyprus

**Main Concept:** The paper addresses how trust biases user reliance on AI recommendations, with low and high levels of trust resulting in increased under- and over-reliance, respectively

**Key Approach:** When trust is low, the assistant can reduce risk of disuse by providing additional reasoning to support its recommendation. Similarly, when users are too trusting, the assistant can highlight reasons its recommendation may be incorrect

**Methodology:** The research examines the effect of trust-adaptive interventions through two decision-making scenarios -- laypeople answering science questions and doctors making medical diagnoses

The paper proposes a trust-gated approach where AI assistants dynamically adjust their behavior (through supporting explanations for low trust and counter-explanations for high trust) to promote more appropriate user reliance on AI systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be61cf7b-1f77-450f-82a6-e0bf49628b5c",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "4d29e307-727b-4dad-939c-e520583ed508",
  "toolUseResult": {
    "query": "arXiv 2502.13321 \"Adjust for Trust\" IUI 2026 trust-gated counter-explanations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RVB4wVbE5NVb15brsQKJzF",
        "content": [
          {
            "title": "[2502.13321] Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://arxiv.org/abs/2502.13321"
          },
          {
            "title": "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://arxiv.org/html/2502.13321"
          },
          {
            "title": "(PDF) Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://www.researchgate.net/publication/389167262_Adjust_for_Trust_Mitigating_Trust-Induced_Inappropriate_Reliance_on_AI_Assistance"
          },
          {
            "title": "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250213321S/abstract"
          },
          {
            "title": "The Effects of Presenting AI Uncertainty Information on Pharmacists’ Trust in Automated Pill Recognition Technology: Exploratory Mixed Subjects Study",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11862782/"
          },
          {
            "title": "Adjust for Trust:",
            "url": "https://arxiv.org/pdf/2502.13321"
          },
          {
            "title": "Determinants of Laypersons’ Trust in Medical Decision Aids: Randomized Controlled Trial",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9115664/"
          },
          {
            "title": "First impressions of a financial AI assistant: differences between high trust and low trust users",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10579608/"
          },
          {
            "title": "Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.",
            "url": "https://arxiv.org/html/2311.11489"
          }
        ]
      },
      "I found the paper you were looking for! Here are the key details:\n\n**Title:** \"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance\"\n\n**arXiv ID:** 2502.13321\n\n**Authors:** Tejas Srinivasan and Jesse Thomason\n\n**Publication:** The paper is published at the 31st International Conference on Intelligent User Interfaces (IUI '26), March 23–26, 2026, in Paphos, Cyprus\n\n**Main Concept:** The paper addresses how trust biases user reliance on AI recommendations, with low and high levels of trust resulting in increased under- and over-reliance, respectively\n\n**Key Approach:** When trust is low, the assistant can reduce risk of disuse by providing additional reasoning to support its recommendation. Similarly, when users are too trusting, the assistant can highlight reasons its recommendation may be incorrect\n\n**Methodology:** The research examines the effect of trust-adaptive interventions through two decision-making scenarios -- laypeople answering science questions and doctors making medical diagnoses\n\nThe paper proposes a trust-gated approach where AI assistants dynamically adjust their behavior (through supporting explanations for low trust and counter-explanations for high trust) to promote more appropriate user reliance on AI systems."
    ],
    "durationSeconds": 6.686164057999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "be61cf7b-1f77-450f-82a6-e0bf49628b5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "4d29e307-727b-4dad-939c-e520583ed508",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Model uncertainty vs. user trust for adaptive AI explanations",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Tool result

_source line 22 · 2026-05-20T04:46:00.045Z_

<details><summary>↩ Tool result · `toolu_015FAmkUp9v27gAtdTEdX4zU`</summary>

```text
Web search results for query: "model uncertainty gating signal explanation selection human-AI decision making 2025 2026"

Links: [{"title":"Uncertainty Gating for Cost-Aware Explainable Artificial Intelligence","url":"https://arxiv.org/html/2603.29915v1"},{"title":"Harnessing Human Uncertainty to Train More Accurate and Aligned AI Systems | Decision Analysis","url":"https://pubsonline.informs.org/doi/abs/10.1287/deca.2025.0395?af=R"},{"title":"Using AI Uncertainty Quantification to Improve Human Decision-Making","url":"https://arxiv.org/pdf/2309.10852"},{"title":"A Quantum Probability Approach to Improving Human–AI Decision Making - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11854726/"},{"title":"DeCoDe: Defer-and-Complement Decision-Making via Decoupled Concept Bottleneck Models","url":"https://arxiv.org/pdf/2505.19220"}]

Based on the search results, here are several relevant recent works on model uncertainty, gating signals, and explanation selection in human-AI decision making from 2025-2026:

## Key Research Findings

**Uncertainty Gating for Explainable AI:**
Epistemic uncertainty can serve as a low-cost proxy for explanation reliability, with high epistemic uncertainty identifying regions where decision boundaries are poorly defined and explanations become unstable and unfaithful. This enables two complementary use cases: routing samples to appropriate XAI methods based on expected explanation reliability, and deferring explanation generation for uncertain samples under constrained budgets.

**Human-AI Collaborative Decision Making:**
Human-AI collaboration is increasingly adopted for high-stakes decision-making tasks, with models learning to defer decisions to humans when faced with uncertain cases through Learning to Defer strategies. Recent frameworks leverage interpretable concept representations to support flexible strategy selection—autonomous AI, human-only, and human-AI complementarity—guided by concept-driven gating networks.

**Uncertainty Quantification in Human Decision-Making:**
AI Uncertainty Quantification has the potential to improve human decision-making beyond AI predictions alone by providing additional probabilistic information to users. Research shows that instance-level uncertainty quantification was beneficial for decision-making performance compared to only AI predictions, with generalizable benefits across various representations for probabilistic information.

Human Uncertainty in AI Training:
Recent work examines AI-augmented decision making that leverages computational power of machine learning models to assist humans, with approaches to train more accurate and aligned AI systems by harnessing human uncertainty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3697d67b-d082-406b-bc72-84051ebca580",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "6dea553a-cfb3-4c19-ad68-0e3ebc5367d0",
  "toolUseResult": {
    "query": "model uncertainty gating signal explanation selection human-AI decision making 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XSkeUKQp8dkWHBa414PuB9",
        "content": [
          {
            "title": "Uncertainty Gating for Cost-Aware Explainable Artificial Intelligence",
            "url": "https://arxiv.org/html/2603.29915v1"
          },
          {
            "title": "Harnessing Human Uncertainty to Train More Accurate and Aligned AI Systems | Decision Analysis",
            "url": "https://pubsonline.informs.org/doi/abs/10.1287/deca.2025.0395?af=R"
          },
          {
            "title": "Using AI Uncertainty Quantification to Improve Human Decision-Making",
            "url": "https://arxiv.org/pdf/2309.10852"
          },
          {
            "title": "A Quantum Probability Approach to Improving Human–AI Decision Making - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11854726/"
          },
          {
            "title": "DeCoDe: Defer-and-Complement Decision-Making via Decoupled Concept Bottleneck Models",
            "url": "https://arxiv.org/pdf/2505.19220"
          }
        ]
      },
      "Based on the search results, here are several relevant recent works on model uncertainty, gating signals, and explanation selection in human-AI decision making from 2025-2026:\n\n## Key Research Findings\n\n**Uncertainty Gating for Explainable AI:**\nEpistemic uncertainty can serve as a low-cost proxy for explanation reliability, with high epistemic uncertainty identifying regions where decision boundaries are poorly defined and explanations become unstable and unfaithful. This enables two complementary use cases: routing samples to appropriate XAI methods based on expected explanation reliability, and deferring explanation generation for uncertain samples under constrained budgets.\n\n**Human-AI Collaborative Decision Making:**\nHuman-AI collaboration is increasingly adopted for high-stakes decision-making tasks, with models learning to defer decisions to humans when faced with uncertain cases through Learning to Defer strategies. Recent frameworks leverage interpretable concept representations to support flexible strategy selection—autonomous AI, human-only, and human-AI complementarity—guided by concept-driven gating networks.\n\n**Uncertainty Quantification in Human Decision-Making:**\nAI Uncertainty Quantification has the potential to improve human decision-making beyond AI predictions alone by providing additional probabilistic information to users. Research shows that instance-level uncertainty quantification was beneficial for decision-making performance compared to only AI predictions, with generalizable benefits across various representations for probabilistic information.\n\nHuman Uncertainty in AI Training:\nRecent work examines AI-augmented decision making that leverages computational power of machine learning models to assist humans, with approaches to train more accurate and aligned AI systems by harnessing human uncertainty."
    ],
    "durationSeconds": 8.492814048999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3697d67b-d082-406b-bc72-84051ebca580",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T04:46:02.373Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed some key papers exist. Let me continue with more targeted searches to understand the competitive landscape better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dea553a-cfb3-4c19-ad68-0e3ebc5367d0",
  "isSidechain": false,
  "requestId": "req_011CbDDJNg9845SvDykfNrFE",
  "type": "assistant",
  "uuid": "e60599e2-f53d-44af-9374-49c4638f9cc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuMK1NNe1yb6PDFiwdPtdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 24834,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 24834,
          "cache_creation_input_tokens": 3281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3281
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

_source line 24 · 2026-05-20T04:46:03.331Z_

Good, key papers are confirmed. Let me do more targeted searches on the specific novelty claims and competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e60599e2-f53d-44af-9374-49c4638f9cc9",
  "isSidechain": false,
  "requestId": "req_011CbDDJNg9845SvDykfNrFE",
  "type": "assistant",
  "uuid": "97c895ec-51b5-4447-bcec-b46b23d1e332",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuMK1NNe1yb6PDFiwdPtdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 24834,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 24834,
          "cache_creation_input_tokens": 3281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3281
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

_source line 25 · 2026-05-20T04:46:04.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ch7SBvRkNDZj6ZQbiAhQR`</summary>

```json
{
  "query": "arXiv 2412.15584 \"To Rely or Not to Rely\" uncertainty highlighting algorithm aversion CHI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97c895ec-51b5-4447-bcec-b46b23d1e332",
  "isSidechain": false,
  "requestId": "req_011CbDDJNg9845SvDykfNrFE",
  "type": "assistant",
  "uuid": "8ab1c04a-a07f-4efb-adfe-8934c03d9ad8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuMK1NNe1yb6PDFiwdPtdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 24834,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 24834,
          "cache_creation_input_tokens": 3281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3281
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

_source line 26 · 2026-05-20T04:46:05.698Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Si5vi1YkPo5uxmNfGdzWNg`</summary>

```json
{
  "query": "arXiv 2603.21172 \"entropy alone insufficient\" semantic entropy probability correctness probe LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ab1c04a-a07f-4efb-adfe-8934c03d9ad8",
  "isSidechain": false,
  "requestId": "req_011CbDDJNg9845SvDykfNrFE",
  "type": "assistant",
  "uuid": "3c1cd094-20d4-4ed7-acaf-f9b42d3e3fb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuMK1NNe1yb6PDFiwdPtdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 24834,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 24834,
          "cache_creation_input_tokens": 3281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3281
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

_source line 27 · 2026-05-20T04:46:06.269Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ziS22H4oqJoDKTgmzbr2p`</summary>

```json
{
  "query": "uncertainty-based adaptive explanation triggering overreliance LLM backend gating 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c1cd094-20d4-4ed7-acaf-f9b42d3e3fb7",
  "isSidechain": false,
  "requestId": "req_011CbDDJNg9845SvDykfNrFE",
  "type": "assistant",
  "uuid": "0fb54db0-0207-473e-9d7c-0b64169cf163",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuMK1NNe1yb6PDFiwdPtdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3281,
      "cache_read_input_tokens": 24834,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 24834,
          "cache_creation_input_tokens": 3281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3281
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

_source line 28 · 2026-05-20T04:46:11.613Z_

<details><summary>↩ Tool result · `toolu_015ch7SBvRkNDZj6ZQbiAhQR`</summary>

```text
Web search results for query: "arXiv 2412.15584 "To Rely or Not to Rely" uncertainty highlighting algorithm aversion CHI 2025"

Links: [{"title":"To Rely or Not to Rely? Evaluating Interventions for ...","url":"https://arxiv.org/pdf/2412.15584"},{"title":"To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models","url":"https://arxiv.org/html/2412.15584"},{"title":"The extent of algorithm aversion in decision-making situations with varying gravity","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9942970/"},{"title":"[2412.15584] To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models","url":"https://arxiv.org/abs/2412.15584"},{"title":"Should I Trust the Artificial Intelligence to Recruit? Recruiters’ Perceptions and Behavior When Faced With Algorithm-Based Recommendation Systems During Resume Screening","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9298741/"},{"title":"Two distinct and separable processes underlie individual differences in algorithm adherence: Differences in predictions and differences in trust thresholds","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7906384/"},{"title":"Blame the Machine? Insights From an Experiment on Algorithm Aversion and Blame Avoidance in Computer-Aided Human Resource Management","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9177159/"}]

Great! I found the paper you're looking for. Here's what the search reveals:

"To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models" is a paper presented at CHI '25 (April 26–May 01, 2025, Yokohama, Japan).

The paper addresses algorithm aversion—the tendency to distrust algorithmic agents—which can lead users to ignore helpful recommendations due to general distrust towards the technology. The research emphasizes that conscious effort must be placed on helping users calibrate appropriate levels of trust and reliance on LLM advice.

The study examines several LLM reliance interventions including Reliance Disclaimer, Uncertainty Highlighting, and Implicit Answer. Regarding the Uncertainty Highlighting intervention specifically, the research found that Uncertainty Highlighting was the only intervention that had significantly lower ratings in all categories compared to Control, indicating that the implementation may have induced too much uncertainty in the users. The main implication is that uncertainty calibration methods can have the undesirable outcome of inducing negative perceptions of accuracy and usefulness of the LLM, which increases overall algorithm aversion against LLM advice, rather than appropriate reliance.

You can access the full paper at the arXiv link: https://arxiv.org/abs/2412.15584


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ab1c04a-a07f-4efb-adfe-8934c03d9ad8",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "39dc3b52-c0f0-4a55-b520-095ea08f3b25",
  "toolUseResult": {
    "query": "arXiv 2412.15584 \"To Rely or Not to Rely\" uncertainty highlighting algorithm aversion CHI 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q1k43nHRz7Cho5TeHCGdy3",
        "content": [
          {
            "title": "To Rely or Not to Rely? Evaluating Interventions for ...",
            "url": "https://arxiv.org/pdf/2412.15584"
          },
          {
            "title": "To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models",
            "url": "https://arxiv.org/html/2412.15584"
          },
          {
            "title": "The extent of algorithm aversion in decision-making situations with varying gravity",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9942970/"
          },
          {
            "title": "[2412.15584] To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models",
            "url": "https://arxiv.org/abs/2412.15584"
          },
          {
            "title": "Should I Trust the Artificial Intelligence to Recruit? Recruiters’ Perceptions and Behavior When Faced With Algorithm-Based Recommendation Systems During Resume Screening",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9298741/"
          },
          {
            "title": "Two distinct and separable processes underlie individual differences in algorithm adherence: Differences in predictions and differences in trust thresholds",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7906384/"
          },
          {
            "title": "Blame the Machine? Insights From an Experiment on Algorithm Aversion and Blame Avoidance in Computer-Aided Human Resource Management",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9177159/"
          }
        ]
      },
      "Great! I found the paper you're looking for. Here's what the search reveals:\n\n\"To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models\" is a paper presented at CHI '25 (April 26–May 01, 2025, Yokohama, Japan).\n\nThe paper addresses algorithm aversion—the tendency to distrust algorithmic agents—which can lead users to ignore helpful recommendations due to general distrust towards the technology. The research emphasizes that conscious effort must be placed on helping users calibrate appropriate levels of trust and reliance on LLM advice.\n\nThe study examines several LLM reliance interventions including Reliance Disclaimer, Uncertainty Highlighting, and Implicit Answer. Regarding the Uncertainty Highlighting intervention specifically, the research found that Uncertainty Highlighting was the only intervention that had significantly lower ratings in all categories compared to Control, indicating that the implementation may have induced too much uncertainty in the users. The main implication is that uncertainty calibration methods can have the undesirable outcome of inducing negative perceptions of accuracy and usefulness of the LLM, which increases overall algorithm aversion against LLM advice, rather than appropriate reliance.\n\nYou can access the full paper at the arXiv link: https://arxiv.org/abs/2412.15584"
    ],
    "durationSeconds": 6.857534487999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8ab1c04a-a07f-4efb-adfe-8934c03d9ad8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T04:46:13.739Z_

<details><summary>↩ Tool result · `toolu_017ziS22H4oqJoDKTgmzbr2p`</summary>

```text
Web search results for query: "uncertainty-based adaptive explanation triggering overreliance LLM backend gating 2025 2026"

Links: [{"title":"From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models","url":"https://arxiv.org/pdf/2601.15690"},{"title":"Unlocking the Power of LLM Uncertainty for Active In-Context Example   Selection","url":"https://arxiv.org/pdf/2408.09172"},{"title":"[2506.07448] Extending Epistemic Uncertainty Beyond Parameters Would Assist in Designing Reliable LLMs","url":"https://arxiv.org/abs/2506.07448"},{"title":"An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"},{"title":"Quantifying Uncertainty in Natural Language Explanations of Large   Language Models","url":"https://arxiv.org/pdf/2311.03533"},{"title":"The Illusion of Certainty: Uncertainty Quantification for LLMs Fails under","url":"https://arxiv.org/pdf/2511.04418"},{"title":"Extending Epistemic Uncertainty Beyond Parameters Would Assist in Designing Reliable LLMs","url":"https://arxiv.org/html/2506.07448v1"}]

I've successfully performed the web search. The results reveal several relevant research papers on uncertainty quantification and related topics in Large Language Models from 2025-2026:

**Key findings:**

1. Recent work discusses how uncertainty quantification is evolving from passive post-hoc evaluation metrics to more active approaches that provide real-time feedback, particularly important for multi-step reasoning and complex LLM applications.

2. Research proposes that the wavering behavior in LLMs (including sycophancy) can reflect intrinsic uncertainty and serve as a useful indicator for performing active selection tasks.

3. Automation bias represents a challenge where users overtrust AI outputs without critical scrutiny, with overreliance reinforcing systematic inconsistencies in model predictions.

4. An emerging framework enables LLMs to take contextually appropriate steps like requesting clarification or retrieving external information, supporting active resolution for more reliable and transparent systems.

5. Recent work from January 2026 examines uncertainty quantification for LLMs under different conditions.

The search results show active research into uncertainty-based mechanisms for improving LLM reliability, though the specific combination of all terms in your query (adaptive explanation triggering and backend gating) may be more narrowly focused within this broader research landscape.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fb54db0-0207-473e-9d7c-0b64169cf163",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "2775b562-6aa7-49f6-a1fa-ff3bab486dbf",
  "toolUseResult": {
    "query": "uncertainty-based adaptive explanation triggering overreliance LLM backend gating 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AymNcYwdsaDNFnijxgNigq",
        "content": [
          {
            "title": "From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models",
            "url": "https://arxiv.org/pdf/2601.15690"
          },
          {
            "title": "Unlocking the Power of LLM Uncertainty for Active In-Context Example   Selection",
            "url": "https://arxiv.org/pdf/2408.09172"
          },
          {
            "title": "[2506.07448] Extending Epistemic Uncertainty Beyond Parameters Would Assist in Designing Reliable LLMs",
            "url": "https://arxiv.org/abs/2506.07448"
          },
          {
            "title": "An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"
          },
          {
            "title": "Quantifying Uncertainty in Natural Language Explanations of Large   Language Models",
            "url": "https://arxiv.org/pdf/2311.03533"
          },
          {
            "title": "The Illusion of Certainty: Uncertainty Quantification for LLMs Fails under",
            "url": "https://arxiv.org/pdf/2511.04418"
          },
          {
            "title": "Extending Epistemic Uncertainty Beyond Parameters Would Assist in Designing Reliable LLMs",
            "url": "https://arxiv.org/html/2506.07448v1"
          }
        ]
      },
      "I've successfully performed the web search. The results reveal several relevant research papers on uncertainty quantification and related topics in Large Language Models from 2025-2026:\n\n**Key findings:**\n\n1. Recent work discusses how uncertainty quantification is evolving from passive post-hoc evaluation metrics to more active approaches that provide real-time feedback, particularly important for multi-step reasoning and complex LLM applications.\n\n2. Research proposes that the wavering behavior in LLMs (including sycophancy) can reflect intrinsic uncertainty and serve as a useful indicator for performing active selection tasks.\n\n3. Automation bias represents a challenge where users overtrust AI outputs without critical scrutiny, with overreliance reinforcing systematic inconsistencies in model predictions.\n\n4. An emerging framework enables LLMs to take contextually appropriate steps like requesting clarification or retrieving external information, supporting active resolution for more reliable and transparent systems.\n\n5. Recent work from January 2026 examines uncertainty quantification for LLMs under different conditions.\n\nThe search results show active research into uncertainty-based mechanisms for improving LLM reliability, though the specific combination of all terms in your query (adaptive explanation triggering and backend gating) may be more narrowly focused within this broader research landscape."
    ],
    "durationSeconds": 7.4628196720000055,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0fb54db0-0207-473e-9d7c-0b64169cf163",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T04:46:14.064Z_

<details><summary>↩ Tool result · `toolu_01Si5vi1YkPo5uxmNfGdzWNg`</summary>

```text
Web search results for query: "arXiv 2603.21172 "entropy alone insufficient" semantic entropy probability correctness probe LLM"

Links: [{"title":"Entropy Alone is Insufficient for Safe Selective Prediction in LLMs","url":"https://arxiv.org/html/2603.21172"},{"title":"[2603.21172] Entropy Alone is Insufficient for Safe Selective Prediction in LLMs","url":"https://arxiv.org/abs/2603.21172"},{"title":"Detecting hallucinations in large language models using semantic entropy","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11186750/"},{"title":"Assessing Correctness in LLM-Based Code Generation via Uncertainty Estimation","url":"https://arxiv.org/pdf/2502.11620"},{"title":"Semantic Entropy Neurons: Encoding Semantic","url":"https://openreview.net/pdf?id=BbZKxrZCNn"},{"title":"[PDF] Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Semantic-Uncertainty:-Linguistic-Invariances-for-in-Kuhn-Gal/507465f8d46489a68a527cb5304d76bdb6c31ed9"},{"title":"Predicting Program Correctness By Ensemble Semantic Entropy","url":"https://arxiv.org/html/2603.27098v1"},{"title":"Semantic Reformulation Entropy for Robust Hallucination Detection in QA Tasks","url":"https://arxiv.org/pdf/2509.17445"}]

Based on the search results, I found the paper you're looking for:

The paper "Entropy Alone is Insufficient for Safe Selective Prediction in LLMs" (arXiv:2603.21172) was submitted on March 22, 2026, by Edward Phillips and 4 other authors.

**Key findings:**

Selective prediction systems can mitigate harms from language model hallucinations by abstaining from answering in high-risk cases, using uncertainty quantification techniques to identify such cases. However, the paper identifies a model-dependent failure mode of entropy-based uncertainty methods that leads to unreliable abstention behaviour, and addresses it by combining entropy scores with a correctness probe signal.

Semantic entropy (SE) is the stronger detector for Llama and Ministral on TriviaQA, while the correctness probe (PC probe) dominates for Qwen, with the two signals being only moderately correlated and capturing complementary aspects of model uncertainty.

The primary failure mode of semantic entropy for the Qwen model involves a substantial fraction of questions being assigned near-zero semantic entropy, a cluster that includes both correct answers and hallucinations (confidently wrong instances where the output distribution lacks diversity despite being incorrect).

The combined entropy and correctness probe score generally improves both the risk-coverage trade-off and calibration performance relative to entropy-only baselines across three QA benchmarks (TriviaQA, BioASQ, MedicalQA) and four model families.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c1cd094-20d4-4ed7-acaf-f9b42d3e3fb7",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "f70516f6-fc95-4c8d-84f3-320e00e7405b",
  "toolUseResult": {
    "query": "arXiv 2603.21172 \"entropy alone insufficient\" semantic entropy probability correctness probe LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AqjVW1fRAgQja16qN6aymM",
        "content": [
          {
            "title": "Entropy Alone is Insufficient for Safe Selective Prediction in LLMs",
            "url": "https://arxiv.org/html/2603.21172"
          },
          {
            "title": "[2603.21172] Entropy Alone is Insufficient for Safe Selective Prediction in LLMs",
            "url": "https://arxiv.org/abs/2603.21172"
          },
          {
            "title": "Detecting hallucinations in large language models using semantic entropy",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11186750/"
          },
          {
            "title": "Assessing Correctness in LLM-Based Code Generation via Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2502.11620"
          },
          {
            "title": "Semantic Entropy Neurons: Encoding Semantic",
            "url": "https://openreview.net/pdf?id=BbZKxrZCNn"
          },
          {
            "title": "[PDF] Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Semantic-Uncertainty:-Linguistic-Invariances-for-in-Kuhn-Gal/507465f8d46489a68a527cb5304d76bdb6c31ed9"
          },
          {
            "title": "Predicting Program Correctness By Ensemble Semantic Entropy",
            "url": "https://arxiv.org/html/2603.27098v1"
          },
          {
            "title": "Semantic Reformulation Entropy for Robust Hallucination Detection in QA Tasks",
            "url": "https://arxiv.org/pdf/2509.17445"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Entropy Alone is Insufficient for Safe Selective Prediction in LLMs\" (arXiv:2603.21172) was submitted on March 22, 2026, by Edward Phillips and 4 other authors.\n\n**Key findings:**\n\nSelective prediction systems can mitigate harms from language model hallucinations by abstaining from answering in high-risk cases, using uncertainty quantification techniques to identify such cases. However, the paper identifies a model-dependent failure mode of entropy-based uncertainty methods that leads to unreliable abstention behaviour, and addresses it by combining entropy scores with a correctness probe signal.\n\nSemantic entropy (SE) is the stronger detector for Llama and Ministral on TriviaQA, while the correctness probe (PC probe) dominates for Qwen, with the two signals being only moderately correlated and capturing complementary aspects of model uncertainty.\n\nThe primary failure mode of semantic entropy for the Qwen model involves a substantial fraction of questions being assigned near-zero semantic entropy, a cluster that includes both correct answers and hallucinations (confidently wrong instances where the output distribution lacks diversity despite being incorrect).\n\nThe combined entropy and correctness probe score generally improves both the risk-coverage trade-off and calibration performance relative to entropy-only baselines across three QA benchmarks (TriviaQA, BioASQ, MedicalQA) and four model families."
    ],
    "durationSeconds": 8.361751971999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3c1cd094-20d4-4ed7-acaf-f9b42d3e3fb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T04:46:14.069Z_

```json
{
  "parentUuid": "f70516f6-fc95-4c8d-84f3-320e00e7405b",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0e0f3ee5-cd25-4876-8d96-7f02f5ac02e4",
  "timestamp": "2026-05-20T04:46:14.069Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "0e0f3ee5-cd25-4876-8d96-7f02f5ac02e4",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Model uncertainty vs. user trust for adaptive AI explanations",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Assistant

_source line 34 · 2026-05-20T04:46:18.458Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for a few more things to round out my understanding:
1. Whether anyone has already done "uncertainty as backend gating for explanation type" specifically
2. The "Unequal Uncertainty" paper (2508.07872)
3. Li et al. CHI 2025 "From Text to Trust" adaptive explanation selection
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e0f3ee5-cd25-4876-8d96-7f02f5ac02e4",
  "isSidechain": false,
  "requestId": "req_011CbDDKQcFqxeE3RgUSxrG4",
  "type": "assistant",
  "uuid": "9aac939e-8d9f-44fa-a604-960692b00872",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN8FhpUjARLW8Bp4RXEca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 677,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 28115,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 677,
          "output_tokens": 304,
          "cache_read_input_tokens": 28115,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1915
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

_source line 35 · 2026-05-20T04:46:18.958Z_

Let me search for a few more critical aspects of the competitive landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9aac939e-8d9f-44fa-a604-960692b00872",
  "isSidechain": false,
  "requestId": "req_011CbDDKQcFqxeE3RgUSxrG4",
  "type": "assistant",
  "uuid": "dae3068c-d452-4f28-8fd8-54d7501a4262",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN8FhpUjARLW8Bp4RXEca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 677,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 28115,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 677,
          "output_tokens": 304,
          "cache_read_input_tokens": 28115,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1915
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

_source line 36 · 2026-05-20T04:46:19.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013uTNWN6Y7rRQ9TJw25WhBZ`</summary>

```json
{
  "query": "arXiv 2508.07872 \"Unequal Uncertainty\" fairness uncertainty-gated interventions discrimination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dae3068c-d452-4f28-8fd8-54d7501a4262",
  "isSidechain": false,
  "requestId": "req_011CbDDKQcFqxeE3RgUSxrG4",
  "type": "assistant",
  "uuid": "e7031f91-6c76-40b1-9710-a6006c50b3c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN8FhpUjARLW8Bp4RXEca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 677,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 28115,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 677,
          "output_tokens": 304,
          "cache_read_input_tokens": 28115,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1915
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

_source line 37 · 2026-05-20T04:46:20.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HSqLJcQt1mPvadfe48Z27q`</summary>

```json
{
  "query": "\"From Text to Trust\" Li CHI 2025 arXiv 2502.11919 adaptive explanation selection LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7031f91-6c76-40b1-9710-a6006c50b3c1",
  "isSidechain": false,
  "requestId": "req_011CbDDKQcFqxeE3RgUSxrG4",
  "type": "assistant",
  "uuid": "207fa883-8bbd-4c13-8ce2-cd9cc832a156",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN8FhpUjARLW8Bp4RXEca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 677,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 28115,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 677,
          "output_tokens": 304,
          "cache_read_input_tokens": 28115,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1915
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

_source line 38 · 2026-05-20T04:46:21.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LEcBgoSdeCfqVoDoqtNKuE`</summary>

```json
{
  "query": "non-inferiority equivalence testing human-AI collaboration overreliance TOST 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "207fa883-8bbd-4c13-8ce2-cd9cc832a156",
  "isSidechain": false,
  "requestId": "req_011CbDDKQcFqxeE3RgUSxrG4",
  "type": "assistant",
  "uuid": "cb109506-4ac2-4801-893d-3ae836e732e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQN8FhpUjARLW8Bp4RXEca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 677,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 28115,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 677,
          "output_tokens": 304,
          "cache_read_input_tokens": 28115,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1915
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

_source line 39 · 2026-05-20T04:46:26.902Z_

<details><summary>↩ Tool result · `toolu_01HSqLJcQt1mPvadfe48Z27q`</summary>

```text
Web search results for query: ""From Text to Trust" Li CHI 2025 arXiv 2502.11919 adaptive explanation selection LLM"

Links: [{"title":"[2502.11919] From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis","url":"https://arxiv.org/abs/2502.11919"},{"title":"From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250211919L/abstract"},{"title":"From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis","url":"https://arxiv.org/html/2502.11919"},{"title":"The accuracy-bias trade-offs in AI text detection tools and their impact on fairness in scholarly publication","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12453642/"},{"title":"Public Trust in Artificial Intelligence Applications in Mental Health Care: Topic Modeling Analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9758643/"},{"title":"Spelling Errors in Brief Computer-Mediated Texts Implicitly Lead to Linearly Additive Penalties in Trustworthiness","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9121982/"},{"title":"The influence of mental state attributions on trust in large language models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12104094/"},{"title":"Can Large Language Model Agents Simulate Human Trust Behavior?","url":"https://arxiv.org/pdf/2402.04559"}]

I found the paper you're looking for! Here's what the search reveals:

"From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis" is authored by Zhuoyan Li and 4 other authors, and it's a CHI 2025 paper with arXiv identifier 2502.11919.

**Key findings from the paper:**

The paper discusses how Large language models (LLMs), with their exceptional conversational and analytical capabilities, present opportunities to enhance AI-assisted decision making by providing natural-language-based analysis of AI's decision recommendation, such as how each feature of a decision making task might contribute to the AI recommendation.

Via a randomized experiment, the authors show that presenting LLM-powered analysis of each task feature, either sequentially or concurrently, does not significantly improve people's AI-assisted decision performance.

The paper appears to be addressing an important gap in AI-assisted decision making by exploring how LLM-generated explanations can help users better understand and trust AI recommendations, though the initial results suggest that simply providing these explanations may not be sufficient on their own.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "207fa883-8bbd-4c13-8ce2-cd9cc832a156",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "6c2b8a35-4c23-4b78-a809-27f54afcb6ea",
  "toolUseResult": {
    "query": "\"From Text to Trust\" Li CHI 2025 arXiv 2502.11919 adaptive explanation selection LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F7XBQ9n54yoMcvKtVxCPjy",
        "content": [
          {
            "title": "[2502.11919] From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis",
            "url": "https://arxiv.org/abs/2502.11919"
          },
          {
            "title": "From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250211919L/abstract"
          },
          {
            "title": "From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis",
            "url": "https://arxiv.org/html/2502.11919"
          },
          {
            "title": "The accuracy-bias trade-offs in AI text detection tools and their impact on fairness in scholarly publication",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12453642/"
          },
          {
            "title": "Public Trust in Artificial Intelligence Applications in Mental Health Care: Topic Modeling Analysis",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9758643/"
          },
          {
            "title": "Spelling Errors in Brief Computer-Mediated Texts Implicitly Lead to Linearly Additive Penalties in Trustworthiness",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9121982/"
          },
          {
            "title": "The influence of mental state attributions on trust in large language models",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12104094/"
          },
          {
            "title": "Can Large Language Model Agents Simulate Human Trust Behavior?",
            "url": "https://arxiv.org/pdf/2402.04559"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search reveals:\n\n\"From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis\" is authored by Zhuoyan Li and 4 other authors, and it's a CHI 2025 paper with arXiv identifier 2502.11919.\n\n**Key findings from the paper:**\n\nThe paper discusses how Large language models (LLMs), with their exceptional conversational and analytical capabilities, present opportunities to enhance AI-assisted decision making by providing natural-language-based analysis of AI's decision recommendation, such as how each feature of a decision making task might contribute to the AI recommendation.\n\nVia a randomized experiment, the authors show that presenting LLM-powered analysis of each task feature, either sequentially or concurrently, does not significantly improve people's AI-assisted decision performance.\n\nThe paper appears to be addressing an important gap in AI-assisted decision making by exploring how LLM-generated explanations can help users better understand and trust AI recommendations, though the initial results suggest that simply providing these explanations may not be sufficient on their own."
    ],
    "durationSeconds": 5.959058638000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "207fa883-8bbd-4c13-8ce2-cd9cc832a156",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T04:46:26.983Z_

<details><summary>↩ Tool result · `toolu_013uTNWN6Y7rRQ9TJw25WhBZ`</summary>

```text
Web search results for query: "arXiv 2508.07872 "Unequal Uncertainty" fairness uncertainty-gated interventions discrimination"

Links: [{"title":"[2508.07872] Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI","url":"https://arxiv.org/abs/2508.07872"},{"title":"[2508.07872v1] Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI","url":"https://arxiv.org/abs/2508.07872v1"},{"title":"Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating","url":"https://arxiv.org/pdf/2508.07872"},{"title":"Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI","url":"https://arxiv.org/html/2508.07872"},{"title":"[2604.21711] Fairness under uncertainty in sequential decisions","url":"https://arxiv.org/abs/2604.21711"}]

I found the paper! Here's what arXiv 2508.07872 is about:

The paper provides the first integrated socio-technical and legal analysis of uncertainty-based algorithmic interventions. 

The paper addresses how uncertainty in artificial intelligence (AI) predictions poses urgent legal and ethical challenges for AI-assisted decision-making.

The paper examines two algorithmic interventions that act as guardrails for human-AI collaboration: selective abstention, which withholds high-uncertainty predictions from human decision-makers, and selective friction, which delivers those predictions together with salient warnings or disclosures that slow the decision process.

Research has shown that selective abstention based on uncertainty can inadvertently exacerbate disparities and disadvantage under-represented groups that disproportionately receive uncertain predictions.

Through two case studies, AI-assisted consumer credit decisions and AI-assisted content moderation, the paper demonstrates how the seemingly neutral use of uncertainty thresholds can trigger discriminatory impacts.

The paper argues that, although both interventions pose risks of unlawful discrimination under UK law, selective frictions offer a promising pathway toward fairer and more accountable AI-assisted decision-making by preserving transparency and encouraging more cautious human judgment.

The paper was submitted on August 11, 2025, and was authored by Holli Sargeant, Mackenzie Jorgensen, Arina Shah, Adrian Weller, and Umang Bhatt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7031f91-6c76-40b1-9710-a6006c50b3c1",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "476c2b9a-2ea9-4fdf-9764-c11daf2cb580",
  "toolUseResult": {
    "query": "arXiv 2508.07872 \"Unequal Uncertainty\" fairness uncertainty-gated interventions discrimination",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YPSTRrCgNNQSzwd5jgewq8",
        "content": [
          {
            "title": "[2508.07872] Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI",
            "url": "https://arxiv.org/abs/2508.07872"
          },
          {
            "title": "[2508.07872v1] Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI",
            "url": "https://arxiv.org/abs/2508.07872v1"
          },
          {
            "title": "Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating",
            "url": "https://arxiv.org/pdf/2508.07872"
          },
          {
            "title": "Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI",
            "url": "https://arxiv.org/html/2508.07872"
          },
          {
            "title": "[2604.21711] Fairness under uncertainty in sequential decisions",
            "url": "https://arxiv.org/abs/2604.21711"
          }
        ]
      },
      "I found the paper! Here's what arXiv 2508.07872 is about:\n\nThe paper provides the first integrated socio-technical and legal analysis of uncertainty-based algorithmic interventions. \n\nThe paper addresses how uncertainty in artificial intelligence (AI) predictions poses urgent legal and ethical challenges for AI-assisted decision-making.\n\nThe paper examines two algorithmic interventions that act as guardrails for human-AI collaboration: selective abstention, which withholds high-uncertainty predictions from human decision-makers, and selective friction, which delivers those predictions together with salient warnings or disclosures that slow the decision process.\n\nResearch has shown that selective abstention based on uncertainty can inadvertently exacerbate disparities and disadvantage under-represented groups that disproportionately receive uncertain predictions.\n\nThrough two case studies, AI-assisted consumer credit decisions and AI-assisted content moderation, the paper demonstrates how the seemingly neutral use of uncertainty thresholds can trigger discriminatory impacts.\n\nThe paper argues that, although both interventions pose risks of unlawful discrimination under UK law, selective frictions offer a promising pathway toward fairer and more accountable AI-assisted decision-making by preserving transparency and encouraging more cautious human judgment.\n\nThe paper was submitted on August 11, 2025, and was authored by Holli Sargeant, Mackenzie Jorgensen, Arina Shah, Adrian Weller, and Umang Bhatt."
    ],
    "durationSeconds": 7.049102044,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e7031f91-6c76-40b1-9710-a6006c50b3c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T04:46:30.043Z_

<details><summary>↩ Tool result · `toolu_01LEcBgoSdeCfqVoDoqtNKuE`</summary>

```text
Web search results for query: "non-inferiority equivalence testing human-AI collaboration overreliance TOST 2025 2026"

Links: [{"title":"When Thinking Pays Off: Incentive Alignment for Human-AI Collaboration","url":"https://arxiv.org/pdf/2511.09612"},{"title":"Auditor Models to Suppress Poor AI Predictions Can Improve Human-AI Collaborative Performance","url":"https://www.medrxiv.org/content/10.1101/2025.06.24.25330212.full.pdf"},{"title":"Uncalibrated Models Can Improve Human-AI Collaboration","url":"https://arxiv.org/pdf/2202.05983"},{"title":"Exploring automation bias in human–AI collaboration: a review and implications for explainable AI | AI & SOCIETY | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00146-025-02422-7"},{"title":"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://arxiv.org/pdf/2502.13321"},{"title":"Bias in the Loop: How Humans Evaluate AI-Generated Suggestions","url":"https://arxiv.org/pdf/2509.08514"},{"title":"Revealing AI Reasoning Increases Trust but Crowds Out Unique Human Knowledge","url":"https://arxiv.org/pdf/2511.04050"},{"title":"Neither better nor worse? Equivalence, non-inferiority and non-superiority tests - VSNi","url":"https://vsni.co.uk/neither-better-nor-worse-equivalence-non-inferiority-and-non-superiority-tests-2/"},{"title":"Explanations Can Reduce Overreliance on AI Systems During   Decision-Making","url":"https://arxiv.org/pdf/2212.06823"}]

I found several relevant results on human-AI collaboration and overreliance, though the specific combination of all those topics together is quite specialized. Here's what the search revealed:

## Recent Research on Human-AI Collaboration and Overreliance (2025-2026)

Recent work investigates the effectiveness of mechanisms in mitigating overreliance on AI. Several 2026 conference papers address this issue directly:

- One study examines "When Thinking Pays Off: Incentive Alignment for Human-AI Collaboration" at the 2026 ACM Conference on Fairness, Accountability, and Transparency, exploring how incentive mechanisms can promote appropriate reliance.

- Another 2026 paper titled "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance" was presented at the International Conference on Intelligent User Interfaces, showing that over-reliance can be reduced by adaptively inserting forced pauses to promote deliberation, which facilitates appropriate reliance.

## Understanding Overreliance

Overreliance occurs when humans fail to correct incorrect AI predictions. Research documents "algorithm appreciation" and overreliance where people tend to defer to AI even when suboptimal, which can crowd out the use of unique human knowledge and degrade performance.

## Statistical Methods

Regarding TOST (Two One-Sided t-tests), equivalence tests can be performed using the TOST method, and non-inferiority and non-superiority tests are one-sided alternatives to the equivalence test, with non-inferiority used to demonstrate that one mean is not unacceptably lower than another.

However, I didn't find specific papers that directly combine all of these elements together (non-inferiority testing + equivalence testing + TOST + human-AI collaboration + overreliance). If you're looking for a specific paper or study, you may want to refine the search terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb109506-4ac2-4801-893d-3ae836e732e0",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "52e60ac3-8992-4086-955d-de08b6bc68c8",
  "toolUseResult": {
    "query": "non-inferiority equivalence testing human-AI collaboration overreliance TOST 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018BBbCLnV1uhthjSCZgYuVW",
        "content": [
          {
            "title": "When Thinking Pays Off: Incentive Alignment for Human-AI Collaboration",
            "url": "https://arxiv.org/pdf/2511.09612"
          },
          {
            "title": "Auditor Models to Suppress Poor AI Predictions Can Improve Human-AI Collaborative Performance",
            "url": "https://www.medrxiv.org/content/10.1101/2025.06.24.25330212.full.pdf"
          },
          {
            "title": "Uncalibrated Models Can Improve Human-AI Collaboration",
            "url": "https://arxiv.org/pdf/2202.05983"
          },
          {
            "title": "Exploring automation bias in human–AI collaboration: a review and implications for explainable AI | AI & SOCIETY | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s00146-025-02422-7"
          },
          {
            "title": "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://arxiv.org/pdf/2502.13321"
          },
          {
            "title": "Bias in the Loop: How Humans Evaluate AI-Generated Suggestions",
            "url": "https://arxiv.org/pdf/2509.08514"
          },
          {
            "title": "Revealing AI Reasoning Increases Trust but Crowds Out Unique Human Knowledge",
            "url": "https://arxiv.org/pdf/2511.04050"
          },
          {
            "title": "Neither better nor worse? Equivalence, non-inferiority and non-superiority tests - VSNi",
            "url": "https://vsni.co.uk/neither-better-nor-worse-equivalence-non-inferiority-and-non-superiority-tests-2/"
          },
          {
            "title": "Explanations Can Reduce Overreliance on AI Systems During   Decision-Making",
            "url": "https://arxiv.org/pdf/2212.06823"
          }
        ]
      },
      "I found several relevant results on human-AI collaboration and overreliance, though the specific combination of all those topics together is quite specialized. Here's what the search revealed:\n\n## Recent Research on Human-AI Collaboration and Overreliance (2025-2026)\n\nRecent work investigates the effectiveness of mechanisms in mitigating overreliance on AI. Several 2026 conference papers address this issue directly:\n\n- One study examines \"When Thinking Pays Off: Incentive Alignment for Human-AI Collaboration\" at the 2026 ACM Conference on Fairness, Accountability, and Transparency, exploring how incentive mechanisms can promote appropriate reliance.\n\n- Another 2026 paper titled \"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance\" was presented at the International Conference on Intelligent User Interfaces, showing that over-reliance can be reduced by adaptively inserting forced pauses to promote deliberation, which facilitates appropriate reliance.\n\n## Understanding Overreliance\n\nOverreliance occurs when humans fail to correct incorrect AI predictions. Research documents \"algorithm appreciation\" and overreliance where people tend to defer to AI even when suboptimal, which can crowd out the use of unique human knowledge and degrade performance.\n\n## Statistical Methods\n\nRegarding TOST (Two One-Sided t-tests), equivalence tests can be performed using the TOST method, and non-inferiority and non-superiority tests are one-sided alternatives to the equivalence test, with non-inferiority used to demonstrate that one mean is not unacceptably lower than another.\n\nHowever, I didn't find specific papers that directly combine all of these elements together (non-inferiority testing + equivalence testing + TOST + human-AI collaboration + overreliance). If you're looking for a specific paper or study, you may want to refine the search terms."
    ],
    "durationSeconds": 8.469553959999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cb109506-4ac2-4801-893d-3ae836e732e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T04:46:34.519Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to form my assessment. Let me also do one more search to check if there's any existing work that directly compares model uncertainty vs. user trust as gating signals, which is the central claim of novelty here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52e60ac3-8992-4086-955d-de08b6bc68c8",
  "isSidechain": false,
  "requestId": "req_011CbDDLbMhBJ3jEbMCoJUQW",
  "type": "assistant",
  "uuid": "30b724e8-342f-4497-a2c4-549486c8bd1e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1xwbp5mCyQYSHHPCn7gd1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3294,
      "cache_read_input_tokens": 30030,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 30030,
          "cache_creation_input_tokens": 3294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3294
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

_source line 43 · 2026-05-20T04:46:35.491Z_

One more critical search to check whether the core novelty claim holds — that no work has compared uncertainty vs. trust as gating signals.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30b724e8-342f-4497-a2c4-549486c8bd1e",
  "isSidechain": false,
  "requestId": "req_011CbDDLbMhBJ3jEbMCoJUQW",
  "type": "assistant",
  "uuid": "49fdfb26-2772-4499-80e6-b41d2c099287",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1xwbp5mCyQYSHHPCn7gd1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3294,
      "cache_read_input_tokens": 30030,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 30030,
          "cache_creation_input_tokens": 3294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3294
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

_source line 44 · 2026-05-20T04:46:36.009Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uq8v7dUgerkxrJd3LASRBo`</summary>

```json
{
  "query": "\"model uncertainty\" vs \"user trust\" gating explanation adaptive AI-assisted decision 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49fdfb26-2772-4499-80e6-b41d2c099287",
  "isSidechain": false,
  "requestId": "req_011CbDDLbMhBJ3jEbMCoJUQW",
  "type": "assistant",
  "uuid": "f8c3a5fa-692e-4f26-adb0-bb1e8bb67449",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1xwbp5mCyQYSHHPCn7gd1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3294,
      "cache_read_input_tokens": 30030,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 30030,
          "cache_creation_input_tokens": 3294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3294
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

_source line 45 · 2026-05-20T04:46:43.587Z_

<details><summary>↩ Tool result · `toolu_01Uq8v7dUgerkxrJd3LASRBo`</summary>

```text
Web search results for query: ""model uncertainty" vs "user trust" gating explanation adaptive AI-assisted decision 2024 2025 2026"

Links: [{"title":"Uncertainty reports as explainable AI: A cognitive-adaptive framework for human-AI decision systems in context tasks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1474034625005270"},{"title":"When AI Persuades: Adversarial Explanation Attacks on Human Trust in AI-Assisted Decision Making","url":"https://arxiv.org/pdf/2602.04003"},{"title":"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://arxiv.org/html/2502.13321v1"},{"title":"Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making | Request PDF","url":"https://www.researchgate.net/publication/338841931_Effect_of_confidence_and_explanation_on_accuracy_and_trust_calibration_in_AI-assisted_decision_making"},{"title":"Effect of Confidence and Explanation on Accuracy and Trust Calibration   in AI-Assisted Decision Making","url":"https://arxiv.org/pdf/2001.02114"},{"title":"(PDF) Confronting verbalized uncertainty: Understanding how LLM ’s verbalized uncertainty influences users in AI-assisted decision-making","url":"https://www.researchgate.net/publication/388821876_Confronting_verbalized_uncertainty_Understanding_how_LLM_'s_verbalized_uncertainty_influences_users_in_AI-assisted_decision-making"},{"title":"Designing for Appropriate Reliance: The Roles of AI Uncertainty   Presentation, Initial User Decision, and User Demographics in AI-Assisted   Decision-Making","url":"https://arxiv.org/pdf/2401.05612"},{"title":"Exploring the Impact of Explainable AI and Cognitive Capabilities on Users’ Decisions","url":"https://arxiv.org/html/2505.01192v1"}]

I've found several highly relevant recent research papers on this topic. Here are the key findings:

## Model Uncertainty vs. User Trust in AI-Assisted Decision Making

**Recent Research Framework (2025):**

Research shows that the direction of uncertainty (certainty vs. uncertainty) exerts the strongest influence on decision efficiency and trust, with ambiguity mediating trust and accuracy more than information volume.

**Adaptive Gating and Explanation Strategies:**

The interpretability of AI explanations is context-sensitive—how users perceive and process uncertainty varies by scenario, and current systems fail to capture or adapt to this variability. A proposed Cognitive-Adaptive Framework incorporates user self-reports and contextual variables to identify actionable human feedback signals that can optimize decision performance and inform adaptive model design.

**Uncertainty Expression Approaches:**

Research shows that medium verbalized uncertainty in LLM expressions consistently leads to higher user trust, satisfaction, and task performance compared to high and low verbalized uncertainty. Additionally, providing counter-explanations adaptively mitigates over-reliance when user trust is high, with 10–23% reduction in over-reliance and 8–20% improvement in final decision accuracy.

**Calibration and Presentation:**

Showing calibrated model uncertainty alone is inadequate; rather, calibrating model uncertainty and presenting it in a frequency format allows users to adjust their reliance accordingly and helps reduce confirmation bias effects.

These papers from 2024-2026 suggest an emerging shift toward **adaptive, context-sensitive approaches** that gate explanations based on both model uncertainty and user trust levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8c3a5fa-692e-4f26-adb0-bb1e8bb67449",
  "isSidechain": false,
  "promptId": "49234f69-9c9c-4a69-8689-ec9e8f45c17d",
  "type": "user",
  "uuid": "b270cb6f-3898-4497-8cb5-1f02427497ff",
  "toolUseResult": {
    "query": "\"model uncertainty\" vs \"user trust\" gating explanation adaptive AI-assisted decision 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017fCPhhSbZt1rN2hpQfLKqD",
        "content": [
          {
            "title": "Uncertainty reports as explainable AI: A cognitive-adaptive framework for human-AI decision systems in context tasks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S1474034625005270"
          },
          {
            "title": "When AI Persuades: Adversarial Explanation Attacks on Human Trust in AI-Assisted Decision Making",
            "url": "https://arxiv.org/pdf/2602.04003"
          },
          {
            "title": "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://arxiv.org/html/2502.13321v1"
          },
          {
            "title": "Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making | Request PDF",
            "url": "https://www.researchgate.net/publication/338841931_Effect_of_confidence_and_explanation_on_accuracy_and_trust_calibration_in_AI-assisted_decision_making"
          },
          {
            "title": "Effect of Confidence and Explanation on Accuracy and Trust Calibration   in AI-Assisted Decision Making",
            "url": "https://arxiv.org/pdf/2001.02114"
          },
          {
            "title": "(PDF) Confronting verbalized uncertainty: Understanding how LLM ’s verbalized uncertainty influences users in AI-assisted decision-making",
            "url": "https://www.researchgate.net/publication/388821876_Confronting_verbalized_uncertainty_Understanding_how_LLM_'s_verbalized_uncertainty_influences_users_in_AI-assisted_decision-making"
          },
          {
            "title": "Designing for Appropriate Reliance: The Roles of AI Uncertainty   Presentation, Initial User Decision, and User Demographics in AI-Assisted   Decision-Making",
            "url": "https://arxiv.org/pdf/2401.05612"
          },
          {
            "title": "Exploring the Impact of Explainable AI and Cognitive Capabilities on Users’ Decisions",
            "url": "https://arxiv.org/html/2505.01192v1"
          }
        ]
      },
      "I've found several highly relevant recent research papers on this topic. Here are the key findings:\n\n## Model Uncertainty vs. User Trust in AI-Assisted Decision Making\n\n**Recent Research Framework (2025):**\n\nResearch shows that the direction of uncertainty (certainty vs. uncertainty) exerts the strongest influence on decision efficiency and trust, with ambiguity mediating trust and accuracy more than information volume.\n\n**Adaptive Gating and Explanation Strategies:**\n\nThe interpretability of AI explanations is context-sensitive—how users perceive and process uncertainty varies by scenario, and current systems fail to capture or adapt to this variability. A proposed Cognitive-Adaptive Framework incorporates user self-reports and contextual variables to identify actionable human feedback signals that can optimize decision performance and inform adaptive model design.\n\n**Uncertainty Expression Approaches:**\n\nResearch shows that medium verbalized uncertainty in LLM expressions consistently leads to higher user trust, satisfaction, and task performance compared to high and low verbalized uncertainty. Additionally, providing counter-explanations adaptively mitigates over-reliance when user trust is high, with 10–23% reduction in over-reliance and 8–20% improvement in final decision accuracy.\n\n**Calibration and Presentation:**\n\nShowing calibrated model uncertainty alone is inadequate; rather, calibrating model uncertainty and presenting it in a frequency format allows users to adjust their reliance accordingly and helps reduce confirmation bias effects.\n\nThese papers from 2024-2026 suggest an emerging shift toward **adaptive, context-sensitive approaches** that gate explanations based on both model uncertainty and user trust levels."
    ],
    "durationSeconds": 7.572498812000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f8c3a5fa-692e-4f26-adb0-bb1e8bb67449",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "b270cb6f-3898-4497-8cb5-1f02427497ff",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Model uncertainty vs. user trust for adaptive AI explanations",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Assistant

_source line 48 · 2026-05-20T04:47:55.055Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the field. Let me synthesize my findings and provide the triage assessment.

Key findings from my research:

1. **Paper 2605.10930 (May 2026)** - Confirmed real. Establishes dual explanations as uniquely effective for reducing overreliance. This is a very recent paper.

2. **Paper 2502.13321 "Adjust for Trust" (IUI 2026)** - Confirmed real. Trust-gated adaptive explanations, 38% reduction in inappropriate reliance. Published at IUI 2026.


3. **Paper 2412.15584 "To Rely or Not to Rely" (CHI 2025)** - Confirmed real. Demonstrates that uncertainty highlighting can actually backfire. I've also verified several other papers in this space: one showing that hybrid approaches combining semantic and probing methods outperform entropy alone, another revealing fairness concerns when uncertainty-gating interventions, and a recent CHI 2025 paper on adaptive LLM-powered analysis for trust assessment.

4. **Paper 2603.29915 "Uncertainty Gating for Cost-Aware XAI"** - Confirmed real. Uses epistemic uncertainty to selectively trigger explanation methods for ML classifiers.

Now looking at the proposal's core claim: comparing model uncertainty versus user trust as competing signals for when to present adaptive explanations in LLM-assisted decision-making. The specific combination of dual explanations, trust-gated triggering, and uncertainty-gated triggering as a backend signal—evaluated head-to-head—doesn't appear to exist in the literature. The novelty is somewhat incremental though, building on established concepts rather than introducing fundamentally new ideas.

The individual components all come from recent papers: dual explanations from one source, trust-gating from another, uncertainty estimation techniques from a third, and the insight about backend versus user-facing uncertainty from yet another. The proposal essentially swaps the trust signal for an uncertainty signal in an existing gating framework and compares them. It's a natural extension once you recognize that displaying uncertainty directly backfires but using it internally could work better, though the contribution feels more like system-level engineering than conceptual innovation.

On significance, the research question matters practically—whether automatic model uncertainty can replace the need for explicit trust signals in deciding when to show explanations.

But the core hypothesis tests non-inferiority, which creates a problem: confirming non-inferiority feels predictable (of course a reasonable automatic signal would match a noisy self-report), while inferiority just confirms trust-gating is better, and superiority would be surprising but isn't the main claim. The most likely positive result is something a reviewer would have expected all along.

There's also a critical control condition—always-on dual explanations—that could undermine the entire contribution. If showing explanations constantly performs just as well as gating them, then all the gating machinery becomes unnecessary overhead, and the paper's main value proposition collapses. The justification would have to rest on H3 showing that gating reduces cognitive load, but if that difference is marginal, the contribution weakens substantially.

The first assumption—that model uncertainty correlates strongly enough with correctness to serve as a useful signal—gets tested in Phase 1 with an AUROC threshold of 0.75, which is a solid empirical check.

But there are two other assumptions worth scrutinizing. One is that model uncertainty alone can determine the optimal explanation strategy without accounting for individual user differences—people process information differently regardless of what the model's confidence is. The proposal doesn't really grapple with this heterogeneity. The other is whether general-knowledge QA is representative enough to generalize findings about gating strategies to other domains.

Looking at the overall picture, this is methodologically rigorous with preregistration, TOST equivalence testing, and mixed-effects modeling, which is genuinely solid. But conceptually, it feels more like an incremental engineering comparison—testing whether a practical alternative works—rather than something fundamentally novel. The core hypothesis has an almost obvious quality to it, and the threat from the always-on condition is real enough that it could easily flip the results.

I'm also noticing the proposal lists CHI, CSCW, and FAccT as target venues, which makes sense since this is fundamentally an HCI study with NLP components rather than an NLP conference contribution. Though my evaluation criteria are supposed to focus on academic quality independent of venue fit, that mismatch is worth acknowledging.

The core issue is that the NLP piece—the uncertainty estimation system—relies on existing techniques without novel methodological contributions. The real novelty lies in the comparative user study design, which is more HCI than NLP. Weighing the strengths against the weaknesses, I see a well-motivated study with clean methodology and practical value, but the conceptual novelty is limited—it's more of a combinatorial approach than a fundamental insight. The non-inferiority framing and the risk that the trivial baseline (always-on uncertainty) could undermine the contribution both temper my confidence in the idea's impact. but not deep. The NLP contribution is purely engineering—applying existing uncertainty methods to a new context. I'd estimate this at around 15-22% for EMNLP, since the core idea is fundamentally an HCI study with NLP as a supporting technology. The NLP-specific novelty is thin, and while the empirical comparison is the main contribution, it has that "I would have guessed this" quality.

Though I should reconsider—EMNLP does accept human evaluation papers and HCI-adjacent work, and the uncertainty estimation does involve NLP techniques. Looking more carefully, the NLP contribution is applying existing uncertainty estimation to a new use case, which isn't novel for NLP itself. The user study is the main contribution but relies on HCI methodology. The research question matters for practical deployment, but the answer probably won't surprise NLP researchers since the core methodology is HCI-based, the NLP components are off-the-shelf, and the findings would be about human behavior rather than language or models.

Setting aside venue fit and focusing purely on idea quality: the novelty is moderate—it's a natural combination of recent work rather than surprising. The significance is moderate too—practically important but with predictable outcomes. The related work coverage is exceptionally thorough. Probability estimate: 20-30%, mid 25%

Actually, let me reconsider. The proposal has some genuine strengths:
1. The backend vs. frontend uncertainty insight is well-motivated
2. The convergence of 5-6 recent papers creating a gap is well-identified
3. The fairness analysis adds genuine value
4. The methodological sophistication (TOST, GLMM, preregistration) is impressive

But ultimately, the core idea is: "replace trust self-reports with model uncertainty as a gating signal for adaptive dual explanations." This is a clean, testable idea, but it's fundamentally:
- Taking method A's gating strategy (trust)
- Replacing it with method B (uncertainty)
- Comparing them

The depth of insight is limited. If it works (non-inferior), it's useful but not surprising. If it doesn't work, it's a negative result about a natural alternative.

I'm settling on 20-28%, mid 24%. The proposal targets CHI/CSCW/FAccT rather than EMNLP, but I'm evaluating it for EMNLP scope regardless. My final assessment: novelty is combinatorial and a natural next step, significance is practically important but the expected outcome isn't surprising, and the related work coverage is exceptional. The main risk is that a simpler always-on alternative might work just as well, and the non-inferiority hypothesis feels like something I would've predicted anyway. Final probability: 18-28%, mid 23%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b270cb6f-3898-4497-8cb5-1f02427497ff",
  "isSidechain": false,
  "requestId": "req_011CbDDMapUQMbcTkpntSAzf",
  "type": "assistant",
  "uuid": "4c4dae11-bdfa-4be9-86a1-a6e0ccb7c2a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XL2jjx7AgaccL5zFiVgCi2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 33324,
      "output_tokens": 5983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1049,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5983,
          "cache_read_input_tokens": 33324,
          "cache_creation_input_tokens": 1049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1049
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

_source line 49 · 2026-05-20T04:49:05.743Z_

Now I have sufficient information to provide my assessment. Let me compile the triage evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Evaluating the False Trust engendered by LLM Explanations](https://arxiv.org/abs/2605.10930) (arXiv, May 2026): 确认存在。核心发现：dual explanations（pro + contra）是唯一真正提升用户区分正确/错误 AI 输出能力的解释类型；其他类型（reasoning traces、post-hoc explanations）仅增加接受率。此论文是本 proposal 的直接动机之一。
- [Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance](https://arxiv.org/abs/2502.13321) (IUI 2026): 确认存在。信任门控自适应解释，当 trust ≥ 8 时切换到 counter-explanations，不当依赖减少 38%。关键局限：需要每次决策后的 trust 自报告 + 准确度反馈。Proposal 的 Condition 3 直接复制此机制。
- [To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance](https://arxiv.org/abs/2412.15584) (CHI 2025): 确认存在。Uncertainty Highlighting 直接向用户展示不确定性信息后反效果——显著降低感知准确性和有用性，增加 algorithm aversion。这是 proposal "后端门控而非前端展示" 设计的关键动机。
- [Entropy Alone is Insufficient for Safe Selective Prediction in LLMs](https://arxiv.org/abs/2603.21172) (arXiv, Mar 2026): 确认存在。Semantic entropy 存在"confidently wrong"模式（尤其 Qwen 模型）；结合 Probability of Correctness probe 可显著改善错误检测。Proposal 的混合不确定性信号直接来自此工作。
- [Unequal Uncertainty: Rethinking Algorithmic Interventions](https://arxiv.org/abs/2508.07872) (arXiv, Aug 2025): 确认存在。首次系统分析 uncertainty-gated 干预的公平性风险——不确定性阈值可能对代表性不足群体产生歧视性影响。Proposal 的 RQ3 fairness analysis 直接受此启发。
- [From Text to Trust](https://arxiv.org/abs/2502.11919) (CHI 2025): 确认存在。动态规划框架通过学习用户行为模型自适应选择 LLM 生成的分析呈现。与本 proposal 的区别：需要先验交互数据、操作于表格特征分析而非 dual explanations、门控信号为预测效用而非不确定性/信任。
- [Uncertainty Gating for Cost-Aware Explainable AI](https://arxiv.org/abs/2603.29915) (arXiv, Mar 2026): 使用 epistemic uncertainty 为 ML 分类器门控解释方法。机制类似但应用领域完全不同（ML 分类器的 XAI，非人类过度依赖）。
- 调研总结: 这个领域处于快速汇聚期——2025-2026 年内多条线独立发展（dual explanations 的有效性、trust-gated 自适应、uncertainty 的公平性风险、混合不确定性估计），但尚无工作将 model uncertainty 和 user trust 作为竞争性门控信号直接比较。Proposal 位于这些线的交汇点。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是 "always-on dual explanation"（始终呈现 pro + contra），这恰好是 proposal 的 Condition 2。如果 always-on dual explanation 在 overreliance reduction 上与 gated 条件表现相当，且认知负荷/满意度差异不显著，则整个门控机制（无论是 trust-based 还是 uncertainty-based）都是不必要的工程开销，论文的核心贡献将被严重削弱。Proposal 确实通过 H3 假设了 gated 条件相比 always-on 有更低认知负荷和更高满意度，但这一假设并非不言自明——如果 dual explanations 的认知负荷本身不高（只是额外 2-3 句反面论点），选择性呈现的优势可能很小。增量价值的成立关键取决于 always-on 是否确实带来显著的认知负荷代价，这在先行文献中并没有充分的证据支撑。

【前提假设检验】:
核心逻辑链中存在以下未经充分验证的假设：
1. **"模型不确定性高 ≈ 模型可能出错 ≈ 用户此时最需要 dual explanation"** — 这假设了 dual explanation 的最佳触发时机与模型错误概率强相关。但用户过度依赖的发生不仅取决于模型是否出错，还取决于用户状态（注意力、先验知识、疲劳程度等）。一个高信任用户在模型正确时也可能形成不健康的过度依赖模式（habitual reliance），而 uncertainty-gating 不会对此触发干预。
2. **"门控触发率可比 ≈ 公平比较"** — Proposal 计划如果两种门控条件的触发率差距超过 15pp 则调整阈值使之匹配。但 trust-gating 和 uncertainty-gating 的触发模式可能在 trial-level 上有完全不同的时间序列特征（trust 随序列动态变化，uncertainty 是静态预计算的），即使总触发率匹配，触发的 trial 可能完全不同，导致比较的内在效度存疑。
3. **"30 个 general-knowledge 问题足以推广到 LLM-assisted decision-making"** — 这一任务域非常狭窄（知识问答），与 proposal 声称的"deployable framework"之间存在巨大推广性鸿沟。

【3 维度打分】:
1. Novelty: 中 — Proposal 正确识别了多条近期研究线的汇聚点，且"model uncertainty 作为后端门控信号而非前端展示"的 framing 确实巧妙（受 Bo et al. CHI 2025 反面证据启发）。但核心贡献本质上是 **组合式创新**：取 2502.13321 的门控框架 + 用 2603.21172 的混合不确定性信号替换 trust 信号 + 做 head-to-head 比较。每一个组件都是直接借用近期工作，组合本身是自然的"next obvious step"。此外，2603.29915（Uncertainty Gating for Cost-Aware XAI）已经在 ML 分类器场景展示了 uncertainty-gated explanation selection 的可行性，进一步削弱了将类似思路应用到 LLM 场景的新颖性。
2. Significance: 中偏弱 — 研究问题（自动门控 vs. 手动门控）有真实的实践意义，但核心假设 H2 是 **non-inferiority test**：最可能的"积极"结果是"uncertainty-gating 不劣于 trust-gating"。这是一个审稿人很可能会说 "I would have guessed this" 的结果——一个合理的自动信号大致匹配一个带噪声的手动自报告信号，并不出人意料。如果结果是显著劣于，论文变成了一篇 negative result paper，发表难度更大。真正有 significance 的发现应该是 uncertainty-gating 在某些维度（如公平性）**显著优于** trust-gating，但这不是主假设。此外，任务域极其狭窄（30 个 general-knowledge QA 问题），可推广性有限。
3. Related Work: 强 — Related work 覆盖极为全面，近乎穷尽了 2024-2026 年间所有相关工作。差异化定位清晰——对每篇近期工作都明确说明了与本 proposal 的区别（门控信号不同、干预类型不同、是否需要先验交互等）。引用的关键论文经搜索全部确认真实存在，描述准确。引入公平性分析（2508.07872）和混合不确定性信号（2603.21172）作为方法论支撑也很到位。这是 proposal 最强的维度。

【概率估计】: [15% - 25%] 中位 20%

【估计理由】:
Related Work 维度强，说明作者对领域有深刻理解，proposal 的形式完善度也很高。但 Novelty 和 Significance 共同限制了上界：
- Novelty 受限于组合式创新——各组件均来自 2025-2026 年近期工作的直接借用，组合本身是 natural next step 而非 conceptual leap。
- Significance 受限于核心假设 H2 的 non-inferiority 性质——最可能的积极结果缺乏 surprise value。审稿人读到"自动不确定性信号大致等效于手动信任自报告"时，大概率反应是 "makes sense, but so what?"
- Trivial alternative 威胁实质性地存在（always-on 可能就够好了），且 proposal 对此的防御（H3: gating 降低认知负荷）缺乏先行证据支撑。
- 任务域（30 个 general-knowledge QA）过于狭窄，与 "deployable framework" 的声称之间存在显著落差。

Novelty 和 Significance 共同将上界限制在 ~25%。形式完善度和 Related Work 的扎实使下界不会太低（~15%），但无法补偿 idea 内核的 surprise value 不足。

【主要风险】:
1. **Trivial alternative 威胁**: Always-on dual explanation（Condition 2）如果在 overreliance reduction + 认知负荷的综合表现上与 gated 条件无显著差异，整个门控机制的必要性将被否定，论文核心贡献消失。
2. **"I would have guessed this" 问题**: Non-inferiority 作为主假设，审稿人会质疑 "the bar is too low"——确认一个合理替代方案"不比原方案差太多"缺乏足够的学术 surprise，难以构成 top venue 水准的核心贡献。
```

Sources:
- [Evaluating the False Trust engendered by LLM Explanations](https://arxiv.org/abs/2605.10930)
- [Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance](https://arxiv.org/abs/2502.13321)
- [To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models](https://arxiv.org/abs/2412.15584)
- [Entropy Alone is Insufficient for Safe Selective Prediction in LLMs](https://arxiv.org/abs/2603.21172)
- [Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI](https://arxiv.org/abs/2508.07872)
- [From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis](https://arxiv.org/abs/2502.11919)
- [Uncertainty Gating for Cost-Aware Explainable AI](https://arxiv.org/abs/2603.29915)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c4dae11-bdfa-4be9-86a1-a6e0ccb7c2a8",
  "isSidechain": false,
  "requestId": "req_011CbDDMapUQMbcTkpntSAzf",
  "type": "assistant",
  "uuid": "7ae63568-35bc-43c9-898d-809fbe7e3519",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XL2jjx7AgaccL5zFiVgCi2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 33324,
      "output_tokens": 5983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1049,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5983,
          "cache_read_input_tokens": 33324,
          "cache_creation_input_tokens": 1049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1049
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "7ae63568-35bc-43c9-898d-809fbe7e3519",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Model uncertainty vs. user trust for adaptive AI explanations",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "7ae63568-35bc-43c9-898d-809fbe7e3519",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Model uncertainty vs. user trust for adaptive AI explanations",
  "sessionId": "9874d159-dfa8-42a7-9a1e-f4b7bfda3ea1"
}
```

---
