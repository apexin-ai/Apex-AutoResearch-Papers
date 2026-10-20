# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/365e0176-961c-40cc-a37e-0044c1093d8b.jsonl`
- **Structured JSON:** [`21dcf758d0dc242f9f2d.json`](../../sessions/21/21dcf758d0dc242f9f2d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:18:27.938Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:18:27.938Z",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"DemoCalib: Data-Efficient Dialect-Behavioral Calibration of LLM User Simulators for Fair Agentic Evaluation\",\n  \"core_problem\": \"LLM user simulators exhibit systematic behavioral miscalibration for dialectal speaker groups in agentic task-completion settings: they are excessively cooperative, over-polite, and question-asking at rates that diverge sharply from real users in groups like AAVE and Indian English speakers. Seshadri et al. (AFAA@ICLR 2026; arXiv 2601.17087) document that AAVE speakers ask questions in only ~10% of turns versus 18.8% for LLM simulators, use politeness markers at ~19.7% versus 39.2%; Indian English speakers (India-based Prolific participants, 18–34 age group) show nearly identical behavioral profiles — 9.9% question rate and 20.1% politeness rate — both groups sharply divergent from simulator baselines. This behavioral miscalibration is not merely noisy: Seshadri et al. report a concrete downstream consequence — AAVE real users achieve approximately 39% agent task-completion rate versus ~49% for SAE speakers; India-based participants achieve approximately 46.2%. If this gap is partly attributable to simulator over-cooperativeness producing artificially inflated success rate estimates for dominant-group speakers, then calibrated simulators should produce success rate estimates closer to the real-user baselines. Seshadri et al. demonstrate in Appendix A.6 that a 'minimal intervention' behavioral constraint prompt (BCP) limiting politeness to 'at most one or two times across the entire conversation' shifts 11 of 18 tasks' difficulty bins and reduces aggregate simulated success rate from 50.0% to 46.7% — partially improving calibration for AAVE, Indian, and Kenyan groups. However, the BCP constrains only politeness frequency, leaving the question-asking rate gap (18.8% simulated vs. ~10% real for both AAVE and Indian English) entirely unaddressed; aggregate success rate remains at 46.7%, far above the AAVE real-user baseline of ~39%. No method exists to adapt a general-purpose LLM simulator's full behavioral distribution to match the empirically observed behavioral profile of a target dialectal group given a small reference sample — addressing both question-asking and politeness dimensions without degrading calibration for other groups — and no prior work has validated such adaptation against downstream agent evaluation consistency. Importantly, because assembling a genuine Prolific reference corpus requires IRB approval and participant recruitment (minimum 6–7 weeks), the framework must be demonstrable via a synthetic pilot that uses empirically-documented behavioral rates from published studies as calibration targets — enabling proof-of-concept results within a typical submission window, with full human validation as a planned follow-up contribution.\",\n  \"opportunity\": \"'Lost in Simulation' (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) conducted a Prolific-recruited user study (~40 participants per group from the US, India, Kenya, Nigeria) running the full τ-Bench protocol, and documented sharp behavioral gaps between real users and LLM simulators. Critically, Table 6 of Seshadri et al. provides group-level behavioral rate breakdowns for both AAVE and Indian English speakers: AAVE speakers asked questions in only ~10% of turns versus 18.8% for LLM simulators; politeness marker usage was ~19.7% for AAVE real users versus 39.2% for simulators. India-based participants (18–34 age group, the only Indian age cohort recruited due to Prolific availability constraints) asked questions in 9.9% of turns and used politeness markers in 20.1% of turns — strikingly similar to AAVE rates and equally divergent from the 18.8%/39.2% simulator baseline. This convergence of AAVE and Indian English rates, both sharply below simulator baselines, provides a strong empirical foundation for a two-group calibration study: both groups have published target rates from the same study using the same methodology, enabling a direct comparison of calibration difficulty and transferability. Table 3 reports per-group agent success rates: AAVE real users achieved approximately 39% agent task-completion versus approximately 49% for SAE real users; India-based participants achieved approximately 46.2%. These per-group success rates anchor the proxy downstream evaluation: if behavioral miscalibration is a primary driver of biased success rate estimates, calibrated simulators should produce estimates closer to these real-user baselines.\\n\\nCritically, Seshadri et al. also document (Appendix A.6) a 'minimal intervention': a behavioral constraint prompt (BCP) limiting politeness to 'at most one or two times across the entire conversation' shifts 11 of 18 tasks' difficulty bins and reduces aggregate simulated success rate from 50.0% to 46.7%. The BCP improves simulator calibration for AAVE, Indian, and Kenyan groups but worsens it for SAE and Nigerian participants — demonstrating that a universal politeness constraint is not group-neutral and that single-dimension prompting falls short of full calibration. The BCP constrains only politeness; it leaves the question-asking rate divergence (18.8% simulated vs. ~10% real) entirely unaddressed, and aggregate success rate at 46.7% remains far above the AAVE real-user baseline of ~39%. The Indian English target (~46.2%) is closer to BCP's 46.7% aggregate, but this proximity is coincidental: a group-specific Indian English calibration targeting 9.9% question rate and 20.1% politeness rate requires matching both behavioral dimensions simultaneously and without degrading other groups. DemoCalib extends from BCP's single-dimension prompting to a full data-efficient behavioral distribution matching framework — addressing both dimensions, providing a concrete sample complexity characterization, and enabling group-specific calibration without universal constraint.\\n\\nAVAVE participants also encountered argument errors at 45.8% versus 32.2% for simulators; the Indian English group showed an Expected Calibration Error (ECE) of 18.9% versus 13.0% for SAE — confirming simulator miscalibration is worst for both groups. These are large effect sizes in agentic task language, far exceeding the ~1.5% demographic-variance figure from SCOPE (arXiv 2601.07110), which measured variance in survey opinion responses, not language-production behavior during task completion. Importantly, the 9-point agent-success-rate variation documented in 'Lost in Simulation' is primarily a model-to-model spread across 31 different LLM simulators; the demographic disparity is a secondary finding: simulated users are differentially unreliable proxies, performing worst for AAVE and Indian English speakers, with disparities compounding with age. 'Mind the Sim2Real Gap' (arXiv 2603.11245, CMU, March 2026) corroborates simulator over-cooperativeness across 451 real participants in aggregate (no per-dialect breakdown) but provides no adaptation method and has no dialect-group-specific rate data. Neither study has released participant interaction logs publicly: Seshadri et al. include no data availability statement or GitHub repository in the paper; 'Mind the Sim2Real Gap' likewise omits a data release. The CC-BY 4.0 license on the Seshadri et al. paper applies to the paper text only, not to participant interaction data — reuse of participant traces requires a separate formal data-sharing agreement and likely participant reconsent for secondary use, a process requiring 4–8 weeks. MirrorBench (arXiv 2601.08118) provides metrics for evaluating human-likeness (MATTR, HD-D, GTEval) without any training signal to produce calibrated simulators. The LLM-based conversational user simulation survey (arXiv 2604.24977) identifies demographic calibration as an open challenge. 'Toward Scalable Verifiable Reward: Proxy State-Based Evaluation for Multi-turn Tool-Calling LLM Agents' (arXiv 2602.16246) demonstrates LLM-driven proxy evaluation for τ-bench-style agentic tasks with >90% human-judge agreement, providing methodological grounding for the proxy downstream evaluation component. Crucially, the published empirical rates from Seshadri et al. Table 6 — AAVE: 10% question rate, ~19.7% politeness rate; Indian English (18–34): 9.9% question rate, 20.1% politeness rate; simulator: 18.8%, 39.2% — provide concrete, IRB-free calibration targets that directly parameterize synthetic reference corpus construction and DPO contrastive pair generation for both groups. The 18–34 age constraint on Indian English participants (a Prolific recruitment limitation in Seshadri et al., not a design choice) means the calibration targets represent younger adult Indian English speakers; age-stratified calibration for Indian English across broader demographics is a planned extension. This synthetic pilot validates the calibration pipeline; a full Prolific human-validation study is planned as a follow-on contribution. Seshadri et al.'s Prolific methodology (racial/ethnic + dialect self-identification screening) has been validated for recruiting AAVE speakers in LLM user studies (corroborated by Black LLMirror at CHI 2026), making the planned human validation study concrete and feasible at ~$1,200–2,200 (~120–180 participants × $7–10 each including platform fees). DialectLLM/MDial (arXiv 2601.22888, KAIST and Amazon, January 2026; updated May 2026) is used as a source of Indian English linguistic transformation rules for synthetic corpus generation in Phase 1 and as Baseline (e) for the Indian English group.\",\n  \"landscape\": \"The user simulation landscape centers on τ-Bench and related agentic task benchmarks. 'Lost in Simulation' (AFAA Workshop @ ICLR 2026; arXiv 2601.17087) and 'Mind the Sim2Real Gap' (CMU, 2026) both quantify simulator-to-human gaps but provide no adaptation methods and have not released participant data. MirrorBench evaluates human-likeness without producing calibrated simulators. Liu et al. (arXiv 2605.02624, May 2026) propose 'realsim,' an 8-dimensional framework for evaluating user simulation quality across communicative functions, user states, and message surface forms, finding that simulated users systematically underrepresent communication frictions that real users introduce; unlike DemoCalib, it focuses on evaluation metrics rather than adaptation methodology, and does not address dialect-group behavioral calibration.\\n\\nA critical related method emerges from Seshadri et al. themselves: in Appendix A.6, the authors demonstrate a 'Behavioral Constraint Prompt' (BCP) that limits politeness to 'at most one or two times across the entire conversation.' The BCP reduces aggregate simulated success rate from 50.0% to 46.7% and shifts 11 of 18 tasks' difficulty bins, improving calibration for AAVE, Indian, and Kenyan groups while worsening it for SAE and Nigerian participants. The BCP is a zero-compute single-dimension prompting intervention that partially achieves DemoCalib's goal. Its limitations are threefold: (1) it constrains only politeness frequency, leaving the question-asking rate divergence (18.8% simulated vs. ~10% real for both AAVE and Indian English) entirely unaddressed; (2) aggregate success rate at 46.7% remains far above the AAVE real-user baseline (~39%), indicating that politeness-only calibration is insufficient for the hardest miscalibration cases; (3) it applies a universal constraint affecting all groups, degrading calibration for already well-calibrated groups (SAE, Nigerian), whereas DemoCalib provides group-specific calibration. DemoCalib includes BCP as Baseline (f) — extended to constrain both politeness and question rate explicitly — to provide a direct comparison between zero-compute prompting and data-efficient training. This comparison is informative regardless of outcome: if BCP (extended) achieves comparable behavioral rate matching without training, DemoCalib identifies the condition under which prompting suffices; if DPO outperforms extended BCP on held-out test traces and/or proxy downstream evaluation, the paper demonstrates added value of data-efficient training for multi-dimensional behavioral calibration.\\n\\nSeveral concurrent works partially address related problems but do not close the specific gap:\\n\\nUserLM-R1 (arXiv 2601.09215, Meituan and collaborating Chinese universities — Meituan, Peking University, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences, Dalian University of Technology — January 2026): The current frontier in user simulation model training. Trains user LMs with multi-reward RL combining rule-based (format, field verification) and rubric-based (reasoning quality, strategic alignment, conversational initiative) reward signals, using Qwen-3 8B/32B base models with adaptive user profiles that combine static persona traits (background, personality, expression style) and dynamic scenario-specific goals. Trained on 90,000 user profiles from AlignX and 450 task SOPs across 6 business scenarios; achieves strong performance particularly on adversarial agent-interaction tasks. Two key distinctions from DemoCalib: (1) UserLM-R1 is explicitly trained on Chinese-language samples with no English dialect or demographic calibration, and does not address the simulator-to-human behavioral gap for any dialect group; (2) it targets strategic reasoning capability and cross-domain generalization rather than matching the behavioral distribution of a specific real dialectal group in English agentic settings. UserLM-R1 is included as Baseline (c): zero-shot with an AAVE/Indian English dialect system prompt, testing whether RL-trained adaptive persona and reasoning capability — without explicit behavioral calibration — closes the miscalibration gap documented by Seshadri et al.\\n\\nUserLM-8b ('Flipping the Dialogue,' arXiv 2510.06552, NAACL 2025, Microsoft Research): Fine-tunes an 8B model on WildChat for general-conversation user simulation with no dialect-group targeting, no sample complexity analysis, and no downstream agent evaluation consistency metric.\\n\\nDialectLLM/MDial (arXiv 2601.22888, KAIST and Amazon, January 2026; updated May 2026): Rule-based framework for generating dialect-accurate multi-turn dialogues across 9 English dialects (SAE/US, Australian, British, Canadian, Indian, Irish, Nigerian, Philippine, Scottish) using linguist-curated lexical/orthographic/morphosyntactic transformation rules applied to SAE seed dialogues. Produces DialectLLM-Bench with 50k+ dialogues and 97k+ QA pairs; evaluation of 17 LLMs shows frontier models achieve under 70% dialect accuracy. Three critical distinctions from DemoCalib: (1) DialectLLM targets linguistic form accuracy — surface dialect features in generated text — while DemoCalib targets behavioral interaction dynamics (question rates, politeness frequency, repair patterns) in multi-turn agentic task flows; (2) DialectLLM generates generic conversational exchanges, not agentic task-completion traces under τ-Bench protocol with tool-use and policy constraints; (3) DialectLLM applies rule-based SAE-to-dialect transformation without any feedback loop for behavioral distribution matching. Note: DialectLLM covers Indian English but does not include AAVE among its 9 dialects (Nigerian English is present; AAVE as a US variety requires separate feature sources such as CORAAL and AAVENUE). DialectLLM-conditioned generation is included as Baseline (e) for the Indian English group: applying its IN transformation rules to uncalibrated simulator outputs tests whether rule-based linguistic form calibration alone suffices versus DemoCalib's behavioral distribution matching.\\n\\nThe PAL framework (arXiv 2511.10215, TACL): Uses DPO for persona-conditioned dialogue generation, optimizing persona alignment in general dialogue rather than matching the behavioral distribution of a specific real dialect group in agentic task settings.\\n\\nPersoDPO (arXiv 2602.04493, February 2026): Applies DPO with multi-LLM automatic evaluation signals to construct preference pairs for persona-consistent dialogue generation, optimizing for coherence, personalization, and instruction adherence on the FoCus conversational dialogue benchmark. Three distinctions from DemoCalib: (1) PersoDPO targets generic persona consistency (narrative coherence and identity alignment) rather than measurable behavioral rate matching (question-asking frequency, politeness marker frequency) for specific dialect groups; (2) it evaluates on open-domain conversational dialogue rather than multi-turn agentic task-completion under τ-Bench protocol with tool-use and policy constraints; (3) it does not address the simulator-to-human behavioral gap for any dialect group and includes no dialect or demographic variation analysis. PersoDPO is methodologically complementary: DemoCalib extends preference optimization from persona coherence to empirically grounded behavioral rate calibration in agentic evaluation settings.\\n\\nSocrates/SocSci210 (arXiv 2509.05830, EMNLP 2025, Stanford): Fine-tunes on 2.9M social science experiment responses — a survey/experiment domain rather than multi-turn agentic task completion, and with orders of magnitude more training data than DemoCalib's small-sample setting.\\n\\nPopulation-Aligned Persona Generation (arXiv 2509.10127, September 2025, Microsoft Research): Methodologically closest prior work — uses importance sampling to align LLM persona distributions to Big Five psychometric reference distributions for social simulation. Operates on self-report survey data (not agentic interaction traces), targets population-level psychometric distributions (not dialect-group behavioral fingerprints), and does not validate against downstream task evaluation consistency.\\n\\nHUMAINE (arXiv 2603.04409, ICLR 2026): Stratifies the evaluation dataset across 22 demographic groups, calibrating what we measure rather than how we simulate.\\n\\nSCOPE (arXiv 2601.07110): Argues demographic-only personas explain ~1.5% of variance in survey response similarity — a finding about opinion responses, not the language-production behavioral patterns (question rate, politeness frequency, repair sequences) that differ substantially between dialect groups in agentic task completion.\\n\\nHaq and Saldías (arXiv 2604.21152, April 2026) study implicit dialect signals (AAVE, Singlish) versus explicit demographic profiles in LLM responses, documenting a 'dialect jailbreak' phenomenon where implicit dialect cues reduce model refusal rates toward near-zero — an input-side bias in how LLMs respond to dialect users, distinct from DemoCalib's simulator-side behavioral calibration, but corroborating that implicit dialect features produce measurable and consequential LLM behavioral differences.\\n\\nToward Scalable Verifiable Reward (arXiv 2602.16246, 2026): Introduces proxy state-based evaluation for multi-turn tool-calling agents using LLM-driven state tracking and goal-completion judges, achieving >90% human-judge agreement. Provides methodological grounding for the proxy downstream evaluation component of DemoCalib but does not address dialect-group behavioral calibration.\\n\\nThe gap: given a small reference corpus or empirically-documented target behavioral profile for a specific dialect group, no existing method closes the loop from behavioral fingerprint extraction → simulator adaptation → proxy downstream agent evaluation consistency validation, with quantified sample complexity, in the τ-Bench agentic evaluation context. Seshadri et al.'s BCP (Appendix A.6) represents the strongest prior intervention — zero-compute, sourced from the primary motivating paper — but its single-dimension (politeness-only) scope and universal (non-group-specific) application demonstrate that it falls short of the full calibration problem DemoCalib addresses.\",\n  \"approach\": \"DemoCalib is a data-efficient framework that adapts a general-purpose LLM simulator (Qwen 2.5 7B-Instruct as primary base model, selected for strong instruction-following capability, extensive open-weight documentation, and active HuggingFace community; Qwen 3.5 9B evaluated as a secondary ablation, contingent on publicly released weights being available on HuggingFace at time of submission) to match the behavioral distribution of a target dialect group. The framework operates in two phases: a proof-of-concept synthetic pilot (primary, 16-day feasible, IRB-free) and a planned human validation study (follow-up, providing downstream agent evaluation consistency validation and a genuine reference corpus contribution).\\n\\n**Phase 1 — Synthetic Pilot (Primary, Submission-Ready):**\\n\\nTarget behavioral profiles for each dialect group are directly specified from published empirical rates in Seshadri et al. (AFAA Workshop @ ICLR 2026; arXiv 2601.17087), Table 6: AAVE (question rate = 10% per turn, politeness marker rate = ~19.7%); Indian English (question rate = 9.9% per turn, politeness marker rate = 20.1%; India-based Prolific participants, 18–34 age group — the only Indian English cohort recruited in Seshadri et al. due to platform availability constraints, so calibration targets represent younger adult speakers; age-stratified Indian English calibration is a planned extension); SAE control (uncalibrated simulator baseline rates of 18.8% question rate, 39.2% politeness rate, from the same study).\\n\\n**Two-Group Design: Testing Cross-Feature Calibration Under Matched Behavioral Targets.** AAVE (10%/~19.7%) and Indian English (9.9%/20.1%) share nearly identical published calibration targets. Rather than treating this as a limitation, the two-group design explicitly tests two questions distinct from differential behavioral fingerprint matching: (a) whether DemoCalib can achieve matched behavioral targets across groups that differ substantially in linguistic surface features — AAVE calibration draws on CORAAL/AAVENUE morphosyntactic features (copula deletion, habitual be, negative concord, preverbal aspect marking), while Indian English calibration uses DialectLLM IN transformation rules (retroflex markers, topic-prominent constructions, distinct lexical items) — and (b) whether calibration difficulty, sample complexity curve, and method effectiveness (DPO vs. retrieval vs. BCP prompting) differ across groups despite identical numerical targets. If calibration converges at different rates or requires different N for AAVE vs. Indian English despite identical targets, this indicates that surface linguistic feature complexity mediates calibration difficulty — a theoretically important finding about the coupling between form and behavioral adaptation. The Indian English group additionally enables unique comparison with Baseline (e) (DialectLLM-conditioned generation), which has no AAVE analogue. This framing is stated explicitly in the paper to preempt the concern that a two-group study with matched targets only tests one behavioral profile: the multi-group contribution is cross-feature calibration under shared targets, not differential fingerprint matching.\\n\\nA synthetic reference corpus is generated for each group using a dialect-conditioned LLM (GPT-4o or Llama-3.1 70B) prompted with dialect-appropriate system instructions on τ-Bench retail tasks: AAVE instructions are informed by CORAAL-documented morphosyntactic features and AAVENUE benchmark patterns; Indian English instructions use DialectLLM/MDial's (KAIST and Amazon) Indian English transformation rules. This produces 100–200 τ-Bench interaction traces per group (~300–600 total). Generated turns are then post-processed to match target behavioral rates (e.g., excess question-asking turns identified by a simple utterance-type classifier and replaced with non-question continuations until the target rate is achieved). This post-processing step is critical: it prevents the circularity of using LLM-generated corpus to calibrate LLM behavioral rates, since the LLM generator itself exhibits the same over-questioning and over-politeness miscalibration being corrected. Linguistic texture comes from the dialect-conditioned generator; behavioral rates are independently grounded in Seshadri et al.'s published human data.\\n\\nPost-processing coherence constraint: Each replacement turn must pass a slot-filling consistency check against the task state before being accepted. Specifically, (1) the replacement must not introduce an open question that the agent has already answered in the preceding turn, and (2) it must reference only task variables (product IDs, order numbers, return policies) that have been established in the dialogue history up to that point. This check is implemented as a regex-based slot tracker operating on the τ-Bench structured task state, requiring no additional model calls and adding negligible latency to the post-processing pipeline. Replacement candidates failing this check are discarded and regenerated until a coherent candidate is found or the turn is flagged for manual review.\\n\\nThe entire generation and post-processing pipeline takes 1–2 days via API calls at ~$20–50 in API costs.\\n\\nBehavioral fingerprints are extracted from each group's reference traces: question-asking rate per turn, politeness marker frequency (detected via a curated lexicon), turn-length histograms, lexical diversity (MATTR, HD-D), clarification-request frequency, and error-repair patterns. As a validity criterion (not a completed finding), the fingerprint extraction is designed so that fingerprints from the synthetic reference traces should separate dialect groups at >50% 3-class classification accuracy; this threshold confirms that the synthetic corpus exhibits sufficient behavioral divergence to ground calibration. If this criterion is met, the calibration training proceeds as planned. If not, a two-stage contingency applies: (a) First fallback — increase dialect feature density in the generation prompt using stricter CORAAL-derived morphosyntactic constraints for AAVE and more restrictive DialectLLM IN transformation rules for Indian English, then regenerate the corpus and re-evaluate fingerprint classification; (b) Second fallback — if the criterion still fails after corpus revision, reduce the behavioral gap being matched from the full dialect–SAE divergence to the most robustly reproducible subset (e.g., politeness marker rate only, which shows the largest absolute divergence), report partial calibration results, and frame the incomplete fingerprint separation as a substantive finding about the limits of current dialect-conditioned LLM generation — a publishable negative result about the circularity constraint in synthetic dialect calibration. This contingency turns a binary pass/fail into a graceful degradation with interpretable findings at each stage.\\n\\nMeeting the primary validity criterion demonstrates that behavioral fingerprints in agentic task data capture group differences beyond SCOPE's 1.5% survey-response variance figure — because the behavioral rate targets were independently specified from human data rather than derived from the LLM generator.\\n\\nTwo calibration strategies are compared: (1) DPO fine-tuning with contrastive pairs opposing reference group turns against uncalibrated simulator outputs on identical task prompts, implemented with LoRA (rank=64) for data-efficient adaptation; (2) retrieval-augmented few-shot conditioning injecting the k most behaviorally similar reference turns as in-context demonstrations at inference time, requiring no gradient updates. Six baselines:\\n\\n(a) Uncalibrated Qwen 2.5 7B-Instruct with demographic system prompt (HUMAINE-style persona prompting) — the generic demographically-aware prompting baseline;\\n\\n(b) UserLM-8b conditioned on dialect-group system prompt;\\n\\n(c) UserLM-R1 (Qwen-3 8B, from Meituan and collaborating Chinese universities, if weights are publicly available at submission time; otherwise approximated as zero-shot Qwen-3 8B with identical dialect system prompt) with AAVE/Indian English dialect system prompt — testing whether RL-trained adaptive persona and reasoning capability without explicit behavioral calibration closes the gap;\\n\\n(d) Population-Aligned Persona Generation adapted to use behavioral fingerprints instead of Big Five traits for importance sampling;\\n\\n(e) DialectLLM-conditioned generation (KAIST and Amazon; arXiv 2601.22888) applied to τ-Bench interactions for the Indian English group only (DialectLLM does not cover AAVE), testing whether rule-based linguistic form calibration alone suffices versus DemoCalib's behavioral distribution matching;\\n\\n(f) Behavioral Constraint Prompt (BCP) — Qwen 2.5 7B-Instruct prompted with explicit per-turn behavioral rate targets derived directly from Seshadri et al. Table 6: 'Ask questions in approximately 10% of turns. Use politeness markers (e.g., please, thank you, sorry) in approximately 20% of turns.' Applied independently to each dialect group (AAVE and Indian English). This extends the 'minimal intervention' documented in Seshadri et al. Appendix A.6 — which constrained only politeness to 'at most one or two times across the entire conversation' and reduced aggregate success rate from 50.0% to 46.7% — to a full two-dimensional behavioral rate constraint. BCP is zero-compute (no training, no data), and is the critical comparison point for assessing whether DemoCalib's DPO fine-tuning adds value over simply encoding target rates in the system prompt. It is also the most natural baseline a reviewer familiar with Seshadri et al. would expect. Expected outcome: BCP achieves partial behavioral rate compliance on both dimensions but produces turns with degraded pragmatic coherence — abrupt non-questions that disrupt task flow — because instruction-following for rate constraints does not guarantee coherent substitution. DemoCalib's DPO/retrieval approach learns the underlying behavioral distribution, producing calibrated turns that maintain agentic pragmatic function. The comparison is informative regardless of direction: if BCP achieves comparable rate matching, DemoCalib identifies the condition under which prompting suffices; if DPO outperforms BCP on fingerprint match rate and/or proxy downstream evaluation, the paper demonstrates the added value of data-efficient training. Note: the Seshadri et al. BCP (politeness-only) worsens calibration for SAE and Nigerian groups while improving for AAVE, Indian, and Kenyan — demonstrating that universal behavioral constraint prompting is not group-neutral. DemoCalib's group-specific calibration avoids this: it targets AAVE and Indian English specifically without requiring a universal constraint applied to all groups.\\n\\nCalibration quality is validated via MirrorBench metrics (MATTR, HD-D, GTEval), behavioral fingerprint match rate (do calibrated outputs achieve target question/politeness rates on held-out synthetic test traces?), and task-completion preservation (does calibration maintain agentic task functionality?). Sample complexity is characterized by varying reference corpus size from N=10 to N=100 synthetic dialogues, reporting the minimum N needed to achieve fingerprint match within a target threshold — giving practitioners a concrete sample requirement curve for any dialect group.\\n\\n**Proxy Downstream Evaluation (Within Phase 1, Submission-Ready):**\\n\\nTo validate that behavioral rate calibration produces consequential changes in agent evaluation outcomes — directly addressing the gap between demonstrating behavioral rate matching and claiming calibration reduces evaluation bias — we run a proxy downstream evaluation within the synthetic pilot, using Seshadri et al.'s published real-user success rates as ground truth. Setup: (1) Fix a single agent (GPT-4o with τ-Bench retail tool access, using the standard τ-Bench retail tool configuration); (2) run N=50 τ-Bench retail task episodes per condition (250 total) using five simulator variants: uncalibrated Qwen 2.5 7B with AAVE demographic system prompt (Baseline a), BCP-extended AAVE simulator (Baseline f), DemoCalib DPO-calibrated AAVE simulator at optimal N, DemoCalib retrieval-augmented AAVE simulator at optimal N, and the DemoCalib DPO-calibrated Indian English simulator at optimal N; (3) compute simulated agent success rate per condition; (4) compare directionally to Seshadri et al.'s published human-grounded baselines: AAVE real users achieved approximately 39% agent task-completion; India-based participants achieved approximately 46.2%; SAE real users achieved approximately 49% — with the AAVE–SAE gap (approximately 10 percentage points) and the India–SAE gap (approximately 3 percentage points) anchoring the fairness claims for their respective groups. Including both real-user baselines — AAVE (~39%) and Indian English (~46.2%) — allows the proxy evaluation to cover both calibration arms: a calibrated AAVE simulator should produce success rate estimates directionally closer to ~39%, while a calibrated Indian English simulator should produce estimates directionally closer to ~46.2%.\\n\\nHypothesis: uncalibrated simulators, being excessively cooperative (over-polite, over-questioning), give agents more opportunities to clarify intent and recover from errors, artificially inflating estimated success rates above the real-user baselines; BCP (extended, two-dimensional) reduces cooperativeness via prompting but produces less pragmatically coherent turns; DemoCalib calibrated simulators produce behaviorally calibrated, pragmatically coherent interactions, generating success rate estimates directionally closer to the real-user baselines than either the uncalibrated simulator or BCP. Even directional confirmation of this hierarchy (uncalibrated → BCP → DemoCalib, each closer to real-user baselines) validates both that behavioral miscalibration is consequential for downstream evaluation fairness and that data-efficient training adds value over zero-compute prompting. Since we post-process only question rate and politeness frequency, calibration reduces but does not eliminate the full behavioral gap — remaining divergence in argument error rates (AAVE: 45.8% vs. simulator 32.2%) and repair sequences is expected to produce residual sim-real success rate discrepancy, motivating Phase 2. This proxy evaluation draws on the methodology established by 'Toward Scalable Verifiable Reward' (arXiv 2602.16246), which demonstrates LLM-driven proxy state tracking and goal-completion assessment for τ-Bench-style tasks with >90% human-judge agreement.\\n\\nAgent comparability caveat: Our proxy evaluation fixes GPT-4o with the standard τ-Bench retail tool configuration; Seshadri et al. do not report their exact agent setup, so the directional comparison to their real-user baselines may partly reflect agent-side differences independent of simulator calibration — we treat this comparison as indicative, with full agent-controlled comparison deferred to Phase 2.\\n\\nAPI cost: ~$75–300 at 250 episodes × $0.30–1.20/episode (GPT-4o agent calls plus simulator inference, including BCP baseline episodes); no GPU required. Runtime: 2–3 days concurrent with main experiment analysis, well within the 16-day pilot window.\\n\\nContribution claims are scoped explicitly to match results: if directional alignment is confirmed for both groups, the paper claims DemoCalib 'reduces simulation bias in agent success rate estimates for AAVE and Indian English speakers, producing estimates directionally closer to Seshadri et al. real-user baselines, outperforming both uncalibrated prompting and BCP behavioral constraint prompting'; if the proxy evaluation confirms directional improvement over uncalibrated but not over BCP, the paper claims DemoCalib is comparable to zero-compute BCP with the added benefit of behavioral distribution generalization; if the proxy evaluation does not confirm directional alignment, contribution claims are rewritten to strictly address 'behavioral rate matching in simulation,' downstream evaluation consequence is moved entirely to Phase 2, and the absence of directional alignment is itself a substantive finding about the limits of behavioral rate calibration as a proxy for evaluation consequence.\\n\\n**Sample Complexity and Synthetic Corpus Fidelity Caveats:**\\n\\nThe N=10–100 sample complexity curve characterizes data efficiency under synthetic-to-synthetic transfer conditions: both the calibration training signal and the held-out test traces are synthetic. Efficiency under real-to-real transfer (Phase 2 Prolific corpus) may differ because genuine human interaction traces exhibit natural behavioral variation beyond the rate targets specified as calibration targets — including idiosyncratic repair sequences, code-switching, and pragmatic patterns not captured by the two-dimensional fingerprint. This caveat is stated explicitly in the paper's limitations section. Phase 2 is the mechanism for characterizing real-to-real sample complexity.\\n\\nThe post-processing step guarantees target behavioral rates on the two measured dimensions (question rate, politeness frequency); however, other behavioral dimensions in the synthetic corpus — including code-switching patterns, error-repair sequences, pragmatic hedging, and clarification phrasing — remain subject to the same LLM miscalibration that the framework aims to correct, and may not fully reflect real AAVE or Indian English speaker patterns. Specifically, dialect-conditioned LLM generators that over-ask questions in unconditioned settings may also produce stylistically uniform repair sequences and formulaic hedging that differs from naturally occurring AAVE or Indian English pragmatic variation. Phase 2 human validation is the mechanism for assessing the full scope of behavioral fidelity beyond the two post-processed rate dimensions — the comparison between synthetic-corpus-calibrated and human-corpus-calibrated simulators in Phase 2 will directly quantify the gap introduced by uncontrolled LLM miscalibration on non-post-processed behavioral dimensions.\\n\\n**Phase 2 — Human Validation (Planned, Post-Submission):**\\n\\nA Prolific study following the validated Seshadri et al. (AFAA Workshop @ ICLR 2026) methodology recruits AAVE speakers (~40–60, US-based), Indian English speakers (~40–60, India-based, spanning a broader age range than Seshadri et al.'s 18–34 constraint), and SAE controls (~40), each completing 4 τ-Bench retail tasks (order management, product inquiry, return processing, cancellation), yielding 160–240 real interaction dialogues per group at ~$1,200–2,200 total. This study provides: (a) a genuine human reference corpus replacing the synthetic corpus (enabling direct comparison of synthetic vs. human reference corpus calibration quality and real-to-real sample complexity), (b) downstream agent evaluation consistency validation — calibrated-simulator-estimated agent success rate versus real-user success rate on held-out τ-Bench tasks using a matched agent configuration, targeting reduction of the sim-real behavioral calibration gap documented by Seshadri et al., (c) age-stratified Indian English behavioral rates beyond the 18–34 window, and (d) a public curated dataset contribution (AAVE and Indian English τ-Bench interaction traces). If Prolific data is available by camera-ready deadline, it upgrades the submission scope and supports a Main track revision.\\n\\nRegarding Seshadri et al. data access: We will contact the authors to request participant interaction traces under a formal institutional data sharing agreement for academic reuse (separate from the CC-BY 4.0 paper license, which applies only to paper text). This process requires institutional review and participant anonymization protocols and cannot be treated as a reliable fast-track. It is pursued opportunistically; if granted, Seshadri et al. traces would serve as an independent validation set.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~120h A100 80GB\",\n      \"gpu_utilization\": \"LOW-MODERATE (~40–50%): GPU idles during synthetic corpus generation (days 1–2, primarily LLM API calls), behavioral fingerprint extraction, DPO pair curation, code development, and result analysis between experiment runs. BCP baseline (f) runs via API with no GPU cost. Primary advantage over prior version: no IRB wait or Prolific recruitment gates the start of the GPU-intensive phase.\",\n      \"timeline\": \"2–4 months for synthetic pilot (including proxy downstream evaluation with BCP comparison); Prolific human validation adds 4–8 weeks as a parallel follow-on once submission is in\",\n      \"team\": \"2 researchers\",\n      \"data_collection_cost\": \"$20–50 (synthetic corpus generation via LLM API, ~300–600 τ-Bench dialogues); $75–300 (proxy downstream evaluation: 250 τ-Bench episodes × $0.30–1.20/episode including BCP baseline, no GPU required); $1,200–2,200 for planned Prolific human validation study (separate, post-submission)\",\n      \"estimated_gpu_cost\": \"$170–200 (at ~$1.50/h via Vast.ai spot market)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200h A100 80GB\",\n      \"gpu_utilization\": \"MODERATE (~55–65%): Agent batches DPO runs (3 groups × 3 sample sizes × 2 configs = 18 runs × ~6h each = 108h), few-shot sweeps, and τ-Bench evaluation passes; human approval gates (~30 min/day) replace idle phases. Synthetic corpus generation completes in days 1–2 before GPU-intensive phase begins with no external dependency. BCP baseline (f) and proxy downstream evaluation (250 episodes) run via API concurrently with DPO analysis, requiring no GPU.\",\n      \"timeline\": \"1–2 months (no external IRB or recruitment dependency gates the primary synthetic pilot path)\",\n      \"team\": \"1 researcher, ~30 min/day check-in for experiment approval and direction\",\n      \"claude_api_cost\": \"$100–200 (~1,500 turns × $0.10/turn for experiment orchestration over 1–2 months)\",\n      \"estimated_gpu_cost\": \"$280–320 (at ~$1.50/h)\",\n      \"data_collection_cost\": \"$20–50 (synthetic corpus generation); $75–300 (proxy downstream evaluation including BCP baseline, API only); $1,200–2,200 for planned Prolific study (post-submission, human-initiated)\",\n      \"risk_note\": \"Primary risks: (1) UserLM-R1 weights may not be publicly released at submission time — fall back to zero-shot Qwen-3 8B with dialect prompt, with reduced baseline fidelity noted in the paper; (2) validity criterion (>50% 3-class fingerprint classification accuracy) may fail on synthetic corpus — two-stage contingency in place; (3) BCP (Baseline f) may match behavioral rates comparably to DemoCalib — reframe contribution as identifying conditions under which zero-compute prompting suffices versus data-efficient training, both outcomes publishable; (4) proxy downstream evaluation may not show directional alignment — contribution claims reframed as behavioral rate matching; (5) early few-shot sweep (days 3–5) recommended to check whether retrieval-augmented conditioning achieves comparable calibration without DPO compute, enabling grid pruning.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~360h A100 80GB (full grid: 3 groups × 6 baselines × 4 sample sizes × 2 DPO hyperparameter configs + evaluation sweeps; ≈180h H100-equivalent, within 200h H100 budget)\",\n      \"gpu_utilization\": \"HIGH (~85–90%): Continuous experiment queue with no human-induced idle; agents schedule synthetic corpus generation (days 1–2), DPO runs, few-shot sweeps, τ-Bench evaluation passes, BCP baseline API runs, and proxy downstream evaluation API calls back-to-back across 4–6 parallel A100s\",\n      \"timeline\": \"3–5 days with 4–6 parallel A100s (each Qwen 2.5 7B LoRA-DPO run: ~6h on one A100 80GB); BCP baseline and proxy downstream evaluation (250 episodes) run concurrently via API from day 3 onward\",\n      \"team\": \"0 (initial setup only: ~3h to configure synthetic corpus generation pipeline, post-processing scripts, experiment manifests, BCP baseline harness, proxy downstream evaluation harness, and evaluation harness; no IRB step required for primary path)\",\n      \"claude_api_cost\": \"$200–350 (~2,500 turns × $0.10/turn for experiment orchestration, result synthesis, and draft writing)\",\n      \"estimated_gpu_cost\": \"$520–560 (at ~$1.50/h)\",\n      \"data_collection_cost\": \"$20–50 (synthetic corpus generation); $75–300 (proxy downstream evaluation including BCP baseline episodes, API only); Prolific human validation ($1,200–2,200) is post-submission and human-initiated\",\n      \"speed_bottleneck\": \"Purely compute-bound: synthetic corpus generation completes in days 1–2 (API-rate-limited, not GPU-limited); BCP baseline runs can be scheduled immediately alongside corpus generation (no GPU required); GPU phase starts day 2; proxy downstream evaluation API calls begin day 3 concurrent with DPO analysis. If UserLM-R1 weights are unavailable, baseline (c) falls back to zero-shot Qwen-3 8B — agent should detect via HuggingFace availability check and handle the fallback automatically.\",\n      \"risk_note\": \"Primary risk: agent invests in full DPO grid before discovering retrieval-augmented conditioning or BCP achieves comparable calibration at zero/minimal compute. A human checkpoint at day 2 (post-initial few-shot and BCP results) is strongly recommended to prune DPO configurations. Secondary risk: validity criterion (>50% fingerprint classification accuracy) may not be met — two-stage contingency in place. Tertiary risk: proxy downstream evaluation may not show directional alignment — contribution claims are reframed as behavioral rate matching only, null finding is reported, Phase 2 resolves downstream validation. Agent should surface BCP baseline results, fingerprint classification results, and initial proxy evaluation results at day 3 checkpoint before committing full DPO compute.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (ACL Rolling Review, ongoing cycles; primary target — synthetic pilot with proxy downstream evaluation including BCP comparison and planned human validation is well-matched to Findings scope; novel end-to-end framework with proof-of-concept results and clear empirical grounding in two dialect groups)\",\n    \"EMNLP 2026 Main (stretch target; requires all three upside conditions: (1) calibrated simulator reduces sim-real behavioral fingerprint gap by >40% relative versus best baseline including BCP; (2) sample complexity curve shows effective calibration at N≤20 synthetic dialogues; (3) proxy downstream evaluation confirms directional alignment between calibrated simulator success rate estimates and Seshadri et al.'s real-user baselines for both AAVE (~39%) and Indian English (~46.2%))\",\n    \"AAAI 2027 (submission deadline expected July–August 2026; if Prolific validation study is complete by then, downstream agent evaluation consistency results substantially strengthen the submission)\",\n    \"CHI 2027 (submission deadline September 10, 2026; HCI + fair evaluation angle; Prolific human validation data and equitable agentic AI evaluation framing align with CHI scope)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) — primary source for AAVE behavioral rates (~10% question, ~19.7% politeness), Indian English rates (9.9%/20.1%, Table 6, 18–34 age group), per-group agent success rates (AAVE ~39%, India ~46.2%, SAE ~49%, Table 3), and Appendix A.6 'minimal intervention' BCP (politeness-only constraint reducing aggregate success rate 50.0%→46.7%, shifting 11/18 task difficulty bins, improving calibration for AAVE/Indian/Kenyan but worsening for SAE/Nigerian). Accepted as oral at the ICLR 2026 Workshop on Algorithmic Fairness Across Alignment Procedures and Agentic Systems (AFAA).\",\n    \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks (arXiv 2603.11245, CMU, March 2026) — corroborates aggregate simulator over-cooperativeness across 451 participants; no per-dialect breakdown\",\n    \"MirrorBench: An Extensible Framework to Evaluate User-Proxy Agents for Human-Likeness (arXiv 2601.08118, 2026)\",\n    \"Synthetic Users, Real Differences: an Evaluation Framework for User Simulation in Multi-Turn Conversations (Liu et al., arXiv 2605.02624, May 2026) — proposes 'realsim,' an 8-dimensional framework for evaluating user simulation quality across communicative functions, user states, and message surface forms; evaluation-focused concurrent work that does not provide adaptation methodology or address dialect-group behavioral calibration\",\n    \"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles (Haq and Saldías, arXiv 2604.21152, April 2026) — documents a 'dialect jailbreak' phenomenon in AAVE and Singlish where implicit dialect cues reduce LLM refusal rates toward near-zero; input-side bias study adjacent to DemoCalib's simulator-side calibration, corroborating that implicit dialect features produce measurable and consequential LLM behavioral differences\",\n    \"The Need for a Socially-Grounded Persona Framework for User Simulation — SCOPE (arXiv 2601.07110, January 2026)\",\n    \"A Survey on LLM-based Conversational User Simulation (arXiv 2604.24977, EACL 2026)\",\n    \"τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (arXiv 2406.12045, 2024)\",\n    \"Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework (arXiv 2603.04409, ICLR 2026)\",\n    \"Toward Scalable Verifiable Reward: Proxy State-Based Evaluation for Multi-turn Tool-Calling LLM Agents (arXiv 2602.16246, 2026) — methodological grounding for LLM-driven proxy evaluation in τ-bench-style settings; >90% human-judge agreement\",\n    \"UserLM-R1: Modeling Human Reasoning in User Language Models with Multi-Reward Reinforcement Learning (arXiv 2601.09215, Meituan, Peking University, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences, Dalian University of Technology, January 2026)\",\n    \"Flipping the Dialogue: Training and Evaluating User Language Models — UserLM-8b (Naous et al., arXiv 2510.06552, NAACL 2025, Microsoft Research)\",\n    \"DialectLLM: A Dialect-Aware Dialogue Generation Framework Beyond Standard American English (arXiv 2601.22888, KAIST and Amazon, January 2026) — first author Jio Oh (KAIST and Amazon); rule-based dialect transformation across 9 English dialects including Indian English; used as Baseline (e) and for Indian English corpus generation\",\n    \"Persona-Aware Alignment Framework for Personalized Dialogue Generation — PAL (arXiv 2511.10215, TACL 2025)\",\n    \"PersoDPO: Scalable Preference Optimization for Instruction-Adherent, Persona-Grounded Dialogue via Multi-LLM Evaluation (arXiv 2602.04493, February 2026) — applies DPO with multi-LLM evaluation signals for coherence, personalization, and instruction adherence in open-domain conversational dialogue (FoCus dataset); no dialect-group targeting, no behavioral rate matching, no agentic task evaluation\",\n    \"Finetuning LLMs for Human Behavior Prediction in Social Science Experiments — Socrates/SocSci210 (Kolluri et al., EMNLP 2025; arXiv 2509.05830)\",\n    \"Population-Aligned Persona Generation for LLM-based Social Simulation (arXiv 2509.10127, Microsoft Research, September 2025)\",\n    \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model (Rafailov et al., NeurIPS 2023)\",\n    \"Evaluating Large Language Models as Generative User Simulators for Conversational Recommendation (arXiv 2403.09738)\",\n    \"AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark (arXiv 2024)\",\n    \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models (EMNLP 2025)\",\n    \"Black LLMirror: User (Self) Perceptions in Black American English Interactions with LLMs (CHI 2026)\",\n    \"Corpus of Regional African American Language — CORAAL (oraal.github.io/coraal; Version 2023.06)\"\n  ],\n  \"description\": \"LLM user simulators are systematically miscalibrated for dialect-group speakers in agentic settings: 'Lost in Simulation' (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) documents in Table 6 that AAVE speakers ask questions in only ~10% of turns versus 18.8% for LLM simulators, use politeness markers at ~19.7% versus 39.2%; and India-based participants (18–34 age group) show nearly identical behavioral profiles — 9.9% question rate and 20.1% politeness rate — both groups far below simulator baselines. Table 3 reports per-group agent success rates anchoring the downstream evaluation: AAVE real users achieved approximately 39% agent task-completion; India-based participants achieved approximately 46.2%; SAE real users achieved approximately 49%. Seshadri et al. also demonstrate in Appendix A.6 a 'minimal intervention' Behavioral Constraint Prompt (BCP) that limits politeness to 'at most one or two times across the entire conversation,' reducing aggregate simulated success rate from 50.0% to 46.7% and shifting 11 of 18 task difficulty bins — but this single-dimension (politeness-only) universal constraint leaves question-asking rate divergence unaddressed, fails to reach the AAVE real-user baseline (~39%), and worsens calibration for SAE and Nigerian groups. We propose DemoCalib, a data-efficient framework that adapts a Qwen 2.5 7B-Instruct simulator to a target dialect group using a small reference corpus, calibrating both behavioral dimensions simultaneously with group-specific targeting. Because assembling a genuine Prolific reference corpus requires IRB approval and participant recruitment (minimum 6–7 weeks), the primary submission-ready evaluation uses a synthetic reference corpus: target behavioral profiles are directly specified from published empirical rates (Seshadri et al. Table 6: AAVE 10%/~19.7% question/politeness rates; Indian English 9.9%/20.1%), and dialect-conditioned LLM traces on τ-Bench tasks (AAVE: prompted using CORAAL/AAVENUE-documented features; Indian English: using DialectLLM's IN transformation rules from KAIST and Amazon, arXiv 2601.22888) provide linguistic texture, with turns post-processed to match behavioral rate targets — avoiding the circularity of deriving LLM behavioral targets from LLM-generated data. A coherence constraint ensures replaced turns do not introduce questions already answered by the agent or reference task variables not yet established in the dialogue state, implemented as a lightweight regex-based slot tracker. Post-processing guarantees target behavioral rates on the two measured dimensions (question rate, politeness frequency); other behavioral dimensions — including code-switching patterns, error-repair sequences, pragmatic hedging, and clarification phrasing — remain subject to LLM miscalibration and may not fully reflect real AAVE or Indian English speaker patterns; Phase 2 human validation is the mechanism for assessing full behavioral fidelity beyond these two post-processed dimensions. The two-group design does not test whether DemoCalib can match distinct behavioral fingerprints (AAVE and Indian English have nearly identical published targets: 10%/9.9% question, ~19.7%/20.1% politeness). Instead, it tests whether DemoCalib achieves matched behavioral targets across groups that differ in linguistic surface features (CORAAL/AAVENUE features for AAVE vs. DialectLLM IN rules for Indian English), and whether calibration difficulty or method effectiveness differs across groups despite identical numerical targets — a question with theoretical implications for the coupling between form and behavioral adaptation. A full Prolific human validation study (40–60 participants/group × 3 groups × 4 tasks, ~$1,200–2,200) is planned post-submission for downstream agent evaluation consistency validation and to extend Indian English calibration beyond the 18–34 age window. Behavioral fingerprints (question rate, politeness frequency, MATTR, repair patterns) are extracted from reference traces; as a validity criterion, these fingerprints are designed to separate dialect groups at >50% 3-class classification accuracy; if this fails, a two-stage contingency applies. Two calibration strategies are compared: DPO fine-tuning with contrastive demographic pairs (LoRA-efficient), and retrieval-augmented few-shot conditioning requiring no gradient updates. Six baselines: (a) uncalibrated simulator with demographic system prompt, (b) UserLM-8b with dialect steering, (c) UserLM-R1 (Meituan et al., Qwen-3 8B) with dialect system prompt — testing whether RL-trained adaptive persona reasoning without explicit behavioral calibration closes the gap, (d) Population-Aligned Persona Generation adapted to behavioral fingerprints, (e) DialectLLM-conditioned generation (KAIST and Amazon) for Indian English only — testing whether rule-based linguistic form calibration suffices versus DemoCalib's behavioral distribution matching, (f) Behavioral Constraint Prompt (BCP) — zero-compute two-dimensional rate-targeting system prompt extending Seshadri et al.'s Appendix A.6 minimal intervention to include both question rate (~10%) and politeness rate (~20%) constraints — the critical test of whether DemoCalib's training-based approach adds value over prompting. The BCP comparison is informative regardless of direction: if BCP matches rates comparably to DemoCalib, the paper identifies when zero-compute prompting suffices; if DPO outperforms BCP, the paper demonstrates added value of data-efficient training for multi-dimensional behavioral calibration, and can point to BCP's known failure on pragmatic coherence. Sample complexity is characterized across N=10–100 reference dialogues. The proxy downstream evaluation runs 250 τ-Bench retail task episodes (50 per condition: uncalibrated, BCP, DemoCalib-DPO, DemoCalib-retrieval for AAVE; DemoCalib-DPO for Indian English) with a fixed GPT-4o agent, comparing calibrated and uncalibrated simulator success rate estimates directionally against both real-user baselines — AAVE (~39%) and Indian English (~46.2%) — from Seshadri et al. Tables 3 and 6. Contribution claims are scoped to match results: directional hierarchy (uncalibrated → BCP → DemoCalib, each closer to real-user baselines) confirms behavioral miscalibration is consequential and data-efficient training adds value over zero-compute prompting; partial confirmation and null results are reported as substantive findings. DemoCalib is the first end-to-end calibration procedure for dialect-group behavioral distribution matching in agentic task evaluation, grounded in published empirical rates for two dialect groups from the same Prolific study, with a proxy downstream evaluation anchored to published real-user success rate baselines for both groups, and with an explicit comparison to the strongest zero-compute prompting baseline available in the literature.\",\n  \"project_name\": \"demo_calibrated_sim\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 9)\nIssues: [\"MISSING CITATION — 'ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders' (Meshi, Goldman et al.; arXiv 2602.16938; EACL 2026 long paper, aclanthology.org/2026.eacl-long.244): This EACL 2026 paper explicitly introduces the 'realism gap' concept for LLM-based user simulators — the same central concept underlying DemoCalib's motivation — and demonstrates that data-driven simulators outperform prompted baselines while a significant realism gap persists. Reviewers in the user simulation space who have read this EACL 2026 paper will notice its absence. A one-sentence differentiation in related work is sufficient: 'ConvApparel (Meshi et al., EACL 2026; arXiv 2602.16938) measures the realism gap in conversational recommender simulators and validates data-driven approaches over prompting; unlike DemoCalib, it does not address dialect-group-specific behavioral calibration or agentic task-completion evaluation, and provides no adaptation methodology for closing the gap for target demographic groups.'\"]\nFeedback: DemoCalib has addressed all critical issues from Rounds 1–8 comprehensively. All factual errors are corrected (model names, affiliations, workshop title), all key related work is cited (realsim, Haq & Saldías, PersoDPO, DialectLLM at KAIST+Amazon, UserLM-R1 at Meituan), the BCP baseline (Baseline f) is included with proper two-dimensional rate targeting, the Indian English downstream anchor (~46.2%) is included alongside the AAVE anchor (~39%), all caveats are explicit (agent comparability, synthetic corpus circularity, sample complexity scope), and the two-stage validity criterion contingency is well-specified. One remaining fix:\n\n**Fix — Add ConvApparel to related work (one sentence):** Add the one-sentence citation to ConvApparel (arXiv 2602.16938, EACL 2026) in the landscape/related work section, positioning it as complementary work measuring the realism gap in conversational recommender settings without providing dialect-group adaptation methodology. This is the only missing citation an informed EMNLP reviewer would notice at this stage.\n\nAfter this single addition, the paper is submission-ready for EMNLP 2026 Findings. The average score (3.5–4.0 range) reflects genuine structural constraints of the 16-day scope — the synthetic-only pilot, matched two-group targets, and unresolved BCP vs. DPO comparison — not design errors. These are properly framed as limitations, not oversold as resolved. The paper is a well-motivated, honest, and technically sound Findings-level submission.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 9 轮修订，近 3 轮的平均分从 3.8 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:18:27.943Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:18:27.943Z",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-10T09:18:27.969Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "DemoCalib: Data-Efficient Dialect-Behavioral Calibration of LLM User Simulators for Fair Agentic Evaluation",
  "core_problem": "LLM user simulators exhibit systematic behavioral miscalibration for dialectal speaker groups in agentic task-completion settings: they are excessively cooperative, over-polite, and question-asking at rates that diverge sharply from real users in groups like AAVE and Indian English speakers. Seshadri et al. (AFAA@ICLR 2026; arXiv 2601.17087) document that AAVE speakers ask questions in only ~10% of turns versus 18.8% for LLM simulators, use politeness markers at ~19.7% versus 39.2%; Indian English speakers (India-based Prolific participants, 18–34 age group) show nearly identical behavioral profiles — 9.9% question rate and 20.1% politeness rate — both groups sharply divergent from simulator baselines. This behavioral miscalibration is not merely noisy: Seshadri et al. report a concrete downstream consequence — AAVE real users achieve approximately 39% agent task-completion rate versus ~49% for SAE speakers; India-based participants achieve approximately 46.2%. If this gap is partly attributable to simulator over-cooperativeness producing artificially inflated success rate estimates for dominant-group speakers, then calibrated simulators should produce success rate estimates closer to the real-user baselines. Seshadri et al. demonstrate in Appendix A.6 that a 'minimal intervention' behavioral constraint prompt (BCP) limiting politeness to 'at most one or two times across the entire conversation' shifts 11 of 18 tasks' difficulty bins and reduces aggregate simulated success rate from 50.0% to 46.7% — partially improving calibration for AAVE, Indian, and Kenyan groups. However, the BCP constrains only politeness frequency, leaving the question-asking rate gap (18.8% simulated vs. ~10% real for both AAVE and Indian English) entirely unaddressed; aggregate success rate remains at 46.7%, far above the AAVE real-user baseline of ~39%. No method exists to adapt a general-purpose LLM simulator's full behavioral distribution to match the empirically observed behavioral profile of a target dialectal group given a small reference sample — addressing both question-asking and politeness dimensions without degrading calibration for other groups — and no prior work has validated such adaptation against downstream agent evaluation consistency. Importantly, because assembling a genuine Prolific reference corpus requires IRB approval and participant recruitment (minimum 6–7 weeks), the framework must be demonstrable via a synthetic pilot that uses empirically-documented behavioral rates from published studies as calibration targets — enabling proof-of-concept results within a typical submission window, with full human validation as a planned follow-up contribution.",
  "opportunity": "'Lost in Simulation' (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) conducted a Prolific-recruited user study (~40 participants per group from the US, India, Kenya, Nigeria) running the full τ-Bench protocol, and documented sharp behavioral gaps between real users and LLM simulators. Critically, Table 6 of Seshadri et al. provides group-level behavioral rate breakdowns for both AAVE and Indian English speakers: AAVE speakers asked questions in only ~10% of turns versus 18.8% for LLM simulators; politeness marker usage was ~19.7% for AAVE real users versus 39.2% for simulators. India-based participants (18–34 age group, the only Indian age cohort recruited due to Prolific availability constraints) asked questions in 9.9% of turns and used politeness markers in 20.1% of turns — strikingly similar to AAVE rates and equally divergent from the 18.8%/39.2% simulator baseline. This convergence of AAVE and Indian English rates, both sharply below simulator baselines, provides a strong empirical foundation for a two-group calibration study: both groups have published target rates from the same study using the same methodology, enabling a direct comparison of calibration difficulty and transferability. Table 3 reports per-group agent success rates: AAVE real users achieved approximately 39% agent task-completion versus approximately 49% for SAE real users; India-based participants achieved approximately 46.2%. These per-group success rates anchor the proxy downstream evaluation: if behavioral miscalibration is a primary driver of biased success rate estimates, calibrated simulators should produce estimates closer to these real-user baselines.\n\nCritically, Seshadri et al. also document (Appendix A.6) a 'minimal intervention': a behavioral constraint prompt (BCP) limiting politeness to 'at most one or two times across the entire conversation' shifts 11 of 18 tasks' difficulty bins and reduces aggregate simulated success rate from 50.0% to 46.7%. The BCP improves simulator calibration for AAVE, Indian, and Kenyan groups but worsens it for SAE and Nigerian participants — demonstrating that a universal politeness constraint is not group-neutral and that single-dimension prompting falls short of full calibration. The BCP constrains only politeness; it leaves the question-asking rate divergence (18.8% simulated vs. ~10% real) entirely unaddressed, and aggregate success rate at 46.7% remains far above the AAVE real-user baseline of ~39%. The Indian English target (~46.2%) is closer to BCP's 46.7% aggregate, but this proximity is coincidental: a group-specific Indian English calibration targeting 9.9% question rate and 20.1% politeness rate requires matching both behavioral dimensions simultaneously and without degrading other groups. DemoCalib extends from BCP's single-dimension prompting to a full data-efficient behavioral distribution matching framework — addressing both dimensions, providing a concrete sample complexity characterization, and enabling group-specific calibration without universal constraint.\n\nAVAVE participants also encountered argument errors at 45.8% versus 32.2% for simulators; the Indian English group showed an Expected Calibration Error (ECE) of 18.9% versus 13.0% for SAE — confirming simulator miscalibration is worst for both groups. These are large effect sizes in agentic task language, far exceeding the ~1.5% demographic-variance figure from SCOPE (arXiv 2601.07110), which measured variance in survey opinion responses, not language-production behavior during task completion. Importantly, the 9-point agent-success-rate variation documented in 'Lost in Simulation' is primarily a model-to-model spread across 31 different LLM simulators; the demographic disparity is a secondary finding: simulated users are differentially unreliable proxies, performing worst for AAVE and Indian English speakers, with disparities compounding with age. 'Mind the Sim2Real Gap' (arXiv 2603.11245, CMU, March 2026) corroborates simulator over-cooperativeness across 451 real participants in aggregate (no per-dialect breakdown) but provides no adaptation method and has no dialect-group-specific rate data. Neither study has released participant interaction logs publicly: Seshadri et al. include no data availability statement or GitHub repository in the paper; 'Mind the Sim2Real Gap' likewise omits a data release. The CC-BY 4.0 license on the Seshadri et al. paper applies to the paper text only, not to participant interaction data — reuse of participant traces requires a separate formal data-sharing agreement and likely participant reconsent for secondary use, a process requiring 4–8 weeks. MirrorBench (arXiv 2601.08118) provides metrics for evaluating human-likeness (MATTR, HD-D, GTEval) without any training signal to produce calibrated simulators. The LLM-based conversational user simulation survey (arXiv 2604.24977) identifies demographic calibration as an open challenge. 'Toward Scalable Verifiable Reward: Proxy State-Based Evaluation for Multi-turn Tool-Calling LLM Agents' (arXiv 2602.16246) demonstrates LLM-driven proxy evaluation for τ-bench-style agentic tasks with >90% human-judge agreement, providing methodological grounding for the proxy downstream evaluation component. Crucially, the published empirical rates from Seshadri et al. Table 6 — AAVE: 10% question rate, ~19.7% politeness rate; Indian English (18–34): 9.9% question rate, 20.1% politeness rate; simulator: 18.8%, 39.2% — provide concrete, IRB-free calibration targets that directly parameterize synthetic reference corpus construction and DPO contrastive pair generation for both groups. The 18–34 age constraint on Indian English participants (a Prolific recruitment limitation in Seshadri et al., not a design choice) means the calibration targets represent younger adult Indian English speakers; age-stratified calibration for Indian English across broader demographics is a planned extension. This synthetic pilot validates the calibration pipeline; a full Prolific human-validation study is planned as a follow-on contribution. Seshadri et al.'s Prolific methodology (racial/ethnic + dialect self-identification screening) has been validated for recruiting AAVE speakers in LLM user studies (corroborated by Black LLMirror at CHI 2026), making the planned human validation study concrete and feasible at ~$1,200–2,200 (~120–180 participants × $7–10 each including platform fees). DialectLLM/MDial (arXiv 2601.22888, KAIST and Amazon, January 2026; updated May 2026) is used as a source of Indian English linguistic transformation rules for synthetic corpus generation in Phase 1 and as Baseline (e) for the Indian English group.",
  "landscape": "The user simulation landscape centers on τ-Bench and related agentic task benchmarks. 'Lost in Simulation' (AFAA Workshop @ ICLR 2026; arXiv 2601.17087) and 'Mind the Sim2Real Gap' (CMU, 2026) both quantify simulator-to-human gaps but provide no adaptation methods and have not released participant data. MirrorBench evaluates human-likeness without producing calibrated simulators. Liu et al. (arXiv 2605.02624, May 2026) propose 'realsim,' an 8-dimensional framework for evaluating user simulation quality across communicative functions, user states, and message surface forms, finding that simulated users systematically underrepresent communication frictions that real users introduce; unlike DemoCalib, it focuses on evaluation metrics rather than adaptation methodology, and does not address dialect-group behavioral calibration.\n\nA critical related method emerges from Seshadri et al. themselves: in Appendix A.6, the authors demonstrate a 'Behavioral Constraint Prompt' (BCP) that limits politeness to 'at most one or two times across the entire conversation.' The BCP reduces aggregate simulated success rate from 50.0% to 46.7% and shifts 11 of 18 tasks' difficulty bins, improving calibration for AAVE, Indian, and Kenyan groups while worsening it for SAE and Nigerian participants. The BCP is a zero-compute single-dimension prompting intervention that partially achieves DemoCalib's goal. Its limitations are threefold: (1) it constrains only politeness frequency, leaving the question-asking rate divergence (18.8% simulated vs. ~10% real for both AAVE and Indian English) entirely unaddressed; (2) aggregate success rate at 46.7% remains far above the AAVE real-user baseline (~39%), indicating that politeness-only calibration is insufficient for the hardest miscalibration cases; (3) it applies a universal constraint affecting all groups, degrading calibration for already well-calibrated groups (SAE, Nigerian), whereas DemoCalib provides group-specific calibration. DemoCalib includes BCP as Baseline (f) — extended to constrain both politeness and question rate explicitly — to provide a direct comparison between zero-compute prompting and data-efficient training. This comparison is informative regardless of outcome: if BCP (extended) achieves comparable behavioral rate matching without training, DemoCalib identifies the condition under which prompting suffices; if DPO outperforms extended BCP on held-out test traces and/or proxy downstream evaluation, the paper demonstrates added value of data-efficient training for multi-dimensional behavioral calibration.\n\nSeveral concurrent works partially address related problems but do not close the specific gap:\n\nUserLM-R1 (arXiv 2601.09215, Meituan and collaborating Chinese universities — Meituan, Peking University, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences, Dalian University of Technology — January 2026): The current frontier in user simulation model training. Trains user LMs with multi-reward RL combining rule-based (format, field verification) and rubric-based (reasoning quality, strategic alignment, conversational initiative) reward signals, using Qwen-3 8B/32B base models with adaptive user profiles that combine static persona traits (background, personality, expression style) and dynamic scenario-specific goals. Trained on 90,000 user profiles from AlignX and 450 task SOPs across 6 business scenarios; achieves strong performance particularly on adversarial agent-interaction tasks. Two key distinctions from DemoCalib: (1) UserLM-R1 is explicitly trained on Chinese-language samples with no English dialect or demographic calibration, and does not address the simulator-to-human behavioral gap for any dialect group; (2) it targets strategic reasoning capability and cross-domain generalization rather than matching the behavioral distribution of a specific real dialectal group in English agentic settings. UserLM-R1 is included as Baseline (c): zero-shot with an AAVE/Indian English dialect system prompt, testing whether RL-trained adaptive persona and reasoning capability — without explicit behavioral calibration — closes the miscalibration gap documented by Seshadri et al.\n\nUserLM-8b ('Flipping the Dialogue,' arXiv 2510.06552, NAACL 2025, Microsoft Research): Fine-tunes an 8B model on WildChat for general-conversation user simulation with no dialect-group targeting, no sample complexity analysis, and no downstream agent evaluation consistency metric.\n\nDialectLLM/MDial (arXiv 2601.22888, KAIST and Amazon, January 2026; updated May 2026): Rule-based framework for generating dialect-accurate multi-turn dialogues across 9 English dialects (SAE/US, Australian, British, Canadian, Indian, Irish, Nigerian, Philippine, Scottish) using linguist-curated lexical/orthographic/morphosyntactic transformation rules applied to SAE seed dialogues. Produces DialectLLM-Bench with 50k+ dialogues and 97k+ QA pairs; evaluation of 17 LLMs shows frontier models achieve under 70% dialect accuracy. Three critical distinctions from DemoCalib: (1) DialectLLM targets linguistic form accuracy — surface dialect features in generated text — while DemoCalib targets behavioral interaction dynamics (question rates, politeness frequency, repair patterns) in multi-turn agentic task flows; (2) DialectLLM generates generic conversational exchanges, not agentic task-completion traces under τ-Bench protocol with tool-use and policy constraints; (3) DialectLLM applies rule-based SAE-to-dialect transformation without any feedback loop for behavioral distribution matching. Note: DialectLLM covers Indian English but does not include AAVE among its 9 dialects (Nigerian English is present; AAVE as a US variety requires separate feature sources such as CORAAL and AAVENUE). DialectLLM-conditioned generation is included as Baseline (e) for the Indian English group: applying its IN transformation rules to uncalibrated simulator outputs tests whether rule-based linguistic form calibration alone suffices versus DemoCalib's behavioral distribution matching.\n\nThe PAL framework (arXiv 2511.10215, TACL): Uses DPO for persona-conditioned dialogue generation, optimizing persona alignment in general dialogue rather than matching the behavioral distribution of a specific real dialect group in agentic task settings.\n\nPersoDPO (arXiv 2602.04493, February 2026): Applies DPO with multi-LLM automatic evaluation signals to construct preference pairs for persona-consistent dialogue generation, optimizing for coherence, personalization, and instruction adherence on the FoCus conversational dialogue benchmark. Three distinctions from DemoCalib: (1) PersoDPO targets generic persona consistency (narrative coherence and identity alignment) rather than measurable behavioral rate matching (question-asking frequency, politeness marker frequency) for specific dialect groups; (2) it evaluates on open-domain conversational dialogue rather than multi-turn agentic task-completion under τ-Bench protocol with tool-use and policy constraints; (3) it does not address the simulator-to-human behavioral gap for any dialect group and includes no dialect or demographic variation analysis. PersoDPO is methodologically complementary: DemoCalib extends preference optimization from persona coherence to empirically grounded behavioral rate calibration in agentic evaluation settings.\n\nSocrates/SocSci210 (arXiv 2509.05830, EMNLP 2025, Stanford): Fine-tunes on 2.9M social science experiment responses — a survey/experiment domain rather than multi-turn agentic task completion, and with orders of magnitude more training data than DemoCalib's small-sample setting.\n\nPopulation-Aligned Persona Generation (arXiv 2509.10127, September 2025, Microsoft Research): Methodologically closest prior work — uses importance sampling to align LLM persona distributions to Big Five psychometric reference distributions for social simulation. Operates on self-report survey data (not agentic interaction traces), targets population-level psychometric distributions (not dialect-group behavioral fingerprints), and does not validate against downstream task evaluation consistency.\n\nHUMAINE (arXiv 2603.04409, ICLR 2026): Stratifies the evaluation dataset across 22 demographic groups, calibrating what we measure rather than how we simulate.\n\nSCOPE (arXiv 2601.07110): Argues demographic-only personas explain ~1.5% of variance in survey response similarity — a finding about opinion responses, not the language-production behavioral patterns (question rate, politeness frequency, repair sequences) that differ substantially between dialect groups in agentic task completion.\n\nHaq and Saldías (arXiv 2604.21152, April 2026) study implicit dialect signals (AAVE, Singlish) versus explicit demographic profiles in LLM responses, documenting a 'dialect jailbreak' phenomenon where implicit dialect cues reduce model refusal rates toward near-zero — an input-side bias in how LLMs respond to dialect users, distinct from DemoCalib's simulator-side behavioral calibration, but corroborating that implicit dialect features produce measurable and consequential LLM behavioral differences.\n\nToward Scalable Verifiable Reward (arXiv 2602.16246, 2026): Introduces proxy state-based evaluation for multi-turn tool-calling agents using LLM-driven state tracking and goal-completion judges, achieving >90% human-judge agreement. Provides methodological grounding for the proxy downstream evaluation component of DemoCalib but does not address dialect-group behavioral calibration.\n\nThe gap: given a small reference corpus or empirically-documented target behavioral profile for a specific dialect group, no existing method closes the loop from behavioral fingerprint extraction → simulator adaptation → proxy downstream agent evaluation consistency validation, with quantified sample complexity, in the τ-Bench agentic evaluation context. Seshadri et al.'s BCP (Appendix A.6) represents the strongest prior intervention — zero-compute, sourced from the primary motivating paper — but its single-dimension (politeness-only) scope and universal (non-group-specific) application demonstrate that it falls short of the full calibration problem DemoCalib addresses.",
  "approach": "DemoCalib is a data-efficient framework that adapts a general-purpose LLM simulator (Qwen 2.5 7B-Instruct as primary base model, selected for strong instruction-following capability, extensive open-weight documentation, and active HuggingFace community; Qwen 3.5 9B evaluated as a secondary ablation, contingent on publicly released weights being available on HuggingFace at time of submission) to match the behavioral distribution of a target dialect group. The framework operates in two phases: a proof-of-concept synthetic pilot (primary, 16-day feasible, IRB-free) and a planned human validation study (follow-up, providing downstream agent evaluation consistency validation and a genuine reference corpus contribution).\n\n**Phase 1 — Synthetic Pilot (Primary, Submission-Ready):**\n\nTarget behavioral profiles for each dialect group are directly specified from published empirical rates in Seshadri et al. (AFAA Workshop @ ICLR 2026; arXiv 2601.17087), Table 6: AAVE (question rate = 10% per turn, politeness marker rate = ~19.7%); Indian English (question rate = 9.9% per turn, politeness marker rate = 20.1%; India-based Prolific participants, 18–34 age group — the only Indian English cohort recruited in Seshadri et al. due to platform availability constraints, so calibration targets represent younger adult speakers; age-stratified Indian English calibration is a planned extension); SAE control (uncalibrated simulator baseline rates of 18.8% question rate, 39.2% politeness rate, from the same study).\n\n**Two-Group Design: Testing Cross-Feature Calibration Under Matched Behavioral Targets.** AAVE (10%/~19.7%) and Indian English (9.9%/20.1%) share nearly identical published calibration targets. Rather than treating this as a limitation, the two-group design explicitly tests two questions distinct from differential behavioral fingerprint matching: (a) whether DemoCalib can achieve matched behavioral targets across groups that differ substantially in linguistic surface features — AAVE calibration draws on CORAAL/AAVENUE morphosyntactic features (copula deletion, habitual be, negative concord, preverbal aspect marking), while Indian English calibration uses DialectLLM IN transformation rules (retroflex markers, topic-prominent constructions, distinct lexical items) — and (b) whether calibration difficulty, sample complexity curve, and method effectiveness (DPO vs. retrieval vs. BCP prompting) differ across groups despite identical numerical targets. If calibration converges at different rates or requires different N for AAVE vs. Indian English despite identical targets, this indicates that surface linguistic feature complexity mediates calibration difficulty — a theoretically important finding about the coupling between form and behavioral adaptation. The Indian English group additionally enables unique comparison with Baseline (e) (DialectLLM-conditioned generation), which has no AAVE analogue. This framing is stated explicitly in the paper to preempt the concern that a two-group study with matched targets only tests one behavioral profile: the multi-group contribution is cross-feature calibration under shared targets, not differential fingerprint matching.\n\nA synthetic reference corpus is generated for each group using a dialect-conditioned LLM (GPT-4o or Llama-3.1 70B) prompted with dialect-appropriate system instructions on τ-Bench retail tasks: AAVE instructions are informed by CORAAL-documented morphosyntactic features and AAVENUE benchmark patterns; Indian English instructions use DialectLLM/MDial's (KAIST and Amazon) Indian English transformation rules. This produces 100–200 τ-Bench interaction traces per group (~300–600 total). Generated turns are then post-processed to match target behavioral rates (e.g., excess question-asking turns identified by a simple utterance-type classifier and replaced with non-question continuations until the target rate is achieved). This post-processing step is critical: it prevents the circularity of using LLM-generated corpus to calibrate LLM behavioral rates, since the LLM generator itself exhibits the same over-questioning and over-politeness miscalibration being corrected. Linguistic texture comes from the dialect-conditioned generator; behavioral rates are independently grounded in Seshadri et al.'s published human data.\n\nPost-processing coherence constraint: Each replacement turn must pass a slot-filling consistency check against the task state before being accepted. Specifically, (1) the replacement must not introduce an open question that the agent has already answered in the preceding turn, and (2) it must reference only task variables (product IDs, order numbers, return policies) that have been established in the dialogue history up to that point. This check is implemented as a regex-based slot tracker operating on the τ-Bench structured task state, requiring no additional model calls and adding negligible latency to the post-processing pipeline. Replacement candidates failing this check are discarded and regenerated until a coherent candidate is found or the turn is flagged for manual review.\n\nThe entire generation and post-processing pipeline takes 1–2 days via API calls at ~$20–50 in API costs.\n\nBehavioral fingerprints are extracted from each group's reference traces: question-asking rate per turn, politeness marker frequency (detected via a curated lexicon), turn-length histograms, lexical diversity (MATTR, HD-D), clarification-request frequency, and error-repair patterns. As a validity criterion (not a completed finding), the fingerprint extraction is designed so that fingerprints from the synthetic reference traces should separate dialect groups at >50% 3-class classification accuracy; this threshold confirms that the synthetic corpus exhibits sufficient behavioral divergence to ground calibration. If this criterion is met, the calibration training proceeds as planned. If not, a two-stage contingency applies: (a) First fallback — increase dialect feature density in the generation prompt using stricter CORAAL-derived morphosyntactic constraints for AAVE and more restrictive DialectLLM IN transformation rules for Indian English, then regenerate the corpus and re-evaluate fingerprint classification; (b) Second fallback — if the criterion still fails after corpus revision, reduce the behavioral gap being matched from the full dialect–SAE divergence to the most robustly reproducible subset (e.g., politeness marker rate only, which shows the largest absolute divergence), report partial calibration results, and frame the incomplete fingerprint separation as a substantive finding about the limits of current dialect-conditioned LLM generation — a publishable negative result about the circularity constraint in synthetic dialect calibration. This contingency turns a binary pass/fail into a graceful degradation with interpretable findings at each stage.\n\nMeeting the primary validity criterion demonstrates that behavioral fingerprints in agentic task data capture group differences beyond SCOPE's 1.5% survey-response variance figure — because the behavioral rate targets were independently specified from human data rather than derived from the LLM generator.\n\nTwo calibration strategies are compared: (1) DPO fine-tuning with contrastive pairs opposing reference group turns against uncalibrated simulator outputs on identical task prompts, implemented with LoRA (rank=64) for data-efficient adaptation; (2) retrieval-augmented few-shot conditioning injecting the k most behaviorally similar reference turns as in-context demonstrations at inference time, requiring no gradient updates. Six baselines:\n\n(a) Uncalibrated Qwen 2.5 7B-Instruct with demographic system prompt (HUMAINE-style persona prompting) — the generic demographically-aware prompting baseline;\n\n(b) UserLM-8b conditioned on dialect-group system prompt;\n\n(c) UserLM-R1 (Qwen-3 8B, from Meituan and collaborating Chinese universities, if weights are publicly available at submission time; otherwise approximated as zero-shot Qwen-3 8B with identical dialect system prompt) with AAVE/Indian English dialect system prompt — testing whether RL-trained adaptive persona and reasoning capability without explicit behavioral calibration closes the gap;\n\n(d) Population-Aligned Persona Generation adapted to use behavioral fingerprints instead of Big Five traits for importance sampling;\n\n(e) DialectLLM-conditioned generation (KAIST and Amazon; arXiv 2601.22888) applied to τ-Bench interactions for the Indian English group only (DialectLLM does not cover AAVE), testing whether rule-based linguistic form calibration alone suffices versus DemoCalib's behavioral distribution matching;\n\n(f) Behavioral Constraint Prompt (BCP) — Qwen 2.5 7B-Instruct prompted with explicit per-turn behavioral rate targets derived directly from Seshadri et al. Table 6: 'Ask questions in approximately 10% of turns. Use politeness markers (e.g., please, thank you, sorry) in approximately 20% of turns.' Applied independently to each dialect group (AAVE and Indian English). This extends the 'minimal intervention' documented in Seshadri et al. Appendix A.6 — which constrained only politeness to 'at most one or two times across the entire conversation' and reduced aggregate success rate from 50.0% to 46.7% — to a full two-dimensional behavioral rate constraint. BCP is zero-compute (no training, no data), and is the critical comparison point for assessing whether DemoCalib's DPO fine-tuning adds value over simply encoding target rates in the system prompt. It is also the most natural baseline a reviewer familiar with Seshadri et al. would expect. Expected outcome: BCP achieves partial behavioral rate compliance on both dimensions but produces turns with degraded pragmatic coherence — abrupt non-questions that disrupt task flow — because instruction-following for rate constraints does not guarantee coherent substitution. DemoCalib's DPO/retrieval approach learns the underlying behavioral distribution, producing calibrated turns that maintain agentic pragmatic function. The comparison is informative regardless of direction: if BCP achieves comparable rate matching, DemoCalib identifies the condition under which prompting suffices; if DPO outperforms BCP on fingerprint match rate and/or proxy downstream evaluation, the paper demonstrates the added value of data-efficient training. Note: the Seshadri et al. BCP (politeness-only) worsens calibration for SAE and Nigerian groups while improving for AAVE, Indian, and Kenyan — demonstrating that universal behavioral constraint prompting is not group-neutral. DemoCalib's group-specific calibration avoids this: it targets AAVE and Indian English specifically without requiring a universal constraint applied to all groups.\n\nCalibration quality is validated via MirrorBench metrics (MATTR, HD-D, GTEval), behavioral fingerprint match rate (do calibrated outputs achieve target question/politeness rates on held-out synthetic test traces?), and task-completion preservation (does calibration maintain agentic task functionality?). Sample complexity is characterized by varying reference corpus size from N=10 to N=100 synthetic dialogues, reporting the minimum N needed to achieve fingerprint match within a target threshold — giving practitioners a concrete sample requirement curve for any dialect group.\n\n**Proxy Downstream Evaluation (Within Phase 1, Submission-Ready):**\n\nTo validate that behavioral rate calibration produces consequential changes in agent evaluation outcomes — directly addressing the gap between demonstrating behavioral rate matching and claiming calibration reduces evaluation bias — we run a proxy downstream evaluation within the synthetic pilot, using Seshadri et al.'s published real-user success rates as ground truth. Setup: (1) Fix a single agent (GPT-4o with τ-Bench retail tool access, using the standard τ-Bench retail tool configuration); (2) run N=50 τ-Bench retail task episodes per condition (250 total) using five simulator variants: uncalibrated Qwen 2.5 7B with AAVE demographic system prompt (Baseline a), BCP-extended AAVE simulator (Baseline f), DemoCalib DPO-calibrated AAVE simulator at optimal N, DemoCalib retrieval-augmented AAVE simulator at optimal N, and the DemoCalib DPO-calibrated Indian English simulator at optimal N; (3) compute simulated agent success rate per condition; (4) compare directionally to Seshadri et al.'s published human-grounded baselines: AAVE real users achieved approximately 39% agent task-completion; India-based participants achieved approximately 46.2%; SAE real users achieved approximately 49% — with the AAVE–SAE gap (approximately 10 percentage points) and the India–SAE gap (approximately 3 percentage points) anchoring the fairness claims for their respective groups. Including both real-user baselines — AAVE (~39%) and Indian English (~46.2%) — allows the proxy evaluation to cover both calibration arms: a calibrated AAVE simulator should produce success rate estimates directionally closer to ~39%, while a calibrated Indian English simulator should produce estimates directionally closer to ~46.2%.\n\nHypothesis: uncalibrated simulators, being excessively cooperative (over-polite, over-questioning), give agents more opportunities to clarify intent and recover from errors, artificially inflating estimated success rates above the real-user baselines; BCP (extended, two-dimensional) reduces cooperativeness via prompting but produces less pragmatically coherent turns; DemoCalib calibrated simulators produce behaviorally calibrated, pragmatically coherent interactions, generating success rate estimates directionally closer to the real-user baselines than either the uncalibrated simulator or BCP. Even directional confirmation of this hierarchy (uncalibrated → BCP → DemoCalib, each closer to real-user baselines) validates both that behavioral miscalibration is consequential for downstream evaluation fairness and that data-efficient training adds value over zero-compute prompting. Since we post-process only question rate and politeness frequency, calibration reduces but does not eliminate the full behavioral gap — remaining divergence in argument error rates (AAVE: 45.8% vs. simulator 32.2%) and repair sequences is expected to produce residual sim-real success rate discrepancy, motivating Phase 2. This proxy evaluation draws on the methodology established by 'Toward Scalable Verifiable Reward' (arXiv 2602.16246), which demonstrates LLM-driven proxy state tracking and goal-completion assessment for τ-Bench-style tasks with >90% human-judge agreement.\n\nAgent comparability caveat: Our proxy evaluation fixes GPT-4o with the standard τ-Bench retail tool configuration; Seshadri et al. do not report their exact agent setup, so the directional comparison to their real-user baselines may partly reflect agent-side differences independent of simulator calibration — we treat this comparison as indicative, with full agent-controlled comparison deferred to Phase 2.\n\nAPI cost: ~$75–300 at 250 episodes × $0.30–1.20/episode (GPT-4o agent calls plus simulator inference, including BCP baseline episodes); no GPU required. Runtime: 2–3 days concurrent with main experiment analysis, well within the 16-day pilot window.\n\nContribution claims are scoped explicitly to match results: if directional alignment is confirmed for both groups, the paper claims DemoCalib 'reduces simulation bias in agent success rate estimates for AAVE and Indian English speakers, producing estimates directionally closer to Seshadri et al. real-user baselines, outperforming both uncalibrated prompting and BCP behavioral constraint prompting'; if the proxy evaluation confirms directional improvement over uncalibrated but not over BCP, the paper claims DemoCalib is comparable to zero-compute BCP with the added benefit of behavioral distribution generalization; if the proxy evaluation does not confirm directional alignment, contribution claims are rewritten to strictly address 'behavioral rate matching in simulation,' downstream evaluation consequence is moved entirely to Phase 2, and the absence of directional alignment is itself a substantive finding about the limits of behavioral rate calibration as a proxy for evaluation consequence.\n\n**Sample Complexity and Synthetic Corpus Fidelity Caveats:**\n\nThe N=10–100 sample complexity curve characterizes data efficiency under synthetic-to-synthetic transfer conditions: both the calibration training signal and the held-out test traces are synthetic. Efficiency under real-to-real transfer (Phase 2 Prolific corpus) may differ because genuine human interaction traces exhibit natural behavioral variation beyond the rate targets specified as calibration targets — including idiosyncratic repair sequences, code-switching, and pragmatic patterns not captured by the two-dimensional fingerprint. This caveat is stated explicitly in the paper's limitations section. Phase 2 is the mechanism for characterizing real-to-real sample complexity.\n\nThe post-processing step guarantees target behavioral rates on the two measured dimensions (question rate, politeness frequency); however, other behavioral dimensions in the synthetic corpus — including code-switching patterns, error-repair sequences, pragmatic hedging, and clarification phrasing — remain subject to the same LLM miscalibration that the framework aims to correct, and may not fully reflect real AAVE or Indian English speaker patterns. Specifically, dialect-conditioned LLM generators that over-ask questions in unconditioned settings may also produce stylistically uniform repair sequences and formulaic hedging that differs from naturally occurring AAVE or Indian English pragmatic variation. Phase 2 human validation is the mechanism for assessing the full scope of behavioral fidelity beyond the two post-processed rate dimensions — the comparison between synthetic-corpus-calibrated and human-corpus-calibrated simulators in Phase 2 will directly quantify the gap introduced by uncontrolled LLM miscalibration on non-post-processed behavioral dimensions.\n\n**Phase 2 — Human Validation (Planned, Post-Submission):**\n\nA Prolific study following the validated Seshadri et al. (AFAA Workshop @ ICLR 2026) methodology recruits AAVE speakers (~40–60, US-based), Indian English speakers (~40–60, India-based, spanning a broader age range than Seshadri et al.'s 18–34 constraint), and SAE controls (~40), each completing 4 τ-Bench retail tasks (order management, product inquiry, return processing, cancellation), yielding 160–240 real interaction dialogues per group at ~$1,200–2,200 total. This study provides: (a) a genuine human reference corpus replacing the synthetic corpus (enabling direct comparison of synthetic vs. human reference corpus calibration quality and real-to-real sample complexity), (b) downstream agent evaluation consistency validation — calibrated-simulator-estimated agent success rate versus real-user success rate on held-out τ-Bench tasks using a matched agent configuration, targeting reduction of the sim-real behavioral calibration gap documented by Seshadri et al., (c) age-stratified Indian English behavioral rates beyond the 18–34 window, and (d) a public curated dataset contribution (AAVE and Indian English τ-Bench interaction traces). If Prolific data is available by camera-ready deadline, it upgrades the submission scope and supports a Main track revision.\n\nRegarding Seshadri et al. data access: We will contact the authors to request participant interaction traces under a formal institutional data sharing agreement for academic reuse (separate from the CC-BY 4.0 paper license, which applies only to paper text). This process requires institutional review and participant anonymization protocols and cannot be treated as a reliable fast-track. It is pursued opportunistically; if granted, Seshadri et al. traces would serve as an independent validation set.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h A100 80GB",
      "gpu_utilization": "LOW-MODERATE (~40–50%): GPU idles during synthetic corpus generation (days 1–2, primarily LLM API calls), behavioral fingerprint extraction, DPO pair curation, code development, and result analysis between experiment runs. BCP baseline (f) runs via API with no GPU cost. Primary advantage over prior version: no IRB wait or Prolific recruitment gates the start of the GPU-intensive phase.",
      "timeline": "2–4 months for synthetic pilot (including proxy downstream evaluation with BCP comparison); Prolific human validation adds 4–8 weeks as a parallel follow-on once submission is in",
      "team": "2 researchers",
      "data_collection_cost": "$20–50 (synthetic corpus generation via LLM API, ~300–600 τ-Bench dialogues); $75–300 (proxy downstream evaluation: 250 τ-Bench episodes × $0.30–1.20/episode including BCP baseline, no GPU required); $1,200–2,200 for planned Prolific human validation study (separate, post-submission)",
      "estimated_gpu_cost": "$170–200 (at ~$1.50/h via Vast.ai spot market)"
    },
    "human_in_loop": {
      "gpu_hours": "~200h A100 80GB",
      "gpu_utilization": "MODERATE (~55–65%): Agent batches DPO runs (3 groups × 3 sample sizes × 2 configs = 18 runs × ~6h each = 108h), few-shot sweeps, and τ-Bench evaluation passes; human approval gates (~30 min/day) replace idle phases. Synthetic corpus generation completes in days 1–2 before GPU-intensive phase begins with no external dependency. BCP baseline (f) and proxy downstream evaluation (250 episodes) run via API concurrently with DPO analysis, requiring no GPU.",
      "timeline": "1–2 months (no external IRB or recruitment dependency gates the primary synthetic pilot path)",
      "team": "1 researcher, ~30 min/day check-in for experiment approval and direction",
      "claude_api_cost": "$100–200 (~1,500 turns × $0.10/turn for experiment orchestration over 1–2 months)",
      "estimated_gpu_cost": "$280–320 (at ~$1.50/h)",
      "data_collection_cost": "$20–50 (synthetic corpus generation); $75–300 (proxy downstream evaluation including BCP baseline, API only); $1,200–2,200 for planned Prolific study (post-submission, human-initiated)",
      "risk_note": "Primary risks: (1) UserLM-R1 weights may not be publicly released at submission time — fall back to zero-shot Qwen-3 8B with dialect prompt, with reduced baseline fidelity noted in the paper; (2) validity criterion (>50% 3-class fingerprint classification accuracy) may fail on synthetic corpus — two-stage contingency in place; (3) BCP (Baseline f) may match behavioral rates comparably to DemoCalib — reframe contribution as identifying conditions under which zero-compute prompting suffices versus data-efficient training, both outcomes publishable; (4) proxy downstream evaluation may not show directional alignment — contribution claims reframed as behavioral rate matching; (5) early few-shot sweep (days 3–5) recommended to check whether retrieval-augmented conditioning achieves comparable calibration without DPO compute, enabling grid pruning."
    },
    "auto_research": {
      "gpu_hours": "~360h A100 80GB (full grid: 3 groups × 6 baselines × 4 sample sizes × 2 DPO hyperparameter configs + evaluation sweeps; ≈180h H100-equivalent, within 200h H100 budget)",
      "gpu_utilization": "HIGH (~85–90%): Continuous experiment queue with no human-induced idle; agents schedule synthetic corpus generation (days 1–2), DPO runs, few-shot sweeps, τ-Bench evaluation passes, BCP baseline API runs, and proxy downstream evaluation API calls back-to-back across 4–6 parallel A100s",
      "timeline": "3–5 days with 4–6 parallel A100s (each Qwen 2.5 7B LoRA-DPO run: ~6h on one A100 80GB); BCP baseline and proxy downstream evaluation (250 episodes) run concurrently via API from day 3 onward",
      "team": "0 (initial setup only: ~3h to configure synthetic corpus generation pipeline, post-processing scripts, experiment manifests, BCP baseline harness, proxy downstream evaluation harness, and evaluation harness; no IRB step required for primary path)",
      "claude_api_cost": "$200–350 (~2,500 turns × $0.10/turn for experiment orchestration, result synthesis, and draft writing)",
      "estimated_gpu_cost": "$520–560 (at ~$1.50/h)",
      "data_collection_cost": "$20–50 (synthetic corpus generation); $75–300 (proxy downstream evaluation including BCP baseline episodes, API only); Prolific human validation ($1,200–2,200) is post-submission and human-initiated",
      "speed_bottleneck": "Purely compute-bound: synthetic corpus generation completes in days 1–2 (API-rate-limited, not GPU-limited); BCP baseline runs can be scheduled immediately alongside corpus generation (no GPU required); GPU phase starts day 2; proxy downstream evaluation API calls begin day 3 concurrent with DPO analysis. If UserLM-R1 weights are unavailable, baseline (c) falls back to zero-shot Qwen-3 8B — agent should detect via HuggingFace availability check and handle the fallback automatically.",
      "risk_note": "Primary risk: agent invests in full DPO grid before discovering retrieval-augmented conditioning or BCP achieves comparable calibration at zero/minimal compute. A human checkpoint at day 2 (post-initial few-shot and BCP results) is strongly recommended to prune DPO configurations. Secondary risk: validity criterion (>50% fingerprint classification accuracy) may not be met — two-stage contingency in place. Tertiary risk: proxy downstream evaluation may not show directional alignment — contribution claims are reframed as behavioral rate matching only, null finding is reported, Phase 2 resolves downstream validation. Agent should surface BCP baseline results, fingerprint classification results, and initial proxy evaluation results at day 3 checkpoint before committing full DPO compute."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ACL Rolling Review, ongoing cycles; primary target — synthetic pilot with proxy downstream evaluation including BCP comparison and planned human validation is well-matched to Findings scope; novel end-to-end framework with proof-of-concept results and clear empirical grounding in two dialect groups)",
    "EMNLP 2026 Main (stretch target; requires all three upside conditions: (1) calibrated simulator reduces sim-real behavioral fingerprint gap by >40% relative versus best baseline including BCP; (2) sample complexity curve shows effective calibration at N≤20 synthetic dialogues; (3) proxy downstream evaluation confirms directional alignment between calibrated simulator success rate estimates and Seshadri et al.'s real-user baselines for both AAVE (~39%) and Indian English (~46.2%))",
    "AAAI 2027 (submission deadline expected July–August 2026; if Prolific validation study is complete by then, downstream agent evaluation consistency results substantially strengthen the submission)",
    "CHI 2027 (submission deadline September 10, 2026; HCI + fair evaluation angle; Prolific human validation data and equitable agentic AI evaluation framing align with CHI scope)"
  ],
  "level": "solid",
  "key_references": [
    "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) — primary source for AAVE behavioral rates (~10% question, ~19.7% politeness), Indian English rates (9.9%/20.1%, Table 6, 18–34 age group), per-group agent success rates (AAVE ~39%, India ~46.2%, SAE ~49%, Table 3), and Appendix A.6 'minimal intervention' BCP (politeness-only constraint reducing aggregate success rate 50.0%→46.7%, shifting 11/18 task difficulty bins, improving calibration for AAVE/Indian/Kenyan but worsening for SAE/Nigerian). Accepted as oral at the ICLR 2026 Workshop on Algorithmic Fairness Across Alignment Procedures and Agentic Systems (AFAA).",
    "Mind the Sim2Real Gap in User Simulation for Agentic Tasks (arXiv 2603.11245, CMU, March 2026) — corroborates aggregate simulator over-cooperativeness across 451 participants; no per-dialect breakdown",
    "MirrorBench: An Extensible Framework to Evaluate User-Proxy Agents for Human-Likeness (arXiv 2601.08118, 2026)",
    "Synthetic Users, Real Differences: an Evaluation Framework for User Simulation in Multi-Turn Conversations (Liu et al., arXiv 2605.02624, May 2026) — proposes 'realsim,' an 8-dimensional framework for evaluating user simulation quality across communicative functions, user states, and message surface forms; evaluation-focused concurrent work that does not provide adaptation methodology or address dialect-group behavioral calibration",
    "Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles (Haq and Saldías, arXiv 2604.21152, April 2026) — documents a 'dialect jailbreak' phenomenon in AAVE and Singlish where implicit dialect cues reduce LLM refusal rates toward near-zero; input-side bias study adjacent to DemoCalib's simulator-side calibration, corroborating that implicit dialect features produce measurable and consequential LLM behavioral differences",
    "The Need for a Socially-Grounded Persona Framework for User Simulation — SCOPE (arXiv 2601.07110, January 2026)",
    "A Survey on LLM-based Conversational User Simulation (arXiv 2604.24977, EACL 2026)",
    "τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (arXiv 2406.12045, 2024)",
    "Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework (arXiv 2603.04409, ICLR 2026)",
    "Toward Scalable Verifiable Reward: Proxy State-Based Evaluation for Multi-turn Tool-Calling LLM Agents (arXiv 2602.16246, 2026) — methodological grounding for LLM-driven proxy evaluation in τ-bench-style settings; >90% human-judge agreement",
    "UserLM-R1: Modeling Human Reasoning in User Language Models with Multi-Reward Reinforcement Learning (arXiv 2601.09215, Meituan, Peking University, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences, Dalian University of Technology, January 2026)",
    "Flipping the Dialogue: Training and Evaluating User Language Models — UserLM-8b (Naous et al., arXiv 2510.06552, NAACL 2025, Microsoft Research)",
    "DialectLLM: A Dialect-Aware Dialogue Generation Framework Beyond Standard American English (arXiv 2601.22888, KAIST and Amazon, January 2026) — first author Jio Oh (KAIST and Amazon); rule-based dialect transformation across 9 English dialects including Indian English; used as Baseline (e) and for Indian English corpus generation",
    "Persona-Aware Alignment Framework for Personalized Dialogue Generation — PAL (arXiv 2511.10215, TACL 2025)",
    "PersoDPO: Scalable Preference Optimization for Instruction-Adherent, Persona-Grounded Dialogue via Multi-LLM Evaluation (arXiv 2602.04493, February 2026) — applies DPO with multi-LLM evaluation signals for coherence, personalization, and instruction adherence in open-domain conversational dialogue (FoCus dataset); no dialect-group targeting, no behavioral rate matching, no agentic task evaluation",
    "Finetuning LLMs for Human Behavior Prediction in Social Science Experiments — Socrates/SocSci210 (Kolluri et al., EMNLP 2025; arXiv 2509.05830)",
    "Population-Aligned Persona Generation for LLM-based Social Simulation (arXiv 2509.10127, Microsoft Research, September 2025)",
    "Direct Preference Optimization: Your Language Model is Secretly a Reward Model (Rafailov et al., NeurIPS 2023)",
    "Evaluating Large Language Models as Generative User Simulators for Conversational Recommendation (arXiv 2403.09738)",
    "AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark (arXiv 2024)",
    "EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models (EMNLP 2025)",
    "Black LLMirror: User (Self) Perceptions in Black American English Interactions with LLMs (CHI 2026)",
    "Corpus of Regional African American Language — CORAAL (oraal.github.io/coraal; Version 2023.06)"
  ],
  "description": "LLM user simulators are systematically miscalibrated for dialect-group speakers in agentic settings: 'Lost in Simulation' (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) documents in Table 6 that AAVE speakers ask questions in only ~10% of turns versus 18.8% for LLM simulators, use politeness markers at ~19.7% versus 39.2%; and India-based participants (18–34 age group) show nearly identical behavioral profiles — 9.9% question rate and 20.1% politeness rate — both groups far below simulator baselines. Table 3 reports per-group agent success rates anchoring the downstream evaluation: AAVE real users achieved approximately 39% agent task-completion; India-based participants achieved approximately 46.2%; SAE real users achieved approximately 49%. Seshadri et al. also demonstrate in Appendix A.6 a 'minimal intervention' Behavioral Constraint Prompt (BCP) that limits politeness to 'at most one or two times across the entire conversation,' reducing aggregate simulated success rate from 50.0% to 46.7% and shifting 11 of 18 task difficulty bins — but this single-dimension (politeness-only) universal constraint leaves question-asking rate divergence unaddressed, fails to reach the AAVE real-user baseline (~39%), and worsens calibration for SAE and Nigerian groups. We propose DemoCalib, a data-efficient framework that adapts a Qwen 2.5 7B-Instruct simulator to a target dialect group using a small reference corpus, calibrating both behavioral dimensions simultaneously with group-specific targeting. Because assembling a genuine Prolific reference corpus requires IRB approval and participant recruitment (minimum 6–7 weeks), the primary submission-ready evaluation uses a synthetic reference corpus: target behavioral profiles are directly specified from published empirical rates (Seshadri et al. Table 6: AAVE 10%/~19.7% question/politeness rates; Indian English 9.9%/20.1%), and dialect-conditioned LLM traces on τ-Bench tasks (AAVE: prompted using CORAAL/AAVENUE-documented features; Indian English: using DialectLLM's IN transformation rules from KAIST and Amazon, arXiv 2601.22888) provide linguistic texture, with turns post-processed to match behavioral rate targets — avoiding the circularity of deriving LLM behavioral targets from LLM-generated data. A coherence constraint ensures replaced turns do not introduce questions already answered by the agent or reference task variables not yet established in the dialogue state, implemented as a lightweight regex-based slot tracker. Post-processing guarantees target behavioral rates on the two measured dimensions (question rate, politeness frequency); other behavioral dimensions — including code-switching patterns, error-repair sequences, pragmatic hedging, and clarification phrasing — remain subject to LLM miscalibration and may not fully reflect real AAVE or Indian English speaker patterns; Phase 2 human validation is the mechanism for assessing full behavioral fidelity beyond these two post-processed dimensions. The two-group design does not test whether DemoCalib can match distinct behavioral fingerprints (AAVE and Indian English have nearly identical published targets: 10%/9.9% question, ~19.7%/20.1% politeness). Instead, it tests whether DemoCalib achieves matched behavioral targets across groups that differ in linguistic surface features (CORAAL/AAVENUE features for AAVE vs. DialectLLM IN rules for Indian English), and whether calibration difficulty or method effectiveness differs across groups despite identical numerical targets — a question with theoretical implications for the coupling between form and behavioral adaptation. A full Prolific human validation study (40–60 participants/group × 3 groups × 4 tasks, ~$1,200–2,200) is planned post-submission for downstream agent evaluation consistency validation and to extend Indian English calibration beyond the 18–34 age window. Behavioral fingerprints (question rate, politeness frequency, MATTR, repair patterns) are extracted from reference traces; as a validity criterion, these fingerprints are designed to separate dialect groups at >50% 3-class classification accuracy; if this fails, a two-stage contingency applies. Two calibration strategies are compared: DPO fine-tuning with contrastive demographic pairs (LoRA-efficient), and retrieval-augmented few-shot conditioning requiring no gradient updates. Six baselines: (a) uncalibrated simulator with demographic system prompt, (b) UserLM-8b with dialect steering, (c) UserLM-R1 (Meituan et al., Qwen-3 8B) with dialect system prompt — testing whether RL-trained adaptive persona reasoning without explicit behavioral calibration closes the gap, (d) Population-Aligned Persona Generation adapted to behavioral fingerprints, (e) DialectLLM-conditioned generation (KAIST and Amazon) for Indian English only — testing whether rule-based linguistic form calibration suffices versus DemoCalib's behavioral distribution matching, (f) Behavioral Constraint Prompt (BCP) — zero-compute two-dimensional rate-targeting system prompt extending Seshadri et al.'s Appendix A.6 minimal intervention to include both question rate (~10%) and politeness rate (~20%) constraints — the critical test of whether DemoCalib's training-based approach adds value over prompting. The BCP comparison is informative regardless of direction: if BCP matches rates comparably to DemoCalib, the paper identifies when zero-compute prompting suffices; if DPO outperforms BCP, the paper demonstrates added value of data-efficient training for multi-dimensional behavioral calibration, and can point to BCP's known failure on pragmatic coherence. Sample complexity is characterized across N=10–100 reference dialogues. The proxy downstream evaluation runs 250 τ-Bench retail task episodes (50 per condition: uncalibrated, BCP, DemoCalib-DPO, DemoCalib-retrieval for AAVE; DemoCalib-DPO for Indian English) with a fixed GPT-4o agent, comparing calibrated and uncalibrated simulator success rate estimates directionally against both real-user baselines — AAVE (~39%) and Indian English (~46.2%) — from Seshadri et al. Tables 3 and 6. Contribution claims are scoped to match results: directional hierarchy (uncalibrated → BCP → DemoCalib, each closer to real-user baselines) confirms behavioral miscalibration is consequential and data-efficient training adds value over zero-compute prompting; partial confirmation and null results are reported as substantive findings. DemoCalib is the first end-to-end calibration procedure for dialect-group behavioral distribution matching in agentic task evaluation, grounded in published empirical rates for two dialect groups from the same Prolific study, with a proxy downstream evaluation anchored to published real-user success rate baselines for both groups, and with an explicit comparison to the strongest zero-compute prompting baseline available in the literature.",
  "project_name": "demo_calibrated_sim",
  "source": "web_research"
}

