# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "tit

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 113
- **Recorded user turns:** 9
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d.jsonl`
- **Structured JSON:** [`e3c3fefec3008c814615.json`](../../sessions/e3/e3c3fefec3008c814615.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T03:24:53.670Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:24:53.670Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Multimodal Scientific Reasoning\",\n  \"core_problem\": \"Reinforcement learning with structured rewards has advanced rapidly for verifiable multimodal tasks (PaLMR, SR-MCR, Chart-RL) and non-verifiable text-only tasks (Rubric-ARM, Writing-Zero, RubricEM), and even non-verifiable image captioning (RubiCap). However, a critical domain remains unaddressed: graded scientific visual reasoning — tasks like scientific figure explanation generation, visual argument assessment, and figure-based analytical interpretation — where (a) no single correct answer exists, (b) evaluation requires domain-specific rubrics, and (c) visual grounding quality directly conditions reasoning quality. Existing non-verifiable multimodal RL (RubiCap) targets captioning, not scientific reasoning; existing gated multimodal rewards (PaLMR) target verifiable answer correctness, not graded explanation quality. The intersection — gated structured rewards for non-verifiable scientific multimodal reasoning — remains unexplored.\",\n  \"opportunity\": \"The landscape reveals a clear gap at the intersection of two well-explored axes. Axis 1: Gated/hierarchical rewards for multimodal RL exist (PaLMR gates answer rewards on visual fidelity; SR-MCR combines five sub-rewards; V-Triune uses sample-level reward routing) but exclusively for verifiable tasks with binary correctness. Axis 2: Rubric-based RL for non-verifiable tasks exists (RubiCap for captioning, Rubric-ARM for text instruction-following, RubricEM for deep research) but either operates in text-only settings or on general captioning without scientific domain structure. The crucial insight: scientific visual reasoning exhibits a unique property — visual grounding quality is a NECESSARY CONDITION for reasoning quality (you cannot produce a valid scientific explanation of a figure you misperceive), creating a natural gating hierarchy. PaLMR demonstrated this gating principle for verifiable tasks (binary visual fidelity → answer reward). We extend it to non-verifiable settings where each tier produces continuous graded scores from domain rubrics, not binary checks. The 'Reward Design for Physical Reasoning in VLMs' (arXiv:2604.13993) found accuracy rewards outperform flat composite rubric rewards on verifiable tasks — but this is expected because accuracy provides a strong, unambiguous signal. In non-verifiable settings, accuracy is UNAVAILABLE; the comparison becomes gated rubric vs. flat rubric vs. no rubric, where gating's curriculum effect (grounded in the 'Implicit Curriculum' theory, arXiv:2602.14872) should prevent the 'eloquent hallucination' failure mode — visually ungrounded but linguistically polished explanations that flat rewards cannot penalize.\",\n  \"landscape\": \"VERIFIABLE MULTIMODAL + STRUCTURED REWARDS: PaLMR (arXiv:2603.06652, Feb 2026) uses gated hierarchical reward R = S_vis · (α·S_ans + (1-α)·S_fmt) where binary visual fidelity gates answer reward — closest to our gating principle but for verifiable tasks with binary visual check. SR-MCR (arXiv:2512.22545, Dec 2025) integrates five self-referential sub-rewards (semantic alignment, lexical fidelity, non-redundancy, visual grounding, step consistency) with GRPO — multi-component but flat combination on verifiable tasks. RuCL (arXiv:2602.21628, Feb 2026) implements stratified rubric-based curriculum progressing perception→reasoning on multimodal — dynamic rubric weighting but still verifiable benchmarks. Vision-SR1 (arXiv:2508.19652, Aug 2025) decomposes VLM reasoning into visual perception and language reasoning with self-rewarding — verifiable tasks. Vero (arXiv:2604.04917, Apr 2026) uses task-routed rewards across 59 datasets — broad but verifiable. V-Triune (arXiv:2505.18129, May 2026) sample-level reward routing for unified multimodal RL — verifiable. Chart-RL (arXiv:2603.06958, Mar 2026) applies RLVR to chart reasoning — verifiable. PEARL (CVPR 2026) dual-branch perception-reasoning but binary outcome gate. CogFlow (ICLR 2026) Visual-Gated Policy Optimization — binary answer reward. Faithful GRPO (arXiv:2604.08476, Apr 2026) constrains policy for visual grounding — verifiable spatial tasks. NON-VERIFIABLE + STRUCTURED REWARDS (TEXT-ONLY): Rubric-ARM (arXiv:2602.01511, Feb 2026) alternating RL for rubric-based reward modeling — text-only non-verifiable. Writing-Zero (arXiv:2506.00103) bridges non-verifiable tasks via pairwise GenRM — text-only. Rubric-Grounded RL (arXiv:2605.08061, May 2026) decomposes reward via LLM-judge rubrics — text-only. RubricEM (arXiv:2605.10899, May 2026) meta-RL with rubric-guided policy decomposition for deep research agents — text-only. PrefBERT/Semantically-Aware Rewards (arXiv:2506.15068) for open-ended free-form generation — text-only. NON-VERIFIABLE MULTIMODAL: RubiCap (arXiv:2603.09160, Mar 2026) applies rubric-guided RL to dense image captioning with LLM-written rubrics — closest multimodal non-verifiable work but targets general captioning, not scientific reasoning, and uses dynamically generated instance-level rubrics without gating. CapRL (ICLR 2026) uses VQA-based proxy verifiable reward for captioning. BalCapRL (Mar 2026) balanced multi-objective RL for captioning. NEGATIVE RESULTS: 'Reward Design for Physical Reasoning in VLMs' (arXiv:2604.13993, Apr 2026) found accuracy-based rewards outperform flat composite rubric rewards on verifiable physics tasks — motivates our focus on non-verifiable settings where accuracy is unavailable. 'LLMs Gaming Verifiers' (arXiv 2026) shows reward hacking exploits what verifiers fail to enforce — motivates our gating to prevent exploitation of higher-tier rewards through ungrounded reasoning. THE GAP: No work applies gated/hierarchical structured rewards to non-verifiable scientific multimodal reasoning tasks where visual grounding quality should condition reasoning quality evaluation.\",\n  \"inspired_by\": \"Intersection gap: structured reward RL exists for (verifiable multimodal) and (non-verifiable text-only) and (non-verifiable captioning), but NOT for (non-verifiable scientific multimodal reasoning). Innovation pattern: 'Principled Extension' — take PaLMR's gating principle (proven for verifiable tasks) and Rubric-ARM/RubiCap's rubric principle (proven for non-verifiable tasks) and combine them for the scientifically important domain of graded visual reasoning. Theoretical grounding: the 'Implicit Curriculum' paper (arXiv:2602.14872) shows RLVR naturally creates easy→hard curriculum; our gating makes this explicit and domain-appropriate for scientific reasoning. Building block: GRPO's compatibility with multi-reward designs (proven by SR-MCR, Vero, V-Triune) makes it the natural optimization backbone.\",\n  \"approach\": \"We propose GatedRubric-GRPO, which extends gated structured rewards to non-verifiable multimodal scientific reasoning within standard GRPO training on a 7-8B VLM (Qwen3-VL-8B). The framework decomposes evaluation into three gated tiers, generalizing PaLMR's binary gating to continuous graded rubric scores. Tier-1 (Visual Grounding, continuous 0-1): programmatic and lightweight LLM checks assess whether the response correctly references visual elements present in the figure — element identification accuracy, spatial description consistency, and data reading fidelity — producing a continuous score (NOT binary like PaLMR's S_vis). Tier-2 (Structural Quality, gated on Tier-1 ≥ τ₁): a frozen LLM judge (Qwen3-32B) evaluates logical coherence, evidence-claim alignment, domain terminology appropriateness, and visual-textual consistency using domain-specific rubric templates designed per scientific discipline. Activated only when Tier-1 exceeds threshold τ₁, preventing reward for structurally polished but visually ungrounded explanations. Tier-3 (Reasoning Quality, gated on Tier-2 ≥ τ₂): bootstrapped pairwise comparison within GRPO rollout groups assesses analytical depth, interpretive insight, explanation completeness, and critical assessment quality — extending Writing-Zero's BRPO to multimodal. Activated only when Tier-2 exceeds τ₂. The composite reward is R = w₁·R₁ + w₂·𝟙(R₁≥τ₁)·R₂ + w₃·𝟙(R₁≥τ₁)·𝟙(R₂≥τ₂)·R₃. TRAINING TASKS (genuinely non-verifiable): (1) Scientific figure explanation generation using MMSci (Nature Communications figures, 72 disciplines) — given a figure, generate a comprehensive scientific explanation evaluated by multi-dimensional rubric; (2) Open-ended scientific graph analysis using SciGraphQA re-annotated with rubric scoring (replacing CIDEr/BLEU) — given a graph and question, provide detailed analytical interpretation; (3) Scientific figure critique construction: a new benchmark of ~2K figure-critique pairs from diverse ArXiv papers, with LLM-generated rubric annotations validated by domain experts on a 20% subset. CONTROLLED COMPARISON (verifiable baselines): CharXiv and SciFIBench used as controlled comparisons to demonstrate WHERE binary rewards suffice versus where rubric rewards add value, directly addressing the verifiable/non-verifiable boundary. KEY ABLATIONS to isolate gating contribution: (A1) flat composite: R = w₁·R₁ + w₂·R₂ + w₃·R₃ (no gating); (A2) dynamic weighting à la RuCL (rubric weights adjust during training); (A3) PaLMR-style binary gating (R₁ binarized); (A4) Tier-1+2 only (no reasoning quality); (A5) Tier-1+3 only (no structural quality). This ablation suite directly tests whether gated > flat composite (addressing the negative result from Reward Design for Physical Reasoning, which tested FLAT composite on VERIFIABLE tasks) and whether continuous gating > binary gating. THEORETICAL MOTIVATION: (1) Gradient interference: in flat composite rewards, high reasoning fluency can compensate for poor visual grounding, creating conflicting gradient signals; gating eliminates this by zeroing higher-tier gradients when grounding is insufficient. (2) Explicit curriculum: gating implements a controlled version of the implicit curriculum discovered in RLVR training dynamics (arXiv:2602.14872), appropriate for the perception→structure→reasoning progression in scientific analysis. (3) Anti-hacking: gating specifically prevents the 'eloquent hallucination' failure mode where models generate well-structured but visually ungrounded scientific explanations — the multimodal analogue of the reward hacking patterns identified by 'LLMs Gaming Verifiers.'\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"900-1200 (8×H100: ~100h LLM-based rubric annotation with 32B judge on ~10K examples, ~450h main GatedRubric-GRPO training and ablation suite across 3 tiers and 5 ablation conditions, ~150h baseline reproductions including RubiCap/PaLMR-style baselines, ~150h evaluation and analysis)\",\n      \"human_annotation\": \"~500 person-hours domain expert validation (20% of rubric annotations, 3 annotators × ~500 examples × 20 min each, ~$12K at expert rates)\",\n      \"timeline\": \"4-5 months (5 weeks dataset curation with LLM-assisted rubric annotation + expert validation, 3 weeks baseline implementation, 6 weeks GatedRubric-GRPO training and full ablation suite, 4 weeks evaluation and paper writing)\",\n      \"estimated_gpu_cost\": \"$1,800-$3,000 (at $2-2.50/H100-hr spot pricing)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"700-900 (Claude generates rubric templates, annotation pipelines, and ablation configurations; human validates scientific accuracy of graded annotations on 20% subset)\",\n      \"human_annotation\": \"~300 person-hours expert validation (~$7K — reduced via Claude-assisted rubric calibration)\",\n      \"timeline\": \"3-4 months (4 weeks dataset curation with Claude-assisted rubric generation and calibration, 2.5 weeks baseline setup, 5 weeks training and ablations, 3.5 weeks evaluation and writing)\",\n      \"claude_api_cost\": \"$400-700 (rubric generation for ~10K examples, annotation calibration, reward module code generation, experiment analysis — ~120M input + 25M output tokens via Sonnet batch API)\",\n      \"estimated_gpu_cost\": \"$1,400-$2,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"700-900 (same compute floor; GPU time is irreducible)\",\n      \"human_annotation\": \"~200 person-hours minimum expert validation (~$5K — cannot be fully automated for scientific domain rubrics)\",\n      \"timeline\": \"2.5-3.5 months (parallel dataset curation and code development, automated hyperparameter sweeps for τ₁/τ₂ thresholds)\",\n      \"claude_api_cost\": \"$700-1,200 (heavier annotation generation, automated rubric calibration experiments, paper drafting — ~250M input + 50M output tokens)\",\n      \"estimated_gpu_cost\": \"$1,400-$2,250\",\n      \"speed_bottleneck\": \"Domain expert validation of scientific rubric annotations is the irreducible bottleneck. LLM judges can generate initial rubric scores, but scientific reasoning quality assessment requires human calibration to prevent systematic LLM biases (e.g., preferring verbose over concise explanations). Expert recruitment and calibration for multi-disciplinary scientific figures (biology, physics, chemistry) requires 3-4 weeks minimum.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract: Jul 21 2026, paper: Jul 28 2026 — confirmed, feasible with focused initial results on 2 of 3 tasks)\",\n    \"WACV 2027 Round 2 (paper: Aug 27 2026 — confirmed, full results including all ablations)\",\n    \"EACL 2027 (ARR submission: Aug 3 2026 — confirmed, framing emphasizes NLP/rubric aspects)\",\n    \"CVPR 2027 (estimated ~Nov 2026 — TBA, full paper with complete analysis)\",\n    \"ICLR 2027 (estimated ~Oct 2026 — TBA, full paper with theoretical analysis)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment (arXiv:2603.06652, Feb 2026) — hierarchical gated reward R=S_vis·(α·S_ans+(1-α)·S_fmt) for verifiable tasks; our gating extends this to non-verifiable with continuous graded scores\",\n    \"RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning (arXiv:2603.09160, Mar 2026) — rubric-based RL for non-verifiable multimodal captioning; we target scientific reasoning with gated tiers\",\n    \"RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, Feb 2026) — dynamic rubric weighting for curriculum on verifiable tasks; we extend curriculum via gating to non-verifiable\",\n    \"SR-MCR: Self-Rewarded Multimodal Coherent Reasoning (arXiv:2512.22545, Dec 2025) — five structured sub-rewards with GRPO; flat combination on verifiable tasks\",\n    \"RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards (arXiv:2605.10899, May 2026) — rubric-guided policy decomposition for non-verifiable deep research; text-only\",\n    \"Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition (arXiv:2508.19652, Aug 2025) — perception-reasoning decomposition with self-reward; verifiable tasks\",\n    \"Rubric-ARM: Alternating RL for Rubric-Based Reward Modeling in Non-Verifiable Post-Training (arXiv:2602.01511, Feb 2026) — joint rubric generator + judge optimization; text-only\",\n    \"Reward Design for Physical Reasoning in VLMs (arXiv:2604.13993, Apr 2026) — accuracy > flat composite rubric on verifiable tasks; motivates our non-verifiable focus where accuracy is unavailable\",\n    \"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards (arXiv:2602.14872, Feb 2026) — theoretical grounding for curriculum effects in RLVR; our gating implements explicit curriculum\",\n    \"Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards (arXiv:2506.00103) — pairwise GenRM for text non-verifiable tasks; we extend BRPO to multimodal Tier-3\",\n    \"Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning (arXiv:2605.08061, May 2026) — LLM-judge rubric decomposition; text-only\",\n    \"Vero: An Open RL Recipe for General Visual Reasoning (arXiv:2604.04917, Apr 2026) — task-routed rewards across 59 datasets; verifiable tasks only\",\n    \"V-Triune: Visual Triple Unified Reinforcement Learning (arXiv:2505.18129, May 2026) — sample-level reward routing; verifiable tasks\",\n    \"BalCapRL: A Balanced Framework for RL-Based MLLM Image Captioning (Mar 2026) — multi-objective RL for captioning; general captioning not scientific reasoning\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv 2026) — reward hacking pathways; motivates anti-hacking gating design\",\n    \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)\",\n    \"Reward Hacking in the Era of Large Models (arXiv:2604.13602, Apr 2026)\",\n    \"PEARL: Perceptual-Evidence Anchored Reinforced Learning (CVPR 2026) — binary outcome gate on perception\",\n    \"CogFlow: Visual-Gated Policy Optimization (ICLR 2026) — binary answer reward\",\n    \"Faithful GRPO: Constrained Policy Optimization for Visual Grounding (arXiv:2604.08476, Apr 2026)\",\n    \"AlphaGRPO: Decompositional Verifiable Reward for Multimodal Generation (arXiv:2605.12495, May 2026)\",\n    \"Rethinking RFT in LVLM: GRPO Convergence under Composite Rewards (arXiv:2604.19857, Apr 2026)\",\n    \"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding (arXiv:2407.04903, NeurIPS 2024 Workshop) — 72-discipline scientific figure dataset with open-ended captioning\",\n    \"SciGraphQA: A Large-Scale Synthetic Multi-Turn QA Dataset for Scientific Graphs (arXiv:2308.03349) — open-ended graph analysis with reference answers\",\n    \"CharXiv: Charting Gaps in Realistic Chart Understanding in MLLMs (NeurIPS 2024)\",\n    \"SciFIBench: Benchmarking LMMs for Scientific Figure Interpretation (NeurIPS 2024)\",\n    \"CapArena: Benchmarking Detailed Image Captioning in the LLM Era (arXiv:2503.12329, Mar 2026) — arena-style open-ended evaluation\"\n  ],\n  \"description\": \"We propose GatedRubric-GRPO, a framework that extends gated structured reward RL to non-verifiable multimodal scientific reasoning — scientific figure explanation generation, graph-based analytical interpretation, and scientific figure critique — where answers are inherently graded and no single correct response exists. The key innovation is applying and generalizing the gating principle (demonstrated by PaLMR for verifiable tasks with binary visual checks) to non-verifiable settings with continuous graded rubric scores across three tiers: Tier-1 provides continuous visual-grounding scores via programmatic and lightweight LLM checks; Tier-2 delivers structural quality scores via frozen LLM-judge rubrics calibrated per scientific discipline; Tier-3 supplies reasoning quality via bootstrapped pairwise comparison (extending Writing-Zero's BRPO to multimodal), with each tier gating the next. We train Qwen3-VL-8B on genuinely non-verifiable scientific tasks: MMSci figure explanation generation, SciGraphQA open-ended analysis (re-annotated with rubric scoring), and a new 2K-sample scientific figure critique benchmark — with CharXiv/SciFIBench as controlled verifiable baselines demonstrating where binary rewards suffice. A comprehensive ablation suite (flat composite, dynamic weighting à la RuCL, binary gating à la PaLMR, tier-specific ablations) isolates the gating contribution, directly addressing the negative result from 'Reward Design for Physical Reasoning' (which tested FLAT composite on VERIFIABLE tasks, a different regime). This fills the specific gap at the intersection of two established research directions: structured multimodal rewards (PaLMR, SR-MCR, RuCL — all verifiable) and non-verifiable rubric RL (RubiCap for captioning, Rubric-ARM/RubricEM for text), providing the first gated reward framework for graded scientific visual reasoning.\",\n  \"project_name\": \"gated_rubric_nonverif_sci_mm\",\n  \"source\": \"web_research\",\n  \"changes_summary\": {\n    \"issue_1_datasets\": \"CRITICAL FIX: Replaced verifiable-only evaluation with genuinely non-verifiable tasks (MMSci figure explanation generation, SciGraphQA with rubric re-annotation, new scientific figure critique benchmark). CharXiv/SciFIBench retained ONLY as controlled verifiable baselines to demonstrate the verifiable/non-verifiable boundary.\",\n    \"issue_2_concurrent_work\": \"CRITICAL FIX: Thoroughly integrated 7+ missing concurrent works — PaLMR (gated reward, most similar), RubiCap (non-verifiable multimodal), RuCL (rubric curriculum), SR-MCR (multi-component GRPO), RubricEM (non-verifiable rubric decomposition), Vision-SR1 (perception-reasoning decomposition), Rubric-ARM (non-verifiable text rubric RL), Vero/V-Triune (task-routed rewards). Landscape completely rewritten with honest positioning at the intersection gap.\",\n    \"issue_3_gating_justification\": \"MAJOR FIX: (a) Acknowledged PaLMR as prior art for gating in verifiable setting — our contribution extends to non-verifiable with continuous graded scores. (b) Addressed 'Reward Design for Physical Reasoning' negative result: their flat composite tested on verifiable tasks where accuracy dominates; our non-verifiable setting has no accuracy signal, making the comparison gated-rubric vs flat-rubric. (c) Provided three theoretical motivations: gradient interference prevention, explicit curriculum effect grounded in 'Implicit Curriculum' theory, anti-hacking for 'eloquent hallucination' mode. (d) Designed comprehensive ablation suite (5 conditions) to empirically isolate gating contribution.\",\n    \"issue_4_framing\": \"MAJOR FIX: Reframed from 'no work has proposed structured reward decomposition for multimodal reasoning' to 'extending gated structured rewards (which exist for verifiable multimodal) and rubric RL (which exists for non-verifiable text/captioning) to non-verifiable scientific multimodal reasoning.' Title and description reflect narrower but honest novelty claim.\",\n    \"issue_5_wacv_round1\": \"MODERATE FIX: Dropped WACV Round 1 (Jun 25 infeasible). Retained WACV Round 2 (Aug 27), AAAI 2027, EACL 2027, CVPR 2027, ICLR 2027.\",\n    \"issue_6_resource_estimates\": \"MODERATE FIX: Separated GPU annotation hours from human annotation hours. Added explicit human annotation cost (~$5-12K for domain expert validation). Reduced GPU annotation estimate to 100-150h (LLM-based). Acknowledged expert recruitment and calibration as irreducible bottleneck.\"\n  }\n}\n\n## Reviewer feedback (round 2)\nIssues: [\"MODERATE: At least 8 relevant concurrent works are missing from the landscape: (1) DRO (arXiv:2506.13351, Jun 2025/May 2026) uses 'rubric-gating' as feasibility constraints for non-verifiable tasks — directly overlaps the gating-for-non-verifiable concept albeit text-only; (2) Training AI Co-Scientists (arXiv:2512.23707, Dec 2025) does rubric RL for scientific research plan generation; (3) Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) studies rubric reward hacking in medical/science domains — directly relevant to the anti-hacking motivation; (4) ARES (arXiv:2605.23454, May 2026) automates rubric synthesis for scalable non-verifiable RL; (5) Perception-R1 (arXiv:2506.07218) adds visual perception reward to RLVR; (6) ClaimDiff-RL (arXiv:2605.20278, May 2026) does fine-grained claim-level captioning RL; (7) POW3R (arXiv:2605.20164, May 2026) shows policy-aware rubric weighting outperforms static weighting; (8) rDPO (arXiv:2604.13029, Apr 2026) applies instance-specific rubric rewards for multimodal DPO.\", \"MODERATE: Novelty is incremental — extending binary gating (proven in verifiable settings by PaLMR/PEARL/CogFlow) to continuous gating for non-verifiable settings is a modest technical contribution. DRO already demonstrates rubric-gating for non-verifiable text tasks. The main novelty reduces to 'apply continuous gating to multimodal scientific domain,' which risks being perceived as 'apply X to domain Y.'\", \"MODERATE: The new 2K scientific figure critique benchmark construction is under-specified. What is the source of figure-critique pairs? How are ArXiv papers selected? What are the rubric dimensions? What LLM generates the annotations? What does '20% expert validation' mean quantitatively (inter-annotator agreement, acceptance rate)? A 2K sample may also be too small for RL training — RubiCap uses much larger datasets.\", \"MODERATE: MMSci is originally evaluated with CIDEr/BLEU against reference captions from Nature Communications papers. Re-framing it as 'open-ended explanation generation with rubric evaluation' is reasonable but requires justification: why are the original captions insufficient as references? What rubric dimensions capture quality beyond what reference-based metrics measure? This re-annotation effort needs cost/methodology detail.\", \"MINOR: The interpretation of 'Reward Design for Physical Reasoning' is oversimplified. That paper found rubric rewards DO 'improve structured reasoning quality without consistent accuracy improvements' — they don't simply fail. The non-verifiable vs. verifiable distinction is valid, but the proposal should acknowledge rubric rewards provide value even in verifiable settings, just different value than accuracy rewards.\", \"MINOR: POW3R (May 2026) demonstrates that static rubric weighting (which the proposal uses: fixed w₁, w₂, w₃) is suboptimal because 'many important criteria are already saturated or currently unreachable.' The proposal's dynamic weighting ablation (à la RuCL) partially addresses this, but POW3R's policy-aware approach is more principled and should be discussed as a potential enhancement.\"]\nFeedback: The round 1→2 revision was excellent: genuinely non-verifiable tasks, thorough landscape integration, honest positioning, comprehensive ablation design. The gap is real. However, to reach pass-quality: (1) INTEGRATE the ~8 missing concurrent works — particularly DRO (rubric-gating for non-verifiable, text-only), 'Training AI Co-Scientists' (rubric RL for scientific reasoning), and 'Reward Hacking in Rubric-Based RL' (directly validates your anti-hacking motivation). These don't close your gap but strengthen your positioning. (2) SHARPEN the novelty claim beyond domain extension: consider whether continuous gating introduces qualitatively different training dynamics than binary gating (DRO uses binary rubric-gates; PaLMR uses binary visual gates). Can you provide a formal argument or preliminary evidence that the continuous→binary distinction matters? This would elevate the contribution above 'apply X to domain Y.' (3) DETAIL the 2K critique benchmark: specify source papers, selection criteria, rubric dimensions, LLM annotation pipeline, expert validation protocol (IAA targets, calibration procedure), and scale justification. Consider expanding to 5K+ if feasible. (4) SPECIFY the MMSci re-annotation pipeline: what rubric dimensions replace CIDEr/BLEU? How are they calibrated across 72 disciplines? (5) ENGAGE with POW3R's finding that static rubric weights are suboptimal — consider adding a policy-aware variant to the ablation suite. (6) ACKNOWLEDGE that rubric rewards provide reasoning quality benefits even in verifiable settings (per Reward Design for Physical Reasoning), then argue why gating provides additional value in the non-verifiable regime specifically.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T03:24:53.673Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:24:53.673Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-28T03:24:53.717Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
{
  "title": "GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Multimodal Scientific Reasoning",
  "core_problem": "Reinforcement learning with structured rewards has advanced rapidly for verifiable multimodal tasks (PaLMR, SR-MCR, Chart-RL) and non-verifiable text-only tasks (Rubric-ARM, Writing-Zero, RubricEM), and even non-verifiable image captioning (RubiCap). However, a critical domain remains unaddressed: graded scientific visual reasoning — tasks like scientific figure explanation generation, visual argument assessment, and figure-based analytical interpretation — where (a) no single correct answer exists, (b) evaluation requires domain-specific rubrics, and (c) visual grounding quality directly conditions reasoning quality. Existing non-verifiable multimodal RL (RubiCap) targets captioning, not scientific reasoning; existing gated multimodal rewards (PaLMR) target verifiable answer correctness, not graded explanation quality. The intersection — gated structured rewards for non-verifiable scientific multimodal reasoning — remains unexplored.",
  "opportunity": "The landscape reveals a clear gap at the intersection of two well-explored axes. Axis 1: Gated/hierarchical rewards for multimodal RL exist (PaLMR gates answer rewards on visual fidelity; SR-MCR combines five sub-rewards; V-Triune uses sample-level reward routing) but exclusively for verifiable tasks with binary correctness. Axis 2: Rubric-based RL for non-verifiable tasks exists (RubiCap for captioning, Rubric-ARM for text instruction-following, RubricEM for deep research) but either operates in text-only settings or on general captioning without scientific domain structure. The crucial insight: scientific visual reasoning exhibits a unique property — visual grounding quality is a NECESSARY CONDITION for reasoning quality (you cannot produce a valid scientific explanation of a figure you misperceive), creating a natural gating hierarchy. PaLMR demonstrated this gating principle for verifiable tasks (binary visual fidelity → answer reward). We extend it to non-verifiable settings where each tier produces continuous graded scores from domain rubrics, not binary checks. The 'Reward Design for Physical Reasoning in VLMs' (arXiv:2604.13993) found accuracy rewards outperform flat composite rubric rewards on verifiable tasks — but this is expected because accuracy provides a strong, unambiguous signal. In non-verifiable settings, accuracy is UNAVAILABLE; the comparison becomes gated rubric vs. flat rubric vs. no rubric, where gating's curriculum effect (grounded in the 'Implicit Curriculum' theory, arXiv:2602.14872) should prevent the 'eloquent hallucination' failure mode — visually ungrounded but linguistically polished explanations that flat rewards cannot penalize.",
  "landscape": "VERIFIABLE MULTIMODAL + STRUCTURED REWARDS: PaLMR (arXiv:2603.06652, Feb 2026) uses gated hierarchical reward R = S_vis · (α·S_ans + (1-α)·S_fmt) where binary visual fidelity gates answer reward — closest to our gating principle but for verifiable tasks with binary visual check. SR-MCR (arXiv:2512.22545, Dec 2025) integrates five self-referential sub-rewards (semantic alignment, lexical fidelity, non-redundancy, visual grounding, step consistency) with GRPO — multi-component but flat combination on verifiable tasks. RuCL (arXiv:2602.21628, Feb 2026) implements stratified rubric-based curriculum progressing perception→reasoning on multimodal — dynamic rubric weighting but still verifiable benchmarks. Vision-SR1 (arXiv:2508.19652, Aug 2025) decomposes VLM reasoning into visual perception and language reasoning with self-rewarding — verifiable tasks. Vero (arXiv:2604.04917, Apr 2026) uses task-routed rewards across 59 datasets — broad but verifiable. V-Triune (arXiv:2505.18129, May 2026) sample-level reward routing for unified multimodal RL — verifiable. Chart-RL (arXiv:2603.06958, Mar 2026) applies RLVR to chart reasoning — verifiable. PEARL (CVPR 2026) dual-branch perception-reasoning but binary outcome gate. CogFlow (ICLR 2026) Visual-Gated Policy Optimization — binary answer reward. Faithful GRPO (arXiv:2604.08476, Apr 2026) constrains policy for visual grounding — verifiable spatial tasks. NON-VERIFIABLE + STRUCTURED REWARDS (TEXT-ONLY): Rubric-ARM (arXiv:2602.01511, Feb 2026) alternating RL for rubric-based reward modeling — text-only non-verifiable. Writing-Zero (arXiv:2506.00103) bridges non-verifiable tasks via pairwise GenRM — text-only. Rubric-Grounded RL (arXiv:2605.08061, May 2026) decomposes reward via LLM-judge rubrics — text-only. RubricEM (arXiv:2605.10899, May 2026) meta-RL with rubric-guided policy decomposition for deep research agents — text-only. PrefBERT/Semantically-Aware Rewards (arXiv:2506.15068) for open-ended free-form generation — text-only. NON-VERIFIABLE MULTIMODAL: RubiCap (arXiv:2603.09160, Mar 2026) applies rubric-guided RL to dense image captioning with LLM-written rubrics — closest multimodal non-verifiable work but targets general captioning, not scientific reasoning, and uses dynamically generated instance-level rubrics without gating. CapRL (ICLR 2026) uses VQA-based proxy verifiable reward for captioning. BalCapRL (Mar 2026) balanced multi-objective RL for captioning. NEGATIVE RESULTS: 'Reward Design for Physical Reasoning in VLMs' (arXiv:2604.13993, Apr 2026) found accuracy-based rewards outperform flat composite rubric rewards on verifiable physics tasks — motivates our focus on non-verifiable settings where accuracy is unavailable. 'LLMs Gaming Verifiers' (arXiv 2026) shows reward hacking exploits what verifiers fail to enforce — motivates our gating to prevent exploitation of higher-tier rewards through ungrounded reasoning. THE GAP: No work applies gated/hierarchical structured rewards to non-verifiable scientific multimodal reasoning tasks where visual grounding quality should condition reasoning quality evaluation.",
  "inspired_by": "Intersection gap: structured reward RL exists for (verifiable multimodal) and (non-verifiable text-only) and (non-verifiable captioning), but NOT for (non-verifiable scientific multimodal reasoning). Innovation pattern: 'Principled Extension' — take PaLMR's gating principle (proven for verifiable tasks) and Rubric-ARM/RubiCap's rubric principle (proven for non-verifiable tasks) and combine them for the scientifically important domain of graded visual reasoning. Theoretical grounding: the 'Implicit Curriculum' paper (arXiv:2602.14872) shows RLVR naturally creates easy→hard curriculum; our gating makes this explicit and domain-appropriate for scientific reasoning. Building block: GRPO's compatibility with multi-reward designs (proven by SR-MCR, Vero, V-Triune) makes it the natural optimization backbone.",
  "approach": "We propose GatedRubric-GRPO, which extends gated structured rewards to non-verifiable multimodal scientific reasoning within standard GRPO training on a 7-8B VLM (Qwen3-VL-8B). The framework decomposes evaluation into three gated tiers, generalizing PaLMR's binary gating to continuous graded rubric scores. Tier-1 (Visual Grounding, continuous 0-1): programmatic and lightweight LLM checks assess whether the response correctly references visual elements present in the figure — element identification accuracy, spatial description consistency, and data reading fidelity — producing a continuous score (NOT binary like PaLMR's S_vis). Tier-2 (Structural Quality, gated on Tier-1 ≥ τ₁): a frozen LLM judge (Qwen3-32B) evaluates logical coherence, evidence-claim alignment, domain terminology appropriateness, and visual-textual consistency using domain-specific rubric templates designed per scientific discipline. Activated only when Tier-1 exceeds threshold τ₁, preventing reward for structurally polished but visually ungrounded explanations. Tier-3 (Reasoning Quality, gated on Tier-2 ≥ τ₂): bootstrapped pairwise comparison within GRPO rollout groups assesses analytical depth, interpretive insight, explanation completeness, and critical assessment quality — extending Writing-Zero's BRPO to multimodal. Activated only when Tier-2 exceeds τ₂. The composite reward is R = w₁·R₁ + w₂·𝟙(R₁≥τ₁)·R₂ + w₃·𝟙(R₁≥τ₁)·𝟙(R₂≥τ₂)·R₃. TRAINING TASKS (genuinely non-verifiable): (1) Scientific figure explanation generation using MMSci (Nature Communications figures, 72 disciplines) — given a figure, generate a comprehensive scientific explanation evaluated by multi-dimensional rubric; (2) Open-ended scientific graph analysis using SciGraphQA re-annotated with rubric scoring (replacing CIDEr/BLEU) — given a graph and question, provide detailed analytical interpretation; (3) Scientific figure critique construction: a new benchmark of ~2K figure-critique pairs from diverse ArXiv papers, with LLM-generated rubric annotations validated by domain experts on a 20% subset. CONTROLLED COMPARISON (verifiable baselines): CharXiv and SciFIBench used as controlled comparisons to demonstrate WHERE binary rewards suffice versus where rubric rewards add value, directly addressing the verifiable/non-verifiable boundary. KEY ABLATIONS to isolate gating contribution: (A1) flat composite: R = w₁·R₁ + w₂·R₂ + w₃·R₃ (no gating); (A2) dynamic weighting à la RuCL (rubric weights adjust during training); (A3) PaLMR-style binary gating (R₁ binarized); (A4) Tier-1+2 only (no reasoning quality); (A5) Tier-1+3 only (no structural quality). This ablation suite directly tests whether gated > flat composite (addressing the negative result from Reward Design for Physical Reasoning, which tested FLAT composite on VERIFIABLE tasks) and whether continuous gating > binary gating. THEORETICAL MOTIVATION: (1) Gradient interference: in flat composite rewards, high reasoning fluency can compensate for poor visual grounding, creating conflicting gradient signals; gating eliminates this by zeroing higher-tier gradients when grounding is insufficient. (2) Explicit curriculum: gating implements a controlled version of the implicit curriculum discovered in RLVR training dynamics (arXiv:2602.14872), appropriate for the perception→structure→reasoning progression in scientific analysis. (3) Anti-hacking: gating specifically prevents the 'eloquent hallucination' failure mode where models generate well-structured but visually ungrounded scientific explanations — the multimodal analogue of the reward hacking patterns identified by 'LLMs Gaming Verifiers.'",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "900-1200 (8×H100: ~100h LLM-based rubric annotation with 32B judge on ~10K examples, ~450h main GatedRubric-GRPO training and ablation suite across 3 tiers and 5 ablation conditions, ~150h baseline reproductions including RubiCap/PaLMR-style baselines, ~150h evaluation and analysis)",
      "human_annotation": "~500 person-hours domain expert validation (20% of rubric annotations, 3 annotators × ~500 examples × 20 min each, ~$12K at expert rates)",
      "timeline": "4-5 months (5 weeks dataset curation with LLM-assisted rubric annotation + expert validation, 3 weeks baseline implementation, 6 weeks GatedRubric-GRPO training and full ablation suite, 4 weeks evaluation and paper writing)",
      "estimated_gpu_cost": "$1,800-$3,000 (at $2-2.50/H100-hr spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "700-900 (Claude generates rubric templates, annotation pipelines, and ablation configurations; human validates scientific accuracy of graded annotations on 20% subset)",
      "human_annotation": "~300 person-hours expert validation (~$7K — reduced via Claude-assisted rubric calibration)",
      "timeline": "3-4 months (4 weeks dataset curation with Claude-assisted rubric generation and calibration, 2.5 weeks baseline setup, 5 weeks training and ablations, 3.5 weeks evaluation and writing)",
      "claude_api_cost": "$400-700 (rubric generation for ~10K examples, annotation calibration, reward module code generation, experiment analysis — ~120M input + 25M output tokens via Sonnet batch API)",
      "estimated_gpu_cost": "$1,400-$2,250"
    },
    "auto_research": {
      "gpu_hours": "700-900 (same compute floor; GPU time is irreducible)",
      "human_annotation": "~200 person-hours minimum expert validation (~$5K — cannot be fully automated for scientific domain rubrics)",
      "timeline": "2.5-3.5 months (parallel dataset curation and code development, automated hyperparameter sweeps for τ₁/τ₂ thresholds)",
      "claude_api_cost": "$700-1,200 (heavier annotation generation, automated rubric calibration experiments, paper drafting — ~250M input + 50M output tokens)",
      "estimated_gpu_cost": "$1,400-$2,250",
      "speed_bottleneck": "Domain expert validation of scientific rubric annotations is the irreducible bottleneck. LLM judges can generate initial rubric scores, but scientific reasoning quality assessment requires human calibration to prevent systematic LLM biases (e.g., preferring verbose over concise explanations). Expert recruitment and calibration for multi-disciplinary scientific figures (biology, physics, chemistry) requires 3-4 weeks minimum."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: Jul 21 2026, paper: Jul 28 2026 — confirmed, feasible with focused initial results on 2 of 3 tasks)",
    "WACV 2027 Round 2 (paper: Aug 27 2026 — confirmed, full results including all ablations)",
    "EACL 2027 (ARR submission: Aug 3 2026 — confirmed, framing emphasizes NLP/rubric aspects)",
    "CVPR 2027 (estimated ~Nov 2026 — TBA, full paper with complete analysis)",
    "ICLR 2027 (estimated ~Oct 2026 — TBA, full paper with theoretical analysis)"
  ],
  "level": "solid",
  "key_references": [
    "PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment (arXiv:2603.06652, Feb 2026) — hierarchical gated reward R=S_vis·(α·S_ans+(1-α)·S_fmt) for verifiable tasks; our gating extends this to non-verifiable with continuous graded scores",
    "RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning (arXiv:2603.09160, Mar 2026) — rubric-based RL for non-verifiable multimodal captioning; we target scientific reasoning with gated tiers",
    "RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, Feb 2026) — dynamic rubric weighting for curriculum on verifiable tasks; we extend curriculum via gating to non-verifiable",
    "SR-MCR: Self-Rewarded Multimodal Coherent Reasoning (arXiv:2512.22545, Dec 2025) — five structured sub-rewards with GRPO; flat combination on verifiable tasks",
    "RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards (arXiv:2605.10899, May 2026) — rubric-guided policy decomposition for non-verifiable deep research; text-only",
    "Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition (arXiv:2508.19652, Aug 2025) — perception-reasoning decomposition with self-reward; verifiable tasks",
    "Rubric-ARM: Alternating RL for Rubric-Based Reward Modeling in Non-Verifiable Post-Training (arXiv:2602.01511, Feb 2026) — joint rubric generator + judge optimization; text-only",
    "Reward Design for Physical Reasoning in VLMs (arXiv:2604.13993, Apr 2026) — accuracy > flat composite rubric on verifiable tasks; motivates our non-verifiable focus where accuracy is unavailable",
    "The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards (arXiv:2602.14872, Feb 2026) — theoretical grounding for curriculum effects in RLVR; our gating implements explicit curriculum",
    "Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards (arXiv:2506.00103) — pairwise GenRM for text non-verifiable tasks; we extend BRPO to multimodal Tier-3",
    "Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning (arXiv:2605.08061, May 2026) — LLM-judge rubric decomposition; text-only",
    "Vero: An Open RL Recipe for General Visual Reasoning (arXiv:2604.04917, Apr 2026) — task-routed rewards across 59 datasets; verifiable tasks only",
    "V-Triune: Visual Triple Unified Reinforcement Learning (arXiv:2505.18129, May 2026) — sample-level reward routing; verifiable tasks",
    "BalCapRL: A Balanced Framework for RL-Based MLLM Image Captioning (Mar 2026) — multi-objective RL for captioning; general captioning not scientific reasoning",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv 2026) — reward hacking pathways; motivates anti-hacking gating design",
    "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)",
    "Reward Hacking in the Era of Large Models (arXiv:2604.13602, Apr 2026)",
    "PEARL: Perceptual-Evidence Anchored Reinforced Learning (CVPR 2026) — binary outcome gate on perception",
    "CogFlow: Visual-Gated Policy Optimization (ICLR 2026) — binary answer reward",
    "Faithful GRPO: Constrained Policy Optimization for Visual Grounding (arXiv:2604.08476, Apr 2026)",
    "AlphaGRPO: Decompositional Verifiable Reward for Multimodal Generation (arXiv:2605.12495, May 2026)",
    "Rethinking RFT in LVLM: GRPO Convergence under Composite Rewards (arXiv:2604.19857, Apr 2026)",
    "MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding (arXiv:2407.04903, NeurIPS 2024 Workshop) — 72-discipline scientific figure dataset with open-ended captioning",
    "SciGraphQA: A Large-Scale Synthetic Multi-Turn QA Dataset for Scientific Graphs (arXiv:2308.03349) — open-ended graph analysis with reference answers",
    "CharXiv: Charting Gaps in Realistic Chart Understanding in MLLMs (NeurIPS 2024)",
    "SciFIBench: Benchmarking LMMs for Scientific Figure Interpretation (NeurIPS 2024)",
    "CapArena: Benchmarking Detailed Image Captioning in the LLM Era (arXiv:2503.12329, Mar 2026) — arena-style open-ended evaluation"
  ],
  "description": "We propose GatedRubric-GRPO, a framework that extends gated structured reward RL to non-verifiable multimodal scientific reasoning — scientific figure explanation generation, graph-based analytical interpretation, and scientific figure critique — where answers are inherently graded and no single correct response exists. The key innovation is applying and generalizing the gating principle (demonstrated by PaLMR for verifiable tasks with binary visual checks) to non-verifiable settings with continuous graded rubric scores across three tiers: Tier-1 provides continuous visual-grounding scores via programmatic and lightweight LLM checks; Tier-2 delivers structural quality scores via frozen LLM-judge rubrics calibrated per scientific discipline; Tier-3 supplies reasoning quality via bootstrapped pairwise comparison (extending Writing-Zero's BRPO to multimodal), with each tier gating the next. We train Qwen3-VL-8B on genuinely non-verifiable scientific tasks: MMSci figure explanation generation, SciGraphQA open-ended analysis (re-annotated with rubric scoring), and a new 2K-sample scientific figure critique benchmark — with CharXiv/SciFIBench as controlled verifiable baselines demonstrating where binary rewards suffice. A comprehensive ablation suite (flat composite, dynamic weighting à la RuCL, binary gating à la PaLMR, tier-specific ablations) isolates the gating contribution, directly addressing the negative result from 'Reward Design for Physical Reasoning' (which tested FLAT composite on VERIFIABLE tasks, a different regime). This fills the specific gap at the intersection of two established research directions: structured multimodal rewards (PaLMR, SR-MCR, RuCL — all verifiable) and non-verifiable rubric RL (RubiCap for captioning, Rubric-ARM/RubricEM for text), providing the first gated reward framework for graded scientific visual reasoning.",
  "project_name": "gated_rubric_nonverif_sci_mm",
  "source": "web_research",
  "changes_summary": {
    "issue_1_datasets": "CRITICAL FIX: Replaced verifiable-only evaluation with genuinely non-verifiable tasks (MMSci figure explanation generation, SciGraphQA with rubric re-annotation, new scientific figure critique benchmark). CharXiv/SciFIBench retained ONLY as controlled verifiable baselines to demonstrate the verifiable/non-verifiable boundary.",
    "issue_2_concurrent_work": "CRITICAL FIX: Thoroughly integrated 7+ missing concurrent works — PaLMR (gated reward, most similar), RubiCap (non-verifiable multimodal), RuCL (rubric curriculum), SR-MCR (multi-component GRPO), RubricEM (non-verifiable rubric decomposition), Vision-SR1 (perception-reasoning decomposition), Rubric-ARM (non-verifiable text rubric RL), Vero/V-Triune (task-routed rewards). Landscape completely rewritten with honest positioning at the intersection gap.",
    "issue_3_gating_justification": "MAJOR FIX: (a) Acknowledged PaLMR as prior art for gating in verifiable setting — our contribution extends to non-verifiable with continuous graded scores. (b) Addressed 'Reward Design for Physical Reasoning' negative result: their flat composite tested on verifiable tasks where accuracy dominates; our non-verifiable setting has no accuracy signal, making the comparison gated-rubric vs flat-rubric. (c) Provided three theoretical motivations: gradient interference prevention, explicit curriculum effect grounded in 'Implicit Curriculum' theory, anti-hacking for 'eloquent hallucination' mode. (d) Designed comprehensive ablation suite (5 conditions) to empirically isolate gating contribution.",
    "issue_4_framing": "MAJOR FIX: Reframed from 'no work has proposed structured reward decomposition for multimodal reasoning' to 'extending gated structured rewards (which exist for verifiable multimodal) and rubric RL (which exists for non-verifiable text/captioning) to non-verifiable scientific multimodal reasoning.' Title and description reflect narrower but honest novelty claim.",
    "issue_5_wacv_round1": "MODERATE FIX: Dropped WACV Round 1 (Jun 25 infeasible). Retained WACV Round 2 (Aug 27), AAAI 2027, EACL 2027, CVPR 2027, ICLR 2027.",
    "issue_6_resource_estimates": "MODERATE FIX: Separated GPU annotation hours from human annotation hours. Added explicit human annotation cost (~$5-12K for domain expert validation). Reduced GPU annotation estimate to 100-150h (LLM-based). Acknowledged expert recruitment and calibration as irreducible bottleneck."
  }
}

## Reviewer feedback (round 2)
Issues: ["MODERATE: At least 8 relevant concurrent works are missing from the landscape: (1) DRO (arXiv:2506.13351, Jun 2025/May 2026) uses 'rubric-gating' as feasibility constraints for non-verifiable tasks — directly overlaps the gating-for-non-verifiable concept albeit text-only; (2) Training AI Co-Scientists (arXiv:2512.23707, Dec 2025) does rubric RL for scientific research plan generation; (3) Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) studies rubric reward hacking in medical/science domains — directly relevant to the anti-hacking motivation; (4) ARES (arXiv:2605.23454, May 2026) automates rubric synthesis for scalable non-verifiable RL; (5) Perception-R1 (arXiv:2506.07218) adds visual perception reward to RLVR; (6) ClaimDiff-RL (arXiv:2605.20278, May 2026) does fine-grained claim-level captioning RL; (7) POW3R (arXiv:2605.20164, May 2026) shows policy-aware rubric weighting outperforms static weighting; (8) rDPO (arXiv:2604.13029, Apr 2026) applies instance-specific rubric rewards for multimodal DPO.", "MODERATE: Novelty is incremental — extending binary gating (proven in verifiable settings by PaLMR/PEARL/CogFlow) to continuous gating for non-verifiable settings is a modest technical contribution. DRO already demonstrates rubric-gating for non-verifiable text tasks. The main novelty reduces to 'apply continuous gating to multimodal scientific domain,' which risks being perceived as 'apply X to domain Y.'", "MODERATE: The new 2K scientific figure critique benchmark construction is under-specified. What is the source of figure-critique pairs? How are ArXiv papers selected? What are the rubric dimensions? What LLM generates the annotations? What does '20% expert validation' mean quantitatively (inter-annotator agreement, acceptance rate)? A 2K sample may also be too small for RL training — RubiCap uses much larger datasets.", "MODERATE: MMSci is originally evaluated with CIDEr/BLEU against reference captions from Nature Communications papers. Re-framing it as 'open-ended explanation generation with rubric evaluation' is reasonable but requires justification: why are the original captions insufficient as references? What rubric dimensions capture quality beyond what reference-based metrics measure? This re-annotation effort needs cost/methodology detail.", "MINOR: The interpretation of 'Reward Design for Physical Reasoning' is oversimplified. That paper found rubric rewards DO 'improve structured reasoning quality without consistent accuracy improvements' — they don't simply fail. The non-verifiable vs. verifiable distinction is valid, but the proposal should acknowledge rubric rewards provide value even in verifiable settings, just different value than accuracy rewards.", "MINOR: POW3R (May 2026) demonstrates that static rubric weighting (which the proposal uses: fixed w₁, w₂, w₃) is suboptimal because 'many important criteria are already saturated or currently unreachable.' The proposal's dynamic weighting ablation (à la RuCL) partially addresses this, but POW3R's policy-aware approach is more principled and should be discussed as a potential enhancement."]
Feedback: The round 1→2 revision was excellent: genuinely non-verifiable tasks, thorough landscape integration, honest positioning, comprehensive ablation design. The gap is real. However, to reach pass-quality: (1) INTEGRATE the ~8 missing concurrent works — particularly DRO (rubric-gating for non-verifiable, text-only), 'Training AI Co-Scientists' (rubric RL for scientific reasoning), and 'Reward Hacking in Rubric-Based RL' (directly validates your anti-hacking motivation). These don't close your gap but strengthen your positioning. (2) SHARPEN the novelty claim beyond domain extension: consider whether continuous gating introduces qualitatively different training dynamics than binary gating (DRO uses binary rubric-gates; PaLMR uses binary visual gates). Can you provide a formal argument or preliminary evidence that the continuous→binary distinction matters? This would elevate the contribution above 'apply X to domain Y.' (3) DETAIL the 2K critique benchmark: specify source papers, selection criteria, rubric dimensions, LLM annotation pipeline, expert validation protocol (IAA targets, calibration procedure), and scale justification. Consider expanding to 5K+ if feasible. (4) SPECIFY the MMSci re-annotation pipeline: what rubric dimensions replace CIDEr/BLEU? How are they calibrated across 72 disciplines? (5) ENGAGE with POW3R's finding that static rubric weights are suboptimal — consider adding a policy-aware variant to the ablation suite. (6) ACKNOWLEDGE that rubric rewards provide reasoning quality benefits even in verifiable settings (per Reward Design for Physical Reasoning), then argue why gating provides additional value in the non-verifiable regime specifically.

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
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "b4cde690-dbbe-495a-9a18-4203258df244",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T03:24:53.715Z_

```json
{
  "parentUuid": "b4cde690-dbbe-495a-9a18-4203258df244",
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
  "uuid": "0784f966-89f4-47dd-bc04-83ffadf0ad2e",
  "timestamp": "2026-05-28T03:24:53.715Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T03:24:53.715Z_

```json
{
  "parentUuid": "0784f966-89f4-47dd-bc04-83ffadf0ad2e",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "bec4e3e2-406a-4598-9213-e85c5c5f6d94",
  "timestamp": "2026-05-28T03:24:53.715Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-28T03:24:53.715Z_

```json
{
  "parentUuid": "bec4e3e2-406a-4598-9213-e85c5c5f6d94",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "686b8ec2-0f3d-4add-8b14-4da44caf801e",
  "timestamp": "2026-05-28T03:24:53.715Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "686b8ec2-0f3d-4add-8b14-4da44caf801e",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Assistant

_source line 9 · 2026-05-28T03:25:00.371Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research strategy:

1. **8 missing concurrent works** - Need to search for and read each of these papers
2. **Novelty concern** - Need to think deeply about continuous vs binary gating distinction
3. **2K critique benchmark under-specified** - Need to detail the benchmark construction
4. **MMSci re-annotation pipeline** - Need to specify rubric dimensions and calibration
5. **Reward Design interpretation** - Need to nuance the interpretation
6. **POW3R static weights** - Need to engage with policy-aware weighting

Let me start by searching for and reading the key missing papers, particularly DRO, Training AI Co-Scientists, Reward Hacking in Rubric-Based RL, ARES, Perception-R1, ClaimDiff-RL, POW3R, and rDPO.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "686b8ec2-0f3d-4add-8b14-4da44caf801e",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "7b50ef0c-1012-420e-a428-8391e631580f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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

_source line 10 · 2026-05-28T03:25:02.043Z_

I'll start by researching the missing concurrent works and key issues raised by the reviewer. Let me launch parallel research agents for the most critical papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b50ef0c-1012-420e-a428-8391e631580f",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "3fb40ef6-147b-46f4-b9f7-3b870b6c67f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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

_source line 11 · 2026-05-28T03:25:07.643Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01G3HBvidcjxWLYV1jbqgBqR`</summary>

```json
{
  "description": "Research DRO paper",
  "prompt": "Search for and read the paper \"DRO\" (arXiv:2506.13351) which uses 'rubric-gating' as feasibility constraints for non-verifiable tasks. This is a text-only RL paper that uses rubric-gating for non-verifiable tasks. \n\nI need to understand:\n1. What exactly is \"rubric-gating\" in DRO? Is it binary or continuous?\n2. What tasks does it apply to (text-only? what domains)?\n3. How does their gating mechanism work technically?\n4. What are the key results?\n5. How does it differ from applying gated rewards to multimodal scientific reasoning?\n\nUse WebSearch and WebFetch to find and read this paper. Search for \"DRO rubric gating non-verifiable reinforcement learning 2506.13351\" and related queries. Report your findings in detail.",
  "subagent_type": "general-purpose",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fb40ef6-147b-46f4-b9f7-3b870b6c67f1",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "57fde941-8d78-4abc-84f5-86e79153f9a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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

_source line 12 · 2026-05-28T03:25:36.814Z_

<details><summary>↩ Tool result · `toolu_01AWPQEUjgcGxkaDFkLv6QkX`</summary>

```text
Async agent launched successfully.
agentId: a87c831bd24e0caa5 (internal ID - do not mention to user. Use SendMessage with to: 'a87c831bd24e0caa5' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a87c831bd24e0caa5.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f3345ec-0b58-4824-9f32-d3575241351c",
  "isSidechain": false,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "08555df9-7a95-44b5-93b0-c30cfc3f3768",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a87c831bd24e0caa5",
    "description": "Research MMSci dataset details",
    "prompt": "Search for and read details about the MMSci dataset (arXiv:2407.04903, NeurIPS 2024 Workshop) for scientific figure understanding. I need to understand:\n\n1. How many figures/examples does it contain?\n2. What are the 72 scientific disciplines covered?\n3. What are the original evaluation metrics (CIDEr/BLEU)?\n4. What do the reference captions look like - are they figure captions from Nature Communications papers?\n5. What kinds of tasks does it support (captioning, QA, etc.)?\n6. What is the data format and annotation structure?\n\nAlso search for how other papers have re-annotated or re-purposed existing captioning datasets with rubric-based evaluation. Try queries like:\n- \"MMSci dataset scientific figure understanding NeurIPS 2024\"\n- \"rubric annotation scientific figure captioning\"\n- \"converting reference-based metrics to rubric evaluation\"\n\nI need this to specify a detailed re-annotation pipeline for converting MMSci from reference-based evaluation to rubric-based evaluation for non-verifiable RL training. Report your findings in detail.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a87c831bd24e0caa5.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "5f3345ec-0b58-4824-9f32-d3575241351c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T03:25:07.654Z_

<details><summary>↩ Tool result · `toolu_01G3HBvidcjxWLYV1jbqgBqR`</summary>

```text
Async agent launched successfully.
agentId: a953639c763da791d (internal ID - do not mention to user. Use SendMessage with to: 'a953639c763da791d' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a953639c763da791d.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57fde941-8d78-4abc-84f5-86e79153f9a4",
  "isSidechain": false,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "847d425b-4057-46bb-b5f1-10fd2e9c0af9",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a953639c763da791d",
    "description": "Research DRO paper",
    "prompt": "Search for and read the paper \"DRO\" (arXiv:2506.13351) which uses 'rubric-gating' as feasibility constraints for non-verifiable tasks. This is a text-only RL paper that uses rubric-gating for non-verifiable tasks. \n\nI need to understand:\n1. What exactly is \"rubric-gating\" in DRO? Is it binary or continuous?\n2. What tasks does it apply to (text-only? what domains)?\n3. How does their gating mechanism work technically?\n4. What are the key results?\n5. How does it differ from applying gated rewards to multimodal scientific reasoning?\n\nUse WebSearch and WebFetch to find and read this paper. Search for \"DRO rubric gating non-verifiable reinforcement learning 2506.13351\" and related queries. Report your findings in detail.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a953639c763da791d.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "57fde941-8d78-4abc-84f5-86e79153f9a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-28T03:25:11.427Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012AGG9yHcSe9XexCrqwDDdQ`</summary>

```json
{
  "description": "Research Training AI Co-Scientists",
  "prompt": "Search for and read the paper \"Training AI Co-Scientists\" (arXiv:2512.23707, Dec 2025) which does rubric RL for scientific research plan generation.\n\nI need to understand:\n1. What scientific reasoning tasks does it address?\n2. How does it use rubrics for RL training?\n3. Is it multimodal or text-only?\n4. What are its key contributions and results?\n5. How does it relate to non-verifiable scientific reasoning with rubric-based rewards?\n\nUse WebSearch and WebFetch to find and read this paper. Search for \"Training AI Co-Scientists arXiv 2512.23707 rubric reinforcement learning scientific\" and related queries. Report your findings in detail.",
  "subagent_type": "general-purpose",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "847d425b-4057-46bb-b5f1-10fd2e9c0af9",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "326ba988-574c-4de5-92ce-866e65842f58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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

_source line 15 · 2026-05-28T03:25:11.432Z_

<details><summary>↩ Tool result · `toolu_012AGG9yHcSe9XexCrqwDDdQ`</summary>

```text
Async agent launched successfully.
agentId: aba5f8b5a313742c2 (internal ID - do not mention to user. Use SendMessage with to: 'aba5f8b5a313742c2' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/aba5f8b5a313742c2.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "326ba988-574c-4de5-92ce-866e65842f58",
  "isSidechain": false,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "280934c7-70b1-46e4-adb7-5735c58a889f",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "aba5f8b5a313742c2",
    "description": "Research Training AI Co-Scientists",
    "prompt": "Search for and read the paper \"Training AI Co-Scientists\" (arXiv:2512.23707, Dec 2025) which does rubric RL for scientific research plan generation.\n\nI need to understand:\n1. What scientific reasoning tasks does it address?\n2. How does it use rubrics for RL training?\n3. Is it multimodal or text-only?\n4. What are its key contributions and results?\n5. How does it relate to non-verifiable scientific reasoning with rubric-based rewards?\n\nUse WebSearch and WebFetch to find and read this paper. Search for \"Training AI Co-Scientists arXiv 2512.23707 rubric reinforcement learning scientific\" and related queries. Report your findings in detail.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/aba5f8b5a313742c2.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "326ba988-574c-4de5-92ce-866e65842f58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T03:25:14.678Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YbrVTXBby2NQWbcBVLiWFv`</summary>

```json
{
  "description": "Research Reward Hacking Rubric RL",
  "prompt": "Search for and read the paper \"Reward Hacking in Rubric-Based RL\" (arXiv:2605.12474, May 2026) which studies rubric reward hacking in medical/science domains.\n\nI need to understand:\n1. What specific reward hacking patterns does it identify in rubric-based RL?\n2. What domains does it study (medical, science)?\n3. What mitigations does it propose?\n4. How does this relate to gating as an anti-hacking mechanism?\n5. Key findings and recommendations.\n\nUse WebSearch and WebFetch to find and read this paper. Search for \"Reward Hacking Rubric-Based RL arXiv 2605.12474 medical science\" and related queries. Report your findings in detail.",
  "subagent_type": "general-purpose",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "280934c7-70b1-46e4-adb7-5735c58a889f",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "b0b45752-6ea6-4f60-9e6b-6f3bd7bf7196",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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

_source line 17 · 2026-05-28T03:25:14.688Z_

<details><summary>↩ Tool result · `toolu_01YbrVTXBby2NQWbcBVLiWFv`</summary>

```text
Async agent launched successfully.
agentId: ae9ecf87b6381e647 (internal ID - do not mention to user. Use SendMessage with to: 'ae9ecf87b6381e647' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/ae9ecf87b6381e647.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0b45752-6ea6-4f60-9e6b-6f3bd7bf7196",
  "isSidechain": false,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "94c725a9-d249-450f-9b06-dd81997e3bd6",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ae9ecf87b6381e647",
    "description": "Research Reward Hacking Rubric RL",
    "prompt": "Search for and read the paper \"Reward Hacking in Rubric-Based RL\" (arXiv:2605.12474, May 2026) which studies rubric reward hacking in medical/science domains.\n\nI need to understand:\n1. What specific reward hacking patterns does it identify in rubric-based RL?\n2. What domains does it study (medical, science)?\n3. What mitigations does it propose?\n4. How does this relate to gating as an anti-hacking mechanism?\n5. Key findings and recommendations.\n\nUse WebSearch and WebFetch to find and read this paper. Search for \"Reward Hacking Rubric-Based RL arXiv 2605.12474 medical science\" and related queries. Report your findings in detail.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/ae9ecf87b6381e647.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "b0b45752-6ea6-4f60-9e6b-6f3bd7bf7196",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T03:25:19.981Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KxuSdkN91hUkCL1pexV5Ub`</summary>

```json
{
  "description": "Research ARES POW3R rDPO papers",
  "prompt": "Search for and read these three papers:\n\n1. **ARES** (arXiv:2605.23454, May 2026) - automates rubric synthesis for scalable non-verifiable RL\n2. **POW3R** (arXiv:2605.20164, May 2026) - shows policy-aware rubric weighting outperforms static weighting\n3. **rDPO** (arXiv:2604.13029, Apr 2026) - applies instance-specific rubric rewards for multimodal DPO\n\nFor each paper, I need:\n1. Core technical contribution\n2. Key findings/results\n3. Whether it's text-only or multimodal\n4. How it relates to gated rubric rewards for non-verifiable multimodal scientific reasoning\n\nUse WebSearch and WebFetch to find and read these papers. Try queries like:\n- \"ARES automated rubric synthesis non-verifiable RL 2605.23454\"\n- \"POW3R policy-aware rubric weighting 2605.20164\"\n- \"rDPO instance-specific rubric multimodal DPO 2604.13029\"\n\nReport your findings in detail for all three papers.",
  "subagent_type": "general-purpose",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94c725a9-d249-450f-9b06-dd81997e3bd6",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "842ea84d-f9aa-4520-8432-6a7523ac0b67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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

_source line 19 · 2026-05-28T03:25:20.008Z_

<details><summary>↩ Tool result · `toolu_01KxuSdkN91hUkCL1pexV5Ub`</summary>

```text
Async agent launched successfully.
agentId: ac16169121d45159b (internal ID - do not mention to user. Use SendMessage with to: 'ac16169121d45159b' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/ac16169121d45159b.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "842ea84d-f9aa-4520-8432-6a7523ac0b67",
  "isSidechain": false,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "d106096a-64f6-4d68-82cb-2ca275d285f1",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ac16169121d45159b",
    "description": "Research ARES POW3R rDPO papers",
    "prompt": "Search for and read these three papers:\n\n1. **ARES** (arXiv:2605.23454, May 2026) - automates rubric synthesis for scalable non-verifiable RL\n2. **POW3R** (arXiv:2605.20164, May 2026) - shows policy-aware rubric weighting outperforms static weighting\n3. **rDPO** (arXiv:2604.13029, Apr 2026) - applies instance-specific rubric rewards for multimodal DPO\n\nFor each paper, I need:\n1. Core technical contribution\n2. Key findings/results\n3. Whether it's text-only or multimodal\n4. How it relates to gated rubric rewards for non-verifiable multimodal scientific reasoning\n\nUse WebSearch and WebFetch to find and read these papers. Try queries like:\n- \"ARES automated rubric synthesis non-verifiable RL 2605.23454\"\n- \"POW3R policy-aware rubric weighting 2605.20164\"\n- \"rDPO instance-specific rubric multimodal DPO 2604.13029\"\n\nReport your findings in detail for all three papers.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/ac16169121d45159b.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "842ea84d-f9aa-4520-8432-6a7523ac0b67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T03:25:23.721Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01A3amkypRoZ4hTMsQjm2dmh`</summary>

```json
{
  "description": "Research Perception-R1 ClaimDiff-RL",
  "prompt": "Search for and read these two papers:\n\n1. **Perception-R1** (arXiv:2506.07218) - adds visual perception reward to RLVR\n2. **ClaimDiff-RL** (arXiv:2605.20278, May 2026) - does fine-grained claim-level captioning RL\n\nFor each paper, I need:\n1. Core technical contribution\n2. Key findings/results\n3. Whether it's verifiable or non-verifiable\n4. How it relates to gated rubric rewards for non-verifiable multimodal scientific reasoning\n\nUse WebSearch and WebFetch to find and read these papers. Try queries like:\n- \"Perception-R1 visual perception reward RLVR 2506.07218\"\n- \"ClaimDiff-RL claim-level captioning RL 2605.20278\"\n\nReport your findings in detail for both papers.",
  "subagent_type": "general-purpose",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d106096a-64f6-4d68-82cb-2ca275d285f1",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "e264a56c-28db-4753-9318-0edf727ae4ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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

_source line 21 · 2026-05-28T03:25:23.729Z_

<details><summary>↩ Tool result · `toolu_01A3amkypRoZ4hTMsQjm2dmh`</summary>

```text
Async agent launched successfully.
agentId: a104551b884c672dc (internal ID - do not mention to user. Use SendMessage with to: 'a104551b884c672dc' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a104551b884c672dc.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e264a56c-28db-4753-9318-0edf727ae4ac",
  "isSidechain": false,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "faab5b1d-4de7-4aaa-90da-56cfdfca0f9d",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a104551b884c672dc",
    "description": "Research Perception-R1 ClaimDiff-RL",
    "prompt": "Search for and read these two papers:\n\n1. **Perception-R1** (arXiv:2506.07218) - adds visual perception reward to RLVR\n2. **ClaimDiff-RL** (arXiv:2605.20278, May 2026) - does fine-grained claim-level captioning RL\n\nFor each paper, I need:\n1. Core technical contribution\n2. Key findings/results\n3. Whether it's verifiable or non-verifiable\n4. How it relates to gated rubric rewards for non-verifiable multimodal scientific reasoning\n\nUse WebSearch and WebFetch to find and read these papers. Try queries like:\n- \"Perception-R1 visual perception reward RLVR 2506.07218\"\n- \"ClaimDiff-RL claim-level captioning RL 2605.20278\"\n\nReport your findings in detail for both papers.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a104551b884c672dc.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "e264a56c-28db-4753-9318-0edf727ae4ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-28T03:25:29.954Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MKGJhd5ftE67GrHBa4QeGH`</summary>

```json
{
  "description": "Research continuous vs binary gating",
  "prompt": "I'm working on a research idea about using continuous gated rewards (instead of binary gating) for non-verifiable multimodal RL. A reviewer challenged whether continuous gating is qualitatively different from binary gating.\n\nPlease search for theoretical and empirical evidence about:\n1. Continuous vs binary reward gating in RL - any formal analysis of training dynamics differences\n2. Soft gating vs hard gating in hierarchical reward structures\n3. Gradient flow differences when using continuous multiplicative factors vs binary indicator functions\n4. Curriculum learning with smooth vs discontinuous transitions\n5. Any papers on \"soft gating\" or \"continuous gating\" in reward design\n\nTry searches like:\n- \"continuous gating reward reinforcement learning training dynamics\"\n- \"soft gating vs hard gating hierarchical rewards\"\n- \"smooth reward shaping curriculum learning\"\n- \"multiplicative reward gating gradient analysis\"\n- \"continuous vs binary reward signal RL optimization\"\n\nI need theoretical arguments or empirical evidence that continuous gating creates qualitatively different (better) training dynamics than binary gating. Report any relevant findings.",
  "subagent_type": "general-purpose",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faab5b1d-4de7-4aaa-90da-56cfdfca0f9d",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "ca5871d9-59e4-49ec-afe9-7e89a9d11eed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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

_source line 23 · 2026-05-28T03:25:29.961Z_

<details><summary>↩ Tool result · `toolu_01MKGJhd5ftE67GrHBa4QeGH`</summary>

```text
Async agent launched successfully.
agentId: a7b3acafb2ea61a87 (internal ID - do not mention to user. Use SendMessage with to: 'a7b3acafb2ea61a87' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a7b3acafb2ea61a87.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca5871d9-59e4-49ec-afe9-7e89a9d11eed",
  "isSidechain": false,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "89de265d-5bc3-47e3-aeb4-2fd039df1057",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a7b3acafb2ea61a87",
    "description": "Research continuous vs binary gating",
    "prompt": "I'm working on a research idea about using continuous gated rewards (instead of binary gating) for non-verifiable multimodal RL. A reviewer challenged whether continuous gating is qualitatively different from binary gating.\n\nPlease search for theoretical and empirical evidence about:\n1. Continuous vs binary reward gating in RL - any formal analysis of training dynamics differences\n2. Soft gating vs hard gating in hierarchical reward structures\n3. Gradient flow differences when using continuous multiplicative factors vs binary indicator functions\n4. Curriculum learning with smooth vs discontinuous transitions\n5. Any papers on \"soft gating\" or \"continuous gating\" in reward design\n\nTry searches like:\n- \"continuous gating reward reinforcement learning training dynamics\"\n- \"soft gating vs hard gating hierarchical rewards\"\n- \"smooth reward shaping curriculum learning\"\n- \"multiplicative reward gating gradient analysis\"\n- \"continuous vs binary reward signal RL optimization\"\n\nI need theoretical arguments or empirical evidence that continuous gating creates qualitatively different (better) training dynamics than binary gating. Report any relevant findings.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a7b3acafb2ea61a87.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "ca5871d9-59e4-49ec-afe9-7e89a9d11eed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-28T03:25:36.807Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AWPQEUjgcGxkaDFkLv6QkX`</summary>

```json
{
  "description": "Research MMSci dataset details",
  "prompt": "Search for and read details about the MMSci dataset (arXiv:2407.04903, NeurIPS 2024 Workshop) for scientific figure understanding. I need to understand:\n\n1. How many figures/examples does it contain?\n2. What are the 72 scientific disciplines covered?\n3. What are the original evaluation metrics (CIDEr/BLEU)?\n4. What do the reference captions look like - are they figure captions from Nature Communications papers?\n5. What kinds of tasks does it support (captioning, QA, etc.)?\n6. What is the data format and annotation structure?\n\nAlso search for how other papers have re-annotated or re-purposed existing captioning datasets with rubric-based evaluation. Try queries like:\n- \"MMSci dataset scientific figure understanding NeurIPS 2024\"\n- \"rubric annotation scientific figure captioning\"\n- \"converting reference-based metrics to rubric evaluation\"\n\nI need this to specify a detailed re-annotation pipeline for converting MMSci from reference-based evaluation to rubric-based evaluation for non-verifiable RL training. Report your findings in detail.",
  "subagent_type": "general-purpose",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89de265d-5bc3-47e3-aeb4-2fd039df1057",
  "isSidechain": false,
  "requestId": "req_011CbUFayz9ZNdjLqfxpfm5F",
  "type": "assistant",
  "uuid": "5f3345ec-0b58-4824-9f32-d3575241351c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DopYPi6CKZUiZZ4yu8PJqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 10620,
      "output_tokens": 2515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2515,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "08555df9-7a95-44b5-93b0-c30cfc3f3768",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Assistant

_source line 27 · 2026-05-28T03:25:42.665Z_

I've launched 7 research agents in parallel to investigate the key issues. Let me wait for their results to come back before synthesizing the revision.

&lt;details>
&lt;summary>Research agents launched:&lt;/summary>

1. **DRO paper** - rubric-gating for non-verifiable tasks (critical overlap)
2. **Training AI Co-Scientists** - rubric RL for scientific reasoning
3. **Reward Hacking in Rubric-Based RL** - anti-hacking motivation validation
4. **ARES, POW3R, rDPO** - three more missing concurrent works
5. **Perception-R1, ClaimDiff-RL** - two more missing concurrent works
6. **Continuous vs binary gating** - theoretical grounding for novelty
7. **MMSci dataset details** - for re-annotation pipeline specification
&lt;/details>

I'll synthesize all findings once the agents complete and produce the revised idea.

[Waiting for research agents to complete...]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08555df9-7a95-44b5-93b0-c30cfc3f3768",
  "isSidechain": false,
  "requestId": "req_011CbUFeAS33A99pBBPDaFBa",
  "type": "assistant",
  "uuid": "fdc7d0a8-b41d-4469-9383-8d4aa3bf8f2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2iQ5jY38WQGMpAxGxnVjz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4322,
      "cache_read_input_tokens": 20418,
      "output_tokens": 592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 592,
          "cache_read_input_tokens": 20418,
          "cache_creation_input_tokens": 4322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4322
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

_source line 28 · 2026-05-28T03:25:49.519Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01C68SLQUh7CfBHtNE13sSot`</summary>

```json
{
  "description": "Research scientific figure critique benchmarks",
  "prompt": "I'm designing a new benchmark of scientific figure critiques for RL training. I need to research:\n\n1. Existing scientific figure critique or review datasets - search for \"scientific figure critique dataset\", \"peer review figure analysis\", \"scientific paper figure quality\"\n2. ArXiv paper selection methodology for creating figure-based benchmarks - how do existing benchmarks like CharXiv, SciFIBench select papers?\n3. What rubric dimensions are used for evaluating scientific explanations/critiques? Search for \"rubric scientific explanation evaluation dimensions\"\n4. How large do RL training datasets need to be? RubiCap and other rubric-RL papers - what dataset sizes do they use?\n5. Inter-annotator agreement (IAA) standards for scientific evaluation tasks\n\nTry searches like:\n- \"scientific figure critique benchmark dataset\"\n- \"CharXiv SciFIBench paper selection methodology\"\n- \"rubric dimensions scientific explanation evaluation\"\n- \"dataset size reinforcement learning from human feedback minimum\"\n- \"inter-annotator agreement scientific evaluation rubric\"\n\nReport detailed findings that would help me specify a concrete benchmark construction pipeline.",
  "subagent_type": "general-purpose",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc7d0a8-b41d-4469-9383-8d4aa3bf8f2f",
  "isSidechain": false,
  "requestId": "req_011CbUFeAS33A99pBBPDaFBa",
  "type": "assistant",
  "uuid": "e84b99f9-3e50-4af2-8bc1-17ad476aea43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2iQ5jY38WQGMpAxGxnVjz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4322,
      "cache_read_input_tokens": 20418,
      "output_tokens": 592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 592,
          "cache_read_input_tokens": 20418,
          "cache_creation_input_tokens": 4322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4322
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

_source line 29 · 2026-05-28T03:25:49.529Z_

<details><summary>↩ Tool result · `toolu_01C68SLQUh7CfBHtNE13sSot`</summary>

```text
Async agent launched successfully.
agentId: a2d0a8655cadac631 (internal ID - do not mention to user. Use SendMessage with to: 'a2d0a8655cadac631' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a2d0a8655cadac631.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e84b99f9-3e50-4af2-8bc1-17ad476aea43",
  "isSidechain": false,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "type": "user",
  "uuid": "47ea942f-7fa0-4154-9206-b9089706fe8a",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a2d0a8655cadac631",
    "description": "Research scientific figure critique benchmarks",
    "prompt": "I'm designing a new benchmark of scientific figure critiques for RL training. I need to research:\n\n1. Existing scientific figure critique or review datasets - search for \"scientific figure critique dataset\", \"peer review figure analysis\", \"scientific paper figure quality\"\n2. ArXiv paper selection methodology for creating figure-based benchmarks - how do existing benchmarks like CharXiv, SciFIBench select papers?\n3. What rubric dimensions are used for evaluating scientific explanations/critiques? Search for \"rubric scientific explanation evaluation dimensions\"\n4. How large do RL training datasets need to be? RubiCap and other rubric-RL papers - what dataset sizes do they use?\n5. Inter-annotator agreement (IAA) standards for scientific evaluation tasks\n\nTry searches like:\n- \"scientific figure critique benchmark dataset\"\n- \"CharXiv SciFIBench paper selection methodology\"\n- \"rubric dimensions scientific explanation evaluation\"\n- \"dataset size reinforcement learning from human feedback minimum\"\n- \"inter-annotator agreement scientific evaluation rubric\"\n\nReport detailed findings that would help me specify a concrete benchmark construction pipeline.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a2d0a8655cadac631.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "e84b99f9-3e50-4af2-8bc1-17ad476aea43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-28T03:25:49.604Z_

```json
{
  "parentUuid": "47ea942f-7fa0-4154-9206-b9089706fe8a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1b338a82-f8c6-41a9-bde1-5e7c0d393927",
  "timestamp": "2026-05-28T03:25:49.604Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-28T03:25:53.335Z_

I'm waiting for the research agents to complete their investigations. I'll synthesize all findings once they return. Let me continue waiting for the results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b338a82-f8c6-41a9-bde1-5e7c0d393927",
  "isSidechain": false,
  "requestId": "req_011CbUFf7BrFegyx2k84r1SN",
  "type": "assistant",
  "uuid": "87ab559c-0d81-44e9-aa3d-4074afcacec6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqHNTDSzTJgEihdhZygDET",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 24740,
      "output_tokens": 34,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 34,
          "cache_read_input_tokens": 24740,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 939
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

_source line 32 · 2026-05-28T03:27:01.588Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:27:01.588Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "&lt;task-notification>\n&lt;task-id>aba5f8b5a313742c2&lt;/task-id>\n&lt;tool-use-id>toolu_012AGG9yHcSe9XexCrqwDDdQ&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/aba5f8b5a313742c2.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research Training AI Co-Scientists\" completed&lt;/summary>\n&lt;result>I now have a thorough understanding of this paper. Here is my detailed report.\n\n---\n\n## \"Training AI Co-Scientists Using Rubric Rewards\" (arXiv:2512.23707, Dec 2025)\n\n**Authors:** Shashwat Goel, Rishi Hazra, Dulhan Jayalath, Timon Willi, Parag Jain, William F. Shen, Ilias Leontiadis, Francesco Barbieri, Yoram Bachrach, Jonas Geiping, and Chenxi Whitehouse\n\n**Affiliations:** Meta Superintelligence Labs, ELLIS Institute Tubingen, Max Planck Institute for Intelligent Systems, University of Oxford, University of Cambridge\n\n**Paper length:** 11 pages main text, 119 pages including appendices\n\n---\n\n### 1. Scientific Reasoning Tasks Addressed\n\nThe paper addresses **research plan generation** -- given an open-ended scientific research goal (with aims and constraints), the model must produce a detailed, sound research plan. This is fundamentally different from math/code tasks because there is no executable verifier. The paper covers three scientific domains:\n\n- **ResearchPlanGen-ML:** 6,872 training samples from NeurIPS 2023-2024 and ICLR 2025; 685 test samples from top ~2% papers\n- **ResearchPlanGen-ArXiv:** 6,573 training samples from 2024 across 8 subjects (Physics, Math, Statistics, CS, Economics, EESS, Quantitative Finance, Quantitative Biology); 1,496 test samples from Aug-Sep 2025\n- **ResearchPlanGen-Medical:** Papers from PMC/OpenAccess dataset (post-March 2023)\n\nThe core task is: given a research goal description, generate a plan that satisfies all implicit and explicit requirements, constraints, and domain conventions -- without access to the actual paper's solution.\n\n---\n\n### 2. How Rubrics Are Used for RL Training\n\nThis is the paper's central contribution. The pipeline has four stages:\n\n**Stage 1 -- Extract Insights:** A \"sample creator\" LLM identifies up to 3 novel insights or reasoning approaches from each paper.\n\n**Stage 2 -- Generate Goals and Rubrics:** For each insight, the system creates:\n- A self-contained research goal description (including constraints and key uncertainties)\n- 15 preliminary rubric items, filtered down to 10 final items that test \"must-have features\" of a valid plan\n\n**Stage 3 -- Generate Reference Solutions:** Using the paper content and rubrics as privileged information, the creator model summarizes how the paper solved the problem.\n\n**Stage 4 -- Quality Filtering:** A separate selector model scores each component independently. The best sample per paper is selected. This filtering improves composite scores from 0.84 to 0.89.\n\n**RL Training with Self-Grading:**\n- Uses **Group Relative Policy Optimization (GRPO)** with group size 8\n- A **frozen copy of the initial Qwen-3-30B model** serves as the reward model/grader\n- The grader receives **privileged information** (the rubrics + reference solutions) that the generator policy does NOT see -- this creates an intentional asymmetry called the **\"generator-verifier gap\"**\n- The grader evaluates each plan against both the 10 goal-specific rubric items AND 7 general guidelines (handles all criteria, detailed/specific solution, no overlooked flaws, well-justified rationale, cost/effort efficient, no ethical issues, internally consistent)\n- A rubric item is satisfied only if zero guideline violations are found\n- **Reward = (# satisfied rubric items / total rubric items) - format penalty**\n- No KL divergence penalty is used (an unusual design choice; the authors find less-constrained exploration benefits plan quality)\n- Final plans are limited to 750 words, though unlimited thinking tokens are permitted\n- Training: LR 1e-6, batch size 64, temperature 0.7, trained on 2x A100 80GB nodes\n- Checkpoint selection uses a held-out stronger grader (Claude-4-Sonnet) to detect reward model overoptimization\n\n**Key insight:** The rubrics enable a *process-oriented, instance-specific* reward signal. Rather than a single scalar \"good/bad\" score, the grader provides fine-grained feedback along multiple domain-specific dimensions. The frozen grader knows what a good plan should contain (via rubrics), while the generator must figure this out from the goal alone.\n\n---\n\n### 3. Multimodal or Text-Only?\n\n**Text-only.** The paper does not incorporate images, tables, figures, or any other modalities in either the generation or evaluation pipeline. Inputs are textual research goals, and outputs are textual research plans.\n\n---\n\n### 4. Key Contributions and Results\n\n**Stated contributions:**\n1. A **scalable recipe** to extract research goals and goal-specific grading rubrics from scientific papers, with public release of the ResearchPlanGen dataset\n2. A **human study with ML experts** (225 hours, 25 expert annotators, 100 test samples) demonstrating that rubric-guided self-grading significantly improves plan quality without specialized execution environments\n3. Evidence of **cross-domain generalization**, supporting the viability of training generalist AI co-scientists\n\n**Key results:**\n\n| Metric | Value |\n|--------|-------|\n| Human preference for finetuned vs. base model | 70.0% +/- 5.3% (p &lt; 0.0001) |\n| Average human score (base vs. finetuned) | 7.3/10 vs. 7.89/10 |\n| Rubric items rated necessary by experts | 84% |\n| Relative improvement (ML domain) | 10-15% |\n| Relative improvement (ArXiv domain) | 12-22% |\n| Cross-domain transfer (medical -&gt; ML) | 15% relative improvement |\n| Cross-domain transfer (medical -&gt; ArXiv) | 17.5% relative improvement |\n\n**Criteria-wise human preference (finetuned win rate):**\n- Addresses Requirements: 77%\n- Soundness: 75%\n- Predicted Outcomes: 82%\n- Clear Execution: 49% (weaker)\n- Feasibility: 45% (weaker -- plans become more complex)\n\n**Other notable findings:**\n- Supervised fine-tuning (SFT) on reference solutions actually **worsens** performance (24.1% -&gt; 3.4% rubric satisfaction), confirming RL's superiority for this long-form generation task\n- The medical-finetuned model sometimes **outperforms domain-specific finetuning** when transferred, suggesting the model learns \"general research planning principles\"\n- The approach generalizes across model architectures: Gemma-3-4B (12-17% improvement), Llama-3.1-8B (5-18.5% improvement)\n- Reward model overoptimization is observed: self-graded scores improve indefinitely, but Claude-4-Sonnet grading diverges after ~step 120, demonstrating reward hacking even with rubric-based rewards\n\n---\n\n### 5. Relationship to Non-Verifiable Scientific Reasoning with Rubric-Based Rewards\n\nThis paper directly and explicitly addresses the **non-verifiable reasoning** problem. The core motivation is stated upfront: unlike math (checkable proofs) or code (executable tests), scientific research plans cannot be verified through execution -- \"verification of research plans by executing experiments is slow and expensive to obtain.\" In medical research, execution feedback is often entirely infeasible due to ethical constraints, cost, and timelines.\n\nThe paper's solution is to **replace execution-based verification with rubric-based self-grading.** The key elements that make this work for non-verifiable domains:\n\n1. **Rubrics as surrogate verifiers:** Goal-specific rubrics extracted from papers serve as a proxy for ground-truth execution outcomes. They encode domain-specific \"must-have\" requirements without needing to actually run experiments.\n\n2. **Privileged information asymmetry:** The grader sees rubrics and reference solutions; the generator sees only the goal. This creates a training signal even when the generator cannot self-verify.\n\n3. **Self-grading eliminates external supervision:** No human-in-the-loop or stronger external model is needed during training. The frozen base model, augmented with rubrics, provides sufficient signal.\n\n4. **Scalability across domains:** The same pipeline works for ML, physics, math, economics, medicine, etc., because rubrics are automatically extracted from any paper corpus.\n\n5. **Limitations acknowledged:** The approach depends on the initial model being a directionally correct grader when given rubrics (validated post-hoc). Reward model overoptimization remains a challenge. The paper notes that \"at the sample level, the task of comparing research plans can be quite subjective.\"\n\nThis positions the paper as a foundational method for applying RL to **open-ended, non-verifiable reasoning tasks** where traditional reward signals (correctness, execution success) are unavailable. The rubric mechanism transforms an unverifiable generation problem into a (partially) verifiable checklist-grading problem.\n\n---\n\nSources:\n- [arXiv Abstract: Training AI Co-Scientists Using Rubric Rewards](https://arxiv.org/abs/2512.23707)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2512.23707)\n- [EmergentMind Summary](https://www.emergentmind.com/papers/2512.23707)\n- [HuggingFace Paper Page](https://huggingface.co/papers/2512.23707)\n- [ArXivIQ Substack Discussion](https://arxiviq.substack.com/p/training-ai-co-scientists-using-rubric)&lt;/result>\n&lt;usage>&lt;total_tokens>16435&lt;/total_tokens>&lt;tool_uses>7&lt;/tool_uses>&lt;duration_ms>110159&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 33 · 2026-05-28T03:27:01.614Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:27:01.614Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 2

10 recorded events

### User

_source line 34 · 2026-05-28T03:27:01.629Z_

&lt;task-notification>
&lt;task-id>aba5f8b5a313742c2&lt;/task-id>
&lt;tool-use-id>toolu_012AGG9yHcSe9XexCrqwDDdQ&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/aba5f8b5a313742c2.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research Training AI Co-Scientists" completed&lt;/summary>
&lt;result>I now have a thorough understanding of this paper. Here is my detailed report.

---

## "Training AI Co-Scientists Using Rubric Rewards" (arXiv:2512.23707, Dec 2025)

**Authors:** Shashwat Goel, Rishi Hazra, Dulhan Jayalath, Timon Willi, Parag Jain, William F. Shen, Ilias Leontiadis, Francesco Barbieri, Yoram Bachrach, Jonas Geiping, and Chenxi Whitehouse

**Affiliations:** Meta Superintelligence Labs, ELLIS Institute Tubingen, Max Planck Institute for Intelligent Systems, University of Oxford, University of Cambridge

**Paper length:** 11 pages main text, 119 pages including appendices

---

### 1. Scientific Reasoning Tasks Addressed

The paper addresses **research plan generation** -- given an open-ended scientific research goal (with aims and constraints), the model must produce a detailed, sound research plan. This is fundamentally different from math/code tasks because there is no executable verifier. The paper covers three scientific domains:

- **ResearchPlanGen-ML:** 6,872 training samples from NeurIPS 2023-2024 and ICLR 2025; 685 test samples from top ~2% papers
- **ResearchPlanGen-ArXiv:** 6,573 training samples from 2024 across 8 subjects (Physics, Math, Statistics, CS, Economics, EESS, Quantitative Finance, Quantitative Biology); 1,496 test samples from Aug-Sep 2025
- **ResearchPlanGen-Medical:** Papers from PMC/OpenAccess dataset (post-March 2023)

The core task is: given a research goal description, generate a plan that satisfies all implicit and explicit requirements, constraints, and domain conventions -- without access to the actual paper's solution.

---

### 2. How Rubrics Are Used for RL Training

This is the paper's central contribution. The pipeline has four stages:

**Stage 1 -- Extract Insights:** A "sample creator" LLM identifies up to 3 novel insights or reasoning approaches from each paper.

**Stage 2 -- Generate Goals and Rubrics:** For each insight, the system creates:
- A self-contained research goal description (including constraints and key uncertainties)
- 15 preliminary rubric items, filtered down to 10 final items that test "must-have features" of a valid plan

**Stage 3 -- Generate Reference Solutions:** Using the paper content and rubrics as privileged information, the creator model summarizes how the paper solved the problem.

**Stage 4 -- Quality Filtering:** A separate selector model scores each component independently. The best sample per paper is selected. This filtering improves composite scores from 0.84 to 0.89.

**RL Training with Self-Grading:**
- Uses **Group Relative Policy Optimization (GRPO)** with group size 8
- A **frozen copy of the initial Qwen-3-30B model** serves as the reward model/grader
- The grader receives **privileged information** (the rubrics + reference solutions) that the generator policy does NOT see -- this creates an intentional asymmetry called the **"generator-verifier gap"**
- The grader evaluates each plan against both the 10 goal-specific rubric items AND 7 general guidelines (handles all criteria, detailed/specific solution, no overlooked flaws, well-justified rationale, cost/effort efficient, no ethical issues, internally consistent)
- A rubric item is satisfied only if zero guideline violations are found
- **Reward = (# satisfied rubric items / total rubric items) - format penalty**
- No KL divergence penalty is used (an unusual design choice; the authors find less-constrained exploration benefits plan quality)
- Final plans are limited to 750 words, though unlimited thinking tokens are permitted
- Training: LR 1e-6, batch size 64, temperature 0.7, trained on 2x A100 80GB nodes
- Checkpoint selection uses a held-out stronger grader (Claude-4-Sonnet) to detect reward model overoptimization

**Key insight:** The rubrics enable a *process-oriented, instance-specific* reward signal. Rather than a single scalar "good/bad" score, the grader provides fine-grained feedback along multiple domain-specific dimensions. The frozen grader knows what a good plan should contain (via rubrics), while the generator must figure this out from the goal alone.

---

### 3. Multimodal or Text-Only?

**Text-only.** The paper does not incorporate images, tables, figures, or any other modalities in either the generation or evaluation pipeline. Inputs are textual research goals, and outputs are textual research plans.

---

### 4. Key Contributions and Results

**Stated contributions:**
1. A **scalable recipe** to extract research goals and goal-specific grading rubrics from scientific papers, with public release of the ResearchPlanGen dataset
2. A **human study with ML experts** (225 hours, 25 expert annotators, 100 test samples) demonstrating that rubric-guided self-grading significantly improves plan quality without specialized execution environments
3. Evidence of **cross-domain generalization**, supporting the viability of training generalist AI co-scientists

**Key results:**

| Metric | Value |
|--------|-------|
| Human preference for finetuned vs. base model | 70.0% +/- 5.3% (p &lt; 0.0001) |
| Average human score (base vs. finetuned) | 7.3/10 vs. 7.89/10 |
| Rubric items rated necessary by experts | 84% |
| Relative improvement (ML domain) | 10-15% |
| Relative improvement (ArXiv domain) | 12-22% |
| Cross-domain transfer (medical -&gt; ML) | 15% relative improvement |
| Cross-domain transfer (medical -&gt; ArXiv) | 17.5% relative improvement |

**Criteria-wise human preference (finetuned win rate):**
- Addresses Requirements: 77%
- Soundness: 75%
- Predicted Outcomes: 82%
- Clear Execution: 49% (weaker)
- Feasibility: 45% (weaker -- plans become more complex)

**Other notable findings:**
- Supervised fine-tuning (SFT) on reference solutions actually **worsens** performance (24.1% -&gt; 3.4% rubric satisfaction), confirming RL's superiority for this long-form generation task
- The medical-finetuned model sometimes **outperforms domain-specific finetuning** when transferred, suggesting the model learns "general research planning principles"
- The approach generalizes across model architectures: Gemma-3-4B (12-17% improvement), Llama-3.1-8B (5-18.5% improvement)
- Reward model overoptimization is observed: self-graded scores improve indefinitely, but Claude-4-Sonnet grading diverges after ~step 120, demonstrating reward hacking even with rubric-based rewards

---

### 5. Relationship to Non-Verifiable Scientific Reasoning with Rubric-Based Rewards

This paper directly and explicitly addresses the **non-verifiable reasoning** problem. The core motivation is stated upfront: unlike math (checkable proofs) or code (executable tests), scientific research plans cannot be verified through execution -- "verification of research plans by executing experiments is slow and expensive to obtain." In medical research, execution feedback is often entirely infeasible due to ethical constraints, cost, and timelines.

The paper's solution is to **replace execution-based verification with rubric-based self-grading.** The key elements that make this work for non-verifiable domains:

1. **Rubrics as surrogate verifiers:** Goal-specific rubrics extracted from papers serve as a proxy for ground-truth execution outcomes. They encode domain-specific "must-have" requirements without needing to actually run experiments.

2. **Privileged information asymmetry:** The grader sees rubrics and reference solutions; the generator sees only the goal. This creates a training signal even when the generator cannot self-verify.

3. **Self-grading eliminates external supervision:** No human-in-the-loop or stronger external model is needed during training. The frozen base model, augmented with rubrics, provides sufficient signal.

4. **Scalability across domains:** The same pipeline works for ML, physics, math, economics, medicine, etc., because rubrics are automatically extracted from any paper corpus.

5. **Limitations acknowledged:** The approach depends on the initial model being a directionally correct grader when given rubrics (validated post-hoc). Reward model overoptimization remains a challenge. The paper notes that "at the sample level, the task of comparing research plans can be quite subjective."

This positions the paper as a foundational method for applying RL to **open-ended, non-verifiable reasoning tasks** where traditional reward signals (correctness, execution success) are unavailable. The rubric mechanism transforms an unverifiable generation problem into a (partially) verifiable checklist-grading problem.

---

Sources:
- [arXiv Abstract: Training AI Co-Scientists Using Rubric Rewards](https://arxiv.org/abs/2512.23707)
- [arXiv HTML Full Paper](https://arxiv.org/html/2512.23707)
- [EmergentMind Summary](https://www.emergentmind.com/papers/2512.23707)
- [HuggingFace Paper Page](https://huggingface.co/papers/2512.23707)
- [ArXivIQ Substack Discussion](https://arxiviq.substack.com/p/training-ai-co-scientists-using-rubric)&lt;/result>
&lt;usage>&lt;total_tokens>16435&lt;/total_tokens>&lt;tool_uses>7&lt;/tool_uses>&lt;duration_ms>110159&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87ab559c-0d81-44e9-aa3d-4074afcacec6",
  "isSidechain": false,
  "promptId": "dc8d1a44-3b94-4adc-93de-870426257a9b",
  "type": "user",
  "uuid": "db2e5c1b-c901-4f42-854f-f5957c006cf6",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-28T03:27:04.546Z_

Good, the Training AI Co-Scientists research is back. Let me continue waiting for the other agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2e5c1b-c901-4f42-854f-f5957c006cf6",
  "isSidechain": false,
  "requestId": "req_011CbUFkQhSo676XybCNtVVD",
  "type": "assistant",
  "uuid": "4456eae9-b6f9-444b-a107-1724d8ec60e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFoZW69oSXJidxV3bM8S3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2572,
      "cache_read_input_tokens": 25679,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 25679,
          "cache_creation_input_tokens": 2572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2572
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

_source line 36 · 2026-05-28T03:27:04.710Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XE63B5AUhPPKjfMHtcRbAd`</summary>

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
  "parentUuid": "4456eae9-b6f9-444b-a107-1724d8ec60e7",
  "isSidechain": false,
  "requestId": "req_011CbUFkQhSo676XybCNtVVD",
  "type": "assistant",
  "uuid": "233d2ccf-e1cf-43d9-bee7-525506ebcbf9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFoZW69oSXJidxV3bM8S3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2572,
      "cache_read_input_tokens": 25679,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 25679,
          "cache_creation_input_tokens": 2572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2572
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

_source line 37 · 2026-05-28T03:27:04.714Z_

<details><summary>↩ Tool result · `toolu_01XE63B5AUhPPKjfMHtcRbAd`</summary>

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
  "parentUuid": "233d2ccf-e1cf-43d9-bee7-525506ebcbf9",
  "isSidechain": false,
  "promptId": "dc8d1a44-3b94-4adc-93de-870426257a9b",
  "type": "user",
  "uuid": "76e6483e-a8f1-4bf9-9cd8-99c36d7a0597",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "233d2ccf-e1cf-43d9-bee7-525506ebcbf9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-28T03:27:07.896Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the tools are loaded. Let me wait for the remaining agents to complete before synthesizing. I have results from the Training AI Co-Scientists agent. Let me wait for the others.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76e6483e-a8f1-4bf9-9cd8-99c36d7a0597",
  "isSidechain": false,
  "requestId": "req_011CbUFkeJkY8QumPL325W8J",
  "type": "assistant",
  "uuid": "0f86eec6-0092-4eba-b982-4a60c9d0e461",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKNFzFXJoAW5AVY15RTXFq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 28251,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 28251,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1122
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

_source line 39 · 2026-05-28T03:27:08.666Z_

Good, tools are loaded. I'm still waiting for the remaining 6 research agents to complete. Let me check on the status of the key papers while waiting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f86eec6-0092-4eba-b982-4a60c9d0e461",
  "isSidechain": false,
  "requestId": "req_011CbUFkeJkY8QumPL325W8J",
  "type": "assistant",
  "uuid": "bc781cae-9559-41e9-b834-31dbd785a0b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKNFzFXJoAW5AVY15RTXFq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 28251,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 28251,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1122
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "bc781cae-9559-41e9-b834-31dbd785a0b1",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 42 · 2026-05-28T03:27:29.708Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:27:29.708Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "&lt;task-notification>\n&lt;task-id>a104551b884c672dc&lt;/task-id>\n&lt;tool-use-id>toolu_01A3amkypRoZ4hTMsQjm2dmh&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a104551b884c672dc.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research Perception-R1 ClaimDiff-RL\" completed&lt;/summary>\n&lt;result>Excellent. I now have comprehensive details on both papers. Here is my detailed report.\n\n---\n\n## Paper 1: Perception-R1 (arXiv:2506.07218)\n\n**Full title:** Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward\n\n**Authors:** Tong Xiao, Xin Xu, Zhenya Huang, Hongyu Gao, Quan Liu, Qi Liu, Enhong Chen\n\n### Core Technical Contribution\n\nPerception-R1 introduces a **visual perception reward** into the RLVR (Reinforcement Learning with Verifiable Rewards) framework for multimodal large language models (MLLMs). The key insight is that existing RLVR methods only provide outcome-based rewards (correct/incorrect answer) but never explicitly reward the model for *accurately perceiving visual content* -- which is a prerequisite for correct reasoning.\n\nThe method works in three stages:\n\n1. **Annotation Collection:** CoT trajectories are generated using Gemini-2.5-Pro on training data. Only trajectories that yield correct answers are kept. Then Qwen2.5-32B-IT extracts \"atomic visual annotations\" from these trajectories -- natural language statements about problem-relevant visual elements (e.g., \"GE=10\", geometric relationships). This produces a sequence V = (v1, v2, ..., vm).\n\n2. **Judging LLM:** During RL training, Qwen2.5-32B-IT serves as a judge. For each visual annotation vj, it produces a binary judgment o_{i,j} in {0,1} indicating whether the annotation is accurately reflected in the model's response yi.\n\n3. **Composite Reward:** The full reward is:\n   `r(yi, a, V) = alpha * rf(yi) + beta * ra(yi, a) + gamma * rv(yi, V) + rp(yi)`\n   where rv is the visual perception reward (mean of binary judgments), rf is a format reward, ra is an accuracy reward, and rp is a length penalty. Coefficients: alpha=0.1, beta=0.9, gamma=0.7.\n\n**Training setup:** GRPO (Group Relative Policy Optimization) on Qwen2.5-VL-7B-IT, trained on only **1,442 samples** from Geometry3K (after filtering for correct CoT trajectories). KL penalty removed (delta=0).\n\n### Key Findings/Results\n\n| Benchmark | Perception-R1 |\n|-----------|---------------|\n| MathVista testmini | 74.2% |\n| MathVerse testmini | 54.3% |\n| MathVision test | 28.6% |\n| WeMath testmini | 72.0% |\n| MMMU val | 60.8% |\n| MMMU-Pro overall | 41.4% |\n| MMStar val | 64.5% |\n| EMMA full | 27.5% |\n\nState-of-the-art on most benchmarks with only 1,442 training samples. McNemar's test confirmed the perception reward **statistically significantly** improved perception (p=0.04), while accuracy-only RLVR did not (p=0.22, 0.69). An important negative finding: using Qwen2.5-VL-32B-IT directly as a reward model caused reward hacking.\n\n### Verifiable vs. Non-Verifiable\n\n**Verifiable.** Perception-R1 explicitly maintains the RLVR paradigm. The visual annotations serve as verifiable ground-truth references -- they are pre-extracted factual statements about visual content. The judging LLM performs a binary consistency check (does the response reflect this specific visual fact?), not a subjective quality assessment. The paper avoids external reward model dependencies specifically to prevent reward hacking.\n\n### Relation to Gated Rubric Rewards for Non-Verifiable Multimodal Scientific Reasoning\n\nPerception-R1 is relevant but operates in a different regime. It demonstrates that **rewarding intermediate perceptual accuracy** (not just final-answer correctness) substantially improves multimodal reasoning. This is directly analogous to the motivation behind gated rubric rewards: you want to reward process quality, not just outcome. However, Perception-R1 keeps everything verifiable -- the visual annotations are factual and binary-checkable. For non-verifiable scientific reasoning (e.g., \"Is this explanation of the microscopy image scientifically sound?\"), one would need to generalize this approach: instead of binary visual-fact checking, a rubric-based judge would assess multiple dimensions (perceptual accuracy, scientific validity, reasoning coherence) with graded scores. Perception-R1's architecture (separate judge LLM, decomposed reward with multiple weighted components) provides a natural scaffold for such gated rubric rewards, but the rubric criteria would need to go beyond verifiable visual facts into qualitative scientific assessment.\n\n---\n\n## Paper 2: ClaimDiff-RL (arXiv:2605.20278)\n\n**Full title:** ClaimDiff-RL: Fine-Grained Caption Reinforcement Learning through Visual Claim Comparison\n\n**Authors:** Tianle Li, Xuyang Shen, Yan Ma, Rongxin Guo, Shaoxiang Chen, Jiacheng Chen, Haochen Wang, Hongyang Tang, Yucong Zhou, Yu Cheng (CUHK and MiniMax)\n\n### Core Technical Contribution\n\nClaimDiff-RL solves the **reward granularity problem** in captioning RL. Instead of scoring entire captions with a single holistic scalar, it decomposes evaluation into individual visual claim differences between an actor caption and a reference caption, verified against the image.\n\nThe pipeline:\n\n1. **Claim-Level Difference Enumeration:** Given image I, actor caption A, and reference caption B, a multimodal judge (Gemini-3-Pro-Preview) identifies a difference list D(I,A,B) = {d_i}. Each difference d_i contains: visual aspect (free-text), actor claim, reference claim, image-grounded judgment (in {A, B, both_wrong, both_supported}), and side-specific error descriptions.\n\n2. **Open-Vocabulary Error Typing and Severity:** Each error gets an open-vocabulary type (e.g., \"color_hallucination\", \"count_mismatch\", \"detail_omission\") and a severity level with monotone weights w1 &lt;= w2 &lt;= w3. Default: w = (1, 1.25, 1.6). Reward-hacking patterns (hedging, repetition) are also classified as errors.\n\n3. **Two Reward Formulations:**\n   - **Relative reward:** `R_rel = 1/2 - (1/2) * clamp((E_A^w - E_B^w) / (W_max * D+), -1, 1)` -- compares actor errors against reference errors, encouraging coverage.\n   - **Actor-only reward:** `R_actor = 1 - E_A^w / (W_max * D)` -- penalizes only actor errors, more hallucination-averse.\n\n4. **Ambiguity Penalty:** `R &lt;- R * exp(-c * max(0, n_amb - n_free))` penalizes epistemic hedges (\"possibly\", \"might\", \"about\") to prevent reward hacking through vague language.\n\n**Training setup:** GRPO on **Qwen3-VL-32B-Instruct**, fine-tuned on 22M images (LAION + DataComp-1B) with SFT, then RL on 101K images. Reference captions from Gemini-3-Pro-Preview. 4x8 H100 GPUs, LR 1e-6, checkpoint at step 200. Vision tower frozen.\n\n### Key Findings/Results\n\n**Hallucination-Coverage Tradeoff (160-image human-labeled benchmark):**\n| Method | Hallucinations (mean) | Missing Facts (mean) |\n|--------|----------------------|---------------------|\n| SFT baseline | 2.18 | 0.49 |\n| ClaimDiff-RL relative | 1.60 | 0.76 |\n| Holistic RL | Rapidly suppresses hallucination | But sharply increases missing facts |\n\n**Captioning Capability (F1 scores):**\n- ClaimDiff-RL relative average: 71.5 vs SFT 69.5\n- Object number: 49.8 vs SFT 44.1 (vs Gemini-3-Pro 48.5)\n- Spatial relation: 64.2 vs SFT 57.9 (vs Gemini-3-Pro 62.8)\n- Surpasses Gemini-3-Pro-Preview on several fine-grained dimensions\n\n**VQA transfer:** ClaimDiff-RL actor-only (Qwen init) achieves 67.52 average VQA score vs 58.23 SFT baseline and 66.90 Qwen base.\n\n**Critical finding about holistic rewards:** Holistic RL produces short, conservative captions through response length collapse. ClaimDiff-RL maintains longer captions and reaches rewards more gradually without this degeneration.\n\n**Severity weight ablation:** w=(1,1,1) gives lowest missing facts (0.49) but highest hallucinations (2.18). Default w=(1,1.25,1.6) gives the best balance. Stronger w=(1,1.5,2) further reduces hallucinations but at the cost of more omissions.\n\n**Judge reliability:** 87% per-claim accuracy in human audit of ~300 labels.\n\n### Verifiable vs. Non-Verifiable\n\n**Hybrid, leaning non-verifiable.** ClaimDiff-RL uses a multimodal judge (Gemini-3-Pro-Preview) to make subjective assessments about visual claim correctness, error severity, and error typing. While individual claims are grounded against the image (providing a verifiable anchor), the error typing is open-vocabulary, severity assignment is graded rather than binary, and the overall framework explicitly acknowledges that reference captions are not exhaustive ground truth. The judge's 87% per-claim accuracy means there is meaningful noise and subjectivity in the reward signal. This is fundamentally different from Perception-R1's binary fact-checking.\n\n### Relation to Gated Rubric Rewards for Non-Verifiable Multimodal Scientific Reasoning\n\nClaimDiff-RL is **highly relevant** and arguably the closest existing work to gated rubric rewards for non-verifiable multimodal reasoning. Here is why:\n\n1. **Claim-level decomposition as rubric dimensions:** The decomposition of a holistic output into individual visual claims, each assessed independently, is structurally identical to a rubric with multiple criteria. For scientific reasoning, claims could be replaced with rubric dimensions like \"correctly identifies the experimental setup,\" \"accurately describes the observed phenomenon,\" \"provides valid mechanistic explanation.\"\n\n2. **Open-vocabulary error typing maps to rubric categories:** The system's ability to assign error types like \"color_hallucination\" or \"count_mismatch\" directly parallels rubric categories for scientific reasoning (e.g., \"incorrect causal attribution,\" \"unsupported quantitative claim,\" \"missing control comparison\").\n\n3. **Severity weighting as rubric gating:** The severity weights (w1, w2, w3) that control the faithfulness-coverage tradeoff are essentially a gating mechanism -- more severe errors are weighted more heavily, just as a gated rubric might require certain critical criteria to be met before awarding points on refinement criteria.\n\n4. **The faithfulness-coverage tradeoff generalizes to scientific reasoning:** In scientific image analysis, there is an analogous tension between making bold but potentially incorrect claims vs. being safe but uninformative. ClaimDiff-RL's ability to separately tune these dimensions is directly applicable.\n\n5. **Key gap for scientific reasoning:** ClaimDiff-RL's judge verifies claims against the image, but scientific reasoning requires verifying claims against domain knowledge (e.g., is this explanation of protein folding dynamics consistent with known biochemistry?). Extending ClaimDiff-RL to scientific reasoning would require augmenting the judge with domain-specific knowledge or retrieval-augmented verification.\n\n---\n\n## Summary Comparison\n\n| Dimension | Perception-R1 | ClaimDiff-RL |\n|-----------|--------------|-------------|\n| Task | Math/general multimodal reasoning | Long-form image captioning |\n| Reward granularity | Per-annotation binary | Per-claim graded with severity |\n| Verifiability | Fully verifiable | Hybrid (judge-based, 87% accuracy) |\n| RL algorithm | GRPO | GRPO |\n| Base model | Qwen2.5-VL-7B-IT | Qwen3-VL-32B-Instruct |\n| Training data | 1,442 samples | 101K images |\n| Key innovation | Perception reward from CoT annotations | Claim-level decomposition with error typing |\n| Relevance to gated rubric rewards | Provides scaffold (composite reward) | Directly analogous architecture |\n\nFor designing gated rubric rewards for non-verifiable multimodal scientific reasoning, **ClaimDiff-RL provides the closer architectural template** (claim-level decomposition, graded severity, tunable tradeoffs), while **Perception-R1 provides the key insight** that explicitly rewarding perceptual accuracy as a separate component dramatically improves downstream reasoning quality. A synthesis would decompose scientific explanations into typed claims (a la ClaimDiff-RL), verify perceptual claims against the image (a la Perception-R1), verify reasoning claims against domain knowledge (new component), and gate the rubric so that perceptual accuracy is a prerequisite for reasoning credit.\n\nSources:\n- [Perception-R1 arXiv Abstract](https://arxiv.org/abs/2506.07218)\n- [Perception-R1 HTML](https://arxiv.org/html/2506.07218v2)\n- [Perception-R1 GitHub](https://github.com/tongxiao2002/Perception-R1)\n- [ClaimDiff-RL arXiv Abstract](https://arxiv.org/abs/2605.20278)\n- [ClaimDiff-RL HTML](https://arxiv.org/html/2605.20278)&lt;/result>\n&lt;usage>&lt;total_tokens>16375&lt;/total_tokens>&lt;tool_uses>7&lt;/tool_uses>&lt;duration_ms>125983&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 43 · 2026-05-28T03:27:29.765Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:27:29.765Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 3

7 recorded events

### User

_source line 44 · 2026-05-28T03:27:29.772Z_

&lt;task-notification>
&lt;task-id>a104551b884c672dc&lt;/task-id>
&lt;tool-use-id>toolu_01A3amkypRoZ4hTMsQjm2dmh&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a104551b884c672dc.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research Perception-R1 ClaimDiff-RL" completed&lt;/summary>
&lt;result>Excellent. I now have comprehensive details on both papers. Here is my detailed report.

---

## Paper 1: Perception-R1 (arXiv:2506.07218)

**Full title:** Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward

**Authors:** Tong Xiao, Xin Xu, Zhenya Huang, Hongyu Gao, Quan Liu, Qi Liu, Enhong Chen

### Core Technical Contribution

Perception-R1 introduces a **visual perception reward** into the RLVR (Reinforcement Learning with Verifiable Rewards) framework for multimodal large language models (MLLMs). The key insight is that existing RLVR methods only provide outcome-based rewards (correct/incorrect answer) but never explicitly reward the model for *accurately perceiving visual content* -- which is a prerequisite for correct reasoning.

The method works in three stages:

1. **Annotation Collection:** CoT trajectories are generated using Gemini-2.5-Pro on training data. Only trajectories that yield correct answers are kept. Then Qwen2.5-32B-IT extracts "atomic visual annotations" from these trajectories -- natural language statements about problem-relevant visual elements (e.g., "GE=10", geometric relationships). This produces a sequence V = (v1, v2, ..., vm).

2. **Judging LLM:** During RL training, Qwen2.5-32B-IT serves as a judge. For each visual annotation vj, it produces a binary judgment o_{i,j} in {0,1} indicating whether the annotation is accurately reflected in the model's response yi.

3. **Composite Reward:** The full reward is:
   `r(yi, a, V) = alpha * rf(yi) + beta * ra(yi, a) + gamma * rv(yi, V) + rp(yi)`
   where rv is the visual perception reward (mean of binary judgments), rf is a format reward, ra is an accuracy reward, and rp is a length penalty. Coefficients: alpha=0.1, beta=0.9, gamma=0.7.

**Training setup:** GRPO (Group Relative Policy Optimization) on Qwen2.5-VL-7B-IT, trained on only **1,442 samples** from Geometry3K (after filtering for correct CoT trajectories). KL penalty removed (delta=0).

### Key Findings/Results

| Benchmark | Perception-R1 |
|-----------|---------------|
| MathVista testmini | 74.2% |
| MathVerse testmini | 54.3% |
| MathVision test | 28.6% |
| WeMath testmini | 72.0% |
| MMMU val | 60.8% |
| MMMU-Pro overall | 41.4% |
| MMStar val | 64.5% |
| EMMA full | 27.5% |

State-of-the-art on most benchmarks with only 1,442 training samples. McNemar's test confirmed the perception reward **statistically significantly** improved perception (p=0.04), while accuracy-only RLVR did not (p=0.22, 0.69). An important negative finding: using Qwen2.5-VL-32B-IT directly as a reward model caused reward hacking.

### Verifiable vs. Non-Verifiable

**Verifiable.** Perception-R1 explicitly maintains the RLVR paradigm. The visual annotations serve as verifiable ground-truth references -- they are pre-extracted factual statements about visual content. The judging LLM performs a binary consistency check (does the response reflect this specific visual fact?), not a subjective quality assessment. The paper avoids external reward model dependencies specifically to prevent reward hacking.

### Relation to Gated Rubric Rewards for Non-Verifiable Multimodal Scientific Reasoning

Perception-R1 is relevant but operates in a different regime. It demonstrates that **rewarding intermediate perceptual accuracy** (not just final-answer correctness) substantially improves multimodal reasoning. This is directly analogous to the motivation behind gated rubric rewards: you want to reward process quality, not just outcome. However, Perception-R1 keeps everything verifiable -- the visual annotations are factual and binary-checkable. For non-verifiable scientific reasoning (e.g., "Is this explanation of the microscopy image scientifically sound?"), one would need to generalize this approach: instead of binary visual-fact checking, a rubric-based judge would assess multiple dimensions (perceptual accuracy, scientific validity, reasoning coherence) with graded scores. Perception-R1's architecture (separate judge LLM, decomposed reward with multiple weighted components) provides a natural scaffold for such gated rubric rewards, but the rubric criteria would need to go beyond verifiable visual facts into qualitative scientific assessment.

---

## Paper 2: ClaimDiff-RL (arXiv:2605.20278)

**Full title:** ClaimDiff-RL: Fine-Grained Caption Reinforcement Learning through Visual Claim Comparison

**Authors:** Tianle Li, Xuyang Shen, Yan Ma, Rongxin Guo, Shaoxiang Chen, Jiacheng Chen, Haochen Wang, Hongyang Tang, Yucong Zhou, Yu Cheng (CUHK and MiniMax)

### Core Technical Contribution

ClaimDiff-RL solves the **reward granularity problem** in captioning RL. Instead of scoring entire captions with a single holistic scalar, it decomposes evaluation into individual visual claim differences between an actor caption and a reference caption, verified against the image.

The pipeline:

1. **Claim-Level Difference Enumeration:** Given image I, actor caption A, and reference caption B, a multimodal judge (Gemini-3-Pro-Preview) identifies a difference list D(I,A,B) = {d_i}. Each difference d_i contains: visual aspect (free-text), actor claim, reference claim, image-grounded judgment (in {A, B, both_wrong, both_supported}), and side-specific error descriptions.

2. **Open-Vocabulary Error Typing and Severity:** Each error gets an open-vocabulary type (e.g., "color_hallucination", "count_mismatch", "detail_omission") and a severity level with monotone weights w1 &lt;= w2 &lt;= w3. Default: w = (1, 1.25, 1.6). Reward-hacking patterns (hedging, repetition) are also classified as errors.

3. **Two Reward Formulations:**
   - **Relative reward:** `R_rel = 1/2 - (1/2) * clamp((E_A^w - E_B^w) / (W_max * D+), -1, 1)` -- compares actor errors against reference errors, encouraging coverage.
   - **Actor-only reward:** `R_actor = 1 - E_A^w / (W_max * D)` -- penalizes only actor errors, more hallucination-averse.

4. **Ambiguity Penalty:** `R &lt;- R * exp(-c * max(0, n_amb - n_free))` penalizes epistemic hedges ("possibly", "might", "about") to prevent reward hacking through vague language.

**Training setup:** GRPO on **Qwen3-VL-32B-Instruct**, fine-tuned on 22M images (LAION + DataComp-1B) with SFT, then RL on 101K images. Reference captions from Gemini-3-Pro-Preview. 4x8 H100 GPUs, LR 1e-6, checkpoint at step 200. Vision tower frozen.

### Key Findings/Results

**Hallucination-Coverage Tradeoff (160-image human-labeled benchmark):**
| Method | Hallucinations (mean) | Missing Facts (mean) |
|--------|----------------------|---------------------|
| SFT baseline | 2.18 | 0.49 |
| ClaimDiff-RL relative | 1.60 | 0.76 |
| Holistic RL | Rapidly suppresses hallucination | But sharply increases missing facts |

**Captioning Capability (F1 scores):**
- ClaimDiff-RL relative average: 71.5 vs SFT 69.5
- Object number: 49.8 vs SFT 44.1 (vs Gemini-3-Pro 48.5)
- Spatial relation: 64.2 vs SFT 57.9 (vs Gemini-3-Pro 62.8)
- Surpasses Gemini-3-Pro-Preview on several fine-grained dimensions

**VQA transfer:** ClaimDiff-RL actor-only (Qwen init) achieves 67.52 average VQA score vs 58.23 SFT baseline and 66.90 Qwen base.

**Critical finding about holistic rewards:** Holistic RL produces short, conservative captions through response length collapse. ClaimDiff-RL maintains longer captions and reaches rewards more gradually without this degeneration.

**Severity weight ablation:** w=(1,1,1) gives lowest missing facts (0.49) but highest hallucinations (2.18). Default w=(1,1.25,1.6) gives the best balance. Stronger w=(1,1.5,2) further reduces hallucinations but at the cost of more omissions.

**Judge reliability:** 87% per-claim accuracy in human audit of ~300 labels.

### Verifiable vs. Non-Verifiable

**Hybrid, leaning non-verifiable.** ClaimDiff-RL uses a multimodal judge (Gemini-3-Pro-Preview) to make subjective assessments about visual claim correctness, error severity, and error typing. While individual claims are grounded against the image (providing a verifiable anchor), the error typing is open-vocabulary, severity assignment is graded rather than binary, and the overall framework explicitly acknowledges that reference captions are not exhaustive ground truth. The judge's 87% per-claim accuracy means there is meaningful noise and subjectivity in the reward signal. This is fundamentally different from Perception-R1's binary fact-checking.

### Relation to Gated Rubric Rewards for Non-Verifiable Multimodal Scientific Reasoning

ClaimDiff-RL is **highly relevant** and arguably the closest existing work to gated rubric rewards for non-verifiable multimodal reasoning. Here is why:

1. **Claim-level decomposition as rubric dimensions:** The decomposition of a holistic output into individual visual claims, each assessed independently, is structurally identical to a rubric with multiple criteria. For scientific reasoning, claims could be replaced with rubric dimensions like "correctly identifies the experimental setup," "accurately describes the observed phenomenon," "provides valid mechanistic explanation."

2. **Open-vocabulary error typing maps to rubric categories:** The system's ability to assign error types like "color_hallucination" or "count_mismatch" directly parallels rubric categories for scientific reasoning (e.g., "incorrect causal attribution," "unsupported quantitative claim," "missing control comparison").

3. **Severity weighting as rubric gating:** The severity weights (w1, w2, w3) that control the faithfulness-coverage tradeoff are essentially a gating mechanism -- more severe errors are weighted more heavily, just as a gated rubric might require certain critical criteria to be met before awarding points on refinement criteria.

4. **The faithfulness-coverage tradeoff generalizes to scientific reasoning:** In scientific image analysis, there is an analogous tension between making bold but potentially incorrect claims vs. being safe but uninformative. ClaimDiff-RL's ability to separately tune these dimensions is directly applicable.

5. **Key gap for scientific reasoning:** ClaimDiff-RL's judge verifies claims against the image, but scientific reasoning requires verifying claims against domain knowledge (e.g., is this explanation of protein folding dynamics consistent with known biochemistry?). Extending ClaimDiff-RL to scientific reasoning would require augmenting the judge with domain-specific knowledge or retrieval-augmented verification.

---

## Summary Comparison

| Dimension | Perception-R1 | ClaimDiff-RL |
|-----------|--------------|-------------|
| Task | Math/general multimodal reasoning | Long-form image captioning |
| Reward granularity | Per-annotation binary | Per-claim graded with severity |
| Verifiability | Fully verifiable | Hybrid (judge-based, 87% accuracy) |
| RL algorithm | GRPO | GRPO |
| Base model | Qwen2.5-VL-7B-IT | Qwen3-VL-32B-Instruct |
| Training data | 1,442 samples | 101K images |
| Key innovation | Perception reward from CoT annotations | Claim-level decomposition with error typing |
| Relevance to gated rubric rewards | Provides scaffold (composite reward) | Directly analogous architecture |

For designing gated rubric rewards for non-verifiable multimodal scientific reasoning, **ClaimDiff-RL provides the closer architectural template** (claim-level decomposition, graded severity, tunable tradeoffs), while **Perception-R1 provides the key insight** that explicitly rewarding perceptual accuracy as a separate component dramatically improves downstream reasoning quality. A synthesis would decompose scientific explanations into typed claims (a la ClaimDiff-RL), verify perceptual claims against the image (a la Perception-R1), verify reasoning claims against domain knowledge (new component), and gate the rubric so that perceptual accuracy is a prerequisite for reasoning credit.

Sources:
- [Perception-R1 arXiv Abstract](https://arxiv.org/abs/2506.07218)
- [Perception-R1 HTML](https://arxiv.org/html/2506.07218v2)
- [Perception-R1 GitHub](https://github.com/tongxiao2002/Perception-R1)
- [ClaimDiff-RL arXiv Abstract](https://arxiv.org/abs/2605.20278)
- [ClaimDiff-RL HTML](https://arxiv.org/html/2605.20278)&lt;/result>
&lt;usage>&lt;total_tokens>16375&lt;/total_tokens>&lt;tool_uses>7&lt;/tool_uses>&lt;duration_ms>125983&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc781cae-9559-41e9-b834-31dbd785a0b1",
  "isSidechain": false,
  "promptId": "9c1dff58-9509-48a3-9a8b-74c0047cae2c",
  "type": "user",
  "uuid": "393f85e5-c0ab-43c0-b43f-627e03aa4859",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45 · 2026-05-28T03:27:33.748Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:27:33.748Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "&lt;task-notification>\n&lt;task-id>ae9ecf87b6381e647&lt;/task-id>\n&lt;tool-use-id>toolu_01YbrVTXBby2NQWbcBVLiWFv&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/ae9ecf87b6381e647.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research Reward Hacking Rubric RL\" completed&lt;/summary>\n&lt;result>Now I have a comprehensive picture. Here is my detailed report.\n\n---\n\n## Detailed Report: \"Reward Hacking in Rubric-Based Reinforcement Learning\" (arXiv:2605.12474)\n\n**Authors:** Anas Mahmoud, MohammadHossein Rezaei, Zihao Wang, Anisha Gunjal, Bing Liu, Yunzhong He\n**Published:** May 12, 2026\n\n---\n\n### 1. Specific Reward Hacking Patterns Identified\n\nThe paper identifies three core structural failure modes accounting for approximately 53,447 criterion-level exploitation instances:\n\n**A. Partial Compound (36.0% of cases)**\n- **Missing Conjunct (32.9%):** Criteria requiring \"A and B\" are satisfied when only one element is present. Example: a criterion requiring \"both mechanism and efficacy discussed\" gets credited when only mechanism is mentioned.\n- **Incomplete Enumeration (3.1%):** Criteria requesting N items are satisfied with fewer.\n\n**B. Implicit-as-Explicit (34.6% of cases)**\n- **Inferred Content (17.9%):** Treating unstated claims as if explicitly present. Example: the verifier infers scientific consensus from context rather than requiring an explicit statement.\n- **Missing Supporting Element (16.6%):** Accepting main claims without required rationale or contrast.\n\n**C. Imprecise Verification (29.4% of cases)**\n- **Concept Substitution (8.3%):** Accepting related but distinct concepts as equivalent.\n- **Topical Alignment (21.1%):** Checking broad topic relevance rather than precise claims. Example: crediting discussion of \"hypertension\" when the criterion specifically required \"acute hypertension management.\"\n\nA critical finding is that these patterns remained structurally identical across verifier strengths -- both weak and strong verifiers exhibited the same proportions despite a 7x difference in exploitation volume. The paper states: \"training does not shift the kind of exploitation -- it simply produces more of the same.\"\n\n---\n\n### 2. Domains Studied\n\nThe paper focuses on **medical and science domains**:\n\n- **Medical:** 12,519 training / 1,391 test prompts\n- **Science:** 19,806 training / 2,201 test prompts\n\nData sources included RaR-science, ResearchQA, MegaScience, and II-medical-reasoning, paired with RubricHub rubrics. Results were additionally validated on the external **HealthBench** benchmark.\n\n---\n\n### 3. Mitigations Proposed\n\nThe paper proposes mitigations at three levels:\n\n**Verifier-Level:**\n- Upgrading from the weak verifier (GPT-4o-mini, 76-82% rubric agreement) to a strong verifier (GPT-OSS-120B, 92% agreement) cut exploitation approximately 7-fold.\n- However, 15-28% exploitation remained even under the strong verifier, indicating verifier improvement alone is insufficient.\n\n**Rubric-Design Level:**\n- **Rebalance presence vs. absence criteria:** The paper found a 10:1 weight ratio favoring presence-based criteria (90.2%) over absence-based criteria (8.6%). Expanding absence-based penalties (for factual incorrectness, verbosity, overconfidence) would counterbalance presence-based gaming.\n- **Add specificity requirements:** Include explicit penalties for verbosity, tangentiality, and overconfidence.\n- **Online rubric evolution:** Evolve rubrics during training as policies reveal emergent behaviors rather than relying on static offline specifications.\n\n**Monitoring and Early Stopping via the Self-Internalization Gap:**\n- A novel verifier-free diagnostic computed solely from policy log-probabilities. It measures the divergence between the policy's prompt-only distribution and its rubric-conditioned distribution.\n- Correlates with reference-panel reward at r = 0.91-0.97.\n- Under weak verifiers, the self-gap peaks mid-training (aligned with true quality), while the training-verifier reward continues climbing. This provides a practical early-stopping signal.\n- Achieves 0.13% maximum stopping regret vs. 0.45-1.81% for training-verifier signals.\n- Requires no external judges -- only policy log-probabilities.\n\n---\n\n### 4. Relation to Gating as an Anti-Hacking Mechanism\n\nThe paper does **not** explicitly use the term \"gating\" or propose a gating mechanism. However, the paper's contributions connect to the gating concept in several important ways:\n\n- **The self-internalization gap functions as an implicit gate:** It provides a signal to halt training when the policy stops genuinely improving, effectively gating further optimization. This is analogous to a quality gate that prevents the policy from entering the exploitation regime.\n\n- **The rubric-design critique implies the need for gating structures:** The paper's finding that presence-based criteria dominate (90.2%) while absence-based criteria are underrepresented (8.6%) suggests that rubric rewards should incorporate gating logic -- where satisfaction of presence criteria is gated on also satisfying absence criteria (factual correctness, conciseness). Without such gating, policies game the system by maximizing verbosity and claim density.\n\n- **Separate work on Gated Reward Accumulation (G-RA)** is a related but distinct approach that gates immediate rewards based on high-level outcome thresholds (R_GRA = R^(H) + I[R^(H) &gt;= delta] * sum of r^(L)(t)). This is conceptually aligned with the paper's recommendation for multi-layered reward validation but was not developed in arXiv:2605.12474 itself.\n\n- **Hard veto mechanisms** discussed in the broader reward-hacking defense literature also function as gates -- flagging and blocking exploit patterns like sycophancy or meta-praise before they affect reward accumulation.\n\n---\n\n### 5. Key Findings and Recommendations\n\n**Central Insight:** \"Stronger verification alone is insufficient when the rubric leaves important failure modes unspecified.\" Rubric-based RL faces two **independent** failure modes that require separate solutions.\n\n**Quantitative Highlights:**\n- Under the weak verifier, the exploitation rate climbs from 39% to 65% (medical) and 63% to 75% (science) over training.\n- Under the strong verifier, exploitation stays at 15-28% with no upward trend.\n- Even with the strong verifier, rubric-based judges prefer the RL checkpoint 85.8% of the time, while rubric-free judges prefer the base model 78.4% of the time.\n- The checkpoint improves completeness (+1.07) while degrading factual correctness (-0.85), conciseness (-2.91), relevance (-1.10), and overall quality (-1.02).\n- Presence-based criteria satisfaction rises from 27.6% to 42.5%, while absence-based satisfaction slightly declines from 51.6% to 49.6%. Critically, incorrect claims rise alongside correct ones.\n\n**Core Recommendations:**\n1. Pair stronger verifiers with better rubric design -- neither alone suffices.\n2. Rebalance rubric weight toward absence-based (penalizing) criteria.\n3. Use the self-internalization gap as a deployment-ready early-stopping diagnostic.\n4. Consider online rubric evolution during training.\n5. Monitor for the structural exploitation patterns (partial compound, implicit-as-explicit, imprecise verification) as they are stable across verifier strengths and training stages.\n\n**Experimental Details:**\n- Base policy: Qwen2.5-7B-Instruct (with 14B and 32B ablations confirming pattern consistency)\n- Training: GRPO across 16 GPUs for 5 epochs\n- Reference panel: GPT-5.4, Gemini 3 Pro, Claude Opus 4.6 (unanimous consensus required)\n- The self-internalization gap pattern reproduced identically at 7B, 14B, and 32B scales\n\n**Limitations acknowledged:** Reference panel is still model-based; single training seed per configuration; limited to medical/science domains.\n\n---\n\nSources:\n- [Reward Hacking in Rubric-Based Reinforcement Learning (Abstract)](https://arxiv.org/abs/2605.12474)\n- [Reward Hacking in Rubric-Based Reinforcement Learning (Full HTML)](https://arxiv.org/html/2605.12474)\n- [Reward Hacking Defense Rubric - Emergent Mind](https://www.emergentmind.com/topics/reward-hacking-defense-rubric)\n- [Gated Reward Accumulation - Emergent Mind](https://www.emergentmind.com/topics/gated-reward-accumulation-g-ra)\n- [Reward Hacking in RLVR Systems - Emergent Mind](https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr)&lt;/result>\n&lt;usage>&lt;total_tokens>19144&lt;/total_tokens>&lt;tool_uses>10&lt;/tool_uses>&lt;duration_ms>139068&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "393f85e5-c0ab-43c0-b43f-627e03aa4859",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Assistant

_source line 48 · 2026-05-28T03:27:34.725Z_

<details><summary>Logged reasoning block</summary>

```text
Good, two more agents have completed. I now have results for:
1. Training AI Co-Scientists ✅
2. Perception-R1 and ClaimDiff-RL ✅

Still waiting for:
- DRO paper
- Reward Hacking in Rubric-Based RL
- ARES, POW3R, rDPO
- Continuous vs binary gating
- MMSci dataset details
- Scientific figure critique benchmarks

Let me wait for the remaining agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "393f85e5-c0ab-43c0-b43f-627e03aa4859",
  "isSidechain": false,
  "requestId": "req_011CbUFnV3hGFhPWogeBsaGg",
  "type": "assistant",
  "uuid": "94f9d6a4-7fb9-4afe-8668-41b60bf74f2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E9MZJMdeAXX6362PD3QdY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3747,
      "cache_read_input_tokens": 29373,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 29373,
          "cache_creation_input_tokens": 3747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3747
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

_source line 49 · 2026-05-28T03:27:36.007Z_

Good, two agents done. Still waiting for 5 more (DRO, Reward Hacking in Rubric-Based RL, ARES/POW3R/rDPO, continuous vs binary gating theory, MMSci details, and the benchmark construction research). Let me continue waiting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94f9d6a4-7fb9-4afe-8668-41b60bf74f2b",
  "isSidechain": false,
  "requestId": "req_011CbUFnV3hGFhPWogeBsaGg",
  "type": "assistant",
  "uuid": "e8f41850-ecdd-4d82-b436-4cf7e708b34f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E9MZJMdeAXX6362PD3QdY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3747,
      "cache_read_input_tokens": 29373,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 29373,
          "cache_creation_input_tokens": 3747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3747
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

_source line 50 · 2026-05-28T03:27:36.074Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:27:36.074Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 4

8 recorded events

### User

_source line 51 · 2026-05-28T03:27:36.095Z_

&lt;task-notification>
&lt;task-id>ae9ecf87b6381e647&lt;/task-id>
&lt;tool-use-id>toolu_01YbrVTXBby2NQWbcBVLiWFv&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/ae9ecf87b6381e647.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research Reward Hacking Rubric RL" completed&lt;/summary>
&lt;result>Now I have a comprehensive picture. Here is my detailed report.

---

## Detailed Report: "Reward Hacking in Rubric-Based Reinforcement Learning" (arXiv:2605.12474)

**Authors:** Anas Mahmoud, MohammadHossein Rezaei, Zihao Wang, Anisha Gunjal, Bing Liu, Yunzhong He
**Published:** May 12, 2026

---

### 1. Specific Reward Hacking Patterns Identified

The paper identifies three core structural failure modes accounting for approximately 53,447 criterion-level exploitation instances:

**A. Partial Compound (36.0% of cases)**
- **Missing Conjunct (32.9%):** Criteria requiring "A and B" are satisfied when only one element is present. Example: a criterion requiring "both mechanism and efficacy discussed" gets credited when only mechanism is mentioned.
- **Incomplete Enumeration (3.1%):** Criteria requesting N items are satisfied with fewer.

**B. Implicit-as-Explicit (34.6% of cases)**
- **Inferred Content (17.9%):** Treating unstated claims as if explicitly present. Example: the verifier infers scientific consensus from context rather than requiring an explicit statement.
- **Missing Supporting Element (16.6%):** Accepting main claims without required rationale or contrast.

**C. Imprecise Verification (29.4% of cases)**
- **Concept Substitution (8.3%):** Accepting related but distinct concepts as equivalent.
- **Topical Alignment (21.1%):** Checking broad topic relevance rather than precise claims. Example: crediting discussion of "hypertension" when the criterion specifically required "acute hypertension management."

A critical finding is that these patterns remained structurally identical across verifier strengths -- both weak and strong verifiers exhibited the same proportions despite a 7x difference in exploitation volume. The paper states: "training does not shift the kind of exploitation -- it simply produces more of the same."

---

### 2. Domains Studied

The paper focuses on **medical and science domains**:

- **Medical:** 12,519 training / 1,391 test prompts
- **Science:** 19,806 training / 2,201 test prompts

Data sources included RaR-science, ResearchQA, MegaScience, and II-medical-reasoning, paired with RubricHub rubrics. Results were additionally validated on the external **HealthBench** benchmark.

---

### 3. Mitigations Proposed

The paper proposes mitigations at three levels:

**Verifier-Level:**
- Upgrading from the weak verifier (GPT-4o-mini, 76-82% rubric agreement) to a strong verifier (GPT-OSS-120B, 92% agreement) cut exploitation approximately 7-fold.
- However, 15-28% exploitation remained even under the strong verifier, indicating verifier improvement alone is insufficient.

**Rubric-Design Level:**
- **Rebalance presence vs. absence criteria:** The paper found a 10:1 weight ratio favoring presence-based criteria (90.2%) over absence-based criteria (8.6%). Expanding absence-based penalties (for factual incorrectness, verbosity, overconfidence) would counterbalance presence-based gaming.
- **Add specificity requirements:** Include explicit penalties for verbosity, tangentiality, and overconfidence.
- **Online rubric evolution:** Evolve rubrics during training as policies reveal emergent behaviors rather than relying on static offline specifications.

**Monitoring and Early Stopping via the Self-Internalization Gap:**
- A novel verifier-free diagnostic computed solely from policy log-probabilities. It measures the divergence between the policy's prompt-only distribution and its rubric-conditioned distribution.
- Correlates with reference-panel reward at r = 0.91-0.97.
- Under weak verifiers, the self-gap peaks mid-training (aligned with true quality), while the training-verifier reward continues climbing. This provides a practical early-stopping signal.
- Achieves 0.13% maximum stopping regret vs. 0.45-1.81% for training-verifier signals.
- Requires no external judges -- only policy log-probabilities.

---

### 4. Relation to Gating as an Anti-Hacking Mechanism

The paper does **not** explicitly use the term "gating" or propose a gating mechanism. However, the paper's contributions connect to the gating concept in several important ways:

- **The self-internalization gap functions as an implicit gate:** It provides a signal to halt training when the policy stops genuinely improving, effectively gating further optimization. This is analogous to a quality gate that prevents the policy from entering the exploitation regime.

- **The rubric-design critique implies the need for gating structures:** The paper's finding that presence-based criteria dominate (90.2%) while absence-based criteria are underrepresented (8.6%) suggests that rubric rewards should incorporate gating logic -- where satisfaction of presence criteria is gated on also satisfying absence criteria (factual correctness, conciseness). Without such gating, policies game the system by maximizing verbosity and claim density.

- **Separate work on Gated Reward Accumulation (G-RA)** is a related but distinct approach that gates immediate rewards based on high-level outcome thresholds (R_GRA = R^(H) + I[R^(H) &gt;= delta] * sum of r^(L)(t)). This is conceptually aligned with the paper's recommendation for multi-layered reward validation but was not developed in arXiv:2605.12474 itself.

- **Hard veto mechanisms** discussed in the broader reward-hacking defense literature also function as gates -- flagging and blocking exploit patterns like sycophancy or meta-praise before they affect reward accumulation.

---

### 5. Key Findings and Recommendations

**Central Insight:** "Stronger verification alone is insufficient when the rubric leaves important failure modes unspecified." Rubric-based RL faces two **independent** failure modes that require separate solutions.

**Quantitative Highlights:**
- Under the weak verifier, the exploitation rate climbs from 39% to 65% (medical) and 63% to 75% (science) over training.
- Under the strong verifier, exploitation stays at 15-28% with no upward trend.
- Even with the strong verifier, rubric-based judges prefer the RL checkpoint 85.8% of the time, while rubric-free judges prefer the base model 78.4% of the time.
- The checkpoint improves completeness (+1.07) while degrading factual correctness (-0.85), conciseness (-2.91), relevance (-1.10), and overall quality (-1.02).
- Presence-based criteria satisfaction rises from 27.6% to 42.5%, while absence-based satisfaction slightly declines from 51.6% to 49.6%. Critically, incorrect claims rise alongside correct ones.

**Core Recommendations:**
1. Pair stronger verifiers with better rubric design -- neither alone suffices.
2. Rebalance rubric weight toward absence-based (penalizing) criteria.
3. Use the self-internalization gap as a deployment-ready early-stopping diagnostic.
4. Consider online rubric evolution during training.
5. Monitor for the structural exploitation patterns (partial compound, implicit-as-explicit, imprecise verification) as they are stable across verifier strengths and training stages.

**Experimental Details:**
- Base policy: Qwen2.5-7B-Instruct (with 14B and 32B ablations confirming pattern consistency)
- Training: GRPO across 16 GPUs for 5 epochs
- Reference panel: GPT-5.4, Gemini 3 Pro, Claude Opus 4.6 (unanimous consensus required)
- The self-internalization gap pattern reproduced identically at 7B, 14B, and 32B scales

**Limitations acknowledged:** Reference panel is still model-based; single training seed per configuration; limited to medical/science domains.

---

Sources:
- [Reward Hacking in Rubric-Based Reinforcement Learning (Abstract)](https://arxiv.org/abs/2605.12474)
- [Reward Hacking in Rubric-Based Reinforcement Learning (Full HTML)](https://arxiv.org/html/2605.12474)
- [Reward Hacking Defense Rubric - Emergent Mind](https://www.emergentmind.com/topics/reward-hacking-defense-rubric)
- [Gated Reward Accumulation - Emergent Mind](https://www.emergentmind.com/topics/gated-reward-accumulation-g-ra)
- [Reward Hacking in RLVR Systems - Emergent Mind](https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr)&lt;/result>
&lt;usage>&lt;total_tokens>19144&lt;/total_tokens>&lt;tool_uses>10&lt;/tool_uses>&lt;duration_ms>139068&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8f41850-ecdd-4d82-b436-4cf7e708b34f",
  "isSidechain": false,
  "promptId": "7b4a995c-437c-4fd2-84f9-de8b0c894251",
  "type": "user",
  "uuid": "9dcc63fd-25d4-4b04-b528-94963e06b08e",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 52 · 2026-05-28T03:27:41.244Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:27:41.244Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "&lt;task-notification>\n&lt;task-id>a953639c763da791d&lt;/task-id>\n&lt;tool-use-id>toolu_01G3HBvidcjxWLYV1jbqgBqR&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a953639c763da791d.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research DRO paper\" completed&lt;/summary>\n&lt;result>Now I have comprehensive information about the DRO paper. Here is my detailed report.\n\n---\n\n## DRO: Direct Reasoning Optimization (arXiv:2506.13351) -- Detailed Analysis\n\n### Paper Overview\n\n**Title:** Direct Reasoning Optimization: Constrained RL with Token-Level Dense Reward and Rubric-Gated Constraints for Open-ended Tasks\n\n**Authors:** Yifei Xu, Tusher Chakraborty, Srinagesh Sharma, Leonardo Nunes, Swati Sharma, Kate Drakos Demopulos, Emre Kiciman, Songwu Lu, Ranveer Chandra\n\n**Submitted:** June 16, 2025 (v2: May 7, 2026)\n\nDRO frames RL training of LLMs on open-ended (non-verifiable) tasks as **constrained RL**, combining two components: (1) a token-level dense reward called R3 (Reasoning Reflection Reward), and (2) rubric-gating as hard feasibility constraints at the rollout group level.\n\n---\n\n### 1. What Exactly Is \"Rubric-Gating\"? Binary or Continuous?\n\nRubric-gating is **strictly binary** -- it operates as a hard accept/reject mechanism at the rollout group level (not individual samples). There is no continuous scoring. An entire rollout group (all G=16 sampled outputs for a given query) either passes both gates and is used for the policy gradient update, or it is rejected entirely and discarded from the current update.\n\n**How rubrics are generated:** For each query, the LLM (the reference policy itself) proposes a compact set of critical rubrics formulated as **yes/no questions**. The reference answer is then verified to satisfy each rubric -- this prevents ill-posed constraints (i.e., you don't impose constraints that even the \"correct\" answer fails).\n\n**Two sequential gates are applied:**\n\n- **Coverage Gate:** Every rubric must be satisfied by at least **mu** rollouts in the group. This ensures feasibility compliance with tunable strictness. Default: mu=1 (at least one rollout must satisfy each rubric).\n\n- **Consistency Gate:** The top **rho%** of rollouts (ranked by R3 reward) must each satisfy at least **nu%** of the rubrics. This ensures that the rollouts most responsible for driving policy updates are also constrained at a minimum rubric coverage level. Default: rho=25%, nu=60%.\n\nIf a rollout group fails either gate, it is **discarded (not resampled)**. The query remains in the training set for future iterations, but that specific group does not contribute to the gradient update.\n\n---\n\n### 2. What Tasks Does It Apply To? (Text-Only? What Domains?)\n\nDRO is **entirely text-only**. There is no multimodal component whatsoever -- no images, figures, diagrams, or scientific visualizations. The paper evaluates on four datasets:\n\n1. **ParaRev** -- Scientific paragraph revision: improving academic text based on reviewer feedback (long-form, hundreds of tokens)\n2. **RaR-Medicine** -- Medical question-answering / clinical reasoning (long-form)\n3. **ContractNLI** -- Legal contract review requiring document-level natural language inference (structured JSON output)\n4. **FinQA** -- Financial numerical reasoning involving calculations over financial data (short-form, verifiable answers)\n\nThree of these (ParaRev, RaR-Medicine, ContractNLI) are genuinely non-verifiable / open-ended. FinQA is included as a verifiable benchmark to show DRO approaches oracle-verifier performance even on structured tasks.\n\nNotably, rubric-gating was **not applied to FinQA** since its answers are short-form and verifiable -- gating was only used on the open-ended tasks.\n\n---\n\n### 3. How Does the Gating Mechanism Work Technically?\n\nThe technical mechanism operates within the GRPO (Group Relative Policy Optimization) framework:\n\n**Step-by-step process:**\n1. Sample G=16 rollouts per query from the current policy\n2. For each rollout, compute the R3 reward (token-level dense reward based on reasoning quality)\n3. Apply the rubric-gating check on the entire group:\n   - Generate query-specific rubrics (yes/no questions) via the LLM\n   - Verify the reference answer satisfies all rubrics (to prevent ill-posed constraints)\n   - Check each rollout's final answer against each rubric\n   - **Coverage gate:** Does at least mu=1 rollout satisfy every rubric?\n   - **Consistency gate:** Do the top rho=25% of rollouts (by R3 score) each satisfy at least nu=60% of rubrics?\n4. If the group fails either gate, discard it entirely\n5. If accepted, also apply variance-based filtering (discard low-variance groups where R3 scores don't differentiate)\n6. Compute GRPO advantages via group-wise z-scoring of R3 rewards\n7. Execute the clipped policy gradient update with KL regularization\n\n**The key design principle is separation of optimization from feasibility:** R3 handles reward quality ranking within a group, while rubric-gating handles group-level feasibility. They are complementary but operate independently.\n\n**This is NOT Lagrangian or penalty-based constrained RL.** It is hard rejection -- a form of constrained RL where infeasible samples are simply excluded from training.\n\n---\n\n### 4. Key Results\n\n**Main performance (Table 1):**\n\n| Dataset | DRO (Full) | Best Baseline | Metric |\n|---------|-----------|--------------|--------|\n| ParaRev | 63.7% | 55.9% (Rubric only) | Win rate vs base |\n| RaR-Medicine | 57.6% | 56.1% (R3 + Rubric) | Win rate vs base |\n| ContractNLI | 84.5 | 80.6 (R3 only) | Macro-F1 |\n| FinQA | 68.4% | 69.0% (Oracle RL-F1) | Accuracy |\n\n**Key findings:**\n- DRO achieves **2-3x faster** learning than plain probability aggregation approaches\n- On FinQA, DRO **approaches oracle verifier performance** despite not having access to ground-truth verification\n- ROUGE-L F1 baseline completely failed on open-ended tasks (ParaRev: 40.8%, RaR-Medicine: 46.7%)\n- Rubric-gating **consistently improves** R3-only results on ParaRev (+3.8%) and RaR-Medicine (+1.9%)\n- Rejection rates from rubric-gating **decrease over training**, showing the model learns to comply with constraints\n- On ContractNLI, rubric-gating had limited impact because JSON formatting constraints are hard to express as yes/no rubric questions\n- The emphasis parameter omega is sensitive -- values above 4 reduce peak performance and hasten training collapse\n\n**Ablation on rubric-gating:**\n- R3 alone: ParaRev 57.8%, RaR-Medicine 54.2%\n- R3 + Rubric-gating: ParaRev 61.6%, RaR-Medicine 56.1%\n- Full DRO (R3 + Rubric + variance filtering): ParaRev 63.7%, RaR-Medicine 57.6%\n\n---\n\n### 5. How Does DRO Differ from Applying Gated Rewards to Multimodal Scientific Reasoning?\n\nThis is the most important comparative question. Here are the key differences:\n\n**(a) Modality:** DRO is purely text-in, text-out. There is no handling of images, figures, molecular structures, experimental data visualizations, or any non-textual modality. A multimodal scientific reasoning system would need to handle visual inputs (e.g., spectra, plots, microscopy images) alongside text.\n\n**(b) Nature of rubrics:** DRO's rubrics are text-based yes/no questions generated by the LLM itself and verified against text reference answers. In multimodal scientific reasoning, feasibility constraints would need to account for:\n- Correctness of visual interpretation (e.g., did the model correctly read a graph?)\n- Consistency between visual evidence and textual reasoning\n- Domain-specific scientific validity that may require specialized verifiers (not just LLM self-assessment)\n\n**(c) Rubric generation assumes text self-assessment capability:** DRO relies on the LLM itself to both generate rubrics and verify them against reference answers. This self-contained approach works for text because LLMs are competent text evaluators. For multimodal tasks, the model's ability to generate and verify rubrics about visual content is far less reliable.\n\n**(d) Binary gating vs. graded scientific correctness:** DRO's binary accept/reject is appropriate for text tasks where \"core task principles\" are either met or violated. Scientific reasoning often has graded correctness -- a partially correct derivation, an approximately right numerical answer, or a valid but suboptimal experimental interpretation. Binary gating would discard partially valuable training signal.\n\n**(e) Scope of \"non-verifiable\":** DRO targets tasks like paragraph revision and medical QA where there is no single correct answer but there are quality criteria. Scientific reasoning tasks (especially in STEM) often have verifiable ground truths (correct calculations, known molecular properties, established physical laws) mixed with non-verifiable elements (interpretation, hypothesis generation). DRO's framework does not address this hybrid verifiable/non-verifiable structure.\n\n**(f) R3's token-level variance mechanism is text-specific:** R3 identifies \"reasoning-reflective tokens\" through variance of token-level self-certainty across CoT traces. This mechanism is designed for text token sequences and would need fundamental rethinking for multimodal reasoning where critical reasoning steps may involve visual attention patterns rather than text tokens.\n\n**(g) No structured scientific outputs:** DRO struggles even with JSON formatting (ContractNLI showed limited gains). Scientific tasks often require structured outputs (equations, chemical formulas, data tables, citations) that would likely face similar or worse difficulties with rubric-gating.\n\n---\n\n### Summary\n\nDRO's rubric-gating is a **binary, hard-rejection constraint mechanism** that filters out rollout groups whose outputs violate LLM-generated yes/no criteria. It is conceptually clean: separate feasibility (rubric-gating) from optimization (R3 reward). The approach is effective for text-only open-ended tasks (scientific writing revision, medical QA, legal contracts) but has not been tested on or designed for multimodal settings. Extending it to multimodal scientific reasoning would require addressing: (1) how to generate and verify rubrics about visual content, (2) whether binary gating is appropriate for graded scientific correctness, (3) how to handle hybrid verifiable/non-verifiable task structures, and (4) how to adapt the token-level R3 mechanism for non-textual reasoning.\n\nSources:\n- [arXiv:2506.13351 Abstract](https://arxiv.org/abs/2506.13351)\n- [arXiv:2506.13351 Full HTML (v2)](https://arxiv.org/html/2506.13351v2)\n- [EmergentMind Summary](https://www.emergentmind.com/papers/2506.13351)\n- [Joshua Berkowitz Blog Post](https://joshuaberkowitz.us/blog/papers-7/how-direct-reasoning-optimization-teaches-llms-to-grade-their-own-thinking-906)&lt;/result>\n&lt;usage>&lt;total_tokens>20049&lt;/total_tokens>&lt;tool_uses>12&lt;/tool_uses>&lt;duration_ms>153596&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 53 · 2026-05-28T03:27:44.854Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:27:44.854Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "&lt;task-notification>\n&lt;task-id>ac16169121d45159b&lt;/task-id>\n&lt;tool-use-id>toolu_01KxuSdkN91hUkCL1pexV5Ub&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/ac16169121d45159b.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research ARES POW3R rDPO papers\" completed&lt;/summary>\n&lt;result>Now I have comprehensive details on all three papers. Here is my detailed report.\n\n---\n\n## Paper 1: ARES -- Automated Rubric Synthesis for Scalable LLM Reinforcement Learning\n\n**arXiv: 2605.23454 (May 2026)**\n\n**Authors:** Xiaoyuan Li, Keqin Bao, Moxin Li, Yubo Ma, Yichang Zhang, Wenjie Wang, Fuli Feng, Dayiheng Liu (USTC, Alibaba Group, NUS)\n\n### Core Technical Contribution\n\nARES is a fully automated pipeline that converts raw pretraining documents into rubric-annotated RL training data at scale. The key innovation is **co-generating** question-answer pairs alongside question-specific weighted rubrics in a single LLM pass, rather than relying on fixed, task-level rubrics or binary (correct/incorrect) rewards.\n\nThe pipeline has three stages:\n1. **Source Preparation:** Documents are filtered for quality, then classified into 10 domains and assigned one of 3 target personas for diversity.\n2. **QA-Rubric Co-generation:** A single generator produces tuples of (self-contained question, reference answer, weighted rubric). Each rubric consists of (criterion, weight) pairs where positive weights reward desirable properties and negative weights penalize critical omissions.\n3. **Quality Control:** Three validation layers check question self-containment, answer faithfulness, and rubric well-formedness/weight diversity.\n\nThe reward function is: `R = sum(w_k * J_phi(q, y, c_k))` where `J_phi` is a judge evaluating criterion satisfaction. Training uses **GRPO** with 8 rollouts per question, epsilon=0.2 clipping, and beta=0.01 KL penalty.\n\n### Key Findings/Results\n\n- Dataset: 101,847 instances across 10 domains with 1.1M total criteria (avg 10.88 per instance; 817K positive, 291K negative).\n- **HealthBench:** +5.37 over binary-reward RL (41.45 vs 36.08)\n- **IFEval:** +19.27 improvement (54.88 vs 35.61)\n- **GSM8K:** 86.96 (top result)\n- Average across 7 benchmarks: 52.69\n- Rubric-based RL consistently outperforms continual pretraining, SFT, and binary-reward RL, with the largest gains on multi-dimensional open-ended tasks.\n\n### Text-only or Multimodal\n\n**Text-only.** No multimodal component is present.\n\n### Relation to Gated Rubric Rewards for Non-verifiable Multimodal Scientific Reasoning\n\nARES addresses the rubric *generation* bottleneck -- a critical upstream requirement for any rubric-based reward system. Its automated pipeline for synthesizing instance-specific weighted rubrics from raw documents could be adapted to generate rubrics for scientific domains. However, it does not address: (a) dynamic rubric weighting during training, (b) multimodal inputs, or (c) gating mechanisms. It provides the **data infrastructure** layer that a gated rubric reward system would need, but not the reward adaptation or multimodal reasoning components.\n\n---\n\n## Paper 2: POW3R -- Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR\n\n**arXiv: 2605.20164 (May 2026)**\n\n**Authors:** Utkarsh Tyagi, Xingang Guo, MohammadHossein Rezaei, Daniel George, Anas Mahmoud, Jackson Lee, Bing Liu, Yunzhong He\n\n### Core Technical Contribution\n\nPOW3R decouples a criterion's **human-assigned importance** (what should matter in the final answer) from its **current usefulness as an optimization signal** (what can teach the current policy). The key insight is that many important criteria are already saturated (pass rate near 1) or currently unreachable (pass rate near 0), contributing zero gradient signal, while criteria that actually distinguish rollouts may not have the largest human weights.\n\nThe adaptive weighting mechanism:\n1. **Measure rollout contrastiveness:** Compute variance `v_j` of judge verdicts for criterion j across rollouts. Dead (p=0) and saturated (p=1) criteria have v=0.\n2. **Smooth:** `g_j = sqrt(v_j + epsilon)`\n3. **Category-normalize:** Compute mean contrastiveness within each rubric category.\n4. **Blend and clip:** `alpha_j = clip((1-lambda) + lambda * (g_j / g_bar_category), alpha_min, alpha_max)` with alpha_min=0.67, alpha_max=1.5, lambda=0.5.\n5. **EMA update:** Smooth across training steps with beta_ema=0.2.\n6. **Renormalize within categories** so human weight priors and category mass remain intact.\n\nFinal reward: `R_dyn = (1/K) * sum_categories[ (1/W_tilde_k) * sum_criteria_in_k[ w_j * alpha_j * s_j ] ]`\n\n### Key Findings/Results\n\n- Wins **24 of 30** base-policy/metric comparisons across 3 base policies and 2 datasets.\n- Reaches the same performance plateau in **2.5-4x fewer training steps**.\n- Multimodal dataset (10K tasks, 6 rubric categories, complex images): Qwen3-VL-8B achieves 51.6% rubric reward vs 50.4% for static category-balanced weighting.\n- HealthBench (text-only medical QA): +3.7 to +4.7 percentage point gains across models.\n- Improves both mean rubric reward AND strict completion (fraction of prompts where every required criterion is satisfied).\n\n### Text-only or Multimodal\n\n**Both.** Experiments span a multimodal dataset (charts, diagrams, photos evaluated with Qwen3-VL models) and a text-only dataset (HealthBench with Qwen3/Gemma3 text models).\n\n### Relation to Gated Rubric Rewards for Non-verifiable Multimodal Scientific Reasoning\n\nPOW3R is highly relevant. It directly addresses the problem of making rubric rewards more informative for non-verifiable tasks by dynamically adapting criterion weights based on the current policy's capabilities. Its mechanism is **complementary to but distinct from** gating: rather than binary accept/reject of criteria, it continuously rescales their influence. For multimodal scientific reasoning, POW3R's approach could ensure that as a model masters basic visual parsing criteria, training pressure shifts toward deeper scientific reasoning criteria. The category-preservation mechanism is particularly useful for scientific rubrics where different dimensions (factual accuracy, reasoning chain, visual grounding) must maintain balanced representation.\n\n---\n\n## Paper 3: rDPO -- Visual Preference Optimization with Rubric Rewards\n\n**arXiv: 2604.13029 (April 2026)**\n\n**Authors:** Ya-Qi Yu, Fangyu Hong, Xiangyang Qu, Hao Wang, Gaojie Wu, Qiaoyu Luo, Nuo Xu, Huixin Wang, Wuheng Xu, Yongxin Liao, Zihao Chen, Haonan Li, Ziming Li, Dezhi Peng, Minghui Liao, Jihao Wu, Haoyu Ren, Dandan Tu\n\n### Core Technical Contribution\n\nrDPO introduces **instance-specific, checklist-style rubrics** for constructing preference pairs in multimodal DPO. Instead of using coarse outcome-based signals or off-policy perturbations, each image-instruction pair gets a custom rubric with essential and additional criteria, each scored at the criterion level.\n\nKey design principles for rubrics: **Atomic** (single indivisible points), **Comprehensive** (all vital dimensions), **Precise** (aligned with user query), **Objective** (grounded in observable facts).\n\nEach criterion is a triplet: (assertion, reference ground truth, importance weight) where weights are 1=Auxiliary, 2=Important, 3=Key. Two generation strategies handle varying data quality: **Expert-Grounded** (conditioned on trustworthy annotations) and **Answer-Agnostic** (for noisy/missing labels). Multiple frontier models generate rubric candidates independently, then are aggregated to mitigate systematic bias.\n\nTraining pipeline:\n1. **Seed Mining:** Ensemble disagreement filtering identifies challenging instances using 4 VLMs.\n2. **Rubric Drafting:** Instance-specific JSON checklists with essential/additional categorization.\n3. **Preference Data Curation:** Sample 32 on-policy responses per prompt, score via VLM-as-a-Judge with 3 independent runs (median voting), apply 5 strict pairing rules (chosen/rejected qualification, margin constraint, learning capacity, diversity control).\n4. **Iterative DPO** with Mixed Preference Optimization: `L_MPO = L_DPO + alpha * L_SFT`, using 3 sequential data splits.\n\nReward formula: `r_phi(x, y, C^x) = sum_k[ w_k * s_phi(x, y, c_k, a_k) ]` where scores are {0, 0.5, 1} for no/partial/full credit.\n\n### Key Findings/Results\n\n- **Reward Modeling:** Rubric prompting on Qwen3-VL-30B-A3B achieves 74.83 macro average across 5 reward benchmarks, approaching GPT-5.4's 74.91 (vs 71.73 baseline).\n- **Downstream:** Rubric-based filtering achieves **82.69 macro** vs 75.82 for outcome-based filtering (and 81.14 base).\n- **Scaling:** rDPO achieves **61.01** on comprehensive benchmark vs 52.36 baseline, with gains across perception (+7.15), understanding (+8.43), knowledge (+10.25), reasoning (+8.76).\n- Key ablations: Iterative DPO adds +1.74, essential qualification enforcement adds +2.65, diversity control adds +1.67.\n\n### Text-only or Multimodal\n\n**Multimodal.** Specifically designed for vision-language models, evaluated with VLMs on visual reasoning tasks (AI2D, ChartQA, M3CoT, and comprehensive internal benchmarks spanning perception, understanding, knowledge, and reasoning).\n\n### Relation to Gated Rubric Rewards for Non-verifiable Multimodal Scientific Reasoning\n\nrDPO is the most directly relevant of the three papers. It is explicitly multimodal, uses instance-specific rubrics, and targets non-verifiable visual reasoning tasks. Its distinction between **essential** and **additional** criteria functions as a soft gating mechanism -- the five strict pairing rules enforce that chosen responses must satisfy essential criteria (a qualification gate) while rejected responses must fail on essentials. The \"learning capacity\" and \"margin constraint\" pairing rules further ensure preference pairs are pedagogically useful. For scientific reasoning specifically, its evaluation on M3CoT (multimodal multi-step chain-of-thought) demonstrates applicability to scientific reasoning chains, and the knowledge (+10.25) and reasoning (+8.76) gains are particularly promising for scientific domains.\n\n---\n\n## Cross-Paper Synthesis: Relevance to Gated Rubric Rewards for Non-verifiable Multimodal Scientific Reasoning\n\n| Dimension | ARES | POW3R | rDPO |\n|---|---|---|---|\n| Modality | Text-only | Both (text + multimodal) | Multimodal |\n| Rubric source | Auto-generated from documents | Assumes rubrics exist | Auto-generated per instance |\n| Weighting approach | Static co-generated weights | Dynamic policy-aware weights | Static importance weights (1-3) |\n| Gating mechanism | None | Soft (continuous rescaling via contrastiveness) | Soft (essential vs additional qualification rules) |\n| RL paradigm | GRPO | GRPO | DPO (iterative, mixed) |\n| Scientific reasoning | Not targeted | Not targeted specifically | M3CoT evaluation; knowledge/reasoning gains |\n\nA complete system for **gated rubric rewards for non-verifiable multimodal scientific reasoning** would benefit from combining:\n- **ARES's** automated rubric synthesis pipeline (adapted for scientific documents and multimodal inputs)\n- **POW3R's** policy-aware dynamic weighting (to avoid wasting training signal on saturated/unreachable criteria)\n- **rDPO's** multimodal instance-specific rubric design with essential/additional gating and iterative preference optimization\n\nNone of the three papers implements a hard gating mechanism where rubric criteria explicitly unlock or gate subsequent training phases, which would be a novel contribution in this space.\n\nSources:\n- [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/abs/2605.23454)\n- [ARES HTML version](https://arxiv.org/html/2605.23454)\n- [POW3R: Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR](https://arxiv.org/abs/2605.20164v1)\n- [POW3R HTML version](https://arxiv.org/html/2605.20164v1)\n- [rDPO: Visual Preference Optimization with Rubric Rewards](https://arxiv.org/abs/2604.13029v1)\n- [Rubric-Driven DPO for Visual Tasks - StartupHub.ai](https://www.startuphub.ai/ai-news/ai-research/2026/rubric-driven-dpo-for-visual-tasks)&lt;/result>\n&lt;usage>&lt;total_tokens>18028&lt;/total_tokens>&lt;tool_uses>11&lt;/tool_uses>&lt;duration_ms>144850&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "9dcc63fd-25d4-4b04-b528-94963e06b08e",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Assistant

_source line 56 · 2026-05-28T03:27:39.373Z_

<details><summary>Logged reasoning block</summary>

```text
Three agents done now. Still waiting for:
- DRO paper
- ARES, POW3R, rDPO
- Continuous vs binary gating
- MMSci dataset details
- Scientific figure critique benchmarks

Let me wait for the remaining agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dcc63fd-25d4-4b04-b528-94963e06b08e",
  "isSidechain": false,
  "requestId": "req_011CbUFnx5PmA3cU5hBagshb",
  "type": "assistant",
  "uuid": "d9424fcd-f1b3-4397-8375-1393899f3265",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yqphDGQ8rsGEJtXFFVA5t",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2549,
      "cache_read_input_tokens": 33120,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 33120,
          "cache_creation_input_tokens": 2549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2549
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

_source line 57 · 2026-05-28T03:27:46.061Z_

Good, three agents done. Key findings so far:

1. **Training AI Co-Scientists** - Uses rubric RL (GRPO) for scientific research plan generation. Text-only. Uses instance-specific rubrics extracted from papers. Reward = (# satisfied rubric items / total). Demonstrates reward model overoptimization even with rubric rewards.

2. **Perception-R1** - Adds visual perception reward to RLVR. Verifiable. Composite reward with perception as separate weighted component. Shows explicitly rewarding perceptual accuracy improves reasoning.

3. **ClaimDiff-RL** - Claim-level captioning RL with graded severity. Hybrid verifiable/non-verifiable. Closest architecture to our approach - claim decomposition as rubric dimensions, severity weighting as soft gating.

4. **Reward Hacking in Rubric-Based RL** - Studies rubric hacking in medical/science domains. Finds three structural exploitation patterns. Key finding: presence-based criteria dominate (90%), models game by maximizing verbosity. Proposes self-internalization gap as early stopping signal. Directly validates our anti-hacking motivation but also shows gating alone isn't sufficient.

Still waiting for 4 more agents (DRO, ARES/POW3R/rDPO, continuous vs binary gating theory, MMSci details, benchmark construction).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9424fcd-f1b3-4397-8375-1393899f3265",
  "isSidechain": false,
  "requestId": "req_011CbUFnx5PmA3cU5hBagshb",
  "type": "assistant",
  "uuid": "d794c24a-d555-4697-889b-fd6bd5003a1f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yqphDGQ8rsGEJtXFFVA5t",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2549,
      "cache_read_input_tokens": 33120,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 33120,
          "cache_creation_input_tokens": 2549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2549
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

_source line 58 · 2026-05-28T03:27:46.128Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:27:46.128Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 5

4 recorded events

### User

_source line 59 · 2026-05-28T03:27:46.133Z_

&lt;task-notification>
&lt;task-id>a953639c763da791d&lt;/task-id>
&lt;tool-use-id>toolu_01G3HBvidcjxWLYV1jbqgBqR&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a953639c763da791d.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research DRO paper" completed&lt;/summary>
&lt;result>Now I have comprehensive information about the DRO paper. Here is my detailed report.

---

## DRO: Direct Reasoning Optimization (arXiv:2506.13351) -- Detailed Analysis

### Paper Overview

**Title:** Direct Reasoning Optimization: Constrained RL with Token-Level Dense Reward and Rubric-Gated Constraints for Open-ended Tasks

**Authors:** Yifei Xu, Tusher Chakraborty, Srinagesh Sharma, Leonardo Nunes, Swati Sharma, Kate Drakos Demopulos, Emre Kiciman, Songwu Lu, Ranveer Chandra

**Submitted:** June 16, 2025 (v2: May 7, 2026)

DRO frames RL training of LLMs on open-ended (non-verifiable) tasks as **constrained RL**, combining two components: (1) a token-level dense reward called R3 (Reasoning Reflection Reward), and (2) rubric-gating as hard feasibility constraints at the rollout group level.

---

### 1. What Exactly Is "Rubric-Gating"? Binary or Continuous?

Rubric-gating is **strictly binary** -- it operates as a hard accept/reject mechanism at the rollout group level (not individual samples). There is no continuous scoring. An entire rollout group (all G=16 sampled outputs for a given query) either passes both gates and is used for the policy gradient update, or it is rejected entirely and discarded from the current update.

**How rubrics are generated:** For each query, the LLM (the reference policy itself) proposes a compact set of critical rubrics formulated as **yes/no questions**. The reference answer is then verified to satisfy each rubric -- this prevents ill-posed constraints (i.e., you don't impose constraints that even the "correct" answer fails).

**Two sequential gates are applied:**

- **Coverage Gate:** Every rubric must be satisfied by at least **mu** rollouts in the group. This ensures feasibility compliance with tunable strictness. Default: mu=1 (at least one rollout must satisfy each rubric).

- **Consistency Gate:** The top **rho%** of rollouts (ranked by R3 reward) must each satisfy at least **nu%** of the rubrics. This ensures that the rollouts most responsible for driving policy updates are also constrained at a minimum rubric coverage level. Default: rho=25%, nu=60%.

If a rollout group fails either gate, it is **discarded (not resampled)**. The query remains in the training set for future iterations, but that specific group does not contribute to the gradient update.

---

### 2. What Tasks Does It Apply To? (Text-Only? What Domains?)

DRO is **entirely text-only**. There is no multimodal component whatsoever -- no images, figures, diagrams, or scientific visualizations. The paper evaluates on four datasets:

1. **ParaRev** -- Scientific paragraph revision: improving academic text based on reviewer feedback (long-form, hundreds of tokens)
2. **RaR-Medicine** -- Medical question-answering / clinical reasoning (long-form)
3. **ContractNLI** -- Legal contract review requiring document-level natural language inference (structured JSON output)
4. **FinQA** -- Financial numerical reasoning involving calculations over financial data (short-form, verifiable answers)

Three of these (ParaRev, RaR-Medicine, ContractNLI) are genuinely non-verifiable / open-ended. FinQA is included as a verifiable benchmark to show DRO approaches oracle-verifier performance even on structured tasks.

Notably, rubric-gating was **not applied to FinQA** since its answers are short-form and verifiable -- gating was only used on the open-ended tasks.

---

### 3. How Does the Gating Mechanism Work Technically?

The technical mechanism operates within the GRPO (Group Relative Policy Optimization) framework:

**Step-by-step process:**
1. Sample G=16 rollouts per query from the current policy
2. For each rollout, compute the R3 reward (token-level dense reward based on reasoning quality)
3. Apply the rubric-gating check on the entire group:
   - Generate query-specific rubrics (yes/no questions) via the LLM
   - Verify the reference answer satisfies all rubrics (to prevent ill-posed constraints)
   - Check each rollout's final answer against each rubric
   - **Coverage gate:** Does at least mu=1 rollout satisfy every rubric?
   - **Consistency gate:** Do the top rho=25% of rollouts (by R3 score) each satisfy at least nu=60% of rubrics?
4. If the group fails either gate, discard it entirely
5. If accepted, also apply variance-based filtering (discard low-variance groups where R3 scores don't differentiate)
6. Compute GRPO advantages via group-wise z-scoring of R3 rewards
7. Execute the clipped policy gradient update with KL regularization

**The key design principle is separation of optimization from feasibility:** R3 handles reward quality ranking within a group, while rubric-gating handles group-level feasibility. They are complementary but operate independently.

**This is NOT Lagrangian or penalty-based constrained RL.** It is hard rejection -- a form of constrained RL where infeasible samples are simply excluded from training.

---

### 4. Key Results

**Main performance (Table 1):**

| Dataset | DRO (Full) | Best Baseline | Metric |
|---------|-----------|--------------|--------|
| ParaRev | 63.7% | 55.9% (Rubric only) | Win rate vs base |
| RaR-Medicine | 57.6% | 56.1% (R3 + Rubric) | Win rate vs base |
| ContractNLI | 84.5 | 80.6 (R3 only) | Macro-F1 |
| FinQA | 68.4% | 69.0% (Oracle RL-F1) | Accuracy |

**Key findings:**
- DRO achieves **2-3x faster** learning than plain probability aggregation approaches
- On FinQA, DRO **approaches oracle verifier performance** despite not having access to ground-truth verification
- ROUGE-L F1 baseline completely failed on open-ended tasks (ParaRev: 40.8%, RaR-Medicine: 46.7%)
- Rubric-gating **consistently improves** R3-only results on ParaRev (+3.8%) and RaR-Medicine (+1.9%)
- Rejection rates from rubric-gating **decrease over training**, showing the model learns to comply with constraints
- On ContractNLI, rubric-gating had limited impact because JSON formatting constraints are hard to express as yes/no rubric questions
- The emphasis parameter omega is sensitive -- values above 4 reduce peak performance and hasten training collapse

**Ablation on rubric-gating:**
- R3 alone: ParaRev 57.8%, RaR-Medicine 54.2%
- R3 + Rubric-gating: ParaRev 61.6%, RaR-Medicine 56.1%
- Full DRO (R3 + Rubric + variance filtering): ParaRev 63.7%, RaR-Medicine 57.6%

---

### 5. How Does DRO Differ from Applying Gated Rewards to Multimodal Scientific Reasoning?

This is the most important comparative question. Here are the key differences:

**(a) Modality:** DRO is purely text-in, text-out. There is no handling of images, figures, molecular structures, experimental data visualizations, or any non-textual modality. A multimodal scientific reasoning system would need to handle visual inputs (e.g., spectra, plots, microscopy images) alongside text.

**(b) Nature of rubrics:** DRO's rubrics are text-based yes/no questions generated by the LLM itself and verified against text reference answers. In multimodal scientific reasoning, feasibility constraints would need to account for:
- Correctness of visual interpretation (e.g., did the model correctly read a graph?)
- Consistency between visual evidence and textual reasoning
- Domain-specific scientific validity that may require specialized verifiers (not just LLM self-assessment)

**(c) Rubric generation assumes text self-assessment capability:** DRO relies on the LLM itself to both generate rubrics and verify them against reference answers. This self-contained approach works for text because LLMs are competent text evaluators. For multimodal tasks, the model's ability to generate and verify rubrics about visual content is far less reliable.

**(d) Binary gating vs. graded scientific correctness:** DRO's binary accept/reject is appropriate for text tasks where "core task principles" are either met or violated. Scientific reasoning often has graded correctness -- a partially correct derivation, an approximately right numerical answer, or a valid but suboptimal experimental interpretation. Binary gating would discard partially valuable training signal.

**(e) Scope of "non-verifiable":** DRO targets tasks like paragraph revision and medical QA where there is no single correct answer but there are quality criteria. Scientific reasoning tasks (especially in STEM) often have verifiable ground truths (correct calculations, known molecular properties, established physical laws) mixed with non-verifiable elements (interpretation, hypothesis generation). DRO's framework does not address this hybrid verifiable/non-verifiable structure.

**(f) R3's token-level variance mechanism is text-specific:** R3 identifies "reasoning-reflective tokens" through variance of token-level self-certainty across CoT traces. This mechanism is designed for text token sequences and would need fundamental rethinking for multimodal reasoning where critical reasoning steps may involve visual attention patterns rather than text tokens.

**(g) No structured scientific outputs:** DRO struggles even with JSON formatting (ContractNLI showed limited gains). Scientific tasks often require structured outputs (equations, chemical formulas, data tables, citations) that would likely face similar or worse difficulties with rubric-gating.

---

### Summary

DRO's rubric-gating is a **binary, hard-rejection constraint mechanism** that filters out rollout groups whose outputs violate LLM-generated yes/no criteria. It is conceptually clean: separate feasibility (rubric-gating) from optimization (R3 reward). The approach is effective for text-only open-ended tasks (scientific writing revision, medical QA, legal contracts) but has not been tested on or designed for multimodal settings. Extending it to multimodal scientific reasoning would require addressing: (1) how to generate and verify rubrics about visual content, (2) whether binary gating is appropriate for graded scientific correctness, (3) how to handle hybrid verifiable/non-verifiable task structures, and (4) how to adapt the token-level R3 mechanism for non-textual reasoning.

Sources:
- [arXiv:2506.13351 Abstract](https://arxiv.org/abs/2506.13351)
- [arXiv:2506.13351 Full HTML (v2)](https://arxiv.org/html/2506.13351v2)
- [EmergentMind Summary](https://www.emergentmind.com/papers/2506.13351)
- [Joshua Berkowitz Blog Post](https://joshuaberkowitz.us/blog/papers-7/how-direct-reasoning-optimization-teaches-llms-to-grade-their-own-thinking-906)&lt;/result>
&lt;usage>&lt;total_tokens>20049&lt;/total_tokens>&lt;tool_uses>12&lt;/tool_uses>&lt;duration_ms>153596&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d794c24a-d555-4697-889b-fd6bd5003a1f",
  "isSidechain": false,
  "promptId": "8366cdfe-8c46-43eb-84c1-36de10b75297",
  "type": "user",
  "uuid": "70ed194b-93c1-477d-b762-570959686104",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-28T03:27:51.287Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have results for:
1. Training AI Co-Scientists ✅
2. Perception-R1 and ClaimDiff-RL ✅
3. Reward Hacking in Rubric-Based RL ✅
4. DRO ✅

Still waiting for:
- ARES, POW3R, rDPO
- Continuous vs binary gating theory
- MMSci dataset details
- Scientific figure critique benchmarks

The DRO paper is critical - it uses binary rubric-gating for non-verifiable tasks. This is a key competitor. The key difference: DRO uses binary gating (yes/no rubric questions) while our approach uses continuous gating. Also DRO is text-only.


Waiting on the remaining papers to come through.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70ed194b-93c1-477d-b762-570959686104",
  "isSidechain": false,
  "requestId": "req_011CbUFogzKHrULLJEE16nea",
  "type": "assistant",
  "uuid": "12f09ee8-0ed5-40b2-b893-27b88be1a770",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dz7cgVpvjGxXNB8SXzG8fB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3358,
      "cache_read_input_tokens": 35669,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 35669,
          "cache_creation_input_tokens": 3358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3358
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

_source line 61 · 2026-05-28T03:27:53.078Z_

Excellent, the DRO research is back - this is the most critical competitive paper. Key finding: DRO uses **binary** rubric-gating as hard accept/reject constraints for non-verifiable tasks, but is text-only. This directly overlaps our "gating for non-verifiable" concept, making the continuous vs. binary distinction even more important for novelty. Still waiting for 4 more agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12f09ee8-0ed5-40b2-b893-27b88be1a770",
  "isSidechain": false,
  "requestId": "req_011CbUFogzKHrULLJEE16nea",
  "type": "assistant",
  "uuid": "fc0f4c54-a0c4-4bba-9d45-86d156588f9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dz7cgVpvjGxXNB8SXzG8fB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3358,
      "cache_read_input_tokens": 35669,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 297,
          "cache_read_input_tokens": 35669,
          "cache_creation_input_tokens": 3358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3358
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

_source line 62 · 2026-05-28T03:27:53.149Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:27:53.149Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 6

7 recorded events

### User

_source line 63 · 2026-05-28T03:27:53.159Z_

&lt;task-notification>
&lt;task-id>ac16169121d45159b&lt;/task-id>
&lt;tool-use-id>toolu_01KxuSdkN91hUkCL1pexV5Ub&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/ac16169121d45159b.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research ARES POW3R rDPO papers" completed&lt;/summary>
&lt;result>Now I have comprehensive details on all three papers. Here is my detailed report.

---

## Paper 1: ARES -- Automated Rubric Synthesis for Scalable LLM Reinforcement Learning

**arXiv: 2605.23454 (May 2026)**

**Authors:** Xiaoyuan Li, Keqin Bao, Moxin Li, Yubo Ma, Yichang Zhang, Wenjie Wang, Fuli Feng, Dayiheng Liu (USTC, Alibaba Group, NUS)

### Core Technical Contribution

ARES is a fully automated pipeline that converts raw pretraining documents into rubric-annotated RL training data at scale. The key innovation is **co-generating** question-answer pairs alongside question-specific weighted rubrics in a single LLM pass, rather than relying on fixed, task-level rubrics or binary (correct/incorrect) rewards.

The pipeline has three stages:
1. **Source Preparation:** Documents are filtered for quality, then classified into 10 domains and assigned one of 3 target personas for diversity.
2. **QA-Rubric Co-generation:** A single generator produces tuples of (self-contained question, reference answer, weighted rubric). Each rubric consists of (criterion, weight) pairs where positive weights reward desirable properties and negative weights penalize critical omissions.
3. **Quality Control:** Three validation layers check question self-containment, answer faithfulness, and rubric well-formedness/weight diversity.

The reward function is: `R = sum(w_k * J_phi(q, y, c_k))` where `J_phi` is a judge evaluating criterion satisfaction. Training uses **GRPO** with 8 rollouts per question, epsilon=0.2 clipping, and beta=0.01 KL penalty.

### Key Findings/Results

- Dataset: 101,847 instances across 10 domains with 1.1M total criteria (avg 10.88 per instance; 817K positive, 291K negative).
- **HealthBench:** +5.37 over binary-reward RL (41.45 vs 36.08)
- **IFEval:** +19.27 improvement (54.88 vs 35.61)
- **GSM8K:** 86.96 (top result)
- Average across 7 benchmarks: 52.69
- Rubric-based RL consistently outperforms continual pretraining, SFT, and binary-reward RL, with the largest gains on multi-dimensional open-ended tasks.

### Text-only or Multimodal

**Text-only.** No multimodal component is present.

### Relation to Gated Rubric Rewards for Non-verifiable Multimodal Scientific Reasoning

ARES addresses the rubric *generation* bottleneck -- a critical upstream requirement for any rubric-based reward system. Its automated pipeline for synthesizing instance-specific weighted rubrics from raw documents could be adapted to generate rubrics for scientific domains. However, it does not address: (a) dynamic rubric weighting during training, (b) multimodal inputs, or (c) gating mechanisms. It provides the **data infrastructure** layer that a gated rubric reward system would need, but not the reward adaptation or multimodal reasoning components.

---

## Paper 2: POW3R -- Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR

**arXiv: 2605.20164 (May 2026)**

**Authors:** Utkarsh Tyagi, Xingang Guo, MohammadHossein Rezaei, Daniel George, Anas Mahmoud, Jackson Lee, Bing Liu, Yunzhong He

### Core Technical Contribution

POW3R decouples a criterion's **human-assigned importance** (what should matter in the final answer) from its **current usefulness as an optimization signal** (what can teach the current policy). The key insight is that many important criteria are already saturated (pass rate near 1) or currently unreachable (pass rate near 0), contributing zero gradient signal, while criteria that actually distinguish rollouts may not have the largest human weights.

The adaptive weighting mechanism:
1. **Measure rollout contrastiveness:** Compute variance `v_j` of judge verdicts for criterion j across rollouts. Dead (p=0) and saturated (p=1) criteria have v=0.
2. **Smooth:** `g_j = sqrt(v_j + epsilon)`
3. **Category-normalize:** Compute mean contrastiveness within each rubric category.
4. **Blend and clip:** `alpha_j = clip((1-lambda) + lambda * (g_j / g_bar_category), alpha_min, alpha_max)` with alpha_min=0.67, alpha_max=1.5, lambda=0.5.
5. **EMA update:** Smooth across training steps with beta_ema=0.2.
6. **Renormalize within categories** so human weight priors and category mass remain intact.

Final reward: `R_dyn = (1/K) * sum_categories[ (1/W_tilde_k) * sum_criteria_in_k[ w_j * alpha_j * s_j ] ]`

### Key Findings/Results

- Wins **24 of 30** base-policy/metric comparisons across 3 base policies and 2 datasets.
- Reaches the same performance plateau in **2.5-4x fewer training steps**.
- Multimodal dataset (10K tasks, 6 rubric categories, complex images): Qwen3-VL-8B achieves 51.6% rubric reward vs 50.4% for static category-balanced weighting.
- HealthBench (text-only medical QA): +3.7 to +4.7 percentage point gains across models.
- Improves both mean rubric reward AND strict completion (fraction of prompts where every required criterion is satisfied).

### Text-only or Multimodal

**Both.** Experiments span a multimodal dataset (charts, diagrams, photos evaluated with Qwen3-VL models) and a text-only dataset (HealthBench with Qwen3/Gemma3 text models).

### Relation to Gated Rubric Rewards for Non-verifiable Multimodal Scientific Reasoning

POW3R is highly relevant. It directly addresses the problem of making rubric rewards more informative for non-verifiable tasks by dynamically adapting criterion weights based on the current policy's capabilities. Its mechanism is **complementary to but distinct from** gating: rather than binary accept/reject of criteria, it continuously rescales their influence. For multimodal scientific reasoning, POW3R's approach could ensure that as a model masters basic visual parsing criteria, training pressure shifts toward deeper scientific reasoning criteria. The category-preservation mechanism is particularly useful for scientific rubrics where different dimensions (factual accuracy, reasoning chain, visual grounding) must maintain balanced representation.

---

## Paper 3: rDPO -- Visual Preference Optimization with Rubric Rewards

**arXiv: 2604.13029 (April 2026)**

**Authors:** Ya-Qi Yu, Fangyu Hong, Xiangyang Qu, Hao Wang, Gaojie Wu, Qiaoyu Luo, Nuo Xu, Huixin Wang, Wuheng Xu, Yongxin Liao, Zihao Chen, Haonan Li, Ziming Li, Dezhi Peng, Minghui Liao, Jihao Wu, Haoyu Ren, Dandan Tu

### Core Technical Contribution

rDPO introduces **instance-specific, checklist-style rubrics** for constructing preference pairs in multimodal DPO. Instead of using coarse outcome-based signals or off-policy perturbations, each image-instruction pair gets a custom rubric with essential and additional criteria, each scored at the criterion level.

Key design principles for rubrics: **Atomic** (single indivisible points), **Comprehensive** (all vital dimensions), **Precise** (aligned with user query), **Objective** (grounded in observable facts).

Each criterion is a triplet: (assertion, reference ground truth, importance weight) where weights are 1=Auxiliary, 2=Important, 3=Key. Two generation strategies handle varying data quality: **Expert-Grounded** (conditioned on trustworthy annotations) and **Answer-Agnostic** (for noisy/missing labels). Multiple frontier models generate rubric candidates independently, then are aggregated to mitigate systematic bias.

Training pipeline:
1. **Seed Mining:** Ensemble disagreement filtering identifies challenging instances using 4 VLMs.
2. **Rubric Drafting:** Instance-specific JSON checklists with essential/additional categorization.
3. **Preference Data Curation:** Sample 32 on-policy responses per prompt, score via VLM-as-a-Judge with 3 independent runs (median voting), apply 5 strict pairing rules (chosen/rejected qualification, margin constraint, learning capacity, diversity control).
4. **Iterative DPO** with Mixed Preference Optimization: `L_MPO = L_DPO + alpha * L_SFT`, using 3 sequential data splits.

Reward formula: `r_phi(x, y, C^x) = sum_k[ w_k * s_phi(x, y, c_k, a_k) ]` where scores are {0, 0.5, 1} for no/partial/full credit.

### Key Findings/Results

- **Reward Modeling:** Rubric prompting on Qwen3-VL-30B-A3B achieves 74.83 macro average across 5 reward benchmarks, approaching GPT-5.4's 74.91 (vs 71.73 baseline).
- **Downstream:** Rubric-based filtering achieves **82.69 macro** vs 75.82 for outcome-based filtering (and 81.14 base).
- **Scaling:** rDPO achieves **61.01** on comprehensive benchmark vs 52.36 baseline, with gains across perception (+7.15), understanding (+8.43), knowledge (+10.25), reasoning (+8.76).
- Key ablations: Iterative DPO adds +1.74, essential qualification enforcement adds +2.65, diversity control adds +1.67.

### Text-only or Multimodal

**Multimodal.** Specifically designed for vision-language models, evaluated with VLMs on visual reasoning tasks (AI2D, ChartQA, M3CoT, and comprehensive internal benchmarks spanning perception, understanding, knowledge, and reasoning).

### Relation to Gated Rubric Rewards for Non-verifiable Multimodal Scientific Reasoning

rDPO is the most directly relevant of the three papers. It is explicitly multimodal, uses instance-specific rubrics, and targets non-verifiable visual reasoning tasks. Its distinction between **essential** and **additional** criteria functions as a soft gating mechanism -- the five strict pairing rules enforce that chosen responses must satisfy essential criteria (a qualification gate) while rejected responses must fail on essentials. The "learning capacity" and "margin constraint" pairing rules further ensure preference pairs are pedagogically useful. For scientific reasoning specifically, its evaluation on M3CoT (multimodal multi-step chain-of-thought) demonstrates applicability to scientific reasoning chains, and the knowledge (+10.25) and reasoning (+8.76) gains are particularly promising for scientific domains.

---

## Cross-Paper Synthesis: Relevance to Gated Rubric Rewards for Non-verifiable Multimodal Scientific Reasoning

| Dimension | ARES | POW3R | rDPO |
|---|---|---|---|
| Modality | Text-only | Both (text + multimodal) | Multimodal |
| Rubric source | Auto-generated from documents | Assumes rubrics exist | Auto-generated per instance |
| Weighting approach | Static co-generated weights | Dynamic policy-aware weights | Static importance weights (1-3) |
| Gating mechanism | None | Soft (continuous rescaling via contrastiveness) | Soft (essential vs additional qualification rules) |
| RL paradigm | GRPO | GRPO | DPO (iterative, mixed) |
| Scientific reasoning | Not targeted | Not targeted specifically | M3CoT evaluation; knowledge/reasoning gains |

A complete system for **gated rubric rewards for non-verifiable multimodal scientific reasoning** would benefit from combining:
- **ARES's** automated rubric synthesis pipeline (adapted for scientific documents and multimodal inputs)
- **POW3R's** policy-aware dynamic weighting (to avoid wasting training signal on saturated/unreachable criteria)
- **rDPO's** multimodal instance-specific rubric design with essential/additional gating and iterative preference optimization

None of the three papers implements a hard gating mechanism where rubric criteria explicitly unlock or gate subsequent training phases, which would be a novel contribution in this space.

Sources:
- [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/abs/2605.23454)
- [ARES HTML version](https://arxiv.org/html/2605.23454)
- [POW3R: Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR](https://arxiv.org/abs/2605.20164v1)
- [POW3R HTML version](https://arxiv.org/html/2605.20164v1)
- [rDPO: Visual Preference Optimization with Rubric Rewards](https://arxiv.org/abs/2604.13029v1)
- [Rubric-Driven DPO for Visual Tasks - StartupHub.ai](https://www.startuphub.ai/ai-news/ai-research/2026/rubric-driven-dpo-for-visual-tasks)&lt;/result>
&lt;usage>&lt;total_tokens>18028&lt;/total_tokens>&lt;tool_uses>11&lt;/tool_uses>&lt;duration_ms>144850&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc0f4c54-a0c4-4bba-9d45-86d156588f9a",
  "isSidechain": false,
  "promptId": "b8742a54-d1a0-47de-8dfc-5d054361c2e6",
  "type": "user",
  "uuid": "fe091199-6e5c-4633-84d7-5110179b33ad",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "fe091199-6e5c-4633-84d7-5110179b33ad",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 66 · 2026-05-28T03:28:01.015Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:28:01.015Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "&lt;task-notification>\n&lt;task-id>a7b3acafb2ea61a87&lt;/task-id>\n&lt;tool-use-id>toolu_01MKGJhd5ftE67GrHBa4QeGH&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a7b3acafb2ea61a87.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research continuous vs binary gating\" completed&lt;/summary>\n&lt;result>I now have a comprehensive picture. Here is my synthesis of the findings.\n\n---\n\n## Theoretical and Empirical Evidence: Continuous vs Binary Reward Gating in RL\n\nBelow is a structured summary of the evidence that continuous (soft) gating creates qualitatively different -- and generally superior -- training dynamics compared to binary (hard) gating. The evidence spans formal theoretical analysis, recent empirical results on LLM training, and foundational RL theory.\n\n---\n\n### 1. Binary Rewards Create Fundamental Gradient Pathologies\n\n**Gradient Vanishing and Explosion (ReDit, arXiv 2506.18631):**\nBinary rewards cause two distinct gradient pathologies. During early training, the policy rarely produces correct outputs, so most mini-batches contain only zero rewards, and gradients remain minimal (\"gradient vanishing\"). Conversely, when small policy changes cause a sequence to flip from incorrect (reward 0) to correct (reward 1), the resulting advantage estimates become disproportionately large, triggering sudden destabilizing gradient spikes (\"gradient explosion\"). ReDit addresses this by injecting calibrated zero-mean noise into discrete rewards, effectively making them continuous. This achieves GRPO-equivalent performance in approximately 10% of the training steps.\n\n**Gradient Starvation (arXiv 2605.07689):**\nIn binary-reward GRPO, when every response in a group is either all-correct or all-incorrect, the group-mean-centered advantage becomes exactly zero -- the policy receives no learning signal at all. This \"gradient starvation\" was measured at a 0.69 degeneracy rate at group size 4. A simple fix (replacing group-mean centering with a fixed-reference continuous advantage A=2r-1) yielded a 45.4-point accuracy gain (73.8% vs 28.4%).\n\n**Vanishing Gradients in Reinforcement Finetuning (arXiv 2310.20703, ICLR 2024):**\nRazin et al. formally prove that the expected gradient vanishes when the reward standard deviation under the current policy is small -- even if expected reward is far from optimal. Binary rewards exacerbate this because their standard deviation is inherently bounded and frequently near-zero for hard problems. This establishes a formal theoretical basis for why continuous reward signals provide stronger gradient signals.\n\n**Binary Rewards as a Fundamental Degeneracy (arXiv 2605.02375):**\nThis paper argues that binary rewards create a fundamental degeneracy for policy gradient methods: the set of distributions maximizing expected binary reward is infinite with no distinguished element, leading to diversity collapse where single-sample accuracy improves but multi-sample coverage degrades.\n\n---\n\n### 2. Smooth (Soft) Gate Functions Outperform Hard Clipping/Gating\n\n**Smooth Gate Functions for Policy Optimization (arXiv 2602.19345):**\nThis paper directly formalizes the question of smooth vs hard gating in policy optimization. GRPO's hard clipping creates discontinuous gradients. The authors formalize key properties that admissible gate functions should satisfy, then evaluate families of smooth alternatives (sigmoid-based, polynomial decay, Gaussian attenuation). They find that smooth gate functions produce more stable training dynamics. The paper provides a formal framework for reasoning about gate function design.\n\n**Soft Adaptive Policy Optimization / SAPO (arXiv 2511.20347):**\nSAPO replaces PPO's hard clip with a temperature-controlled sigmoid gate. The key insight: hard clipping forces a binary choice (gradient passes or is zeroed), making it difficult to balance between overly tight clipping (too few valid gradient samples) and too loose clipping (noisy off-policy gradients). Sigmoid-based soft clipping achieves 10-60x higher performance values than standard PPO by enabling continuous gradient modulation.\n\n---\n\n### 3. Multiplicative (Continuous) Shaping Generalizes Binary Gating\n\n**GR3: Group Relative Reward Rescaling (arXiv 2603.10535):**\nThis is perhaps the most directly relevant paper. GR3 reframes reward control as a multiplicative rescaling paradigm, establishing what the authors explicitly call a \"generalized, continuous, and reward-dependent gating mechanism.\" Key findings:\n- In the strict binary reward setting, multiplicative shaping is mathematically equivalent to heuristic gating.\n- In continuous reward settings, multiplicative shaping provides a principled \"soft\" gating mechanism where hard binary indicators fail.\n- Gated additive variants (with hard thresholds) underperform and produce optimization instability from the discontinuities introduced by hard gating.\n- GR3's continuous multiplicative approach maintains task reward parity with standard GRPO while achieving controlled length reduction across both RLHF and RLVR settings.\n\nThis directly supports your argument: continuous gating is a strict generalization of binary gating, they are equivalent in the binary case, but continuous gating is qualitatively superior when rewards are non-binary.\n\n---\n\n### 4. Gradient Flow Theory for Multiplicative Gating\n\n**Theory of Gating in Recurrent Neural Networks (Phys. Rev. X, arXiv 2007.14823):**\nThis physics-oriented paper provides formal analysis of how multiplicative gating controls gradient flow. Gating offers flexible control of two features: timescales and dimensionality. Continuous gates enable a \"marginally stable\" regime where the network functions as a flexible integrator. However, the Hadamard product (element-wise multiplication underlying gating) can contribute to gradient instability when multiplicands involve sigmoidal activations -- gradients may vanish or explode depending on input scale. This provides both the theoretical justification for continuous gating (flexible timescale control) and a warning about proper calibration.\n\n---\n\n### 5. Optimization Landscape and Lipschitz Continuity Arguments\n\n**Lipschitz Continuity and Convergence (arXiv 2404.13316, arXiv 1804.07193):**\nFoundational RL theory establishes that Lipschitz continuity of the reward and value functions is a key property for convergence guarantees. A continuous gating function preserves Lipschitz continuity of the composite reward, while binary gating introduces discontinuities that break this property. Stronger Lipschitz conditions on the value function yield tighter convergence bounds and smaller gaps between approximate and optimal solutions.\n\n**Potential-Based Reward Shaping (Ng, Harada, Russell, ICML 1999):**\nThe foundational PBRS framework proves that reward transformations of the form F(s,s') = gamma * Phi(s') - Phi(s) preserve optimal policies. This framework inherently assumes continuous potential functions. Recent extensions note theoretical limitations when potential functions are discontinuous, further supporting the argument that smooth/continuous reward transformations have stronger theoretical properties.\n\n---\n\n### 6. Curriculum Learning: Smooth vs Discontinuous Transitions\n\nResearch on curriculum learning consistently shows that smooth transitions between difficulty levels outperform abrupt shifts. Episode-based Dynamic Reward Shaping mechanisms combined with curriculum learning balance exploration and convergence by gradually reducing shaping strength. Abrupt difficulty transitions can cause \"extinction effects\" that reset learning progress. This is analogous to the continuous vs binary gating question: continuous gating provides smooth curriculum-like transitions in reward emphasis, while binary gating creates discontinuous jumps.\n\n---\n\n### 7. Multimodal RL with Continuous Gating\n\n**PEPO (arXiv 2603.22847):**\nDirectly relevant to your multimodal setting. PEPO uses a smooth gating mechanism to combine perception priors (hidden-state similarity to visual tokens) with exploration priors (token entropy) for token-level advantage estimation. The gating is explicitly continuous -- perception remains dominant while entropy acts as a continuous modulator. This integrates seamlessly with GRPO/DAPO and shows consistent improvements across multimodal benchmarks.\n\n**HARMO (arXiv 2510.05283):**\nProposes hybrid rewards integrating verifiable (rule-based) and non-verifiable (model-based) signals for multimodal LLM alignment, with continuous weighting between reward aspects. Achieves ~9.5% average improvement across benchmarks.\n\n---\n\n### Summary of Key Arguments for Your Reviewer Response\n\n1. **Gradient pathology elimination**: Binary gating creates provable gradient vanishing (when reward std is small) and gradient starvation (when all group members agree). Continuous gating eliminates both pathologies by ensuring non-zero gradient signals throughout training. This is formalized in arXiv 2310.20703 (ICLR 2024) and demonstrated empirically in arXiv 2605.07689.\n\n2. **Strict mathematical generalization**: GR3 (arXiv 2603.10535) proves that multiplicative continuous gating reduces exactly to binary gating in the binary reward case, but provides a principled extension for continuous rewards. Binary gating is a special case of continuous gating, not an equivalent alternative.\n\n3. **Optimization landscape smoothness**: Continuous gating preserves Lipschitz continuity of the reward landscape, maintaining convergence guarantees that binary gating breaks. Hard gating introduces optimization discontinuities empirically shown to cause instability (GR3's comparison of gated additive vs multiplicative approaches).\n\n4. **Quantitative evidence**: ReDit shows 10x training speedup from making binary rewards continuous; SAPO shows 10-60x performance improvement from smooth vs hard clipping; gradient starvation fix shows 45-point accuracy gain.\n\n5. **The qualitative difference is precisely the difference between continuous and discontinuous optimization**: this is not merely a quantitative improvement but a structural change in the loss landscape that eliminates degenerate gradient regions.\n\n---\n\nSources:\n- [ReDit: Reward Dithering for Improved LLM Policy Optimization](https://arxiv.org/html/2506.18631v1)\n- [Binary Rewards and Reinforcement Learning: Fundamental Challenges](https://arxiv.org/abs/2605.02375v1)\n- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689)\n- [Vanishing Gradients in Reinforcement Finetuning of Language Models](https://arxiv.org/abs/2310.20703)\n- [Smooth Gate Functions for Soft Advantage Policy Optimization](https://arxiv.org/abs/2602.19345)\n- [Soft Adaptive Policy Optimization (SAPO)](https://arxiv.org/abs/2511.20347)\n- [GR3: Group Relative Reward Rescaling](https://arxiv.org/abs/2603.10535)\n- [On the Optimization Dynamics of RLVR: Gradient Gap and Step Size Thresholds](https://arxiv.org/abs/2510.08539)\n- [Theory of Gating in Recurrent Neural Networks](https://arxiv.org/abs/2007.14823)\n- [Lipschitz Continuity in Model-based Reinforcement Learning](https://arxiv.org/pdf/1804.07193)\n- [On the Stability of Lipschitz Continuous Control Problems](https://arxiv.org/abs/2404.13316)\n- [Policy Invariance Under Reward Transformations (Ng, Harada, Russell)](https://www.semanticscholar.org/paper/94066dc12fe31e96af7557838159bde598cb4f10)\n- [PEPO: Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought](https://arxiv.org/abs/2603.22847)\n- [HARMO: Beyond Monolithic Rewards](https://arxiv.org/abs/2510.05283)\n- [RLNVR: Reinforcement Learning from Non-Verified Real-World Rewards](https://arxiv.org/pdf/2508.12165)\n- [Variance Aware Reward Smoothing](https://www.sciencedirect.com/science/article/abs/pii/S0925231221009139)&lt;/result>\n&lt;usage>&lt;total_tokens>28698&lt;/total_tokens>&lt;tool_uses>25&lt;/tool_uses>&lt;duration_ms>151058&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Assistant

_source line 67 · 2026-05-28T03:28:00.718Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have results for:
1. Training AI Co-Scientists ✅
2. Perception-R1 and ClaimDiff-RL ✅
3. Reward Hacking in Rubric-Based RL ✅
4. DRO ✅
5. ARES, POW3R, rDPO ✅

Still waiting for:
- Continuous vs binary gating theory
- MMSci dataset details
- Scientific figure critique benchmarks

Key new findings from ARES/POW3R/rDPO:
- **ARES**: Automated rubric synthesis from documents. Text-only. Static weights. No gating.


- **POW3R**: Introduces dynamic rubric weighting that adapts based on policy, handles both text and multimodal inputs, and demonstrates that static weighting approaches are suboptimal—this is a strong ablation baseline to include.
- **rDPO**: Uses instance-specific rubrics with soft gating through essential versus additional criteria for multimodal DPO, making it a key competitor to compare against.

Waiting on the last three pieces before moving forward.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe091199-6e5c-4633-84d7-5110179b33ad",
  "isSidechain": false,
  "requestId": "req_011CbUFpD45Kyvxq7XN2WRUN",
  "type": "assistant",
  "uuid": "0e9d1803-40a6-4b83-baad-452faf668eb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNyVzyzX73paFqi5RxCATu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3839,
      "cache_read_input_tokens": 39027,
      "output_tokens": 449,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 449,
          "cache_read_input_tokens": 39027,
          "cache_creation_input_tokens": 3839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3839
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

_source line 68 · 2026-05-28T03:28:02.268Z_

Excellent, now 5 agents done. Key new insights:

- **ARES**: Automated rubric synthesis pipeline from documents at scale (101K instances). Text-only. Could adapt for scientific document rubric generation.
- **POW3R**: Policy-aware dynamic rubric weighting - shows static weights are suboptimal because criteria can be saturated or unreachable. Both text AND multimodal. Must engage with this - adding a POW3R-style variant to ablations.
- **rDPO**: Multimodal DPO with instance-specific rubrics. Essential vs. additional criteria = soft gating. Closest multimodal rubric competitor.

Still waiting for 3 agents: continuous vs binary gating theory, MMSci details, benchmark construction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e9d1803-40a6-4b83-baad-452faf668eb7",
  "isSidechain": false,
  "requestId": "req_011CbUFpD45Kyvxq7XN2WRUN",
  "type": "assistant",
  "uuid": "fe4b5aba-b782-4743-802a-b9fcee25b7c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNyVzyzX73paFqi5RxCATu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3839,
      "cache_read_input_tokens": 39027,
      "output_tokens": 449,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 449,
          "cache_read_input_tokens": 39027,
          "cache_creation_input_tokens": 3839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3839
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

_source line 69 · 2026-05-28T03:28:02.359Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:28:02.359Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 7

7 recorded events

### User

_source line 70 · 2026-05-28T03:28:02.373Z_

&lt;task-notification>
&lt;task-id>a7b3acafb2ea61a87&lt;/task-id>
&lt;tool-use-id>toolu_01MKGJhd5ftE67GrHBa4QeGH&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a7b3acafb2ea61a87.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research continuous vs binary gating" completed&lt;/summary>
&lt;result>I now have a comprehensive picture. Here is my synthesis of the findings.

---

## Theoretical and Empirical Evidence: Continuous vs Binary Reward Gating in RL

Below is a structured summary of the evidence that continuous (soft) gating creates qualitatively different -- and generally superior -- training dynamics compared to binary (hard) gating. The evidence spans formal theoretical analysis, recent empirical results on LLM training, and foundational RL theory.

---

### 1. Binary Rewards Create Fundamental Gradient Pathologies

**Gradient Vanishing and Explosion (ReDit, arXiv 2506.18631):**
Binary rewards cause two distinct gradient pathologies. During early training, the policy rarely produces correct outputs, so most mini-batches contain only zero rewards, and gradients remain minimal ("gradient vanishing"). Conversely, when small policy changes cause a sequence to flip from incorrect (reward 0) to correct (reward 1), the resulting advantage estimates become disproportionately large, triggering sudden destabilizing gradient spikes ("gradient explosion"). ReDit addresses this by injecting calibrated zero-mean noise into discrete rewards, effectively making them continuous. This achieves GRPO-equivalent performance in approximately 10% of the training steps.

**Gradient Starvation (arXiv 2605.07689):**
In binary-reward GRPO, when every response in a group is either all-correct or all-incorrect, the group-mean-centered advantage becomes exactly zero -- the policy receives no learning signal at all. This "gradient starvation" was measured at a 0.69 degeneracy rate at group size 4. A simple fix (replacing group-mean centering with a fixed-reference continuous advantage A=2r-1) yielded a 45.4-point accuracy gain (73.8% vs 28.4%).

**Vanishing Gradients in Reinforcement Finetuning (arXiv 2310.20703, ICLR 2024):**
Razin et al. formally prove that the expected gradient vanishes when the reward standard deviation under the current policy is small -- even if expected reward is far from optimal. Binary rewards exacerbate this because their standard deviation is inherently bounded and frequently near-zero for hard problems. This establishes a formal theoretical basis for why continuous reward signals provide stronger gradient signals.

**Binary Rewards as a Fundamental Degeneracy (arXiv 2605.02375):**
This paper argues that binary rewards create a fundamental degeneracy for policy gradient methods: the set of distributions maximizing expected binary reward is infinite with no distinguished element, leading to diversity collapse where single-sample accuracy improves but multi-sample coverage degrades.

---

### 2. Smooth (Soft) Gate Functions Outperform Hard Clipping/Gating

**Smooth Gate Functions for Policy Optimization (arXiv 2602.19345):**
This paper directly formalizes the question of smooth vs hard gating in policy optimization. GRPO's hard clipping creates discontinuous gradients. The authors formalize key properties that admissible gate functions should satisfy, then evaluate families of smooth alternatives (sigmoid-based, polynomial decay, Gaussian attenuation). They find that smooth gate functions produce more stable training dynamics. The paper provides a formal framework for reasoning about gate function design.

**Soft Adaptive Policy Optimization / SAPO (arXiv 2511.20347):**
SAPO replaces PPO's hard clip with a temperature-controlled sigmoid gate. The key insight: hard clipping forces a binary choice (gradient passes or is zeroed), making it difficult to balance between overly tight clipping (too few valid gradient samples) and too loose clipping (noisy off-policy gradients). Sigmoid-based soft clipping achieves 10-60x higher performance values than standard PPO by enabling continuous gradient modulation.

---

### 3. Multiplicative (Continuous) Shaping Generalizes Binary Gating

**GR3: Group Relative Reward Rescaling (arXiv 2603.10535):**
This is perhaps the most directly relevant paper. GR3 reframes reward control as a multiplicative rescaling paradigm, establishing what the authors explicitly call a "generalized, continuous, and reward-dependent gating mechanism." Key findings:
- In the strict binary reward setting, multiplicative shaping is mathematically equivalent to heuristic gating.
- In continuous reward settings, multiplicative shaping provides a principled "soft" gating mechanism where hard binary indicators fail.
- Gated additive variants (with hard thresholds) underperform and produce optimization instability from the discontinuities introduced by hard gating.
- GR3's continuous multiplicative approach maintains task reward parity with standard GRPO while achieving controlled length reduction across both RLHF and RLVR settings.

This directly supports your argument: continuous gating is a strict generalization of binary gating, they are equivalent in the binary case, but continuous gating is qualitatively superior when rewards are non-binary.

---

### 4. Gradient Flow Theory for Multiplicative Gating

**Theory of Gating in Recurrent Neural Networks (Phys. Rev. X, arXiv 2007.14823):**
This physics-oriented paper provides formal analysis of how multiplicative gating controls gradient flow. Gating offers flexible control of two features: timescales and dimensionality. Continuous gates enable a "marginally stable" regime where the network functions as a flexible integrator. However, the Hadamard product (element-wise multiplication underlying gating) can contribute to gradient instability when multiplicands involve sigmoidal activations -- gradients may vanish or explode depending on input scale. This provides both the theoretical justification for continuous gating (flexible timescale control) and a warning about proper calibration.

---

### 5. Optimization Landscape and Lipschitz Continuity Arguments

**Lipschitz Continuity and Convergence (arXiv 2404.13316, arXiv 1804.07193):**
Foundational RL theory establishes that Lipschitz continuity of the reward and value functions is a key property for convergence guarantees. A continuous gating function preserves Lipschitz continuity of the composite reward, while binary gating introduces discontinuities that break this property. Stronger Lipschitz conditions on the value function yield tighter convergence bounds and smaller gaps between approximate and optimal solutions.

**Potential-Based Reward Shaping (Ng, Harada, Russell, ICML 1999):**
The foundational PBRS framework proves that reward transformations of the form F(s,s') = gamma * Phi(s') - Phi(s) preserve optimal policies. This framework inherently assumes continuous potential functions. Recent extensions note theoretical limitations when potential functions are discontinuous, further supporting the argument that smooth/continuous reward transformations have stronger theoretical properties.

---

### 6. Curriculum Learning: Smooth vs Discontinuous Transitions

Research on curriculum learning consistently shows that smooth transitions between difficulty levels outperform abrupt shifts. Episode-based Dynamic Reward Shaping mechanisms combined with curriculum learning balance exploration and convergence by gradually reducing shaping strength. Abrupt difficulty transitions can cause "extinction effects" that reset learning progress. This is analogous to the continuous vs binary gating question: continuous gating provides smooth curriculum-like transitions in reward emphasis, while binary gating creates discontinuous jumps.

---

### 7. Multimodal RL with Continuous Gating

**PEPO (arXiv 2603.22847):**
Directly relevant to your multimodal setting. PEPO uses a smooth gating mechanism to combine perception priors (hidden-state similarity to visual tokens) with exploration priors (token entropy) for token-level advantage estimation. The gating is explicitly continuous -- perception remains dominant while entropy acts as a continuous modulator. This integrates seamlessly with GRPO/DAPO and shows consistent improvements across multimodal benchmarks.

**HARMO (arXiv 2510.05283):**
Proposes hybrid rewards integrating verifiable (rule-based) and non-verifiable (model-based) signals for multimodal LLM alignment, with continuous weighting between reward aspects. Achieves ~9.5% average improvement across benchmarks.

---

### Summary of Key Arguments for Your Reviewer Response

1. **Gradient pathology elimination**: Binary gating creates provable gradient vanishing (when reward std is small) and gradient starvation (when all group members agree). Continuous gating eliminates both pathologies by ensuring non-zero gradient signals throughout training. This is formalized in arXiv 2310.20703 (ICLR 2024) and demonstrated empirically in arXiv 2605.07689.

2. **Strict mathematical generalization**: GR3 (arXiv 2603.10535) proves that multiplicative continuous gating reduces exactly to binary gating in the binary reward case, but provides a principled extension for continuous rewards. Binary gating is a special case of continuous gating, not an equivalent alternative.

3. **Optimization landscape smoothness**: Continuous gating preserves Lipschitz continuity of the reward landscape, maintaining convergence guarantees that binary gating breaks. Hard gating introduces optimization discontinuities empirically shown to cause instability (GR3's comparison of gated additive vs multiplicative approaches).

4. **Quantitative evidence**: ReDit shows 10x training speedup from making binary rewards continuous; SAPO shows 10-60x performance improvement from smooth vs hard clipping; gradient starvation fix shows 45-point accuracy gain.

5. **The qualitative difference is precisely the difference between continuous and discontinuous optimization**: this is not merely a quantitative improvement but a structural change in the loss landscape that eliminates degenerate gradient regions.

---

Sources:
- [ReDit: Reward Dithering for Improved LLM Policy Optimization](https://arxiv.org/html/2506.18631v1)
- [Binary Rewards and Reinforcement Learning: Fundamental Challenges](https://arxiv.org/abs/2605.02375v1)
- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689)
- [Vanishing Gradients in Reinforcement Finetuning of Language Models](https://arxiv.org/abs/2310.20703)
- [Smooth Gate Functions for Soft Advantage Policy Optimization](https://arxiv.org/abs/2602.19345)
- [Soft Adaptive Policy Optimization (SAPO)](https://arxiv.org/abs/2511.20347)
- [GR3: Group Relative Reward Rescaling](https://arxiv.org/abs/2603.10535)
- [On the Optimization Dynamics of RLVR: Gradient Gap and Step Size Thresholds](https://arxiv.org/abs/2510.08539)
- [Theory of Gating in Recurrent Neural Networks](https://arxiv.org/abs/2007.14823)
- [Lipschitz Continuity in Model-based Reinforcement Learning](https://arxiv.org/pdf/1804.07193)
- [On the Stability of Lipschitz Continuous Control Problems](https://arxiv.org/abs/2404.13316)
- [Policy Invariance Under Reward Transformations (Ng, Harada, Russell)](https://www.semanticscholar.org/paper/94066dc12fe31e96af7557838159bde598cb4f10)
- [PEPO: Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought](https://arxiv.org/abs/2603.22847)
- [HARMO: Beyond Monolithic Rewards](https://arxiv.org/abs/2510.05283)
- [RLNVR: Reinforcement Learning from Non-Verified Real-World Rewards](https://arxiv.org/pdf/2508.12165)
- [Variance Aware Reward Smoothing](https://www.sciencedirect.com/science/article/abs/pii/S0925231221009139)&lt;/result>
&lt;usage>&lt;total_tokens>28698&lt;/total_tokens>&lt;tool_uses>25&lt;/tool_uses>&lt;duration_ms>151058&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe4b5aba-b782-4743-802a-b9fcee25b7c4",
  "isSidechain": false,
  "promptId": "c362c636-76af-4a0e-aeb8-41abeea73ea1",
  "type": "user",
  "uuid": "efdac1df-e8b8-4858-92ab-6b66cc0eb704",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-28T03:28:07.328Z_

<details><summary>Logged reasoning block</summary>

```text
This is excellent! The continuous vs binary gating research agent found very strong evidence. Key findings:

1. **GR3** proves continuous multiplicative gating is a strict mathematical generalization of binary gating
2. Multiple papers show binary rewards create gradient pathologies (vanishing, starvation, explosion)
3. Smooth gate functions outperform hard clipping
4. **PEPO** uses smooth gating in multimodal RL specifically

This gives me strong theoretical grounding for the novelty claim. Now I'm still waiting for:
- MMSci dataset details
- Scientific figure critique benchmarks

Let me wait for those, then synthesize everything.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efdac1df-e8b8-4858-92ab-6b66cc0eb704",
  "isSidechain": false,
  "requestId": "req_011CbUFptSfX33u28RpKUk7q",
  "type": "assistant",
  "uuid": "4f4cec63-ec7a-4446-86b5-ab8481873133",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Szw8ykvi82iF3dGsGj4FXu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3497,
      "cache_read_input_tokens": 42866,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 361,
          "cache_read_input_tokens": 42866,
          "cache_creation_input_tokens": 3497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3497
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

_source line 72 · 2026-05-28T03:28:10.675Z_

This is a goldmine for the novelty argument. The continuous vs binary gating agent found:

1. **GR3 (arXiv:2603.10535)** - Proves continuous multiplicative gating is a **strict mathematical generalization** of binary gating, and that hard gating causes optimization instability
2. **Gradient pathology evidence** - Binary rewards create provable gradient vanishing/starvation (multiple papers with formal proofs)
3. **PEPO (arXiv:2603.22847)** - Smooth gating specifically for multimodal RL
4. **Quantitative evidence** - 10x training speedup, 45-point accuracy gains from continuous vs binary reward signals

This is the key theoretical argument to elevate novelty beyond "apply X to domain Y." Now waiting for last 2 agents (MMSci details, benchmark construction).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f4cec63-ec7a-4446-86b5-ab8481873133",
  "isSidechain": false,
  "requestId": "req_011CbUFptSfX33u28RpKUk7q",
  "type": "assistant",
  "uuid": "03f5f645-8d5b-4dc7-869c-d67eb633716d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Szw8ykvi82iF3dGsGj4FXu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3497,
      "cache_read_input_tokens": 42866,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 361,
          "cache_read_input_tokens": 42866,
          "cache_creation_input_tokens": 3497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3497
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

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "03f5f645-8d5b-4dc7-869c-d67eb633716d",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 75 · 2026-05-28T03:30:07.674Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:30:07.674Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "&lt;task-notification>\n&lt;task-id>a87c831bd24e0caa5&lt;/task-id>\n&lt;tool-use-id>toolu_01AWPQEUjgcGxkaDFkLv6QkX&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a87c831bd24e0caa5.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research MMSci dataset details\" completed&lt;/summary>\n&lt;result>I now have extensive information. Let me compile the comprehensive report.\n\n---\n\nHere is my detailed research report on the MMSci dataset and rubric-based re-annotation approaches.\n\n---\n\n## 1. MMSci Dataset Overview\n\n**Paper:** arXiv:2407.04903, accepted at NeurIPS 2024 Workshop on Scientific Document Understanding.\n**Repository:** https://github.com/Leezekun/MMSci\n**License:** CC BY 4.0 (data), Apache 2.0 (code)\n\n### Scale and Splits\n\n| Component | Size |\n|-----------|------|\n| Total articles | 131,393 |\n| Total figures | 742,273 |\n| Total sub-captions/sub-figures | 514,054 |\n| Training articles | 128,561 |\n| Training samples | ~1,079,797 |\n| Validation articles | 1,414 |\n| Test articles | 1,418 |\n| Benchmark samples per task setting | ~1,200 |\n\nAll data is sourced from **Nature Communications** open-access peer-reviewed articles.\n\n---\n\n## 2. The 72 Scientific Disciplines\n\nGrouped into five major categories (note: the exact count per group varies slightly across paper versions due to overlapping categorization -- e.g., \"Ecology\" appears under both Earth/Environmental and Biological):\n\n**Physical Sciences (~8):** Materials Science, Chemistry, Physics, Nanoscience and Technology, Optics and Photonics, Engineering, Energy Science and Technology, Mathematics and Computing\n\n**Earth and Environmental Sciences (~13):** Astronomy and Planetary Science, Ecology, Climate Sciences, Solid Earth Sciences, Environmental Sciences, Biogeochemistry, Ocean Sciences, Environmental Social Sciences, Natural Hazards, Planetary Science, Hydrology, Limnology, Space Physics\n\n**Biological Sciences (~27):** Cell Biology, Biochemistry, Microbiology, Neuroscience, Molecular Biology, Genetics, Cancer, Immunology, Biological Techniques, Computational Biology and Bioinformatics, Biotechnology, Biophysics, Structural Biology, Developmental Biology, Evolution, Plant Sciences, Physiology, Chemical Biology, Systems Biology, Drug Discovery, Stem Cells, Zoology, Psychology, Diseases, Medical Research, Oncology\n\n**Health Sciences (~15):** Health Care, Pathogenesis, Biomarkers, Cardiology, Gastroenterology, Endocrinology, Anatomy, Neurology, Molecular Medicine, Risk Factors, Rheumatology, Nephrology, Signs and Symptoms, Urology, Health Occupations\n\n**Scientific Community and Society (~9):** Social Sciences, Scientific Community, Energy and Society, Agriculture, Developing World, Water Resources, Geography, Business and Industry, Forestry\n\nThese 72 subjects were consolidated into 18 broader groups for annotation, and 10 major scientific domains had PhD-level annotators available: Material Science, Chemistry, Physics, Biochemistry, Environment, Climate Sciences, Earth Sciences, Biological Sciences, Biomedical Sciences, and Health and Medicine.\n\n---\n\n## 3. Original Evaluation Metrics\n\nMMSci uses two tiers of evaluation:\n\n### Traditional Reference-Based Metrics\n- **BLEU@1-4** (n-gram overlap)\n- **ROUGE-L** (longest common subsequence)\n- **METEOR** (alignment-based)\n- **BERTScore** (contextual embedding similarity)\n- **CIDEr** (TF-IDF weighted n-gram consensus)\n- **CLIPScore / RefCLIPScore** (vision-language alignment)\n\n### LLM-Based Metrics (the paper's more advanced evaluation)\n- **Modified FActScore** (0-1 scale): Decomposes generated captions into atomic factual statements and assesses each unit's accuracy. Adapted from the original FActScore to handle complex multi-sub-figure captions.\n- **G-Eval** (1-5 scale): Assesses overall similarity and quality relative to reference captions using LLM judgment.\n\n### Key Scores (selected models)\n\n| Model | Setting | BLEU-2 | ROUGE-L | CIDEr | FActScore | G-Eval |\n|-------|---------|--------|---------|-------|-----------|--------|\n| GPT-4o | Image-only | 4.93 | 15.59 | 0.27 | - | 4.01 |\n| GPT-4o | Abstract-grounded | - | - | - | - | 4.22 |\n| Claude-3.5-Sonnet | Image-only | 5.01 | 15.54 | 0.65 | - | 3.53 |\n| Claude-3.5-Sonnet | Abstract-grounded | - | - | - | - | 4.04 |\n| Qwen2-VL-7B-MMSci | Image-only | 19.13 | 21.78 | 3.73 | 18.17 | 3.21 |\n| Qwen2-VL-7B-MMSci | Abstract-grounded | - | - | - | 20.59 | 3.54 |\n| LLaVA-Next-MMSci | Abstract-grounded | - | - | - | - | - |\n\n**Critical observation:** CIDEr scores are consistently extremely low (0.00-3.73) across ALL models, highlighting that reference-based n-gram metrics are fundamentally inadequate for scientific figure captioning where the same content can be described in vastly different ways. This is a strong motivation for rubric-based evaluation.\n\n---\n\n## 4. Reference Captions\n\nReference captions are the **original author-written figure captions** from Nature Communications papers -- not synthetic or crowd-sourced annotations. Key characteristics:\n\n- **Average length:** 153 words (much longer than natural image captions like COCO's ~10 words)\n- **Structure:** Main caption (often bold) + color-coded sub-captions for each sub-figure panel (a, b, c, ...)\n- **Content:** Highly technical, domain-specific language requiring graduate-level expertise\n- **Sub-captions:** 514,054 extracted via regex matching of alphabetical indices (a-z)\n- **Preprocessing:** LaTeX expressions converted to plain text\n\nThese are authentic scientific descriptions, not simplified or paraphrased versions.\n\n---\n\n## 5. Supported Tasks\n\n1. **Figure Captioning** (three settings):\n   - Image-only (ungrounded)\n   - Abstract-grounded (figure + paper abstract as context)\n   - Full content-grounded (figure + full paper text)\n\n2. **Multiple-Choice Questions** (three variants):\n   - Figure-to-Caption matching (given figure, pick correct caption from 4)\n   - Subfigure-to-Subcaption matching\n   - Subcaption-to-Subfigure matching\n\n3. **Multi-turn Conversations** (training only): Visual instruction tuning dialogues about figure interpretation\n\n4. **Pre-training**: MMC4-formatted interleaved text-image sequences for multimodal pre-training\n\n---\n\n## 6. Data Format and Annotation Structure\n\n### Source Data Schema (`{uid}_data.json`)\n```\n{\n  \"pdf_link\": string,           // Article PDF URL\n  \"review_pdf_link\": string,    // Review PDF URL (if available)\n  \"unique_id\": string,          // Unique article identifier\n  \"title\": string,              // Article headline\n  \"abstract\": string,           // Article summary\n  \"published_time\": date,       // Publication date\n  \"images\": [\n    {\n      \"image_filename\": string, // e.g., \"{uid}_figure_1.png\"\n      \"text_filename\": string,  // Caption text file\n      \"caption\": string,        // Main figure description\n      \"description\": string     // Detailed caption with sub-captions\n    }\n  ],\n  \"sections\": [\n    {\n      \"section\": string,        // Section name\n      \"content\": string         // Section text\n    }\n  ],\n  \"references\": [\n    {\n      \"idx\": string,\n      \"title\": string,\n      \"link\": string\n    }\n  ]\n}\n```\n\n### Task-Specific Files\n- `image_caption_generation_data.json` -- captioning task (uid, category, subject, abstract, article content, image filename, caption)\n- `image_caption_matching_data.json` -- multiple-choice (uid, category, subject, question, options A-D, answer key, image)\n- `image_caption_chat_data.json` -- multi-turn conversations (training only)\n\n### Organization\nData is organized hierarchically: `category/subject/article_uid/` with PNG figure files and JSON metadata. Test set answers are anonymized to prevent data contamination.\n\n---\n\n## 7. How Other Papers Have Done Rubric-Based Re-Annotation\n\n### RubiCap (arXiv:2603.09160) -- Most Directly Relevant\n\nRubiCap is the closest precedent for what you want to do. It converts reference-based dense image captioning to rubric-based RL training:\n\n**Pipeline:**\n1. **Teacher Committee Generation:** 5 diverse VLMs (Gemini 2.5 Pro, GPT-5, Qwen2.5-VL-72B, Gemma-3-27B, Qwen3-VL-30B) each generate a candidate caption for each image\n2. **Student Baseline:** Current policy generates its own caption\n3. **Consensus Extraction:** LLM rubric writer identifies descriptive elements where majority (&gt;=K/2 of K teachers) agree\n4. **Deficiency Diagnosis:** Comparative analysis between student caption and teacher consensus, categorized by severity: Critical (weight 3.0), Important (2.0), Minor (1.0)\n5. **Rubric Formulation:** Each gap becomes a binary pass/fail criterion with severity weight\n\n**Rubric Structure:** R(x, c_student, {c_teacher_k}) = {(r_m, w_m)}^M where each r_m is a binary criterion with weight w_m\n\n**Reward:** G(x, c_student) = sum(w_m * y_hat_m) / sum(w_m) -- weighted proportion of criteria satisfied, used with GRPO\n\n### OpenRubrics (arXiv:2510.07743) -- Scalable Rubric Generation\n\n**Key innovation:** Contrastive Rubric Generation (CRG) -- derives rubrics by contrasting preferred vs. rejected responses to extract:\n- **Hard rules:** Objective, explicitly verifiable constraints\n- **Principles:** Qualitative aspects requiring judgment\n\nBuilt from diverse public datasets. Produces Rubric-RM which achieves 6.8% average improvement across benchmarks.\n\n### Rubric-ARM (arXiv:2602.01511) -- Joint Optimization\n\nTreats rubric generation as a latent action in RL. Alternates between:\n- Judge update (fixed rubric generator)\n- Rubric generator update (fixed judge)\n\nSupports both DPO (offline) and GRPO (online) with rubric-conditioned rewards.\n\n### TechImage-Bench (arXiv:2512.12220) -- Technical Image Rubrics\n\nConverts abstract evaluation criteria into binary unit-test-like questions. Pipeline:\n1. Extract captions and contextual text\n2. LMM identifies implicit constraints\n3. Expand constraints into fine-grained binary scoring points (inclusion + exclusion)\n4. Human expert refinement\n\n### SciCapenter (arXiv:2403.17784) -- Scientific Figure Caption Checklist\n\nUses a 6-dimension checklist for scientific figure captions:\n- Helpfulness, OCR mention, Relation (element relationships), Stats (numerical data), Takeaway (conclusions), Visual properties (color/shape/size)\n- Scored on 1-6 scale via GPT-3.5-turbo zero-shot evaluation\n\n---\n\n## 8. Proposed Re-Annotation Pipeline for MMSci (Reference-Based to Rubric-Based)\n\nBased on all the above research, here is a detailed specification for converting MMSci from reference-based to rubric-based evaluation for non-verifiable RL training:\n\n### Phase 1: Rubric Generation per Figure\n\nFor each (figure, reference_caption) pair in MMSci:\n\n**Step 1 -- Structured Caption Analysis.** Use an LLM (e.g., GPT-4o, Claude) to decompose the reference caption into atomic claims:\n- Factual statements about what is shown in each sub-figure\n- Quantitative claims (numbers, trends, comparisons)\n- Methodological descriptions (what technique produced this visualization)\n- Interpretive claims (what the results mean scientifically)\n- Structural/compositional descriptions (layout, labels, axes)\n\n**Step 2 -- Dimension-Specific Criteria Extraction.** For each figure, generate criteria along these dimensions (inspired by SciCapenter + RubiCap + TechImage-Bench):\n- **Visual Accuracy:** Does the caption correctly describe what is visually present?\n- **Sub-figure Coverage:** Are all sub-figures (a, b, c...) addressed?\n- **Quantitative Fidelity:** Are numerical values, trends, and comparisons correctly stated?\n- **Scientific Terminology:** Is appropriate domain-specific vocabulary used?\n- **Methodological Context:** Is the experimental/computational method mentioned?\n- **Interpretive Validity:** Are conclusions/takeaways scientifically sound?\n- **Structural Description:** Are axes, labels, legends, and scales described?\n\n**Step 3 -- Binary Criterion Formulation.** Convert each extracted claim into a binary pass/fail criterion with severity weight:\n- Critical (3.0): Core factual/scientific correctness\n- Important (2.0): Completeness and coverage\n- Minor (1.0): Stylistic and structural polish\n\n**Step 4 -- Teacher Committee Augmentation (optional but recommended).** Generate 3-5 alternative captions using diverse VLMs. Use consensus analysis to identify which criteria are universally agreed upon (higher confidence) vs. model-specific.\n\n### Phase 2: Rubric Validation\n\n- Sample ~500 figure-rubric pairs for human expert review across the 10 PhD-annotated domains\n- Measure inter-annotator agreement (target Cohen's Kappa &gt;= 0.7)\n- Iteratively refine the rubric generation prompt based on expert feedback\n\n### Phase 3: Reward Signal for RL\n\n**Explicit aggregation:** Score = sum(w_i * binary_score_i) / sum(w_i), normalized to [0, 1]\n\n**LLM Judge:** For each generated caption, an LLM evaluates each binary criterion, producing the reward signal. Use position-switching and multi-sample scoring for robustness.\n\n**Training:** Use GRPO with the rubric-based reward, computing advantage estimates from the structured scores rather than a single scalar.\n\n### Key Design Decisions\n\n1. **Instance-specific rubrics** (per-figure, not generic) -- essential given the diversity of 72 disciplines\n2. **Reference-grounded** -- rubrics are derived from the high-quality Nature Communications captions, ensuring expert-level grounding\n3. **Abstract-conditioned** -- for abstract-grounded captioning, rubrics should also account for whether the caption integrates information from the abstract\n4. **Severity weighting** -- prevents the model from gaming easy criteria while ignoring hard scientific content\n5. **Discipline-aware** -- rubric generation prompts should include the discipline label so criteria are domain-appropriate\n\nSources:\n- [MMSci Paper (arXiv:2407.04903)](https://arxiv.org/abs/2407.04903)\n- [MMSci HTML v3](https://arxiv.org/html/2407.04903v3)\n- [MMSci GitHub Repository](https://github.com/Leezekun/MMSci)\n- [MMSci DATACARD](https://github.com/Leezekun/MMSci/blob/main/mmsci-data/DATACARD.md)\n- [MMSci OpenReview](https://openreview.net/forum?id=DEOV74Idsg)\n- [RubiCap (arXiv:2603.09160)](https://arxiv.org/html/2603.09160)\n- [Rubric-ARM (arXiv:2602.01511)](https://arxiv.org/abs/2602.01511)\n- [OpenRubrics (arXiv:2510.07743)](https://arxiv.org/abs/2510.07743)\n- [TechImage-Bench (arXiv:2512.12220)](https://arxiv.org/html/2512.12220)\n- [SciCapenter (arXiv:2403.17784)](https://arxiv.org/html/2403.17784v1)\n- [Rubric-Based Rewards for RL (Cameron Wolfe blog)](https://cameronrwolfe.substack.com/p/rubric-rl)\n- [Five Years of SciCap](https://arxiv.org/html/2512.21789)&lt;/result>\n&lt;usage>&lt;total_tokens>31689&lt;/total_tokens>&lt;tool_uses>27&lt;/tool_uses>&lt;duration_ms>270864&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
````

---

### Runtime record

_source line 76 · 2026-05-28T03:30:07.725Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:30:07.725Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 8

7 recorded events

### User

_source line 77 · 2026-05-28T03:30:07.733Z_

&lt;task-notification>
&lt;task-id>a87c831bd24e0caa5&lt;/task-id>
&lt;tool-use-id>toolu_01AWPQEUjgcGxkaDFkLv6QkX&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a87c831bd24e0caa5.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research MMSci dataset details" completed&lt;/summary>
&lt;result>I now have extensive information. Let me compile the comprehensive report.

---

Here is my detailed research report on the MMSci dataset and rubric-based re-annotation approaches.

---

## 1. MMSci Dataset Overview

**Paper:** arXiv:2407.04903, accepted at NeurIPS 2024 Workshop on Scientific Document Understanding.
**Repository:** https://github.com/Leezekun/MMSci
**License:** CC BY 4.0 (data), Apache 2.0 (code)

### Scale and Splits

| Component | Size |
|-----------|------|
| Total articles | 131,393 |
| Total figures | 742,273 |
| Total sub-captions/sub-figures | 514,054 |
| Training articles | 128,561 |
| Training samples | ~1,079,797 |
| Validation articles | 1,414 |
| Test articles | 1,418 |
| Benchmark samples per task setting | ~1,200 |

All data is sourced from **Nature Communications** open-access peer-reviewed articles.

---

## 2. The 72 Scientific Disciplines

Grouped into five major categories (note: the exact count per group varies slightly across paper versions due to overlapping categorization -- e.g., "Ecology" appears under both Earth/Environmental and Biological):

**Physical Sciences (~8):** Materials Science, Chemistry, Physics, Nanoscience and Technology, Optics and Photonics, Engineering, Energy Science and Technology, Mathematics and Computing

**Earth and Environmental Sciences (~13):** Astronomy and Planetary Science, Ecology, Climate Sciences, Solid Earth Sciences, Environmental Sciences, Biogeochemistry, Ocean Sciences, Environmental Social Sciences, Natural Hazards, Planetary Science, Hydrology, Limnology, Space Physics

**Biological Sciences (~27):** Cell Biology, Biochemistry, Microbiology, Neuroscience, Molecular Biology, Genetics, Cancer, Immunology, Biological Techniques, Computational Biology and Bioinformatics, Biotechnology, Biophysics, Structural Biology, Developmental Biology, Evolution, Plant Sciences, Physiology, Chemical Biology, Systems Biology, Drug Discovery, Stem Cells, Zoology, Psychology, Diseases, Medical Research, Oncology

**Health Sciences (~15):** Health Care, Pathogenesis, Biomarkers, Cardiology, Gastroenterology, Endocrinology, Anatomy, Neurology, Molecular Medicine, Risk Factors, Rheumatology, Nephrology, Signs and Symptoms, Urology, Health Occupations

**Scientific Community and Society (~9):** Social Sciences, Scientific Community, Energy and Society, Agriculture, Developing World, Water Resources, Geography, Business and Industry, Forestry

These 72 subjects were consolidated into 18 broader groups for annotation, and 10 major scientific domains had PhD-level annotators available: Material Science, Chemistry, Physics, Biochemistry, Environment, Climate Sciences, Earth Sciences, Biological Sciences, Biomedical Sciences, and Health and Medicine.

---

## 3. Original Evaluation Metrics

MMSci uses two tiers of evaluation:

### Traditional Reference-Based Metrics
- **BLEU@1-4** (n-gram overlap)
- **ROUGE-L** (longest common subsequence)
- **METEOR** (alignment-based)
- **BERTScore** (contextual embedding similarity)
- **CIDEr** (TF-IDF weighted n-gram consensus)
- **CLIPScore / RefCLIPScore** (vision-language alignment)

### LLM-Based Metrics (the paper's more advanced evaluation)
- **Modified FActScore** (0-1 scale): Decomposes generated captions into atomic factual statements and assesses each unit's accuracy. Adapted from the original FActScore to handle complex multi-sub-figure captions.
- **G-Eval** (1-5 scale): Assesses overall similarity and quality relative to reference captions using LLM judgment.

### Key Scores (selected models)

| Model | Setting | BLEU-2 | ROUGE-L | CIDEr | FActScore | G-Eval |
|-------|---------|--------|---------|-------|-----------|--------|
| GPT-4o | Image-only | 4.93 | 15.59 | 0.27 | - | 4.01 |
| GPT-4o | Abstract-grounded | - | - | - | - | 4.22 |
| Claude-3.5-Sonnet | Image-only | 5.01 | 15.54 | 0.65 | - | 3.53 |
| Claude-3.5-Sonnet | Abstract-grounded | - | - | - | - | 4.04 |
| Qwen2-VL-7B-MMSci | Image-only | 19.13 | 21.78 | 3.73 | 18.17 | 3.21 |
| Qwen2-VL-7B-MMSci | Abstract-grounded | - | - | - | 20.59 | 3.54 |
| LLaVA-Next-MMSci | Abstract-grounded | - | - | - | - | - |

**Critical observation:** CIDEr scores are consistently extremely low (0.00-3.73) across ALL models, highlighting that reference-based n-gram metrics are fundamentally inadequate for scientific figure captioning where the same content can be described in vastly different ways. This is a strong motivation for rubric-based evaluation.

---

## 4. Reference Captions

Reference captions are the **original author-written figure captions** from Nature Communications papers -- not synthetic or crowd-sourced annotations. Key characteristics:

- **Average length:** 153 words (much longer than natural image captions like COCO's ~10 words)
- **Structure:** Main caption (often bold) + color-coded sub-captions for each sub-figure panel (a, b, c, ...)
- **Content:** Highly technical, domain-specific language requiring graduate-level expertise
- **Sub-captions:** 514,054 extracted via regex matching of alphabetical indices (a-z)
- **Preprocessing:** LaTeX expressions converted to plain text

These are authentic scientific descriptions, not simplified or paraphrased versions.

---

## 5. Supported Tasks

1. **Figure Captioning** (three settings):
   - Image-only (ungrounded)
   - Abstract-grounded (figure + paper abstract as context)
   - Full content-grounded (figure + full paper text)

2. **Multiple-Choice Questions** (three variants):
   - Figure-to-Caption matching (given figure, pick correct caption from 4)
   - Subfigure-to-Subcaption matching
   - Subcaption-to-Subfigure matching

3. **Multi-turn Conversations** (training only): Visual instruction tuning dialogues about figure interpretation

4. **Pre-training**: MMC4-formatted interleaved text-image sequences for multimodal pre-training

---

## 6. Data Format and Annotation Structure

### Source Data Schema (`{uid}_data.json`)
```
{
  "pdf_link": string,           // Article PDF URL
  "review_pdf_link": string,    // Review PDF URL (if available)
  "unique_id": string,          // Unique article identifier
  "title": string,              // Article headline
  "abstract": string,           // Article summary
  "published_time": date,       // Publication date
  "images": [
    {
      "image_filename": string, // e.g., "{uid}_figure_1.png"
      "text_filename": string,  // Caption text file
      "caption": string,        // Main figure description
      "description": string     // Detailed caption with sub-captions
    }
  ],
  "sections": [
    {
      "section": string,        // Section name
      "content": string         // Section text
    }
  ],
  "references": [
    {
      "idx": string,
      "title": string,
      "link": string
    }
  ]
}
```

### Task-Specific Files
- `image_caption_generation_data.json` -- captioning task (uid, category, subject, abstract, article content, image filename, caption)
- `image_caption_matching_data.json` -- multiple-choice (uid, category, subject, question, options A-D, answer key, image)
- `image_caption_chat_data.json` -- multi-turn conversations (training only)

### Organization
Data is organized hierarchically: `category/subject/article_uid/` with PNG figure files and JSON metadata. Test set answers are anonymized to prevent data contamination.

---

## 7. How Other Papers Have Done Rubric-Based Re-Annotation

### RubiCap (arXiv:2603.09160) -- Most Directly Relevant

RubiCap is the closest precedent for what you want to do. It converts reference-based dense image captioning to rubric-based RL training:

**Pipeline:**
1. **Teacher Committee Generation:** 5 diverse VLMs (Gemini 2.5 Pro, GPT-5, Qwen2.5-VL-72B, Gemma-3-27B, Qwen3-VL-30B) each generate a candidate caption for each image
2. **Student Baseline:** Current policy generates its own caption
3. **Consensus Extraction:** LLM rubric writer identifies descriptive elements where majority (&gt;=K/2 of K teachers) agree
4. **Deficiency Diagnosis:** Comparative analysis between student caption and teacher consensus, categorized by severity: Critical (weight 3.0), Important (2.0), Minor (1.0)
5. **Rubric Formulation:** Each gap becomes a binary pass/fail criterion with severity weight

**Rubric Structure:** R(x, c_student, {c_teacher_k}) = {(r_m, w_m)}^M where each r_m is a binary criterion with weight w_m

**Reward:** G(x, c_student) = sum(w_m * y_hat_m) / sum(w_m) -- weighted proportion of criteria satisfied, used with GRPO

### OpenRubrics (arXiv:2510.07743) -- Scalable Rubric Generation

**Key innovation:** Contrastive Rubric Generation (CRG) -- derives rubrics by contrasting preferred vs. rejected responses to extract:
- **Hard rules:** Objective, explicitly verifiable constraints
- **Principles:** Qualitative aspects requiring judgment

Built from diverse public datasets. Produces Rubric-RM which achieves 6.8% average improvement across benchmarks.

### Rubric-ARM (arXiv:2602.01511) -- Joint Optimization

Treats rubric generation as a latent action in RL. Alternates between:
- Judge update (fixed rubric generator)
- Rubric generator update (fixed judge)

Supports both DPO (offline) and GRPO (online) with rubric-conditioned rewards.

### TechImage-Bench (arXiv:2512.12220) -- Technical Image Rubrics

Converts abstract evaluation criteria into binary unit-test-like questions. Pipeline:
1. Extract captions and contextual text
2. LMM identifies implicit constraints
3. Expand constraints into fine-grained binary scoring points (inclusion + exclusion)
4. Human expert refinement

### SciCapenter (arXiv:2403.17784) -- Scientific Figure Caption Checklist

Uses a 6-dimension checklist for scientific figure captions:
- Helpfulness, OCR mention, Relation (element relationships), Stats (numerical data), Takeaway (conclusions), Visual properties (color/shape/size)
- Scored on 1-6 scale via GPT-3.5-turbo zero-shot evaluation

---

## 8. Proposed Re-Annotation Pipeline for MMSci (Reference-Based to Rubric-Based)

Based on all the above research, here is a detailed specification for converting MMSci from reference-based to rubric-based evaluation for non-verifiable RL training:

### Phase 1: Rubric Generation per Figure

For each (figure, reference_caption) pair in MMSci:

**Step 1 -- Structured Caption Analysis.** Use an LLM (e.g., GPT-4o, Claude) to decompose the reference caption into atomic claims:
- Factual statements about what is shown in each sub-figure
- Quantitative claims (numbers, trends, comparisons)
- Methodological descriptions (what technique produced this visualization)
- Interpretive claims (what the results mean scientifically)
- Structural/compositional descriptions (layout, labels, axes)

**Step 2 -- Dimension-Specific Criteria Extraction.** For each figure, generate criteria along these dimensions (inspired by SciCapenter + RubiCap + TechImage-Bench):
- **Visual Accuracy:** Does the caption correctly describe what is visually present?
- **Sub-figure Coverage:** Are all sub-figures (a, b, c...) addressed?
- **Quantitative Fidelity:** Are numerical values, trends, and comparisons correctly stated?
- **Scientific Terminology:** Is appropriate domain-specific vocabulary used?
- **Methodological Context:** Is the experimental/computational method mentioned?
- **Interpretive Validity:** Are conclusions/takeaways scientifically sound?
- **Structural Description:** Are axes, labels, legends, and scales described?

**Step 3 -- Binary Criterion Formulation.** Convert each extracted claim into a binary pass/fail criterion with severity weight:
- Critical (3.0): Core factual/scientific correctness
- Important (2.0): Completeness and coverage
- Minor (1.0): Stylistic and structural polish

**Step 4 -- Teacher Committee Augmentation (optional but recommended).** Generate 3-5 alternative captions using diverse VLMs. Use consensus analysis to identify which criteria are universally agreed upon (higher confidence) vs. model-specific.

### Phase 2: Rubric Validation

- Sample ~500 figure-rubric pairs for human expert review across the 10 PhD-annotated domains
- Measure inter-annotator agreement (target Cohen's Kappa &gt;= 0.7)
- Iteratively refine the rubric generation prompt based on expert feedback

### Phase 3: Reward Signal for RL

**Explicit aggregation:** Score = sum(w_i * binary_score_i) / sum(w_i), normalized to [0, 1]

**LLM Judge:** For each generated caption, an LLM evaluates each binary criterion, producing the reward signal. Use position-switching and multi-sample scoring for robustness.

**Training:** Use GRPO with the rubric-based reward, computing advantage estimates from the structured scores rather than a single scalar.

### Key Design Decisions

1. **Instance-specific rubrics** (per-figure, not generic) -- essential given the diversity of 72 disciplines
2. **Reference-grounded** -- rubrics are derived from the high-quality Nature Communications captions, ensuring expert-level grounding
3. **Abstract-conditioned** -- for abstract-grounded captioning, rubrics should also account for whether the caption integrates information from the abstract
4. **Severity weighting** -- prevents the model from gaming easy criteria while ignoring hard scientific content
5. **Discipline-aware** -- rubric generation prompts should include the discipline label so criteria are domain-appropriate

Sources:
- [MMSci Paper (arXiv:2407.04903)](https://arxiv.org/abs/2407.04903)
- [MMSci HTML v3](https://arxiv.org/html/2407.04903v3)
- [MMSci GitHub Repository](https://github.com/Leezekun/MMSci)
- [MMSci DATACARD](https://github.com/Leezekun/MMSci/blob/main/mmsci-data/DATACARD.md)
- [MMSci OpenReview](https://openreview.net/forum?id=DEOV74Idsg)
- [RubiCap (arXiv:2603.09160)](https://arxiv.org/html/2603.09160)
- [Rubric-ARM (arXiv:2602.01511)](https://arxiv.org/abs/2602.01511)
- [OpenRubrics (arXiv:2510.07743)](https://arxiv.org/abs/2510.07743)
- [TechImage-Bench (arXiv:2512.12220)](https://arxiv.org/html/2512.12220)
- [SciCapenter (arXiv:2403.17784)](https://arxiv.org/html/2403.17784v1)
- [Rubric-Based Rewards for RL (Cameron Wolfe blog)](https://cameronrwolfe.substack.com/p/rubric-rl)
- [Five Years of SciCap](https://arxiv.org/html/2512.21789)&lt;/result>
&lt;usage>&lt;total_tokens>31689&lt;/total_tokens>&lt;tool_uses>27&lt;/tool_uses>&lt;duration_ms>270864&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03f5f645-8d5b-4dc7-869c-d67eb633716d",
  "isSidechain": false,
  "promptId": "91eedfa7-49b2-4f0f-ad4f-cb8f72ecdc18",
  "type": "user",
  "uuid": "bcb51c84-7509-4234-9020-69eff24cb914",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-28T03:30:23.925Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have 6 out of 8 agents done. Still waiting for the scientific figure critique benchmark research agent. Let me review what I have:

1. **DRO** ✅ - Binary rubric-gating for non-verifiable text tasks. Key competitor. Uses hard accept/reject.
2. **Training AI Co-Scientists** ✅ - Rubric RL for scientific research plans. Text-only. Uses GRPO with rubric satisfaction ratio reward.
3. **Reward Hacking in Rubric-Based RL** ✅ - Studies rubric hacking in medical/science. Three exploitation patterns. Self-internalization gap as early stopping.


4. **ARES** ✅ - Automated rubric synthesis from documents. Text-only. 101K instances.
5. **POW3R** ✅ - Policy-aware dynamic rubric weighting. Both text and multimodal. Static weights suboptimal.
6. **rDPO** ✅ - Instance-specific rubrics for multimodal DPO. Essential vs additional criteria.
7. **Perception-R1** ✅ - Visual perception reward in RLVR. Verifiable.
8. **ClaimDiff-RL** ✅ - Claim-level captioning RL with graded severity.
9. **Continuous vs binary gating** ✅ - Continuous gating shows strong theoretical advantages: GR3 demonstrates it's a strict generalization of binary, binary approaches suffer from gradient issues, and PEPO extends this to multimodal settings.
10. **MMSci details** ✅ - Large-scale dataset with 742K figures across 72 scientific disciplines, using reference captions from Nature Communications, though CIDEr scores are notably low.

I'm waiting on the scientific figure critique benchmark research before pulling everything together.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcb51c84-7509-4234-9020-69eff24cb914",
  "isSidechain": false,
  "requestId": "req_011CbUFz8ndKzs1HatZYYLHk",
  "type": "assistant",
  "uuid": "fc8043da-5b5e-4956-ba94-a78006194632",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLzMhaW5PX6SF4qogRpAC9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4678,
      "cache_read_input_tokens": 46363,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 776,
          "cache_read_input_tokens": 46363,
          "cache_creation_input_tokens": 4678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4678
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

_source line 79 · 2026-05-28T03:30:29.545Z_

Excellent - 7 out of 8 agents done. Only the scientific figure critique benchmark research agent remains. Let me check if it's still running.

The key research findings are now very clear:

**For novelty elevation (the critical issue):**
- DRO uses binary rubric-gating for non-verifiable tasks (text-only) → directly overlaps
- But GR3 proves continuous gating is a **strict mathematical generalization** of binary gating with qualitatively different gradient properties
- Multiple papers show binary rewards/gates cause gradient vanishing, starvation, explosion
- This gives us a formal argument: continuous gating ≠ "just softening binary gating" — it eliminates provable gradient pathologies

**For landscape completeness:**
- 8 new papers identified and researched in detail
- POW3R shows static weights suboptimal → must add policy-aware variant
- rDPO is the closest multimodal rubric competitor (DPO not RL though)
- ClaimDiff-RL provides complementary claim-level decomposition approach

**For benchmark specification:**
- MMSci has 742K figures across 72 disciplines with reference captions from Nature Communications
- CIDEr scores are extremely low (0-3.73) → strong motivation for rubric-based evaluation
- Detailed re-annotation pipeline now available based on RubiCap/SciCapenter precedents

Waiting for the last agent on benchmark construction...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc8043da-5b5e-4956-ba94-a78006194632",
  "isSidechain": false,
  "requestId": "req_011CbUFz8ndKzs1HatZYYLHk",
  "type": "assistant",
  "uuid": "03e9cf01-7565-4f98-ad9c-314efa7327b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLzMhaW5PX6SF4qogRpAC9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4678,
      "cache_read_input_tokens": 46363,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 776,
          "cache_read_input_tokens": 46363,
          "cache_creation_input_tokens": 4678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4678
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

_source line 80_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "03e9cf01-7565-4f98-ad9c-314efa7327b0",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 82 · 2026-05-28T03:34:44.701Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T03:34:44.701Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "content": "&lt;task-notification>\n&lt;task-id>a2d0a8655cadac631&lt;/task-id>\n&lt;tool-use-id>toolu_01C68SLQUh7CfBHtNE13sSot&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a2d0a8655cadac631.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research scientific figure critique benchmarks\" completed&lt;/summary>\n&lt;result>Now I have comprehensive findings across all five areas. Let me compile the detailed report.\n\n---\n\nHere is a detailed synthesis of findings across your five research areas, organized to support a concrete benchmark construction pipeline.\n\n---\n\n## 1. Existing Scientific Figure Critique / Review Datasets\n\nSeveral benchmarks and datasets are directly relevant:\n\n**PRISMM-Bench** ([arXiv 2510.16505](https://arxiv.org/abs/2510.16505)) is the closest existing work to a \"figure critique\" benchmark. It contains 384 validated inconsistencies across 353 papers, mined from 18,009 ICLR open peer reviews. The construction pipeline has six stages: (1) collect reviews from OpenReview API focusing on rejected/withdrawn papers, (2) LLM-based filtering with Mistral Nemo to identify inconsistency mentions (yielded 6,056 candidates from 2,458 reviews), (3) manual verification with custom annotation tool, (4) LMM-based multiple-choice question generation via Gemini 2.5 Flash, (5) manual task refinement, (6) debiasing via structured JSON answer formats. It covers 15 inconsistency categories, with intra-figure inconsistencies (23.7%) and figure-text mismatches (21.9%) being most common. State-of-the-art models scored only 27.8-53.9%.\n\n**SIQA** ([arXiv 2603.06700](https://arxiv.org/html/2603.06700v1)) models scientific image quality along four dimensions: Scientific Validity, Scientific Completeness, Cognitive Clarity, and Disciplinary Conformity. It includes 2,240 benchmark images and 2,100 expert-annotated images. Annotators needed SRCC &gt; 0.8 with consensus to qualify. 17 STEM-credentialed annotators rated on 5-point scales with calibration testing, 60-minute session limits, and outlier rejection.\n\n**MMSci** ([arXiv 2407.04903](https://arxiv.org/abs/2407.04903)) covers 72 scientific fields from Nature Communications, with 131K articles and 742K figures (514K sub-figure/sub-caption pairs extracted via regex). Two benchmark tasks: figure captioning and multiple-choice QA.\n\n**ReviewBench** ([bioRxiv 2026](https://www.biorxiv.org/content/10.64898/2026.04.17.719279v1.full)) compares 145,021 human and AI review comments across CS, social science, and life science, evaluating structure, claim alignment, impact, and critique category.\n\n**Peer Review Analyze** ([PMC 8794172](https://pmc.ncbi.nlm.nih.gov/articles/PMC8794172/)) provides 1,199 ICLR 2018 reviews (~17,000 sentences) annotated across four layers: Section Correspondence, Aspect Category, Functionality, and Significance. Krippendorff's alpha: Layer 1 = 0.86, Layer 2 = 0.70, Layer 3 = 0.73, Layer 4 = 0.84.\n\n**SciCap** ([arXiv 2110.11624](https://arxiv.org/abs/2110.11624)) contains 2M+ figures from 290K CS arXiv papers (2010-2020), with 416K graph plots. This provides a large-scale figure extraction pipeline you could build on.\n\n---\n\n## 2. ArXiv Paper Selection Methodology\n\nThree benchmarks provide replicable paper selection pipelines:\n\n**CharXiv** ([arXiv 2406.18521](https://arxiv.org/abs/2406.18521), NeurIPS 2024): Downloaded all arXiv preprints across 8 academic subjects from Jan 2020 to Sep 2023. Figures extracted from source files and re-rendered to high-res JPEG (1024px long side). A four-step chart selection pipeline: (1) use pretrained SigLIP visual encoder to compute cosine similarity with MathVista chart embeddings (threshold &gt;= 0.65), (2-4) additional filtering and diversity promotion steps. Final: 2,323 charts, all handpicked and human-verified. Descriptive questions examine basic chart elements; reasoning questions require synthesizing across complex visual elements.\n\n**SciFIBench** ([arXiv 2405.08807](https://arxiv.org/abs/2405.08807), NeurIPS 2024): Drew from SciCap (~94K CS figure-caption pairs) and ArXivCap (32 arXiv categories). Key steps: (1) caption normalization and deduplication, (2) adversarial filtering using CLIP ViT-H-14-378-quickgelu embeddings -- concatenated text+image into 2048-dim vectors, built Faiss nearest-neighbor index, selected k-nearest neighbors as hard negative options, (3) similarity filtering to remove semantically identical pairs, (4) human verification -- sorted by difficulty, verified by domain experts, also filtered questions that GPT-4V and Gemini-Pro answered correctly. Final: 2,000 questions (1K CS, 1K General). Uncurated noise ~20-25%; after curation, \"at most a few percent.\"\n\n**MMSci**: Extracted all figures/captions from Nature Communications articles across 72 fields. Used regex matching to identify sub-figure indices, yielding 514K sub-figure/sub-caption pairs. This shows a venue-based (rather than arXiv-based) selection strategy.\n\n**Practical pipeline for your benchmark**: (1) Select arXiv categories and date range, (2) extract figures from source files (LaTeX compilation or PDF extraction), (3) classify figure types (use a visual encoder like SigLIP for filtering), (4) pair figures with captions and in-text references, (5) apply adversarial filtering for hard negatives, (6) human expert verification with quality threshold.\n\n---\n\n## 3. Rubric Dimensions for Evaluating Scientific Critiques\n\nSeveral frameworks provide concrete rubric dimension taxonomies:\n\n**SciFig's Six Rubric Dimensions** ([arXiv 2601.04390](https://arxiv.org/abs/2601.04390)) for scientific figure quality:\n- R1: Technical Accuracy and Correctness (scientific fidelity, mathematical consistency, algorithmic fidelity)\n- R2: Visual Clarity and Readability (component distinction, flow direction, visual hierarchy, text legibility, information density)\n- R3: Structural Coherence (logical progression, module boundaries, connection clarity, grouping)\n- R4: Design Consistency (visual language, notation, stylistic coherence, professional aesthetic)\n- R5: Interpretability and Accessibility (intuitive representation, self-containment, color accessibility, legend completeness)\n- R6: Technical Implementation Quality (vector graphics quality, typography, layout efficiency, resolution)\n\n**SIQA's Four Dimensions** ([arXiv 2603.06700](https://arxiv.org/html/2603.06700v1)):\n- Knowledge: Scientific Validity + Scientific Completeness\n- Perception: Cognitive Clarity + Disciplinary Conformity\n\n**Dr. SCI's Rubric Item Categories** ([arXiv 2602.08321](https://arxiv.org/html/2602.08321)) for open-ended scientific evaluation:\n- Essential: critical facts/steps; omission invalidates answer\n- Important: key information/reasoning; absence severely weakens response\n- Optional: secondary details\n- Pitfall: common vital mistakes that must be penalized\n- Average 14.5 rubric items per question (7-20 range)\n\n**VerAs** ([arXiv 2402.05224](https://arxiv.org/abs/2402.05224)) uses analytic rubrics with a 6-point scale for STEM lab reports, with separate verifier and assessment modules.\n\n**Rubrics as Rewards** ([arXiv 2507.17746](https://arxiv.org/abs/2507.17746)) rubric dimensions: factual accuracy, logical coherence, completeness, style, and safety, with 7-20 self-contained items per prompt, categorized as Essential/Important/Optional/Pitfall.\n\n**For your figure critique benchmark**, a synthesis rubric might include: (1) Identification accuracy -- correctly spotting issues, (2) Scientific reasoning quality -- explanation of why it's problematic, (3) Completeness -- covering all relevant issues, (4) Specificity -- pointing to exact visual elements, (5) Constructive suggestion quality -- actionable improvement recommendations, (6) Domain knowledge demonstration.\n\n---\n\n## 4. RL Training Dataset Sizes\n\nConcrete numbers from the literature:\n\n| System | Training Size | Task Domain | Notes |\n|--------|-------------|-------------|-------|\n| **Rubrics as Rewards (RaR)** | ~20K prompts each for RaR-Medicine and RaR-Science | Medical + science reasoning | 7.5 avg rubrics/question; GRPO with Qwen2.5-7B; 300 train steps |\n| **Self-Rewarding Rubric RL** | 4,000 samples (HealthBench Easy subset) | Medical reasoning | Sufficient to exceed GPT-5 on HealthBench Hard |\n| **RL with Rubric Anchors** | 5K+ samples | Open-ended (humanities) | Qwen-30B-A3B outperformed 671B DeepSeek-V3 |\n| **Dr. SCI** | 1M SFT examples; 461K verifiable + 545K open-ended for RL | STEM scientific reasoning | Dynamic difficulty curriculum; 4B model |\n| **InstructGPT** | Hundreds of thousands of comparisons | General RLHF | Full reward model training |\n| **General RLHF** | ~50K labeled preference samples (typical) | Various | Rule-of-thumb baseline |\n| **RubiCap** | ~3.5M images (COCO118K + BLIP558K + CC3M) | Dense image captioning | Vision domain; much larger scale |\n\n**Key findings on minimum sizes**:\n- Rubric-based RL can be effective with as few as **4,000-5,000 samples** for domain-specific tasks\n- **20K prompts** is a robust working point for rubric-RL systems\n- For reward model training: prioritize **prompt diversity** over multiple responses per prompt\n- For policy training: \"moderate size and high-quality prompts\" with 4-8 responses sampled per prompt\n- **Scaling finding**: RLHF scales less efficiently than pretraining; beyond a threshold, adding more data yields diminishing returns (from \"Does RLHF Scale?\" [arXiv 2412.06000](https://arxiv.org/abs/2412.06000))\n\n---\n\n## 5. Inter-Annotator Agreement Standards\n\n**Accepted thresholds** (from Krippendorff's methodology and standard practice):\n- **Krippendorff's alpha &gt;= 0.80**: satisfactory agreement, acceptable for production/conclusions\n- **alpha 0.67-0.79**: moderate agreement, tentative conclusions only\n- **alpha &lt; 0.67**: unreliable, not suitable for drawing conclusions\n- **Clinical/high-stakes**: alpha &gt; 0.90 often required\n\n**Reported values from relevant scientific evaluation benchmarks**:\n- Peer Review Analyze: alpha = 0.70 to 0.86 across four annotation layers (with Section Correspondence at 0.86 and Aspect Category at 0.70)\n- SIQA: Required SRCC &gt; 0.80 as annotator qualification threshold\n- Cohen's kappa &gt;= 0.82 achieved in complex NLP classification tasks\n\n**Best practices for your benchmark**:\n- Use **Krippendorff's alpha** (handles multiple annotators, ordinal data, missing values)\n- Calculate IAA **separately per rubric dimension** rather than averaging across dimensions\n- Use **calibration rounds** (SIQA used 30 calibration images; Peer Review Analyze had a 2-month training phase)\n- Enforce **session time limits** to prevent fatigue (SIQA: 60-minute sessions with rest)\n- Apply **outlier rejection** post-annotation\n- Target alpha &gt;= 0.80 for final benchmark dimensions; flag any dimension below 0.67 for redesign\n- For ordinal rubric scales, weighted kappa or ICC may be more appropriate than unweighted kappa\n\n---\n\n## Recommended Benchmark Construction Pipeline\n\nBased on this research, a concrete pipeline would be:\n\n1. **Paper/Figure Collection**: Select arXiv categories + date range; extract figures from source files (SciCap-style pipeline scales to 290K+ papers); filter figure types using SigLIP visual encoder (CharXiv approach, cosine similarity &gt;= 0.65)\n2. **Critique Collection**: Either mine open peer reviews (PRISMM-Bench approach via OpenReview API) or commission expert annotations with structured rubrics\n3. **Rubric Design**: 6-8 dimensions (adapt SciFig/SIQA frameworks); 5-point or 6-point ordinal scales; Essential/Important/Optional/Pitfall weighting (Dr. SCI approach); target 7-20 rubric items per figure\n4. **Annotation**: 3+ annotators per item; 2-month calibration phase; 60-min sessions; require Krippendorff's alpha &gt;= 0.80 per dimension\n5. **Dataset Size**: For RL training, target **5K-20K** annotated figure critiques as a working range (4K minimum demonstrated effective for rubric-RL; 20K is a robust target)\n6. **Quality Control**: Adversarial filtering (SciFIBench CLIP-based approach); structured JSON outputs to minimize linguistic bias (PRISMM-Bench); human verification with noise below 5%\n7. **RL Training**: Use GRPO with rubric-weighted rewards; sample 4-8 responses per prompt; prioritize prompt diversity over response count\n\nSources:\n- [PRISMM-Bench](https://arxiv.org/abs/2510.16505)\n- [SIQA](https://arxiv.org/html/2603.06700v1)\n- [MMSci](https://arxiv.org/abs/2407.04903)\n- [ReviewBench](https://www.biorxiv.org/content/10.64898/2026.04.17.719279v1.full)\n- [Peer Review Analyze](https://pmc.ncbi.nlm.nih.gov/articles/PMC8794172/)\n- [SciCap](https://arxiv.org/abs/2110.11624)\n- [CharXiv](https://arxiv.org/abs/2406.18521)\n- [SciFIBench](https://arxiv.org/abs/2405.08807)\n- [SciFig](https://arxiv.org/abs/2601.04390)\n- [VerAs](https://arxiv.org/abs/2402.05224)\n- [Rubrics as Rewards](https://arxiv.org/abs/2507.17746)\n- [Self-Rewarding Rubric RL](https://arxiv.org/abs/2509.25534)\n- [RL with Rubric Anchors](https://arxiv.org/abs/2508.12790)\n- [Dr. SCI](https://arxiv.org/html/2602.08321)\n- [Does RLHF Scale?](https://arxiv.org/abs/2412.06000)\n- [OpenRubrics](https://arxiv.org/abs/2510.07743)\n- [RubricHub](https://arxiv.org/html/2601.08430v1)\n- [RubiCap](https://arxiv.org/abs/2603.09160)\n- [Krippendorff's Alpha methodology](https://www.k-alpha.org/methodological-notes)\n- [Counting on Consensus: IAA metrics](https://arxiv.org/html/2603.06865)\n- [M.E.D.V.I.S. figure scoring](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0336917)&lt;/result>\n&lt;usage>&lt;total_tokens>42646&lt;/total_tokens>&lt;tool_uses>44&lt;/tool_uses>&lt;duration_ms>535178&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 83 · 2026-05-28T03:34:44.777Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T03:34:44.777Z",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

## Round 9

30 recorded events

### User

_source line 84 · 2026-05-28T03:34:44.784Z_

&lt;task-notification>
&lt;task-id>a2d0a8655cadac631&lt;/task-id>
&lt;tool-use-id>toolu_01C68SLQUh7CfBHtNE13sSot&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tasks/a2d0a8655cadac631.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research scientific figure critique benchmarks" completed&lt;/summary>
&lt;result>Now I have comprehensive findings across all five areas. Let me compile the detailed report.

---

Here is a detailed synthesis of findings across your five research areas, organized to support a concrete benchmark construction pipeline.

---

## 1. Existing Scientific Figure Critique / Review Datasets

Several benchmarks and datasets are directly relevant:

**PRISMM-Bench** ([arXiv 2510.16505](https://arxiv.org/abs/2510.16505)) is the closest existing work to a "figure critique" benchmark. It contains 384 validated inconsistencies across 353 papers, mined from 18,009 ICLR open peer reviews. The construction pipeline has six stages: (1) collect reviews from OpenReview API focusing on rejected/withdrawn papers, (2) LLM-based filtering with Mistral Nemo to identify inconsistency mentions (yielded 6,056 candidates from 2,458 reviews), (3) manual verification with custom annotation tool, (4) LMM-based multiple-choice question generation via Gemini 2.5 Flash, (5) manual task refinement, (6) debiasing via structured JSON answer formats. It covers 15 inconsistency categories, with intra-figure inconsistencies (23.7%) and figure-text mismatches (21.9%) being most common. State-of-the-art models scored only 27.8-53.9%.

**SIQA** ([arXiv 2603.06700](https://arxiv.org/html/2603.06700v1)) models scientific image quality along four dimensions: Scientific Validity, Scientific Completeness, Cognitive Clarity, and Disciplinary Conformity. It includes 2,240 benchmark images and 2,100 expert-annotated images. Annotators needed SRCC &gt; 0.8 with consensus to qualify. 17 STEM-credentialed annotators rated on 5-point scales with calibration testing, 60-minute session limits, and outlier rejection.

**MMSci** ([arXiv 2407.04903](https://arxiv.org/abs/2407.04903)) covers 72 scientific fields from Nature Communications, with 131K articles and 742K figures (514K sub-figure/sub-caption pairs extracted via regex). Two benchmark tasks: figure captioning and multiple-choice QA.

**ReviewBench** ([bioRxiv 2026](https://www.biorxiv.org/content/10.64898/2026.04.17.719279v1.full)) compares 145,021 human and AI review comments across CS, social science, and life science, evaluating structure, claim alignment, impact, and critique category.

**Peer Review Analyze** ([PMC 8794172](https://pmc.ncbi.nlm.nih.gov/articles/PMC8794172/)) provides 1,199 ICLR 2018 reviews (~17,000 sentences) annotated across four layers: Section Correspondence, Aspect Category, Functionality, and Significance. Krippendorff's alpha: Layer 1 = 0.86, Layer 2 = 0.70, Layer 3 = 0.73, Layer 4 = 0.84.

**SciCap** ([arXiv 2110.11624](https://arxiv.org/abs/2110.11624)) contains 2M+ figures from 290K CS arXiv papers (2010-2020), with 416K graph plots. This provides a large-scale figure extraction pipeline you could build on.

---

## 2. ArXiv Paper Selection Methodology

Three benchmarks provide replicable paper selection pipelines:

**CharXiv** ([arXiv 2406.18521](https://arxiv.org/abs/2406.18521), NeurIPS 2024): Downloaded all arXiv preprints across 8 academic subjects from Jan 2020 to Sep 2023. Figures extracted from source files and re-rendered to high-res JPEG (1024px long side). A four-step chart selection pipeline: (1) use pretrained SigLIP visual encoder to compute cosine similarity with MathVista chart embeddings (threshold &gt;= 0.65), (2-4) additional filtering and diversity promotion steps. Final: 2,323 charts, all handpicked and human-verified. Descriptive questions examine basic chart elements; reasoning questions require synthesizing across complex visual elements.

**SciFIBench** ([arXiv 2405.08807](https://arxiv.org/abs/2405.08807), NeurIPS 2024): Drew from SciCap (~94K CS figure-caption pairs) and ArXivCap (32 arXiv categories). Key steps: (1) caption normalization and deduplication, (2) adversarial filtering using CLIP ViT-H-14-378-quickgelu embeddings -- concatenated text+image into 2048-dim vectors, built Faiss nearest-neighbor index, selected k-nearest neighbors as hard negative options, (3) similarity filtering to remove semantically identical pairs, (4) human verification -- sorted by difficulty, verified by domain experts, also filtered questions that GPT-4V and Gemini-Pro answered correctly. Final: 2,000 questions (1K CS, 1K General). Uncurated noise ~20-25%; after curation, "at most a few percent."

**MMSci**: Extracted all figures/captions from Nature Communications articles across 72 fields. Used regex matching to identify sub-figure indices, yielding 514K sub-figure/sub-caption pairs. This shows a venue-based (rather than arXiv-based) selection strategy.

**Practical pipeline for your benchmark**: (1) Select arXiv categories and date range, (2) extract figures from source files (LaTeX compilation or PDF extraction), (3) classify figure types (use a visual encoder like SigLIP for filtering), (4) pair figures with captions and in-text references, (5) apply adversarial filtering for hard negatives, (6) human expert verification with quality threshold.

---

## 3. Rubric Dimensions for Evaluating Scientific Critiques

Several frameworks provide concrete rubric dimension taxonomies:

**SciFig's Six Rubric Dimensions** ([arXiv 2601.04390](https://arxiv.org/abs/2601.04390)) for scientific figure quality:
- R1: Technical Accuracy and Correctness (scientific fidelity, mathematical consistency, algorithmic fidelity)
- R2: Visual Clarity and Readability (component distinction, flow direction, visual hierarchy, text legibility, information density)
- R3: Structural Coherence (logical progression, module boundaries, connection clarity, grouping)
- R4: Design Consistency (visual language, notation, stylistic coherence, professional aesthetic)
- R5: Interpretability and Accessibility (intuitive representation, self-containment, color accessibility, legend completeness)
- R6: Technical Implementation Quality (vector graphics quality, typography, layout efficiency, resolution)

**SIQA's Four Dimensions** ([arXiv 2603.06700](https://arxiv.org/html/2603.06700v1)):
- Knowledge: Scientific Validity + Scientific Completeness
- Perception: Cognitive Clarity + Disciplinary Conformity

**Dr. SCI's Rubric Item Categories** ([arXiv 2602.08321](https://arxiv.org/html/2602.08321)) for open-ended scientific evaluation:
- Essential: critical facts/steps; omission invalidates answer
- Important: key information/reasoning; absence severely weakens response
- Optional: secondary details
- Pitfall: common vital mistakes that must be penalized
- Average 14.5 rubric items per question (7-20 range)

**VerAs** ([arXiv 2402.05224](https://arxiv.org/abs/2402.05224)) uses analytic rubrics with a 6-point scale for STEM lab reports, with separate verifier and assessment modules.

**Rubrics as Rewards** ([arXiv 2507.17746](https://arxiv.org/abs/2507.17746)) rubric dimensions: factual accuracy, logical coherence, completeness, style, and safety, with 7-20 self-contained items per prompt, categorized as Essential/Important/Optional/Pitfall.

**For your figure critique benchmark**, a synthesis rubric might include: (1) Identification accuracy -- correctly spotting issues, (2) Scientific reasoning quality -- explanation of why it's problematic, (3) Completeness -- covering all relevant issues, (4) Specificity -- pointing to exact visual elements, (5) Constructive suggestion quality -- actionable improvement recommendations, (6) Domain knowledge demonstration.

---

## 4. RL Training Dataset Sizes

Concrete numbers from the literature:

| System | Training Size | Task Domain | Notes |
|--------|-------------|-------------|-------|
| **Rubrics as Rewards (RaR)** | ~20K prompts each for RaR-Medicine and RaR-Science | Medical + science reasoning | 7.5 avg rubrics/question; GRPO with Qwen2.5-7B; 300 train steps |
| **Self-Rewarding Rubric RL** | 4,000 samples (HealthBench Easy subset) | Medical reasoning | Sufficient to exceed GPT-5 on HealthBench Hard |
| **RL with Rubric Anchors** | 5K+ samples | Open-ended (humanities) | Qwen-30B-A3B outperformed 671B DeepSeek-V3 |
| **Dr. SCI** | 1M SFT examples; 461K verifiable + 545K open-ended for RL | STEM scientific reasoning | Dynamic difficulty curriculum; 4B model |
| **InstructGPT** | Hundreds of thousands of comparisons | General RLHF | Full reward model training |
| **General RLHF** | ~50K labeled preference samples (typical) | Various | Rule-of-thumb baseline |
| **RubiCap** | ~3.5M images (COCO118K + BLIP558K + CC3M) | Dense image captioning | Vision domain; much larger scale |

**Key findings on minimum sizes**:
- Rubric-based RL can be effective with as few as **4,000-5,000 samples** for domain-specific tasks
- **20K prompts** is a robust working point for rubric-RL systems
- For reward model training: prioritize **prompt diversity** over multiple responses per prompt
- For policy training: "moderate size and high-quality prompts" with 4-8 responses sampled per prompt
- **Scaling finding**: RLHF scales less efficiently than pretraining; beyond a threshold, adding more data yields diminishing returns (from "Does RLHF Scale?" [arXiv 2412.06000](https://arxiv.org/abs/2412.06000))

---

## 5. Inter-Annotator Agreement Standards

**Accepted thresholds** (from Krippendorff's methodology and standard practice):
- **Krippendorff's alpha &gt;= 0.80**: satisfactory agreement, acceptable for production/conclusions
- **alpha 0.67-0.79**: moderate agreement, tentative conclusions only
- **alpha &lt; 0.67**: unreliable, not suitable for drawing conclusions
- **Clinical/high-stakes**: alpha &gt; 0.90 often required

**Reported values from relevant scientific evaluation benchmarks**:
- Peer Review Analyze: alpha = 0.70 to 0.86 across four annotation layers (with Section Correspondence at 0.86 and Aspect Category at 0.70)
- SIQA: Required SRCC &gt; 0.80 as annotator qualification threshold
- Cohen's kappa &gt;= 0.82 achieved in complex NLP classification tasks

**Best practices for your benchmark**:
- Use **Krippendorff's alpha** (handles multiple annotators, ordinal data, missing values)
- Calculate IAA **separately per rubric dimension** rather than averaging across dimensions
- Use **calibration rounds** (SIQA used 30 calibration images; Peer Review Analyze had a 2-month training phase)
- Enforce **session time limits** to prevent fatigue (SIQA: 60-minute sessions with rest)
- Apply **outlier rejection** post-annotation
- Target alpha &gt;= 0.80 for final benchmark dimensions; flag any dimension below 0.67 for redesign
- For ordinal rubric scales, weighted kappa or ICC may be more appropriate than unweighted kappa

---

## Recommended Benchmark Construction Pipeline

Based on this research, a concrete pipeline would be:

1. **Paper/Figure Collection**: Select arXiv categories + date range; extract figures from source files (SciCap-style pipeline scales to 290K+ papers); filter figure types using SigLIP visual encoder (CharXiv approach, cosine similarity &gt;= 0.65)
2. **Critique Collection**: Either mine open peer reviews (PRISMM-Bench approach via OpenReview API) or commission expert annotations with structured rubrics
3. **Rubric Design**: 6-8 dimensions (adapt SciFig/SIQA frameworks); 5-point or 6-point ordinal scales; Essential/Important/Optional/Pitfall weighting (Dr. SCI approach); target 7-20 rubric items per figure
4. **Annotation**: 3+ annotators per item; 2-month calibration phase; 60-min sessions; require Krippendorff's alpha &gt;= 0.80 per dimension
5. **Dataset Size**: For RL training, target **5K-20K** annotated figure critiques as a working range (4K minimum demonstrated effective for rubric-RL; 20K is a robust target)
6. **Quality Control**: Adversarial filtering (SciFIBench CLIP-based approach); structured JSON outputs to minimize linguistic bias (PRISMM-Bench); human verification with noise below 5%
7. **RL Training**: Use GRPO with rubric-weighted rewards; sample 4-8 responses per prompt; prioritize prompt diversity over response count

Sources:
- [PRISMM-Bench](https://arxiv.org/abs/2510.16505)
- [SIQA](https://arxiv.org/html/2603.06700v1)
- [MMSci](https://arxiv.org/abs/2407.04903)
- [ReviewBench](https://www.biorxiv.org/content/10.64898/2026.04.17.719279v1.full)
- [Peer Review Analyze](https://pmc.ncbi.nlm.nih.gov/articles/PMC8794172/)
- [SciCap](https://arxiv.org/abs/2110.11624)
- [CharXiv](https://arxiv.org/abs/2406.18521)
- [SciFIBench](https://arxiv.org/abs/2405.08807)
- [SciFig](https://arxiv.org/abs/2601.04390)
- [VerAs](https://arxiv.org/abs/2402.05224)
- [Rubrics as Rewards](https://arxiv.org/abs/2507.17746)
- [Self-Rewarding Rubric RL](https://arxiv.org/abs/2509.25534)
- [RL with Rubric Anchors](https://arxiv.org/abs/2508.12790)
- [Dr. SCI](https://arxiv.org/html/2602.08321)
- [Does RLHF Scale?](https://arxiv.org/abs/2412.06000)
- [OpenRubrics](https://arxiv.org/abs/2510.07743)
- [RubricHub](https://arxiv.org/html/2601.08430v1)
- [RubiCap](https://arxiv.org/abs/2603.09160)
- [Krippendorff's Alpha methodology](https://www.k-alpha.org/methodological-notes)
- [Counting on Consensus: IAA metrics](https://arxiv.org/html/2603.06865)
- [M.E.D.V.I.S. figure scoring](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0336917)&lt;/result>
&lt;usage>&lt;total_tokens>42646&lt;/total_tokens>&lt;tool_uses>44&lt;/tool_uses>&lt;duration_ms>535178&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03e9cf01-7565-4f98-ad9c-314efa7327b0",
  "isSidechain": false,
  "promptId": "d0628049-5dd6-44e2-863d-4e5f7a82f317",
  "type": "user",
  "uuid": "ca26bdba-48a7-4d3e-b1cb-9427710067d0",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 85 · 2026-05-28T03:34:44.784Z_

```json
{
  "parentUuid": "ca26bdba-48a7-4d3e-b1cb-9427710067d0",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f9e11f86-9fe6-4763-8186-a19bf8f7e82a",
  "timestamp": "2026-05-28T03:34:44.784Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 86 · 2026-05-28T03:36:54.580Z_

<details><summary>Logged reasoning block</summary>

```text
All 8 research agents have now completed. Let me synthesize all findings and produce the revised idea.

Let me think deeply about each reviewer issue and how the research findings inform the revision:

## Issue 1: 8 missing concurrent works
Now fully researched:
1. **DRO** - Binary rubric-gating for non-verifiable text tasks. Directly overlaps "gating for non-verifiable" concept. Uses hard accept/reject at group level.
2. **Training AI Co-Scientists** - Rubric RL (GRPO) for scientific research plans. Text-only. Instance-specific rubrics from papers. Shows reward overoptimization.


3. **Reward Hacking in Rubric-Based RL** - Identifies three exploitation patterns in medical and scientific domains, revealing a self-internalization gap that validates my anti-hacking motivation but suggests gating alone won't fully solve the problem.
4. **ARES** - Automated rubric synthesis from documents at scale with 101K instances, text-only approach.
5. **Perception-R1** - Visual perception reward mechanism in RLVR framework, verifiable with composite reward structure.
6. **ClaimDiff-RL** - Claim-level captioning with graded severity scoring, bridging verifiable and non-verifiable reward spaces.
7. **POW3R** - Policy-aware dynamic rubric approach...
8. **rDPO** - Instance-specific rubrics for multimodal DPO distinguishing essential from additional criteria.

Now looking at the continuous versus binary gating research—GR3 provides the mathematical foundation showing continuous multiplicative gating strictly generalizes binary gating, while binary approaches like DRO and PaLMR suffer from provable gradient pathologies including vanishing, starvation, and explosion. PEPO demonstrates smooth gating works in multimodal RL with quantifiable improvements: 10x speedup and 45-point accuracy gains. This reframes my novelty contribution around the theoretical advantage that continuous gating eliminates gradient failure modes binary gating cannot avoid.

The architectural contribution is combining continuous gating with multimodal reasoning and non-verifiable scientific tasks while adapting weights based on policy performance. I'll include comprehensive ablations with binary gating as a baseline to validate the approach empirically.

For the benchmark, I'm finding that existing datasets like PRISMM-Bench (384 inconsistencies mined from ICLR reviews), SIQA (2,240 scientific image assessments), and SciCap (2M+ figures from 290K papers) provide precedent and scale. Rubric RL needs at least 4K-5K samples to be effective, with 20K providing robustness, so I should expand beyond 2K as the reviewer suggested and draw detailed rubric dimensions from these sources.

On the MMSci re-annotation front, I'm looking at 742K figures across 72 disciplines with Nature Communications reference captions. The CIDEr scores are extremely low (0-3.73), which strongly motivates the work. I can use the RubiCap pipeline as a template and SciCapenter's 6-dimension checklist to build a 7-dimension rubric with severity weighting.

For reward design, I need to acknowledge that rubric rewards do improve reasoning quality even in verifiable settings, then argue that gating provides additional value specifically in non-verifiable regimes. I should also add a POW3R-style policy-aware weight variant to the ablation suite—or potentially make it a core enhancement rather than just an ablation.

Now I'm deciding whether this requires a major revision or just careful integration of these pieces.

This is actually a major revision. The novelty needs to shift from "domain extension" to "continuous gating as a principled generalization with provable advantages." I need to expand the related work substantially, enhance the approach with policy-aware weight adaptation and self-internalization gap monitoring, grow the benchmark from 2K to 5K+ examples with detailed specifications, and add a DRO-style binary gating baseline to the ablations.

The core insight is that continuous multiplicative gating is a strict mathematical generalization of binary gating, which reframes the entire contribution.

Now I'm clarifying why this matters: binary gating introduces discontinuities that break Lipschitz continuity and cause gradient vanishing, while continuous gating provides smooth curriculum transitions. The novelty isn't just applying gating to scientific reasoning—it's showing that continuous gating is the principled generalization when rewards are inherently graded rather than binary, and that visual grounding in scientific reasoning is naturally graded rather than all-or-nothing. I'm also planning to add policy-aware adaptive gating that adjusts gate weights based on the policy's current performance.

To strengthen this, I should replace the fixed thresholds with adaptive ones inspired by POW3R, add claim-level decomposition for the first tier, monitor the self-internalization gap to catch reward hacking, expand the baselines to include DRO-style binary gating for direct comparison, and scale the benchmark to 5K+ examples with a detailed construction pipeline. The reward formula itself needs to shift from binary gates to a continuous formulation.

Instead of hard thresholds that create gradient discontinuities, I'll use sigmoid gates with a temperature parameter that smoothly transitions between rewards while preserving Lipschitz continuity and enabling curriculum learning. As temperature approaches zero, this naturally reduces to the original binary gating, so it's a strict generalization. The key insight is that the original formula already used continuous reward values—I just need to replace those binary indicator functions with smooth sigmoid gates, which aligns with what GR3 advocates. Now I'm considering whether to layer POW3R-style adaptive weighting on top of this.

I think the stronger approach is to make adaptive weighting a core variant rather than just an ablation. So the proposal splits into a base version with smooth continuous gating and an extended version that adds policy-aware adaptive weights and thresholds. Then the ablation suite systematically tests flat composites, binary gating at the group level, binarized visual gates, dynamic weighting, policy-aware weighting without gating, and various tier combinations to isolate which components drive the improvements.

The ablations should demonstrate that continuous gating outperforms binary approaches, which both beat flat composites, and that combining continuous gating with policy-aware weighting beats either strategy alone. For the benchmark, I'm defining SciCritique-5K by extracting figures from recent ArXiv papers across five STEM domains, using LaTeX compilation and visual filtering to get clean figure data, then generating critiques through a multi-model ensemble for diversity. The rubric has eight dimensions covering visual accuracy through constructive suggestions, each rated on a five-point scale with a binary critical flag.

For validation, I'm weighting severity levels and having three annotators evaluate a thousand items to reach strong inter-rater agreement. I'm also planning to re-annotate a stratified sample of ten thousand figures from the broader corpus using a seven-dimension rubric that breaks down reference captions into atomic components.

The teacher committee approach uses multiple VLMs to generate alternative captions for consensus, and I'm targeting expert validation across PhD-annotated domains with a Cohen's kappa threshold of 0.70. The core motivation is that existing reference-based metrics like CIDEr show limited range across models, suggesting they're fundamentally inadequate for this task.

Now I'm drafting the complete JSON structure and reconsidering the changes summary—integrating all the related works I found and reframing the continuous gating mechanism as a principled generalization approach.

I've addressed the major issues: expanded the benchmark from 2K to 5K with a detailed construction pipeline, specified the 7-dimension rubric with the teacher committee calibration protocol, clarified that rubric rewards work in verifiable settings while gating provides anti-degeneracy value in non-verifiable regimes, and elevated the policy-aware adaptive variant as a core enhancement rather than just an ablation.

For venue timing, AAAI 2027 is tight at about two months away, while WACV 2027 Round 2 gives me roughly three months.

Generating the paper JSON... I'm working through the benchmark specifications and re-annotation framework now — the 5K SciCritique dataset with detailed evaluation criteria and the expanded MMSci rubric across seven dimensions. But I need to address the core novelty concern more directly: continuous gating isn't just softening binary indicators, it's a mathematically principled approach that avoids gradient pathologies that binary methods suffer from. The real distinction is that combining continuous gating with multimodal scientific reasoning creates fundamentally different optimization dynamics than text-only settings, which is where the technical contribution actually lies. the gradient landscape and gradient starvation literature, continuous gating outperforms binary approaches. The epistemic dependency structure in scientific visual reasoning—where perception must precede structural analysis and reasoning—naturally aligns with hierarchical continuous gating, making this a principled rather than ad-hoc design choice. Combined with policy-aware adaptation and anti-hacking safeguards, this positions the work as a formal generalization grounded in domain-specific constraints rather than just applying existing techniques to a new setting.

Now I'm working through the resource requirements for the expanded scope—the annotation costs scale with the larger benchmark, and the ablation study has grown to eight conditions, which drives up the GPU hours needed for training and evaluation. I'm recalculating the annotation costs more carefully—1K items with three annotators at 30 minutes each gives 1500 person-hours for SciCritique, plus 500 person-hours for MMSci rubric validation, which totals around 2000 person-hours or roughly $40K at expert rates. That's significantly higher than my initial estimate, so I need to reconsider the validation scope.

Let me be more pragmatic: validating just 20% of the 5K benchmark with expert annotators brings it down to 1K items, which with calibration overhead comes to around 600-700 person-hours for SciCritique, plus 375 person-hours for the MMSci re-annotation validation, totaling 700-800 person-hours or $15-18K at PhD student rates.

Now I'm thinking about whether to incorporate ARES-style automated rubric generation into the pipeline, since that approach could help scale rubric creation for MMSci without requiring as much manual effort.

I could also apply ClaimDiff-RL's claim decomposition strategy to Tier-1 validation—breaking down visual responses into atomic claims and checking each one rather than just verifying overall visual elements.

For the gating mechanism, I'm working through a sigmoid formulation with temperature scaling that gates each tier's contribution based on the previous tier's performance, creating a smooth transition where lower tiers only activate when higher tiers meet a threshold.

Exploring a multiplicative rescaling variant inspired by GR3 that normalizes contributions relative to the base response...

actually, that's overcomplicating things. The additive formulation with sigmoid gates is cleaner: each reward component gets weighted by smooth gate functions that depend on whether previous components exceeded their thresholds, and these gates smoothly interpolate between binary hard gating and flat weighting depending on the temperature parameter. For an adaptive version, I can make the weights themselves time-dependent to create a curriculum effect during training.

This feels like a solid direction. Now I need to write out the full JSON specification, and I'm thinking the change_type should be "major" since we're fundamentally shifting from domain extension to principled generalization, moving from binary to continuous gating, introducing policy-aware adaptation, and expanding the benchmark significantly.

Before I finalize everything, I should reconsider the title—the original phrasing was too formulaic. Something like "Continuous Hierarchical Gating for Non-Verifiable Multimodal Scientific Reasoning" or "Smooth-Gated Rubric Rewards for Non-Verifiable Multimodal Scientific Reasoning" would better highlight the core innovation around continuous gating rather than just applying an existing method to a new domain.

Now I need to compile the references, which will be substantial—pulling from the original 25 plus the eight papers the reviewer suggested, plus another eight to ten from my own research on related topics like gate functions and gradient dynamics. I'll be selective and prioritize the most relevant ones for the final JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9e11f86-9fe6-4763-8186-a19bf8f7e82a",
  "isSidechain": false,
  "requestId": "req_011CbUGLZbS7PNwWJnqRvAQA",
  "type": "assistant",
  "uuid": "ab969ca3-7ca1-446c-ac8b-33ddb567fff8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2LTu3o3txpiXjDTSAFkz7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5045,
      "cache_read_input_tokens": 51041,
      "output_tokens": 16655,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 16655,
          "cache_read_input_tokens": 51041,
          "cache_creation_input_tokens": 5045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5045
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

_source line 87 · 2026-05-28T03:36:54.582Z_

All 8 research agents have completed. I now have comprehensive findings on every issue. Let me synthesize everything and produce the complete revised idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab969ca3-7ca1-446c-ac8b-33ddb567fff8",
  "isSidechain": false,
  "requestId": "req_011CbUGLZbS7PNwWJnqRvAQA",
  "type": "assistant",
  "uuid": "f06159a2-f2d1-492d-bf2b-8548c277f8ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2LTu3o3txpiXjDTSAFkz7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5045,
      "cache_read_input_tokens": 51041,
      "output_tokens": 16655,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 16655,
          "cache_read_input_tokens": 51041,
          "cache_creation_input_tokens": 5045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5045
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

_source line 88 · 2026-05-28T03:40:51.202Z_

<details open><summary>🔧 Tool call — Write · `toolu_014dLvpbwUWuuXJTS848CCuy`</summary>

```json
{
  "file_path": "/home/ubuntu/idea-review/revised_idea_r3.json",
  "content": "{\n  \"title\": \"GatedRubric-GRPO: Smooth Hierarchical Gating for Non-Verifiable Multimodal Scientific Reasoning\",\n  \"core_problem\": \"Reinforcement learning with structured rewards has advanced rapidly across two axes: (1) gated/hierarchical rewards for verifiable multimodal tasks (PaLMR, PEARL, CogFlow use binary visual gates; SR-MCR uses flat multi-component rewards), and (2) rubric-based RL for non-verifiable tasks in text-only settings (DRO uses binary rubric-gates as feasibility constraints; Rubric-ARM alternates rubric generator and judge; Training AI Co-Scientists applies rubric RL to scientific plan generation; ARES automates rubric synthesis at scale; RubricEM decomposes policy via rubrics). RubiCap extends rubric RL to non-verifiable multimodal captioning, while rDPO applies instance-specific rubrics for multimodal DPO with essential/additional criteria gating. However, ALL existing gating mechanisms — whether for visual fidelity (PaLMR), rubric feasibility (DRO), or essential criteria qualification (rDPO) — employ BINARY gates: hard accept/reject, yes/no, pass/fail. This creates a critical technical limitation: binary gating introduces discontinuities in the reward landscape that provably cause gradient vanishing and gradient starvation in policy optimization (demonstrated formally by Razin et al. ICLR 2024, and empirically by gradient starvation analysis in GRPO). The problem is especially acute for non-verifiable scientific visual reasoning — tasks like scientific figure explanation, graph-based analytical interpretation, and figure critique — where both visual grounding quality and reasoning quality are INHERENTLY CONTINUOUS and GRADED, not binary. A figure can be 70% correctly perceived; a scientific explanation can be partially valid. Binary gating discards this graded signal.\",\n  \"opportunity\": \"The landscape reveals a precise technical gap at the intersection of three established directions. Direction 1: Gated multimodal rewards exist (PaLMR, PEARL, CogFlow) but use binary gates on verifiable tasks. Direction 2: Rubric-gated non-verifiable RL exists (DRO uses binary rubric-gates as group-level feasibility constraints) but is text-only. Direction 3: Non-verifiable multimodal rubric RL exists (RubiCap for captioning, rDPO for visual preference) but without hierarchical gating. The crucial insight combines two observations: (A) Scientific visual reasoning exhibits an epistemic dependency — visual grounding is a NECESSARY CONDITION for valid reasoning (you cannot produce a correct explanation of a misperceived figure) — creating a natural gating hierarchy. (B) GR3 (arXiv:2603.10535) formally proves that continuous multiplicative gating is a STRICT MATHEMATICAL GENERALIZATION of binary gating: they are equivalent when rewards are binary, but continuous gating is provably superior when rewards are graded, because it preserves Lipschitz continuity of the reward landscape and eliminates gradient dead zones. This means continuous gating is not merely 'softening' binary gates — it enables qualitatively different training dynamics. The convergence of these observations motivates smooth-gated rubric rewards: where DRO uses binary rubric-gates (yes/no feasibility constraints) and PaLMR uses binary visual gates (pass/fail fidelity checks), we introduce smooth sigmoid gates that (1) preserve the epistemic dependency structure, (2) maintain differentiable gradient flow, and (3) naturally encode a continuous curriculum from perception to reasoning. Additionally, POW3R (arXiv:2605.20164) demonstrates that static rubric weights are suboptimal because important criteria can be saturated or unreachable at different training stages — motivating policy-aware adaptive gating. And 'Reward Hacking in Rubric-Based RL' (arXiv:2605.12474) reveals systematic exploitation patterns in rubric rewards for scientific/medical domains — motivating our integration of the self-internalization gap as a training diagnostic. Importantly, we acknowledge (per 'Reward Design for Physical Reasoning in VLMs', arXiv:2604.13993) that rubric rewards DO provide reasoning quality benefits even in verifiable settings — accuracy rewards and rubric rewards capture DIFFERENT value. In non-verifiable settings where accuracy is unavailable, rubric rewards become the primary signal, and gating's additional value is preventing the specific failure mode of visually ungrounded but linguistically polished explanations — the 'eloquent hallucination' pattern that Reward Hacking in Rubric-Based RL documents as 'topical alignment' exploitation.\",\n  \"landscape\": \"VERIFIABLE MULTIMODAL + GATED/STRUCTURED REWARDS: PaLMR (arXiv:2603.06652, Feb 2026) uses gated hierarchical reward R = S_vis·(alpha·S_ans + (1-alpha)·S_fmt) where BINARY visual fidelity gates answer reward — closest gating principle but verifiable with binary gate. SR-MCR (arXiv:2512.22545, Dec 2025) integrates five self-referential sub-rewards with GRPO — flat combination on verifiable tasks. RuCL (arXiv:2602.21628, Feb 2026) implements stratified rubric-based curriculum on verifiable multimodal tasks. Perception-R1 (arXiv:2506.07218) adds visual perception reward component to RLVR — composite reward with perception as separate weighted component, verifiable, shows explicitly rewarding perceptual accuracy improves downstream reasoning. Vision-SR1 (arXiv:2508.19652, Aug 2025) decomposes VLM reasoning into visual perception and language reasoning with self-rewarding — verifiable. Vero (arXiv:2604.04917, Apr 2026) uses task-routed rewards across 59 datasets — verifiable. V-Triune (arXiv:2505.18129, May 2026) sample-level reward routing — verifiable. Chart-RL (arXiv:2603.06958, Mar 2026) applies RLVR to chart reasoning — verifiable. PEARL (CVPR 2026) binary perception-reasoning gate. CogFlow (ICLR 2026) Visual-Gated Policy Optimization — binary gate. Faithful GRPO (arXiv:2604.08476, Apr 2026) constrains policy for spatial grounding — verifiable. NON-VERIFIABLE + GATED/STRUCTURED REWARDS (TEXT-ONLY): DRO (arXiv:2506.13351, Jun 2025/May 2026) uses BINARY rubric-gating as hard feasibility constraints at rollout-group level for non-verifiable text tasks (scientific paragraph revision, medical QA) — coverage gate + consistency gate, both binary accept/reject. Most directly overlapping with our gating-for-non-verifiable concept, but text-only and strictly binary. Training AI Co-Scientists (arXiv:2512.23707, Dec 2025) applies rubric RL (GRPO) to scientific research plan generation — instance-specific rubrics extracted from papers, reward = proportion of satisfied rubric items, text-only, demonstrates cross-domain generalization but also reward model overoptimization. Rubric-ARM (arXiv:2602.01511, Feb 2026) alternating RL for rubric-based reward modeling — text-only. Writing-Zero (arXiv:2506.00103) bridges non-verifiable tasks via pairwise GenRM — text-only. Rubric-Grounded RL (arXiv:2605.08061, May 2026) LLM-judge rubric decomposition — text-only. RubricEM (arXiv:2605.10899, May 2026) meta-RL with rubric-guided policy decomposition — text-only. ARES (arXiv:2605.23454, May 2026) automates rubric synthesis from documents at scale (101K instances, 1.1M criteria) with QA-rubric co-generation — text-only, addresses rubric generation bottleneck but no gating. NON-VERIFIABLE MULTIMODAL: RubiCap (arXiv:2603.09160, Mar 2026) rubric-guided RL for dense image captioning with dynamically generated instance-level rubrics — no gating, general captioning not scientific reasoning. ClaimDiff-RL (arXiv:2605.20278, May 2026) decomposes captioning evaluation into individual visual claims with graded severity weighting — claim-level decomposition structurally analogous to rubric dimensions, severity weighting as implicit soft gating, hybrid verifiable/non-verifiable but for general captioning. rDPO (arXiv:2604.13029, Apr 2026) applies instance-specific rubrics for multimodal DPO with essential/additional criteria functioning as soft gating — multimodal, uses DPO not GRPO, scores are {0, 0.5, 1} per criterion. BalCapRL (Mar 2026) balanced multi-objective RL for captioning. REWARD DYNAMICS AND ANTI-HACKING: Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) identifies three systematic exploitation patterns in rubric rewards for medical/science domains — partial compound (36%), implicit-as-explicit (34.6%), imprecise verification (29.4%) — and proposes self-internalization gap as verifier-free diagnostic (r=0.91-0.97 correlation with reference panel). Directly validates anti-hacking motivation and informs our monitoring strategy. POW3R (arXiv:2605.20164, May 2026) demonstrates policy-aware rubric weighting outperforms static weighting because important criteria can be saturated or unreachable — both text AND multimodal experiments. Reward Design for Physical Reasoning (arXiv:2604.13993, Apr 2026) found accuracy-based rewards outperform flat composite rubric rewards on verifiable physics tasks, BUT also found rubric rewards improve structured reasoning quality — motivates our focus on non-verifiable settings where accuracy is unavailable, while acknowledging rubric rewards provide complementary value even in verifiable settings. CONTINUOUS vs BINARY GATING THEORY: GR3 (arXiv:2603.10535) proves continuous multiplicative gating is a strict mathematical generalization of binary gating — equivalent in binary case, strictly superior when rewards are graded, because binary gating breaks Lipschitz continuity. Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) shows 0.69 degeneracy rate at group size 4 with binary rewards; continuous fix yields 45-point accuracy gain. ReDit (arXiv:2506.18631) achieves GRPO-equivalent performance in 10% of training steps by making discrete rewards continuous. Smooth Gate Functions (arXiv:2602.19345) formalizes properties of admissible gate functions and shows smooth alternatives to hard clipping produce more stable training. PEPO (arXiv:2603.22847) uses smooth gating for multimodal token-level advantage estimation, directly relevant to our multimodal setting. THE GAP: No work combines (1) CONTINUOUS hierarchical gating (all existing gating is binary) with (2) non-verifiable multimodal settings with (3) scientific reasoning requiring domain-specific rubrics with (4) policy-aware adaptive weight/threshold scheduling.\",\n  \"inspired_by\": \"Intersection gap with principled generalization: DRO provides binary rubric-gating for non-verifiable text tasks; PaLMR provides binary visual gating for verifiable multimodal tasks; GR3 proves continuous gating is a strict mathematical generalization of binary gating with provably better gradient properties. We synthesize these into continuous hierarchical gating for non-verifiable multimodal scientific reasoning. The key theoretical insight: binary gating introduces gradient discontinuities that are especially harmful when rewards are inherently graded (as in scientific reasoning rubrics) — continuous gating eliminates this while preserving the epistemic dependency structure (perception→structure→reasoning). POW3R demonstrates static rubric weights are suboptimal — we integrate policy-aware adaptation. Reward Hacking in Rubric-Based RL identifies exploitation patterns in scientific/medical rubric RL — we integrate self-internalization gap monitoring. ClaimDiff-RL provides the architectural template for claim-level visual verification in Tier-1. Building block: GRPO's compatibility with multi-reward designs (proven by SR-MCR, DRO, Vero, V-Triune, POW3R) makes it the natural optimization backbone.\",\n  \"approach\": \"We propose GatedRubric-GRPO, which introduces CONTINUOUS hierarchical gating for non-verifiable multimodal scientific reasoning within standard GRPO training on Qwen3-VL-8B. The key technical innovation over existing gated approaches (DRO's binary rubric-gates, PaLMR's binary visual gates) is replacing binary indicator functions with smooth sigmoid gates, formally grounded in GR3's proof that continuous gating is a strict generalization of binary gating.\\n\\nSMOOTH GATING FORMULATION: The composite reward decomposes into three epistemically dependent tiers:\\n\\nR = w₁·R₁ + w₂·g₁(R₁)·R₂ + w₃·g₁(R₁)·g₂(R₂)·R₃\\n\\nwhere g_k(x) = sigma((x - tau_k) / T_k) are smooth sigmoid gate functions with temperature T_k controlling sharpness. Key properties: (1) As T_k → 0, g_k → binary indicator 𝟙(x ≥ tau_k), recovering DRO/PaLMR-style hard gating — our formulation is a strict generalization. (2) For finite T_k, g_k preserves Lipschitz continuity of the reward landscape, eliminating gradient dead zones at thresholds. (3) T_k can be scheduled during training (warm→cool), implementing an explicit smooth curriculum from exploration to exploitation.\\n\\nTIER-1 (Visual Grounding, continuous 0-1): Inspired by ClaimDiff-RL's claim-level decomposition and Perception-R1's visual perception reward, we decompose model outputs into atomic visual claims and verify each against the figure. Programmatic checks (element identification, data reading, spatial description) combined with lightweight LLM verification produce a continuous grounding score. This extends Perception-R1's approach (binary verification of pre-extracted annotations) to open-ended claim generation with graded scoring.\\n\\nTIER-2 (Structural Quality, soft-gated on Tier-1): A frozen LLM judge (Qwen3-32B) evaluates logical coherence, evidence-claim alignment, domain terminology, and visual-textual consistency using discipline-specific rubric templates. Rubric templates are auto-generated following ARES's pipeline adapted for scientific figures, then expert-calibrated. Soft-gated by g₁(R₁): when visual grounding is poor, structural quality reward is smoothly attenuated (NOT zeroed as in binary gating), providing gradient signal proportional to grounding quality.\\n\\nTIER-3 (Reasoning Quality, soft-gated on Tier-1 AND Tier-2): Bootstrapped pairwise comparison within GRPO rollout groups assesses analytical depth, interpretive insight, explanation completeness — extending Writing-Zero's BRPO to multimodal. Soft-gated by g₁(R₁)·g₂(R₂).\\n\\nPOLICY-AWARE ADAPTIVE VARIANT (GatedRubric-GRPO+): Inspired by POW3R's finding that static rubric weights are suboptimal, we additionally implement an adaptive variant where: (a) per-criterion contrastiveness is computed from rollout variance within each GRPO group, (b) weights w₁, w₂, w₃ and temperatures T₁, T₂ are rescaled based on criterion contrastiveness with EMA smoothing, and (c) category-level normalization preserves the tier structure. This ensures training pressure shifts from saturated criteria (e.g., basic element identification) to actionable criteria (e.g., interpretive depth) as the policy improves.\\n\\nANTI-HACKING MONITORING: Integrating the self-internalization gap from 'Reward Hacking in Rubric-Based RL', we compute the divergence between the policy's prompt-only distribution and rubric-conditioned distribution using only policy log-probabilities. This provides a verifier-free early-stopping diagnostic (r=0.91-0.97 correlation with reference panel in their experiments) to detect when the policy begins exploiting rubric structure rather than genuinely improving.\\n\\nTRAINING TASKS (genuinely non-verifiable):\\n\\n(1) Scientific figure explanation generation using MMSci (Nature Communications figures, 72 disciplines) — 10K stratified sample across 18 discipline groups. RE-ANNOTATION PIPELINE: Reference captions decomposed into atomic claims by Qwen3-32B, converted to per-figure rubric criteria across 7 dimensions: Visual Accuracy (correct identification of visual elements), Sub-figure Coverage (all panels addressed), Quantitative Fidelity (numerical values, trends, comparisons), Scientific Terminology (domain-appropriate vocabulary), Methodological Context (experimental/computational technique), Interpretive Validity (scientifically sound conclusions), Structural Description (axes, labels, legends). Each criterion assigned severity weight: Critical (3.0), Important (2.0), Minor (1.0). Teacher committee of 3 VLMs generates alternative captions for consensus extraction following RubiCap's pipeline. MOTIVATION: CIDEr scores are 0.00-3.73 across ALL models on MMSci, demonstrating reference-based metrics are fundamentally inadequate for scientific figure captioning where identical content admits vastly different valid descriptions.\\n\\n(2) Open-ended scientific graph analysis using SciGraphQA re-annotated with rubric scoring (same 7-dimension framework, adapted for QA format).\\n\\n(3) SciCritique-5K: A new benchmark of ~5K scientific figure critique examples. CONSTRUCTION PIPELINE: (a) Source: ArXiv papers (2020-2025) across 5 STEM domains (physics, chemistry, biology, materials science, earth science), selected via SciCap extraction pipeline. (b) Figure type classification using SigLIP visual encoder (CharXiv approach, cosine similarity ≥ 0.65). (c) Critique generation: 3-model ensemble (GPT-4o, Claude, Gemini) generates structured critiques per figure. (d) Rubric dimensions (8): Visual Accuracy, Scientific Validity, Quantitative Fidelity, Methodological Context, Interpretive Depth, Structural Completeness, Domain Terminology, Constructive Suggestions — informed by SciFig's 6-dimension taxonomy and SIQA's scientific image quality framework. (e) Each dimension: 5-point ordinal scale + Essential/Important/Optional/Pitfall classification (Dr.SCI approach). (f) LLM annotation: Qwen3-32B scores each critique against rubric, with 3-run median voting and position-switching for robustness (following rDPO's protocol). (g) Expert validation: 20% subset (1K items), 3 annotators per item from STEM PhD pool across the 5 domains, 2-week calibration phase with 50 consensus examples, target Krippendorff's alpha ≥ 0.75 per dimension, 60-minute session limits to prevent fatigue. (h) SIZE JUSTIFICATION: 5K is within the effective range for rubric-RL (Training AI Co-Scientists uses 6.8K; DRO uses 12.5-19.8K; Self-Rewarding Rubric RL demonstrated effectiveness with 4K), and we supplement with 10K MMSci + SciGraphQA samples for total training set of ~20K+.\\n\\nCONTROLLED COMPARISON (verifiable baselines): CharXiv and SciFIBench as controlled comparisons demonstrating WHERE binary rewards suffice.\\n\\nCOMPREHENSIVE ABLATION SUITE (7 conditions to isolate each contribution):\\n(A1) Flat composite: R = w₁·R₁ + w₂·R₂ + w₃·R₃ (no gating) — tests whether gating adds value over flat combination\\n(A2) DRO-style binary rubric-gating: hard accept/reject at rollout-group level — tests continuous vs. binary gating for non-verifiable tasks, directly comparing our approach against DRO's mechanism\\n(A3) PaLMR-style binary visual gate: R₁ binarized, indicator function gates — tests continuous vs. binary gating for visual grounding specifically\\n(A4) POW3R-style policy-aware weighting WITHOUT gating: adaptive weights but flat combination — tests whether gating or adaptive weighting is the primary contributor\\n(A5) Dynamic weighting a la RuCL: rubric weights adjust during training but without gating structure\\n(A6) Tier-1+2 only (no reasoning quality tier)\\n(A7) Tier-1+3 only (no structural quality tier)\\n\\nThis ablation suite directly addresses: (1) the negative result from Reward Design for Physical Reasoning (which tested FLAT composite on VERIFIABLE tasks — a different regime where accuracy dominates); (2) the comparison against DRO's binary gating (the most direct competitor for gating-on-non-verifiable); (3) the comparison against POW3R's adaptive weighting (the most direct competitor for dynamic reward adjustment); (4) whether continuous gating + adaptive weighting together exceed either alone.\\n\\nTHEORETICAL MOTIVATION: (1) Gradient continuity: GR3 proves continuous multiplicative gating preserves Lipschitz continuity while binary gating introduces discontinuities causing gradient dead zones — especially harmful when rewards are inherently graded (as in rubric evaluation). (2) Gradient starvation prevention: binary gating at group level (DRO-style) can produce zero-gradient groups when all rollouts either pass or fail the gate; continuous gating always provides a non-zero gradient signal proportional to gate proximity. (3) Smooth curriculum: temperature scheduling T_k(t) implements a principled version of the implicit curriculum discovered in RLVR training dynamics (arXiv:2602.14872), with warm temperatures enabling broad exploration early and cool temperatures enforcing stricter gating later. (4) Anti-exploitation: Reward Hacking in Rubric-Based RL identifies that 90% of rubric criteria are presence-based (easy to game) — our tiered gating ensures that presence of higher-tier content (reasoning quality) cannot compensate for absence of lower-tier requirements (visual grounding), while continuous gates prevent the all-or-nothing rejection that wastes partially valuable training signal.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1100-1500 (8xH100: ~120h LLM-based rubric annotation with 32B judge on ~15K examples, ~600h main GatedRubric-GRPO training and 7-condition ablation suite, ~180h baseline reproductions including DRO/RubiCap/PaLMR-style baselines, ~150h evaluation and analysis)\",\n      \"human_annotation\": \"~700 person-hours domain expert validation (~$17K at expert rates: 1K SciCritique validation items x 3 annotators x 25 min + 500 MMSci rubric validation items x 3 annotators x 15 min + ~100h calibration/coordination, 5 STEM PhD annotators at $22-25/hr)\",\n      \"timeline\": \"4.5-5.5 months (6 weeks dataset curation with LLM-assisted rubric annotation + expert validation including 2-week calibration, 3 weeks baseline implementation, 7 weeks GatedRubric-GRPO training and full 7-condition ablation suite, 4 weeks evaluation and paper writing)\",\n      \"estimated_gpu_cost\": \"$2,200-$3,750 (at $2-2.50/H100-hr spot pricing)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"900-1200 (Claude generates rubric templates, annotation pipelines, ablation configurations, and smooth gating module code; human validates scientific accuracy)\",\n      \"human_annotation\": \"~500 person-hours expert validation (~$12K — reduced via Claude-assisted rubric calibration and automated quality filtering)\",\n      \"timeline\": \"3.5-4.5 months (5 weeks dataset curation with Claude-assisted rubric generation and calibration, 2.5 weeks baseline setup, 6 weeks training and ablations, 3.5 weeks evaluation and writing)\",\n      \"claude_api_cost\": \"$500-850 (rubric generation for ~15K examples, annotation calibration, reward module code generation, experiment analysis — ~150M input + 30M output tokens via Sonnet batch API)\",\n      \"estimated_gpu_cost\": \"$1,800-$3,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"900-1200 (same compute floor; GPU time is irreducible)\",\n      \"human_annotation\": \"~300 person-hours minimum expert validation (~$7.5K — cannot be fully automated for scientific domain rubrics; Reward Hacking in Rubric-Based RL shows LLM judges systematically exploit 'topical alignment' without human calibration)\",\n      \"timeline\": \"3-4 months (parallel dataset curation and code development, automated hyperparameter sweeps for tau and T parameters)\",\n      \"claude_api_cost\": \"$800-1,400 (heavier annotation generation, automated rubric calibration experiments, smooth gating hyperparameter search, paper drafting — ~300M input + 60M output tokens)\",\n      \"estimated_gpu_cost\": \"$1,800-$3,000\",\n      \"speed_bottleneck\": \"Domain expert validation of scientific rubric annotations is the irreducible bottleneck. Reward Hacking in Rubric-Based RL (arXiv:2605.12474) demonstrates that even strong LLM verifiers retain 15-28% exploitation rate — systematic LLM biases in scientific rubric evaluation (preferring verbose, topically aligned but imprecise responses) require human calibration. Expert recruitment and calibration across 5 STEM domains requires 3-4 weeks minimum.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract: Jul 21 2026, paper: Jul 28 2026 — tight but feasible with focused results on 2 of 3 tasks and key ablations A1-A3)\",\n    \"WACV 2027 Round 2 (paper: Aug 27 2026 — full results including all 7 ablations and SciCritique-5K benchmark)\",\n    \"EACL 2027 (ARR submission: Aug 3 2026 — framing emphasizes rubric RL and gating formalism)\",\n    \"CVPR 2027 (estimated ~Nov 2026 — TBA, full paper with complete analysis and policy-aware adaptive variant)\",\n    \"ICLR 2027 (estimated ~Oct 2026 — TBA, full paper with theoretical analysis of continuous vs binary gating dynamics)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment (arXiv:2603.06652, Feb 2026) — binary gated hierarchical reward for verifiable tasks; our smooth gating extends this principle\",\n    \"DRO: Direct Reasoning Optimization with Rubric-Gated Constraints (arXiv:2506.13351, Jun 2025/May 2026) — BINARY rubric-gating as hard feasibility constraints for non-verifiable TEXT tasks; most direct competitor, we generalize from binary to continuous gating and from text to multimodal\",\n    \"RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning (arXiv:2603.09160, Mar 2026) — rubric-based RL for non-verifiable multimodal captioning without gating; we add hierarchical gating for scientific reasoning\",\n    \"Training AI Co-Scientists Using Rubric Rewards (arXiv:2512.23707, Dec 2025) — rubric RL (GRPO) for scientific research plan generation, text-only; demonstrates cross-domain generalization and reward model overoptimization\",\n    \"Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) — identifies three systematic exploitation patterns in medical/science rubric RL; proposes self-internalization gap (r=0.91-0.97) as verifier-free diagnostic; directly informs our anti-hacking monitoring\",\n    \"GR3: Group Relative Reward Rescaling (arXiv:2603.10535) — FORMALLY PROVES continuous multiplicative gating is a strict generalization of binary gating with superior gradient properties; key theoretical foundation for our approach\",\n    \"POW3R: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164, May 2026) — demonstrates static rubric weights are suboptimal via policy-aware contrastiveness-based adaptation; both text and multimodal; inspires our adaptive variant\",\n    \"ARES: Automated Rubric Synthesis for Scalable RL (arXiv:2605.23454, May 2026) — automated QA-rubric co-generation pipeline at scale (101K instances, 1.1M criteria); informs our rubric generation methodology\",\n    \"rDPO: Visual Preference Optimization with Rubric Rewards (arXiv:2604.13029, Apr 2026) — instance-specific rubrics for multimodal DPO with essential/additional criteria as soft gating; closest multimodal rubric competitor but uses DPO not RL\",\n    \"ClaimDiff-RL: Fine-Grained Caption RL through Visual Claim Comparison (arXiv:2605.20278, May 2026) — claim-level captioning decomposition with graded severity; architectural template for our Tier-1 visual claim verification\",\n    \"Perception-R1: Visual Perception Reward for MLLMs (arXiv:2506.07218) — adds visual perception reward to RLVR with composite reward design; verifiable tasks but demonstrates perception reward improves downstream reasoning\",\n    \"Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — demonstrates 0.69 degeneracy rate and 45-point accuracy gain from continuous fix; empirical evidence for continuous over binary rewards\",\n    \"ReDit: Reward Dithering for Improved LLM Policy Optimization (arXiv:2506.18631) — achieves GRPO-equivalent performance in 10% of training steps by making discrete rewards continuous; quantitative evidence for continuous reward advantages\",\n    \"Smooth Gate Functions for Soft Advantage Policy Optimization (arXiv:2602.19345) — formalizes properties of admissible gate functions; smooth alternatives produce more stable training\",\n    \"PEPO: Rethinking Token-Level Policy Optimization for Multimodal CoT (arXiv:2603.22847) — smooth gating for multimodal token-level advantage estimation; directly relevant to our multimodal setting\",\n    \"SR-MCR: Self-Rewarded Multimodal Coherent Reasoning (arXiv:2512.22545, Dec 2025) — five structured sub-rewards with GRPO; flat combination on verifiable tasks\",\n    \"RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, Feb 2026) — dynamic rubric weighting for curriculum; verifiable\",\n    \"RubricEM: Meta-RL with Rubric-guided Policy Decomposition (arXiv:2605.10899, May 2026) — rubric-guided policy decomposition; text-only\",\n    \"Rubric-ARM: Alternating RL for Rubric-Based Reward Modeling (arXiv:2602.01511, Feb 2026) — joint rubric generator and judge optimization; text-only\",\n    \"Reward Design for Physical Reasoning in VLMs (arXiv:2604.13993, Apr 2026) — accuracy > flat composite rubric on verifiable tasks, BUT rubric rewards improve structured reasoning quality; motivates our non-verifiable focus while acknowledging complementary value of rubric rewards\",\n    \"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards (arXiv:2602.14872, Feb 2026) — theoretical grounding for curriculum effects; our temperature scheduling implements explicit smooth curriculum\",\n    \"Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards (arXiv:2506.00103) — pairwise GenRM for text non-verifiable tasks; we extend BRPO to multimodal Tier-3\",\n    \"Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition (arXiv:2508.19652, Aug 2025) — perception-reasoning decomposition; verifiable\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv 2026) — reward hacking pathways\",\n    \"Vero: An Open RL Recipe for General Visual Reasoning (arXiv:2604.04917, Apr 2026) — task-routed rewards; verifiable\",\n    \"V-Triune: Visual Triple Unified Reinforcement Learning (arXiv:2505.18129, May 2026) — sample-level reward routing; verifiable\",\n    \"Rubric-Grounded RL: Structured Judge Rewards (arXiv:2605.08061, May 2026) — LLM-judge rubric decomposition; text-only\",\n    \"Faithful GRPO: Constrained Policy Optimization for Visual Grounding (arXiv:2604.08476, Apr 2026) — verifiable spatial tasks\",\n    \"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding (arXiv:2407.04903, NeurIPS 2024 Workshop) — 72-discipline scientific figure dataset\",\n    \"SciGraphQA: A Large-Scale Synthetic Multi-Turn QA Dataset for Scientific Graphs (arXiv:2308.03349) — open-ended graph analysis\",\n    \"CharXiv: Charting Gaps in Realistic Chart Understanding (NeurIPS 2024)\",\n    \"SciFIBench: Benchmarking LMMs for Scientific Figure Interpretation (NeurIPS 2024)\",\n    \"PRISMM-Bench: Measuring Multimodal Inconsistency in Scientific Papers (arXiv:2510.16505) — 384 validated inconsistencies from peer reviews; informs SciCritique-5K construction\",\n    \"SIQA: Scientific Image Quality Assessment (arXiv:2603.06700) — 4-dimension scientific image quality framework with expert annotation protocol\",\n    \"SciFig: Scientific Figure Quality Rubric (arXiv:2601.04390) — 6-dimension rubric framework for scientific figure evaluation\",\n    \"Dr.SCI: Scientific Reasoning with Rubric Item Categories (arXiv:2602.08321) — Essential/Important/Optional/Pitfall rubric categorization for STEM evaluation\"\n  ],\n  \"description\": \"We propose GatedRubric-GRPO, a framework that introduces SMOOTH CONTINUOUS hierarchical gating for non-verifiable multimodal scientific reasoning. The key technical innovation is replacing the BINARY gates used by all prior gated reward systems (DRO uses binary rubric-gates for non-verifiable text; PaLMR uses binary visual gates for verifiable multimodal) with smooth sigmoid gate functions g_k(x) = sigma((x - tau_k)/T_k), formally grounded in GR3's proof that continuous multiplicative gating is a strict mathematical generalization of binary gating that preserves Lipschitz continuity and eliminates gradient dead zones. Three epistemically dependent tiers — Tier-1: visual grounding via claim-level decomposition (ClaimDiff-RL-inspired), Tier-2: structural quality via frozen LLM-judge rubrics (ARES-inspired auto-generation, expert-calibrated), Tier-3: reasoning quality via bootstrapped pairwise comparison — are combined as R = w₁·R₁ + w₂·g₁(R₁)·R₂ + w₃·g₁(R₁)·g₂(R₂)·R₃, with an adaptive variant (GatedRubric-GRPO+) incorporating POW3R-style policy-aware weight/temperature scheduling. Anti-exploitation monitoring via self-internalization gap (from Reward Hacking in Rubric-Based RL). Training on genuinely non-verifiable scientific tasks: MMSci figure explanation (10K, re-annotated with 7-dimension rubric across 72 disciplines), SciGraphQA open-ended analysis (rubric-scored), and SciCritique-5K (new benchmark: 5K figure-critique pairs from 5 STEM domains, 8-dimension rubric, 20% expert-validated with target Krippendorff's alpha >= 0.75). A 7-condition ablation suite directly compares against DRO-style binary gating, PaLMR-style binary visual gates, POW3R-style adaptive weighting without gating, and flat composite baselines, isolating the contribution of continuous gating, hierarchical structure, and adaptive scheduling independently.\",\n  \"project_name\": \"gated_rubric_nonverif_sci_mm\",\n  \"source\": \"web_research\",\n  \"change_type\": \"major\",\n  \"changes_summary\": {\n    \"issue_1_missing_works\": \"MAJOR FIX: Integrated all 8 reviewer-identified missing works plus 7 additional works discovered during deep research. DRO (binary rubric-gating for non-verifiable text) is now positioned as the most direct competitor with explicit differentiation (binary vs continuous, text vs multimodal). Training AI Co-Scientists positioned as demonstrating rubric RL feasibility for scientific domains. Reward Hacking in Rubric-Based RL directly incorporated — its self-internalization gap becomes a core monitoring component, and its exploitation taxonomy informs our anti-hacking design. ARES informs rubric generation pipeline. POW3R's policy-aware weighting becomes a core adaptive variant (GatedRubric-GRPO+). rDPO positioned as closest multimodal rubric competitor (uses DPO not RL). Perception-R1 and ClaimDiff-RL inform Tier-1 design. Additionally integrated: GR3 (formal proof of continuous > binary gating), PEPO (smooth gating for multimodal), gradient starvation analysis, ReDit, Smooth Gate Functions paper, PRISMM-Bench, SIQA, SciFig, Dr.SCI.\",\n    \"issue_2_novelty_sharpened\": \"MAJOR FIX: Novelty fundamentally reframed from 'domain extension' to 'principled generalization with formal justification.' Three-pillar argument: (1) FORMAL — GR3 proves continuous multiplicative gating is a strict mathematical generalization of binary gating; binary gating breaks Lipschitz continuity and causes gradient dead zones (formalized by Razin et al. ICLR 2024, demonstrated empirically by gradient starvation analysis showing 0.69 degeneracy rate). (2) STRUCTURAL — scientific visual reasoning has inherently continuous graded quality, not binary correctness; binary gating (DRO/PaLMR) discards graded signal. (3) PRACTICAL — comprehensive ablation directly comparing continuous vs binary gating (A2: DRO-style, A3: PaLMR-style) will provide first empirical evidence of the gap. The continuous gating formulation R = w₁·R₁ + w₂·sigma((R₁-tau₁)/T₁)·R₂ + w₃·sigma((R₁-tau₁)/T₁)·sigma((R₂-tau₂)/T₂)·R₃ is the concrete technical contribution — temperature scheduling T_k(t) implements a principled smooth curriculum.\",\n    \"issue_3_benchmark_detailed\": \"MAJOR FIX: SciCritique expanded from 2K to 5K with complete construction pipeline specified: (a) ArXiv papers 2020-2025 across 5 STEM domains, (b) SigLIP-based figure type classification following CharXiv, (c) 3-model ensemble critique generation, (d) 8-dimension rubric informed by SciFig and SIQA frameworks, (e) Essential/Important/Optional/Pitfall categorization following Dr.SCI, (f) LLM annotation with 3-run median voting and position-switching following rDPO, (g) 20% expert validation (1K items, 3 annotators, 2-week calibration, target Krippendorff's alpha >= 0.75, 60-min sessions). Size justified by comparison: Training AI Co-Scientists uses 6.8K, DRO uses 12.5-19.8K, Self-Rewarding Rubric RL effective with 4K.\",\n    \"issue_4_mmsci_reannotation\": \"MAJOR FIX: Specified 7-dimension rubric replacing CIDEr/BLEU: Visual Accuracy, Sub-figure Coverage, Quantitative Fidelity, Scientific Terminology, Methodological Context, Interpretive Validity, Structural Description. Motivation: CIDEr scores are 0.00-3.73 across ALL models (including GPT-4o, Claude-3.5-Sonnet), demonstrating reference-based metrics are fundamentally inadequate. Pipeline: Qwen3-32B decomposes reference captions into atomic claims, converts to binary criteria with Critical/Important/Minor severity weights. Teacher committee of 3 VLMs for consensus extraction following RubiCap. Expert validation: 500 items across 10 PhD-annotated domains, target Cohen's kappa >= 0.70.\",\n    \"issue_5_reward_design_nuanced\": \"MODERATE FIX: Acknowledged that rubric rewards DO improve structured reasoning quality even in verifiable settings (per Reward Design for Physical Reasoning), not simply 'fail.' Reframed: accuracy rewards and rubric rewards capture DIFFERENT value — accuracy measures correctness, rubrics measure process quality. In non-verifiable settings where accuracy is unavailable, rubric rewards become the primary signal, and gating provides ADDITIONAL value by preventing the specific 'eloquent hallucination' failure mode documented as 'topical alignment' exploitation by Reward Hacking in Rubric-Based RL (21.1% of all exploitation instances).\",\n    \"issue_6_pow3r_engaged\": \"MAJOR FIX: POW3R's finding that static rubric weights are suboptimal is not merely acknowledged but INCORPORATED as a core adaptive variant (GatedRubric-GRPO+). Policy-aware contrastiveness-based weight and temperature adaptation with EMA smoothing and category-level normalization preserving tier structure. Additionally added as ablation A4 (POW3R-style adaptive weighting WITHOUT gating) to test whether gating or adaptive weighting is the primary contributor. This ensures we can empirically demonstrate that continuous gating + adaptive weighting together exceed either alone.\",\n    \"additional_improvements\": \"New ablation A2 directly compares against DRO-style binary gating on the same non-verifiable tasks — the most important comparison for establishing novelty. Self-internalization gap monitoring integrated from Reward Hacking paper as anti-hacking diagnostic. ClaimDiff-RL-inspired claim-level decomposition for Tier-1 visual grounding. Smooth gating temperature scheduling T_k(t) as principled curriculum mechanism. Total ablation suite expanded from 5 to 7 conditions. Reference list expanded from 25 to 36 to reflect comprehensive landscape coverage.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f06159a2-f2d1-492d-bf2b-8548c277f8ca",
  "isSidechain": false,
  "requestId": "req_011CbUGLZbS7PNwWJnqRvAQA",
  "type": "assistant",
  "uuid": "c2ac782f-c251-406d-85c8-be049c2ce036",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2LTu3o3txpiXjDTSAFkz7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5045,
      "cache_read_input_tokens": 51041,
      "output_tokens": 16655,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5045,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 16655,
          "cache_read_input_tokens": 51041,
          "cache_creation_input_tokens": 5045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5045
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

_source line 89 · 2026-05-28T03:40:51.209Z_

<details><summary>↩ Tool result · reported error · `toolu_014dLvpbwUWuuXJTS848CCuy`</summary>

```text
Claude requested permissions to write to /home/ubuntu/idea-review/revised_idea_r3.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2ac782f-c251-406d-85c8-be049c2ce036",
  "isSidechain": false,
  "promptId": "d0628049-5dd6-44e2-863d-4e5f7a82f317",
  "type": "user",
  "uuid": "1624a070-7383-4907-badf-815bc9efba60",
  "toolUseResult": "Error: Claude requested permissions to write to /home/ubuntu/idea-review/revised_idea_r3.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "c2ac782f-c251-406d-85c8-be049c2ce036",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 90_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "1624a070-7383-4907-badf-815bc9efba60",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 91_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Tool call

_source line 92 · 2026-05-28T03:40:55.642Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XgAQp7QYye2tboygGXtKU2`</summary>

```json
{
  "command": "ls /home/ubuntu/idea-review/ 2>/dev/null || echo \"Directory does not exist\"",
  "description": "Check if idea-review directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1624a070-7383-4907-badf-815bc9efba60",
  "isSidechain": false,
  "requestId": "req_011CbUGoZpaTsRchvJKaHyVA",
  "type": "assistant",
  "uuid": "8c57b037-74c7-49c7-a0ff-17ccaa630915",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaacMUg7qAAYUHEFRZfdEb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16708,
      "cache_read_input_tokens": 56086,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 56086,
          "cache_creation_input_tokens": 16708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16708
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

_source line 93 · 2026-05-28T03:40:55.657Z_

<details><summary>↩ Tool result · reported error · `toolu_01XgAQp7QYye2tboygGXtKU2`</summary>

```text
ls in '/home/ubuntu/idea-review/' was blocked. For security, Claude Code may only list files in the allowed working directories for this session: '/home/ubuntu/idea_review'.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c57b037-74c7-49c7-a0ff-17ccaa630915",
  "isSidechain": false,
  "promptId": "d0628049-5dd6-44e2-863d-4e5f7a82f317",
  "type": "user",
  "uuid": "fb9da49d-ba98-49dc-912b-8b52c94f1538",
  "toolUseResult": "Error: ls in '/home/ubuntu/idea-review/' was blocked. For security, Claude Code may only list files in the allowed working directories for this session: '/home/ubuntu/idea_review'.",
  "sourceToolAssistantUUID": "8c57b037-74c7-49c7-a0ff-17ccaa630915",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-28T03:40:58.738Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UunTebckrdjVwA8MEh5a2z`</summary>

```json
{
  "command": "ls /home/ubuntu/idea_review/",
  "description": "List files in idea_review directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb9da49d-ba98-49dc-912b-8b52c94f1538",
  "isSidechain": false,
  "requestId": "req_011CbUGotkcD8pBKVfYpuwnH",
  "type": "assistant",
  "uuid": "2c082801-db77-454d-8f5e-57d148704a64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gg8mS5da7CgdWmcQUnnd2P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 72794,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 72794,
          "cache_creation_input_tokens": 159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 159
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

_source line 95 · 2026-05-28T03:40:58.885Z_

<details><summary>↩ Tool result · `toolu_01UunTebckrdjVwA8MEh5a2z`</summary>

```text
__pycache__
batch_triage.py
conference.py
config.py
convergence.py
dispatch
io_utils.py
parsers.py
prompts
reviewer.py
审idea的agent
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c082801-db77-454d-8f5e-57d148704a64",
  "isSidechain": false,
  "promptId": "d0628049-5dd6-44e2-863d-4e5f7a82f317",
  "type": "user",
  "uuid": "4bfd520d-59cb-426d-857c-f02b7238825d",
  "toolUseResult": {
    "stdout": "__pycache__\nbatch_triage.py\nconference.py\nconfig.py\nconvergence.py\ndispatch\nio_utils.py\nparsers.py\nprompts\nreviewer.py\n审idea的agent",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2c082801-db77-454d-8f5e-57d148704a64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-28T03:45:26.438Z_

<details open><summary>🔧 Tool call — Write · `toolu_012JekAvLWWWkguCoRW7F2Gk`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/revised_idea_r3.json",
  "content": "{\n  \"title\": \"GatedRubric-GRPO: Smooth Hierarchical Gating for Non-Verifiable Multimodal Scientific Reasoning\",\n  \"core_problem\": \"Reinforcement learning with structured rewards has advanced rapidly across two axes: (1) gated/hierarchical rewards for verifiable multimodal tasks (PaLMR, PEARL, CogFlow use binary visual gates; SR-MCR uses flat multi-component rewards), and (2) rubric-based RL for non-verifiable tasks in text-only settings (DRO uses binary rubric-gates as feasibility constraints; Rubric-ARM alternates rubric generator and judge; Training AI Co-Scientists applies rubric RL to scientific plan generation; ARES automates rubric synthesis at scale; RubricEM decomposes policy via rubrics). RubiCap extends rubric RL to non-verifiable multimodal captioning, while rDPO applies instance-specific rubrics for multimodal DPO with essential/additional criteria gating. However, ALL existing gating mechanisms — whether for visual fidelity (PaLMR), rubric feasibility (DRO), or essential criteria qualification (rDPO) — employ BINARY gates: hard accept/reject, yes/no, pass/fail. This creates a critical technical limitation: binary gating introduces discontinuities in the reward landscape that provably cause gradient vanishing and gradient starvation in policy optimization (demonstrated formally by Razin et al. ICLR 2024, and empirically by gradient starvation analysis in GRPO). The problem is especially acute for non-verifiable scientific visual reasoning — tasks like scientific figure explanation, graph-based analytical interpretation, and figure critique — where both visual grounding quality and reasoning quality are INHERENTLY CONTINUOUS and GRADED, not binary. A figure can be 70% correctly perceived; a scientific explanation can be partially valid. Binary gating discards this graded signal.\",\n  \"opportunity\": \"The landscape reveals a precise technical gap at the intersection of three established directions. Direction 1: Gated multimodal rewards exist (PaLMR, PEARL, CogFlow) but use binary gates on verifiable tasks. Direction 2: Rubric-gated non-verifiable RL exists (DRO uses binary rubric-gates as group-level feasibility constraints) but is text-only. Direction 3: Non-verifiable multimodal rubric RL exists (RubiCap for captioning, rDPO for visual preference) but without hierarchical gating. The crucial insight combines two observations: (A) Scientific visual reasoning exhibits an epistemic dependency — visual grounding is a NECESSARY CONDITION for valid reasoning (you cannot produce a correct explanation of a misperceived figure) — creating a natural gating hierarchy. (B) GR3 (arXiv:2603.10535) formally proves that continuous multiplicative gating is a STRICT MATHEMATICAL GENERALIZATION of binary gating: they are equivalent when rewards are binary, but continuous gating is provably superior when rewards are graded, because it preserves Lipschitz continuity of the reward landscape and eliminates gradient dead zones. This means continuous gating is not merely 'softening' binary gates — it enables qualitatively different training dynamics. The convergence of these observations motivates smooth-gated rubric rewards: where DRO uses binary rubric-gates (yes/no feasibility constraints) and PaLMR uses binary visual gates (pass/fail fidelity checks), we introduce smooth sigmoid gates that (1) preserve the epistemic dependency structure, (2) maintain differentiable gradient flow, and (3) naturally encode a continuous curriculum from perception to reasoning. Additionally, POW3R (arXiv:2605.20164) demonstrates that static rubric weights are suboptimal because important criteria can be saturated or unreachable at different training stages — motivating policy-aware adaptive gating. And 'Reward Hacking in Rubric-Based RL' (arXiv:2605.12474) reveals systematic exploitation patterns in rubric rewards for scientific/medical domains — motivating our integration of the self-internalization gap as a training diagnostic. Importantly, we acknowledge (per 'Reward Design for Physical Reasoning in VLMs', arXiv:2604.13993) that rubric rewards DO provide reasoning quality benefits even in verifiable settings — accuracy rewards and rubric rewards capture DIFFERENT value. In non-verifiable settings where accuracy is unavailable, rubric rewards become the primary signal, and gating's additional value is preventing the specific failure mode of visually ungrounded but linguistically polished explanations — the 'eloquent hallucination' pattern that Reward Hacking in Rubric-Based RL documents as 'topical alignment' exploitation.\",\n  \"landscape\": \"VERIFIABLE MULTIMODAL + GATED/STRUCTURED REWARDS: PaLMR (arXiv:2603.06652, Feb 2026) uses gated hierarchical reward R = S_vis·(alpha·S_ans + (1-alpha)·S_fmt) where BINARY visual fidelity gates answer reward — closest gating principle but verifiable with binary gate. SR-MCR (arXiv:2512.22545, Dec 2025) integrates five self-referential sub-rewards with GRPO — flat combination on verifiable tasks. RuCL (arXiv:2602.21628, Feb 2026) implements stratified rubric-based curriculum on verifiable multimodal tasks. Perception-R1 (arXiv:2506.07218) adds visual perception reward component to RLVR — composite reward with perception as separate weighted component, verifiable, shows explicitly rewarding perceptual accuracy improves downstream reasoning. Vision-SR1 (arXiv:2508.19652, Aug 2025) decomposes VLM reasoning into visual perception and language reasoning with self-rewarding — verifiable. Vero (arXiv:2604.04917, Apr 2026) uses task-routed rewards across 59 datasets — verifiable. V-Triune (arXiv:2505.18129, May 2026) sample-level reward routing — verifiable. Chart-RL (arXiv:2603.06958, Mar 2026) applies RLVR to chart reasoning — verifiable. PEARL (CVPR 2026) binary perception-reasoning gate. CogFlow (ICLR 2026) Visual-Gated Policy Optimization — binary gate. Faithful GRPO (arXiv:2604.08476, Apr 2026) constrains policy for spatial grounding — verifiable. NON-VERIFIABLE + GATED/STRUCTURED REWARDS (TEXT-ONLY): DRO (arXiv:2506.13351, Jun 2025/May 2026) uses BINARY rubric-gating as hard feasibility constraints at rollout-group level for non-verifiable text tasks (scientific paragraph revision, medical QA) — coverage gate + consistency gate, both binary accept/reject. Most directly overlapping with our gating-for-non-verifiable concept, but text-only and strictly binary. Training AI Co-Scientists (arXiv:2512.23707, Dec 2025) applies rubric RL (GRPO) to scientific research plan generation — instance-specific rubrics extracted from papers, reward = proportion of satisfied rubric items, text-only, demonstrates cross-domain generalization but also reward model overoptimization. Rubric-ARM (arXiv:2602.01511, Feb 2026) alternating RL for rubric-based reward modeling — text-only. Writing-Zero (arXiv:2506.00103) bridges non-verifiable tasks via pairwise GenRM — text-only. Rubric-Grounded RL (arXiv:2605.08061, May 2026) LLM-judge rubric decomposition — text-only. RubricEM (arXiv:2605.10899, May 2026) meta-RL with rubric-guided policy decomposition — text-only. ARES (arXiv:2605.23454, May 2026) automates rubric synthesis from documents at scale (101K instances, 1.1M criteria) with QA-rubric co-generation — text-only, addresses rubric generation bottleneck but no gating. NON-VERIFIABLE MULTIMODAL: RubiCap (arXiv:2603.09160, Mar 2026) rubric-guided RL for dense image captioning with dynamically generated instance-level rubrics — no gating, general captioning not scientific reasoning. ClaimDiff-RL (arXiv:2605.20278, May 2026) decomposes captioning evaluation into individual visual claims with graded severity weighting — claim-level decomposition structurally analogous to rubric dimensions, severity weighting as implicit soft gating, hybrid verifiable/non-verifiable but for general captioning. rDPO (arXiv:2604.13029, Apr 2026) applies instance-specific rubrics for multimodal DPO with essential/additional criteria functioning as soft gating — multimodal, uses DPO not GRPO, scores are {0, 0.5, 1} per criterion. BalCapRL (Mar 2026) balanced multi-objective RL for captioning. REWARD DYNAMICS AND ANTI-HACKING: Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) identifies three systematic exploitation patterns in rubric rewards for medical/science domains — partial compound (36%), implicit-as-explicit (34.6%), imprecise verification (29.4%) — and proposes self-internalization gap as verifier-free diagnostic (r=0.91-0.97 correlation with reference panel). Directly validates anti-hacking motivation and informs our monitoring strategy. POW3R (arXiv:2605.20164, May 2026) demonstrates policy-aware rubric weighting outperforms static weighting because important criteria can be saturated or unreachable — both text AND multimodal experiments. Reward Design for Physical Reasoning (arXiv:2604.13993, Apr 2026) found accuracy-based rewards outperform flat composite rubric rewards on verifiable physics tasks, BUT also found rubric rewards improve structured reasoning quality — motivates our focus on non-verifiable settings where accuracy is unavailable, while acknowledging rubric rewards provide complementary value even in verifiable settings. CONTINUOUS vs BINARY GATING THEORY: GR3 (arXiv:2603.10535) proves continuous multiplicative gating is a strict mathematical generalization of binary gating — equivalent in binary case, strictly superior when rewards are graded, because binary gating breaks Lipschitz continuity. Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) shows 0.69 degeneracy rate at group size 4 with binary rewards; continuous fix yields 45-point accuracy gain. ReDit (arXiv:2506.18631) achieves GRPO-equivalent performance in 10% of training steps by making discrete rewards continuous. Smooth Gate Functions (arXiv:2602.19345) formalizes properties of admissible gate functions and shows smooth alternatives to hard clipping produce more stable training. PEPO (arXiv:2603.22847) uses smooth gating for multimodal token-level advantage estimation, directly relevant to our multimodal setting. THE GAP: No work combines (1) CONTINUOUS hierarchical gating (all existing gating is binary) with (2) non-verifiable multimodal settings with (3) scientific reasoning requiring domain-specific rubrics with (4) policy-aware adaptive weight/threshold scheduling.\",\n  \"inspired_by\": \"Intersection gap with principled generalization: DRO provides binary rubric-gating for non-verifiable text tasks; PaLMR provides binary visual gating for verifiable multimodal tasks; GR3 proves continuous gating is a strict mathematical generalization of binary gating with provably better gradient properties. We synthesize these into continuous hierarchical gating for non-verifiable multimodal scientific reasoning. The key theoretical insight: binary gating introduces gradient discontinuities that are especially harmful when rewards are inherently graded (as in scientific reasoning rubrics) — continuous gating eliminates this while preserving the epistemic dependency structure (perception to structure to reasoning). POW3R demonstrates static rubric weights are suboptimal — we integrate policy-aware adaptation. Reward Hacking in Rubric-Based RL identifies exploitation patterns in scientific/medical rubric RL — we integrate self-internalization gap monitoring. ClaimDiff-RL provides the architectural template for claim-level visual verification in Tier-1. Building block: GRPO's compatibility with multi-reward designs (proven by SR-MCR, DRO, Vero, V-Triune, POW3R) makes it the natural optimization backbone.\",\n  \"approach\": \"We propose GatedRubric-GRPO, which introduces CONTINUOUS hierarchical gating for non-verifiable multimodal scientific reasoning within standard GRPO training on Qwen3-VL-8B. The key technical innovation over existing gated approaches (DRO's binary rubric-gates, PaLMR's binary visual gates) is replacing binary indicator functions with smooth sigmoid gates, formally grounded in GR3's proof that continuous gating is a strict generalization of binary gating.\\n\\nSMOOTH GATING FORMULATION: The composite reward decomposes into three epistemically dependent tiers:\\n\\nR = w_1*R_1 + w_2*g_1(R_1)*R_2 + w_3*g_1(R_1)*g_2(R_2)*R_3\\n\\nwhere g_k(x) = sigma((x - tau_k) / T_k) are smooth sigmoid gate functions with temperature T_k controlling sharpness. Key properties: (1) As T_k approaches 0, g_k approaches binary indicator, recovering DRO/PaLMR-style hard gating — our formulation is a strict generalization. (2) For finite T_k, g_k preserves Lipschitz continuity of the reward landscape, eliminating gradient dead zones at thresholds. (3) T_k can be scheduled during training (warm to cool), implementing an explicit smooth curriculum from exploration to exploitation.\\n\\nTIER-1 (Visual Grounding, continuous 0-1): Inspired by ClaimDiff-RL's claim-level decomposition and Perception-R1's visual perception reward, we decompose model outputs into atomic visual claims and verify each against the figure. Programmatic checks (element identification, data reading, spatial description) combined with lightweight LLM verification produce a continuous grounding score. This extends Perception-R1's approach (binary verification of pre-extracted annotations) to open-ended claim generation with graded scoring.\\n\\nTIER-2 (Structural Quality, soft-gated on Tier-1): A frozen LLM judge (Qwen3-32B) evaluates logical coherence, evidence-claim alignment, domain terminology, and visual-textual consistency using discipline-specific rubric templates. Rubric templates are auto-generated following ARES's pipeline adapted for scientific figures, then expert-calibrated. Soft-gated by g_1(R_1): when visual grounding is poor, structural quality reward is smoothly attenuated (NOT zeroed as in binary gating), providing gradient signal proportional to grounding quality.\\n\\nTIER-3 (Reasoning Quality, soft-gated on Tier-1 AND Tier-2): Bootstrapped pairwise comparison within GRPO rollout groups assesses analytical depth, interpretive insight, explanation completeness — extending Writing-Zero's BRPO to multimodal. Soft-gated by g_1(R_1)*g_2(R_2).\\n\\nPOLICY-AWARE ADAPTIVE VARIANT (GatedRubric-GRPO+): Inspired by POW3R's finding that static rubric weights are suboptimal, we additionally implement an adaptive variant where: (a) per-criterion contrastiveness is computed from rollout variance within each GRPO group, (b) weights w_1, w_2, w_3 and temperatures T_1, T_2 are rescaled based on criterion contrastiveness with EMA smoothing, and (c) category-level normalization preserves the tier structure. This ensures training pressure shifts from saturated criteria (e.g., basic element identification) to actionable criteria (e.g., interpretive depth) as the policy improves.\\n\\nANTI-HACKING MONITORING: Integrating the self-internalization gap from 'Reward Hacking in Rubric-Based RL', we compute the divergence between the policy's prompt-only distribution and rubric-conditioned distribution using only policy log-probabilities. This provides a verifier-free early-stopping diagnostic (r=0.91-0.97 correlation with reference panel in their experiments) to detect when the policy begins exploiting rubric structure rather than genuinely improving.\\n\\nTRAINING TASKS (genuinely non-verifiable):\\n\\n(1) Scientific figure explanation generation using MMSci (Nature Communications figures, 72 disciplines) — 10K stratified sample across 18 discipline groups. RE-ANNOTATION PIPELINE: Reference captions decomposed into atomic claims by Qwen3-32B, converted to per-figure rubric criteria across 7 dimensions: Visual Accuracy (correct identification of visual elements), Sub-figure Coverage (all panels addressed), Quantitative Fidelity (numerical values, trends, comparisons), Scientific Terminology (domain-appropriate vocabulary), Methodological Context (experimental/computational technique), Interpretive Validity (scientifically sound conclusions), Structural Description (axes, labels, legends). Each criterion assigned severity weight: Critical (3.0), Important (2.0), Minor (1.0). Teacher committee of 3 VLMs generates alternative captions for consensus extraction following RubiCap's pipeline. MOTIVATION: CIDEr scores are 0.00-3.73 across ALL models on MMSci, demonstrating reference-based metrics are fundamentally inadequate for scientific figure captioning where identical content admits vastly different valid descriptions.\\n\\n(2) Open-ended scientific graph analysis using SciGraphQA re-annotated with rubric scoring (same 7-dimension framework, adapted for QA format).\\n\\n(3) SciCritique-5K: A new benchmark of approximately 5K scientific figure critique examples. CONSTRUCTION PIPELINE: (a) Source: ArXiv papers (2020-2025) across 5 STEM domains (physics, chemistry, biology, materials science, earth science), selected via SciCap extraction pipeline with LaTeX source compilation for high-resolution figure extraction. (b) Figure type classification using SigLIP visual encoder (CharXiv approach, cosine similarity >= 0.65) to select informative scientific figures (plots, diagrams, micrographs) and exclude decorative or trivial figures. (c) Critique generation: 3-model ensemble (GPT-4o, Claude, Gemini) generates structured critiques per figure, covering interpretation accuracy, methodological assessment, and constructive feedback. (d) Rubric dimensions (8): Visual Accuracy, Scientific Validity, Quantitative Fidelity, Methodological Context, Interpretive Depth, Structural Completeness, Domain Terminology, Constructive Suggestions — informed by SciFig's 6-dimension taxonomy and SIQA's scientific image quality framework. (e) Each dimension: 5-point ordinal scale + Essential/Important/Optional/Pitfall classification (Dr.SCI approach, averaging 14.5 rubric items per instance). (f) LLM annotation: Qwen3-32B scores each critique against rubric, with 3-run median voting and position-switching for robustness (following rDPO's protocol). (g) Expert validation: 20% subset (1K items), 3 annotators per item from STEM PhD pool across the 5 domains, 2-week calibration phase with 50 consensus examples, target Krippendorff's alpha >= 0.75 per dimension, 60-minute session limits to prevent fatigue (following SIQA protocol). (h) SIZE JUSTIFICATION: 5K is within the effective range for rubric-RL (Training AI Co-Scientists uses 6.8K; DRO uses 12.5-19.8K; Self-Rewarding Rubric RL demonstrated effectiveness with 4K), and we supplement with 10K MMSci + SciGraphQA samples for total training set of 20K+.\\n\\nCONTROLLED COMPARISON (verifiable baselines): CharXiv and SciFIBench as controlled comparisons demonstrating WHERE binary rewards suffice.\\n\\nCOMPREHENSIVE ABLATION SUITE (7 conditions to isolate each contribution):\\n(A1) Flat composite: R = w_1*R_1 + w_2*R_2 + w_3*R_3 (no gating) — tests whether gating adds value over flat combination\\n(A2) DRO-style binary rubric-gating: hard accept/reject at rollout-group level — tests continuous vs. binary gating for non-verifiable tasks, directly comparing against DRO's mechanism\\n(A3) PaLMR-style binary visual gate: R_1 binarized, indicator function gates — tests continuous vs. binary gating for visual grounding specifically\\n(A4) POW3R-style policy-aware weighting WITHOUT gating: adaptive weights but flat combination — tests whether gating or adaptive weighting is the primary contributor\\n(A5) Dynamic weighting a la RuCL: rubric weights adjust during training but without gating structure\\n(A6) Tier-1+2 only (no reasoning quality tier)\\n(A7) Tier-1+3 only (no structural quality tier)\\n\\nThis ablation suite directly addresses: (1) the negative result from Reward Design for Physical Reasoning (which tested FLAT composite on VERIFIABLE tasks — a different regime where accuracy dominates); (2) the comparison against DRO's binary gating (the most direct competitor); (3) the comparison against POW3R's adaptive weighting (the most direct competitor for dynamic reward adjustment); (4) whether continuous gating + adaptive weighting together exceed either alone.\\n\\nTHEORETICAL MOTIVATION: (1) Gradient continuity: GR3 proves continuous multiplicative gating preserves Lipschitz continuity while binary gating introduces discontinuities — especially harmful when rewards are inherently graded. (2) Gradient starvation prevention: binary gating at group level (DRO-style) can produce zero-gradient groups when all rollouts either pass or fail the gate; continuous gating always provides non-zero gradient signal proportional to gate proximity. (3) Smooth curriculum: temperature scheduling T_k(t) implements a principled version of the implicit curriculum discovered in RLVR training dynamics (arXiv:2602.14872), with warm temperatures enabling broad exploration early and cool temperatures enforcing stricter gating later. (4) Anti-exploitation: Reward Hacking in Rubric-Based RL identifies that 90% of rubric criteria are presence-based — our tiered gating ensures higher-tier content cannot compensate for lower-tier deficiencies, while continuous gates prevent all-or-nothing rejection that wastes partially valuable training signal.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1100-1500 (8xH100: ~120h LLM-based rubric annotation with 32B judge on ~15K examples, ~600h main GatedRubric-GRPO training and 7-condition ablation suite, ~180h baseline reproductions including DRO/RubiCap/PaLMR-style baselines, ~150h evaluation and analysis)\",\n      \"human_annotation\": \"~700 person-hours domain expert validation (~$17K at expert rates: 1K SciCritique validation items x 3 annotators x 25 min + 500 MMSci rubric validation items x 3 annotators x 15 min + ~100h calibration/coordination, 5 STEM PhD annotators at $22-25/hr)\",\n      \"timeline\": \"4.5-5.5 months (6 weeks dataset curation with LLM-assisted rubric annotation + expert validation including 2-week calibration, 3 weeks baseline implementation, 7 weeks GatedRubric-GRPO training and full 7-condition ablation suite, 4 weeks evaluation and paper writing)\",\n      \"estimated_gpu_cost\": \"$2,200-$3,750 (at $2-2.50/H100-hr spot pricing)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"900-1200 (Claude generates rubric templates, annotation pipelines, ablation configurations, and smooth gating module code; human validates scientific accuracy)\",\n      \"human_annotation\": \"~500 person-hours expert validation (~$12K — reduced via Claude-assisted rubric calibration and automated quality filtering)\",\n      \"timeline\": \"3.5-4.5 months (5 weeks dataset curation with Claude-assisted rubric generation and calibration, 2.5 weeks baseline setup, 6 weeks training and ablations, 3.5 weeks evaluation and writing)\",\n      \"claude_api_cost\": \"$500-850 (rubric generation for ~15K examples, annotation calibration, reward module code generation, experiment analysis — ~150M input + 30M output tokens via Sonnet batch API)\",\n      \"estimated_gpu_cost\": \"$1,800-$3,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"900-1200 (same compute floor; GPU time is irreducible)\",\n      \"human_annotation\": \"~300 person-hours minimum expert validation (~$7.5K — cannot be fully automated for scientific domain rubrics; Reward Hacking in Rubric-Based RL shows LLM judges systematically exploit 'topical alignment' without human calibration)\",\n      \"timeline\": \"3-4 months (parallel dataset curation and code development, automated hyperparameter sweeps for tau and T parameters)\",\n      \"claude_api_cost\": \"$800-1,400 (heavier annotation generation, automated rubric calibration experiments, smooth gating hyperparameter search, paper drafting — ~300M input + 60M output tokens)\",\n      \"estimated_gpu_cost\": \"$1,800-$3,000\",\n      \"speed_bottleneck\": \"Domain expert validation of scientific rubric annotations is the irreducible bottleneck. Reward Hacking in Rubric-Based RL (arXiv:2605.12474) demonstrates that even strong LLM verifiers retain 15-28% exploitation rate — systematic LLM biases in scientific rubric evaluation (preferring verbose, topically aligned but imprecise responses) require human calibration. Expert recruitment and calibration across 5 STEM domains requires 3-4 weeks minimum.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract: Jul 21 2026, paper: Jul 28 2026 — tight but feasible with focused results on 2 of 3 tasks and key ablations A1-A3)\",\n    \"WACV 2027 Round 2 (paper: Aug 27 2026 — full results including all 7 ablations and SciCritique-5K benchmark)\",\n    \"EACL 2027 (ARR submission: Aug 3 2026 — framing emphasizes rubric RL and gating formalism)\",\n    \"CVPR 2027 (estimated ~Nov 2026 — TBA, full paper with complete analysis and policy-aware adaptive variant)\",\n    \"ICLR 2027 (estimated ~Oct 2026 — TBA, full paper with theoretical analysis of continuous vs binary gating dynamics)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment (arXiv:2603.06652, Feb 2026) — binary gated hierarchical reward for verifiable tasks; our smooth gating extends this principle\",\n    \"DRO: Direct Reasoning Optimization with Rubric-Gated Constraints (arXiv:2506.13351, Jun 2025/May 2026) — BINARY rubric-gating as hard feasibility constraints for non-verifiable TEXT tasks; most direct competitor, we generalize from binary to continuous gating and from text to multimodal\",\n    \"RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning (arXiv:2603.09160, Mar 2026) — rubric-based RL for non-verifiable multimodal captioning without gating; we add hierarchical gating for scientific reasoning\",\n    \"Training AI Co-Scientists Using Rubric Rewards (arXiv:2512.23707, Dec 2025) — rubric RL (GRPO) for scientific research plan generation, text-only; demonstrates cross-domain generalization and reward model overoptimization\",\n    \"Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) — identifies three systematic exploitation patterns in medical/science rubric RL; proposes self-internalization gap (r=0.91-0.97) as verifier-free diagnostic; directly informs our anti-hacking monitoring\",\n    \"GR3: Group Relative Reward Rescaling (arXiv:2603.10535) — FORMALLY PROVES continuous multiplicative gating is a strict generalization of binary gating with superior gradient properties; key theoretical foundation for our approach\",\n    \"POW3R: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164, May 2026) — demonstrates static rubric weights are suboptimal via policy-aware contrastiveness-based adaptation; both text and multimodal; inspires our adaptive variant\",\n    \"ARES: Automated Rubric Synthesis for Scalable RL (arXiv:2605.23454, May 2026) — automated QA-rubric co-generation pipeline at scale (101K instances, 1.1M criteria); informs our rubric generation methodology\",\n    \"rDPO: Visual Preference Optimization with Rubric Rewards (arXiv:2604.13029, Apr 2026) — instance-specific rubrics for multimodal DPO with essential/additional criteria as soft gating; closest multimodal rubric competitor but uses DPO not RL\",\n    \"ClaimDiff-RL: Fine-Grained Caption RL through Visual Claim Comparison (arXiv:2605.20278, May 2026) — claim-level captioning decomposition with graded severity; architectural template for our Tier-1 visual claim verification\",\n    \"Perception-R1: Visual Perception Reward for MLLMs (arXiv:2506.07218) — adds visual perception reward to RLVR with composite reward design; verifiable tasks but demonstrates perception reward improves downstream reasoning\",\n    \"Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — demonstrates 0.69 degeneracy rate and 45-point accuracy gain from continuous fix; empirical evidence for continuous over binary rewards\",\n    \"ReDit: Reward Dithering for Improved LLM Policy Optimization (arXiv:2506.18631) — achieves GRPO-equivalent performance in 10% of training steps by making discrete rewards continuous; quantitative evidence for continuous reward advantages\",\n    \"Smooth Gate Functions for Soft Advantage Policy Optimization (arXiv:2602.19345) — formalizes properties of admissible gate functions; smooth alternatives produce more stable training\",\n    \"PEPO: Rethinking Token-Level Policy Optimization for Multimodal CoT (arXiv:2603.22847) — smooth gating for multimodal token-level advantage estimation; directly relevant to our multimodal setting\",\n    \"SR-MCR: Self-Rewarded Multimodal Coherent Reasoning (arXiv:2512.22545, Dec 2025) — five structured sub-rewards with GRPO; flat combination on verifiable tasks\",\n    \"RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, Feb 2026) — dynamic rubric weighting for curriculum; verifiable\",\n    \"RubricEM: Meta-RL with Rubric-guided Policy Decomposition (arXiv:2605.10899, May 2026) — rubric-guided policy decomposition; text-only\",\n    \"Rubric-ARM: Alternating RL for Rubric-Based Reward Modeling (arXiv:2602.01511, Feb 2026) — joint rubric generator and judge optimization; text-only\",\n    \"Reward Design for Physical Reasoning in VLMs (arXiv:2604.13993, Apr 2026) — accuracy > flat composite rubric on verifiable tasks, BUT rubric rewards improve structured reasoning quality; motivates our non-verifiable focus while acknowledging complementary value of rubric rewards\",\n    \"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards (arXiv:2602.14872, Feb 2026) — theoretical grounding for curriculum effects; our temperature scheduling implements explicit smooth curriculum\",\n    \"Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards (arXiv:2506.00103) — pairwise GenRM for text non-verifiable tasks; we extend BRPO to multimodal Tier-3\",\n    \"Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition (arXiv:2508.19652, Aug 2025) — perception-reasoning decomposition; verifiable\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv 2026) — reward hacking pathways\",\n    \"Vero: An Open RL Recipe for General Visual Reasoning (arXiv:2604.04917, Apr 2026) — task-routed rewards; verifiable\",\n    \"V-Triune: Visual Triple Unified Reinforcement Learning (arXiv:2505.18129, May 2026) — sample-level reward routing; verifiable\",\n    \"Rubric-Grounded RL: Structured Judge Rewards (arXiv:2605.08061, May 2026) — LLM-judge rubric decomposition; text-only\",\n    \"Faithful GRPO: Constrained Policy Optimization for Visual Grounding (arXiv:2604.08476, Apr 2026) — verifiable spatial tasks\",\n    \"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding (arXiv:2407.04903, NeurIPS 2024 Workshop) — 72-discipline scientific figure dataset with 742K figures\",\n    \"SciGraphQA: A Large-Scale Synthetic Multi-Turn QA Dataset for Scientific Graphs (arXiv:2308.03349) — open-ended graph analysis\",\n    \"CharXiv: Charting Gaps in Realistic Chart Understanding (NeurIPS 2024)\",\n    \"SciFIBench: Benchmarking LMMs for Scientific Figure Interpretation (NeurIPS 2024)\",\n    \"PRISMM-Bench: Measuring Multimodal Inconsistency in Scientific Papers (arXiv:2510.16505) — 384 validated inconsistencies from peer reviews; informs SciCritique-5K construction\",\n    \"SIQA: Scientific Image Quality Assessment (arXiv:2603.06700) — 4-dimension scientific image quality framework with expert annotation protocol\",\n    \"SciFig: Scientific Figure Quality Rubric (arXiv:2601.04390) — 6-dimension rubric framework for scientific figure evaluation\",\n    \"Dr.SCI: Scientific Reasoning with Rubric Item Categories (arXiv:2602.08321) — Essential/Important/Optional/Pitfall rubric categorization for STEM evaluation\"\n  ],\n  \"description\": \"We propose GatedRubric-GRPO, a framework that introduces SMOOTH CONTINUOUS hierarchical gating for non-verifiable multimodal scientific reasoning. The key technical innovation is replacing the BINARY gates used by all prior gated reward systems (DRO uses binary rubric-gates for non-verifiable text; PaLMR uses binary visual gates for verifiable multimodal) with smooth sigmoid gate functions g_k(x) = sigma((x - tau_k)/T_k), formally grounded in GR3's proof that continuous multiplicative gating is a strict mathematical generalization of binary gating that preserves Lipschitz continuity and eliminates gradient dead zones. Three epistemically dependent tiers — Tier-1: visual grounding via claim-level decomposition (ClaimDiff-RL-inspired), Tier-2: structural quality via frozen LLM-judge rubrics (ARES-inspired auto-generation, expert-calibrated), Tier-3: reasoning quality via bootstrapped pairwise comparison — are combined as R = w_1*R_1 + w_2*g_1(R_1)*R_2 + w_3*g_1(R_1)*g_2(R_2)*R_3, with an adaptive variant (GatedRubric-GRPO+) incorporating POW3R-style policy-aware weight/temperature scheduling. Anti-exploitation monitoring via self-internalization gap (from Reward Hacking in Rubric-Based RL). Training on genuinely non-verifiable scientific tasks: MMSci figure explanation (10K, re-annotated with 7-dimension rubric across 72 disciplines), SciGraphQA open-ended analysis (rubric-scored), and SciCritique-5K (new benchmark: 5K figure-critique pairs from 5 STEM domains, 8-dimension rubric, 20% expert-validated with target Krippendorff's alpha >= 0.75). A 7-condition ablation suite directly compares against DRO-style binary gating, PaLMR-style binary visual gates, POW3R-style adaptive weighting without gating, and flat composite baselines, isolating the contribution of continuous gating, hierarchical structure, and adaptive scheduling independently.\",\n  \"project_name\": \"gated_rubric_nonverif_sci_mm\",\n  \"source\": \"web_research\",\n  \"change_type\": \"major\",\n  \"changes_summary\": {\n    \"issue_1_missing_works\": \"MAJOR FIX: Integrated all 8 reviewer-identified missing works plus 7 additional works discovered during deep research. DRO (binary rubric-gating for non-verifiable text) is now positioned as the most direct competitor with explicit differentiation (binary vs continuous, text vs multimodal). Training AI Co-Scientists positioned as demonstrating rubric RL feasibility for scientific domains. Reward Hacking in Rubric-Based RL directly incorporated — its self-internalization gap becomes a core monitoring component, and its exploitation taxonomy informs our anti-hacking design. ARES informs rubric generation pipeline. POW3R's policy-aware weighting becomes a core adaptive variant (GatedRubric-GRPO+). rDPO positioned as closest multimodal rubric competitor (uses DPO not RL). Perception-R1 and ClaimDiff-RL inform Tier-1 design. Additionally integrated: GR3 (formal proof of continuous > binary gating), PEPO (smooth gating for multimodal), gradient starvation analysis, ReDit, Smooth Gate Functions paper, PRISMM-Bench, SIQA, SciFig, Dr.SCI.\",\n    \"issue_2_novelty_sharpened\": \"MAJOR FIX: Novelty fundamentally reframed from 'domain extension' to 'principled generalization with formal justification.' Three-pillar argument: (1) FORMAL — GR3 proves continuous multiplicative gating is a strict mathematical generalization of binary gating; binary gating breaks Lipschitz continuity and causes gradient dead zones (formalized by Razin et al. ICLR 2024, demonstrated empirically by gradient starvation analysis showing 0.69 degeneracy rate). (2) STRUCTURAL — scientific visual reasoning has inherently continuous graded quality, not binary correctness; binary gating (DRO/PaLMR) discards graded signal. (3) PRACTICAL — comprehensive ablation directly comparing continuous vs binary gating (A2: DRO-style, A3: PaLMR-style) will provide first empirical evidence of the gap. The continuous gating formulation R = w_1*R_1 + w_2*sigma((R_1-tau_1)/T_1)*R_2 + w_3*sigma((R_1-tau_1)/T_1)*sigma((R_2-tau_2)/T_2)*R_3 is the concrete technical contribution — temperature scheduling T_k(t) implements a principled smooth curriculum.\",\n    \"issue_3_benchmark_detailed\": \"MAJOR FIX: SciCritique expanded from 2K to 5K with complete construction pipeline specified: (a) ArXiv papers 2020-2025 across 5 STEM domains, (b) SigLIP-based figure type classification following CharXiv, (c) 3-model ensemble critique generation, (d) 8-dimension rubric informed by SciFig and SIQA frameworks, (e) Essential/Important/Optional/Pitfall categorization following Dr.SCI, (f) LLM annotation with 3-run median voting and position-switching following rDPO, (g) 20% expert validation (1K items, 3 annotators, 2-week calibration, target Krippendorff's alpha >= 0.75, 60-min sessions). Size justified by comparison: Training AI Co-Scientists uses 6.8K, DRO uses 12.5-19.8K, Self-Rewarding Rubric RL effective with 4K.\",\n    \"issue_4_mmsci_reannotation\": \"MAJOR FIX: Specified 7-dimension rubric replacing CIDEr/BLEU: Visual Accuracy, Sub-figure Coverage, Quantitative Fidelity, Scientific Terminology, Methodological Context, Interpretive Validity, Structural Description. Motivation: CIDEr scores are 0.00-3.73 across ALL models (including GPT-4o, Claude-3.5-Sonnet), demonstrating reference-based metrics are fundamentally inadequate. Pipeline: Qwen3-32B decomposes reference captions into atomic claims, converts to binary criteria with Critical/Important/Minor severity weights. Teacher committee of 3 VLMs for consensus extraction following RubiCap. Expert validation: 500 items across 10 PhD-annotated domains, target Cohen's kappa >= 0.70.\",\n    \"issue_5_reward_design_nuanced\": \"MODERATE FIX: Acknowledged that rubric rewards DO improve structured reasoning quality even in verifiable settings (per Reward Design for Physical Reasoning), not simply 'fail.' Reframed: accuracy rewards and rubric rewards capture DIFFERENT value — accuracy measures correctness, rubrics measure process quality. In non-verifiable settings where accuracy is unavailable, rubric rewards become the primary signal, and gating provides ADDITIONAL value by preventing the specific 'eloquent hallucination' failure mode documented as 'topical alignment' exploitation by Reward Hacking in Rubric-Based RL (21.1% of all exploitation instances).\",\n    \"issue_6_pow3r_engaged\": \"MAJOR FIX: POW3R's finding that static rubric weights are suboptimal is not merely acknowledged but INCORPORATED as a core adaptive variant (GatedRubric-GRPO+). Policy-aware contrastiveness-based weight and temperature adaptation with EMA smoothing and category-level normalization preserving tier structure. Additionally added as ablation A4 (POW3R-style adaptive weighting WITHOUT gating) to test whether gating or adaptive weighting is the primary contributor. This ensures we can empirically demonstrate that continuous gating + adaptive weighting together exceed either alone.\",\n    \"additional_improvements\": \"New ablation A2 directly compares against DRO-style binary gating on the same non-verifiable tasks — the most important comparison for establishing novelty. Self-internalization gap monitoring integrated from Reward Hacking paper as anti-hacking diagnostic. ClaimDiff-RL-inspired claim-level decomposition for Tier-1 visual grounding. Smooth gating temperature scheduling T_k(t) as principled curriculum mechanism. Total ablation suite expanded from 5 to 7 conditions. Reference list expanded from 25 to 36 to reflect comprehensive landscape coverage.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bfd520d-59cb-426d-857c-f02b7238825d",
  "isSidechain": false,
  "requestId": "req_011CbUGp8MAcD7pu9Ug4CzsQ",
  "type": "assistant",
  "uuid": "d6db89ab-edb3-4d2f-acb6-5fd7fb02c29d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpeFCk9EUCk3YqwvJ4kJ6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 146,
      "cache_read_input_tokens": 72953,
      "output_tokens": 10761,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10761,
          "cache_read_input_tokens": 72953,
          "cache_creation_input_tokens": 146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 146
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

_source line 97 · 2026-05-28T03:45:26.444Z_

<details><summary>↩ Tool result · reported error · `toolu_012JekAvLWWWkguCoRW7F2Gk`</summary>

```text
Claude requested permissions to write to /home/ubuntu/idea_review/revised_idea_r3.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6db89ab-edb3-4d2f-acb6-5fd7fb02c29d",
  "isSidechain": false,
  "promptId": "d0628049-5dd6-44e2-863d-4e5f7a82f317",
  "type": "user",
  "uuid": "0eecd615-3a2b-466b-986e-10c45a383a1a",
  "toolUseResult": "Error: Claude requested permissions to write to /home/ubuntu/idea_review/revised_idea_r3.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "d6db89ab-edb3-4d2f-acb6-5fd7fb02c29d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 98_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "0eecd615-3a2b-466b-986e-10c45a383a1a",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 99_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Tool call

_source line 100 · 2026-05-28T03:45:29.434Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V3fo1c2kRToBnTcjD2kSfd`</summary>

```json
{
  "command": "ls /home/ubuntu/idea_review/dispatch/",
  "description": "List dispatch directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eecd615-3a2b-466b-986e-10c45a383a1a",
  "isSidechain": false,
  "requestId": "req_011CbUH9rZD66aqAg14ZUyEq",
  "type": "assistant",
  "uuid": "be9bfe8a-32bf-4557-9dd0-639bdcb2e930",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5q3Nwoh8Wg7129R1k3895",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10812,
      "cache_read_input_tokens": 73099,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 73099,
          "cache_creation_input_tokens": 10812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10812
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

_source line 101 · 2026-05-28T03:45:29.485Z_

<details><summary>↩ Tool result · `toolu_01V3fo1c2kRToBnTcjD2kSfd`</summary>

```text
ideas
ideas_0517
ideas_0517_s3
ideas_batch5_20260519_183057
ideas_batch5_20260519_204518
ideas_batch6_20260520_025525
ideas_batch7_20260520_032225
ideas_batch_20260516_014736
ideas_batch_20260516_pass25
ideas_rerun
ideas_stage23
results
results_0517
results_0517_s3
results_batch5_20260519_183057
results_batch5_20260519_204518
results_batch6_20260520_025525
results_batch7_20260520_032225
results_batch_20260516_014736
results_batch_20260516_pass25
results_rerun
results_stage23
run_full_pipeline.py
run_multi_account.sh
run_rerun.log
run_rerun_v3.log
run_s1.log
run_s1_0517.log
run_s1_0517_s3.log
run_s1_stage23.log
run_stage23_only.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be9bfe8a-32bf-4557-9dd0-639bdcb2e930",
  "isSidechain": false,
  "promptId": "d0628049-5dd6-44e2-863d-4e5f7a82f317",
  "type": "user",
  "uuid": "5f46bfb6-a738-4d0b-9667-384d8e765a72",
  "toolUseResult": {
    "stdout": "ideas\nideas_0517\nideas_0517_s3\nideas_batch5_20260519_183057\nideas_batch5_20260519_204518\nideas_batch6_20260520_025525\nideas_batch7_20260520_032225\nideas_batch_20260516_014736\nideas_batch_20260516_pass25\nideas_rerun\nideas_stage23\nresults\nresults_0517\nresults_0517_s3\nresults_batch5_20260519_183057\nresults_batch5_20260519_204518\nresults_batch6_20260520_025525\nresults_batch7_20260520_032225\nresults_batch_20260516_014736\nresults_batch_20260516_pass25\nresults_rerun\nresults_stage23\nrun_full_pipeline.py\nrun_multi_account.sh\nrun_rerun.log\nrun_rerun_v3.log\nrun_s1.log\nrun_s1_0517.log\nrun_s1_0517_s3.log\nrun_s1_stage23.log\nrun_stage23_only.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "be9bfe8a-32bf-4557-9dd0-639bdcb2e930",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-28T03:45:32.224Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0181Didf8SqtGWG5q5TvA7fL`</summary>

```json
{
  "command": "ls /home/ubuntu/",
  "description": "List home directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f46bfb6-a738-4d0b-9667-384d8e765a72",
  "isSidechain": false,
  "requestId": "req_011CbUHA5TM4DE3fE4yhx64g",
  "type": "assistant",
  "uuid": "2a34ce06-4207-44f6-b05b-6a298e279457",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxhQw8FEfrFFoVqBKab84V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 83911,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 83911,
          "cache_creation_input_tokens": 365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 365
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

_source line 103 · 2026-05-28T03:45:32.229Z_

<details><summary>↩ Tool result · reported error · `toolu_0181Didf8SqtGWG5q5TvA7fL`</summary>

```text
ls in '/home/ubuntu' was blocked. For security, Claude Code may only list files in the allowed working directories for this session: '/home/ubuntu/idea_review'.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a34ce06-4207-44f6-b05b-6a298e279457",
  "isSidechain": false,
  "promptId": "d0628049-5dd6-44e2-863d-4e5f7a82f317",
  "type": "user",
  "uuid": "f55345e5-7d6f-4860-95db-b3e22d09ceb3",
  "toolUseResult": "Error: ls in '/home/ubuntu' was blocked. For security, Claude Code may only list files in the allowed working directories for this session: '/home/ubuntu/idea_review'.",
  "sourceToolAssistantUUID": "2a34ce06-4207-44f6-b05b-6a298e279457",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-28T03:49:14.062Z_

<details open><summary>🔧 Tool call — Write · `toolu_01AYcE4cfgUBUpSK7bA35YRZ`</summary>

```json
{
  "file_path": "/home/ubuntu/idea_review/revised_idea_r3.json",
  "content": "{\n  \"title\": \"GatedRubric-GRPO: Smooth Hierarchical Gating for Non-Verifiable Multimodal Scientific Reasoning\",\n  \"core_problem\": \"Reinforcement learning with structured rewards has advanced rapidly across two axes: (1) gated/hierarchical rewards for verifiable multimodal tasks (PaLMR, PEARL, CogFlow use binary visual gates; SR-MCR uses flat multi-component rewards), and (2) rubric-based RL for non-verifiable tasks in text-only settings (DRO uses binary rubric-gates as feasibility constraints; Rubric-ARM alternates rubric generator and judge; Training AI Co-Scientists applies rubric RL to scientific plan generation; ARES automates rubric synthesis at scale; RubricEM decomposes policy via rubrics). RubiCap extends rubric RL to non-verifiable multimodal captioning, while rDPO applies instance-specific rubrics for multimodal DPO with essential/additional criteria gating. However, ALL existing gating mechanisms — whether for visual fidelity (PaLMR), rubric feasibility (DRO), or essential criteria qualification (rDPO) — employ BINARY gates: hard accept/reject, yes/no, pass/fail. This creates a critical technical limitation: binary gating introduces discontinuities in the reward landscape that provably cause gradient vanishing and gradient starvation in policy optimization (demonstrated formally by Razin et al. ICLR 2024, and empirically by gradient starvation analysis in GRPO). The problem is especially acute for non-verifiable scientific visual reasoning — tasks like scientific figure explanation, graph-based analytical interpretation, and figure critique — where both visual grounding quality and reasoning quality are INHERENTLY CONTINUOUS and GRADED, not binary. A figure can be 70% correctly perceived; a scientific explanation can be partially valid. Binary gating discards this graded signal.\",\n  \"opportunity\": \"The landscape reveals a precise technical gap at the intersection of three established directions. Direction 1: Gated multimodal rewards exist (PaLMR, PEARL, CogFlow) but use binary gates on verifiable tasks. Direction 2: Rubric-gated non-verifiable RL exists (DRO uses binary rubric-gates as group-level feasibility constraints) but is text-only. Direction 3: Non-verifiable multimodal rubric RL exists (RubiCap for captioning, rDPO for visual preference) but without hierarchical gating. The crucial insight combines two observations: (A) Scientific visual reasoning exhibits an epistemic dependency — visual grounding is a NECESSARY CONDITION for valid reasoning (you cannot produce a correct explanation of a misperceived figure) — creating a natural gating hierarchy. (B) GR3 (arXiv:2603.10535) formally proves that continuous multiplicative gating is a STRICT MATHEMATICAL GENERALIZATION of binary gating: they are equivalent when rewards are binary, but continuous gating is provably superior when rewards are graded, because it preserves Lipschitz continuity of the reward landscape and eliminates gradient dead zones. This means continuous gating is not merely 'softening' binary gates — it enables qualitatively different training dynamics. The convergence of these observations motivates smooth-gated rubric rewards: where DRO uses binary rubric-gates (yes/no feasibility constraints) and PaLMR uses binary visual gates (pass/fail fidelity checks), we introduce smooth sigmoid gates that (1) preserve the epistemic dependency structure, (2) maintain differentiable gradient flow, and (3) naturally encode a continuous curriculum from perception to reasoning. Additionally, POW3R (arXiv:2605.20164) demonstrates that static rubric weights are suboptimal because important criteria can be saturated or unreachable at different training stages — motivating policy-aware adaptive gating. And 'Reward Hacking in Rubric-Based RL' (arXiv:2605.12474) reveals systematic exploitation patterns in rubric rewards for scientific/medical domains — motivating our integration of the self-internalization gap as a training diagnostic. Importantly, we acknowledge (per 'Reward Design for Physical Reasoning in VLMs', arXiv:2604.13993) that rubric rewards DO provide reasoning quality benefits even in verifiable settings — accuracy rewards and rubric rewards capture DIFFERENT value. In non-verifiable settings where accuracy is unavailable, rubric rewards become the primary signal, and gating's additional value is preventing the specific failure mode of visually ungrounded but linguistically polished explanations — the 'eloquent hallucination' pattern that Reward Hacking in Rubric-Based RL documents as 'topical alignment' exploitation.\",\n  \"landscape\": \"VERIFIABLE MULTIMODAL + GATED/STRUCTURED REWARDS: PaLMR (arXiv:2603.06652, Feb 2026) uses gated hierarchical reward R = S_vis·(alpha·S_ans + (1-alpha)·S_fmt) where BINARY visual fidelity gates answer reward — closest gating principle but verifiable with binary gate. SR-MCR (arXiv:2512.22545, Dec 2025) integrates five self-referential sub-rewards with GRPO — flat combination on verifiable tasks. RuCL (arXiv:2602.21628, Feb 2026) implements stratified rubric-based curriculum on verifiable multimodal tasks. Perception-R1 (arXiv:2506.07218) adds visual perception reward component to RLVR — composite reward with perception as separate weighted component, verifiable, shows explicitly rewarding perceptual accuracy improves downstream reasoning. Vision-SR1 (arXiv:2508.19652, Aug 2025) decomposes VLM reasoning into visual perception and language reasoning with self-rewarding — verifiable. Vero (arXiv:2604.04917, Apr 2026) uses task-routed rewards across 59 datasets — verifiable. V-Triune (arXiv:2505.18129, May 2026) sample-level reward routing — verifiable. Chart-RL (arXiv:2603.06958, Mar 2026) applies RLVR to chart reasoning — verifiable. PEARL (CVPR 2026) binary perception-reasoning gate. CogFlow (ICLR 2026) Visual-Gated Policy Optimization — binary gate. Faithful GRPO (arXiv:2604.08476, Apr 2026) constrains policy for spatial grounding — verifiable. NON-VERIFIABLE + GATED/STRUCTURED REWARDS (TEXT-ONLY): DRO (arXiv:2506.13351, Jun 2025/May 2026) uses BINARY rubric-gating as hard feasibility constraints at rollout-group level for non-verifiable text tasks (scientific paragraph revision, medical QA) — coverage gate + consistency gate, both binary accept/reject. Most directly overlapping with our gating-for-non-verifiable concept, but text-only and strictly binary. Training AI Co-Scientists (arXiv:2512.23707, Dec 2025) applies rubric RL (GRPO) to scientific research plan generation — instance-specific rubrics extracted from papers, reward = proportion of satisfied rubric items, text-only, demonstrates cross-domain generalization but also reward model overoptimization. Rubric-ARM (arXiv:2602.01511, Feb 2026) alternating RL for rubric-based reward modeling — text-only. Writing-Zero (arXiv:2506.00103) bridges non-verifiable tasks via pairwise GenRM — text-only. Rubric-Grounded RL (arXiv:2605.08061, May 2026) LLM-judge rubric decomposition — text-only. RubricEM (arXiv:2605.10899, May 2026) meta-RL with rubric-guided policy decomposition — text-only. ARES (arXiv:2605.23454, May 2026) automates rubric synthesis from documents at scale (101K instances, 1.1M criteria) with QA-rubric co-generation — text-only, addresses rubric generation bottleneck but no gating. NON-VERIFIABLE MULTIMODAL: RubiCap (arXiv:2603.09160, Mar 2026) rubric-guided RL for dense image captioning with dynamically generated instance-level rubrics — no gating, general captioning not scientific reasoning. ClaimDiff-RL (arXiv:2605.20278, May 2026) decomposes captioning evaluation into individual visual claims with graded severity weighting — claim-level decomposition structurally analogous to rubric dimensions, severity weighting as implicit soft gating, hybrid verifiable/non-verifiable but for general captioning. rDPO (arXiv:2604.13029, Apr 2026) applies instance-specific rubrics for multimodal DPO with essential/additional criteria functioning as soft gating — multimodal, uses DPO not GRPO, scores are {0, 0.5, 1} per criterion. BalCapRL (Mar 2026) balanced multi-objective RL for captioning. REWARD DYNAMICS AND ANTI-HACKING: Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) identifies three systematic exploitation patterns in rubric rewards for medical/science domains — partial compound (36%), implicit-as-explicit (34.6%), imprecise verification (29.4%) — and proposes self-internalization gap as verifier-free diagnostic (r=0.91-0.97 correlation with reference panel). Directly validates anti-hacking motivation and informs our monitoring strategy. POW3R (arXiv:2605.20164, May 2026) demonstrates policy-aware rubric weighting outperforms static weighting because important criteria can be saturated or unreachable — both text AND multimodal experiments. Reward Design for Physical Reasoning (arXiv:2604.13993, Apr 2026) found accuracy-based rewards outperform flat composite rubric rewards on verifiable physics tasks, BUT also found rubric rewards improve structured reasoning quality — motivates our focus on non-verifiable settings where accuracy is unavailable, while acknowledging rubric rewards provide complementary value even in verifiable settings. CONTINUOUS vs BINARY GATING THEORY: GR3 (arXiv:2603.10535) proves continuous multiplicative gating is a strict mathematical generalization of binary gating — equivalent in binary case, strictly superior when rewards are graded, because binary gating breaks Lipschitz continuity. Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) shows 0.69 degeneracy rate at group size 4 with binary rewards; continuous fix yields 45-point accuracy gain. ReDit (arXiv:2506.18631) achieves GRPO-equivalent performance in 10% of training steps by making discrete rewards continuous. Smooth Gate Functions (arXiv:2602.19345) formalizes properties of admissible gate functions and shows smooth alternatives to hard clipping produce more stable training. PEPO (arXiv:2603.22847) uses smooth gating for multimodal token-level advantage estimation, directly relevant to our multimodal setting. THE GAP: No work combines (1) CONTINUOUS hierarchical gating (all existing gating is binary) with (2) non-verifiable multimodal settings with (3) scientific reasoning requiring domain-specific rubrics with (4) policy-aware adaptive weight/threshold scheduling.\",\n  \"inspired_by\": \"Intersection gap with principled generalization: DRO provides binary rubric-gating for non-verifiable text tasks; PaLMR provides binary visual gating for verifiable multimodal tasks; GR3 proves continuous gating is a strict mathematical generalization of binary gating with provably better gradient properties. We synthesize these into continuous hierarchical gating for non-verifiable multimodal scientific reasoning. The key theoretical insight: binary gating introduces gradient discontinuities that are especially harmful when rewards are inherently graded (as in scientific reasoning rubrics) — continuous gating eliminates this while preserving the epistemic dependency structure (perception to structure to reasoning). POW3R demonstrates static rubric weights are suboptimal — we integrate policy-aware adaptation. Reward Hacking in Rubric-Based RL identifies exploitation patterns in scientific/medical rubric RL — we integrate self-internalization gap monitoring. ClaimDiff-RL provides the architectural template for claim-level visual verification in Tier-1. Building block: GRPO's compatibility with multi-reward designs (proven by SR-MCR, DRO, Vero, V-Triune, POW3R) makes it the natural optimization backbone.\",\n  \"approach\": \"We propose GatedRubric-GRPO, which introduces CONTINUOUS hierarchical gating for non-verifiable multimodal scientific reasoning within standard GRPO training on Qwen3-VL-8B. The key technical innovation over existing gated approaches (DRO's binary rubric-gates, PaLMR's binary visual gates) is replacing binary indicator functions with smooth sigmoid gates, formally grounded in GR3's proof that continuous gating is a strict generalization of binary gating.\\n\\nSMOOTH GATING FORMULATION: The composite reward decomposes into three epistemically dependent tiers:\\n\\nR = w_1*R_1 + w_2*g_1(R_1)*R_2 + w_3*g_1(R_1)*g_2(R_2)*R_3\\n\\nwhere g_k(x) = sigma((x - tau_k) / T_k) are smooth sigmoid gate functions with temperature T_k controlling sharpness. Key properties: (1) As T_k approaches 0, g_k approaches binary indicator, recovering DRO/PaLMR-style hard gating — our formulation is a strict generalization. (2) For finite T_k, g_k preserves Lipschitz continuity of the reward landscape, eliminating gradient dead zones at thresholds. (3) T_k can be scheduled during training (warm to cool), implementing an explicit smooth curriculum from exploration to exploitation.\\n\\nTIER-1 (Visual Grounding, continuous 0-1): Inspired by ClaimDiff-RL's claim-level decomposition and Perception-R1's visual perception reward, we decompose model outputs into atomic visual claims and verify each against the figure. Programmatic checks (element identification, data reading, spatial description) combined with lightweight LLM verification produce a continuous grounding score. This extends Perception-R1's approach (binary verification of pre-extracted annotations) to open-ended claim generation with graded scoring.\\n\\nTIER-2 (Structural Quality, soft-gated on Tier-1): A frozen LLM judge (Qwen3-32B) evaluates logical coherence, evidence-claim alignment, domain terminology, and visual-textual consistency using discipline-specific rubric templates. Rubric templates are auto-generated following ARES's pipeline adapted for scientific figures, then expert-calibrated. Soft-gated by g_1(R_1): when visual grounding is poor, structural quality reward is smoothly attenuated (NOT zeroed as in binary gating), providing gradient signal proportional to grounding quality.\\n\\nTIER-3 (Reasoning Quality, soft-gated on Tier-1 AND Tier-2): Bootstrapped pairwise comparison within GRPO rollout groups assesses analytical depth, interpretive insight, explanation completeness — extending Writing-Zero's BRPO to multimodal. Soft-gated by g_1(R_1)*g_2(R_2).\\n\\nPOLICY-AWARE ADAPTIVE VARIANT (GatedRubric-GRPO+): Inspired by POW3R's finding that static rubric weights are suboptimal, we additionally implement an adaptive variant where: (a) per-criterion contrastiveness is computed from rollout variance within each GRPO group, (b) weights w_1, w_2, w_3 and temperatures T_1, T_2 are rescaled based on criterion contrastiveness with EMA smoothing, and (c) category-level normalization preserves the tier structure. This ensures training pressure shifts from saturated criteria (e.g., basic element identification) to actionable criteria (e.g., interpretive depth) as the policy improves.\\n\\nANTI-HACKING MONITORING: Integrating the self-internalization gap from 'Reward Hacking in Rubric-Based RL', we compute the divergence between the policy's prompt-only distribution and rubric-conditioned distribution using only policy log-probabilities. This provides a verifier-free early-stopping diagnostic (r=0.91-0.97 correlation with reference panel in their experiments) to detect when the policy begins exploiting rubric structure rather than genuinely improving.\\n\\nTRAINING TASKS (genuinely non-verifiable):\\n\\n(1) Scientific figure explanation generation using MMSci (Nature Communications figures, 72 disciplines) — 10K stratified sample across 18 discipline groups. RE-ANNOTATION PIPELINE: Reference captions decomposed into atomic claims by Qwen3-32B, converted to per-figure rubric criteria across 7 dimensions: Visual Accuracy (correct identification of visual elements), Sub-figure Coverage (all panels addressed), Quantitative Fidelity (numerical values, trends, comparisons), Scientific Terminology (domain-appropriate vocabulary), Methodological Context (experimental/computational technique), Interpretive Validity (scientifically sound conclusions), Structural Description (axes, labels, legends). Each criterion assigned severity weight: Critical (3.0), Important (2.0), Minor (1.0). Teacher committee of 3 VLMs generates alternative captions for consensus extraction following RubiCap's pipeline. MOTIVATION: CIDEr scores are 0.00-3.73 across ALL models on MMSci, demonstrating reference-based metrics are fundamentally inadequate for scientific figure captioning where identical content admits vastly different valid descriptions.\\n\\n(2) Open-ended scientific graph analysis using SciGraphQA re-annotated with rubric scoring (same 7-dimension framework, adapted for QA format).\\n\\n(3) SciCritique-5K: A new benchmark of approximately 5K scientific figure critique examples. CONSTRUCTION PIPELINE: (a) Source: ArXiv papers (2020-2025) across 5 STEM domains (physics, chemistry, biology, materials science, earth science), selected via SciCap extraction pipeline with LaTeX source compilation for high-resolution figure extraction. (b) Figure type classification using SigLIP visual encoder (CharXiv approach, cosine similarity >= 0.65) to select informative scientific figures (plots, diagrams, micrographs) and exclude decorative or trivial figures. (c) Critique generation: 3-model ensemble (GPT-4o, Claude, Gemini) generates structured critiques per figure, covering interpretation accuracy, methodological assessment, and constructive feedback. (d) Rubric dimensions (8): Visual Accuracy, Scientific Validity, Quantitative Fidelity, Methodological Context, Interpretive Depth, Structural Completeness, Domain Terminology, Constructive Suggestions — informed by SciFig's 6-dimension taxonomy and SIQA's scientific image quality framework. (e) Each dimension: 5-point ordinal scale + Essential/Important/Optional/Pitfall classification (Dr.SCI approach, averaging 14.5 rubric items per instance). (f) LLM annotation: Qwen3-32B scores each critique against rubric, with 3-run median voting and position-switching for robustness (following rDPO's protocol). (g) Expert validation: 20% subset (1K items), 3 annotators per item from STEM PhD pool across the 5 domains, 2-week calibration phase with 50 consensus examples, target Krippendorff's alpha >= 0.75 per dimension, 60-minute session limits to prevent fatigue (following SIQA protocol). (h) SIZE JUSTIFICATION: 5K is within the effective range for rubric-RL (Training AI Co-Scientists uses 6.8K; DRO uses 12.5-19.8K; Self-Rewarding Rubric RL demonstrated effectiveness with 4K), and we supplement with 10K MMSci + SciGraphQA samples for total training set of 20K+.\\n\\nCONTROLLED COMPARISON (verifiable baselines): CharXiv and SciFIBench as controlled comparisons demonstrating WHERE binary rewards suffice.\\n\\nCOMPREHENSIVE ABLATION SUITE (7 conditions to isolate each contribution):\\n(A1) Flat composite: R = w_1*R_1 + w_2*R_2 + w_3*R_3 (no gating) — tests whether gating adds value over flat combination\\n(A2) DRO-style binary rubric-gating: hard accept/reject at rollout-group level — tests continuous vs. binary gating for non-verifiable tasks, directly comparing against DRO's mechanism\\n(A3) PaLMR-style binary visual gate: R_1 binarized, indicator function gates — tests continuous vs. binary gating for visual grounding specifically\\n(A4) POW3R-style policy-aware weighting WITHOUT gating: adaptive weights but flat combination — tests whether gating or adaptive weighting is the primary contributor\\n(A5) Dynamic weighting a la RuCL: rubric weights adjust during training but without gating structure\\n(A6) Tier-1+2 only (no reasoning quality tier)\\n(A7) Tier-1+3 only (no structural quality tier)\\n\\nThis ablation suite directly addresses: (1) the negative result from Reward Design for Physical Reasoning (which tested FLAT composite on VERIFIABLE tasks — a different regime where accuracy dominates); (2) the comparison against DRO's binary gating (the most direct competitor); (3) the comparison against POW3R's adaptive weighting (the most direct competitor for dynamic reward adjustment); (4) whether continuous gating + adaptive weighting together exceed either alone.\\n\\nTHEORETICAL MOTIVATION: (1) Gradient continuity: GR3 proves continuous multiplicative gating preserves Lipschitz continuity while binary gating introduces discontinuities — especially harmful when rewards are inherently graded. (2) Gradient starvation prevention: binary gating at group level (DRO-style) can produce zero-gradient groups when all rollouts either pass or fail the gate; continuous gating always provides non-zero gradient signal proportional to gate proximity. (3) Smooth curriculum: temperature scheduling T_k(t) implements a principled version of the implicit curriculum discovered in RLVR training dynamics (arXiv:2602.14872), with warm temperatures enabling broad exploration early and cool temperatures enforcing stricter gating later. (4) Anti-exploitation: Reward Hacking in Rubric-Based RL identifies that 90% of rubric criteria are presence-based — our tiered gating ensures higher-tier content cannot compensate for lower-tier deficiencies, while continuous gates prevent all-or-nothing rejection that wastes partially valuable training signal.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1100-1500 (8xH100: ~120h LLM-based rubric annotation with 32B judge on ~15K examples, ~600h main GatedRubric-GRPO training and 7-condition ablation suite, ~180h baseline reproductions including DRO/RubiCap/PaLMR-style baselines, ~150h evaluation and analysis)\",\n      \"human_annotation\": \"~700 person-hours domain expert validation (~$17K at expert rates: 1K SciCritique validation items x 3 annotators x 25 min + 500 MMSci rubric validation items x 3 annotators x 15 min + ~100h calibration/coordination, 5 STEM PhD annotators at $22-25/hr)\",\n      \"timeline\": \"4.5-5.5 months (6 weeks dataset curation with LLM-assisted rubric annotation + expert validation including 2-week calibration, 3 weeks baseline implementation, 7 weeks GatedRubric-GRPO training and full 7-condition ablation suite, 4 weeks evaluation and paper writing)\",\n      \"estimated_gpu_cost\": \"$2,200-$3,750 (at $2-2.50/H100-hr spot pricing)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"900-1200 (Claude generates rubric templates, annotation pipelines, ablation configurations, and smooth gating module code; human validates scientific accuracy)\",\n      \"human_annotation\": \"~500 person-hours expert validation (~$12K — reduced via Claude-assisted rubric calibration and automated quality filtering)\",\n      \"timeline\": \"3.5-4.5 months (5 weeks dataset curation with Claude-assisted rubric generation and calibration, 2.5 weeks baseline setup, 6 weeks training and ablations, 3.5 weeks evaluation and writing)\",\n      \"claude_api_cost\": \"$500-850 (rubric generation for ~15K examples, annotation calibration, reward module code generation, experiment analysis — ~150M input + 30M output tokens via Sonnet batch API)\",\n      \"estimated_gpu_cost\": \"$1,800-$3,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"900-1200 (same compute floor; GPU time is irreducible)\",\n      \"human_annotation\": \"~300 person-hours minimum expert validation (~$7.5K — cannot be fully automated for scientific domain rubrics; Reward Hacking in Rubric-Based RL shows LLM judges systematically exploit 'topical alignment' without human calibration)\",\n      \"timeline\": \"3-4 months (parallel dataset curation and code development, automated hyperparameter sweeps for tau and T parameters)\",\n      \"claude_api_cost\": \"$800-1,400 (heavier annotation generation, automated rubric calibration experiments, smooth gating hyperparameter search, paper drafting — ~300M input + 60M output tokens)\",\n      \"estimated_gpu_cost\": \"$1,800-$3,000\",\n      \"speed_bottleneck\": \"Domain expert validation of scientific rubric annotations is the irreducible bottleneck. Reward Hacking in Rubric-Based RL (arXiv:2605.12474) demonstrates that even strong LLM verifiers retain 15-28% exploitation rate — systematic LLM biases in scientific rubric evaluation (preferring verbose, topically aligned but imprecise responses) require human calibration. Expert recruitment and calibration across 5 STEM domains requires 3-4 weeks minimum.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract: Jul 21 2026, paper: Jul 28 2026 — tight but feasible with focused results on 2 of 3 tasks and key ablations A1-A3)\",\n    \"WACV 2027 Round 2 (paper: Aug 27 2026 — full results including all 7 ablations and SciCritique-5K benchmark)\",\n    \"EACL 2027 (ARR submission: Aug 3 2026 — framing emphasizes rubric RL and gating formalism)\",\n    \"CVPR 2027 (estimated ~Nov 2026 — TBA, full paper with complete analysis and policy-aware adaptive variant)\",\n    \"ICLR 2027 (estimated ~Oct 2026 — TBA, full paper with theoretical analysis of continuous vs binary gating dynamics)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment (arXiv:2603.06652, Feb 2026) — binary gated hierarchical reward for verifiable tasks; our smooth gating extends this principle\",\n    \"DRO: Direct Reasoning Optimization with Rubric-Gated Constraints (arXiv:2506.13351, Jun 2025/May 2026) — BINARY rubric-gating as hard feasibility constraints for non-verifiable TEXT tasks; most direct competitor, we generalize from binary to continuous gating and from text to multimodal\",\n    \"RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning (arXiv:2603.09160, Mar 2026) — rubric-based RL for non-verifiable multimodal captioning without gating; we add hierarchical gating for scientific reasoning\",\n    \"Training AI Co-Scientists Using Rubric Rewards (arXiv:2512.23707, Dec 2025) — rubric RL (GRPO) for scientific research plan generation, text-only; demonstrates cross-domain generalization and reward model overoptimization\",\n    \"Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) — identifies three systematic exploitation patterns in medical/science rubric RL; proposes self-internalization gap (r=0.91-0.97) as verifier-free diagnostic; directly informs our anti-hacking monitoring\",\n    \"GR3: Group Relative Reward Rescaling (arXiv:2603.10535) — FORMALLY PROVES continuous multiplicative gating is a strict generalization of binary gating with superior gradient properties; key theoretical foundation for our approach\",\n    \"POW3R: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164, May 2026) — demonstrates static rubric weights are suboptimal via policy-aware contrastiveness-based adaptation; both text and multimodal; inspires our adaptive variant\",\n    \"ARES: Automated Rubric Synthesis for Scalable RL (arXiv:2605.23454, May 2026) — automated QA-rubric co-generation pipeline at scale (101K instances, 1.1M criteria); informs our rubric generation methodology\",\n    \"rDPO: Visual Preference Optimization with Rubric Rewards (arXiv:2604.13029, Apr 2026) — instance-specific rubrics for multimodal DPO with essential/additional criteria as soft gating; closest multimodal rubric competitor but uses DPO not RL\",\n    \"ClaimDiff-RL: Fine-Grained Caption RL through Visual Claim Comparison (arXiv:2605.20278, May 2026) — claim-level captioning decomposition with graded severity; architectural template for our Tier-1 visual claim verification\",\n    \"Perception-R1: Visual Perception Reward for MLLMs (arXiv:2506.07218) — adds visual perception reward to RLVR with composite reward design; verifiable tasks but demonstrates perception reward improves downstream reasoning\",\n    \"Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — demonstrates 0.69 degeneracy rate and 45-point accuracy gain from continuous fix; empirical evidence for continuous over binary rewards\",\n    \"ReDit: Reward Dithering for Improved LLM Policy Optimization (arXiv:2506.18631) — achieves GRPO-equivalent performance in 10% of training steps by making discrete rewards continuous; quantitative evidence for continuous reward advantages\",\n    \"Smooth Gate Functions for Soft Advantage Policy Optimization (arXiv:2602.19345) — formalizes properties of admissible gate functions; smooth alternatives produce more stable training\",\n    \"PEPO: Rethinking Token-Level Policy Optimization for Multimodal CoT (arXiv:2603.22847) — smooth gating for multimodal token-level advantage estimation; directly relevant to our multimodal setting\",\n    \"SR-MCR: Self-Rewarded Multimodal Coherent Reasoning (arXiv:2512.22545, Dec 2025) — five structured sub-rewards with GRPO; flat combination on verifiable tasks\",\n    \"RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, Feb 2026) — dynamic rubric weighting for curriculum; verifiable\",\n    \"RubricEM: Meta-RL with Rubric-guided Policy Decomposition (arXiv:2605.10899, May 2026) — rubric-guided policy decomposition; text-only\",\n    \"Rubric-ARM: Alternating RL for Rubric-Based Reward Modeling (arXiv:2602.01511, Feb 2026) — joint rubric generator and judge optimization; text-only\",\n    \"Reward Design for Physical Reasoning in VLMs (arXiv:2604.13993, Apr 2026) — accuracy > flat composite rubric on verifiable tasks, BUT rubric rewards improve structured reasoning quality; motivates our non-verifiable focus while acknowledging complementary value of rubric rewards\",\n    \"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards (arXiv:2602.14872, Feb 2026) — theoretical grounding for curriculum effects; our temperature scheduling implements explicit smooth curriculum\",\n    \"Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards (arXiv:2506.00103) — pairwise GenRM for text non-verifiable tasks; we extend BRPO to multimodal Tier-3\",\n    \"Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition (arXiv:2508.19652, Aug 2025) — perception-reasoning decomposition; verifiable\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv 2026) — reward hacking pathways\",\n    \"Vero: An Open RL Recipe for General Visual Reasoning (arXiv:2604.04917, Apr 2026) — task-routed rewards; verifiable\",\n    \"V-Triune: Visual Triple Unified Reinforcement Learning (arXiv:2505.18129, May 2026) — sample-level reward routing; verifiable\",\n    \"Rubric-Grounded RL: Structured Judge Rewards (arXiv:2605.08061, May 2026) — LLM-judge rubric decomposition; text-only\",\n    \"Faithful GRPO: Constrained Policy Optimization for Visual Grounding (arXiv:2604.08476, Apr 2026) — verifiable spatial tasks\",\n    \"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding (arXiv:2407.04903, NeurIPS 2024 Workshop) — 72-discipline scientific figure dataset with 742K figures\",\n    \"SciGraphQA: A Large-Scale Synthetic Multi-Turn QA Dataset for Scientific Graphs (arXiv:2308.03349) — open-ended graph analysis\",\n    \"CharXiv: Charting Gaps in Realistic Chart Understanding (NeurIPS 2024)\",\n    \"SciFIBench: Benchmarking LMMs for Scientific Figure Interpretation (NeurIPS 2024)\",\n    \"PRISMM-Bench: Measuring Multimodal Inconsistency in Scientific Papers (arXiv:2510.16505) — 384 validated inconsistencies from peer reviews; informs SciCritique-5K construction\",\n    \"SIQA: Scientific Image Quality Assessment (arXiv:2603.06700) — 4-dimension scientific image quality framework with expert annotation protocol\",\n    \"SciFig: Scientific Figure Quality Rubric (arXiv:2601.04390) — 6-dimension rubric framework for scientific figure evaluation\",\n    \"Dr.SCI: Scientific Reasoning with Rubric Item Categories (arXiv:2602.08321) — Essential/Important/Optional/Pitfall rubric categorization for STEM evaluation\"\n  ],\n  \"description\": \"We propose GatedRubric-GRPO, a framework that introduces SMOOTH CONTINUOUS hierarchical gating for non-verifiable multimodal scientific reasoning. The key technical innovation is replacing the BINARY gates used by all prior gated reward systems (DRO uses binary rubric-gates for non-verifiable text; PaLMR uses binary visual gates for verifiable multimodal) with smooth sigmoid gate functions g_k(x) = sigma((x - tau_k)/T_k), formally grounded in GR3's proof that continuous multiplicative gating is a strict mathematical generalization of binary gating that preserves Lipschitz continuity and eliminates gradient dead zones. Three epistemically dependent tiers — Tier-1: visual grounding via claim-level decomposition (ClaimDiff-RL-inspired), Tier-2: structural quality via frozen LLM-judge rubrics (ARES-inspired auto-generation, expert-calibrated), Tier-3: reasoning quality via bootstrapped pairwise comparison — are combined as R = w_1*R_1 + w_2*g_1(R_1)*R_2 + w_3*g_1(R_1)*g_2(R_2)*R_3, with an adaptive variant (GatedRubric-GRPO+) incorporating POW3R-style policy-aware weight/temperature scheduling. Anti-exploitation monitoring via self-internalization gap (from Reward Hacking in Rubric-Based RL). Training on genuinely non-verifiable scientific tasks: MMSci figure explanation (10K, re-annotated with 7-dimension rubric across 72 disciplines), SciGraphQA open-ended analysis (rubric-scored), and SciCritique-5K (new benchmark: 5K figure-critique pairs from 5 STEM domains, 8-dimension rubric, 20% expert-validated with target Krippendorff's alpha >= 0.75). A 7-condition ablation suite directly compares against DRO-style binary gating, PaLMR-style binary visual gates, POW3R-style adaptive weighting without gating, and flat composite baselines, isolating the contribution of continuous gating, hierarchical structure, and adaptive scheduling independently.\",\n  \"project_name\": \"gated_rubric_nonverif_sci_mm\",\n  \"source\": \"web_research\",\n  \"change_type\": \"major\",\n  \"changes_summary\": {\n    \"issue_1_missing_works\": \"MAJOR FIX: Integrated all 8 reviewer-identified missing works plus 7 additional works discovered during deep research. DRO (binary rubric-gating for non-verifiable text) is now positioned as the most direct competitor with explicit differentiation (binary vs continuous, text vs multimodal). Training AI Co-Scientists positioned as demonstrating rubric RL feasibility for scientific domains. Reward Hacking in Rubric-Based RL directly incorporated — its self-internalization gap becomes a core monitoring component, and its exploitation taxonomy informs our anti-hacking design. ARES informs rubric generation pipeline. POW3R's policy-aware weighting becomes a core adaptive variant (GatedRubric-GRPO+). rDPO positioned as closest multimodal rubric competitor (uses DPO not RL). Perception-R1 and ClaimDiff-RL inform Tier-1 design. Additionally integrated: GR3 (formal proof of continuous > binary gating), PEPO (smooth gating for multimodal), gradient starvation analysis, ReDit, Smooth Gate Functions paper, PRISMM-Bench, SIQA, SciFig, Dr.SCI.\",\n    \"issue_2_novelty_sharpened\": \"MAJOR FIX: Novelty fundamentally reframed from 'domain extension' to 'principled generalization with formal justification.' Three-pillar argument: (1) FORMAL — GR3 proves continuous multiplicative gating is a strict mathematical generalization of binary gating; binary gating breaks Lipschitz continuity and causes gradient dead zones (formalized by Razin et al. ICLR 2024, demonstrated empirically by gradient starvation analysis showing 0.69 degeneracy rate). (2) STRUCTURAL — scientific visual reasoning has inherently continuous graded quality, not binary correctness; binary gating (DRO/PaLMR) discards graded signal. (3) PRACTICAL — comprehensive ablation directly comparing continuous vs binary gating (A2: DRO-style, A3: PaLMR-style) will provide first empirical evidence of the gap. The continuous gating formulation R = w_1*R_1 + w_2*sigma((R_1-tau_1)/T_1)*R_2 + w_3*sigma((R_1-tau_1)/T_1)*sigma((R_2-tau_2)/T_2)*R_3 is the concrete technical contribution — temperature scheduling T_k(t) implements a principled smooth curriculum.\",\n    \"issue_3_benchmark_detailed\": \"MAJOR FIX: SciCritique expanded from 2K to 5K with complete construction pipeline specified: (a) ArXiv papers 2020-2025 across 5 STEM domains, (b) SigLIP-based figure type classification following CharXiv, (c) 3-model ensemble critique generation, (d) 8-dimension rubric informed by SciFig and SIQA frameworks, (e) Essential/Important/Optional/Pitfall categorization following Dr.SCI, (f) LLM annotation with 3-run median voting and position-switching following rDPO, (g) 20% expert validation (1K items, 3 annotators, 2-week calibration, target Krippendorff's alpha >= 0.75, 60-min sessions). Size justified by comparison: Training AI Co-Scientists uses 6.8K, DRO uses 12.5-19.8K, Self-Rewarding Rubric RL effective with 4K.\",\n    \"issue_4_mmsci_reannotation\": \"MAJOR FIX: Specified 7-dimension rubric replacing CIDEr/BLEU: Visual Accuracy, Sub-figure Coverage, Quantitative Fidelity, Scientific Terminology, Methodological Context, Interpretive Validity, Structural Description. Motivation: CIDEr scores are 0.00-3.73 across ALL models (including GPT-4o, Claude-3.5-Sonnet), demonstrating reference-based metrics are fundamentally inadequate. Pipeline: Qwen3-32B decomposes reference captions into atomic claims, converts to binary criteria with Critical/Important/Minor severity weights. Teacher committee of 3 VLMs for consensus extraction following RubiCap. Expert validation: 500 items across 10 PhD-annotated domains, target Cohen's kappa >= 0.70.\",\n    \"issue_5_reward_design_nuanced\": \"MODERATE FIX: Acknowledged that rubric rewards DO improve structured reasoning quality even in verifiable settings (per Reward Design for Physical Reasoning), not simply 'fail.' Reframed: accuracy rewards and rubric rewards capture DIFFERENT value — accuracy measures correctness, rubrics measure process quality. In non-verifiable settings where accuracy is unavailable, rubric rewards become the primary signal, and gating provides ADDITIONAL value by preventing the specific 'eloquent hallucination' failure mode documented as 'topical alignment' exploitation by Reward Hacking in Rubric-Based RL (21.1% of all exploitation instances).\",\n    \"issue_6_pow3r_engaged\": \"MAJOR FIX: POW3R's finding that static rubric weights are suboptimal is not merely acknowledged but INCORPORATED as a core adaptive variant (GatedRubric-GRPO+). Policy-aware contrastiveness-based weight and temperature adaptation with EMA smoothing and category-level normalization preserving tier structure. Additionally added as ablation A4 (POW3R-style adaptive weighting WITHOUT gating) to test whether gating or adaptive weighting is the primary contributor. This ensures we can empirically demonstrate that continuous gating + adaptive weighting together exceed either alone.\",\n    \"additional_improvements\": \"New ablation A2 directly compares against DRO-style binary gating on the same non-verifiable tasks — the most important comparison for establishing novelty. Self-internalization gap monitoring integrated from Reward Hacking paper as anti-hacking diagnostic. ClaimDiff-RL-inspired claim-level decomposition for Tier-1 visual grounding. Smooth gating temperature scheduling T_k(t) as principled curriculum mechanism. Total ablation suite expanded from 5 to 7 conditions. Reference list expanded from 25 to 36 to reflect comprehensive landscape coverage.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f55345e5-7d6f-4860-95db-b3e22d09ceb3",
  "isSidechain": false,
  "requestId": "req_011CbUHAHTut63ftpgycq2Sv",
  "type": "assistant",
  "uuid": "1922f7d2-afc4-4c90-b571-eb14d679a329",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxP3amtGYBUjuse921h8bD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 84276,
      "output_tokens": 10761,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 133,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10761,
          "cache_read_input_tokens": 84276,
          "cache_creation_input_tokens": 133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 133
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

_source line 105 · 2026-05-28T03:49:14.068Z_

<details><summary>↩ Tool result · reported error · `toolu_01AYcE4cfgUBUpSK7bA35YRZ`</summary>

```text
Claude requested permissions to write to /home/ubuntu/idea_review/revised_idea_r3.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1922f7d2-afc4-4c90-b571-eb14d679a329",
  "isSidechain": false,
  "promptId": "d0628049-5dd6-44e2-863d-4e5f7a82f317",
  "type": "user",
  "uuid": "f12b37dc-ac20-41d4-a333-12d3e8b74592",
  "toolUseResult": "Error: Claude requested permissions to write to /home/ubuntu/idea_review/revised_idea_r3.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "1922f7d2-afc4-4c90-b571-eb14d679a329",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 106_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "f12b37dc-ac20-41d4-a333-12d3e8b74592",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 107_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Assistant

_source line 108 · 2026-05-28T03:49:17.131Z_

<details><summary>Logged reasoning block</summary>

```text
It seems I don't have write permission. Let me just output the complete JSON directly in my response instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f12b37dc-ac20-41d4-a333-12d3e8b74592",
  "isSidechain": false,
  "requestId": "req_011CbUHSeKisx5qx5T8BzFqZ",
  "type": "assistant",
  "uuid": "4f5f21ad-5efa-47da-b27a-533e702a485f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqGAqJbuxBZWx122fVNTF3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10812,
      "cache_read_input_tokens": 84409,
      "output_tokens": 10005,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10005,
          "cache_read_input_tokens": 84409,
          "cache_creation_input_tokens": 10812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10812
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

_source line 109 · 2026-05-28T03:52:38.648Z_

The file write is being blocked by permissions. Let me output the complete revised idea directly:

---

Here is the **complete revised research idea** (Round 3, major revision), addressing all 6 reviewer issues with deep research backing:

```json
{
  "title": "GatedRubric-GRPO: Smooth Hierarchical Gating for Non-Verifiable Multimodal Scientific Reasoning",
  "core_problem": "Reinforcement learning with structured rewards has advanced rapidly across two axes: (1) gated/hierarchical rewards for verifiable multimodal tasks (PaLMR, PEARL, CogFlow use binary visual gates; SR-MCR uses flat multi-component rewards), and (2) rubric-based RL for non-verifiable tasks in text-only settings (DRO uses binary rubric-gates as feasibility constraints; Rubric-ARM alternates rubric generator and judge; Training AI Co-Scientists applies rubric RL to scientific plan generation; ARES automates rubric synthesis at scale; RubricEM decomposes policy via rubrics). RubiCap extends rubric RL to non-verifiable multimodal captioning, while rDPO applies instance-specific rubrics for multimodal DPO with essential/additional criteria gating. However, ALL existing gating mechanisms — whether for visual fidelity (PaLMR), rubric feasibility (DRO), or essential criteria qualification (rDPO) — employ BINARY gates: hard accept/reject, yes/no, pass/fail. This creates a critical technical limitation: binary gating introduces discontinuities in the reward landscape that provably cause gradient vanishing and gradient starvation in policy optimization (demonstrated formally by Razin et al. ICLR 2024, and empirically by gradient starvation analysis in GRPO). The problem is especially acute for non-verifiable scientific visual reasoning — tasks like scientific figure explanation, graph-based analytical interpretation, and figure critique — where both visual grounding quality and reasoning quality are INHERENTLY CONTINUOUS and GRADED, not binary. A figure can be 70% correctly perceived; a scientific explanation can be partially valid. Binary gating discards this graded signal.",
  "opportunity": "The landscape reveals a precise technical gap at the intersection of three established directions. Direction 1: Gated multimodal rewards exist (PaLMR, PEARL, CogFlow) but use binary gates on verifiable tasks. Direction 2: Rubric-gated non-verifiable RL exists (DRO uses binary rubric-gates as group-level feasibility constraints) but is text-only. Direction 3: Non-verifiable multimodal rubric RL exists (RubiCap for captioning, rDPO for visual preference) but without hierarchical gating. The crucial insight combines two observations: (A) Scientific visual reasoning exhibits an epistemic dependency — visual grounding is a NECESSARY CONDITION for valid reasoning (you cannot produce a correct explanation of a misperceived figure) — creating a natural gating hierarchy. (B) GR3 (arXiv:2603.10535) formally proves that continuous multiplicative gating is a STRICT MATHEMATICAL GENERALIZATION of binary gating: they are equivalent when rewards are binary, but continuous gating is provably superior when rewards are graded, because it preserves Lipschitz continuity of the reward landscape and eliminates gradient dead zones. This means continuous gating is not merely 'softening' binary gates — it enables qualitatively different training dynamics. The convergence of these observations motivates smooth-gated rubric rewards: where DRO uses binary rubric-gates (yes/no feasibility constraints) and PaLMR uses binary visual gates (pass/fail fidelity checks), we introduce smooth sigmoid gates that (1) preserve the epistemic dependency structure, (2) maintain differentiable gradient flow, and (3) naturally encode a continuous curriculum from perception to reasoning. Additionally, POW3R (arXiv:2605.20164) demonstrates that static rubric weights are suboptimal because important criteria can be saturated or unreachable at different training stages — motivating policy-aware adaptive gating. And 'Reward Hacking in Rubric-Based RL' (arXiv:2605.12474) reveals systematic exploitation patterns in rubric rewards for scientific/medical domains — motivating our integration of the self-internalization gap as a training diagnostic. Importantly, we acknowledge (per 'Reward Design for Physical Reasoning in VLMs', arXiv:2604.13993) that rubric rewards DO provide reasoning quality benefits even in verifiable settings — accuracy rewards and rubric rewards capture DIFFERENT value. In non-verifiable settings where accuracy is unavailable, rubric rewards become the primary signal, and gating's additional value is preventing the specific failure mode of visually ungrounded but linguistically polished explanations — the 'eloquent hallucination' pattern that Reward Hacking in Rubric-Based RL documents as 'topical alignment' exploitation.",
  "landscape": "VERIFIABLE MULTIMODAL + GATED/STRUCTURED REWARDS: PaLMR (arXiv:2603.06652, Feb 2026) uses gated hierarchical reward R = S_vis·(α·S_ans + (1-α)·S_fmt) where BINARY visual fidelity gates answer reward — closest gating principle but verifiable with binary gate. SR-MCR (arXiv:2512.22545, Dec 2025) integrates five self-referential sub-rewards with GRPO — flat combination on verifiable tasks. RuCL (arXiv:2602.21628, Feb 2026) implements stratified rubric-based curriculum on verifiable multimodal tasks. Perception-R1 (arXiv:2506.07218) adds visual perception reward component to RLVR — composite reward with perception as separate weighted component, verifiable, shows explicitly rewarding perceptual accuracy improves downstream reasoning. Vision-SR1 (arXiv:2508.19652, Aug 2025) decomposes VLM reasoning into visual perception and language reasoning with self-rewarding — verifiable. Vero (arXiv:2604.04917, Apr 2026) uses task-routed rewards across 59 datasets — verifiable. V-Triune (arXiv:2505.18129, May 2026) sample-level reward routing — verifiable. Chart-RL (arXiv:2603.06958, Mar 2026) applies RLVR to chart reasoning — verifiable. PEARL (CVPR 2026) binary perception-reasoning gate. CogFlow (ICLR 2026) Visual-Gated Policy Optimization — binary gate. Faithful GRPO (arXiv:2604.08476, Apr 2026) constrains policy for spatial grounding — verifiable. NON-VERIFIABLE + GATED/STRUCTURED REWARDS (TEXT-ONLY): DRO (arXiv:2506.13351, Jun 2025/May 2026) uses BINARY rubric-gating as hard feasibility constraints at rollout-group level for non-verifiable text tasks (scientific paragraph revision, medical QA) — coverage gate + consistency gate, both binary accept/reject. Most directly overlapping with our gating-for-non-verifiable concept, but text-only and strictly binary. Training AI Co-Scientists (arXiv:2512.23707, Dec 2025) applies rubric RL (GRPO) to scientific research plan generation — instance-specific rubrics extracted from papers, reward = proportion of satisfied rubric items, text-only, demonstrates cross-domain generalization but also reward model overoptimization. Rubric-ARM (arXiv:2602.01511, Feb 2026) alternating RL for rubric-based reward modeling — text-only. Writing-Zero (arXiv:2506.00103) bridges non-verifiable tasks via pairwise GenRM — text-only. Rubric-Grounded RL (arXiv:2605.08061, May 2026) LLM-judge rubric decomposition — text-only. RubricEM (arXiv:2605.10899, May 2026) meta-RL with rubric-guided policy decomposition — text-only. ARES (arXiv:2605.23454, May 2026) automates rubric synthesis from documents at scale (101K instances, 1.1M criteria) with QA-rubric co-generation — text-only, addresses rubric generation bottleneck but no gating. NON-VERIFIABLE MULTIMODAL: RubiCap (arXiv:2603.09160, Mar 2026) rubric-guided RL for dense image captioning with dynamically generated instance-level rubrics — no gating, general captioning not scientific reasoning. ClaimDiff-RL (arXiv:2605.20278, May 2026) decomposes captioning evaluation into individual visual claims with graded severity weighting — claim-level decomposition structurally analogous to rubric dimensions, severity weighting as implicit soft gating, hybrid verifiable/non-verifiable but for general captioning. rDPO (arXiv:2604.13029, Apr 2026) applies instance-specific rubrics for multimodal DPO with essential/additional criteria functioning as soft gating — multimodal, uses DPO not GRPO, scores are {0, 0.5, 1} per criterion. BalCapRL (Mar 2026) balanced multi-objective RL for captioning. REWARD DYNAMICS AND ANTI-HACKING: Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) identifies three systematic exploitation patterns in rubric rewards for medical/science domains — partial compound (36%), implicit-as-explicit (34.6%), imprecise verification (29.4%) — and proposes self-internalization gap as verifier-free diagnostic (r=0.91-0.97 correlation with reference panel). Directly validates anti-hacking motivation and informs our monitoring strategy. POW3R (arXiv:2605.20164, May 2026) demonstrates policy-aware rubric weighting outperforms static weighting because important criteria can be saturated or unreachable — both text AND multimodal experiments. Reward Design for Physical Reasoning (arXiv:2604.13993, Apr 2026) found accuracy-based rewards outperform flat composite rubric rewards on verifiable physics tasks, BUT also found rubric rewards improve structured reasoning quality — motivates our focus on non-verifiable settings where accuracy is unavailable, while acknowledging rubric rewards provide complementary value even in verifiable settings. CONTINUOUS vs BINARY GATING THEORY: GR3 (arXiv:2603.10535) proves continuous multiplicative gating is a strict mathematical generalization of binary gating — equivalent in binary case, strictly superior when rewards are graded, because binary gating breaks Lipschitz continuity. Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) shows 0.69 degeneracy rate at group size 4 with binary rewards; continuous fix yields 45-point accuracy gain. ReDit (arXiv:2506.18631) achieves GRPO-equivalent performance in 10% of training steps by making discrete rewards continuous. Smooth Gate Functions (arXiv:2602.19345) formalizes properties of admissible gate functions and shows smooth alternatives to hard clipping produce more stable training. PEPO (arXiv:2603.22847) uses smooth gating for multimodal token-level advantage estimation, directly relevant to our multimodal setting. THE GAP: No work combines (1) CONTINUOUS hierarchical gating (all existing gating is binary) with (2) non-verifiable multimodal settings with (3) scientific reasoning requiring domain-specific rubrics with (4) policy-aware adaptive weight/threshold scheduling.",
  "inspired_by": "Intersection gap with principled generalization: DRO provides binary rubric-gating for non-verifiable text tasks; PaLMR provides binary visual gating for verifiable multimodal tasks; GR3 proves continuous gating is a strict mathematical generalization of binary gating with provably better gradient properties. We synthesize these into continuous hierarchical gating for non-verifiable multimodal scientific reasoning. The key theoretical insight: binary gating introduces gradient discontinuities that are especially harmful when rewards are inherently graded (as in scientific reasoning rubrics) — continuous gating eliminates this while preserving the epistemic dependency structure (perception→structure→reasoning). POW3R demonstrates static rubric weights are suboptimal — we integrate policy-aware adaptation. Reward Hacking in Rubric-Based RL identifies exploitation patterns in scientific/medical rubric RL — we integrate self-internalization gap monitoring. ClaimDiff-RL provides the architectural template for claim-level visual verification in Tier-1. Building block: GRPO's compatibility with multi-reward designs (proven by SR-MCR, DRO, Vero, V-Triune, POW3R) makes it the natural optimization backbone.",
  "approach": "We propose GatedRubric-GRPO, which introduces CONTINUOUS hierarchical gating for non-verifiable multimodal scientific reasoning within standard GRPO training on Qwen3-VL-8B. The key technical innovation over existing gated approaches (DRO's binary rubric-gates, PaLMR's binary visual gates) is replacing binary indicator functions with smooth sigmoid gates, formally grounded in GR3's proof that continuous gating is a strict generalization of binary gating.\n\nSMOOTH GATING FORMULATION: The composite reward decomposes into three epistemically dependent tiers:\n\nR = w₁·R₁ + w₂·g₁(R₁)·R₂ + w₃·g₁(R₁)·g₂(R₂)·R₃\n\nwhere g_k(x) = σ((x - τ_k) / T_k) are smooth sigmoid gate functions with temperature T_k controlling sharpness. Key properties: (1) As T_k → 0, g_k → binary indicator 𝟙(x ≥ τ_k), recovering DRO/PaLMR-style hard gating — our formulation is a strict generalization. (2) For finite T_k, g_k preserves Lipschitz continuity of the reward landscape, eliminating gradient dead zones at thresholds. (3) T_k can be scheduled during training (warm→cool), implementing an explicit smooth curriculum from exploration to exploitation.\n\nTIER-1 (Visual Grounding, continuous 0-1): Inspired by ClaimDiff-RL's claim-level decomposition and Perception-R1's visual perception reward, we decompose model outputs into atomic visual claims and verify each against the figure. Programmatic checks (element identification, data reading, spatial description) combined with lightweight LLM verification produce a continuous grounding score. This extends Perception-R1's approach (binary verification of pre-extracted annotations) to open-ended claim generation with graded scoring.\n\nTIER-2 (Structural Quality, soft-gated on Tier-1): A frozen LLM judge (Qwen3-32B) evaluates logical coherence, evidence-claim alignment, domain terminology, and visual-textual consistency using discipline-specific rubric templates. Rubric templates are auto-generated following ARES's pipeline adapted for scientific figures, then expert-calibrated. Soft-gated by g₁(R₁): when visual grounding is poor, structural quality reward is smoothly attenuated (NOT zeroed as in binary gating), providing gradient signal proportional to grounding quality.\n\nTIER-3 (Reasoning Quality, soft-gated on Tier-1 AND Tier-2): Bootstrapped pairwise comparison within GRPO rollout groups assesses analytical depth, interpretive insight, explanation completeness — extending Writing-Zero's BRPO to multimodal. Soft-gated by g₁(R₁)·g₂(R₂).\n\nPOLICY-AWARE ADAPTIVE VARIANT (GatedRubric-GRPO+): Inspired by POW3R's finding that static rubric weights are suboptimal, we additionally implement an adaptive variant where: (a) per-criterion contrastiveness is computed from rollout variance within each GRPO group, (b) weights w₁, w₂, w₃ and temperatures T₁, T₂ are rescaled based on criterion contrastiveness with EMA smoothing, and (c) category-level normalization preserves the tier structure. This ensures training pressure shifts from saturated criteria (e.g., basic element identification) to actionable criteria (e.g., interpretive depth) as the policy improves.\n\nANTI-HACKING MONITORING: Integrating the self-internalization gap from 'Reward Hacking in Rubric-Based RL', we compute the divergence between the policy's prompt-only distribution and rubric-conditioned distribution using only policy log-probabilities. This provides a verifier-free early-stopping diagnostic (r=0.91-0.97 correlation with reference panel) to detect when the policy begins exploiting rubric structure rather than genuinely improving.\n\nTRAINING TASKS (genuinely non-verifiable):\n\n(1) Scientific figure explanation generation using MMSci (Nature Communications figures, 72 disciplines) — 10K stratified sample across 18 discipline groups. RE-ANNOTATION PIPELINE: Reference captions decomposed into atomic claims by Qwen3-32B, converted to per-figure rubric criteria across 7 dimensions: Visual Accuracy (correct identification of visual elements), Sub-figure Coverage (all panels addressed), Quantitative Fidelity (numerical values, trends, comparisons), Scientific Terminology (domain-appropriate vocabulary), Methodological Context (experimental/computational technique), Interpretive Validity (scientifically sound conclusions), Structural Description (axes, labels, legends). Each criterion assigned severity weight: Critical (3.0), Important (2.0), Minor (1.0). Teacher committee of 3 VLMs generates alternative captions for consensus extraction following RubiCap's pipeline. MOTIVATION: CIDEr scores are 0.00-3.73 across ALL models on MMSci, demonstrating reference-based metrics are fundamentally inadequate for scientific figure captioning where identical content admits vastly different valid descriptions.\n\n(2) Open-ended scientific graph analysis using SciGraphQA re-annotated with rubric scoring (same 7-dimension framework, adapted for QA format).\n\n(3) SciCritique-5K: A new benchmark of ~5K scientific figure critique examples. CONSTRUCTION PIPELINE: (a) Source: ArXiv papers (2020-2025) across 5 STEM domains (physics, chemistry, biology, materials science, earth science), selected via SciCap extraction pipeline with LaTeX source compilation for high-resolution figure extraction. (b) Figure type classification using SigLIP visual encoder (CharXiv approach, cosine similarity ≥ 0.65) to select informative scientific figures. (c) Critique generation: 3-model ensemble (GPT-4o, Claude, Gemini) generates structured critiques per figure. (d) Rubric dimensions (8): Visual Accuracy, Scientific Validity, Quantitative Fidelity, Methodological Context, Interpretive Depth, Structural Completeness, Domain Terminology, Constructive Suggestions — informed by SciFig's 6-dimension taxonomy and SIQA's scientific image quality framework. (e) Each dimension: 5-point ordinal scale + Essential/Important/Optional/Pitfall classification (Dr.SCI approach). (f) LLM annotation: Qwen3-32B scores each critique against rubric, with 3-run median voting and position-switching for robustness (following rDPO's protocol). (g) Expert validation: 20% subset (1K items), 3 annotators per item from STEM PhD pool, 2-week calibration phase with 50 consensus examples, target Krippendorff's α ≥ 0.75 per dimension, 60-minute session limits (following SIQA protocol). (h) SIZE JUSTIFICATION: 5K is within the effective range for rubric-RL (Training AI Co-Scientists uses 6.8K; DRO uses 12.5-19.8K; Self-Rewarding Rubric RL effective with 4K), supplemented with 10K MMSci + SciGraphQA for total 20K+.\n\nCONTROLLED COMPARISON: CharXiv and SciFIBench as verifiable baselines demonstrating WHERE binary rewards suffice.\n\nCOMPREHENSIVE ABLATION SUITE (7 conditions):\n(A1) Flat composite: R = w₁·R₁ + w₂·R₂ + w₃·R₃ (no gating)\n(A2) DRO-style binary rubric-gating: hard accept/reject at rollout-group level\n(A3) PaLMR-style binary visual gate: R₁ binarized, indicator function gates\n(A4) POW3R-style policy-aware weighting WITHOUT gating: adaptive weights but flat combination\n(A5) Dynamic weighting à la RuCL: rubric weights adjust during training but without gating\n(A6) Tier-1+2 only (no reasoning quality tier)\n(A7) Tier-1+3 only (no structural quality tier)\n\nTHEORETICAL MOTIVATION: (1) Gradient continuity: GR3 proves continuous multiplicative gating preserves Lipschitz continuity while binary gating introduces discontinuities. (2) Gradient starvation prevention: binary gating produces zero-gradient groups; continuous gating always provides non-zero signal. (3) Smooth curriculum: temperature scheduling T_k(t) implements principled version of implicit curriculum (arXiv:2602.14872). (4) Anti-exploitation: tiered gating ensures higher-tier content cannot compensate for lower-tier deficiencies, while continuous gates prevent all-or-nothing rejection that wastes partially valuable training signal.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1100-1500 (8×H100: ~120h LLM-based rubric annotation with 32B judge on ~15K examples, ~600h main GatedRubric-GRPO training and 7-condition ablation suite, ~180h baseline reproductions including DRO/RubiCap/PaLMR-style baselines, ~150h evaluation and analysis)",
      "human_annotation": "~700 person-hours domain expert validation (~$17K at expert rates: 1K SciCritique validation items × 3 annotators × 25 min + 500 MMSci rubric validation items × 3 annotators × 15 min + ~100h calibration/coordination, 5 STEM PhD annotators at $22-25/hr)",
      "timeline": "4.5-5.5 months (6 weeks dataset curation with LLM-assisted rubric annotation + expert validation including 2-week calibration, 3 weeks baseline implementation, 7 weeks GatedRubric-GRPO training and full 7-condition ablation suite, 4 weeks evaluation and paper writing)",
      "estimated_gpu_cost": "$2,200-$3,750 (at $2-2.50/H100-hr spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "900-1200 (Claude generates rubric templates, annotation pipelines, ablation configurations, and smooth gating module code; human validates scientific accuracy)",
      "human_annotation": "~500 person-hours expert validation (~$12K — reduced via Claude-assisted rubric calibration and automated quality filtering)",
      "timeline": "3.5-4.5 months (5 weeks dataset curation with Claude-assisted rubric generation and calibration, 2.5 weeks baseline setup, 6 weeks training and ablations, 3.5 weeks evaluation and writing)",
      "claude_api_cost": "$500-850 (rubric generation for ~15K examples, annotation calibration, reward module code generation, experiment analysis — ~150M input + 30M output tokens via Sonnet batch API)",
      "estimated_gpu_cost": "$1,800-$3,000"
    },
    "auto_research": {
      "gpu_hours": "900-1200 (same compute floor; GPU time is irreducible)",
      "human_annotation": "~300 person-hours minimum expert validation (~$7.5K — cannot be fully automated for scientific domain rubrics; Reward Hacking in Rubric-Based RL shows LLM judges systematically exploit 'topical alignment' without human calibration)",
      "timeline": "3-4 months (parallel dataset curation and code development, automated hyperparameter sweeps for τ and T parameters)",
      "claude_api_cost": "$800-1,400 (heavier annotation generation, automated rubric calibration experiments, smooth gating hyperparameter search, paper drafting — ~300M input + 60M output tokens)",
      "estimated_gpu_cost": "$1,800-$3,000",
      "speed_bottleneck": "Domain expert validation of scientific rubric annotations is the irreducible bottleneck. Reward Hacking in Rubric-Based RL (arXiv:2605.12474) demonstrates that even strong LLM verifiers retain 15-28% exploitation rate — systematic LLM biases in scientific rubric evaluation require human calibration. Expert recruitment and calibration across 5 STEM domains requires 3-4 weeks minimum."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: Jul 21 2026, paper: Jul 28 2026 — tight but feasible with focused results on 2 of 3 tasks and key ablations A1-A3)",
    "WACV 2027 Round 2 (paper: Aug 27 2026 — full results including all 7 ablations and SciCritique-5K benchmark)",
    "EACL 2027 (ARR submission: Aug 3 2026 — framing emphasizes rubric RL and gating formalism)",
    "CVPR 2027 (estimated ~Nov 2026 — TBA, full paper with complete analysis and policy-aware adaptive variant)",
    "ICLR 2027 (estimated ~Oct 2026 — TBA, full paper with theoretical analysis of continuous vs binary gating dynamics)"
  ],
  "level": "solid",
  "key_references": [
    "PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment (arXiv:2603.06652, Feb 2026) — binary gated hierarchical reward for verifiable tasks; our smooth gating extends this principle",
    "DRO: Direct Reasoning Optimization with Rubric-Gated Constraints (arXiv:2506.13351, Jun 2025/May 2026) — BINARY rubric-gating as hard feasibility constraints for non-verifiable TEXT tasks; most direct competitor, we generalize from binary to continuous gating and from text to multimodal",
    "RubiCap: Rubric-Guided RL for Dense Image Captioning (arXiv:2603.09160, Mar 2026) — rubric-based RL for non-verifiable multimodal captioning without gating",
    "Training AI Co-Scientists Using Rubric Rewards (arXiv:2512.23707, Dec 2025) — rubric RL (GRPO) for scientific research plan generation, text-only; demonstrates cross-domain generalization and reward overoptimization",
    "Reward Hacking in Rubric-Based RL (arXiv:2605.12474, May 2026) — three systematic exploitation patterns in medical/science rubric RL; self-internalization gap (r=0.91-0.97) as verifier-free diagnostic; directly informs our anti-hacking monitoring",
    "GR3: Group Relative Reward Rescaling (arXiv:2603.10535) — FORMALLY PROVES continuous multiplicative gating is a strict generalization of binary gating with superior gradient properties; key theoretical foundation",
    "POW3R: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164, May 2026) — static rubric weights are suboptimal; policy-aware contrastiveness-based adaptation; both text and multimodal; inspires our adaptive variant",
    "ARES: Automated Rubric Synthesis for Scalable RL (arXiv:2605.23454, May 2026) — automated QA-rubric co-generation at scale (101K instances, 1.1M criteria); informs our rubric generation",
    "rDPO: Visual Preference Optimization with Rubric Rewards (arXiv:2604.13029, Apr 2026) — instance-specific rubrics for multimodal DPO; closest multimodal rubric competitor but uses DPO not RL",
    "ClaimDiff-RL: Fine-Grained Caption RL through Visual Claim Comparison (arXiv:2605.20278, May 2026) — claim-level decomposition with graded severity; architectural template for Tier-1",
    "Perception-R1: Visual Perception Reward for MLLMs (arXiv:2506.07218) — visual perception reward in RLVR; demonstrates perception reward improves downstream reasoning",
    "Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — 0.69 degeneracy rate; 45-point accuracy gain from continuous fix",
    "ReDit: Reward Dithering (arXiv:2506.18631) — GRPO-equivalent performance in 10% of steps by making discrete rewards continuous",
    "Smooth Gate Functions for Soft Advantage Policy Optimization (arXiv:2602.19345) — formalizes admissible gate function properties",
    "PEPO: Token-Level Policy Optimization for Multimodal CoT (arXiv:2603.22847) — smooth gating for multimodal advantage estimation",
    "SR-MCR: Self-Rewarded Multimodal Coherent Reasoning (arXiv:2512.22545, Dec 2025) — five sub-rewards with GRPO; flat combination, verifiable",
    "RuCL: Stratified Rubric-Based Curriculum Learning (arXiv:2602.21628, Feb 2026) — dynamic rubric weighting; verifiable",
    "RubricEM: Meta-RL with Rubric-guided Policy Decomposition (arXiv:2605.10899, May 2026) — text-only",
    "Rubric-ARM: Alternating RL for Rubric-Based Reward Modeling (arXiv:2602.01511, Feb 2026) — text-only",
    "Reward Design for Physical Reasoning in VLMs (arXiv:2604.13993, Apr 2026) — accuracy > flat composite rubric on verifiable tasks, BUT rubric rewards improve structured reasoning quality",
    "The Implicit Curriculum in RLVR (arXiv:2602.14872, Feb 2026) — our temperature scheduling implements explicit smooth curriculum",
    "Writing-Zero (arXiv:2506.00103) — pairwise GenRM for text non-verifiable tasks; we extend BRPO to multimodal Tier-3",
    "Vision-SR1 (arXiv:2508.19652, Aug 2025) — perception-reasoning decomposition; verifiable",
    "LLMs Gaming Verifiers (arXiv 2026) — reward hacking pathways",
    "Vero (arXiv:2604.04917, Apr 2026) — task-routed rewards; verifiable",
    "V-Triune (arXiv:2505.18129, May 2026) — sample-level reward routing; verifiable",
    "Rubric-Grounded RL (arXiv:2605.08061, May 2026) — LLM-judge rubric decomposition; text-only",
    "Faithful GRPO (arXiv:2604.08476, Apr 2026) — verifiable spatial tasks",
    "MMSci (arXiv:2407.04903, NeurIPS 2024 Workshop) — 72-discipline, 742K figures from Nature Communications",
    "SciGraphQA (arXiv:2308.03349) — open-ended graph analysis",
    "CharXiv (NeurIPS 2024) — chart understanding benchmark",
    "SciFIBench (NeurIPS 2024) — scientific figure interpretation benchmark",
    "PRISMM-Bench (arXiv:2510.16505) — 384 validated inconsistencies from peer reviews; informs SciCritique-5K construction",
    "SIQA (arXiv:2603.06700) — 4-dimension scientific image quality framework with expert annotation protocol",
    "SciFig (arXiv:2601.04390) — 6-dimension rubric for scientific figure evaluation",
    "Dr.SCI (arXiv:2602.08321) — Essential/Important/Optional/Pitfall rubric categorization for STEM"
  ],
  "description": "We propose GatedRubric-GRPO, a framework that introduces SMOOTH CONTINUOUS hierarchical gating for non-verifiable multimodal scientific reasoning. The key technical innovation is replacing the BINARY gates used by all prior gated reward systems (DRO uses binary rubric-gates for non-verifiable text; PaLMR uses binary visual gates for verifiable multimodal) with smooth sigmoid gate functions g_k(x) = σ((x - τ_k)/T_k), formally grounded in GR3's proof that continuous multiplicative gating is a strict mathematical generalization of binary gating that preserves Lipschitz continuity and eliminates gradient dead zones. Three epistemically dependent tiers — Tier-1: visual grounding via claim-level decomposition (ClaimDiff-RL-inspired), Tier-2: structural quality via frozen LLM-judge rubrics (ARES-inspired auto-generation, expert-calibrated), Tier-3: reasoning quality via bootstrapped pairwise comparison — are combined as R = w₁·R₁ + w₂·g₁(R₁)·R₂ + w₃·g₁(R₁)·g₂(R₂)·R₃, with an adaptive variant (GatedRubric-GRPO+) incorporating POW3R-style policy-aware weight/temperature scheduling. Anti-exploitation monitoring via self-internalization gap (from Reward Hacking in Rubric-Based RL). Training on genuinely non-verifiable scientific tasks: MMSci figure explanation (10K, re-annotated with 7-dimension rubric across 72 disciplines), SciGraphQA open-ended analysis, and SciCritique-5K (new benchmark: 5K figure-critique pairs from 5 STEM domains, 8-dimension rubric, 20% expert-validated with target Krippendorff's α ≥ 0.75). A 7-condition ablation suite directly compares against DRO-style binary gating, PaLMR-style binary visual gates, POW3R-style adaptive weighting without gating, and flat composite baselines.",
  "project_name": "gated_rubric_nonverif_sci_mm",
  "source": "web_research",
  "change_type": "major",
  "changes_summary": {
    "issue_1_missing_works": "MAJOR FIX: Integrated all 8 reviewer-identified missing works plus 7 additional works. DRO positioned as most direct competitor (binary vs continuous, text vs multimodal). Training AI Co-Scientists demonstrates rubric RL for science. Reward Hacking paper's self-internalization gap becomes core monitoring component. ARES informs rubric generation. POW3R becomes core adaptive variant (GatedRubric-GRPO+). rDPO positioned as closest multimodal rubric competitor. Perception-R1/ClaimDiff-RL inform Tier-1 design. Additionally integrated: GR3, PEPO, gradient starvation analysis, ReDit, Smooth Gate Functions, PRISMM-Bench, SIQA, SciFig, Dr.SCI.",
    "issue_2_novelty_sharpened": "MAJOR FIX: Reframed from 'domain extension' to 'principled generalization with formal justification.' Three pillars: (1) FORMAL — GR3 proves continuous gating is strict mathematical generalization; binary gating breaks Lipschitz continuity (gradient starvation 0.69 degeneracy rate). (2) STRUCTURAL — scientific reasoning has inherently graded quality; binary gating discards signal. (3) PRACTICAL — ablation A2/A3 directly compare continuous vs binary. Sigmoid gate formulation with temperature scheduling is concrete technical contribution.",
    "issue_3_benchmark_detailed": "MAJOR FIX: SciCritique expanded 2K→5K with complete pipeline: ArXiv papers 2020-2025 across 5 STEM domains, SigLIP classification, 3-model ensemble critique generation, 8-dimension rubric (SciFig+SIQA), Essential/Important/Optional/Pitfall (Dr.SCI), 3-run median voting (rDPO protocol), 20% expert validation (1K items, 3 annotators, Krippendorff's α ≥ 0.75). Size justified vs Training AI Co-Scientists (6.8K), DRO (12.5-19.8K).",
    "issue_4_mmsci_reannotation": "MAJOR FIX: 7-dimension rubric specified. CIDEr 0.00-3.73 across ALL models motivates switch. Qwen3-32B decomposes captions into atomic claims with Critical/Important/Minor severity. Teacher committee of 3 VLMs for consensus. Expert validation: 500 items across 10 PhD-annotated domains.",
    "issue_5_reward_design_nuanced": "MODERATE FIX: Acknowledged rubric rewards improve structured reasoning even in verifiable settings. Accuracy and rubric rewards capture DIFFERENT value. Gating provides ADDITIONAL value in non-verifiable regime by preventing 'topical alignment' exploitation (21.1% of exploitation instances per Reward Hacking paper).",
    "issue_6_pow3r_engaged": "MAJOR FIX: POW3R incorporated as core adaptive variant (GatedRubric-GRPO+) with policy-aware contrastiveness-based weight/temperature adaptation. Also ablation A4 (POW3R without gating) tests orthogonal contributions.",
    "additional_improvements": "Ablation A2 directly compares DRO-style binary gating. Self-internalization gap monitoring integrated. ClaimDiff-RL claim decomposition for Tier-1. Temperature scheduling T_k(t) as curriculum. Ablation suite expanded 5→7. References expanded 25→36."
  }
}
```

---

## Summary of Key Changes (Round 2 → Round 3)

### Change type: **MAJOR**

**1. Novelty Elevation (the critical fix):** The core novelty is no longer "apply gating to a new domain." It's now grounded in a **formal argument**: GR3 (arXiv:2603.10535) proves continuous multiplicative gating is a strict mathematical generalization of binary gating. Binary gating breaks Lipschitz continuity and causes gradient dead zones (0.69 degeneracy rate empirically). Continuous sigmoid gating with temperature scheduling eliminates these pathologies while preserving the epistemic dependency hierarchy. This is a **qualitative** difference, not just "softening."

**2. Landscape Expansion:** Integrated all 8 missing works + 7 additional papers:
- **DRO** → most direct competitor, binary gating for non-verifiable text
- **Training AI Co-Scientists** → rubric RL for scientific reasoning, text-only  
- **Reward Hacking in Rubric-Based RL** → exploitation patterns → self-internalization gap monitoring
- **POW3R** → policy-aware adaptive variant (GatedRubric-GRPO+)
- **ARES, rDPO, Perception-R1, ClaimDiff-RL** → inform design choices
- **GR3, PEPO, ReDit, gradient starvation** → theoretical foundation

**3. Benchmark Specification:** SciCritique-5K now has a complete construction pipeline with specific tools (SigLIP, SciCap), rubric frameworks (SciFig, SIQA, Dr.SCI), annotation protocol (3-run median, position-switching), and validation targets (Krippendorff's α ≥ 0.75).

**4. MMSci Re-annotation:** 7-dimension rubric specified with severity weights, teacher committee approach, and quantitative motivation (CIDEr 0.00-3.73 across all models).

**5. Reward Design Nuanced:** Acknowledged rubric rewards provide value even in verifiable settings; gating provides *additional* anti-exploitation value.

**6. POW3R Integrated:** Core adaptive variant + ablation A4 for orthogonal testing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f5f21ad-5efa-47da-b27a-533e702a485f",
  "isSidechain": false,
  "requestId": "req_011CbUHSeKisx5qx5T8BzFqZ",
  "type": "assistant",
  "uuid": "3eb4081f-a6a1-446c-a015-6a3e86255a75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqGAqJbuxBZWx122fVNTF3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10812,
      "cache_read_input_tokens": 84409,
      "output_tokens": 10005,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10005,
          "cache_read_input_tokens": 84409,
          "cache_creation_input_tokens": 10812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10812
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

_source line 110_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "3eb4081f-a6a1-446c-a015-6a3e86255a75",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 111_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 112_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"GatedRubric-GRPO: Extending Structured Reward RL to Non-Verifiable Mul…",
  "leafUuid": "3eb4081f-a6a1-446c-a015-6a3e86255a75",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---

### Runtime record

_source line 113_

```json
{
  "type": "ai-title",
  "aiTitle": "Extend gated rubric rewards to scientific multimodal reasoning",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d"
}
```

---
