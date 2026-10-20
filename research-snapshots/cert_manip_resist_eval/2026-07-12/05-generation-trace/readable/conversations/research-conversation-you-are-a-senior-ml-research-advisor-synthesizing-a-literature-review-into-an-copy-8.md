# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/ddb62a84-afb8-42fd-9324-ff5753fa364d.jsonl`
- **Structured JSON:** [`2a138e53627f27205064.json`](../../sessions/2a/2a138e53627f27205064.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:16:37.624Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:16:37.624Z",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Research area: Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding\n\n## Paper analyses (18 papers)\n\n[\n  {\n    \"title\": \"MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts\",\n    \"venue\": \"ICLR 2024 (Oral, top 1.2%)\",\n    \"problem_identification\": \"Prior benchmarks for mathematical reasoning (e.g., MATH, GSM8K) were text-only, while visual QA benchmarks (e.g., VQAv2) tested perception but not mathematical depth. The authors identified that the intersection — mathematical reasoning requiring visual understanding — was fragmented across 28+ small, siloed datasets with no unified evaluation framework. They found this gap by systematically cataloguing existing benchmarks and noticing that no single benchmark tested the compositional skill of interpreting visual information AND performing multi-step mathematical reasoning over it.\",\n    \"key_insight\": \"Rather than building yet another dataset from scratch, the authors realized that the field's fragmentation itself was the problem. The key insight was that a well-designed meta-benchmark — one that unifies existing scattered datasets under a principled taxonomy (5 task types × 7 reasoning types × 15+ visual contexts) and fills specific gaps with targeted new datasets — could catalyze an entire subfield more effectively than any single novel dataset could. The benchmark IS the contribution, not just the vehicle for one.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"MathVista consolidates 28 existing multimodal datasets and introduces 3 new ones (IQTest for pattern/logical reasoning, FunctionQA for algebraic function plot interpretation, PaperQA for scientific figure understanding) into a 6,141-example benchmark. The design is organized along three orthogonal axes: task type (FQA, GPS, MWP, TQA, VQA), mathematical reasoning type (algebraic, arithmetic, geometric, logical, numeric, scientific, statistical), and visual context (geometry diagrams, charts, natural images, function plots, etc.). They developed a 3-stage evaluation protocol: response generation → GPT-4-based answer extraction (>99.5% accuracy, replacing brittle template matching) → normalized scoring. A carefully sampled 1,000-example testmini subset (KL divergence 0.008 from the full set) enables rapid development, while the 5,141-example test set has withheld labels to prevent contamination. They evaluated 12 foundation models across multiple prompting strategies (zero-shot, few-shot, CoT, PoT) plus augmented LLM pipelines using captions and OCR.\",\n    \"what_makes_it_good\": \"Three factors earned this an oral: (1) impeccable timing — it landed precisely as GPT-4V launched and the field desperately needed a way to measure multimodal math reasoning, becoming instantly foundational; (2) thoroughness that built trust — 116 pages, 120 figures, 67 pages of GPT-4V analysis added during revision, rigorous quality controls (Fleiss Kappa 0.775, 99.2% inter-annotator agreement), and a principled taxonomy that organized a messy landscape; (3) actionable findings that shaped future work — the specific revelation that GPT-4V excels at algebraic/scientific reasoning but catastrophically fails at logical reasoning (21.6%) and numeric common sense (20.1%) gave the community precise targets. The benchmark didn't just measure; it diagnosed.\",\n    \"limitations_acknowledged\": \"The authors identified gaps in dataset coverage for certain problem types and visual contexts, the labor-intensive nature of data collection limiting scalability, annotation heterogeneity from consolidating diverse sources (85.6% have annotations but in inconsistent formats), and the inability to disentangle visual perception errors from mathematical reasoning errors within the benchmark's design.\",\n    \"open_questions\": [\n      \"How can we disentangle visual perception failures from mathematical reasoning failures? MathVista conflates these skills — a model might correctly parse a chart but fail at arithmetic, or vice versa, and the benchmark cannot distinguish these failure modes (a concern raised by multiple reviewers that was acknowledged but not resolved).\",\n      \"Why is human performance only 60.3%? This surprisingly low ceiling was flagged by reviewers as either a data quality issue or evidence that the tasks require specialized expertise — understanding which interpretation is correct has implications for how we set targets for AI systems on this benchmark.\",\n      \"What training strategies or architectural innovations would specifically address the logical reasoning and numeric common sense gaps (where models scored 21.6% and 20.1% respectively, far below even modest human baselines)? These represent the sharpest failure modes and remain largely unsolved.\"\n    ],\n    \"building_blocks\": [\n      \"Taxonomy framework: 5 task types × 7 math reasoning types × 15+ visual contexts — reusable for organizing any multi-dimensional evaluation\",\n      \"GPT-4-based answer extraction pipeline (>99.5% accuracy) — replacing brittle regex/template matching for flexible evaluation of free-form model outputs\",\n      \"testmini/test split strategy with KL-divergence-validated representative sampling — pattern for creating development subsets of large benchmarks\",\n      \"28 source datasets consolidated (GeoQA, UniGeo, CLEVR-Math, ChartQA, FigureQA, TabMWP, etc.) — curated inventory of multimodal math datasets\",\n      \"3 new datasets (IQTest, FunctionQA, PaperQA) targeting identified taxonomy gaps\",\n      \"Multi-strategy evaluation protocol (zero-shot, few-shot, CoT, PoT, caption-augmented, OCR-augmented)\",\n      \"Chain-of-Thought and Program-of-Thought prompting applied to visual math tasks\",\n      \"Self-verification and self-consistency evaluation methods for multimodal reasoning\"\n    ],\n    \"reviewer_feedback_summary\": \"All four reviewers appreciated the thoroughness, taxonomy design, and comprehensive model evaluation. Three rated 8/8/8 (accept), one rated 5 (marginally below). Key praise: 'well-motivated and relatively novel construction,' 'thorough review of existing work with a proposed taxonomy,' and the sheer scale of evaluation. Primary concerns: (1) inability to disentangle visual understanding from math reasoning (raised by 2 reviewers), (2) surprisingly low 60.3% human accuracy questioned as possible annotation noise, (3) initial absence of GPT-4V results (resolved by adding 67 pages of analysis in revision), and (4) one reviewer felt results were 'completely superseded by GPT-4V' and missing recent citations. The Area Chair overruled the low-scoring reviewer, noting cited missing works were published after the ICLR submission deadline (9/28/23), and that 'the dataset and results are both insightful for future researchers.' The GPT-4V revision was the critical save — it transformed the paper from a benchmark report into a diagnostic analysis.\",\n    \"relevance_to_seed\": \"MathVista is the foundational evaluation infrastructure for our research area. Any work on integrating visual, symbolic, and textual understanding for mathematical reasoning will be measured against it. The key lesson for our research: the paper succeeded not through algorithmic novelty but through systematic gap identification and principled organization of a fragmented landscape — suggesting that our research could similarly benefit from building structured evaluation frameworks that expose specific failure modes (especially the logical reasoning and numeric common sense gaps MathVista identified but left unsolved) rather than only proposing new model architectures.\"\n  },\n  {\n    \"title\": \"Can MLLMs Reason in Multimodality? EMMA: An Enhanced MultiModal ReAsoning Benchmark\",\n    \"venue\": \"ICML 2025 (Oral, top 1%)\",\n    \"problem_identification\": \"The authors identified that existing multimodal benchmarks (MathVista, MMMU, MMMU-Pro) are fundamentally leaky: many 'multimodal' problems can be solved through text-only reasoning or with superficial visual cues (captions suffice). They found this gap by applying a simple but revealing diagnostic — feeding text-only or text+caption versions of benchmark problems to strong LLMs and discovering that a large fraction could be solved without any genuine visual reasoning. This meant the community was overestimating MLLM multimodal reasoning ability by measuring on benchmarks that didn't actually require it.\",\n    \"key_insight\": \"The core insight is the distinction between 'visual perception' and 'visual reasoning': current MLLMs can recognize what's in an image but cannot reason WITH visual content (e.g., mentally simulating 3D rotations, tracing force vectors, predicting electron flow on molecular diagrams). By operationalizing this distinction through a two-stage filtering pipeline that eliminates caption-solvable problems, the authors revealed that the emperor has no clothes — even frontier models like o1 trail human experts by 32 percentage points on genuinely cross-modal tasks.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"EMMA is a 2,788-problem benchmark spanning math, physics, chemistry, and coding, with 64% newly constructed problems. The key methodological innovation is a two-stage filtering pipeline: (1) remove problems solvable from text alone, and (2) generate image captions via GPT-4o and discard any problem where at least one of three strong LLMs (Llama-3-70B, GPT-4o, Qwen2-72B) answers correctly ≥5/10 times using text+captions. This goes beyond MMMU-Pro's filtering by ensuring that even detailed captions cannot substitute for genuine visual reasoning. The benchmark is organized into domain-specific taxonomies (e.g., 3D spatial simulation, 2D transformation, reaction simulation) that map to specific visual reasoning skills. Evaluation includes direct answering, CoT prompting, and three test-time compute scaling strategies (majority voting, Best-of-N, tournament-style selection) with N up to 16.\",\n    \"what_makes_it_good\": \"Three things likely earned the Oral: (1) The filtering methodology is simple yet devastating — it turns an obvious-in-hindsight observation into a rigorous protocol, making the contribution feel both novel and inevitable. (2) The analysis goes far beyond 'models do poorly' — the CoT degradation finding (open-source models get WORSE with CoT on visual tasks) and the error taxonomy (53% visual reasoning errors vs. 30% perceptual) provide actionable architectural insights. (3) The pass@N analysis showing models can reach 81.5% at N=16 but only 50.75% with majority voting reveals the bottleneck is in reasoning selection, not knowledge — a finding that reframes the problem for the field.\",\n    \"limitations_acknowledged\": \"The authors acknowledge significant domain imbalance (physics has only 156 questions), limited scope in chemistry (primarily organic) and coding (only matplotlib/seaborn), and that o1 was only evaluated on EMMA-mini (400 questions) due to API rate limits. They also note the absence of free-form generation tasks beyond multiple-choice.\",\n    \"open_questions\": [\n      \"Why does Chain-of-Thought hurt open-source models on visual reasoning tasks? Is this a training data issue (insufficient multimodal CoT in pretraining), an architectural issue (weak vision-language connector), or something more fundamental about the incompatibility between sequential linguistic reasoning and parallel spatial reasoning?\",\n      \"The pass@N results show models 'know' the answer but can't reliably select it — can we design better reward models or verifiers specifically for multimodal reasoning, and would training on EMMA-style problems improve visual reasoning capability or merely benchmark performance?\",\n      \"Can we build MLLMs with genuine visual simulation capabilities (mental rotation, spatial transformation) rather than trying to verbalize visual reasoning through language? What architectural changes (e.g., visual scratchpads, iterative image generation during reasoning) would enable this?\"\n    ],\n    \"building_blocks\": [\n      \"Two-stage filtering pipeline (text-only + caption-based) for ensuring genuine multimodality\",\n      \"GPT-4o caption generation as a proxy for visual perception ceiling\",\n      \"Multi-model consensus filtering (3 models × 10 attempts threshold)\",\n      \"Tournament-style selection for test-time compute scaling\",\n      \"Domain-specific visual reasoning taxonomy (3D simulation, 2D transformation, path tracing, etc.)\",\n      \"Error decomposition framework (visual reasoning vs. perceptual vs. textual reasoning vs. knowledge gaps)\",\n      \"EMMA-mini balanced subset design (100 per domain) for efficient evaluation\",\n      \"Cross-model reward evaluation (using stronger model as reward model for weaker model's outputs)\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is directly foundational to multi-modal mathematical reasoning research: it provides both the evaluation infrastructure and the diagnostic evidence that current approaches fail at genuine visual-symbolic integration. For our research area, the key takeaway is that the bottleneck is NOT perception or language reasoning in isolation, but the organic integration of visual simulation with symbolic manipulation — any new method we develop must be evaluated against problems that provably require cross-modal reasoning (using EMMA's filtering protocol), and the CoT degradation finding suggests we may need fundamentally different reasoning paradigms (visual scratchpads, iterative diagram manipulation) rather than simply prompting harder.\"\n  },\n  {\n    \"title\": \"MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine\",\n    \"venue\": \"ICLR 2025 (Poster)\",\n    \"problem_identification\": \"The authors performed a systematic diagnostic decomposition of why MLLMs fail at visual math, identifying three distinct bottlenecks: (1) CLIP-style vision encoders trained on natural images cannot encode abstract, monochromatic mathematical diagrams, (2) vision-language alignment trained on natural image-caption pairs produces poor recognition of geometric elements and spatial relationships (even GPT-4V generates low-quality descriptions of simple figures), and (3) incorporating visual diagrams actually *degrades* CoT reasoning quality compared to text-only input. Critically, they recognized that solving all three simultaneously requires large-scale domain-specific data — but manual annotation of visual math with step-by-step solutions is prohibitively expensive, creating a chicken-and-egg problem that prior work never addressed holistically.\",\n    \"key_insight\": \"Mathematical diagrams are fully *constructive* objects — unlike natural images, every element (shape, coordinate, function curve) is generated from known parameters, meaning the ground-truth description and valid problems can be derived programmatically via backward deduction from known conditions through mathematical formulas. This insight transforms the data bottleneck from an annotation problem into a code-generation problem, enabling a fully automatic pipeline that is correct by construction rather than relying on expensive human verification or error-prone GPT annotation.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"MAVIS builds an automatic data engine that generates three diagram types (plane geometry via iterative shape composition, analytic geometry via random coordinate placement, function curves via parameterized equations) entirely through Python rendering. Captions are produced by filling GPT-4-generated templates (GPT-4 used only once for template creation, never during data generation). Math problems are generated via a backward-deduction strategy: randomly select a known condition as the answer target, then systematically deduce backward through applicable mathematical formulas (Pythagorean theorem, area formulas, etc.) to construct premises, with the solution being the reverse of this deduction chain. This yields 558K diagram-caption pairs (MAVIS-Caption) and 834K problems with CoT rationales (MAVIS-Instruct). The training pipeline has four progressive stages: (1) fine-tune CLIP into CLIP-Math via contrastive learning on MAVIS-Caption, (2) align CLIP-Math with an LLM via MLP projection + LoRA on the same captions, (3) instruction-tune on MAVIS-Instruct with minimized textual redundancy to force visual reliance, and (4) DPO using the model's own incorrect outputs (88K filtered samples) as negative examples against ground-truth CoT as positives.\",\n    \"what_makes_it_good\": \"The paper succeeds because it doesn't just propose a model — it solves the *infrastructure* problem that was blocking the entire subfield: the absence of large-scale, high-quality math-visual training data that doesn't require expensive human annotation or unreliable GPT-4V generation. The systematic decomposition into three orthogonal problems (encoding, alignment, reasoning) with a dedicated training stage for each demonstrates methodological rigor that reviewers valued. The result is striking: a 7B model outperforming LLaVA-NeXT-110B (+6.9%) proves the approach isn't just incrementally better — the data and training recipe matter more than raw scale.\",\n    \"limitations_acknowledged\": \"The authors implicitly acknowledge: 3% of generated diagrams have poor aesthetics (mathematically correct but visually unappealing), rule-based rationales occasionally exhibit fluency issues, and the diagram type coverage is limited to plane geometry, analytic geometry, and function curves (e.g., circumscribed circles, solid geometry are missing). Notably, the paper lacks an explicit limitations section — a gap the reviewers did not strongly penalize but that weakens the scholarly completeness.\",\n    \"open_questions\": [\n      \"Can the backward-deduction data engine be extended to more complex mathematical domains (combinatorics, probability, solid geometry, proofs) where the constructive property of diagrams is less straightforward?\",\n      \"Does the rule-based template approach for captions and problems create systematic blind spots or distributional biases that limit generalization to real-world math problems with natural language variation and messier diagrams?\",\n      \"What is the scaling law for synthetic math-visual data — does performance continue to improve monotonically (as the 25%→100% ablation suggests), or does it plateau, and at what point does real-world data diversity become essential?\"\n    ],\n    \"building_blocks\": [\n      \"CLIP contrastive learning fine-tuned for domain-specific vision encoding (CLIP-Math)\",\n      \"Backward-deduction problem generation from known mathematical formulas\",\n      \"Template-based caption generation (GPT-4 for one-time template creation, programmatic filling at scale)\",\n      \"Progressive multi-stage training (encoding → alignment → instruction tuning → DPO)\",\n      \"DPO with self-generated incorrect outputs as negative samples\",\n      \"Minimized textual redundancy in questions to force visual reliance\",\n      \"Python-based procedural diagram generation (plane geometry via iterative shape composition)\",\n      \"LoRA-based fine-tuning with MLP projection layers for vision-language alignment\",\n      \"MAVIS-Caption (558K) and MAVIS-Instruct (834K) as reusable open-source datasets\"\n    ],\n    \"reviewer_feedback_summary\": \"Ratings: 8, 6, 6, 6 (Accept Poster). The strongest reviewer (8/5 confidence) praised the comprehensive investigation spanning data curation, visual encoding, and learning methodology, calling the rule-based data engine a genuinely useful contribution. Key concerns across reviewers: (1) template-based generation may limit diversity (addressed with evidence of 804K/834K unique questions and complementary real-world data), (2) limited to 7B model scale (addressed with 8×7B and LLaVA-NeXT-8B experiments showing +8.4% transfer), (3) limited diagram type coverage (acknowledged but argued current types cover most benchmarks), (4) the work is 'engineering-focused rather than methodologically innovative' — combining CLIP, LLaVA, and DPO without novel architecture (partially addressed by arguing the data engine itself is the methodological contribution). Reviewer_uZLE raised their score from 5→6 after the rebuttal. The AC noted the rebuttal 'effectively resolved major issues leading to consensus acceptance' despite lingering concerns about rule-based engine extensibility.\",\n    \"relevance_to_seed\": \"This paper is directly central to multi-modal mathematical reasoning research. Its key transferable lesson is that the bottleneck in math-visual AI is not model architecture but *data infrastructure* — and that mathematical objects' constructive nature enables fully automatic data generation that is correct by construction. Any follow-up work in this area should either build on MAVIS's datasets/pipeline or explain why a different data strategy is needed. The backward-deduction problem generation technique and the insight about minimizing textual redundancy to force genuine visual reasoning are particularly reusable methodological innovations.\"\n  },\n  {\n    \"title\": \"DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"Existing visual math benchmarks (MathVista, MathVerse, MATH-V) are static collections, meaning high scores could reflect pattern memorization rather than genuine reasoning. The authors identified this gap by asking a deceptively simple question: if a model can solve a math problem, can it solve trivial variations of the same problem? They drew on the classical robustness/worst-case analysis tradition from adversarial ML and applied it to a domain (visual math) where nobody had systematically measured it, revealing that VLMs lack the compositional stability humans exhibit on minor problem perturbations.\",\n    \"key_insight\": \"Encoding each benchmark question as a parameterized Python program — rather than a fixed image-text pair — transforms evaluation from a static snapshot into a distribution over problem variants, enabling worst-case vs. average-case analysis that exposes robustness failures invisible to conventional benchmarking. The insight is that the program IS the question, not any single rendering of it.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"The authors curate 501 seed questions across 9 math topics (plane geometry, analytic geometry, statistics, algebra, graph theory, etc.) spanning elementary to undergraduate difficulty. Each seed question is manually encoded as a Python program using Matplotlib/Pyglet that accepts random parameters and outputs both a visual figure and a ground-truth answer. Seven variation types are defined: numerical values, geometric transformations, function types, colors, symbolic substitutions, graph structures, and real-life contexts. At evaluation time, 10 concrete variants are sampled per seed (5,010 total), and models are scored on average-case accuracy (mean across variants), worst-case accuracy (fraction of seeds where ALL 10 variants are correct), and reasoning robustness (worst/average ratio). A repetition consistency metric further disentangles stochastic decoding noise from genuine reasoning failures by checking if models give the same (wrong) answer deterministically.\",\n    \"what_makes_it_good\": \"The paper succeeds because it introduces a clean, falsifiable claim — 'VLMs that appear competent on average are catastrophically fragile on variations' — and backs it with a methodology that makes the gap undeniable (GPT-4o: 63.7% avg → 34.7% worst-case). The programmatic design is both the methodological contribution and the practical gift: it makes the benchmark self-renewing, resistant to contamination, and infinitely extensible. The evaluation is thorough (14 models, human baselines, error taxonomy, memorization analysis), turning a benchmark paper into a diagnostic study.\",\n    \"limitations_acknowledged\": \"The authors acknowledge that encoding problems as programs requires substantial human effort, limiting coverage of highly complex problems and making the difficulty distribution 'relatively limited compared to MATH-V.' They also note the benchmark considers only individual variation types rather than combinations, and the seed question selection introduces dataset bias (e.g., Puzzle Tests are only 3.4% of the dataset despite being the hardest category).\",\n    \"open_questions\": [\n      \"Can the programmatic generation approach be automated using LLMs to write the Python programs themselves, scaling beyond human curation? The authors explicitly flag this as future work, and it represents a meta-benchmark-generation problem.\",\n      \"Do the robustness failures stem from visual perception deficits (figure reading errors account for 33.1% of Claude-3.5's mistakes) or from reasoning fragility? Disentangling these would require ablations where models receive perfect symbolic descriptions instead of images.\",\n      \"Would training on programmatically varied visual math data (i.e., using DynaMath-style generators for data augmentation) close the robustness gap, or is the failure architectural — indicating that current VLM vision encoders fundamentally lack the invariance properties needed for mathematical figure understanding?\"\n    ],\n    \"building_blocks\": [\n      \"Parameterized Python programs as benchmark generators (Matplotlib + Pyglet)\",\n      \"Worst-case vs. average-case accuracy framework for robustness evaluation\",\n      \"Reasoning robustness ratio (RR = worst/avg) as a model-comparison metric\",\n      \"Repetition consistency metric to separate stochastic noise from systematic failures\",\n      \"Seven-category variation taxonomy for visual math problems\",\n      \"Error taxonomy: figure reading, reasoning, calculation, hallucination\",\n      \"Seed question sourcing pipeline (MathVista + MATH-V + MMMU + internet + novel)\",\n      \"STEM student annotation of solution strategies as program prototypes\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is directly central to multi-modal mathematical reasoning: it provides both a diagnostic tool and a conceptual framework for understanding WHERE integration of visual, symbolic, and textual understanding breaks down in current models. Its key lesson for our research area is that robustness — not just accuracy — should be the primary evaluation axis, and that programmatic generation of visual-mathematical stimuli is a powerful methodology for stress-testing multi-modal reasoning that we should adopt or extend in our own benchmark/evaluation designs.\"\n  },\n  {\n    \"title\": \"MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?\",\n    \"venue\": \"ECCV 2024\",\n    \"problem_identification\": \"The authors identified that existing visual math benchmarks (MathVista, GeoQA, MMMU) embed redundant textual descriptions that duplicate information already present in diagrams — enabling MLLMs to 'cheat' by deriving answers from text alone without genuinely interpreting visual input. They discovered this by running a simple but devastating pilot ablation on 120 problems: removing diagrams entirely and observing that most MLLMs actually scored *higher* without visual input (e.g., Qwen-VL-Max +5.1%, InternLM-XComposer2 +5.6%). This revealed that the field's evaluation methodology was fundamentally compromised — benchmarks were measuring text comprehension, not visual reasoning.\",\n    \"key_insight\": \"By decomposing the textual content of math problems into three semantic categories (Descriptive Information, Implicit Properties, Essential Conditions) and systematically ablating them across six problem versions, you can create a controlled experimental framework that precisely isolates *what* visual capabilities a model possesses versus what it fakes via textual shortcuts. The insight is that information-theoretic decomposition of the text-vision redundancy — not just removing images — is the right lens for diagnosing multimodal understanding.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"MathVerse collects 2,612 high-quality math problems with diagrams spanning plane geometry, solid geometry, and functions. Each problem's textual content is taxonomized into three categories: Descriptive Information (DI — directly observable diagram content like shape names), Implicit Properties (IP — spatial relationships like parallelism requiring perception but not domain knowledge), and Essential Conditions (EC — precise numerical measurements that cannot be inferred visually). Human annotators then create six versions of each problem by progressively migrating information from text into the diagram: Text-dominant (all text + diagram), Text-lite (remove DI), Text-only (remove diagram entirely), Vision-intensive (remove IP), Vision-dominant (move EC into diagram), and Vision-only (everything rendered visually). This yields 15,672 test samples. Additionally, a two-phase Chain-of-Thought evaluation strategy uses GPT-4 to extract key reasoning steps from model outputs (deliberately without access to ground truth, to avoid bias), then GPT-4V scores each step with error categorization, producing a weighted score: Score = 0.7 × (mean step accuracy) + 0.3 × (final answer accuracy).\",\n    \"what_makes_it_good\": \"Three qualities made this paper stand out. First, the core idea is elegantly simple yet profoundly revealing — the information-level ablation is easy to understand but exposes a systemic blind spot across the entire MLLM evaluation ecosystem. Second, the experimental findings are genuinely surprising and newsworthy: state-of-the-art models performing *better* without visual input is a striking result that demands attention. Third, the methodology is rigorous and generalizable — the DI/IP/EC taxonomy and six-version framework provide a reusable template for probing multimodal understanding in any domain, not just math.\",\n    \"limitations_acknowledged\": \"The authors identify five limitations: restriction to high-school level mathematics, exclusion of multi-diagram problems, reliance on GPT-4(V) for CoT evaluation introducing potential model-specific biases, a small human baseline (only 10 college students), and focus on pure mathematical reasoning rather than real-world application contexts.\",\n    \"open_questions\": [\n      \"Can the DI/IP/EC information decomposition framework be generalized to non-mathematical multimodal tasks (e.g., scientific diagrams, engineering drawings, medical imaging) to similarly expose visual comprehension failures?\",\n      \"The paper reveals that current vision encoders are fundamentally inadequate for mathematical diagrams — what architectural changes (e.g., symbolic parsing heads, geometry-aware pretraining, OCR-integrated encoders) would most effectively close this gap?\",\n      \"The CoT evaluation relies on GPT-4(V) as judge, creating a circular dependency for evaluating future models that surpass GPT-4V — what evaluation methodology would remain valid as frontier models improve?\"\n    ],\n    \"building_blocks\": [\n      \"DI/IP/EC information taxonomy for multimodal text-vision decomposition\",\n      \"Six-level visual ablation framework (Text-dominant → Vision-only)\",\n      \"Two-phase CoT evaluation: blind step extraction + grounded step scoring\",\n      \"GPT-4(V)-as-judge with weighted step-level scoring formula\",\n      \"Curated dataset from GeoQA (750), GEOS (119), Geometry3K (507), plus 1,236 newly collected problems\",\n      \"Error taxonomy: Visual Perception / Reasoning / Knowledge / Calculation errors\",\n      \"Testmini subset sampling strategy (788 problems / 4,728 samples) for efficient evaluation\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is directly foundational to multi-modal mathematical reasoning research: it provides both the diagnostic framework (visual ablation) and the empirical evidence that current MLLMs fundamentally fail at integrating visual understanding with symbolic/textual reasoning. For our research area, the key lesson is methodological — any new approach to multi-modal math reasoning MUST be evaluated under information-controlled conditions (not just end-to-end accuracy), and the DI/IP/EC decomposition offers a ready-made framework for designing such evaluations. The paper also reveals the most critical bottleneck: vision encoders that can parse mathematical diagrams into structured symbolic representations.\"\n  },\n  {\n    \"title\": \"Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset\",\n    \"venue\": \"NeurIPS 2024 (Datasets & Benchmarks Track)\",\n    \"problem_identification\": \"The authors identified that existing multimodal math benchmarks (MathVista, MMMU) suffered from three specific deficiencies: narrow subject coverage (7 categories vs. needed 16), short/template-like questions (avg 15.6 words in MathVista vs. 42.3 in MATH-V), and coarse or incomplete difficulty grading (37.7% of MathVista problems had no difficulty label). They found this gap by doing a systematic comparative audit of existing benchmarks along axes of diversity, granularity, and authenticity — essentially stress-testing the evaluation tools themselves rather than the models, which is a meta-research insight that existing 'human-level' claims on MathVista were artifacts of benchmark weakness, not model strength.\",\n    \"key_insight\": \"Rather than constructing synthetic problems or post-hoc annotating existing images, the authors realized that real math competition problems are a naturally curated source that simultaneously provides visual grounding, calibrated difficulty (via competition grade levels), and taxonomic diversity (competitions span many subfields) — turning the curation problem from 'design good problems' into 'carefully filter and organize existing ones.' This reframing dramatically lowered the cost of creating a high-quality benchmark while increasing its authenticity.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"The authors sourced 3,352 candidate problems from 19 international math competitions (Math Kangaroo, AMC 8/10/12, AIME, UKMT Grey/Pink/Junior/Senior) and applied a rigorous 4-stage curation pipeline: (1) text-image alignment verification by 10 cross-validating annotators (filtering to 3,040 problems), (2) duplicate detection via lexical overlap and Levenshtein distance, (3) subject categorization through majority voting across 3 independent annotation groups with GPT-4V/Gemini Pro consultation, and (4) difficulty assignment mapped from competition grade requirements to a 5-level scale. The final dataset spans 16 mathematical disciplines with a balanced mix of 1,532 multiple-choice and 1,508 free-form problems. They evaluated 15+ models (LLMs with captions, open-source LMMs like LLaVA/SPHINX/InternLM, and closed-source LMMs like GPT-4V/Gemini Pro/Qwen-VL) in zero-shot settings with and without chain-of-thought, and conducted a detailed 232-error manual analysis of GPT-4V failures categorized into 6 error types.\",\n    \"what_makes_it_good\": \"Three things elevate this beyond a routine benchmark paper: First, the gap identification is genuinely actionable — they didn't just say 'we need harder problems' but precisely diagnosed WHY existing benchmarks were insufficient (subject coverage, question complexity, difficulty calibration), making the contribution feel necessary rather than incremental. Second, the error taxonomy (reasoning 42.2%, vision recognition 31.9%, knowledge 15.1%, question misunderstanding 6.9%, calculation 1.3%, refusal 2.6%) provides a diagnostic roadmap that future model builders can directly act on. Third, the finding that chain-of-thought HURTS some models (Gemini Pro -3.32%, Qwen-VL-Max -2.96%) while helping others (GPT-4V +1.22%) is a surprising empirical contribution that challenges the dominant assumption that CoT universally helps, giving the paper analytical depth beyond just reporting accuracy numbers.\",\n    \"limitations_acknowledged\": \"The authors explicitly acknowledged three gaps: the dataset is English-only (no multilingual evaluation), covers only mathematics (no physics or chemistry), and uses only abstract competition diagrams rather than real-world photographs — the last of which they later addressed with the MATH-Vision-Wild variant featuring photographic captures under varying conditions.\",\n    \"open_questions\": [\n      \"Why does chain-of-thought prompting degrade performance for some models but improve it for others? This points to fundamental differences in how models process multi-step visual-symbolic reasoning that are not yet understood and could be a rich research direction.\",\n      \"Vision recognition errors account for 31.9% of GPT-4V failures — is the bottleneck in low-level visual parsing (reading diagram labels, identifying geometric shapes) or in higher-level spatial reasoning (understanding relative positions, inferring 3D from 2D)? Disentangling these would guide whether to improve vision encoders vs. reasoning modules.\",\n      \"The massive gap between human (75.66%) and best model (22.76% at time of publication) suggests that competition math requires reasoning capabilities qualitatively different from what current LMMs possess — what specific cognitive operations (spatial manipulation, multi-step deduction, analogy) are models most lacking, and can these be taught through targeted training rather than scale alone?\"\n    ],\n    \"building_blocks\": [\n      \"Math competition problem databases (Math Kangaroo, AMC/AIME, UKMT) as authentic curated sources for benchmark construction\",\n      \"4-stage curation pipeline (alignment verification → duplicate detection → subject categorization → difficulty assignment) as a reusable template for benchmark building\",\n      \"Hybrid human-AI annotation with majority voting (3 independent groups + LMM consultation for subject categorization)\",\n      \"6-category error taxonomy for multimodal reasoning (reasoning, vision recognition, knowledge, question misunderstanding, calculation, refusal)\",\n      \"Levenshtein distance + lexical overlap for duplicate detection in math problem corpora\",\n      \"Competition grade-level to difficulty-level mapping as a principled approach to calibrating problem difficulty\",\n      \"Zero-shot evaluation with and without CoT as a diagnostic methodology for probing reasoning depth\",\n      \"MATH-Vision-Wild variant methodology — re-photographing problems under real-world conditions to test robustness\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is directly foundational to multi-modal mathematical reasoning research: it provides the most comprehensive diagnostic benchmark for evaluating how well models integrate visual understanding (diagram parsing), symbolic reasoning (algebraic manipulation), and textual comprehension (problem statement interpretation). For our research area, the key takeaway is methodological — the error taxonomy reveals that the bottleneck is roughly evenly split between vision failures (31.9%) and reasoning failures (42.2%), suggesting that advances in multi-modal math reasoning require jointly improving both perception and inference rather than focusing on either alone. The 16-subject taxonomy also reveals which mathematical domains (topology, graph theory, solid geometry) remain hardest, providing a prioritization map for future work.\"\n  },\n  {\n    \"title\": \"URSA: Understanding and Verifying Chain-of-thought Reasoning in Multimodal Mathematics\",\n    \"venue\": \"NeurIPS 2025 (Main Track)\",\n    \"problem_identification\": \"The authors identified that Process Reward Models (PRMs) — already proven for text-only math reasoning via test-time scaling — had never been integrated into multimodal mathematical reasoning. They traced this gap to three compounding bottlenecks: (1) insufficient high-quality multimodal CoT data to build a strong enough foundation model, (2) no automated method for process-level labeling that accounts f\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:16:37.627Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:16:37.627Z",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-28T05:16:37.639Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-28 (UTC).**

## Research area: Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding

## Paper analyses (18 papers)

[
  {
    "title": "MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts",
    "venue": "ICLR 2024 (Oral, top 1.2%)",
    "problem_identification": "Prior benchmarks for mathematical reasoning (e.g., MATH, GSM8K) were text-only, while visual QA benchmarks (e.g., VQAv2) tested perception but not mathematical depth. The authors identified that the intersection — mathematical reasoning requiring visual understanding — was fragmented across 28+ small, siloed datasets with no unified evaluation framework. They found this gap by systematically cataloguing existing benchmarks and noticing that no single benchmark tested the compositional skill of interpreting visual information AND performing multi-step mathematical reasoning over it.",
    "key_insight": "Rather than building yet another dataset from scratch, the authors realized that the field's fragmentation itself was the problem. The key insight was that a well-designed meta-benchmark — one that unifies existing scattered datasets under a principled taxonomy (5 task types × 7 reasoning types × 15+ visual contexts) and fills specific gaps with targeted new datasets — could catalyze an entire subfield more effectively than any single novel dataset could. The benchmark IS the contribution, not just the vehicle for one.",
    "innovation_type": "new_benchmark",
    "method_summary": "MathVista consolidates 28 existing multimodal datasets and introduces 3 new ones (IQTest for pattern/logical reasoning, FunctionQA for algebraic function plot interpretation, PaperQA for scientific figure understanding) into a 6,141-example benchmark. The design is organized along three orthogonal axes: task type (FQA, GPS, MWP, TQA, VQA), mathematical reasoning type (algebraic, arithmetic, geometric, logical, numeric, scientific, statistical), and visual context (geometry diagrams, charts, natural images, function plots, etc.). They developed a 3-stage evaluation protocol: response generation → GPT-4-based answer extraction (>99.5% accuracy, replacing brittle template matching) → normalized scoring. A carefully sampled 1,000-example testmini subset (KL divergence 0.008 from the full set) enables rapid development, while the 5,141-example test set has withheld labels to prevent contamination. They evaluated 12 foundation models across multiple prompting strategies (zero-shot, few-shot, CoT, PoT) plus augmented LLM pipelines using captions and OCR.",
    "what_makes_it_good": "Three factors earned this an oral: (1) impeccable timing — it landed precisely as GPT-4V launched and the field desperately needed a way to measure multimodal math reasoning, becoming instantly foundational; (2) thoroughness that built trust — 116 pages, 120 figures, 67 pages of GPT-4V analysis added during revision, rigorous quality controls (Fleiss Kappa 0.775, 99.2% inter-annotator agreement), and a principled taxonomy that organized a messy landscape; (3) actionable findings that shaped future work — the specific revelation that GPT-4V excels at algebraic/scientific reasoning but catastrophically fails at logical reasoning (21.6%) and numeric common sense (20.1%) gave the community precise targets. The benchmark didn't just measure; it diagnosed.",
    "limitations_acknowledged": "The authors identified gaps in dataset coverage for certain problem types and visual contexts, the labor-intensive nature of data collection limiting scalability, annotation heterogeneity from consolidating diverse sources (85.6% have annotations but in inconsistent formats), and the inability to disentangle visual perception errors from mathematical reasoning errors within the benchmark's design.",
    "open_questions": [
      "How can we disentangle visual perception failures from mathematical reasoning failures? MathVista conflates these skills — a model might correctly parse a chart but fail at arithmetic, or vice versa, and the benchmark cannot distinguish these failure modes (a concern raised by multiple reviewers that was acknowledged but not resolved).",
      "Why is human performance only 60.3%? This surprisingly low ceiling was flagged by reviewers as either a data quality issue or evidence that the tasks require specialized expertise — understanding which interpretation is correct has implications for how we set targets for AI systems on this benchmark.",
      "What training strategies or architectural innovations would specifically address the logical reasoning and numeric common sense gaps (where models scored 21.6% and 20.1% respectively, far below even modest human baselines)? These represent the sharpest failure modes and remain largely unsolved."
    ],
    "building_blocks": [
      "Taxonomy framework: 5 task types × 7 math reasoning types × 15+ visual contexts — reusable for organizing any multi-dimensional evaluation",
      "GPT-4-based answer extraction pipeline (>99.5% accuracy) — replacing brittle regex/template matching for flexible evaluation of free-form model outputs",
      "testmini/test split strategy with KL-divergence-validated representative sampling — pattern for creating development subsets of large benchmarks",
      "28 source datasets consolidated (GeoQA, UniGeo, CLEVR-Math, ChartQA, FigureQA, TabMWP, etc.) — curated inventory of multimodal math datasets",
      "3 new datasets (IQTest, FunctionQA, PaperQA) targeting identified taxonomy gaps",
      "Multi-strategy evaluation protocol (zero-shot, few-shot, CoT, PoT, caption-augmented, OCR-augmented)",
      "Chain-of-Thought and Program-of-Thought prompting applied to visual math tasks",
      "Self-verification and self-consistency evaluation methods for multimodal reasoning"
    ],
    "reviewer_feedback_summary": "All four reviewers appreciated the thoroughness, taxonomy design, and comprehensive model evaluation. Three rated 8/8/8 (accept), one rated 5 (marginally below). Key praise: 'well-motivated and relatively novel construction,' 'thorough review of existing work with a proposed taxonomy,' and the sheer scale of evaluation. Primary concerns: (1) inability to disentangle visual understanding from math reasoning (raised by 2 reviewers), (2) surprisingly low 60.3% human accuracy questioned as possible annotation noise, (3) initial absence of GPT-4V results (resolved by adding 67 pages of analysis in revision), and (4) one reviewer felt results were 'completely superseded by GPT-4V' and missing recent citations. The Area Chair overruled the low-scoring reviewer, noting cited missing works were published after the ICLR submission deadline (9/28/23), and that 'the dataset and results are both insightful for future researchers.' The GPT-4V revision was the critical save — it transformed the paper from a benchmark report into a diagnostic analysis.",
    "relevance_to_seed": "MathVista is the foundational evaluation infrastructure for our research area. Any work on integrating visual, symbolic, and textual understanding for mathematical reasoning will be measured against it. The key lesson for our research: the paper succeeded not through algorithmic novelty but through systematic gap identification and principled organization of a fragmented landscape — suggesting that our research could similarly benefit from building structured evaluation frameworks that expose specific failure modes (especially the logical reasoning and numeric common sense gaps MathVista identified but left unsolved) rather than only proposing new model architectures."
  },
  {
    "title": "Can MLLMs Reason in Multimodality? EMMA: An Enhanced MultiModal ReAsoning Benchmark",
    "venue": "ICML 2025 (Oral, top 1%)",
    "problem_identification": "The authors identified that existing multimodal benchmarks (MathVista, MMMU, MMMU-Pro) are fundamentally leaky: many 'multimodal' problems can be solved through text-only reasoning or with superficial visual cues (captions suffice). They found this gap by applying a simple but revealing diagnostic — feeding text-only or text+caption versions of benchmark problems to strong LLMs and discovering that a large fraction could be solved without any genuine visual reasoning. This meant the community was overestimating MLLM multimodal reasoning ability by measuring on benchmarks that didn't actually require it.",
    "key_insight": "The core insight is the distinction between 'visual perception' and 'visual reasoning': current MLLMs can recognize what's in an image but cannot reason WITH visual content (e.g., mentally simulating 3D rotations, tracing force vectors, predicting electron flow on molecular diagrams). By operationalizing this distinction through a two-stage filtering pipeline that eliminates caption-solvable problems, the authors revealed that the emperor has no clothes — even frontier models like o1 trail human experts by 32 percentage points on genuinely cross-modal tasks.",
    "innovation_type": "new_benchmark",
    "method_summary": "EMMA is a 2,788-problem benchmark spanning math, physics, chemistry, and coding, with 64% newly constructed problems. The key methodological innovation is a two-stage filtering pipeline: (1) remove problems solvable from text alone, and (2) generate image captions via GPT-4o and discard any problem where at least one of three strong LLMs (Llama-3-70B, GPT-4o, Qwen2-72B) answers correctly ≥5/10 times using text+captions. This goes beyond MMMU-Pro's filtering by ensuring that even detailed captions cannot substitute for genuine visual reasoning. The benchmark is organized into domain-specific taxonomies (e.g., 3D spatial simulation, 2D transformation, reaction simulation) that map to specific visual reasoning skills. Evaluation includes direct answering, CoT prompting, and three test-time compute scaling strategies (majority voting, Best-of-N, tournament-style selection) with N up to 16.",
    "what_makes_it_good": "Three things likely earned the Oral: (1) The filtering methodology is simple yet devastating — it turns an obvious-in-hindsight observation into a rigorous protocol, making the contribution feel both novel and inevitable. (2) The analysis goes far beyond 'models do poorly' — the CoT degradation finding (open-source models get WORSE with CoT on visual tasks) and the error taxonomy (53% visual reasoning errors vs. 30% perceptual) provide actionable architectural insights. (3) The pass@N analysis showing models can reach 81.5% at N=16 but only 50.75% with majority voting reveals the bottleneck is in reasoning selection, not knowledge — a finding that reframes the problem for the field.",
    "limitations_acknowledged": "The authors acknowledge significant domain imbalance (physics has only 156 questions), limited scope in chemistry (primarily organic) and coding (only matplotlib/seaborn), and that o1 was only evaluated on EMMA-mini (400 questions) due to API rate limits. They also note the absence of free-form generation tasks beyond multiple-choice.",
    "open_questions": [
      "Why does Chain-of-Thought hurt open-source models on visual reasoning tasks? Is this a training data issue (insufficient multimodal CoT in pretraining), an architectural issue (weak vision-language connector), or something more fundamental about the incompatibility between sequential linguistic reasoning and parallel spatial reasoning?",
      "The pass@N results show models 'know' the answer but can't reliably select it — can we design better reward models or verifiers specifically for multimodal reasoning, and would training on EMMA-style problems improve visual reasoning capability or merely benchmark performance?",
      "Can we build MLLMs with genuine visual simulation capabilities (mental rotation, spatial transformation) rather than trying to verbalize visual reasoning through language? What architectural changes (e.g., visual scratchpads, iterative image generation during reasoning) would enable this?"
    ],
    "building_blocks": [
      "Two-stage filtering pipeline (text-only + caption-based) for ensuring genuine multimodality",
      "GPT-4o caption generation as a proxy for visual perception ceiling",
      "Multi-model consensus filtering (3 models × 10 attempts threshold)",
      "Tournament-style selection for test-time compute scaling",
      "Domain-specific visual reasoning taxonomy (3D simulation, 2D transformation, path tracing, etc.)",
      "Error decomposition framework (visual reasoning vs. perceptual vs. textual reasoning vs. knowledge gaps)",
      "EMMA-mini balanced subset design (100 per domain) for efficient evaluation",
      "Cross-model reward evaluation (using stronger model as reward model for weaker model's outputs)"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is directly foundational to multi-modal mathematical reasoning research: it provides both the evaluation infrastructure and the diagnostic evidence that current approaches fail at genuine visual-symbolic integration. For our research area, the key takeaway is that the bottleneck is NOT perception or language reasoning in isolation, but the organic integration of visual simulation with symbolic manipulation — any new method we develop must be evaluated against problems that provably require cross-modal reasoning (using EMMA's filtering protocol), and the CoT degradation finding suggests we may need fundamentally different reasoning paradigms (visual scratchpads, iterative diagram manipulation) rather than simply prompting harder."
  },
  {
    "title": "MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine",
    "venue": "ICLR 2025 (Poster)",
    "problem_identification": "The authors performed a systematic diagnostic decomposition of why MLLMs fail at visual math, identifying three distinct bottlenecks: (1) CLIP-style vision encoders trained on natural images cannot encode abstract, monochromatic mathematical diagrams, (2) vision-language alignment trained on natural image-caption pairs produces poor recognition of geometric elements and spatial relationships (even GPT-4V generates low-quality descriptions of simple figures), and (3) incorporating visual diagrams actually *degrades* CoT reasoning quality compared to text-only input. Critically, they recognized that solving all three simultaneously requires large-scale domain-specific data — but manual annotation of visual math with step-by-step solutions is prohibitively expensive, creating a chicken-and-egg problem that prior work never addressed holistically.",
    "key_insight": "Mathematical diagrams are fully *constructive* objects — unlike natural images, every element (shape, coordinate, function curve) is generated from known parameters, meaning the ground-truth description and valid problems can be derived programmatically via backward deduction from known conditions through mathematical formulas. This insight transforms the data bottleneck from an annotation problem into a code-generation problem, enabling a fully automatic pipeline that is correct by construction rather than relying on expensive human verification or error-prone GPT annotation.",
    "innovation_type": "combination",
    "method_summary": "MAVIS builds an automatic data engine that generates three diagram types (plane geometry via iterative shape composition, analytic geometry via random coordinate placement, function curves via parameterized equations) entirely through Python rendering. Captions are produced by filling GPT-4-generated templates (GPT-4 used only once for template creation, never during data generation). Math problems are generated via a backward-deduction strategy: randomly select a known condition as the answer target, then systematically deduce backward through applicable mathematical formulas (Pythagorean theorem, area formulas, etc.) to construct premises, with the solution being the reverse of this deduction chain. This yields 558K diagram-caption pairs (MAVIS-Caption) and 834K problems with CoT rationales (MAVIS-Instruct). The training pipeline has four progressive stages: (1) fine-tune CLIP into CLIP-Math via contrastive learning on MAVIS-Caption, (2) align CLIP-Math with an LLM via MLP projection + LoRA on the same captions, (3) instruction-tune on MAVIS-Instruct with minimized textual redundancy to force visual reliance, and (4) DPO using the model's own incorrect outputs (88K filtered samples) as negative examples against ground-truth CoT as positives.",
    "what_makes_it_good": "The paper succeeds because it doesn't just propose a model — it solves the *infrastructure* problem that was blocking the entire subfield: the absence of large-scale, high-quality math-visual training data that doesn't require expensive human annotation or unreliable GPT-4V generation. The systematic decomposition into three orthogonal problems (encoding, alignment, reasoning) with a dedicated training stage for each demonstrates methodological rigor that reviewers valued. The result is striking: a 7B model outperforming LLaVA-NeXT-110B (+6.9%) proves the approach isn't just incrementally better — the data and training recipe matter more than raw scale.",
    "limitations_acknowledged": "The authors implicitly acknowledge: 3% of generated diagrams have poor aesthetics (mathematically correct but visually unappealing), rule-based rationales occasionally exhibit fluency issues, and the diagram type coverage is limited to plane geometry, analytic geometry, and function curves (e.g., circumscribed circles, solid geometry are missing). Notably, the paper lacks an explicit limitations section — a gap the reviewers did not strongly penalize but that weakens the scholarly completeness.",
    "open_questions": [
      "Can the backward-deduction data engine be extended to more complex mathematical domains (combinatorics, probability, solid geometry, proofs) where the constructive property of diagrams is less straightforward?",
      "Does the rule-based template approach for captions and problems create systematic blind spots or distributional biases that limit generalization to real-world math problems with natural language variation and messier diagrams?",
      "What is the scaling law for synthetic math-visual data — does performance continue to improve monotonically (as the 25%→100% ablation suggests), or does it plateau, and at what point does real-world data diversity become essential?"
    ],
    "building_blocks": [
      "CLIP contrastive learning fine-tuned for domain-specific vision encoding (CLIP-Math)",
      "Backward-deduction problem generation from known mathematical formulas",
      "Template-based caption generation (GPT-4 for one-time template creation, programmatic filling at scale)",
      "Progressive multi-stage training (encoding → alignment → instruction tuning → DPO)",
      "DPO with self-generated incorrect outputs as negative samples",
      "Minimized textual redundancy in questions to force visual reliance",
      "Python-based procedural diagram generation (plane geometry via iterative shape composition)",
      "LoRA-based fine-tuning with MLP projection layers for vision-language alignment",
      "MAVIS-Caption (558K) and MAVIS-Instruct (834K) as reusable open-source datasets"
    ],
    "reviewer_feedback_summary": "Ratings: 8, 6, 6, 6 (Accept Poster). The strongest reviewer (8/5 confidence) praised the comprehensive investigation spanning data curation, visual encoding, and learning methodology, calling the rule-based data engine a genuinely useful contribution. Key concerns across reviewers: (1) template-based generation may limit diversity (addressed with evidence of 804K/834K unique questions and complementary real-world data), (2) limited to 7B model scale (addressed with 8×7B and LLaVA-NeXT-8B experiments showing +8.4% transfer), (3) limited diagram type coverage (acknowledged but argued current types cover most benchmarks), (4) the work is 'engineering-focused rather than methodologically innovative' — combining CLIP, LLaVA, and DPO without novel architecture (partially addressed by arguing the data engine itself is the methodological contribution). Reviewer_uZLE raised their score from 5→6 after the rebuttal. The AC noted the rebuttal 'effectively resolved major issues leading to consensus acceptance' despite lingering concerns about rule-based engine extensibility.",
    "relevance_to_seed": "This paper is directly central to multi-modal mathematical reasoning research. Its key transferable lesson is that the bottleneck in math-visual AI is not model architecture but *data infrastructure* — and that mathematical objects' constructive nature enables fully automatic data generation that is correct by construction. Any follow-up work in this area should either build on MAVIS's datasets/pipeline or explain why a different data strategy is needed. The backward-deduction problem generation technique and the insight about minimizing textual redundancy to force genuine visual reasoning are particularly reusable methodological innovations."
  },
  {
    "title": "DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models",
    "venue": "ICLR 2025",
    "problem_identification": "Existing visual math benchmarks (MathVista, MathVerse, MATH-V) are static collections, meaning high scores could reflect pattern memorization rather than genuine reasoning. The authors identified this gap by asking a deceptively simple question: if a model can solve a math problem, can it solve trivial variations of the same problem? They drew on the classical robustness/worst-case analysis tradition from adversarial ML and applied it to a domain (visual math) where nobody had systematically measured it, revealing that VLMs lack the compositional stability humans exhibit on minor problem perturbations.",
    "key_insight": "Encoding each benchmark question as a parameterized Python program — rather than a fixed image-text pair — transforms evaluation from a static snapshot into a distribution over problem variants, enabling worst-case vs. average-case analysis that exposes robustness failures invisible to conventional benchmarking. The insight is that the program IS the question, not any single rendering of it.",
    "innovation_type": "new_benchmark",
    "method_summary": "The authors curate 501 seed questions across 9 math topics (plane geometry, analytic geometry, statistics, algebra, graph theory, etc.) spanning elementary to undergraduate difficulty. Each seed question is manually encoded as a Python program using Matplotlib/Pyglet that accepts random parameters and outputs both a visual figure and a ground-truth answer. Seven variation types are defined: numerical values, geometric transformations, function types, colors, symbolic substitutions, graph structures, and real-life contexts. At evaluation time, 10 concrete variants are sampled per seed (5,010 total), and models are scored on average-case accuracy (mean across variants), worst-case accuracy (fraction of seeds where ALL 10 variants are correct), and reasoning robustness (worst/average ratio). A repetition consistency metric further disentangles stochastic decoding noise from genuine reasoning failures by checking if models give the same (wrong) answer deterministically.",
    "what_makes_it_good": "The paper succeeds because it introduces a clean, falsifiable claim — 'VLMs that appear competent on average are catastrophically fragile on variations' — and backs it with a methodology that makes the gap undeniable (GPT-4o: 63.7% avg → 34.7% worst-case). The programmatic design is both the methodological contribution and the practical gift: it makes the benchmark self-renewing, resistant to contamination, and infinitely extensible. The evaluation is thorough (14 models, human baselines, error taxonomy, memorization analysis), turning a benchmark paper into a diagnostic study.",
    "limitations_acknowledged": "The authors acknowledge that encoding problems as programs requires substantial human effort, limiting coverage of highly complex problems and making the difficulty distribution 'relatively limited compared to MATH-V.' They also note the benchmark considers only individual variation types rather than combinations, and the seed question selection introduces dataset bias (e.g., Puzzle Tests are only 3.4% of the dataset despite being the hardest category).",
    "open_questions": [
      "Can the programmatic generation approach be automated using LLMs to write the Python programs themselves, scaling beyond human curation? The authors explicitly flag this as future work, and it represents a meta-benchmark-generation problem.",
      "Do the robustness failures stem from visual perception deficits (figure reading errors account for 33.1% of Claude-3.5's mistakes) or from reasoning fragility? Disentangling these would require ablations where models receive perfect symbolic descriptions instead of images.",
      "Would training on programmatically varied visual math data (i.e., using DynaMath-style generators for data augmentation) close the robustness gap, or is the failure architectural — indicating that current VLM vision encoders fundamentally lack the invariance properties needed for mathematical figure understanding?"
    ],
    "building_blocks": [
      "Parameterized Python programs as benchmark generators (Matplotlib + Pyglet)",
      "Worst-case vs. average-case accuracy framework for robustness evaluation",
      "Reasoning robustness ratio (RR = worst/avg) as a model-comparison metric",
      "Repetition consistency metric to separate stochastic noise from systematic failures",
      "Seven-category variation taxonomy for visual math problems",
      "Error taxonomy: figure reading, reasoning, calculation, hallucination",
      "Seed question sourcing pipeline (MathVista + MATH-V + MMMU + internet + novel)",
      "STEM student annotation of solution strategies as program prototypes"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is directly central to multi-modal mathematical reasoning: it provides both a diagnostic tool and a conceptual framework for understanding WHERE integration of visual, symbolic, and textual understanding breaks down in current models. Its key lesson for our research area is that robustness — not just accuracy — should be the primary evaluation axis, and that programmatic generation of visual-mathematical stimuli is a powerful methodology for stress-testing multi-modal reasoning that we should adopt or extend in our own benchmark/evaluation designs."
  },
  {
    "title": "MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?",
    "venue": "ECCV 2024",
    "problem_identification": "The authors identified that existing visual math benchmarks (MathVista, GeoQA, MMMU) embed redundant textual descriptions that duplicate information already present in diagrams — enabling MLLMs to 'cheat' by deriving answers from text alone without genuinely interpreting visual input. They discovered this by running a simple but devastating pilot ablation on 120 problems: removing diagrams entirely and observing that most MLLMs actually scored *higher* without visual input (e.g., Qwen-VL-Max +5.1%, InternLM-XComposer2 +5.6%). This revealed that the field's evaluation methodology was fundamentally compromised — benchmarks were measuring text comprehension, not visual reasoning.",
    "key_insight": "By decomposing the textual content of math problems into three semantic categories (Descriptive Information, Implicit Properties, Essential Conditions) and systematically ablating them across six problem versions, you can create a controlled experimental framework that precisely isolates *what* visual capabilities a model possesses versus what it fakes via textual shortcuts. The insight is that information-theoretic decomposition of the text-vision redundancy — not just removing images — is the right lens for diagnosing multimodal understanding.",
    "innovation_type": "new_benchmark",
    "method_summary": "MathVerse collects 2,612 high-quality math problems with diagrams spanning plane geometry, solid geometry, and functions. Each problem's textual content is taxonomized into three categories: Descriptive Information (DI — directly observable diagram content like shape names), Implicit Properties (IP — spatial relationships like parallelism requiring perception but not domain knowledge), and Essential Conditions (EC — precise numerical measurements that cannot be inferred visually). Human annotators then create six versions of each problem by progressively migrating information from text into the diagram: Text-dominant (all text + diagram), Text-lite (remove DI), Text-only (remove diagram entirely), Vision-intensive (remove IP), Vision-dominant (move EC into diagram), and Vision-only (everything rendered visually). This yields 15,672 test samples. Additionally, a two-phase Chain-of-Thought evaluation strategy uses GPT-4 to extract key reasoning steps from model outputs (deliberately without access to ground truth, to avoid bias), then GPT-4V scores each step with error categorization, producing a weighted score: Score = 0.7 × (mean step accuracy) + 0.3 × (final answer accuracy).",
    "what_makes_it_good": "Three qualities made this paper stand out. First, the core idea is elegantly simple yet profoundly revealing — the information-level ablation is easy to understand but exposes a systemic blind spot across the entire MLLM evaluation ecosystem. Second, the experimental findings are genuinely surprising and newsworthy: state-of-the-art models performing *better* without visual input is a striking result that demands attention. Third, the methodology is rigorous and generalizable — the DI/IP/EC taxonomy and six-version framework provide a reusable template for probing multimodal understanding in any domain, not just math.",
    "limitations_acknowledged": "The authors identify five limitations: restriction to high-school level mathematics, exclusion of multi-diagram problems, reliance on GPT-4(V) for CoT evaluation introducing potential model-specific biases, a small human baseline (only 10 college students), and focus on pure mathematical reasoning rather than real-world application contexts.",
    "open_questions": [
      "Can the DI/IP/EC information decomposition framework be generalized to non-mathematical multimodal tasks (e.g., scientific diagrams, engineering drawings, medical imaging) to similarly expose visual comprehension failures?",
      "The paper reveals that current vision encoders are fundamentally inadequate for mathematical diagrams — what architectural changes (e.g., symbolic parsing heads, geometry-aware pretraining, OCR-integrated encoders) would most effectively close this gap?",
      "The CoT evaluation relies on GPT-4(V) as judge, creating a circular dependency for evaluating future models that surpass GPT-4V — what evaluation methodology would remain valid as frontier models improve?"
    ],
    "building_blocks": [
      "DI/IP/EC information taxonomy for multimodal text-vision decomposition",
      "Six-level visual ablation framework (Text-dominant → Vision-only)",
      "Two-phase CoT evaluation: blind step extraction + grounded step scoring",
      "GPT-4(V)-as-judge with weighted step-level scoring formula",
      "Curated dataset from GeoQA (750), GEOS (119), Geometry3K (507), plus 1,236 newly collected problems",
      "Error taxonomy: Visual Perception / Reasoning / Knowledge / Calculation errors",
      "Testmini subset sampling strategy (788 problems / 4,728 samples) for efficient evaluation"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is directly foundational to multi-modal mathematical reasoning research: it provides both the diagnostic framework (visual ablation) and the empirical evidence that current MLLMs fundamentally fail at integrating visual understanding with symbolic/textual reasoning. For our research area, the key lesson is methodological — any new approach to multi-modal math reasoning MUST be evaluated under information-controlled conditions (not just end-to-end accuracy), and the DI/IP/EC decomposition offers a ready-made framework for designing such evaluations. The paper also reveals the most critical bottleneck: vision encoders that can parse mathematical diagrams into structured symbolic representations."
  },
  {
    "title": "Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset",
    "venue": "NeurIPS 2024 (Datasets & Benchmarks Track)",
    "problem_identification": "The authors identified that existing multimodal math benchmarks (MathVista, MMMU) suffered from three specific deficiencies: narrow subject coverage (7 categories vs. needed 16), short/template-like questions (avg 15.6 words in MathVista vs. 42.3 in MATH-V), and coarse or incomplete difficulty grading (37.7% of MathVista problems had no difficulty label). They found this gap by doing a systematic comparative audit of existing benchmarks along axes of diversity, granularity, and authenticity — essentially stress-testing the evaluation tools themselves rather than the models, which is a meta-research insight that existing 'human-level' claims on MathVista were artifacts of benchmark weakness, not model strength.",
    "key_insight": "Rather than constructing synthetic problems or post-hoc annotating existing images, the authors realized that real math competition problems are a naturally curated source that simultaneously provides visual grounding, calibrated difficulty (via competition grade levels), and taxonomic diversity (competitions span many subfields) — turning the curation problem from 'design good problems' into 'carefully filter and organize existing ones.' This reframing dramatically lowered the cost of creating a high-quality benchmark while increasing its authenticity.",
    "innovation_type": "new_benchmark",
    "method_summary": "The authors sourced 3,352 candidate problems from 19 international math competitions (Math Kangaroo, AMC 8/10/12, AIME, UKMT Grey/Pink/Junior/Senior) and applied a rigorous 4-stage curation pipeline: (1) text-image alignment verification by 10 cross-validating annotators (filtering to 3,040 problems), (2) duplicate detection via lexical overlap and Levenshtein distance, (3) subject categorization through majority voting across 3 independent annotation groups with GPT-4V/Gemini Pro consultation, and (4) difficulty assignment mapped from competition grade requirements to a 5-level scale. The final dataset spans 16 mathematical disciplines with a balanced mix of 1,532 multiple-choice and 1,508 free-form problems. They evaluated 15+ models (LLMs with captions, open-source LMMs like LLaVA/SPHINX/InternLM, and closed-source LMMs like GPT-4V/Gemini Pro/Qwen-VL) in zero-shot settings with and without chain-of-thought, and conducted a detailed 232-error manual analysis of GPT-4V failures categorized into 6 error types.",
    "what_makes_it_good": "Three things elevate this beyond a routine benchmark paper: First, the gap identification is genuinely actionable — they didn't just say 'we need harder problems' but precisely diagnosed WHY existing benchmarks were insufficient (subject coverage, question complexity, difficulty calibration), making the contribution feel necessary rather than incremental. Second, the error taxonomy (reasoning 42.2%, vision recognition 31.9%, knowledge 15.1%, question misunderstanding 6.9%, calculation 1.3%, refusal 2.6%) provides a diagnostic roadmap that future model builders can directly act on. Third, the finding that chain-of-thought HURTS some models (Gemini Pro -3.32%, Qwen-VL-Max -2.96%) while helping others (GPT-4V +1.22%) is a surprising empirical contribution that challenges the dominant assumption that CoT universally helps, giving the paper analytical depth beyond just reporting accuracy numbers.",
    "limitations_acknowledged": "The authors explicitly acknowledged three gaps: the dataset is English-only (no multilingual evaluation), covers only mathematics (no physics or chemistry), and uses only abstract competition diagrams rather than real-world photographs — the last of which they later addressed with the MATH-Vision-Wild variant featuring photographic captures under varying conditions.",
    "open_questions": [
      "Why does chain-of-thought prompting degrade performance for some models but improve it for others? This points to fundamental differences in how models process multi-step visual-symbolic reasoning that are not yet understood and could be a rich research direction.",
      "Vision recognition errors account for 31.9% of GPT-4V failures — is the bottleneck in low-level visual parsing (reading diagram labels, identifying geometric shapes) or in higher-level spatial reasoning (understanding relative positions, inferring 3D from 2D)? Disentangling these would guide whether to improve vision encoders vs. reasoning modules.",
      "The massive gap between human (75.66%) and best model (22.76% at time of publication) suggests that competition math requires reasoning capabilities qualitatively different from what current LMMs possess — what specific cognitive operations (spatial manipulation, multi-step deduction, analogy) are models most lacking, and can these be taught through targeted training rather than scale alone?"
    ],
    "building_blocks": [
      "Math competition problem databases (Math Kangaroo, AMC/AIME, UKMT) as authentic curated sources for benchmark construction",
      "4-stage curation pipeline (alignment verification → duplicate detection → subject categorization → difficulty assignment) as a reusable template for benchmark building",
      "Hybrid human-AI annotation with majority voting (3 independent groups + LMM consultation for subject categorization)",
      "6-category error taxonomy for multimodal reasoning (reasoning, vision recognition, knowledge, question misunderstanding, calculation, refusal)",
      "Levenshtein distance + lexical overlap for duplicate detection in math problem corpora",
      "Competition grade-level to difficulty-level mapping as a principled approach to calibrating problem difficulty",
      "Zero-shot evaluation with and without CoT as a diagnostic methodology for probing reasoning depth",
      "MATH-Vision-Wild variant methodology — re-photographing problems under real-world conditions to test robustness"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is directly foundational to multi-modal mathematical reasoning research: it provides the most comprehensive diagnostic benchmark for evaluating how well models integrate visual understanding (diagram parsing), symbolic reasoning (algebraic manipulation), and textual comprehension (problem statement interpretation). For our research area, the key takeaway is methodological — the error taxonomy reveals that the bottleneck is roughly evenly split between vision failures (31.9%) and reasoning failures (42.2%), suggesting that advances in multi-modal math reasoning require jointly improving both perception and inference rather than focusing on either alone. The 16-subject taxonomy also reveals which mathematical domains (topology, graph theory, solid geometry) remain hardest, providing a prioritization map for future work."
  },
  {
    "title": "URSA: Understanding and Verifying Chain-of-thought Reasoning in Multimodal Mathematics",
    "venue": "NeurIPS 2025 (Main Track)",
    "problem_identification": "The authors identified that Process Reward Models (PRMs) — already proven for text-only math reasoning via test-time scaling — had never been integrated into multimodal mathematical reasoning. They traced this gap to three compounding bottlenecks: (1) insufficient high-quality multimodal CoT data to build a strong enough foundation model, (2) no automated method for process-level labeling that accounts f
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
  "promptId": "07328a36-6231-4e3f-9221-67cc86ce1ed7",
  "type": "user",
  "uuid": "e650ff4c-8943-4944-9c19-8e9e17678c36",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:16:37.638Z_

```json
{
  "parentUuid": "e650ff4c-8943-4944-9c19-8e9e17678c36",
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
  "uuid": "4bb86022-0552-4fde-b63c-8c976d5e55a9",
  "timestamp": "2026-05-28T05:16:37.638Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:16:37.638Z_

```json
{
  "parentUuid": "4bb86022-0552-4fde-b63c-8c976d5e55a9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4bda12ba-a01f-47aa-b2ce-1cd05f679b53",
  "timestamp": "2026-05-28T05:16:37.638Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Multi-Modal Mathematical Reasoning —…",
  "leafUuid": "4bda12ba-a01f-47aa-b2ce-1cd05f679b53",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize multi-modal math reasoning literature into strategy guide",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d"
}
```

---

### Assistant

_source line 8 · 2026-05-28T05:17:10.383Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 18 paper analyses into a strategic "Field Guide" for multi-modal mathematical reasoning research. However, the paper analyses appear to be truncated — I can see 7 papers fully described, and the text cuts off mid-sentence in the 7th paper (URSA). Let me work with what I have and also note that there were 18 papers mentioned.

Let me carefully analyze the patterns across these papers and produce the requested JSON output.

Let me catalog what I have:

1. **MathVista** (ICLR 2024 Oral) - Foundational meta-benchmark, 28 existing datasets + 3 new ones, taxonomy framework


2. **EMMA** (ICML 2025 Oral) - Enhanced benchmark with two-stage filtering for genuine multimodality
3. **MAVIS** (ICLR 2025 Poster) - Automatic data engine for math-visual training data, backward-deduction generation
4. **DynaMath** (ICLR 2025) - Dynamic/parameterized benchmark for robustness evaluation
5. **MathVerse** (ECCV 2024) - Visual ablation benchmark, DI/IP/EC taxonomy
6. **MATH-Vision** (NeurIPS 2024 D&B) - Competition-sourced benchmark, 16 math disciplines
7. **URSA** (NeurIPS 2025) - Process Reward Models for multimodal math

Now I'm noticing the core innovation patterns across these papers. There's a strong focus on diagnostic benchmarks that pinpoint specific failure modes rather than just measuring overall performance, and several papers are building automatic data generation engines to scale training data. I can see the trajectory even with the truncated list—these represent the frontier of how we're evaluating and improving multimodal math reasoning.

The reviewer preferences are becoming clearer too: they value rigor and comprehensiveness, they're drawn to counterintuitive findings that challenge assumptions, and they want actionable insights that go beyond raw accuracy metrics. Clean, well-supported claims with principled taxonomies that make sense of the landscape seem to resonate most.

There are some real gaps in the field I'm noticing—understanding why vision and reasoning fail independently, figuring out why chain-of-thought sometimes hurts on visual tasks, building better vision encoders for mathematical diagrams. And then there are these untried combinations that could be powerful: merging data generation approaches with robustness training, combining filtering and ablation techniques for more granular diagnosis, or exploring visual scratchpads that let models manipulate diagrams iteratively during reasoning.

Now I'm ready to pull together a comprehensive field guide based on the available research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bda12ba-a01f-47aa-b2ce-1cd05f679b53",
  "isSidechain": false,
  "requestId": "req_011CbUQ7AD5e2V5qBqQS7bfz",
  "type": "assistant",
  "uuid": "7ca24dc2-41e7-41cb-8361-11209f4bb2ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyVAcEwoJKGQ7ccp7tZkxN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10974,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8668,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 10974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10974
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

_source line 9 · 2026-05-28T05:20:18.000Z_

I'll analyze the paper analyses carefully and synthesize them into a strategic field guide. Let me first review the full content to ensure I capture all the details.

Given the truncation at paper 7 (URSA), I'll work with the rich detail available from the 7 fully described papers plus the partial URSA description to produce the most evidence-based synthesis possible.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Diagnostic Benchmark via Information-Controlled Ablation",
      "description": "Rather than building a standard accuracy benchmark, decompose the information channels (text, vision, captions) and systematically ablate them to reveal what models ACTUALLY use. This transforms benchmarks from measurement tools into diagnostic instruments that generate actionable findings and shape entire research agendas. The key is to demonstrate that models 'cheat' — producing a striking, counterintuitive headline result (e.g., 'models score higher without images') that makes the contribution undeniable.",
      "examples": ["MathVerse (DI/IP/EC six-version ablation)", "EMMA (two-stage text-only + caption filtering)", "MathVista (multi-strategy prompting evaluation)"],
      "success_rate": "high"
    },
    {
      "pattern": "Programmatic/Parameterized Evaluation",
      "description": "Encode benchmark questions as parameterized programs rather than static image-text pairs, enabling infinite variant generation, contamination resistance, and worst-case analysis. This works because mathematical objects are constructive — every element is generated from known parameters. The program IS the question, not any single rendering.",
      "examples": ["DynaMath (Python programs generating 10 variants per seed)", "MAVIS (procedural diagram generation via Python rendering)"],
      "success_rate": "high"
    },
    {
      "pattern": "Automatic Data Engine Exploiting Mathematical Constructiveness",
      "description": "Recognize that mathematical diagrams — unlike natural images — are fully constructive objects where ground truth is derivable from generation parameters. This transforms the data bottleneck from an annotation problem into a code-generation problem. Use backward deduction from known conditions through mathematical formulas to generate problems that are correct by construction.",
      "examples": ["MAVIS (558K captions + 834K problems generated automatically)", "DynaMath (parameterized Python programs)"],
      "success_rate": "high"
    },
    {
      "pattern": "Systematic Decomposition of Failure Modes into Orthogonal Sub-Problems",
      "description": "Rather than proposing one monolithic solution, decompose the problem into independent bottlenecks (e.g., encoding, alignment, reasoning) and address each with a dedicated stage/component. This earns reviewer trust through methodological rigor and makes contributions modular and extensible.",
      "examples": ["MAVIS (3 bottlenecks → 4 training stages)", "URSA (data + PRM + verification as separate contributions)", "MATH-Vision (6-category error taxonomy splitting vision 31.9% vs. reasoning 42.2%)"],
      "success_rate": "high"
    },
    {
      "pattern": "Meta-Benchmark Unification of Fragmented Landscape",
      "description": "When a research area has many small, siloed datasets with inconsistent formats, the highest-impact contribution is not yet another dataset but a principled unification under a clear taxonomy. The taxonomy IS the contribution. This works best at inflection points when a new capability (e.g., GPT-4V) makes evaluation urgent.",
      "examples": ["MathVista (28 datasets unified under 5×7×15 taxonomy)"],
      "success_rate": "high"
    },
    {
      "pattern": "Surprising Empirical Finding as Paper Anchor",
      "description": "Structure the paper around a counterintuitive empirical result that demands explanation: CoT hurts performance, removing images improves scores, worst-case accuracy is half of average-case. This gives reviewers a 'hook' — the paper answers a question they didn't know they had. Every top-venue acceptance in this survey features at least one headline-grabbing finding.",
      "examples": ["MathVerse (models score higher without images)", "EMMA (CoT degrades open-source model performance on visual tasks)", "DynaMath (GPT-4o: 63.7% avg → 34.7% worst-case)", "MATH-Vision (CoT hurts Gemini Pro by 3.32%)"],
      "success_rate": "high"
    }
  ],
  "reviewer_preferences": [
    "Actionable diagnostics over raw accuracy tables: Papers that reveal SPECIFIC failure modes with quantified breakdowns (e.g., MATH-Vision's 42.2% reasoning vs. 31.9% vision recognition errors) consistently earn praise, while papers that just report 'models do poorly' get lukewarm reviews. Reviewers want to learn something that changes how they think about the problem.",
    "Thoroughness that builds trust: MathVista's 116 pages with 120 figures and 67 pages of GPT-4V analysis earned it an Oral. MAVIS's comprehensive investigation spanning data curation, visual encoding, and learning methodology earned the strongest reviewer score (8). Reviewers in this area expect exhaustive evaluation — 10+ models, multiple prompting strategies, ablations on each component.",
    "Principled taxonomies and frameworks: Every accepted paper introduces a taxonomy (MathVista's 5×7×15, MathVerse's DI/IP/EC, EMMA's domain-specific visual reasoning categories, MATH-Vision's 16 disciplines, DynaMath's 7 variation types). Reviewers treat well-designed taxonomies as standalone contributions that organize messy research landscapes.",
    "Counterintuitive or newsworthy findings: The papers receiving the highest venues (ICLR Oral, ICML Oral) all feature striking empirical claims — models better without images, CoT hurting performance, worst-case catastrophic failure. Papers with only expected findings ('bigger model does better') are rated lower.",
    "Methodological contributions that transfer beyond the specific benchmark: Reviewers consistently praise reusable tools — GPT-4-based answer extraction (MathVista), two-stage caption filtering (EMMA), backward-deduction data generation (MAVIS), parameterized program encoding (DynaMath). The question is always 'can I use this in my own work?'",
    "Addressing the 'why' with fine-grained analysis over just reporting the 'what': EMMA's error decomposition (53% visual reasoning vs. 30% perceptual errors) and pass@N analysis revealing reasoning selection as the bottleneck, MAVIS's three-bottleneck diagnosis — these demonstrate understanding, not just measurement.",
    "Skepticism toward 'engineering-focused' work: MAVIS reviewers flagged 'combining CLIP, LLaVA, and DPO without novel architecture' as a concern. Papers need to frame engineering contributions as enabling new capabilities or solving infrastructure problems, not just combining existing components.",
    "Explicit limitations sections and honest acknowledgment of scope: MathVista's acknowledged inability to disentangle perception from reasoning, DynaMath's admitted difficulty distribution limitations — reviewers reward intellectual honesty and penalize papers that oversell."
  ],
  "field_gaps": [
    {
      "gap": "Disentangling visual perception failures from mathematical reasoning failures",
      "evidence": "MathVista explicitly acknowledged this as unresolved (raised by 2 reviewers). MATH-Vision's error taxonomy shows 31.9% vision vs. 42.2% reasoning errors but cannot isolate which occurs first. MathVerse's ablation framework partially addresses this but only at the task level, not within individual model reasoning chains. DynaMath's 33.1% figure-reading errors in Claude-3.5 further highlight the issue. No paper has proposed a method that cleanly separates these failure modes within a single model's processing pipeline.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Vision encoders fundamentally inadequate for mathematical diagrams",
      "evidence": "MAVIS demonstrated CLIP-style encoders trained on natural images cannot encode abstract monochromatic diagrams (motivating CLIP-Math). MathVerse showed models perform better without images, implying vision encoders add noise rather than signal for math diagrams. MATH-Vision found 31.9% of GPT-4V errors are vision recognition failures. DynaMath's figure-reading errors are 33.1% of Claude-3.5 mistakes. No paper has proposed a fundamentally new vision encoder architecture for mathematical content — MAVIS's CLIP-Math fine-tuning is the closest, but it's still a patch on CLIP rather than a purpose-built solution.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Chain-of-Thought degradation on visual reasoning tasks is unexplained",
      "evidence": "EMMA found open-source models get WORSE with CoT on visual tasks. MATH-Vision found CoT hurts Gemini Pro (-3.32%) and Qwen-VL-Max (-2.96%) while helping GPT-4V (+1.22%). Neither paper explains the mechanism — is it training data bias, architectural limitation, or fundamental incompatibility between sequential linguistic reasoning and parallel spatial reasoning? No follow-up work has proposed an explanation or fix.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Visual simulation and spatial manipulation capabilities in MLLMs",
      "evidence": "EMMA explicitly identified that models cannot 'reason WITH visual content' — mentally simulating 3D rotations, tracing force vectors, predicting molecular transformations. They ask whether architectural changes like visual scratchpads or iterative image generation during reasoning would enable this. No paper in the survey implements such capabilities. EMMA's domain taxonomy (3D spatial simulation, 2D transformation, path tracing) provides the evaluation framework, but no training methodology exists.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Robustness of visual math reasoning under trivial perturbations",
      "evidence": "DynaMath showed GPT-4o drops from 63.7% average to 34.7% worst-case accuracy on minor problem variations. No paper proposes a training methodology that specifically targets this robustness gap. DynaMath explicitly asks whether training on programmatically varied data would close the gap or whether the failure is architectural.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Logical reasoning and numeric common sense in visual contexts",
      "evidence": "MathVista identified catastrophic failures in logical reasoning (21.6%) and numeric common sense (20.1%) as 'the sharpest failure modes that remain largely unsolved.' These specific sub-capabilities have not been targeted by any subsequent method paper in the survey.",
      "difficulty": "high",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Process Reward Models (PRMs) for multimodal mathematical reasoning",
      "evidence": "URSA (NeurIPS 2025) began addressing this but the analysis is truncated. The problem description identifies that PRMs proven in text-only math had never been integrated into multimodal math, with compounding bottlenecks in data, labeling methodology, and vision-aware verification. This represents a frontier where test-time compute scaling meets multimodal reasoning.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Scaling laws for synthetic math-visual training data",
      "evidence": "MAVIS shows performance improves from 25% to 100% of their synthetic data but does not characterize the scaling curve or identify diminishing returns. No paper establishes whether synthetic math-visual data follows power-law scaling, when real-world data diversity becomes essential, or what the optimal ratio of synthetic-to-real data is for different mathematical domains.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Evaluation methodology for models that surpass GPT-4V",
      "evidence": "MathVerse relies on GPT-4(V) as a judge for CoT evaluation, creating a circular dependency. As frontier models surpass GPT-4V, the evaluation methodology breaks. No paper proposes a GPT-4V-free evaluation protocol for complex multimodal math reasoning that maintains the step-level granularity of MathVerse's approach.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "Robustness-aware training via MAVIS-style data engines generating DynaMath-style parameterized variants: Use MAVIS's backward-deduction pipeline to generate problems, but instead of sampling each diagram once, generate N parameterized variants per problem (varying numerical values, geometric transformations, colors per DynaMath's 7-category taxonomy). Train with contrastive or consistency objectives that force the model to produce identical reasoning chains across variants, directly targeting the robustness gap DynaMath exposed.",
      "from_papers": ["MAVIS", "DynaMath"],
      "why_promising": "DynaMath showed the robustness gap (63.7% → 34.7%) but only diagnoses it. MAVIS has the data engine to generate training data but doesn't target robustness. Combining them converts a diagnostic finding into a training methodology. The programmatic nature of both approaches means this is implementable without human annotation."
    },
    {
      "idea_sketch": "EMMA-filtered training data + MathVerse-style progressive visual dependency curriculum: Generate or filter training data using EMMA's two-stage protocol to ensure only genuinely multimodal problems survive. Then train models using a curriculum that progressively removes textual hints following MathVerse's Text-dominant → Vision-only progression, forcing models to develop genuine visual reasoning rather than textual shortcuts.",
      "from_papers": ["EMMA", "MathVerse", "MAVIS"],
      "why_promising": "EMMA and MathVerse independently showed that models exploit textual shortcuts, but neither proposed a training methodology to prevent this. MAVIS's 'minimized textual redundancy' hints at this direction but doesn't implement the systematic information-controlled curriculum that MathVerse's framework enables. This combination would produce models evaluated to provably require visual reasoning."
    },
    {
      "idea_sketch": "Visual scratchpad architecture with iterative diagram manipulation for spatial reasoning: Build an MLLM that, during chain-of-thought reasoning, can generate intermediate visual representations (annotated diagrams, auxiliary constructions, coordinate overlays) and re-process them — essentially giving the model a 'visual working memory' or geometric scratchpad. Evaluate specifically on EMMA's 3D simulation and 2D transformation tasks where purely linguistic CoT provably fails.",
      "from_papers": ["EMMA", "MAVIS", "MathVerse"],
      "why_promising": "EMMA showed CoT degrades visual reasoning in open-source models, suggesting sequential linguistic reasoning is fundamentally wrong for spatial tasks. EMMA also showed pass@N analysis reveals models 'know' answers but can't select them — a visual scratchpad could serve as an intermediate verification step. No paper proposes this architecture despite multiple papers identifying the need. This addresses the highest-impact gap (visual simulation capabilities) with a concrete architectural proposal."
    },
    {
      "idea_sketch": "Perception-Reasoning Disentanglement Module: Build a two-stage pipeline where Stage 1 is a specialized vision encoder that outputs a structured symbolic representation of mathematical diagrams (parsed shapes, coordinates, labels, relationships as a scene graph), and Stage 2 is a reasoning module that operates on this symbolic representation. Evaluate by comparing end-to-end performance vs. performance with ground-truth symbolic inputs, cleanly measuring each stage's contribution.",
      "from_papers": ["MathVista", "MathVerse", "MATH-Vision", "MAVIS"],
      "why_promising": "Four papers independently identify the inability to disentangle perception from reasoning as a critical unsolved problem. MAVIS's CLIP-Math partially addresses the encoder side, and MathVerse's DI/IP/EC framework provides the evaluation methodology. A clean modular architecture with a symbolic intermediate representation would make the disentanglement measurable AND improvable. The symbolic bottleneck also enables interpretability — a growing reviewer concern."
    },
    {
      "idea_sketch": "Multimodal Process Reward Model trained on MAVIS-style synthetic CoT data with DynaMath-style consistency verification: Use MAVIS's backward-deduction to generate step-by-step solutions where each step's correctness is known by construction. Train a multimodal PRM that scores individual reasoning steps conditioned on both the visual input and the textual chain. Use DynaMath-style variant consistency as an additional training signal — if a model's reasoning is correct, it should transfer across parameterized variants.",
      "from_papers": ["URSA", "MAVIS", "DynaMath", "EMMA"],
      "why_promising": "URSA identified multimodal PRMs as a frontier but struggled with automated process-level labeling. MAVIS's backward-deduction gives free step-level annotations. DynaMath's variant consistency provides a complementary supervision signal that doesn't require labels at all. EMMA's pass@N results (81.5% at N=16 vs. 50.75% majority voting) prove the verification/selection bottleneck is real and worth solving."
    },
    {
      "idea_sketch": "Cross-domain transfer of mathematical visual reasoning from geometry to chemistry/physics diagrams using domain-specific CLIP variants: Extend MAVIS's CLIP-Math approach to build CLIP-Chem and CLIP-Physics encoders, then study whether the visual encoding improvements transfer across mathematical domains. Use EMMA's multi-domain benchmark (math, physics, chemistry, coding) as the evaluation testbed.",
      "from_papers": ["MAVIS", "EMMA", "MATH-Vision"],
      "why_promising": "MAVIS showed CLIP-Math dramatically improves geometry understanding but only covers 3 diagram types. EMMA's benchmark spans 4 domains but no paper targets cross-domain visual encoding. MATH-Vision's 16-subject taxonomy reveals which domains (topology, graph theory, solid geometry) are hardest — these are precisely where domain-specific encoders could have the most impact. Transfer learning across math-adjacent visual domains is entirely unexplored."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "Two-Stage Caption Filtering Pipeline",
      "what_it_does": "Ensures benchmark problems genuinely require visual reasoning by (1) removing text-only solvable problems, then (2) generating detailed captions and filtering out problems solvable from text+captions using multi-model consensus (3 models × 10 attempts).",
      "used_by": ["EMMA"],
      "could_be_applied_to": "Training data curation — filter existing multimodal math datasets to retain only problems requiring genuine visual reasoning, creating higher-quality fine-tuning data. Could also be applied to any multimodal benchmark in non-math domains (scientific diagrams, medical imaging, engineering drawings) to verify evaluation validity."
    },
    {
      "tool": "Backward-Deduction Problem Generation",
      "what_it_does": "Generates math problems by randomly selecting a known condition as the answer, then systematically deducing backward through applicable mathematical formulas to construct premises. The solution is the reverse of the deduction chain, making it correct by construction.",
      "used_by": ["MAVIS"],
      "could_be_applied_to": "Generating process-level supervision labels for PRM training (each backward step is a verified reasoning step). Could also generate curriculum-difficulty-controlled problems by varying deduction chain length. Extensible to algebraic proof generation, combinatorics problem construction, or physics problem synthesis where forward simulation validates backward construction."
    },
    {
      "tool": "DI/IP/EC Information Taxonomy with Progressive Ablation",
      "what_it_does": "Decomposes multimodal problem text into Descriptive Information (directly observable), Implicit Properties (perceptible spatial relationships), and Essential Conditions (precise measurements). Creates six versions from Text-dominant to Vision-only by progressively migrating information from text to diagram.",
      "used_by": ["MathVerse"],
      "could_be_applied_to": "Training curriculum design — progressively train models on easier (Text-dominant) to harder (Vision-only) versions. Could also serve as a fine-grained evaluation framework for any domain where text and visual information overlap (medical reports + scans, scientific papers + figures, engineering specs + blueprints)."
    },
    {
      "tool": "Parameterized Python Programs as Benchmark Generators",
      "what_it_does": "Encodes each benchmark question as a Python program (Matplotlib/Pyglet) that accepts random parameters and outputs both a visual figure and ground-truth answer, enabling infinite variant generation for robustness testing and contamination resistance.",
      "used_by": ["DynaMath"],
      "could_be_applied_to": "Training data augmentation at scale — generate millions of problem variants for robustness training. Could also be adapted for automatic curriculum generation (varying difficulty by adjusting parameter ranges) or for creating personalized evaluation sets that prevent cross-student cheating in educational settings."
    },
    {
      "tool": "GPT-4-Based Answer Extraction Pipeline",
      "what_it_does": "Uses GPT-4 to extract answers from free-form model outputs with >99.5% accuracy, replacing brittle regex/template matching. Enables evaluation of models that produce verbose, inconsistently formatted responses.",
      "used_by": ["MathVista"],
      "could_be_applied_to": "Any benchmark evaluation where model outputs are free-form and heterogeneous. Particularly useful for evaluating reasoning chains where the final answer may be embedded in natural language rather than formatted consistently."
    },
    {
      "tool": "Progressive Multi-Stage Training Pipeline",
      "what_it_does": "Decomposes model training into orthogonal stages: (1) domain-specific vision encoding via contrastive learning, (2) vision-language alignment via projection + LoRA, (3) instruction tuning on domain data, (4) DPO with self-generated negatives. Each stage addresses a specific bottleneck independently.",
      "used_by": ["MAVIS"],
      "could_be_applied_to": "Any domain adaptation of MLLMs where the vision encoder, alignment layer, and reasoning capability each need domain-specific improvement. The pattern of using self-generated incorrect outputs for DPO is particularly transferable — it requires no additional human annotation and targets the model's specific weaknesses."
    },
    {
      "tool": "Worst-Case / Average-Case Robustness Framework",
      "what_it_does": "Evaluates models on both mean accuracy across problem variants and fraction of seed problems where ALL variants are solved correctly. The robustness ratio (worst/average) isolates reasoning stability from raw capability.",
      "used_by": ["DynaMath"],
      "could_be_applied_to": "Evaluating any claimed reasoning capability — if a model truly 'understands' a concept, it should handle minor variations. Could be applied to text-only math, code generation, logical reasoning, or scientific QA by generating parameterized variants of existing benchmark problems."
    },
    {
      "tool": "Two-Phase CoT Evaluation (Blind Extraction + Grounded Scoring)",
      "what_it_does": "Phase 1: GPT-4 extracts key reasoning steps from model output WITHOUT access to ground truth (preventing bias). Phase 2: GPT-4V scores each extracted step against ground truth with error categorization. Weighted score: 0.7 × step accuracy + 0.3 × final answer accuracy.",
      "used_by": ["MathVerse"],
      "could_be_applied_to": "Evaluating any multi-step reasoning task where process matters, not just outcomes. Could be adapted for code debugging (step-level correctness of debugging reasoning), scientific explanation generation, or proof verification where partial credit is important."
    }
  ],
  "common_pitfalls": [
    "Creating a 'multimodal' benchmark where problems are solvable from text alone: EMMA and MathVerse independently proved that many existing benchmarks (MathVista, MMMU) are leaky — models can solve problems without genuinely interpreting visual input. Any new benchmark MUST include a text-only and caption-based solvability check (EMMA's two-stage filtering or MathVerse's ablation) or reviewers will flag this fatal flaw.",
    "Reporting only average-case accuracy: DynaMath demonstrated that average accuracy (63.7%) can mask catastrophic worst-case failure (34.7%). Reviewers increasingly expect robustness analysis. Report worst-case, per-category breakdowns, and error taxonomies — not just a single leaderboard number.",
    "Assuming Chain-of-Thought universally helps: MATH-Vision showed CoT hurts Gemini Pro (-3.32%) and Qwen-VL-Max (-2.96%). EMMA found open-source models degrade with CoT on visual tasks. Any method paper using CoT must ablate with and without it and explain why it helps (or doesn't) for the specific model and task.",
    "Proposing an engineering combination of existing components without framing the infrastructure contribution: MAVIS reviewers flagged 'combining CLIP, LLaVA, and DPO without novel architecture.' If your contribution is primarily engineering, you must frame it as solving an infrastructure problem (e.g., 'the absence of large-scale math-visual training data') rather than claiming algorithmic novelty.",
    "Neglecting the vision encoder as a bottleneck: Multiple papers (MAVIS, MathVerse, MATH-Vision, DynaMath) converge on vision encoding as a fundamental limitation, yet most method papers keep the vision encoder frozen. Ignoring this bottleneck means building on a broken foundation — reviewers will question whether gains are genuine or artifacts of textual shortcuts.",
    "Using GPT-4(V) as evaluator without acknowledging the circular dependency: MathVerse reviewers flagged that using GPT-4V to evaluate models approaching GPT-4V capability creates a methodological problem. As frontier models improve, this becomes increasingly untenable. Propose alternative evaluation strategies or at minimum acknowledge and bound the bias.",
    "Insufficient human baselines: MathVista's 60.3% human accuracy was questioned as either a data quality issue or evidence of required expertise. MATH-Vision used only 10 college students. Reviewers scrutinize human baselines — use enough annotators with appropriate expertise, and measure inter-annotator agreement (MathVista's Fleiss Kappa 0.775 and 99.2% agreement set the standard).",
    "Missing the timing window for benchmark papers: MathVista succeeded partly because it landed as GPT-4V launched. Benchmark papers are most impactful at capability inflection points. Submitting a benchmark for a capability that's already well-measured (e.g., another geometry benchmark without a novel evaluation dimension) will feel incremental.",
    "Claiming to solve 'multimodal reasoning' while testing only on geometry: MAVIS covers only plane geometry, analytic geometry, and function curves. MATH-Vision spans 16 disciplines but is math-only. EMMA spans 4 domains. Reviewers will penalize narrow scope claims — either scope your claims precisely or demonstrate breadth.",
    "Omitting an explicit limitations section: MAVIS notably lacked one, and while reviewers didn't heavily penalize it, the absence weakened scholarly completeness. Every paper should explicitly acknowledge scope limitations, domain coverage gaps, and methodological constraints — reviewers reward intellectual honesty."
  ],
  "field_trajectory": "The field of multi-modal mathematical reasoning is undergoing a phase transition from benchmark creation to method development, but the benchmarks have revealed that the problem is far harder than initially assumed. Three macro-directions are emerging:\n\n**First, the 'genuine multimodality' movement will force architectural innovation.** EMMA and MathVerse have conclusively demonstrated that current MLLMs don't truly integrate visual and symbolic reasoning — they exploit textual shortcuts. The next wave of impactful work will move beyond diagnosis to treatment: purpose-built vision encoders for mathematical content (extending MAVIS's CLIP-Math), visual scratchpad architectures that allow iterative diagram manipulation during reasoning, and modular perception-reasoning pipelines with symbolic intermediate representations. The CoT degradation finding (EMMA, MATH-Vision) strongly suggests that sequential linguistic reasoning is fundamentally wrong for spatial tasks, creating an opening for non-linguistic reasoning paradigms.\n\n**Second, synthetic data engines will become the primary competitive advantage.** MAVIS proved that a 7B model with the right data beats a 110B model without it. The constructive nature of mathematical objects enables fully automatic, correct-by-construction data generation at scale. The next frontier is combining this with DynaMath-style parameterized variation for robustness training, extending backward-deduction to more complex domains (proofs, combinatorics, solid geometry), and establishing scaling laws for synthetic math-visual data. Process-level annotations — which are prohibitively expensive to collect manually — become free when problems are generated backward from solutions, enabling multimodal PRM training (the direction URSA points toward).\n\n**Third, test-time compute scaling for multimodal reasoning will emerge as a major research direction.** EMMA's pass@N analysis (81.5% at N=16 vs. 50.75% majority voting) reveals that the bottleneck is reasoning selection, not knowledge — models can find correct answers but can't reliably identify them. This directly motivates multimodal reward models, verifiers, and search-based reasoning strategies. Combining URSA's PRM approach with MAVIS's automatic step-level annotations and DynaMath's consistency-based verification creates a concrete path toward effective test-time scaling for visual math, mirroring the trajectory that transformed text-only math reasoning in 2023-2024.",
  "meta_advice": "If you're a PhD student aiming to publish a strong 2026 paper in multi-modal mathematical reasoning, here's the strategic calculus: The benchmark opportunity is closing — MathVista, EMMA, MathVerse, DynaMath, and MATH-Vision have established comprehensive evaluation infrastructure, and incremental benchmarks without a novel evaluation dimension will not clear the bar at top venues (MathVista earned its Oral through impeccable timing and thoroughness that's now the expected baseline). The highest-ROI research direction right now is METHOD work that addresses specific, precisely diagnosed failures that the benchmark papers identified but left unsolved.\n\nConcretely, start with an existing benchmark's error taxonomy (MATH-Vision's 6-category breakdown or EMMA's visual reasoning vs. perceptual decomposition) and pick the failure mode with the highest percentage that no one has specifically targeted. Then build a solution that addresses it through a combination of data and architecture — pure architecture papers without domain-specific data face the objection that MAVIS already showed data matters more than architecture, while pure data papers face the objection that vision encoders are fundamentally broken (MathVerse, MAVIS). The sweet spot is a contribution like MAVIS that solves an infrastructure problem (data, encoding, training recipe) rather than claiming a narrow architectural novelty.\n\nTactically, your paper needs three things to survive review: (1) a surprising empirical finding that anchors the narrative (every Oral in this area has one), (2) evaluation under information-controlled conditions using EMMA's filtering or MathVerse's ablation to prove your method genuinely requires visual reasoning, and (3) a reusable building block (dataset, pipeline, framework, taxonomy) that other researchers can adopt. Do not build on MathVista alone — evaluate on EMMA and MathVerse too, and include robustness analysis à la DynaMath. The reviewers for this area now expect multi-benchmark evaluation, ablation studies on each component, and explicit limitations. Finally, consider the untried combinations listed in this guide — the intersection of synthetic data engines, process reward models, and robustness training via parameterized variants is a rich, largely unexplored space with clear evidence of need from multiple top-venue papers."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ca24dc2-41e7-41cb-8361-11209f4bb2ea",
  "isSidechain": false,
  "requestId": "req_011CbUQ7AD5e2V5qBqQS7bfz",
  "type": "assistant",
  "uuid": "1373859c-d1b1-4c0b-a882-1df19c000831",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyVAcEwoJKGQ7ccp7tZkxN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10974,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8668,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 10974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10974
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Multi-Modal Mathematical Reasoning —…",
  "leafUuid": "1373859c-d1b1-4c0b-a882-1df19c000831",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize multi-modal math reasoning literature into strategy guide",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Multi-Modal Mathematical Reasoning —…",
  "leafUuid": "1373859c-d1b1-4c0b-a882-1df19c000831",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize multi-modal math reasoning literature into strategy guide",
  "sessionId": "ddb62a84-afb8-42fd-9324-ff5753fa364d"
}
```

---