## Reviewer feedback (round 9)
Issues: ["MISSING CITATION — 'ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders' (Meshi, Goldman et al.; arXiv 2602.16938; EACL 2026 long paper, aclanthology.org/2026.eacl-long.244): This EACL 2026 paper explicitly introduces the 'realism gap' concept for LLM-based user simulators — the same central concept underlying DemoCalib's motivation — and demonstrates that data-driven simulators outperform prompted baselines while a significant realism gap persists. Reviewers in the user simulation space who have read this EACL 2026 paper will notice its absence. A one-sentence differentiation in related work is sufficient: 'ConvApparel (Meshi et al., EACL 2026; arXiv 2602.16938) measures the realism gap in conversational recommender simulators and validates data-driven approaches over prompting; unlike DemoCalib, it does not address dialect-group-specific behavioral calibration or agentic task-completion evaluation, and provides no adaptation methodology for closing the gap for target demographic groups.'"]
Feedback: DemoCalib has addressed all critical issues from Rounds 1–8 comprehensively. All factual errors are corrected (model names, affiliations, workshop title), all key related work is cited (realsim, Haq & Saldías, PersoDPO, DialectLLM at KAIST+Amazon, UserLM-R1 at Meituan), the BCP baseline (Baseline f) is included with proper two-dimensional rate targeting, the Indian English downstream anchor (~46.2%) is included alongside the AAVE anchor (~39%), all caveats are explicit (agent comparability, synthetic corpus circularity, sample complexity scope), and the two-stage validity criterion contingency is well-specified. One remaining fix:

