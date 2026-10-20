# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 9
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/35b5d14c-5b69-46e3-9166-8ee9b68949f7.jsonl`
- **Structured JSON:** [`473f0cdac656954614b4.json`](../../sessions/47/473f0cdac656954614b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:28:30.906Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:28:30.906Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diagnostic Co-Evolution\",\n  \"core_problem\": \"Can a PRM serving as a co-evolving diagnostic instrument—classifying step-level reasoning failures into an evolving error taxonomy—drive a more targeted curriculum than concept-level weakness extraction (SwS), scalar uncertainty targeting (R-Zero), or embedding-diversity coverage (Prism), and does the diagnostician's own improvement across iterations compound the generator's gains?\",\n  \"opportunity\": \"Self-improving reasoning loops have proliferated rapidly: SwS (NeurIPS 2025) demonstrates 10%/7.7% gains via concept-level weakness-driven problem synthesis; R-Zero (ICLR 2026) achieves +6.49 via uncertainty-based challenger-solver co-evolution; Prism (March 2026) adds +3.98 over R-Zero via embedding-diversity preservation. Yet all three diagnose weaknesses at fundamentally coarse granularity—SwS extracts topic-level concepts from failed problems (e.g., 'modular arithmetic'), R-Zero targets scalar difficulty (p̂ ≈ 0.5), and Prism ensures geographic coverage in embedding space. None examines WHY the model fails at the reasoning-step level. Meanwhile, PathFinder-PRM (May 2025) classifies step-level errors into types (Mathematical/Consistency/Optimality) but uses this only for PRM training; Data-Driven Reasoning Rubrics (Feb 2026) derives error taxonomies from model failures but applies them statically for reward modeling without curriculum design; and DPE (Feb 2026) implements diagnose→generate→retrain for multimodal models but uses 12 coarse capability dimensions with external frontier LLMs and no verifier co-evolution. The untapped synthesis: use a PRM as a co-evolving diagnostic instrument whose step-level error-type classifications drive targeted problem generation, where the PRM itself improves as it encounters the generator's evolving failure modes. Two problems may share the same concept (algebra) and difficulty level yet fail for completely different reasons (sign error vs. conceptual misunderstanding)—only step-level error-type diagnosis can distinguish these and generate appropriately targeted remediation.\",\n  \"landscape\": \"SwS (NeurIPS 2025) achieves 10%/7.7% average gains (Qwen2.5-7B/32B) via outcome-level weakness identification (max accuracy <50% + negative slope) → concept extraction → concept recombination → filtered problem generation; however, it is single-round, uses no PRM, and cannot distinguish between failures sharing the same topic but differing in error pattern. R-Zero (ICLR 2026) achieves +6.49 (Qwen3-4B) via GRPO-trained challenger targeting p̂ = 0.5 uncertainty, but pseudo-label accuracy degrades from 79% to 63% across iterations and the curriculum signal is purely scalar difficulty. Prism (March 2026) addresses R-Zero's diversity collapse via embedding-cluster-based rarity bonuses (+3.98 AMC), but diversity is geometric rather than diagnostic. Vocabulary Dropout (April 2026) injects random token-mask diversity into R-Zero-style co-evolution (+4.4 avg on Qwen3-8B) but is blind to what kinds of diversity benefit the solver. DPE (Feb 2026, arXiv 2602.22859) implements diagnose→generate→retrain for multimodal LLMs using 12 coarse capability dimensions and 4 frontier LLMs, achieving 8B-surpassing-72B performance but without PRM, step-level analysis, or verifier co-evolution. Data-Driven Reasoning Rubrics (Feb 2026) derives error taxonomies from model failures for domain-adaptive reward modeling (+45% task accuracy over LLM-as-judge) but generates rubrics once without iteration or curriculum design. 'GRPO is Secretly a PRM' (Sep 2025, Saarland University) proves GRPO implicitly performs step-level credit assignment via Monte Carlo estimates from shared token prefixes; lambda-GRPO achieves >10% faster convergence. This challenges explicit PRMs for reward computation but not for structured error diagnosis—the implicit PRM's 'steps' are token-prefix-based, not semantically meaningful error classifications. CoVerRL (ACL 2026) demonstrates generator-verifier co-evolution with 4.7–5.9% gains but uses undirected majority voting. PathFinder-PRM (May 2025) achieves SOTA 67.7 PRMScore with error-aware hierarchical supervision but does not use error types for curriculum. R-PRM (NJUNLP 2025) achieves best open-source PRM with fine-grained error categories but does not leverage them for curriculum. APRM (Nov 2025) creates adversarial PRM curriculum (+3.4pp solver accuracy) but targets PRM robustness only. RL Tango (NeurIPS 2025) co-trains generator and generative verifier via RL but uses outcome-level rewards. AdaRFT (Apr 2025) adapts curriculum on scalar difficulty only (2× speedup). Self-Error-Instruct (ACL 2025) clusters error types for targeted data but uses GPT-4o and doesn't iterate. HSG Hide-and-Seek (Aug 2025) uses adversarial error generation to improve diagnosis by 16.8–31.4% but doesn't close the loop to generator improvement. No existing work combines: (a) step-level PRM error-type classification, (b) error-type-driven targeted problem generation with validated type targeting, (c) iterative co-evolution where the diagnostic instrument itself improves.\",\n  \"inspired_by\": \"SwS (NeurIPS 2025) validates weakness-driven synthesis but at concept level; R-Zero (ICLR 2026) validates co-evolutionary self-improvement but with scalar uncertainty; Prism (2026) validates diversity-aware curriculum but with geographic rather than diagnostic diversity; Data-Driven Reasoning Rubrics (2026) validates auto-derived error taxonomies for reward modeling but without iteration or curriculum; 'GRPO is Secretly a PRM' (2025) establishes that GRPO handles implicit credit assignment, clarifying the PRM's unique value as diagnostic instrument rather than reward signal. Field guide Gap 7 (iterative self-improvement loops), Gap 4 (dynamic co-evolution).\",\n  \"approach\": \"We propose Diagnostic Co-Evolution (DiagCoEvo): a framework where a PRM serves as a co-evolving diagnostic instrument whose step-level error-type classifications drive targeted curriculum generation, while GRPO with standard outcome rewards handles generator training (following the 'GRPO is Secretly a PRM' insight that explicit PRM rewards for GRPO are unnecessary). We initialize generator and PRM from Qwen3-8B. The PRM is trained using PathFinder-PRM's hierarchical error taxonomy as a seed, augmented with data-driven rubric extraction (inspired by Sanders et al. 2026) to produce a dynamic, expandable taxonomy initialized with five core types (Mathematical-Computation, Logical-Consistency, Conceptual-Gap, Strategy-Selection, Hallucination). Each co-evolution iteration executes a four-phase cycle:\\n\\n(1) DIAGNOSE: The PRM evaluates the generator's solutions on a held-out problem bank (2K problems, 8 solutions each), classifying each incorrect step's error type to produce a weakness distribution w = {w_1, ..., w_K} over error types. We also extract 'error-triggering contexts'—the problem features and reasoning patterns most frequently associated with each error type.\\n\\n(2) GENERATE: Targeted problem synthesis uses a two-stage pipeline. Stage A: the generator with type-conditioned prompting produces candidate problems: 'Generate a problem where the solver must [operation associated with error type] in a context where [error-triggering pattern] is likely to cause mistakes.' Budget allocation is proportional to weakness distribution w, following SwS's category-proportional allocation principle. Stage B: error-type-validated rejection sampling—the generator attempts each candidate (4 rollouts), the PRM diagnoses the solutions, and we retain only candidates where at least one solution triggers the intended error type (confirmed by PRM classification). This rejection sampling oracle IS the PRM itself, ensuring generated problems actually target intended weaknesses rather than merely sharing topic labels. We apply Prism-style ZPD gating (retaining problems with 25–75% solvability) to avoid gradient-vanishing extremes.\\n\\n(3) TRAIN GENERATOR: GRPO with outcome-level rewards (Math-Verify for answer correctness) on the error-type-targeted curriculum, augmented with a diversity buffer of problems from underrepresented error types (inspired by Prism's rarity bonus). Standard GRPO handles implicit step-level credit assignment per Sullivan & Koller (2025). We do NOT use explicit PRM rewards for GRPO, cleanly separating the PRM's diagnostic role from the training objective.\\n\\n(4) UPDATE DIAGNOSTICIAN: The PRM is retrained on the generator's new trajectories, exposing it to novel error patterns at the generator's current capability frontier. This mirrors R-Zero's frozen-partner scheme: during generator training the PRM is frozen; during PRM update the generator is frozen.\\n\\nWe run 4–5 iterations, tracking three key dynamics: (a) generator accuracy on MATH-500/AMC/AIME, (b) PRM diagnostic quality on ProcessBench/PRMBench, (c) error-type distribution shift per iteration (our primary analytical contribution—showing how the curriculum automatically adapts as weaknesses evolve). We compare against four baselines: (i) R-Zero-style uncertainty-based co-evolution (scalar difficulty, no error types), (ii) SwS-style concept-level weakness synthesis (single round), (iii) R-Zero + Prism diversity preservation (geographic diversity, no error diagnosis), (iv) static-taxonomy ablation (fixed error types, no PRM co-evolution). Key ablations: error-type-guided vs. concept-level vs. random problem allocation; PRM co-evolution vs. frozen PRM; data-driven taxonomy expansion vs. fixed 5-type taxonomy; number of rejection sampling rollouts.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~3200 (5 iterations × ~350h generator-GRPO + ~100h PRM-SFT + ~80h rejection-sampling problem generation/validation, plus 4 baselines × ~300h each, plus ablations)\",\n      \"timeline\": \"10–14 weeks (sequential iteration dependency: ~2 weeks per co-evolution cycle, plus 2–3 weeks for baselines and writing)\",\n      \"estimated_gpu_cost\": \"$6,400 (A100-80GB at ~$2/GPU-hr cloud spot pricing)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~2700 (Claude-assisted hyperparameter sweep and error taxonomy refinement reduce wasted runs by ~15%)\",\n      \"timeline\": \"8–10 weeks\",\n      \"claude_api_cost\": \"$700–$1,000 (experiment orchestration, error-distribution analysis, taxonomy refinement, ablation design)\",\n      \"estimated_gpu_cost\": \"$5,400\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~3800 (broader ablations: taxonomy granularity, rejection sampling budget, top-K sweep, iteration count, PRM co-evolution frequency, model scale)\",\n      \"timeline\": \"6–8 weeks (max parallelism within iterations, automated analysis between)\",\n      \"claude_api_cost\": \"$1,400–$2,000 (full pipeline orchestration, paper drafting assistance)\",\n      \"estimated_gpu_cost\": \"$7,600\",\n      \"speed_bottleneck\": \"Sequential iteration dependency—each cycle's curriculum depends on previous cycle's error distribution; within-iteration parallelism saturates at ~8 A100s for GRPO; rejection sampling adds ~20% overhead per iteration\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (deadline estimated September–October 2026 — primary target with 16–20 weeks runway, comfortable for 5-iteration experiment + analysis)\",\n    \"ICML 2027 (deadline estimated January 2027 — fallback with time for scale-up ablations and additional baselines)\",\n    \"ACL 2027 ARR (deadline estimated February 2027 — alternative venue if NLP-community framing preferred)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025) — primary baseline: concept-level weakness diagnosis, single round\",\n    \"R-Zero: Self-Evolving Reasoning LLM from Zero Data (ICLR 2026) — primary baseline: uncertainty-based challenger-solver co-evolution, pseudo-label degradation\",\n    \"GRPO is Secretly a Process Reward Model (Sullivan & Koller, arXiv 2025 / ICLR 2026 submitted) — motivates separating PRM's diagnostic role from reward computation\",\n    \"Preventing Curriculum Collapse in Self-Evolving Reasoning Systems [Prism] (arXiv 2026) — diversity preservation via embedding clusters, complementary to error-type targeting\",\n    \"From Blind Spots to Gains: Diagnostic-Driven Iterative Training for Large Multimodal Models [DPE] (arXiv 2026) — closest structural parallel in multimodal domain, coarse diagnosis\",\n    \"Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution (arXiv 2026) — random diversity injection, complementary mechanism\",\n    \"Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling (arXiv 2026) — auto-derived error taxonomy for reward modeling, inspires dynamic taxonomy\",\n    \"CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution (ACL 2026)\",\n    \"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision [PathFinder-PRM] (arXiv 2025)\",\n    \"Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)\",\n    \"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning (NeurIPS 2025)\",\n    \"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning (arXiv 2025)\",\n    \"Adversarial Training for Process Reward Models [APRM] (arXiv 2025)\",\n    \"Efficient Reinforcement Finetuning via Adaptive Curriculum Learning [AdaRFT] (arXiv 2025)\",\n    \"Your Reward Function for RL is Your Best PRM for Search: Unifying RL and Search-Based TTS [AIRL-S] (arXiv 2025)\",\n    \"Hide and Seek with LLMs: An Adversarial Game for Sneaky Error Generation and Self-Improving Diagnosis (arXiv 2025)\",\n    \"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)\",\n    \"R-PRM (NJUNLP 2025) — best open-source PRM with fine-grained error category labels\"\n  ],\n  \"description\": \"We propose Diagnostic Co-Evolution (DiagCoEvo), a framework that repositions the process reward model from a training reward signal to a co-evolving diagnostic instrument for curriculum guidance. Motivated by the finding that GRPO already performs implicit step-level credit assignment (Sullivan & Koller 2025), we cleanly separate concerns: GRPO with outcome rewards handles generator training, while the PRM's unique value lies in classifying step-level reasoning failures into an evolving error taxonomy (Mathematical-Computation, Logical-Consistency, Conceptual-Gap, Strategy-Selection, Hallucination) that drives targeted problem generation. Each iteration executes: (1) DIAGNOSE—PRM evaluates generator solutions, producing an error-type weakness distribution and extracting error-triggering contexts; (2) GENERATE—type-conditioned prompting produces candidate problems with budget proportional to the weakness distribution, then error-type-validated rejection sampling (using the PRM as oracle) retains only candidates that actually trigger intended error types, combined with ZPD-gating for difficulty calibration; (3) TRAIN—GRPO with outcome rewards on the targeted curriculum plus a Prism-inspired diversity buffer; (4) UPDATE—PRM retrained on the generator's new trajectories, improving its diagnostic capability for the next cycle. This addresses key limitations of existing self-improvement methods: SwS (NeurIPS 2025) diagnoses at concept level and cannot distinguish failures sharing the same topic but differing in error pattern; R-Zero (ICLR 2026) targets scalar difficulty without error structure, and its pseudo-labels degrade from 79% to 63% across iterations; Prism (2026) ensures geographic diversity in embedding space but not diagnostic diversity. Our primary empirical contribution is demonstrating that error-type-level curriculum targeting yields more efficient improvement than concept-level (SwS), uncertainty-level (R-Zero), or diversity-level (Prism) signals, and that PRM diagnostic quality compounds across co-evolution iterations. We evaluate on Qwen3-8B across MATH-500/AMC/AIME, comparing against R-Zero, SwS, and Prism-augmented baselines over 4–5 iterations, with detailed analysis of error-type distribution dynamics.\",\n  \"project_name\": \"prm_diag_adaptive_curriculum\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"issue_1_SwS\": \"ADDRESSED (major). SwS is now a primary baseline throughout the landscape, approach, and baselines. We position against it explicitly: SwS diagnoses at concept level (topic extraction from failed problems) while DiagCoEvo diagnoses at error-type level (step-level failure classification via PRM). SwS cannot distinguish between failures sharing the same concept but differing in error pattern—e.g., two algebra failures, one from sign errors and one from conceptual misunderstanding, receive the same concept-recombination treatment. SwS is also single-round, while we iterate with a co-evolving diagnostician.\",\n    \"issue_2_RZero\": \"ADDRESSED (major). R-Zero is now a primary baseline. We position against its uncertainty-based curriculum: R-Zero targets p̂ ≈ 0.5 (scalar difficulty), which is uninformative about what type of error the model makes. Additionally, R-Zero's pseudo-labels degrade from 79% to 63% across iterations—our PRM provides more reliable step-level verification. The frozen-partner training scheme from R-Zero is adopted for our co-evolution loop.\",\n    \"issue_3_Prism\": \"ADDRESSED. Prism is integrated as both a competitor and an inspiration. Its embedding-diversity preservation is complementary to our error-type targeting: we adopt its ZPD-gating principle and add a Prism-inspired diversity buffer. We compare against R-Zero + Prism as a combined baseline to isolate the value of error-type guidance beyond diversity preservation.\",\n    \"issue_4_DPE\": \"ADDRESSED. DPE is discussed as the closest structural parallel. Key differentiators: DPE uses 12 coarse capability dimensions with 4 external frontier LLMs and no verifier co-evolution; we use fine-grained step-level PRM error taxonomy with a single co-evolving diagnostician. DPE is multimodal-focused; we target mathematical reasoning.\",\n    \"issue_5_VocabDropout\": \"ADDRESSED. Vocabulary Dropout is discussed as a complementary diversity mechanism—blind random diversity vs. our targeted diagnostic diversity. Our approach is informed (error-type-driven) while VocabDropout is uninformed (random token masking).\",\n    \"issue_6_Rubrics\": \"ADDRESSED. Data-Driven Reasoning Rubrics inspires our dynamic taxonomy design. We adopt the principle of data-driven rubric extraction to augment our seed taxonomy, but critically extend it with iteration (rubrics update each cycle) and curriculum design (rubrics guide problem generation, not just evaluation).\",\n    \"issue_7_GRPO_PRM\": \"ADDRESSED (major repositioning). This is the most significant change. We now explicitly separate PRM roles: GRPO with outcome rewards handles generator training (the implicit PRM handles credit assignment per Sullivan & Koller 2025). The explicit PRM serves exclusively as a diagnostic instrument for curriculum guidance—classifying error types and validating that generated problems target intended weaknesses. This cleanly addresses the challenge while clarifying the PRM's unique value proposition.\",\n    \"issue_8_venue_timeline\": \"ADDRESSED. AAAI 2027 and EACL ARR removed as primary targets. ICLR 2027 (est. Sep-Oct 2026) is now the primary target with 16-20 weeks runway. ICML 2027 and ACL 2027 ARR are fallbacks.\",\n    \"issue_9_problem_generation\": \"ADDRESSED (major specification). The targeted problem generation mechanism is now concrete: (a) error-triggering contexts extracted from diagnosed failures, (b) type-conditioned prompting with specific templates, (c) error-type-validated rejection sampling where the PRM serves as the oracle—candidates are retained only if the generator's attempts on them trigger the intended error type as classified by the PRM. This closes the specification gap.\",\n    \"issue_10_justification\": \"ADDRESSED. Explicit argument provided: concept-level (SwS) conflates failures with different causes under shared topics; scalar uncertainty (R-Zero) provides no information about error structure; embedding diversity (Prism) ensures geographic but not diagnostic coverage. Error-type taxonomy uniquely captures WHY the model fails, enabling targeted remediation strategies. The argument is strengthened by the Rubrics paper's finding that structured error taxonomy improves reward modeling by +45% over generic judges.\"\n  }\n}\n\n## Reviewer feedback (round 2)\nIssues: [\"MISSING COMPETITORS (moderate): Socratic-Zero (Sep 2025, +20.2pp) implements Teacher-Solver-Generator co-evolution where the Teacher adaptively targets solver weaknesses — structurally very close to DiagCoEvo's diagnose→generate loop, though without formal error taxonomy. Must be in the landscape.\", \"MISSING COMPETITORS (moderate): SAGE (March 2026) implements 4-agent co-evolution (Challenger/Planner/Solver/Critic) with Critic-based quality control — directly comparable co-evolution framework. WarriorMath (Aug 2025) implements defect-aware targeted problem synthesis with iterative fine-tuning on model-specific weaknesses — close parallel to the propose→target→retrain loop.\", \"MISSING COMPETITORS (minor): LEMMA (ACL 2025) uses error-type-grounded mistake augmentation for self-correction; Error Classification of LLMs on MWP (EMNLP 2025 Findings) proposes dynamic adaptive error classification + Error-Aware Prompting; Bidirectional Curriculum (March 2026) simplifies problems to repair specific reasoning failures; VHG (May 2026) uses verifier-backed three-party self-play; Cog-DRIFT (April 2026) adaptively reformulates hard problems.\", \"TYPE-CONDITIONED PROMPTING FEASIBILITY: The entire curriculum targeting hinges on reliably generating problems that trigger specific error types via prompting. No evidence is provided for expected success rates. If the yield before rejection sampling is <10%, the 4-rollout validation budget (per candidate) may be insufficient, and the computational overhead of generating enough valid candidates could be prohibitive. A pilot study or concrete analysis of expected yields is needed.\", \"TAXONOMY EXPANSION UNDERSPECIFIED: The proposal mentions a 'dynamic, expandable taxonomy' but never specifies the expansion mechanism. How are new error types detected? What triggers a split vs. merge? How do you prevent taxonomy explosion across iterations? This is a claimed contribution that lacks specification.\", \"PRM GENERALIZATION RISK: PathFinder-PRM's taxonomy (Math/Consistency/Optimality) was developed on Mistral traces + PRM800K. Applying this to Qwen3-8B may face distribution shift — error patterns are often model-specific. The proposal should discuss adaptation strategy or cold-start risks for the diagnostician.\", \"'GRPO is Secretly a PRM' STATUS: The proposal cites this as 'ICLR 2026 submitted' but at least one OpenReview submission (iRWqcnBlLQ) was withdrawn. Should be cited as arXiv preprint with status noted accurately.\", \"CROWDED FIELD DIFFERENTIATION: With 10+ papers on co-evolutionary self-improvement for reasoning published in the last 12 months, the paper needs to demonstrate not just that error-type targeting works, but that it provides SUBSTANTIALLY better results than simpler approaches. The bar for a meaningful contribution at ICLR 2027 is very high in this specific sub-area.\"]\nFeedback: The revision substantially improved the proposal — all 10 round-1 issues were systematically addressed, the PRM-as-diagnostician framing is clean, and the positioning against R-Zero/SwS/Prism is now explicit. However, three areas still need work: (1) **Landscape completeness**: Add Socratic-Zero, SAGE, WarriorMath, LEMMA, and Error Classification of LLMs on MWP to the landscape — these are structurally adjacent and reviewers will know them. For each, provide the clear differentiator (e.g., Socratic-Zero targets weaknesses generically without error taxonomy; WarriorMath does defect-aware synthesis but without PRM co-evolution or error-type diagnosis). (2) **Type-conditioned prompting validation**: This is the highest-risk component. Provide either: (a) a concrete analysis of expected success rates based on preliminary experiments, or (b) a fallback strategy if yield is too low (e.g., using the PRM's error-triggering context extraction to directly mutate existing problems rather than generate from scratch). Consider the Self-Error-Instruct approach of clustering error keyphrases and sampling from clusters as an alternative generation strategy. (3) **Taxonomy expansion**: Specify the mechanism — e.g., apply clustering (as in Data-Driven Rubrics) to the PRM's error descriptions each iteration, merge clusters below a threshold, split clusters with high internal variance. This is a claimed contribution and needs concrete specification. Minor: fix the GRPO-PRM citation status, and consider whether the SEC paper's MAB-based curriculum approach provides a useful comparison (automatic category selection vs. your error-type-proportional allocation).\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:28:30.909Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:28:30.909Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-28T05:28:30.956Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
{
  "title": "Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diagnostic Co-Evolution",
  "core_problem": "Can a PRM serving as a co-evolving diagnostic instrument—classifying step-level reasoning failures into an evolving error taxonomy—drive a more targeted curriculum than concept-level weakness extraction (SwS), scalar uncertainty targeting (R-Zero), or embedding-diversity coverage (Prism), and does the diagnostician's own improvement across iterations compound the generator's gains?",
  "opportunity": "Self-improving reasoning loops have proliferated rapidly: SwS (NeurIPS 2025) demonstrates 10%/7.7% gains via concept-level weakness-driven problem synthesis; R-Zero (ICLR 2026) achieves +6.49 via uncertainty-based challenger-solver co-evolution; Prism (March 2026) adds +3.98 over R-Zero via embedding-diversity preservation. Yet all three diagnose weaknesses at fundamentally coarse granularity—SwS extracts topic-level concepts from failed problems (e.g., 'modular arithmetic'), R-Zero targets scalar difficulty (p̂ ≈ 0.5), and Prism ensures geographic coverage in embedding space. None examines WHY the model fails at the reasoning-step level. Meanwhile, PathFinder-PRM (May 2025) classifies step-level errors into types (Mathematical/Consistency/Optimality) but uses this only for PRM training; Data-Driven Reasoning Rubrics (Feb 2026) derives error taxonomies from model failures but applies them statically for reward modeling without curriculum design; and DPE (Feb 2026) implements diagnose→generate→retrain for multimodal models but uses 12 coarse capability dimensions with external frontier LLMs and no verifier co-evolution. The untapped synthesis: use a PRM as a co-evolving diagnostic instrument whose step-level error-type classifications drive targeted problem generation, where the PRM itself improves as it encounters the generator's evolving failure modes. Two problems may share the same concept (algebra) and difficulty level yet fail for completely different reasons (sign error vs. conceptual misunderstanding)—only step-level error-type diagnosis can distinguish these and generate appropriately targeted remediation.",
  "landscape": "SwS (NeurIPS 2025) achieves 10%/7.7% average gains (Qwen2.5-7B/32B) via outcome-level weakness identification (max accuracy <50% + negative slope) → concept extraction → concept recombination → filtered problem generation; however, it is single-round, uses no PRM, and cannot distinguish between failures sharing the same topic but differing in error pattern. R-Zero (ICLR 2026) achieves +6.49 (Qwen3-4B) via GRPO-trained challenger targeting p̂ = 0.5 uncertainty, but pseudo-label accuracy degrades from 79% to 63% across iterations and the curriculum signal is purely scalar difficulty. Prism (March 2026) addresses R-Zero's diversity collapse via embedding-cluster-based rarity bonuses (+3.98 AMC), but diversity is geometric rather than diagnostic. Vocabulary Dropout (April 2026) injects random token-mask diversity into R-Zero-style co-evolution (+4.4 avg on Qwen3-8B) but is blind to what kinds of diversity benefit the solver. DPE (Feb 2026, arXiv 2602.22859) implements diagnose→generate→retrain for multimodal LLMs using 12 coarse capability dimensions and 4 frontier LLMs, achieving 8B-surpassing-72B performance but without PRM, step-level analysis, or verifier co-evolution. Data-Driven Reasoning Rubrics (Feb 2026) derives error taxonomies from model failures for domain-adaptive reward modeling (+45% task accuracy over LLM-as-judge) but generates rubrics once without iteration or curriculum design. 'GRPO is Secretly a PRM' (Sep 2025, Saarland University) proves GRPO implicitly performs step-level credit assignment via Monte Carlo estimates from shared token prefixes; lambda-GRPO achieves >10% faster convergence. This challenges explicit PRMs for reward computation but not for structured error diagnosis—the implicit PRM's 'steps' are token-prefix-based, not semantically meaningful error classifications. CoVerRL (ACL 2026) demonstrates generator-verifier co-evolution with 4.7–5.9% gains but uses undirected majority voting. PathFinder-PRM (May 2025) achieves SOTA 67.7 PRMScore with error-aware hierarchical supervision but does not use error types for curriculum. R-PRM (NJUNLP 2025) achieves best open-source PRM with fine-grained error categories but does not leverage them for curriculum. APRM (Nov 2025) creates adversarial PRM curriculum (+3.4pp solver accuracy) but targets PRM robustness only. RL Tango (NeurIPS 2025) co-trains generator and generative verifier via RL but uses outcome-level rewards. AdaRFT (Apr 2025) adapts curriculum on scalar difficulty only (2× speedup). Self-Error-Instruct (ACL 2025) clusters error types for targeted data but uses GPT-4o and doesn't iterate. HSG Hide-and-Seek (Aug 2025) uses adversarial error generation to improve diagnosis by 16.8–31.4% but doesn't close the loop to generator improvement. No existing work combines: (a) step-level PRM error-type classification, (b) error-type-driven targeted problem generation with validated type targeting, (c) iterative co-evolution where the diagnostic instrument itself improves.",
  "inspired_by": "SwS (NeurIPS 2025) validates weakness-driven synthesis but at concept level; R-Zero (ICLR 2026) validates co-evolutionary self-improvement but with scalar uncertainty; Prism (2026) validates diversity-aware curriculum but with geographic rather than diagnostic diversity; Data-Driven Reasoning Rubrics (2026) validates auto-derived error taxonomies for reward modeling but without iteration or curriculum; 'GRPO is Secretly a PRM' (2025) establishes that GRPO handles implicit credit assignment, clarifying the PRM's unique value as diagnostic instrument rather than reward signal. Field guide Gap 7 (iterative self-improvement loops), Gap 4 (dynamic co-evolution).",
  "approach": "We propose Diagnostic Co-Evolution (DiagCoEvo): a framework where a PRM serves as a co-evolving diagnostic instrument whose step-level error-type classifications drive targeted curriculum generation, while GRPO with standard outcome rewards handles generator training (following the 'GRPO is Secretly a PRM' insight that explicit PRM rewards for GRPO are unnecessary). We initialize generator and PRM from Qwen3-8B. The PRM is trained using PathFinder-PRM's hierarchical error taxonomy as a seed, augmented with data-driven rubric extraction (inspired by Sanders et al. 2026) to produce a dynamic, expandable taxonomy initialized with five core types (Mathematical-Computation, Logical-Consistency, Conceptual-Gap, Strategy-Selection, Hallucination). Each co-evolution iteration executes a four-phase cycle:\n\n(1) DIAGNOSE: The PRM evaluates the generator's solutions on a held-out problem bank (2K problems, 8 solutions each), classifying each incorrect step's error type to produce a weakness distribution w = {w_1, ..., w_K} over error types. We also extract 'error-triggering contexts'—the problem features and reasoning patterns most frequently associated with each error type.\n\n(2) GENERATE: Targeted problem synthesis uses a two-stage pipeline. Stage A: the generator with type-conditioned prompting produces candidate problems: 'Generate a problem where the solver must [operation associated with error type] in a context where [error-triggering pattern] is likely to cause mistakes.' Budget allocation is proportional to weakness distribution w, following SwS's category-proportional allocation principle. Stage B: error-type-validated rejection sampling—the generator attempts each candidate (4 rollouts), the PRM diagnoses the solutions, and we retain only candidates where at least one solution triggers the intended error type (confirmed by PRM classification). This rejection sampling oracle IS the PRM itself, ensuring generated problems actually target intended weaknesses rather than merely sharing topic labels. We apply Prism-style ZPD gating (retaining problems with 25–75% solvability) to avoid gradient-vanishing extremes.\n\n(3) TRAIN GENERATOR: GRPO with outcome-level rewards (Math-Verify for answer correctness) on the error-type-targeted curriculum, augmented with a diversity buffer of problems from underrepresented error types (inspired by Prism's rarity bonus). Standard GRPO handles implicit step-level credit assignment per Sullivan & Koller (2025). We do NOT use explicit PRM rewards for GRPO, cleanly separating the PRM's diagnostic role from the training objective.\n\n(4) UPDATE DIAGNOSTICIAN: The PRM is retrained on the generator's new trajectories, exposing it to novel error patterns at the generator's current capability frontier. This mirrors R-Zero's frozen-partner scheme: during generator training the PRM is frozen; during PRM update the generator is frozen.\n\nWe run 4–5 iterations, tracking three key dynamics: (a) generator accuracy on MATH-500/AMC/AIME, (b) PRM diagnostic quality on ProcessBench/PRMBench, (c) error-type distribution shift per iteration (our primary analytical contribution—showing how the curriculum automatically adapts as weaknesses evolve). We compare against four baselines: (i) R-Zero-style uncertainty-based co-evolution (scalar difficulty, no error types), (ii) SwS-style concept-level weakness synthesis (single round), (iii) R-Zero + Prism diversity preservation (geographic diversity, no error diagnosis), (iv) static-taxonomy ablation (fixed error types, no PRM co-evolution). Key ablations: error-type-guided vs. concept-level vs. random problem allocation; PRM co-evolution vs. frozen PRM; data-driven taxonomy expansion vs. fixed 5-type taxonomy; number of rejection sampling rollouts.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~3200 (5 iterations × ~350h generator-GRPO + ~100h PRM-SFT + ~80h rejection-sampling problem generation/validation, plus 4 baselines × ~300h each, plus ablations)",
      "timeline": "10–14 weeks (sequential iteration dependency: ~2 weeks per co-evolution cycle, plus 2–3 weeks for baselines and writing)",
      "estimated_gpu_cost": "$6,400 (A100-80GB at ~$2/GPU-hr cloud spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "~2700 (Claude-assisted hyperparameter sweep and error taxonomy refinement reduce wasted runs by ~15%)",
      "timeline": "8–10 weeks",
      "claude_api_cost": "$700–$1,000 (experiment orchestration, error-distribution analysis, taxonomy refinement, ablation design)",
      "estimated_gpu_cost": "$5,400"
    },
    "auto_research": {
      "gpu_hours": "~3800 (broader ablations: taxonomy granularity, rejection sampling budget, top-K sweep, iteration count, PRM co-evolution frequency, model scale)",
      "timeline": "6–8 weeks (max parallelism within iterations, automated analysis between)",
      "claude_api_cost": "$1,400–$2,000 (full pipeline orchestration, paper drafting assistance)",
      "estimated_gpu_cost": "$7,600",
      "speed_bottleneck": "Sequential iteration dependency—each cycle's curriculum depends on previous cycle's error distribution; within-iteration parallelism saturates at ~8 A100s for GRPO; rejection sampling adds ~20% overhead per iteration"
    }
  },
  "target_venues": [
    "ICLR 2027 (deadline estimated September–October 2026 — primary target with 16–20 weeks runway, comfortable for 5-iteration experiment + analysis)",
    "ICML 2027 (deadline estimated January 2027 — fallback with time for scale-up ablations and additional baselines)",
    "ACL 2027 ARR (deadline estimated February 2027 — alternative venue if NLP-community framing preferred)"
  ],
  "level": "solid",
  "key_references": [
    "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025) — primary baseline: concept-level weakness diagnosis, single round",
    "R-Zero: Self-Evolving Reasoning LLM from Zero Data (ICLR 2026) — primary baseline: uncertainty-based challenger-solver co-evolution, pseudo-label degradation",
    "GRPO is Secretly a Process Reward Model (Sullivan & Koller, arXiv 2025 / ICLR 2026 submitted) — motivates separating PRM's diagnostic role from reward computation",
    "Preventing Curriculum Collapse in Self-Evolving Reasoning Systems [Prism] (arXiv 2026) — diversity preservation via embedding clusters, complementary to error-type targeting",
    "From Blind Spots to Gains: Diagnostic-Driven Iterative Training for Large Multimodal Models [DPE] (arXiv 2026) — closest structural parallel in multimodal domain, coarse diagnosis",
    "Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution (arXiv 2026) — random diversity injection, complementary mechanism",
    "Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling (arXiv 2026) — auto-derived error taxonomy for reward modeling, inspires dynamic taxonomy",
    "CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution (ACL 2026)",
    "Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision [PathFinder-PRM] (arXiv 2025)",
    "Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)",
    "RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning (NeurIPS 2025)",
    "SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning (arXiv 2025)",
    "Adversarial Training for Process Reward Models [APRM] (arXiv 2025)",
    "Efficient Reinforcement Finetuning via Adaptive Curriculum Learning [AdaRFT] (arXiv 2025)",
    "Your Reward Function for RL is Your Best PRM for Search: Unifying RL and Search-Based TTS [AIRL-S] (arXiv 2025)",
    "Hide and Seek with LLMs: An Adversarial Game for Sneaky Error Generation and Self-Improving Diagnosis (arXiv 2025)",
    "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)",
    "R-PRM (NJUNLP 2025) — best open-source PRM with fine-grained error category labels"
  ],
  "description": "We propose Diagnostic Co-Evolution (DiagCoEvo), a framework that repositions the process reward model from a training reward signal to a co-evolving diagnostic instrument for curriculum guidance. Motivated by the finding that GRPO already performs implicit step-level credit assignment (Sullivan & Koller 2025), we cleanly separate concerns: GRPO with outcome rewards handles generator training, while the PRM's unique value lies in classifying step-level reasoning failures into an evolving error taxonomy (Mathematical-Computation, Logical-Consistency, Conceptual-Gap, Strategy-Selection, Hallucination) that drives targeted problem generation. Each iteration executes: (1) DIAGNOSE—PRM evaluates generator solutions, producing an error-type weakness distribution and extracting error-triggering contexts; (2) GENERATE—type-conditioned prompting produces candidate problems with budget proportional to the weakness distribution, then error-type-validated rejection sampling (using the PRM as oracle) retains only candidates that actually trigger intended error types, combined with ZPD-gating for difficulty calibration; (3) TRAIN—GRPO with outcome rewards on the targeted curriculum plus a Prism-inspired diversity buffer; (4) UPDATE—PRM retrained on the generator's new trajectories, improving its diagnostic capability for the next cycle. This addresses key limitations of existing self-improvement methods: SwS (NeurIPS 2025) diagnoses at concept level and cannot distinguish failures sharing the same topic but differing in error pattern; R-Zero (ICLR 2026) targets scalar difficulty without error structure, and its pseudo-labels degrade from 79% to 63% across iterations; Prism (2026) ensures geographic diversity in embedding space but not diagnostic diversity. Our primary empirical contribution is demonstrating that error-type-level curriculum targeting yields more efficient improvement than concept-level (SwS), uncertainty-level (R-Zero), or diversity-level (Prism) signals, and that PRM diagnostic quality compounds across co-evolution iterations. We evaluate on Qwen3-8B across MATH-500/AMC/AIME, comparing against R-Zero, SwS, and Prism-augmented baselines over 4–5 iterations, with detailed analysis of error-type distribution dynamics.",
  "project_name": "prm_diag_adaptive_curriculum",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_SwS": "ADDRESSED (major). SwS is now a primary baseline throughout the landscape, approach, and baselines. We position against it explicitly: SwS diagnoses at concept level (topic extraction from failed problems) while DiagCoEvo diagnoses at error-type level (step-level failure classification via PRM). SwS cannot distinguish between failures sharing the same concept but differing in error pattern—e.g., two algebra failures, one from sign errors and one from conceptual misunderstanding, receive the same concept-recombination treatment. SwS is also single-round, while we iterate with a co-evolving diagnostician.",
    "issue_2_RZero": "ADDRESSED (major). R-Zero is now a primary baseline. We position against its uncertainty-based curriculum: R-Zero targets p̂ ≈ 0.5 (scalar difficulty), which is uninformative about what type of error the model makes. Additionally, R-Zero's pseudo-labels degrade from 79% to 63% across iterations—our PRM provides more reliable step-level verification. The frozen-partner training scheme from R-Zero is adopted for our co-evolution loop.",
    "issue_3_Prism": "ADDRESSED. Prism is integrated as both a competitor and an inspiration. Its embedding-diversity preservation is complementary to our error-type targeting: we adopt its ZPD-gating principle and add a Prism-inspired diversity buffer. We compare against R-Zero + Prism as a combined baseline to isolate the value of error-type guidance beyond diversity preservation.",
    "issue_4_DPE": "ADDRESSED. DPE is discussed as the closest structural parallel. Key differentiators: DPE uses 12 coarse capability dimensions with 4 external frontier LLMs and no verifier co-evolution; we use fine-grained step-level PRM error taxonomy with a single co-evolving diagnostician. DPE is multimodal-focused; we target mathematical reasoning.",
    "issue_5_VocabDropout": "ADDRESSED. Vocabulary Dropout is discussed as a complementary diversity mechanism—blind random diversity vs. our targeted diagnostic diversity. Our approach is informed (error-type-driven) while VocabDropout is uninformed (random token masking).",
    "issue_6_Rubrics": "ADDRESSED. Data-Driven Reasoning Rubrics inspires our dynamic taxonomy design. We adopt the principle of data-driven rubric extraction to augment our seed taxonomy, but critically extend it with iteration (rubrics update each cycle) and curriculum design (rubrics guide problem generation, not just evaluation).",
    "issue_7_GRPO_PRM": "ADDRESSED (major repositioning). This is the most significant change. We now explicitly separate PRM roles: GRPO with outcome rewards handles generator training (the implicit PRM handles credit assignment per Sullivan & Koller 2025). The explicit PRM serves exclusively as a diagnostic instrument for curriculum guidance—classifying error types and validating that generated problems target intended weaknesses. This cleanly addresses the challenge while clarifying the PRM's unique value proposition.",
    "issue_8_venue_timeline": "ADDRESSED. AAAI 2027 and EACL ARR removed as primary targets. ICLR 2027 (est. Sep-Oct 2026) is now the primary target with 16-20 weeks runway. ICML 2027 and ACL 2027 ARR are fallbacks.",
    "issue_9_problem_generation": "ADDRESSED (major specification). The targeted problem generation mechanism is now concrete: (a) error-triggering contexts extracted from diagnosed failures, (b) type-conditioned prompting with specific templates, (c) error-type-validated rejection sampling where the PRM serves as the oracle—candidates are retained only if the generator's attempts on them trigger the intended error type as classified by the PRM. This closes the specification gap.",
    "issue_10_justification": "ADDRESSED. Explicit argument provided: concept-level (SwS) conflates failures with different causes under shared topics; scalar uncertainty (R-Zero) provides no information about error structure; embedding diversity (Prism) ensures geographic but not diagnostic coverage. Error-type taxonomy uniquely captures WHY the model fails, enabling targeted remediation strategies. The argument is strengthened by the Rubrics paper's finding that structured error taxonomy improves reward modeling by +45% over generic judges."
  }
}

## Reviewer feedback (round 2)
Issues: ["MISSING COMPETITORS (moderate): Socratic-Zero (Sep 2025, +20.2pp) implements Teacher-Solver-Generator co-evolution where the Teacher adaptively targets solver weaknesses — structurally very close to DiagCoEvo's diagnose→generate loop, though without formal error taxonomy. Must be in the landscape.", "MISSING COMPETITORS (moderate): SAGE (March 2026) implements 4-agent co-evolution (Challenger/Planner/Solver/Critic) with Critic-based quality control — directly comparable co-evolution framework. WarriorMath (Aug 2025) implements defect-aware targeted problem synthesis with iterative fine-tuning on model-specific weaknesses — close parallel to the propose→target→retrain loop.", "MISSING COMPETITORS (minor): LEMMA (ACL 2025) uses error-type-grounded mistake augmentation for self-correction; Error Classification of LLMs on MWP (EMNLP 2025 Findings) proposes dynamic adaptive error classification + Error-Aware Prompting; Bidirectional Curriculum (March 2026) simplifies problems to repair specific reasoning failures; VHG (May 2026) uses verifier-backed three-party self-play; Cog-DRIFT (April 2026) adaptively reformulates hard problems.", "TYPE-CONDITIONED PROMPTING FEASIBILITY: The entire curriculum targeting hinges on reliably generating problems that trigger specific error types via prompting. No evidence is provided for expected success rates. If the yield before rejection sampling is <10%, the 4-rollout validation budget (per candidate) may be insufficient, and the computational overhead of generating enough valid candidates could be prohibitive. A pilot study or concrete analysis of expected yields is needed.", "TAXONOMY EXPANSION UNDERSPECIFIED: The proposal mentions a 'dynamic, expandable taxonomy' but never specifies the expansion mechanism. How are new error types detected? What triggers a split vs. merge? How do you prevent taxonomy explosion across iterations? This is a claimed contribution that lacks specification.", "PRM GENERALIZATION RISK: PathFinder-PRM's taxonomy (Math/Consistency/Optimality) was developed on Mistral traces + PRM800K. Applying this to Qwen3-8B may face distribution shift — error patterns are often model-specific. The proposal should discuss adaptation strategy or cold-start risks for the diagnostician.", "'GRPO is Secretly a PRM' STATUS: The proposal cites this as 'ICLR 2026 submitted' but at least one OpenReview submission (iRWqcnBlLQ) was withdrawn. Should be cited as arXiv preprint with status noted accurately.", "CROWDED FIELD DIFFERENTIATION: With 10+ papers on co-evolutionary self-improvement for reasoning published in the last 12 months, the paper needs to demonstrate not just that error-type targeting works, but that it provides SUBSTANTIALLY better results than simpler approaches. The bar for a meaningful contribution at ICLR 2027 is very high in this specific sub-area."]
Feedback: The revision substantially improved the proposal — all 10 round-1 issues were systematically addressed, the PRM-as-diagnostician framing is clean, and the positioning against R-Zero/SwS/Prism is now explicit. However, three areas still need work: (1) **Landscape completeness**: Add Socratic-Zero, SAGE, WarriorMath, LEMMA, and Error Classification of LLMs on MWP to the landscape — these are structurally adjacent and reviewers will know them. For each, provide the clear differentiator (e.g., Socratic-Zero targets weaknesses generically without error taxonomy; WarriorMath does defect-aware synthesis but without PRM co-evolution or error-type diagnosis). (2) **Type-conditioned prompting validation**: This is the highest-risk component. Provide either: (a) a concrete analysis of expected success rates based on preliminary experiments, or (b) a fallback strategy if yield is too low (e.g., using the PRM's error-triggering context extraction to directly mutate existing problems rather than generate from scratch). Consider the Self-Error-Instruct approach of clustering error keyphrases and sampling from clusters as an alternative generation strategy. (3) **Taxonomy expansion**: Specify the mechanism — e.g., apply clustering (as in Data-Driven Rubrics) to the PRM's error descriptions each iteration, merge clusters below a threshold, split clusters with high internal variance. This is a claimed contribution and needs concrete specification. Minor: fix the GRPO-PRM citation status, and consider whether the SEC paper's MAB-based curriculum approach provides a useful comparison (automatic category selection vs. your error-type-proportional allocation).

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
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "9c095a55-29bc-45de-866a-3808b8ab556c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:28:30.954Z_

```json
{
  "parentUuid": "9c095a55-29bc-45de-866a-3808b8ab556c",
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
  "uuid": "b75f1ca2-2ee6-4421-becf-0df088d14d42",
  "timestamp": "2026-05-28T05:28:30.954Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:28:30.954Z_

```json
{
  "parentUuid": "b75f1ca2-2ee6-4421-becf-0df088d14d42",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2030c0af-e114-48ae-a518-c0c7dbc693fb",
  "timestamp": "2026-05-28T05:28:30.954Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "2030c0af-e114-48ae-a518-c0c7dbc693fb",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Assistant

_source line 8 · 2026-05-28T05:28:38.653Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research strategy.

The reviewer has 8 issues:

1. **MISSING COMPETITORS (moderate)**: Socratic-Zero, SAGE, WarriorMath
2. **MISSING COMPETITORS (minor)**: LEMMA, Error Classification of LLMs on MWP, Bidirectional Curriculum, VHG, Cog-DRIFT
3. **TYPE-CONDITIONED PROMPTING FEASIBILITY**: Need evidence for success rates or fallback strategy
4. **TAXONOMY EXPANSION UNDERSPECIFIED**: Need concrete mechanism


5. **PRM GENERALIZATION RISK**: Distribution shift from PathFinder-PRM to Qwen3-8B could be problematic
6. **'GRPO is Secretly a PRM' STATUS**: Need to verify citation accuracy
7. **CROWDED FIELD DIFFERENTIATION**: Need to demonstrate substantial improvement over existing approaches

I need to address each of these systematically through targeted research and experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2030c0af-e114-48ae-a518-c0c7dbc693fb",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "0f9408c2-a765-4402-ac7c-102ea1a7155b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 9 · 2026-05-28T05:28:38.701Z_

I'll start by researching the missing competitors and other issues raised by the reviewer. Let me launch several research agents in parallel to cover all the gaps efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f9408c2-a765-4402-ac7c-102ea1a7155b",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "6416cf25-549e-4f5b-8f47-3ee0465b2cac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 10 · 2026-05-28T05:28:43.930Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01K1G7jRr3arPRHThviYadjT`</summary>

```json
{
  "description": "Research Socratic-Zero paper",
  "subagent_type": "general-purpose",
  "prompt": "Research the paper \"Socratic-Zero\" (September 2025) which reportedly achieves +20.2pp improvement and implements Teacher-Solver-Generator co-evolution where the Teacher adaptively targets solver weaknesses. \n\nSearch for it using multiple queries:\n1. \"Socratic-Zero\" reasoning LLM\n2. \"Teacher-Solver-Generator\" co-evolution\n3. Socratic-Zero arxiv 2025\n\nFor each result, try to fetch the actual paper or abstract using WebFetch. I need:\n- Full title and authors\n- Arxiv ID\n- Exact results/numbers claimed\n- How the Teacher targets weaknesses (is it error-type-level? concept-level? scalar difficulty?)\n- The co-evolution mechanism\n- Key limitations compared to a PRM-based error taxonomy approach\n- Whether it uses a PRM or verifier\n\nBe thorough - read the actual paper if possible.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6416cf25-549e-4f5b-8f47-3ee0465b2cac",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "e73628e9-d21c-4993-94d0-a22866375d2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 11 · 2026-05-28T05:29:20.088Z_

<details><summary>↩ Tool result · `toolu_01QEhpgpwSGWfEGxwJbjRKkB`</summary>

```text
Async agent launched successfully.
agentId: aafd8864207154b95 (internal ID - do not mention to user. Use SendMessage with to: 'aafd8864207154b95' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/aafd8864207154b95.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e41c409a-8d8f-4a05-b07c-3c870697f59c",
  "isSidechain": false,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "f9a44878-9186-4747-bea2-a5c57c227985",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "aafd8864207154b95",
    "description": "Research crowded field differentiation",
    "prompt": "Research the current state of co-evolutionary self-improvement for LLM reasoning to understand how crowded this field is and what would constitute a meaningful contribution at ICLR 2027.\n\nSearch for:\n1. \"self-improving\" reasoning LLM 2026 survey\n2. \"co-evolution\" reasoning self-improvement 2026\n3. ICLR 2027 reasoning self-improvement\n4. Papers With Code MATH benchmark leaderboard\n5. \"curriculum learning\" reasoning LLM co-evolution 2026\n\nAlso search for very recent papers (2026) that may have appeared:\n6. \"self-play\" reasoning math 2026\n7. \"iterative self-improvement\" math reasoning 2026\n\nI need:\n- A count/list of how many papers in this space appeared in the last 12 months\n- What the current SOTA numbers are on MATH-500, AMC, AIME for 7B-8B models\n- What gap sizes (percentage points improvement) are considered significant\n- What kind of contribution (empirical, analytical, methodological) would stand out at ICLR 2027\n- Whether error-type analysis as an analytical contribution (showing how error distributions shift across iterations) would be sufficiently novel\n\nUse WebFetch to check recent papers and leaderboards.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/aafd8864207154b95.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "e41c409a-8d8f-4a05-b07c-3c870697f59c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T05:28:43.942Z_

<details><summary>↩ Tool result · `toolu_01K1G7jRr3arPRHThviYadjT`</summary>

```text
Async agent launched successfully.
agentId: a67b76442fb946591 (internal ID - do not mention to user. Use SendMessage with to: 'a67b76442fb946591' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a67b76442fb946591.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e73628e9-d21c-4993-94d0-a22866375d2b",
  "isSidechain": false,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "e2b47b31-66da-4389-a7a4-2e511dcec070",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a67b76442fb946591",
    "description": "Research Socratic-Zero paper",
    "prompt": "Research the paper \"Socratic-Zero\" (September 2025) which reportedly achieves +20.2pp improvement and implements Teacher-Solver-Generator co-evolution where the Teacher adaptively targets solver weaknesses. \n\nSearch for it using multiple queries:\n1. \"Socratic-Zero\" reasoning LLM\n2. \"Teacher-Solver-Generator\" co-evolution\n3. Socratic-Zero arxiv 2025\n\nFor each result, try to fetch the actual paper or abstract using WebFetch. I need:\n- Full title and authors\n- Arxiv ID\n- Exact results/numbers claimed\n- How the Teacher targets weaknesses (is it error-type-level? concept-level? scalar difficulty?)\n- The co-evolution mechanism\n- Key limitations compared to a PRM-based error taxonomy approach\n- Whether it uses a PRM or verifier\n\nBe thorough - read the actual paper if possible.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a67b76442fb946591.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "e73628e9-d21c-4993-94d0-a22866375d2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T05:28:48.290Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012TPYTvbZTSSJvoR5tpeTdX`</summary>

```json
{
  "description": "Research SAGE and WarriorMath papers",
  "subagent_type": "general-purpose",
  "prompt": "Research two papers:\n\n1. **SAGE (March 2026)**: Implements 4-agent co-evolution (Challenger/Planner/Solver/Critic) with Critic-based quality control. Search for:\n   - \"SAGE\" challenger planner solver critic co-evolution\n   - SAGE 4-agent reasoning math 2026\n   - SAGE arxiv co-evolution LLM reasoning\n\n2. **WarriorMath (August 2025)**: Implements defect-aware targeted problem synthesis with iterative fine-tuning on model-specific weaknesses. Search for:\n   - WarriorMath defect-aware problem synthesis\n   - WarriorMath arxiv 2025\n   - \"WarriorMath\" LLM reasoning\n\nFor each paper, try to fetch the actual paper or abstract using WebFetch. I need:\n- Full title and authors\n- Arxiv ID\n- Exact results/numbers\n- How they diagnose weaknesses (error-type? concept-level? capability dimension?)\n- Co-evolution mechanism details\n- Whether they use a PRM\n- Key limitations vs a PRM-based error taxonomy approach\n\nBe thorough and read the actual papers.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2b47b31-66da-4389-a7a4-2e511dcec070",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "ea423fdb-b3df-45d8-a796-11c81ae0cf0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 14 · 2026-05-28T05:28:48.295Z_

<details><summary>↩ Tool result · `toolu_012TPYTvbZTSSJvoR5tpeTdX`</summary>

```text
Async agent launched successfully.
agentId: a230757a73c93e586 (internal ID - do not mention to user. Use SendMessage with to: 'a230757a73c93e586' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a230757a73c93e586.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea423fdb-b3df-45d8-a796-11c81ae0cf0a",
  "isSidechain": false,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "32627dcf-199a-42b5-bf12-04f6c297521d",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a230757a73c93e586",
    "description": "Research SAGE and WarriorMath papers",
    "prompt": "Research two papers:\n\n1. **SAGE (March 2026)**: Implements 4-agent co-evolution (Challenger/Planner/Solver/Critic) with Critic-based quality control. Search for:\n   - \"SAGE\" challenger planner solver critic co-evolution\n   - SAGE 4-agent reasoning math 2026\n   - SAGE arxiv co-evolution LLM reasoning\n\n2. **WarriorMath (August 2025)**: Implements defect-aware targeted problem synthesis with iterative fine-tuning on model-specific weaknesses. Search for:\n   - WarriorMath defect-aware problem synthesis\n   - WarriorMath arxiv 2025\n   - \"WarriorMath\" LLM reasoning\n\nFor each paper, try to fetch the actual paper or abstract using WebFetch. I need:\n- Full title and authors\n- Arxiv ID\n- Exact results/numbers\n- How they diagnose weaknesses (error-type? concept-level? capability dimension?)\n- Co-evolution mechanism details\n- Whether they use a PRM\n- Key limitations vs a PRM-based error taxonomy approach\n\nBe thorough and read the actual papers.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a230757a73c93e586.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "ea423fdb-b3df-45d8-a796-11c81ae0cf0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T05:28:53.594Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01V5YEBTgdoNmBFCJySnzL3Y`</summary>

```json
{
  "description": "Research LEMMA, Error Classification, and other minor competitors",
  "subagent_type": "general-purpose",
  "prompt": "Research these papers mentioned as missing competitors:\n\n1. **LEMMA (ACL 2025)**: Uses error-type-grounded mistake augmentation for self-correction. Search: \"LEMMA error type mistake augmentation ACL 2025\", \"LEMMA self-correction reasoning\"\n\n2. **Error Classification of LLMs on MWP (EMNLP 2025 Findings)**: Proposes dynamic adaptive error classification + Error-Aware Prompting. Search: \"Error Classification LLMs MWP EMNLP 2025\", \"dynamic adaptive error classification math word problems\"\n\n3. **Bidirectional Curriculum (March 2026)**: Simplifies problems to repair specific reasoning failures. Search: \"Bidirectional Curriculum reasoning 2026\", \"simplify problems repair reasoning failures\"\n\n4. **VHG (May 2026)**: Uses verifier-backed three-party self-play. Search: \"VHG verifier three-party self-play 2026\", \"verifier-backed self-play reasoning\"\n\n5. **Cog-DRIFT (April 2026)**: Adaptively reformulates hard problems. Search: \"Cog-DRIFT adaptive reformulation 2026\", \"Cog-DRIFT reasoning\"\n\nFor each paper, use WebFetch to read the actual paper/abstract. I need:\n- Full title and authors\n- Arxiv ID or venue\n- Key mechanism\n- How it relates to error-type-driven curriculum\n- Key limitations vs DiagCoEvo\n\nBe thorough.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32627dcf-199a-42b5-bf12-04f6c297521d",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "805ffcd6-d78c-41af-aded-6eb590d29e5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 16 · 2026-05-28T05:28:53.607Z_

<details><summary>↩ Tool result · `toolu_01V5YEBTgdoNmBFCJySnzL3Y`</summary>

```text
Async agent launched successfully.
agentId: ae5080ea8c0f3bbcf (internal ID - do not mention to user. Use SendMessage with to: 'ae5080ea8c0f3bbcf' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/ae5080ea8c0f3bbcf.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "805ffcd6-d78c-41af-aded-6eb590d29e5d",
  "isSidechain": false,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "5409421b-5121-4e0b-a5a0-53b2758ffa73",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ae5080ea8c0f3bbcf",
    "description": "Research LEMMA, Error Classification, and other minor competitors",
    "prompt": "Research these papers mentioned as missing competitors:\n\n1. **LEMMA (ACL 2025)**: Uses error-type-grounded mistake augmentation for self-correction. Search: \"LEMMA error type mistake augmentation ACL 2025\", \"LEMMA self-correction reasoning\"\n\n2. **Error Classification of LLMs on MWP (EMNLP 2025 Findings)**: Proposes dynamic adaptive error classification + Error-Aware Prompting. Search: \"Error Classification LLMs MWP EMNLP 2025\", \"dynamic adaptive error classification math word problems\"\n\n3. **Bidirectional Curriculum (March 2026)**: Simplifies problems to repair specific reasoning failures. Search: \"Bidirectional Curriculum reasoning 2026\", \"simplify problems repair reasoning failures\"\n\n4. **VHG (May 2026)**: Uses verifier-backed three-party self-play. Search: \"VHG verifier three-party self-play 2026\", \"verifier-backed self-play reasoning\"\n\n5. **Cog-DRIFT (April 2026)**: Adaptively reformulates hard problems. Search: \"Cog-DRIFT adaptive reformulation 2026\", \"Cog-DRIFT reasoning\"\n\nFor each paper, use WebFetch to read the actual paper/abstract. I need:\n- Full title and authors\n- Arxiv ID or venue\n- Key mechanism\n- How it relates to error-type-driven curriculum\n- Key limitations vs DiagCoEvo\n\nBe thorough.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/ae5080ea8c0f3bbcf.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "805ffcd6-d78c-41af-aded-6eb590d29e5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T05:29:00.702Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019xH9bK6GiRDX5txrje6mSa`</summary>

```json
{
  "description": "Research type-conditioned prompting feasibility",
  "subagent_type": "general-purpose",
  "prompt": "Research the feasibility of type-conditioned problem generation for math reasoning. The question is: if you prompt an LLM to \"generate a math problem that will trigger a specific error type (e.g., sign error, conceptual misunderstanding)\", what are realistic success rates?\n\nSearch for:\n1. \"targeted problem generation\" math reasoning error type\n2. \"error-targeted\" problem synthesis LLM\n3. Self-Error-Instruct error keyphrases clustering generation\n4. \"problem mutation\" math reasoning targeted\n5. WarriorMath defect-aware problem synthesis (how they handle targeted generation)\n6. SwS problem synthesis success rate rejection sampling\n\nAlso search for:\n- Any papers that report success rates for targeted/conditioned math problem generation\n- Problem mutation strategies (modifying existing problems to target specific errors) as a fallback\n- Self-Error-Instruct (ACL 2025) - how they cluster error keyphrases and sample from clusters\n\nUse WebFetch to read relevant papers. I need concrete numbers or estimates for:\n- What yield/success rate can be expected for type-conditioned generation?\n- What are realistic rejection sampling budgets?\n- What fallback strategies exist (e.g., problem mutation vs. generation from scratch)?\n\nThis is critical - the reviewer flagged this as the highest-risk component.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5409421b-5121-4e0b-a5a0-53b2758ffa73",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "76afc89d-175f-4952-8e8c-59c5e9091903",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 18 · 2026-05-28T05:29:00.708Z_

<details><summary>↩ Tool result · `toolu_019xH9bK6GiRDX5txrje6mSa`</summary>

```text
Async agent launched successfully.
agentId: a83fcadbf221bd9ca (internal ID - do not mention to user. Use SendMessage with to: 'a83fcadbf221bd9ca' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a83fcadbf221bd9ca.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76afc89d-175f-4952-8e8c-59c5e9091903",
  "isSidechain": false,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "5087d274-0377-499c-a855-86dac970c7ef",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a83fcadbf221bd9ca",
    "description": "Research type-conditioned prompting feasibility",
    "prompt": "Research the feasibility of type-conditioned problem generation for math reasoning. The question is: if you prompt an LLM to \"generate a math problem that will trigger a specific error type (e.g., sign error, conceptual misunderstanding)\", what are realistic success rates?\n\nSearch for:\n1. \"targeted problem generation\" math reasoning error type\n2. \"error-targeted\" problem synthesis LLM\n3. Self-Error-Instruct error keyphrases clustering generation\n4. \"problem mutation\" math reasoning targeted\n5. WarriorMath defect-aware problem synthesis (how they handle targeted generation)\n6. SwS problem synthesis success rate rejection sampling\n\nAlso search for:\n- Any papers that report success rates for targeted/conditioned math problem generation\n- Problem mutation strategies (modifying existing problems to target specific errors) as a fallback\n- Self-Error-Instruct (ACL 2025) - how they cluster error keyphrases and sample from clusters\n\nUse WebFetch to read relevant papers. I need concrete numbers or estimates for:\n- What yield/success rate can be expected for type-conditioned generation?\n- What are realistic rejection sampling budgets?\n- What fallback strategies exist (e.g., problem mutation vs. generation from scratch)?\n\nThis is critical - the reviewer flagged this as the highest-risk component.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a83fcadbf221bd9ca.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "76afc89d-175f-4952-8e8c-59c5e9091903",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T05:29:06.815Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0162oX1xwgsqRvrQSQwpXfVT`</summary>

```json
{
  "description": "Research taxonomy expansion and MAB curriculum",
  "subagent_type": "general-purpose",
  "prompt": "Research two topics:\n\n**Topic 1: Dynamic error taxonomy expansion mechanisms**\nSearch for:\n1. \"dynamic taxonomy\" \"error classification\" machine learning\n2. \"taxonomy expansion\" clustering error types\n3. Data-Driven Reasoning Rubrics Sanders 2026 - how they derive error taxonomies\n4. \"hierarchical clustering\" error types LLM reasoning\n5. \"taxonomy evolution\" adaptive classification\n\nI need concrete mechanisms for:\n- How to detect when a new error type should be added\n- How to merge or split error categories\n- How to prevent taxonomy explosion\n- Any papers that implement dynamic/evolving taxonomies\n\n**Topic 2: Multi-Armed Bandit (MAB) based curriculum approaches**\nThe reviewer mentioned \"SEC paper's MAB-based curriculum approach\" for automatic category selection. Search for:\n1. \"SEC\" multi-armed bandit curriculum reasoning LLM\n2. MAB curriculum selection error category reasoning\n3. \"multi-armed bandit\" curriculum learning LLM training\n4. adaptive curriculum category selection bandit\n\nI need:\n- The specific SEC paper reference\n- How MAB-based curriculum allocation compares to proportional allocation\n- Whether this is a useful comparison/alternative to error-type-proportional allocation\n\nUse WebFetch to read key papers.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5087d274-0377-499c-a855-86dac970c7ef",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "d81292e6-bfeb-4db0-9348-d82646781c81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 20 · 2026-05-28T05:29:06.822Z_

<details><summary>↩ Tool result · `toolu_0162oX1xwgsqRvrQSQwpXfVT`</summary>

```text
Async agent launched successfully.
agentId: a8f539e114872a9c2 (internal ID - do not mention to user. Use SendMessage with to: 'a8f539e114872a9c2' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a8f539e114872a9c2.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d81292e6-bfeb-4db0-9348-d82646781c81",
  "isSidechain": false,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "bd3bf628-05ed-4e49-9b3e-6f01f254ebae",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a8f539e114872a9c2",
    "description": "Research taxonomy expansion and MAB curriculum",
    "prompt": "Research two topics:\n\n**Topic 1: Dynamic error taxonomy expansion mechanisms**\nSearch for:\n1. \"dynamic taxonomy\" \"error classification\" machine learning\n2. \"taxonomy expansion\" clustering error types\n3. Data-Driven Reasoning Rubrics Sanders 2026 - how they derive error taxonomies\n4. \"hierarchical clustering\" error types LLM reasoning\n5. \"taxonomy evolution\" adaptive classification\n\nI need concrete mechanisms for:\n- How to detect when a new error type should be added\n- How to merge or split error categories\n- How to prevent taxonomy explosion\n- Any papers that implement dynamic/evolving taxonomies\n\n**Topic 2: Multi-Armed Bandit (MAB) based curriculum approaches**\nThe reviewer mentioned \"SEC paper's MAB-based curriculum approach\" for automatic category selection. Search for:\n1. \"SEC\" multi-armed bandit curriculum reasoning LLM\n2. MAB curriculum selection error category reasoning\n3. \"multi-armed bandit\" curriculum learning LLM training\n4. adaptive curriculum category selection bandit\n\nI need:\n- The specific SEC paper reference\n- How MAB-based curriculum allocation compares to proportional allocation\n- Whether this is a useful comparison/alternative to error-type-proportional allocation\n\nUse WebFetch to read key papers.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a8f539e114872a9c2.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "d81292e6-bfeb-4db0-9348-d82646781c81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T05:29:13.315Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01M7W2PyYbQxpWWdQKfbZ7nj`</summary>

```json
{
  "description": "Research GRPO-PRM citation status and PRM generalization",
  "subagent_type": "general-purpose",
  "prompt": "Research two topics:\n\n**Topic 1: \"GRPO is Secretly a PRM\" paper status**\nSearch for:\n1. \"GRPO is Secretly a Process Reward Model\" Sullivan Koller\n2. OpenReview iRWqcnBlLQ\n3. \"GRPO\" \"process reward model\" Sullivan 2025 arxiv\n\nI need to find:\n- The exact arxiv ID\n- Whether the ICLR 2026 submission was withdrawn\n- Current status (preprint only? published elsewhere?)\n- The correct way to cite it\n\n**Topic 2: PRM generalization across model families**\nSearch for:\n1. \"process reward model\" \"distribution shift\" generalization\n2. PRM transfer across models reasoning\n3. PathFinder-PRM generalization different models\n4. \"reward model\" transfer \"domain shift\" reasoning\n5. PRM cold start new model\n\nI need:\n- Evidence on whether PRMs trained on one model's traces transfer to another\n- Any papers discussing PRM generalization/adaptation strategies\n- Concrete strategies for handling the cold-start problem when applying a PRM to a new model family (e.g., from Mistral to Qwen)\n\nUse WebFetch to read key papers.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd3bf628-05ed-4e49-9b3e-6f01f254ebae",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "6ca95c7c-572f-44df-a55d-81385e628388",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 22 · 2026-05-28T05:29:13.322Z_

<details><summary>↩ Tool result · `toolu_01M7W2PyYbQxpWWdQKfbZ7nj`</summary>

```text
Async agent launched successfully.
agentId: ae2e2e8874dcc8e9d (internal ID - do not mention to user. Use SendMessage with to: 'ae2e2e8874dcc8e9d' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/ae2e2e8874dcc8e9d.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ca95c7c-572f-44df-a55d-81385e628388",
  "isSidechain": false,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "2a510683-a95a-4752-93fd-5be5d3f30b61",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ae2e2e8874dcc8e9d",
    "description": "Research GRPO-PRM citation status and PRM generalization",
    "prompt": "Research two topics:\n\n**Topic 1: \"GRPO is Secretly a PRM\" paper status**\nSearch for:\n1. \"GRPO is Secretly a Process Reward Model\" Sullivan Koller\n2. OpenReview iRWqcnBlLQ\n3. \"GRPO\" \"process reward model\" Sullivan 2025 arxiv\n\nI need to find:\n- The exact arxiv ID\n- Whether the ICLR 2026 submission was withdrawn\n- Current status (preprint only? published elsewhere?)\n- The correct way to cite it\n\n**Topic 2: PRM generalization across model families**\nSearch for:\n1. \"process reward model\" \"distribution shift\" generalization\n2. PRM transfer across models reasoning\n3. PathFinder-PRM generalization different models\n4. \"reward model\" transfer \"domain shift\" reasoning\n5. PRM cold start new model\n\nI need:\n- Evidence on whether PRMs trained on one model's traces transfer to another\n- Any papers discussing PRM generalization/adaptation strategies\n- Concrete strategies for handling the cold-start problem when applying a PRM to a new model family (e.g., from Mistral to Qwen)\n\nUse WebFetch to read key papers.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/ae2e2e8874dcc8e9d.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "6ca95c7c-572f-44df-a55d-81385e628388",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T05:29:20.078Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QEhpgpwSGWfEGxwJbjRKkB`</summary>

```json
{
  "description": "Research crowded field differentiation",
  "subagent_type": "general-purpose",
  "prompt": "Research the current state of co-evolutionary self-improvement for LLM reasoning to understand how crowded this field is and what would constitute a meaningful contribution at ICLR 2027.\n\nSearch for:\n1. \"self-improving\" reasoning LLM 2026 survey\n2. \"co-evolution\" reasoning self-improvement 2026\n3. ICLR 2027 reasoning self-improvement\n4. Papers With Code MATH benchmark leaderboard\n5. \"curriculum learning\" reasoning LLM co-evolution 2026\n\nAlso search for very recent papers (2026) that may have appeared:\n6. \"self-play\" reasoning math 2026\n7. \"iterative self-improvement\" math reasoning 2026\n\nI need:\n- A count/list of how many papers in this space appeared in the last 12 months\n- What the current SOTA numbers are on MATH-500, AMC, AIME for 7B-8B models\n- What gap sizes (percentage points improvement) are considered significant\n- What kind of contribution (empirical, analytical, methodological) would stand out at ICLR 2027\n- Whether error-type analysis as an analytical contribution (showing how error distributions shift across iterations) would be sufficiently novel\n\nUse WebFetch to check recent papers and leaderboards.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a510683-a95a-4752-93fd-5be5d3f30b61",
  "isSidechain": false,
  "requestId": "req_011CbUR1jp7DVatHDfhh7Wtc",
  "type": "assistant",
  "uuid": "e41c409a-8d8f-4a05-b07c-3c870697f59c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jtz27okpUZ7W825Xz53Hd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8229,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2990,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8229
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "f9a44878-9186-4747-bea2-a5c57c227985",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Assistant

_source line 26 · 2026-05-28T05:29:23.387Z_

I've launched 7 research agents in parallel to investigate all the reviewer's concerns. I'll compile the complete revised proposal once all results are in. Let me wait for them to complete.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9a44878-9186-4747-bea2-a5c57c227985",
  "isSidechain": false,
  "requestId": "req_011CbUR5N42UGHe3rNa6yWSF",
  "type": "assistant",
  "uuid": "5bf575e2-79d8-4d0d-9090-ad7f8059177a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmAxCVCSitBReEqpF3JcqG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4792,
      "cache_read_input_tokens": 19243,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 19243,
          "cache_creation_input_tokens": 4792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4792
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

_source line 27 · 2026-05-28T05:29:27.818Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UovSGyf4zDH9xmwTqFJ7K5`</summary>

```json
{
  "description": "Research Socratic-Zero deeper",
  "subagent_type": "general-purpose",
  "prompt": "I need to find the paper \"Socratic-Zero\" from around September 2025 that reportedly achieves +20.2pp improvement in LLM reasoning through Teacher-Solver-Generator co-evolution.\n\nPlease search using WebSearch for:\n1. \"Socratic-Zero\" arxiv\n2. \"Socratic-Zero\" teacher solver generator reasoning\n\nThen try to fetch papers from these URLs using WebFetch:\n- https://arxiv.org/abs/2509.07566 (possible arxiv ID range for Sep 2025)\n- Search for \"Socratic Zero\" on arxiv.org\n\nI need the full title, arxiv ID, and key details of how the Teacher targets weaknesses.",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bf575e2-79d8-4d0d-9090-ad7f8059177a",
  "isSidechain": false,
  "requestId": "req_011CbUR5N42UGHe3rNa6yWSF",
  "type": "assistant",
  "uuid": "ea7d4630-6a6c-40bc-a501-cccac496aac9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmAxCVCSitBReEqpF3JcqG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4792,
      "cache_read_input_tokens": 19243,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 19243,
          "cache_creation_input_tokens": 4792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4792
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

_source line 28 · 2026-05-28T05:29:27.827Z_

<details><summary>↩ Tool result · `toolu_01UovSGyf4zDH9xmwTqFJ7K5`</summary>

```text
Async agent launched successfully.
agentId: a548af9b7f660e90d (internal ID - do not mention to user. Use SendMessage with to: 'a548af9b7f660e90d' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a548af9b7f660e90d.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea7d4630-6a6c-40bc-a501-cccac496aac9",
  "isSidechain": false,
  "promptId": "667bba46-6444-4626-bab9-970660b89104",
  "type": "user",
  "uuid": "02a09d0e-3000-4204-85d3-9deebfb0618c",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a548af9b7f660e90d",
    "description": "Research Socratic-Zero deeper",
    "prompt": "I need to find the paper \"Socratic-Zero\" from around September 2025 that reportedly achieves +20.2pp improvement in LLM reasoning through Teacher-Solver-Generator co-evolution.\n\nPlease search using WebSearch for:\n1. \"Socratic-Zero\" arxiv\n2. \"Socratic-Zero\" teacher solver generator reasoning\n\nThen try to fetch papers from these URLs using WebFetch:\n- https://arxiv.org/abs/2509.07566 (possible arxiv ID range for Sep 2025)\n- Search for \"Socratic Zero\" on arxiv.org\n\nI need the full title, arxiv ID, and key details of how the Teacher targets weaknesses.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a548af9b7f660e90d.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "ea7d4630-6a6c-40bc-a501-cccac496aac9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-28T05:29:27.979Z_

```json
{
  "parentUuid": "02a09d0e-3000-4204-85d3-9deebfb0618c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "50450846-9233-44c8-ae0a-667678530842",
  "timestamp": "2026-05-28T05:29:27.979Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-28T05:29:30.713Z_

I'm waiting for all 8 research agents to complete their investigations. Let me continue to be patient and wait for the results to come in before synthesizing the revised proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50450846-9233-44c8-ae0a-667678530842",
  "isSidechain": false,
  "requestId": "req_011CbUR5wXRPMzfRwy7ofhdR",
  "type": "assistant",
  "uuid": "0b543f06-9e80-40d8-a734-160b78de9031",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157LfNSAs2v7MXCnDPSdn4r",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 24035,
      "output_tokens": 40,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 40,
          "cache_read_input_tokens": 24035,
          "cache_creation_input_tokens": 663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 663
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

_source line 31 · 2026-05-28T05:30:16.988Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:30:16.988Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "&lt;task-notification>\n&lt;task-id>a548af9b7f660e90d&lt;/task-id>\n&lt;tool-use-id>toolu_01UovSGyf4zDH9xmwTqFJ7K5&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a548af9b7f660e90d.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research Socratic-Zero deeper\" completed&lt;/summary>\n&lt;result>Here are the complete findings on the paper:\n\n---\n\n**Full Title:** Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution\n\n**arXiv ID:** 2509.24726 -- https://arxiv.org/abs/2509.24726\n\n**Submission Date:** September 29, 2025\n\n**Authors:** Shaobo Wang, Zhengbo Jiao, Zifan Zhang, Yilang Peng, Xu Ze, Boyu Yang, Wei Wang, Hu Wei, Linfeng Zhang\n\n---\n\n## Three-Agent Architecture\n\nThe framework co-evolves three agents in a closed loop starting from only 100 seed questions (selected from the MATH dataset, Levels 2-4, across seven math domains):\n\n1. **Solver** -- Generates k=8 solution attempts per problem. Correct and incorrect solutions form preference pairs, and the Solver is trained via Direct Preference Optimization (DPO) to favor correct reasoning trajectories.\n\n2. **Teacher** -- The core weakness-targeting mechanism. The Teacher collects the Solver's failed attempts and analyzes the specific error patterns in those failed trajectories. It uses two functions:\n   - A **verification function** V(q, y) that judges correctness.\n   - A **refinement function** G(q, y_fail) that creates new problem-solution pairs by revising an original problem based on a failed solution.\n   \n   This means the Teacher does not generate random problems -- it directly crafts new challenges that address the exact weaknesses exposed by the Solver's failures. The new problems augment the curriculum for the next iteration.\n\n3. **Generator** -- Trained via weighted supervised fine-tuning (WSFT) to replicate the Teacher's curriculum design strategy at scale. It uses a utility function (unnormalized Gaussian centered at a 0.5 success rate) to score problem difficulty, targeting the \"zone of proximal development\" -- problems that are neither trivial nor impossible for the current Solver.\n\n## Co-Evolution Loop\n\n- **Phase 1 (Solver Learning):** Solver attempts problems, results are split into correct/incorrect, DPO training is applied.\n- **Phase 2 (Curriculum Generation):** Teacher analyzes failures, generates targeted new problems.\n- **Phase 3 (Curriculum Update):** New problems replace outdated content, maintaining dynamic difficulty calibration.\n- The cycle repeats, expanding the curriculum from 100 seed problems to thousands.\n\n## Key Results\n\n- **Socratic-Solver-8B** (Qwen3-8B base): 56.1% average accuracy across 7 benchmarks, a **+20.2pp** gain over static augmentation baselines. Particularly strong on competition math: +19.1pp on AIME-24, +16.5pp on AIME-25.\n- **Cross-architecture generalization:** GLM4-9B gains +17.1pp; Qwen3-14B gains +17.3pp.\n- **Socratic-Generator-32B** achieves 95.6% problem validity and 37.72% downstream training effectiveness, outperforming models 20x its size including Claude-4.1-Opus (37.63%), Qwen3-235B (37.13%), Gemini-2.5-Pro (37.20%), and DeepSeek-V3.1 (36.62%).\n\n---\n\nSources:\n- [Socratic-Zero on arXiv](https://arxiv.org/abs/2509.24726)\n- [Full HTML version](https://arxiv.org/html/2509.24726)\n- [Hugging Face paper page](https://huggingface.co/papers/2509.24726)\n- [OpenReview PDF](https://openreview.net/pdf/1813b5a5e1dd39fac7e9879dc1a7e0885516ac3b.pdf)&lt;/result>\n&lt;usage>&lt;total_tokens>13714&lt;/total_tokens>&lt;tool_uses>6&lt;/tool_uses>&lt;duration_ms>49167&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 32 · 2026-05-28T05:30:17.027Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:30:17.027Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 2

4 recorded events

### User

_source line 33 · 2026-05-28T05:30:17.059Z_

&lt;task-notification>
&lt;task-id>a548af9b7f660e90d&lt;/task-id>
&lt;tool-use-id>toolu_01UovSGyf4zDH9xmwTqFJ7K5&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a548af9b7f660e90d.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research Socratic-Zero deeper" completed&lt;/summary>
&lt;result>Here are the complete findings on the paper:

---

**Full Title:** Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution

**arXiv ID:** 2509.24726 -- https://arxiv.org/abs/2509.24726

**Submission Date:** September 29, 2025

**Authors:** Shaobo Wang, Zhengbo Jiao, Zifan Zhang, Yilang Peng, Xu Ze, Boyu Yang, Wei Wang, Hu Wei, Linfeng Zhang

---

## Three-Agent Architecture

The framework co-evolves three agents in a closed loop starting from only 100 seed questions (selected from the MATH dataset, Levels 2-4, across seven math domains):

1. **Solver** -- Generates k=8 solution attempts per problem. Correct and incorrect solutions form preference pairs, and the Solver is trained via Direct Preference Optimization (DPO) to favor correct reasoning trajectories.

2. **Teacher** -- The core weakness-targeting mechanism. The Teacher collects the Solver's failed attempts and analyzes the specific error patterns in those failed trajectories. It uses two functions:
   - A **verification function** V(q, y) that judges correctness.
   - A **refinement function** G(q, y_fail) that creates new problem-solution pairs by revising an original problem based on a failed solution.
   
   This means the Teacher does not generate random problems -- it directly crafts new challenges that address the exact weaknesses exposed by the Solver's failures. The new problems augment the curriculum for the next iteration.

3. **Generator** -- Trained via weighted supervised fine-tuning (WSFT) to replicate the Teacher's curriculum design strategy at scale. It uses a utility function (unnormalized Gaussian centered at a 0.5 success rate) to score problem difficulty, targeting the "zone of proximal development" -- problems that are neither trivial nor impossible for the current Solver.

## Co-Evolution Loop

- **Phase 1 (Solver Learning):** Solver attempts problems, results are split into correct/incorrect, DPO training is applied.
- **Phase 2 (Curriculum Generation):** Teacher analyzes failures, generates targeted new problems.
- **Phase 3 (Curriculum Update):** New problems replace outdated content, maintaining dynamic difficulty calibration.
- The cycle repeats, expanding the curriculum from 100 seed problems to thousands.

## Key Results

- **Socratic-Solver-8B** (Qwen3-8B base): 56.1% average accuracy across 7 benchmarks, a **+20.2pp** gain over static augmentation baselines. Particularly strong on competition math: +19.1pp on AIME-24, +16.5pp on AIME-25.
- **Cross-architecture generalization:** GLM4-9B gains +17.1pp; Qwen3-14B gains +17.3pp.
- **Socratic-Generator-32B** achieves 95.6% problem validity and 37.72% downstream training effectiveness, outperforming models 20x its size including Claude-4.1-Opus (37.63%), Qwen3-235B (37.13%), Gemini-2.5-Pro (37.20%), and DeepSeek-V3.1 (36.62%).

---

Sources:
- [Socratic-Zero on arXiv](https://arxiv.org/abs/2509.24726)
- [Full HTML version](https://arxiv.org/html/2509.24726)
- [Hugging Face paper page](https://huggingface.co/papers/2509.24726)
- [OpenReview PDF](https://openreview.net/pdf/1813b5a5e1dd39fac7e9879dc1a7e0885516ac3b.pdf)&lt;/result>
&lt;usage>&lt;total_tokens>13714&lt;/total_tokens>&lt;tool_uses>6&lt;/tool_uses>&lt;duration_ms>49167&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b543f06-9e80-40d8-a734-160b78de9031",
  "isSidechain": false,
  "promptId": "f32fafd0-7f3e-4a0c-9e02-af4d1d6593ae",
  "type": "user",
  "uuid": "0c7216b1-b866-4095-8e1c-47ed004d8979",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-28T05:30:20.521Z_

Good, Socratic-Zero research is complete. Let me wait for the remaining agents to finish.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c7216b1-b866-4095-8e1c-47ed004d8979",
  "isSidechain": false,
  "requestId": "req_011CbUR9ZTV2kyNmUGX1oKFd",
  "type": "assistant",
  "uuid": "b44fe646-e89f-4e8c-80bf-5be607b80d02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQ7Qm4RDPcBavtLLZYhbYE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1168,
      "cache_read_input_tokens": 24698,
      "output_tokens": 25,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1168,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 25,
          "cache_read_input_tokens": 24698,
          "cache_creation_input_tokens": 1168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1168
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

_source line 35 · 2026-05-28T05:31:09.612Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:31:09.612Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "&lt;task-notification>\n&lt;task-id>a230757a73c93e586&lt;/task-id>\n&lt;tool-use-id>toolu_012TPYTvbZTSSJvoR5tpeTdX&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a230757a73c93e586.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research SAGE and WarriorMath papers\" completed&lt;/summary>\n&lt;result>I now have comprehensive information on both papers. Here is the thorough analysis:\n\n---\n\n## SAGE: Multi-Agent Self-Evolution for LLM Reasoning\n\n**Full Title:** SAGE: Multi-Agent Self-Evolution for LLM Reasoning\n**ArXiv ID:** 2603.15255 (March 16, 2026)\n**Authors:** Yulin Peng, Xinxin Zhu, Chenxing Wei, Nianbo Zeng, Leilei Wang, Ying Tiffany He, F. Richard Yu\n\n### Co-Evolution Mechanism (4-Agent Loop)\n\nAll four agents share a single LLM backbone and are jointly updated via Task-Relative REINFORCE++ with per-role advantage normalization. Each training iteration has distinct phases:\n\n1. **Challenge Phase:** A reference problem is sampled from a 500-example seed set. The Challenger generates a new question + verifier. The Critic scores question quality (threshold alpha=0.7). The Solver samples Ns answers. An external verifier checks correctness. A difficulty reward is computed as (1 - success_rate), incentivizing the Challenger to produce problems the Solver struggles with.\n\n2. **Plan-Solve Phase:** A question is sampled. The Planner generates a structured multi-step plan. The Critic scores the plan (threshold beta=0.3). If the plan passes, the Solver uses it; otherwise the Solver solves directly. The external verifier checks the answer.\n\n3. **Critic Phase (optional):** Lightweight format calibration objective.\n\n4. **Synchronized Update:** All agents are jointly updated in a single step.\n\nTraining runs for 200 steps total, with peak performance around step 100-120 and gradual decline afterward (suggesting over-specialization risk).\n\n### Critic Details\n\nThe Critic outputs scalar scores on a 1-10 scale, normalized to [0,1]. It evaluates questions on \"clarity, relevance, well-formedness\" and plans on \"logical soundness and completeness.\" It also applies format compliance rewards checking required tags. Critically, **the Critic does NOT determine correctness** -- correctness is always determined by the external verifier. The Critic is a quality filter, not an error diagnoser.\n\n### Weakness Diagnosis\n\n**Binary pass/fail only.** The external verifier provides Vgt(q,a,v) in [0,1] (exact-match for math, test pass rate for code). There is no error taxonomy, no error-type classification, no concept-level analysis. Weakness detection is purely implicit through difficulty rewards: the Challenger is rewarded for generating problems where the Solver has a low success rate, but there is no analysis of *why* the Solver fails.\n\n### PRM Usage\n\n**No PRM is used anywhere.** The framework relies on: (1) external verifiers (ground-truth answers or executable tests), (2) the Critic's soft quality scores (non-verifiable evaluation), and (3) format rewards. The paper explicitly states correctness \"is determined by the external verifier rather than the Critic.\"\n\n### Exact Benchmark Results (Pass@1 %)\n\n**Qwen-2.5-7B-Instruct (the headline model):**\n- HumanEval+: 76.2 | MBPP+: 64.0 | LiveCodeBench: 26.4\n- GSM8K: 92.2 | MATH: 74.7 | AIME2024: 13.3 | AIME2025: 13.3\n- AMC: 52.5 | OlympiadBench: 38.7\n- Code Avg: 55.5 | Math Avg: 47.5 | Overall Avg: 50.1\n\n**Qwen-2.5-3B-Instruct:** Overall Avg 42.0\n**Qwen-3-4B-Base:** Overall Avg 55.9\n\nHeadline improvements: +8.9% on LiveCodeBench, +10.7% on OlympiadBench for the 7B model.\n\n### Stated Limitations\n1. Restricted to verifiable domains (cannot extend to open-ended/subjective tasks)\n2. Still requires a 500-example seed set\n3. Evaluation only on math and code benchmarks\n4. Training instability -- performance declines after ~step 120, requiring early stopping\n\n---\n\n## WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework\n\n**Full Title:** WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework\n**ArXiv ID:** 2508.01245 (August 2, 2025)\n**Authors:** Yue Chen, Minghua He, Fangkai Yang, Pu Zhao, Lu Wang, Yu Kang, Yifei Dong, Yuefeng Zhan, Hao Sun, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang\n\n### Defect Diagnosis Mechanism\n\n**Binary pass/fail, not a true error taxonomy.** Problems where the base model fails on ALL N=16 rollouts are retained as \"defect data.\" The paper mentions that \"inherent defects refer to systematic failure (e.g., misinterpreting quantifiers, incorrect symbolic steps)\" but **does not implement any formal categorization or taxonomy** of these defect types. There is no concept-level, capability-dimension, or error-type classification. The operationalization is purely: can the model solve this problem or not (across 16 attempts)?\n\n### Synthesis Pipeline (Two Stages)\n\n**Stage 1 -- Problem Generation:**\n1. A 5-member expert LLM committee (DeepSeek-R1-Distill-Llama-70B, Qwen2.5-Math-72B-Instruct, QwQ-32B, AceMath-72B-Instruct, Phi-4-reasoning) collaborates.\n2. One LLM acts as \"examiner\" and generates problems across 9 temperature/top-p configurations, with prompts emphasizing Quality, Difficulty, Diversity, and Challenge.\n3. GPT-4-style evaluation scores problems 1-10; only scores 6+ are retained.\n4. KCenterGreedy deduplication using all-roberta-large-v1 embeddings.\n5. Defect assessment: generate N=16 rollouts from the base model; discard problems where all are correct.\n\n**Stage 2 -- Answer Generation:**\n- The examiner answers its own question; a reviewer (another committee member) also answers.\n- The remaining 3 members vote on the best answer.\n- An Elo rating system (adapted from chess) weights votes by each model's historical performance.\n\n### Progressive Training\n\n**Two-phase training:**\n\n1. **SFT Phase:** Uses highest-Elo-ranked responses as gold standard for supervised fine-tuning.\n\n2. **Iterative DPO Alignment (3 iterations, M0 -&gt; M1 -&gt; M2 -&gt; M3):**\n   - Each iteration: sample N=32 solutions per problem (temp 0.7, top-p 0.8)\n   - Identify incorrect outputs as negative examples\n   - Create K=10 preference pairs per problem (gold correct vs. incorrect)\n   - Optimize using DPO loss + NLL auxiliary loss (alpha=1.0, beta=0.1)\n   - Progression on AIME'24: SFT baseline 36.7% -&gt; Iter1 42.5% -&gt; Iter2 44.7% -&gt; Iter3 48.3%\n\nNote: the iterations don't use progressively harder problems; they retrain on the same problems but from the evolving model's new failure patterns.\n\n### PRM Usage\n\n**No PRM is used.** The reward function is binary correctness only: r = 1 if answer matches ground truth, 0 otherwise. Answer quality ranking uses the Elo rating system (not a learned reward model).\n\n### Exact Benchmark Results (Pass@1 %)\n\n| Model | AIME'24 | AIME'25 | AMC'23 | MATH-500 | Minerva | Olympiad |\n|---|---|---|---|---|---|---|\n| **WarriorMath-Qwen-7B** | 48.3 +/- 2.6 | 36.5 +/- 5.0 | 83.0 +/- 2.5 | 88.3 +/- 1.4 | 41.2 +/- 2.8 | 52.1 +/- 0.8 |\n| **WarriorMath-DS-7B** | 60.0 +/- 9.1 | 50.7 +/- 9.1 | 93.2 +/- 4.9 | 95.0 +/- 1.0 | 43.2 +/- 1.9 | 69.6 +/- 1.8 |\n| Qwen2.5-Math-7B-Instruct (base) | 15.7 | 10.7 | 67.0 | 82.9 | 35.0 | 41.3 |\n| DeepSeek-R1-Distill-Qwen-7B (base) | 52.3 | 39.0 | 91.5 | 94.1 | 40.1 | 67.3 |\n\nCommittee ablation: 1 member -&gt; 19.7% on AIME'24; 5 members -&gt; 48.3%.\n\n### Stated Limitations\n- \"As the number of expert models increases, the evaluation process becomes increasingly time-consuming.\"\n- No analysis of which defect *types* are actually addressed by the training\n- Binary correctness signal ignores partial credit / reasoning quality\n- Computational cost of multi-expert committee not quantified\n\n---\n\n## Comparative Analysis: Key Limitations vs. a PRM-Based Error Taxonomy Approach\n\nBoth papers share a critical structural gap that a PRM-based error taxonomy approach would address:\n\n**1. Neither paper uses a PRM or any form of process-level reward.**\nBoth rely entirely on outcome-level binary correctness (right/wrong final answer). This means neither system can identify *where in the reasoning chain* errors occur, nor can they distinguish between a solution that went wrong at step 2 vs. step 15.\n\n**2. Neither paper implements an error taxonomy.**\n- SAGE's weakness detection is purely implicit: the Challenger is rewarded for generating hard problems, but there is no classification of what makes them hard or what error patterns the Solver exhibits.\n- WarriorMath explicitly mentions \"defect-aware\" in its title but operationalizes defects as binary pass/fail across 16 rollouts. The paper acknowledges examples like \"misinterpreting quantifiers\" and \"incorrect symbolic steps\" but never actually classifies or acts on these categories.\n\n**3. No targeted remediation of specific error types.**\n- SAGE generates harder problems in general but cannot target, e.g., \"the model is weak at algebraic manipulation\" vs. \"the model is weak at combinatorial reasoning.\"\n- WarriorMath generates problems the model fails on but doesn't distinguish *why* it fails. Two problems the model gets wrong might exercise completely different skills, but they're treated identically.\n\n**4. A PRM-based error taxonomy approach would enable:**\n- Step-level error localization (which reasoning step fails)\n- Error-type classification (computational error, logical fallacy, conceptual misunderstanding, etc.)\n- Targeted data generation that specifically addresses the most frequent/impactful error types\n- More efficient training by focusing compute on the actual bottleneck capabilities rather than uniform difficulty escalation\n- Curriculum design informed by a principled weakness profile rather than aggregate success rates\n\n**5. SAGE-specific limitations vs. PRM approach:**\n- The Critic scores quality but not correctness or error type -- it's a filter, not a diagnoser\n- The co-evolution loop has no mechanism to ensure coverage across different reasoning skills; it could get stuck in a narrow difficulty corridor\n- Training instability (performance drops after step 120) might be mitigated by a more principled curriculum informed by error type distribution\n\n**6. WarriorMath-specific limitations vs. PRM approach:**\n- The 5-model expert committee is extremely expensive (5 x 70B+ models) but provides only a binary signal\n- DPO preference pairs are (correct, incorrect) without any process-level signal about where the incorrect solution diverged\n- The iterative alignment retrains on the same problems -- a PRM could identify when error patterns shift across iterations, enabling dynamic problem selection\n\nSources:\n- [SAGE: Multi-Agent Self-Evolution for LLM Reasoning (arXiv:2603.15255)](https://arxiv.org/abs/2603.15255)\n- [SAGE HTML version](https://arxiv.org/html/2603.15255v1)\n- [WarriorMath: Enhancing the Mathematical Ability of LLMs with a Defect-aware Framework (arXiv:2508.01245)](https://arxiv.org/abs/2508.01245)\n- [WarriorMath HTML version](https://arxiv.org/html/2508.01245v1)&lt;/result>\n&lt;usage>&lt;total_tokens>18538&lt;/total_tokens>&lt;tool_uses>9&lt;/tool_uses>&lt;duration_ms>141320&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 36 · 2026-05-28T05:31:09.615Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:31:09.615Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 3

7 recorded events

### User

_source line 37 · 2026-05-28T05:31:09.631Z_

&lt;task-notification>
&lt;task-id>a230757a73c93e586&lt;/task-id>
&lt;tool-use-id>toolu_012TPYTvbZTSSJvoR5tpeTdX&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a230757a73c93e586.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research SAGE and WarriorMath papers" completed&lt;/summary>
&lt;result>I now have comprehensive information on both papers. Here is the thorough analysis:

---

## SAGE: Multi-Agent Self-Evolution for LLM Reasoning

**Full Title:** SAGE: Multi-Agent Self-Evolution for LLM Reasoning
**ArXiv ID:** 2603.15255 (March 16, 2026)
**Authors:** Yulin Peng, Xinxin Zhu, Chenxing Wei, Nianbo Zeng, Leilei Wang, Ying Tiffany He, F. Richard Yu

### Co-Evolution Mechanism (4-Agent Loop)

All four agents share a single LLM backbone and are jointly updated via Task-Relative REINFORCE++ with per-role advantage normalization. Each training iteration has distinct phases:

1. **Challenge Phase:** A reference problem is sampled from a 500-example seed set. The Challenger generates a new question + verifier. The Critic scores question quality (threshold alpha=0.7). The Solver samples Ns answers. An external verifier checks correctness. A difficulty reward is computed as (1 - success_rate), incentivizing the Challenger to produce problems the Solver struggles with.

2. **Plan-Solve Phase:** A question is sampled. The Planner generates a structured multi-step plan. The Critic scores the plan (threshold beta=0.3). If the plan passes, the Solver uses it; otherwise the Solver solves directly. The external verifier checks the answer.

3. **Critic Phase (optional):** Lightweight format calibration objective.

4. **Synchronized Update:** All agents are jointly updated in a single step.

Training runs for 200 steps total, with peak performance around step 100-120 and gradual decline afterward (suggesting over-specialization risk).

### Critic Details

The Critic outputs scalar scores on a 1-10 scale, normalized to [0,1]. It evaluates questions on "clarity, relevance, well-formedness" and plans on "logical soundness and completeness." It also applies format compliance rewards checking required tags. Critically, **the Critic does NOT determine correctness** -- correctness is always determined by the external verifier. The Critic is a quality filter, not an error diagnoser.

### Weakness Diagnosis

**Binary pass/fail only.** The external verifier provides Vgt(q,a,v) in [0,1] (exact-match for math, test pass rate for code). There is no error taxonomy, no error-type classification, no concept-level analysis. Weakness detection is purely implicit through difficulty rewards: the Challenger is rewarded for generating problems where the Solver has a low success rate, but there is no analysis of *why* the Solver fails.

### PRM Usage

**No PRM is used anywhere.** The framework relies on: (1) external verifiers (ground-truth answers or executable tests), (2) the Critic's soft quality scores (non-verifiable evaluation), and (3) format rewards. The paper explicitly states correctness "is determined by the external verifier rather than the Critic."

### Exact Benchmark Results (Pass@1 %)

**Qwen-2.5-7B-Instruct (the headline model):**
- HumanEval+: 76.2 | MBPP+: 64.0 | LiveCodeBench: 26.4
- GSM8K: 92.2 | MATH: 74.7 | AIME2024: 13.3 | AIME2025: 13.3
- AMC: 52.5 | OlympiadBench: 38.7
- Code Avg: 55.5 | Math Avg: 47.5 | Overall Avg: 50.1

**Qwen-2.5-3B-Instruct:** Overall Avg 42.0
**Qwen-3-4B-Base:** Overall Avg 55.9

Headline improvements: +8.9% on LiveCodeBench, +10.7% on OlympiadBench for the 7B model.

### Stated Limitations
1. Restricted to verifiable domains (cannot extend to open-ended/subjective tasks)
2. Still requires a 500-example seed set
3. Evaluation only on math and code benchmarks
4. Training instability -- performance declines after ~step 120, requiring early stopping

---

## WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework

**Full Title:** WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework
**ArXiv ID:** 2508.01245 (August 2, 2025)
**Authors:** Yue Chen, Minghua He, Fangkai Yang, Pu Zhao, Lu Wang, Yu Kang, Yifei Dong, Yuefeng Zhan, Hao Sun, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang

### Defect Diagnosis Mechanism

**Binary pass/fail, not a true error taxonomy.** Problems where the base model fails on ALL N=16 rollouts are retained as "defect data." The paper mentions that "inherent defects refer to systematic failure (e.g., misinterpreting quantifiers, incorrect symbolic steps)" but **does not implement any formal categorization or taxonomy** of these defect types. There is no concept-level, capability-dimension, or error-type classification. The operationalization is purely: can the model solve this problem or not (across 16 attempts)?

### Synthesis Pipeline (Two Stages)

**Stage 1 -- Problem Generation:**
1. A 5-member expert LLM committee (DeepSeek-R1-Distill-Llama-70B, Qwen2.5-Math-72B-Instruct, QwQ-32B, AceMath-72B-Instruct, Phi-4-reasoning) collaborates.
2. One LLM acts as "examiner" and generates problems across 9 temperature/top-p configurations, with prompts emphasizing Quality, Difficulty, Diversity, and Challenge.
3. GPT-4-style evaluation scores problems 1-10; only scores 6+ are retained.
4. KCenterGreedy deduplication using all-roberta-large-v1 embeddings.
5. Defect assessment: generate N=16 rollouts from the base model; discard problems where all are correct.

**Stage 2 -- Answer Generation:**
- The examiner answers its own question; a reviewer (another committee member) also answers.
- The remaining 3 members vote on the best answer.
- An Elo rating system (adapted from chess) weights votes by each model's historical performance.

### Progressive Training

**Two-phase training:**

1. **SFT Phase:** Uses highest-Elo-ranked responses as gold standard for supervised fine-tuning.

2. **Iterative DPO Alignment (3 iterations, M0 -&gt; M1 -&gt; M2 -&gt; M3):**
   - Each iteration: sample N=32 solutions per problem (temp 0.7, top-p 0.8)
   - Identify incorrect outputs as negative examples
   - Create K=10 preference pairs per problem (gold correct vs. incorrect)
   - Optimize using DPO loss + NLL auxiliary loss (alpha=1.0, beta=0.1)
   - Progression on AIME'24: SFT baseline 36.7% -&gt; Iter1 42.5% -&gt; Iter2 44.7% -&gt; Iter3 48.3%

Note: the iterations don't use progressively harder problems; they retrain on the same problems but from the evolving model's new failure patterns.

### PRM Usage

**No PRM is used.** The reward function is binary correctness only: r = 1 if answer matches ground truth, 0 otherwise. Answer quality ranking uses the Elo rating system (not a learned reward model).

### Exact Benchmark Results (Pass@1 %)

| Model | AIME'24 | AIME'25 | AMC'23 | MATH-500 | Minerva | Olympiad |
|---|---|---|---|---|---|---|
| **WarriorMath-Qwen-7B** | 48.3 +/- 2.6 | 36.5 +/- 5.0 | 83.0 +/- 2.5 | 88.3 +/- 1.4 | 41.2 +/- 2.8 | 52.1 +/- 0.8 |
| **WarriorMath-DS-7B** | 60.0 +/- 9.1 | 50.7 +/- 9.1 | 93.2 +/- 4.9 | 95.0 +/- 1.0 | 43.2 +/- 1.9 | 69.6 +/- 1.8 |
| Qwen2.5-Math-7B-Instruct (base) | 15.7 | 10.7 | 67.0 | 82.9 | 35.0 | 41.3 |
| DeepSeek-R1-Distill-Qwen-7B (base) | 52.3 | 39.0 | 91.5 | 94.1 | 40.1 | 67.3 |

Committee ablation: 1 member -&gt; 19.7% on AIME'24; 5 members -&gt; 48.3%.

### Stated Limitations
- "As the number of expert models increases, the evaluation process becomes increasingly time-consuming."
- No analysis of which defect *types* are actually addressed by the training
- Binary correctness signal ignores partial credit / reasoning quality
- Computational cost of multi-expert committee not quantified

---

## Comparative Analysis: Key Limitations vs. a PRM-Based Error Taxonomy Approach

Both papers share a critical structural gap that a PRM-based error taxonomy approach would address:

**1. Neither paper uses a PRM or any form of process-level reward.**
Both rely entirely on outcome-level binary correctness (right/wrong final answer). This means neither system can identify *where in the reasoning chain* errors occur, nor can they distinguish between a solution that went wrong at step 2 vs. step 15.

**2. Neither paper implements an error taxonomy.**
- SAGE's weakness detection is purely implicit: the Challenger is rewarded for generating hard problems, but there is no classification of what makes them hard or what error patterns the Solver exhibits.
- WarriorMath explicitly mentions "defect-aware" in its title but operationalizes defects as binary pass/fail across 16 rollouts. The paper acknowledges examples like "misinterpreting quantifiers" and "incorrect symbolic steps" but never actually classifies or acts on these categories.

**3. No targeted remediation of specific error types.**
- SAGE generates harder problems in general but cannot target, e.g., "the model is weak at algebraic manipulation" vs. "the model is weak at combinatorial reasoning."
- WarriorMath generates problems the model fails on but doesn't distinguish *why* it fails. Two problems the model gets wrong might exercise completely different skills, but they're treated identically.

**4. A PRM-based error taxonomy approach would enable:**
- Step-level error localization (which reasoning step fails)
- Error-type classification (computational error, logical fallacy, conceptual misunderstanding, etc.)
- Targeted data generation that specifically addresses the most frequent/impactful error types
- More efficient training by focusing compute on the actual bottleneck capabilities rather than uniform difficulty escalation
- Curriculum design informed by a principled weakness profile rather than aggregate success rates

**5. SAGE-specific limitations vs. PRM approach:**
- The Critic scores quality but not correctness or error type -- it's a filter, not a diagnoser
- The co-evolution loop has no mechanism to ensure coverage across different reasoning skills; it could get stuck in a narrow difficulty corridor
- Training instability (performance drops after step 120) might be mitigated by a more principled curriculum informed by error type distribution

**6. WarriorMath-specific limitations vs. PRM approach:**
- The 5-model expert committee is extremely expensive (5 x 70B+ models) but provides only a binary signal
- DPO preference pairs are (correct, incorrect) without any process-level signal about where the incorrect solution diverged
- The iterative alignment retrains on the same problems -- a PRM could identify when error patterns shift across iterations, enabling dynamic problem selection

Sources:
- [SAGE: Multi-Agent Self-Evolution for LLM Reasoning (arXiv:2603.15255)](https://arxiv.org/abs/2603.15255)
- [SAGE HTML version](https://arxiv.org/html/2603.15255v1)
- [WarriorMath: Enhancing the Mathematical Ability of LLMs with a Defect-aware Framework (arXiv:2508.01245)](https://arxiv.org/abs/2508.01245)
- [WarriorMath HTML version](https://arxiv.org/html/2508.01245v1)&lt;/result>
&lt;usage>&lt;total_tokens>18538&lt;/total_tokens>&lt;tool_uses>9&lt;/tool_uses>&lt;duration_ms>141320&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b44fe646-e89f-4e8c-80bf-5be607b80d02",
  "isSidechain": false,
  "promptId": "cfd5920f-d72d-42a0-9d18-ef55ca2fd682",
  "type": "user",
  "uuid": "7faf5cfd-d71d-4235-84e7-a5b0396ff256",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "7faf5cfd-d71d-4235-84e7-a5b0396ff256",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Assistant

_source line 40 · 2026-05-28T05:31:12.296Z_

<details><summary>Logged reasoning block</summary>

```text
Good, SAGE and WarriorMath research is complete. Let me wait for the remaining agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7faf5cfd-d71d-4235-84e7-a5b0396ff256",
  "isSidechain": false,
  "requestId": "req_011CbURDS7aFUjtMT7fxduzP",
  "type": "assistant",
  "uuid": "bde1eeba-54eb-4736-884d-8a48470bf538",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GZQGxhbLdjjRKzuAS56L8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 25866,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 25866,
          "cache_creation_input_tokens": 3421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3421
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

_source line 41 · 2026-05-28T05:31:13.156Z_

Excellent - SAGE and WarriorMath research is complete with very detailed findings. Both lack error taxonomy and PRM, which strengthens our positioning. Still waiting for the remaining 5 agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bde1eeba-54eb-4736-884d-8a48470bf538",
  "isSidechain": false,
  "requestId": "req_011CbURDS7aFUjtMT7fxduzP",
  "type": "assistant",
  "uuid": "0910b106-1668-4b3b-9a58-8a948702aed7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GZQGxhbLdjjRKzuAS56L8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 25866,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 25866,
          "cache_creation_input_tokens": 3421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3421
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

_source line 42 · 2026-05-28T05:31:35.528Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:31:35.528Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "&lt;task-notification>\n&lt;task-id>a67b76442fb946591&lt;/task-id>\n&lt;tool-use-id>toolu_01K1G7jRr3arPRHThviYadjT&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a67b76442fb946591.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research Socratic-Zero paper\" completed&lt;/summary>\n&lt;result>I now have the complete paper content. Let me compile the comprehensive research report.\n\n---\n\nHere is the thorough analysis of the Socratic-Zero paper:\n\n## Full Title and Authors\n\n**Title:** Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution\n\n**Arxiv ID:** 2509.24726 (submitted September 29, 2025; preprint, under review)\n\n**Authors (with affiliations):**\n- Shaobo Wang* (EPIC Lab, Shanghai Jiao Tong University) -- 2nd-year PhD candidate, also research intern at Alibaba Qwen Team\n- Zhengbo Jiao* (Alibaba Group, EPIC Lab SJTU, Shanghai Univ. of Finance and Economics) -- *equal contribution\n- Zifan Zhang (Alibaba Group, Wuhan University)\n- Yilang Peng (Alibaba Group, Zhejiang University)\n- Xu Ze (Alibaba Group)\n- Boyu Yang (Alibaba Group)\n- Wei Wang (Alibaba Group)\n- Hu Wei (Alibaba Group) -- corresponding author\n- Linfeng Zhang (EPIC Lab, Shanghai Jiao Tong University) -- corresponding author\n\n---\n\n## Exact Results/Numbers Claimed\n\n**The +20.2pp claim:** The abstract states \"Socratic-Solver-8B achieves an average gain of +20.2 percentage points over prior data synthesis methods.\" However, looking at Table 1 closely, the actual average accuracy comparison is:\n\n| Method | Avg Accuracy |\n|---|---|\n| Qwen3-8B + Zero-shot | 29.9% |\n| + SFT | 35.9% |\n| + Static Augmentation | 40.7% |\n| + LLM2LLM Stage 3 | 40.9% |\n| **+ Socratic Stage 3** | **56.1%** |\n\nThe gap from Static Augmentation is +15.4pp, and from LLM2LLM is +15.2pp. The +20.2pp figure appears to come from comparing against the SFT baseline (56.1 - 35.9 = 20.2), which is framed as improvement \"over prior data synthesis methods\" but is actually measured against the pre-augmentation SFT checkpoint, not the augmentation baselines themselves. This is a somewhat misleading framing -- the most defensible improvement over the strongest comparable baseline is **+15.2pp to +15.4pp**.\n\n**Individual benchmark gains (Stage 3 vs Static Augmentation):**\n- AMC: 63.7 vs 45.8 (+17.9)\n- Minerva: 52.4 vs 41.9 (+10.5)\n- MATH-500: 81.2 vs 62.7 (+18.5)\n- GSM8K: 87.3 vs 74.6 (+12.7)\n- Olympiad: 55.1 vs 35.9 (+19.2)\n- AIME-25: 24.6 vs 11.4 (+13.2)\n- AIME-24: 28.4 vs 12.3 (+16.1)\n\n**Cross-architecture:** GLM4-9B reaches 52.3% avg; Qwen3-14B reaches 60.3% avg.\n\n**Generator results:** Socratic-Generator-32B (a 32B model) achieves 37.72% downstream training effectiveness, marginally outperforming data from Claude-4.1-Opus (37.63%), Qwen3-235B (37.13%), GPT-5 (36.62%), Gemini-2.5-Pro (37.20%), Grok-4 (37.01%), DeepSeek-V3.1 (36.62%).\n\n**General reasoning transfer:** +6.02pp average across BBEH, MMLU-Pro, SuperGPQA.\n\n---\n\n## How the Teacher Targets Weaknesses\n\nThe Teacher operates at the **error-instance level**, not at an error-type taxonomy level or concept level. Specifically:\n\n1. **Verification function** `V(q, y) -&gt; {0,1}`: Binary correctness judgment on each solution attempt.\n\n2. **Problem refinement function** `G(q, y_fail) -&gt; (q', y'_ref)`: The Teacher is prompted with a *specific failed solution attempt* and creates a new problem designed to target the *specific reasoning error exhibited in that failed attempt*.\n\n3. **Zone-adaptive generation** based on scalar difficulty (success rate `s_q`):\n   - **Mastered Zone** (s_q = 1): All attempts correct. Teacher generates harder variants from successful solutions.\n   - **Learning Zone** (0 &lt; s_q &lt; 1): Partial success. Teacher is prompted with specific failed solutions and generates problems targeting those specific errors.\n   - **Too Difficult Zone** (s_q = 0): All attempts fail. These problems are **excluded** from generation to prevent counterproductive difficulty escalation.\n\n**Critically, the targeting is NOT:**\n- Error-type-level (no taxonomy of error categories like \"algebraic manipulation errors\" vs \"logic errors\")\n- Concept-level (no explicit identification of which mathematical concepts are weak)\n- It IS instance-level: each failed solution is individually used as input to generate a new problem that targets that specific failure\n\nThe difficulty calibration uses a Gaussian utility function `U(q') = exp(-(s_q' - 0.5)^2 / (2 * 0.2^2))` centered at 50% success rate, which provides a scalar difficulty signal but not a structured error taxonomy.\n\n---\n\n## The Co-Evolution Mechanism\n\nThree phases per iteration:\n\n**Phase 1 -- Solver Evolution (Online Preference Learning):**\n- Solver generates k=8 solution attempts per problem\n- Teacher verifies each (binary correct/incorrect)\n- Solutions partitioned into winning set and losing set\n- If Solver produces zero correct solutions, the reference solution serves as the winning example\n- Solver trained via **DPO (Direct Preference Optimization)** loss on preference pairs\n\n**Phase 2 -- Generator Evolution (Offline Value-Weighted Distillation):**\n- Failed solution attempts collected\n- Teacher generates new problems from failures via `G(q, y_fail)`\n- Each new problem scored by utility function (Gaussian centered at 50% Solver success rate)\n- Generator trained via **weighted SFT (WSFT)** to mimic Teacher's problem refinement, weighted by utility scores\n- This teaches the Generator to produce problems at the optimal difficulty frontier\n\n**Phase 3 -- Curriculum Expansion:**\n- New Teacher-generated problems added to curriculum\n- All existing problems recategorized (Mastered/Learning/Too Difficult) based on updated Solver\n- Problems dynamically transition between zones as Solver improves\n\nThe system runs for 3 stages total. Initial SFT on 1,500 Level-5 MATH problems is required before the co-evolution loop begins (ablation shows only +2.34pp without SFT vs +18.38pp with SFT).\n\n---\n\n## Whether It Uses a PRM or Verifier\n\n**No PRM (Process Reward Model) is used.** The system uses:\n\n1. **MathRule** -- a rule-based tool that extracts and standardizes final numerical answers using pattern matching (looking for \"Therefore,\" \"The answer is,\" boxed expressions, etc.)\n\n2. **LLM Judge** -- the Teacher model (Qwen3-235B-A22B) performs semantic validation at temperature 0.1\n\nThis is a **dual outcome-level verification** approach (binary correct/incorrect on final answers), not step-level process supervision. There is no process reward model evaluating intermediate reasoning steps. The verification function is `V(q, y) -&gt; {0, 1}` -- purely binary outcome.\n\n---\n\n## Key Limitations Compared to a PRM-Based Error Taxonomy Approach\n\n**Limitations explicitly stated in the paper:**\n\n1. **No formal convergence analysis** -- the authors acknowledge this gap and defer it to future work\n\n2. **Domain restriction** -- currently only mathematical reasoning; adaptation to other domains would \"require careful adaptation of the Teacher's evaluation capabilities and problem generation templates\"\n\n3. **Heavy computational requirements** -- 8x NVIDIA H20 GPUs for Solver + 16x AMD MI308X GPUs (3,072GB total) for Teacher inference\n\n4. **Fixed Teacher dependency** -- relies on Qwen3-235B-A22B as a static oracle; no mechanism for the Teacher itself to improve\n\n5. **Not truly \"data-free\"** -- requires 100 curated seed problems with 10-70% success rate + 1,500 problems for initial SFT\n\n6. **Critical SFT dependency** -- without initial SFT, the system barely works (+2.34pp vs +18.38pp)\n\n**Implicit limitations particularly relevant vs a PRM-based error taxonomy approach:**\n\n7. **No structured error diagnosis** -- The Teacher generates new problems from individual failed solutions but never builds a taxonomy of error types. A PRM-based approach could identify *classes* of errors (e.g., \"sign errors in algebraic manipulation,\" \"incorrect application of modular arithmetic\") and systematically target each category. Socratic-Zero's instance-level targeting may miss systematic error patterns.\n\n8. **No step-level feedback** -- With only binary outcome verification, the system cannot pinpoint *where* in a reasoning chain the error occurs. A PRM provides step-level reward signals that identify the exact step where reasoning goes wrong. This means Socratic-Zero's DPO training treats entire solutions as good/bad without localizing errors.\n\n9. **No error pattern aggregation** -- Because there is no taxonomy, the system cannot measure whether the Solver has systematic weaknesses in specific reasoning skills. It relies on the Teacher's implicit (prompt-based) analysis of individual failures rather than explicit statistical tracking of error categories.\n\n10. **Quality control relies on Teacher self-verification** -- this creates a closed loop where systematic Teacher errors could propagate. A PRM trained on diverse annotations would provide an independent quality signal.\n\n11. **Difficulty is scalar, not multidimensional** -- The Gaussian utility function targets a single number (50% success rate). It cannot distinguish between a problem that is hard because of novel concepts vs one that is hard because of computational complexity. A PRM-based taxonomy could target specific skill dimensions independently.\n\n12. **Generator distills Teacher behavior, not error structure** -- The Generator learns to mimic *how* the Teacher creates problems from failures but does not learn a structured representation of error types that could enable more principled curriculum design.\n\n---\n\nSources:\n- [Socratic-Zero on arXiv (abstract)](https://arxiv.org/abs/2509.24726)\n- [Socratic-Zero full HTML paper](https://arxiv.org/html/2509.24726)\n- [Socratic-Zero PDF](https://arxiv.org/pdf/2509.24726)\n- [Socratic-Zero on OpenReview](https://openreview.net/forum?id=I1garriWB7)\n- [Socratic-Zero on HuggingFace Papers](https://huggingface.co/papers/2509.24726)\n- [Socratic-Zero Literature Review (Moonlight)](https://www.themoonlight.io/en/review/socratic-zero-bootstrapping-reasoning-via-data-free-agent-co-evolution)\n- [Shaobo Wang's homepage](https://gszfwsb.github.io/)\n- [Semantic Scholar entry](https://www.semanticscholar.org/paper/Socratic-Zero-:-Bootstrapping-Reasoning-via-Agent-Wang-Jiao/08d60a8f1169eb65c120b67a1b6b8a8c448f9913)&lt;/result>\n&lt;usage>&lt;total_tokens>49061&lt;/total_tokens>&lt;tool_uses>16&lt;/tool_uses>&lt;duration_ms>171591&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 43 · 2026-05-28T05:31:35.531Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:31:35.531Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 4

5 recorded events

### User

_source line 44 · 2026-05-28T05:31:35.540Z_

&lt;task-notification>
&lt;task-id>a67b76442fb946591&lt;/task-id>
&lt;tool-use-id>toolu_01K1G7jRr3arPRHThviYadjT&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a67b76442fb946591.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research Socratic-Zero paper" completed&lt;/summary>
&lt;result>I now have the complete paper content. Let me compile the comprehensive research report.

---

Here is the thorough analysis of the Socratic-Zero paper:

## Full Title and Authors

**Title:** Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution

**Arxiv ID:** 2509.24726 (submitted September 29, 2025; preprint, under review)

**Authors (with affiliations):**
- Shaobo Wang* (EPIC Lab, Shanghai Jiao Tong University) -- 2nd-year PhD candidate, also research intern at Alibaba Qwen Team
- Zhengbo Jiao* (Alibaba Group, EPIC Lab SJTU, Shanghai Univ. of Finance and Economics) -- *equal contribution
- Zifan Zhang (Alibaba Group, Wuhan University)
- Yilang Peng (Alibaba Group, Zhejiang University)
- Xu Ze (Alibaba Group)
- Boyu Yang (Alibaba Group)
- Wei Wang (Alibaba Group)
- Hu Wei (Alibaba Group) -- corresponding author
- Linfeng Zhang (EPIC Lab, Shanghai Jiao Tong University) -- corresponding author

---

## Exact Results/Numbers Claimed

**The +20.2pp claim:** The abstract states "Socratic-Solver-8B achieves an average gain of +20.2 percentage points over prior data synthesis methods." However, looking at Table 1 closely, the actual average accuracy comparison is:

| Method | Avg Accuracy |
|---|---|
| Qwen3-8B + Zero-shot | 29.9% |
| + SFT | 35.9% |
| + Static Augmentation | 40.7% |
| + LLM2LLM Stage 3 | 40.9% |
| **+ Socratic Stage 3** | **56.1%** |

The gap from Static Augmentation is +15.4pp, and from LLM2LLM is +15.2pp. The +20.2pp figure appears to come from comparing against the SFT baseline (56.1 - 35.9 = 20.2), which is framed as improvement "over prior data synthesis methods" but is actually measured against the pre-augmentation SFT checkpoint, not the augmentation baselines themselves. This is a somewhat misleading framing -- the most defensible improvement over the strongest comparable baseline is **+15.2pp to +15.4pp**.

**Individual benchmark gains (Stage 3 vs Static Augmentation):**
- AMC: 63.7 vs 45.8 (+17.9)
- Minerva: 52.4 vs 41.9 (+10.5)
- MATH-500: 81.2 vs 62.7 (+18.5)
- GSM8K: 87.3 vs 74.6 (+12.7)
- Olympiad: 55.1 vs 35.9 (+19.2)
- AIME-25: 24.6 vs 11.4 (+13.2)
- AIME-24: 28.4 vs 12.3 (+16.1)

**Cross-architecture:** GLM4-9B reaches 52.3% avg; Qwen3-14B reaches 60.3% avg.

**Generator results:** Socratic-Generator-32B (a 32B model) achieves 37.72% downstream training effectiveness, marginally outperforming data from Claude-4.1-Opus (37.63%), Qwen3-235B (37.13%), GPT-5 (36.62%), Gemini-2.5-Pro (37.20%), Grok-4 (37.01%), DeepSeek-V3.1 (36.62%).

**General reasoning transfer:** +6.02pp average across BBEH, MMLU-Pro, SuperGPQA.

---

## How the Teacher Targets Weaknesses

The Teacher operates at the **error-instance level**, not at an error-type taxonomy level or concept level. Specifically:

1. **Verification function** `V(q, y) -&gt; {0,1}`: Binary correctness judgment on each solution attempt.

2. **Problem refinement function** `G(q, y_fail) -&gt; (q', y'_ref)`: The Teacher is prompted with a *specific failed solution attempt* and creates a new problem designed to target the *specific reasoning error exhibited in that failed attempt*.

3. **Zone-adaptive generation** based on scalar difficulty (success rate `s_q`):
   - **Mastered Zone** (s_q = 1): All attempts correct. Teacher generates harder variants from successful solutions.
   - **Learning Zone** (0 &lt; s_q &lt; 1): Partial success. Teacher is prompted with specific failed solutions and generates problems targeting those specific errors.
   - **Too Difficult Zone** (s_q = 0): All attempts fail. These problems are **excluded** from generation to prevent counterproductive difficulty escalation.

**Critically, the targeting is NOT:**
- Error-type-level (no taxonomy of error categories like "algebraic manipulation errors" vs "logic errors")
- Concept-level (no explicit identification of which mathematical concepts are weak)
- It IS instance-level: each failed solution is individually used as input to generate a new problem that targets that specific failure

The difficulty calibration uses a Gaussian utility function `U(q') = exp(-(s_q' - 0.5)^2 / (2 * 0.2^2))` centered at 50% success rate, which provides a scalar difficulty signal but not a structured error taxonomy.

---

## The Co-Evolution Mechanism

Three phases per iteration:

**Phase 1 -- Solver Evolution (Online Preference Learning):**
- Solver generates k=8 solution attempts per problem
- Teacher verifies each (binary correct/incorrect)
- Solutions partitioned into winning set and losing set
- If Solver produces zero correct solutions, the reference solution serves as the winning example
- Solver trained via **DPO (Direct Preference Optimization)** loss on preference pairs

**Phase 2 -- Generator Evolution (Offline Value-Weighted Distillation):**
- Failed solution attempts collected
- Teacher generates new problems from failures via `G(q, y_fail)`
- Each new problem scored by utility function (Gaussian centered at 50% Solver success rate)
- Generator trained via **weighted SFT (WSFT)** to mimic Teacher's problem refinement, weighted by utility scores
- This teaches the Generator to produce problems at the optimal difficulty frontier

**Phase 3 -- Curriculum Expansion:**
- New Teacher-generated problems added to curriculum
- All existing problems recategorized (Mastered/Learning/Too Difficult) based on updated Solver
- Problems dynamically transition between zones as Solver improves

The system runs for 3 stages total. Initial SFT on 1,500 Level-5 MATH problems is required before the co-evolution loop begins (ablation shows only +2.34pp without SFT vs +18.38pp with SFT).

---

## Whether It Uses a PRM or Verifier

**No PRM (Process Reward Model) is used.** The system uses:

1. **MathRule** -- a rule-based tool that extracts and standardizes final numerical answers using pattern matching (looking for "Therefore," "The answer is," boxed expressions, etc.)

2. **LLM Judge** -- the Teacher model (Qwen3-235B-A22B) performs semantic validation at temperature 0.1

This is a **dual outcome-level verification** approach (binary correct/incorrect on final answers), not step-level process supervision. There is no process reward model evaluating intermediate reasoning steps. The verification function is `V(q, y) -&gt; {0, 1}` -- purely binary outcome.

---

## Key Limitations Compared to a PRM-Based Error Taxonomy Approach

**Limitations explicitly stated in the paper:**

1. **No formal convergence analysis** -- the authors acknowledge this gap and defer it to future work

2. **Domain restriction** -- currently only mathematical reasoning; adaptation to other domains would "require careful adaptation of the Teacher's evaluation capabilities and problem generation templates"

3. **Heavy computational requirements** -- 8x NVIDIA H20 GPUs for Solver + 16x AMD MI308X GPUs (3,072GB total) for Teacher inference

4. **Fixed Teacher dependency** -- relies on Qwen3-235B-A22B as a static oracle; no mechanism for the Teacher itself to improve

5. **Not truly "data-free"** -- requires 100 curated seed problems with 10-70% success rate + 1,500 problems for initial SFT

6. **Critical SFT dependency** -- without initial SFT, the system barely works (+2.34pp vs +18.38pp)

**Implicit limitations particularly relevant vs a PRM-based error taxonomy approach:**

7. **No structured error diagnosis** -- The Teacher generates new problems from individual failed solutions but never builds a taxonomy of error types. A PRM-based approach could identify *classes* of errors (e.g., "sign errors in algebraic manipulation," "incorrect application of modular arithmetic") and systematically target each category. Socratic-Zero's instance-level targeting may miss systematic error patterns.

8. **No step-level feedback** -- With only binary outcome verification, the system cannot pinpoint *where* in a reasoning chain the error occurs. A PRM provides step-level reward signals that identify the exact step where reasoning goes wrong. This means Socratic-Zero's DPO training treats entire solutions as good/bad without localizing errors.

9. **No error pattern aggregation** -- Because there is no taxonomy, the system cannot measure whether the Solver has systematic weaknesses in specific reasoning skills. It relies on the Teacher's implicit (prompt-based) analysis of individual failures rather than explicit statistical tracking of error categories.

10. **Quality control relies on Teacher self-verification** -- this creates a closed loop where systematic Teacher errors could propagate. A PRM trained on diverse annotations would provide an independent quality signal.

11. **Difficulty is scalar, not multidimensional** -- The Gaussian utility function targets a single number (50% success rate). It cannot distinguish between a problem that is hard because of novel concepts vs one that is hard because of computational complexity. A PRM-based taxonomy could target specific skill dimensions independently.

12. **Generator distills Teacher behavior, not error structure** -- The Generator learns to mimic *how* the Teacher creates problems from failures but does not learn a structured representation of error types that could enable more principled curriculum design.

---

Sources:
- [Socratic-Zero on arXiv (abstract)](https://arxiv.org/abs/2509.24726)
- [Socratic-Zero full HTML paper](https://arxiv.org/html/2509.24726)
- [Socratic-Zero PDF](https://arxiv.org/pdf/2509.24726)
- [Socratic-Zero on OpenReview](https://openreview.net/forum?id=I1garriWB7)
- [Socratic-Zero on HuggingFace Papers](https://huggingface.co/papers/2509.24726)
- [Socratic-Zero Literature Review (Moonlight)](https://www.themoonlight.io/en/review/socratic-zero-bootstrapping-reasoning-via-data-free-agent-co-evolution)
- [Shaobo Wang's homepage](https://gszfwsb.github.io/)
- [Semantic Scholar entry](https://www.semanticscholar.org/paper/Socratic-Zero-:-Bootstrapping-Reasoning-via-Agent-Wang-Jiao/08d60a8f1169eb65c120b67a1b6b8a8c448f9913)&lt;/result>
&lt;usage>&lt;total_tokens>49061&lt;/total_tokens>&lt;tool_uses>16&lt;/tool_uses>&lt;duration_ms>171591&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0910b106-1668-4b3b-9a58-8a948702aed7",
  "isSidechain": false,
  "promptId": "f89db8f7-25be-4b95-8a64-c251602eb91a",
  "type": "user",
  "uuid": "e8f17dec-e8a7-4303-9630-7562d632f56c",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-28T05:31:38.176Z_

<details><summary>Logged reasoning block</summary>

```text
Great, now I have detailed Socratic-Zero research from both agents. Let me wait for the remaining agents to complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8f17dec-e8a7-4303-9630-7562d632f56c",
  "isSidechain": false,
  "requestId": "req_011CbURFLt7VW89CUX3k2yGt",
  "type": "assistant",
  "uuid": "ec8ea139-e59d-4cf8-8943-6e170d210718",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNPdKGiYrBHL8PVRhwAcqR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 29287,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 115,
          "cache_read_input_tokens": 29287,
          "cache_creation_input_tokens": 3101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3101
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

_source line 46 · 2026-05-28T05:31:39.887Z_

Excellent - now I have very detailed Socratic-Zero findings from both agents. Key insight: it targets weaknesses at instance-level (individual failed solutions) but has no error taxonomy, no PRM, and no step-level feedback. Strong differentiator for DiagCoEvo. Still waiting for 5 more agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec8ea139-e59d-4cf8-8943-6e170d210718",
  "isSidechain": false,
  "requestId": "req_011CbURFLt7VW89CUX3k2yGt",
  "type": "assistant",
  "uuid": "aa6ce73f-11e7-422c-9707-c8a85a2a1c07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNPdKGiYrBHL8PVRhwAcqR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 29287,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 115,
          "cache_read_input_tokens": 29287,
          "cache_creation_input_tokens": 3101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3101
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

_source line 47 · 2026-05-28T05:32:12.457Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:32:12.457Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "&lt;task-notification>\n&lt;task-id>ae5080ea8c0f3bbcf&lt;/task-id>\n&lt;tool-use-id>toolu_01V5YEBTgdoNmBFCJySnzL3Y&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/ae5080ea8c0f3bbcf.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research LEMMA, Error Classification, and other minor competitors\" completed&lt;/summary>\n&lt;result>DiagCoEvo doesn't appear in the local files. It is likely the name of the paper/idea being reviewed. I now have all the information needed to provide a comprehensive report. Here is the complete research summary:\n\n---\n\n## Paper 1: LEMMA (ACL 2025 Findings)\n\n**Full Title:** LEMMA: Learning from Errors for MatheMatical Advancement in LLMs\n\n**Authors:** Zhuoshi Pan, Yu Li, Honglin Lin, Qizhi Pei, Zinan Tang, Wei Wu, Chenlin Ming, H. Vicky Zhao, Conghui He, Lijun Wu\n\n**Arxiv ID:** 2503.17439 | **Venue:** Findings of ACL 2025\n\n**Key Mechanism:**\nLEMMA constructs error-corrective training trajectories through three stages:\n1. **Error taxonomy analysis** -- defines 7 error types: Calculation Error (CA), Counting Error (CO), Formula Confusion (FC), Question Misinterpretation (QM), Missing Step (MS), Confusing Concept (CC), Nonsensical Output (NO). The distribution is analyzed empirically per model.\n2. **Error-type grounded mistake augmentation** -- a teacher model (GPT-4o) intentionally injects errors by sampling from the analyzed error-type distribution, combined with the student model's own organic mistakes.\n3. **Dual correction trajectories** -- \"Fix &amp; Continue\" (correct the first error step and continue) and \"Fresh &amp; Restart\" (critique errors, then solve from scratch). Both are smoothed into training data with reflection phrases.\n\nThe final SFT dataset is ~88,900 examples. The model learns to self-correct without external critique models.\n\n**Relation to error-type-driven curriculum:** LEMMA is the closest precursor to the idea of using error types to drive training. It explicitly defines an error taxonomy and uses error-type distributions to generate augmented mistakes. However, it is a **static SFT approach** -- the error distribution is analyzed once and used to generate a fixed dataset, with no iterative co-evolution between problem difficulty and error diagnosis.\n\n**Key limitations vs DiagCoEvo:**\n- **No curriculum or co-evolution** -- the training data is constructed once, not adapted over training rounds based on evolving model weaknesses.\n- **Small fixed dataset** (~89K examples) -- authors acknowledge scalability is unexplored.\n- **No RL integration** -- purely supervised fine-tuning; authors note RL could extend the work but do not pursue it.\n- **Static error distribution** -- the error type proportions are measured once and then frozen, not dynamically updated as the model improves.\n- **Teacher-dependent** -- relies on GPT-4o for both error injection and correction trajectory generation.\n\n---\n\n## Paper 2: Error Classification of LLMs on MWP (EMNLP 2025 Findings)\n\n**Full Title:** Error Classification of Large Language Models on Math Word Problems: A Dynamically Adaptive Framework\n\n**Authors:** Yuhong Sun, Zhangyue Yin, Xuanjing Huang, Xipeng Qiu, Hui Zhao\n\n**Arxiv ID:** 2501.15581 | **Venue:** Findings of EMNLP 2025\n\n**Key Mechanism:**\n1. **MWPES-300K dataset** -- 304,865 error samples collected from 15 LLMs (GPT-3.5-turbo, GPT-4o, o1-mini, Claude-3.5-sonnet, Llama-3.1 family, Gemma-2, Qwen2.5 variants) across 4 MWP datasets.\n2. **Dynamic adaptive error classification** -- instead of predefined static categories (which achieved only 35.65% accuracy), uses GPT-4o as Error Analyzer + text-embedding-3-large + K-means clustering to discover 39 fine-grained error clusters from actual model behavior. This contrasts with static taxonomies that use broad categories like \"Hallucination.\"\n3. **Error-Aware Prompting (EAP)** -- at inference time, labels knowledge points in the problem, retrieves relevant error cluster summaries via similarity matching, and appends them to the prompt as avoidance guidance. Llama-3.1-8B improved +26.33% on MATH with EAP.\n\nKey finding: error patterns evolve with model capability -- weaker models show basic computational mistakes while stronger models exhibit sophisticated reasoning failures (e.g., boundary condition analysis gaps).\n\n**Relation to error-type-driven curriculum:** This paper provides the **analytical foundation** for understanding how error types vary across models and datasets. Its dynamic error classification is more principled than LEMMA's fixed 7-category taxonomy. However, it only uses error knowledge at **inference time** (prompting), not for training data construction or curriculum design.\n\n**Key limitations vs DiagCoEvo:**\n- **Inference-time only** -- EAP is a prompting strategy, not a training methodology. It does not change model weights or construct training curricula.\n- **No training signal** -- error analysis informs prompts but never feeds back into data generation or model fine-tuning.\n- **Process-answer inconsistency blind spot** -- only analyzes cases where both process and answer are wrong; ignores correct answers from flawed reasoning.\n- **Domain-specific** -- tested only on math word problems; generalization unexplored.\n- **No co-evolution** -- error categories are discovered once from a static corpus, not dynamically updated as a model improves.\n\n---\n\n## Paper 3: Bidirectional Curriculum Generation (March 2026)\n\n**Full Title:** Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning\n\n**Authors:** Boren Hu, Xiao Liu, Boci Peng, Xinping Zhao, Xiaoran Shang, Yun Zhu, Lijun Wu\n\n**Arxiv ID:** 2603.05120 | **Submitted:** March 5, 2026\n\n**Key Mechanism:**\nA multi-agent framework with four specialized agents:\n1. **Problem Simplification Agent** -- when the model fails, reduces complexity by removing constraints, lowering numerical magnitudes, breaking multistep problems into components, or creating scaffolding.\n2. **Problem Complication Agent** -- after success, increases difficulty by adding constraints, conditional branches, or combining techniques.\n3. **Evaluation Agent** -- assesses correctness and identifies failure points.\n4. **Routing Agent** -- decides whether to simplify or complicate based on performance.\n\nGrounded in an \"Optimal Pacing Theorem\" that matches problem difficulty to current model capability. The bidirectional nature (both simplifying and complicating) distinguishes it from standard unidirectional curricula.\n\n**Relation to error-type-driven curriculum:** This is the most structurally similar competitor -- it implements a **closed-loop adaptive curriculum** that responds to model failures. The simplification agent implicitly addresses error categories (calculation errors via simplified numerics, reasoning gaps via decomposition, conceptual misunderstandings via foundational variants). However, the error diagnosis is **implicit and coarse-grained** -- it adapts difficulty direction (simpler/harder) based on pass/fail, not based on classified error types.\n\n**Key limitations vs DiagCoEvo:**\n- **No explicit error taxonomy** -- adaptations are driven by pass/fail signals, not by diagnosed error types. The system does not know *why* the model failed, only *that* it failed.\n- **Multi-agent overhead** -- requires coordinating four separate agents, with computational costs acknowledged by the authors.\n- **Diminishing returns** -- performance gains plateau on olympiad-level problems.\n- **No error-type-specific problem generation** -- simplification/complication is generic, not targeted at specific error categories (e.g., generating more formula confusion problems vs. more calculation problems).\n- **Unidirectional in error understanding** -- adjusts difficulty but does not co-evolve the error diagnosis itself.\n\n---\n\n## Paper 4: VHG (May 2026)\n\n**Full Title:** Verifier-Backed Hard Problem Generation for Mathematical Reasoning\n\n**Authors:** Yuhang Lai, Jiazhan Feng, Yee Whye Teh, Ning Miao\n\n**Affiliations:** City University of Hong Kong, Peking University, University of Oxford\n\n**Arxiv ID:** 2605.06660 | **Submitted:** May 7, 2026\n\n**Key Mechanism:**\nVHG extends two-party self-play (setter-solver) into **three-party self-play** by adding an independent Verifier:\n1. **Setter (Q)** -- generates problem-reference pairs (x, y*).\n2. **Solver (S)** -- attempts to solve; pass-rate measures difficulty.\n3. **Verifier (V)** -- validates problem correctness before difficulty scoring.\n\nThe setter's reward: R_Q(x,y*) = 1[V(x,y*)=1] * (1 - Acc_S(x,y*)). This prevents \"reward hacking\" where setters generate invalid-but-hard problems.\n\nTwo verifier variants: **Hard Verifier** (symbolic, e.g., SymPy for integrals -- near-perfect) and **Soft Verifier** (LLM-as-judge + format filters -- broader but less accurate).\n\nThe setter exhibits two-phase learning: first establishing validity (30.6% to 65.2%), then increasing difficulty while maintaining validity. Results: Pass@1 improved from 56.8% to 69.0% on general math benchmarks; strong \"weak-to-strong\" transfer (problems challenging for larger 8B-32B models).\n\n**Relation to error-type-driven curriculum:** VHG focuses on **generating maximally difficult valid problems** through adversarial self-play. It is a difficulty-calibration mechanism, not an error-type-aware one. It drives the solver toward harder problems but does not diagnose *what kind* of errors the solver makes or generate problems targeting specific weaknesses.\n\n**Key limitations vs DiagCoEvo:**\n- **No error diagnosis at all** -- the system optimizes for difficulty (1 - accuracy) without any error categorization. It cannot distinguish between a solver failing due to calculation errors vs. conceptual misunderstanding.\n- **Validity-focused, not weakness-focused** -- the verifier ensures problems are valid, not that they target specific model weaknesses.\n- **No curriculum structure** -- problems are generated to be maximally hard, not sequenced in a pedagogically meaningful order.\n- **Domain constraints** -- the Hard Verifier is only applicable to domains with symbolic verification (e.g., integration). The Soft Verifier trades accuracy for generality.\n- **No co-evolution of error understanding** -- the setter learns to make harder problems, but there is no evolving model of what the solver struggles with specifically.\n\n---\n\n## Paper 5: Cog-DRIFT (April 2026)\n\n**Full Title:** Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems\n\n**Authors:** Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal\n\n**Arxiv ID:** 2604.04767 | **Submitted:** April 6, 2026\n\n**Key Mechanism:**\nAddresses the problem that RLVR cannot learn from problems the model never solves (pass@64=0). Instead of abandoning hard problems, Cog-DRIFT **reformulates** them into cognitively simpler formats:\n1. **4-Choice MCQ** -- easiest; constrains output space to 4 options.\n2. **10-Choice MCQ** -- moderate; more options, harder discrimination.\n3. **Cloze format** -- partial answer masking (e.g., \"The answer looks like: 1__\").\n4. **Open-ended** -- original format (hardest).\n\nAn **instance-level adaptive curriculum** promotes each problem through the difficulty hierarchy: when the model achieves &gt;=50% accuracy at a given format, it advances to the next format. Progression is per-problem, not batch-level. The theoretical grounding invokes the \"Zone of Proximal Development\" from educational psychology.\n\nResults: +10.11% on hard problems for Qwen, +8.64% for Llama. Cross-benchmark average: +4.72% (Qwen), +3.23% (Llama) over second-best baselines.\n\n**Relation to error-type-driven curriculum:** Cog-DRIFT implements adaptive curriculum learning but through **task format reformulation** rather than error-type diagnosis. It reduces cognitive load by changing the answer format, not by targeting the specific reasoning failure. The curriculum adapts based on accuracy thresholds, not based on what type of error the model made.\n\n**Key limitations vs DiagCoEvo:**\n- **No error diagnosis** -- progression is driven by pass/fail accuracy thresholds, not by understanding *why* the model fails. A model failing due to calculation errors gets the same treatment as one failing due to conceptual misunderstanding.\n- **Format-based, not content-based** -- reformulation changes how the answer is elicited (MCQ vs. open-ended), not the problem content itself. This cannot address content-specific weaknesses.\n- **No problem generation** -- works with existing problems, only reformulating their format. Does not generate new problems targeting specific weaknesses.\n- **Reliance on LLM quality for reformulation** -- GPT-5.4 is used for both reformulation and data quality filtering.\n- **Limited curriculum signal** -- binary (pass threshold / fail threshold) rather than multi-dimensional error-type information.\n- **No co-evolution** -- the reformulation strategy and curriculum are fixed designs; they do not evolve based on changing error patterns.\n\n---\n\n## Summary: Positioning Table\n\n| Paper | Error Taxonomy | Curriculum | Co-Evolution | Training Method | Problem Generation |\n|-------|---------------|------------|--------------|-----------------|-------------------|\n| LEMMA | 7 explicit types | None (static SFT) | None | SFT on ~89K examples | Teacher-injected errors |\n| Error Classification (MWP) | 39 dynamic clusters | None | None | None (inference-time prompting) | None |\n| Bidirectional Curriculum | Implicit (pass/fail) | Bidirectional (simplify/complicate) | Partial (adapts difficulty) | SFT | Multi-agent generation |\n| VHG | None | None (maximize difficulty) | Setter-solver co-training | RL (self-play) | Adversarial generation |\n| Cog-DRIFT | None | Format-based adaptive | None | RLVR (GRPO) | Format reformulation only |\n\nThe gap that DiagCoEvo would fill: **none of these five works combines explicit error-type diagnosis with adaptive curriculum construction in a co-evolutionary loop**. LEMMA has the error taxonomy but no curriculum. Bidirectional Curriculum has the adaptive curriculum but no error taxonomy. VHG has co-evolution but no error awareness. Cog-DRIFT has curriculum but only over task format, not error-targeted content. The Error Classification paper has the richest error analysis but uses it only at inference time.\n\nSources:\n- [LEMMA - ACL Anthology](https://aclanthology.org/2025.findings-acl.605/)\n- [LEMMA - arXiv](https://arxiv.org/abs/2503.17439)\n- [LEMMA - GitHub](https://github.com/pzs19/LEMMA)\n- [Error Classification of LLMs on MWP - ACL Anthology](https://aclanthology.org/2025.findings-emnlp.20/)\n- [Error Classification of LLMs on MWP - arXiv](https://arxiv.org/abs/2501.15581)\n- [Bidirectional Curriculum Generation - arXiv](https://arxiv.org/abs/2603.05120)\n- [VHG: Verifier-Backed Hard Problem Generation - arXiv](https://arxiv.org/html/2605.06660)\n- [Cog-DRIFT - arXiv](https://arxiv.org/abs/2604.04767)\n- [Cog-DRIFT - HuggingFace Papers](https://huggingface.co/papers/2604.04767)&lt;/result>\n&lt;usage>&lt;total_tokens>35344&lt;/total_tokens>&lt;tool_uses>23&lt;/tool_uses>&lt;duration_ms>198858&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 48 · 2026-05-28T05:32:12.475Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:32:12.475Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 5

7 recorded events

### User

_source line 49 · 2026-05-28T05:32:12.483Z_

&lt;task-notification>
&lt;task-id>ae5080ea8c0f3bbcf&lt;/task-id>
&lt;tool-use-id>toolu_01V5YEBTgdoNmBFCJySnzL3Y&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/ae5080ea8c0f3bbcf.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research LEMMA, Error Classification, and other minor competitors" completed&lt;/summary>
&lt;result>DiagCoEvo doesn't appear in the local files. It is likely the name of the paper/idea being reviewed. I now have all the information needed to provide a comprehensive report. Here is the complete research summary:

---

## Paper 1: LEMMA (ACL 2025 Findings)

**Full Title:** LEMMA: Learning from Errors for MatheMatical Advancement in LLMs

**Authors:** Zhuoshi Pan, Yu Li, Honglin Lin, Qizhi Pei, Zinan Tang, Wei Wu, Chenlin Ming, H. Vicky Zhao, Conghui He, Lijun Wu

**Arxiv ID:** 2503.17439 | **Venue:** Findings of ACL 2025

**Key Mechanism:**
LEMMA constructs error-corrective training trajectories through three stages:
1. **Error taxonomy analysis** -- defines 7 error types: Calculation Error (CA), Counting Error (CO), Formula Confusion (FC), Question Misinterpretation (QM), Missing Step (MS), Confusing Concept (CC), Nonsensical Output (NO). The distribution is analyzed empirically per model.
2. **Error-type grounded mistake augmentation** -- a teacher model (GPT-4o) intentionally injects errors by sampling from the analyzed error-type distribution, combined with the student model's own organic mistakes.
3. **Dual correction trajectories** -- "Fix &amp; Continue" (correct the first error step and continue) and "Fresh &amp; Restart" (critique errors, then solve from scratch). Both are smoothed into training data with reflection phrases.

The final SFT dataset is ~88,900 examples. The model learns to self-correct without external critique models.

**Relation to error-type-driven curriculum:** LEMMA is the closest precursor to the idea of using error types to drive training. It explicitly defines an error taxonomy and uses error-type distributions to generate augmented mistakes. However, it is a **static SFT approach** -- the error distribution is analyzed once and used to generate a fixed dataset, with no iterative co-evolution between problem difficulty and error diagnosis.

**Key limitations vs DiagCoEvo:**
- **No curriculum or co-evolution** -- the training data is constructed once, not adapted over training rounds based on evolving model weaknesses.
- **Small fixed dataset** (~89K examples) -- authors acknowledge scalability is unexplored.
- **No RL integration** -- purely supervised fine-tuning; authors note RL could extend the work but do not pursue it.
- **Static error distribution** -- the error type proportions are measured once and then frozen, not dynamically updated as the model improves.
- **Teacher-dependent** -- relies on GPT-4o for both error injection and correction trajectory generation.

---

## Paper 2: Error Classification of LLMs on MWP (EMNLP 2025 Findings)

**Full Title:** Error Classification of Large Language Models on Math Word Problems: A Dynamically Adaptive Framework

**Authors:** Yuhong Sun, Zhangyue Yin, Xuanjing Huang, Xipeng Qiu, Hui Zhao

**Arxiv ID:** 2501.15581 | **Venue:** Findings of EMNLP 2025

**Key Mechanism:**
1. **MWPES-300K dataset** -- 304,865 error samples collected from 15 LLMs (GPT-3.5-turbo, GPT-4o, o1-mini, Claude-3.5-sonnet, Llama-3.1 family, Gemma-2, Qwen2.5 variants) across 4 MWP datasets.
2. **Dynamic adaptive error classification** -- instead of predefined static categories (which achieved only 35.65% accuracy), uses GPT-4o as Error Analyzer + text-embedding-3-large + K-means clustering to discover 39 fine-grained error clusters from actual model behavior. This contrasts with static taxonomies that use broad categories like "Hallucination."
3. **Error-Aware Prompting (EAP)** -- at inference time, labels knowledge points in the problem, retrieves relevant error cluster summaries via similarity matching, and appends them to the prompt as avoidance guidance. Llama-3.1-8B improved +26.33% on MATH with EAP.

Key finding: error patterns evolve with model capability -- weaker models show basic computational mistakes while stronger models exhibit sophisticated reasoning failures (e.g., boundary condition analysis gaps).

**Relation to error-type-driven curriculum:** This paper provides the **analytical foundation** for understanding how error types vary across models and datasets. Its dynamic error classification is more principled than LEMMA's fixed 7-category taxonomy. However, it only uses error knowledge at **inference time** (prompting), not for training data construction or curriculum design.

**Key limitations vs DiagCoEvo:**
- **Inference-time only** -- EAP is a prompting strategy, not a training methodology. It does not change model weights or construct training curricula.
- **No training signal** -- error analysis informs prompts but never feeds back into data generation or model fine-tuning.
- **Process-answer inconsistency blind spot** -- only analyzes cases where both process and answer are wrong; ignores correct answers from flawed reasoning.
- **Domain-specific** -- tested only on math word problems; generalization unexplored.
- **No co-evolution** -- error categories are discovered once from a static corpus, not dynamically updated as a model improves.

---

## Paper 3: Bidirectional Curriculum Generation (March 2026)

**Full Title:** Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning

**Authors:** Boren Hu, Xiao Liu, Boci Peng, Xinping Zhao, Xiaoran Shang, Yun Zhu, Lijun Wu

**Arxiv ID:** 2603.05120 | **Submitted:** March 5, 2026

**Key Mechanism:**
A multi-agent framework with four specialized agents:
1. **Problem Simplification Agent** -- when the model fails, reduces complexity by removing constraints, lowering numerical magnitudes, breaking multistep problems into components, or creating scaffolding.
2. **Problem Complication Agent** -- after success, increases difficulty by adding constraints, conditional branches, or combining techniques.
3. **Evaluation Agent** -- assesses correctness and identifies failure points.
4. **Routing Agent** -- decides whether to simplify or complicate based on performance.

Grounded in an "Optimal Pacing Theorem" that matches problem difficulty to current model capability. The bidirectional nature (both simplifying and complicating) distinguishes it from standard unidirectional curricula.

**Relation to error-type-driven curriculum:** This is the most structurally similar competitor -- it implements a **closed-loop adaptive curriculum** that responds to model failures. The simplification agent implicitly addresses error categories (calculation errors via simplified numerics, reasoning gaps via decomposition, conceptual misunderstandings via foundational variants). However, the error diagnosis is **implicit and coarse-grained** -- it adapts difficulty direction (simpler/harder) based on pass/fail, not based on classified error types.

**Key limitations vs DiagCoEvo:**
- **No explicit error taxonomy** -- adaptations are driven by pass/fail signals, not by diagnosed error types. The system does not know *why* the model failed, only *that* it failed.
- **Multi-agent overhead** -- requires coordinating four separate agents, with computational costs acknowledged by the authors.
- **Diminishing returns** -- performance gains plateau on olympiad-level problems.
- **No error-type-specific problem generation** -- simplification/complication is generic, not targeted at specific error categories (e.g., generating more formula confusion problems vs. more calculation problems).
- **Unidirectional in error understanding** -- adjusts difficulty but does not co-evolve the error diagnosis itself.

---

## Paper 4: VHG (May 2026)

**Full Title:** Verifier-Backed Hard Problem Generation for Mathematical Reasoning

**Authors:** Yuhang Lai, Jiazhan Feng, Yee Whye Teh, Ning Miao

**Affiliations:** City University of Hong Kong, Peking University, University of Oxford

**Arxiv ID:** 2605.06660 | **Submitted:** May 7, 2026

**Key Mechanism:**
VHG extends two-party self-play (setter-solver) into **three-party self-play** by adding an independent Verifier:
1. **Setter (Q)** -- generates problem-reference pairs (x, y*).
2. **Solver (S)** -- attempts to solve; pass-rate measures difficulty.
3. **Verifier (V)** -- validates problem correctness before difficulty scoring.

The setter's reward: R_Q(x,y*) = 1[V(x,y*)=1] * (1 - Acc_S(x,y*)). This prevents "reward hacking" where setters generate invalid-but-hard problems.

Two verifier variants: **Hard Verifier** (symbolic, e.g., SymPy for integrals -- near-perfect) and **Soft Verifier** (LLM-as-judge + format filters -- broader but less accurate).

The setter exhibits two-phase learning: first establishing validity (30.6% to 65.2%), then increasing difficulty while maintaining validity. Results: Pass@1 improved from 56.8% to 69.0% on general math benchmarks; strong "weak-to-strong" transfer (problems challenging for larger 8B-32B models).

**Relation to error-type-driven curriculum:** VHG focuses on **generating maximally difficult valid problems** through adversarial self-play. It is a difficulty-calibration mechanism, not an error-type-aware one. It drives the solver toward harder problems but does not diagnose *what kind* of errors the solver makes or generate problems targeting specific weaknesses.

**Key limitations vs DiagCoEvo:**
- **No error diagnosis at all** -- the system optimizes for difficulty (1 - accuracy) without any error categorization. It cannot distinguish between a solver failing due to calculation errors vs. conceptual misunderstanding.
- **Validity-focused, not weakness-focused** -- the verifier ensures problems are valid, not that they target specific model weaknesses.
- **No curriculum structure** -- problems are generated to be maximally hard, not sequenced in a pedagogically meaningful order.
- **Domain constraints** -- the Hard Verifier is only applicable to domains with symbolic verification (e.g., integration). The Soft Verifier trades accuracy for generality.
- **No co-evolution of error understanding** -- the setter learns to make harder problems, but there is no evolving model of what the solver struggles with specifically.

---

## Paper 5: Cog-DRIFT (April 2026)

**Full Title:** Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems

**Authors:** Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal

**Arxiv ID:** 2604.04767 | **Submitted:** April 6, 2026

**Key Mechanism:**
Addresses the problem that RLVR cannot learn from problems the model never solves (pass@64=0). Instead of abandoning hard problems, Cog-DRIFT **reformulates** them into cognitively simpler formats:
1. **4-Choice MCQ** -- easiest; constrains output space to 4 options.
2. **10-Choice MCQ** -- moderate; more options, harder discrimination.
3. **Cloze format** -- partial answer masking (e.g., "The answer looks like: 1__").
4. **Open-ended** -- original format (hardest).

An **instance-level adaptive curriculum** promotes each problem through the difficulty hierarchy: when the model achieves &gt;=50% accuracy at a given format, it advances to the next format. Progression is per-problem, not batch-level. The theoretical grounding invokes the "Zone of Proximal Development" from educational psychology.

Results: +10.11% on hard problems for Qwen, +8.64% for Llama. Cross-benchmark average: +4.72% (Qwen), +3.23% (Llama) over second-best baselines.

**Relation to error-type-driven curriculum:** Cog-DRIFT implements adaptive curriculum learning but through **task format reformulation** rather than error-type diagnosis. It reduces cognitive load by changing the answer format, not by targeting the specific reasoning failure. The curriculum adapts based on accuracy thresholds, not based on what type of error the model made.

**Key limitations vs DiagCoEvo:**
- **No error diagnosis** -- progression is driven by pass/fail accuracy thresholds, not by understanding *why* the model fails. A model failing due to calculation errors gets the same treatment as one failing due to conceptual misunderstanding.
- **Format-based, not content-based** -- reformulation changes how the answer is elicited (MCQ vs. open-ended), not the problem content itself. This cannot address content-specific weaknesses.
- **No problem generation** -- works with existing problems, only reformulating their format. Does not generate new problems targeting specific weaknesses.
- **Reliance on LLM quality for reformulation** -- GPT-5.4 is used for both reformulation and data quality filtering.
- **Limited curriculum signal** -- binary (pass threshold / fail threshold) rather than multi-dimensional error-type information.
- **No co-evolution** -- the reformulation strategy and curriculum are fixed designs; they do not evolve based on changing error patterns.

---

## Summary: Positioning Table

| Paper | Error Taxonomy | Curriculum | Co-Evolution | Training Method | Problem Generation |
|-------|---------------|------------|--------------|-----------------|-------------------|
| LEMMA | 7 explicit types | None (static SFT) | None | SFT on ~89K examples | Teacher-injected errors |
| Error Classification (MWP) | 39 dynamic clusters | None | None | None (inference-time prompting) | None |
| Bidirectional Curriculum | Implicit (pass/fail) | Bidirectional (simplify/complicate) | Partial (adapts difficulty) | SFT | Multi-agent generation |
| VHG | None | None (maximize difficulty) | Setter-solver co-training | RL (self-play) | Adversarial generation |
| Cog-DRIFT | None | Format-based adaptive | None | RLVR (GRPO) | Format reformulation only |

The gap that DiagCoEvo would fill: **none of these five works combines explicit error-type diagnosis with adaptive curriculum construction in a co-evolutionary loop**. LEMMA has the error taxonomy but no curriculum. Bidirectional Curriculum has the adaptive curriculum but no error taxonomy. VHG has co-evolution but no error awareness. Cog-DRIFT has curriculum but only over task format, not error-targeted content. The Error Classification paper has the richest error analysis but uses it only at inference time.

Sources:
- [LEMMA - ACL Anthology](https://aclanthology.org/2025.findings-acl.605/)
- [LEMMA - arXiv](https://arxiv.org/abs/2503.17439)
- [LEMMA - GitHub](https://github.com/pzs19/LEMMA)
- [Error Classification of LLMs on MWP - ACL Anthology](https://aclanthology.org/2025.findings-emnlp.20/)
- [Error Classification of LLMs on MWP - arXiv](https://arxiv.org/abs/2501.15581)
- [Bidirectional Curriculum Generation - arXiv](https://arxiv.org/abs/2603.05120)
- [VHG: Verifier-Backed Hard Problem Generation - arXiv](https://arxiv.org/html/2605.06660)
- [Cog-DRIFT - arXiv](https://arxiv.org/abs/2604.04767)
- [Cog-DRIFT - HuggingFace Papers](https://huggingface.co/papers/2604.04767)&lt;/result>
&lt;usage>&lt;total_tokens>35344&lt;/total_tokens>&lt;tool_uses>23&lt;/tool_uses>&lt;duration_ms>198858&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa6ce73f-11e7-422c-9707-c8a85a2a1c07",
  "isSidechain": false,
  "promptId": "fb8dabc9-1218-43e1-a2f5-1cc99847897a",
  "type": "user",
  "uuid": "553da50a-d1ea-4c29-b748-30a8224bd9e2",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "553da50a-d1ea-4c29-b748-30a8224bd9e2",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Assistant

_source line 52 · 2026-05-28T05:32:18.185Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have detailed research on all the minor competitors. Let me wait for the remaining 4 agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "553da50a-d1ea-4c29-b748-30a8224bd9e2",
  "isSidechain": false,
  "requestId": "req_011CbURJ4rY2jDmkkabEPfma",
  "type": "assistant",
  "uuid": "ac415780-6cc9-4fa0-b713-0b2139de377b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SywxTZvpoMGRsKXkFf7RVD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4234,
      "cache_read_input_tokens": 32388,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 32388,
          "cache_creation_input_tokens": 4234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4234
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

_source line 53 · 2026-05-28T05:32:19.392Z_

All 5 minor competitors are thoroughly researched. The positioning table is very clear - DiagCoEvo uniquely combines error taxonomy + adaptive curriculum + co-evolution. Waiting for 4 more agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac415780-6cc9-4fa0-b713-0b2139de377b",
  "isSidechain": false,
  "requestId": "req_011CbURJ4rY2jDmkkabEPfma",
  "type": "assistant",
  "uuid": "c9bce1ab-c27b-40f6-aad7-04e1a9e751d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SywxTZvpoMGRsKXkFf7RVD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4234,
      "cache_read_input_tokens": 32388,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 32388,
          "cache_creation_input_tokens": 4234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4234
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

_source line 54 · 2026-05-28T05:33:04.935Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:33:04.935Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "&lt;task-notification>\n&lt;task-id>ae2e2e8874dcc8e9d&lt;/task-id>\n&lt;tool-use-id>toolu_01M7W2PyYbQxpWWdQKfbZ7nj&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/ae2e2e8874dcc8e9d.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research GRPO-PRM citation status and PRM generalization\" completed&lt;/summary>\n&lt;result>I now have comprehensive information on both topics. Here is my complete report.\n\n---\n\n## Topic 1: \"GRPO is Secretly a Process Reward Model\" -- Paper Status\n\n### Identification\n- **Title:** GRPO is Secretly a Process Reward Model\n- **Authors:** Michael Sullivan, Alexander Koller (Saarland University)\n- **Exact arXiv ID:** `2509.21154`\n- **arXiv URL:** https://arxiv.org/abs/2509.21154\n- **Version history:** v1 (Sep 25, 2025), v2 (Oct 8, 2025), v3 (Feb 20, 2026)\n\n### Venue / Submission Status\n\nThere are **two distinct OpenReview submissions** to be aware of -- this is a source of confusion:\n\n1. **OpenReview `o0k034W6vx`** -- This is the Sullivan/Koller paper \"GRPO is Secretly a Process Reward Model,\" submitted to **ICLR 2026 Conference** (submission #20614, dated Sep 19, 2025, modified Feb 11, 2026). Based on my fetch of the OpenReview page, **no explicit decision (accepted/rejected/withdrawn) is visible** on the public page. The arXiv v3 metadata (Feb 2026) states the paper is **\"under review at ICML 2026\"**, which strongly suggests the ICLR 2026 submission was either **withdrawn or rejected**, and the authors resubmitted to ICML 2026.\n\n2. **OpenReview `iRWqcnBlLQ`** -- This is a **different paper**: \"GRPO-lambda: Credit Assignment improves LLM Reasoning\" by Parthasarathi, Reymond, Chen, Cui, and Chandar. It was submitted to ICLR 2026 and has been **explicitly marked as \"Withdrawn Submission.\"** This is NOT the Sullivan/Koller paper despite the similar topic.\n\n### Current Status Summary\n- The paper is currently a **preprint on arXiv** (v3, Feb 2026).\n- It appears to be **under review at ICML 2026** (per the arXiv page metadata).\n- The ICLR 2026 submission appears to have been unsuccessful (withdrawn or rejected), though the OpenReview page does not display a clear public decision.\n- It has **not yet been published** at a peer-reviewed venue as of this writing.\n\n### Recommended Citation\n```\n@article{sullivan2025grpo,\n  title={GRPO is Secretly a Process Reward Model},\n  author={Sullivan, Michael and Koller, Alexander},\n  journal={arXiv preprint arXiv:2509.21154},\n  year={2025}\n}\n```\nUntil ICML 2026 decisions are announced, citing it as an arXiv preprint is the correct approach.\n\n---\n\n## Topic 2: PRM Generalization Across Model Families\n\n### Key Finding: PRMs Have Limited Cross-Model Transfer\n\nThe evidence consistently shows that **PRMs are sensitive to the policy model they were trained on**, and applying them to a different model's reasoning traces constitutes an out-of-distribution (OOD) scenario. The literature identifies two types of OOD challenge:\n\n1. **Step OOD** -- caused by differences in reasoning patterns across model types and sizes. Different LLMs produce different reasoning styles, step granularities, and error patterns, so a PRM trained on Qwen traces sees unfamiliar reasoning patterns when applied to Mistral traces.\n\n2. **Question OOD** -- caused by dataset shifts between training data and real-world problems.\n\n**Concrete evidence:**\n- The **Qwen2.5-Math-PRM** paper (Zhang et al., \"The Lessons of Developing Process Reward Models in Mathematical Reasoning,\" arXiv:2501.07301) found that PRM trained on Qwen2.5-Math-7B-Instruct traces generalizes better than PRMs with Mistral or Llama as base models, suggesting model family matters significantly.\n- **PathFinder-PRM** (Pala et al., arXiv:2505.19706) found that augmenting training with weaker model traces (e.g., Mistral-7B) **saturates quickly** and may even **slightly degrade performance**, underscoring that data quality and match to the target model matter more than raw diversity.\n- Surveys (Liu et al., arXiv:2510.01925; the PRM survey at arXiv:2510.08049) consistently note that **discriminative PRMs struggle with OOD scenarios** and that \"performance can significantly drop when we change the domains or difficulty levels of queries, or even the formats of reasoning paths.\"\n\n### Papers with Positive Transfer Results\n\nSome approaches show more robust cross-model generalization:\n\n| Paper | Key Finding |\n|-------|-------------|\n| **RetrievalPRM** (Zhu et al., arXiv:2502.14361) | Retrieval-augmented PRM retrieves semantically similar questions and steps, improving generalization across different models and problem types. Addresses both step OOD and question OOD. |\n| **ThinkPRM** (Khalifa et al., arXiv:2504.16828) | Generative verification using chain-of-thought reasoning. Surpasses discriminative verifiers on OOD tasks (GPQA-Diamond: +8%, LiveCodeBench: +4.5%) using only 1% of PRM800K labels. |\n| **FoVer** (Kamoi et al., arXiv:2505.15960) | PRMs trained on formally verified data (Z3, Isabelle) generalize to informal math, logic, NLI, and BBH benchmarks -- demonstrating formal-to-informal and cross-task transfer. |\n| **VisualPRM** (Wang et al., arXiv:2503.10291) | An 8B PRM improves MLLMs across 3 model families and 4 model scales, including a 5.9-point improvement on InternVL2.5-78B. |\n| **APRM** (Juneja et al., arXiv:2511.22888) | Adversarially trained PRMs show +5.3 pp gains on OOD tasks, significantly better than static-data PRMs. |\n| **Chen et al.** (arXiv:2506.00027) \"From Mathematical Reasoning to Code\" | PRMs trained on math data perform comparably to code-specific PRMs, showing cross-domain transfer. |\n\n### Concrete Strategies for Cold-Start PRM Deployment on a New Model Family\n\nBased on the literature, here are actionable strategies for applying a PRM to a new model family (e.g., from Mistral to Qwen):\n\n1. **Use generative/ThinkPRM approaches over discriminative PRMs.** Generative verifiers that produce chain-of-thought verification reasoning are significantly more robust to distribution shift than discriminative classifiers. ThinkPRM achieves strong OOD results with minimal labeled data.\n\n2. **Retrieval augmentation (RetrievalPRM).** Augment PRM evaluation with retrieved examples of semantically similar reasoning steps and questions. This directly addresses step OOD by grounding the PRM's judgments in relevant reference material.\n\n3. **Train on formally verified data (FoVer).** Use formal verification tools to generate step-level labels. This produces model-agnostic ground truth that transfers across models and domains, avoiding dependence on any single model's reasoning style.\n\n4. **Adversarial training (APRM).** Train a generator to produce challenging reasoning errors alongside the PRM. This creates diverse negative examples that improve robustness to novel error patterns from unseen models.\n\n5. **Bootstrap with the new model's own traces.** Generate reasoning traces from the new model, use an existing PRM or LLM-as-judge to provide initial (noisy) step-level labels, then fine-tune a new PRM on these labeled traces. The Qwen PRM paper suggests consensus filtering (combining MC estimation + LLM-as-judge + heuristics) improves label quality.\n\n6. **Portable Reward Tuning (Chijiwa et al., arXiv:2502.12776).** Train reward models as separate portable modules that can be applied to any foundation model sharing the same vocabulary, avoiding retraining for each new model.\n\n7. **Hidden-state regularization (arXiv:2406.10216).** Regularize PRM hidden states during training to prevent overfitting to distribution-specific features, improving accuracy on OOD tasks.\n\n8. **Calibration techniques.** Use quantile-regression-based calibration to address overconfidence when a PRM encounters unfamiliar reasoning patterns from a new policy model. Weaker/different models cause more overconfidence in uncalibrated PRMs.\n\n9. **Start small, validate cross-model.** The literature strongly recommends **cross-model validation** during PRM development. PRMs should be evaluated not just on the training model's traces but on traces from the target deployment model. Large gains on one model family (e.g., Qwen) do not reliably transfer to others (e.g., Llama).\n\n### Key Takeaway\n\nThe cold-start problem is real and well-documented. The most practical near-term approach is: **(a)** use a generative verifier (ThinkPRM-style) as the most transfer-robust architecture, **(b)** bootstrap initial labels on the new model's traces using consensus of existing PRMs and LLM-as-judge, **(c)** augment with retrieval (RetrievalPRM) or formally verified training data (FoVer) to improve robustness, and **(d)** validate on the target model's actual traces before deployment.&lt;/result>\n&lt;usage>&lt;total_tokens>33043&lt;/total_tokens>&lt;tool_uses>40&lt;/tool_uses>&lt;duration_ms>231617&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
````

---

### Runtime record

_source line 55 · 2026-05-28T05:33:04.971Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:33:04.971Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 6

7 recorded events

### User

_source line 56 · 2026-05-28T05:33:04.982Z_

&lt;task-notification>
&lt;task-id>ae2e2e8874dcc8e9d&lt;/task-id>
&lt;tool-use-id>toolu_01M7W2PyYbQxpWWdQKfbZ7nj&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/ae2e2e8874dcc8e9d.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research GRPO-PRM citation status and PRM generalization" completed&lt;/summary>
&lt;result>I now have comprehensive information on both topics. Here is my complete report.

---

## Topic 1: "GRPO is Secretly a Process Reward Model" -- Paper Status

### Identification
- **Title:** GRPO is Secretly a Process Reward Model
- **Authors:** Michael Sullivan, Alexander Koller (Saarland University)
- **Exact arXiv ID:** `2509.21154`
- **arXiv URL:** https://arxiv.org/abs/2509.21154
- **Version history:** v1 (Sep 25, 2025), v2 (Oct 8, 2025), v3 (Feb 20, 2026)

### Venue / Submission Status

There are **two distinct OpenReview submissions** to be aware of -- this is a source of confusion:

1. **OpenReview `o0k034W6vx`** -- This is the Sullivan/Koller paper "GRPO is Secretly a Process Reward Model," submitted to **ICLR 2026 Conference** (submission #20614, dated Sep 19, 2025, modified Feb 11, 2026). Based on my fetch of the OpenReview page, **no explicit decision (accepted/rejected/withdrawn) is visible** on the public page. The arXiv v3 metadata (Feb 2026) states the paper is **"under review at ICML 2026"**, which strongly suggests the ICLR 2026 submission was either **withdrawn or rejected**, and the authors resubmitted to ICML 2026.

2. **OpenReview `iRWqcnBlLQ`** -- This is a **different paper**: "GRPO-lambda: Credit Assignment improves LLM Reasoning" by Parthasarathi, Reymond, Chen, Cui, and Chandar. It was submitted to ICLR 2026 and has been **explicitly marked as "Withdrawn Submission."** This is NOT the Sullivan/Koller paper despite the similar topic.

### Current Status Summary
- The paper is currently a **preprint on arXiv** (v3, Feb 2026).
- It appears to be **under review at ICML 2026** (per the arXiv page metadata).
- The ICLR 2026 submission appears to have been unsuccessful (withdrawn or rejected), though the OpenReview page does not display a clear public decision.
- It has **not yet been published** at a peer-reviewed venue as of this writing.

### Recommended Citation
```
@article{sullivan2025grpo,
  title={GRPO is Secretly a Process Reward Model},
  author={Sullivan, Michael and Koller, Alexander},
  journal={arXiv preprint arXiv:2509.21154},
  year={2025}
}
```
Until ICML 2026 decisions are announced, citing it as an arXiv preprint is the correct approach.

---

## Topic 2: PRM Generalization Across Model Families

### Key Finding: PRMs Have Limited Cross-Model Transfer

The evidence consistently shows that **PRMs are sensitive to the policy model they were trained on**, and applying them to a different model's reasoning traces constitutes an out-of-distribution (OOD) scenario. The literature identifies two types of OOD challenge:

1. **Step OOD** -- caused by differences in reasoning patterns across model types and sizes. Different LLMs produce different reasoning styles, step granularities, and error patterns, so a PRM trained on Qwen traces sees unfamiliar reasoning patterns when applied to Mistral traces.

2. **Question OOD** -- caused by dataset shifts between training data and real-world problems.

**Concrete evidence:**
- The **Qwen2.5-Math-PRM** paper (Zhang et al., "The Lessons of Developing Process Reward Models in Mathematical Reasoning," arXiv:2501.07301) found that PRM trained on Qwen2.5-Math-7B-Instruct traces generalizes better than PRMs with Mistral or Llama as base models, suggesting model family matters significantly.
- **PathFinder-PRM** (Pala et al., arXiv:2505.19706) found that augmenting training with weaker model traces (e.g., Mistral-7B) **saturates quickly** and may even **slightly degrade performance**, underscoring that data quality and match to the target model matter more than raw diversity.
- Surveys (Liu et al., arXiv:2510.01925; the PRM survey at arXiv:2510.08049) consistently note that **discriminative PRMs struggle with OOD scenarios** and that "performance can significantly drop when we change the domains or difficulty levels of queries, or even the formats of reasoning paths."

### Papers with Positive Transfer Results

Some approaches show more robust cross-model generalization:

| Paper | Key Finding |
|-------|-------------|
| **RetrievalPRM** (Zhu et al., arXiv:2502.14361) | Retrieval-augmented PRM retrieves semantically similar questions and steps, improving generalization across different models and problem types. Addresses both step OOD and question OOD. |
| **ThinkPRM** (Khalifa et al., arXiv:2504.16828) | Generative verification using chain-of-thought reasoning. Surpasses discriminative verifiers on OOD tasks (GPQA-Diamond: +8%, LiveCodeBench: +4.5%) using only 1% of PRM800K labels. |
| **FoVer** (Kamoi et al., arXiv:2505.15960) | PRMs trained on formally verified data (Z3, Isabelle) generalize to informal math, logic, NLI, and BBH benchmarks -- demonstrating formal-to-informal and cross-task transfer. |
| **VisualPRM** (Wang et al., arXiv:2503.10291) | An 8B PRM improves MLLMs across 3 model families and 4 model scales, including a 5.9-point improvement on InternVL2.5-78B. |
| **APRM** (Juneja et al., arXiv:2511.22888) | Adversarially trained PRMs show +5.3 pp gains on OOD tasks, significantly better than static-data PRMs. |
| **Chen et al.** (arXiv:2506.00027) "From Mathematical Reasoning to Code" | PRMs trained on math data perform comparably to code-specific PRMs, showing cross-domain transfer. |

### Concrete Strategies for Cold-Start PRM Deployment on a New Model Family

Based on the literature, here are actionable strategies for applying a PRM to a new model family (e.g., from Mistral to Qwen):

1. **Use generative/ThinkPRM approaches over discriminative PRMs.** Generative verifiers that produce chain-of-thought verification reasoning are significantly more robust to distribution shift than discriminative classifiers. ThinkPRM achieves strong OOD results with minimal labeled data.

2. **Retrieval augmentation (RetrievalPRM).** Augment PRM evaluation with retrieved examples of semantically similar reasoning steps and questions. This directly addresses step OOD by grounding the PRM's judgments in relevant reference material.

3. **Train on formally verified data (FoVer).** Use formal verification tools to generate step-level labels. This produces model-agnostic ground truth that transfers across models and domains, avoiding dependence on any single model's reasoning style.

4. **Adversarial training (APRM).** Train a generator to produce challenging reasoning errors alongside the PRM. This creates diverse negative examples that improve robustness to novel error patterns from unseen models.

5. **Bootstrap with the new model's own traces.** Generate reasoning traces from the new model, use an existing PRM or LLM-as-judge to provide initial (noisy) step-level labels, then fine-tune a new PRM on these labeled traces. The Qwen PRM paper suggests consensus filtering (combining MC estimation + LLM-as-judge + heuristics) improves label quality.

6. **Portable Reward Tuning (Chijiwa et al., arXiv:2502.12776).** Train reward models as separate portable modules that can be applied to any foundation model sharing the same vocabulary, avoiding retraining for each new model.

7. **Hidden-state regularization (arXiv:2406.10216).** Regularize PRM hidden states during training to prevent overfitting to distribution-specific features, improving accuracy on OOD tasks.

8. **Calibration techniques.** Use quantile-regression-based calibration to address overconfidence when a PRM encounters unfamiliar reasoning patterns from a new policy model. Weaker/different models cause more overconfidence in uncalibrated PRMs.

9. **Start small, validate cross-model.** The literature strongly recommends **cross-model validation** during PRM development. PRMs should be evaluated not just on the training model's traces but on traces from the target deployment model. Large gains on one model family (e.g., Qwen) do not reliably transfer to others (e.g., Llama).

### Key Takeaway

The cold-start problem is real and well-documented. The most practical near-term approach is: **(a)** use a generative verifier (ThinkPRM-style) as the most transfer-robust architecture, **(b)** bootstrap initial labels on the new model's traces using consensus of existing PRMs and LLM-as-judge, **(c)** augment with retrieval (RetrievalPRM) or formally verified training data (FoVer) to improve robustness, and **(d)** validate on the target model's actual traces before deployment.&lt;/result>
&lt;usage>&lt;total_tokens>33043&lt;/total_tokens>&lt;tool_uses>40&lt;/tool_uses>&lt;duration_ms>231617&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9bce1ab-c27b-40f6-aad7-04e1a9e751d0",
  "isSidechain": false,
  "promptId": "9e829651-ea62-40e9-a8a1-b60c536bd5c8",
  "type": "user",
  "uuid": "9e8680fd-c24c-49de-922f-0aa2ef16b4f7",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-28T05:33:12.302Z_

<details><summary>Logged reasoning block</summary>

```text
Great, now I have the GRPO-PRM citation status and PRM generalization research. Key findings:
1. Sullivan & Koller paper is arXiv:2509.21154, currently under review at ICML 2026 (ICLR 2026 submission was unsuccessful). The withdrawn paper iRWqcnBlLQ is a DIFFERENT paper.
2. PRM generalization is a real concern - need to address with bootstrapping on target model traces + generative verification.

Still waiting for 3 more agents: type-conditioned prompting feasibility, taxonomy expansion/MAB, and crowded field differentiation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e8680fd-c24c-49de-922f-0aa2ef16b4f7",
  "isSidechain": false,
  "requestId": "req_011CbURMwJEKbA373HTT9RVe",
  "type": "assistant",
  "uuid": "57ec6663-bc2b-407c-b783-a0b67c09c356",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RquQNrqoVdxd8MW4nRYBvw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2617,
      "cache_read_input_tokens": 36622,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 36622,
          "cache_creation_input_tokens": 2617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2617
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

_source line 58 · 2026-05-28T05:33:13.033Z_

Excellent findings on GRPO-PRM status (arXiv preprint, under review at ICML 2026 - the withdrawn OpenReview was a different paper) and PRM generalization strategies. Still waiting for 3 more agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57ec6663-bc2b-407c-b783-a0b67c09c356",
  "isSidechain": false,
  "requestId": "req_011CbURMwJEKbA373HTT9RVe",
  "type": "assistant",
  "uuid": "780fc791-708f-4de1-9e27-0a711898cc11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RquQNrqoVdxd8MW4nRYBvw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2617,
      "cache_read_input_tokens": 36622,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 36622,
          "cache_creation_input_tokens": 2617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2617
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

_source line 59 · 2026-05-28T05:34:11.558Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:34:11.558Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "&lt;task-notification>\n&lt;task-id>aafd8864207154b95&lt;/task-id>\n&lt;tool-use-id>toolu_01QEhpgpwSGWfEGxwJbjRKkB&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/aafd8864207154b95.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research crowded field differentiation\" completed&lt;/summary>\n&lt;result>I now have comprehensive data. Let me compile the findings.\n\nHere is my research synthesis on the current state of co-evolutionary self-improvement for LLM reasoning, organized around your five questions.\n\n---\n\n## 1. Paper Count: How Crowded Is This Field?\n\nThis field is **extremely active and increasingly crowded**. In the last 12 months (mid-2025 through May 2026), I identified the following:\n\n**Core co-evolutionary / self-play self-improvement papers (2025-2026):**\n- **R-Zero** (ICLR 2026 accepted) -- Challenger-Solver co-evolution from zero data, +6.49 on math benchmarks for Qwen3-4B\n- **Absolute Zero Reasoner** (NeurIPS 2025 Spotlight) -- self-play task proposal + solving with code executor\n- **Multi-Agent Evolve (MAE)** -- Proposer/Solver/Judge triplet co-evolution, +4.54% average on Qwen2.5-3B\n- **SAGE** (March 2026) -- 4-agent co-evolution (Challenger/Planner/Solver/Critic), +8.9% LiveCodeBench, +10.7% OlympiadBench on Qwen-2.5-7B\n- **CoVerRL** (March 2026) -- Generator-Verifier co-evolution addressing \"consensus trap,\" +4.7-5.9% over label-free baselines\n- **R-Diverse** (February 2026) -- Memory-Augmented Penalty + Skill-Aware Measurement for self-play diversity\n- **Seirenes** (May 2026) -- Adversarial self-play with evolving distractions, +7.2 to +10.2 points across scales\n- **SPC** (2025) -- Self-Play Critic via adversarial games\n\n**Closely related self-improvement papers:**\n- **B-STaR** (ICLR 2025) -- Balancing exploration/exploitation in self-taught reasoning\n- **rStar-Math** (ICML 2025) -- MCTS self-evolution, Qwen2.5-7B from 58.8% to 90.0% on MATH\n- **Self-Evolving Curriculum (SEC)** -- curriculum as multi-armed bandit during RL fine-tuning (Yoshua Bengio group)\n- **E2H Reasoner** -- easy-to-hard curriculum RL\n- **CLPO** -- curriculum learning meets policy optimization\n- **Task-Centric Theory** -- theoretical guarantees for iterative self-improvement with curricula\n- **Test-time Recursive Thinking** -- self-improvement without external feedback, +10.4-14.8pp on hard problems\n- **LADDER** -- recursive problem decomposition, 2% to 82% on integration problems\n- **SPOC** -- self-play critic boosting Llama-3.1 by +8.8/+11.6% on MATH500, +10/+20% on AMC23\n- **Think, Prune, Train, Improve** -- scaling reasoning without scaling models\n- **LEMMA** -- learning from errors for math advancement\n- **Self-Error-Instruct** -- generalizing from error types\n\n**Community signal:** The ICLR 2026 Workshop on Recursive Self-Improvement alone accepted **110 papers** across oral/spotlight/poster/short-paper tracks. The Awesome-Self-Evolving-Agents repository lists **200+ papers total**, with **~90+ published in 2025-2026**. \n\n**Bottom line:** There are roughly **25-30 directly relevant papers** in the co-evolutionary / self-play self-improvement subfield from the last 12 months, and **50+ more** in the broader self-improvement-for-reasoning space. This is a crowded area with very rapid iteration.\n\n---\n\n## 2. Current SOTA Numbers for 7B-8B Models\n\n| Benchmark | Model | Score | Notes |\n|-----------|-------|-------|-------|\n| **MATH-500** | Qwen3-8B (Thinking) | **90.4** | Current best open 8B model |\n| **MATH-500** | Qwen3-8B (Non-thinking) | **82.8** | Without chain-of-thought |\n| **MATH-500** | rStar-Math + Qwen2.5-Math-7B | **90.0** | With 64 MCTS trajectories at test time |\n| **MATH-500** | Qwen2.5-Coder-7B-Instruct | 66.0 | Baseline comparison |\n| **MATH-500** | Llama-3.1-8B-Instruct | 51.9 | Baseline comparison |\n| **AIME 2024** | Qwen2.5-7B-Instruct | ~16.7% | Baseline before self-improvement |\n| **AIME 2025** | No 7B-8B model in top 50 | &lt;50% est. | Smallest in top 50 was 30B (GLM-4.7-Flash at 91.6%) |\n| **MATH-500 SOTA** | GPT-5 | 99.4 | Frontier reference |\n| **AIME 2025 SOTA** | GPT-5.2 / Grok-4 Heavy | 100% | Multiple models at ceiling |\n\nKey observations: MATH-500 is becoming saturated at the frontier (99%+), but 7B-8B models still have a ~9-point gap to frontier. AIME remains very challenging for small models. AMC scores for 7B-8B models are sparsely reported but SPOC showed +10-20% gains on AMC23 for Llama-3.1 models.\n\n---\n\n## 3. What Gap Sizes Are Considered Significant?\n\nBased on the papers surveyed:\n\n- **+4-5pp** average across benchmarks: This is the **minimum** that gets published (MAE achieved +4.54%, CoVerRL +4.7-5.9%). This level alone is unlikely to get a top-venue oral.\n- **+7-10pp** on specific benchmarks: This is where papers start getting attention (Seirenes +7.2 to +10.2, SAGE +8.9/+10.7, SPOC +8.8/+11.6).\n- **+15-30pp** on specific benchmarks: This is blockbuster territory (rStar-Math +31.2pp on MATH, random rewards adding +15-27pp on MATH500/AIME).\n- For **AIME specifically**, even +3-5 problems solved (out of 30, ~10-17pp) is notable for small models given how hard the benchmark is.\n\n**For ICLR 2027, a paper with only +4-5pp improvements and no other contribution would likely be below the bar.** You would need either larger empirical gains (+8pp+) or a compelling analytical/theoretical contribution to complement moderate empirical results.\n\n---\n\n## 4. What Kind of Contribution Would Stand Out at ICLR 2027?\n\nGiven the landscape, here is my assessment by contribution type:\n\n**Pure empirical (new SOTA on benchmarks):** Very hard to stand out. rStar-Math, Absolute Zero, and SAGE have already pushed 7B models to ~90% on MATH-500. You would need to either (a) achieve these results with dramatically less compute/data, (b) show strong results on harder benchmarks like AIME/HMMT where small models still struggle, or (c) demonstrate generalization to non-math domains.\n\n**Methodological (new training framework):** Moderately crowded. The Proposer-Solver-Verifier paradigm has several variants (MAE, R-Zero, SAGE, CoVerRL). A new variant needs a clear conceptual distinction. Areas that are less explored:\n- Co-evolution with explicit curriculum control (the SEC paper touches this but doesn't combine it with multi-agent co-evolution)\n- Co-evolution that addresses *when* to stop (convergence criteria, diminishing returns detection)\n- Bridging co-evolution with test-time compute scaling\n\n**Analytical/theoretical:** This is the **most underexplored** and highest-potential area. The Task-Centric Theory paper provides some theoretical guarantees, but the field overwhelmingly lacks:\n- Formal understanding of *why* co-evolution works when it does and fails when it doesn't\n- Analysis of convergence properties and stability conditions\n- Characterization of the failure modes across iterations\n- Understanding of what the \"consensus trap\" (CoVerRL) and \"diversity illusion\" (R-Diverse) have in common formally\n\n**An analytical contribution would stand out precisely because the field is empirically crowded but theoretically sparse.** The RSI Workshop organizers explicitly noted the gap: \"principled methods, system designs, and evaluations that make self-improvement measurable, reliable, and deployable\" are missing.\n\n---\n\n## 5. Would Error-Type Analysis Across Iterations Be Sufficiently Novel?\n\n**Partially -- but it needs to go beyond what exists.** Here is the current state:\n\n**What already exists:**\n- **LEMMA** (ACL 2025 Findings) already provides a 7-category error taxonomy for math reasoning (Calculation Error, Counting Error, Formula Confusion, Question Misinterpretation, Missing Step, Confusing Concept, Nonsensical Output) and shows how error distributions shift after training (e.g., calculation errors dropping from ~25% to ~15%).\n- **ErrorAtlas** provides a 17-category general error taxonomy for LLMs.\n- **Self-Error-Instruct** generalizes training based on error types.\n- Multiple papers document that SFT can paradoxically increase certain error types while decreasing others.\n\n**What does NOT yet exist (and would be novel):**\n1. **Error distribution dynamics across multiple co-evolutionary iterations** -- LEMMA only looks at before vs. after one round of training. Nobody has tracked how error types evolve across 3-5+ iterations of self-play/co-evolution, showing cascade effects, error type migration, and convergence patterns.\n2. **Relating error distribution shifts to training signal quality** -- showing that certain error types predict when self-improvement will plateau or collapse (the \"tail narrowing\" and \"diversity illusion\" phenomena lack error-type-level granularity).\n3. **Error-aware curriculum design** -- using the error distribution analysis to dynamically steer which problems the Challenger generates, creating a feedback loop between error analysis and training data selection.\n4. **Cross-iteration error phase transitions** -- showing that co-evolution goes through distinct phases (e.g., first fixing calculation errors, then concept errors, then reasoning structure errors) would be a genuinely new analytical insight.\n\n**My assessment:** A paper that simply applies LEMMA's taxonomy to a co-evolutionary setting and reports how distributions shift would be **incremental** (likely workshop-level). To reach main-conference ICLR 2027 quality, the error analysis needs to be either:\n- **Predictive** (error distributions predict convergence/collapse before it happens)\n- **Prescriptive** (error analysis drives a demonstrably better training curriculum)\n- **Theoretically grounded** (formal connection between error-type entropy and self-improvement rate)\n\nThe strongest version would combine all three: show that error distributions follow predictable phase transitions during co-evolution, prove this theoretically, and use it to build a better training algorithm that achieves superior empirical results.\n\n---\n\n## Summary of Key Gaps and Opportunities\n\n| Gap | Opportunity | Competition Level |\n|-----|-------------|-------------------|\n| Theoretical understanding of co-evolution convergence | Formal analysis with proofs | Low competition |\n| Error dynamics across iterations | Phase transition analysis | Moderate (LEMMA exists but is single-iteration) |\n| When to stop self-improvement | Convergence criteria based on observable signals | Low competition |\n| Co-evolution on harder benchmarks (AIME, HMMT) for small models | Empirical + analysis | Moderate |\n| Unifying \"consensus trap\" and \"diversity illusion\" | Formal framework | Low competition |\n| Error-aware dynamic curriculum in co-evolution | Methodological + analytical | Moderate |\n\n**ICLR 2027 timeline note:** ICLR 2026 had its abstract deadline on September 27, 2025. If ICLR 2027 follows the same pattern, the submission deadline would be around **late September to early October 2026**, giving approximately 4 months from now.\n\nSources:\n- [SAGE: Multi-Agent Self-Evolution for LLM Reasoning](https://arxiv.org/abs/2603.15255)\n- [Multi-Agent Evolve: LLM Self-Improve through Co-evolution](https://arxiv.org/abs/2510.23595)\n- [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004)\n- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335)\n- [Self-Evolving Curriculum for LLM Reasoning](https://arxiv.org/abs/2505.14970)\n- [Seirenes: Adversarial Self-Play with Evolving Distractions](https://arxiv.org/abs/2605.11636)\n- [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103)\n- [CoVerRL: Breaking the Consensus Trap via Generator-Verifier Co-Evolution](https://arxiv.org/pdf/2603.17775)\n- [B-STaR: Monitoring and Balancing Exploration and Exploitation in Self-Taught Reasoners](https://arxiv.org/abs/2412.17256)\n- [A Task-Centric Theory for Iterative Self-Improvement](https://arxiv.org/pdf/2602.10014)\n- [LEMMA: Learning from Errors for MatheMatical Advancement](https://arxiv.org/abs/2503.17439)\n- [Self-Error-Instruct: Generalizing from Errors](https://arxiv.org/pdf/2505.22591)\n- [ICLR 2026 Workshop on Recursive Self-Improvement](https://recursive-workshop.github.io/)\n- [RSI Workshop Accepted Papers](https://recursive-workshop.github.io/papers.html)\n- [Awesome Self-Evolving Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents)\n- [MATH-500 Leaderboard](https://pricepertoken.com/leaderboards/benchmark/math-500)\n- [AIME 2025 Leaderboard](https://llm-stats.com/benchmarks/aime-2025)\n- [rStar-Math: Small LLMs Can Master Math Reasoning](https://arxiv.org/html/2501.04519v1)\n- [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1)\n- [ICLR 2026 Accepted Papers Highlights](https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/)&lt;/result>\n&lt;usage>&lt;total_tokens>40757&lt;/total_tokens>&lt;tool_uses>46&lt;/tool_uses>&lt;duration_ms>291477&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "780fc791-708f-4de1-9e27-0a711898cc11",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 62 · 2026-05-28T05:34:11.589Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:34:11.589Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 7

5 recorded events

### User

_source line 63 · 2026-05-28T05:34:11.601Z_

&lt;task-notification>
&lt;task-id>aafd8864207154b95&lt;/task-id>
&lt;tool-use-id>toolu_01QEhpgpwSGWfEGxwJbjRKkB&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/aafd8864207154b95.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research crowded field differentiation" completed&lt;/summary>
&lt;result>I now have comprehensive data. Let me compile the findings.

Here is my research synthesis on the current state of co-evolutionary self-improvement for LLM reasoning, organized around your five questions.

---

## 1. Paper Count: How Crowded Is This Field?

This field is **extremely active and increasingly crowded**. In the last 12 months (mid-2025 through May 2026), I identified the following:

**Core co-evolutionary / self-play self-improvement papers (2025-2026):**
- **R-Zero** (ICLR 2026 accepted) -- Challenger-Solver co-evolution from zero data, +6.49 on math benchmarks for Qwen3-4B
- **Absolute Zero Reasoner** (NeurIPS 2025 Spotlight) -- self-play task proposal + solving with code executor
- **Multi-Agent Evolve (MAE)** -- Proposer/Solver/Judge triplet co-evolution, +4.54% average on Qwen2.5-3B
- **SAGE** (March 2026) -- 4-agent co-evolution (Challenger/Planner/Solver/Critic), +8.9% LiveCodeBench, +10.7% OlympiadBench on Qwen-2.5-7B
- **CoVerRL** (March 2026) -- Generator-Verifier co-evolution addressing "consensus trap," +4.7-5.9% over label-free baselines
- **R-Diverse** (February 2026) -- Memory-Augmented Penalty + Skill-Aware Measurement for self-play diversity
- **Seirenes** (May 2026) -- Adversarial self-play with evolving distractions, +7.2 to +10.2 points across scales
- **SPC** (2025) -- Self-Play Critic via adversarial games

**Closely related self-improvement papers:**
- **B-STaR** (ICLR 2025) -- Balancing exploration/exploitation in self-taught reasoning
- **rStar-Math** (ICML 2025) -- MCTS self-evolution, Qwen2.5-7B from 58.8% to 90.0% on MATH
- **Self-Evolving Curriculum (SEC)** -- curriculum as multi-armed bandit during RL fine-tuning (Yoshua Bengio group)
- **E2H Reasoner** -- easy-to-hard curriculum RL
- **CLPO** -- curriculum learning meets policy optimization
- **Task-Centric Theory** -- theoretical guarantees for iterative self-improvement with curricula
- **Test-time Recursive Thinking** -- self-improvement without external feedback, +10.4-14.8pp on hard problems
- **LADDER** -- recursive problem decomposition, 2% to 82% on integration problems
- **SPOC** -- self-play critic boosting Llama-3.1 by +8.8/+11.6% on MATH500, +10/+20% on AMC23
- **Think, Prune, Train, Improve** -- scaling reasoning without scaling models
- **LEMMA** -- learning from errors for math advancement
- **Self-Error-Instruct** -- generalizing from error types

**Community signal:** The ICLR 2026 Workshop on Recursive Self-Improvement alone accepted **110 papers** across oral/spotlight/poster/short-paper tracks. The Awesome-Self-Evolving-Agents repository lists **200+ papers total**, with **~90+ published in 2025-2026**. 

**Bottom line:** There are roughly **25-30 directly relevant papers** in the co-evolutionary / self-play self-improvement subfield from the last 12 months, and **50+ more** in the broader self-improvement-for-reasoning space. This is a crowded area with very rapid iteration.

---

## 2. Current SOTA Numbers for 7B-8B Models

| Benchmark | Model | Score | Notes |
|-----------|-------|-------|-------|
| **MATH-500** | Qwen3-8B (Thinking) | **90.4** | Current best open 8B model |
| **MATH-500** | Qwen3-8B (Non-thinking) | **82.8** | Without chain-of-thought |
| **MATH-500** | rStar-Math + Qwen2.5-Math-7B | **90.0** | With 64 MCTS trajectories at test time |
| **MATH-500** | Qwen2.5-Coder-7B-Instruct | 66.0 | Baseline comparison |
| **MATH-500** | Llama-3.1-8B-Instruct | 51.9 | Baseline comparison |
| **AIME 2024** | Qwen2.5-7B-Instruct | ~16.7% | Baseline before self-improvement |
| **AIME 2025** | No 7B-8B model in top 50 | &lt;50% est. | Smallest in top 50 was 30B (GLM-4.7-Flash at 91.6%) |
| **MATH-500 SOTA** | GPT-5 | 99.4 | Frontier reference |
| **AIME 2025 SOTA** | GPT-5.2 / Grok-4 Heavy | 100% | Multiple models at ceiling |

Key observations: MATH-500 is becoming saturated at the frontier (99%+), but 7B-8B models still have a ~9-point gap to frontier. AIME remains very challenging for small models. AMC scores for 7B-8B models are sparsely reported but SPOC showed +10-20% gains on AMC23 for Llama-3.1 models.

---

## 3. What Gap Sizes Are Considered Significant?

Based on the papers surveyed:

- **+4-5pp** average across benchmarks: This is the **minimum** that gets published (MAE achieved +4.54%, CoVerRL +4.7-5.9%). This level alone is unlikely to get a top-venue oral.
- **+7-10pp** on specific benchmarks: This is where papers start getting attention (Seirenes +7.2 to +10.2, SAGE +8.9/+10.7, SPOC +8.8/+11.6).
- **+15-30pp** on specific benchmarks: This is blockbuster territory (rStar-Math +31.2pp on MATH, random rewards adding +15-27pp on MATH500/AIME).
- For **AIME specifically**, even +3-5 problems solved (out of 30, ~10-17pp) is notable for small models given how hard the benchmark is.

**For ICLR 2027, a paper with only +4-5pp improvements and no other contribution would likely be below the bar.** You would need either larger empirical gains (+8pp+) or a compelling analytical/theoretical contribution to complement moderate empirical results.

---

## 4. What Kind of Contribution Would Stand Out at ICLR 2027?

Given the landscape, here is my assessment by contribution type:

**Pure empirical (new SOTA on benchmarks):** Very hard to stand out. rStar-Math, Absolute Zero, and SAGE have already pushed 7B models to ~90% on MATH-500. You would need to either (a) achieve these results with dramatically less compute/data, (b) show strong results on harder benchmarks like AIME/HMMT where small models still struggle, or (c) demonstrate generalization to non-math domains.

**Methodological (new training framework):** Moderately crowded. The Proposer-Solver-Verifier paradigm has several variants (MAE, R-Zero, SAGE, CoVerRL). A new variant needs a clear conceptual distinction. Areas that are less explored:
- Co-evolution with explicit curriculum control (the SEC paper touches this but doesn't combine it with multi-agent co-evolution)
- Co-evolution that addresses *when* to stop (convergence criteria, diminishing returns detection)
- Bridging co-evolution with test-time compute scaling

**Analytical/theoretical:** This is the **most underexplored** and highest-potential area. The Task-Centric Theory paper provides some theoretical guarantees, but the field overwhelmingly lacks:
- Formal understanding of *why* co-evolution works when it does and fails when it doesn't
- Analysis of convergence properties and stability conditions
- Characterization of the failure modes across iterations
- Understanding of what the "consensus trap" (CoVerRL) and "diversity illusion" (R-Diverse) have in common formally

**An analytical contribution would stand out precisely because the field is empirically crowded but theoretically sparse.** The RSI Workshop organizers explicitly noted the gap: "principled methods, system designs, and evaluations that make self-improvement measurable, reliable, and deployable" are missing.

---

## 5. Would Error-Type Analysis Across Iterations Be Sufficiently Novel?

**Partially -- but it needs to go beyond what exists.** Here is the current state:

**What already exists:**
- **LEMMA** (ACL 2025 Findings) already provides a 7-category error taxonomy for math reasoning (Calculation Error, Counting Error, Formula Confusion, Question Misinterpretation, Missing Step, Confusing Concept, Nonsensical Output) and shows how error distributions shift after training (e.g., calculation errors dropping from ~25% to ~15%).
- **ErrorAtlas** provides a 17-category general error taxonomy for LLMs.
- **Self-Error-Instruct** generalizes training based on error types.
- Multiple papers document that SFT can paradoxically increase certain error types while decreasing others.

**What does NOT yet exist (and would be novel):**
1. **Error distribution dynamics across multiple co-evolutionary iterations** -- LEMMA only looks at before vs. after one round of training. Nobody has tracked how error types evolve across 3-5+ iterations of self-play/co-evolution, showing cascade effects, error type migration, and convergence patterns.
2. **Relating error distribution shifts to training signal quality** -- showing that certain error types predict when self-improvement will plateau or collapse (the "tail narrowing" and "diversity illusion" phenomena lack error-type-level granularity).
3. **Error-aware curriculum design** -- using the error distribution analysis to dynamically steer which problems the Challenger generates, creating a feedback loop between error analysis and training data selection.
4. **Cross-iteration error phase transitions** -- showing that co-evolution goes through distinct phases (e.g., first fixing calculation errors, then concept errors, then reasoning structure errors) would be a genuinely new analytical insight.

**My assessment:** A paper that simply applies LEMMA's taxonomy to a co-evolutionary setting and reports how distributions shift would be **incremental** (likely workshop-level). To reach main-conference ICLR 2027 quality, the error analysis needs to be either:
- **Predictive** (error distributions predict convergence/collapse before it happens)
- **Prescriptive** (error analysis drives a demonstrably better training curriculum)
- **Theoretically grounded** (formal connection between error-type entropy and self-improvement rate)

The strongest version would combine all three: show that error distributions follow predictable phase transitions during co-evolution, prove this theoretically, and use it to build a better training algorithm that achieves superior empirical results.

---

## Summary of Key Gaps and Opportunities

| Gap | Opportunity | Competition Level |
|-----|-------------|-------------------|
| Theoretical understanding of co-evolution convergence | Formal analysis with proofs | Low competition |
| Error dynamics across iterations | Phase transition analysis | Moderate (LEMMA exists but is single-iteration) |
| When to stop self-improvement | Convergence criteria based on observable signals | Low competition |
| Co-evolution on harder benchmarks (AIME, HMMT) for small models | Empirical + analysis | Moderate |
| Unifying "consensus trap" and "diversity illusion" | Formal framework | Low competition |
| Error-aware dynamic curriculum in co-evolution | Methodological + analytical | Moderate |

**ICLR 2027 timeline note:** ICLR 2026 had its abstract deadline on September 27, 2025. If ICLR 2027 follows the same pattern, the submission deadline would be around **late September to early October 2026**, giving approximately 4 months from now.

Sources:
- [SAGE: Multi-Agent Self-Evolution for LLM Reasoning](https://arxiv.org/abs/2603.15255)
- [Multi-Agent Evolve: LLM Self-Improve through Co-evolution](https://arxiv.org/abs/2510.23595)
- [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004)
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335)
- [Self-Evolving Curriculum for LLM Reasoning](https://arxiv.org/abs/2505.14970)
- [Seirenes: Adversarial Self-Play with Evolving Distractions](https://arxiv.org/abs/2605.11636)
- [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103)
- [CoVerRL: Breaking the Consensus Trap via Generator-Verifier Co-Evolution](https://arxiv.org/pdf/2603.17775)
- [B-STaR: Monitoring and Balancing Exploration and Exploitation in Self-Taught Reasoners](https://arxiv.org/abs/2412.17256)
- [A Task-Centric Theory for Iterative Self-Improvement](https://arxiv.org/pdf/2602.10014)
- [LEMMA: Learning from Errors for MatheMatical Advancement](https://arxiv.org/abs/2503.17439)
- [Self-Error-Instruct: Generalizing from Errors](https://arxiv.org/pdf/2505.22591)
- [ICLR 2026 Workshop on Recursive Self-Improvement](https://recursive-workshop.github.io/)
- [RSI Workshop Accepted Papers](https://recursive-workshop.github.io/papers.html)
- [Awesome Self-Evolving Agents](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents)
- [MATH-500 Leaderboard](https://pricepertoken.com/leaderboards/benchmark/math-500)
- [AIME 2025 Leaderboard](https://llm-stats.com/benchmarks/aime-2025)
- [rStar-Math: Small LLMs Can Master Math Reasoning](https://arxiv.org/html/2501.04519v1)
- [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1)
- [ICLR 2026 Accepted Papers Highlights](https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/)&lt;/result>
&lt;usage>&lt;total_tokens>40757&lt;/total_tokens>&lt;tool_uses>46&lt;/tool_uses>&lt;duration_ms>291477&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "780fc791-708f-4de1-9e27-0a711898cc11",
  "isSidechain": false,
  "promptId": "8b4fd2b9-2954-41b4-be53-425ba8b68ce8",
  "type": "user",
  "uuid": "874c65f6-53a2-484d-b66b-cadbe520a933",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-28T05:34:17.353Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the crowded field analysis. Key insights:
- 25-30 directly relevant papers in last 12 months
- Need +8pp+ or compelling analytical contribution
- Error-type analysis across iterations would be novel IF it's predictive/prescriptive/theoretically grounded
- The SEC paper (Self-Evolving Curriculum) uses MAB - need to integrate this

Still waiting for 2 agents: type-conditioned prompting feasibility and taxonomy expansion/MAB.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "874c65f6-53a2-484d-b66b-cadbe520a933",
  "isSidechain": false,
  "requestId": "req_011CbURSr9JdmfhSjSLQncFx",
  "type": "assistant",
  "uuid": "649a4038-ff65-4cea-b3f7-a69bcd806d99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFNUVryZWx5jx72VSgeWFe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4136,
      "cache_read_input_tokens": 39239,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4136,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 185,
          "cache_read_input_tokens": 39239,
          "cache_creation_input_tokens": 4136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4136
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

_source line 65 · 2026-05-28T05:34:18.951Z_

Very valuable crowded field analysis. Key insight: the analytical contribution (error distribution dynamics across iterations) needs to be **predictive or prescriptive**, not just descriptive. Also identified the SEC paper for MAB-based curriculum. Waiting for 2 more agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "649a4038-ff65-4cea-b3f7-a69bcd806d99",
  "isSidechain": false,
  "requestId": "req_011CbURSr9JdmfhSjSLQncFx",
  "type": "assistant",
  "uuid": "026d7724-2d24-4ba2-ac5b-90301c495661",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFNUVryZWx5jx72VSgeWFe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4136,
      "cache_read_input_tokens": 39239,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4136,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 185,
          "cache_read_input_tokens": 39239,
          "cache_creation_input_tokens": 4136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4136
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

_source line 66 · 2026-05-28T05:35:19.158Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:35:19.158Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "&lt;task-notification>\n&lt;task-id>a83fcadbf221bd9ca&lt;/task-id>\n&lt;tool-use-id>toolu_019xH9bK6GiRDX5txrje6mSa&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a83fcadbf221bd9ca.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research type-conditioned prompting feasibility\" completed&lt;/summary>\n&lt;result>I now have sufficient data to provide a comprehensive research synthesis. Here is my analysis:\n\n---\n\n## Research Findings: Feasibility of Type-Conditioned Problem Generation for Math Reasoning\n\n### Executive Summary\n\nType-conditioned problem generation (prompting an LLM to generate a math problem that triggers a specific error type like \"sign error\" or \"conceptual misunderstanding\") is feasible but comes with significant yield challenges. No paper reports a direct \"type-conditioned generation success rate\" as a clean metric, but converging evidence from six major frameworks allows us to estimate realistic numbers.\n\n---\n\n### 1. Estimated Yield/Success Rates for Type-Conditioned Generation\n\n**The honest answer: nobody reports this number directly.** But we can triangulate from related pipelines:\n\n**Upper bound (~40-50% raw yield for \"generate a problem in category X\"):**\n- The VHG (Verifier-backed Hard Generation) paper provides the most granular data. For general math with a soft verifier: 400,000 candidates generated --&gt; 270,064 after deduplication --&gt; 107,398 after solver filtering --&gt; 20,670 after judge validation. That is a **~5.2% end-to-end yield** from raw generation to validated problems. For a hard verifier domain (indefinite integrals), yield was higher at **~21.9%** (4,074 of 18,663). These are for *hardness-conditioned* generation, not error-type conditioned, but the pipeline structure is analogous.\n\n**Mid-range estimate (~20-30% for error-cluster-conditioned generation):**\n- Self-Error-Instruct (ACL 2025) clusters error keyphrases (extracted by GPT-4o from model failure cases on GSM8K/MATH), then conditions new problem generation on sampled bad cases from each cluster. They apply a one-shot filtering process to retain only effective examples. Though exact filtering rates are not published, the framework explicitly acknowledges that only a subset of generated data survives quality control. Based on the pipeline design (cluster-conditioned generation + one-shot filtering), a 20-30% acceptance rate is a reasonable inference.\n\n**Lower bound for fine-grained conditioning (~10-15%):**\n- The hypothesis-driven error analysis paper (arXiv 2604.04386) found that **\"the model produces more flawed problems when guided by high-accuracy hypotheses\"** -- meaning the more specific and accurate your error hypothesis, the harder it is for the generator to produce valid problems targeting that weakness. Their best hypotheses reduced solve rates from 77% to 45%, but the generator quality degrades precisely when targeting the most useful error types. This is a fundamental tension.\n\n**Key insight from FLAMES:** A solvability filter (checking if problems are actually solvable) **incorrectly rejects 30% of real human-crafted MATH problems** and **50% of Level 5 problems**. This means automated validation itself introduces substantial noise, so reported yield numbers may undercount valid generations.\n\n---\n\n### 2. Realistic Rejection Sampling Budgets\n\n**DART-Math provides the most concrete data:**\n- For uniform sampling (40 correct responses per query): `nmax = 2048` achieves &gt;90% query coverage, requiring ~5M raw samples total\n- For difficulty-proportional sampling: `nmax &gt;= 8,192` needed for 90% coverage, requiring &gt;15M raw samples\n- Their full experiment: ~150M total samples to achieve 95% query coverage, ~590K final dataset. That is roughly a **250:1 raw-to-final ratio**\n- Computational cost: 5 days on 32 NVIDIA A100 GPUs\n- Critical finding: standard rejection tuning drops over 50% of the hardest (Level 5) queries, with difficult queries representing only 10.5% of final samples\n\n**For type-conditioned generation specifically, expect:**\n- Easy error types (calculation errors, arithmetic slips): 5-10 samples per valid problem\n- Medium error types (algebraic simplification, sign errors): 10-30 samples per valid problem  \n- Hard error types (conceptual misunderstanding, invalid inference): 30-100+ samples per valid problem\n- These estimates are derived from the DART-Math difficulty scaling curves and the VHG soft-verifier pipeline ratios\n\n---\n\n### 3. Fallback Strategies: Mutation vs. Generation from Scratch\n\n**Strategy A: Problem Mutation (Lower risk, recommended as primary)**\n- **Arrows of Math (AMD):** Uses four mutation strategies on mathematical programs -- constraint mutation, variable mutation, constant mutation, and code variation. Generated 12.3M triples, yielding 1.8M unique pairs after deduplication. Mutation within a symbolic/programmatic space provides guaranteed correctness via bilateral validation (LLM solutions verified against program execution).\n- **EvolMathEval:** Evolutionary mutation with two generations, using a dual-filter mechanism (composite fitness threshold of -0.5, plus bottom-1st-percentile rejection on any single metric). Reduced model accuracy by an average of 48% on evolved problems. Rejected candidates re-enter the evolutionary cycle.\n- **Neuro-Symbolic approach:** Mutation in symbolic space enables systematic sampling and symbolic solving, providing verified ground truth.\n\n**Strategy B: Weakness-Targeted Synthesis (Medium risk)**\n- **SwS (Microsoft, 2025):** Records consistent failures during RL training, groups them by category, extracts concepts, synthesizes 40K problems per model. Quality filters: (a) answer consistency &gt;= 50% across multiple model generations, (b) difficulty in [25%, 75%] accuracy range, (c) quality ratings must be \"perfect\" with no \"bad\" ratings. After training on augmented data, models solved up to 20% more of their consistent failure problems (Intermediate Algebra).\n- **WarriorMath:** Uses a 5-model expert committee (DeepSeek-R1-Distill-Llama-70B, Qwen2.5-Math-72B, etc.) with N=16 rollouts for defect detection. Only failures are retained. Results: 12.57% average improvement, with iterative gains (36.7% -&gt; 42.5% -&gt; 44.7% -&gt; 48.3% across 3 iterations).\n\n**Strategy C: Error-Cluster-Conditioned Generation from Scratch (Higher risk)**\n- **Self-Error-Instruct:** The closest to pure type-conditioned generation. Pipeline: (1) find bad cases, (2) extract error keyphrases via GPT-4o, (3) cluster keyphrases into error types, (4) sample bad cases per error type as few-shot examples, (5) synthesize new problems via self-instruct, (6) one-shot filter. This works but requires the instructor model (GPT-4o) and an iterative refinement loop.\n\n---\n\n### 4. Concrete Recommendations for Risk Mitigation\n\nGiven that the reviewer flagged this as highest-risk, here is what the evidence supports:\n\n**Recommended hybrid approach (ordered by risk):**\n\n1. **Start with mutation (safest):** Take existing problems the model fails on, mutate them in a structured way (change constants, add/remove constraints, alter variable relationships). The Arrows of Math and EvolMathEval approaches demonstrate this works reliably. Mutation preserves problem validity better than generation from scratch.\n\n2. **Use weakness-category conditioning (medium risk):** Following SwS/WarriorMath, group failures by mathematical category (algebra, geometry, etc.) and generate new problems within those categories. This is coarser than specific error-type conditioning but much more reliable. Budget 40K problems per model as SwS does.\n\n3. **Fine-grained error-type conditioning (highest risk, use with heavy filtering):** Following Self-Error-Instruct, condition on specific error keyphrases. But budget for a **3-5x rejection sampling overhead** beyond what you would expect for category-level conditioning. Expect ~10-25% of generated problems to actually trigger the targeted specific error pattern.\n\n4. **Verifier-backed validation is essential:** The VHG paper shows that judge-backed filtering can recover valid hard candidates from a noisy generated pool, but end-to-end yield is only 5-22%. Build your pipeline assuming you need to generate 5-20x more candidates than your target dataset size.\n\n**Budget planning numbers:**\n- For 10K type-conditioned problems: generate 50K-200K candidates (5-20x overhead)\n- Computational cost reference: DART-Math needed 5 days on 32 A100s for 590K problems from 150M samples\n- Simpler estimate: for moderate-difficulty type conditioning, plan for ~10x rejection sampling ratio\n\n---\n\n### 5. The Fundamental Tension (Key Risk)\n\nThe hypothesis-driven error analysis paper identifies the core challenge: **generator quality degrades when targeting the model's weakest areas**. The generator LLM is itself weak in the same areas you want to target. High-accuracy hypotheses (the most useful ones) produce more flawed problems. This creates a catch-22 that no current paper has fully solved.\n\n**Mitigations:**\n- Use a stronger model as generator than the target model (e.g., GPT-4o/GPT-5 generating problems for a 7B model)\n- Use symbolic/programmatic mutation rather than pure LLM generation for the hardest error types\n- Accept that fine-grained error-type conditioning (e.g., \"generate a problem that triggers sign errors in polynomial division\") will have lower yield than coarse conditioning (e.g., \"generate a hard algebra problem\"), and plan your pipeline budget accordingly\n\n---\n\n### Sources\n\n- [Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis](https://arxiv.org/html/2604.04386) - Key paper on hypothesis-driven error targeting, solve rate data (45-95% range)\n- [Verifier-Backed Hard Problem Generation (VHG)](https://arxiv.org/html/2605.06660) - Best concrete yield data: 5.2-21.9% end-to-end yield\n- [Self-Error-Instruct (ACL 2025)](https://aclanthology.org/2025.acl-long.417/) - Error keyphrase clustering and type-conditioned synthesis\n- [SwS: Self-aware Weakness-driven Problem Synthesis](https://arxiv.org/abs/2506.08989) - 40K problems per model, [25%,75%] difficulty filtering, 50% answer consistency threshold\n- [WarriorMath](https://arxiv.org/abs/2508.01245) - 5-model expert committee, N=16 rollouts, 12.57% average gain\n- [DART-Math (NeurIPS 2024)](https://arxiv.org/abs/2407.13690) - nmax=2048-8192, 150M samples for 590K dataset, 250:1 ratio\n- [FLAMES](https://arxiv.org/abs/2508.16514) - Solvability filter incorrectly rejects 30% of real problems, 50% of Level 5\n- [EvolMathEval](https://arxiv.org/html/2508.13003v1) - Evolutionary mutation, 48% average accuracy reduction, dual-filter mechanism\n- [Arrows of Math Reasoning Data Synthesis](https://arxiv.org/abs/2508.18824) - 12.3M to 1.8M pipeline, four mutation strategies\n- [LEMMA](https://arxiv.org/pdf/2503.17439) - Error-type grounded mistake augmentation, &lt;90K examples\n- [Controllable Text Generation Survey](https://dl.acm.org/doi/10.1145/3617680) - Attribute accuracy 85-92% for style/sentiment conditioning&lt;/result>\n&lt;usage>&lt;total_tokens>41696&lt;/total_tokens>&lt;tool_uses>47&lt;/tool_uses>&lt;duration_ms>378454&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---

### Runtime record

_source line 67 · 2026-05-28T05:35:19.229Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:35:19.229Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 8

7 recorded events

### User

_source line 68 · 2026-05-28T05:35:19.238Z_

&lt;task-notification>
&lt;task-id>a83fcadbf221bd9ca&lt;/task-id>
&lt;tool-use-id>toolu_019xH9bK6GiRDX5txrje6mSa&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a83fcadbf221bd9ca.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research type-conditioned prompting feasibility" completed&lt;/summary>
&lt;result>I now have sufficient data to provide a comprehensive research synthesis. Here is my analysis:

---

## Research Findings: Feasibility of Type-Conditioned Problem Generation for Math Reasoning

### Executive Summary

Type-conditioned problem generation (prompting an LLM to generate a math problem that triggers a specific error type like "sign error" or "conceptual misunderstanding") is feasible but comes with significant yield challenges. No paper reports a direct "type-conditioned generation success rate" as a clean metric, but converging evidence from six major frameworks allows us to estimate realistic numbers.

---

### 1. Estimated Yield/Success Rates for Type-Conditioned Generation

**The honest answer: nobody reports this number directly.** But we can triangulate from related pipelines:

**Upper bound (~40-50% raw yield for "generate a problem in category X"):**
- The VHG (Verifier-backed Hard Generation) paper provides the most granular data. For general math with a soft verifier: 400,000 candidates generated --&gt; 270,064 after deduplication --&gt; 107,398 after solver filtering --&gt; 20,670 after judge validation. That is a **~5.2% end-to-end yield** from raw generation to validated problems. For a hard verifier domain (indefinite integrals), yield was higher at **~21.9%** (4,074 of 18,663). These are for *hardness-conditioned* generation, not error-type conditioned, but the pipeline structure is analogous.

**Mid-range estimate (~20-30% for error-cluster-conditioned generation):**
- Self-Error-Instruct (ACL 2025) clusters error keyphrases (extracted by GPT-4o from model failure cases on GSM8K/MATH), then conditions new problem generation on sampled bad cases from each cluster. They apply a one-shot filtering process to retain only effective examples. Though exact filtering rates are not published, the framework explicitly acknowledges that only a subset of generated data survives quality control. Based on the pipeline design (cluster-conditioned generation + one-shot filtering), a 20-30% acceptance rate is a reasonable inference.

**Lower bound for fine-grained conditioning (~10-15%):**
- The hypothesis-driven error analysis paper (arXiv 2604.04386) found that **"the model produces more flawed problems when guided by high-accuracy hypotheses"** -- meaning the more specific and accurate your error hypothesis, the harder it is for the generator to produce valid problems targeting that weakness. Their best hypotheses reduced solve rates from 77% to 45%, but the generator quality degrades precisely when targeting the most useful error types. This is a fundamental tension.

**Key insight from FLAMES:** A solvability filter (checking if problems are actually solvable) **incorrectly rejects 30% of real human-crafted MATH problems** and **50% of Level 5 problems**. This means automated validation itself introduces substantial noise, so reported yield numbers may undercount valid generations.

---

### 2. Realistic Rejection Sampling Budgets

**DART-Math provides the most concrete data:**
- For uniform sampling (40 correct responses per query): `nmax = 2048` achieves &gt;90% query coverage, requiring ~5M raw samples total
- For difficulty-proportional sampling: `nmax &gt;= 8,192` needed for 90% coverage, requiring &gt;15M raw samples
- Their full experiment: ~150M total samples to achieve 95% query coverage, ~590K final dataset. That is roughly a **250:1 raw-to-final ratio**
- Computational cost: 5 days on 32 NVIDIA A100 GPUs
- Critical finding: standard rejection tuning drops over 50% of the hardest (Level 5) queries, with difficult queries representing only 10.5% of final samples

**For type-conditioned generation specifically, expect:**
- Easy error types (calculation errors, arithmetic slips): 5-10 samples per valid problem
- Medium error types (algebraic simplification, sign errors): 10-30 samples per valid problem  
- Hard error types (conceptual misunderstanding, invalid inference): 30-100+ samples per valid problem
- These estimates are derived from the DART-Math difficulty scaling curves and the VHG soft-verifier pipeline ratios

---

### 3. Fallback Strategies: Mutation vs. Generation from Scratch

**Strategy A: Problem Mutation (Lower risk, recommended as primary)**
- **Arrows of Math (AMD):** Uses four mutation strategies on mathematical programs -- constraint mutation, variable mutation, constant mutation, and code variation. Generated 12.3M triples, yielding 1.8M unique pairs after deduplication. Mutation within a symbolic/programmatic space provides guaranteed correctness via bilateral validation (LLM solutions verified against program execution).
- **EvolMathEval:** Evolutionary mutation with two generations, using a dual-filter mechanism (composite fitness threshold of -0.5, plus bottom-1st-percentile rejection on any single metric). Reduced model accuracy by an average of 48% on evolved problems. Rejected candidates re-enter the evolutionary cycle.
- **Neuro-Symbolic approach:** Mutation in symbolic space enables systematic sampling and symbolic solving, providing verified ground truth.

**Strategy B: Weakness-Targeted Synthesis (Medium risk)**
- **SwS (Microsoft, 2025):** Records consistent failures during RL training, groups them by category, extracts concepts, synthesizes 40K problems per model. Quality filters: (a) answer consistency &gt;= 50% across multiple model generations, (b) difficulty in [25%, 75%] accuracy range, (c) quality ratings must be "perfect" with no "bad" ratings. After training on augmented data, models solved up to 20% more of their consistent failure problems (Intermediate Algebra).
- **WarriorMath:** Uses a 5-model expert committee (DeepSeek-R1-Distill-Llama-70B, Qwen2.5-Math-72B, etc.) with N=16 rollouts for defect detection. Only failures are retained. Results: 12.57% average improvement, with iterative gains (36.7% -&gt; 42.5% -&gt; 44.7% -&gt; 48.3% across 3 iterations).

**Strategy C: Error-Cluster-Conditioned Generation from Scratch (Higher risk)**
- **Self-Error-Instruct:** The closest to pure type-conditioned generation. Pipeline: (1) find bad cases, (2) extract error keyphrases via GPT-4o, (3) cluster keyphrases into error types, (4) sample bad cases per error type as few-shot examples, (5) synthesize new problems via self-instruct, (6) one-shot filter. This works but requires the instructor model (GPT-4o) and an iterative refinement loop.

---

### 4. Concrete Recommendations for Risk Mitigation

Given that the reviewer flagged this as highest-risk, here is what the evidence supports:

**Recommended hybrid approach (ordered by risk):**

1. **Start with mutation (safest):** Take existing problems the model fails on, mutate them in a structured way (change constants, add/remove constraints, alter variable relationships). The Arrows of Math and EvolMathEval approaches demonstrate this works reliably. Mutation preserves problem validity better than generation from scratch.

2. **Use weakness-category conditioning (medium risk):** Following SwS/WarriorMath, group failures by mathematical category (algebra, geometry, etc.) and generate new problems within those categories. This is coarser than specific error-type conditioning but much more reliable. Budget 40K problems per model as SwS does.

3. **Fine-grained error-type conditioning (highest risk, use with heavy filtering):** Following Self-Error-Instruct, condition on specific error keyphrases. But budget for a **3-5x rejection sampling overhead** beyond what you would expect for category-level conditioning. Expect ~10-25% of generated problems to actually trigger the targeted specific error pattern.

4. **Verifier-backed validation is essential:** The VHG paper shows that judge-backed filtering can recover valid hard candidates from a noisy generated pool, but end-to-end yield is only 5-22%. Build your pipeline assuming you need to generate 5-20x more candidates than your target dataset size.

**Budget planning numbers:**
- For 10K type-conditioned problems: generate 50K-200K candidates (5-20x overhead)
- Computational cost reference: DART-Math needed 5 days on 32 A100s for 590K problems from 150M samples
- Simpler estimate: for moderate-difficulty type conditioning, plan for ~10x rejection sampling ratio

---

### 5. The Fundamental Tension (Key Risk)

The hypothesis-driven error analysis paper identifies the core challenge: **generator quality degrades when targeting the model's weakest areas**. The generator LLM is itself weak in the same areas you want to target. High-accuracy hypotheses (the most useful ones) produce more flawed problems. This creates a catch-22 that no current paper has fully solved.

**Mitigations:**
- Use a stronger model as generator than the target model (e.g., GPT-4o/GPT-5 generating problems for a 7B model)
- Use symbolic/programmatic mutation rather than pure LLM generation for the hardest error types
- Accept that fine-grained error-type conditioning (e.g., "generate a problem that triggers sign errors in polynomial division") will have lower yield than coarse conditioning (e.g., "generate a hard algebra problem"), and plan your pipeline budget accordingly

---

### Sources

- [Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis](https://arxiv.org/html/2604.04386) - Key paper on hypothesis-driven error targeting, solve rate data (45-95% range)
- [Verifier-Backed Hard Problem Generation (VHG)](https://arxiv.org/html/2605.06660) - Best concrete yield data: 5.2-21.9% end-to-end yield
- [Self-Error-Instruct (ACL 2025)](https://aclanthology.org/2025.acl-long.417/) - Error keyphrase clustering and type-conditioned synthesis
- [SwS: Self-aware Weakness-driven Problem Synthesis](https://arxiv.org/abs/2506.08989) - 40K problems per model, [25%,75%] difficulty filtering, 50% answer consistency threshold
- [WarriorMath](https://arxiv.org/abs/2508.01245) - 5-model expert committee, N=16 rollouts, 12.57% average gain
- [DART-Math (NeurIPS 2024)](https://arxiv.org/abs/2407.13690) - nmax=2048-8192, 150M samples for 590K dataset, 250:1 ratio
- [FLAMES](https://arxiv.org/abs/2508.16514) - Solvability filter incorrectly rejects 30% of real problems, 50% of Level 5
- [EvolMathEval](https://arxiv.org/html/2508.13003v1) - Evolutionary mutation, 48% average accuracy reduction, dual-filter mechanism
- [Arrows of Math Reasoning Data Synthesis](https://arxiv.org/abs/2508.18824) - 12.3M to 1.8M pipeline, four mutation strategies
- [LEMMA](https://arxiv.org/pdf/2503.17439) - Error-type grounded mistake augmentation, &lt;90K examples
- [Controllable Text Generation Survey](https://dl.acm.org/doi/10.1145/3617680) - Attribute accuracy 85-92% for style/sentiment conditioning&lt;/result>
&lt;usage>&lt;total_tokens>41696&lt;/total_tokens>&lt;tool_uses>47&lt;/tool_uses>&lt;duration_ms>378454&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "026d7724-2d24-4ba2-ac5b-90301c495661",
  "isSidechain": false,
  "promptId": "23bca2a0-176a-49ed-8ea9-28b91f4d3190",
  "type": "user",
  "uuid": "a6eeb629-22f2-477a-8017-7d06aeb48e11",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "a6eeb629-22f2-477a-8017-7d06aeb48e11",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Assistant

_source line 71 · 2026-05-28T05:35:23.969Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent - this is very valuable research on type-conditioned prompting feasibility. Key insights:
1. No one reports direct success rates for error-type-conditioned generation
2. Estimated 10-25% yield for fine-grained error-type conditioning
3. A hybrid approach (mutation + category conditioning + fine-grained with heavy filtering) is recommended
4. The fundamental tension: generator quality degrades when targeting weak areas
5. Need 5-20x rejection sampling overhead

Still waiting for 1 more agent: taxonomy expansion/MAB.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6eeb629-22f2-477a-8017-7d06aeb48e11",
  "isSidechain": false,
  "requestId": "req_011CbURXqKaxad36eLcf3wHk",
  "type": "assistant",
  "uuid": "f5286baa-05b0-4550-82d8-d831893e9b65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013o4sb1JjhFNCTt4e7D6mJF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 43375,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 43375,
          "cache_creation_input_tokens": 3190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3190
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

_source line 72 · 2026-05-28T05:35:28.439Z_

Critical findings on type-conditioned prompting - realistic yield estimates (10-25% for fine-grained error targeting), hybrid mutation+generation fallback strategy, and the fundamental tension that generators are weak in the same areas they need to target. One more agent remaining.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5286baa-05b0-4550-82d8-d831893e9b65",
  "isSidechain": false,
  "requestId": "req_011CbURXqKaxad36eLcf3wHk",
  "type": "assistant",
  "uuid": "b5f1664b-b0dc-4fc1-a830-d70cb0d9bed6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013o4sb1JjhFNCTt4e7D6mJF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 43375,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 43375,
          "cache_creation_input_tokens": 3190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3190
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

_source line 73 · 2026-05-28T05:36:23.444Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:36:23.444Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "content": "&lt;task-notification>\n&lt;task-id>a8f539e114872a9c2&lt;/task-id>\n&lt;tool-use-id>toolu_0162oX1xwgsqRvrQSQwpXfVT&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a8f539e114872a9c2.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Research taxonomy expansion and MAB curriculum\" completed&lt;/summary>\n&lt;result>Now I have comprehensive information on both topics. Let me compile the findings.\n\n---\n\nHere is a detailed research report on both topics.\n\n---\n\n## Topic 1: Dynamic Error Taxonomy Expansion Mechanisms\n\n### Key Papers Found\n\n**1. ErrorMap/ErrorAtlas (Jan 2026)** - [arXiv:2601.15812](https://arxiv.org/abs/2601.15812)\nThe most directly relevant paper. ErrorMap is a methodology for systematically building error taxonomies from LLM failures across any benchmark.\n\n**Pipeline for building taxonomies:**\n- **Stage 1 (Per-instance analysis):** An analyst LLM examines each incorrect prediction, identifies the first major error causing failure, and generates a structured error label and summary. It uses \"Informative Correct Predictions\" (correct answers from other models) as reference points.\n- **Stage 2a (Category generation):** Iterative LLM-based data mining in three phases: (1) Category Generation - LLM receives error labels with frequencies and generates initial categories; (2) Iterative Refinement - multiple cycles where LLM receives previously generated categories plus new sampled batches, incrementally updating; (3) Final Review for coherence.\n- **Stage 2b (Error assignment):** Batched LLM call assigns each error label to the most appropriate category.\n- This recurses to build hierarchy: for each parent category, child categories are derived from errors assigned to it.\n\n**Detecting new error types:** New types emerge organically during the iterative refinement - unique labels that don't map to existing categories trigger new category creation.\n\n**Preventing taxonomy explosion:**\n- Maximum category limit of 25 per level (configurable)\n- Iterative consolidation merges similar error types during refinement\n- Hierarchical stopping when no further meaningful subdivisions exist\n- Result: 17 top-level categories in ErrorAtlas\n\n**Quality metrics:** 95.2% coverage (only 11 of 7,049 errors assigned to \"other\"), 92% inter-annotator agreement, robust to sample size variation.\n\n**Key insight:** The authors note \"a dynamic taxonomy that would fit an ad hoc analysis is best for many needs, [while] a stable taxonomy simplifies comparisons across time\" -- suggesting both evolving and static approaches are complementary.\n\n---\n\n**2. Sanders et al. \"Generating Data-Driven Reasoning Rubrics\" (Feb 2026)** - [arXiv:2602.06795](https://arxiv.org/abs/2602.06795)\nAuthors: Kate Sanders, Nathaniel Weir, Sapana Chaudhary, Kaj Bostrom, Huzefa Rangwala.\n\n**How they derive error taxonomies from data:**\n- Start with incorrect reasoning traces from a trained model\n- **Trace compression:** LLM summarizes traces to remove exploratory content, retaining only logical steps influencing the final answer\n- **Error extraction:** Claude 3.5 Sonnet v2 analyzes compressed traces against ground truth, identifying catastrophic errors\n- **Rubric item structuring:** Each error becomes a 3-part rubric item: (1) main error description (&lt;=25 words), (2) keyword for recall-optimized filtering, (3) verification details\n- **Keyword consolidation:** LLM groups related keywords, reducing count by ~50%\n\n**Taxonomy size:** 234-296 rubric items per domain, 89-169 keywords after clustering. Domains tested: SWE-Bench (coding), NuminaMath (math), Chemistry.\n\n**Preventing explosion:** Keyword clustering reduces redundancy by ~50%. Ablation tested sizes of 25, 50, 100, 150, and full. Larger rubrics generally better but domain-dependent.\n\n**Two-stage classification:** Keywords first filter traces (high recall), then detailed rubric items applied only to matching traces (high precision). This is an efficient way to use large taxonomies.\n\n**Key result:** +45% improvement over general LLM-as-judge baselines, approaching verifiable reward performance with only 20% of gold labels.\n\n**Limitation for dynamic expansion:** The paper does not describe an explicit mechanism for detecting when NEW error types should be added post-generation. The rubric is generated once from training data. However, the pipeline could be re-run periodically on new failure data.\n\n---\n\n**3. TaxoAdapt (2025)** - [arXiv:2506.10737](https://arxiv.org/abs/2506.10737)\nFramework for constructing multidimensional taxonomies that dynamically adapt to corpora.\n\n**Key mechanisms for expansion:**\n- Knowledge-augmented expansion using LLMs\n- Hierarchical text classification for targeted exploration\n- Taxonomy-aware clustering that determines granularity-consistent candidate entities, maximizing coverage while minimizing redundancy\n- Iteratively expands both taxonomy width and depth based on topical distribution\n\n**Results:** 26.51% more granularity-preserving and 50.41% more coherent than baselines.\n\n---\n\n**4. TaxoCom (WWW 2022)** - [arXiv:2201.06771](https://arxiv.org/abs/2201.06771)\nTaxonomy completion with hierarchical discovery of novel topic clusters.\n\n**Key mechanism for detecting new categories:**\n- **Locally discriminative embedding:** Optimizes embedding space to be discriminative among known sub-topics\n- **Novelty adaptive clustering:** Assigns terms into either known sub-topics OR novel sub-topics\n- This dual assignment is the key -- it explicitly separates known vs. novel category detection\n\n---\n\n**5. FLAME (2024)** - [arXiv:2402.13623](https://arxiv.org/abs/2402.13623)\nSelf-supervised low-resource taxonomy expansion using LLMs. Uses few-shot prompting to extract hypernym knowledge, plus reinforcement learning for fine-tuning. +12.8% accuracy over 11 baselines.\n\n---\n\n### Concrete Mechanisms Summary for Your Needs\n\n**How to detect when a new error type should be added:**\n- **Embedding distance threshold approach:** Compute embedding centroid for each existing error category. New errors whose distance to all centroids exceeds a threshold (Euclidean or Mahalanobis) are candidates for new categories. KNN-based average distance scoring also works.\n- **ErrorMap approach:** Re-run iterative LLM-based clustering periodically on new failure data; new labels that don't map to existing categories organically surface as new types.\n- **TaxoCom approach:** Novelty-adaptive clustering explicitly partitions new data into \"known\" vs. \"novel\" clusters.\n- **Accumulation trigger:** Monitor an \"other/uncategorized\" bin -- when it exceeds a percentage threshold (e.g., &gt;5% of recent errors), trigger re-clustering.\n\n**How to merge or split error categories:**\n- **ErrorMap:** Recursive top-down construction naturally splits. Iterative refinement consolidates (merges) similar types across cycles.\n- **Sanders rubric:** Keyword clustering merges related categories (~50% reduction). No explicit split mechanism, but hierarchy depth handles granularity.\n- **Quantitative signals for merge:** If two categories have cosine similarity &gt;0.9 in embedding space, or if one category's frequency drops below a minimum threshold, merge.\n- **Quantitative signals for split:** If intra-category variance exceeds inter-category variance for the nearest neighbor, or if a category's error count grows disproportionately, split.\n\n**How to prevent taxonomy explosion:**\n- Hard cap on categories per level (ErrorMap uses max 25)\n- Keyword/semantic clustering to consolidate similar items (~50% reduction per Sanders)\n- Minimum frequency thresholds -- prune categories below N instances\n- Hierarchical depth limits (ErrorMap uses max 3 layers)\n- Iterative consolidation during refinement cycles\n\n---\n\n## Topic 2: Multi-Armed Bandit (MAB) Based Curriculum Approaches\n\n### The SEC Paper\n\n**Full reference:** \"Self-Evolving Curriculum for LLM Reasoning\" by Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo. [arXiv:2505.14970](https://arxiv.org/abs/2505.14970). Code: [github.com/ServiceNow/sec](https://github.com/ServiceNow/sec).\n\n### How MAB-Based Curriculum Works\n\n**Formulation:** Each problem category (difficulty level, problem type) = one arm in a non-stationary MAB.\n\n**Reward signal:** Absolute advantage from policy gradient:\n```\nr(c) = E_{(s_t,a_t) ~ pi_theta(x_i), x_i ~ c} |A_hat_t|\n```\nThis measures immediate learning gain. Under binary rewards with success rate p, this simplifies to `2*sqrt(p*(1-p))`, maximized at p=0.5 -- problems of intermediate difficulty yield most learning.\n\n**Policy:** Boltzmann distribution over Q-values:\n```\np(c) = exp(Q_t(c)/tau) / sum_i exp(Q_t(c_i)/tau)\n```\n\n**Update:** TD(0) exponential moving average:\n```\nQ_{t+1}(c) = alpha * r_t(c) + (1-alpha) * Q_t(c)\n```\n\n**Non-stationarity handling:** The exponential moving average naturally forgets old reward estimates as the model improves, continuously adapting which categories are most useful.\n\n### Key Quantitative Results (SEC vs. Baselines)\n\nBaselines are **Random** (uniform allocation) and **Difficulty-Ordered** (easy-to-hard curriculum). No explicit \"proportional allocation\" baseline was tested.\n\n| Task | Split | Random | Ordered | **SEC** |\n|------|-------|--------|---------|---------|\n| Countdown | OOD | 0.479 | 0.321 | **0.542** |\n| Zebra | OOD | 0.285 | 0.329 | **0.345** |\n| ARC-1D | OOD | 0.313 | 0.363 | **0.381** |\n| AIME24 | - | 0.075 | 0.054 | **0.100** |\n\nRelative improvements: +13% (Countdown), +21% (Zebra), +22% (ARC-1D), +33% (AIME24) over random.\n\nSEC generalizes across RL algorithms (GRPO, PPO, RLOO). With PPO: ID 0.621 -&gt; 0.750, OOD 0.159 -&gt; 0.224.\n\n**SEC-2D (multi-task, 9 arms):** Random curriculum shows performance collapse mid-training; SEC-2D maintains stable performance. E.g., ARC OOD: 0.251 (random) vs. 0.327 (SEC-2D).\n\n### How MAB Compares to Proportional Allocation\n\nThe SEC paper does **not** directly compare against proportional allocation (sampling categories proportional to their size or error frequency). Its baselines are:\n- **Uniform/Random** -- equal probability across all categories\n- **Difficulty-Ordered** -- sequential easy-to-hard\n\nHowever, the mathematical analysis is informative: the reward `2*sqrt(p*(1-p))` is maximized at p=0.5, meaning MAB naturally gravitates toward categories where the model has ~50% success rate. This is fundamentally different from error-type-proportional allocation, which would over-sample frequent error types regardless of learnability. **MAB-based selection is learning-gain-optimized rather than frequency-optimized.**\n\n### SPaRFT (Aug 2025) - Another MAB Curriculum Paper\n\n[arXiv:2508.05015](https://arxiv.org/abs/2508.05015) - \"Self-Paced Reinforcement Fine-Tuning.\" Combines semantic clustering with MAB:\n- Clusters training data by semantics AND difficulty\n- Each cluster = one bandit arm\n- Uses **Thompson Sampling** (vs. SEC's Boltzmann/TD(0))\n- Achieves comparable or better accuracy with up to **100x fewer samples**\n\n### Is MAB a Useful Alternative to Error-Type-Proportional Allocation?\n\n**Yes, and the comparison is illuminating:**\n\n1. **Proportional allocation** (sample error types proportional to their frequency) assumes all errors are equally learnable and valuable to fix. This is naive -- some error types may be nearly solved (high success rate), while others may be too hard for the current model.\n\n2. **MAB-based allocation** optimizes for *learning gain* -- it automatically discovers which error categories offer the most improvement at each training stage. It naturally implements a \"zone of proximal development\" by favoring categories with ~50% success rate.\n\n3. **Key advantage of MAB:** It adapts as the model improves. Early in training, basic errors may be most learnable. Later, the model has fixed those and the MAB shifts to harder categories. Proportional allocation doesn't adapt.\n\n4. **Key advantage of proportional allocation:** It ensures coverage of all error types, preventing rare-but-important errors from being ignored. MAB might under-sample rare categories that happen to be too hard currently.\n\n5. **Best hybrid:** Use proportional allocation as a *floor* (minimum sampling rate per category) combined with MAB for the remaining budget. This ensures coverage while optimizing learning gain.\n\n### Additional Related Papers\n\n- [Curriculum Reinforcement Learning from Easy to Hard](https://arxiv.org/pdf/2506.06632) (2025)\n- [AdaCuRL: Adaptive Curriculum RL](https://arxiv.org/pdf/2511.09478) - addresses invalid sample mitigation when difficulty extremes cause reward collapse\n- [LASeR: Learning to Adaptively Select Reward Models with MAB](https://arxiv.org/pdf/2410.01735) - applies bandit to reward model selection rather than data selection&lt;/result>\n&lt;usage>&lt;total_tokens>34163&lt;/total_tokens>&lt;tool_uses>29&lt;/tool_uses>&lt;duration_ms>436626&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
````

---

### Runtime record

_source line 74 · 2026-05-28T05:36:23.528Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:36:23.528Z",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

## Round 9

13 recorded events

### User

_source line 75 · 2026-05-28T05:36:23.538Z_

&lt;task-notification>
&lt;task-id>a8f539e114872a9c2&lt;/task-id>
&lt;tool-use-id>toolu_0162oX1xwgsqRvrQSQwpXfVT&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu-idea-review/35b5d14c-5b69-46e3-9166-8ee9b68949f7/tasks/a8f539e114872a9c2.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Research taxonomy expansion and MAB curriculum" completed&lt;/summary>
&lt;result>Now I have comprehensive information on both topics. Let me compile the findings.

---

Here is a detailed research report on both topics.

---

## Topic 1: Dynamic Error Taxonomy Expansion Mechanisms

### Key Papers Found

**1. ErrorMap/ErrorAtlas (Jan 2026)** - [arXiv:2601.15812](https://arxiv.org/abs/2601.15812)
The most directly relevant paper. ErrorMap is a methodology for systematically building error taxonomies from LLM failures across any benchmark.

**Pipeline for building taxonomies:**
- **Stage 1 (Per-instance analysis):** An analyst LLM examines each incorrect prediction, identifies the first major error causing failure, and generates a structured error label and summary. It uses "Informative Correct Predictions" (correct answers from other models) as reference points.
- **Stage 2a (Category generation):** Iterative LLM-based data mining in three phases: (1) Category Generation - LLM receives error labels with frequencies and generates initial categories; (2) Iterative Refinement - multiple cycles where LLM receives previously generated categories plus new sampled batches, incrementally updating; (3) Final Review for coherence.
- **Stage 2b (Error assignment):** Batched LLM call assigns each error label to the most appropriate category.
- This recurses to build hierarchy: for each parent category, child categories are derived from errors assigned to it.

**Detecting new error types:** New types emerge organically during the iterative refinement - unique labels that don't map to existing categories trigger new category creation.

**Preventing taxonomy explosion:**
- Maximum category limit of 25 per level (configurable)
- Iterative consolidation merges similar error types during refinement
- Hierarchical stopping when no further meaningful subdivisions exist
- Result: 17 top-level categories in ErrorAtlas

**Quality metrics:** 95.2% coverage (only 11 of 7,049 errors assigned to "other"), 92% inter-annotator agreement, robust to sample size variation.

**Key insight:** The authors note "a dynamic taxonomy that would fit an ad hoc analysis is best for many needs, [while] a stable taxonomy simplifies comparisons across time" -- suggesting both evolving and static approaches are complementary.

---

**2. Sanders et al. "Generating Data-Driven Reasoning Rubrics" (Feb 2026)** - [arXiv:2602.06795](https://arxiv.org/abs/2602.06795)
Authors: Kate Sanders, Nathaniel Weir, Sapana Chaudhary, Kaj Bostrom, Huzefa Rangwala.

**How they derive error taxonomies from data:**
- Start with incorrect reasoning traces from a trained model
- **Trace compression:** LLM summarizes traces to remove exploratory content, retaining only logical steps influencing the final answer
- **Error extraction:** Claude 3.5 Sonnet v2 analyzes compressed traces against ground truth, identifying catastrophic errors
- **Rubric item structuring:** Each error becomes a 3-part rubric item: (1) main error description (&lt;=25 words), (2) keyword for recall-optimized filtering, (3) verification details
- **Keyword consolidation:** LLM groups related keywords, reducing count by ~50%

**Taxonomy size:** 234-296 rubric items per domain, 89-169 keywords after clustering. Domains tested: SWE-Bench (coding), NuminaMath (math), Chemistry.

**Preventing explosion:** Keyword clustering reduces redundancy by ~50%. Ablation tested sizes of 25, 50, 100, 150, and full. Larger rubrics generally better but domain-dependent.

**Two-stage classification:** Keywords first filter traces (high recall), then detailed rubric items applied only to matching traces (high precision). This is an efficient way to use large taxonomies.

**Key result:** +45% improvement over general LLM-as-judge baselines, approaching verifiable reward performance with only 20% of gold labels.

**Limitation for dynamic expansion:** The paper does not describe an explicit mechanism for detecting when NEW error types should be added post-generation. The rubric is generated once from training data. However, the pipeline could be re-run periodically on new failure data.

---

**3. TaxoAdapt (2025)** - [arXiv:2506.10737](https://arxiv.org/abs/2506.10737)
Framework for constructing multidimensional taxonomies that dynamically adapt to corpora.

**Key mechanisms for expansion:**
- Knowledge-augmented expansion using LLMs
- Hierarchical text classification for targeted exploration
- Taxonomy-aware clustering that determines granularity-consistent candidate entities, maximizing coverage while minimizing redundancy
- Iteratively expands both taxonomy width and depth based on topical distribution

**Results:** 26.51% more granularity-preserving and 50.41% more coherent than baselines.

---

**4. TaxoCom (WWW 2022)** - [arXiv:2201.06771](https://arxiv.org/abs/2201.06771)
Taxonomy completion with hierarchical discovery of novel topic clusters.

**Key mechanism for detecting new categories:**
- **Locally discriminative embedding:** Optimizes embedding space to be discriminative among known sub-topics
- **Novelty adaptive clustering:** Assigns terms into either known sub-topics OR novel sub-topics
- This dual assignment is the key -- it explicitly separates known vs. novel category detection

---

**5. FLAME (2024)** - [arXiv:2402.13623](https://arxiv.org/abs/2402.13623)
Self-supervised low-resource taxonomy expansion using LLMs. Uses few-shot prompting to extract hypernym knowledge, plus reinforcement learning for fine-tuning. +12.8% accuracy over 11 baselines.

---

### Concrete Mechanisms Summary for Your Needs

**How to detect when a new error type should be added:**
- **Embedding distance threshold approach:** Compute embedding centroid for each existing error category. New errors whose distance to all centroids exceeds a threshold (Euclidean or Mahalanobis) are candidates for new categories. KNN-based average distance scoring also works.
- **ErrorMap approach:** Re-run iterative LLM-based clustering periodically on new failure data; new labels that don't map to existing categories organically surface as new types.
- **TaxoCom approach:** Novelty-adaptive clustering explicitly partitions new data into "known" vs. "novel" clusters.
- **Accumulation trigger:** Monitor an "other/uncategorized" bin -- when it exceeds a percentage threshold (e.g., &gt;5% of recent errors), trigger re-clustering.

**How to merge or split error categories:**
- **ErrorMap:** Recursive top-down construction naturally splits. Iterative refinement consolidates (merges) similar types across cycles.
- **Sanders rubric:** Keyword clustering merges related categories (~50% reduction). No explicit split mechanism, but hierarchy depth handles granularity.
- **Quantitative signals for merge:** If two categories have cosine similarity &gt;0.9 in embedding space, or if one category's frequency drops below a minimum threshold, merge.
- **Quantitative signals for split:** If intra-category variance exceeds inter-category variance for the nearest neighbor, or if a category's error count grows disproportionately, split.

**How to prevent taxonomy explosion:**
- Hard cap on categories per level (ErrorMap uses max 25)
- Keyword/semantic clustering to consolidate similar items (~50% reduction per Sanders)
- Minimum frequency thresholds -- prune categories below N instances
- Hierarchical depth limits (ErrorMap uses max 3 layers)
- Iterative consolidation during refinement cycles

---

## Topic 2: Multi-Armed Bandit (MAB) Based Curriculum Approaches

### The SEC Paper

**Full reference:** "Self-Evolving Curriculum for LLM Reasoning" by Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo. [arXiv:2505.14970](https://arxiv.org/abs/2505.14970). Code: [github.com/ServiceNow/sec](https://github.com/ServiceNow/sec).

### How MAB-Based Curriculum Works

**Formulation:** Each problem category (difficulty level, problem type) = one arm in a non-stationary MAB.

**Reward signal:** Absolute advantage from policy gradient:
```
r(c) = E_{(s_t,a_t) ~ pi_theta(x_i), x_i ~ c} |A_hat_t|
```
This measures immediate learning gain. Under binary rewards with success rate p, this simplifies to `2*sqrt(p*(1-p))`, maximized at p=0.5 -- problems of intermediate difficulty yield most learning.

**Policy:** Boltzmann distribution over Q-values:
```
p(c) = exp(Q_t(c)/tau) / sum_i exp(Q_t(c_i)/tau)
```

**Update:** TD(0) exponential moving average:
```
Q_{t+1}(c) = alpha * r_t(c) + (1-alpha) * Q_t(c)
```

**Non-stationarity handling:** The exponential moving average naturally forgets old reward estimates as the model improves, continuously adapting which categories are most useful.

### Key Quantitative Results (SEC vs. Baselines)

Baselines are **Random** (uniform allocation) and **Difficulty-Ordered** (easy-to-hard curriculum). No explicit "proportional allocation" baseline was tested.

| Task | Split | Random | Ordered | **SEC** |
|------|-------|--------|---------|---------|
| Countdown | OOD | 0.479 | 0.321 | **0.542** |
| Zebra | OOD | 0.285 | 0.329 | **0.345** |
| ARC-1D | OOD | 0.313 | 0.363 | **0.381** |
| AIME24 | - | 0.075 | 0.054 | **0.100** |

Relative improvements: +13% (Countdown), +21% (Zebra), +22% (ARC-1D), +33% (AIME24) over random.

SEC generalizes across RL algorithms (GRPO, PPO, RLOO). With PPO: ID 0.621 -&gt; 0.750, OOD 0.159 -&gt; 0.224.

**SEC-2D (multi-task, 9 arms):** Random curriculum shows performance collapse mid-training; SEC-2D maintains stable performance. E.g., ARC OOD: 0.251 (random) vs. 0.327 (SEC-2D).

### How MAB Compares to Proportional Allocation

The SEC paper does **not** directly compare against proportional allocation (sampling categories proportional to their size or error frequency). Its baselines are:
- **Uniform/Random** -- equal probability across all categories
- **Difficulty-Ordered** -- sequential easy-to-hard

However, the mathematical analysis is informative: the reward `2*sqrt(p*(1-p))` is maximized at p=0.5, meaning MAB naturally gravitates toward categories where the model has ~50% success rate. This is fundamentally different from error-type-proportional allocation, which would over-sample frequent error types regardless of learnability. **MAB-based selection is learning-gain-optimized rather than frequency-optimized.**

### SPaRFT (Aug 2025) - Another MAB Curriculum Paper

[arXiv:2508.05015](https://arxiv.org/abs/2508.05015) - "Self-Paced Reinforcement Fine-Tuning." Combines semantic clustering with MAB:
- Clusters training data by semantics AND difficulty
- Each cluster = one bandit arm
- Uses **Thompson Sampling** (vs. SEC's Boltzmann/TD(0))
- Achieves comparable or better accuracy with up to **100x fewer samples**

### Is MAB a Useful Alternative to Error-Type-Proportional Allocation?

**Yes, and the comparison is illuminating:**

1. **Proportional allocation** (sample error types proportional to their frequency) assumes all errors are equally learnable and valuable to fix. This is naive -- some error types may be nearly solved (high success rate), while others may be too hard for the current model.

2. **MAB-based allocation** optimizes for *learning gain* -- it automatically discovers which error categories offer the most improvement at each training stage. It naturally implements a "zone of proximal development" by favoring categories with ~50% success rate.

3. **Key advantage of MAB:** It adapts as the model improves. Early in training, basic errors may be most learnable. Later, the model has fixed those and the MAB shifts to harder categories. Proportional allocation doesn't adapt.

4. **Key advantage of proportional allocation:** It ensures coverage of all error types, preventing rare-but-important errors from being ignored. MAB might under-sample rare categories that happen to be too hard currently.

5. **Best hybrid:** Use proportional allocation as a *floor* (minimum sampling rate per category) combined with MAB for the remaining budget. This ensures coverage while optimizing learning gain.

### Additional Related Papers

- [Curriculum Reinforcement Learning from Easy to Hard](https://arxiv.org/pdf/2506.06632) (2025)
- [AdaCuRL: Adaptive Curriculum RL](https://arxiv.org/pdf/2511.09478) - addresses invalid sample mitigation when difficulty extremes cause reward collapse
- [LASeR: Learning to Adaptively Select Reward Models with MAB](https://arxiv.org/pdf/2410.01735) - applies bandit to reward model selection rather than data selection&lt;/result>
&lt;usage>&lt;total_tokens>34163&lt;/total_tokens>&lt;tool_uses>29&lt;/tool_uses>&lt;duration_ms>436626&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5f1664b-b0dc-4fc1-a830-d70cb0d9bed6",
  "isSidechain": false,
  "promptId": "60780c74-3181-49b9-b43d-765dac2f38fa",
  "type": "user",
  "uuid": "72dc60d4-b035-408a-89e8-7efd7d12f979",
  "permissionMode": "default",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 76 · 2026-05-28T05:37:24.055Z_

<details><summary>Logged reasoning block</summary>

```text
All 8 research agents have completed. Let me now synthesize all the findings and produce the revised proposal.

Let me organize what I've learned:

## Key Research Findings

### 1. Missing Competitors (Moderate)
**Socratic-Zero** (arXiv:2509.24726):
- Teacher-Solver-Generator co-evolution, +15.2-15.4pp over comparable baselines (the +20.2pp is vs SFT baseline)
- Teacher targets weaknesses at instance-level (individual failed solutions), NOT error-type level
- No PRM, no error taxonomy, no step-level feedback


- Uses DPO for solver training with binary outcome verification, but lacks structured error diagnosis and can't aggregate error patterns across problems

**SAGE** (arXiv:2603.15255):
- 4-agent system with Challenger, Planner, Solver, and Critic components in co-evolution
- Critic filters quality rather than diagnosing errors, with no PRM or error taxonomy
- Achieves +8.9% on LiveCodeBench and +10.7% on OlympiadBench with Qwen-2.5-7B, though training becomes unstable after step 120

**WarriorMath** (arXiv:2508.01245):
- Defect-aware approach...

Actually, looking at the next thinking, WarriorMath is positioned as defect-aware in name but relies on binary pass/fail outcomes in practice, using a 5-model expert committee without PRM and iterative DPO across 3 rounds, yet still lacks explicit error-type classification despite its framing.

Beyond these, LEMMA introduces 7 explicit error types with error-type-grounded mistake augmentation, though it only uses static SFT without curriculum or co-evolution, making it the closest precursor to error-driven training. There's also work on error classification for math word problems that identifies 39 dynamic error clusters via K-means and applies error-aware prompting at inference time, but without any training signal or curriculum integration.

Other related approaches include bidirectional curriculum learning that simplifies or complicates problems based on pass/fail outcomes without an error taxonomy, verifier-backed self-play focused on difficulty rather than error diagnosis, and format-based reformulation through multiple question types that doesn't address underlying content errors.

On type-conditioned prompting specifically, I'm not finding direct success rates reported anywhere, and the feasibility looks limited—estimates suggest only 10-25% yield for fine-grained error-type conditioning with 5-20x rejection sampling overhead needed, since the fundamental issue is that the generator tends to be weak in the same areas where errors occur. A hybrid approach combining mutation as the primary strategy with category conditioning and selective fine-grained prompting seems more practical.

For expanding the taxonomy itself, I'm seeing several mechanisms: iterative LLM-based clustering that can reach about 25 categories per level with 95% coverage, keyword-based approaches that reduce categories by roughly 50%, and novelty-adaptive clustering that distinguishes known from novel error types. The concrete implementation details involve embedding distance thresholds, monitoring an "other" bin for uncategorized errors, and using variance metrics to decide when to split or merge categories.

There's also a multi-armed bandit approach from the Bengio group that treats problem categories as arms and allocates curriculum based on maximizing advantage at the 0.5 difficulty point, showing 13-33% improvements over random allocation.

Now I need to note that the GRPO-PRM paper I should cite is the arXiv preprint under review at ICML 2026, not the withdrawn OpenReview version which is actually a different paper on GRPO-lambda. For PRM generalization, the main challenge is that these models don't transfer well across different model architectures or question types, so I'm looking at strategies like generative verification, bootstrapping on the target model's own traces, retrieval augmentation, and adversarial training to improve robustness, with consensus labeling helping during the cold-start phase on new models.

The crowded field is the real pressure point—25 to 30 papers in the last year means I need either an 8+ percentage point improvement or a genuinely novel analytical angle. The error-type analysis is where I can differentiate: tracking how error distributions evolve across training iterations hasn't been done in co-evolution work before, but I need to make it prescriptive rather than just descriptive. The most underexplored territory is analytical contributions, and combining error-type categories with MAB-based curriculum allocation could be the key to making this work stand out, especially with an ICLR 2027 deadline around September-October 2026.

I'm mapping out the concrete changes needed: filling in all the missing competitors in the landscape, specifying the hybrid generation approach with mutation as the primary strategy and generation as fallback, detailing the taxonomy expansion mechanism using existing frameworks, replacing pure proportional allocation with MAB-based methods, bootstrapping the PRM to handle cold-start, and fixing the GRPO-PRM citation. This is a substantial revision that strengthens the differentiation around predictive error dynamics and the MAB plus error-types synthesis, but it's not a fundamental pivot—more of a major refinement to address the reviewer's core concerns.

Now I'm reconsidering whether the real differentiator should be analytical rather than purely empirical. The crowded field means incremental gains won't stand out, but understanding how error-type distributions evolve across iterations could be genuinely novel if it's predictive. I'm thinking about reframing this as a theory-plus-practice paper: the primary contribution becomes understanding and predicting error dynamics in co-evolutionary self-improvement, the MAB plus error-type curriculum becomes the prescriptive application, and the PRM shifts to being a diagnostic tool cleanly separated from the reward signal. This positioning feels stronger for ICLR 2027.

For the MAB component, instead of just allocating proportionally across error types, I could use multi-armed bandits to optimize which error categories to focus on—balancing between common errors that are already being fixed, rare errors with high learning potential, and errors that are currently too difficult. This naturally implements curriculum adaptation and is more sophisticated than simple proportional allocation. I'm also planning to integrate hybrid generation with mutation-first as the primary strategy, expand the taxonomy using an ErrorMap-inspired mechanism, add recent baselines like Socratic-Zero and SAGE to the landscape, and include a cold-start strategy for the PRM.

Now I'm refining the core contribution: understanding error dynamics through analysis plus a prescriptive error-type MAB curriculum. I should also explore whether error distributions can predict convergence or collapse. The reviewer specifically mentioned the SEC paper's MAB approach, so I need to explicitly contrast MAB-based allocation against proportional allocation and frame our work as a synthesis. This is a substantial revision, so I'm restructuring the entire JSON proposal—tightening the title, refining the core problem and opportunity, expanding the landscape comprehensively, and overhauling the approach section with all the generation, allocation, and taxonomy changes.

Writing the full proposal now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72dc60d4-b035-408a-89e8-7efd7d12f979",
  "isSidechain": false,
  "requestId": "req_011CbURcbgC6W9DzAqg7Do95",
  "type": "assistant",
  "uuid": "155a36f5-86ad-4667-9dc4-9abb3f3c4e9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DisHFjgcUWd8YE5y8ot7uH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3751,
      "cache_read_input_tokens": 46565,
      "output_tokens": 2348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2348,
          "cache_read_input_tokens": 46565,
          "cache_creation_input_tokens": 3751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3751
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

_source line 77 · 2026-05-28T05:37:24.073Z_

All 8 research agents have completed. Now I have comprehensive findings on every issue. Let me synthesize everything into the revised proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "155a36f5-86ad-4667-9dc4-9abb3f3c4e9a",
  "isSidechain": false,
  "requestId": "req_011CbURcbgC6W9DzAqg7Do95",
  "type": "assistant",
  "uuid": "20df692f-7b4f-4eb9-802f-f9477f4fedd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DisHFjgcUWd8YE5y8ot7uH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3751,
      "cache_read_input_tokens": 46565,
      "output_tokens": 2348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2348,
          "cache_read_input_tokens": 46565,
          "cache_creation_input_tokens": 3751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3751
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

_source line 78 · 2026-05-28T05:37:24.075Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AqmL86KXVU6UmW2rUDj72T`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20df692f-7b4f-4eb9-802f-f9477f4fedd7",
  "isSidechain": false,
  "requestId": "req_011CbURcbgC6W9DzAqg7Do95",
  "type": "assistant",
  "uuid": "92d689de-eee1-4dae-8bed-3bc3a0bbe7b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DisHFjgcUWd8YE5y8ot7uH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3751,
      "cache_read_input_tokens": 46565,
      "output_tokens": 2348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2348,
          "cache_read_input_tokens": 46565,
          "cache_creation_input_tokens": 3751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3751
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

_source line 79 · 2026-05-28T05:37:24.082Z_

<details><summary>↩ Tool result · `toolu_01AqmL86KXVU6UmW2rUDj72T`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92d689de-eee1-4dae-8bed-3bc3a0bbe7b0",
  "isSidechain": false,
  "promptId": "60780c74-3181-49b9-b43d-765dac2f38fa",
  "type": "user",
  "uuid": "f3ebb5f7-7dc1-46b6-a9d9-007c7d9f5d43",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "92d689de-eee1-4dae-8bed-3bc3a0bbe7b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 80 · 2026-05-28T05:37:24.128Z_

```json
{
  "parentUuid": "f3ebb5f7-7dc1-46b6-a9d9-007c7d9f5d43",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "34c2707e-9ec4-4735-bdf2-eeebe9770c2d",
  "timestamp": "2026-05-28T05:37:24.128Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "34c2707e-9ec4-4735-bdf2-eeebe9770c2d",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 82_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Assistant

_source line 83 · 2026-05-28T05:41:12.615Z_

Now let me synthesize all research findings into the complete revised proposal. This is a major revision with substantial methodological refinements.

```json
{
  "change_type": "major",
  "title": "Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diagnostic Co-Evolution",
  "core_problem": "Can a PRM serving as a co-evolving diagnostic instrument—classifying step-level reasoning failures into an evolving error taxonomy and feeding a bandit-based curriculum allocator—drive more efficient self-improvement than instance-level weakness targeting (Socratic-Zero), concept-level weakness extraction (SwS), scalar uncertainty targeting (R-Zero), embedding-diversity coverage (Prism), or multi-agent quality filtering (SAGE), and does tracking error-type distribution dynamics across iterations yield predictive signals for convergence and curriculum collapse?",
  "opportunity": "Self-improving reasoning loops have proliferated rapidly, with 25–30 directly relevant papers in the last 12 months alone (ICLR 2026 RSI Workshop accepted 110 papers). Yet despite this activity, every existing framework diagnoses weaknesses at a granularity that is either too coarse or unstructured to support targeted remediation. Socratic-Zero (Sep 2025) achieves +15.4pp via Teacher-generated problems from individual failed solutions but performs instance-level targeting without aggregating error patterns—it cannot detect that 40% of algebra failures stem from sign errors vs. 60% from conceptual gaps. SwS (NeurIPS 2025) achieves 10%/7.7% gains via concept-level weakness identification but conflates distinct failure modes under shared topic labels. R-Zero (ICLR 2026) achieves +6.49 via uncertainty-based co-evolution but its curriculum signal is purely scalar (p̂ ≈ 0.5). SAGE (March 2026) implements 4-agent co-evolution where the Critic scores quality but not error type—it is a filter, not a diagnoser. WarriorMath (Aug 2025) claims 'defect-aware' synthesis but operationalizes defects as binary pass/fail across 16 rollouts. Prism (March 2026) preserves embedding-space diversity but not diagnostic diversity. Meanwhile, the analytical tools exist but remain disconnected from curriculum design: LEMMA (ACL 2025) defines 7 error types for static SFT; Error Classification of LLMs on MWP (EMNLP 2025) discovers 39 dynamic error clusters but uses them only for inference-time prompting; ErrorMap (Jan 2026) builds hierarchical error taxonomies with 95.2% coverage but applies them only for evaluation. The untapped synthesis: use a PRM as a co-evolving diagnostic instrument whose step-level error-type classifications feed a bandit-based curriculum allocator that optimizes learning gain per error category, while tracking error-type distribution dynamics to predict convergence and detect curriculum collapse before it occurs. Two problems may share the same concept (algebra), difficulty level, and even the same error instance pattern yet fail for structurally different reasons (sign propagation error vs. domain restriction oversight)—only error-type-level diagnosis with aggregated statistics can detect these systematic patterns and allocate training resources accordingly. The Self-Evolving Curriculum (SEC, Bengio group, 2025) demonstrates that bandit-based allocation over problem categories yields +13–33% gains over random allocation, but operates on difficulty levels, not error types. Combining MAB allocation with error-type categories would optimize for learning gain per error category—automatically deprioritizing error types that are already being fixed (diminishing returns) or currently too hard (low returns), and upweighting the most learnable weaknesses at each iteration.",
  "landscape": "**Primary co-evolution baselines:** R-Zero (ICLR 2026) achieves +6.49 (Qwen3-4B) via GRPO-trained challenger targeting p̂ = 0.5 uncertainty, but pseudo-label accuracy degrades from 79% to 63% across iterations and the curriculum signal is purely scalar difficulty. Socratic-Zero (arXiv:2509.24726, Sep 2025) achieves +15.4pp (Qwen3-8B) via Teacher-Solver-Generator co-evolution where the Teacher crafts new problems from individual failed solutions using zone-adaptive generation (Gaussian utility centered at 50% success rate); however, it performs instance-level targeting without error taxonomy or step-level diagnosis—it cannot aggregate error patterns across failures or detect systematic weaknesses. SAGE (arXiv:2603.15255, March 2026) implements 4-agent co-evolution (Challenger/Planner/Solver/Critic) with Task-Relative REINFORCE++ achieving +8.9% on LiveCodeBench and +10.7% on OlympiadBench (Qwen-2.5-7B), but the Critic is a quality filter (scores clarity/relevance on a 1–10 scale), not an error diagnoser—weakness detection is purely implicit through difficulty rewards with no error categorization. WarriorMath (arXiv:2508.01245, Aug 2025) implements 'defect-aware' synthesis with a 5-model expert committee and iterative DPO (36.7%→48.3% on AIME'24 across 3 iterations), but operationalizes defects as binary pass/fail across 16 rollouts with no formal error taxonomy despite the title's implication.\n\n**Weakness-driven synthesis (non-co-evolutionary):** SwS (NeurIPS 2025) achieves 10%/7.7% average gains (Qwen2.5-7B/32B) via outcome-level weakness identification → concept extraction → concept recombination → filtered problem generation; single-round, no PRM, cannot distinguish failures sharing the same topic but differing in error pattern.\n\n**Diversity and curriculum:** Prism (March 2026) addresses R-Zero's diversity collapse via embedding-cluster-based rarity bonuses (+3.98 AMC), but diversity is geometric rather than diagnostic. Vocabulary Dropout (April 2026) injects random token-mask diversity (+4.4 avg on Qwen3-8B) but is blind to what kinds of diversity benefit the solver. Self-Evolving Curriculum (SEC, arXiv:2505.14970, Bengio group) formulates curriculum as multi-armed bandit over problem categories, yielding +13–33% over random allocation via learning-gain-optimized selection; operates on difficulty levels, not error types. Cog-DRIFT (arXiv:2604.04767, April 2026) achieves +10.11% on hard problems via format reformulation (MCQ→cloze→open-ended) with instance-level adaptive progression, but reformulates task format rather than targeting error-type-specific content. Bidirectional Curriculum (arXiv:2603.05120, March 2026) simplifies/complicates problems based on pass/fail signals with a multi-agent framework, but adapts difficulty direction without error taxonomy.\n\n**Error taxonomy and diagnosis:** LEMMA (ACL 2025 Findings, arXiv:2503.17439) defines 7 error types (Calculation/Counting/Formula-Confusion/Question-Misinterpretation/Missing-Step/Confusing-Concept/Nonsensical) for error-type-grounded mistake augmentation in static SFT (~89K examples); closest precursor to error-type-driven training but no curriculum, no co-evolution, no RL. Error Classification of LLMs on MWP (EMNLP 2025 Findings, arXiv:2501.15581) discovers 39 dynamic error clusters via K-means on GPT-4o-analyzed failures and applies Error-Aware Prompting (+26.33% on MATH for Llama-3.1-8B), but uses error knowledge only at inference time, not for training or curriculum. Data-Driven Reasoning Rubrics (arXiv:2602.06795, Feb 2026) derives 234–296 rubric items per domain with keyword clustering (~50% consolidation), achieving +45% over LLM-as-judge baselines; generates rubrics once without iteration or curriculum design. ErrorMap/ErrorAtlas (arXiv:2601.15812, Jan 2026) builds hierarchical error taxonomies via iterative LLM-based clustering with 95.2% coverage and max 25 categories per level, but applies them only for evaluation. PathFinder-PRM (May 2025) achieves SOTA 67.7 PRMScore with error-aware hierarchical supervision (Mathematical/Consistency/Optimality) but does not use error types for curriculum.\n\n**Verifier co-evolution:** CoVerRL (ACL 2026) demonstrates generator-verifier co-evolution with 4.7–5.9% gains but uses undirected majority voting. VHG (arXiv:2605.06660, May 2026) uses verifier-backed three-party self-play (Setter/Solver/Verifier) to prevent reward hacking in problem generation, improving Pass@1 from 56.8% to 69.0%, but optimizes for difficulty without error diagnosis. RL Tango (NeurIPS 2025) co-trains generator and generative verifier via RL but uses outcome-level rewards. Seirenes (May 2026) implements adversarial self-play with evolving distractions (+7.2 to +10.2pp across scales).\n\n**Other related:** DPE (arXiv:2602.22859, Feb 2026) implements diagnose→generate→retrain for multimodal LLMs using 12 coarse capability dimensions with 4 frontier LLMs but without PRM, step-level analysis, or verifier co-evolution. Self-Error-Instruct (ACL 2025) clusters error keyphrases for targeted data generation but uses GPT-4o and doesn't iterate. R-PRM (NJUNLP 2025) achieves best open-source PRM with fine-grained error categories but does not leverage them for curriculum. APRM (Nov 2025) creates adversarial PRM curriculum (+3.4pp solver accuracy) but targets PRM robustness only. 'GRPO is Secretly a PRM' (Sullivan & Koller, arXiv:2509.21154, Sep 2025; under review at ICML 2026) proves GRPO implicitly performs step-level credit assignment via Monte Carlo estimates from shared token prefixes, clarifying that explicit PRMs add unique value as diagnostic instruments rather than reward signals.\n\n**Positioning summary:** No existing work combines: (a) step-level PRM error-type classification, (b) bandit-based learning-gain-optimized allocation across error categories, (c) hybrid mutation+generation problem synthesis with error-type-validated targeting, (d) iterative co-evolution where the diagnostic instrument itself improves, and (e) predictive analysis of error-type distribution dynamics across iterations.",
  "inspired_by": "Socratic-Zero (2025) validates instance-level weakness targeting via Teacher-Solver-Generator co-evolution but without error taxonomy or pattern aggregation; SwS (NeurIPS 2025) validates weakness-driven synthesis but at concept level; R-Zero (ICLR 2026) validates co-evolutionary self-improvement but with scalar uncertainty; SAGE (2026) validates multi-agent co-evolution but with quality filtering rather than error diagnosis; Prism (2026) validates diversity-aware curriculum but with geographic rather than diagnostic diversity; SEC (2025, Bengio group) validates bandit-based curriculum allocation over problem categories but with difficulty levels rather than error types; LEMMA (ACL 2025) validates error-type-grounded training data construction but in a static single-round SFT setting; Error Classification on MWP (EMNLP 2025) validates dynamic error clustering but only for inference-time prompting; ErrorMap (2026) validates iterative taxonomy construction with 95.2% coverage; Data-Driven Reasoning Rubrics (2026) validates auto-derived error taxonomies with +45% over LLM-as-judge; 'GRPO is Secretly a PRM' (Sullivan & Koller 2025) establishes that GRPO handles implicit credit assignment, clarifying the PRM's unique value as diagnostic instrument. Field guide Gap 7 (iterative self-improvement loops), Gap 4 (dynamic co-evolution).",
  "approach": "We propose Diagnostic Co-Evolution (DiagCoEvo): a framework where a PRM serves as a co-evolving diagnostic instrument whose step-level error-type classifications feed a bandit-based curriculum allocator, while GRPO with standard outcome rewards handles generator training. We initialize generator and PRM from Qwen3-8B.\n\n**PRM Initialization and Cold-Start Strategy.** Rather than directly applying PathFinder-PRM's taxonomy (trained on Mistral traces + PRM800K), which would face distribution shift to Qwen3-8B, we bootstrap the PRM on the target model's own traces: (i) generate 16 solution attempts per problem from Qwen3-8B on a 3K-problem seed bank; (ii) obtain initial step-level labels via consensus of three signals—Monte Carlo correctness estimation, Math-Verify outcome checking, and LLM-as-judge (Qwen3-72B) analysis; (iii) train the PRM on these Qwen3-8B-native traces with PathFinder-PRM's hierarchical error taxonomy as a seed, augmented with data-driven rubric extraction (inspired by Sanders et al. 2026). The initial taxonomy contains five core types: Mathematical-Computation, Logical-Consistency, Conceptual-Gap, Strategy-Selection, Hallucination.\n\n**Taxonomy Expansion Mechanism.** We adopt a concrete expansion protocol inspired by ErrorMap (2026) and TaxoCom (2022): (i) After each DIAGNOSE phase, errors classified with low PRM confidence (softmax < 0.6) are collected into an 'uncertain' pool. (ii) When the uncertain pool exceeds 5% of recent errors, we apply embedding-based novelty detection: compute cosine distance from each uncertain error's representation to all existing category centroids; errors exceeding a Mahalanobis distance threshold (χ² p < 0.01) are flagged as potential novel types. (iii) Flagged errors are clustered (agglomerative clustering with Ward linkage, silhouette-score-optimal k), and clusters with ≥ 20 instances become candidate new categories. (iv) To prevent explosion, we enforce a hard cap of 12 leaf categories and merge categories whose centroid cosine similarity > 0.85 or whose frequency drops below 2% of total errors for two consecutive iterations. (v) Each expansion/merge event is logged for the error dynamics analysis.\n\n**Each co-evolution iteration executes a four-phase cycle:**\n\n(1) DIAGNOSE: The PRM evaluates the generator's solutions on a held-out problem bank (2K problems, 8 solutions each), classifying each incorrect step's error type to produce a weakness distribution w = {w_1, ..., w_K} over error types. We also extract 'error-triggering contexts'—the problem features and reasoning patterns (e.g., nested negation, multi-variable substitution) most frequently associated with each error type via attention-weighted feature extraction from the PRM's intermediate representations.\n\n(2) GENERATE: Hybrid problem synthesis using a three-tier pipeline ordered by reliability. Tier A (Primary—Problem Mutation, ~50% of budget): Take existing problems the model fails on, apply structured mutations targeting the diagnosed error type—constant perturbation, constraint addition/removal, variable relationship alteration (inspired by Arrows of Math). Mutation preserves problem validity better than generation from scratch. Tier B (Secondary—Weakness-Category-Conditioned Generation, ~35% of budget): The generator produces candidate problems conditioned on error-triggering contexts: 'Generate a problem requiring [operation] in a context where [error-triggering pattern] is likely.' This follows SwS's category-conditioned generation but at error-type rather than concept level. Tier C (Tertiary—Fine-Grained Error-Type Generation, ~15% of budget): Direct type-conditioned prompting for the most specific error types, budgeted conservatively given expected 10–25% yield. All tiers pass through error-type-validated rejection sampling: the generator attempts each candidate (8 rollouts per Tier A/B, 12 per Tier C to compensate for lower yield), the PRM diagnoses the solutions, and we retain only candidates where at least one solution triggers the intended error type. ZPD gating (25–75% solvability) filters gradient-vanishing extremes.\n\n(3) TRAIN GENERATOR: GRPO with outcome-level rewards (Math-Verify for answer correctness). Curriculum allocation uses a multi-armed bandit (MAB) over error-type categories, following SEC's formulation: each error type is one arm, reward = |advantage| from GRPO (measuring immediate learning gain), and selection uses Boltzmann policy over Q-values updated via exponential moving average. This automatically upweights the most learnable error types at each stage—deprioritizing types that are nearly solved (diminishing returns) or currently too hard (low returns). A proportional-allocation floor (minimum 5% sampling rate per active category) ensures coverage of rare-but-important error types, preventing the bandit from ignoring them entirely. Standard GRPO handles implicit step-level credit assignment per Sullivan & Koller (2025). We do NOT use explicit PRM rewards for GRPO, cleanly separating the PRM's diagnostic role from the training objective.\n\n(4) UPDATE DIAGNOSTICIAN: The PRM is retrained on the generator's new trajectories, exposing it to novel error patterns at the generator's current capability frontier. This mirrors R-Zero's frozen-partner scheme: during generator training the PRM is frozen; during PRM update the generator is frozen. After PRM update, the taxonomy expansion mechanism runs to detect emergent error types.\n\n**Experimental Design.** We run 5 iterations, tracking three key dynamics: (a) generator accuracy on MATH-500/AMC/AIME, (b) PRM diagnostic quality on ProcessBench/PRMBench, (c) error-type distribution shift per iteration. Our primary analytical contribution is demonstrating that error-type distributions follow predictable phase transitions during co-evolution (e.g., computational errors resolve first, then logical errors, then strategic errors), and that entropy of the error distribution and per-category learning-gain trajectories provide early-warning signals for convergence plateaus and curriculum collapse—enabling principled stopping criteria.\n\nWe compare against five baselines: (i) Socratic-Zero-style instance-level Teacher targeting (closest structural competitor), (ii) R-Zero-style uncertainty-based co-evolution (scalar difficulty, no error types), (iii) SwS-style concept-level weakness synthesis (single round), (iv) R-Zero + Prism diversity preservation (geographic diversity, no error diagnosis), (v) SEC-style MAB over difficulty levels (bandit allocation without error-type diagnosis). Key ablations: (A) error-type MAB vs. proportional allocation vs. uniform allocation (isolates MAB value); (B) hybrid mutation+generation vs. generation-only (isolates mutation value); (C) PRM co-evolution vs. frozen PRM (isolates diagnostician improvement); (D) dynamic taxonomy expansion vs. fixed 5-type taxonomy (isolates expansion value); (E) number of rejection sampling rollouts (8 vs. 12 vs. 16); (F) tiered generation budget ratios.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~3600 (5 iterations × ~400h generator-GRPO + ~120h PRM-SFT + ~100h hybrid problem generation/mutation/validation, plus 5 baselines × ~280h each, plus ablations ~400h)",
      "timeline": "10–14 weeks (sequential iteration dependency: ~2 weeks per co-evolution cycle, plus 2–3 weeks for baselines and writing)",
      "estimated_gpu_cost": "$7,200 (A100-80GB at ~$2/GPU-hr cloud spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "~3000 (Claude-assisted hyperparameter sweep, taxonomy validation, and MAB tuning reduce wasted runs by ~17%)",
      "timeline": "8–10 weeks",
      "claude_api_cost": "$800–$1,200 (experiment orchestration, error-distribution analysis, taxonomy refinement, MAB reward calibration, ablation design)",
      "estimated_gpu_cost": "$6,000"
    },
    "auto_research": {
      "gpu_hours": "~4200 (broader ablations: taxonomy granularity, rejection sampling budget, MAB temperature sweep, tiered generation ratios, iteration count, PRM co-evolution frequency, model scale, cold-start strategies)",
      "timeline": "6–8 weeks (max parallelism within iterations, automated analysis between)",
      "claude_api_cost": "$1,600–$2,200 (full pipeline orchestration, error dynamics analysis, paper drafting assistance)",
      "estimated_gpu_cost": "$8,400",
      "speed_bottleneck": "Sequential iteration dependency—each cycle's curriculum depends on previous cycle's error distribution; within-iteration parallelism saturates at ~8 A100s for GRPO; hybrid generation adds ~25% overhead per iteration vs. pure generation but with higher yield"
    }
  },
  "target_venues": [
    "ICLR 2027 (deadline estimated September–October 2026 — primary target with 16–18 weeks runway, comfortable for 5-iteration experiment + analysis + error dynamics visualization)",
    "ICML 2027 (deadline estimated January 2027 — fallback with time for scale-up ablations and additional baselines)",
    "ACL 2027 ARR (deadline estimated February 2027 — alternative venue if NLP-community framing preferred)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Socratic-Zero: Bootstrapping Reasoning via Data-Free Agent Co-evolution (arXiv:2509.24726, Sep 2025) — primary baseline: Teacher-Solver-Generator co-evolution, instance-level weakness targeting, +15.4pp (Qwen3-8B), no error taxonomy or PRM",
    "SAGE: Multi-Agent Self-Evolution for LLM Reasoning (arXiv:2603.15255, March 2026) — primary baseline: 4-agent co-evolution (Challenger/Planner/Solver/Critic), Critic as quality filter not error diagnoser",
    "WarriorMath: Enhancing Mathematical Ability with a Defect-aware Framework (arXiv:2508.01245, Aug 2025) — defect-aware in name but binary pass/fail operationalization, 5-model expert committee, iterative DPO",
    "SwS: Self-aware Weakness-driven Problem Synthesis in RL for LLM Reasoning (NeurIPS 2025) — primary baseline: concept-level weakness diagnosis, single round",
    "R-Zero: Self-Evolving Reasoning LLM from Zero Data (ICLR 2026) — primary baseline: uncertainty-based challenger-solver co-evolution, pseudo-label degradation 79%→63%",
    "Self-Evolving Curriculum for LLM Reasoning [SEC] (arXiv:2505.14970, Bengio group 2025) — MAB-based curriculum allocation over difficulty categories, +13–33% over random; inspires our error-type MAB",
    "GRPO is Secretly a Process Reward Model (Sullivan & Koller, arXiv:2509.21154, Sep 2025; under review at ICML 2026) — motivates separating PRM's diagnostic role from reward computation",
    "Preventing Curriculum Collapse in Self-Evolving Reasoning Systems [Prism] (arXiv 2026) — diversity preservation via embedding clusters, complementary to error-type targeting",
    "LEMMA: Learning from Errors for MatheMatical Advancement (ACL 2025 Findings, arXiv:2503.17439) — 7 error types for static SFT, closest precursor to error-type-driven training",
    "Error Classification of Large Language Models on Math Word Problems (EMNLP 2025 Findings, arXiv:2501.15581) — 39 dynamic error clusters, Error-Aware Prompting, inference-time only",
    "ErrorMap/ErrorAtlas (arXiv:2601.15812, Jan 2026) — iterative LLM-based taxonomy construction, 95.2% coverage, max 25 categories; inspires our taxonomy expansion mechanism",
    "Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling (arXiv:2602.06795, Feb 2026) — auto-derived error taxonomy with keyword clustering, +45% over LLM-as-judge; inspires dynamic taxonomy",
    "From Blind Spots to Gains: Diagnostic-Driven Iterative Training [DPE] (arXiv:2602.22859, Feb 2026) — closest structural parallel in multimodal domain, 12 coarse capability dimensions",
    "Vocabulary Dropout for Curriculum Diversity in LLM Co-Evolution (arXiv 2026) — random diversity injection, complementary mechanism",
    "CoVerRL: Breaking the Consensus Trap via Generator-Verifier Co-Evolution (ACL 2026) — generator-verifier co-evolution, +4.7–5.9%",
    "Error Typing for Smarter Rewards: Error-Aware Hierarchical Supervision [PathFinder-PRM] (arXiv 2025) — SOTA PRM with error taxonomy (Math/Consistency/Optimality), seed for our taxonomy",
    "Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025) — error keyphrase clustering for targeted data generation",
    "Verifier-Backed Hard Problem Generation [VHG] (arXiv:2605.06660, May 2026) — three-party self-play with verifier validation, difficulty-focused",
    "Cog-DRIFT: Exploration on Adaptively Reformulated Instances (arXiv:2604.04767, April 2026) — format-based adaptive curriculum, ZPD progression",
    "Bidirectional Curriculum Generation (arXiv:2603.05120, March 2026) — simplify/complicate multi-agent framework, pass/fail-driven",
    "Seirenes: Adversarial Self-Play with Evolving Distractions (May 2026) — +7.2 to +10.2pp across scales",
    "RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning (NeurIPS 2025)",
    "Adversarial Training for Process Reward Models [APRM] (arXiv 2025) — adversarial PRM training improves OOD robustness by +5.3pp",
    "R-PRM (NJUNLP 2025) — best open-source PRM with fine-grained error categories",
    "TaxoCom: Taxonomy Completion with Hierarchical Discovery of Novel Topic Clusters (WWW 2022) — novelty-adaptive clustering for known vs. novel categories; inspires taxonomy expansion",
    "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)",
    "Arrows of Math Reasoning Data Synthesis (arXiv:2508.18824, Aug 2025) — structured problem mutation strategies; inspires our Tier A generation",
    "DART-Math: Difficulty-Aware Rejection Tuning (NeurIPS 2024) — rejection sampling budgets and yield analysis"
  ],
  "description": "We propose Diagnostic Co-Evolution (DiagCoEvo), a framework that repositions the process reward model from a training reward signal to a co-evolving diagnostic instrument for bandit-based curriculum guidance. In a field with 25+ co-evolutionary self-improvement papers in the past year, DiagCoEvo's contribution is both methodological and analytical: methodologically, it uniquely combines step-level PRM error-type classification with MAB-based learning-gain-optimized allocation across error categories and hybrid mutation+generation problem synthesis; analytically, it provides the first characterization of error-type distribution dynamics across multiple co-evolution iterations, yielding predictive signals for convergence and curriculum collapse.\n\nMotivated by Sullivan & Koller (2025, arXiv preprint under review at ICML 2026) showing GRPO already performs implicit step-level credit assignment, we cleanly separate concerns: GRPO with outcome rewards handles generator training, while the PRM's unique value lies in classifying step-level reasoning failures into an evolving error taxonomy that drives curriculum design. The PRM is bootstrapped on the target model's (Qwen3-8B) own traces to avoid cross-model distribution shift, with consensus labeling (MC estimation + Math-Verify + LLM-as-judge) for initialization.\n\nEach iteration executes four phases: (1) DIAGNOSE—PRM evaluates generator solutions, producing an error-type weakness distribution and extracting error-triggering contexts; (2) GENERATE—hybrid three-tier pipeline: problem mutation (50% budget, highest reliability), weakness-category-conditioned generation (35%), and fine-grained type-conditioned generation (15%), all validated via PRM-based error-type rejection sampling with ZPD gating; (3) TRAIN—GRPO with outcome rewards, where curriculum allocation uses a multi-armed bandit over error-type categories (reward = |GRPO advantage|, Boltzmann selection) with a proportional-allocation floor ensuring rare-type coverage; (4) UPDATE—PRM retrained on new trajectories, followed by taxonomy expansion via embedding-based novelty detection with hard cap of 12 leaf categories and automatic merge/split rules.\n\nThis addresses key limitations across the landscape: Socratic-Zero (Sep 2025, +15.4pp) targets weaknesses at instance level without aggregating error patterns or building systematic weakness profiles; SAGE (March 2026) uses a Critic as quality filter rather than error diagnoser; WarriorMath (Aug 2025) operationalizes 'defects' as binary pass/fail; SwS (NeurIPS 2025) diagnoses at concept level; R-Zero (ICLR 2026) targets scalar difficulty; LEMMA (ACL 2025) defines error types but in a static SFT setting without curriculum or co-evolution; SEC (2025) demonstrates MAB curriculum but over difficulty levels, not error types.\n\nOur primary empirical contribution targets +8pp average across MATH-500/AMC/AIME over the strongest baseline, but the primary analytical contribution—showing that error-type distributions follow predictable phase transitions during co-evolution and that per-category learning-gain trajectories provide early-warning signals for convergence—addresses the field's acknowledged gap in theoretical understanding of when and why self-improvement works. We evaluate on Qwen3-8B across 5 iterations against Socratic-Zero, R-Zero, SwS, Prism-augmented, and SEC baselines, with detailed ablations isolating the value of error-type MAB allocation, hybrid generation, PRM co-evolution, and taxonomy expansion.",
  "project_name": "prm_diag_adaptive_curriculum",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_SocraticZero": "ADDRESSED (moderate). Socratic-Zero (arXiv:2509.24726) is now a primary competitor throughout landscape, approach, and baselines. After thorough analysis of the full paper, we position against it precisely: Socratic-Zero's Teacher performs instance-level targeting—generating new problems from individual failed solutions via a refinement function G(q, y_fail)—but never aggregates error patterns into a taxonomy. It cannot detect that 40% of algebra failures stem from sign errors vs. 60% from conceptual gaps because it processes each failure independently. Its verification is binary outcome-level (no PRM, no step-level diagnosis), its difficulty calibration is a scalar Gaussian utility (same as R-Zero's p̂≈0.5), and its Teacher is a frozen 235B oracle rather than a co-evolving diagnostician. DiagCoEvo's error-type-level diagnosis captures systematic patterns that instance-level targeting misses, and its bandit-based allocation optimizes learning gain across error categories rather than treating all failures as equally informative. Socratic-Zero is included as the first baseline (closest structural competitor) in our experimental comparison.",
    "issue_2_SAGE_WarriorMath": "ADDRESSED (moderate). SAGE (arXiv:2603.15255) and WarriorMath (arXiv:2508.01245) are now in the landscape with detailed analysis. SAGE's Critic evaluates question quality (clarity, relevance, well-formedness) on a 1–10 scale but explicitly does NOT determine correctness or diagnose error types—it is a quality filter, not a diagnostic instrument. The Critic cannot distinguish between a Solver failing due to calculation errors vs. conceptual misunderstanding. WarriorMath claims 'defect-aware' but operationalizes defects as binary pass/fail across N=16 rollouts—no formal error categorization exists despite the title. Both papers' key limitation is that weakness detection is implicit through aggregate difficulty/pass-rate signals, whereas DiagCoEvo provides explicit error-type classification enabling targeted remediation.",
    "issue_3_minor_competitors": "ADDRESSED (minor). All five papers now in landscape: LEMMA (ACL 2025 Findings, 7 error types for static SFT), Error Classification of LLMs on MWP (EMNLP 2025 Findings, 39 dynamic clusters for inference-time prompting), Bidirectional Curriculum (March 2026, simplify/complicate on pass/fail), VHG (May 2026, verifier-backed difficulty-focused 3-party self-play), Cog-DRIFT (April 2026, format-based adaptive reformulation). For each, the clear differentiator is provided. LEMMA is the closest precursor (error types + training) but is static/single-round/SFT-only. The Error Classification paper's 39-cluster approach validates dynamic taxonomy discovery but applies it only at inference time. These gaps collectively motivate DiagCoEvo's unique combination of error-type diagnosis + iterative co-evolution + curriculum design.",
    "issue_4_type_conditioned_prompting": "ADDRESSED (highest-risk component, major specification). Based on thorough research, we acknowledge that no paper reports direct success rates for error-type-conditioned generation, and converging evidence suggests 10–25% yield for fine-grained conditioning. We replace the single-strategy generation with a hybrid three-tier pipeline ordered by reliability: Tier A—Problem Mutation (~50% budget): structured mutations of existing failed problems (constant perturbation, constraint addition/removal, variable alteration), inspired by Arrows of Math (2025), which achieves high validity preservation. Tier B—Category-Conditioned Generation (~35%): generation conditioned on error-triggering contexts at moderate specificity, following SwS's approach at error-type rather than concept level. Tier C—Fine-Grained Type-Conditioned Generation (~15%): direct type-conditioned prompting, budgeted conservatively with 12 rollouts per candidate (vs. 8 for Tiers A/B) to compensate for lower yield. All tiers share the PRM-based error-type-validated rejection sampling. This hybrid approach mitigates the fundamental tension identified in the literature (generator quality degrades when targeting its own weaknesses) by anchoring most generation in mutation of existing valid problems. If Tier C yields prove too low (<10%), budget automatically shifts to Tiers A/B.",
    "issue_5_taxonomy_expansion": "ADDRESSED (claimed contribution, now fully specified). We specify a concrete expansion protocol: (i) Low-confidence PRM classifications (softmax < 0.6) accumulate in an 'uncertain' pool. (ii) When the pool exceeds 5% of recent errors, embedding-based novelty detection flags errors exceeding Mahalanobis distance threshold (χ² p < 0.01) from all existing centroids. (iii) Flagged errors undergo agglomerative clustering (Ward linkage, silhouette-score-optimal k); clusters with ≥20 instances become candidate new categories. (iv) Hard cap of 12 leaf categories; categories with centroid cosine similarity > 0.85 merge; categories below 2% frequency for two consecutive iterations merge into nearest neighbor. Inspired by ErrorMap (2026, iterative LLM-based clustering with 95.2% coverage), TaxoCom (2022, novelty-adaptive clustering for known vs. novel categories), and Sanders et al. (2026, keyword clustering with ~50% consolidation). All expansion/merge events are logged for the error dynamics analysis.",
    "issue_6_PRM_generalization": "ADDRESSED. The proposal now includes an explicit cold-start strategy. Rather than applying PathFinder-PRM's taxonomy trained on Mistral traces directly, we bootstrap the PRM on Qwen3-8B's own traces via consensus labeling (MC estimation + Math-Verify + LLM-as-judge). This directly addresses the documented distribution shift problem—PRMs trained on one model's traces face Step OOD when applied to another model family (Qwen PRM paper, 2025; PRM survey, 2025). PathFinder-PRM's taxonomy serves only as a structural seed (category definitions), not as a pretrained model. The co-evolution loop further mitigates cold-start risk: PRM quality improves each iteration as it sees more of the target model's actual failure patterns.",
    "issue_7_GRPO_PRM_citation": "ADDRESSED (minor). Citation corrected to: Sullivan & Koller, arXiv:2509.21154, Sep 2025; under review at ICML 2026. The OpenReview submission iRWqcnBlLQ was confirmed to be a DIFFERENT paper ('GRPO-lambda' by Parthasarathi et al.) that was withdrawn. The Sullivan & Koller paper had an ICLR 2026 submission (OpenReview o0k034W6vx) that was apparently unsuccessful; v3 (Feb 2026) indicates resubmission to ICML 2026. We cite it as an arXiv preprint with status noted.",
    "issue_8_crowded_field": "ADDRESSED (strategic repositioning). With 25–30 directly relevant papers and 110 accepted at the ICLR 2026 RSI Workshop, we explicitly acknowledge the crowded field and position DiagCoEvo's contribution as dual: (1) Methodological—the unique combination of error-type PRM diagnosis + MAB-based allocation + hybrid generation + co-evolution. No existing paper combines all four. (2) Analytical—the first characterization of error-type distribution dynamics across multiple co-evolution iterations, providing predictive signals for convergence and curriculum collapse. The crowded-field analysis (Seirenes, VHG, R-Diverse, SPOC, etc.) confirms that the field is empirically crowded but analytically sparse. The RSI Workshop organizers explicitly noted the gap in 'principled methods that make self-improvement measurable, reliable, and deployable.' Our error dynamics analysis directly addresses this—showing whether error distributions follow predictable phase transitions, whether per-category learning gain predicts convergence, and whether entropy measures detect curriculum collapse. This analytical angle is underexplored and provides a contribution independent of the exact empirical gap size. We integrate SEC's MAB insight as a key component (comparing error-type MAB vs. difficulty-level MAB as a baseline) to demonstrate that the bandit allocation works better over error-type categories than over difficulty levels."
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c2707e-9ec4-4735-bdf2-eeebe9770c2d",
  "isSidechain": false,
  "requestId": "req_011CbURh3GRtK5EqC7m9H3G4",
  "type": "assistant",
  "uuid": "6d2626d0-153b-460b-8e22-667534ec5774",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVwgW9zNEyFY3fmQGj9yCx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2966,
      "cache_read_input_tokens": 50316,
      "output_tokens": 9555,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 9555,
          "cache_read_input_tokens": 50316,
          "cache_creation_input_tokens": 2966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2966
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

_source line 84_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "6d2626d0-153b-460b-8e22-667534ec5774",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 86_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Error-Taxonomy-Guided Curriculum for Self-Improving Reasoning via Diag…",
  "leafUuid": "6d2626d0-153b-460b-8e22-667534ec5774",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise research idea based on round 2 reviewer feedback",
  "sessionId": "35b5d14c-5b69-46e3-9166-8ee9b68949f7"
}
```

---
