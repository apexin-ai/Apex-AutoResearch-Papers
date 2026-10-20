# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Model Uncertainty vs. User Trust 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/f0a97c89-af9e-4a64-bfe0-0b468fdc3f88.jsonl`
- **Structured JSON:** [`6ad35d08826ad0a476a0.json`](../../sessions/6a/6ad35d08826ad0a476a0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:31:09.621Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:31:09.621Z",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Making\n\n## Description\nWe propose the first head-to-head comparison of model uncertainty and user trust as gating signals for adaptive dual explanation presentation in LLM-assisted decision-making. Building on three convergent findings—that dual explanations are the only explanation type genuinely reducing overreliance (2605.10930), that trust-gated counter-explanations cut inappropriate reliance by 38% but require obtrusive self-reports and accuracy feedback (Adjust for Trust, IUI 2026), and that displaying uncertainty directly to users backfires by increasing algorithm aversion (Bo et al., CHI 2025)—we test whether automatic model uncertainty can serve as a practical, first-interaction-ready *backend* gating signal that selects explanation type without burdening users. The system uses a validated hybrid uncertainty estimator (semantic entropy + Probability of Correctness probe over Qwen3-30B-A3B's shared residual stream representations, addressing both the 'confidently wrong' regime identified by 2603.21172 and MoE-specific probing considerations) to selectively trigger dual explanations when model error is likely. The uncertainty threshold is set via Youden's J-optimal cutpoint with cross-validated calibration, and triggering rates are verified against the trust-gated condition in a pilot study. A preregistered between-subjects study (N≈560, Prolific) compares four conditions across 30 general-knowledge questions: no explanation, always-on dual explanation, trust-gated dual explanation (replicating the Adjust for Trust mechanism with trust ≥ 8 threshold), and uncertainty-gated dual explanation. We measure overreliance reduction, discrimination accuracy, appropriate reliance ratio, cognitive load, and satisfaction. The central hypothesis (H2) tests non-inferiority of uncertainty-gating via TOST with a pre-registered equivalence margin of Cohen's d = 0.35 (≈7 percentage points on overreliance rate), justified by cost-benefit SESOI reasoning: below this threshold, uncertainty-gating's deployment advantages (no surveys, no feedback dependency, first-interaction readiness) outweigh any effectiveness loss. Power analysis confirms N=140/group provides 80% power for TOST at d = 0.35 (Lakens, 2017). Analysis uses GLMMs with crossed random effects for participants and items (Baayen et al., 2008; Westfall et al., 2014) to account for question-specific variance. Unlike prior adaptive approaches that require learned user models from prior interactions (Li et al., CHI 2025), our uncertainty-gated condition requires no user state measurement and works from the first interaction. Uniquely, we include a fairness analysis—motivated by 'Unequal Uncertainty' (2508.07872)—examining whether uncertainty-gated interventions trigger disproportionately across demographic groups. We explicitly acknowledge the ecological validity limitation that accuracy feedback (provided for comparability) is rarely available in deployment, and argue—supported by Okamura & Yamada (CHI 2024)—that uncertainty-gating's relative advantage is likely *larger* in practice because trust calibration degrades without feedback while uncertainty-gating is feedback-independent. This work bridges uncertainty quantification in NLP with adaptive explanation design in HCI, offering both a principled comparison of gating strategies and a deployable framework that requires no user state measurement.\n\n## Core Problem\nWhich gating signal—model uncertainty (automatic, available from first interaction) or user trust (self-reported, requiring repeated measurement)—better governs when to present dual explanations for reducing LLM overreliance, and does uncertainty-based gating introduce demographic fairness risks through differential triggering?\n\n## Opportunity\nTwo recent lines of work create a convergent opportunity. First, the 'false trust' study (2605.10930, May 2026) establishes that dual explanations (pro + contra arguments) are the *only* explanation type that genuinely improves users' ability to distinguish correct from incorrect LLM outputs—all other types merely increase acceptance. Second, 'Adjust for Trust' (2502.13321, IUI 2026) demonstrates that adaptively triggering counter-explanations based on user trust reduces inappropriate reliance by up to 38%. However, their approach requires obtrusive trust self-reports after every decision and real-time accuracy feedback—conditions rarely met in deployment. Their own analysis reveals that predicting trust from behavioral signals alone achieves F1 ≤ 0.5, making passive trust detection impractical, and they explicitly acknowledge that 'a key assumption of our setup does not hold in most real-world settings: that both parties have access to real-time feedback about decision accuracy.' Model uncertainty offers a complementary gating signal: it is computed automatically, requires no user input, works from the first interaction, and—critically—does not depend on accuracy feedback for calibration. Yet no work has empirically compared these two gating strategies. Meanwhile, 'The Persuasion Paradox' (2604.03237) shows that explanation effectiveness is strongly task-dependent—explanations help for language-based reasoning (72.5% accuracy vs. 48.5% baseline on LSAT) but hurt for visual reasoning—suggesting that uncertainty-gated explanation switching is most valuable precisely for the knowledge QA domain where explanations are effective. Critically, 'To Rely or Not to Rely?' (2412.15584, CHI 2025) finds that *displaying* uncertainty to users (via token-level probability highlighting) actually backfires—increasing algorithm aversion without improving appropriate reliance. This counter-evidence is important because it shows that uncertainty information is counterproductive when presented directly to users, but it does not indict using uncertainty as a *backend gating signal* to select which explanation type to present. Indeed, it strengthens the case for our approach: rather than burdening users with uncertainty visualization, we use uncertainty behind the scenes to select the more effective dual explanation format when model error is likely. The missing piece remains a head-to-head comparison that determines when model uncertainty outperforms, matches, or falls short of trust-based gating, while also measuring the fairness implications that 'Unequal Uncertainty' (2508.07872) warns about.\n\n## Landscape\nThe false trust paper (2605.10930, May 2026) establishes dual explanations as uniquely effective but tested them uniformly. 'Adjust for Trust' (2502.13321, IUI 2026) is the closest prior work on gating strategy: it gates between supporting and counter-explanations based on self-reported user trust (11-point scale, 0-10), achieving 38% reduction in inappropriate reliance and 20% accuracy improvement across science QA and medical diagnosis with 30 trials per participant. Critically, their trust measurement requires accuracy feedback after each trial and explicit trust surveys—conditions that limit deployment scalability. Their trust threshold (≥8 on 0-10 scale for counter-explanations) was set by visual inspection of reliance curves, not formal optimization. Their attempt to predict trust from interaction features yielded F1 ≤ 0.5. 'From Text to Trust' (Li et al., 2502.11919, CHI 2025) is the closest prior work on adaptive explanation selection: they use a dynamic programming framework with a learned human behavior model to selectively decide which LLM-generated feature analyses to present for tabular AI predictions (income, recidivism; N=447 and N=397, 15 trials per participant), significantly improving appropriate reliance versus always-on and control conditions. However, their approach differs from ours in three key respects: (1) it requires prior interaction data to train the behavior model (cold-start problem), (2) it operates on tabular feature-level analyses rather than natural-language dual explanations, and (3) their gating is based on predicted utility of each analysis rather than on model uncertainty or user trust as explicit signals. Our work complements theirs by comparing two deployment-practical gating signals (model uncertainty and self-reported trust) for a different intervention type (dual pro/contra explanations) in knowledge QA. 'To Rely or Not to Rely?' (Bo et al., 2412.15584, CHI 2025) benchmarks three reliance interventions on N=400 participants across LSAT and image estimation (only 4 trials per participant): Reliance Disclaimer (static warning text), Uncertainty Highlighting (red/pink token-level probability visualization), and Implicit Answer (removing explicit answer statements). Their central finding is sobering: while interventions reduce over-reliance, they generally fail to improve *appropriate* reliance—only Reliance Disclaimer improves the Appropriate Reliance Ratio, and only on LSAT (ARR=1.62 vs. 1.17 control, p=.04). Uncertainty Highlighting specifically backfired, significantly reducing perceived accuracy and helpfulness and increasing algorithm aversion rather than calibrating reliance. This is critical counter-evidence that our approach must address. The key distinction is mechanistic: Bo et al.'s Uncertainty Highlighting *displays* uncertainty information to users, imposing cognitive burden and triggering aversion. Our uncertainty-gated approach uses uncertainty as a *backend signal* to select explanation type—users never see uncertainty scores; they see adaptively selected explanation content. Furthermore, their interventions (disclaimer, highlighting, implicit answer) are simpler cognitive forcing mechanisms, whereas our dual explanation (pro + contra arguments) is the only format shown to genuinely improve discrimination ability (2605.10930). 'Selectively Providing Reliance Calibration Cues' (2302.09995) predicts human reliance behavior to selectively present calibration cues, but uses a learned user model rather than model uncertainty and does not switch explanation types. 'The Persuasion Paradox' (2604.03237) finds that uncertainty-based selective automation outperforms explanations for visual reasoning, but their own results show LLM explanations dramatically improve performance on language-based tasks (LSAT: 72.5% vs. 48.5%), supporting explanation-type switching for knowledge QA. 'Contrastive Explanations That Anticipate Misconceptions' (2410.04253, CHI 2025) generates explanations addressing the gap between AI and user reasoning (N=628, improves decision skills), but applies them uniformly without selective gating. 'Don't Just Translate, Agitate' (2504.12424) proposes LLMs as devil's advocates for XAI but is a position paper without empirical evaluation. 'Why Not Both?' (Frontiers 2025) shows explanations and uncertainty estimates serve complementary roles—uncertainty improves accuracy while explanations improve understanding—supporting the value of combining both signals. 'Unequal Uncertainty' (2508.07872) provides the first socio-technical and legal analysis of uncertainty-gated interventions, showing they can disproportionately affect underrepresented groups through differential triggering rates, creating fairness and legal risks under UK Equality Act 2010. 'Entropy Alone is Insufficient' (2603.21172) demonstrates that semantic entropy has a 'confidently wrong regime' and combining it with a Probability of Correctness probe substantially improves reliability. 'Revisiting Uncertainty Estimation' (2505.23854) shows LLMs have better calibration on reasoning tasks than knowledge-heavy ones across 80 models, and that good calibration does not guarantee effective error ranking—necessitating explicit validation for our QA domain. 'LLMs Should Express Uncertainty Explicitly' (2604.05306) proposes verbalized confidence and reasoning-time uncertainty markers, achieving improved calibration. 'Dissenting Explanations' (AAAI 2024) leverages model multiplicity for disagreeing explanations but applies them uniformly. Partial explanations (de Jong et al., PACM HCI 2025) reduce overreliance through cognitive forcing but do not modulate explanation type. 'Framework for Machine Evaluation of Reasoning Completeness' (Patil, 2510.21884) introduces the RACE framework evaluating alignment between LLM explanations and interpretable feature importance, finding a 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues—relevant context for understanding how explanation quality may covary with model correctness. Multi-AI panel work (2603.22152) finds single dissent reduces conformity while broad disagreement confuses. Uncertainty Gating for Cost-Aware XAI (2603.29915) uses epistemic uncertainty to gate explanation methods for ML classifiers, not human overreliance; notably, they use percentile-based thresholds calibrated per dataset across ν ∈ {0.1, 0.3, 0.5, 0.7, 0.9}. No existing work directly compares model uncertainty and user trust as competing gating signals for adaptive explanation presentation in LLM-assisted decision-making.\n\n## Approach\nThe study proceeds in two phases. **Phase 1: Uncertainty Signal Validation.** Before any human-subjects work, we validate the gating signal on our specific task. Using Qwen3-30B-A3B—a Mixture-of-Experts model with 30.5B total parameters but only 3.3B activated per token (128 experts/layer, 8 selected per token)—we generate answers to 200 candidate general-knowledge questions and compute semantic entropy over 10 sampled completions per question. Semantic entropy operates on output-level semantics (clustering sampled completions by meaning), so it is unaffected by MoE routing variability. Following 'Entropy Alone is Insufficient' (2603.21172), we also train a lightweight Probability of Correctness (PC) probe on Qwen3-30B-A3B's hidden-state activations using a held-out set. For the PC probe specifically, we address MoE-specific considerations: we probe the shared residual stream representations (post-attention, pre-MoE routing) rather than post-expert states, avoiding the routing variability where different tokens activate different expert subsets. We validate probe stability by measuring variance across multiple forward passes on identical inputs, since MoE routing is deterministic for greedy decoding but may vary under sampling. Alternatively, we can adopt the Semantic Entropy Probes approach (Kossen et al., 2024), which approximates semantic entropy from single-generation hidden states, eliminating the need for multiple samples entirely. We combine semantic entropy and PC probe scores via logistic regression to produce a hybrid uncertainty signal. We require AUROC ≥ 0.75 for distinguishing correct from incorrect answers before proceeding; if this threshold is not met, we evaluate alternative models (Llama-4-Scout-17B, Mixtral-8x22B) or uncertainty methods (semantic energy, verbalized confidence per 2604.05306). **Threshold calibration:** The uncertainty gating threshold is set at the Youden's J optimal cutpoint (maximizing sensitivity + specificity − 1) on Phase 1 validation data, with bootstrap 95% CI for the cutpoint to quantify threshold uncertainty. Cross-validation (leave-20%-out) prevents overfitting on the 200-question set. From validated questions, we select 30 for the main study (15 where the model is correct, 15 where it is incorrect, balanced across uncertainty levels and topic domains). The increase from 20 to 30 items matches the 'Adjust for Trust' protocol (30 trials per participant) and provides sufficient levels for stable item-level random effects estimation in the GLMM analysis (Westfall, Kenny, & Judd, 2014, show that with ≤8 items, maximal attainable power is <0.5 regardless of participant N; 30 items is well above this threshold and above the ≥5-level minimum recommended by Gelman & Hill, 2006). **Phase 2: Comparative User Study.** A preregistered between-subjects study (N≈560, 140 per condition) on Prolific with four conditions: (1) **No explanation**—LLM answer only; (2) **Always-on dual explanation**—every answer includes structured pro and contra arguments (replicating the effective condition from 2605.10930); (3) **Trust-gated dual explanation**—participants report trust on an 11-point scale (0-10) after each of the 30 trials; when trust exceeds 8 (adopting the 'Adjust for Trust' threshold, which was empirically calibrated against reliance behavior), the next trial presents dual explanation, otherwise single explanation; (4) **Uncertainty-gated dual explanation**—when the hybrid uncertainty signal exceeds the Youden's J-optimal threshold from Phase 1, dual explanation is presented; otherwise single explanation. **Triggering rate calibration:** In the pilot study (N=60, 15 per condition), we compare empirical triggering rates between Conditions 3 and 4. If rates differ by >15 percentage points, we adjust the uncertainty threshold to the percentile that approximately matches the trust-gated triggering rate, reporting both Youden-optimal and rate-matched thresholds as sensitivity analyses. This ensures condition comparability while preserving transparency about any threshold adjustment. Crucially, unlike the Uncertainty Highlighting intervention in Bo et al. (2412.15584) which *displays* token-level probability information to users (and backfired by increasing algorithm aversion), our uncertainty-gated condition uses uncertainty purely as a backend signal—participants see only the selected explanation format, never the uncertainty estimate itself. This design choice is directly informed by Bo et al.'s finding that user-facing uncertainty visualization is counterproductive. All conditions receive accuracy feedback after each trial (following 'Adjust for Trust' protocol, ensuring comparability). Dual explanations are generated via Claude API with structured prompting (pro: 3-4 sentences supporting the answer; contra: 2-3 sentences presenting the strongest counter-argument and alternative answer), with human review for quality. **Measures**: Primary—overreliance rate (accepting incorrect AI answers), discrimination accuracy (AUROC of accept/reject decisions vs. correctness), appropriate reliance (composite of over- and under-reliance, following the Appropriate Reliance Ratio from Bo et al., 2412.15584). Secondary—cognitive load (NASA-TLX), task completion time, subjective satisfaction (7-point Likert), perceived AI competence. **Analysis plan**: Generalized linear mixed model (GLMM) with a logit link for trial-level accept/reject decisions, including crossed random intercepts for participants and items (questions), and random slopes for condition by item to capture differential treatment effects across questions (following Baayen, Davidson, & Bates, 2008; Westfall, Kenny, & Judd, 2014). Fixed effects: condition (4 levels), item correctness (correct/incorrect), and their interaction. Participant-level covariates: age, education, domain knowledge (pre-test). This approach accounts for item-level variance (question difficulty, topic familiarity) that would otherwise inflate Type I error if items were treated as fixed (Judd, Westfall, & Kenny, 2012). **Equivalence testing specification (H2)**: We use Two One-Sided Tests (TOST; Lakens, 2017) with a pre-registered equivalence margin of Cohen's d = 0.35, justified by cost-benefit SESOI reasoning (Lakens, Scheel, & Isager, 2018): this represents the maximum effectiveness difference at which uncertainty-gating's deployment advantages—no user surveys, no accuracy feedback dependency, first-interaction readiness—still outweigh the performance loss versus trust-gating. In raw terms, d = 0.35 corresponds to approximately 7 percentage points on overreliance rate (assuming participant-level SD ≈ 0.20), meaning we accept non-inferiority if uncertainty-gating's overreliance rate is no more than 7pp higher than trust-gating's. As sensitivity analyses, we also report equivalence tests at d = 0.25 (stricter) and d = 0.50 (more lenient) to demonstrate robustness to margin specification. **Power analysis**: For H2 (TOST non-inferiority, d = 0.35 bounds, α = 0.05): N = 140 per group provides ~80% power (computed via TOSTER::power_t_TOST; consistent with Lakens, 2017, Table 1: d = 0.30 requires N = 191/group, d = 0.40 requires N = 108/group, interpolating to ~140 for d = 0.35). For H1 and H3 (superiority tests, expected d ≈ 0.50 based on 'Adjust for Trust' effect sizes): N = 140 per group provides >95% power. Total sample: N = 560 (140 per condition). **Fairness analysis** (RQ3, addressing 'Unequal Uncertainty'): We collect demographic data (gender, race/ethnicity, education, English proficiency) and analyze whether uncertainty-gated dual explanations trigger at different rates for questions where demographic knowledge gaps exist, whether differential triggering correlates with demographics, and whether any differential triggering translates to differential overreliance reduction. **Key hypotheses**: H1—Conditions 3 and 4 both reduce overreliance compared to Condition 1; H2—Condition 4 (uncertainty-gated) achieves non-inferior overreliance reduction compared to Condition 3 (trust-gated), tested via TOST with equivalence margin d = 0.35; H3—Condition 4 produces lower cognitive load and higher satisfaction than Condition 2 (always-on dual); H4—Condition 4 incurs no measurement burden (no trust surveys), making it more practical; H5—Uncertainty-gated triggering rates do not differ significantly across demographic groups (fairness hypothesis, tested as a secondary analysis with appropriate corrections for multiple comparisons). **Ecological validity limitation**: Accuracy feedback after every trial, while necessary for the trust-gated condition (Condition 3) and provided to all conditions for comparability, is rarely available in real-world deployment. The 'Adjust for Trust' authors explicitly acknowledge this limitation. Okamura and Yamada (CHI 2024, arXiv 2111.08222) demonstrate that outcome feedback substantially improves trust calibration, while interpretability alone does not—implying that trust-gating's effectiveness degrades in feedback-free settings. Critically, uncertainty-gating is feedback-independent: the model computes uncertainty from its own outputs regardless of whether users receive outcome information. This means our study likely *underestimates* uncertainty-gating's relative advantage over trust-gating in deployment, because the experimental feedback supports trust calibration that would be absent in practice. We discuss this asymmetry as a key deployment implication: in feedback-scarce environments (the norm for most LLM-assisted decisions), uncertainty-gating may be the *only* viable adaptive strategy, as trust-gating without feedback relies on potentially miscalibrated self-reports that the 'Adjust for Trust' authors themselves note may reflect 'potentially incorrect perceptions of expertise.' A follow-up study varying feedback availability (present vs. absent) across both gating conditions would directly quantify this interaction and is identified as priority future work.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '300-400 (Qwen3-30B-A3B hosting for Phase 1 validation: ~2K questions × 10 samples + PC probe training on shared residual stream representations; Phase 2: ~10K inference calls × 10 samples for pilot + main study on A100-80GB; note Qwen3-30B-A3B activates only 3.3B parameters per token, reducing per-inference cost vs. dense 30B models)', 'timeline': '5-7 months (Month 1: system build + Phase 1 uncertainty validation + threshold calibration; Month 2: IRB submission + pilot design; Month 3: IRB approval + pilot N=60 + triggering rate calibration; Month 4: pilot analysis + main study refinement; Month 5: main study N≈560; Month 6-7: analysis + writing; aggressive 4.5-month variant possible if IRB uses expedited review for minimal-risk online study)', 'estimated_gpu_cost': '$700-1000 (A100 at ~$3/hr; MoE efficiency reduces per-inference cost)'}, 'human_in_loop': {'gpu_hours': '200-300 (Claude API generates candidate explanations and counter-arguments; GPU only for Qwen3-30B-A3B uncertainty estimation and PC probe training)', 'timeline': '4.5-6 months (Claude accelerates explanation generation, stimulus quality control, statistical modeling, and fairness analysis code)', 'claude_api_cost': '$600-900 (explanation generation for 200 candidate + 30 final questions × 4 conditions × multiple pilot rounds, plus analysis assistance)', 'estimated_gpu_cost': '$500-750'}, 'auto_research': {'gpu_hours': '200-300', 'timeline': '4.5-6 months minimum', 'claude_api_cost': '$900-1400 (automated stimulus optimization, power analysis simulation, equivalence testing code, fairness analysis, draft writing)', 'estimated_gpu_cost': '$500-750', 'speed_bottleneck': 'IRB approval (4-8 weeks, expedited review possible for minimal-risk online survey) and Prolific data collection (~2-3 weeks for N=560) are non-automatable; participant compensation ~$6,200-7,000 (560 participants × ~40 min average session × $12/hr Prolific recommended minimum + 33.3% Prolific academic service fee + ~10% buffer for rejections/replacements; Condition 3 sessions may extend to ~45 min due to trust surveys after each of 30 trials); trust measurement in Condition 3 requires interactive protocol that may extend session duration'}}\n\n## Inspired By\nThe 'Adjust for Trust' finding that trust-gated counter-explanations reduce overreliance by 38%—combined with their own limitation that trust cannot be reliably predicted from behavior (F1 ≤ 0.5) and their acknowledgment that accuracy feedback is unavailable in most deployment settings—directly motivates testing model uncertainty as a practical alternative gating signal. The convergence of (1) dual explanations as uniquely effective (2605.10930), (2) adaptive gating as effective but trust-measurement-limited (2502.13321), (3) adaptive explanation selection as effective but requiring learned user models (2502.11919), (4) 'Entropy Alone is Insufficient' showing hybrid uncertainty signals improve reliability (2603.21172), (5) uncertainty *display* backfiring while the underlying signal remains informative (2412.15584), and (6) 'Unequal Uncertainty' raising fairness concerns about uncertainty-gated interventions (2508.07872) creates a well-motivated research question that no single prior paper addresses.\n\n## Target Venues\n- CHI 2027 (paper deadline Sep 10, 2026 — aggressive but achievable with 4.5-month timeline if Phase 1 validates quickly and IRB uses expedited review; flagship HCI venue, strong fit for adaptive AI-assisted decision-making comparison study; revise-and-resubmit process available)\n- CSCW 2027 (rolling submission from Jan 2027 — comfortable primary target if CHI 2027 timeline proves too tight; strongest fit for adaptive AI-assisted decision-making with fairness analysis; 3-4 month review cycle)\n- FAccT 2027 (estimated deadline ~Jan 2027 — fairness analysis of uncertainty-gated interventions is strong fit; equity framing as secondary contribution)\n- CHI 2028 (paper deadline ~Sep 2027 — safe fallback if earlier venues require major revision)\n\n## Key References\n- Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (IUI 2026, arXiv 2502.13321) — *primary point of differentiation*: trust-gated adaptive counter-explanations, 38% reduction in inappropriate reliance, 30 trials/participant, trust ≥ 8 threshold; our Condition 3 replicates their mechanism\n- Evaluating the False Trust engendered by LLM Explanations (arXiv 2605.10930, May 2026) — establishes dual explanations as uniquely effective; motivates explanation type selection\n- From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis (Li et al., CHI 2025, arXiv 2502.11919) — dynamic programming framework with learned human behavior model for selectively presenting LLM-generated feature analyses (N=447, N=397, 15 trials/participant); improves appropriate reliance on tabular AI tasks; differs from our work in requiring prior interaction data, operating on feature-level analyses rather than dual explanations, and using predicted utility rather than model uncertainty or trust as gating signal\n- To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models (Bo et al., CHI 2025, arXiv 2412.15584) — benchmarks three reliance interventions (Reliance Disclaimer, Uncertainty Highlighting, Implicit Answer) on N=400 (only 4 trials/participant); finds interventions generally fail to improve appropriate reliance; Uncertainty Highlighting specifically backfires by increasing algorithm aversion; *critical counter-evidence* that motivates our backend-gating design: we use uncertainty to select explanation type, never displaying it to users; Appropriate Reliance Ratio adopted as primary metric\n- The Persuasion Paradox: When LLM Explanations Fail to Improve Human-AI Team Performance (arXiv 2604.03237) — shows explanation effectiveness is task-dependent; supports explanation switching for language-based QA while selective automation is better for visual tasks\n- Selectively Providing Reliance Calibration Cues With Reliance Prediction (arXiv 2302.09995) — selective intervention via predicted reliance behavior; differs in gating signal (user model vs. model uncertainty) and intervention type (calibration cues vs. explanation switching)\n- Contrastive Explanations That Anticipate Human Misconceptions (CHI 2025, arXiv 2410.04253) — human-centered contrastive explanations improve decision skills (N=628); applied uniformly, not selectively gated\n- Don't Just Translate, Agitate: Using LLMs as Devil's Advocates for AI Explanations (arXiv 2504.12424) — position paper proposing LLMs as constructive agitators; no empirical evaluation\n- Why Not Both? Complementing Explanations with Uncertainty (Frontiers in Computer Science 2025) — shows explanations and uncertainty serve complementary roles; supports combining both signals\n- Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI (arXiv 2508.07872) — fairness risks of uncertainty-gated interventions; directly motivates our RQ3 fairness analysis\n- Entropy Alone is Insufficient for Safe Selective Prediction in LLMs (arXiv 2603.21172) — demonstrates 'confidently wrong' regime of semantic entropy; motivates our hybrid SE + PC probe approach\n- Revisiting Uncertainty Estimation and Calibration of Large Language Models (arXiv 2505.23854) — shows calibration varies across 80 models, worse on knowledge vs. reasoning tasks; motivates Phase 1 validation\n- LLMs Should Express Uncertainty Explicitly (arXiv 2604.05306) — verbalized confidence and reasoning-time uncertainty markers improve calibration; alternative uncertainty elicitation if SE fails validation\n- To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance (CSCW 2021) — establishes effectiveness-usability tradeoff in CFF interventions\n- An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, January 2026) — Assumption CFF reduces overreliance but decreases satisfaction\n- Cognitive Forcing for Better Decision-Making: Reducing Overreliance Through Partial Explanations (PACM HCI 2025) — partial explanations as cognitive forcing; no uncertainty-based modulation\n- Dissenting Explanations: Leveraging Disagreement to Reduce Model Overreliance (AAAI 2024) — model multiplicity for disagreeing explanations; applied uniformly without selective gating\n- More Isn't Always Better: Balancing Decision Accuracy and Conformity Pressures in Multi-AI Advice (arXiv 2603.22152) — single dissent reduces conformity; supports targeted rather than blanket counter-argumentation\n- Uncertainty Gating for Cost-Aware Explainable AI (arXiv 2603.29915) — uses epistemic uncertainty to gate explanation methods for ML classifiers with percentile-based thresholds; analogous mechanism but entirely different application domain\n- Framework for Machine Evaluation of Reasoning Completeness in Large Language Models for Classification Tasks (Patil, arXiv 2510.21884) — RACE framework evaluating explanation-feature alignment; finds 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues; relevant context for understanding explanation quality covariation with model correctness\n- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (Kossen et al., arXiv 2406.15927) — approximates semantic entropy from single-generation hidden states, reducing computational overhead to near zero; potential efficiency improvement for Phase 1 uncertainty estimation\n- Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (Lakens, 2017, Social Psychological and Personality Science) — TOST procedure and power analysis tables; our equivalence margin and power calculations follow this framework\n- Equivalence Testing for Psychological Research: A Tutorial (Lakens, Scheel, & Isager, 2018, AMPPS) — SESOI justification approaches including cost-benefit analysis; grounds our d = 0.35 margin choice\n- Statistical Power and Optimal Design in Experiments in Which Samples of Participants Respond to Samples of Stimuli (Westfall, Kenny, & Judd, 2014, JEP:General) — power analysis for crossed random effects designs; shows ≤8 items cap maximal power at <0.5; motivates our 30-item stimulus set\n- Mixed-Effects Modeling with Crossed Random Effects for Subjects and Items (Baayen, Davidson, & Bates, 2008, J Memory & Language) — methodological foundation for our GLMM analysis plan with crossed random effects for participants and items\n- Adaptive Trust Calibration for Human-AI Collaboration (Okamura & Yamada, CHI 2024, arXiv 2111.08222) — directly compares feedback vs. no-feedback conditions; shows outcome feedback substantially improves trust calibration while interpretability alone does not; grounds our ecological validity discussion\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:31:09.627Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:31:09.627Z",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-20T03:31:09.650Z_

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
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "451f4513-4b23-4945-84a9-d0dda6282c3e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:31:09.644Z_

```json
{
  "parentUuid": "451f4513-4b23-4945-84a9-d0dda6282c3e",
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
  "uuid": "2490e10a-730a-4683-85fe-13d9fa675ded",
  "timestamp": "2026-05-20T03:31:09.644Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:31:09.644Z_

```json
{
  "parentUuid": "2490e10a-730a-4683-85fe-13d9fa675ded",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ea27864e-99cc-44d4-95d4-db217fcddb53",
  "timestamp": "2026-05-20T03:31:09.644Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
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
  "leafUuid": "ea27864e-99cc-44d4-95d4-db217fcddb53",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare uncertainty vs. trust gating for adaptive LLM explanations",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:31:25.121Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed research proposal that I need to evaluate as the "入口评审 agent." Let me first understand the core idea, then conduct thorough web searches to assess novelty, significance, and related work before providing my assessment.

The proposal is about comparing two gating signals (model uncertainty vs. user trust) for adaptively presenting dual explanations in LLM-assisted decision-making. The core claim is that model uncertainty can serve as a practical backend gating signal that's as effective as trust-based gating but without requiring user self-reports or accuracy feedback.

Let me search for the key papers and the current state of this field before making any judgments.


I notice there's a mismatch between the stated target venue (CoRL 2026) and what the proposal actually describes—this is clearly an HCI/AI-assisted decision-making paper that would fit venues like CHI, CSCW, or FAccT, not a robotics conference. That's worth flagging, but I should focus my evaluation on the research idea itself rather than the venue confusion.

Let me start by searching for relevant work in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea27864e-99cc-44d4-95d4-db217fcddb53",
  "isSidechain": false,
  "requestId": "req_011CbD7bNaxVG9JpLmGxK2su",
  "type": "assistant",
  "uuid": "1df761c7-f631-4df7-952a-bc407cb16b18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ka3SsRktWzvK9oTQxtZc3F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9663,
      "cache_read_input_tokens": 13985,
      "output_tokens": 465,
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
          "output_tokens": 465,
          "cache_read_input_tokens": 13985,
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

### Assistant

_source line 9 · 2026-05-20T03:31:25.251Z_

I need to conduct thorough literature research before evaluating this proposal. Let me first load the WebSearch tool and then search for the key related works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1df761c7-f631-4df7-952a-bc407cb16b18",
  "isSidechain": false,
  "requestId": "req_011CbD7bNaxVG9JpLmGxK2su",
  "type": "assistant",
  "uuid": "f7e24e6a-a08f-422a-90d8-0f416552661c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ka3SsRktWzvK9oTQxtZc3F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9663,
      "cache_read_input_tokens": 13985,
      "output_tokens": 465,
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
          "output_tokens": 465,
          "cache_read_input_tokens": 13985,
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

_source line 10 · 2026-05-20T03:31:25.629Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RzgZjQhugoP4hrGRS3nBfn`</summary>

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
  "parentUuid": "f7e24e6a-a08f-422a-90d8-0f416552661c",
  "isSidechain": false,
  "requestId": "req_011CbD7bNaxVG9JpLmGxK2su",
  "type": "assistant",
  "uuid": "0b102734-b4f7-4c13-baba-5300db676203",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ka3SsRktWzvK9oTQxtZc3F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9663,
      "cache_read_input_tokens": 13985,
      "output_tokens": 465,
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
          "output_tokens": 465,
          "cache_read_input_tokens": 13985,
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

_source line 11 · 2026-05-20T03:31:25.637Z_

<details><summary>↩ Tool result · `toolu_01RzgZjQhugoP4hrGRS3nBfn`</summary>

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
  "parentUuid": "0b102734-b4f7-4c13-baba-5300db676203",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "73256e40-b0ca-4f2d-9f94-592d5f5d07c7",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "0b102734-b4f7-4c13-baba-5300db676203",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T03:31:28.547Z_

Now let me conduct the necessary literature searches. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73256e40-b0ca-4f2d-9f94-592d5f5d07c7",
  "isSidechain": false,
  "requestId": "req_011CbD7cYq8tzAWfK8FqP2r6",
  "type": "assistant",
  "uuid": "25a4c8a1-dbb9-4769-84e3-457ff36c5d98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H1LqPwjgtaPp1MaJspCND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 992,
      "cache_read_input_tokens": 23648,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 23648,
          "cache_creation_input_tokens": 992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 992
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

_source line 13 · 2026-05-20T03:31:29.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XZJwt5QUymYNyfWk6ssT3U`</summary>

```json
{
  "query": "adaptive explanation gating LLM overreliance dual explanation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25a4c8a1-dbb9-4769-84e3-457ff36c5d98",
  "isSidechain": false,
  "requestId": "req_011CbD7cYq8tzAWfK8FqP2r6",
  "type": "assistant",
  "uuid": "7bd70642-8b3e-4b9d-b700-92c146a77ede",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H1LqPwjgtaPp1MaJspCND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 992,
      "cache_read_input_tokens": 23648,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 23648,
          "cache_creation_input_tokens": 992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 992
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

_source line 14 · 2026-05-20T03:31:36.567Z_

<details><summary>↩ Tool result · `toolu_01XZJwt5QUymYNyfWk6ssT3U`</summary>

```text
Web search results for query: "adaptive explanation gating LLM overreliance dual explanation 2025 2026"

Links: [{"title":"LLM09: Overreliance - OWASP Gen AI Security Project","url":"https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/"},{"title":"LLM-Guided Gating Mechanism","url":"https://www.emergentmind.com/topics/llm-guided-gating-mechanism"},{"title":"Efficient LLM Reasoning via Variational Posterior Guidance with Efficiency Awareness","url":"https://arxiv.org/html/2605.11019v1"},{"title":"Fostering Appropriate Reliance on Large Language Models: The Role of   Explanations, Sources, and Inconsistencies","url":"https://arxiv.org/pdf/2502.08554"},{"title":"Measuring and mitigating overreliance is necessary for building human-compatible AI","url":"https://arxiv.org/pdf/2509.08010"},{"title":"Explanations from Large Language Models Make Small Reasoners Better","url":"https://arxiv.org/pdf/2210.06726"}]

Based on the search results, here's what I found:

The search returned relevant information about LLM overreliance and explanations, though the specific combination of "adaptive explanation gating," "dual explanation," and related mechanisms isn't prominently featured in these results.

Key findings from the search:

1. **LLM Overreliance Research**: As LLMs increasingly influence consequential decisions across diverse domains, the risk of overreliance — relying on LLMs beyond their capabilities — grows, particularly when users accept incorrect outputs or inappropriately delegate decisions.

2. **Explanations and LLM Use**: A 2025 paper titled "Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies" was presented at CHI Conference on Human Factors in Computing Systems in April-May 2025.

3. **LLM-Guided Gating Mechanisms**: LLM-guided gating mechanisms integrate LLM outputs, confidences, or induced priors to conditionally modulate the computational path, blending, or regularization pressure within a broader machine learning system. Key mechanisms include curriculum-based step gating, instance-adaptive neural gates, and contextual regularization scheduling.

4. **Explanations Improving Model Performance**: Explanations generated from LLMs can consistently improve reasoning capability of smaller language models.

However, the search didn't return specific papers or research explicitly on "adaptive explanation gating" or "dual explanation" frameworks as described in your query. If you're looking for more specific research on these particular approaches, a more targeted search might be helpful.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bd70642-8b3e-4b9d-b700-92c146a77ede",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "d32fcc41-00ef-4465-b467-647256d35eb8",
  "toolUseResult": {
    "query": "adaptive explanation gating LLM overreliance dual explanation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011qni3HrYhrPmgFcA4US1vG",
        "content": [
          {
            "title": "LLM09: Overreliance - OWASP Gen AI Security Project",
            "url": "https://genai.owasp.org/llmrisk2023-24/llm09-overreliance/"
          },
          {
            "title": "LLM-Guided Gating Mechanism",
            "url": "https://www.emergentmind.com/topics/llm-guided-gating-mechanism"
          },
          {
            "title": "Efficient LLM Reasoning via Variational Posterior Guidance with Efficiency Awareness",
            "url": "https://arxiv.org/html/2605.11019v1"
          },
          {
            "title": "Fostering Appropriate Reliance on Large Language Models: The Role of   Explanations, Sources, and Inconsistencies",
            "url": "https://arxiv.org/pdf/2502.08554"
          },
          {
            "title": "Measuring and mitigating overreliance is necessary for building human-compatible AI",
            "url": "https://arxiv.org/pdf/2509.08010"
          },
          {
            "title": "Explanations from Large Language Models Make Small Reasoners Better",
            "url": "https://arxiv.org/pdf/2210.06726"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nThe search returned relevant information about LLM overreliance and explanations, though the specific combination of \"adaptive explanation gating,\" \"dual explanation,\" and related mechanisms isn't prominently featured in these results.\n\nKey findings from the search:\n\n1. **LLM Overreliance Research**: As LLMs increasingly influence consequential decisions across diverse domains, the risk of overreliance — relying on LLMs beyond their capabilities — grows, particularly when users accept incorrect outputs or inappropriately delegate decisions.\n\n2. **Explanations and LLM Use**: A 2025 paper titled \"Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies\" was presented at CHI Conference on Human Factors in Computing Systems in April-May 2025.\n\n3. **LLM-Guided Gating Mechanisms**: LLM-guided gating mechanisms integrate LLM outputs, confidences, or induced priors to conditionally modulate the computational path, blending, or regularization pressure within a broader machine learning system. Key mechanisms include curriculum-based step gating, instance-adaptive neural gates, and contextual regularization scheduling.\n\n4. **Explanations Improving Model Performance**: Explanations generated from LLMs can consistently improve reasoning capability of smaller language models.\n\nHowever, the search didn't return specific papers or research explicitly on \"adaptive explanation gating\" or \"dual explanation\" frameworks as described in your query. If you're looking for more specific research on these particular approaches, a more targeted search might be helpful."
    ],
    "durationSeconds": 7.341509962,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7bd70642-8b3e-4b9d-b700-92c146a77ede",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T03:31:39.400Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BWU1Au4t5zvjUVo9AspmyJ`</summary>

```json
{
  "query": "\"Adjust for Trust\" trust-gated counter-explanation IUI 2026 arXiv 2502.13321"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d32fcc41-00ef-4465-b467-647256d35eb8",
  "isSidechain": false,
  "requestId": "req_011CbD7dMRpDMkMwR1SaDW8U",
  "type": "assistant",
  "uuid": "f1bd7598-a119-4ee6-8125-5ec595e9f4f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPeHirDwjUmGktA8KmRauH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 24640,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 24640,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 773
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

_source line 16 · 2026-05-20T03:31:45.466Z_

<details><summary>↩ Tool result · `toolu_01BWU1Au4t5zvjUVo9AspmyJ`</summary>

```text
Web search results for query: ""Adjust for Trust" trust-gated counter-explanation IUI 2026 arXiv 2502.13321"

Links: [{"title":"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://arxiv.org/html/2502.13321"},{"title":"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://arxiv.org/pdf/2502.13321"},{"title":"(PDF) Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://www.researchgate.net/publication/389167262_Adjust_for_Trust_Mitigating_Trust-Induced_Inappropriate_Reliance_on_AI_Assistance"},{"title":"[Literature Review] Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://www.themoonlight.io/en/review/adjust-for-trust-mitigating-trust-induced-inappropriate-reliance-on-ai-assistance"},{"title":"[2502.13321] Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance","url":"https://arxiv.org/abs/2502.13321"},{"title":"Ditch the Gate: How to Build Trust and Demand with Ungated Content in 2026","url":"https://www.a88lab.com/blog/ditch-the-gate-how-to-build-trust-and-demand-with-ungated-content"}]

Perfect! I found the paper you're looking for. Here's what I found:

**"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance"** is a paper presented at the 31st International Conference on Intelligent User Interfaces (IUI '26), March 23–26, 2026, in Paphos, Cyprus. The paper is authored by Tejas Srinivasan and Jesse Thomason from the University of Southern California.

**Key Contribution:**

The paper addresses how user trust biases reliance on AI assistance during decision-making tasks, proposing that AI assistants should adapt their behavior through trust-adaptive interventions to mitigate such inappropriate reliance.

**Main Findings:**

In two decision-making scenarios—laypeople answering science questions and medical doctors making diagnoses—the researchers found that providing supporting and counter-explanations during moments of low and high trust, respectively, yields up to 38% reduction in inappropriate reliance and 20% improvement in decision accuracy. Additionally, the researchers were able to reduce over-reliance by adaptively inserting forced pauses to promote deliberation.

The arXiv preprint number is **2502.13321**, and the paper is available on ArXiv in both HTML and PDF formats.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1bd7598-a119-4ee6-8125-5ec595e9f4f6",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "9760f694-30e4-4293-aa99-bd134cae34a9",
  "toolUseResult": {
    "query": "\"Adjust for Trust\" trust-gated counter-explanation IUI 2026 arXiv 2502.13321",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LYx8Q9RyapfcCixRAP6i26",
        "content": [
          {
            "title": "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://arxiv.org/html/2502.13321"
          },
          {
            "title": "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://arxiv.org/pdf/2502.13321"
          },
          {
            "title": "(PDF) Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://www.researchgate.net/publication/389167262_Adjust_for_Trust_Mitigating_Trust-Induced_Inappropriate_Reliance_on_AI_Assistance"
          },
          {
            "title": "[Literature Review] Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://www.themoonlight.io/en/review/adjust-for-trust-mitigating-trust-induced-inappropriate-reliance-on-ai-assistance"
          },
          {
            "title": "[2502.13321] Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
            "url": "https://arxiv.org/abs/2502.13321"
          },
          {
            "title": "Ditch the Gate: How to Build Trust and Demand with Ungated Content in 2026",
            "url": "https://www.a88lab.com/blog/ditch-the-gate-how-to-build-trust-and-demand-with-ungated-content"
          }
        ]
      },
      "Perfect! I found the paper you're looking for. Here's what I found:\n\n**\"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance\"** is a paper presented at the 31st International Conference on Intelligent User Interfaces (IUI '26), March 23–26, 2026, in Paphos, Cyprus. The paper is authored by Tejas Srinivasan and Jesse Thomason from the University of Southern California.\n\n**Key Contribution:**\n\nThe paper addresses how user trust biases reliance on AI assistance during decision-making tasks, proposing that AI assistants should adapt their behavior through trust-adaptive interventions to mitigate such inappropriate reliance.\n\n**Main Findings:**\n\nIn two decision-making scenarios—laypeople answering science questions and medical doctors making diagnoses—the researchers found that providing supporting and counter-explanations during moments of low and high trust, respectively, yields up to 38% reduction in inappropriate reliance and 20% improvement in decision accuracy. Additionally, the researchers were able to reduce over-reliance by adaptively inserting forced pauses to promote deliberation.\n\nThe arXiv preprint number is **2502.13321**, and the paper is available on ArXiv in both HTML and PDF formats."
    ],
    "durationSeconds": 6.061144136999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f1bd7598-a119-4ee6-8125-5ec595e9f4f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T03:31:48.613Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0111hE9u7mdrk34NtinF3u8a`</summary>

```json
{
  "query": "arXiv 2605.10930 \"false trust\" LLM explanations dual explanations overreliance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9760f694-30e4-4293-aa99-bd134cae34a9",
  "isSidechain": false,
  "requestId": "req_011CbD7e1RK9WvMmJ9ecZwbG",
  "type": "assistant",
  "uuid": "7d3937ef-1631-4507-8b04-abd34980c17c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXpKiUUG7ibpuFXa1n6dk9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 25413,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 25413,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 789
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

_source line 18 · 2026-05-20T03:31:55.883Z_

<details><summary>↩ Tool result · `toolu_0111hE9u7mdrk34NtinF3u8a`</summary>

```text
Web search results for query: "arXiv 2605.10930 "false trust" LLM explanations dual explanations overreliance 2026"

Links: [{"title":"[2605.10930] Evaluating the False Trust engendered by LLM Explanations","url":"https://arxiv.org/abs/2605.10930"},{"title":"Are self-explanations from Large Language Models faithful?","url":"https://arxiv.org/pdf/2401.07927"},{"title":"LLM-Generated Black-box Explanations Can Be Adversarially Helpful","url":"https://arxiv.org/pdf/2405.06800"},{"title":"Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations","url":"https://arxiv.org/pdf/2504.14150"},{"title":"Can LLMs Produce Faithful Explanations For Fact-checking? Towards   Faithful Explainable Fact-Checking via Multi-Agent Debate","url":"https://arxiv.org/pdf/2402.07401"},{"title":"Truthful or Fabricated? Using Causal Attribution to Mitigate Reward Hacking in Explanations","url":"https://arxiv.org/pdf/2504.05294"},{"title":"Quantifying Uncertainty in Natural Language Explanations of Large   Language Models","url":"https://arxiv.org/pdf/2311.03533"},{"title":"Explainability of Large Language Models: Opportunities and Challenges toward Generating Trustworthy Explanations","url":"https://arxiv.org/pdf/2510.17256"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Evaluating the False Trust engendered by LLM Explanations"

**Key Findings:**

Reasoning traces and post-hoc explanations are persuasive but not informative: they increase user acceptance of LLM predictions regardless of their correctness. This demonstrates the "false trust" problem with standard explanation approaches.

The study tested a contrastive dual explanation setting where arguments for and against the AI's answer were presented, and dual explanation was the only condition that genuinely improves users' ability to distinguish correct from incorrect AI outputs.

**Study Approach:**

The researchers conducted a between-subject user study, simulating a setting where users do not have the means to verify the solution and analyzed the false trust engendered by commonly used LLM explanations - reasoning traces, their summaries and post-hoc explanations.

**Core Problem:**

Reasoning traces, despite evidence that they are neither faithful representations of the model's computations nor necessarily semantically meaningful, are often interpreted as provenance explanations, and it is unclear whether explanations or reasoning traces help users identify when the AI is incorrect, or whether they simply persuade users to trust the AI regardless.

The paper was submitted in May 2026 and addresses the important issue of overreliance on LLM explanations through user-centered evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d3937ef-1631-4507-8b04-abd34980c17c",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "560fd4da-b916-4a78-98ce-0f9109d487bf",
  "toolUseResult": {
    "query": "arXiv 2605.10930 \"false trust\" LLM explanations dual explanations overreliance 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HPx8E322Tvm291PE5rPpcm",
        "content": [
          {
            "title": "[2605.10930] Evaluating the False Trust engendered by LLM Explanations",
            "url": "https://arxiv.org/abs/2605.10930"
          },
          {
            "title": "Are self-explanations from Large Language Models faithful?",
            "url": "https://arxiv.org/pdf/2401.07927"
          },
          {
            "title": "LLM-Generated Black-box Explanations Can Be Adversarially Helpful",
            "url": "https://arxiv.org/pdf/2405.06800"
          },
          {
            "title": "Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations",
            "url": "https://arxiv.org/pdf/2504.14150"
          },
          {
            "title": "Can LLMs Produce Faithful Explanations For Fact-checking? Towards   Faithful Explainable Fact-Checking via Multi-Agent Debate",
            "url": "https://arxiv.org/pdf/2402.07401"
          },
          {
            "title": "Truthful or Fabricated? Using Causal Attribution to Mitigate Reward Hacking in Explanations",
            "url": "https://arxiv.org/pdf/2504.05294"
          },
          {
            "title": "Quantifying Uncertainty in Natural Language Explanations of Large   Language Models",
            "url": "https://arxiv.org/pdf/2311.03533"
          },
          {
            "title": "Explainability of Large Language Models: Opportunities and Challenges toward Generating Trustworthy Explanations",
            "url": "https://arxiv.org/pdf/2510.17256"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** \"Evaluating the False Trust engendered by LLM Explanations\"\n\n**Key Findings:**\n\nReasoning traces and post-hoc explanations are persuasive but not informative: they increase user acceptance of LLM predictions regardless of their correctness. This demonstrates the \"false trust\" problem with standard explanation approaches.\n\nThe study tested a contrastive dual explanation setting where arguments for and against the AI's answer were presented, and dual explanation was the only condition that genuinely improves users' ability to distinguish correct from incorrect AI outputs.\n\n**Study Approach:**\n\nThe researchers conducted a between-subject user study, simulating a setting where users do not have the means to verify the solution and analyzed the false trust engendered by commonly used LLM explanations - reasoning traces, their summaries and post-hoc explanations.\n\n**Core Problem:**\n\nReasoning traces, despite evidence that they are neither faithful representations of the model's computations nor necessarily semantically meaningful, are often interpreted as provenance explanations, and it is unclear whether explanations or reasoning traces help users identify when the AI is incorrect, or whether they simply persuade users to trust the AI regardless.\n\nThe paper was submitted in May 2026 and addresses the important issue of overreliance on LLM explanations through user-centered evaluation."
    ],
    "durationSeconds": 7.261703911999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7d3937ef-1631-4507-8b04-abd34980c17c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T03:31:58.742Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JQg8bEBkeWBb7ChvNVsJnN`</summary>

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
  "parentUuid": "560fd4da-b916-4a78-98ce-0f9109d487bf",
  "isSidechain": false,
  "requestId": "req_011CbD7emxiW3fDKkkqrSbEW",
  "type": "assistant",
  "uuid": "83053a39-eb2c-44f2-9d5f-5979d2238dc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115cQ5jNse3PpCJZZTi8SMs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 26202,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 26202,
          "cache_creation_input_tokens": 799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 799
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

_source line 20 · 2026-05-20T03:32:05.293Z_

<details><summary>↩ Tool result · `toolu_01JQg8bEBkeWBb7ChvNVsJnN`</summary>

```text
Web search results for query: "model uncertainty gating signal explanation selection human-AI decision making 2025 2026"

Links: [{"title":"Uncertainty Gating for Cost-Aware Explainable Artificial Intelligence","url":"https://arxiv.org/html/2603.29915v1"},{"title":"Harnessing Human Uncertainty to Train More Accurate and Aligned AI Systems | Decision Analysis","url":"https://pubsonline.informs.org/doi/abs/10.1287/deca.2025.0395?af=R"},{"title":"Using AI Uncertainty Quantification to Improve Human Decision-Making","url":"https://arxiv.org/pdf/2309.10852"},{"title":"A Quantum Probability Approach to Improving Human–AI Decision Making - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11854726/"},{"title":"DeCoDe: Defer-and-Complement Decision-Making via Decoupled Concept Bottleneck Models","url":"https://arxiv.org/pdf/2505.19220"}]

I found several relevant research results on your topic. Here's what the web search revealed:

## Key Findings

**Uncertainty Gating for Explainable AI:**
Epistemic uncertainty can serve as a low-cost proxy for explanation reliability, with high epistemic uncertainty identifying regions where the decision boundary is poorly defined and explanations become unstable and unfaithful. This enables two complementary approaches: routing samples to different XAI methods based on expected explanation reliability, and deferring explanation generation for uncertain samples under budget constraints.

**Human-AI Decision Making:**
AI Uncertainty Quantification (UQ) has the potential to improve human decision-making beyond AI predictions alone by providing additional probabilistic information to users. Research showed that UQ was beneficial for decision-making performance compared to only AI predictions, with generalizable benefits across various representations for probabilistic information.

**Strategy Selection in Collaboration:**
Machine learning models are often endowed with the ability to defer decisions to humans when faced with unfamiliar or uncertain cases through a strategy known as Learning to Defer (L2D), enabling the model to learn when to predict jointly and when to defer. Recent frameworks leverage interpretable concept representations to support flexible strategy selection—autonomous AI, human-only, and human-AI complementarity—guided by a concept-driven gating network.

The search results show active 2025-2026 research on integrating uncertainty quantification with human-AI collaboration and explanation selection mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83053a39-eb2c-44f2-9d5f-5979d2238dc5",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "298c8872-8574-4b2d-8ad0-5284054d45d7",
  "toolUseResult": {
    "query": "model uncertainty gating signal explanation selection human-AI decision making 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NcNo2VZrntvXncpeMCTy9k",
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
      "I found several relevant research results on your topic. Here's what the web search revealed:\n\n## Key Findings\n\n**Uncertainty Gating for Explainable AI:**\nEpistemic uncertainty can serve as a low-cost proxy for explanation reliability, with high epistemic uncertainty identifying regions where the decision boundary is poorly defined and explanations become unstable and unfaithful. This enables two complementary approaches: routing samples to different XAI methods based on expected explanation reliability, and deferring explanation generation for uncertain samples under budget constraints.\n\n**Human-AI Decision Making:**\nAI Uncertainty Quantification (UQ) has the potential to improve human decision-making beyond AI predictions alone by providing additional probabilistic information to users. Research showed that UQ was beneficial for decision-making performance compared to only AI predictions, with generalizable benefits across various representations for probabilistic information.\n\n**Strategy Selection in Collaboration:**\nMachine learning models are often endowed with the ability to defer decisions to humans when faced with unfamiliar or uncertain cases through a strategy known as Learning to Defer (L2D), enabling the model to learn when to predict jointly and when to defer. Recent frameworks leverage interpretable concept representations to support flexible strategy selection—autonomous AI, human-only, and human-AI complementarity—guided by a concept-driven gating network.\n\nThe search results show active 2025-2026 research on integrating uncertainty quantification with human-AI collaboration and explanation selection mechanisms."
    ],
    "durationSeconds": 6.545761969999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "83053a39-eb2c-44f2-9d5f-5979d2238dc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "298c8872-8574-4b2d-8ad0-5284054d45d7",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare uncertainty vs. trust gating for adaptive LLM explanations",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Tool call

_source line 23 · 2026-05-20T03:32:08.205Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QAbeidqbaMhuo7VTKfn9k2`</summary>

```json
{
  "query": "\"To Rely or Not to Rely\" Bo CHI 2025 uncertainty highlighting algorithm aversion LLM arXiv 2412.15584"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "298c8872-8574-4b2d-8ad0-5284054d45d7",
  "isSidechain": false,
  "requestId": "req_011CbD7fUBRAFDjTKBrk1WoL",
  "type": "assistant",
  "uuid": "c8b4acf9-ea3b-4495-b18e-35c6bc74ce48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTD3vYK7JV7w7gMxCwbT8N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 27001,
      "output_tokens": 85,
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
          "output_tokens": 85,
          "cache_read_input_tokens": 27001,
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

### Tool result

_source line 24 · 2026-05-20T03:32:14.694Z_

<details><summary>↩ Tool result · `toolu_01QAbeidqbaMhuo7VTKfn9k2`</summary>

```text
Web search results for query: ""To Rely or Not to Rely" Bo CHI 2025 uncertainty highlighting algorithm aversion LLM arXiv 2412.15584"

Links: [{"title":"To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3706598.3714097"},{"title":"To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models","url":"https://arxiv.org/html/2412.15584"},{"title":"(PDF) To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models","url":"https://www.researchgate.net/publication/391269940_To_Rely_or_Not_to_Rely_Evaluating_Interventions_for_Appropriate_Reliance_on_Large_Language_Models"},{"title":"An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"},{"title":"To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models","url":"https://arxiv.org/pdf/2412.15584"}]

I found the paper! Here's information about "To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models":

**Paper Details:**
- Authors: Jessica Y. Bo, Sophia Wan, and Ashton Anderson. Published in 2025 at the ACM Conference on Human Factors in Computing Systems (CHI '25), April 26–May 01, 2025, Yokohama, Japan
- ArXiv ID: 2412.15584
- DOI: 10.1145/3706598.3714097

**Research Focus:**
The paper addresses how as Large Language Models become integral to decision-making, users may over-rely on LLM advice that is confidently stated but wrong, or under-rely due to mistrust. The authors evaluate reliance interventions for their effectiveness.

**Key Interventions Tested:**
The paper evaluates three LLM reliance interventions: Reliance Disclaimer, Uncertainty Highlighting, and Implicit Answer.

**Main Findings:**
- While interventions reduce over-reliance, they generally fail to improve appropriate reliance
- Uncertainty Highlighting had significantly lower ratings in all categories compared to Control, indicating that the implementation may have induced too much uncertainty in users
- Uncertainty calibration methods can have the undesirable outcome of inducing negative perceptions of accuracy and usefulness of the LLM, which increases overall algorithm aversion against LLM advice


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8b4acf9-ea3b-4495-b18e-35c6bc74ce48",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "8f6519ce-cf82-42ee-b8f1-2b8efbb12eb9",
  "toolUseResult": {
    "query": "\"To Rely or Not to Rely\" Bo CHI 2025 uncertainty highlighting algorithm aversion LLM arXiv 2412.15584",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Cpbc6XaWnrsxLmbJEQ4Xwo",
        "content": [
          {
            "title": "To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems",
            "url": "https://dl.acm.org/doi/10.1145/3706598.3714097"
          },
          {
            "title": "To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models",
            "url": "https://arxiv.org/html/2412.15584"
          },
          {
            "title": "(PDF) To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models",
            "url": "https://www.researchgate.net/publication/391269940_To_Rely_or_Not_to_Rely_Evaluating_Interventions_for_Appropriate_Reliance_on_Large_Language_Models"
          },
          {
            "title": "An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"
          },
          {
            "title": "To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models",
            "url": "https://arxiv.org/pdf/2412.15584"
          }
        ]
      },
      "I found the paper! Here's information about \"To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models\":\n\n**Paper Details:**\n- Authors: Jessica Y. Bo, Sophia Wan, and Ashton Anderson. Published in 2025 at the ACM Conference on Human Factors in Computing Systems (CHI '25), April 26–May 01, 2025, Yokohama, Japan\n- ArXiv ID: 2412.15584\n- DOI: 10.1145/3706598.3714097\n\n**Research Focus:**\nThe paper addresses how as Large Language Models become integral to decision-making, users may over-rely on LLM advice that is confidently stated but wrong, or under-rely due to mistrust. The authors evaluate reliance interventions for their effectiveness.\n\n**Key Interventions Tested:**\nThe paper evaluates three LLM reliance interventions: Reliance Disclaimer, Uncertainty Highlighting, and Implicit Answer.\n\n**Main Findings:**\n- While interventions reduce over-reliance, they generally fail to improve appropriate reliance\n- Uncertainty Highlighting had significantly lower ratings in all categories compared to Control, indicating that the implementation may have induced too much uncertainty in users\n- Uncertainty calibration methods can have the undesirable outcome of inducing negative perceptions of accuracy and usefulness of the LLM, which increases overall algorithm aversion against LLM advice"
    ],
    "durationSeconds": 6.484557585000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c8b4acf9-ea3b-4495-b18e-35c6bc74ce48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T03:32:17.061Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HGugHiTgE5EYUP5FWs6u2s`</summary>

```json
{
  "query": "adaptive AI explanation selection uncertainty trust comparison user study 2025 2026 CHI CSCW"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f6519ce-cf82-42ee-b8f1-2b8efbb12eb9",
  "isSidechain": false,
  "requestId": "req_011CbD7gAUawKoNb51HSWBwo",
  "type": "assistant",
  "uuid": "c6fd68c7-5c85-4606-ade9-8fb8d01d2115",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsxhoS3iVwcLKnYb3Cb9U9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 27679,
      "output_tokens": 73,
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
          "output_tokens": 73,
          "cache_read_input_tokens": 27679,
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

_source line 26 · 2026-05-20T03:32:23.953Z_

<details><summary>↩ Tool result · `toolu_01HGugHiTgE5EYUP5FWs6u2s`</summary>

```text
Web search results for query: "adaptive AI explanation selection uncertainty trust comparison user study 2025 2026 CHI CSCW"

Links: [{"title":"The Effects of Presenting AI Uncertainty Information on Pharmacists’ Trust in Automated Pill Recognition Technology: Exploratory Mixed Subjects Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11862782/"},{"title":"A Diachronic Perspective on User Trust in AI under Uncertainty","url":"https://arxiv.org/pdf/2310.13544"},{"title":"arXiv:2502.13321v1 [cs.HC] 18 Feb 2025","url":"https://arxiv.org/pdf/2502.13321"},{"title":"Preliminary Quantitative Study on Explainability and Trust in AI Systems","url":"https://arxiv.org/pdf/2510.15769"},{"title":"When AI Persuades: Adversarial Explanation Attacks on Human Trust in AI-Assisted Decision Making","url":"https://arxiv.org/pdf/2602.04003"}]

Based on the search results, here are the relevant research findings on adaptive AI explanation selection, uncertainty, trust, and user studies from 2025-2026 in the CHI/CSCW space:

## Key Findings:

**Adaptive Explanations and Trust:**
Research shows that trust-adaptive explanations help, with showing explanations adaptively reducing under-reliance in user-AI interactions.

**Uncertainty Information and Trust:**
The introduction of an uncertainty plot to AI aid significantly enhanced pharmacists' end trust, and providing visual explanations enhanced trust and confidence in participants' decision-making.

**Trust Dynamics Under Uncertainty:**
Even a few incorrect instances with inaccurate confidence estimates damage user trust and performance, with very slow recovery, and different types of miscalibration—unconfidently correct and confidently incorrect—have different negative effects on user trust.

**Explanation Design Impact:**
Explanations are central to trust calibration, the process by which users align their confidence in a system with its actual reliability.

**Trust Miscalibration in Explanations:**
Most users make decisions based on explanations, and adversarial explanations do not substantially reduce trust scores, with incorrect outputs framed adversarially receiving trust scores close to correct outputs.

These findings highlight the critical role of adaptive explanation selection and uncertainty presentation in managing user trust in AI systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6fd68c7-5c85-4606-ade9-8fb8d01d2115",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "43368040-7235-4ee8-8667-1ef49f770244",
  "toolUseResult": {
    "query": "adaptive AI explanation selection uncertainty trust comparison user study 2025 2026 CHI CSCW",
    "results": [
      {
        "tool_use_id": "srvtoolu_0163vhTEzMDXQvzVUgtgpkSm",
        "content": [
          {
            "title": "The Effects of Presenting AI Uncertainty Information on Pharmacists’ Trust in Automated Pill Recognition Technology: Exploratory Mixed Subjects Study",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11862782/"
          },
          {
            "title": "A Diachronic Perspective on User Trust in AI under Uncertainty",
            "url": "https://arxiv.org/pdf/2310.13544"
          },
          {
            "title": "arXiv:2502.13321v1 [cs.HC] 18 Feb 2025",
            "url": "https://arxiv.org/pdf/2502.13321"
          },
          {
            "title": "Preliminary Quantitative Study on Explainability and Trust in AI Systems",
            "url": "https://arxiv.org/pdf/2510.15769"
          },
          {
            "title": "When AI Persuades: Adversarial Explanation Attacks on Human Trust in AI-Assisted Decision Making",
            "url": "https://arxiv.org/pdf/2602.04003"
          }
        ]
      },
      "Based on the search results, here are the relevant research findings on adaptive AI explanation selection, uncertainty, trust, and user studies from 2025-2026 in the CHI/CSCW space:\n\n## Key Findings:\n\n**Adaptive Explanations and Trust:**\nResearch shows that trust-adaptive explanations help, with showing explanations adaptively reducing under-reliance in user-AI interactions.\n\n**Uncertainty Information and Trust:**\nThe introduction of an uncertainty plot to AI aid significantly enhanced pharmacists' end trust, and providing visual explanations enhanced trust and confidence in participants' decision-making.\n\n**Trust Dynamics Under Uncertainty:**\nEven a few incorrect instances with inaccurate confidence estimates damage user trust and performance, with very slow recovery, and different types of miscalibration—unconfidently correct and confidently incorrect—have different negative effects on user trust.\n\n**Explanation Design Impact:**\nExplanations are central to trust calibration, the process by which users align their confidence in a system with its actual reliability.\n\n**Trust Miscalibration in Explanations:**\nMost users make decisions based on explanations, and adversarial explanations do not substantially reduce trust scores, with incorrect outputs framed adversarially receiving trust scores close to correct outputs.\n\nThese findings highlight the critical role of adaptive explanation selection and uncertainty presentation in managing user trust in AI systems."
    ],
    "durationSeconds": 6.886057572999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c6fd68c7-5c85-4606-ade9-8fb8d01d2115",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T03:32:26.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DSJus7iLnsKvr4vRUQN4uM`</summary>

```json
{
  "query": "\"From Text to Trust\" Li CHI 2025 adaptive LLM explanation dynamic programming arXiv 2502.11919"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43368040-7235-4ee8-8667-1ef49f770244",
  "isSidechain": false,
  "requestId": "req_011CbD7gqysKsKb85N5h7ZNR",
  "type": "assistant",
  "uuid": "781f7af2-203a-471a-b7bf-166a3c45cf9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WUg7XA3TGzWcnBfsoETiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 28491,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 28491,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
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

_source line 28 · 2026-05-20T03:32:33.784Z_

<details><summary>↩ Tool result · `toolu_01DSJus7iLnsKvr4vRUQN4uM`</summary>

```text
Web search results for query: ""From Text to Trust" Li CHI 2025 adaptive LLM explanation dynamic programming arXiv 2502.11919"

Links: [{"title":"[2502.11919] From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis","url":"https://arxiv.org/abs/2502.11919"},{"title":"Computation and Language Feb 2025","url":"https://arxiv.org/list/cs.CL/2025-02?skip=2100&show=50"},{"title":"From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis","url":"https://arxiv.org/html/2502.11919"},{"title":"From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3706598.3713133"},{"title":"When to Trust LLMs: Aligning Confidence with Response Quality","url":"https://arxiv.org/pdf/2404.17287"},{"title":"Don't Overthink It: Inter-Rollout Action Agreement as a Free Adaptive-Compute Signal for LLM Agents","url":"https://arxiv.org/pdf/2604.08369"}]

I found the research paper! Here's what I discovered:

"From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis" is a paper accepted to CHI 2025, authored by Zhuoyan Li, Hangxiao Zhu, Zhuoran Lu, Ziang Xiao, and Ming Yin.

The paper addresses an important problem: AI-assisted decision making becomes increasingly prevalent, yet individuals often fail to utilize AI-based decision aids appropriately especially when the AI explanations are absent.

The key contribution involves using LLMs to help with this challenge. Large language models, with their exceptional conversational and analytical capabilities, present great opportunities to enhance AI-assisted decision making in the absence of AI explanations by providing natural-language-based analysis of AI's decision recommendation. However, the paper shows via a randomized experiment that presenting LLM-powered analysis of each task feature, either sequentially or concurrently, does not significantly improve people's AI-assisted decision performance.

The paper was submitted to arXiv on February 17, 2025, with the identifier arXiv:2502.11919.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "781f7af2-203a-471a-b7bf-166a3c45cf9e",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "524f88f5-6184-42ff-b373-e0ae9a34e378",
  "toolUseResult": {
    "query": "\"From Text to Trust\" Li CHI 2025 adaptive LLM explanation dynamic programming arXiv 2502.11919",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QnZkzvYcB16cwNr1o9qWi8",
        "content": [
          {
            "title": "[2502.11919] From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis",
            "url": "https://arxiv.org/abs/2502.11919"
          },
          {
            "title": "Computation and Language Feb 2025",
            "url": "https://arxiv.org/list/cs.CL/2025-02?skip=2100&show=50"
          },
          {
            "title": "From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis",
            "url": "https://arxiv.org/html/2502.11919"
          },
          {
            "title": "From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems",
            "url": "https://dl.acm.org/doi/10.1145/3706598.3713133"
          },
          {
            "title": "When to Trust LLMs: Aligning Confidence with Response Quality",
            "url": "https://arxiv.org/pdf/2404.17287"
          },
          {
            "title": "Don't Overthink It: Inter-Rollout Action Agreement as a Free Adaptive-Compute Signal for LLM Agents",
            "url": "https://arxiv.org/pdf/2604.08369"
          }
        ]
      },
      "I found the research paper! Here's what I discovered:\n\n\"From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis\" is a paper accepted to CHI 2025, authored by Zhuoyan Li, Hangxiao Zhu, Zhuoran Lu, Ziang Xiao, and Ming Yin.\n\nThe paper addresses an important problem: AI-assisted decision making becomes increasingly prevalent, yet individuals often fail to utilize AI-based decision aids appropriately especially when the AI explanations are absent.\n\nThe key contribution involves using LLMs to help with this challenge. Large language models, with their exceptional conversational and analytical capabilities, present great opportunities to enhance AI-assisted decision making in the absence of AI explanations by providing natural-language-based analysis of AI's decision recommendation. However, the paper shows via a randomized experiment that presenting LLM-powered analysis of each task feature, either sequentially or concurrently, does not significantly improve people's AI-assisted decision performance.\n\nThe paper was submitted to arXiv on February 17, 2025, with the identifier arXiv:2502.11919."
    ],
    "durationSeconds": 7.168813569000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "781f7af2-203a-471a-b7bf-166a3c45cf9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T03:32:33.787Z_

```json
{
  "parentUuid": "524f88f5-6184-42ff-b373-e0ae9a34e378",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7e30ab87-8271-49b8-9bc3-46430d9a0699",
  "timestamp": "2026-05-20T03:32:33.787Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T03:32:37.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MUhJvJdx2mqd4v1jcBaZDT`</summary>

```json
{
  "query": "\"Unequal Uncertainty\" fairness uncertainty-gated interventions discrimination arXiv 2508.07872"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e30ab87-8271-49b8-9bc3-46430d9a0699",
  "isSidechain": false,
  "requestId": "req_011CbD7ha5BWsi4As3tNST6B",
  "type": "assistant",
  "uuid": "7c8ba682-69b6-4cbd-b3a5-a0608fd0f123",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfM6uGcjoRFQopV6AHnBAk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 806,
      "cache_read_input_tokens": 29158,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 29158,
          "cache_creation_input_tokens": 806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 806
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

_source line 31 · 2026-05-20T03:32:44.998Z_

<details><summary>↩ Tool result · `toolu_01MUhJvJdx2mqd4v1jcBaZDT`</summary>

```text
Web search results for query: ""Unequal Uncertainty" fairness uncertainty-gated interventions discrimination arXiv 2508.07872"

Links: [{"title":"[2508.07872] Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI","url":"https://arxiv.org/abs/2508.07872"},{"title":"[2508.07872v1] Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI","url":"https://arxiv.org/abs/2508.07872v1"},{"title":"Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating","url":"https://arxiv.org/pdf/2508.07872"},{"title":"Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI","url":"https://arxiv.org/html/2508.07872v1"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=4075&show=25"}]

Based on the search results, here's what I found about the paper arXiv 2508.07872:

**Paper Title:** Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI

**Authors:** Holli Sargeant, Mackenzie Jorgensen, Arina Shah, Adrian Weller, Umang Bhatt

**Core Focus:** The paper provides the first integrated socio-technical and legal analysis of uncertainty-based algorithmic interventions.

**Main Topic:** Uncertainty in artificial intelligence (AI) predictions poses urgent legal and ethical challenges for AI-assisted decision-making.

**Interventions Examined:** The paper examines two algorithmic interventions that act as guardrails for human-AI collaboration: selective abstention, which withholds high-uncertainty predictions from human decision-makers, and selective friction, which delivers those predictions together with salient warnings or disclosures that slow the decision process.

**Key Problem:** Research has shown that selective abstention based on uncertainty can inadvertently exacerbate disparities and disadvantage under-represented groups that disproportionately receive uncertain predictions.

**Case Studies:** The paper demonstrates through two case studies—AI-assisted consumer credit decisions and AI-assisted content moderation—how the seemingly neutral use of uncertainty thresholds can trigger discriminatory impacts.

**Conclusion:** The authors argue that although both interventions pose risks of unlawful discrimination under UK law, selective frictions offer a promising pathway toward fairer and more accountable AI-assisted decision-making by preserving transparency and encouraging more cautious human judgment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c8ba682-69b6-4cbd-b3a5-a0608fd0f123",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "e1f564b5-f31e-4d08-b904-003bad55730e",
  "toolUseResult": {
    "query": "\"Unequal Uncertainty\" fairness uncertainty-gated interventions discrimination arXiv 2508.07872",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TvHaFiRRoTVvhZpkBTmQYd",
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
            "url": "https://arxiv.org/html/2508.07872v1"
          },
          {
            "title": "Computer Science Aug 2025",
            "url": "https://arxiv.org/list/cs/2025-08?skip=4075&show=25"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper arXiv 2508.07872:\n\n**Paper Title:** Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI\n\n**Authors:** Holli Sargeant, Mackenzie Jorgensen, Arina Shah, Adrian Weller, Umang Bhatt\n\n**Core Focus:** The paper provides the first integrated socio-technical and legal analysis of uncertainty-based algorithmic interventions.\n\n**Main Topic:** Uncertainty in artificial intelligence (AI) predictions poses urgent legal and ethical challenges for AI-assisted decision-making.\n\n**Interventions Examined:** The paper examines two algorithmic interventions that act as guardrails for human-AI collaboration: selective abstention, which withholds high-uncertainty predictions from human decision-makers, and selective friction, which delivers those predictions together with salient warnings or disclosures that slow the decision process.\n\n**Key Problem:** Research has shown that selective abstention based on uncertainty can inadvertently exacerbate disparities and disadvantage under-represented groups that disproportionately receive uncertain predictions.\n\n**Case Studies:** The paper demonstrates through two case studies—AI-assisted consumer credit decisions and AI-assisted content moderation—how the seemingly neutral use of uncertainty thresholds can trigger discriminatory impacts.\n\n**Conclusion:** The authors argue that although both interventions pose risks of unlawful discrimination under UK law, selective frictions offer a promising pathway toward fairer and more accountable AI-assisted decision-making by preserving transparency and encouraging more cautious human judgment."
    ],
    "durationSeconds": 7.224312183000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7c8ba682-69b6-4cbd-b3a5-a0608fd0f123",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T03:32:50.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DvJPP7HnqKnEzVmV2pjkdV`</summary>

```json
{
  "query": "semantic entropy probability correctness probe LLM uncertainty \"confidently wrong\" hybrid 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1f564b5-f31e-4d08-b904-003bad55730e",
  "isSidechain": false,
  "requestId": "req_011CbD7iPxWFzZfK1Lb4b44X",
  "type": "assistant",
  "uuid": "ef95c2ee-4cd0-4a3b-a954-7f0b6078047f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HVj4Lj4Cxgf9x1L3nr26J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 29964,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 29964,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 33 · 2026-05-20T03:33:08.166Z_

<details><summary>↩ Tool result · `toolu_01DvJPP7HnqKnEzVmV2pjkdV`</summary>

```text
Web search results for query: "semantic entropy probability correctness probe LLM uncertainty "confidently wrong" hybrid 2025 2026"

Links: [{"title":"Entropy Alone is Insufficient for Safe Selective Prediction in LLMs","url":"https://arxiv.org/html/2603.21172"},{"title":"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs","url":"https://arxiv.org/pdf/2406.15927"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.20026"},{"title":"Detecting hallucinations in large language models using semantic entropy - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11186750/"},{"title":"[2406.15927] Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs","url":"https://arxiv.org/abs/2406.15927"},{"title":"Predicting Program Correctness By Ensemble Semantic Entropy","url":"https://arxiv.org/html/2603.27098v1"},{"title":"Beyond Semantic Entropy: Boosting LLM Uncertainty ...","url":"https://aclanthology.org/2025.findings-acl.234.pdf"},{"title":"Addressing Uncertainty in LLMs to Enhance Reliability in Generative AI","url":"https://arxiv.org/pdf/2411.02381"}]

Based on the search results, here's what I found on this topic:

## Key Findings

Uncertainty quantification (UQ) techniques for detecting LLM hallucinations fall into two categories: entropy-based methods that treat distributional sharpness as a proxy for confidence, and correctness-based methods that learn a supervised factuality signal from model activations.

### The "Confidently Wrong" Problem

A key challenge is that hallucinations can be "confidently wrong" instances in which the output distribution lacks diversity despite being incorrect. The semantic entropy approach explicitly does not directly address situations where LLMs are confidently wrong due to systematic training issues, as these represent different underlying mechanisms requiring separate handling.

### Hybrid Approaches

Recent research has explored combining these methods. The two method types have been found to be only moderately correlated, such that simple combinations can outperform individual methods as hallucination detectors. Entropy-based and correctness-based signals are only moderately correlated, suggesting they capture complementary aspects of model uncertainty.

### 2025-2026 Developments

Semantic entropy probes (SEPs) were proposed as a cheap and reliable method for uncertainty quantification that approximates semantic entropy from hidden states of a single generation, reducing computational overhead to almost zero. Semantic Rényi entropy with UQ maximization consistently outperforms baselines, even surpassing methods reliant on supervised learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef95c2ee-4cd0-4a3b-a954-7f0b6078047f",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "3ec4f35a-4059-4de5-8acf-442d55a8194e",
  "toolUseResult": {
    "query": "semantic entropy probability correctness probe LLM uncertainty \"confidently wrong\" hybrid 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NBCxeheKjsRe1g7ff9ck1j",
        "content": [
          {
            "title": "Entropy Alone is Insufficient for Safe Selective Prediction in LLMs",
            "url": "https://arxiv.org/html/2603.21172"
          },
          {
            "title": "Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs",
            "url": "https://arxiv.org/pdf/2406.15927"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2601.20026"
          },
          {
            "title": "Detecting hallucinations in large language models using semantic entropy - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11186750/"
          },
          {
            "title": "[2406.15927] Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs",
            "url": "https://arxiv.org/abs/2406.15927"
          },
          {
            "title": "Predicting Program Correctness By Ensemble Semantic Entropy",
            "url": "https://arxiv.org/html/2603.27098v1"
          },
          {
            "title": "Beyond Semantic Entropy: Boosting LLM Uncertainty ...",
            "url": "https://aclanthology.org/2025.findings-acl.234.pdf"
          },
          {
            "title": "Addressing Uncertainty in LLMs to Enhance Reliability in Generative AI",
            "url": "https://arxiv.org/pdf/2411.02381"
          }
        ]
      },
      "Based on the search results, here's what I found on this topic:\n\n## Key Findings\n\nUncertainty quantification (UQ) techniques for detecting LLM hallucinations fall into two categories: entropy-based methods that treat distributional sharpness as a proxy for confidence, and correctness-based methods that learn a supervised factuality signal from model activations.\n\n### The \"Confidently Wrong\" Problem\n\nA key challenge is that hallucinations can be \"confidently wrong\" instances in which the output distribution lacks diversity despite being incorrect. The semantic entropy approach explicitly does not directly address situations where LLMs are confidently wrong due to systematic training issues, as these represent different underlying mechanisms requiring separate handling.\n\n### Hybrid Approaches\n\nRecent research has explored combining these methods. The two method types have been found to be only moderately correlated, such that simple combinations can outperform individual methods as hallucination detectors. Entropy-based and correctness-based signals are only moderately correlated, suggesting they capture complementary aspects of model uncertainty.\n\n### 2025-2026 Developments\n\nSemantic entropy probes (SEPs) were proposed as a cheap and reliable method for uncertainty quantification that approximates semantic entropy from hidden states of a single generation, reducing computational overhead to almost zero. Semantic Rényi entropy with UQ maximization consistently outperforms baselines, even surpassing methods reliant on supervised learning."
    ],
    "durationSeconds": 17.772011236999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ef95c2ee-4cd0-4a3b-a954-7f0b6078047f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "3ec4f35a-4059-4de5-8acf-442d55a8194e",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare uncertainty vs. trust gating for adaptive LLM explanations",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Tool call

_source line 36 · 2026-05-20T03:33:11.824Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VUQjc1K383RHiD5Qbeqpdw`</summary>

```json
{
  "query": "CoRL 2026 conference topics scope robot learning submission requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ec4f35a-4059-4de5-8acf-442d55a8194e",
  "isSidechain": false,
  "requestId": "req_011CbD7k73KfnmRYYdUTw2Qk",
  "type": "assistant",
  "uuid": "59975d24-b3f2-4b00-917c-7cdba0395b59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DrVMEvKHqp1Tf2ioGE94T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 30711,
      "output_tokens": 64,
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
          "output_tokens": 64,
          "cache_read_input_tokens": 30711,
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

_source line 37 · 2026-05-20T03:33:21.186Z_

<details><summary>↩ Tool result · `toolu_01VUQjc1K383RHiD5Qbeqpdw`</summary>

```text
Web search results for query: "CoRL 2026 conference topics scope robot learning submission requirements"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"}]

Based on the search results, here's comprehensive information about CoRL 2026:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics. CoRL 2026 is scheduled for November 10–12, 2026, in Austin, Texas.

## Topics and Scope

CoRL is a selective, single-track international conference addressing theory and practice of machine learning for robots. The conference welcomes papers in areas including:

Learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics (by behavioral cloning and/or inverse reinforcement learning), reinforcement learning for control of physical robots, and video models and latent world models for robot learning.

Additional core themes include robot manipulation (grasping, dexterous manipulation, and assembly tasks), real-world deployment (sim-to-real methods and domain randomization), and learning for control (integration with traditional control theory).

## Submission Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.

Papers are limited to 8 pages of content plus unlimited references. The paper submission deadline is May 29, 2026.

All submissions must include at least one author who agrees to serve as a CoRL reviewer and is qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59975d24-b3f2-4b00-917c-7cdba0395b59",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "ce069cd2-1dad-4356-8e2a-45396463f528",
  "toolUseResult": {
    "query": "CoRL 2026 conference topics scope robot learning submission requirements",
    "results": [
      {
        "tool_use_id": "srvtoolu_012TbakGJ5kt1BnPRJDm8UEh",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about CoRL 2026:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics. CoRL 2026 is scheduled for November 10–12, 2026, in Austin, Texas.\n\n## Topics and Scope\n\nCoRL is a selective, single-track international conference addressing theory and practice of machine learning for robots. The conference welcomes papers in areas including:\n\nLearning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics (by behavioral cloning and/or inverse reinforcement learning), reinforcement learning for control of physical robots, and video models and latent world models for robot learning.\n\nAdditional core themes include robot manipulation (grasping, dexterous manipulation, and assembly tasks), real-world deployment (sim-to-real methods and domain randomization), and learning for control (integration with traditional control theory).\n\n## Submission Requirements\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\nAll submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.\n\nPapers are limited to 8 pages of content plus unlimited references. The paper submission deadline is May 29, 2026.\n\nAll submissions must include at least one author who agrees to serve as a CoRL reviewer and is qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal."
    ],
    "durationSeconds": 9.358341951000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "59975d24-b3f2-4b00-917c-7cdba0395b59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T03:33:24.055Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018rndXvnurhHPVhRBpqTzsg`</summary>

```json
{
  "query": "selectively providing reliance calibration cues prediction human AI collaboration explanation switching 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce069cd2-1dad-4356-8e2a-45396463f528",
  "isSidechain": false,
  "requestId": "req_011CbD7m4hTVodWAJgmEbd9C",
  "type": "assistant",
  "uuid": "87b9cd4b-d90e-497a-aca0-a5955e2fa0da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yJozuEMiEFaKKoRCJWhYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 31489,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 31489,
          "cache_creation_input_tokens": 837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 837
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

_source line 39 · 2026-05-20T03:33:29.493Z_

<details><summary>↩ Tool result · `toolu_018rndXvnurhHPVhRBpqTzsg`</summary>

```text
Web search results for query: "selectively providing reliance calibration cues prediction human AI collaboration explanation switching 2024 2025"

Links: [{"title":"Selectively Providing Reliance Calibration Cues With Reliance Prediction","url":"https://arxiv.org/pdf/2302.09995"},{"title":"Selectively Providing Reliance Calibration Cues With Reliance Prediction","url":"https://arxiv.org/html/2302.09995"},{"title":"Enhancing Intuitive Decision-Making and Reliance Through Human–AI Collaboration: A Review","url":"https://www.mdpi.com/2227-9709/12/4/135"},{"title":"Selectively Providing Reliance Calibration Cues With Reliance Prediction","url":"https://escholarship.org/uc/item/8zp6g0mj"},{"title":"[2302.09995] Selectively Providing Reliance Calibration Cues With Reliance Prediction","url":"https://arxiv.org/abs/2302.09995"},{"title":"Selectively Providing Reliance Calibration Cues With Reliance Prediction | Request PDF","url":"https://www.researchgate.net/publication/368664488_Selectively_Providing_Reliance_Calibration_Cues_With_Reliance_Prediction"}]

I found relevant research on this topic. Here's what the web search revealed:

## Key Research Finding

Pred-RC is a method for selectively providing reliance calibration cues (RCCs) in human-AI collaboration. For effective collaboration between humans and intelligent agents that employ machine learning for decision-making, humans must understand what agents can and cannot do to avoid over/under-reliance, and a solution is adjusting human reliance through communication using reliance calibration cues (RCCs) to help humans assess agents' capabilities.

## How Pred-RC Works

Pred-RC uses a cognitive reliance model to predict whether a human will assign a task to an agent, and by comparing the prediction results for both cases with and without an RCC, evaluates the influence of the RCC on human reliance. Testing of Pred-RC in a human-AI collaboration task found that it can successfully calibrate human reliance with a reduced number of RCCs.

## Related 2024-2025 Research

More recently, trust and explainability research with recent work (2024–2025) is addressing trust calibration and cognitive biases in human-AI collaboration, indicating this remains an active area of study.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87b9cd4b-d90e-497a-aca0-a5955e2fa0da",
  "isSidechain": false,
  "promptId": "cea24803-62cb-4053-a5dc-86ccb15e1f79",
  "type": "user",
  "uuid": "61970c6a-e1ce-49ab-a5cd-9c94ddc76481",
  "toolUseResult": {
    "query": "selectively providing reliance calibration cues prediction human AI collaboration explanation switching 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015rABq1WMhmZo8Kxdigto13",
        "content": [
          {
            "title": "Selectively Providing Reliance Calibration Cues With Reliance Prediction",
            "url": "https://arxiv.org/pdf/2302.09995"
          },
          {
            "title": "Selectively Providing Reliance Calibration Cues With Reliance Prediction",
            "url": "https://arxiv.org/html/2302.09995"
          },
          {
            "title": "Enhancing Intuitive Decision-Making and Reliance Through Human–AI Collaboration: A Review",
            "url": "https://www.mdpi.com/2227-9709/12/4/135"
          },
          {
            "title": "Selectively Providing Reliance Calibration Cues With Reliance Prediction",
            "url": "https://escholarship.org/uc/item/8zp6g0mj"
          },
          {
            "title": "[2302.09995] Selectively Providing Reliance Calibration Cues With Reliance Prediction",
            "url": "https://arxiv.org/abs/2302.09995"
          },
          {
            "title": "Selectively Providing Reliance Calibration Cues With Reliance Prediction | Request PDF",
            "url": "https://www.researchgate.net/publication/368664488_Selectively_Providing_Reliance_Calibration_Cues_With_Reliance_Prediction"
          }
        ]
      },
      "I found relevant research on this topic. Here's what the web search revealed:\n\n## Key Research Finding\n\nPred-RC is a method for selectively providing reliance calibration cues (RCCs) in human-AI collaboration. For effective collaboration between humans and intelligent agents that employ machine learning for decision-making, humans must understand what agents can and cannot do to avoid over/under-reliance, and a solution is adjusting human reliance through communication using reliance calibration cues (RCCs) to help humans assess agents' capabilities.\n\n## How Pred-RC Works\n\nPred-RC uses a cognitive reliance model to predict whether a human will assign a task to an agent, and by comparing the prediction results for both cases with and without an RCC, evaluates the influence of the RCC on human reliance. Testing of Pred-RC in a human-AI collaboration task found that it can successfully calibrate human reliance with a reduced number of RCCs.\n\n## Related 2024-2025 Research\n\nMore recently, trust and explainability research with recent work (2024–2025) is addressing trust calibration and cognitive biases in human-AI collaboration, indicating this remains an active area of study."
    ],
    "durationSeconds": 5.432258214000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "87b9cd4b-d90e-497a-aca0-a5955e2fa0da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T03:34:12.279Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make a thorough assessment. Let me synthesize my findings and evaluate this proposal.

Key observations:

1. **Venue Mismatch (Critical)**: The user asks me to evaluate this for CoRL 2026, but CoRL is a robot learning conference. This proposal is about HCI/human-AI decision-making with LLM explanations - it has nothing to do with robotics. The proposal itself lists CHI, CSCW, FAccT as target venues. This is a fundamental mismatch that would result in desk rejection.


2. **Core Idea Assessment**: The proposal's central mechanism is comparing model uncertainty against user trust as signals for when to display dual explanations. The cited papers appear legitimate and well-chosen, with the "Adjust for Trust" work from IUI 2026 being the most relevant precedent. The approach of using model uncertainty as a backend signal rather than exposing it directly to users is a sensible design decision grounded in prior findings.
3. **Novelty Assessment**: At its core, the idea amounts to substituting model uncertainty for explicit user trust queries when deciding whether to show dual explanations.

The proposal essentially combines two established findings—that dual explanations help and that adaptive gating helps—but swaps out the gating mechanism. There's precedent for uncertainty-based gating in the literature, though applied to different contexts like classifier confidence rather than human reliance. The real contribution seems to lie more in the experimental comparison than in a fundamentally novel concept, and the logical progression from "trust measurement is impractical" to "use uncertainty instead" feels fairly straightforward.

4. **Trivial Alternative**: A more direct solution would be to simply always show dual explanations, which is already included as one of the study conditions. If dual explanations are what actually prevents overreliance, there's a question of whether selective gating adds meaningful value over this simpler baseline.

The always-on approach might perform comparably or even better, and random gating at equivalent rates could serve as a useful control to verify whether the uncertainty signal is actually informative. The core assumptions—that semantic entropy plus the PC probe will reliably detect uncertainty in general knowledge QA, and that this uncertainty signal will align with cases where dual explanations matter most—remain untested. The non-inferiority framing also means the study is really asking whether uncertainty-gating is "not substantially worse" than trust-gating rather than demonstrating superiority. The practical advantage of avoiding surveys is a valid deployment consideration, but it's more of an engineering argument than a scientific one.

6. **Significance**: The research question does address a real practical need.

The contribution is fundamentally comparative and empirical rather than introducing novel mechanisms, which could be valuable for CHI or CSCW venues but is completely misaligned with CoRL's scope. This paper has no connection to robot learning—it's purely about LLM-assisted knowledge QA with human subjects on Prolific, with no robots, physical systems, or control involved. It would face immediate desk rejection at CoRL.

Given this severe venue mismatch, the probability of acceptance at CoRL is essentially zero, though I should still evaluate the idea on its own merits and flag the fundamental misalignment.

Looking at the core idea itself, the strengths are solid: it's well-motivated by recent convergent findings, addresses a real practical limitation of trust-gated approaches, includes fairness analysis, and uses rigorous statistical design with preregistration. But the core insight is fairly straightforward—using uncertainty instead of trust surveys for gating—and the non-inferiority framing limits the novelty somewhat.

The bigger conceptual issue is that if dual explanations are truly the only effective type, there's no strong reason to gate them at all, which undermines the central premise. The connection between model uncertainty and when dual explanations help most is assumed rather than theorized. For a venue like CHI or CSCW, this would be a solid 30-40% paper—well-designed, practically relevant, but incremental. For CoRL 2026 specifically, it's essentially 0-2%—the topic mismatch is so fundamental that desk rejection is nearly certain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61970c6a-e1ce-49ab-a5cd-9c94ddc76481",
  "isSidechain": false,
  "requestId": "req_011CbD7mgC9h6CxdfxaQjBBU",
  "type": "assistant",
  "uuid": "a28015ec-ab00-45bb-a713-46f7c1b857c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Czqg3qeWvnurJL65Sg9wEb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 32326,
      "output_tokens": 5322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5322,
          "cache_read_input_tokens": 32326,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 704
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

_source line 41 · 2026-05-20T03:35:45.903Z_

Now I have sufficient information to provide my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance" (IUI 2026, arXiv 2502.13321): 
   最直接的先行工作。提出基于用户自报信任度的自适应反向解释策略，在科学问答和医学诊断任务中将不当依赖降低38%。但需要每次决策后用户填写信任量表+准确性反馈，部署成本高。该 proposal 的 Condition 3 直接复现此机制。论文确实存在且描述准确。

2. "Evaluating the False Trust engendered by LLM Explanations" (arXiv 2605.10930, May 2026): 
   确认双重解释（pro + contra）是唯一真正提高用户区分正确/错误 LLM 输出能力的解释类型，其他类型仅增加接受率。论文存在，描述准确，是 proposal 的关键动机之一。

3. "To Rely or Not to Rely?" (Bo et al., CHI 2025, arXiv 2412.15584): 
   测试三种干预措施，发现 Uncertainty Highlighting 直接向用户展示不确定性反而加剧算法厌恶。论文存在且描述准确。Proposal 利用此发现论证"后端使用不确定性而非前端展示"的设计合理性。

4. "From Text to Trust" (Li et al., CHI 2025, arXiv 2502.11919): 
   使用动态规划框架+学习的人类行为模型来选择性展示 LLM 生成的特征分析。需要先前交互数据（冷启动问题），操作对象为表格数据特征分析而非自然语言双重解释。论文存在，描述准确。

5. "Uncertainty Gating for Cost-Aware Explainable AI" (arXiv 2603.29915): 
   使用认知不确定性来门控解释方法（选择不同的 XAI 方法），但针对传统 ML 分类器而非 LLM 辅助决策中的人类过度依赖。机制类似但应用域不同。

6. "Unequal Uncertainty" (arXiv 2508.07872): 
   首次对基于不确定性的算法干预进行社会技术+法律分析，指出不确定性阈值可能对代表性不足的群体产生不成比例的影响。论文存在，proposal 的公平性分析 (RQ3) 直接受此启发。

7. "Entropy Alone is Insufficient for Safe Selective Prediction in LLMs" (arXiv 2603.21172): 
   证明语义熵存在"自信但错误"区域，结合 Probability of Correctness probe 显著提高可靠性。Proposal 的混合不确定性估计器直接来源于此。

8. "Semantic Entropy Probes" (Kossen et al., arXiv 2406.15927): 
   从单次生成的隐藏状态近似语义熵，大幅降低计算成本。Proposal 将其作为 Phase 1 的备选方案。

- 调研总结: 这个领域（LLM 辅助决策中的自适应解释/干预）在 2024-2026 年非常活跃，"什么时候该给什么样的解释"是一个被广泛关注的问题。核心先行工作——信任门控 (IUI 2026) 和双重解释有效性 (2605.10930)——都是 2026 年的最新成果，proposal 的定位是对这些工作的自然组合与实用性改进。但"用模型不确定性替代用户信任度作为门控信号"这个想法本身是一个相当直觉化的工程替代，而非概念层面的突破。


【Trivial Alternative 检验】:

**存在严重的 trivial alternative 威胁：Always-On Dual Explanation (Condition 2)。**

如果 2605.10930 已经证明双重解释是唯一真正有效的解释类型，那么最简单的策略就是**始终展示双重解释**——不需要任何门控信号、不需要不确定性估计、不需要信任量表、零额外部署成本。Proposal 确实包含了这个条件作为 baseline (Condition 2)，但这恰恰暴露了核心逻辑的薄弱：

- 如果 always-on ≈ uncertainty-gated，那门控的价值存疑（唯一可能的 argument 是降低认知负荷，但这需要 H3 positive 来支撑，而这本身是一个较弱的预期效应）
- 如果 always-on > uncertainty-gated，那 uncertainty-gating 就输给了 trivial baseline
- 只有 uncertainty-gated > always-on（选择性触发比始终触发更好）才能充分证明门控的价值，但 proposal 并没有将此设为核心假设

增量价值主要落在**实用性层面**（不需要用户问卷、首次交互即可用）相对于 trust-gating 的优势，以及**认知负荷**层面相对于 always-on 的优势。这些是工程/部署论证，不是科学洞见。


【前提假设检验】:

核心逻辑链中有以下未经验证的关键假设：

1. **"模型不确定性高 ≈ 用户最需要双重解释的时刻"**——这是整个 idea 的核心假设，但没有理论或实证支撑。模型不确定性高意味着模型可能出错，但用户过度依赖的原因是多方面的（过度信任、认知懒惰、锚定效应等），不确定性高的题目不一定是用户最容易过度依赖的题目。信任门控至少直接测量了用户状态，而不确定性门控假设模型状态可以替代用户状态——这个替代性本身就是需要被验证的。

2. **非劣效性框架的预设立场**——H2 使用 TOST 检验"不确定性门控不劣于信任门控"（Cohen's d = 0.35 等价边界），这意味着 proposal 的"最佳结果"仅仅是"大致一样有效"。如果一个研究的天花板就是"我的新方法和旧方法差不多"，其学术贡献主要在实用性而非科学发现。

3. **假设 Qwen3-30B-A3B 的混合不确定性估计器能在通用知识问答上达到 AUROC ≥ 0.75**——虽然 proposal 设置了 fallback 方案，但如果这个阈值达不到，整个研究的基础就不存在。2505.23854 已经指出 LLM 在知识密集型任务上的校准比推理任务差。

4. **假设"准确性反馈"这个实验条件的引入不会严重扭曲生态效度**——proposal 自己承认准确性反馈在部署中罕见，但所有条件都提供了反馈。这意味着 uncertainty-gating 在实验中的相对优势可能被低估（如 proposal 所述），但也可能意味着实验结果对真实部署场景的外推存在系统性偏差。


【3 维度打分】:

1. **Novelty: 弱-中** — 核心贡献是"用模型不确定性替代用户信任度作为双重解释的门控信号"。这是一个自然、直觉化的工程替代，而非概念突破。
   - "Adjust for Trust" (IUI 2026) 已建立自适应门控框架
   - "Uncertainty Gating for Cost-Aware XAI" (2603.29915) 已在 ML 分类器上使用不确定性做解释门控
   - Li et al. (CHI 2025) 已建立自适应解释选择框架
   - 本 proposal 的增量是将"不确定性作为后端门控"应用到"双重解释"场景——组合性贡献而非原创性贡献
   - "后端使用 vs 前端展示"不确定性的区分有一定见解，但更像是工程设计选择而非理论洞见（Bo et al. 的发现已经隐含了这个方向）
   - 如果核心发现是 positive（不确定性门控 ≈ 信任门控），审稿人很可能说 "I would have guessed this"——用模型内部信号替代人工问卷直觉上是合理的

2. **Significance: 中** — 研究问题在 HCI/AI-assisted decision making 领域有实际价值：部署中如何无侵入地实现自适应解释是一个真实痛点。
   - 但对领域的推动是渐进式的：主要贡献是实用性改进（去掉问卷）而非新的理解或理论
   - 公平性分析 (RQ3) 是有意义的补充，但作为二级贡献，不足以独立支撑论文
   - 非劣效性框架限制了学术影响力的上限——即使所有假设成立，结论也只是"可以用不确定性替代信任度，效果差不多"
   - 对 NLP/CL 领域的贡献有限，更多是 HCI 贡献
   - **关键问题：这是一篇 CHI/CSCW 论文，不是 CoRL 论文**（见下文）

3. **Related Work: 强** — 对已有工作的覆盖非常充分且准确。
   - 所有核心引用（2605.10930, 2502.13321, 2412.15584, 2502.11919, 2603.21172, 2508.07872）均经验证存在且描述准确
   - 差异化定位清晰：明确区分了与 "Adjust for Trust"（门控信号不同）、Li et al.（任务域和方法不同）、Bo et al.（前端展示 vs 后端门控）的差异
   - 对 uncertainty quantification 文献的覆盖也足够（semantic entropy, PC probes, calibration）
   - 对最新 2025-2026 工作的跟踪及时


【概率估计】: [0% - 3%] 中位 1%

【估计理由】: 
**概率估计受到致命的 venue mismatch 约束。** CoRL (Conference on Robot Learning) 是一个聚焦机器人学习的单轨会议，核心话题包括：机器人感知与控制的学习表征、模仿学习、强化学习、sim-to-real、机器人操作等。本 proposal 是一项纯 HCI 用户研究，涉及 LLM 辅助知识问答中的解释设计和人类过度依赖——**与机器人学习没有任何交集**。没有物理机器人、没有控制策略、没有感知系统、没有仿真环境。即使 idea 本身在 HCI 领域有一定价值，投稿 CoRL 也几乎必然被 desk rejection。

如果抛开 venue mismatch 纯评 idea 质量（假设投稿 CHI/CSCW），概率估计约为 **[20% - 35%] 中位 27%**：idea 方向正确且有实际需求，但核心贡献是组合性/工程性的而非原创性的，非劣效性框架限制了学术影响力上限，且面临 always-on dual explanation 这一 trivial alternative 的严重威胁。Novelty 维度是主要限制因素。

【主要风险】:
1. **致命的 venue 不匹配**：CoRL 是机器人学习会议，本 proposal 是 HCI 用户研究，与 CoRL 的 scope 完全不重叠，几乎确定被 desk reject。
2. **Trivial alternative 威胁**（idea 层面）：Always-on dual explanation 是一个零成本的替代方案，如果其效果接近或优于 uncertainty-gating，则门控机制的增量价值难以成立。核心创新沦为"差不多一样好但更方便"的实用性论证，这对顶会 novelty 要求而言不够。
```

**补充说明：**

该 proposal 自身列出的目标 venue 是 CHI 2027、CSCW 2027、FAccT 2027——这些都是合理的 venue 选择。但用户询问的是 **CoRL 2026** 的中稿潜力，这存在根本性的 scope 不匹配。建议将投稿目标调整回 proposal 原始规划的 HCI 会议。

即使在 CHI/CSCW 的语境下，idea 的核心瓶颈仍然是 **novelty 不够强**：核心贡献是一个直觉化的工程替代（用不确定性替代信任问卷），非劣效性框架进一步削弱了学术影响力上限。要提升中稿概率，需要在 idea 层面找到超越 "practical alternative" 的 deeper insight——例如，不确定性门控和信任门控在何种条件下会 diverge（不仅仅是"差不多"），或者为什么模型不确定性能捕捉到用户信任度捕捉不到的过度依赖模式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a28015ec-ab00-45bb-a713-46f7c1b857c0",
  "isSidechain": false,
  "requestId": "req_011CbD7mgC9h6CxdfxaQjBBU",
  "type": "assistant",
  "uuid": "0610fdae-690d-46b4-9dc1-34228149b871",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Czqg3qeWvnurJL65Sg9wEb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 32326,
      "output_tokens": 5322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5322,
          "cache_read_input_tokens": 32326,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 704
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "0610fdae-690d-46b4-9dc1-34228149b871",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare uncertainty vs. trust gating for adaptive LLM explanations",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Makin…",
  "leafUuid": "0610fdae-690d-46b4-9dc1-34228149b871",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare uncertainty vs. trust gating for adaptive LLM explanations",
  "sessionId": "f0a97c89-af9e-4a64-bfe0-0b468fdc3f88"
}
```

---