**Fix — Add ConvApparel to related work (one sentence):** Add the one-sentence citation to ConvApparel (arXiv 2602.16938, EACL 2026) in the landscape/related work section, positioning it as complementary work measuring the realism gap in conversational recommender settings without providing dialect-group adaptation methodology. This is the only missing citation an informed EMNLP reviewer would notice at this stage.

After this single addition, the paper is submission-ready for EMNLP 2026 Findings. The average score (3.5–4.0 range) reflects genuine structural constraints of the 16-day scope — the synthetic-only pilot, matched two-group targets, and unresolved BCP vs. DPO comparison — not design errors. These are properly framed as limitations, not oversold as resolved. The paper is a well-motivated, honest, and technically sound Findings-level submission.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 9 轮修订，近 3 轮的平均分从 3.8 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7bf5b6f4-2fce-4939-b957-c7f6bd302693",
  "type": "user",
  "uuid": "41e9c069-98a4-465a-8a3a-a5bb3b7aef94",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:18:27.966Z_

```json
{
  "parentUuid": "41e9c069-98a4-465a-8a3a-a5bb3b7aef94",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "d07f2f77-7b90-4ef9-ab2f-4efa62ad6293",
  "timestamp": "2026-05-10T09:18:27.966Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:18:27.966Z_

```json
{
  "parentUuid": "d07f2f77-7b90-4ef9-ab2f-4efa62ad6293",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d6375caa-7c2f-447c-83ef-7e0e6ca53e94",
  "timestamp": "2026-05-10T09:18:27.966Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"DemoCalib: Data-Efficient Dialect-Behavioral Calibration of LLM User S…",
  "leafUuid": "d6375caa-7c2f-447c-83ef-7e0e6ca53e94",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibrating LLM user simulators for dialect groups in agentic evaluation",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:18:53.176Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on the approach.

**Current State:**
- Round 9 of revisions
- Average score: 3.5-4.0 range, recent trend 3.8 to 3.5 (declining)
- The reviewer's only remaining fix is: Add ConvApparel citation (arXiv 2602.16938, EACL 2026) to related work

**Key question: Should I do a minor fix, major revision, or pivot?**

The reviewer says this is the ONLY remaining issue, and after this fix the paper is "submission-ready for EMNLP 2026 Findings." The declining score reflects "genuine structural constraints of the 16-day scope — the synthetic-only pilot, matched two-group targets, and unresolved BCP vs. 

DPO comparison — not design errors." The stagnation warning is real, but I need to think about whether the score decline signals a fundamental problem or just the natural ceiling for this scope. The reviewer explicitly frames the limitations as properly acknowledged rather than oversold, and endorses submission-readiness at the Findings level. Nine rounds is substantial, but the feedback has narrowed to a single citation addition, suggesting the core idea has been thoroughly refined. A 3.5-4.0 score is likely the realistic ceiling for a solid empirical study with inherent scope constraints.

Pivoting now would waste all that refinement work. The core problem—dialect behavioral miscalibration in LLM simulators—is real and documented, the approach is technically sound, and the constraints are genuine limitations rather than fixable errors. A major revision might push novelty beyond the BCP baseline, but the reviewer's explicit statement that this is the only remaining issue points toward a minor fix instead. Adding the ConvApparel citation is straightforward, and the declining score trend reflects structural constraints, not errors. I should commit to the minor revision path rather than starting over.

That said, I need to actually fetch and read the ConvApparel paper to understand what it does and craft a proper differentiation. Let me search for it on arXiv and see what the actual contribution is, then consider whether there are deeper issues I've been overlooking given nine rounds of revision already.

Looking at the core limitations holding back the score: the synthetic-only pilot uses identical behavioral targets for both dialect groups, so the two-group design doesn't really test whether the method can match different fingerprints. There's also the unresolved question of whether BCP—which requires zero compute—might already achieve the same performance, which would undercut the paper's contribution. And the sample complexity findings from synthetic-to-synthetic transfer may not hold up with real users.

I'm wondering if a pivot could address these more fundamentally—maybe by shifting focus toward building a more robust evaluation framework for measuring calibration quality across dialect groups, or by expanding to additional dialect groups to strengthen the empirical foundation.

But the reviewer's feedback is actually encouraging: they're saying this is submission-ready for a Findings venue, and a 3.5-4.0 score is acceptable. The guidance is clear—if I'm confident a revision round can achieve a breakthrough, keep improving; otherwise, make targeted fixes. Given that, I think the right move is to address the ConvApparel citation issue and then reassess whether there's a way to strengthen the novelty claim without overreaching. Let me actually look up the ConvApparel paper to understand what it covers and whether there's a real gap to address.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6375caa-7c2f-447c-83ef-7e0e6ca53e94",
  "isSidechain": false,
  "requestId": "req_011CatdzJ4Ahu4tbofVeo8WC",
  "type": "assistant",
  "uuid": "fbbbc1ae-531a-463e-a058-be60d0f41fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QSEj1jm4RpjccimfRVPj9k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21584,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1354,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21584
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T09:18:53.177Z_

I'll fetch the ConvApparel paper to understand it properly before crafting the differentiation, and do a targeted search to check if there's anything else I'm missing given the stagnation pattern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbbbc1ae-531a-463e-a058-be60d0f41fe3",
  "isSidechain": false,
  "requestId": "req_011CatdzJ4Ahu4tbofVeo8WC",
  "type": "assistant",
  "uuid": "c3c329ad-7a09-48a4-92ff-56b7c84f2f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QSEj1jm4RpjccimfRVPj9k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21584,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1354,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21584
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T09:18:53.186Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017sUaDGFDhHsdGQdqo2TmZX`</summary>

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
  "parentUuid": "c3c329ad-7a09-48a4-92ff-56b7c84f2f1c",
  "isSidechain": false,
  "requestId": "req_011CatdzJ4Ahu4tbofVeo8WC",
  "type": "assistant",
  "uuid": "d269188d-95b5-4cc3-bcb7-18fbcb4b748d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QSEj1jm4RpjccimfRVPj9k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21584,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1354,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21584
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T09:18:53.192Z_

<details><summary>↩ Tool result · `toolu_017sUaDGFDhHsdGQdqo2TmZX`</summary>

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
  "parentUuid": "d269188d-95b5-4cc3-bcb7-18fbcb4b748d",
  "isSidechain": false,
  "promptId": "7bf5b6f4-2fce-4939-b957-c7f6bd302693",
  "type": "user",
  "uuid": "52f9188d-0b00-468a-b57c-657664fdf451",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "d269188d-95b5-4cc3-bcb7-18fbcb4b748d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T09:18:55.249Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the ConvApparel paper and also do some searches to understand the current landscape better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52f9188d-0b00-468a-b57c-657664fdf451",
  "isSidechain": false,
  "requestId": "req_011Cate2A2miE8NiganFnkrD",
  "type": "assistant",
  "uuid": "ab6e5c26-f9c3-4cfa-888a-f424c42e74fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Li9phAVkY2yCHZ6DFwBQPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2368,
      "cache_read_input_tokens": 33215,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 33215,
          "cache_creation_input_tokens": 2368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2368
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T09:18:58.044Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012zDYCSNj2oiXTE7s8GeTYq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16938",
  "prompt": "Extract: (1) the paper's full title and authors, (2) the abstract, (3) the concept of 'realism gap' as defined/used in the paper, (4) the key findings about data-driven vs prompted simulators, (5) whether it addresses any dialect/demographic groups, (6) the task domain (conversational recommendation vs agentic task completion), and (7) whether it provides any adaptation methodology for closing the realism gap."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab6e5c26-f9c3-4cfa-888a-f424c42e74fe",
  "isSidechain": false,
  "requestId": "req_011Cate2A2miE8NiganFnkrD",
  "type": "assistant",
  "uuid": "8b9247ae-4c44-4951-8995-9aa8f7cca2ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Li9phAVkY2yCHZ6DFwBQPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2368,
      "cache_read_input_tokens": 33215,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 33215,
          "cache_creation_input_tokens": 2368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2368
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T09:18:58.501Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TkV4aMvXKAPt6gKaVatJR1`</summary>

```json
{
  "query": "ConvApparel realism gap user simulator conversational recommender EACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9247ae-4c44-4951-8995-9aa8f7cca2ee",
  "isSidechain": false,
  "requestId": "req_011Cate2A2miE8NiganFnkrD",
  "type": "assistant",
  "uuid": "270f0b78-f5ef-409a-8ec8-8694b5a3c4bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Li9phAVkY2yCHZ6DFwBQPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2368,
      "cache_read_input_tokens": 33215,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 33215,
          "cache_creation_input_tokens": 2368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2368
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T09:18:58.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LL6MxaGP4tk3a8aJPubzQ1`</summary>

```json
{
  "query": "dialect behavioral calibration LLM simulator agentic task 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "270f0b78-f5ef-409a-8ec8-8694b5a3c4bf",
  "isSidechain": false,
  "requestId": "req_011Cate2A2miE8NiganFnkrD",
  "type": "assistant",
  "uuid": "90d62061-6665-49e8-82fb-ee1402a28229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Li9phAVkY2yCHZ6DFwBQPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2368,
      "cache_read_input_tokens": 33215,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 33215,
          "cache_creation_input_tokens": 2368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2368
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T09:19:03.665Z_

<details><summary>↩ Tool result · `toolu_012zDYCSNj2oiXTE7s8GeTYq`</summary>

```text
# ConvApparel Paper Analysis

## (1) Title and Authors
**Title:** "ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders"

**Authors:** Ofer Meshi, Krisztian Balog, Sally Goldman, Avi Caciularu, Guy Tennenholtz, Jihwan Jeong, Amir Globerson, Craig Boutilier

## (2) Abstract
The paper introduces ConvApparel to address a critical problem: "The promise of LLM-based user simulators to improve conversational AI is hindered by a critical 'realism gap'" that causes systems optimized for simulated interactions to underperform in real-world contexts. The dataset uses a dual-agent protocol with both good and poor recommenders, capturing diverse user experiences with satisfaction annotations.

## (3) The 'Realism Gap'
The realism gap refers to the significant discrepancy between how user simulators behave in controlled settings versus real-world interactions, causing systems optimized through simulation to fail when deployed with actual users.

## (4) Key Findings: Data-Driven vs Prompted Simulators
The experiments demonstrate that "data-driven simulators outperform a prompted baseline, particularly in counterfactual validation where they adapt more realistically to unseen behaviors," suggesting they embody more robust user models.

## (5) Dialect/Demographic Groups
The provided content contains no information addressing specific dialect or demographic groups.

## (6) Task Domain
**Conversational recommendation** – specifically user simulators for conversational recommender systems.

## (7) Adaptation Methodology
The paper proposes a validation framework combining statistical alignment, human-likeness scoring, and counterfactual validation but does not describe an explicit methodology for closing the realism gap itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b9247ae-4c44-4951-8995-9aa8f7cca2ee",
  "isSidechain": false,
  "promptId": "7bf5b6f4-2fce-4939-b957-c7f6bd302693",
  "type": "user",
  "uuid": "81026711-cea6-4140-9090-08e70676d314",
  "toolUseResult": {
    "bytes": 46759,
    "code": 200,
    "codeText": "OK",
    "result": "# ConvApparel Paper Analysis\n\n## (1) Title and Authors\n**Title:** \"ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders\"\n\n**Authors:** Ofer Meshi, Krisztian Balog, Sally Goldman, Avi Caciularu, Guy Tennenholtz, Jihwan Jeong, Amir Globerson, Craig Boutilier\n\n## (2) Abstract\nThe paper introduces ConvApparel to address a critical problem: \"The promise of LLM-based user simulators to improve conversational AI is hindered by a critical 'realism gap'\" that causes systems optimized for simulated interactions to underperform in real-world contexts. The dataset uses a dual-agent protocol with both good and poor recommenders, capturing diverse user experiences with satisfaction annotations.\n\n## (3) The 'Realism Gap'\nThe realism gap refers to the significant discrepancy between how user simulators behave in controlled settings versus real-world interactions, causing systems optimized through simulation to fail when deployed with actual users.\n\n## (4) Key Findings: Data-Driven vs Prompted Simulators\nThe experiments demonstrate that \"data-driven simulators outperform a prompted baseline, particularly in counterfactual validation where they adapt more realistically to unseen behaviors,\" suggesting they embody more robust user models.\n\n## (5) Dialect/Demographic Groups\nThe provided content contains no information addressing specific dialect or demographic groups.\n\n## (6) Task Domain\n**Conversational recommendation** – specifically user simulators for conversational recommender systems.\n\n## (7) Adaptation Methodology\nThe paper proposes a validation framework combining statistical alignment, human-likeness scoring, and counterfactual validation but does not describe an explicit methodology for closing the realism gap itself.",
    "durationMs": 5616,
    "url": "https://arxiv.org/abs/2602.16938"
  },
  "sourceToolAssistantUUID": "8b9247ae-4c44-4951-8995-9aa8f7cca2ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T09:19:04.261Z_

<details><summary>↩ Tool result · `toolu_01LL6MxaGP4tk3a8aJPubzQ1`</summary>

```text
Web search results for query: "dialect behavioral calibration LLM simulator agentic task 2026"

Links: [{"title":"A Taxonomy of RL Environments for LLM Agents","url":"https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Agentic LLM-based robotic systems for real-world applications: a review on their agenticness and ethics - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12402697/"},{"title":"Large language models empowered agent-based modeling and simulation: a survey and perspectives | Humanities and Social Sciences Communications","url":"https://www.nature.com/articles/s41599-024-03611-3"},{"title":"Flipping the Dialogue: Training and Evaluating User Language Models | OpenReview","url":"https://openreview.net/forum?id=ykSmkVqzn4"},{"title":"Creation, evaluation and self-validation of simulation models with large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S092523122502702X"},{"title":"Best Agentic LLM Models & Frameworks 2026 | Adaline","url":"https://www.adaline.ai/blog/top-agentic-llm-models-frameworks-for-2026"},{"title":"The Best Open-Source LLMs for Agentic Coding in 2026 | MindStudio","url":"https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026"},{"title":"Abstract","url":"https://arxiv.org/html/2507.19364v2"},{"title":"LLM-Simulated Users","url":"https://www.emergentmind.com/topics/llm-simulated-users"}]

Based on the web search results, I found several highly relevant findings related to your query about dialect behavioral calibration, LLM simulators, and agentic tasks in 2026:

## Key Findings

**Behavioral Calibration and Dialect Disparities:**

Across τ-Bench tasks, simulated users overestimate agent success on easy tasks and underestimate on hard ones with Expected Calibration Error up to 15.1%, and dialect/group disparities up to 20.3%, differentially disadvantaging real-world populations such as AAVE and Indian English speakers (Seshadri et al., January 2026).

**Artifacts and Behavioral Mismatches:**

Simulated users produce more verbose, question-rich, and polite outputs, surface different dialogue error types, and can skew agent tuning toward unnatural interaction patterns.

**LLM-Driven Agent Behavior:**

The research emphasizes challenges in behavioral fidelity when using LLMs as simulated agents. Particular attention is given to the challenges of behavioral fidelity, calibration, and reproducibility in large-scale LLM-driven simulations.

**Best Practices for Behavioral Calibration:**

Best practices include multi-model evaluation, direct calibration against human sessions, or hybrid simulation/human-in-the-loop protocols to maintain robustness and validity.

These findings indicate that behavioral calibration of LLM simulators remains a critical challenge in 2026, particularly with respect to preserving dialect authenticity and fairness across different linguistic populations in agentic tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90d62061-6665-49e8-82fb-ee1402a28229",
  "isSidechain": false,
  "promptId": "7bf5b6f4-2fce-4939-b957-c7f6bd302693",
  "type": "user",
  "uuid": "b618440d-d5e2-4c51-bdf3-2fd9cb9dcb55",
  "toolUseResult": {
    "query": "dialect behavioral calibration LLM simulator agentic task 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Enx4HPfxK3dKyufLEMZREc",
        "content": [
          {
            "title": "A Taxonomy of RL Environments for LLM Agents",
            "url": "https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/"
          },
          {
            "title": "GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub",
            "url": "https://github.com/tmgthb/Autonomous-Agents"
          },
          {
            "title": "Agentic LLM-based robotic systems for real-world applications: a review on their agenticness and ethics - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12402697/"
          },
          {
            "title": "Large language models empowered agent-based modeling and simulation: a survey and perspectives | Humanities and Social Sciences Communications",
            "url": "https://www.nature.com/articles/s41599-024-03611-3"
          },
          {
            "title": "Flipping the Dialogue: Training and Evaluating User Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=ykSmkVqzn4"
          },
          {
            "title": "Creation, evaluation and self-validation of simulation models with large language models - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S092523122502702X"
          },
          {
            "title": "Best Agentic LLM Models & Frameworks 2026 | Adaline",
            "url": "https://www.adaline.ai/blog/top-agentic-llm-models-frameworks-for-2026"
          },
          {
            "title": "The Best Open-Source LLMs for Agentic Coding in 2026 | MindStudio",
            "url": "https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026"
          },
          {
            "title": "Abstract",
            "url": "https://arxiv.org/html/2507.19364v2"
          },
          {
            "title": "LLM-Simulated Users",
            "url": "https://www.emergentmind.com/topics/llm-simulated-users"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant findings related to your query about dialect behavioral calibration, LLM simulators, and agentic tasks in 2026:\n\n## Key Findings\n\n**Behavioral Calibration and Dialect Disparities:**\n\nAcross τ-Bench tasks, simulated users overestimate agent success on easy tasks and underestimate on hard ones with Expected Calibration Error up to 15.1%, and dialect/group disparities up to 20.3%, differentially disadvantaging real-world populations such as AAVE and Indian English speakers (Seshadri et al., January 2026).\n\n**Artifacts and Behavioral Mismatches:**\n\nSimulated users produce more verbose, question-rich, and polite outputs, surface different dialogue error types, and can skew agent tuning toward unnatural interaction patterns.\n\n**LLM-Driven Agent Behavior:**\n\nThe research emphasizes challenges in behavioral fidelity when using LLMs as simulated agents. Particular attention is given to the challenges of behavioral fidelity, calibration, and reproducibility in large-scale LLM-driven simulations.\n\n**Best Practices for Behavioral Calibration:**\n\nBest practices include multi-model evaluation, direct calibration against human sessions, or hybrid simulation/human-in-the-loop protocols to maintain robustness and validity.\n\nThese findings indicate that behavioral calibration of LLM simulators remains a critical challenge in 2026, particularly with respect to preserving dialect authenticity and fairness across different linguistic populations in agentic tasks."
    ],
    "durationSeconds": 5.572856964999999
  },
  "sourceToolAssistantUUID": "90d62061-6665-49e8-82fb-ee1402a28229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T09:19:06.245Z_

<details><summary>↩ Tool result · `toolu_01TkV4aMvXKAPt6gKaVatJR1`</summary>

```text
Web search results for query: "ConvApparel realism gap user simulator conversational recommender EACL 2026"

Links: [{"title":"ConvApparel: Measuring and bridging the realism gap in user simulators","url":"https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/"},{"title":"ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.244/"},{"title":"ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders","url":"https://arxiv.org/html/2602.16938v1"},{"title":"[2602.16938] ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders","url":"https://arxiv.org/abs/2602.16938"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Measuring and bridging the realism gap in user simulators - geekfence.com","url":"https://geekfence.com/measuring-and-bridging-the-realism-gap-in-user-simulators/"},{"title":"Krisztian Balog - Google Research","url":"https://research.google/people/107636/"},{"title":"(PDF) ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders","url":"https://www.researchgate.net/publication/400970935_ConvApparel_A_Benchmark_Dataset_and_Validation_Framework_for_User_Simulators_in_Conversational_Recommenders"},{"title":"ConvApparel: A Benchmark Dataset and Validation Framework for","url":"https://openreview.net/pdf/7155ec3a7add6e8523c432a4d878bf90f4bf5f82.pdf"},{"title":"Ofer Meshi","url":"https://research.google/people/ofermeshi/"}]

Based on the search results, here's what I found about ConvApparel:

## Overview

ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders was published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), with the paper presented at EACL 2026 in Rabat, Morocco.

## Problem Addressed

The promise of LLM-based user simulators to improve conversational AI is hindered by a critical "realism gap," leading to systems that are optimized for simulated interactions, but may fail to perform well in the real world.

## Key Contribution

The paper introduces ConvApparel, a new dataset of human-AI conversations designed to address this gap. Its unique dual-agent data collection protocol—using both "good" and "bad" recommenders—enables counterfactual validation by capturing a wide spectrum of user experiences, enriched with first-person annotations of user satisfaction.

## Methodology

The paper proposes a comprehensive validation framework that combines statistical alignment, a human-likeness score, and counterfactual validation to test for generalization.

## Key Findings

The experiments reveal a significant realism gap across all simulators. However, the framework also shows that data-driven simulators outperform a prompted baseline, particularly in counterfactual validation where they adapt more realistically to unseen behaviors.

The authors include Ofer Meshi, Krisztian Balog, Sally Goldman, Avi Caciularu, Guy Tennenholtz, Jihwan Jeong, Amir Globerson, and Craig Boutilier.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "270f0b78-f5ef-409a-8ec8-8694b5a3c4bf",
  "isSidechain": false,
  "promptId": "7bf5b6f4-2fce-4939-b957-c7f6bd302693",
  "type": "user",
  "uuid": "f5918431-ee59-446d-882a-6556d698cf41",
  "toolUseResult": {
    "query": "ConvApparel realism gap user simulator conversational recommender EACL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V9tqtX2WqymXDumMsWHQdV",
        "content": [
          {
            "title": "ConvApparel: Measuring and bridging the realism gap in user simulators",
            "url": "https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/"
          },
          {
            "title": "ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders - ACL Anthology",
            "url": "https://aclanthology.org/2026.eacl-long.244/"
          },
          {
            "title": "ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders",
            "url": "https://arxiv.org/html/2602.16938v1"
          },
          {
            "title": "[2602.16938] ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders",
            "url": "https://arxiv.org/abs/2602.16938"
          },
          {
            "title": "Main Conference Accepted Papers -",
            "url": "https://2026.eacl.org/program/main-accepted/"
          },
          {
            "title": "Measuring and bridging the realism gap in user simulators - geekfence.com",
            "url": "https://geekfence.com/measuring-and-bridging-the-realism-gap-in-user-simulators/"
          },
          {
            "title": "Krisztian Balog - Google Research",
            "url": "https://research.google/people/107636/"
          },
          {
            "title": "(PDF) ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders",
            "url": "https://www.researchgate.net/publication/400970935_ConvApparel_A_Benchmark_Dataset_and_Validation_Framework_for_User_Simulators_in_Conversational_Recommenders"
          },
          {
            "title": "ConvApparel: A Benchmark Dataset and Validation Framework for",
            "url": "https://openreview.net/pdf/7155ec3a7add6e8523c432a4d878bf90f4bf5f82.pdf"
          },
          {
            "title": "Ofer Meshi",
            "url": "https://research.google/people/ofermeshi/"
          }
        ]
      },
      "Based on the search results, here's what I found about ConvApparel:\n\n## Overview\n\nConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders was published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), with the paper presented at EACL 2026 in Rabat, Morocco.\n\n## Problem Addressed\n\nThe promise of LLM-based user simulators to improve conversational AI is hindered by a critical \"realism gap,\" leading to systems that are optimized for simulated interactions, but may fail to perform well in the real world.\n\n## Key Contribution\n\nThe paper introduces ConvApparel, a new dataset of human-AI conversations designed to address this gap. Its unique dual-agent data collection protocol—using both \"good\" and \"bad\" recommenders—enables counterfactual validation by capturing a wide spectrum of user experiences, enriched with first-person annotations of user satisfaction.\n\n## Methodology\n\nThe paper proposes a comprehensive validation framework that combines statistical alignment, a human-likeness score, and counterfactual validation to test for generalization.\n\n## Key Findings\n\nThe experiments reveal a significant realism gap across all simulators. However, the framework also shows that data-driven simulators outperform a prompted baseline, particularly in counterfactual validation where they adapt more realistically to unseen behaviors.\n\nThe authors include Ofer Meshi, Krisztian Balog, Sally Goldman, Avi Caciularu, Guy Tennenholtz, Jihwan Jeong, Amir Globerson, and Craig Boutilier."
    ],
    "durationSeconds": 7.741304558999997
  },
  "sourceToolAssistantUUID": "270f0b78-f5ef-409a-8ec8-8694b5a3c4bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"DemoCalib: Data-Efficient Dialect-Behavioral Calibration of LLM User S…",
  "leafUuid": "f5918431-ee59-446d-882a-6556d698cf41",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibrating LLM user simulators for dialect groups in agentic evaluation",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---

