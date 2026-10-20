# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/e2ff682e-1fce-46ae-a817-147e98b79cfa.jsonl`
- **Structured JSON:** [`b999bf0865fb375d1666.json`](../../sessions/b9/b999bf0865fb375d1666.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T16:26:03.018Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T16:26:03.018Z",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Research area: Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding\n\n## Paper analyses (20 papers)\n\n[\n  {\n    \"title\": \"MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts\",\n    \"venue\": \"ICLR 2024 (Oral, top 1.2%)\",\n    \"problem_identification\": \"Prior to MathVista, mathematical reasoning and visual understanding were evaluated in separate silos — text-only math benchmarks (GSM8K, MATH) ignored visual input, while VQA benchmarks lacked mathematical depth. The authors identified that the *intersection* — tasks requiring both fine-grained visual perception and compositional mathematical reasoning — had never been systematically evaluated. They found this gap by observing that 28+ datasets existed across math-QA and VQA domains, but none unified them under a coherent taxonomy, and critical domains (puzzle-based logical reasoning, function plot analysis, scientific figure interpretation) had no dedicated evaluation at all.\",\n    \"key_insight\": \"The core insight was that mathematical reasoning in visual contexts is not a simple sum of 'vision + math' but a distinct capability requiring compositional integration — and the right way to expose this was not to create one monolithic new dataset, but to consolidate and systematically organize existing fragmented resources under a principled three-dimensional taxonomy (task type × reasoning type × visual context), while surgically creating only the three new datasets needed to fill genuine gaps (IQTest, FunctionQA, PaperQA).\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"MathVista constructs a 6,141-example benchmark from 31 source datasets (28 existing + 3 new) organized along three taxonomic dimensions: 5 task types (FQA, GPS, MWP, TQA, VQA), 7 mathematical reasoning types (algebraic, arithmetic, geometric, logical, numeric, scientific, statistical), and 15 visual context types spanning geometry diagrams to medical images. The three new datasets — IQTest (logical reasoning on puzzle figures), FunctionQA (algebraic reasoning over function plots), and PaperQA (scientific reasoning from academic figures) — were created to fill specific coverage gaps. The evaluation protocol supports both multiple-choice and free-form answers with precision-aware scoring, and tests models under multiple augmentation strategies: zero-shot, few-shot (0–4), chain-of-thought (CoT), program-of-thought (PoT), and caption+OCR text augmentation for text-only LLMs. A 1,000-example testmini split enables fast development while the 5,141-example test split has private labels for fair leaderboard evaluation. The authors further explored GPT-4V's self-verification and self-consistency capabilities as novel analysis dimensions.\",\n    \"what_makes_it_good\": \"Three factors propelled this to an oral: (1) *Timing and impact* — it launched alongside GPT-4V and immediately became the standard evaluation for the rapidly emerging multimodal reasoning field, filling an obvious-in-retrospect gap that nobody else had systematized. (2) *Methodological rigor in curation* — rather than brute-force creating a new dataset, the authors demonstrated that principled consolidation with a clear taxonomy (making existing scattered resources usable under a unified evaluation) was itself a first-class contribution, and they were surgical about creating only 3 new datasets to fill genuine holes. (3) *Comprehensive evaluation with actionable findings* — testing 12 models under multiple strategies with fine-grained error analysis (by reasoning type, visual context, grade level) produced diagnostic insights, not just a leaderboard number.\",\n    \"limitations_acknowledged\": \"The authors acknowledged that MathVista cannot cleanly disentangle visual perception errors from mathematical reasoning errors — a model might fail because it misread a chart or because it couldn't solve the underlying math, and the benchmark doesn't distinguish these. Human performance at only 60.3% (with AMT annotators having high school diplomas or above) also raised questions about problem difficulty calibration versus annotation quality, which the authors addressed with Fleiss Kappa of 0.775 but did not fully resolve.\",\n    \"open_questions\": [\n      \"How can we design benchmarks that *disentangle* visual perception from mathematical reasoning — e.g., by providing ground-truth scene descriptions alongside images, enabling controlled ablation of the visual understanding component?\",\n      \"Can we move beyond static evaluation to *process-level* assessment — evaluating not just final answers but intermediate reasoning steps, to understand where in the visual-to-symbolic-to-solution pipeline models break down?\",\n      \"As models rapidly saturate MathVista (InternVL2-Pro at 65.8% now exceeds original human baselines), what is the next-generation benchmark that captures harder compositional reasoning, multi-step visual proofs, or dynamic/interactive mathematical contexts?\"\n    ],\n    \"building_blocks\": [\n      \"Three-dimensional taxonomy framework (task type × reasoning type × visual context) — reusable for any multimodal benchmark design\",\n      \"Consolidation-plus-surgical-creation methodology — curating 28 existing datasets + creating only 3 new ones to fill gaps\",\n      \"Dual-split evaluation design (1K public testmini + 5K private test) with leaderboard infrastructure\",\n      \"Multi-strategy evaluation protocol (zero-shot, few-shot, CoT, PoT, caption+OCR augmentation)\",\n      \"Precision-aware scoring for free-form numerical answers\",\n      \"Self-verification and self-consistency analysis as diagnostic tools for GPT-4V-class models\",\n      \"Source datasets: GeoQA+, Geometry3K, UniGeo, CLEVR-Math, TabMWP, ChartQA, FigureQA, ScienceQA, AI2D, IconQA, and others\",\n      \"AMT-based human performance baseline methodology with Fleiss Kappa inter-annotator agreement\"\n    ],\n    \"reviewer_feedback_summary\": \"**Scores**: 5, 8, 8, 8 (three accepts + one marginal reject → oral). **Key praise**: Reviewers lauded the well-designed taxonomy, comprehensive coverage from 31 sources, and the importance of the research area. Reviewer 2 called it 'well-designed and relatively large'; Reviewer 4 praised the 'thorough review of existing work.' **Key concerns**: (1) Cannot disentangle visual vs. mathematical reasoning failures (raised by Reviewers 2 and 4); (2) Human accuracy of only 60.3% raised data quality questions; (3) Initially missing GPT-4V results (paper submitted before GPT-4V launch). **Author response was decisive**: They added 67 pages including comprehensive GPT-4V analysis (49.9% accuracy), self-verification studies, expanded few-shot evaluations, and inter-annotator agreement (Fleiss Kappa 0.775). Reviewer 3 explicitly upgraded their assessment after the rebuttal, calling it 'a strong and interesting paper.' The Area Chair summarized: 'Benchmark is solid work... The work seems impactful for the community.' **What would have made it stronger**: A mechanism to isolate visual vs. reasoning errors, higher human baselines with expert annotators, and a finetuning training split.\",\n    \"relevance_to_seed\": \"MathVista is the foundational evaluation infrastructure for our research area — any new method for multi-modal mathematical reasoning must benchmark against it. More importantly, its *methodology* teaches us how to identify fertile research directions: the taxonomy reveals that logical reasoning (19% accuracy for top models) and complex figure understanding remain the hardest unsolved problems, and the inability to disentangle visual from symbolic reasoning points directly to the need for architectures that make this decomposition explicit — a core opportunity in integrating visual, symbolic, and textual understanding.\"\n  },\n  {\n    \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\",\n    \"venue\": \"Nature 645, 633–638 (2025)\",\n    \"problem_identification\": \"The authors identified that the standard post-training paradigm (SFT on human reasoning traces → RL) inherently caps model reasoning at human-level performance because human demonstrations omit critical steps like self-verification and reflection, and they constrain the model to explore only human-like reasoning pathways. They found this gap by observing that SFT-trained models plateau on hard competition math/code while the base model's latent potential remained untapped—its pre-training on massive math/code corpora already gave it the raw ingredients for reasoning, but SFT was the bottleneck preventing self-discovery of superior strategies.\",\n    \"key_insight\": \"If you skip SFT entirely and apply RL with only outcome-based rule rewards (correctness + format) directly on a strong base model, the model will autonomously discover sophisticated reasoning behaviors—self-reflection, verification, backtracking, and dynamic strategy switching—that were never explicitly taught. The 'aha moment' (the model spontaneously learning to say 'Wait, let me reconsider...') is not engineered but emergent, proving that reasoning is latent in pre-trained representations and can be unlocked purely through reward incentives.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"DeepSeek-R1-Zero applies Group Relative Policy Optimization (GRPO)—a PPO variant that eliminates the value model by computing advantages via group-relative normalization of sampled rewards—directly on the DeepSeek-V3-Base (671B MoE) model with no SFT warmup. Rewards are purely rule-based: binary accuracy (answer match or test-case pass) plus a format reward for using &lt;think>/&lt;answer> tags; no neural reward models are used, avoiding reward hacking. For each question, 16 outputs are sampled and advantages are computed as z-scores within each group (Equation 3). DeepSeek-R1 then builds on this via a multi-stage pipeline: (1) a small cold-start SFT using thousands of curated long-CoT samples from R1-Zero (rewritten for readability), (2) first RL stage with rule-based rewards plus a language consistency reward, (3) rejection sampling from the RL checkpoint to collect ~600K reasoning + ~200K non-reasoning SFT samples, (4) second RL stage combining rule-based reasoning rewards with model-based helpfulness/harmlessness rewards. Distillation transfers R1's reasoning traces to 1.5B–70B student models via SFT on R1-generated trajectories.\",\n    \"what_makes_it_good\": \"Three factors made this Nature-worthy: (1) It is a bold, clean scientific claim backed by a striking empirical result—the 'aha moment' where a model spontaneously invents self-reflection is a genuinely surprising emergent phenomenon that captures imagination beyond ML. (2) The simplification narrative is compelling: removing SFT, removing neural reward models, and removing the PPO value model each reduces complexity while improving or matching performance, turning conventional wisdom on its head. (3) The open-source release of the full model family (including distilled 1.5B–70B variants that beat o1-mini) created massive real-world impact, and the paper was transparent about limitations like language mixing and reward hacking—a level of candor reviewers value.\",\n    \"limitations_acknowledged\": \"The authors explicitly identify: (1) reward hacking remains unsolved for non-verifiable tasks (writing, open QA) where reliable rule-based rewards cannot be constructed; (2) token inefficiency and overthinking on simple problems; (3) language mixing when queries are in non-English/Chinese languages; (4) sensitivity to prompting (few-shot degrades performance); (5) limited improvement on software engineering tasks due to slow evaluation loops in RL; (6) structured output and tool use remain weak.\",\n    \"open_questions\": [\n      \"Can pure RL reasoning be extended to multimodal inputs (visual math, diagram reasoning, chart understanding) where reward verification is harder but still possible? The paper's framework only addresses text-in/text-out tasks.\",\n      \"How do we construct reliable reward signals for 'soft' reasoning tasks (scientific argumentation, proof verification, multi-step real-world planning) where binary correctness is unavailable—can we break the reward hacking barrier that limited the paper to ~400 steps of model-based RL?\",\n      \"What is the mechanistic explanation for the emergent reasoning behaviors? The paper documents the 'aha moment' phenomenologically but does not explain WHY or WHEN self-reflection emerges during training—understanding this could allow us to engineer it more efficiently or in smaller models without distillation.\"\n    ],\n    \"building_blocks\": [\n      \"GRPO (Group Relative Policy Optimization) — value-model-free RL algorithm with group-relative advantage estimation\",\n      \"Rule-based reward design (accuracy + format) for verifiable tasks — avoids neural reward model fragility\",\n      \"Language consistency reward (target-language word proportion) for controlling code-switching\",\n      \"Cold-start data curation pipeline: sample from R1-Zero → filter correct + readable → rewrite with LLM → human verify\",\n      \"Rejection sampling from RL checkpoint to generate high-quality SFT data at scale (~600K samples)\",\n      \"Multi-stage training pipeline: cold-start SFT → reasoning RL → rejection sampling SFT → general RL\",\n      \"Distillation via SFT on teacher-generated long-CoT reasoning traces\",\n      \"DeepSeek-V3-Base (671B MoE, 37B active) as foundation model\",\n      \"vLLM-based rollout infrastructure with expert parallelism and speculative decoding for efficient RL\",\n      \"DualPipe algorithm for efficient pipeline parallelism in training\"\n    ],\n    \"reviewer_feedback_summary\": \"Nature peer review comments were behind a paywall and could not be accessed directly. However, based on the paper's structure and the v1→v2 revision (Jan 2025 → Jan 2026), key likely reviewer concerns can be inferred: (1) the paper added extensive ablation studies (GRPO vs PPO comparison in Appendix A.3, clip ratio sensitivity, language consistency reward ablation in B.6), suggesting reviewers demanded more rigorous experimental controls; (2) the ethics/safety section (Section 5) with comprehensive safety benchmarks was likely expanded per reviewer request given the Nature audience; (3) the detailed data contamination analysis and fresh test set evaluations suggest reviewers questioned benchmark validity; (4) the transparency about pre-training data containing reasoning traces (Appendix A.1) and the careful distancing from claims of 'human-like intelligence' (Section B.3.2) suggest reviewers pushed back on overclaiming about emergent cognition.\",\n    \"relevance_to_seed\": \"This paper is the direct ancestor of the multimodal RL-reasoning line of work. Its GRPO algorithm, rule-based reward design, and multi-stage training pipeline are immediately applicable to visual-mathematical reasoning tasks where answers are verifiable (e.g., geometry diagram problems, chart-based calculations, visual equation solving). The key lesson for our research area is that the bottleneck to multimodal math reasoning may not be better vision encoders or more labeled data, but rather designing the right RL reward structure that lets models discover their own visual-symbolic-textual integration strategies through self-play—just as DeepSeek-R1 discovered self-reflection without being taught it.\"\n  },\n  {\n    \"title\": \"URSA: Understanding and Verifying Chain-of-thought Reasoning in Multimodal Mathematics\",\n    \"venue\": \"NeurIPS 2025 (Poster)\",\n    \"problem_identification\": \"The authors observed that Process Reward Models (PRMs) had proven highly effective for text-only LLM math reasoning via test-time scaling and RL, yet their integration into multimodal reasoning was entirely unexplored. They diagnosed three concrete bottlenecks blocking this transfer: (1) no large-scale multimodal CoT data to build strong enough foundation models for PRM-based methods to improve upon, (2) no automated process labeling technique that captures both logical errors AND perceptual hallucinations unique to vision-language settings, and (3) naive scalar PRM integration into RL causes reward hacking and length bias. The gap was found by systematically attempting the text-only PRM playbook in the multimodal setting and documenting where each step broke down.\",\n    \"key_insight\": \"While absolute PRM scalar rewards become unreliable during online RL training (the model games them), the PRM's ability to detect *relative drops* between consecutive reasoning steps ('drop-moments') remains trustworthy. This means process supervision can be converted from an unreliable scalar signal into a robust binary penalty on outcome rewards — you don't need to trust the PRM's numbers, only its ability to spot when something goes wrong relative to the previous step.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"URSA is a three-stage pipeline. Stage I synthesizes MMathCoT-1M by collecting 1.43M multimodal math samples and applying CoT expansion (for answer-only data), rewriting (for analysis-format data), and format unification (for existing CoT data) via a strong LLM, then filtering for correctness/consistency; SFT on this yields URSA-8B. Stage II constructs DualMath-1.1M via two complementary engines: a Binary Error Locating Engine (BEL) that uses MCTS with binary search to efficiently locate first-error steps in ~553K incorrect solutions, and a Misinterpretation Insertion Engine (MIE) that artificially injects perceptual hallucinations into ~302K correct solutions to create process-level supervision for vision-text inconsistencies. Stage III introduces PS-GRPO: rather than using PRM scalar rewards directly (shown to cause reward hacking and length bias), the method detects 'drop-moments' — significant relative decreases in PRM reward between consecutive steps — and applies a penalty γ to outcome-correct rollouts that exhibit such drops, thus differentiating high-quality from lucky reasoning without being susceptible to the PRM's absolute score biases.\",\n    \"what_makes_it_good\": \"The paper succeeds because it identifies a clearly important open problem (PRMs for multimodal math) and systematically addresses *all three* bottlenecks rather than proposing a single trick. The negative results analysis — showing exactly how and why naive scalar PRM rewards fail before introducing PS-GRPO — demonstrates intellectual rigor that reviewers valued. The 8B model outperforming GPT-4o by 2.7% across six benchmarks is a compelling headline result, and the release of two large-scale public datasets (MMathCoT-1M and DualMath-1.1M) provides lasting community value beyond the method itself.\",\n    \"limitations_acknowledged\": \"The authors note a significant performance gap on DynaMath, suggesting smaller-scale MLLMs still lack robust problem-solving capabilities on dynamic/adversarial benchmarks. No formal limitations section is included, but reviewers flagged high computational cost (~$320 for data synthesis using Gemini-1.5-Flash), limited theoretical justification for the drop-moment threshold, and concerns about synthetic process label quality.\",\n    \"open_questions\": [\n      \"Can the drop-moment concept be grounded theoretically (e.g., via Q-value ranking properties) rather than relying on empirical threshold tuning, and can adaptive thresholds outperform fixed ρ values?\",\n      \"How well does this pipeline transfer beyond mathematics — do dual-view process supervision and PS-GRPO generalize to other multimodal reasoning domains (science, coding with visual specs, chart understanding) where perceptual consistency also matters?\",\n      \"What is the quality ceiling of synthetic process labels vs. human annotations — the authors showed 87.6% LLM-as-judge consistency, but does the remaining ~12% noise systematically bias the PRM in ways that compound during RL training?\"\n    ],\n    \"building_blocks\": [\n      \"MCTS-based process annotation with binary search for efficient first-error localization (BEL)\",\n      \"Misinterpretation Insertion Engine for synthetic hallucination-based negative examples (MIE)\",\n      \"Drop-moment detection as a robust signal extraction method from noisy reward models\",\n      \"PS-GRPO: process-as-outcome penalty RL method compatible with standard GRPO\",\n      \"MMathCoT-1M dataset (1M multimodal CoT samples from 1.43M open-source examples)\",\n      \"DualMath-1.1M dataset (1.1M process supervision annotations)\",\n      \"LLaVA-like architecture with math-intensive alignment pretraining (URSA-Alignment-860K)\",\n      \"Three-category CoT synthesis strategy: expansion, rewriting, format unification\",\n      \"Dual correctness filtering (answer correctness + reasoning consistency)\"\n    ],\n    \"reviewer_feedback_summary\": \"Four reviewers rated the paper 4/4/3/3, accepted as poster. **Praise**: Timely and important direction (first to integrate PRMs into multimodal math reasoning), strong empirical results across six benchmarks, solid ablation studies demonstrating each component's contribution, high-quality public dataset releases, and well-written presentation. **Key concerns**: (1) Reviewer 4akc argued limited algorithmic novelty — PS-GRPO resembles DeepSeekMath's step-level GRPO and the pipeline is primarily engineering; authors responded with direct DS-GRPO comparison showing PS-GRPO wins (58.2 vs. 56.5 avg). (2) Reviewer U6mC questioned theoretical justification for ρ=0.3 and synthetic label quality; authors provided Q-value ranking theorem grounding and 87.6% LLM-judge validation. (3) Reviewer GTaC found gains 'modest' and novelty limited to applying LLM paradigms to vision; authors added ORM baselines (PRM outperforms 55.0 vs. 54.3). (4) Reviewer E38C requested confidence intervals; authors provided ±0.1-0.5% ranges. The engineering-vs-novelty tension was the central debate — the paper survived by demonstrating that the specific combination and the drop-moment insight are non-obvious and empirically validated.\",\n    \"relevance_to_seed\": \"This paper is directly central to multi-modal mathematical reasoning research. Its key lessons for our area are: (1) the 'dual-view' framing — treating logical validity and perceptual consistency as separate supervision signals — is a powerful decomposition that could inspire new approaches to visual-symbolic integration, and (2) the finding that relative PRM signals (drop-moments) are trustworthy while absolute scores are not provides a principled way to incorporate process supervision into any multimodal reasoning RL pipeline, opening a concrete path for future work on visual theorem proving, diagram reasoning, and cross-modal verification.\"\n  },\n  {\n    \"title\": \"MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?\",\n    \"venue\": \"ECCV 2024\",\n    \"problem_identification\": \"The authors discovered that existing visual math benchmarks (MathVista, GeoQA, MMMU) encode excessive textual redundancy — the problem text duplicates information already present in diagrams. By running a simple ablation (removing the diagram entirely), they showed that most MLLMs perform the same or *better* without visual input (e.g., Qwen-VL-Max +5.1%, InternLM-XComposer2 +5.6%). This means the field's reported progress on 'visual math reasoning' was partially illusory — models were solving problems from text, not from diagrams.\",\n    \"key_insight\": \"The information in a visual math problem can be decomposed into three semantic types — Descriptive Information (directly observable), Implicit Properties (perceptually extractable), and Essential Conditions (numeric/algebraic specifics) — and by systematically controlling which types appear in text vs. diagram across six problem versions, you can precisely isolate and quantify the degree to which a model genuinely interprets visual content versus exploiting textual shortcuts.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"The authors curated 2,612 high-quality math problems with diagrams across plane geometry (1,746), solid geometry (332), and functions (534). Human annotators then classified each problem's textual content into three information types (DI, IP, EC) and created six versions per problem: text-dominant (full text + diagram), text-lite (no DI), text-only (no diagram), vision-intensive (no IP in text), vision-dominant (no EC in text), and vision-only (all info in diagram only) — yielding ~15K test instances. For evaluation, they introduced a CoT scoring pipeline where GPT-4 first extracts key reasoning steps from model outputs (without seeing the ground truth answer, to avoid bias), then GPT-4V scores each step against the diagram and ground truth, producing a weighted score: Score = 0.7 × (average step correctness) + 0.3 × (final answer correctness). This reveals intermediate reasoning quality beyond binary accuracy.\",\n    \"what_makes_it_good\": \"The paper succeeds because it identifies a methodological blind spot hiding in plain sight — the entire field was benchmarking 'visual reasoning' with benchmarks that don't require vision — and provides an elegant, systematic solution rather than just pointing out the problem. The six-version transformation framework is simple to understand, rigorous in execution, and immediately useful as an evaluation tool. The CoT evaluation strategy adds a second complementary contribution, making the paper a complete evaluation package rather than just a dataset release.\",\n    \"limitations_acknowledged\": \"The benchmark is limited to high-school-level mathematics (plane geometry, solid geometry, functions), excluding advanced topics like calculus or combinatorics. The CoT evaluation pipeline depends on GPT-4V as the judge, introducing potential circularity when evaluating GPT-4V itself and coupling benchmark longevity to a proprietary model.\",\n    \"open_questions\": [\n      \"Can the DI/IP/EC information taxonomy be extended to other multimodal reasoning domains (e.g., scientific diagrams, engineering schematics, medical imaging) to expose similar text-reliance shortcuts?\",\n      \"What architectural changes to vision encoders would most improve diagram comprehension — is the bottleneck in low-level visual parsing (OCR, symbol recognition) or in higher-level spatial reasoning over extracted elements?\",\n      \"As models improve on MathVerse's vision-only setting, how should the benchmark evolve — do we need adversarial diagram perturbations or procedurally generated problems to prevent overfitting to the fixed 2,612-problem corpus?\"\n    ],\n    \"building_blocks\": [\n      \"Three-tier information taxonomy for multimodal problems (Descriptive Information / Implicit Property / Essential Condition)\",\n      \"Six-version problem transformation framework for controlled text-vision ablation\",\n      \"GPT-4V-based adaptive CoT step extraction and scoring pipeline\",\n      \"Weighted scoring formula combining step-level and final-answer accuracy (α=0.7)\",\n      \"Source datasets: GeoQA, UniGeo (for plane geometry problems), plus newly collected solid geometry and function problems\",\n      \"Error taxonomy for visual math: visual perception errors, reasoning errors, knowledge errors, calculation errors\",\n      \"Prompt engineering templates for both direct-answer and chain-of-thought elicitation\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is foundational to Multi-Modal Mathematical Reasoning research because it establishes that the visual understanding component — the hardest part of the integration problem — is largely unsolved and was being masked by evaluation artifacts. Any new work in integrating visual, symbolic, and textual understanding for math must contend with MathVerse's finding that models default to text-only reasoning. The DI/IP/EC taxonomy provides a precise vocabulary for designing experiments that genuinely test visual grounding, and the six-version methodology offers a reusable template for building evaluations that resist shortcut learning in any multimodal reasoning domain.\"\n  },\n  {\n    \"title\": \"Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset\",\n    \"venue\": \"NeurIPS 2024 (Datasets & Benchmarks Track)\",\n    \"problem_identification\": \"The authors noticed that LMMs were reportedly approaching human-level performance on MathVista (57.6% vs 60.3%), but instead of accepting this at face value, they performed a forensic audit of MathVista itself. They discovered that among its 375 abstract-scene questions, the vast majority collapsed into just 3 question types (object counting, length measurement, clock reading), and the subject scope was limited to plane geometry, tables, and charts. This meant the benchmark was giving a dangerously misleading signal — models appeared competent because the test was narrow, not because they could reason mathematically.\",\n    \"key_insight\": \"Benchmark saturation is not the same as capability saturation. By sourcing problems from real math competitions — which naturally demand diverse visual reasoning, multi-step logic, and cross-domain knowledge — you can construct a benchmark that exposes a 53-percentage-point gap (22.76% vs 75.66%) that was invisible on prior benchmarks. The key move was using competition provenance as a quality filter rather than trying to synthetically generate 'harder' questions.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"The authors collected ~9,000 problems from 19 real math competitions (Math Kangaroo, AMC 8/10/12, AIME, UK challenges, etc.), filtering for those with essential visual components (~3,500). A 4-stage curation pipeline followed: (1) alignment verification using Mathpix API to catch OCR/image errors, reducing to 3,352 problems; (2) deduplication via lexical overlap and Levenshtein distance, yielding 3,040 problems; (3) subject categorization by triple-annotated majority voting across 16 disciplines; and (4) difficulty assignment based on the grade level of the source competition. The final dataset is balanced 50.4/49.6% between multiple-choice and free-form answers. They evaluated 14 models (open and closed-source LMMs plus text-only LLMs) and conducted a detailed error taxonomy on GPT-4V's 232 failures, finding reasoning errors (42.2%), vision recognition errors (31.9%), knowledge errors (15.1%), and calculation errors (1.3%).\",\n    \"what_makes_it_good\": \"Three things made this paper compelling for reviewers: (1) the 'forensic audit' framing — instead of just building a harder benchmark, they convincingly demonstrated WHY existing benchmarks were misleading, making the contribution feel urgent; (2) the competition-sourcing strategy provided natural quality control and difficulty calibration without expensive expert authoring; (3) the error taxonomy moved beyond just reporting a gap to providing actionable diagnostic categories (vision recognition as bottleneck, reasoning as primary failure mode) that give the community clear targets. The 53-point human-model gap is a striking, memorable result that reframes the narrative about LMM mathematical competence.\",\n    \"limitations_acknowledged\": \"The authors identified three gaps: all problems are English-only, the dataset covers only mathematics (not physics/chemistry where multimodal reasoning also matters), and all images are abstract/schematic rather than real-world photographs — meaning the benchmark doesn't test perception of natural visual scenes.\",\n    \"open_questions\": [\n      \"How much of the 42.2% reasoning error is attributable to the LLM backbone vs. information loss during vision encoding? The paper hints the vision encoder is a bottleneck but doesn't disentangle these two failure modes.\",\n      \"Chain-of-thought prompting hurt Gemini Pro (-3.32%) and Qwen-VL-Max (-2.96%) — why does explicit reasoning degrade some models on visual math? This suggests CoT may amplify vision misinterpretation rather than correcting it.\",\n      \"As frontier models improve, will competition-sourced benchmarks face the same saturation problem? The paper doesn't discuss how to maintain benchmark longevity or whether the difficulty ceiling (Level 5 competition problems) is high enough for future models.\"\n    ],\n    \"building_blocks\": [\n      \"Mathpix API for PDF/image-to-LaTeX extraction\",\n      \"Levenshtein distance + lexical overlap for deduplication\",\n      \"Triple-annotator majority voting for subject categorization\",\n      \"Competition grade levels as difficulty proxy\",\n      \"4-category error taxonomy (reasoning, vision recognition, knowledge, calculation)\",\n      \"N-gram overlap analysis for data contamination detection\",\n      \"Zero-shot chain-of-thought prompting protocol from Kojima et al.\",\n      \"Math Kangaroo, AMC, AIME, UK Math Challenges as problem sources\"\n    ],\n    \"reviewer_feedback_summary\": \"Scores: 7, 8, 5, 8 (Accepted as Poster). Reviewers praised the competition-sourced quality, 16-discipline breadth, and the striking human-model gap. The most substantive concern came from Reviewer 3 (ZxmA, score 5) who raised multiple issues: some problems don't genuinely require images, data contamination risks, annotator qualifications for competition-level math, and copyright/licensing of competition problems. The authors effectively countered: only 2.89% of questions were image-independent, n-gram analysis showed <1% overlap with training data at 6-grams and 0% at 13-grams, and they obtained rights from AKSF (Kangaroo) and cited precedent for MAA problems. Reviewer 2 raised their score after the 'no image needed' rebuttal. Reviewer 3 never responded to the rebuttal. The ethics flag (competition problem licensing) was a real vulnerability — the MAA response ('did not receive negative feedback from board members') was the weakest defense, and stronger licensing documentation would have made the paper more bulletproof.\",\n    \"relevance_to_seed\": \"This paper is directly foundational to multi-modal mathematical reasoning research: it provides the most comprehensive diagnostic benchmark for understanding WHERE models fail at integrating visual, symbolic, and textual understanding. The key lesson for our research area is that the error taxonomy (42% reasoning, 32% vision recognition) reveals that the vision-to-symbol translation step is a critical bottleneck — future work on tighter integration of visual perception with symbolic reasoning should target this interface. The competition-sourcing methodology is also reusable: real competitions naturally produce problems requiring genuine multi-modal reasoning, avoiding the synthetic-data trap where problems can be solved by text alone.\"\n  },\n  {\n    \"title\": \"Vision-R1: Incentivizing Reasoning Capability in Multimodal Large Language Models\",\n    \"venue\": \"ICLR 2026 (Poster)\",\n    \"problem_identification\": \"The authors identified that while DeepSeek-R1-Zero showed reasoning can emerge in text-only LLMs via pure RL, this fails for multimodal LLMs — direct RL cannot activate complex reasoning (questioning, reflection, self-correction) in MLLMs due to the absence of high-quality multimodal reasoning data. They found this gap by attempting 'Vision-R1-Zero' (pure RL on MLLMs), which yielded only 50.7% accuracy and failed to produce long, structured CoT. The key diagnostic was that existing multimodal CoT datasets produce 'Pseudo-CoT' lacking genuine cognitive processes — verified by counting reflection markers like 'Wait' (585K instances in their data vs. 1,122 in Mulberry).\",\n    \"key_insight\": \"You can bootstrap high-quality multimodal reasoning data WITHOUT human annotation by using 'modality bridging' — having an MLLM convert images to rich text descriptions, then feeding those to a powerful text-only reasoning model (DeepSeek-R1) to generate genuine CoT. The second insight is that after cold-start SFT, models develop an 'overthinking problem' where correct reasoning concentrates in short sequences but RL pushes toward longer (incorrect) ones, which can be solved by progressively relaxing length constraints (PTST) rather than training at full length from the start.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Vision-R1 operates in two phases. Phase 1 (Cold Start): They construct a 200K multimodal CoT dataset by (a) using Qwen2.5-VL-72B to generate pseudo-CoT and detailed image descriptions from image-question pairs, (b) feeding these text descriptions to DeepSeek-R1 to produce high-quality reasoning chains with genuine reflection/questioning, and (c) filtering for answer correctness. The base model (Qwen2.5-VL-7B) is SFT'd on this dataset. Phase 2 (RL with PTST): They apply GRPO with a hard binary reward (1 if format correct AND answer correct, 0 otherwise) on 10K multimodal math problems. The key innovation is Progressive Thinking Suppression Training: Stage 1 constrains generation to 4K tokens with 16 samples per input (forcing concise correct reasoning), then Stage 2 relaxes to 8K tokens with 8 samples (allowing elaboration on the established reasoning foundation). This two-stage approach outperforms both short-only (54.3%) and long-only (47.7%) baselines, achieving 55.4% average and 73.5% on MathVista.\",\n    \"what_makes_it_good\": \"The paper succeeded because of its strong empirical results — a 7B model matching OpenAI o1 on MathVista is a striking headline number that demands attention. The modality bridging technique for data construction is clever and practical, requiring zero human annotation while producing demonstrably richer reasoning data than alternatives. The paper also identified and named a real phenomenon (the Overthinking Optimization Problem) and provided a simple, principled solution (PTST), giving reviewers a clear narrative arc from problem diagnosis to solution. Despite borderline initial scores (8/4/4/4), the authors' rebuttal — showing generalization to non-math benchmarks and providing contamination analysis — swung two reviewers from 4→6, and the AC judged merits outweighed flaws.\",\n    \"limitations_acknowledged\": \"The authors acknowledged that 'directly using RL to incentivize reasoning capability of MLLMs for solving complex reasoning problems remains a challenging task, especially under constraints of data quality and quantity, as well as computation resources.' They position the work as 'an early exploration' rather than a definitive solution, and all primary experiments used math-related datasets only.\",\n    \"open_questions\": [\n      \"Does PTST generalize beyond math to other reasoning domains (spatial, causal, temporal)? The rebuttal showed some transfer to MMMU/LogicVista, but systematic study is missing. A curriculum over reasoning types — not just length — could be more principled.\",\n      \"The modality bridging pipeline assumes the MLLM can produce sufficiently detailed image descriptions for DeepSeek-R1 to reason over. Reviewer XezA noted this creates 'answer-directed bias' — the descriptions are generated with knowledge of the question, potentially leaking answer structure. How much does this bias inflate benchmark numbers vs. genuine visual reasoning?\",\n      \"Why does adding a Stage 3 (16K tokens) degrade performance (55.4→53.4%)? The authors attribute this to 'model capacity limitations' of 7B models, but this raises a deeper question: is there a fundamental tension between model scale and the length of reasoning chains RL can optimize, and what is the scaling law for PTST stages?\"\n    ],\n    \"building_blocks\": [\n      \"GRPO (Group Relative Policy Optimization) — the RL algorithm from DeepSeek-R1\",\n      \"Modality Bridging — converting visual information to detailed text descriptions for text-only LLM processing\",\n      \"Hard binary formatting+correctness reward function (simple but effective)\",\n      \"Progressive Thinking Suppression Training — staged RL with increasing length limits and decreasing sample counts\",\n      \"Qwen2.5-VL-72B as a captioning/description backbone\",\n      \"DeepSeek-R1 as a text-only CoT generator\",\n      \"Vision-R1-cold dataset (200K multimodal CoT samples, publicly available)\",\n      \"Rule-based CoT filtering by ans\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T16:26:03.021Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T16:26:03.021Z",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-27T16:26:03.064Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-27 (UTC).**

## Research area: Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding

## Paper analyses (20 papers)

[
  {
    "title": "MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts",
    "venue": "ICLR 2024 (Oral, top 1.2%)",
    "problem_identification": "Prior to MathVista, mathematical reasoning and visual understanding were evaluated in separate silos — text-only math benchmarks (GSM8K, MATH) ignored visual input, while VQA benchmarks lacked mathematical depth. The authors identified that the *intersection* — tasks requiring both fine-grained visual perception and compositional mathematical reasoning — had never been systematically evaluated. They found this gap by observing that 28+ datasets existed across math-QA and VQA domains, but none unified them under a coherent taxonomy, and critical domains (puzzle-based logical reasoning, function plot analysis, scientific figure interpretation) had no dedicated evaluation at all.",
    "key_insight": "The core insight was that mathematical reasoning in visual contexts is not a simple sum of 'vision + math' but a distinct capability requiring compositional integration — and the right way to expose this was not to create one monolithic new dataset, but to consolidate and systematically organize existing fragmented resources under a principled three-dimensional taxonomy (task type × reasoning type × visual context), while surgically creating only the three new datasets needed to fill genuine gaps (IQTest, FunctionQA, PaperQA).",
    "innovation_type": "new_benchmark",
    "method_summary": "MathVista constructs a 6,141-example benchmark from 31 source datasets (28 existing + 3 new) organized along three taxonomic dimensions: 5 task types (FQA, GPS, MWP, TQA, VQA), 7 mathematical reasoning types (algebraic, arithmetic, geometric, logical, numeric, scientific, statistical), and 15 visual context types spanning geometry diagrams to medical images. The three new datasets — IQTest (logical reasoning on puzzle figures), FunctionQA (algebraic reasoning over function plots), and PaperQA (scientific reasoning from academic figures) — were created to fill specific coverage gaps. The evaluation protocol supports both multiple-choice and free-form answers with precision-aware scoring, and tests models under multiple augmentation strategies: zero-shot, few-shot (0–4), chain-of-thought (CoT), program-of-thought (PoT), and caption+OCR text augmentation for text-only LLMs. A 1,000-example testmini split enables fast development while the 5,141-example test split has private labels for fair leaderboard evaluation. The authors further explored GPT-4V's self-verification and self-consistency capabilities as novel analysis dimensions.",
    "what_makes_it_good": "Three factors propelled this to an oral: (1) *Timing and impact* — it launched alongside GPT-4V and immediately became the standard evaluation for the rapidly emerging multimodal reasoning field, filling an obvious-in-retrospect gap that nobody else had systematized. (2) *Methodological rigor in curation* — rather than brute-force creating a new dataset, the authors demonstrated that principled consolidation with a clear taxonomy (making existing scattered resources usable under a unified evaluation) was itself a first-class contribution, and they were surgical about creating only 3 new datasets to fill genuine holes. (3) *Comprehensive evaluation with actionable findings* — testing 12 models under multiple strategies with fine-grained error analysis (by reasoning type, visual context, grade level) produced diagnostic insights, not just a leaderboard number.",
    "limitations_acknowledged": "The authors acknowledged that MathVista cannot cleanly disentangle visual perception errors from mathematical reasoning errors — a model might fail because it misread a chart or because it couldn't solve the underlying math, and the benchmark doesn't distinguish these. Human performance at only 60.3% (with AMT annotators having high school diplomas or above) also raised questions about problem difficulty calibration versus annotation quality, which the authors addressed with Fleiss Kappa of 0.775 but did not fully resolve.",
    "open_questions": [
      "How can we design benchmarks that *disentangle* visual perception from mathematical reasoning — e.g., by providing ground-truth scene descriptions alongside images, enabling controlled ablation of the visual understanding component?",
      "Can we move beyond static evaluation to *process-level* assessment — evaluating not just final answers but intermediate reasoning steps, to understand where in the visual-to-symbolic-to-solution pipeline models break down?",
      "As models rapidly saturate MathVista (InternVL2-Pro at 65.8% now exceeds original human baselines), what is the next-generation benchmark that captures harder compositional reasoning, multi-step visual proofs, or dynamic/interactive mathematical contexts?"
    ],
    "building_blocks": [
      "Three-dimensional taxonomy framework (task type × reasoning type × visual context) — reusable for any multimodal benchmark design",
      "Consolidation-plus-surgical-creation methodology — curating 28 existing datasets + creating only 3 new ones to fill gaps",
      "Dual-split evaluation design (1K public testmini + 5K private test) with leaderboard infrastructure",
      "Multi-strategy evaluation protocol (zero-shot, few-shot, CoT, PoT, caption+OCR augmentation)",
      "Precision-aware scoring for free-form numerical answers",
      "Self-verification and self-consistency analysis as diagnostic tools for GPT-4V-class models",
      "Source datasets: GeoQA+, Geometry3K, UniGeo, CLEVR-Math, TabMWP, ChartQA, FigureQA, ScienceQA, AI2D, IconQA, and others",
      "AMT-based human performance baseline methodology with Fleiss Kappa inter-annotator agreement"
    ],
    "reviewer_feedback_summary": "**Scores**: 5, 8, 8, 8 (three accepts + one marginal reject → oral). **Key praise**: Reviewers lauded the well-designed taxonomy, comprehensive coverage from 31 sources, and the importance of the research area. Reviewer 2 called it 'well-designed and relatively large'; Reviewer 4 praised the 'thorough review of existing work.' **Key concerns**: (1) Cannot disentangle visual vs. mathematical reasoning failures (raised by Reviewers 2 and 4); (2) Human accuracy of only 60.3% raised data quality questions; (3) Initially missing GPT-4V results (paper submitted before GPT-4V launch). **Author response was decisive**: They added 67 pages including comprehensive GPT-4V analysis (49.9% accuracy), self-verification studies, expanded few-shot evaluations, and inter-annotator agreement (Fleiss Kappa 0.775). Reviewer 3 explicitly upgraded their assessment after the rebuttal, calling it 'a strong and interesting paper.' The Area Chair summarized: 'Benchmark is solid work... The work seems impactful for the community.' **What would have made it stronger**: A mechanism to isolate visual vs. reasoning errors, higher human baselines with expert annotators, and a finetuning training split.",
    "relevance_to_seed": "MathVista is the foundational evaluation infrastructure for our research area — any new method for multi-modal mathematical reasoning must benchmark against it. More importantly, its *methodology* teaches us how to identify fertile research directions: the taxonomy reveals that logical reasoning (19% accuracy for top models) and complex figure understanding remain the hardest unsolved problems, and the inability to disentangle visual from symbolic reasoning points directly to the need for architectures that make this decomposition explicit — a core opportunity in integrating visual, symbolic, and textual understanding."
  },
  {
    "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
    "venue": "Nature 645, 633–638 (2025)",
    "problem_identification": "The authors identified that the standard post-training paradigm (SFT on human reasoning traces → RL) inherently caps model reasoning at human-level performance because human demonstrations omit critical steps like self-verification and reflection, and they constrain the model to explore only human-like reasoning pathways. They found this gap by observing that SFT-trained models plateau on hard competition math/code while the base model's latent potential remained untapped—its pre-training on massive math/code corpora already gave it the raw ingredients for reasoning, but SFT was the bottleneck preventing self-discovery of superior strategies.",
    "key_insight": "If you skip SFT entirely and apply RL with only outcome-based rule rewards (correctness + format) directly on a strong base model, the model will autonomously discover sophisticated reasoning behaviors—self-reflection, verification, backtracking, and dynamic strategy switching—that were never explicitly taught. The 'aha moment' (the model spontaneously learning to say 'Wait, let me reconsider...') is not engineered but emergent, proving that reasoning is latent in pre-trained representations and can be unlocked purely through reward incentives.",
    "innovation_type": "simplification",
    "method_summary": "DeepSeek-R1-Zero applies Group Relative Policy Optimization (GRPO)—a PPO variant that eliminates the value model by computing advantages via group-relative normalization of sampled rewards—directly on the DeepSeek-V3-Base (671B MoE) model with no SFT warmup. Rewards are purely rule-based: binary accuracy (answer match or test-case pass) plus a format reward for using &lt;think>/&lt;answer> tags; no neural reward models are used, avoiding reward hacking. For each question, 16 outputs are sampled and advantages are computed as z-scores within each group (Equation 3). DeepSeek-R1 then builds on this via a multi-stage pipeline: (1) a small cold-start SFT using thousands of curated long-CoT samples from R1-Zero (rewritten for readability), (2) first RL stage with rule-based rewards plus a language consistency reward, (3) rejection sampling from the RL checkpoint to collect ~600K reasoning + ~200K non-reasoning SFT samples, (4) second RL stage combining rule-based reasoning rewards with model-based helpfulness/harmlessness rewards. Distillation transfers R1's reasoning traces to 1.5B–70B student models via SFT on R1-generated trajectories.",
    "what_makes_it_good": "Three factors made this Nature-worthy: (1) It is a bold, clean scientific claim backed by a striking empirical result—the 'aha moment' where a model spontaneously invents self-reflection is a genuinely surprising emergent phenomenon that captures imagination beyond ML. (2) The simplification narrative is compelling: removing SFT, removing neural reward models, and removing the PPO value model each reduces complexity while improving or matching performance, turning conventional wisdom on its head. (3) The open-source release of the full model family (including distilled 1.5B–70B variants that beat o1-mini) created massive real-world impact, and the paper was transparent about limitations like language mixing and reward hacking—a level of candor reviewers value.",
    "limitations_acknowledged": "The authors explicitly identify: (1) reward hacking remains unsolved for non-verifiable tasks (writing, open QA) where reliable rule-based rewards cannot be constructed; (2) token inefficiency and overthinking on simple problems; (3) language mixing when queries are in non-English/Chinese languages; (4) sensitivity to prompting (few-shot degrades performance); (5) limited improvement on software engineering tasks due to slow evaluation loops in RL; (6) structured output and tool use remain weak.",
    "open_questions": [
      "Can pure RL reasoning be extended to multimodal inputs (visual math, diagram reasoning, chart understanding) where reward verification is harder but still possible? The paper's framework only addresses text-in/text-out tasks.",
      "How do we construct reliable reward signals for 'soft' reasoning tasks (scientific argumentation, proof verification, multi-step real-world planning) where binary correctness is unavailable—can we break the reward hacking barrier that limited the paper to ~400 steps of model-based RL?",
      "What is the mechanistic explanation for the emergent reasoning behaviors? The paper documents the 'aha moment' phenomenologically but does not explain WHY or WHEN self-reflection emerges during training—understanding this could allow us to engineer it more efficiently or in smaller models without distillation."
    ],
    "building_blocks": [
      "GRPO (Group Relative Policy Optimization) — value-model-free RL algorithm with group-relative advantage estimation",
      "Rule-based reward design (accuracy + format) for verifiable tasks — avoids neural reward model fragility",
      "Language consistency reward (target-language word proportion) for controlling code-switching",
      "Cold-start data curation pipeline: sample from R1-Zero → filter correct + readable → rewrite with LLM → human verify",
      "Rejection sampling from RL checkpoint to generate high-quality SFT data at scale (~600K samples)",
      "Multi-stage training pipeline: cold-start SFT → reasoning RL → rejection sampling SFT → general RL",
      "Distillation via SFT on teacher-generated long-CoT reasoning traces",
      "DeepSeek-V3-Base (671B MoE, 37B active) as foundation model",
      "vLLM-based rollout infrastructure with expert parallelism and speculative decoding for efficient RL",
      "DualPipe algorithm for efficient pipeline parallelism in training"
    ],
    "reviewer_feedback_summary": "Nature peer review comments were behind a paywall and could not be accessed directly. However, based on the paper's structure and the v1→v2 revision (Jan 2025 → Jan 2026), key likely reviewer concerns can be inferred: (1) the paper added extensive ablation studies (GRPO vs PPO comparison in Appendix A.3, clip ratio sensitivity, language consistency reward ablation in B.6), suggesting reviewers demanded more rigorous experimental controls; (2) the ethics/safety section (Section 5) with comprehensive safety benchmarks was likely expanded per reviewer request given the Nature audience; (3) the detailed data contamination analysis and fresh test set evaluations suggest reviewers questioned benchmark validity; (4) the transparency about pre-training data containing reasoning traces (Appendix A.1) and the careful distancing from claims of 'human-like intelligence' (Section B.3.2) suggest reviewers pushed back on overclaiming about emergent cognition.",
    "relevance_to_seed": "This paper is the direct ancestor of the multimodal RL-reasoning line of work. Its GRPO algorithm, rule-based reward design, and multi-stage training pipeline are immediately applicable to visual-mathematical reasoning tasks where answers are verifiable (e.g., geometry diagram problems, chart-based calculations, visual equation solving). The key lesson for our research area is that the bottleneck to multimodal math reasoning may not be better vision encoders or more labeled data, but rather designing the right RL reward structure that lets models discover their own visual-symbolic-textual integration strategies through self-play—just as DeepSeek-R1 discovered self-reflection without being taught it."
  },
  {
    "title": "URSA: Understanding and Verifying Chain-of-thought Reasoning in Multimodal Mathematics",
    "venue": "NeurIPS 2025 (Poster)",
    "problem_identification": "The authors observed that Process Reward Models (PRMs) had proven highly effective for text-only LLM math reasoning via test-time scaling and RL, yet their integration into multimodal reasoning was entirely unexplored. They diagnosed three concrete bottlenecks blocking this transfer: (1) no large-scale multimodal CoT data to build strong enough foundation models for PRM-based methods to improve upon, (2) no automated process labeling technique that captures both logical errors AND perceptual hallucinations unique to vision-language settings, and (3) naive scalar PRM integration into RL causes reward hacking and length bias. The gap was found by systematically attempting the text-only PRM playbook in the multimodal setting and documenting where each step broke down.",
    "key_insight": "While absolute PRM scalar rewards become unreliable during online RL training (the model games them), the PRM's ability to detect *relative drops* between consecutive reasoning steps ('drop-moments') remains trustworthy. This means process supervision can be converted from an unreliable scalar signal into a robust binary penalty on outcome rewards — you don't need to trust the PRM's numbers, only its ability to spot when something goes wrong relative to the previous step.",
    "innovation_type": "combination",
    "method_summary": "URSA is a three-stage pipeline. Stage I synthesizes MMathCoT-1M by collecting 1.43M multimodal math samples and applying CoT expansion (for answer-only data), rewriting (for analysis-format data), and format unification (for existing CoT data) via a strong LLM, then filtering for correctness/consistency; SFT on this yields URSA-8B. Stage II constructs DualMath-1.1M via two complementary engines: a Binary Error Locating Engine (BEL) that uses MCTS with binary search to efficiently locate first-error steps in ~553K incorrect solutions, and a Misinterpretation Insertion Engine (MIE) that artificially injects perceptual hallucinations into ~302K correct solutions to create process-level supervision for vision-text inconsistencies. Stage III introduces PS-GRPO: rather than using PRM scalar rewards directly (shown to cause reward hacking and length bias), the method detects 'drop-moments' — significant relative decreases in PRM reward between consecutive steps — and applies a penalty γ to outcome-correct rollouts that exhibit such drops, thus differentiating high-quality from lucky reasoning without being susceptible to the PRM's absolute score biases.",
    "what_makes_it_good": "The paper succeeds because it identifies a clearly important open problem (PRMs for multimodal math) and systematically addresses *all three* bottlenecks rather than proposing a single trick. The negative results analysis — showing exactly how and why naive scalar PRM rewards fail before introducing PS-GRPO — demonstrates intellectual rigor that reviewers valued. The 8B model outperforming GPT-4o by 2.7% across six benchmarks is a compelling headline result, and the release of two large-scale public datasets (MMathCoT-1M and DualMath-1.1M) provides lasting community value beyond the method itself.",
    "limitations_acknowledged": "The authors note a significant performance gap on DynaMath, suggesting smaller-scale MLLMs still lack robust problem-solving capabilities on dynamic/adversarial benchmarks. No formal limitations section is included, but reviewers flagged high computational cost (~$320 for data synthesis using Gemini-1.5-Flash), limited theoretical justification for the drop-moment threshold, and concerns about synthetic process label quality.",
    "open_questions": [
      "Can the drop-moment concept be grounded theoretically (e.g., via Q-value ranking properties) rather than relying on empirical threshold tuning, and can adaptive thresholds outperform fixed ρ values?",
      "How well does this pipeline transfer beyond mathematics — do dual-view process supervision and PS-GRPO generalize to other multimodal reasoning domains (science, coding with visual specs, chart understanding) where perceptual consistency also matters?",
      "What is the quality ceiling of synthetic process labels vs. human annotations — the authors showed 87.6% LLM-as-judge consistency, but does the remaining ~12% noise systematically bias the PRM in ways that compound during RL training?"
    ],
    "building_blocks": [
      "MCTS-based process annotation with binary search for efficient first-error localization (BEL)",
      "Misinterpretation Insertion Engine for synthetic hallucination-based negative examples (MIE)",
      "Drop-moment detection as a robust signal extraction method from noisy reward models",
      "PS-GRPO: process-as-outcome penalty RL method compatible with standard GRPO",
      "MMathCoT-1M dataset (1M multimodal CoT samples from 1.43M open-source examples)",
      "DualMath-1.1M dataset (1.1M process supervision annotations)",
      "LLaVA-like architecture with math-intensive alignment pretraining (URSA-Alignment-860K)",
      "Three-category CoT synthesis strategy: expansion, rewriting, format unification",
      "Dual correctness filtering (answer correctness + reasoning consistency)"
    ],
    "reviewer_feedback_summary": "Four reviewers rated the paper 4/4/3/3, accepted as poster. **Praise**: Timely and important direction (first to integrate PRMs into multimodal math reasoning), strong empirical results across six benchmarks, solid ablation studies demonstrating each component's contribution, high-quality public dataset releases, and well-written presentation. **Key concerns**: (1) Reviewer 4akc argued limited algorithmic novelty — PS-GRPO resembles DeepSeekMath's step-level GRPO and the pipeline is primarily engineering; authors responded with direct DS-GRPO comparison showing PS-GRPO wins (58.2 vs. 56.5 avg). (2) Reviewer U6mC questioned theoretical justification for ρ=0.3 and synthetic label quality; authors provided Q-value ranking theorem grounding and 87.6% LLM-judge validation. (3) Reviewer GTaC found gains 'modest' and novelty limited to applying LLM paradigms to vision; authors added ORM baselines (PRM outperforms 55.0 vs. 54.3). (4) Reviewer E38C requested confidence intervals; authors provided ±0.1-0.5% ranges. The engineering-vs-novelty tension was the central debate — the paper survived by demonstrating that the specific combination and the drop-moment insight are non-obvious and empirically validated.",
    "relevance_to_seed": "This paper is directly central to multi-modal mathematical reasoning research. Its key lessons for our area are: (1) the 'dual-view' framing — treating logical validity and perceptual consistency as separate supervision signals — is a powerful decomposition that could inspire new approaches to visual-symbolic integration, and (2) the finding that relative PRM signals (drop-moments) are trustworthy while absolute scores are not provides a principled way to incorporate process supervision into any multimodal reasoning RL pipeline, opening a concrete path for future work on visual theorem proving, diagram reasoning, and cross-modal verification."
  },
  {
    "title": "MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?",
    "venue": "ECCV 2024",
    "problem_identification": "The authors discovered that existing visual math benchmarks (MathVista, GeoQA, MMMU) encode excessive textual redundancy — the problem text duplicates information already present in diagrams. By running a simple ablation (removing the diagram entirely), they showed that most MLLMs perform the same or *better* without visual input (e.g., Qwen-VL-Max +5.1%, InternLM-XComposer2 +5.6%). This means the field's reported progress on 'visual math reasoning' was partially illusory — models were solving problems from text, not from diagrams.",
    "key_insight": "The information in a visual math problem can be decomposed into three semantic types — Descriptive Information (directly observable), Implicit Properties (perceptually extractable), and Essential Conditions (numeric/algebraic specifics) — and by systematically controlling which types appear in text vs. diagram across six problem versions, you can precisely isolate and quantify the degree to which a model genuinely interprets visual content versus exploiting textual shortcuts.",
    "innovation_type": "new_benchmark",
    "method_summary": "The authors curated 2,612 high-quality math problems with diagrams across plane geometry (1,746), solid geometry (332), and functions (534). Human annotators then classified each problem's textual content into three information types (DI, IP, EC) and created six versions per problem: text-dominant (full text + diagram), text-lite (no DI), text-only (no diagram), vision-intensive (no IP in text), vision-dominant (no EC in text), and vision-only (all info in diagram only) — yielding ~15K test instances. For evaluation, they introduced a CoT scoring pipeline where GPT-4 first extracts key reasoning steps from model outputs (without seeing the ground truth answer, to avoid bias), then GPT-4V scores each step against the diagram and ground truth, producing a weighted score: Score = 0.7 × (average step correctness) + 0.3 × (final answer correctness). This reveals intermediate reasoning quality beyond binary accuracy.",
    "what_makes_it_good": "The paper succeeds because it identifies a methodological blind spot hiding in plain sight — the entire field was benchmarking 'visual reasoning' with benchmarks that don't require vision — and provides an elegant, systematic solution rather than just pointing out the problem. The six-version transformation framework is simple to understand, rigorous in execution, and immediately useful as an evaluation tool. The CoT evaluation strategy adds a second complementary contribution, making the paper a complete evaluation package rather than just a dataset release.",
    "limitations_acknowledged": "The benchmark is limited to high-school-level mathematics (plane geometry, solid geometry, functions), excluding advanced topics like calculus or combinatorics. The CoT evaluation pipeline depends on GPT-4V as the judge, introducing potential circularity when evaluating GPT-4V itself and coupling benchmark longevity to a proprietary model.",
    "open_questions": [
      "Can the DI/IP/EC information taxonomy be extended to other multimodal reasoning domains (e.g., scientific diagrams, engineering schematics, medical imaging) to expose similar text-reliance shortcuts?",
      "What architectural changes to vision encoders would most improve diagram comprehension — is the bottleneck in low-level visual parsing (OCR, symbol recognition) or in higher-level spatial reasoning over extracted elements?",
      "As models improve on MathVerse's vision-only setting, how should the benchmark evolve — do we need adversarial diagram perturbations or procedurally generated problems to prevent overfitting to the fixed 2,612-problem corpus?"
    ],
    "building_blocks": [
      "Three-tier information taxonomy for multimodal problems (Descriptive Information / Implicit Property / Essential Condition)",
      "Six-version problem transformation framework for controlled text-vision ablation",
      "GPT-4V-based adaptive CoT step extraction and scoring pipeline",
      "Weighted scoring formula combining step-level and final-answer accuracy (α=0.7)",
      "Source datasets: GeoQA, UniGeo (for plane geometry problems), plus newly collected solid geometry and function problems",
      "Error taxonomy for visual math: visual perception errors, reasoning errors, knowledge errors, calculation errors",
      "Prompt engineering templates for both direct-answer and chain-of-thought elicitation"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is foundational to Multi-Modal Mathematical Reasoning research because it establishes that the visual understanding component — the hardest part of the integration problem — is largely unsolved and was being masked by evaluation artifacts. Any new work in integrating visual, symbolic, and textual understanding for math must contend with MathVerse's finding that models default to text-only reasoning. The DI/IP/EC taxonomy provides a precise vocabulary for designing experiments that genuinely test visual grounding, and the six-version methodology offers a reusable template for building evaluations that resist shortcut learning in any multimodal reasoning domain."
  },
  {
    "title": "Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset",
    "venue": "NeurIPS 2024 (Datasets & Benchmarks Track)",
    "problem_identification": "The authors noticed that LMMs were reportedly approaching human-level performance on MathVista (57.6% vs 60.3%), but instead of accepting this at face value, they performed a forensic audit of MathVista itself. They discovered that among its 375 abstract-scene questions, the vast majority collapsed into just 3 question types (object counting, length measurement, clock reading), and the subject scope was limited to plane geometry, tables, and charts. This meant the benchmark was giving a dangerously misleading signal — models appeared competent because the test was narrow, not because they could reason mathematically.",
    "key_insight": "Benchmark saturation is not the same as capability saturation. By sourcing problems from real math competitions — which naturally demand diverse visual reasoning, multi-step logic, and cross-domain knowledge — you can construct a benchmark that exposes a 53-percentage-point gap (22.76% vs 75.66%) that was invisible on prior benchmarks. The key move was using competition provenance as a quality filter rather than trying to synthetically generate 'harder' questions.",
    "innovation_type": "new_benchmark",
    "method_summary": "The authors collected ~9,000 problems from 19 real math competitions (Math Kangaroo, AMC 8/10/12, AIME, UK challenges, etc.), filtering for those with essential visual components (~3,500). A 4-stage curation pipeline followed: (1) alignment verification using Mathpix API to catch OCR/image errors, reducing to 3,352 problems; (2) deduplication via lexical overlap and Levenshtein distance, yielding 3,040 problems; (3) subject categorization by triple-annotated majority voting across 16 disciplines; and (4) difficulty assignment based on the grade level of the source competition. The final dataset is balanced 50.4/49.6% between multiple-choice and free-form answers. They evaluated 14 models (open and closed-source LMMs plus text-only LLMs) and conducted a detailed error taxonomy on GPT-4V's 232 failures, finding reasoning errors (42.2%), vision recognition errors (31.9%), knowledge errors (15.1%), and calculation errors (1.3%).",
    "what_makes_it_good": "Three things made this paper compelling for reviewers: (1) the 'forensic audit' framing — instead of just building a harder benchmark, they convincingly demonstrated WHY existing benchmarks were misleading, making the contribution feel urgent; (2) the competition-sourcing strategy provided natural quality control and difficulty calibration without expensive expert authoring; (3) the error taxonomy moved beyond just reporting a gap to providing actionable diagnostic categories (vision recognition as bottleneck, reasoning as primary failure mode) that give the community clear targets. The 53-point human-model gap is a striking, memorable result that reframes the narrative about LMM mathematical competence.",
    "limitations_acknowledged": "The authors identified three gaps: all problems are English-only, the dataset covers only mathematics (not physics/chemistry where multimodal reasoning also matters), and all images are abstract/schematic rather than real-world photographs — meaning the benchmark doesn't test perception of natural visual scenes.",
    "open_questions": [
      "How much of the 42.2% reasoning error is attributable to the LLM backbone vs. information loss during vision encoding? The paper hints the vision encoder is a bottleneck but doesn't disentangle these two failure modes.",
      "Chain-of-thought prompting hurt Gemini Pro (-3.32%) and Qwen-VL-Max (-2.96%) — why does explicit reasoning degrade some models on visual math? This suggests CoT may amplify vision misinterpretation rather than correcting it.",
      "As frontier models improve, will competition-sourced benchmarks face the same saturation problem? The paper doesn't discuss how to maintain benchmark longevity or whether the difficulty ceiling (Level 5 competition problems) is high enough for future models."
    ],
    "building_blocks": [
      "Mathpix API for PDF/image-to-LaTeX extraction",
      "Levenshtein distance + lexical overlap for deduplication",
      "Triple-annotator majority voting for subject categorization",
      "Competition grade levels as difficulty proxy",
      "4-category error taxonomy (reasoning, vision recognition, knowledge, calculation)",
      "N-gram overlap analysis for data contamination detection",
      "Zero-shot chain-of-thought prompting protocol from Kojima et al.",
      "Math Kangaroo, AMC, AIME, UK Math Challenges as problem sources"
    ],
    "reviewer_feedback_summary": "Scores: 7, 8, 5, 8 (Accepted as Poster). Reviewers praised the competition-sourced quality, 16-discipline breadth, and the striking human-model gap. The most substantive concern came from Reviewer 3 (ZxmA, score 5) who raised multiple issues: some problems don't genuinely require images, data contamination risks, annotator qualifications for competition-level math, and copyright/licensing of competition problems. The authors effectively countered: only 2.89% of questions were image-independent, n-gram analysis showed <1% overlap with training data at 6-grams and 0% at 13-grams, and they obtained rights from AKSF (Kangaroo) and cited precedent for MAA problems. Reviewer 2 raised their score after the 'no image needed' rebuttal. Reviewer 3 never responded to the rebuttal. The ethics flag (competition problem licensing) was a real vulnerability — the MAA response ('did not receive negative feedback from board members') was the weakest defense, and stronger licensing documentation would have made the paper more bulletproof.",
    "relevance_to_seed": "This paper is directly foundational to multi-modal mathematical reasoning research: it provides the most comprehensive diagnostic benchmark for understanding WHERE models fail at integrating visual, symbolic, and textual understanding. The key lesson for our research area is that the error taxonomy (42% reasoning, 32% vision recognition) reveals that the vision-to-symbol translation step is a critical bottleneck — future work on tighter integration of visual perception with symbolic reasoning should target this interface. The competition-sourcing methodology is also reusable: real competitions naturally produce problems requiring genuine multi-modal reasoning, avoiding the synthetic-data trap where problems can be solved by text alone."
  },
  {
    "title": "Vision-R1: Incentivizing Reasoning Capability in Multimodal Large Language Models",
    "venue": "ICLR 2026 (Poster)",
    "problem_identification": "The authors identified that while DeepSeek-R1-Zero showed reasoning can emerge in text-only LLMs via pure RL, this fails for multimodal LLMs — direct RL cannot activate complex reasoning (questioning, reflection, self-correction) in MLLMs due to the absence of high-quality multimodal reasoning data. They found this gap by attempting 'Vision-R1-Zero' (pure RL on MLLMs), which yielded only 50.7% accuracy and failed to produce long, structured CoT. The key diagnostic was that existing multimodal CoT datasets produce 'Pseudo-CoT' lacking genuine cognitive processes — verified by counting reflection markers like 'Wait' (585K instances in their data vs. 1,122 in Mulberry).",
    "key_insight": "You can bootstrap high-quality multimodal reasoning data WITHOUT human annotation by using 'modality bridging' — having an MLLM convert images to rich text descriptions, then feeding those to a powerful text-only reasoning model (DeepSeek-R1) to generate genuine CoT. The second insight is that after cold-start SFT, models develop an 'overthinking problem' where correct reasoning concentrates in short sequences but RL pushes toward longer (incorrect) ones, which can be solved by progressively relaxing length constraints (PTST) rather than training at full length from the start.",
    "innovation_type": "combination",
    "method_summary": "Vision-R1 operates in two phases. Phase 1 (Cold Start): They construct a 200K multimodal CoT dataset by (a) using Qwen2.5-VL-72B to generate pseudo-CoT and detailed image descriptions from image-question pairs, (b) feeding these text descriptions to DeepSeek-R1 to produce high-quality reasoning chains with genuine reflection/questioning, and (c) filtering for answer correctness. The base model (Qwen2.5-VL-7B) is SFT'd on this dataset. Phase 2 (RL with PTST): They apply GRPO with a hard binary reward (1 if format correct AND answer correct, 0 otherwise) on 10K multimodal math problems. The key innovation is Progressive Thinking Suppression Training: Stage 1 constrains generation to 4K tokens with 16 samples per input (forcing concise correct reasoning), then Stage 2 relaxes to 8K tokens with 8 samples (allowing elaboration on the established reasoning foundation). This two-stage approach outperforms both short-only (54.3%) and long-only (47.7%) baselines, achieving 55.4% average and 73.5% on MathVista.",
    "what_makes_it_good": "The paper succeeded because of its strong empirical results — a 7B model matching OpenAI o1 on MathVista is a striking headline number that demands attention. The modality bridging technique for data construction is clever and practical, requiring zero human annotation while producing demonstrably richer reasoning data than alternatives. The paper also identified and named a real phenomenon (the Overthinking Optimization Problem) and provided a simple, principled solution (PTST), giving reviewers a clear narrative arc from problem diagnosis to solution. Despite borderline initial scores (8/4/4/4), the authors' rebuttal — showing generalization to non-math benchmarks and providing contamination analysis — swung two reviewers from 4→6, and the AC judged merits outweighed flaws.",
    "limitations_acknowledged": "The authors acknowledged that 'directly using RL to incentivize reasoning capability of MLLMs for solving complex reasoning problems remains a challenging task, especially under constraints of data quality and quantity, as well as computation resources.' They position the work as 'an early exploration' rather than a definitive solution, and all primary experiments used math-related datasets only.",
    "open_questions": [
      "Does PTST generalize beyond math to other reasoning domains (spatial, causal, temporal)? The rebuttal showed some transfer to MMMU/LogicVista, but systematic study is missing. A curriculum over reasoning types — not just length — could be more principled.",
      "The modality bridging pipeline assumes the MLLM can produce sufficiently detailed image descriptions for DeepSeek-R1 to reason over. Reviewer XezA noted this creates 'answer-directed bias' — the descriptions are generated with knowledge of the question, potentially leaking answer structure. How much does this bias inflate benchmark numbers vs. genuine visual reasoning?",
      "Why does adding a Stage 3 (16K tokens) degrade performance (55.4→53.4%)? The authors attribute this to 'model capacity limitations' of 7B models, but this raises a deeper question: is there a fundamental tension between model scale and the length of reasoning chains RL can optimize, and what is the scaling law for PTST stages?"
    ],
    "building_blocks": [
      "GRPO (Group Relative Policy Optimization) — the RL algorithm from DeepSeek-R1",
      "Modality Bridging — converting visual information to detailed text descriptions for text-only LLM processing",
      "Hard binary formatting+correctness reward function (simple but effective)",
      "Progressive Thinking Suppression Training — staged RL with increasing length limits and decreasing sample counts",
      "Qwen2.5-VL-72B as a captioning/description backbone",
      "DeepSeek-R1 as a text-only CoT generator",
      "Vision-R1-cold dataset (200K multimodal CoT samples, publicly available)",
      "Rule-based CoT filtering by ans
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
  "promptId": "7b5187d0-5038-4eb4-99a9-836a0409b48b",
  "type": "user",
  "uuid": "8e8db6df-e0e1-4627-a2f4-a29f620dd634",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T16:26:03.063Z_

```json
{
  "parentUuid": "8e8db6df-e0e1-4627-a2f4-a29f620dd634",
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
  "uuid": "6b611e74-13ae-4f50-af10-29d32f226b33",
  "timestamp": "2026-05-27T16:26:03.063Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T16:26:03.063Z_

```json
{
  "parentUuid": "6b611e74-13ae-4f50-af10-29d32f226b33",
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
  "uuid": "b82d6c3d-7b43-4d65-8cb3-92bfdf0cc99a",
  "timestamp": "2026-05-27T16:26:03.063Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-27T16:26:03.063Z_

```json
{
  "parentUuid": "b82d6c3d-7b43-4d65-8cb3-92bfdf0cc99a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2e604747-f38a-47aa-b308-059d8c89d022",
  "timestamp": "2026-05-27T16:26:03.063Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-27 (UTC).**  ## Research area: Multi-Modal Mathematical Reasoning —…",
  "leafUuid": "2e604747-f38a-47aa-b308-059d8c89d022",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize multimodal math reasoning literature into strategy guide",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa"
}
```

---

### Assistant

_source line 9 · 2026-05-27T16:26:22.917Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 20 paper analyses into a strategic "Field Guide" for multi-modal mathematical reasoning research. Let me carefully analyze all the papers provided (noting that the input was truncated at paper 8, but I have detailed analyses for papers 1-7 and partial for paper 8).

Let me work with what I have - the 7+ papers provide rich material. Let me identify patterns, gaps, reviewer preferences, etc.

Wait, the user said 20 papers but the input was truncated. Let me work with what I have - the 7 papers with full analyses contain enough signal to produce a high-quality synthesis. 

Now I'm cataloging the papers I have access to: MathVista from ICLR 2024 as an oral presentation, DeepSeek-R1 published in Nature 2025, URSA at NeurIPS 2025, MathVerse from ECCV 2024, MATH-Vision at NeurIPS 2024, and Vision-R1 slated for ICLR 2026, plus partial information on additional papers. With these seven papers as my foundation, I can identify the key innovation patterns, methodological approaches, and strategic insights that define this research area. Let me start synthesizing these into the requested JSON format, focusing on what the evidence actually shows across these high-impact venues.

The innovation patterns I'm seeing cluster around several themes: papers like MathVista, MathVerse, and MATH-Vision all conducted critical audits of existing benchmarks, uncovered systematic flaws, and then constructed improved evaluation frameworks; DeepSeek-R1 demonstrated that removing components like supervised fine-tuning and value models actually improved performance, challenging conventional wisdom; URSA showed how to thoughtfully combine existing techniques like process reward models, group relative policy optimization, and dual-view supervision; Vision-R1 bridged modalities by leveraging text-only models to generate multimodal chain-of-thought data; and MathVista introduced taxonomy-driven analysis while MathVerse and others used structured taxonomies to identify capability gaps. For reviewer preferences, I'm noticing a strong appreciation for forensic analysis that exposes problems in prior work, negative results that justify the contribution, public releases of datasets or resources, detailed ablations proving each component matters, and careful positioning around whether the work is primarily engineering or introducing fundamentally novel concepts.

Looking at what's still unexplored, there are clear gaps: disentangling visual perception from mathematical reasoning remains unsolved, process-level evaluation needs more work, reinforcement learning for multimodal reasoning with non-verifiable rewards is largely untouched, and the theoretical foundations underlying these empirical techniques are weak. Some promising untried combinations include merging MathVerse's controlled multi-version evaluation with URSA's dual-view PRM training, combining DeepSeek-R1's pure RL approach with formal visual grounding, or leveraging competition-sourced data alongside process supervision. I should also watch out for common pitfalls: benchmarks that don't actually require vision, using absolute PRM scores which tend to cause reward hacking, claiming visual reasoning improvements without proper controlled ablations, and overcomplicating the RL formulation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e604747-f38a-47aa-b308-059d8c89d022",
  "isSidechain": false,
  "requestId": "req_011CbTPM1TVQtYirypttVps3",
  "type": "assistant",
  "uuid": "76a3681b-6d8b-4b6e-917e-c7861dd93490",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cNJfj3ekspL43bEH2QWUF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11817,
      "cache_read_input_tokens": 10620,
      "output_tokens": 9184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 9184,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 11817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11817
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

_source line 10 · 2026-05-27T16:29:48.896Z_

I'll analyze the papers systematically to build a comprehensive field guide. Let me first review the full set of provided analyses carefully, then synthesize patterns.

Given the depth of the 7+ detailed paper analyses provided (the input was truncated mid-paper but contains rich material), let me produce the strategic synthesis:

```json
{
  "innovation_patterns": [
    {
      "pattern": "Forensic Audit → Reframed Benchmark",
      "description": "Identify a methodological flaw hiding in existing benchmarks (e.g., text leakage, narrow question types, shortcut exploitation), demonstrate the flaw empirically with a simple ablation, then construct a new benchmark that eliminates the flaw and reveals a much larger capability gap than previously reported. The audit itself is half the contribution — it reframes the field's understanding of where things stand.",
      "examples": ["MathVerse (showed models perform same/better WITHOUT diagrams, exposing text-reliance)", "MATH-Vision (forensic audit of MathVista showing 375 abstract-scene questions collapse to 3 types)", "MathVista (identified 28 fragmented datasets with no unified evaluation)"],
      "success_rate": "high"
    },
    {
      "pattern": "Principled Taxonomy → Surgical Gap Filling",
      "description": "Rather than creating a monolithic new dataset, construct a multi-dimensional taxonomy of the problem space, map existing resources onto it, and surgically create only the datasets needed to fill genuine coverage gaps. The taxonomy itself becomes a reusable community tool. This pattern consistently earns reviewer praise for rigor over brute-force data collection.",
      "examples": ["MathVista (3D taxonomy: task type × reasoning type × visual context, created only 3 new datasets out of 31)", "MathVerse (DI/IP/EC information taxonomy enabling 6 controlled problem versions)"],
      "success_rate": "high"
    },
    {
      "pattern": "Simplification as Innovation",
      "description": "Remove an assumed-necessary component (SFT warmup, value model, neural reward model) and show that the simpler system matches or exceeds the complex one. The narrative power comes from overturning conventional wisdom — each removal must be accompanied by a clear explanation of WHY the removed component was actually a bottleneck, not just that it can be dropped.",
      "examples": ["DeepSeek-R1 (removed SFT, removed value model, removed neural reward model — each simplification improved or matched performance)", "DeepSeek-R1-Zero (pure RL with only rule-based rewards produced emergent self-reflection)"],
      "success_rate": "high"
    },
    {
      "pattern": "Negative Result → Principled Fix",
      "description": "Attempt the obvious transfer of a text-only technique to the multimodal setting, document exactly WHERE and WHY it breaks, then introduce a targeted fix for each failure mode. The negative result analysis is as important as the solution — it demonstrates intellectual rigor and gives reviewers confidence the solution addresses root causes rather than symptoms.",
      "examples": ["URSA (showed naive scalar PRM rewards cause reward hacking → invented drop-moment detection)", "Vision-R1 (showed Vision-R1-Zero pure RL fails at 50.7% → diagnosed absence of quality CoT data → modality bridging)", "URSA (documented three specific bottlenecks blocking PRM transfer to multimodal, addressed all three)"],
      "success_rate": "high"
    },
    {
      "pattern": "Cross-Modal Data Bootstrapping",
      "description": "Use a strong model in one modality to generate training data for another modality, avoiding expensive human annotation. The key is a 'bridging' step that translates between modalities (e.g., image→text description→reasoning chain, or correct solution→injected hallucination→process label). Quality filtering (correctness, consistency, deduplication) is essential to make synthetic data competitive with human-authored data.",
      "examples": ["Vision-R1 (image→description via Qwen2.5-VL-72B→CoT via DeepSeek-R1)", "URSA (MMathCoT-1M via CoT expansion/rewriting/unification; DualMath-1.1M via MCTS error localization + hallucination injection)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Multi-Stage Training Pipeline with Escalating Sophistication",
      "description": "Structure training as a sequence of stages where each stage builds on the previous one's checkpoint: cold-start SFT → reasoning-focused RL → rejection sampling → general RL. Each stage uses progressively more sophisticated data and reward signals. The pipeline structure itself becomes the contribution, as it's reusable and each stage can be independently ablated.",
      "examples": ["DeepSeek-R1 (cold-start SFT → reasoning RL → rejection sampling SFT → general RL)", "URSA (math-alignment SFT → CoT SFT → PS-GRPO RL)", "Vision-R1 (cold-start SFT → PTST staged RL)"],
      "success_rate": "high"
    }
  ],

  "reviewer_preferences": [
    "**Ablation studies that isolate each component's marginal contribution.** Across all reviewed papers, the single most frequent reviewer request was component-level ablation. URSA's acceptance hinged on showing PS-GRPO > DS-GRPO (58.2 vs 56.5). Vision-R1's rebuttal survived by adding PTST ablations (short-only 54.3% vs staged 55.4%). Papers that preempt this demand fare better than those that add ablations in rebuttal.",
    "**Negative results and failure analysis before the proposed solution.** Reviewers consistently praised papers that showed WHY the obvious approach fails before introducing their fix. URSA's analysis of naive PRM reward hacking, Vision-R1's Vision-R1-Zero failure (50.7%), and MathVerse's 'models work better without images' ablation all earned explicit reviewer praise. This pattern builds trust that the authors understand the problem deeply.",
    "**Public dataset and resource releases with lasting community value.** URSA released MMathCoT-1M and DualMath-1.1M; Vision-R1 released Vision-R1-cold (200K samples); MathVista provided a dual-split leaderboard. Reviewers consistently flag public resource releases as a reason to accept, especially when the contribution might otherwise be seen as 'just engineering.'",
    "**Decisive rebuttals with new experiments, not just clarifications.** MathVista's rebuttal added 67 pages including GPT-4V analysis, upgrading Reviewer 3's score. Vision-R1 added generalization experiments to non-math benchmarks and contamination analysis, swinging two reviewers from 4→6. MATH-Vision countered 'image-independent questions' with a 2.89% quantification. In this field, rebuttals that add data consistently win; rebuttals that only argue do not.",
    "**Honest limitation acknowledgment and transparent negative results.** DeepSeek-R1's candor about reward hacking, language mixing, and overthinking was explicitly noted as valuable. URSA's gap on DynaMath was acknowledged. Papers that try to hide weaknesses get caught — reviewers in this area are sophisticated enough to spot evasion, and honesty builds credibility for the claims that ARE made.",
    "**Headline-worthy quantitative gaps that reframe the narrative.** MATH-Vision's 53-point human-model gap, MathVerse's finding that removing diagrams HELPS models, DeepSeek-R1's emergent 'aha moment' — these are memorable, tweetable results that capture attention. The quantitative result should be surprising enough to shift the community's beliefs, not just incrementally better than prior SOTA.",
    "**Systematic error taxonomies that give the community actionable targets.** MATH-Vision's 4-category error taxonomy (42% reasoning, 32% vision recognition) and MathVerse's perception/reasoning/knowledge/calculation breakdown both earned praise. These go beyond 'model X got Y%' to telling the field WHERE to focus next."
  ],

  "field_gaps": [
    {
      "gap": "Disentangling visual perception errors from mathematical reasoning errors in evaluation and training",
      "evidence": "MathVista reviewers (2 and 4) flagged this as the primary limitation. MathVerse's entire contribution is built around this gap. MATH-Vision's error taxonomy shows 32% vision recognition errors vs 42% reasoning errors but cannot further decompose their interaction. No existing benchmark provides ground-truth scene descriptions alongside images for controlled ablation.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Process-level evaluation for multimodal reasoning — assessing intermediate steps, not just final answers",
      "evidence": "MathVista's open questions explicitly call for process-level assessment. URSA builds process supervision (DualMath-1.1M) but only for training, not evaluation. MathVerse's CoT scoring (0.7×step + 0.3×answer) is a first step but relies on GPT-4V as judge, creating circularity. No benchmark provides human-annotated step-level correctness labels for multimodal math.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "RL reward design for non-verifiable multimodal reasoning tasks (scientific argumentation, proof verification, open-ended visual analysis)",
      "evidence": "DeepSeek-R1 explicitly acknowledges reward hacking remains unsolved for non-verifiable tasks. URSA's PS-GRPO relies on binary answer correctness. Vision-R1 uses hard binary rewards. ALL current RL approaches in this space depend on having a ground-truth answer — extending to tasks where correctness is graded or subjective (proof elegance, explanation quality, scientific reasoning) is completely open.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Theoretical understanding of when and why reasoning behaviors emerge during RL training",
      "evidence": "DeepSeek-R1 documents the 'aha moment' phenomenologically but provides no mechanistic explanation. Vision-R1 observes that pure RL fails for MLLMs without cold-start data but doesn't explain the phase transition. URSA's drop-moment threshold (ρ=0.3) is empirically tuned with post-hoc theoretical justification. The field has strong empirical results but no predictive theory of reasoning emergence.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Benchmark longevity and resistance to saturation for multimodal math reasoning",
      "evidence": "MathVista was already approaching saturation (InternVL2-Pro at 65.8% vs human 60.3%) within ~18 months. MATH-Vision's open questions ask whether competition-sourced benchmarks will face the same problem. MathVerse's 2,612-problem corpus is static. No benchmark uses procedural generation, adversarial perturbation, or dynamic difficulty adjustment to maintain longevity.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Visual mathematical reasoning beyond high-school geometry — calculus, combinatorics, topology, advanced proofs",
      "evidence": "MathVerse is limited to high-school math. MATH-Vision acknowledges English-only and abstract-image-only limitations. MathVista's taxonomy shows 15 visual context types but most problems are at pre-university level. Competition problems (AMC, AIME) provide some advanced content but cap at undergraduate level. No benchmark tests graduate-level visual mathematical reasoning.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Multimodal reasoning with dynamic, interactive, or multi-image mathematical contexts",
      "evidence": "URSA notes a significant performance gap on DynaMath (dynamic/adversarial benchmarks). All current benchmarks use single static images. Real mathematical reasoning often involves manipulating diagrams, overlaying constructions, comparing multiple figures, or interacting with plots — none of this is captured in current evaluation.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Quality ceiling of synthetic process labels vs. human annotations for multimodal math",
      "evidence": "URSA achieved 87.6% LLM-as-judge consistency but the remaining ~12% noise is uncharacterized. Vision-R1's modality bridging creates 'answer-directed bias' (reviewer XezA). The entire field's training data pipeline relies on LLM-generated CoT with correctness filtering, but nobody has systematically compared synthetic vs. expert-annotated process supervision for multimodal math training.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    }
  ],

  "untried_combinations": [
    {
      "idea_sketch": "MathVerse's 6-version controlled evaluation + URSA's dual-view PRM training: Train a Process Reward Model using MathVerse-style text-vision ablations as training signal. For each problem, the PRM sees the model's reasoning chain alongside different information versions (text-only, vision-only, vision-dominant), learning to detect when reasoning steps rely on textual shortcuts vs. genuine visual understanding. This creates a 'visual grounding PRM' that penalizes text-reliant reasoning during RL.",
      "from_papers": ["MathVerse", "URSA"],
      "why_promising": "MathVerse proved models exploit text shortcuts, and URSA proved PRMs can guide RL training. Combining them creates targeted supervision for the exact failure mode (text-reliance) that MathVerse identified as the field's core problem. No paper has used controlled information ablation as a PRM training signal."
    },
    {
      "idea_sketch": "DeepSeek-R1's emergent reasoning discovery + formal disentanglement benchmark: Design a benchmark with paired (image, ground-truth-scene-graph) inputs and apply pure RL (à la R1-Zero) where the model can optionally query the scene graph. Track whether the model learns to query visual information vs. hallucinate it, creating the first controlled study of visual grounding emergence under RL. Reward = answer correctness + scene-graph-consistency bonus.",
      "from_papers": ["DeepSeek-R1", "MathVista", "MathVerse"],
      "why_promising": "MathVista's top open question is disentangling vision from reasoning errors. DeepSeek-R1 showed emergent behaviors arise from reward structure alone. Combining these with a structured scene representation could reveal whether visual grounding can emerge from RL the way self-reflection emerged in R1-Zero — addressing the theoretical gap about reasoning emergence while solving the disentanglement problem."
    },
    {
      "idea_sketch": "Competition-sourced problems (MATH-Vision) + URSA's MCTS-based process annotation + Vision-R1's PTST: Build a process-supervised training dataset from competition math problems (which are harder and more diverse than current process supervision datasets), using MCTS binary search for error localization and hallucination injection for perceptual errors, then train with PTST-style progressive length curricula. The key novelty is that competition problems' multi-step nature provides richer process supervision signal than the simpler problems in DualMath-1.1M.",
      "from_papers": ["MATH-Vision", "URSA", "Vision-R1"],
      "why_promising": "Current process supervision datasets (DualMath-1.1M) use relatively easy problems where reasoning chains are short. Competition problems naturally require longer chains with more opportunity for error, producing higher-quality process supervision. MATH-Vision's 53-point gap shows these problems are unsolved, and PTST's progressive training is designed for exactly this kind of hard problem where models need to build up reasoning capacity gradually."
    },
    {
      "idea_sketch": "Dynamic/procedural benchmark generation using MathVista's taxonomy + adversarial perturbation: Use the three-dimensional taxonomy (task × reasoning × visual context) as a specification language, then train a problem generator that procedurally creates new visual math problems on-the-fly, with adversarial perturbations (diagram rotations, label swaps, scale changes) that specifically target known model failure modes from MATH-Vision's error taxonomy (32% vision recognition errors).",
      "from_papers": ["MathVista", "MATH-Vision", "MathVerse"],
      "why_promising": "Benchmark saturation is an acknowledged field-wide problem (MathVista saturating within 18 months, MATH-Vision questioning longevity). A procedural generator would create an inexhaustible, difficulty-adjustable benchmark. MathVista's taxonomy provides the structure, MATH-Vision's error taxonomy provides the adversarial targets, and MathVerse's information control framework ensures generated problems genuinely require vision."
    },
    {
      "idea_sketch": "URSA's drop-moment PRM signal + DeepSeek-R1's distillation to small models: Distill not just reasoning traces but also process reward signals from large PRMs to small student models. Train a small (1.5B-3B) model that simultaneously generates reasoning chains AND predicts its own step-quality scores, enabling self-monitoring during inference without an external PRM. The drop-moment signal becomes an internal 'confidence detector' for self-correction.",
      "from_papers": ["URSA", "DeepSeek-R1"],
      "why_promising": "Current PRM-guided inference requires running a separate reward model at each step, which is expensive and scales poorly. DeepSeek-R1 showed distillation preserves reasoning quality; URSA showed drop-moments are a robust signal. Combining them could produce small, self-monitoring models — critical for deployment and for scaling test-time compute without external verifiers."
    },
    {
      "idea_sketch": "Multi-image reasoning with step-by-step visual construction: Instead of single static image + text, present problems where the model must reason over a SEQUENCE of diagram construction steps (e.g., 'First draw triangle ABC, then construct the perpendicular bisector, then...'). Each step adds visual information, requiring the model to maintain a mental model across frames. Combine with MathVerse's information control to vary what's shown visually vs. described textually at each step.",
      "from_papers": ["MathVerse", "MathVista", "URSA"],
      "why_promising": "All current benchmarks use single static images, which is unrealistic for actual mathematical reasoning (proofs involve construction sequences, plots involve parameter variation). This would test dynamic visual-symbolic integration — a capability no current benchmark measures — and could expose new failure modes in how models maintain state across visual steps."
    }
  ],

  "method_building_blocks": [
    {
      "tool": "GRPO (Group Relative Policy Optimization)",
      "what_it_does": "Value-model-free RL algorithm that computes advantages via z-score normalization within groups of sampled outputs for the same input, eliminating the need for a separate value network while maintaining stable policy optimization",
      "used_by": ["DeepSeek-R1", "URSA (PS-GRPO variant)", "Vision-R1"],
      "could_be_applied_to": "RL training for visual theorem provers, where the action space includes both reasoning steps AND diagram manipulation operations (point placement, line drawing, annotation). GRPO's simplicity makes it feasible to add new action types without retraining a value model."
    },
    {
      "tool": "Drop-moment detection from Process Reward Models",
      "what_it_does": "Converts unreliable absolute PRM scores into robust binary signals by detecting significant relative decreases between consecutive reasoning steps, then applies penalties to outcome rewards for rollouts containing drop-moments",
      "used_by": ["URSA"],
      "could_be_applied_to": "Any multimodal RL pipeline where reward models are noisy — e.g., using CLIP-based visual consistency scores as a PRM and detecting drop-moments when the model's reasoning suddenly diverges from visual evidence. Could also be applied to code generation with visual specifications (UI mockups → code)."
    },
    {
      "tool": "Modality Bridging for data synthesis",
      "what_it_does": "Converts visual information to rich text descriptions via a captioning MLLM, then feeds descriptions to a powerful text-only reasoning model to generate high-quality CoT data — bootstrapping multimodal training data without human annotation",
      "used_by": ["Vision-R1"],
      "could_be_applied_to": "Scientific figure understanding (convert figures to structured descriptions → generate scientific reasoning chains), medical image diagnosis (convert scans to textual findings → generate diagnostic reasoning), or engineering diagram analysis (convert schematics to component lists → generate design analysis)."
    },
    {
      "tool": "MCTS-based binary search for first-error localization",
      "what_it_does": "Given an incorrect multi-step solution, uses Monte Carlo Tree Search with binary search to efficiently locate the first erroneous step by evaluating whether the remaining steps can lead to a correct answer — dramatically more efficient than step-by-step human annotation",
      "used_by": ["URSA (Binary Error Locating Engine)"],
      "could_be_applied_to": "Automated debugging of visual reasoning chains — given a wrong answer to a diagram problem, identify exactly which step introduced the visual misinterpretation. Could also be used for curriculum learning: prioritize training on problems where errors occur at early vs. late steps to diagnose perception vs. reasoning failures."
    },
    {
      "tool": "Misinterpretation Insertion Engine",
      "what_it_does": "Takes correct multimodal reasoning solutions and artificially injects perceptual hallucinations (misreading a label, miscounting objects, misinterpreting a symbol) to create negative examples for process supervision training",
      "used_by": ["URSA"],
      "could_be_applied_to": "Training visual grounding detectors — the injected hallucinations create contrastive pairs (correct perception vs. hallucination) that could train a lightweight 'visual consistency checker' module, applicable to any MLLM pipeline beyond math (document understanding, chart analysis, medical imaging)."
    },
    {
      "tool": "DI/IP/EC Information Taxonomy with 6-version controlled transformation",
      "what_it_does": "Classifies multimodal problem information into Descriptive (directly observable), Implicit Properties (perceptually extractable), and Essential Conditions (numeric/algebraic), then creates 6 versions of each problem with different text-vision information distributions to precisely measure visual reliance",
      "used_by": ["MathVerse"],
      "could_be_applied_to": "Evaluating visual grounding in ANY multimodal reasoning domain — science diagrams, engineering schematics, medical imaging. Could also be used as a training-time data augmentation strategy: train on the vision-only version to force genuine visual understanding, then fine-tune on mixed versions."
    },
    {
      "tool": "Progressive Thinking Suppression Training (PTST)",
      "what_it_does": "Stages RL training with progressively relaxing generation length constraints (e.g., 4K→8K tokens) and decreasing sample counts per input (16→8), forcing the model to first learn concise correct reasoning before expanding to more elaborate chains",
      "used_by": ["Vision-R1"],
      "could_be_applied_to": "Training visual proof assistants where reasoning chains naturally vary in length — start with simple geometric proofs (short chains) and progressively increase to multi-step construction proofs. Also applicable to any RL-trained model exhibiting the overthinking problem where longer outputs correlate with errors."
    },
    {
      "tool": "Competition problem sourcing as natural quality filter",
      "what_it_does": "Uses real math competition problems (AMC, AIME, Math Kangaroo, etc.) as benchmark data, leveraging the competition design process as an implicit quality control mechanism that ensures problems require genuine reasoning, have verified answers, and span calibrated difficulty levels",
      "used_by": ["MATH-Vision"],
      "could_be_applied_to": "Constructing training sets (not just benchmarks) for visual math reasoning — competition problems with diagrams could serve as high-quality seeds for synthetic data expansion via problem perturbation (change numbers, rotate diagrams, swap geometric configurations) while preserving the competition-grade reasoning requirements."
    },
    {
      "tool": "Dual-split evaluation design with leaderboard infrastructure",
      "what_it_does": "Provides a small public development split (1K examples) for fast iteration and a large private test split (5K+ examples) with held-out labels for fair comparison, combined with a persistent leaderboard",
      "used_by": ["MathVista"],
      "could_be_applied_to": "Any new benchmark in this space should adopt this pattern — the public testmini enables rapid development while the private test prevents overfitting. Could be enhanced with periodic refresh of the private set using procedural generation."
    },
    {
      "tool": "Rule-based reward design (accuracy + format)",
      "what_it_does": "Uses simple binary rewards (answer correct AND format correct = 1, else 0) without neural reward models, avoiding reward hacking while providing sufficient signal for RL to discover reasoning strategies",
      "used_by": ["DeepSeek-R1", "Vision-R1"],
      "could_be_applied_to": "Geometry proof verification (a proof either proves the theorem or doesn't), algebraic equation solving from visual input (the answer is either correct or not), and chart-based calculation (the extracted number either matches or doesn't). The simplicity is the feature — complex reward models are shown to introduce more problems than they solve."
    }
  ],

  "common_pitfalls": [
    "**Building 'visual math' benchmarks that don't actually require vision.** MathVerse demonstrated that most MLLMs perform the same or BETTER without diagrams on existing benchmarks. Any new benchmark MUST include a 'no-image' ablation baseline, and any new method MUST report performance with and without visual input. Failing to do this invites immediate reviewer rejection (MathVerse Reviewers, MATH-Vision Reviewer 3 'ZxmA').",
    "**Using absolute PRM scores as RL rewards.** URSA showed that naive scalar PRM rewards cause reward hacking and length bias during online RL training. Use relative signals (drop-moments) or binary penalties instead. This is a known failure mode that reviewers will flag if your method depends on absolute process scores.",
    "**Claiming 'visual reasoning' improvement when the gain comes from a better LLM backbone.** MATH-Vision's error taxonomy shows 42% of errors are pure reasoning failures independent of vision. Any architecture paper must ablate the vision component independently of the language backbone — otherwise reviewers will argue the improvement came from the LLM side. Vision-R1's reviewer XezA raised exactly this concern about answer-directed bias in modality bridging.",
    "**Proposing a single-trick method for a multi-bottleneck problem.** URSA's acceptance hinged on addressing ALL THREE bottlenecks (data, labeling, RL reward) rather than just one. Vision-R1 similarly addressed both data synthesis and the overthinking problem. Papers that tackle only one aspect of the multimodal math reasoning pipeline get the 'limited novelty / just engineering' criticism (URSA Reviewer 4akc, Vision-R1 initial scores of 4/4/4).",
    "**Ignoring the overthinking/token-efficiency problem.** DeepSeek-R1 and Vision-R1 both document that RL-trained reasoning models generate excessively long outputs on simple problems, wasting compute and sometimes degrading accuracy. Any RL-based approach should include a length analysis and ideally a curriculum or constraint mechanism. Reviewers are increasingly aware of this issue.",
    "**Relying on GPT-4V as both subject and judge.** MathVerse's CoT evaluation pipeline uses GPT-4V to score model outputs, creating circularity when evaluating GPT-4V itself. Any evaluation protocol should either use open-source judges or provide human-annotation baselines for calibration. This was flagged as a limitation by the MathVerse authors and is a known vulnerability.",
    "**Insufficient contamination analysis for competition-sourced problems.** MATH-Vision Reviewer 3 raised data contamination as a concern. Competition problems are widely available online and likely in pre-training data. Any benchmark using competition problems MUST include n-gram overlap analysis (at multiple n values), and ideally test on recently published competitions not in any training corpus.",
    "**Omitting confidence intervals and statistical significance.** URSA Reviewer E38C specifically requested confidence intervals, and the authors had to provide ±0.1-0.5% ranges in rebuttal. Report standard deviations across multiple runs for RL-trained models (which have high variance) from the start — adding them in rebuttal is seen as an afterthought.",
    "**Treating CoT as a universal improvement.** MATH-Vision found that chain-of-thought prompting HURT Gemini Pro (-3.32%) and Qwen-VL-Max (-2.96%) on visual math. CoT may amplify visual misinterpretation by giving the model more steps to diverge from the correct visual grounding. Always compare CoT vs. direct-answer baselines.",
    "**Copyright and licensing negligence for benchmark data.** MATH-Vision's weakest rebuttal point was the MAA licensing response ('did not receive negative feedback from board members'). Any benchmark using competition or copyrighted problems must secure explicit licensing. Reviewers and ethics committees increasingly scrutinize this — MATH-Vision Reviewer 3 raised it as a primary concern."
  ],

  "field_trajectory": "The field of multi-modal mathematical reasoning is converging on three macro-directions that will define the next 2-3 years of research.\n\n**First, RL-driven reasoning emergence in multimodal settings is the central technical frontier.** DeepSeek-R1 proved that RL can unlock reasoning behaviors never explicitly taught, and Vision-R1/URSA showed the first successful transfers to multimodal models — but with significant caveats (need for cold-start data, reward hacking, overthinking). The next wave will focus on making RL work more reliably for visual reasoning: better reward functions that capture visual grounding (not just answer correctness), process supervision that distinguishes perceptual errors from logical errors, and theoretical understanding of when reasoning emerges. Expect GRPO variants with vision-specific rewards to become standard.\n\n**Second, the evaluation paradigm is shifting from static benchmarks to dynamic, disentangled, process-level assessment.** MathVista saturated within 18 months. MathVerse showed existing benchmarks don't test vision. MATH-Vision showed they don't test hard math. The next-generation benchmark will be procedurally generated (solving longevity), provide ground-truth scene graphs alongside images (enabling disentanglement), and evaluate intermediate reasoning steps (not just final answers). The DI/IP/EC information control framework from MathVerse will likely be extended into a general-purpose evaluation methodology for any multimodal reasoning task.\n\n**Third, the field is moving toward explicit visual-symbolic-textual decomposition architectures.** Current MLLMs treat everything as token-in/token-out, but the consistent finding across all papers is that the vision-to-symbol interface is the primary bottleneck (32% vision recognition errors in MATH-Vision, models not using images in MathVerse). Future architectures will likely have explicit modules for visual parsing (extracting geometric primitives, reading chart values), symbolic representation (maintaining formal mathematical objects), and textual reasoning (proving theorems, solving equations) — with learned interfaces between them rather than end-to-end token prediction. URSA's dual-view supervision (logical validity + perceptual consistency) is an early signal of this decomposition trend.",

  "meta_advice": "If you are a PhD student aiming to write a strong 2026 paper in multi-modal mathematical reasoning, here is what the evidence from accepted papers tells you.\n\n**Start with a forensic negative result, not a new method.** The highest-impact papers in this field (MathVerse oral at ECCV, MathVista oral at ICLR, MATH-Vision at NeurIPS) all began by proving something the field believed was WRONG — that benchmarks actually test vision, that models are approaching human performance, that SFT is necessary for reasoning. Find a specific, testable assumption in the current paradigm and design a clean experiment to falsify it. This creates the motivation that makes your subsequent contribution feel urgent rather than incremental.\n\n**Target the vision-symbol interface specifically.** Every error analysis in this field points to the same bottleneck: translating visual information into symbolic mathematical objects. This is where the 32% vision recognition errors live (MATH-Vision), where models fail when text cues are removed (MathVerse), and where naive RL cannot self-discover solutions (Vision-R1-Zero at 50.7%). A paper that makes measurable progress on this specific interface — with a mechanism, not just more data — will be impactful.\n\n**Combine building blocks from different papers rather than inventing everything from scratch.** The most successful NeurIPS/ICLR papers in this space are 'principled combinations' (URSA combined PRMs + GRPO + dual-view supervision; Vision-R1 combined modality bridging + PTST + GRPO). The building blocks — GRPO, MCTS error localization, drop-moment detection, DI/IP/EC taxonomy, modality bridging — are all publicly available. Your novelty should be in the *combination* and in the *insight* about WHY the combination works, not in inventing a new algorithm from scratch. Reviewers will accept a paper with known components if you demonstrate a non-obvious interaction effect.\n\n**Pre-empt the 'engineering vs. novelty' critique.** This was the central debate in URSA's review (4akc: 'limited algorithmic novelty') and Vision-R1's borderline scores. Defend against it by: (1) including a clear negative result showing the naive combination fails, (2) providing an ablation showing each component's marginal contribution, (3) framing your insight at the level of a transferable principle (e.g., 'relative signals are more robust than absolute scores' from URSA), not just a pipeline description.\n\n**Release datasets and code.** In a field where reproducibility is challenging and compute is expensive, public artifacts are a powerful signal of lasting contribution. URSA's two datasets, Vision-R1's 200K CoT samples, and MathVista's leaderboard infrastructure all earned explicit reviewer praise and contributed to acceptance decisions. If your paper is borderline, released resources can tip the balance.\n\n**Finally, don't work on saturated problems.** MathVista is nearly saturated. Basic geometry diagram QA is well-explored. Instead, target: (1) dynamic/interactive visual math, (2) process-level evaluation, (3) non-verifiable multimodal reasoning rewards, (4) theoretical foundations for reasoning emergence, or (5) explicit visual-symbolic decomposition architectures. These are the gaps every paper in this review identifies but nobody has solved."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76a3681b-6d8b-4b6e-917e-c7861dd93490",
  "isSidechain": false,
  "requestId": "req_011CbTPM1TVQtYirypttVps3",
  "type": "assistant",
  "uuid": "b46f5547-3b29-42b8-a1ac-21c176d787fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cNJfj3ekspL43bEH2QWUF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11817,
      "cache_read_input_tokens": 10620,
      "output_tokens": 9184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 9184,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 11817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11817
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-27 (UTC).**  ## Research area: Multi-Modal Mathematical Reasoning —…",
  "leafUuid": "b46f5547-3b29-42b8-a1ac-21c176d787fc",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize multimodal math reasoning literature into strategy guide",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-27 (UTC).**  ## Research area: Multi-Modal Mathematical Reasoning —…",
  "leafUuid": "b46f5547-3b29-42b8-a1ac-21c176d787fc",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize multimodal math reasoning literature into strategy guide",
  "sessionId": "e2ff682e-1fce-46ae-a817-147e98b79cfa"
}
```

---