### Assistant

_source line 21 · 2026-05-10T09:19:31.605Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of ConvApparel:

1. **Title**: "ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders"
2. **Authors**: Ofer Meshi, Krisztian Balog, Sally Goldman, Avi Caciularu, Guy Tennenholtz, Jihwan Jeong, Amir Globerson, Craig Boutilier (Google Research)
3. **Task domain**: Conversational recommendation (not agentic task completion)
4. **Realism gap**: Discrepancy between simulated and real-world user behavior — same concept underlying DemoCalib


5. **Key finding**: Data-driven simulators outperform prompted baselines
6. **No dialect/demographic groups**: Does not address any specific dialect groups
7. **No adaptation methodology**: Provides a validation framework but not a method for closing the realism gap

The reviewer's suggested one-sentence differentiation is accurate. After nine rounds of revisions with declining scores, the only remaining action is adding the ConvApparel citation—the paper should be ready to submit once that's done.

But I'm noticing the real constraints here: the synthetic-only pilot with matched behavioral targets, the possibility that BCP baseline performance matches DPO, and the limited characterization of sample complexity. These structural issues are what's keeping the score capped. I could either take the minor fix route and accept a 3.5-4.0 range, or rethink the framing more fundamentally—maybe moving away from the synthetic pilot entirely and grounding this in actual data collection instead.

Wait, let me reconsider what the score trajectory actually means. The decline from 3.8 to 3.5 over recent rounds might not signal a weaker paper, but rather the reviewer becoming more precise about what the contribution really is and what it isn't.

The reviewer's feedback suggests the paper is ready for EMNLP 2026 Findings with just a citation fix, which is a solid outcome. But I'm weighing whether to push for Main track instead by targeting those three conditions: demonstrating >40% relative improvement in the behavioral fingerprint gap, showing effective calibration with minimal synthetic data, and validating downstream alignment. These are within reach if the experiments succeed, though they'd require the method to actually deliver on its promise rather than just being well-framed.

The honest take is that this is a legitimate Findings-level contribution as currently designed, and the score decline reflects realistic assessment of scope rather than paper quality degradation.

I'm noticing the Google Research blog post frames ConvApparel as "bridging" the realism gap, which makes me want to verify whether the paper actually proposes concrete bridging mechanisms or just measures the gap. There's also a meaningful distinction the reviewer raised: ConvApparel targets conversational recommendation systems, not agentic tool-use tasks like τ-Bench, which is a legitimate differentiation worth acknowledging.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5918431-ee59-446d-882a-6556d698cf41",
  "isSidechain": false,
  "requestId": "req_011Cate37cStVu5fLmmKQBT8",
  "type": "assistant",
  "uuid": "6e1054bf-d9fa-4797-9992-4143fd77fa9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GexXM1xZfUeTt7oL94Wr89",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 1727,
      "cache_read_input_tokens": 35583,
      "output_tokens": 1296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 922,
          "output_tokens": 1296,
          "cache_read_input_tokens": 35583,
          "cache_creation_input_tokens": 1727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1727
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T09:19:31.608Z_

Let me also check the Google Research blog post on ConvApparel to understand whether it does more than the abstract suggests:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e1054bf-d9fa-4797-9992-4143fd77fa9e",
  "isSidechain": false,
  "requestId": "req_011Cate37cStVu5fLmmKQBT8",
  "type": "assistant",
  "uuid": "e5c8177d-8ed9-476e-adf6-af24859d0f2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GexXM1xZfUeTt7oL94Wr89",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 1727,
      "cache_read_input_tokens": 35583,
      "output_tokens": 1296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 922,
          "output_tokens": 1296,
          "cache_read_input_tokens": 35583,
          "cache_creation_input_tokens": 1727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1727
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T09:19:32.426Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EQdSZAvX4CCvkQboTRT2aB`</summary>

```json
{
  "url": "https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/",
  "prompt": "What does the paper actually do to 'bridge' the realism gap — does it propose an adaptation methodology, or is bridging only implied through better evaluation/validation? Does it address demographic or dialect groups? What is the exact task domain? Report the key technical contributions precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5c8177d-8ed9-476e-adf6-af24859d0f2f",
  "isSidechain": false,
  "requestId": "req_011Cate37cStVu5fLmmKQBT8",
  "type": "assistant",
  "uuid": "e16bdf3a-51f8-4ce2-83cd-56480ca55fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GexXM1xZfUeTt7oL94Wr89",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 1727,
      "cache_read_input_tokens": 35583,
      "output_tokens": 1296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 922,
          "output_tokens": 1296,
          "cache_read_input_tokens": 35583,
          "cache_creation_input_tokens": 1727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1727
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T09:19:38.211Z_

<details><summary>↩ Tool result · `toolu_01EQdSZAvX4CCvkQboTRT2aB`</summary>

```text
# ConvApparel: Key Technical Contributions

## What "Bridging" Actually Means

The paper does **not** propose an adaptation methodology to improve simulators. Instead, "bridging" refers only to measuring the gap through evaluation. As stated: the framework provides "tools necessary to rigorously measure and, ultimately, bridge this gap," with the authors acknowledging that "determining the precise degree of fidelity needed...remains an open question."

## Exact Task Domain

The work focuses on **Conversational Recommender Systems (CRS)** in apparel shopping, using "over 4,000 human-AI multi-turn conversations (totaling nearly 15,000 turns) in the apparel shopping domain."

## Key Technical Contributions

1. **ConvApparel Dataset**: A human-AI conversation corpus with dual-agent collection ("Good" vs. "Bad" recommenders) and turn-level retrospective annotations capturing satisfaction and frustration.

2. **Three-Pillar Validation Framework**:
   - Population-level statistical alignment comparing behavioral distributions
   - Human-likeness score via trained discriminator
   - Counterfactual validation testing simulator adaptation to unseen "bad agent" behavior

3. **Counterfactual Validation**: Testing whether simulators trained exclusively on "good agent" conversations realistically adapt when encountering the frustrating "bad agent."

## Demographic/Dialect Coverage

The page provides **no information** about demographic diversity, dialect representation, or participant composition beyond noting raters were "paid contractors" above living wage in their country.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e16bdf3a-51f8-4ce2-83cd-56480ca55fab",
  "isSidechain": false,
  "promptId": "7bf5b6f4-2fce-4939-b957-c7f6bd302693",
  "type": "user",
  "uuid": "f89292ad-250b-46aa-95da-2cce14c478b9",
  "toolUseResult": {
    "bytes": 115216,
    "code": 200,
    "codeText": "OK",
    "result": "# ConvApparel: Key Technical Contributions\n\n## What \"Bridging\" Actually Means\n\nThe paper does **not** propose an adaptation methodology to improve simulators. Instead, \"bridging\" refers only to measuring the gap through evaluation. As stated: the framework provides \"tools necessary to rigorously measure and, ultimately, bridge this gap,\" with the authors acknowledging that \"determining the precise degree of fidelity needed...remains an open question.\"\n\n## Exact Task Domain\n\nThe work focuses on **Conversational Recommender Systems (CRS)** in apparel shopping, using \"over 4,000 human-AI multi-turn conversations (totaling nearly 15,000 turns) in the apparel shopping domain.\"\n\n## Key Technical Contributions\n\n1. **ConvApparel Dataset**: A human-AI conversation corpus with dual-agent collection (\"Good\" vs. \"Bad\" recommenders) and turn-level retrospective annotations capturing satisfaction and frustration.\n\n2. **Three-Pillar Validation Framework**:\n   - Population-level statistical alignment comparing behavioral distributions\n   - Human-likeness score via trained discriminator\n   - Counterfactual validation testing simulator adaptation to unseen \"bad agent\" behavior\n\n3. **Counterfactual Validation**: Testing whether simulators trained exclusively on \"good agent\" conversations realistically adapt when encountering the frustrating \"bad agent.\"\n\n## Demographic/Dialect Coverage\n\nThe page provides **no information** about demographic diversity, dialect representation, or participant composition beyond noting raters were \"paid contractors\" above living wage in their country.",
    "durationMs": 5782,
    "url": "https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/"
  },
  "sourceToolAssistantUUID": "e16bdf3a-51f8-4ce2-83cd-56480ca55fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T09:19:55.716Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very clear picture:

**ConvApparel** (Meshi, Goldman et al., EACL 2026; arXiv 2602.16938):
- **Task domain**: Conversational recommendation (apparel shopping), NOT agentic task completion
- **Realism gap**: Measures the gap but does NOT provide adaptation methodology to close it
- **"Bridging"**: Only in the sense of providing better measurement tools; the paper acknowledges determining what fidelity is needed "remains an open question"
- **Demographics/dialects**: No demographic or dialect groups addressed


- **Key differences from DemoCalib**: It operates in a conversational recommendation setting rather than agentic tool-use, validates that data-driven approaches outperform prompting-based ones, but crucially doesn't attempt dialect-specific behavioral calibration or evaluate performance across agentic task-completion scenarios.

The reviewer's one-sentence summary captures this well—ConvApparel measures the realism gap in conversational recommender simulators without providing adaptation methodology for closing that gap across demographic groups, unlike DemoCalib's calibration focus.

Given that this is the only remaining issue and the paper is otherwise submission-ready, I'm going with a minor fix: adding the ConvApparel citation to the related work section near Liu et al.'s realsim work, since both are evaluation-focused user simulation papers that lack adaptation methodology.

Now I'll draft the revised JSON with just this addition. I can see ConvApparel fits naturally with the other evaluation-focused works like Liu et al. — it measures realism gaps without providing adaptation methodology. I'll add it right after Liu et al. in the landscape section, then update the key_references and mark this as a minor change.

Now I'm writing the updated JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f89292ad-250b-46aa-95da-2cce14c478b9",
  "isSidechain": false,
  "requestId": "req_011Cate5UHxR4eSFWUqcGfXc",
  "type": "assistant",
  "uuid": "d8c7b705-98c1-442e-b1e6-47ddf5cc114e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GXRDfr7tjNZbtZLZDR4Cko",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2570,
      "cache_read_input_tokens": 37310,
      "output_tokens": 15788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15788,
          "cache_read_input_tokens": 37310,
          "cache_creation_input_tokens": 2570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2570
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T09:25:28.031Z_

I now have everything I need. ConvApparel:
- Conversational recommendation domain (apparel shopping), **not** agentic tool-use task completion
- Measures and validates the realism gap via a three-pillar framework but explicitly **does not** provide adaptation methodology ("remains an open question")
- **No** demographic or dialect groups addressed
- The reviewer's suggested one-sentence differentiation is accurate verbatim

The fix is genuinely minor: add one sentence to the landscape and one entry to key_references. Given round 9 is the first clean pass with no substantive critiques — and the reviewer explicitly marks the paper submission-ready after this single addition — a minor fix is correct. A pivot would restart the iteration cycle without addressing the structural constraints that the reviewer has already acknowledged are properly framed as limitations.

Here is the complete revised JSON:

```json
{
  "title": "DemoCalib: Data-Efficient Dialect-Behavioral Calibration of LLM User Simulators for Fair Agentic Evaluation",
  "change_type": "minor",
  "core_problem": "LLM user simulators exhibit systematic behavioral miscalibration for dialectal speaker groups in agentic task-completion settings: they are excessively cooperative, over-polite, and question-asking at rates that diverge sharply from real users in groups like AAVE and Indian English speakers. Seshadri et al. (AFAA@ICLR 2026; arXiv 2601.17087) document that AAVE speakers ask questions in only ~10% of turns versus 18.8% for LLM simulators, use politeness markers at ~19.7% versus 39.2%; Indian English speakers (India-based Prolific participants, 18–34 age group) show nearly identical behavioral profiles — 9.9% question rate and 20.1% politeness rate — both groups sharply divergent from simulator baselines. This behavioral miscalibration is not merely noisy: Seshadri et al. report a concrete downstream consequence — AAVE real users achieve approximately 39% agent task-completion rate versus ~49% for SAE speakers; India-based participants achieve approximately 46.2%. If this gap is partly attributable to simulator over-cooperativeness producing artificially inflated success rate estimates for dominant-group speakers, then calibrated simulators should produce success rate estimates closer to the real-user baselines. Seshadri et al. demonstrate in Appendix A.6 that a 'minimal intervention' behavioral constraint prompt (BCP) limiting politeness to 'at most one or two times across the entire conversation' shifts 11 of 18 tasks' difficulty bins and reduces aggregate simulated success rate from 50.0% to 46.7% — partially improving calibration for AAVE, Indian, and Kenyan groups. However, the BCP constrains only politeness frequency, leaving the question-asking rate gap (18.8% simulated vs. ~10% real for both AAVE and Indian English) entirely unaddressed; aggregate success rate remains at 46.7%, far above the AAVE real-user baseline of ~39%. No method exists to adapt a general-purpose LLM simulator's full behavioral distribution to match the empirically observed behavioral profile of a target dialectal group given a small reference sample — addressing both question-asking and politeness dimensions without degrading calibration for other groups — and no prior work has validated such adaptation against downstream agent evaluation consistency. Importantly, because assembling a genuine Prolific reference corpus requires IRB approval and participant recruitment (minimum 6–7 weeks), the framework must be demonstrable via a synthetic pilot that uses empirically-documented behavioral rates from published studies as calibration targets — enabling proof-of-concept results within a typical submission window, with full human validation as a planned follow-up contribution.",
  "opportunity": "'Lost in Simulation' (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) conducted a Prolific-recruited user study (~40 participants per group from the US, India, Kenya, Nigeria) running the full τ-Bench protocol, and documented sharp behavioral gaps between real users and LLM simulators. Critically, Table 6 of Seshadri et al. provides group-level behavioral rate breakdowns for both AAVE and Indian English speakers: AAVE speakers asked questions in only ~10% of turns versus 18.8% for LLM simulators; politeness marker usage was ~19.7% for AAVE real users versus 39.2% for simulators. India-based participants (18–34 age group, the only Indian age cohort recruited due to Prolific availability constraints) asked questions in 9.9% of turns and used politeness markers in 20.1% of turns — strikingly similar to AAVE rates and equally divergent from the 18.8%/39.2% simulator baseline. This convergence of AAVE and Indian English rates, both sharply below simulator baselines, provides a strong empirical foundation for a two-group calibration study: both groups have published target rates from the same study using the same methodology, enabling a direct comparison of calibration difficulty and transferability. Table 3 reports per-group agent success rates: AAVE real users achieved approximately 39% agent task-completion versus approximately 49% for SAE real users; India-based participants achieved approximately 46.2%. These per-group success rates anchor the proxy downstream evaluation: if behavioral miscalibration is a primary driver of biased success rate estimates, calibrated simulators should produce estimates closer to these real-user baselines.\n\nCritically, Seshadri et al. also document (Appendix A.6) a 'minimal intervention': a behavioral constraint prompt (BCP) limiting politeness to 'at most one or two times across the entire conversation' shifts 11 of 18 tasks' difficulty bins and reduces aggregate simulated success rate from 50.0% to 46.7%. The BCP improves simulator calibration for AAVE, Indian, and Kenyan groups but worsens it for SAE and Nigerian participants — demonstrating that a universal politeness constraint is not group-neutral and that single-dimension prompting falls short of full calibration. The BCP constrains only politeness; it leaves the question-asking rate divergence (18.8% simulated vs. ~10% real) entirely unaddressed, and aggregate success rate at 46.7% remains far above the AAVE real-user baseline of ~39%. The Indian English target (~46.2%) is closer to BCP's 46.7% aggregate, but this proximity is coincidental: a group-specific Indian English calibration targeting 9.9% question rate and 20.1% politeness rate requires matching both behavioral dimensions simultaneously and without degrading other groups. DemoCalib extends from BCP's single-dimension prompting to a full data-efficient behavioral distribution matching framework — addressing both dimensions, providing a concrete sample complexity characterization, and enabling group-specific calibration without universal constraint.\n\nAVAVE participants also encountered argument errors at 45.8% versus 32.2% for simulators; the Indian English group showed an Expected Calibration Error (ECE) of 18.9% versus 13.0% for SAE — confirming simulator miscalibration is worst for both groups. These are large effect sizes in agentic task language, far exceeding the ~1.5% demographic-variance figure from SCOPE (arXiv 2601.07110), which measured variance in survey opinion responses, not language-production behavior during task completion. Importantly, the 9-point agent-success-rate variation documented in 'Lost in Simulation' is primarily a model-to-model spread across 31 different LLM simulators; the demographic disparity is a secondary finding: simulated users are differentially unreliable proxies, performing worst for AAVE and Indian English speakers, with disparities compounding with age. 'Mind the Sim2Real Gap' (arXiv 2603.11245, CMU, March 2026) corroborates simulator over-cooperativeness across 451 real participants in aggregate (no per-dialect breakdown) but provides no adaptation method and has no dialect-group-specific rate data. Neither study has released participant interaction logs publicly: Seshadri et al. include no data availability statement or GitHub repository in the paper; 'Mind the Sim2Real Gap' likewise omits a data release. The CC-BY 4.0 license on the Seshadri et al. paper applies to the paper text only, not to participant interaction data — reuse of participant traces requires a separate formal data-sharing agreement and likely participant reconsent for secondary use, a process requiring 4–8 weeks. MirrorBench (arXiv 2601.08118) provides metrics for evaluating human-likeness (MATTR, HD-D, GTEval) without any training signal to produce calibrated simulators. The LLM-based conversational user simulation survey (arXiv 2604.24977) identifies demographic calibration as an open challenge. 'Toward Scalable Verifiable Reward: Proxy State-Based Evaluation for Multi-turn Tool-Calling LLM Agents' (arXiv 2602.16246) demonstrates LLM-driven proxy evaluation for τ-bench-style agentic tasks with >90% human-judge agreement, providing methodological grounding for the proxy downstream evaluation component. Crucially, the published empirical rates from Seshadri et al. Table 6 — AAVE: 10% question rate, ~19.7% politeness rate; Indian English (18–34): 9.9% question rate, 20.1% politeness rate; simulator: 18.8%, 39.2% — provide concrete, IRB-free calibration targets that directly parameterize synthetic reference corpus construction and DPO contrastive pair generation for both groups. The 18–34 age constraint on Indian English participants (a Prolific recruitment limitation in Seshadri et al., not a design choice) means the calibration targets represent younger adult Indian English speakers; age-stratified calibration for Indian English across broader demographics is a planned extension. This synthetic pilot validates the calibration pipeline; a full Prolific human-validation study is planned as a follow-on contribution. Seshadri et al.'s Prolific methodology (racial/ethnic + dialect self-identification screening) has been validated for recruiting AAVE speakers in LLM user studies (corroborated by Black LLMirror at CHI 2026), making the planned human validation study concrete and feasible at ~$1,200–2,200 (~120–180 participants × $7–10 each including platform fees). DialectLLM/MDial (arXiv 2601.22888, KAIST and Amazon, January 2026; updated May 2026) is used as a source of Indian English linguistic transformation rules for synthetic corpus generation in Phase 1 and as Baseline (e) for the Indian English group.",
  "landscape": "The user simulation landscape centers on τ-Bench and related agentic task benchmarks. 'Lost in Simulation' (AFAA Workshop @ ICLR 2026; arXiv 2601.17087) and 'Mind the Sim2Real Gap' (CMU, 2026) both quantify simulator-to-human gaps but provide no adaptation methods and have not released participant data. MirrorBench evaluates human-likeness without producing calibrated simulators. Liu et al. (arXiv 2605.02624, May 2026) propose 'realsim,' an 8-dimensional framework for evaluating user simulation quality across communicative functions, user states, and message surface forms, finding that simulated users systematically underrepresent communication frictions that real users introduce; unlike DemoCalib, it focuses on evaluation metrics rather than adaptation methodology, and does not address dialect-group behavioral calibration. ConvApparel (Meshi et al., EACL 2026; arXiv 2602.16938) measures the realism gap in conversational recommender simulators and validates data-driven approaches over prompting; unlike DemoCalib, it does not address dialect-group-specific behavioral calibration or agentic task-completion evaluation, and provides no adaptation methodology for closing the gap for target demographic groups.\n\nA critical related method emerges from Seshadri et al. themselves: in Appendix A.6, the authors demonstrate a 'Behavioral Constraint Prompt' (BCP) that limits politeness to 'at most one or two times across the entire conversation.' The BCP reduces aggregate simulated success rate from 50.0% to 46.7% and shifts 11 of 18 tasks' difficulty bins, improving calibration for AAVE, Indian, and Kenyan groups while worsening it for SAE and Nigerian participants. The BCP is a zero-compute single-dimension prompting intervention that partially achieves DemoCalib's goal. Its limitations are threefold: (1) it constrains only politeness frequency, leaving the question-asking rate divergence (18.8% simulated vs. ~10% real for both AAVE and Indian English) entirely unaddressed; (2) aggregate success rate at 46.7% remains far above the AAVE real-user baseline (~39%), indicating that politeness-only calibration is insufficient for the hardest miscalibration cases; (3) it applies a universal constraint affecting all groups, degrading calibration for already well-calibrated groups (SAE, Nigerian), whereas DemoCalib provides group-specific calibration. DemoCalib includes BCP as Baseline (f) — extended to constrain both politeness and question rate explicitly — to provide a direct comparison between zero-compute prompting and data-efficient training. This comparison is informative regardless of outcome: if BCP (extended) achieves comparable behavioral rate matching without training, DemoCalib identifies the condition under which prompting suffices; if DPO outperforms extended BCP on held-out test traces and/or proxy downstream evaluation, the paper demonstrates added value of data-efficient training for multi-dimensional behavioral calibration.\n\nSeveral concurrent works partially address related problems but do not close the specific gap:\n\nUserLM-R1 (arXiv 2601.09215, Meituan and collaborating Chinese universities — Meituan, Peking University, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences, Dalian University of Technology — January 2026): The current frontier in user simulation model training. Trains user LMs with multi-reward RL combining rule-based (format, field verification) and rubric-based (reasoning quality, strategic alignment, conversational initiative) reward signals, using Qwen-3 8B/32B base models with adaptive user profiles that combine static persona traits (background, personality, expression style) and dynamic scenario-specific goals. Trained on 90,000 user profiles from AlignX and 450 task SOPs across 6 business scenarios; achieves strong performance particularly on adversarial agent-interaction tasks. Two key distinctions from DemoCalib: (1) UserLM-R1 is explicitly trained on Chinese-language samples with no English dialect or demographic calibration, and does not address the simulator-to-human behavioral gap for any dialect group; (2) it targets strategic reasoning capability and cross-domain generalization rather than matching the behavioral distribution of a specific real dialectal group in English agentic settings. UserLM-R1 is included as Baseline (c): zero-shot with an AAVE/Indian English dialect system prompt, testing whether RL-trained adaptive persona and reasoning capability — without explicit behavioral calibration — closes the miscalibration gap documented by Seshadri et al.\n\nUserLM-8b ('Flipping the Dialogue,' arXiv 2510.06552, NAACL 2025, Microsoft Research): Fine-tunes an 8B model on WildChat for general-conversation user simulation with no dialect-group targeting, no sample complexity analysis, and no downstream agent evaluation consistency metric.\n\nDialectLLM/MDial (arXiv 2601.22888, KAIST and Amazon, January 2026; updated May 2026): Rule-based framework for generating dialect-accurate multi-turn dialogues across 9 English dialects (SAE/US, Australian, British, Canadian, Indian, Irish, Nigerian, Philippine, Scottish) using linguist-curated lexical/orthographic/morphosyntactic transformation rules applied to SAE seed dialogues. Produces DialectLLM-Bench with 50k+ dialogues and 97k+ QA pairs; evaluation of 17 LLMs shows frontier models achieve under 70% dialect accuracy. Three critical distinctions from DemoCalib: (1) DialectLLM targets linguistic form accuracy — surface dialect features in generated text — while DemoCalib targets behavioral interaction dynamics (question rates, politeness frequency, repair patterns) in multi-turn agentic task flows; (2) DialectLLM generates generic conversational exchanges, not agentic task-completion traces under τ-Bench protocol with tool-use and policy constraints; (3) DialectLLM applies rule-based SAE-to-dialect transformation without any feedback loop for behavioral distribution matching. Note: DialectLLM covers Indian English but does not include AAVE among its 9 dialects (Nigerian English is present; AAVE as a US variety requires separate feature sources such as CORAAL and AAVENUE). DialectLLM-conditioned generation is included as Baseline (e) for the Indian English group: applying its IN transformation rules to uncalibrated simulator outputs tests whether rule-based linguistic form calibration alone suffices versus DemoCalib's behavioral distribution matching.\n\nThe PAL framework (arXiv 2511.10215, TACL): Uses DPO for persona-conditioned dialogue generation, optimizing persona alignment in general dialogue rather than matching the behavioral distribution of a specific real dialect group in agentic task settings.\n\nPersoDPO (arXiv 2602.04493, February 2026): Applies DPO with multi-LLM automatic evaluation signals to construct preference pairs for persona-consistent dialogue generation, optimizing for coherence, personalization, and instruction adherence on the FoCus conversational dialogue benchmark. Three distinctions from DemoCalib: (1) PersoDPO targets generic persona consistency (narrative coherence and identity alignment) rather than measurable behavioral rate matching (question-asking frequency, politeness marker frequency) for specific dialect groups; (2) it evaluates on open-domain conversational dialogue rather than multi-turn agentic task-completion under τ-Bench protocol with tool-use and policy constraints; (3) it does not address the simulator-to-human behavioral gap for any dialect group and includes no dialect or demographic variation analysis. PersoDPO is methodologically complementary: DemoCalib extends preference optimization from persona coherence to empirically grounded behavioral rate calibration in agentic evaluation settings.\n\nSocrates/SocSci210 (arXiv 2509.05830, EMNLP 2025, Stanford): Fine-tunes on 2.9M social science experiment responses — a survey/experiment domain rather than multi-turn agentic task completion, and with orders of magnitude more training data than DemoCalib's small-sample setting.\n\nPopulation-Aligned Persona Generation (arXiv 2509.10127, September 2025, Microsoft Research): Methodologically closest prior work — uses importance sampling to align LLM persona distributions to Big Five psychometric reference distributions for social simulation. Operates on self-report survey data (not agentic interaction traces), targets population-level psychometric distributions (not dialect-group behavioral fingerprints), and does not validate against downstream task evaluation consistency.\n\nHUMAINE (arXiv 2603.04409, ICLR 2026): Stratifies the evaluation dataset across 22 demographic groups, calibrating what we measure rather than how we simulate.\n\nSCOPE (arXiv 2601.07110): Argues demographic-only personas explain ~1.5% of variance in survey response similarity — a finding about opinion responses, not the language-production behavioral patterns (question rate, politeness frequency, repair sequences) that differ substantially between dialect groups in agentic task completion.\n\nHaq and Saldías (arXiv 2604.21152, April 2026) study implicit dialect signals (AAVE, Singlish) versus explicit demographic profiles in LLM responses, documenting a 'dialect jailbreak' phenomenon where implicit dialect cues reduce model refusal rates toward near-zero — an input-side bias in how LLMs respond to dialect users, distinct from DemoCalib's simulator-side behavioral calibration, but corroborating that implicit dialect features produce measurable and consequential LLM behavioral differences.\n\nToward Scalable Verifiable Reward (arXiv 2602.16246, 2026): Introduces proxy state-based evaluation for multi-turn tool-calling agents using LLM-driven state tracking and goal-completion judges, achieving >90% human-judge agreement. Provides methodological grounding for the proxy downstream evaluation component of DemoCalib but does not address dialect-group behavioral calibration.\n\nThe gap: given a small reference corpus or empirically-documented target behavioral profile for a specific dialect group, no existing method closes the loop from behavioral fingerprint extraction → simulator adaptation → proxy downstream agent evaluation consistency validation, with quantified sample complexity, in the τ-Bench agentic evaluation context. Seshadri et al.'s BCP (Appendix A.6) represents the strongest prior intervention — zero-compute, sourced from the primary motivating paper — but its single-dimension (politeness-only) scope and universal (non-group-specific) application demonstrate that it falls short of the full calibration problem DemoCalib addresses.",
  "approach": "DemoCalib is a data-efficient framework that adapts a general-purpose LLM simulator (Qwen 2.5 7B-Instruct as primary base model, selected for strong instruction-following capability, extensive open-weight documentation, and active HuggingFace community; Qwen 3.5 9B evaluated as a secondary ablation, contingent on publicly released weights being available on HuggingFace at time of submission) to match the behavioral distribution of a target dialect group. The framework operates in two phases: a proof-of-concept synthetic pilot (primary, 16-day feasible, IRB-free) and a planned human validation study (follow-up, providing downstream agent evaluation consistency validation and a genuine reference corpus contribution).\n\n**Phase 1 — Synthetic Pilot (Primary, Submission-Ready):**\n\nTarget behavioral profiles for each dialect group are directly specified from published empirical rates in Seshadri et al. (AFAA Workshop @ ICLR 2026; arXiv 2601.17087), Table 6: AAVE (question rate = 10% per turn, politeness marker rate = ~19.7%); Indian English (question rate = 9.9% per turn, politeness marker rate = 20.1%; India-based Prolific participants, 18–34 age group — the only Indian English cohort recruited in Seshadri et al. due to platform availability constraints, so calibration targets represent younger adult speakers; age-stratified Indian English calibration is a planned extension); SAE control (uncalibrated simulator baseline rates of 18.8% question rate, 39.2% politeness rate, from the same study).\n\n**Two-Group Design: Testing Cross-Feature Calibration Under Matched Behavioral Targets.** AAVE (10%/~19.7%) and Indian English (9.9%/20.1%) share nearly identical published calibration targets. Rather than treating this as a limitation, the two-group design explicitly tests two questions distinct from differential behavioral fingerprint matching: (a) whether DemoCalib can achieve matched behavioral targets across groups that differ substantially in linguistic surface features — AAVE calibration draws on CORAAL/AAVENUE morphosyntactic features (copula deletion, habitual be, negative concord, preverbal aspect marking), while Indian English calibration uses DialectLLM IN transformation rules (retroflex markers, topic-prominent constructions, distinct lexical items) — and (b) whether calibration difficulty, sample complexity curve, and method effectiveness (DPO vs. retrieval vs. BCP prompting) differ across groups despite identical numerical targets. If calibration converges at different rates or requires different N for AAVE vs. Indian English despite identical targets, this indicates that surface linguistic feature complexity mediates calibration difficulty — a theoretically important finding about the coupling between form and behavioral adaptation. The Indian English group additionally enables unique comparison with Baseline (e) (DialectLLM-conditioned generation), which has no AAVE analogue. This framing is stated explicitly in the paper to preempt the concern that a two-group study with matched targets only tests one behavioral profile: the multi-group contribution is cross-feature calibration under shared targets, not differential fingerprint matching.\n\nA synthetic reference corpus is generated for each group using a dialect-conditioned LLM (GPT-4o or Llama-3.1 70B) prompted with dialect-appropriate system instructions on τ-Bench retail tasks: AAVE instructions are informed by CORAAL-documented morphosyntactic features and AAVENUE benchmark patterns; Indian English instructions use DialectLLM/MDial's (KAIST and Amazon) Indian English transformation rules. This produces 100–200 τ-Bench interaction traces per group (~300–600 total). Generated turns are then post-processed to match target behavioral rates (e.g., excess question-asking turns identified by a simple utterance-type classifier and replaced with non-question continuations until the target rate is achieved). This post-processing step is critical: it prevents the circularity of using LLM-generated corpus to calibrate LLM behavioral rates, since the LLM generator itself exhibits the same over-questioning and over-politeness miscalibration being corrected. Linguistic texture comes from the dialect-conditioned generator; behavioral rates are independently grounded in Seshadri et al.'s published human data.\n\nPost-processing coherence constraint: Each replacement turn must pass a slot-filling consistency check against the task state before being accepted. Specifically, (1) the replacement must not introduce an open question that the agent has already answered in the preceding turn, and (2) it must reference only task variables (product IDs, order numbers, return policies) that have been established in the dialogue history up to that point. This check is implemented as a regex-based slot tracker operating on the τ-Bench structured task state, requiring no additional model calls and adding negligible latency to the post-processing pipeline. Replacement candidates failing this check are discarded and regenerated until a coherent candidate is found or the turn is flagged for manual review.\n\nThe entire generation and post-processing pipeline takes 1–2 days via API calls at ~$20–50 in API costs.\n\nBehavioral fingerprints are extracted from each group's reference traces: question-asking rate per turn, politeness marker frequency (detected via a curated lexicon), turn-length histograms, lexical diversity (MATTR, HD-D), clarification-request frequency, and error-repair patterns. As a validity criterion (not a completed finding), the fingerprint extraction is designed so that fingerprints from the synthetic reference traces should separate dialect groups at >50% 3-class classification accuracy; this threshold confirms that the synthetic corpus exhibits sufficient behavioral divergence to ground calibration. If this criterion is met, the calibration training proceeds as planned. If not, a two-stage contingency applies: (a) First fallback — increase dialect feature density in the generation prompt using stricter CORAAL-derived morphosyntactic constraints for AAVE and more restrictive DialectLLM IN transformation rules for Indian English, then regenerate the corpus and re-evaluate fingerprint classification; (b) Second fallback — if the criterion still fails after corpus revision, reduce the behavioral gap being matched from the full dialect–SAE divergence to the most robustly reproducible subset (e.g., politeness marker rate only, which shows the largest absolute divergence), report partial calibration results, and frame the incomplete fingerprint separation as a substantive finding about the limits of current dialect-conditioned LLM generation — a publishable negative result about the circularity constraint in synthetic dialect calibration. This contingency turns a binary pass/fail into a graceful degradation with interpretable findings at each stage.\n\nMeeting the primary validity criterion demonstrates that behavioral fingerprints in agentic task data capture group differences beyond SCOPE's 1.5% survey-response variance figure — because the behavioral rate targets were independently specified from human data rather than derived from the LLM generator.\n\nTwo calibration strategies are compared: (1) DPO fine-tuning with contrastive pairs opposing reference group turns against uncalibrated simulator outputs on identical task prompts, implemented with LoRA (rank=64) for data-efficient adaptation; (2) retrieval-augmented few-shot conditioning injecting the k most behaviorally similar reference turns as in-context demonstrations at inference time, requiring no gradient updates. Six baselines:\n\n(a) Uncalibrated Qwen 2.5 7B-Instruct with demographic system prompt (HUMAINE-style persona prompting) — the generic demographically-aware prompting baseline;\n\n(b) UserLM-8b conditioned on dialect-group system prompt;\n\n(c) UserLM-R1 (Qwen-3 8B, from Meituan and collaborating Chinese universities, if weights are publicly available at submission time; otherwise approximated as zero-shot Qwen-3 8B with identical dialect system prompt) with AAVE/Indian English dialect system prompt — testing whether RL-trained adaptive persona and reasoning capability without explicit behavioral calibration closes the gap;\n\n(d) Population-Aligned Persona Generation adapted to use behavioral fingerprints instead of Big Five traits for importance sampling;\n\n(e) DialectLLM-conditioned generation (KAIST and Amazon; arXiv 2601.22888) applied to τ-Bench interactions for the Indian English group only (DialectLLM does not cover AAVE), testing whether rule-based linguistic form calibration alone suffices versus DemoCalib's behavioral distribution matching;\n\n(f) Behavioral Constraint Prompt (BCP) — Qwen 2.5 7B-Instruct prompted with explicit per-turn behavioral rate targets derived directly from Seshadri et al. Table 6: 'Ask questions in approximately 10% of turns. Use politeness markers (e.g., please, thank you, sorry) in approximately 20% of turns.' Applied independently to each dialect group (AAVE and Indian English). This extends the 'minimal intervention' documented in Seshadri et al. Appendix A.6 — which constrained only politeness to 'at most one or two times across the entire conversation' and reduced aggregate success rate from 50.0% to 46.7% — to a full two-dimensional behavioral rate constraint. BCP is zero-compute (no training, no data), and is the critical comparison point for assessing whether DemoCalib's DPO fine-tuning adds value over simply encoding target rates in the system prompt. It is also the most natural baseline a reviewer familiar with Seshadri et al. would expect. Expected outcome: BCP achieves partial behavioral rate compliance on both dimensions but produces turns with degraded pragmatic coherence — abrupt non-questions that disrupt task flow — because instruction-following for rate constraints does not guarantee coherent substitution. DemoCalib's DPO/retrieval approach learns the underlying behavioral distribution, producing calibrated turns that maintain agentic pragmatic function. The comparison is informative regardless of direction: if BCP achieves comparable rate matching, DemoCalib identifies the condition under which prompting suffices; if DPO outperforms BCP on fingerprint match rate and/or proxy downstream evaluation, the paper demonstrates the added value of data-efficient training. Note: the Seshadri et al. BCP (politeness-only) worsens calibration for SAE and Nigerian groups while improving for AAVE, Indian, and Kenyan — demonstrating that universal behavioral constraint prompting is not group-neutral. DemoCalib's group-specific calibration avoids this: it targets AAVE and Indian English specifically without requiring a universal constraint applied to all groups.\n\nCalibration quality is validated via MirrorBench metrics (MATTR, HD-D, GTEval), behavioral fingerprint match rate (do calibrated outputs achieve target question/politeness rates on held-out synthetic test traces?), and task-completion preservation (does calibration maintain agentic task functionality?). Sample complexity is characterized by varying reference corpus size from N=10 to N=100 synthetic dialogues, reporting the minimum N needed to achieve fingerprint match within a target threshold — giving practitioners a concrete sample requirement curve for any dialect group.\n\n**Proxy Downstream Evaluation (Within Phase 1, Submission-Ready):**\n\nTo validate that behavioral rate calibration produces consequential changes in agent evaluation outcomes — directly addressing the gap between demonstrating behavioral rate matching and claiming calibration reduces evaluation bias — we run a proxy downstream evaluation within the synthetic pilot, using Seshadri et al.'s published real-user success rates as ground truth. Setup: (1) Fix a single agent (GPT-4o with τ-Bench retail tool access, using the standard τ-Bench retail tool configuration); (2) run N=50 τ-Bench retail task episodes per condition (250 total) using five simulator variants: uncalibrated Qwen 2.5 7B with AAVE demographic system prompt (Baseline a), BCP-extended AAVE simulator (Baseline f), DemoCalib DPO-calibrated AAVE simulator at optimal N, DemoCalib retrieval-augmented AAVE simulator at optimal N, and the DemoCalib DPO-calibrated Indian English simulator at optimal N; (3) compute simulated agent success rate per condition; (4) compare directionally to Seshadri et al.'s published human-grounded baselines: AAVE real users achieved approximately 39% agent task-completion; India-based participants achieved approximately 46.2%; SAE real users achieved approximately 49% — with the AAVE–SAE gap (approximately 10 percentage points) and the India–SAE gap (approximately 3 percentage points) anchoring the fairness claims for their respective groups. Including both real-user baselines — AAVE (~39%) and Indian English (~46.2%) — allows the proxy evaluation to cover both calibration arms: a calibrated AAVE simulator should produce success rate estimates directionally closer to ~39%, while a calibrated Indian English simulator should produce estimates directionally closer to ~46.2%.\n\nHypothesis: uncalibrated simulators, being excessively cooperative (over-polite, over-questioning), give agents more opportunities to clarify intent and recover from errors, artificially inflating estimated success rates above the real-user baselines; BCP (extended, two-dimensional) reduces cooperativeness via prompting but produces less pragmatically coherent turns; DemoCalib calibrated simulators produce behaviorally calibrated, pragmatically coherent interactions, generating success rate estimates directionally closer to the real-user baselines than either the uncalibrated simulator or BCP. Even directional confirmation of this hierarchy (uncalibrated → BCP → DemoCalib, each closer to real-user baselines) validates both that behavioral miscalibration is consequential for downstream evaluation fairness and that data-efficient training adds value over zero-compute prompting. Since we post-process only question rate and politeness frequency, calibration reduces but does not eliminate the full behavioral gap — remaining divergence in argument error rates (AAVE: 45.8% vs. simulator 32.2%) and repair sequences is expected to produce residual sim-real success rate discrepancy, motivating Phase 2. This proxy evaluation draws on the methodology established by 'Toward Scalable Verifiable Reward' (arXiv 2602.16246), which demonstrates LLM-driven proxy state tracking and goal-completion assessment for τ-Bench-style tasks with >90% human-judge agreement.\n\nAgent comparability caveat: Our proxy evaluation fixes GPT-4o with the standard τ-Bench retail tool configuration; Seshadri et al. do not report their exact agent setup, so the directional comparison to their real-user baselines may partly reflect agent-side differences independent of simulator calibration — we treat this comparison as indicative, with full agent-controlled comparison deferred to Phase 2.\n\nAPI cost: ~$75–300 at 250 episodes × $0.30–1.20/episode (GPT-4o agent calls plus simulator inference, including BCP baseline episodes); no GPU required. Runtime: 2–3 days concurrent with main experiment analysis, well within the 16-day pilot window.\n\nContribution claims are scoped explicitly to match results: if directional alignment is confirmed for both groups, the paper claims DemoCalib 'reduces simulation bias in agent success rate estimates for AAVE and Indian English speakers, producing estimates directionally closer to Seshadri et al. real-user baselines, outperforming both uncalibrated prompting and BCP behavioral constraint prompting'; if the proxy evaluation confirms directional improvement over uncalibrated but not over BCP, the paper claims DemoCalib is comparable to zero-compute BCP with the added benefit of behavioral distribution generalization; if the proxy evaluation does not confirm directional alignment, contribution claims are rewritten to strictly address 'behavioral rate matching in simulation,' downstream evaluation consequence is moved entirely to Phase 2, and the absence of directional alignment is itself a substantive finding about the limits of behavioral rate calibration as a proxy for evaluation consequence.\n\n**Sample Complexity and Synthetic Corpus Fidelity Caveats:**\n\nThe N=10–100 sample complexity curve characterizes data efficiency under synthetic-to-synthetic transfer conditions: both the calibration training signal and the held-out test traces are synthetic. Efficiency under real-to-real transfer (Phase 2 Prolific corpus) may differ because genuine human interaction traces exhibit natural behavioral variation beyond the rate targets specified as calibration targets — including idiosyncratic repair sequences, code-switching, and pragmatic patterns not captured by the two-dimensional fingerprint. This caveat is stated explicitly in the paper's limitations section. Phase 2 is the mechanism for characterizing real-to-real sample complexity.\n\nThe post-processing step guarantees target behavioral rates on the two measured dimensions (question rate, politeness frequency); however, other behavioral dimensions in the synthetic corpus — including code-switching patterns, error-repair sequences, pragmatic hedging, and clarification phrasing — remain subject to the same LLM miscalibration that the framework aims to correct, and may not fully reflect real AAVE or Indian English speaker patterns. Specifically, dialect-conditioned LLM generators that over-ask questions in unconditioned settings may also produce stylistically uniform repair sequences and formulaic hedging that differs from naturally occurring AAVE or Indian English pragmatic variation. Phase 2 human validation is the mechanism for assessing the full scope of behavioral fidelity beyond the two post-processed rate dimensions — the comparison between synthetic-corpus-calibrated and human-corpus-calibrated simulators in Phase 2 will directly quantify the gap introduced by uncontrolled LLM miscalibration on non-post-processed behavioral dimensions.\n\n**Phase 2 — Human Validation (Planned, Post-Submission):**\n\nA Prolific study following the validated Seshadri et al. (AFAA Workshop @ ICLR 2026) methodology recruits AAVE speakers (~40–60, US-based), Indian English speakers (~40–60, India-based, spanning a broader age range than Seshadri et al.'s 18–34 constraint), and SAE controls (~40), each completing 4 τ-Bench retail tasks (order management, product inquiry, return processing, cancellation), yielding 160–240 real interaction dialogues per group at ~$1,200–2,200 total. This study provides: (a) a genuine human reference corpus replacing the synthetic corpus (enabling direct comparison of synthetic vs. human reference corpus calibration quality and real-to-real sample complexity), (b) downstream agent evaluation consistency validation — calibrated-simulator-estimated agent success rate versus real-user success rate on held-out τ-Bench tasks using a matched agent configuration, targeting reduction of the sim-real behavioral calibration gap documented by Seshadri et al., (c) age-stratified Indian English behavioral rates beyond the 18–34 window, and (d) a public curated dataset contribution (AAVE and Indian English τ-Bench interaction traces). If Prolific data is available by camera-ready deadline, it upgrades the submission scope and supports a Main track revision.\n\nRegarding Seshadri et al. data access: We will contact the authors to request participant interaction traces under a formal institutional data sharing agreement for academic reuse (separate from the CC-BY 4.0 paper license, which applies only to paper text). This process requires institutional review and participant anonymization protocols and cannot be treated as a reliable fast-track. It is pursued opportunistically; if granted, Seshadri et al. traces would serve as an independent validation set.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h A100 80GB",
      "gpu_utilization": "LOW-MODERATE (~40–50%): GPU idles during synthetic corpus generation (days 1–2, primarily LLM API calls), behavioral fingerprint extraction, DPO pair curation, code development, and result analysis between experiment runs. BCP baseline (f) runs via API with no GPU cost. Primary advantage over prior version: no IRB wait or Prolific recruitment gates the start of the GPU-intensive phase.",
      "timeline": "2–4 months for synthetic pilot (including proxy downstream evaluation with BCP comparison); Prolific human validation adds 4–8 weeks as a parallel follow-on once submission is in",
      "team": "2 researchers",
      "data_collection_cost": "$20–50 (synthetic corpus generation via LLM API, ~300–600 τ-Bench dialogues); $75–300 (proxy downstream evaluation: 250 τ-Bench episodes × $0.30–1.20/episode including BCP baseline, no GPU required); $1,200–2,200 for planned Prolific human validation study (separate, post-submission)",
      "estimated_gpu_cost": "$170–200 (at ~$1.50/h via Vast.ai spot market)"
    },
    "human_in_loop": {
      "gpu_hours": "~200h A100 80GB",
      "gpu_utilization": "MODERATE (~55–65%): Agent batches DPO runs (3 groups × 3 sample sizes × 2 configs = 18 runs × ~6h each = 108h), few-shot sweeps, and τ-Bench evaluation passes; human approval gates (~30 min/day) replace idle phases. Synthetic corpus generation completes in days 1–2 before GPU-intensive phase begins with no external dependency. BCP baseline (f) and proxy downstream evaluation (250 episodes) run via API concurrently with DPO analysis, requiring no GPU.",
      "timeline": "1–2 months (no external IRB or recruitment dependency gates the primary synthetic pilot path)",
      "team": "1 researcher, ~30 min/day check-in for experiment approval and direction",
      "claude_api_cost": "$100–200 (~1,500 turns × $0.10/turn for experiment orchestration over 1–2 months)",
      "estimated_gpu_cost": "$280–320 (at ~$1.50/h)",
      "data_collection_cost": "$20–50 (synthetic corpus generation); $75–300 (proxy downstream evaluation including BCP baseline, API only); $1,200–2,200 for planned Prolific study (post-submission, human-initiated)",
      "risk_note": "Primary risks: (1) UserLM-R1 weights may not be publicly released at submission time — fall back to zero-shot Qwen-3 8B with dialect prompt, with reduced baseline fidelity noted in the paper; (2) validity criterion (>50% 3-class fingerprint classification accuracy) may fail on synthetic corpus — two-stage contingency in place; (3) BCP (Baseline f) may match behavioral rates comparably to DemoCalib — reframe contribution as identifying conditions under which zero-compute prompting suffices versus data-efficient training, both outcomes publishable; (4) proxy downstream evaluation may not show directional alignment — contribution claims reframed as behavioral rate matching; (5) early few-shot sweep (days 3–5) recommended to check whether retrieval-augmented conditioning achieves comparable calibration without DPO compute, enabling grid pruning."
    },
    "auto_research": {
      "gpu_hours": "~360h A100 80GB (full grid: 3 groups × 6 baselines × 4 sample sizes × 2 DPO hyperparameter configs + evaluation sweeps; ≈180h H100-equivalent, within 200h H100 budget)",
      "gpu_utilization": "HIGH (~85–90%): Continuous experiment queue with no human-induced idle; agents schedule synthetic corpus generation (days 1–2), DPO runs, few-shot sweeps, τ-Bench evaluation passes, BCP baseline API runs, and proxy downstream evaluation API calls back-to-back across 4–6 parallel A100s",
      "timeline": "3–5 days with 4–6 parallel A100s (each Qwen 2.5 7B LoRA-DPO run: ~6h on one A100 80GB); BCP baseline and proxy downstream evaluation (250 episodes) run concurrently via API from day 3 onward",
      "team": "0 (initial setup only: ~3h to configure synthetic corpus generation pipeline, post-processing scripts, experiment manifests, BCP baseline harness, proxy downstream evaluation harness, and evaluation harness; no IRB step required for primary path)",
      "claude_api_cost": "$200–350 (~2,500 turns × $0.10/turn for experiment orchestration, result synthesis, and draft writing)",
      "estimated_gpu_cost": "$520–560 (at ~$1.50/h)",
      "data_collection_cost": "$20–50 (synthetic corpus generation); $75–300 (proxy downstream evaluation including BCP baseline episodes, API only); Prolific human validation ($1,200–2,200) is post-submission and human-initiated",
      "speed_bottleneck": "Purely compute-bound: synthetic corpus generation completes in days 1–2 (API-rate-limited, not GPU-limited); BCP baseline runs can be scheduled immediately alongside corpus generation (no GPU required); GPU phase starts day 2; proxy downstream evaluation API calls begin day 3 concurrent with DPO analysis. If UserLM-R1 weights are unavailable, baseline (c) falls back to zero-shot Qwen-3 8B — agent should detect via HuggingFace availability check and handle the fallback automatically.",
      "risk_note": "Primary risk: agent invests in full DPO grid before discovering retrieval-augmented conditioning or BCP achieves comparable calibration at zero/minimal compute. A human checkpoint at day 2 (post-initial few-shot and BCP results) is strongly recommended to prune DPO configurations. Secondary risk: validity criterion (>50% fingerprint classification accuracy) may not be met — two-stage contingency in place. Tertiary risk: proxy downstream evaluation may not show directional alignment — contribution claims are reframed as behavioral rate matching only, null finding is reported, Phase 2 resolves downstream validation. Agent should surface BCP baseline results, fingerprint classification results, and initial proxy evaluation results at day 3 checkpoint before committing full DPO compute."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ACL Rolling Review, ongoing cycles; primary target — synthetic pilot with proxy downstream evaluation including BCP comparison and planned human validation is well-matched to Findings scope; novel end-to-end framework with proof-of-concept results and clear empirical grounding in two dialect groups)",
    "EMNLP 2026 Main (stretch target; requires all three upside conditions: (1) calibrated simulator reduces sim-real behavioral fingerprint gap by >40% relative versus best baseline including BCP; (2) sample complexity curve shows effective calibration at N≤20 synthetic dialogues; (3) proxy downstream evaluation confirms directional alignment between calibrated simulator success rate estimates and Seshadri et al.'s real-user baselines for both AAVE (~39%) and Indian English (~46.2%))",
    "AAAI 2027 (submission deadline expected July–August 2026; if Prolific validation study is complete by then, downstream agent evaluation consistency results substantially strengthen the submission)",
    "CHI 2027 (submission deadline September 10, 2026; HCI + fair evaluation angle; Prolific human validation data and equitable agentic AI evaluation framing align with CHI scope)"
  ],
  "level": "solid",
  "key_references": [
    "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) — primary source for AAVE behavioral rates (~10% question, ~19.7% politeness), Indian English rates (9.9%/20.1%, Table 6, 18–34 age group), per-group agent success rates (AAVE ~39%, India ~46.2%, SAE ~49%, Table 3), and Appendix A.6 'minimal intervention' BCP (politeness-only constraint reducing aggregate success rate 50.0%→46.7%, shifting 11/18 task difficulty bins, improving calibration for AAVE/Indian/Kenyan but worsening for SAE/Nigerian). Accepted as oral at the ICLR 2026 Workshop on Algorithmic Fairness Across Alignment Procedures and Agentic Systems (AFAA).",
    "Mind the Sim2Real Gap in User Simulation for Agentic Tasks (arXiv 2603.11245, CMU, March 2026) — corroborates aggregate simulator over-cooperativeness across 451 participants; no per-dialect breakdown",
    "MirrorBench: An Extensible Framework to Evaluate User-Proxy Agents for Human-Likeness (arXiv 2601.08118, 2026)",
    "Synthetic Users, Real Differences: an Evaluation Framework for User Simulation in Multi-Turn Conversations (Liu et al., arXiv 2605.02624, May 2026) — proposes 'realsim,' an 8-dimensional framework for evaluating user simulation quality across communicative functions, user states, and message surface forms; evaluation-focused concurrent work that does not provide adaptation methodology or address dialect-group behavioral calibration",
    "ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders (Meshi, Goldman et al., EACL 2026; arXiv 2602.16938; aclanthology.org/2026.eacl-long.244) — introduces a validation framework measuring the 'realism gap' in conversational recommender simulators and demonstrates that data-driven simulators outperform prompted baselines; unlike DemoCalib, it does not address dialect-group-specific behavioral calibration or agentic task-completion evaluation, and provides no adaptation methodology for closing the gap for target demographic groups",
    "Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles (Haq and Saldías, arXiv 2604.21152, April 2026) — documents a 'dialect jailbreak' phenomenon in AAVE and Singlish where implicit dialect cues reduce LLM refusal rates toward near-zero; input-side bias study adjacent to DemoCalib's simulator-side calibration, corroborating that implicit dialect features produce measurable and consequential LLM behavioral differences",
    "The Need for a Socially-Grounded Persona Framework for User Simulation — SCOPE (arXiv 2601.07110, January 2026)",
    "A Survey on LLM-based Conversational User Simulation (arXiv 2604.24977, EACL 2026)",
    "τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (arXiv 2406.12045, 2024)",
    "Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework (arXiv 2603.04409, ICLR 2026)",
    "Toward Scalable Verifiable Reward: Proxy State-Based Evaluation for Multi-turn Tool-Calling LLM Agents (arXiv 2602.16246, 2026) — methodological grounding for LLM-driven proxy evaluation in τ-bench-style settings; >90% human-judge agreement",
    "UserLM-R1: Modeling Human Reasoning in User Language Models with Multi-Reward Reinforcement Learning (arXiv 2601.09215, Meituan, Peking University, Beijing University of Posts and Telecommunications, University of Chinese Academy of Sciences, Dalian University of Technology, January 2026)",
    "Flipping the Dialogue: Training and Evaluating User Language Models — UserLM-8b (Naous et al., arXiv 2510.06552, NAACL 2025, Microsoft Research)",
    "DialectLLM: A Dialect-Aware Dialogue Generation Framework Beyond Standard American English (arXiv 2601.22888, KAIST and Amazon, January 2026) — first author Jio Oh (KAIST and Amazon); rule-based dialect transformation across 9 English dialects including Indian English; used as Baseline (e) and for Indian English corpus generation",
    "Persona-Aware Alignment Framework for Personalized Dialogue Generation — PAL (arXiv 2511.10215, TACL 2025)",
    "PersoDPO: Scalable Preference Optimization for Instruction-Adherent, Persona-Grounded Dialogue via Multi-LLM Evaluation (arXiv 2602.04493, February 2026) — applies DPO with multi-LLM evaluation signals for coherence, personalization, and instruction adherence in open-domain conversational dialogue (FoCus dataset); no dialect-group targeting, no behavioral rate matching, no agentic task evaluation",
    "Finetuning LLMs for Human Behavior Prediction in Social Science Experiments — Socrates/SocSci210 (Kolluri et al., EMNLP 2025; arXiv 2509.05830)",
    "Population-Aligned Persona Generation for LLM-based Social Simulation (arXiv 2509.10127, Microsoft Research, September 2025)",
    "Direct Preference Optimization: Your Language Model is Secretly a Reward Model (Rafailov et al., NeurIPS 2023)",
    "Evaluating Large Language Models as Generative User Simulators for Conversational Recommendation (arXiv 2403.09738)",
    "AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark (arXiv 2024)",
    "EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models (EMNLP 2025)",
    "Black LLMirror: User (Self) Perceptions in Black American English Interactions with LLMs (CHI 2026)",
    "Corpus of Regional African American Language — CORAAL (oraal.github.io/coraal; Version 2023.06)"
  ],
  "description": "LLM user simulators are systematically miscalibrated for dialect-group speakers in agentic settings: 'Lost in Simulation' (Seshadri et al., AFAA Workshop @ ICLR 2026; arXiv 2601.17087) documents in Table 6 that AAVE speakers ask questions in only ~10% of turns versus 18.8% for LLM simulators, use politeness markers at ~19.7% versus 39.2%; and India-based participants (18–34 age group) show nearly identical behavioral profiles — 9.9% question rate and 20.1% politeness rate — both groups far below simulator baselines. Table 3 reports per-group agent success rates anchoring the downstream evaluation: AAVE real users achieved approximately 39% agent task-completion; India-based participants achieved approximately 46.2%; SAE real users achieved approximately 49%. Seshadri et al. also demonstrate in Appendix A.6 a 'minimal intervention' Behavioral Constraint Prompt (BCP) that limits politeness to 'at most one or two times across the entire conversation,' reducing aggregate simulated success rate from 50.0% to 46.7% and shifting 11 of 18 task difficulty bins — but this single-dimension (politeness-only) universal constraint leaves question-asking rate divergence unaddressed, fails to reach the AAVE real-user baseline (~39%), and worsens calibration for SAE and Nigerian groups. We propose DemoCalib, a data-efficient framework that adapts a Qwen 2.5 7B-Instruct simulator to a target dialect group using a small reference corpus, calibrating both behavioral dimensions simultaneously with group-specific targeting. Because assembling a genuine Prolific reference corpus requires IRB approval and participant recruitment (minimum 6–7 weeks), the primary submission-ready evaluation uses a synthetic reference corpus: target behavioral profiles are directly specified from published empirical rates (Seshadri et al. Table 6: AAVE 10%/~19.7% question/politeness rates; Indian English 9.9%/20.1%), and dialect-conditioned LLM traces on τ-Bench tasks (AAVE: prompted using CORAAL/AAVENUE-documented features; Indian English: using DialectLLM's IN transformation rules from KAIST and Amazon, arXiv 2601.22888) provide linguistic texture, with turns post-processed to match behavioral rate targets — avoiding the circularity of deriving LLM behavioral targets from LLM-generated data. A coherence constraint ensures replaced turns do not introduce questions already answered by the agent or reference task variables not yet established in the dialogue state, implemented as a lightweight regex-based slot tracker. Post-processing guarantees target behavioral rates on the two measured dimensions (question rate, politeness frequency); other behavioral dimensions — including code-switching patterns, error-repair sequences, pragmatic hedging, and clarification phrasing — remain subject to LLM miscalibration and may not fully reflect real AAVE or Indian English speaker patterns; Phase 2 human validation is the mechanism for assessing full behavioral fidelity beyond these two post-processed dimensions. The two-group design does not test whether DemoCalib can match distinct behavioral fingerprints (AAVE and Indian English have nearly identical published targets: 10%/9.9% question, ~19.7%/20.1% politeness). Instead, it tests whether DemoCalib achieves matched behavioral targets across groups that differ in linguistic surface features (CORAAL/AAVENUE features for AAVE vs. DialectLLM IN rules for Indian English), and whether calibration difficulty or method effectiveness differs across groups despite identical numerical targets — a question with theoretical implications for the coupling between form and behavioral adaptation. A full Prolific human validation study (40–60 participants/group × 3 groups × 4 tasks, ~$1,200–2,200) is planned post-submission for downstream agent evaluation consistency validation and to extend Indian English calibration beyond the 18–34 age window. Behavioral fingerprints (question rate, politeness frequency, MATTR, repair patterns) are extracted from reference traces; as a validity criterion, these fingerprints are designed to separate dialect groups at >50% 3-class classification accuracy; if this fails, a two-stage contingency applies. Two calibration strategies are compared: DPO fine-tuning with contrastive demographic pairs (LoRA-efficient), and retrieval-augmented few-shot conditioning requiring no gradient updates. Six baselines: (a) uncalibrated simulator with demographic system prompt, (b) UserLM-8b with dialect steering, (c) UserLM-R1 (Meituan et al., Qwen-3 8B) with dialect system prompt — testing whether RL-trained adaptive persona reasoning without explicit behavioral calibration closes the gap, (d) Population-Aligned Persona Generation adapted to behavioral fingerprints, (e) DialectLLM-conditioned generation (KAIST and Amazon) for Indian English only — testing whether rule-based linguistic form calibration suffices versus DemoCalib's behavioral distribution matching, (f) Behavioral Constraint Prompt (BCP) — zero-compute two-dimensional rate-targeting system prompt extending Seshadri et al.'s Appendix A.6 minimal intervention to include both question rate (~10%) and politeness rate (~20%) constraints — the critical test of whether DemoCalib's training-based approach adds value over prompting. The BCP comparison is informative regardless of direction: if BCP matches rates comparably to DemoCalib, the paper identifies when zero-compute prompting suffices; if DPO outperforms BCP, the paper demonstrates added value of data-efficient training for multi-dimensional behavioral calibration, and can point to BCP's known failure on pragmatic coherence. Sample complexity is characterized across N=10–100 reference dialogues. The proxy downstream evaluation runs 250 τ-Bench retail task episodes (50 per condition: uncalibrated, BCP, DemoCalib-DPO, DemoCalib-retrieval for AAVE; DemoCalib-DPO for Indian English) with a fixed GPT-4o agent, comparing calibrated and uncalibrated simulator success rate estimates directionally against both real-user baselines — AAVE (~39%) and Indian English (~46.2%) — from Seshadri et al. Tables 3 and 6. Contribution claims are scoped to match results: directional hierarchy (uncalibrated → BCP → DemoCalib, each closer to real-user baselines) confirms behavioral miscalibration is consequential and data-efficient training adds value over zero-compute prompting; partial confirmation and null results are reported as substantive findings. DemoCalib is the first end-to-end calibration procedure for dialect-group behavioral distribution matching in agentic task evaluation, grounded in published empirical rates for two dialect groups from the same Prolific study, with a proxy downstream evaluation anchored to published real-user success rate baselines for both groups, and with an explicit comparison to the strongest zero-compute prompting baseline available in the literature.",
  "project_name": "demo_calibrated_sim",
  "source": "web_research"
}
```

---

**What changed and why:** Single addition — ConvApparel (arXiv 2602.16938, EACL 2026) added to the `landscape` section (one sentence after Liu et al./realsim, the natural grouping of evaluation-framework-only works) and to `key_references`. The differentiation is precise: ConvApparel measures the realism gap in conversational recommendation, demonstrates data-driven > prompted, but explicitly provides no adaptation methodology and addresses no dialect or demographic groups — complementary to DemoCalib without overlapping its contribution. All other content is unchanged. `change_type: "minor"`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8c7b705-98c1-442e-b1e6-47ddf5cc114e",
  "isSidechain": false,
  "requestId": "req_011Cate5UHxR4eSFWUqcGfXc",
  "type": "assistant",
  "uuid": "d0545838-ae3c-4bbb-b4fb-a567907c1585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GXRDfr7tjNZbtZLZDR4Cko",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2570,
      "cache_read_input_tokens": 37310,
      "output_tokens": 15788,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15788,
          "cache_read_input_tokens": 37310,
          "cache_creation_input_tokens": 2570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2570
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"DemoCalib: Data-Efficient Dialect-Behavioral Calibration of LLM User S…",
  "leafUuid": "d0545838-ae3c-4bbb-b4fb-a567907c1585",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibrating LLM user simulators for dialect groups in agentic evaluation",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"DemoCalib: Data-Efficient Dialect-Behavioral Calibration of LLM User S…",
  "leafUuid": "d0545838-ae3c-4bbb-b4fb-a567907c1585",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibrating LLM user simulators for dialect groups in agentic evaluation",
  "sessionId": "365e0176-961c-40cc-a37e-0044c1093d8b"
}
```

---
