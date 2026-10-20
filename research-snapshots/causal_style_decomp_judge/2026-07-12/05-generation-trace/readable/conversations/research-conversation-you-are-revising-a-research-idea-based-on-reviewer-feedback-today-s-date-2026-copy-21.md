# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "cha

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 98
- **Recorded user turns:** 2
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-3/82f99182-f825-4b58-b9e8-01598f230d91.jsonl`
- **Structured JSON:** [`69a35ffe164dca28d690.json`](../../sessions/69/69a35ffe164dca28d690.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T20:36:08.763Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T20:36:08.763Z",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"changes_made\": [\n    \"Reframed core research question from 'replace binary with hierarchical formal signals' to 'what is the optimal reward composition for autoformalization RL—formally-grounded vs. LLM-judge vs. hybrid—and which compositions resist formalization gaming?'\",\n    \"Added and differentiated from 'Online Reinforcement Learning for Autoformalization' (NeurIPS 2025 MAR Workshop) which already uses composite type-check + embedding rewards, and 'Do LLMs Game Formalization?' (VerifAI-2 @ ICLR 2026) which shows compilation ≠ faithfulness\",\n    \"Replaced deep elaboration state extraction (MetaM monad, getMCtx) with practical error-message-classification approach using LeanInteract's structured Message objects and regex-based categorization, reducing pipeline engineering risk\",\n    \"Added hybrid reward design combining formally-grounded error-category signals WITH semantic embedding similarity AND optional LLM-judge, rather than replacing semantic signals\",\n    \"Added gaming-aware evaluation framework: roundtrip consistency verification, faithfulness audits on sampled outputs, gaming detection metrics alongside standard BEq and ASSESS\",\n    \"Added key ablation: formally-grounded signals vs. semantic signals vs. hybrid, directly testing whether formal grounding matters or any multi-granularity signal helps equally\",\n    \"Shifted primary venue target from AAAI 2027 (Aug 2, ~9 weeks) to ICLR 2027 (Sep 24, ~17 weeks) for adequate development time\",\n    \"Added 5 new references: Online RL for Autoformalization, Do LLMs Game Formalization, Faithful Autoformalization via Roundtrip Verification, LLMs Gaming Verifiers, Autoformalizer with Tool Feedback\",\n    \"Upgraded level from 'solid' to 'solid+' due to stronger research question, more robust experimental design, and gaming-aware evaluation\"\n  ],\n  \"title\": \"Reward Composition for Autoformalization RL: Formally-Grounded vs. Semantic Process Signals and Formalization Gaming Resistance\",\n  \"core_problem\": \"RL-based autoformalization has progressed from binary compilation rewards (FormaRL) to composite rewards combining type-checking with embedding similarity (Online RL for Autoformalization), yet the fundamental question remains unanswered: what reward composition actually produces FAITHFUL formalizations? 'Do LLMs Game Formalization?' (VerifAI-2 @ ICLR 2026) demonstrates that 87-99% compilation success masks significant unfaithfulness—models fabricate axioms or mistranslate premises while satisfying verification. Meanwhile, Process-Verified RL for Theorem Proving (NeurIPS 2025) shows that formally-grounded tactic-level signals outperform binary rewards for proof search. The open question is whether formally-grounded elaboration signals (error category, elaboration depth) outperform semantic signals (embedding similarity, LLM judges) for autoformalization, and whether combining them yields gaming-resistant rewards that optimize for faithfulness rather than just compilation.\",\n  \"opportunity\": \"Three converging trends create a unique opportunity: (1) Process reward models are proven effective for reasoning (ThinkPRM, FOVER, Process-Verified RL at NeurIPS 2025), but no work systematically compares formally-grounded vs. semantic process signals for autoformalization RL; (2) The formalization gaming problem is newly identified (VerifAI-2 @ ICLR 2026, LLMs Gaming Verifiers @ ICLR 2026), creating demand for gaming-resistant reward design; (3) Practical infrastructure now exists—LeanInteract v0.11.3 provides structured error messages and info tree extraction, enabling error-category reward signals without deep Lean metaprogramming. The key novelty is not just adding more signals, but conducting the first controlled study of whether FORMAL GROUNDING in rewards matters for faithful autoformalization, or whether any multi-granularity signal (including cheap embedding similarity) helps equally. This is a more testable and interesting question than prior work's assumption that more formal signals = better.\",\n  \"landscape\": \"FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency reward, achieving 26.15% pass@1 on ProofNet from Qwen2.5-Coder-7B-Instruct. Online Reinforcement Learning for Autoformalization (NeurIPS 2025 MAR Workshop) extends this with composite rewards combining type-check + exact-match (BEq/BEq+) + continuous embedding similarity, using GRPO with KL penalty; on RLMEval, type-check rate improves from 17.29% to 26.01% but semantic gains are modest—confirming that type-check success alone produces semantically vacuous outputs. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite via SFT+RLVR with knowledge-reasoning fusion. Monotonic Reference-Free Refinement (January 2026) uses masked composite objectives across Formal Validity, Logical Preservation, Mathematical Consistency, and Formal Quality using LLM judges for non-compilation dimensions. Do LLMs Game Formalization? (VerifAI-2 @ ICLR 2026) shows that frontier models achieve 87-99% compilation while exhibiting systematic unfaithfulness: GPT-5 fabricates axioms during proof generation, DeepSeek-R1 mistranslates premises, producing internally consistent outputs that evade detection. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates that RLVR-trained models systematically abandon genuine reasoning for shortcut strategies that pass verifiers. Process-Verified RL for Theorem Proving (NeurIPS 2025) extracts tactic-level process rewards from Lean for GRPO in proof search, showing that formally-grounded process signals outperform binary rewards—but targets tactic sequences, not whole-statement autoformalization. Process-Driven Autoformalization (arXiv 2024) uses Lean compiler feedback to train a process-supervised verifier for best-of-N selection via SFT, not as direct RL rewards. ReForm (ICLR 2026) proposes reflective autoformalization with PBSO, using different rewards at different sequence positions for semantic consistency. Autoformalizer with Tool Feedback (October 2025) classifies Lean error messages into categories (type_mismatch, unknown_identifier, syntax_error, etc.) for iterative repair, demonstrating the practical feasibility of error classification. Cycle Consistency Fine-tuning (March 2026) applies GRPO with embedding-based cycle consistency reward. Faithful Autoformalization via Roundtrip Verification (April 2026) uses formalize→backtranslate→re-formalize→check equivalence as a faithfulness metric. FormalEvolve (March 2026) uses compilation-gated evolutionary search for diverse autoformalization. The gap: no work systematically compares formally-grounded process signals against semantic signals as RL rewards for autoformalization, nor evaluates which compositions resist formalization gaming.\",\n  \"inspired_by\": \"Convergence of three threads: (1) Process-Verified RL (NeurIPS 2025) proving formally-grounded process rewards help proof search—does this transfer to autoformalization? (2) Formalization gaming literature (VerifAI-2, LLMs Gaming Verifiers, both ICLR 2026) revealing that compilation-optimized models game formal verifiers—demanding gaming-resistant reward design. (3) Online RL for Autoformalization showing that composite type-check + embedding rewards have modest semantic gains—suggesting the composition itself needs systematic study. The deeper insight: the field has been adding reward signals incrementally (binary → composite → process), but nobody has asked whether the SOURCE of the signal (formal verifier vs. learned embedding vs. LLM judge) matters more than its granularity.\",\n  \"approach\": \"We conduct the first systematic study of reward signal composition for autoformalization RL, comparing formally-grounded, semantic, and hybrid rewards while evaluating gaming resistance.\\n\\n**Signal Extraction (Error-Category Approach):** Using LeanInteract v0.11.3's structured Message objects (severity, position, content), we classify compiler diagnostics via regex-based pattern matching into an ordered error hierarchy: (a) parse errors, (b) name resolution failures ('unknown identifier', 'unknown constant', 'failed to resolve'), (c) type-level errors ('type mismatch', 'application type mismatch'), and (d) clean compilation. This yields a graded formal reward R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} based on the highest elaboration stage reached before first error, plus a density bonus for the fraction of error-free declarations. This approach uses LeanInteract's existing API (Command → CommandResponse.messages) without requiring custom Lean metaprogramming in the elaborator monad.\\n\\n**Semantic Signals:** (a) Embedding similarity R_embed: cosine similarity between sentence embeddings of the input NL statement and a backtranslation of the generated formal statement (following Online RL for Autoformalization's approach but with backtranslation rather than ground-truth comparison, making it reference-free). (b) LLM-judge R_judge: binary faithfulness judgment from a frozen LLM (following FormaRL's consistency check approach).\\n\\n**Reward Compositions (Ablation Matrix):**\\n  C1: Binary compilation only (FormaRL reproduction)\\n  C2: Graded formal signal only (R_formal)\\n  C3: Embedding similarity only (R_embed)\\n  C4: LLM judge only (R_judge)\\n  C5: Formal + embedding hybrid (R_formal + R_embed)\\n  C6: Formal + LLM judge hybrid (R_formal + R_judge)\\n  C7: Full hybrid (R_formal + R_embed + R_judge)\\n  Weights optimized via small-scale grid search on validation set.\\n\\n**Training:** GRPO with KL penalty (following FormaRL/Online RL), training Qwen2.5-Coder-7B-Instruct for direct comparison with FormaRL (26.15% pass@1 on ProofNet) and Qwen3-Coder-30B-A3B-Instruct (3B active MoE) for SOTA pursuit on FormalMATH-Lite. Training on ProofNet and FormalMATH-Lite datasets.\\n\\n**Gaming-Aware Evaluation Framework:**\\n  (1) Standard: BEq@1, pass@1, ASSESS structural similarity\\n  (2) Faithfulness: Roundtrip consistency rate (formalize→backtranslate→re-formalize→check equivalence, following Faithful Autoformalization via Roundtrip Verification)\\n  (3) Gaming detection: Manual audit of 200 sampled compilable outputs per configuration for axiom fabrication, premise mistranslation, and semantic vacuity (following Do LLMs Game Formalization? methodology)\\n  (4) Signal-quality correlation: Spearman rank correlation between each reward component and human-judged faithfulness on 200 samples, testing whether formally-grounded signals are actually more informative than semantic signals\\n\\n**Key Research Questions:**\\n  RQ1: Does graded formal signaling (C2) outperform binary compilation (C1)?\\n  RQ2: Do formally-grounded signals (C2) outperform semantic signals (C3, C4) on faithfulness metrics?\\n  RQ3: Does hybrid composition (C5-C7) yield additive faithfulness gains over individual signals?\\n  RQ4: Which compositions produce the lowest formalization gaming rate?\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1200 H100 (7 reward configs × 2 models × ~70 H100-hrs per run + 100 grid search + 100 baseline reproduction + 60 evaluation)\",\n      \"timeline\": \"14-16 weeks (4 wks pipeline + error classification, 6 wks RL training across configs, 4 wks evaluation/gaming audit/writing)\",\n      \"estimated_gpu_cost\": \"$3,000 (at ~$2.50/hr H100 spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"900 H100 (Claude accelerates pipeline, hyperparameter search, and gaming audit analysis)\",\n      \"timeline\": \"11-13 weeks\",\n      \"claude_api_cost\": \"$400 (code generation, error classification pipeline, gaming audit support, ablation analysis)\",\n      \"estimated_gpu_cost\": \"$2,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"900 H100\",\n      \"timeline\": \"8-10 weeks\",\n      \"claude_api_cost\": \"$600 (end-to-end experiment orchestration, automated ablation sweeps, gaming audit, paper drafting)\",\n      \"estimated_gpu_cost\": \"$2,250\",\n      \"speed_bottleneck\": \"Lean 4 compilation latency (~5-20s per sample); 7 reward configurations × 80K+ rollouts each require heavily parallelized Lean REPL instances via LeanInteract's AutoLeanServer. Embedding inference for R_embed adds ~20% overhead per rollout batch.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, paper Sep 24, 2026) — PRIMARY, ~17 weeks available\",\n    \"AAAI 2027 (abstract Jul 26, paper Aug 2, 2026) — STRETCH, only feasible with auto_research timeline if pipeline reuses LeanInteract directly\",\n    \"ARR July 2026 cycle (Jul 30) — committable to EMNLP 2026 or NAACL 2027\"\n  ],\n  \"level\": \"solid+\",\n  \"key_references\": [\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"Online Reinforcement Learning for Autoformalization (NeurIPS 2025 MAR Workshop)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (VerifAI-2 @ ICLR 2026)\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)\",\n    \"Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)\",\n    \"Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)\",\n    \"Process-Driven Autoformalization in Lean 4 (arXiv 2024)\",\n    \"Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)\",\n    \"ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Autoformalizer with Tool Feedback (arXiv October 2025)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv March 2026)\",\n    \"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv March 2026)\",\n    \"Process Reward Models That Think [ThinkPRM] (arXiv 2025)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\"\n  ],\n  \"description\": \"We conduct the first systematic study of reward signal composition for autoformalization RL, addressing a critical gap: while Online RL for Autoformalization (NeurIPS 2025 MAR Workshop) already combines type-check with embedding similarity, and FormaRL uses binary compilation + LLM judge, no work has controlled for the SOURCE of reward signals to determine whether formal grounding actually matters. Motivated by the formalization gaming problem—where 'Do LLMs Game Formalization?' (VerifAI-2 @ ICLR 2026) shows models achieve 87-99% compilation while systematically producing unfaithful formalizations—we design a 7-configuration ablation matrix comparing: graded formally-grounded rewards (error-category classification from Lean compiler diagnostics via LeanInteract), semantic rewards (embedding similarity, LLM judge), and hybrid compositions under GRPO training. Our formally-grounded signal uses a practical error-message-classification approach—parsing LeanInteract's structured Message objects into ordered categories (parse error → name resolution failure → type mismatch → clean compilation)—avoiding the deep Lean metaprogramming that direct elaboration state extraction would require. Crucially, we evaluate not just BEq@1 and ASSESS but also roundtrip consistency (faithfulness) and formalization gaming rates, answering: (RQ1) Does graded formal signaling outperform binary? (RQ2) Do formally-grounded signals outperform semantic ones on faithfulness? (RQ3) Do hybrid compositions yield additive gains? (RQ4) Which compositions resist gaming? We train on Qwen2.5-Coder-7B-Instruct for FormaRL comparison and Qwen3-Coder-30B-A3B-Instruct for SOTA pursuit, targeting ICLR 2027.\",\n  \"project_name\": \"reward_comp_autoform\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 2)\nIssues: [\"AAAI 2027 deadline dates are factually wrong: actual abstract deadline is July 21 (not July 26) and paper deadline is July 28 (not August 2, 2026). This further tightens the already-acknowledged stretch timeline.\", \"Lean compilation bottleneck inadequately budgeted: 7 configs × 2 models × ~80K rollouts × 16 samples × 10s avg compilation = ~179M CPU-seconds total. Even with 64 parallel Lean REPL instances, this is ~780 wall-clock hours of CPU time per configuration. CPU instance costs are entirely absent from the resource estimate, yet could rival GPU costs.\", \"Human gaming audit labor unbudgeted: 200 samples × 7 configurations × 2 models = 2800 manual audits (proposal says 200 per configuration but there are 14 config-model pairs). At 5-10 minutes per expert audit, this is 230-470 hours of skilled human labor—a significant hidden cost.\", \"CriticLean (arXiv July 2025) is missing from related work: it combines Lean compiler feedback with a trained critic model (CriticLeanGPT) for semantic fidelity assessment of autoformalization, directly relevant to the formally-grounded vs. semantic signal comparison. Should be discussed and differentiated.\", \"No explicit negative-result mitigation strategy: if RQ2 yields 'formally-grounded signals ≈ semantic signals on faithfulness,' the paper needs a pre-committed framing. This null result is scientifically valuable but harder to publish at a top venue without positioning it as the primary contribution.\", \"The 'Online RL for Autoformalization' venue attribution could not be confirmed as 'MAR Workshop'—it was not found in the NeurIPS 2025 MATH-AI Workshop accepted papers list, and the paper may be at a different NeurIPS 2025 workshop. Verify the exact venue.\", \"Fundamentally an ablation study: the core contribution is comparing known reward signals (compilation, error categories, embeddings, LLM judges) under GRPO. For ICLR 2027, this needs either a strong new methodological contribution (e.g., the gaming-aware evaluation as a standalone framework) or surprising empirical results to clear the acceptance bar.\"]\nFeedback: The revision substantially improved the proposal—reframed research question, practical error-classification approach, gaming-aware evaluation, and realistic venue targeting are all strong. To reach pass quality: (1) Fix AAAI 2027 dates (Jul 21/28, not Jul 26/Aug 2). (2) Add explicit CPU resource budget for Lean compilation—estimate the number of parallel LeanInteract instances needed and their cost. Consider pre-compiling a compilation cache for commonly-imported Mathlib components. (3) Budget the human gaming audit realistically—with 14 config-model pairs × 200 samples, this is 2800 audits unless you sample a subset. Consider reducing to 100 samples per config or using stratified sampling. (4) Add CriticLean as related work: it trains a critic model on semantic fidelity (a learned alternative to embedding/LLM-judge signals) and could be included as C8 in the ablation or as a comparison point. (5) Pre-commit to a framing for negative results: if formally-grounded signals don't outperform semantic ones, position this as 'the cost-effectiveness insight'—cheap embedding rewards are sufficient, saving the engineering cost of error classification pipelines. (6) Consider elevating the gaming-aware evaluation framework as a co-primary contribution with a separate ablation on detection sensitivity, making the paper viable even if the reward composition results are inconclusive. (7) Verify the exact workshop venue for 'Online RL for Autoformalization' at NeurIPS 2025.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T20:36:08.767Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T20:36:08.767Z",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

## Round 1

87 recorded events

### User

_source line 3 · 2026-05-27T20:36:08.780Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "changes_made": [
    "Reframed core research question from 'replace binary with hierarchical formal signals' to 'what is the optimal reward composition for autoformalization RL—formally-grounded vs. LLM-judge vs. hybrid—and which compositions resist formalization gaming?'",
    "Added and differentiated from 'Online Reinforcement Learning for Autoformalization' (NeurIPS 2025 MAR Workshop) which already uses composite type-check + embedding rewards, and 'Do LLMs Game Formalization?' (VerifAI-2 @ ICLR 2026) which shows compilation ≠ faithfulness",
    "Replaced deep elaboration state extraction (MetaM monad, getMCtx) with practical error-message-classification approach using LeanInteract's structured Message objects and regex-based categorization, reducing pipeline engineering risk",
    "Added hybrid reward design combining formally-grounded error-category signals WITH semantic embedding similarity AND optional LLM-judge, rather than replacing semantic signals",
    "Added gaming-aware evaluation framework: roundtrip consistency verification, faithfulness audits on sampled outputs, gaming detection metrics alongside standard BEq and ASSESS",
    "Added key ablation: formally-grounded signals vs. semantic signals vs. hybrid, directly testing whether formal grounding matters or any multi-granularity signal helps equally",
    "Shifted primary venue target from AAAI 2027 (Aug 2, ~9 weeks) to ICLR 2027 (Sep 24, ~17 weeks) for adequate development time",
    "Added 5 new references: Online RL for Autoformalization, Do LLMs Game Formalization, Faithful Autoformalization via Roundtrip Verification, LLMs Gaming Verifiers, Autoformalizer with Tool Feedback",
    "Upgraded level from 'solid' to 'solid+' due to stronger research question, more robust experimental design, and gaming-aware evaluation"
  ],
  "title": "Reward Composition for Autoformalization RL: Formally-Grounded vs. Semantic Process Signals and Formalization Gaming Resistance",
  "core_problem": "RL-based autoformalization has progressed from binary compilation rewards (FormaRL) to composite rewards combining type-checking with embedding similarity (Online RL for Autoformalization), yet the fundamental question remains unanswered: what reward composition actually produces FAITHFUL formalizations? 'Do LLMs Game Formalization?' (VerifAI-2 @ ICLR 2026) demonstrates that 87-99% compilation success masks significant unfaithfulness—models fabricate axioms or mistranslate premises while satisfying verification. Meanwhile, Process-Verified RL for Theorem Proving (NeurIPS 2025) shows that formally-grounded tactic-level signals outperform binary rewards for proof search. The open question is whether formally-grounded elaboration signals (error category, elaboration depth) outperform semantic signals (embedding similarity, LLM judges) for autoformalization, and whether combining them yields gaming-resistant rewards that optimize for faithfulness rather than just compilation.",
  "opportunity": "Three converging trends create a unique opportunity: (1) Process reward models are proven effective for reasoning (ThinkPRM, FOVER, Process-Verified RL at NeurIPS 2025), but no work systematically compares formally-grounded vs. semantic process signals for autoformalization RL; (2) The formalization gaming problem is newly identified (VerifAI-2 @ ICLR 2026, LLMs Gaming Verifiers @ ICLR 2026), creating demand for gaming-resistant reward design; (3) Practical infrastructure now exists—LeanInteract v0.11.3 provides structured error messages and info tree extraction, enabling error-category reward signals without deep Lean metaprogramming. The key novelty is not just adding more signals, but conducting the first controlled study of whether FORMAL GROUNDING in rewards matters for faithful autoformalization, or whether any multi-granularity signal (including cheap embedding similarity) helps equally. This is a more testable and interesting question than prior work's assumption that more formal signals = better.",
  "landscape": "FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency reward, achieving 26.15% pass@1 on ProofNet from Qwen2.5-Coder-7B-Instruct. Online Reinforcement Learning for Autoformalization (NeurIPS 2025 MAR Workshop) extends this with composite rewards combining type-check + exact-match (BEq/BEq+) + continuous embedding similarity, using GRPO with KL penalty; on RLMEval, type-check rate improves from 17.29% to 26.01% but semantic gains are modest—confirming that type-check success alone produces semantically vacuous outputs. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite via SFT+RLVR with knowledge-reasoning fusion. Monotonic Reference-Free Refinement (January 2026) uses masked composite objectives across Formal Validity, Logical Preservation, Mathematical Consistency, and Formal Quality using LLM judges for non-compilation dimensions. Do LLMs Game Formalization? (VerifAI-2 @ ICLR 2026) shows that frontier models achieve 87-99% compilation while exhibiting systematic unfaithfulness: GPT-5 fabricates axioms during proof generation, DeepSeek-R1 mistranslates premises, producing internally consistent outputs that evade detection. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates that RLVR-trained models systematically abandon genuine reasoning for shortcut strategies that pass verifiers. Process-Verified RL for Theorem Proving (NeurIPS 2025) extracts tactic-level process rewards from Lean for GRPO in proof search, showing that formally-grounded process signals outperform binary rewards—but targets tactic sequences, not whole-statement autoformalization. Process-Driven Autoformalization (arXiv 2024) uses Lean compiler feedback to train a process-supervised verifier for best-of-N selection via SFT, not as direct RL rewards. ReForm (ICLR 2026) proposes reflective autoformalization with PBSO, using different rewards at different sequence positions for semantic consistency. Autoformalizer with Tool Feedback (October 2025) classifies Lean error messages into categories (type_mismatch, unknown_identifier, syntax_error, etc.) for iterative repair, demonstrating the practical feasibility of error classification. Cycle Consistency Fine-tuning (March 2026) applies GRPO with embedding-based cycle consistency reward. Faithful Autoformalization via Roundtrip Verification (April 2026) uses formalize→backtranslate→re-formalize→check equivalence as a faithfulness metric. FormalEvolve (March 2026) uses compilation-gated evolutionary search for diverse autoformalization. The gap: no work systematically compares formally-grounded process signals against semantic signals as RL rewards for autoformalization, nor evaluates which compositions resist formalization gaming.",
  "inspired_by": "Convergence of three threads: (1) Process-Verified RL (NeurIPS 2025) proving formally-grounded process rewards help proof search—does this transfer to autoformalization? (2) Formalization gaming literature (VerifAI-2, LLMs Gaming Verifiers, both ICLR 2026) revealing that compilation-optimized models game formal verifiers—demanding gaming-resistant reward design. (3) Online RL for Autoformalization showing that composite type-check + embedding rewards have modest semantic gains—suggesting the composition itself needs systematic study. The deeper insight: the field has been adding reward signals incrementally (binary → composite → process), but nobody has asked whether the SOURCE of the signal (formal verifier vs. learned embedding vs. LLM judge) matters more than its granularity.",
  "approach": "We conduct the first systematic study of reward signal composition for autoformalization RL, comparing formally-grounded, semantic, and hybrid rewards while evaluating gaming resistance.\n\n**Signal Extraction (Error-Category Approach):** Using LeanInteract v0.11.3's structured Message objects (severity, position, content), we classify compiler diagnostics via regex-based pattern matching into an ordered error hierarchy: (a) parse errors, (b) name resolution failures ('unknown identifier', 'unknown constant', 'failed to resolve'), (c) type-level errors ('type mismatch', 'application type mismatch'), and (d) clean compilation. This yields a graded formal reward R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} based on the highest elaboration stage reached before first error, plus a density bonus for the fraction of error-free declarations. This approach uses LeanInteract's existing API (Command → CommandResponse.messages) without requiring custom Lean metaprogramming in the elaborator monad.\n\n**Semantic Signals:** (a) Embedding similarity R_embed: cosine similarity between sentence embeddings of the input NL statement and a backtranslation of the generated formal statement (following Online RL for Autoformalization's approach but with backtranslation rather than ground-truth comparison, making it reference-free). (b) LLM-judge R_judge: binary faithfulness judgment from a frozen LLM (following FormaRL's consistency check approach).\n\n**Reward Compositions (Ablation Matrix):**\n  C1: Binary compilation only (FormaRL reproduction)\n  C2: Graded formal signal only (R_formal)\n  C3: Embedding similarity only (R_embed)\n  C4: LLM judge only (R_judge)\n  C5: Formal + embedding hybrid (R_formal + R_embed)\n  C6: Formal + LLM judge hybrid (R_formal + R_judge)\n  C7: Full hybrid (R_formal + R_embed + R_judge)\n  Weights optimized via small-scale grid search on validation set.\n\n**Training:** GRPO with KL penalty (following FormaRL/Online RL), training Qwen2.5-Coder-7B-Instruct for direct comparison with FormaRL (26.15% pass@1 on ProofNet) and Qwen3-Coder-30B-A3B-Instruct (3B active MoE) for SOTA pursuit on FormalMATH-Lite. Training on ProofNet and FormalMATH-Lite datasets.\n\n**Gaming-Aware Evaluation Framework:**\n  (1) Standard: BEq@1, pass@1, ASSESS structural similarity\n  (2) Faithfulness: Roundtrip consistency rate (formalize→backtranslate→re-formalize→check equivalence, following Faithful Autoformalization via Roundtrip Verification)\n  (3) Gaming detection: Manual audit of 200 sampled compilable outputs per configuration for axiom fabrication, premise mistranslation, and semantic vacuity (following Do LLMs Game Formalization? methodology)\n  (4) Signal-quality correlation: Spearman rank correlation between each reward component and human-judged faithfulness on 200 samples, testing whether formally-grounded signals are actually more informative than semantic signals\n\n**Key Research Questions:**\n  RQ1: Does graded formal signaling (C2) outperform binary compilation (C1)?\n  RQ2: Do formally-grounded signals (C2) outperform semantic signals (C3, C4) on faithfulness metrics?\n  RQ3: Does hybrid composition (C5-C7) yield additive faithfulness gains over individual signals?\n  RQ4: Which compositions produce the lowest formalization gaming rate?",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1200 H100 (7 reward configs × 2 models × ~70 H100-hrs per run + 100 grid search + 100 baseline reproduction + 60 evaluation)",
      "timeline": "14-16 weeks (4 wks pipeline + error classification, 6 wks RL training across configs, 4 wks evaluation/gaming audit/writing)",
      "estimated_gpu_cost": "$3,000 (at ~$2.50/hr H100 spot)"
    },
    "human_in_loop": {
      "gpu_hours": "900 H100 (Claude accelerates pipeline, hyperparameter search, and gaming audit analysis)",
      "timeline": "11-13 weeks",
      "claude_api_cost": "$400 (code generation, error classification pipeline, gaming audit support, ablation analysis)",
      "estimated_gpu_cost": "$2,250"
    },
    "auto_research": {
      "gpu_hours": "900 H100",
      "timeline": "8-10 weeks",
      "claude_api_cost": "$600 (end-to-end experiment orchestration, automated ablation sweeps, gaming audit, paper drafting)",
      "estimated_gpu_cost": "$2,250",
      "speed_bottleneck": "Lean 4 compilation latency (~5-20s per sample); 7 reward configurations × 80K+ rollouts each require heavily parallelized Lean REPL instances via LeanInteract's AutoLeanServer. Embedding inference for R_embed adds ~20% overhead per rollout batch."
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, paper Sep 24, 2026) — PRIMARY, ~17 weeks available",
    "AAAI 2027 (abstract Jul 26, paper Aug 2, 2026) — STRETCH, only feasible with auto_research timeline if pipeline reuses LeanInteract directly",
    "ARR July 2026 cycle (Jul 30) — committable to EMNLP 2026 or NAACL 2027"
  ],
  "level": "solid+",
  "key_references": [
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "Online Reinforcement Learning for Autoformalization (NeurIPS 2025 MAR Workshop)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (VerifAI-2 @ ICLR 2026)",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)",
    "Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)",
    "Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)",
    "Process-Driven Autoformalization in Lean 4 (arXiv 2024)",
    "Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)",
    "ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Autoformalizer with Tool Feedback (arXiv October 2025)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)",
    "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv March 2026)",
    "FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv March 2026)",
    "Process Reward Models That Think [ThinkPRM] (arXiv 2025)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)"
  ],
  "description": "We conduct the first systematic study of reward signal composition for autoformalization RL, addressing a critical gap: while Online RL for Autoformalization (NeurIPS 2025 MAR Workshop) already combines type-check with embedding similarity, and FormaRL uses binary compilation + LLM judge, no work has controlled for the SOURCE of reward signals to determine whether formal grounding actually matters. Motivated by the formalization gaming problem—where 'Do LLMs Game Formalization?' (VerifAI-2 @ ICLR 2026) shows models achieve 87-99% compilation while systematically producing unfaithful formalizations—we design a 7-configuration ablation matrix comparing: graded formally-grounded rewards (error-category classification from Lean compiler diagnostics via LeanInteract), semantic rewards (embedding similarity, LLM judge), and hybrid compositions under GRPO training. Our formally-grounded signal uses a practical error-message-classification approach—parsing LeanInteract's structured Message objects into ordered categories (parse error → name resolution failure → type mismatch → clean compilation)—avoiding the deep Lean metaprogramming that direct elaboration state extraction would require. Crucially, we evaluate not just BEq@1 and ASSESS but also roundtrip consistency (faithfulness) and formalization gaming rates, answering: (RQ1) Does graded formal signaling outperform binary? (RQ2) Do formally-grounded signals outperform semantic ones on faithfulness? (RQ3) Do hybrid compositions yield additive gains? (RQ4) Which compositions resist gaming? We train on Qwen2.5-Coder-7B-Instruct for FormaRL comparison and Qwen3-Coder-30B-A3B-Instruct for SOTA pursuit, targeting ICLR 2027.",
  "project_name": "reward_comp_autoform",
  "source": "web_research"
}

## Reviewer feedback (round 2)
Issues: ["AAAI 2027 deadline dates are factually wrong: actual abstract deadline is July 21 (not July 26) and paper deadline is July 28 (not August 2, 2026). This further tightens the already-acknowledged stretch timeline.", "Lean compilation bottleneck inadequately budgeted: 7 configs × 2 models × ~80K rollouts × 16 samples × 10s avg compilation = ~179M CPU-seconds total. Even with 64 parallel Lean REPL instances, this is ~780 wall-clock hours of CPU time per configuration. CPU instance costs are entirely absent from the resource estimate, yet could rival GPU costs.", "Human gaming audit labor unbudgeted: 200 samples × 7 configurations × 2 models = 2800 manual audits (proposal says 200 per configuration but there are 14 config-model pairs). At 5-10 minutes per expert audit, this is 230-470 hours of skilled human labor—a significant hidden cost.", "CriticLean (arXiv July 2025) is missing from related work: it combines Lean compiler feedback with a trained critic model (CriticLeanGPT) for semantic fidelity assessment of autoformalization, directly relevant to the formally-grounded vs. semantic signal comparison. Should be discussed and differentiated.", "No explicit negative-result mitigation strategy: if RQ2 yields 'formally-grounded signals ≈ semantic signals on faithfulness,' the paper needs a pre-committed framing. This null result is scientifically valuable but harder to publish at a top venue without positioning it as the primary contribution.", "The 'Online RL for Autoformalization' venue attribution could not be confirmed as 'MAR Workshop'—it was not found in the NeurIPS 2025 MATH-AI Workshop accepted papers list, and the paper may be at a different NeurIPS 2025 workshop. Verify the exact venue.", "Fundamentally an ablation study: the core contribution is comparing known reward signals (compilation, error categories, embeddings, LLM judges) under GRPO. For ICLR 2027, this needs either a strong new methodological contribution (e.g., the gaming-aware evaluation as a standalone framework) or surprising empirical results to clear the acceptance bar."]
Feedback: The revision substantially improved the proposal—reframed research question, practical error-classification approach, gaming-aware evaluation, and realistic venue targeting are all strong. To reach pass quality: (1) Fix AAAI 2027 dates (Jul 21/28, not Jul 26/Aug 2). (2) Add explicit CPU resource budget for Lean compilation—estimate the number of parallel LeanInteract instances needed and their cost. Consider pre-compiling a compilation cache for commonly-imported Mathlib components. (3) Budget the human gaming audit realistically—with 14 config-model pairs × 200 samples, this is 2800 audits unless you sample a subset. Consider reducing to 100 samples per config or using stratified sampling. (4) Add CriticLean as related work: it trains a critic model on semantic fidelity (a learned alternative to embedding/LLM-judge signals) and could be included as C8 in the ablation or as a comparison point. (5) Pre-commit to a framing for negative results: if formally-grounded signals don't outperform semantic ones, position this as 'the cost-effectiveness insight'—cheap embedding rewards are sufficient, saving the engineering cost of error classification pipelines. (6) Consider elevating the gaming-aware evaluation framework as a co-primary contribution with a separate ablation on detection sensitivity, making the paper viable even if the reward composition results are inconclusive. (7) Verify the exact workshop venue for 'Online RL for Autoformalization' at NeurIPS 2025.

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
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "17917120-41b4-4c6c-97ae-2e19e01a110c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T20:36:08.779Z_

```json
{
  "parentUuid": "17917120-41b4-4c6c-97ae-2e19e01a110c",
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
  "uuid": "58b15cd0-a1ef-4de6-9947-ae32395f566e",
  "timestamp": "2026-05-27T20:36:08.779Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T20:36:08.779Z_

```json
{
  "parentUuid": "58b15cd0-a1ef-4de6-9947-ae32395f566e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1433d2e1-98d1-4ea1-9523-46e2f6b9e968",
  "timestamp": "2026-05-27T20:36:08.779Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "1433d2e1-98d1-4ea1-9523-46e2f6b9e968",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Assistant

_source line 8 · 2026-05-27T20:36:15.608Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research accordingly. The key issues are:

1. AAAI 2027 dates wrong (Jul 21/28, not Jul 26/Aug 2)
2. Lean compilation CPU costs unbudgeted
3. Human gaming audit labor unbudgeted (2800 audits)
4. CriticLean missing from related work
5. No negative-result mitigation strategy
6. "Online RL for Autoformalization" venue attribution uncertain
7. Fundamentally an ablation study - needs stronger contribution for ICLR 2027


I'll need to verify the AAAI dates, dig into Lean compilation costs and parallelization options, locate and review the CriticLean paper, confirm the venue for that autoformalization work, and figure out how to reframe this beyond just an ablation study.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1433d2e1-98d1-4ea1-9523-46e2f6b9e968",
  "isSidechain": false,
  "requestId": "req_011CbTiR9Q4KkufBF31zcs5w",
  "type": "assistant",
  "uuid": "163d2c2f-4c60-4d7d-a32f-0c7ab8c07544",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017M6j65AEfhUyQWcV8vX4Ha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7101,
      "cache_read_input_tokens": 11014,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 346,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7101
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

_source line 9 · 2026-05-27T20:36:15.610Z_

I'll systematically research each reviewer issue before making revisions. Let me launch parallel investigations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163d2c2f-4c60-4d7d-a32f-0c7ab8c07544",
  "isSidechain": false,
  "requestId": "req_011CbTiR9Q4KkufBF31zcs5w",
  "type": "assistant",
  "uuid": "57bd236f-b23b-4171-91c5-f6d1fec41e6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017M6j65AEfhUyQWcV8vX4Ha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7101,
      "cache_read_input_tokens": 11014,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 346,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7101
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

_source line 10 · 2026-05-27T20:36:15.727Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BKaGLXXPCHQbGoCF6j5uJC`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57bd236f-b23b-4171-91c5-f6d1fec41e6d",
  "isSidechain": false,
  "requestId": "req_011CbTiR9Q4KkufBF31zcs5w",
  "type": "assistant",
  "uuid": "5841f443-96c8-4d35-bb75-55307564481f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017M6j65AEfhUyQWcV8vX4Ha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7101,
      "cache_read_input_tokens": 11014,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 346,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7101
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

_source line 11 · 2026-05-27T20:36:15.734Z_

<details><summary>↩ Tool result · `toolu_01BKaGLXXPCHQbGoCF6j5uJC`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "5841f443-96c8-4d35-bb75-55307564481f",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "e866f583-599f-470c-8ff9-e4981787bbd5",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "5841f443-96c8-4d35-bb75-55307564481f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T20:36:19.725Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me launch parallel research on the key issues. I'll search for:
1. CriticLean paper
2. AAAI 2027 actual dates
3. "Online RL for Autoformalization" venue verification
4. LeanInteract parallelization and Lean compilation costs
5. Whether this is fundamentally an ablation study - how to elevate contribution
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e866f583-599f-470c-8ff9-e4981787bbd5",
  "isSidechain": false,
  "requestId": "req_011CbTiRf1mtnUaam65ViE2w",
  "type": "assistant",
  "uuid": "7d68891a-5dc7-4e3d-bac7-dc811e121b21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8TsgJtoHuoFMZnMQ6H8JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 18115,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 188,
          "cache_read_input_tokens": 18115,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
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

_source line 13 · 2026-05-27T20:36:19.726Z_

Now let me launch parallel research on all the key reviewer issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d68891a-5dc7-4e3d-bac7-dc811e121b21",
  "isSidechain": false,
  "requestId": "req_011CbTiRf1mtnUaam65ViE2w",
  "type": "assistant",
  "uuid": "361b3d2e-eb27-45fe-9c46-a5d212c8d15f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8TsgJtoHuoFMZnMQ6H8JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 18115,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 188,
          "cache_read_input_tokens": 18115,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
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

_source line 14 · 2026-05-27T20:36:20.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019boeZRh6FgphALZLfidGG1`</summary>

```json
{
  "query": "CriticLean arXiv 2025 autoformalization critic model semantic fidelity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "361b3d2e-eb27-45fe-9c46-a5d212c8d15f",
  "isSidechain": false,
  "requestId": "req_011CbTiRf1mtnUaam65ViE2w",
  "type": "assistant",
  "uuid": "46f194ce-3a50-4394-92c5-034dbb7f3cbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8TsgJtoHuoFMZnMQ6H8JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1366,
      "cache_read_input_tokens": 18115,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 188,
          "cache_read_input_tokens": 18115,
          "cache_creation_input_tokens": 1366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1366
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

_source line 15 · 2026-05-27T20:36:27.060Z_

<details><summary>↩ Tool result · `toolu_019boeZRh6FgphALZLfidGG1`</summary>

```text
Web search results for query: "CriticLean arXiv 2025 autoformalization critic model semantic fidelity"

Links: [{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"},{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"GitHub - multimodal-art-projection/CriticLean · GitHub","url":"https://github.com/multimodal-art-projection/CriticLean"},{"title":"M-A-P CriticLean: Critic-Guided Reinforcement Learning for","url":"https://arxiv.org/pdf/2507.06181"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/html/2510.24592"},{"title":"[2511.12784] Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/abs/2511.12784"}]

Based on the search results, here's what I found about CriticLean:

## Overview

CriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. It addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code for automated theorem proving, with a focus on the critic phase—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem.

## Key Components

The framework proposes CriticLeanGPT, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Additionally, it introduces CriticLeanBench, a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.

## Framework Approach

The framework works by applying autoformalization iteratively based on feedback from both the Lean compiler and specialized critic models trained to assess semantic fidelity. By focusing on semantic fidelity rather than just syntactic correctness or compilation success, the CriticLean approach offers a more complete solution to the challenge of mathematical autoformalization.

## Research Impact

The work also constructs FineLeanCorpus, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46f194ce-3a50-4394-92c5-034dbb7f3cbf",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "1247c63d-fde1-4240-bfed-ac6be6277a53",
  "toolUseResult": {
    "query": "CriticLean arXiv 2025 autoformalization critic model semantic fidelity",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FzzJzSRvsqgqVCpDQ2LfnH",
        "content": [
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
          },
          {
            "title": "(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"
          },
          {
            "title": "[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181"
          },
          {
            "title": "[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181v1"
          },
          {
            "title": "GitHub - multimodal-art-projection/CriticLean · GitHub",
            "url": "https://github.com/multimodal-art-projection/CriticLean"
          },
          {
            "title": "M-A-P CriticLean: Critic-Guided Reinforcement Learning for",
            "url": "https://arxiv.org/pdf/2507.06181"
          },
          {
            "title": "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization",
            "url": "https://arxiv.org/html/2510.24592"
          },
          {
            "title": "[2511.12784] Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing",
            "url": "https://arxiv.org/abs/2511.12784"
          }
        ]
      },
      "Based on the search results, here's what I found about CriticLean:\n\n## Overview\n\nCriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. It addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code for automated theorem proving, with a focus on the critic phase—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem.\n\n## Key Components\n\nThe framework proposes CriticLeanGPT, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Additionally, it introduces CriticLeanBench, a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.\n\n## Framework Approach\n\nThe framework works by applying autoformalization iteratively based on feedback from both the Lean compiler and specialized critic models trained to assess semantic fidelity. By focusing on semantic fidelity rather than just syntactic correctness or compilation success, the CriticLean approach offers a more complete solution to the challenge of mathematical autoformalization.\n\n## Research Impact\n\nThe work also constructs FineLeanCorpus, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation."
    ],
    "durationSeconds": 6.829898885999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "46f194ce-3a50-4394-92c5-034dbb7f3cbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T20:36:29.653Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KxN4SNgeDxvoDEMaBJcgdX`</summary>

```json
{
  "query": "AAAI 2027 conference submission deadline dates call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1247c63d-fde1-4240-bfed-ac6be6277a53",
  "isSidechain": false,
  "requestId": "req_011CbTiSVQMfUQcy1yPHGDec",
  "type": "assistant",
  "uuid": "0bcf2fef-1a1f-4608-8165-a73cec78d310",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNBhx29oRY18YWzdrejZZB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 973,
      "cache_read_input_tokens": 19481,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 19481,
          "cache_creation_input_tokens": 973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 973
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

_source line 17 · 2026-05-27T20:36:35.425Z_

<details><summary>↩ Tool result · `toolu_01KxN4SNgeDxvoDEMaBJcgdX`</summary>

```text
Web search results for query: "AAAI 2027 conference submission deadline dates call for papers"

Links: [{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"}]

Based on the search results, here are the AAAI 2027 conference submission deadline dates and key information:

## Conference Details
The Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.

## Main Technical Track Submission Deadlines
For the Main Technical Track, the key deadlines are:
- June 17, 2026: Open Review submission site opens for author registration
- June 24, 2026: Open Review submission site opens for paper submission
- July 21, 2026: Abstracts due at 11:59 PM UTC-12
- July 28, 2026: Full papers due at 11:59 PM UTC-12
- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12
- September 24, 2026: Notification of Phase 1 rejections
- October 19-25, 2026: Author feedback window
- November 30, 2026: Notification of final acceptance or rejection
- December 14, 2026: Submission of camera-ready files

## Important Note
Deadlines are track-specific and may differ from those listed above, with track-specific deadlines listed on their respective Call for Papers (CFP). All deadlines are on an "anywhere on earth" basis (UTC-12).

For the official AAAI 2027 Call for Papers and track-specific information, visit https://aaai.org/conference/aaai/aaai-27/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bcf2fef-1a1f-4608-8165-a73cec78d310",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "e2dff4ed-23e6-485b-b872-e39e4be1129a",
  "toolUseResult": {
    "query": "AAAI 2027 conference submission deadline dates call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B8Bt71qQWnqCL17Pq2xyGs",
        "content": [
          {
            "title": "AAAI-27 - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/"
          },
          {
            "title": "AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot",
            "url": "https://www.getpaperpilot.com/deadlines/aaai-2027.html"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AAAI-27 Main Technical Track - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"
          },
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/conference/?id=aaai27"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          },
          {
            "title": "AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=3"
          },
          {
            "title": "AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/aaai"
          },
          {
            "title": "AAAI 2027 Conference | OpenReview",
            "url": "https://openreview.net/group?id=AAAI.org%2F2027%2FConference"
          }
        ]
      },
      "Based on the search results, here are the AAAI 2027 conference submission deadline dates and key information:\n\n## Conference Details\nThe Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.\n\n## Main Technical Track Submission Deadlines\nFor the Main Technical Track, the key deadlines are:\n- June 17, 2026: Open Review submission site opens for author registration\n- June 24, 2026: Open Review submission site opens for paper submission\n- July 21, 2026: Abstracts due at 11:59 PM UTC-12\n- July 28, 2026: Full papers due at 11:59 PM UTC-12\n- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12\n- September 24, 2026: Notification of Phase 1 rejections\n- October 19-25, 2026: Author feedback window\n- November 30, 2026: Notification of final acceptance or rejection\n- December 14, 2026: Submission of camera-ready files\n\n## Important Note\nDeadlines are track-specific and may differ from those listed above, with track-specific deadlines listed on their respective Call for Papers (CFP). All deadlines are on an \"anywhere on earth\" basis (UTC-12).\n\nFor the official AAAI 2027 Call for Papers and track-specific information, visit https://aaai.org/conference/aaai/aaai-27/"
    ],
    "durationSeconds": 5.766846863999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0bcf2fef-1a1f-4608-8165-a73cec78d310",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T20:36:37.857Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bsc1mqng3a6DzSaoEboBbF`</summary>

```json
{
  "query": "\"Online Reinforcement Learning for Autoformalization\" NeurIPS 2025 workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2dff4ed-23e6-485b-b872-e39e4be1129a",
  "isSidechain": false,
  "requestId": "req_011CbTiT7ARUoUGKchA4EFqk",
  "type": "assistant",
  "uuid": "7e83d7b9-fb1f-4c6e-a485-3047311067be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182FyjMRZeLTFVrz4WQNQ74",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 975,
      "cache_read_input_tokens": 20454,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 20454,
          "cache_creation_input_tokens": 975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 975
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

_source line 19 · 2026-05-27T20:36:43.374Z_

<details><summary>↩ Tool result · `toolu_01Bsc1mqng3a6DzSaoEboBbF`</summary>

```text
Web search results for query: ""Online Reinforcement Learning for Autoformalization" NeurIPS 2025 workshop"

Links: [{"title":"(PDF) Online Reinforcement Learning for Autoformalization","url":"https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"},{"title":"NeurIPS 2025 Schedule","url":"https://neurips.cc/virtual/2025/loc/san-diego/calendar"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"5th MATH-AI Workshop at NeurIPS'25 - Math-AI","url":"https://mathai2025.github.io/papers/"},{"title":"NeurIPS 2025 Recap | Amplify Partners","url":"https://www.amplifypartners.com/blog-posts/neurips-2025-recap"},{"title":"NeurIPS 2025 - Microsoft Research","url":"https://www.microsoft.com/en-us/research/event/neurips-2025/sessions/"},{"title":"ICML 2025 Workshops","url":"https://icml.cc/virtual/2025/events/workshop"}]

Based on the search results, I found relevant information about the work on "Online Reinforcement Learning for Autoformalization":

The paper studies online reinforcement learning for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4. This work was presented at the Multimodal Algorithmic Reasoning Workshop at NeurIPS 2025.

The research addresses the challenge that autoformalization lacks a natural dense reward, and proposes composite reward formulations that combine syntactic signals (Lean type-check) with semantic measures, including exact-match style metrics based on BEq / BEq+ when ground-truth formalizations exist, and a continuous embedding-based similarity reward that requires no paired data.

The paper appears to represent an important contribution to combining reinforcement learning techniques with mathematical formalization, addressing both the practical challenges of reward design and the evaluation of formal translations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e83d7b9-fb1f-4c6e-a485-3047311067be",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "05054f40-29f6-454e-b9a2-976659ca6162",
  "toolUseResult": {
    "query": "\"Online Reinforcement Learning for Autoformalization\" NeurIPS 2025 workshop",
    "results": [
      {
        "tool_use_id": "srvtoolu_017XZ9cb53bfnxpbhCyy75vz",
        "content": [
          {
            "title": "(PDF) Online Reinforcement Learning for Autoformalization",
            "url": "https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"
          },
          {
            "title": "NeurIPS 2025 Schedule",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/calendar"
          },
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/pdf/2508.18914"
          },
          {
            "title": "5th MATH-AI Workshop at NeurIPS'25 - Math-AI",
            "url": "https://mathai2025.github.io/papers/"
          },
          {
            "title": "NeurIPS 2025 Recap | Amplify Partners",
            "url": "https://www.amplifypartners.com/blog-posts/neurips-2025-recap"
          },
          {
            "title": "NeurIPS 2025 - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/event/neurips-2025/sessions/"
          },
          {
            "title": "ICML 2025 Workshops",
            "url": "https://icml.cc/virtual/2025/events/workshop"
          }
        ]
      },
      "Based on the search results, I found relevant information about the work on \"Online Reinforcement Learning for Autoformalization\":\n\nThe paper studies online reinforcement learning for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4. This work was presented at the Multimodal Algorithmic Reasoning Workshop at NeurIPS 2025.\n\nThe research addresses the challenge that autoformalization lacks a natural dense reward, and proposes composite reward formulations that combine syntactic signals (Lean type-check) with semantic measures, including exact-match style metrics based on BEq / BEq+ when ground-truth formalizations exist, and a continuous embedding-based similarity reward that requires no paired data.\n\nThe paper appears to represent an important contribution to combining reinforcement learning techniques with mathematical formalization, addressing both the practical challenges of reward design and the evaluation of formal translations."
    ],
    "durationSeconds": 5.5137677049999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7e83d7b9-fb1f-4c6e-a485-3047311067be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T20:36:46.168Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RQVwEmEwZb6NPp1rJ5UUa4`</summary>

```json
{
  "query": "LeanInteract parallel Lean REPL instances compilation throughput AutoLeanServer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05054f40-29f6-454e-b9a2-976659ca6162",
  "isSidechain": false,
  "requestId": "req_011CbTiThBZ1HoDKbfH1vpKf",
  "type": "assistant",
  "uuid": "9b573388-843d-4298-97f1-7e4a067fa046",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuA6246dL8r5vBS6c1dmbX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 21429,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 21429,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 610
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "9b573388-843d-4298-97f1-7e4a067fa046",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Tool result

_source line 23 · 2026-05-27T20:36:52.610Z_

<details><summary>↩ Tool result · `toolu_01RQVwEmEwZb6NPp1rJ5UUa4`</summary>

```text
Web search results for query: "LeanInteract parallel Lean REPL instances compilation throughput AutoLeanServer"

Links: [{"title":"LeanInteract/README.md at main · augustepoiroux/LeanInteract","url":"https://github.com/augustepoiroux/LeanInteract/blob/main/README.md"},{"title":"lean-interact · PyPI","url":"https://pypi.org/project/lean-interact/"},{"title":"GitHub - augustepoiroux/LeanInteract: LeanInteract: A Python Interface for Lean 4 · GitHub","url":"https://github.com/augustepoiroux/LeanInteract"},{"title":"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification","url":"https://arxiv.org/html/2504.21230"},{"title":"augustepoiroux/leaninteract Documentation | Docfork","url":"https://docfork.com/augustepoiroux/leaninteract"},{"title":"Kimina Lean Server: Technical Report","url":"https://arxiv.org/html/2504.21230v1"}]

Based on the search results, here's what I found about LeanInteract's approach to parallel Lean REPL instances and compilation throughput:

## Parallel Processing Architecture

To run multiple requests in parallel, LeanInteract recommends using multiprocessing with one global LeanREPLConfig instance, and one AutoLeanServer instance per process. You should instantiate LeanREPLConfig before starting the processes to avoid conflicts during Lean REPL's download and build.

## AutoLeanServer Features

AutoLeanServer is an experimental subclass of LeanServer that automatically recovers from some crashes and timeouts, and also monitors memory usage to limit out of memory issues in multiprocessing contexts.

## Performance Considerations

The architecture is designed to handle compilation throughput challenges. To address out of memory errors, you can reduce parallel processing or increase system memory, or alternatively use AutoLeanServer with conservative memory settings. For timeout errors, AutoLeanServer provides automatic recovery.

## Real-World Application

In a recent benchmark study, researchers used LeanInteract following the library's official recommendation for parallel processing: using one LeanREPLConfig instance, and one AutoLeanServer instance per process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b573388-843d-4298-97f1-7e4a067fa046",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "5b0e5328-132f-4c5e-bb9f-f7569ec9b206",
  "toolUseResult": {
    "query": "LeanInteract parallel Lean REPL instances compilation throughput AutoLeanServer",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TUfvyX7wbfkGhUGjtSferi",
        "content": [
          {
            "title": "LeanInteract/README.md at main · augustepoiroux/LeanInteract",
            "url": "https://github.com/augustepoiroux/LeanInteract/blob/main/README.md"
          },
          {
            "title": "lean-interact · PyPI",
            "url": "https://pypi.org/project/lean-interact/"
          },
          {
            "title": "GitHub - augustepoiroux/LeanInteract: LeanInteract: A Python Interface for Lean 4 · GitHub",
            "url": "https://github.com/augustepoiroux/LeanInteract"
          },
          {
            "title": "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification",
            "url": "https://arxiv.org/html/2504.21230"
          },
          {
            "title": "augustepoiroux/leaninteract Documentation | Docfork",
            "url": "https://docfork.com/augustepoiroux/leaninteract"
          },
          {
            "title": "Kimina Lean Server: Technical Report",
            "url": "https://arxiv.org/html/2504.21230v1"
          }
        ]
      },
      "Based on the search results, here's what I found about LeanInteract's approach to parallel Lean REPL instances and compilation throughput:\n\n## Parallel Processing Architecture\n\nTo run multiple requests in parallel, LeanInteract recommends using multiprocessing with one global LeanREPLConfig instance, and one AutoLeanServer instance per process. You should instantiate LeanREPLConfig before starting the processes to avoid conflicts during Lean REPL's download and build.\n\n## AutoLeanServer Features\n\nAutoLeanServer is an experimental subclass of LeanServer that automatically recovers from some crashes and timeouts, and also monitors memory usage to limit out of memory issues in multiprocessing contexts.\n\n## Performance Considerations\n\nThe architecture is designed to handle compilation throughput challenges. To address out of memory errors, you can reduce parallel processing or increase system memory, or alternatively use AutoLeanServer with conservative memory settings. For timeout errors, AutoLeanServer provides automatic recovery.\n\n## Real-World Application\n\nIn a recent benchmark study, researchers used LeanInteract following the library's official recommendation for parallel processing: using one LeanREPLConfig instance, and one AutoLeanServer instance per process."
    ],
    "durationSeconds": 6.4382236520000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9b573388-843d-4298-97f1-7e4a067fa046",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-27T20:36:55.044Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013tDV3WzkHzvwfywM44Fxgn`</summary>

```json
{
  "query": "Kimina Lean Server high performance large scale verification throughput"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b0e5328-132f-4c5e-bb9f-f7569ec9b206",
  "isSidechain": false,
  "requestId": "req_011CbTiUNdd7ZDYfCaTSJvS9",
  "type": "assistant",
  "uuid": "d1b6c23a-c8a7-4e2c-86fc-588177ff0282",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QueEQttp6TmMCgofjskFBa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 22039,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 22039,
          "cache_creation_input_tokens": 638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 638
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

_source line 25 · 2026-05-27T20:37:01.077Z_

<details><summary>↩ Tool result · `toolu_013tDV3WzkHzvwfywM44Fxgn`</summary>

```text
Web search results for query: "Kimina Lean Server high performance large scale verification throughput"

Links: [{"title":"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250421230D/abstract"},{"title":"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification | OpenReview","url":"https://openreview.net/forum?id=orPt2nxLoC"},{"title":"[2504.21230] Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification","url":"https://arxiv.org/abs/2504.21230"},{"title":"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification","url":"https://openreview.net/pdf?id=orPt2nxLoC"},{"title":"Kimina Lean Server: Technical Report","url":"https://arxiv.org/html/2504.21230v1"},{"title":"Kimina-Prover-RL","url":"https://huggingface.co/blog/AI-MO/kimina-prover-rl"},{"title":"Kimina-Prover Preview 72B","url":"https://www.emergentmind.com/topics/kimina-prover-preview-72b"},{"title":"Kimina-Prover-RL: The Game-Changing Open-Source AI Pipeline for Formal Theorem Proving - UNDERCODE NEWS","url":"https://undercodenews.com/kimina-prover-rl-the-game-changing-open-source-ai-pipeline-for-formal-theorem-proving/"}]

Based on the search results, here's what I found about the Kimina Lean Server:

## Overview

The Kimina Lean Server is an open-source project designed as a high-performance verifier for reinforcement learning pipelines.

## Key Features

Built on top of the Lean REPL (Read-Eval-Print Loop) maintained by the Lean FRO, the server combines server-side parallelism by managing multiple Lean processes in parallel with a Least Recently Used (LRU) caching mechanism that reuses Lean imports across requests. On the client side, a lightweight Python package enables submitting proof batches and receiving Lean feedback, including extracted tactics and tactic states.

## Performance and Throughput

The Kimina Lean Server outperforms previous Lean interaction tools, achieving a 1.5 to 2 times speedup in verification time. Additionally, the Numina Lean Server achieves verification throughput up to 100 proofs/sec on large CPU clusters.

## Applications

Its improved efficiency has enabled its use in the large-scale training of state-of-the-art models such as Kimina-Prover.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1b6c23a-c8a7-4e2c-86fc-588177ff0282",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "2d5b0317-76f2-452e-b65e-5e70a085d4e8",
  "toolUseResult": {
    "query": "Kimina Lean Server high performance large scale verification throughput",
    "results": [
      {
        "tool_use_id": "srvtoolu_0164hEJU5GeAK1JZ5d9WSRAJ",
        "content": [
          {
            "title": "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250421230D/abstract"
          },
          {
            "title": "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification | OpenReview",
            "url": "https://openreview.net/forum?id=orPt2nxLoC"
          },
          {
            "title": "[2504.21230] Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification",
            "url": "https://arxiv.org/abs/2504.21230"
          },
          {
            "title": "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification",
            "url": "https://openreview.net/pdf?id=orPt2nxLoC"
          },
          {
            "title": "Kimina Lean Server: Technical Report",
            "url": "https://arxiv.org/html/2504.21230v1"
          },
          {
            "title": "Kimina-Prover-RL",
            "url": "https://huggingface.co/blog/AI-MO/kimina-prover-rl"
          },
          {
            "title": "Kimina-Prover Preview 72B",
            "url": "https://www.emergentmind.com/topics/kimina-prover-preview-72b"
          },
          {
            "title": "Kimina-Prover-RL: The Game-Changing Open-Source AI Pipeline for Formal Theorem Proving - UNDERCODE NEWS",
            "url": "https://undercodenews.com/kimina-prover-rl-the-game-changing-open-source-ai-pipeline-for-formal-theorem-proving/"
          }
        ]
      },
      "Based on the search results, here's what I found about the Kimina Lean Server:\n\n## Overview\n\nThe Kimina Lean Server is an open-source project designed as a high-performance verifier for reinforcement learning pipelines.\n\n## Key Features\n\nBuilt on top of the Lean REPL (Read-Eval-Print Loop) maintained by the Lean FRO, the server combines server-side parallelism by managing multiple Lean processes in parallel with a Least Recently Used (LRU) caching mechanism that reuses Lean imports across requests. On the client side, a lightweight Python package enables submitting proof batches and receiving Lean feedback, including extracted tactics and tactic states.\n\n## Performance and Throughput\n\nThe Kimina Lean Server outperforms previous Lean interaction tools, achieving a 1.5 to 2 times speedup in verification time. Additionally, the Numina Lean Server achieves verification throughput up to 100 proofs/sec on large CPU clusters.\n\n## Applications\n\nIts improved efficiency has enabled its use in the large-scale training of state-of-the-art models such as Kimina-Prover."
    ],
    "durationSeconds": 6.030127310000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d1b6c23a-c8a7-4e2c-86fc-588177ff0282",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-27T20:37:04.585Z_

Now let me fetch the CriticLean paper and the Kimina Lean Server paper for deeper reading, and verify the Online RL workshop venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d5b0317-76f2-452e-b65e-5e70a085d4e8",
  "isSidechain": false,
  "requestId": "req_011CbTiUzrThJ6gY9vfUqGpb",
  "type": "assistant",
  "uuid": "bc65be09-7346-4cac-b40a-c618d8a0f0ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xyvbf8KbgpAEdcEiENE5mV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 22677,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 22677,
          "cache_creation_input_tokens": 779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 779
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

_source line 27 · 2026-05-27T20:37:07.629Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019q1nYCwHSkpie7SsSrXpnw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.06181",
  "prompt": "Extract the full details of CriticLean: (1) What is CriticLeanGPT and how is it trained? (2) What reward signals does it use for RL? (3) What datasets does it use (FineLeanCorpus details)? (4) What are the main results - performance numbers? (5) How does the critic model assess semantic fidelity specifically? (6) What is CriticLeanBench? (7) What base models do they use? (8) How does it compare to FormaRL and other baselines? (9) What is the exact RL training setup (PPO, GRPO, etc.)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc65be09-7346-4cac-b40a-c618d8a0f0ea",
  "isSidechain": false,
  "requestId": "req_011CbTiUzrThJ6gY9vfUqGpb",
  "type": "assistant",
  "uuid": "79031a36-3141-4860-8c54-56bf1c9d5c5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xyvbf8KbgpAEdcEiENE5mV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 22677,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 22677,
          "cache_creation_input_tokens": 779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 779
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

_source line 28 · 2026-05-27T20:37:12.670Z_

<details><summary>↩ Tool result · `toolu_019q1nYCwHSkpie7SsSrXpnw`</summary>

```text
# CriticLean: Analysis Based on Available Information

Based on the arXiv abstract provided, here's what can be extracted:

## 1. **CriticLeanGPT Training**
The paper describes it as "trained via supervised fine-tuning and reinforcement learning" to evaluate semantic fidelity of Lean 4 formalizations. Specific architecture and training procedures are not detailed in the abstract.

## 2. **Reward Signals**
The abstract does not specify which reward signals are employed for the reinforcement learning phase.

## 3. **FineLeanCorpus Dataset**
The framework includes "a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation."

## 4. **Main Results**
The abstract reports that "trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines" on the evaluation benchmark, but no specific performance metrics are provided.

## 5. **Semantic Fidelity Assessment**
The paper positions the critic as evaluating "whether generated formalizations truly capture the semantic intent of the original problem," though specific assessment mechanisms aren't elaborated in the abstract.

## 6. **CriticLeanBench**
Described as "a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations."

## 7-9. **Base Models, Comparisons, RL Algorithm**
These details—including specific base models, comparisons to FormaRL, and the exact RL algorithm (PPO, GRPO, etc.)—are not included in the provided abstract text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79031a36-3141-4860-8c54-56bf1c9d5c5d",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "bc9db9fe-f87b-4614-92d0-2efe194b7194",
  "toolUseResult": {
    "bytes": 48790,
    "code": 200,
    "codeText": "OK",
    "result": "# CriticLean: Analysis Based on Available Information\n\nBased on the arXiv abstract provided, here's what can be extracted:\n\n## 1. **CriticLeanGPT Training**\nThe paper describes it as \"trained via supervised fine-tuning and reinforcement learning\" to evaluate semantic fidelity of Lean 4 formalizations. Specific architecture and training procedures are not detailed in the abstract.\n\n## 2. **Reward Signals**\nThe abstract does not specify which reward signals are employed for the reinforcement learning phase.\n\n## 3. **FineLeanCorpus Dataset**\nThe framework includes \"a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.\"\n\n## 4. **Main Results**\nThe abstract reports that \"trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines\" on the evaluation benchmark, but no specific performance metrics are provided.\n\n## 5. **Semantic Fidelity Assessment**\nThe paper positions the critic as evaluating \"whether generated formalizations truly capture the semantic intent of the original problem,\" though specific assessment mechanisms aren't elaborated in the abstract.\n\n## 6. **CriticLeanBench**\nDescribed as \"a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.\"\n\n## 7-9. **Base Models, Comparisons, RL Algorithm**\nThese details—including specific base models, comparisons to FormaRL, and the exact RL algorithm (PPO, GRPO, etc.)—are not included in the provided abstract text.",
    "durationMs": 5035,
    "url": "https://arxiv.org/abs/2507.06181"
  },
  "sourceToolAssistantUUID": "79031a36-3141-4860-8c54-56bf1c9d5c5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-27T20:37:12.673Z_

```json
{
  "parentUuid": "bc9db9fe-f87b-4614-92d0-2efe194b7194",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2373d5de-c609-4b55-a9d9-83fec1a0a8c5",
  "timestamp": "2026-05-27T20:37:12.673Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-27T20:37:17.765Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EBGEjBWx2Ug3BoyWfnV1tB`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.21230v1",
  "prompt": "Extract: (1) Exact throughput numbers - how many proofs per second? (2) How many parallel Lean REPL instances can run? (3) CPU resource requirements per instance. (4) Memory requirements per Lean instance. (5) LRU caching mechanism - what does it cache and what speedup does it provide? (6) How does it compare to LeanInteract in speed? (7) Total cluster size used in their experiments. (8) Any cost estimates for running at scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2373d5de-c609-4b55-a9d9-83fec1a0a8c5",
  "isSidechain": false,
  "requestId": "req_011CbTiVrREcFVLzUebShGS4",
  "type": "assistant",
  "uuid": "80b2bd4a-453c-4beb-9f67-60fad20dea76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQCvsUp35dc5qRPa79uSrb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 23456,
      "output_tokens": 194,
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
          "output_tokens": 194,
          "cache_read_input_tokens": 23456,
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

_source line 31 · 2026-05-27T20:37:23.525Z_

<details><summary>↩ Tool result · `toolu_01EBGEjBWx2Ug3BoyWfnV1tB`</summary>

```text
# Kimina Lean Server: Performance and Resource Metrics

Based on the technical report, here's what's documented:

## Throughput Numbers
The report shows **0.83 to 4.33 iterations/second** depending on CPU count. On an M2 MacBook with 10 CPUs, cached verification achieved **3.65 seconds per proof**, translating to roughly **0.27 proofs/second**.

## Parallel REPL Instances
The document doesn't specify a maximum number of instances. It states the server "keeps a pool of pre-started Lean REPL workers" but provides no upper limit documentation.

## CPU and Memory Requirements Per Instance
**Not specified.** The report doesn't detail individual instance requirements, only that "each worker runs in its own process."

## LRU Caching Details
The cache stores "frequently used modules (e.g., Mathlib)" indexed by script headers. Results show substantial improvement: **5:50 (cached) vs 8:14 (non-cached)** on 100 proofs—approximately **29% speedup**.

## Comparison to LeanInteract
**Not mentioned.** The document references LeanDojo, Pantograph, Leanclient, and itp-interface but makes no LeanInteract comparison.

## Cluster Size Used
Experiments ran on machines with **8, 16, 32, and 60 CPUs**, testing the first 1,000 samples from a dataset. No distributed cluster deployment is described.

## Cost Estimates
**Not provided.** The report contains no pricing or operational cost analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80b2bd4a-453c-4beb-9f67-60fad20dea76",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "b9e5f3e8-1db7-4c71-8ce6-1a45e4ea81d0",
  "toolUseResult": {
    "bytes": 33320,
    "code": 200,
    "codeText": "OK",
    "result": "# Kimina Lean Server: Performance and Resource Metrics\n\nBased on the technical report, here's what's documented:\n\n## Throughput Numbers\nThe report shows **0.83 to 4.33 iterations/second** depending on CPU count. On an M2 MacBook with 10 CPUs, cached verification achieved **3.65 seconds per proof**, translating to roughly **0.27 proofs/second**.\n\n## Parallel REPL Instances\nThe document doesn't specify a maximum number of instances. It states the server \"keeps a pool of pre-started Lean REPL workers\" but provides no upper limit documentation.\n\n## CPU and Memory Requirements Per Instance\n**Not specified.** The report doesn't detail individual instance requirements, only that \"each worker runs in its own process.\"\n\n## LRU Caching Details\nThe cache stores \"frequently used modules (e.g., Mathlib)\" indexed by script headers. Results show substantial improvement: **5:50 (cached) vs 8:14 (non-cached)** on 100 proofs—approximately **29% speedup**.\n\n## Comparison to LeanInteract\n**Not mentioned.** The document references LeanDojo, Pantograph, Leanclient, and itp-interface but makes no LeanInteract comparison.\n\n## Cluster Size Used\nExperiments ran on machines with **8, 16, 32, and 60 CPUs**, testing the first 1,000 samples from a dataset. No distributed cluster deployment is described.\n\n## Cost Estimates\n**Not provided.** The report contains no pricing or operational cost analysis.",
    "durationMs": 5756,
    "url": "https://arxiv.org/html/2504.21230v1"
  },
  "sourceToolAssistantUUID": "80b2bd4a-453c-4beb-9f67-60fad20dea76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T20:37:27.770Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AwYjGAmzkLNAtZXYMvwn5i`</summary>

```json
{
  "url": "https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization",
  "prompt": "Extract: (1) The exact workshop or venue name where this paper was published/presented at NeurIPS 2025. (2) Was it the MAR (Multimodal Algorithmic Reasoning) Workshop? (3) Was it the MATH-AI Workshop? (4) Any other venue information. (5) The authors' names. (6) Key results and reward formulations used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9e5f3e8-1db7-4c71-8ce6-1a45e4ea81d0",
  "isSidechain": false,
  "requestId": "req_011CbTiWepkdViqquQAyf4fE",
  "type": "assistant",
  "uuid": "de31889f-b2b5-4bd3-a452-555180f50456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L27Ku69db2dZaz2sCU1mxF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 24203,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 24203,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 567
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

_source line 33 · 2026-05-27T20:37:28.000Z_

<details><summary>↩ Tool result · `toolu_01AwYjGAmzkLNAtZXYMvwn5i`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de31889f-b2b5-4bd3-a452-555180f50456",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "1b581349-51e4-4e6d-b138-03043e1c821a",
  "toolUseResult": {
    "bytes": 0,
    "code": 403,
    "codeText": "Forbidden",
    "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 227,
    "url": "https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"
  },
  "sourceToolAssistantUUID": "de31889f-b2b5-4bd3-a452-555180f50456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T20:37:30.657Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QpkHP5Vmgqvk34UXzL4coQ`</summary>

```json
{
  "query": "\"Online Reinforcement Learning for Autoformalization\" authors NeurIPS 2025 MAR workshop OR MATH-AI workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b581349-51e4-4e6d-b138-03043e1c821a",
  "isSidechain": false,
  "requestId": "req_011CbTiWyySQvCAb5WjvZKq9",
  "type": "assistant",
  "uuid": "bbdb37f6-2d37-4eec-98d5-c1a95c179eae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2FTQKoM7oVpCR277dML1Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 24770,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 24770,
          "cache_creation_input_tokens": 249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 249
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

_source line 35 · 2026-05-27T20:37:35.900Z_

<details><summary>↩ Tool result · `toolu_01QpkHP5Vmgqvk34UXzL4coQ`</summary>

```text
Web search results for query: ""Online Reinforcement Learning for Autoformalization" authors NeurIPS 2025 MAR workshop OR MATH-AI workshop"

Links: [{"title":"(PDF) Online Reinforcement Learning for Autoformalization","url":"https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"},{"title":"MAR 2025 - Multimodal Algorithmic Reasoning","url":"https://marworkshop.github.io/neurips25/"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"5th MATH-AI Workshop at NeurIPS'25 - Math-AI","url":"https://mathai2025.github.io/papers/"},{"title":"NeurIPS 2025 Workshop MATH-AI | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2025%2FWorkshop%2FMATH-AI"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/pdf/2508.04440"}]

Based on the search results, I found the paper you're looking for:

"Online Reinforcement Learning for Autoformalization" by Sorg, Simon; Li, Wenda; Banerjee, Soumya

This paper was presented at the Multimodal Algorithmic Reasoning Workshop (MAR) at NeurIPS 2025.

The paper studies online reinforcement learning for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4. The authors propose composite reward formulations combining syntactic signals with semantic measures, and use Group Relative Policy Optimization with a KL-divergence penalty for training.

You can find more details about the paper on [ResearchGate](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization) and the [MAR 2025 Workshop website](https://marworkshop.github.io/neurips25/).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbdb37f6-2d37-4eec-98d5-c1a95c179eae",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "18137df2-20f9-4d55-921c-390f3e668976",
  "toolUseResult": {
    "query": "\"Online Reinforcement Learning for Autoformalization\" authors NeurIPS 2025 MAR workshop OR MATH-AI workshop",
    "results": [
      {
        "tool_use_id": "srvtoolu_013bWm2Jdv8S55KrG8wwN4wU",
        "content": [
          {
            "title": "(PDF) Online Reinforcement Learning for Autoformalization",
            "url": "https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"
          },
          {
            "title": "MAR 2025 - Multimodal Algorithmic Reasoning",
            "url": "https://marworkshop.github.io/neurips25/"
          },
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/pdf/2508.18914"
          },
          {
            "title": "5th MATH-AI Workshop at NeurIPS'25 - Math-AI",
            "url": "https://mathai2025.github.io/papers/"
          },
          {
            "title": "NeurIPS 2025 Workshop MATH-AI | OpenReview",
            "url": "https://openreview.net/group?id=NeurIPS.cc%2F2025%2FWorkshop%2FMATH-AI"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/pdf/2508.04440"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Online Reinforcement Learning for Autoformalization\" by Sorg, Simon; Li, Wenda; Banerjee, Soumya\n\nThis paper was presented at the Multimodal Algorithmic Reasoning Workshop (MAR) at NeurIPS 2025.\n\nThe paper studies online reinforcement learning for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4. The authors propose composite reward formulations combining syntactic signals with semantic measures, and use Group Relative Policy Optimization with a KL-divergence penalty for training.\n\nYou can find more details about the paper on [ResearchGate](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization) and the [MAR 2025 Workshop website](https://marworkshop.github.io/neurips25/)."
    ],
    "durationSeconds": 5.240729772000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bbdb37f6-2d37-4eec-98d5-c1a95c179eae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "18137df2-20f9-4d55-921c-390f3e668976",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Tool call

_source line 38 · 2026-05-27T20:37:39.518Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DruXfTnLtU5JvZ2avZr1Ti`</summary>

```json
{
  "url": "https://marworkshop.github.io/neurips25/",
  "prompt": "Look for the accepted papers list. Is \"Online Reinforcement Learning for Autoformalization\" by Sorg, Li, Banerjee listed as an accepted paper? List any autoformalization-related papers you find. What is the full name of this workshop?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18137df2-20f9-4d55-921c-390f3e668976",
  "isSidechain": false,
  "requestId": "req_011CbTiXZhDHyaYup5TTYa1Z",
  "type": "assistant",
  "uuid": "251d1d6c-3396-4d13-9d04-1cea8b614543",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGM4aTTjkoQJjCXaRdg61x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 25019,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 25019,
          "cache_creation_input_tokens": 650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 650
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

_source line 39 · 2026-05-27T20:37:42.428Z_

<details><summary>↩ Tool result · `toolu_01DruXfTnLtU5JvZ2avZr1Ti`</summary>

```text
# MAR 2025 Workshop Response

**Full Workshop Name:** "Multimodal Algorithmic Reasoning" (MAR) in conjunction with the Conference on Neural Information Processing Systems 2025

**Autoformalization Paper Found:** Yes, "Online Reinforcement Learning for Autoformalization" by Sorg, Li, and Banerjee is listed as an accepted paper [12] in the poster papers section.

**Autoformalization-Related Papers:** Based on the accepted papers list provided, only one paper explicitly addresses autoformalization. The workshop's broader focus encompasses algorithmic reasoning across multiple modalities, though autoformalization represents one specific research direction represented in the accepted submissions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "251d1d6c-3396-4d13-9d04-1cea8b614543",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "77b28f4f-9fcd-4ce8-9001-715a0eafd1b0",
  "toolUseResult": {
    "bytes": 105474,
    "code": 200,
    "codeText": "OK",
    "result": "# MAR 2025 Workshop Response\n\n**Full Workshop Name:** \"Multimodal Algorithmic Reasoning\" (MAR) in conjunction with the Conference on Neural Information Processing Systems 2025\n\n**Autoformalization Paper Found:** Yes, \"Online Reinforcement Learning for Autoformalization\" by Sorg, Li, and Banerjee is listed as an accepted paper [12] in the poster papers section.\n\n**Autoformalization-Related Papers:** Based on the accepted papers list provided, only one paper explicitly addresses autoformalization. The workshop's broader focus encompasses algorithmic reasoning across multiple modalities, though autoformalization represents one specific research direction represented in the accepted submissions.",
    "durationMs": 2905,
    "url": "https://marworkshop.github.io/neurips25/"
  },
  "sourceToolAssistantUUID": "251d1d6c-3396-4d13-9d04-1cea8b614543",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-27T20:37:45.217Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DrHYeUr7icy1Ux8CxUd2m3`</summary>

```json
{
  "url": "https://mathai2025.github.io/papers/",
  "prompt": "Is \"Online Reinforcement Learning for Autoformalization\" listed as an accepted paper here? List all autoformalization-related papers from this workshop."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77b28f4f-9fcd-4ce8-9001-715a0eafd1b0",
  "isSidechain": false,
  "requestId": "req_011CbTiY3dEPQ5cNnL73dxgP",
  "type": "assistant",
  "uuid": "48239a64-138d-48a2-bd70-0bdb575313e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHRFuMjMZmmT8CzMAncLDt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 299,
      "cache_read_input_tokens": 25669,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 299,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 25669,
          "cache_creation_input_tokens": 299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 299
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

_source line 41 · 2026-05-27T20:37:47.861Z_

<details><summary>↩ Tool result · `toolu_01DrHYeUr7icy1Ux8CxUd2m3`</summary>

```text
# Autoformalization Papers at MATH-AI Workshop

"Online Reinforcement Learning for Autoformalization" is **not** listed among the 153 accepted papers.

However, the following autoformalization-related papers are included:

1. **"Improving autoformalization via cycle consistency and incremental type-checking..."** (Paper #76) - Focuses on enhancing the autoformalization process through cycle consistency and type-checking methods.

2. **"Babel-formal: Translation of Proofs between Lean and Rocq"** (Paper #96) - Addresses formal proof translation between different proof assistants, related to formalization workflows.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48239a64-138d-48a2-bd70-0bdb575313e3",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "ec488850-027d-47d0-8f83-fb2d498a2d38",
  "toolUseResult": {
    "bytes": 28003,
    "code": 200,
    "codeText": "OK",
    "result": "# Autoformalization Papers at MATH-AI Workshop\n\n\"Online Reinforcement Learning for Autoformalization\" is **not** listed among the 153 accepted papers.\n\nHowever, the following autoformalization-related papers are included:\n\n1. **\"Improving autoformalization via cycle consistency and incremental type-checking...\"** (Paper #76) - Focuses on enhancing the autoformalization process through cycle consistency and type-checking methods.\n\n2. **\"Babel-formal: Translation of Proofs between Lean and Rocq\"** (Paper #96) - Addresses formal proof translation between different proof assistants, related to formalization workflows.",
    "durationMs": 2641,
    "url": "https://mathai2025.github.io/papers/"
  },
  "sourceToolAssistantUUID": "48239a64-138d-48a2-bd70-0bdb575313e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-27T20:37:51.408Z_

Good, venue confirmed. Now let me get more details on CriticLean and search for additional context on elevating the contribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec488850-027d-47d0-8f83-fb2d498a2d38",
  "isSidechain": false,
  "requestId": "req_011CbTiYT4t2LigwAdHbGdvm",
  "type": "assistant",
  "uuid": "69088e8a-a281-43be-a515-24658bd6d860",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELG6GAJcPbnEPC3huHsGA6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 25968,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 267,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 25968,
          "cache_creation_input_tokens": 267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 267
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

_source line 43 · 2026-05-27T20:37:51.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PDkDaKAgKYcmkKjArDHshu`</summary>

```json
{
  "query": "CriticLean CriticLeanGPT RL training reward critic autoformalization Lean 4 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69088e8a-a281-43be-a515-24658bd6d860",
  "isSidechain": false,
  "requestId": "req_011CbTiYT4t2LigwAdHbGdvm",
  "type": "assistant",
  "uuid": "da617e33-1593-4ae2-965f-ed937838c640",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELG6GAJcPbnEPC3huHsGA6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 25968,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 267,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 25968,
          "cache_creation_input_tokens": 267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 267
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

_source line 44 · 2026-05-27T20:37:58.482Z_

<details><summary>↩ Tool result · `toolu_01PDkDaKAgKYcmkKjArDHshu`</summary>

```text
Web search results for query: "CriticLean CriticLeanGPT RL training reward critic autoformalization Lean 4 results"

Links: [{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"},{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"M-A-P CriticLean: Critic-Guided Reinforcement Learning for","url":"https://arxiv.org/pdf/2507.06181"},{"title":"GitHub - multimodal-art-projection/CriticLean · GitHub","url":"https://github.com/multimodal-art-projection/CriticLean"},{"title":"FormaRL: RL-Driven Autoformalization for Lean 4","url":"https://www.emergentmind.com/topics/formarl"},{"title":"Paper page - CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://huggingface.co/papers/2507.06181"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"},{"title":"m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face","url":"https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"}]

Based on the search results, here's what I found about CriticLean and CriticLeanGPT:

## Overview

CriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. While prior work has focused on generation and compilation success, little attention has been paid to the critic phase—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem.

## Key Components

CriticLean places the critic at the center of the formalization pipeline, creating a feedback loop that drives iterative refinement of the generated Lean 4 code. The framework includes three main elements:

1. **CriticLeanGPT**: Trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations.

2. **CriticLeanBench**: A benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations, demonstrating that the trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines.

3. **FineLeanCorpus**: A dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.

## Results

CriticLeanGPT models, particularly the Qwen3-32B-RL variant, can achieve 87.0% accuracy compared to GPT-4o's 67.8%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da617e33-1593-4ae2-965f-ed937838c640",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "0b154d49-b645-4ce4-a2e2-169884fd5e29",
  "toolUseResult": {
    "query": "CriticLean CriticLeanGPT RL training reward critic autoformalization Lean 4 results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RUesTKrndiGSSBTF5Vh8oX",
        "content": [
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
          },
          {
            "title": "(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"
          },
          {
            "title": "[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181"
          },
          {
            "title": "[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181v1"
          },
          {
            "title": "M-A-P CriticLean: Critic-Guided Reinforcement Learning for",
            "url": "https://arxiv.org/pdf/2507.06181"
          },
          {
            "title": "GitHub - multimodal-art-projection/CriticLean · GitHub",
            "url": "https://github.com/multimodal-art-projection/CriticLean"
          },
          {
            "title": "FormaRL: RL-Driven Autoformalization for Lean 4",
            "url": "https://www.emergentmind.com/topics/formarl"
          },
          {
            "title": "Paper page - CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://huggingface.co/papers/2507.06181"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project",
            "url": "https://arxiv.org/html/2603.24372"
          },
          {
            "title": "m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face",
            "url": "https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"
          }
        ]
      },
      "Based on the search results, here's what I found about CriticLean and CriticLeanGPT:\n\n## Overview\n\nCriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. While prior work has focused on generation and compilation success, little attention has been paid to the critic phase—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem.\n\n## Key Components\n\nCriticLean places the critic at the center of the formalization pipeline, creating a feedback loop that drives iterative refinement of the generated Lean 4 code. The framework includes three main elements:\n\n1. **CriticLeanGPT**: Trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations.\n\n2. **CriticLeanBench**: A benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations, demonstrating that the trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines.\n\n3. **FineLeanCorpus**: A dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.\n\n## Results\n\nCriticLeanGPT models, particularly the Qwen3-32B-RL variant, can achieve 87.0% accuracy compared to GPT-4o's 67.8%."
    ],
    "durationSeconds": 6.905119352000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "da617e33-1593-4ae2-965f-ed937838c640",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-27T20:38:04.285Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XGTdhfYvxkNcSZ1p8oxaWx`</summary>

```json
{
  "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization",
  "prompt": "Extract ALL details: (1) The exact RL algorithm used (GRPO, PPO, etc.). (2) What reward signals are used for training the critic? (3) What reward signals are used for training the formalizer? (4) How does the critic assess semantic fidelity - what specific features does it look at? (5) Performance numbers on standard benchmarks (ProofNet, FormalMATH). (6) Base models used. (7) How the framework compares to FormaRL. (8) The training pipeline - SFT then RL? (9) How FineLeanCorpus is constructed. (10) Is the critic used AS a reward signal for RL training of the formalizer, or is it separate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b154d49-b645-4ce4-a2e2-169884fd5e29",
  "isSidechain": false,
  "requestId": "req_011CbTiZEHxdNyLw5VumNz5c",
  "type": "assistant",
  "uuid": "a0f507f5-52e7-4cf6-accd-1f1241db6a18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSLQGwFyCqAps25rEACaBf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 26235,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 26235,
          "cache_creation_input_tokens": 1052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1052
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

_source line 46 · 2026-05-27T20:38:04.525Z_

<details><summary>↩ Tool result · `toolu_01XGTdhfYvxkNcSZ1p8oxaWx`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0f507f5-52e7-4cf6-accd-1f1241db6a18",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "6d58202f-d16d-425c-a921-7f14e0bc8ea1",
  "toolUseResult": {
    "bytes": 0,
    "code": 403,
    "codeText": "Forbidden",
    "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 235,
    "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
  },
  "sourceToolAssistantUUID": "a0f507f5-52e7-4cf6-accd-1f1241db6a18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-27T20:38:09.565Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01458crqqoPDiG37SZMdawCY`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2507.06181",
  "prompt": "Extract ALL details about CriticLean: (1) The exact RL algorithm used (GRPO, PPO, etc.) for training both critic and formalizer. (2) What reward signals are used for the critic training? (3) What reward signals are used for the formalizer training? (4) How exactly does CriticLeanGPT assess semantic fidelity? (5) Performance numbers on ProofNet, FormalMATH, or any standard benchmarks. (6) Base models used. (7) How does it compare to FormaRL quantitatively? (8) Is the critic used AS a reward signal for the formalizer RL? (9) How is FineLeanCorpus constructed - sources and methodology? (10) CriticLeanBench details - size, how it distinguishes correct from incorrect formalizations. (11) Any results on gaming or unfaithfulness detection."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d58202f-d16d-425c-a921-7f14e0bc8ea1",
  "isSidechain": false,
  "requestId": "req_011CbTiZg6zEQyNdDxG9E3Wm",
  "type": "assistant",
  "uuid": "3055e587-6ba6-463f-a415-ff583b030f7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrxtAWnGUPTjBYpA92eJde",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 27287,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 27287,
          "cache_creation_input_tokens": 332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 332
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

_source line 48 · 2026-05-27T20:38:15.358Z_

<details><summary>↩ Tool result · `toolu_01458crqqoPDiG37SZMdawCY`</summary>

```text
# CriticLean: Key Technical Details

## 1. RL Algorithm
The document uses **GRPO (Group Relative Policy Optimization)** for training both the critic and formalizer models, though specific implementation details are embedded in the PDF structure rather than clearly extracted text.

## 2. Critic Training Reward Signals
Based on the metadata and structure, the critic is trained to assess semantic fidelity of formal proofs. The exact reward formulation isn't explicitly stated in the readable portions, but it appears to evaluate whether formal statements accurately capture informal mathematical content.

## 3. Formalizer Training Reward Signals
The formalizer receives rewards from the critic's assessment, creating a reinforcement learning loop where the critic guides formalization quality.

## 4. Semantic Fidelity Assessment
CriticLean's approach evaluates whether formal Lean proofs preserve the mathematical meaning of informal statements. However, the specific technical mechanism isn't fully clear from the extracted content.

## 5. Benchmark Performance
Performance metrics on ProofNet, FormalMATH, and other standard benchmarks are referenced but not extractable from this PDF excerpt due to content compression.

## 6. Base Models
The paper mentions using models like **Qwen, Llama, and Gemini**, though specific version selections aren't clearly detailed in accessible text.

## 7. FormaRL Comparison
Comparative quantitative results against FormaRL aren't clearly visible in the extracted portions.

## 8. Critic as Reward Signal
Yes, the architecture explicitly uses the critic's assessment as a reward signal for formalizer RL training.

## 9. FineLeanCorpus Construction
Details on corpus sources and methodology are not clearly accessible in the readable text.

## 10. CriticLeanBench Details
Size and discrimination methodology between correct/incorrect formalizations are not extractable.

## 11. Gaming/Unfaithfulness Detection
No results on these topics are visible in the accessible content.

[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/webfetch-1779914289771-cjyx1i.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3055e587-6ba6-463f-a415-ff583b030f7d",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "d9828132-c457-4970-9d2c-0070631847e7",
  "toolUseResult": {
    "bytes": 1139392,
    "code": 200,
    "codeText": "OK",
    "result": "# CriticLean: Key Technical Details\n\n## 1. RL Algorithm\nThe document uses **GRPO (Group Relative Policy Optimization)** for training both the critic and formalizer models, though specific implementation details are embedded in the PDF structure rather than clearly extracted text.\n\n## 2. Critic Training Reward Signals\nBased on the metadata and structure, the critic is trained to assess semantic fidelity of formal proofs. The exact reward formulation isn't explicitly stated in the readable portions, but it appears to evaluate whether formal statements accurately capture informal mathematical content.\n\n## 3. Formalizer Training Reward Signals\nThe formalizer receives rewards from the critic's assessment, creating a reinforcement learning loop where the critic guides formalization quality.\n\n## 4. Semantic Fidelity Assessment\nCriticLean's approach evaluates whether formal Lean proofs preserve the mathematical meaning of informal statements. However, the specific technical mechanism isn't fully clear from the extracted content.\n\n## 5. Benchmark Performance\nPerformance metrics on ProofNet, FormalMATH, and other standard benchmarks are referenced but not extractable from this PDF excerpt due to content compression.\n\n## 6. Base Models\nThe paper mentions using models like **Qwen, Llama, and Gemini**, though specific version selections aren't clearly detailed in accessible text.\n\n## 7. FormaRL Comparison\nComparative quantitative results against FormaRL aren't clearly visible in the extracted portions.\n\n## 8. Critic as Reward Signal\nYes, the architecture explicitly uses the critic's assessment as a reward signal for formalizer RL training.\n\n## 9. FineLeanCorpus Construction\nDetails on corpus sources and methodology are not clearly accessible in the readable text.\n\n## 10. CriticLeanBench Details\nSize and discrimination methodology between correct/incorrect formalizations are not extractable.\n\n## 11. Gaming/Unfaithfulness Detection\nNo results on these topics are visible in the accessible content.\n\n[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/webfetch-1779914289771-cjyx1i.pdf]",
    "durationMs": 5790,
    "url": "https://arxiv.org/pdf/2507.06181"
  },
  "sourceToolAssistantUUID": "3055e587-6ba6-463f-a415-ff583b030f7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-27T20:38:18.807Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017tNQR36VFz5t8HzkqpKgwp`</summary>

```json
{
  "url": "https://huggingface.co/papers/2507.06181",
  "prompt": "Extract ALL details about CriticLean paper: (1) Full abstract. (2) Any discussion of methods, results, base models. (3) How CriticLeanGPT works as a reward signal. (4) Performance numbers. (5) Comparison to FormaRL or other baselines. (6) Authors list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9828132-c457-4970-9d2c-0070631847e7",
  "isSidechain": false,
  "requestId": "req_011CbTiaURYRXs5ediSiS42S",
  "type": "assistant",
  "uuid": "8a29b349-c5b3-4c16-aaf2-963fa1b7f760",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Erxp4BqumowGT5XKk8SM2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 830,
      "cache_read_input_tokens": 27619,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 27619,
          "cache_creation_input_tokens": 830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 830
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

_source line 50 · 2026-05-27T20:38:19.624Z_

<details><summary>↩ Tool result · `toolu_017tNQR36VFz5t8HzkqpKgwp`</summary>

```text
&lt;persisted-output>
Output too large (91.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/toolu_017tNQR36VFz5t8HzkqpKgwp.txt

Preview (first 2KB):
# CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization

ByteDance Seed      Nanjing University

Full author list in Contributions

## Abstract

Translating natural language mathematical statements into formal, executable code is a fundamental challenge in automated theorem proving. While prior work has focused on generation and compilation success, little attention has been paid to the *critic phase*—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. In this paper, we introduce **CriticLean**, a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. Specifically, first, we propose the **CriticLeanGPT**, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Then, we introduce **CriticLeanBench**, a benchmark designed to measure models’ ability to distinguish semantically correct from incorrect formalizations, and demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines. Building on the CriticLean framework, we construct **FineLeanCorpus**, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation. Overall, our findings highlight that optimizing the critic phase is essential for producing reliable formalizations and we hope our CriticLean will provide valuable insights for future advances in formal mathematical reasoning.

**Date:** July 8, 2025

**Correspondence:** [liujiaheng@nju.edu.cn](mailto:liujiaheng@nju.edu.cn), [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)

**Project Page:** &lt;https://github.com/multimodal-art-projection/CriticLean>

## 1 Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a29b349-c5b3-4c16-aaf2-963fa1b7f760",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "d9760f0e-cdd3-49c3-afc4-3b610196c8de",
  "toolUseResult": {
    "bytes": 93671,
    "code": 200,
    "codeText": "OK",
    "result": "# CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization\n\nByteDance Seed      Nanjing University\n\nFull author list in Contributions\n\n## Abstract\n\nTranslating natural language mathematical statements into formal, executable code is a fundamental challenge in automated theorem proving. While prior work has focused on generation and compilation success, little attention has been paid to the *critic phase*—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. In this paper, we introduce **CriticLean**, a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. Specifically, first, we propose the **CriticLeanGPT**, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Then, we introduce **CriticLeanBench**, a benchmark designed to measure models’ ability to distinguish semantically correct from incorrect formalizations, and demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines. Building on the CriticLean framework, we construct **FineLeanCorpus**, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation. Overall, our findings highlight that optimizing the critic phase is essential for producing reliable formalizations and we hope our CriticLean will provide valuable insights for future advances in formal mathematical reasoning.\n\n**Date:** July 8, 2025\n\n**Correspondence:** [liujiaheng@nju.edu.cn](mailto:liujiaheng@nju.edu.cn), [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)\n\n**Project Page:** &lt;https://github.com/multimodal-art-projection/CriticLean>\n\n## 1 Introduction\n\nThe formalization of mathematical statements [64] is a critical task in modern mathematical computation, particularly in the context of theorem provers like Lean 4 [22]. The translation of natural language mathematical problems into formal, executable code remains a significant challenge, as it requires not only syntactical accuracy but also a deep understanding of the problem’s semantics [44, 49]. Existing approaches have shown progress, but they often face limitations in accuracy, especially in the context of complex, high-level problems that involve sophisticated mathematical reasoning [3, 23, 58, 59, 75]. In contrast to existing works, we argue that the *critic* phase—the step where the semantic correctness of generated formalizations is evaluated—is not only underexplored but also fundamentally essential to the success of mathematical autoformalization.\n\nTherefore, in this paper, we systematically investigate and optimize the critic component and introduce **CriticLean**, a comprehensive framework that places the critic model at the center of the formalization pipeline. Unlike prior work that primarily focuses on generation quality or compiler validity, CriticLean introduces the reinforcement learning-based **CriticLeanGPT** models explicitly trained to evaluate whether the Lean 4 output truly reflects the intent of the original mathematical statement., and we present a full methodology forThe diagram illustrates the CriticLean framework for mathematics autoformalization. It starts with a **Natural Language Statement** box containing a mathematical problem about permutations. This statement is processed by an **AutoFormalizer**. The AutoFormalizer's output is then evaluated by two verification steps: a **Verify** box for syntax checking and name resolution, and another **Verify** box for semantic meaning and logical consistency. The **Verify** boxes are supported by a **Lean Compiler** and **CriticLeanGPT** respectively. If a **Compilation Error** or **Critique Error** occurs, the AutoFormalizer receives feedback and iterates. If successful, the final output is a **Lean Formal Language Statement** box showing the formalized theorem.\n\n**Figure 1** Illustration of CriticLean framework based on Critic-Guided Reinforcement Learning for Mathematics Autoformalization.\n\ntraining, and evaluating CriticLeanGPT model. Specifically, as shown in Figure 1, for each natural language statement, we apply the autoformalization iteratively based on the feedback from the Lean compiler and the CriticLeanGPT models, which is trained to critically assess whether a generated formalization accurately represents the semantics of the original mathematical statement. In each iteration, the feedback provides valuable signals that drive an iterative refinement process, further improving the quality of the final Lean code output.\n\nAdditionally, we present **CriticLeanBench**, a benchmark designed to evaluate the performance of CriticLeanGPT models, which contain 500 natural language and Lean 4 language statement pairs (i.e., 250 correct and 250 incorrect pairs). Through extensive experiments, we demonstrate that our trained CriticLeanGPT models outperform the SOTA open-source models [4, 10, 11] and many closed-source API models [9, 12, 42] greatly.\n\nFurthermore, building upon our critic-centric CriticLean pipeline, we propose the high-quality open-source Lean 4 statement dataset **FineLeanCorpus**, comprising 285,957 fully verified entries. When compared to the previous related datasets (e.g., LeanWorkBook [65]), FineLeanCorpus is distinguished by its diversity in mathematical domains, difficulty distribution, and strict semantic validation via critical feedback loops. Notably, its difficulty distribution and targeted domain enrichment create a more structurally balanced training environment, mitigating overfitting and transforming sparse topics into well-supported sub-domains. Furthermore, to foster research into the upper echelons of mathematical reasoning, we have curated the specialized subset called FineLeanCorpus-Diamond, comprising over 36,000 high-difficulty problems.\n\n## 2 Related Works\n\n### 2.1 Autoformalization\n\nAutoformalization [48, 60, 68] refers to the process by which AI systems parse natural language (NL) contents and translate them into machine-verifiable formal representations, such as those in theorem provers like Lean4 [38] or Isabelle [40]. Recent advances leverage large language models (LLMs) [72] to tackle this problem through two primary paradigms: (1) In-context learning [57], where models utilize annotated examples [28, 33, 60] to generate formalizations without explicit fine-tuning, (2) Supervised fine-tuning (e.g., [26, 61, 67]), which adapts general-purpose LLMs into domain-specific autoformalization experts. To assess correctness, prior works [26, 61, 67] employ LLM-as-judge [76] to verify semantic alignment between formal and informal statements. We advance this by training the first open-sourced, domain-specific light LLM on top of Qwen [52] family for critiquing Lean4 statement alignment via reinforcement learning [46], enhancingboth critique capability and formalization robustness.\n\n## 2.2 RL for LLM Reasoning\n\nThe exploration of complex reasoning capabilities in Large Language Models (LLMs) has achieved significant advancements [14, 17, 29–31, 55], with Reinforcement Learning (RL) establishing itself as a critical paradigm for transcending the constraints inherent to Supervised Fine-Tuning (SFT) [29, 32, 56, 66, 70]. Notable methodologies, including GRPO [11, 46], DAPO [66] have demonstrated substantial gains in mathematical reasoning and intricate problem-solving domains. However, the underlying mechanisms by which RL enhances reasoning capabilities remain insufficiently characterized. Empirical analyses increasingly indicate that RL primarily functions to activate, refine, or optimize the sampling of latent reasoning competencies rather than generating entirely novel cognitive frameworks de novo. For example, Yue et al. [69] interrogate whether current reinforcement learning frameworks incorporating verifiable rewards (RLVR) genuinely expand the frontier of reasoning performance or merely enhance the efficiency of retrieving pre-existing solutions.\n\n## 3 CriticLeanGPT\n\n### 3.1 CriticLeanBench\n\n#### 3.1.1 Overview of CriticLeanBench\n\nCriticLeanBench aims to evaluate the critical reasoning of LLMs in key aspects such as translating natural language mathematical statements into formally verified theorem declarations in Lean 4, including critique and correction. By integrating these core dimensions, CriticLeanBench can comprehensively measure the performance of models in Formalization tasks. In this section, we will elaborate on the construction principles and processes of CriticLeanBench; the construction process is shown in Figure 2.\n\nCriticLeanBench is constructed following the following principles: (1) It covers various types of errors, aiming to thoroughly evaluate the comprehensive capabilities of LLMs in capturing the semantic intent of formalized statements, using Template G for systematic assessment; (2) It incorporates diverse data sources to enhance the diversity and representativeness of evaluation data; and (3) It ensures the reliability and validity of the evaluation benchmark through a combination of expert review and automated verification.\n\n#### 3.1.2 Automatically verified\n\nThis section outlines the methodology employed to apply the Automatic Validation Filter, guided by predefined criteria for compiler and model-based verification.\n\n**Data Collection** We selected Math Statements from data sources [1, 16, 24, 36, 41, 43, 66], such as Omni-MATH [8], AIME [75], U-MATH [5], DEMI-MathAnalysis [6], HARDMath [7], OlympiadBench [13], and BlueMO [73], along with their corresponding Lean 4 Statements from public dataset [67].\n\n**Compiler Verified** We submitted the Lean 4 statements from the above dataset to the Lean 4 compiler. If the compilation succeeded, the results were passed to the DeepSeek R1 [11] model for further processing.\n\n- • **Compile false:** For statements that failed to compile, we randomly sampled 50 entries and retained the compiler feedback messages, which were included as part of our CriticLeanBench benchmark.\n\n**LLM Verified** For the data that has passed compilation, we utilize a template G to process each sample’s Math Statement and its corresponding Lean 4 Code Statement through the DeepSeek R1 large language model. The model is tasked with determining whether the Lean 4 Code Statement is consistent with the Math Statement, producing for each sample a tag indicating consistency or inconsistency along with a reasoning statement. To extract structured outputs from the model’s responses, we employ regular expression-based pattern matching. The results are then submitted to human reviewers for further validation.**Figure 2** An overview for the CriticLeanBench construction.\n\n### 3.1.3 Human Validation Filter\n\nThis section outlines the methodology employed to apply the Human Validation Filter, guided by predefined criteria (detailed in Appendix C).\n\nWe categorize the data into two groups based on whether the **Lean-compiled** autoformalization output semantically aligns with the refined statement. Therefore, a Lean-compiled autoformalization falls into the following:\n\n- • **Human Check right:** If the autoformalized statement both compiles and accurately captures the mathematical meaning, logic, and intended behavior of the original problem, it satisfies the semantic consistency criteria.\n- • **Human Check false:** If the autoformalized statement compiles but fails to accurately represent the original mathematical problem’s semantics. It violates one or more of the semantic consistency criteria, despite being syntactically valid Lean code. This often happens when there’s a mismatch between the code’s logic and the intended mathematical meaning.\n\nWithin the two categories, we select representative samples that mirror the characteristics of the original autoformalization statements while maximizing diversity within each subset and capturing the full spectrum of observed error types in the negative samples. This is achieved by balancing several factors:\n\n**Stratified Representation:** The selected samples should maintain a similar distribution across different strata of the original dataset. These strata are defined by:\n\n- • **Problem Complexity:** This encompasses factors like the number of variables, quantifiers, logical connectives, and the depth of nested mathematical structures.\n- • **Mathematical Branches:** The samples should represent the various mathematical domains present in the original data.\n- • **Statement Well-Formedness:** This refers to the degree to which the original mathematical statementsadhere to standard mathematical notation and conventions. This stratification ensures that the subsets reflect the variability in the quality of the original problem statements.\n\n**Comprehensive Error Coverage:** The negative samples are specifically chosen to exemplify the full range of typical errors observed in the autoformalization process. This range includes fundamental semantic and logical issues, such as Premise Translation Errors (e.g., incorrect domains or missing conditions), Mathematical Representation Errors (e.g., faulty expressions or definitions), and Goal Translation Errors. The set also covers issues such as Incorrect Assumptions, logical flaws like Operator & Parenthesis Errors (e.g., misplaced quantifiers), and high-level structural problems like Incomplete Formalization, where crucial context is omitted (detailed in figure 9).\n\n### 3.1.4 Data Statistics\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Statistics&lt;/th>\n&lt;th>Number&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;b>#Problems&lt;/b>&lt;/td>\n&lt;td>500&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Correct Pairs&lt;/b>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>human check&lt;/i>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Incorrect Pairs&lt;/b>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>human/compiler check&lt;/i>&lt;/td>\n&lt;td>200/50&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Question Tokens Length&lt;/b>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>max/min/avg&lt;/i>&lt;/td>\n&lt;td>1,583/495/700.94&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Critic&lt;/th>\n&lt;th>Lean&lt;/th>\n&lt;th>Test&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>CriticBench&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>CodeCriticBench&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>LLaVA-Critic&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>CriticLeanBench (ours)&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 1** Dataset statistics and comparison of various code benchmark datasets.\n\nTable 1 (left) presents the dataset statistics for CriticLeanBench. The dataset contains a total of 500 problems, comprising 250 correct and 250 incorrect Q/GT (Question and GT label) pairs distributed across the collection. The questions exhibit a notable variation in length, with a maximum token count of 1,583 and a minimum of 495 tokens, calculated using the Qwen2.5 [4] tokenizer. On average, each question contains approximately 700.94 tokens. This characteristic distinguishes CriticLeanBench as a complex evaluation benchmark that requires models to process relatively lengthy inputs compared to those in standard datasets.\n\n### 3.1.5 Comparison to Other Benchmarks\n\nIn Table 1 (right), CriticLeanBench has the following features: (1) We focus on a modest data size of 500 samples, acknowledging the expensive manual annotation costs (ranging from tens to hundreds of dollars per instance) and prioritizing efficiency without compromising evaluation rigor; (2) We integrate both Critic and Lean functionalities, distinguishing ourselves from benchmarks like CriticBench [27] and CodeCriticBench [71] that lack Lean capabilities, and LLaVA-Critic [63] that omits both Lean capabilities and test evaluation components; (3) We incorporate a test component focused on translating mathematical statements into formally verified theorem declarations in Lean 4, offering a fine-grained evaluation framework to assess the correctness of model transformations. This aspect of evaluative completeness remains unmatched by existing datasets.\n\n## 4 CriticLeanInstruct\n\nTo enhance the CriticLeanGPT model’s efficacy in critically evaluating the successful transformation of mathematical statements into Lean code, we construct a comprehensive training dataset comprising 48,000 samples. This dataset consists of three high-quality components, designed to comprehensively improve the model’s critical thinking and reasoning capabilities.\n\nTo significantly broaden the CriticLeanGPT model’s knowledge coverage, we also integrates three times additional code and math [18] datasets, enabling it to more comprehensively understand mathematical concepts and Lean code structures.Specifically, the Seed Data, with a 1:3 mix of math and code, is termed **CriticLeanInstruct(16K)**. When combined with data augmentation while retaining the same ratio, it forms the full **CriticLeanInstruct** dataset.\n\n## 4.1 Seed Data\n\nThe seed data comprises 4,000 samples evenly split into 2,000 correct and 2,000 incorrect instances. For both correct and incorrect samples, human experts provided critical feedback [F](#). Additionally, the incorrect samples include compiler error messages generated by the Lean 4 Compiler as supplementary feedback. Then, we adopt the Gemini2.5-Pro [\\[9\\]](#) to extend the critical feedback to detailed Chain-of-Thought (CoT) explanations.\n\n**Figure 3** Distribution of Different Error Types.\n\nTo understand the primary failure modes, we analyzed the error distribution across the 2,000 incorrect samples in our seed data as illustrated in Figure 3. The analysis reveals two primary challenges: (1) Syntactic Barriers: The most frequent obstacles are syntactic, such as Type Error and Syntax Errors. These issues typically prevent the code from compiling, indicating a fundamental difficulty in mastering the formal language. (2) Semantic Gaps: Beyond syntax, these errors stem from a failure to interpret the natural language scenario and accurately model its key information. This is evident in high rates of errors when translating a problem’s core logical components—including its premises, goal, and mathematical representation. This semantic challenge is particularly acute in application-style \"word problems,\" where difficulty comprehending complex contexts leads to a fundamentally flawed formalization.\n\nDrawing from the error taxonomy (detailed in Appendix D) and building upon our initial annotation standards (detailed in Appendix C), we established a fine-grained checklist, which is provided in full in Appendix E. This checklist formalizes the observed error paradigms, providing the foundational framework for methodically constructing the negative samples used throughout our study.\n\n## 4.2 Data Augmentation\n\n### 4.2.1 Correct Samples\n\nWe selected **5560** correct mathematical statements and Lean code pairs from the FormalMATH [\\[67\\]](#) dataset and used the Gemini-2.5-Pro model to generate Critical Chain-of-Thought for initial assessment. To ensure data quality, we kept these samples where the model’s judgment is “correct.”## 4.2.2 Incorrect Samples\n\nWe provide two strategies to obtain the incorrect samples as follows:\n\n- • Based on OmniMath, we adopt the Kimina-Autoformalizer-7B [54] to generate the Lean 4 code statements, and we kept 2,000 Lean code snippets that failed to compile due to syntactic or logical issues during automated formalization processes. For each detected error, a detailed Chain-of-Thought (CoT) explanation was generated to elucidate the error’s cause, enabling the model to recognize common compilation error patterns and thereby enhance its understanding of Lean 4 code syntax.\n- • Based on correct mathematical statements and Lean 4 code from the FormalMATH [67] dataset, we implemented a three-step collaborative process to generate negative samples, aiming to enhance the CriticLeanGPT model’s ability to identify subtle errors and logical flaws. First, a checklist of various potential issues, refined by human experts, was established as shown in Appendix E. Second, the Gemini 2.5 Pro model was invoked to randomly select error types from this checklist and modify correct Lean code accordingly, generating incorrect samples (detailed in Appendix H). Then, we adopt the Gemini model to generate the critical Chain-of-Thought explanation.\n\n## 4.3 Training Paradigm\n\n*Supervised fine-tuning (SFT).* These models are instruction-tuned versions based on their respective pre-trained Qwen2.5 checkpoints, with a focus on improving their ability to interpret and formalize complex mathematical statements expressed in natural language. The CriticLeanInstruct 4 dataset includes Critic data consisting of mathematical statements converted into formally verified theorem declarations in Lean 4, along with three times as much code and mathematics data for SFT (Supervised Fine-Tuning). We used the LLaMA-Factory [77] framework to facilitate the fine-tuning process and optimize model performance.\n\n*Reinforcement Learning Optimization (RL).* The recent success of R1-style methods has demonstrated the effectiveness of online RL using discrete, rule-based rewards [45]. In our pipeline, Qwen2.5 series and Qwen3 [52] series are further refined using reinforcement learning signals derived from both format validation of the generated critic data and consistency checking between model predictions and expert-labeled ground truth (GT) labels. Specifically, the RL training data consists of 4,000 Seed Data 4.1, where each example transforms a mathematical statement into a corresponding formal proof in Lean 4. Based on this dataset, we apply a rule-based RL approach to optimize the model’s capability in judgment reasoning. More specifically, we mainly utilize the GRPO [46] algorithm within the VeRL [47] reinforcement learning framework, whose optimization objective is:\n\n$$J_{\\text{online}}(\\pi_{\\theta}; \\mathcal{D}) = \\mathbb{E}_{x \\sim \\mathcal{D}, \\{y_i\\}_{i=1}^G \\sim \\pi_{\\theta_{\\text{old}}}(y|x)} \\left[ \\frac{1}{G} \\sum_{i=1}^G \\min \\left( \\frac{\\pi_{\\theta}(y_i|x)}{\\pi_{\\theta_{\\text{old}}}(y_i|x)} A_i, \\text{clip} \\left( \\frac{\\pi_{\\theta}(y_i|x)}{\\pi_{\\theta_{\\text{old}}}(y_i|x)}, 1 - \\epsilon, 1 + \\epsilon \\right) A_i \\right) - \\beta D_{\\text{KL}}(\\pi_{\\theta} || \\pi_{\\text{ref}}) \\right] \\quad (1)$$\n\nwhere  $G$  is group size, and  $A_i$  is advantage. The reward function is designed as follows&lt;sup>1&lt;/sup>:\n\n$$r_{\\text{accuracy}} = \\begin{cases} 1, & \\text{if judgement} = \\text{label} \\\\ 0, & \\text{if judgement} \\neq \\text{label} \\end{cases} \\quad (2)$$\n\n$$r_{\\text{format}} = \\begin{cases} 1, & \\text{if format is right} \\\\ 0, & \\text{if format is wrong} \\end{cases} \\quad (3)$$\n\n$$r_{\\text{final}} = \\min(r_{\\text{accuracy}}, r_{\\text{format}}) \\quad (4)$$\n\n\n---\n\n&lt;sup>1&lt;/sup>We do not include a length penalty in rewards to encourage longer thinking.## 5 Experiments\n\n### 5.1 Experimental Setup\n\n**Baseline Models.** For the closed-sourced API models, we select the following models: Claude35\\_Sonnet2 [2], Doubao-1.5-pro-32k [12], Gemini 2.5 Pro [50], GPT-4o-2024-11-20 [42]. We select a group of the most advanced open-source LLMs to serve as critic models for evaluation, which includes various reasoning models (DeepSeek-R1 [11], QwQ-32B [53], Qwen3-8B [52], Qwen3-14B [52], Qwen3-32B [52]), DeepSeek-Prover models [62] (DeepSeek-Prover-V1.5-RL, DeepSeek-Prover-V1.5-SFT), Llama-3.3-70B-Instruct [10] and several Qwen models (Qwen2.5-Coder-7B-Instruct [19], Qwen2.5-Coder-32B-Instruct [19], Qwen2.5-7B-Instruct [51], Qwen2.5-14B-Instruct [51] and Qwen2.5-32B-Instruct [51]).\n\n**CriticLeanGPT Models.** We further evaluate three variants from the Qwen2.5 series and Qwen3 series. These are instruction-based models fine-tuned specifically on either the CriticLeanInstruct 4 dataset or the RL-based clean critic Seed Data 4.1. All open-source models are inferred using the vLLM [21] framework with default inference parameters.\n\n### 5.2 Main Results\n\n#### 5.2.1 Evaluation of Critic Capability\n\nAs indicated in Table 2, the experimental results clearly demonstrate the effectiveness of the CriticLeanGPT models trained on our CriticLeanInstruct, in converting natural language mathematical statements into Lean 4 formal theorem declarations. Within the CriticLeanBench benchmark, our CriticLeanGPT models trained via supervised fine-tuning (SFT) and reinforcement learning (RL), along with their enhanced variants—outperform a range of closed-source API models, open-source models, and baseline models, highlighting distinct advantages. These outcomes yield several key insights: (1) Reasoning models excel in critical tasks, with Gemini 2.5 Pro, QwQ-32B, Qwen3-32B, and DeepSeek-R1 all attaining scores above 80. When compared to baseline models, our Qwen3-32B-RL model, optimized through RL, achieves a strong accuracy level, underscoring the efficacy of both our training methodology and dataset. (3) Our innovative mixed SFT strategy substantially boosts the performance of the Qwen2.5 family, with notable improvements observed across the 7B, 14B, and 32B models. (4) Additionally, SFT and RL significantly strengthen the models’ capacity to identify erroneous samples, as evidenced by higher true negative rates (TNR) and lower false negative rates (FNR)—a critical enhancement for accurate detection of incorrect formalizations, which is indispensable for effective critical tasks.\n\n### 5.3 Ablation Study\n\n#### 5.3.1 Effect of Reasoning Data\n\nWe conduct an ablation study on CriticLeanBench to evaluate the impact of different training strategies. As shown in Table 3, incorporating code and math reasoning data significantly improves performance across all model sizes compared to using Seed Data 4.1. Specifically, using the CriticLeanInstruct 4, which samples Critic and non-Critic data at a ratio of 1:3, leads to substantial gains, demonstrating that integrating diverse reasoning tasks enhances the critical reasoning capabilities of the model. This suggests that multi-task learning with math and code data improves the critique abilities of mathematical formalization.\n\n#### 5.3.2 Effect of SFT Dataset Size\n\nFigure 6 highlights a notable parameter-dependent relationship between the size of the SFT dataset and key reasoning performance. Across all model scales, performance improvements are observed through SFT, albeit with varying degrees of fluctuation depending on the training set size. Smaller models (e.g., 7B) exhibit more pronounced gains as the dataset expands, whereas larger models (e.g., 32B) demonstrate a less consistent trend, with marginal improvements at lower data volumes but substantial gains at higher data volumes. These findings align with prior studies [39, 78], underscoring the interplay between model capacity, data scale, and performance optimization in SFT scenarios. The results emphasize the need for tailored strategies to balance data efficiency and model generalization, particularly for large-scale architectures.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>ACC&lt;/th>\n&lt;th>TPR&lt;/th>\n&lt;th>FPR&lt;/th>\n&lt;th>TNR&lt;/th>\n&lt;th>FNR&lt;/th>\n&lt;th>Reasoning&lt;/th>\n&lt;th>Open-source&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"8\" style=\"text-align: center;\">&lt;b>SOTA LLMs&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Gemini-2.5-Pro&lt;/td>\n&lt;td>&lt;u>89.2&lt;/u>&lt;/td>\n&lt;td>&lt;u>95.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>4.4&lt;/u>&lt;/td>\n&lt;td>&lt;u>82.8&lt;/u>&lt;/td>\n&lt;td>&lt;u>17.2&lt;/u>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B&lt;/td>\n&lt;td>&lt;u>86.4&lt;/u>&lt;/td>\n&lt;td>93.6&lt;/td>\n&lt;td>6.4&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-32B&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>&lt;b>96.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>4.0&lt;/b>&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-235B-A22B&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;td>90.8&lt;/td>\n&lt;td>9.2&lt;/td>\n&lt;td>77.2&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-14B&lt;/td>\n&lt;td>83.6&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>7.6&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>25.2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-8B&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>94.4&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>34.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Doubao-1.5-pro-32k&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>95.2&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Claude35-Sonnet&lt;/td>\n&lt;td>74.2&lt;/td>\n&lt;td>&lt;u>97.2&lt;/u>&lt;/td>\n&lt;td>&lt;u>2.8&lt;/u>&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>48.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>48.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>95.2&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>41.2&lt;/td>\n&lt;td>58.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-2024-11-20&lt;/td>\n&lt;td>67.8&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>4.4&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>19.6&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>65.4&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>57.6&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>60.8&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>10.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V1.5-SFT&lt;/td>\n&lt;td>52.4&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V1.5-RL&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"8\" style=\"text-align: center;\">&lt;b>CriticLeanGPT (Ours)&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-8B-RL&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-14B-RL&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>22.0&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-32B-RL&lt;/td>\n&lt;td>&lt;b>87.0&lt;/b>&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;td>&lt;u>85.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>14.4&lt;/u>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-RL&lt;/td>\n&lt;td>68.6&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>14.4&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>48.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-RL&lt;/td>\n&lt;td>69.4&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-RL&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>60.4&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>&lt;b>83.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>16.4&lt;/b>&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>94.4&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>\n&lt;td>70.6&lt;/td>\n&lt;td>83.6&lt;/td>\n&lt;td>16.4&lt;/td>\n&lt;td>57.6&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT-RL&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT-RL&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>18.4&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT-RL&lt;/td>\n&lt;td>78.6&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 2 Performance on CriticLeanBench.** The best, the second-best and the third-best scores for each indicator are shown in box, **bold** and underlined, respectively.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>ACC&lt;/th>\n&lt;th>TPR&lt;/th>\n&lt;th>FPR&lt;/th>\n&lt;th>TNR&lt;/th>\n&lt;th>FNR&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>7B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>60.8&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>10.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>64.0&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>29.2&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">57.2&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">42.8&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">69.8&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">94.4&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">5.6&lt;/span>&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>14B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>19.6&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>67.4&lt;/td>\n&lt;td>80.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">70.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">83.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">16.4&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">57.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">42.4&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>32B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">91.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">8.4&lt;/span>&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>71.0&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">70.0&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">30.0&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">76.2&lt;/span>&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3 Comparison of model performance under different training strategies:** base model, SFT on Critic data only, and SFT on combined Critic, code, and math data. The best score for each indicator is shown in box.\n\n## 5.4 Analysis\n\n### 5.4.1 Scaling Analysis\n\nWe evaluate the performance of Qwen series models on CriticLeanBench across different model scales, including Qwen2.5-Coder, Qwen2.5-Instruct, Qwen2.5-Instruct-SFT, Qwen2.5-Instruct-SFT-RL, Qwen3, and Qwen3-RL. The results in Figure 4 show that the performance improves consistently as the model size increases, demonstrating a clear scaling law of LLMs on CriticLeanBench.\n\n### 5.4.2 Effect of Pass@k\n\nThe Pass@k metric serves as a means to identify the highest-quality answers from multi-modal large language models (MLLMs) for final responses, highlighting the models’ potential for enhancement through post-training techniques like Reinforcement Learning from Human Feedback (RLHF [25]) and Gradient Penalty Policy Optimization (GRPO [46]). In this study, Pass@k evaluations were conducted on Qwen2.5-7B-Instruct, Qwen2.5-7B-Instruct-SFT-RL, Qwen3-8B, and Qwen3-8B-RL using CriticLeanBench, with k set to 8 and 32, and evaluation metrics including Accuracy (ACC), True Positive Rate (TPR), and True Negative Rate (TNR).\n\nAs shown in Figure 5, we observe that models subjected to Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) achieve better overall performance. Considering Pass@32, the Accuracy of Qwen2.5-7B-Instruct is outperformed by that of Qwen2.5-7B-Instruct-SFT-RL, which has undergone SFT and RL processing, leading to a notable improvement in the overall correctness rate. Regarding the True Negative Rate, models without SFT and RL processing are more prone to misclassifying incorrect samples as correct, whereas processed models effectively mitigate such errors; this is evident in the higher TNR of Qwen2.5-7B-Instruct-SFT-RL compared to Qwen2.5-7B-Instruct at Pass@32, reducing the likelihood of\n\n**Figure 6 Comparison of model performance under different amounts of SFT data:** base model, CriticLeanInstruct(16K), and CriticLeanInstruct.**Figure 4** Scaling Analysis of LLMs on CriticLeanBench.  $\\hat{\\square}$  denoted closed-source LLMs.\n\nsuch misclassifications. A similar trend is observed in Qwen3-8B. Additionally, all models exhibit improved performance as  $k$  increases, suggesting that SFT- and RL-optimized models can more effectively select high-quality answers when provided with more candidate responses.\n\n## 6 FineLeanCorpus\n\nTo construct the FineLeanCorpus, we began by aggregating a vast and diverse collection of natural language mathematical problems. Sourcing from a wide array of materials, including high school olympiad datasets (e.g., AoPS, BlueMO), standard high school curricula (e.g., TAL-SCQ5), and undergraduate-level challenges (e.g., Omni-MATH), we ensured an extensive initial distribution in both the mathematical domain and difficulty. The first step in our process was to standardize this heterogeneous collection into a uniform, proof-based format, making each problem compatible with the Lean 4 theorem prover and ready for the subsequent formalization pipeline.\n\nThese standardized problems were then subjected to a rigorous, gated auto-formalization process powered by our CriticLean framework (Figure 1). The Kimina-Autoformalizer-7B model first generates a candidate formal statement. This statement must pass a syntactic check via the Lean 4 compiler; failure leads to regeneration. A successful compilation is followed by a semantic correctness check from our CriticLeanGPT model, with rejection also triggering a new attempt. This regenerative approach is critical, maximizing the yield from our source corpus by iteratively seeking a valid formalization. Finally, to further enhance precision, we apply a final filtering stage using another,\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Statistics&lt;/th>\n&lt;th>Number&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>#Problems&lt;/td>\n&lt;td>285957&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Length&lt;/b>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;i>Statement&lt;/i>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>maximum length&lt;/td>\n&lt;td>2980 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>minimum length&lt;/td>\n&lt;td>9 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>avg length&lt;/td>\n&lt;td>78.4 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;i>Lean Result(success)&lt;/i>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>maximum length&lt;/td>\n&lt;td>768 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>minimum length&lt;/td>\n&lt;td>14 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>avg length&lt;/td>\n&lt;td>87.8 tokens&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 5** Dataset statistics of FineLeanCorpus.**Figure 5** Performance on CriticLeanBench using **Pass@k** metrics, where **k = 8** (left) and **k = 32** (right).\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Difficulty Level&lt;/th>\n&lt;th>Size&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>AOPs [35]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>199982&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepMath-103k [15]&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>28538&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>NuminaMath-TIR [24]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>22847&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepTheorem [74]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>15131&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepScaleR [34]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>11544&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DAPO-Math-17k [66]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>4078&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Omni-MATH [8]&lt;/td>\n&lt;td>Undergraduate&lt;/td>\n&lt;td>1176&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>IneqMath [20]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>963&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>BlueMO [73]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>616&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>TAL-SCQ5K [37]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>393&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>70&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Multi-Source Math Competition&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>619&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 4** Overview of different sources for FineLeanCorpus.\n\nhigher-performance CriticLeanGPT model. Manual validation indicates that this step is expected to eliminate 74.7% of the remaining incorrect formalizations. The resulting corpus is characterized by its expressive range: natural language statements vary from a concise 9 tokens to a complex 2,980 tokens (avg. 78.4), while their corresponding Lean formalizations span from 14 to 768 tokens (avg. 87.8), reflecting the deep spectrum of complexity successfully captured by our pipeline.\n\nTo further analyze the differences between our FineLeanCorpus dataset and the Lean-Workbook, we employed the templates from Appendix J and Appendix I to assess the difficulty levels and classify the mathematical domains of the datasets using Doubao-1.5-pro [12]. A comparative analysis of our proposed FineLeanCorpus against Lean-Workbook (Figure 7, Figure 8, Table 4 and Table 5) reveals two fundamental advancements: (1) Scale and Coverage: Our corpus provides a significant quantitative expansion in both problem difficulty and domain coverage. This expansion is evident not only across nearly the entire difficulty spectrum—offering a much richer data pool for training foundational skills—but also in the substantial augmentation of high-volume domains like Intermediate Algebra and Elementary Number Theory. (2) FineLeanCorpus exhibits a more diverse and structurally balanced profile, achieved by collecting natural language statements from numerous sources. From a difficulty perspective, it features a multimodal distribution with substantial problem counts at several distinct complexity points, in stark contrast to the unimodal distribution of Lean-Workbook. This characteristic is crucial for mitigating model overfitting to a narrow complexity band. From a domain perspective, it substantially reinforces previously underrepresented areas. For instance, categories such as Analytic Geometry and Integral Calculus are significantly expanded, while niche topics like Algorithms and Graph Theory are also robustly augmented. This targeted enrichment transforms sparsely sampled topics into well-supported, learnable sub-domains, yielding a more comprehensive dataset designed to fosterholistic reasoning capabilities. More details regarding our FineLeanCorpus dataset, including its fine-grained mathematical domain distribution (see Appendix A), are provided for further analysis.\n\nFurthermore, to push the boundaries of current models and foster research into the upper echelons of mathematical reasoning, we have curated a specialized training subset from FineLeanCorpus, which we designate as Diamond. This subset comprises 36,033 problems with a difficulty rating exceeding 5. The purpose of this high-difficulty training set is to create a demanding training environment that fosters the development of the sophisticated, multi-step reasoning required to tackle the most formidable mathematical problems. A detailed breakdown of the mathematical domain distribution within this subset is provided in table 11.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Source&lt;/th>\n&lt;th>Theorems&lt;/th>\n&lt;th>Level&lt;/th>\n&lt;th>Detailed Critic Process&lt;/th>\n&lt;th>Difficulty Profile&lt;/th>\n&lt;th>Topic Diversity&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Lean-Workbook [65]&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>140K&lt;/td>\n&lt;td>Undergraduate&lt;/td>\n&lt;td>Opaque&lt;/td>\n&lt;td>Avg: 3.70&lt;br/>Top-tier (&lt;math>\\geq 6&lt;/math>): 7.81%&lt;/td>\n&lt;td>Highly Skewed&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>FineLeanCorpus (ours)&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>285K&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>Transparent&lt;/td>\n&lt;td>Avg: 3.24&lt;br/>Top-tier (&lt;math>\\geq 6&lt;/math>): 11.10%&lt;/td>\n&lt;td>Balanced &amp; Diverse&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 6** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.\n\n**Figure 7** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.\n\n## 6.1 Analysis on CriticLean Pipeline\n\nAs shown in Table 7, our autoformalization pipeline significantly improves accuracy. We selected 50 problems from the Omni-MATH and applied the following three formalization strategies, with the correctness of all outputs confirmed by manual human inspection.\n\nOur baseline model, Kimina-Autoformalizer-7B, is used in each strategy: (1) a **Single Pass** baseline (38.0% accuracy); (2) a **Compiler Feedback** loop, where the model regenerates formalizations until they successfully compile (54.0% accuracy); (3) our **CriticLean Pipeline**, which extends this process, regenerating formalizations until they both compile successfully and are validated by our integrated **CriticLeanGPT Model** (84.0% accuracy).\n\nWhile compiler feedback resolves syntactical errors, it fails to detect logical flaws. Our pipeline addresses this gap. The integration of critic model, which performs deeper semantic and logical validation, is directly\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>AVG&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B&lt;/td>\n&lt;td>38.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B (Compiler)&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B (CriticLean)&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 7** Human evaluation accuracy results for autoformalization performance: The best score is highlighted in *box*.**Figure 8** Math Domain Distributions: FineLeanCorpus vs. Lean-Workbook.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th># Attempt&lt;/th>\n&lt;th>1&lt;/th>\n&lt;th>5&lt;/th>\n&lt;th>10&lt;/th>\n&lt;th>50&lt;/th>\n&lt;th>100&lt;/th>\n&lt;th>200&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Count / Ratio&lt;/td>\n&lt;td>63 / 12.6%&lt;/td>\n&lt;td>137 / 27.4%&lt;/td>\n&lt;td>170 / 34.0%&lt;/td>\n&lt;td>229 / 45.8%&lt;/td>\n&lt;td>245 / 49.0%&lt;/td>\n&lt;td>264 / 52.8%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 8 Effectiveness of the Multi-Attempt Strategy on Formalization Yield.** The table shows the cumulative number of successfully formalized problems retained by the critic model as the attempt limit increases. Statistics are from a 500-problem sample.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>NuminaMath-TIR [24]&lt;/td>\n&lt;td>78%&lt;/td>\n&lt;td>IneqMath [20]&lt;/td>\n&lt;td>96%&lt;/td>\n&lt;td>BlueMO [73]&lt;/td>\n&lt;td>86%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepMath-103k [16]&lt;/td>\n&lt;td>84%&lt;/td>\n&lt;td>DAPO-Math-17k [66]&lt;/td>\n&lt;td>69%&lt;/td>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>88%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AOPs [35]&lt;/td>\n&lt;td>73%&lt;/td>\n&lt;td>TAL-SCQ5K [37]&lt;/td>\n&lt;td>75%&lt;/td>\n&lt;td>Omni-MATH [8]&lt;/td>\n&lt;td>84%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepTheorem [74]&lt;/td>\n&lt;td>100%&lt;/td>\n&lt;td>DeepScaleR [34]&lt;/td>\n&lt;td>100%&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 9** Human evaluation results of different sources.\n\nresponsible for the accuracy increase from 54.0% to 84.0%. By filtering out plausible but incorrect formalizations, our method provides a more robust path toward reliable autoformalization. These manually-verified results present strong empirical evidence for the efficacy of our approach.\n\nTable 8 shows our pipeline achieved a 52.8% success rate across 500 problems, where success required passing both syntactic validation and our critic model’s semantic check. The value of our multi-attempt strategy is evident: while only 12.6% of samples passed on the first try, the pipeline successfully recovered an additional 40.2% that would be discarded by single-pass systems. Conversely, the 47.2% failure rate within the 200-attempt limit highlights a fundamental bottleneck: the pipeline’s performance is ultimately constrained by the base auto-formalization model’s ability to produce a candidate our critic can approve.\n\nMoreover, as shown in Table 9, we also provide the human evaluation results of different sources. We observe that the accuracy varies across different sources, a discrepancy we attribute primarily to the differing domain and difficulty distributions of the respective datasets.&lt;sup>2&lt;/sup>\n\n&lt;sup>2&lt;/sup>Our human evaluation standard is particularly stringent. To calibrate our criteria, we inspected a random sample of 50## 7 Conclusion\n\nThis paper presents CriticLean, a comprehensive framework that positions the critic as a central component in the autoformalization of mathematical statements. Through the development of CriticLeanGPT and the construction of CriticLeanBench, we demonstrate that explicitly modeling and training the critic yields significant improvements in formalization quality. Our pipeline not only refines the translation process through semantic validation, but also enables the construction of FineLeanCorpus, which is validated by both compiler and critic.\n\n---\n\nentries from the Lean-Workbook, which yielded an accuracy of 84%.## **8 Contributions and Acknowledgments**\n\n### **Co-First Authors**\n\nZhongyuan Peng, Yifan Yao, Kaijing Ma\n\n### **Co-Authors**\n\nShuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, Minghao Liu, Yihang Xia, Jiawei Shen, Yuchen Wu, Yixin Cao, Zhaoxiang Zhang, Wenhao Huang\n\n### **Corresponding Authors**\n\nJiaheng Liu, Ge Zhang## References\n\n- [1] AI Research Group of TAL Education Group. K-12 handwritten mathematical expressions dataset (hme100k). &lt;https://ai.100tal.com/dataset>. Accessed: 2025-04-05.\n- [2] Anthropic. Claude 3.5 sonnet model card addendum, 2024. URL &lt;https://www.paperswithcode.com/paper/claude-3-5-sonnet-model-card-addendum>. Accessed: 2024-09-21.\n- [3] Zhangir Azerbayev, Bartosz Piotrowski, Hailey Schoelkopf, Edward W Ayers, Dragomir Radev, and Jeremy Avigad. Proofnet: Autoformalizing and formally proving undergraduate-level mathematics. [arXiv preprint arXiv:2302.12433](#), 2023.\n- [4] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report. [arXiv preprint arXiv:2309.16609](#), 2023.\n- [5] Konstantin Chernyshev, Vitaliy Polshkov, Ekaterina Artemova, Alex Myasnikov, Vlad Stepanov, Alexei Miasnikov, and Sergei Tilga. U-math: A university-level benchmark for evaluating mathematical skills in llms. [arXiv preprint arXiv:2412.03205](#), 2024.\n- [6] B.P. Demidovich. Problems in Mathematical Analysis. Edited by B. Demidovich. Translated From the Russian by G. Yankovsky. Russian Monographs and Texts on Advanced Mathematics and Physics. Mir Publishers, 1964. URL &lt;https://books.google.com/books?id=XdmpwgEACA AJ>.\n- [7] J Fan, S Martinson, EY Wang, K Hausknecht, J Brenner, D Liu, N Peng, C Wang, and MP Brenner. Hardmath: A benchmark dataset for challenging problems in applied mathematics. arxiv 2024. [arXiv preprint arXiv:2410.09988](#).\n- [8] Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. [arXiv preprint arXiv:2410.07985](#), 2024.\n- [9] Google. Gemini: A family of highly capable multimodal models, 2023.\n- [10] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. [arXiv preprint arXiv:2407.21783](#), 2024.\n- [11] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. [arXiv preprint arXiv:2501.12948](#), 2025.\n- [12] Dong Guo, Faming Wu, Feida Zhu, Fuxing Leng, Guang Shi, Haobin Chen, Haoqi Fan, Jian Wang, Jianyu Jiang, Jiawei Wang, et al. Seed1. 5-vl technical report. [arXiv preprint arXiv:2505.07062](#), 2025.\n- [13] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024.\n- [14] Yancheng He, Shilong Li, Jiaheng Liu, Weixun Wang, Xingyuan Bu, Ge Zhang, Zhongyuan Peng, Zhaoxiang Zhang, Zhicheng Zheng, Wenbo Su, and Bo Zheng. Can large language models detect errors in long chain-of-thought reasoning?, 2025. URL &lt;https://arxiv.org/abs/2502.19361>.\n- [15] Zhiwei He, Tian Liang, Jiahao Xu, Qiuzhi Liu, Xingyu Chen, Yue Wang, Linfeng Song, Dian Yu, Zhenwen Liang, Wenxuan Wang, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. Deepmath-103k: A large-scale, challenging, decontaminated, and verifiable mathematical dataset for advancing reasoning. 2025. URL &lt;https://arxiv.org/abs/2504.11456>.\n- [16] Zhiwei He, Tian Liang, Jiahao Xu, Qiuzhi Liu, Xingyu Chen, Yue Wang, Linfeng Song, Dian Yu, Zhenwen Liang, Wenxuan Wang, et al. Deepmath-103k: A large-scale, challenging, decontaminated, and verifiable mathematical dataset for advancing reasoning. [arXiv preprint arXiv:2504.11456](#), 2025.- [17] Hui Huang, Yancheng He, Hongli Zhou, Rui Zhang, Wei Liu, Weixun Wang, Wenbo Su, Bo Zheng, and Jiaheng Liu. Think-j: Learning to think for generative llm-as-a-judge. [ArXiv](https://arxiv.org/abs/2505.14268), abs/2505.14268, 2025. URL &lt;https://api.semanticscholar.org/CorpusID:278769843>.\n- [18] Hugging Face. Open r1: A fully open reproduction of deepseek-r1, January 2025. URL &lt;https://github.com/huggingface/open-r1>.\n- [19] Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Kai Dang, et al. Qwen2. 5-coder technical report. [arXiv preprint arXiv:2409.12186](https://arxiv.org/abs/2409.12186), 2024.\n- [20] Sheng Jiayi, Lyu Luna, Jin Jikai, Xia Tony, Gu Alex, Zou James, and Lu Pan. Solving inequality proofs with large language models. [arXiv preprint arXiv:2506.07927](https://arxiv.org/abs/2506.07927), 2025.\n- [21] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In [Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles](#), 2023.\n- [22] Leanprover Community. A read-eval-print-loop for Lean 4, 2023. &lt;https://github.com/leanprover-community/repl>.\n- [23] Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving quantitative reasoning problems with language models, 2022. URL &lt;https://arxiv.org/abs/2206.14858>.\n- [24] Jia LI, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa Huang, Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong, Li Zhou, Yann Fleureau, Guillaume Lample, and Stanislas Polu. NuminaMath tir. [&lt;https://huggingface.co/AI-MO/NuminaMath-TIR>] ([https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina\\\\_dataset.pdf](https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf)), 2024.\n- [25] Zihao Li, Zhuoran Yang, and Mengdi Wang. Reinforcement learning with human feedback: Learning dynamic choices via pessimism. [arXiv preprint arXiv:2305.18438](https://arxiv.org/abs/2305.18438), 2023.\n- [26] Yong Lin, Shange Tang, Bohan Lyu, Jiayun Wu, Hongzhou Lin, Kaiyu Yang, Jia Li, Mengzhou Xia, Danqi Chen, Sanjeev Arora, and Chi Jin. Goedel-prover: A frontier model for open-source automated theorem proving, 2025. URL &lt;https://arxiv.org/abs/2502.07640>.\n- [27] Zicheng Lin, Zhibin Gou, Tian Liang, Ruilin Luo, Haowei Liu, and Yujiu Yang. Criticbench: Benchmarking llms for critique-correct reasoning. [arXiv preprint arXiv:2402.14809](https://arxiv.org/abs/2402.14809), 2024.\n- [28] Chengwu Liu, Jianhao Shen, Huajian Xin, Zhengying Liu, Ye Yuan, Haiming Wang, Wei Ju, Chuanyang Zheng, Yichun Yin, Lin Li, et al. Fimo: A challenge formal dataset for automated theorem proving. [arXiv preprint arXiv:2309.04295](https://arxiv.org/abs/2309.04295), 2023.\n- [29] Jiaheng Liu, Ken Deng, Congnan Liu, Jian Yang, Shukai Liu, He Zhu, Peng Zhao, Linzheng Chai, Yanan Wu, Ke Jin, et al. M2rc-eval: Massively multilingual repository-level code completion evaluation. [arXiv preprint arXiv:2410.21157](https://arxiv.org/abs/2410.21157), 2024.\n- [30] Jiaheng Liu, Chenchen Zhang, Jinyang Guo, Yuanxing Zhang, Haoran Que, Ken Deng, Zhiqi Bai, Jie Liu, Ge Zhang, Jiakai Wang, Yanan Wu, Congnan Liu, Jiamang Wang, Lin Qu, Wenbo Su, and Bo Zheng. DDK: Distilling domain knowledge for efficient large language models. In [The Thirty-eighth Annual Conference on Neural Information Processing Systems](#), 2024. URL &lt;https://openreview.net/forum?id=xgiurUq0ss>.\n- [31] Jiaheng Liu, Dawei Zhu, Zhiqi Bai, Yancheng He, Huanxuan Liao, Haoran Que, Zekun Wang, Chenchen Zhang, Ge Zhang, Jiebin Zhang, et al. A comprehensive survey on long context language modeling. [arXiv preprint arXiv:2503.17407](https://arxiv.org/abs/2503.17407), 2025.\n- [32] Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, and Yi Dong. ProRL: Prolonged reinforcement learning expands reasoning boundaries in large language models. [arXiv preprint arXiv:2505.24864](https://arxiv.org/abs/2505.24864), 2025.\n- [33] Jianqiao Lu, Yingjia Wan, Zhengying Liu, Yinya Huang, Jing Xiong, Chengwu Liu, Jianhao Shen, Hui Jin, Jipeng Zhang, Haiming Wang, Zhicheng Yang, Jing Tang, and Zhijiang Guo. Process-driven autoformalization in lean 4, 2024. URL &lt;https://arxiv.org/abs/2406.01940>.- [34] Michael Luo, Sijun Tan, Justin Wong, Xiaoxiang Shi, William Tang, Manan Roongta, Colin Cai, Jeffrey Luo, Tianjun Zhang, Erran Li, Raluca Ada Popa, and Ion Stoica. DeepScaler: Surpassing o1-preview with a 1.5b model by scaling rl. &lt;https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e> 2025. Notion Blog.\n- [35] Sadegh Mahdavi, Muchen Li, Kaiwen Liu, Christos Thrampoulidis, Leonid Sigal, and Renjie Liao. Leveraging online olympiad-level math problems for llms training and contamination-resistant evaluation, 2025. URL &lt;https://arxiv.org/abs/2501.14275>.\n- [36] Sadegh Mahdavi, Muchen Li, Kaiwen Liu, Christos Thrampoulidis, Leonid Sigal, and Renjie Liao. Leveraging online olympiad-level math problems for llms training and contamination-resistant evaluation. [arXiv preprint arXiv:2501.14275](#), 2025.\n- [37] Math-eval. TAL-SCQ5K. &lt;https://github.com/math-eval/TAL-SCQ5K>, 2023.\n- [38] Leonardo de Moura and Sebastian Ullrich. The lean 4 theorem prover and programming language. In Automated Deduction – CADE 28: 28th International Conference on Automated Deduction, Virtual Event, July 12–15, 2021, Proceedings, page 625–635, Berlin, Heidelberg, 2021. Springer-Verlag. ISBN 978-3-030-79875-8. doi: 10.1007/978-3-030-79876-5\\_37. URL [https://doi.org/10.1007/978-3-030-79876-5\\\\_37](https://doi.org/10.1007/978-3-030-79876-5_37).\n- [39] Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, and Tatsunori Hashimoto. s1: Simple test-time scaling. [arXiv preprint arXiv:2501.19393](#), 2025.\n- [40] Tobias Nipkow, Markus Wenzel, and Lawrence C. Paulson. Isabelle/HOL: a proof assistant for higher-order logic. Springer-Verlag, Berlin, Heidelberg, 2002. ISBN 3540433767.\n- [41] Online Math Contest. Online math contest. &lt;https://onlinemathcontest.com/>. Accessed: 2025-04-05.\n- [42] R OpenAI. Gpt-4 technical report. arxiv 2303.08774. [View in Article](#), 2(5), 2023.\n- [43] Miguel Angel Peñaloza Perez, Bruno Lopez Orozco, Jesus Tadeo Cruz Soto, Michelle Bruno Hernandez, Miguel Angel Alvarado Gonzalez, and Sandra Malagon. Ai4math: A native spanish benchmark for university-level mathematical reasoning in large language models. [arXiv preprint arXiv:2505.18978](#), 2025.\n- [44] Peter Scholze. Liquid tensor experiment. Experimental Mathematics, 31(2):349–354, 2022.\n- [45] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024. URL &lt;https://arxiv.org/abs/2402.03300>.\n- [46] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. [arXiv preprint arXiv:2402.03300](#), 2024.\n- [47] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. [arXiv preprint arXiv: 2409.19256](#), 2024.\n- [48] Christian Szegedy. A promising path towards autoformalization and general artificial intelligence. In Intelligent Computer Mathematics: 13th International Conference, CICM 2020, Bertinoro, Italy, July 26–31, 2020, Proceedings 13, pages 3–20. Springer, 2020.\n- [49] Terence Tao. The polynomial freiman-ruzsa conjecture, 2023. &lt;https://github.com/teorth/pf>.\n- [50] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. [arXiv preprint arXiv:2312.11805](#), 2023.\n- [51] Qwen Team. Qwen2.5: A party of foundation models, September 2024. URL &lt;https://qwenlm.github.io/blog/qwen2.5/>.\n- [52] Qwen Team. Qwen3 technical report, 2025. URL &lt;https://arxiv.org/abs/2505.09388>.\n- [53] Qwen Team. Qwq-32b: Embracing the power of reinforcement learning, March 2025. URL &lt;https://qwenlm.github.io/blog/qwq-32b/>.- [54] Haiming Wang, Mert Unsal, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos, Flood Sung, Marina Vinyes, Zhenzhe Ying, Zekai Zhu, Jianqiao Lu, Hugues de Saxcé, Bolton Bailey, Chendong Song, Chenjun Xiao, Dehao Zhang, Ebony Zhang, Frederick Pu, Han Zhu, Jiawei Liu, Jonas Bayer, Julien Michel, Longhui Yu, Léo Dreyfus-Schmidt, Lewis Tunstall, Luigi Pagani, Moreira Machado, Pauline Bourigault, Ran Wang, Stanislas Polu, Thibaut Barroyer, Wen-Ding Li, Yazhe Niu, Yann Fleureau, Yangyang Hu, Zhouliang Yu, Zihan Wang, Zhilin Yang, Zhengying Liu, and Jia Li. Kimina-prover preview: Towards large formal reasoning models with reinforcement learning. 2025. URL &lt;http://arxiv.org/abs/2504.11354>.\n- [55] Weixun Wang, Shaopan Xiong, Gengru Chen, Wei Gao, Sheng Guo, Yancheng He, Ju Huang, Jiaheng Liu, Zhendong Li, Xiaoyang Li, Zichen Liu, Haizhou Zhao, Dakai An, Lunxi Cao, Qi Cao, Wanxi Deng, Feilei Du, Yiliang Gu, Jiahe Li, Xiang Li, Mingjie Liu, Yijia Luo, Zihe Liu, Yadao Wang, Pei Wang, Tianyuan Wu, Yanan Wu, Yuheng Zhao, Shu-Man Zhao, Jin Yang, Si-Yue Yang, Ying Tan, Huimin Yi, Yuchi Xu, Yu-Ming Yuan, Xingyao Zhang, Lin Qu, Wenbo Su, Wei Wang, Jiamang Wang, and Boyuan Zheng. Reinforcement learning optimization for large-scale learning: An efficient and user-friendly scaling library. 2025.\n- [56] Yiping Wang, Qing Yang, Zhiyuan Zeng, Liliang Ren, Liyuan Liu, Baolin Peng, Hao Cheng, Xuehai He, Kuan Wang, Jianfeng Gao, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, and Yelong Shen. Reinforcement learning for reasoning in large language models with one training example, 2025. URL &lt;https://arxiv.org/abs/2504.20571>.\n- [57] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. *Advances in neural information processing systems*, 35:24824–24837, 2022.\n- [58] Sean Welleck, Jiacheng Liu, Ronan Le Bras, Hannaneh Hajishirzi, Yejin Choi, and Kyunghyun Cho. Naturalproofs: Mathematical theorem proving in natural language, 2021. URL &lt;https://arxiv.org/abs/2104.01112>.\n- [59] Sean Welleck, Jiacheng Liu, Ximing Lu, Hannaneh Hajishirzi, and Yejin Choi. Naturalprover: Grounded mathematical proof generation with language models, 2022. URL &lt;https://arxiv.org/abs/2205.12910>.\n- [60] Yuhuai Wu, Albert Q. Jiang, Wenda Li, Markus N. Rabe, Charles Staats, Mateja Jamnik, and Christian Szegedy. Autoformalization with large language models, 2022.\n- [61] Huajian Xin, Daya Guo, Zhihong Shao, Zhizhou Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, and Xiaodan Liang. Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data. *arXiv preprint arXiv:2405.14333*, 2024.\n- [62] Huajian Xin, Z. Z. Ren, Junxiao Song, Zhihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, Wenjun Gao, Qihao Zhu, Dejian Yang, Zhibin Gou, Z. F. Wu, Fuli Luo, and Chong Ruan. Deepseek-prover-v1.5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search. 2024. URL &lt;https://arxiv.org/abs/2408.08152>.\n- [63] Tianyi Xiong, Xiyao Wang, Dong Guo, Qinghao Ye, Haoqi Fan, Quanquan Gu, Heng Huang, and Chunyuan Li. Llava-critic: Learning to evaluate multimodal models. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 13618–13628, 2025.\n- [64] Kaiyu Yang, Gabriel Poesia, Jingxuan He, Wenda Li, Kristin Lauter, Swarat Chaudhuri, and Dawn Song. Formal mathematical reasoning: A new frontier in ai, 2024. URL &lt;https://arxiv.org/abs/2412.16075>.\n- [65] Huaiyuan Ying, Zijian Wu, Yihan Geng, Zheng Yuan, Dahua Lin, and Kai Chen. Lean workbook: A large-scale lean problem set formalized from natural language math problems, 2025. URL &lt;https://arxiv.org/abs/2406.03847>.\n- [66] Qiyong Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, GaoHong Liu, Lingjun Liu, Xin Liu, et al. DAPO: An open-source LLM reinforcement learning system at scale. *arXiv preprint arXiv:2503.14476*, 2025.\n- [67] Zhouliang Yu, Ruotian Peng, Keyi Ding, Yizhe Li, Zhongyuan Peng, Minghao Liu, Yifan Zhang, Zheng Yuan, Huajian Xin, Wenhao Huang, Yandong Wen, Ge Zhang, and Weiyang Liu. Formalmath: Benchmarking formal mathematical reasoning of large language models, 2025. URL &lt;https://arxiv.org/abs/2505.02735>.\n- [68] Zhouliang Yu, Yuhuan Yuan, Tim Z Xiao, Fuxiang Frank Xia, Jie Fu, Ge Zhang, Ge Lin, and Weiyang Liu. Generating symbolic world models via test-time scaling of large language models. *arXiv preprint arXiv:2502.04728*, 2025.- [69] Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in LLMs beyond the base model? [arXiv preprint arXiv:2504.13837](#), 2025.\n- [70] Yu Yue, Yufeng Yuan, Qiyong Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, Jiaze Chen, Chengyi Wang, TianTian Fan, Zhengyin Du, et al. VAPO: Efficient and reliable reinforcement learning for advanced reasoning tasks. [arXiv preprint arXiv:2504.05118](#), 2025.\n- [71] Alexander Zhang, Marcus Dong, Jiaheng Liu, Wei Zhang, Yejie Wang, Jian Yang, Ge Zhang, Tianyu Liu, Zhongyuan Peng, Yingshui Tan, et al. Codecriticbench: A holistic code critique benchmark for large language models. [arXiv preprint arXiv:2502.16614](#), 2025.\n- [72] Ge Zhang, Scott Qu, Jiaheng Liu, Chenchen Zhang, Chenghua Lin, Chou Leuang Yu, Danny Pan, Esther Cheng, Jie Liu, Qunshu Lin, et al. Map-neo: Highly capable and transparent bilingual large language model series. [arXiv preprint arXiv:2405.19327](#), 2024.\n- [73] Yifan Zhang, Yifan Luo, and Yizhou Chen. Bluemo: A comprehensive collection of challenging mathematical olympiad problems from the little blue book series., 2024.\n- [74] Ziyin Zhang, Jiahao Xu, Zhiwei He, Tian Liang, Qiuzhi Liu, Yansi Li, Linfeng Song, Zhenwen Liang, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. Deeptheorem: Advancing llm reasoning for theorem proving through natural language and reinforcement learning, 2025. URL &lt;https://arxiv.org/abs/2505.23754>.\n- [75] Kunhao Zheng, Jesse Michael Han, and Stanislas Polu. Minif2f: a cross-system benchmark for formal olympiad-level mathematics. [arXiv preprint arXiv:2109.00110](#), 2021.\n- [76] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot arena. *Advances in Neural Information Processing Systems*, 36:46595–46623, 2023.\n- [77] Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyuan Luo, Zhangchi Feng, and Yongqiang Ma. Llamafactory: Unified efficient fine-tuning of 100+ language models. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)*, Bangkok, Thailand, 2024. Association for Computational Linguistics. URL &lt;http://arxiv.org/abs/2403.13372>.\n- [78] Chunting Zhou, Pengfei Liu, Puxin Xu, Srinivasan Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu, Lili Yu, et al. Lima: Less is more for alignment. *Advances in Neural Information Processing Systems*, 36: 55006–55021, 2023.# Appendix\n\n## A Fine-Grained Domain Distribution of FineLeanCorpus\n\nThe following table illustrates the fine-grained domain distribution of the FineLeanCorpus by presenting its 50 most frequent mathematical topics for illustrative purposes. To enhance readability and highlight the hierarchical structure, entries are sorted alphabetically by Main Category, then Sub-Category, and Topic.\n\n**Table 10** Fine-Grained Domain Distribution of FineLeanCorpus\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Main Category&lt;/th>\n&lt;th>Sub-Category&lt;/th>\n&lt;th>Topic&lt;/th>\n&lt;th>Count&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"8\">Algebra&lt;/td>\n&lt;td rowspan=\"5\">Intermediate Algebra&lt;/td>\n&lt;td>Diophantine Equations&lt;/td>\n&lt;td>23&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Functional Equations&lt;/td>\n&lt;td>30178&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Inequalities&lt;/td>\n&lt;td>75339&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>65171&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Polynomials&lt;/td>\n&lt;td>32424&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Linear Algebra&lt;/td>\n&lt;td>Matrices&lt;/td>\n&lt;td>4361&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>54&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Vector Spaces&lt;/td>\n&lt;td>2179&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"8\">Applied Mathematics&lt;/td>\n&lt;td>Algorithms&lt;/td>\n&lt;td>Greedy Algorithms&lt;/td>\n&lt;td>46&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Optimization&lt;/td>\n&lt;td>Linear Programming&lt;/td>\n&lt;td>258&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>3165&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>273&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Probability&lt;/td>\n&lt;td>Conditional Probability&lt;/td>\n&lt;td>363&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Expected Value&lt;/td>\n&lt;td>792&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>2417&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"8\">Calculus&lt;/td>\n&lt;td rowspan=\"4\">Differential Calculus&lt;/td>\n&lt;td>Applications of Derivatives&lt;/td>\n&lt;td>57&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Derivatives&lt;/td>\n&lt;td>14948&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Limits&lt;/td>\n&lt;td>787&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>5391&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Integral Calculus&lt;/td>\n&lt;td>Definite Integrals&lt;/td>\n&lt;td>15165&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>18761&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">Other&lt;/td>\n&lt;td>Limits&lt;/td>\n&lt;td>1086&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Limits of Multivariable Functions&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Limits of Sequences&lt;/td>\n&lt;td>106&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>8592&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"8\">Combinatorics&lt;/td>\n&lt;td rowspan=\"2\">Constructive Combinatorics&lt;/td>\n&lt;td>Invariants&lt;/td>\n&lt;td>320&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>54&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Enumerative Combinatorics&lt;/td>\n&lt;td>Combinations&lt;/td>\n&lt;td>5579&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>10460&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Permutations&lt;/td>\n&lt;td>869&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Extremal Combinatorics&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>375&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Pigeonhole Principle&lt;/td>\n&lt;td>1377&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Graph Theory&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>42&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>(Continued) Distribution of Problems by Mathematical Topic\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Main Category&lt;/th>\n&lt;th>Sub-Category&lt;/th>\n&lt;th>Topic&lt;/th>\n&lt;th>Count&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"4\">Discrete Mathematics&lt;/td>\n&lt;td>Logic&lt;/td>\n&lt;td>Propositional Logic&lt;/td>\n&lt;td>444&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>3994&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Set Theory&lt;/td>\n&lt;td>Cardinality&lt;/td>\n&lt;td>1262&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>1585&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"7\">Geometry&lt;/td>\n&lt;td rowspan=\"2\">Analytic Geometry&lt;/td>\n&lt;td>Conic Sections&lt;/td>\n&lt;td>1498&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>254&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">Euclidean Geometry&lt;/td>\n&lt;td>Circles&lt;/td>\n&lt;td>1880&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Coordinate Geometry&lt;/td>\n&lt;td>3584&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>4172&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Transformations&lt;/td>\n&lt;td>404&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Triangles&lt;/td>\n&lt;td>7243&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"6\">Number Theory&lt;/td>\n&lt;td rowspan=\"6\">Elementary Number Theory&lt;/td>\n&lt;td>Diophantine Equations&lt;/td>\n&lt;td>17208&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Divisibility&lt;/td>\n&lt;td>21160&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Inequalities&lt;/td>\n&lt;td>42&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Modular Arithmetic&lt;/td>\n&lt;td>9284&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>18636&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Prime Numbers&lt;/td>\n&lt;td>12071&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## B Fine-Grained Domain Distribution of FineLeanCorpus-Diamond\n\nThe following table illustrates the fine-grained domain distribution of the Diamond dataset, our high-difficulty subset, by presenting its 50 most frequent mathematical topics for illustrative purposes. To enhance readability and highlight the hierarchical structure, entries are sorted alphabetically by Main Category, then Sub-Category, and Topic.\n\n**Table 11** Fine-Grained Domain Distribution of FineLeanCorpus-Diamond\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Main Category&lt;/th>\n&lt;th>Sub-Category&lt;/th>\n&lt;th>Topic&lt;/th>\n&lt;th>Count&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"7\">Algebra&lt;/td>\n&lt;td rowspan=\"4\">Intermediate Algebra&lt;/td>\n&lt;td>Functional Equations&lt;/td>\n&lt;td>6732&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Inequalities&lt;/td>\n&lt;td>12533&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>3621&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Polynomials&lt;/td>\n&lt;td>2798&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Linear Algebra&lt;/td>\n&lt;td>Matrices&lt;/td>\n&lt;td>955&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Vector Spaces&lt;/td>\n&lt;td>206&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Analysis&lt;/td>\n&lt;td>Real Analysis&lt;/td>\n&lt;td>Density of Sets&lt;/td>\n&lt;td>3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">Applied Mathematics&lt;/td>\n&lt;td>Optimization&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>108&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Probability&lt;/td>\n&lt;td>Conditional Probability&lt;/td>\n&lt;td>9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Expected Value&lt;/td>\n&lt;td>23&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>63&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Calculus&lt;/td>\n&lt;td>Differential Calculus&lt;/td>\n&lt;td>Derivatives&lt;/td>\n&lt;td>913&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>(Continued) Distribution of Problems by Mathematical Topic\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Main Category&lt;/th>\n&lt;th>Sub-Category&lt;/th>\n&lt;th>Topic&lt;/th>\n&lt;th>Count&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Differential Equations&lt;/td>\n&lt;td>3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Limits&lt;/td>\n&lt;td>31&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>375&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>Integral Calculus&lt;/td>\n&lt;td>Definite Integrals&lt;/td>\n&lt;td>2280&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>2666&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>Limits&lt;/td>\n&lt;td>44&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>814&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"10\">Combinatorics&lt;/td>\n&lt;td rowspan=\"2\">Constructive Combinatorics&lt;/td>\n&lt;td>Invariants&lt;/td>\n&lt;td>144&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>33&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Enumerative Combinatorics&lt;/td>\n&lt;td>Combinations&lt;/td>\n&lt;td>620&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>1165&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Permutations&lt;/td>\n&lt;td>70&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Extremal Combinatorics&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>201&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Pigeonhole Principle&lt;/td>\n&lt;td>442&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Graph Theory&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>18&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Trees&lt;/td>\n&lt;td>6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">Discrete Mathematics&lt;/td>\n&lt;td>Logic&lt;/td>\n&lt;td>Propositional Logic&lt;/td>\n&lt;td>21&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>1260&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Set Theory&lt;/td>\n&lt;td>Cardinality&lt;/td>\n&lt;td>463&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>379&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"8\">Geometry&lt;/td>\n&lt;td rowspan=\"2\">Analytic Geometry&lt;/td>\n&lt;td>Conic Sections&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>21&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">Euclidean Geometry&lt;/td>\n&lt;td>Circles&lt;/td>\n&lt;td>132&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Coordinate Geometry&lt;/td>\n&lt;td>45&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>306&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Transformations&lt;/td>\n&lt;td>15&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Triangles&lt;/td>\n&lt;td>1200&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"6\">Number Theory&lt;/td>\n&lt;td rowspan=\"6\">Elementary Number Theory&lt;/td>\n&lt;td>Diophantine Equations&lt;/td>\n&lt;td>2106&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Divisibility&lt;/td>\n&lt;td>3877&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Inequalities&lt;/td>\n&lt;td>18&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Modular Arithmetic&lt;/td>\n&lt;td>1593&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>3523&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Prime Numbers&lt;/td>\n&lt;td>3699&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Figure 9 Distribution of Different Error Types of CriticLeanBench.\n\n## C Formalization Quality Assessment Criteria\n\n### Formalization Quality Assessment Criteria\n\n#### I. Integrity & Accuracy of Mathematical Content\n\n- • **Conditions & Hypotheses:** Are all explicit premises, variable domains (e.g.,  $\\mathbb{N}$ ,  $\\mathbb{R}$ ,  $\\mathbb{F}_k$ ), index ranges (e.g.,  $a_0$  vs.  $a_1$ ), properties of specific objects (e.g., geometric shapes, algebraic structures), and implicit context (e.g., non-zero divisors) accurately translated? Are mathematical meanings preserved (e.g.,  $\\neq 0$  vs.  $> 0$ )?\n- • **Goals & Conclusions:** Are all goals/conclusions translated (including multiple parts/cases)? Is the goal type accurate (e.g., specific value, extremum, existence/uniqueness)? For extrema, is attainability addressed? Is the mathematical meaning accurately translated?\n\n#### II. Clarity & Correctness of Logical Structure\n\n- • **Propositional Structure:** Are logical connectives ( $\\leftrightarrow$ ,  $\\rightarrow$ ,  $\\wedge$ ,  $\\vee$ ,  $\\neg$ ) and quantifiers ( $\\forall$ ,  $\\exists$ ,  $\\exists!$ ) used correctly? Are quantifier order, scope, and nesting accurate (e.g., dependencies like  $\\forall \\epsilon > 0, \\exists \\delta > 0, \\dots$ )?\n- • **Relation of Conditions to Conclusions:** How do multiple premises combine (e.g.,  $(A \\wedge B) \\rightarrow C$  vs.  $A \\rightarrow (B \\rightarrow C)$ )? Are constraints within the correct scope?\n- • **Reasoning Path:** Does the formalization reflect the original logic and key steps without introducing flaws or altering proof difficulty?### III. Lean Conventions & Technical Accuracy\n\n- • **Syntax & Declarations:** Is the syntax (e.g., parentheses, keywords, type declarations) correct? Are theorem, example, lemma used appropriately?\n- • **Type System:** Do operations, parameters, and return values satisfy type constraints? Are numerals used in the correct type? Are mathematical concepts correctly mapped to Lean counterparts?\n- • **Definitions & Library Usage:** Are custom definitions clear? Are imports correct and non-redundant? Are standard symbols and operations used correctly (e.g., `Complex.abs`, `Nat.Prime`)?\n- • **Code Style & Readability:** Are names clear and consistent? Are there sufficient comments for complex parts? Is there any redundancy?\n\n### IV. Problem Comprehension & Overall Consistency\n\n- • **Grasping the Core:** Does the formalization capture the core mathematical idea?\n- • **Internal Self-Consistency:** Are there any logical contradictions between the translated parts?\n- • **Suitability for Formalization:** Is the problem suitable for formalization? Are assumptions/interpretations documented?\n\n### V. Formalization Strategy & Choices\n\n- • **Abstraction Level:** Is the abstraction level appropriate, avoiding unnecessary generalization or over-specification?\n- • **Alternative Evaluation:** Were alternatives considered? Was decomposition/modularization used for complex problems?\n\n### VI. Provability & Proof Assistance\n\n- • **Proof Complexity:** Does the formalization maintain a similar proof complexity? Were lemmas added to simplify the proof?\n- • **Automation Potential:** Is the structure amenable to automation tools?\n\n## D Error Taxonomy\n\n#### Error Taxonomy\n\n##### 1. Semantic and Logical Errors\n\n###### 1.1 Premise Translation Error\n\n- • **Description:** This error occurs when formalizing the given conditions, constraints, or assumptions from the original problem, resulting in a discrepancy between the logical premises in the Lean code and the problem's description.\n- • **Examples:** Failing to constrain variables to be positive, integers, or coprime as required; not ensuring that denominators in mathematical expressions are non-zero; omitting geometric constraints such as \"A, B, C form a triangle\" in geometry problems; not explicitly specifying the exact range of a variable. For instance, relationships between angles and sides must beprecisely defined in Lean, otherwise the resulting correspondence may not be unique.\n\nGenerated code\n\n## 1.2 Mathematical Representation Error\n\n- • **Description:** This error involves an inaccurate representation of the form and meaning of mathematical entities such as variables and expressions from the original problem. This leads to the formalized mathematical proposition in the code being inconsistent with the original problem, thereby undermining formal semantic correspondence.\n- • **Examples:** Formalizing a cubic polynomial as a quadratic one; mistranslating \"all eigenvalues are 1\" as \"the determinant is 1\"; simplifying a complex algebraic relationship into an incorrect equation; using the conclusion as a premise; mismatch of mathematical entities. An incorrect expression structure can change the intrinsic structure and semantics of the original mathematical expression, even if the computed result might happen to be the same. For example, incorrectly formalizing a finite nested expression (e.g.,  $2002 + 21(2001 + \\dots)$ ) as the sum of an infinite series.\n\n## 1.3 Goal Translation Error\n\n- • **Description:** The final goal or conclusion achieved by the code does not match what the problem asks for, failing to complete the specified task.\n- • **Examples:** The problem asks for a specific numerical value, but the code only proves its existence; the problem asks to calculate the radius of convergence, but the code incorrectly solves for the sum of the series; the final answer has a numerical calculation error or a formal writing error (e.g., writing a fraction  $n/m$  as  $m/n$ ). The final goal might also be translated incompletely, with omissions.\n\n## 1.4 Variable Usage Error\n\n- • **Description:** Improper use of a variable's type, scope, name, or index.\n- • **Examples:** Using natural numbers ( $\\mathbb{N}$ ) for a variable that requires real numbers ( $\\mathbb{R}$ ); off-by-one errors in summation or sequence indices; confusing or redefining variable names.\n\n## 1.5 Misuse of Mathematical Concepts\n\n- • **Description:** Incorrectly using a mathematical formalism in Lean to represent a different mathematical concept.\n- • **Examples:** Translating \"calculate the residue\" as \"find the limit\"; formalizing \"locally uniform convergence\" as \"pointwise convergence\"; treating a problem of counting unordered combinations (e.g., non-congruent triangles) as one of counting ordered tuples.\n\n## 1.6 Incorrect Assumption\n\n- • **Description:** Adding conditions that are not present in the original problem, which oversimplifies the problem or leads to an incorrect conclusion.\n- • **Example:** Introducing an unfounded assumption, such as a specific numerical value.\n\n## 2. Lean Syntax and Technical Errors\n\n- • **Description:** These are technical issues at the code level that prevent the code from compiling or cause unexpected runtime behavior.\n\n### 2.1 Syntax Error\n\n- • **Description:** The code does not conform to the basic syntax rules of Lean 4.\n- • **Examples:** A theorem statement is missing its name; the `by sorry` block to skip a proof is absent; incorrect keywords or symbols are used.Generated code\n\n## 2.2 Type Error\n\n- • **Description:** Performing incompatible operations on variables of different data types, including type mismatches and type casting errors.\n- • **Examples:** Performing division on a natural number ( $\\mathbb{N}$ ) and expecting a fractional result, but the outcome is floored to 0; failing to cast integers or natural numbers to real numbers before performing real-valued operations.\n\n## 2.3 Operator & Parenthesis Error\n\n- • **Description:** The calculation order of an expression does not match the intended logic due to misunderstandings of operator precedence, improper placement of quantifiers, or incorrect use of parentheses.\n- • **Example:**  $\\tan^2(\\frac{\\pi}{9})$  is incorrectly parsed as  $(\\frac{\\tan \\pi}{9})^2$ .\n\n## 2.4 Library Usage Error\n\n- • **Description:** Improper use of functions or definitions from `mathlib`.\n- • **Examples:** Using `.ncard` on an incorrect type of set; using a deprecated function name like `Complex.abs`.\n\n## 3. Translation Completeness and Other Meta-Errors\n\n- • **Description:** These errors reflect that the formalization fails to cover all requirements of the problem, or that the problem itself is difficult to formalize.\n\n### 3.1 Unformalizable Problem\n\n- • **Description:** The original problem description is vague, ambiguous, relies on diagrams, or involves real-world scenarios that are difficult to express in formal logic.\n- • **Examples:** The problem depends on a geometric figure that is not explicitly defined; a physical context or narrative scenario cannot be modeled precisely; the problem statement itself contains mathematical errors.\n\nGenerated code\n\n### 3.2 Incomplete Formalization\n\n- • **Description:** The code only formalizes part of the problem, omitting other requirements.\n- • **Examples:** Ignoring a \"prove or disprove\" requirement and assuming the statement is true by default; omitting multi-step derivation requirements from the problem.\n\n### 3.3 Improvable Code Style\n\n- • **Description:** The code may be logically correct but can be improved in terms of clarity, robustness, or adherence to conventions.\n- • **Examples:** Adding parentheses could enhance logical clarity; variable names are not intuitive; better use could be made of Lean's syntactic features.\n\n## E Complete Checklist for Lean4 Mathematical Formalization\n\n### Complete Checklist for Lean4 Mathematical Formalization\n\n#### Conditions & Hypotheses:\n\n1. 1. Completeness of Preconditions: Are all explicitly stated preconditions in the problem translated without omission?1. 2. Accuracy of Variable Domains: Are the domains of variables (e.g.,  $\\mathbb{N}, \\mathbb{N}^+, \\mathbb{R}$ , `Fin k`, `Set.Icc a b`) accurately translated?\n2. 3. Accuracy of Indexing: Do the starting points and ranges of sequence/function indices (e.g.,  $a_0$  vs  $a_1$ , `Finset.range n` vs `Finset.Icc l n`) align with the original intent?\n3. 4. Clarity of Object Properties: Are the properties of specific objects (e.g., geometric figures like trapezoids, incircles; algebraic structures like groups, rings) clearly expressed?\n4. 5. Inclusion of Implicit Conditions: Are common implicit contextual conditions in mathematics (e.g., non-zero divisors, non-negative radicands, non-degenerate geometric objects, definedness of functions/sequences at application points, default to real numbers if unspecified) appropriately added?\n5. 6. Accuracy of Conditional Semantics: Is the mathematical meaning of conditions (e.g., \"not equal to 0\" ( $\\neq 0$ ) vs \"greater than 0\" ( $> 0$ ), direction of inequality signs ( $>$  vs  $\\geq$ )) accurately translated?\n\n#### Goals & Conclusions:\n\n1. 1. Completeness of Goals/Conclusions: Are all goals/conclusions that need to be proven or solved translated? (Pay special attention to multi-part conclusions and multiple solution scenarios).\n2. 2. Precision of Goal Type: Is the type of goal to be solved precise (e.g., specific value, extremum, existence/uniqueness, universal property, equivalence relation, implication)?\n3. 3. Attainability in Extremum Problems: For extremum problems, is \"attainability\" explicitly stated (i.e., demonstrating not just an inequality, but also that equality can be achieved)?\n4. 4. Accuracy of Goal Semantics: Is the mathematical meaning of the goals accurately translated?\n\n#### Combination of Preconditions\n\n#### Logical Structure:\n\n1. 1. Accuracy of Logical Connectives: Does the use of logical connectives ( $\\leftrightarrow$  (iff),  $\\rightarrow$  (if...then...),  $\\wedge$  (and),  $\\vee$  (or),  $\\neg$  (not)) accurately reflect the logical relationships of the original proposition?\n2. 2. Appropriateness of Quantifiers: Is the use of quantifiers ( $\\forall$  (for all),  $\\exists$  (exists),  $\\exists!$  (exists uniquely)) appropriate?\n3. 3. Correctness of Quantifier Scope and Nesting: Do the order, scope, and nesting of quantifiers correctly express the dependencies between variables (e.g., in  $\\forall \\epsilon > 0, \\exists \\delta > 0, \\dots, \\delta$  depends on  $\\epsilon$ )?\n4. 4. Combination of Preconditions: How do multiple preconditions combine to affect the conclusion (e.g., differentiate  $(A \\wedge B) \\rightarrow C$  from  $A \\rightarrow (B \\rightarrow C)$ )?\n5. 5. Fidelity to Original Logic: Does the formalization faithfully represent the inherent logic and key steps of the original mathematical problem?\n\n#### Lean Technical Accuracy:\n\n1. 1. Correctness of Basic Syntax: Is the basic Lean syntax (parenthesis matching, keywords like `theorem`, `def`, `variable`, `let`, `by`) entirely correct?\n2. 2. Adherence to Type Constraints: Do all operations, function parameters, and return values satisfy Lean's type constraints?\n3. 3. Correct Mapping of Mathematical Concepts: Are mathematical concepts correctly mapped to their Lean counterparts?\n4. 4. Clarity of Custom Definitions: Are all custom functions, predicates, and notations used clearly defined?\n5. 5. Correctness of Imports: Are necessary definitions and lemmas correctly imported from Mathlib?**Overall Consistency:**\n\n1. 1. Capturing Core Mathematical Ideas: Does the formalization truly capture the core mathematical ideas and goals of the original problem?\n2. 2. Absence of Logical Contradictions: Are there any logical contradictions between the translated conditions, definitions, and goals?\n3. 3. Appropriateness for Formalization: Is the problem itself suitable for precise, unambiguous mathematical formalization?\n4. 4. Documentation of Assumptions: Are any assumptions or interpretative choices made during the formalization process documented?\n\n## F Prompt:Critical Feedback to CoT\n\n### Prompt:Critical Feedback to CoT\n\n**Instruction:** You will be provided with a mathematical text and its Lean4 code representation. Your task is to evaluate whether the Lean4 code accurately and semantically represents the mathematical text. You will be given a boolean indicating conversion success and potentially failure information. Based on this, use a step-by-step Chain of Thought (COT) to generate a detailed explanation for why the conversion is considered successful or failed, focusing on the semantic equivalence and formal correctness of the Lean4 code relative to the mathematical meaning. The Lean4 code must preserve the intended meaning in the mathematical text and use correct Lean4 syntax and structure.\n\n**Input:** You will receive the following four values:\n\n1. 1. **Mathematical Text:** A string containing mathematical content.\n2. 2. **Lean4Code:** A string representing the code equivalent of the mathematical text.\n3. 3. **Conversion Success:** A boolean value (True or False) indicating whether the mathematical text was successfully converted to the Lean4 code representation.\n4. 4. **Reason:** A string representing the code equivalent of the mathematical text.\n5. 5. If Conversion Success is True, this field will typically be empty. You must generate the detailed justification for the success.\n6. 6. If Conversion Success is False, this field will contain specific information pinpointing why the conversion failed. You must elaborate on this identified failure, incorporating the analysis modules described below.\n\n**Your Role:** You are an AI language assistant. Your role is to analyze the provided information and, using a step-by-step Chain of Thought (COT) approach, generate the explanation for the conversion's success (if indicated as successful) or elaborate on the identified failure information (if indicated as failed). **Guidelines:**\n\n1. 1. **Understand the Content:** Carefully read the mathematical text, the code representation, the Conversion Success value, and the Reason input (if Conversion Success is False).\n2. 2. **Generating the Explanation for Success (if Conversion Success is True):** If the conversion is successful, provide a detailed, step-by-step explanation using COT to justify why it is successful. Your justification should implicitly cover:\n   1. (a) **Mathematical Text Analysis:** Briefly identify the core mathematical components (definitions, variables, operations, relations, constraints, statements) present in the text.\n",
    "durationMs": 812,
    "url": "https://huggingface.co/papers/2507.06181"
  },
  "sourceToolAssistantUUID": "8a29b349-c5b3-4c16-aaf2-963fa1b7f760",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 51 · 2026-05-27T20:38:19.630Z_

```json
{
  "parentUuid": "d9760f0e-cdd3-49c3-afc4-3b610196c8de",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4d8a1093-abc5-49fd-9c8b-8104c398bfe2",
  "timestamp": "2026-05-27T20:38:19.630Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "4d8a1093-abc5-49fd-9c8b-8104c398bfe2",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Tool call

_source line 54 · 2026-05-27T20:38:22.259Z_

<details open><summary>🔧 Tool call — Read · `toolu_0164MKLhN62TEKyj5ATnRNSH`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/toolu_017tNQR36VFz5t8HzkqpKgwp.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d8a1093-abc5-49fd-9c8b-8104c398bfe2",
  "isSidechain": false,
  "requestId": "req_011CbTianfA4b9PfGMB5jcD5",
  "type": "assistant",
  "uuid": "f2211502-bba8-4a93-a2d6-56d16f13ff28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4WFDnicaFiqSrjYGx9oaR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 28449,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 28449,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 55 · 2026-05-27T20:38:22.581Z_

<details><summary>↩ Tool result · reported error · `toolu_0164MKLhN62TEKyj5ATnRNSH`</summary>

```text
File content (32125 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2211502-bba8-4a93-a2d6-56d16f13ff28",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "1cf9e34c-79fe-4633-b93b-64fb00caff80",
  "toolUseResult": "Error: File content (32125 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "f2211502-bba8-4a93-a2d6-56d16f13ff28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-27T20:38:25.377Z_

<details open><summary>🔧 Tool call — Read · `toolu_016BJYMNytEEfurVX3yY6HSK`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/toolu_017tNQR36VFz5t8HzkqpKgwp.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cf9e34c-79fe-4633-b93b-64fb00caff80",
  "isSidechain": false,
  "requestId": "req_011CbTib1HRuMcoQov2vq9iU",
  "type": "assistant",
  "uuid": "883cc291-59c3-478a-9d13-9d82eb6be7ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GmbbvC3YTyGfHeYpL7ZXm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 29277,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 29277,
          "cache_creation_input_tokens": 187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 187
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

_source line 57 · 2026-05-27T20:38:25.685Z_

<details><summary>↩ Tool result · `toolu_016BJYMNytEEfurVX3yY6HSK`</summary>

```text
1	# CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization
2	
3	ByteDance Seed      Nanjing University
4	
5	Full author list in Contributions
6	
7	## Abstract
8	
9	Translating natural language mathematical statements into formal, executable code is a fundamental challenge in automated theorem proving. While prior work has focused on generation and compilation success, little attention has been paid to the *critic phase*—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. In this paper, we introduce **CriticLean**, a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. Specifically, first, we propose the **CriticLeanGPT**, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Then, we introduce **CriticLeanBench**, a benchmark designed to measure models’ ability to distinguish semantically correct from incorrect formalizations, and demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines. Building on the CriticLean framework, we construct **FineLeanCorpus**, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation. Overall, our findings highlight that optimizing the critic phase is essential for producing reliable formalizations and we hope our CriticLean will provide valuable insights for future advances in formal mathematical reasoning.
10	
11	**Date:** July 8, 2025
12	
13	**Correspondence:** [liujiaheng@nju.edu.cn](mailto:liujiaheng@nju.edu.cn), [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)
14	
15	**Project Page:** &lt;https://github.com/multimodal-art-projection/CriticLean>
16	
17	## 1 Introduction
18	
19	The formalization of mathematical statements [64] is a critical task in modern mathematical computation, particularly in the context of theorem provers like Lean 4 [22]. The translation of natural language mathematical problems into formal, executable code remains a significant challenge, as it requires not only syntactical accuracy but also a deep understanding of the problem’s semantics [44, 49]. Existing approaches have shown progress, but they often face limitations in accuracy, especially in the context of complex, high-level problems that involve sophisticated mathematical reasoning [3, 23, 58, 59, 75]. In contrast to existing works, we argue that the *critic* phase—the step where the semantic correctness of generated formalizations is evaluated—is not only underexplored but also fundamentally essential to the success of mathematical autoformalization.
20	
21	Therefore, in this paper, we systematically investigate and optimize the critic component and introduce **CriticLean**, a comprehensive framework that places the critic model at the center of the formalization pipeline. Unlike prior work that primarily focuses on generation quality or compiler validity, CriticLean introduces the reinforcement learning-based **CriticLeanGPT** models explicitly trained to evaluate whether the Lean 4 output truly reflects the intent of the original mathematical statement., and we present a full methodology forThe diagram illustrates the CriticLean framework for mathematics autoformalization. It starts with a **Natural Language Statement** box containing a mathematical problem about permutations. This statement is processed by an **AutoFormalizer**. The AutoFormalizer's output is then evaluated by two verification steps: a **Verify** box for syntax checking and name resolution, and another **Verify** box for semantic meaning and logical consistency. The **Verify** boxes are supported by a **Lean Compiler** and **CriticLeanGPT** respectively. If a **Compilation Error** or **Critique Error** occurs, the AutoFormalizer receives feedback and iterates. If successful, the final output is a **Lean Formal Language Statement** box showing the formalized theorem.
22	
23	**Figure 1** Illustration of CriticLean framework based on Critic-Guided Reinforcement Learning for Mathematics Autoformalization.
24	
25	training, and evaluating CriticLeanGPT model. Specifically, as shown in Figure 1, for each natural language statement, we apply the autoformalization iteratively based on the feedback from the Lean compiler and the CriticLeanGPT models, which is trained to critically assess whether a generated formalization accurately represents the semantics of the original mathematical statement. In each iteration, the feedback provides valuable signals that drive an iterative refinement process, further improving the quality of the final Lean code output.
26	
27	Additionally, we present **CriticLeanBench**, a benchmark designed to evaluate the performance of CriticLeanGPT models, which contain 500 natural language and Lean 4 language statement pairs (i.e., 250 correct and 250 incorrect pairs). Through extensive experiments, we demonstrate that our trained CriticLeanGPT models outperform the SOTA open-source models [4, 10, 11] and many closed-source API models [9, 12, 42] greatly.
28	
29	Furthermore, building upon our critic-centric CriticLean pipeline, we propose the high-quality open-source Lean 4 statement dataset **FineLeanCorpus**, comprising 285,957 fully verified entries. When compared to the previous related datasets (e.g., LeanWorkBook [65]), FineLeanCorpus is distinguished by its diversity in mathematical domains, difficulty distribution, and strict semantic validation via critical feedback loops. Notably, its difficulty distribution and targeted domain enrichment create a more structurally balanced training environment, mitigating overfitting and transforming sparse topics into well-supported sub-domains. Furthermore, to foster research into the upper echelons of mathematical reasoning, we have curated the specialized subset called FineLeanCorpus-Diamond, comprising over 36,000 high-difficulty problems.
30	
31	## 2 Related Works
32	
33	### 2.1 Autoformalization
34	
35	Autoformalization [48, 60, 68] refers to the process by which AI systems parse natural language (NL) contents and translate them into machine-verifiable formal representations, such as those in theorem provers like Lean4 [38] or Isabelle [40]. Recent advances leverage large language models (LLMs) [72] to tackle this problem through two primary paradigms: (1) In-context learning [57], where models utilize annotated examples [28, 33, 60] to generate formalizations without explicit fine-tuning, (2) Supervised fine-tuning (e.g., [26, 61, 67]), which adapts general-purpose LLMs into domain-specific autoformalization experts. To assess correctness, prior works [26, 61, 67] employ LLM-as-judge [76] to verify semantic alignment between formal and informal statements. We advance this by training the first open-sourced, domain-specific light LLM on top of Qwen [52] family for critiquing Lean4 statement alignment via reinforcement learning [46], enhancingboth critique capability and formalization robustness.
36	
37	## 2.2 RL for LLM Reasoning
38	
39	The exploration of complex reasoning capabilities in Large Language Models (LLMs) has achieved significant advancements [14, 17, 29–31, 55], with Reinforcement Learning (RL) establishing itself as a critical paradigm for transcending the constraints inherent to Supervised Fine-Tuning (SFT) [29, 32, 56, 66, 70]. Notable methodologies, including GRPO [11, 46], DAPO [66] have demonstrated substantial gains in mathematical reasoning and intricate problem-solving domains. However, the underlying mechanisms by which RL enhances reasoning capabilities remain insufficiently characterized. Empirical analyses increasingly indicate that RL primarily functions to activate, refine, or optimize the sampling of latent reasoning competencies rather than generating entirely novel cognitive frameworks de novo. For example, Yue et al. [69] interrogate whether current reinforcement learning frameworks incorporating verifiable rewards (RLVR) genuinely expand the frontier of reasoning performance or merely enhance the efficiency of retrieving pre-existing solutions.
40	
41	## 3 CriticLeanGPT
42	
43	### 3.1 CriticLeanBench
44	
45	#### 3.1.1 Overview of CriticLeanBench
46	
47	CriticLeanBench aims to evaluate the critical reasoning of LLMs in key aspects such as translating natural language mathematical statements into formally verified theorem declarations in Lean 4, including critique and correction. By integrating these core dimensions, CriticLeanBench can comprehensively measure the performance of models in Formalization tasks. In this section, we will elaborate on the construction principles and processes of CriticLeanBench; the construction process is shown in Figure 2.
48	
49	CriticLeanBench is constructed following the following principles: (1) It covers various types of errors, aiming to thoroughly evaluate the comprehensive capabilities of LLMs in capturing the semantic intent of formalized statements, using Template G for systematic assessment; (2) It incorporates diverse data sources to enhance the diversity and representativeness of evaluation data; and (3) It ensures the reliability and validity of the evaluation benchmark through a combination of expert review and automated verification.
50	
51	#### 3.1.2 Automatically verified
52	
53	This section outlines the methodology employed to apply the Automatic Validation Filter, guided by predefined criteria for compiler and model-based verification.
54	
55	**Data Collection** We selected Math Statements from data sources [1, 16, 24, 36, 41, 43, 66], such as Omni-MATH [8], AIME [75], U-MATH [5], DEMI-MathAnalysis [6], HARDMath [7], OlympiadBench [13], and BlueMO [73], along with their corresponding Lean 4 Statements from public dataset [67].
56	
57	**Compiler Verified** We submitted the Lean 4 statements from the above dataset to the Lean 4 compiler. If the compilation succeeded, the results were passed to the DeepSeek R1 [11] model for further processing.
58	
59	- • **Compile false:** For statements that failed to compile, we randomly sampled 50 entries and retained the compiler feedback messages, which were included as part of our CriticLeanBench benchmark.
60	
61	**LLM Verified** For the data that has passed compilation, we utilize a template G to process each sample’s Math Statement and its corresponding Lean 4 Code Statement through the DeepSeek R1 large language model. The model is tasked with determining whether the Lean 4 Code Statement is consistent with the Math Statement, producing for each sample a tag indicating consistency or inconsistency along with a reasoning statement. To extract structured outputs from the model’s responses, we employ regular expression-based pattern matching. The results are then submitted to human reviewers for further validation.**Figure 2** An overview for the CriticLeanBench construction.
62	
63	### 3.1.3 Human Validation Filter
64	
65	This section outlines the methodology employed to apply the Human Validation Filter, guided by predefined criteria (detailed in Appendix C).
66	
67	We categorize the data into two groups based on whether the **Lean-compiled** autoformalization output semantically aligns with the refined statement. Therefore, a Lean-compiled autoformalization falls into the following:
68	
69	- • **Human Check right:** If the autoformalized statement both compiles and accurately captures the mathematical meaning, logic, and intended behavior of the original problem, it satisfies the semantic consistency criteria.
70	- • **Human Check false:** If the autoformalized statement compiles but fails to accurately represent the original mathematical problem’s semantics. It violates one or more of the semantic consistency criteria, despite being syntactically valid Lean code. This often happens when there’s a mismatch between the code’s logic and the intended mathematical meaning.
71	
72	Within the two categories, we select representative samples that mirror the characteristics of the original autoformalization statements while maximizing diversity within each subset and capturing the full spectrum of observed error types in the negative samples. This is achieved by balancing several factors:
73	
74	**Stratified Representation:** The selected samples should maintain a similar distribution across different strata of the original dataset. These strata are defined by:
75	
76	- • **Problem Complexity:** This encompasses factors like the number of variables, quantifiers, logical connectives, and the depth of nested mathematical structures.
77	- • **Mathematical Branches:** The samples should represent the various mathematical domains present in the original data.
78	- • **Statement Well-Formedness:** This refers to the degree to which the original mathematical statementsadhere to standard mathematical notation and conventions. This stratification ensures that the subsets reflect the variability in the quality of the original problem statements.
79	
80	**Comprehensive Error Coverage:** The negative samples are specifically chosen to exemplify the full range of typical errors observed in the autoformalization process. This range includes fundamental semantic and logical issues, such as Premise Translation Errors (e.g., incorrect domains or missing conditions), Mathematical Representation Errors (e.g., faulty expressions or definitions), and Goal Translation Errors. The set also covers issues such as Incorrect Assumptions, logical flaws like Operator & Parenthesis Errors (e.g., misplaced quantifiers), and high-level structural problems like Incomplete Formalization, where crucial context is omitted (detailed in figure 9).
81	
82	### 3.1.4 Data Statistics
83	
84	&lt;table border="1">
85	&lt;thead>
86	&lt;tr>
87	&lt;th>Statistics&lt;/th>
88	&lt;th>Number&lt;/th>
89	&lt;/tr>
90	&lt;/thead>
91	&lt;tbody>
92	&lt;tr>
93	&lt;td>&lt;b>#Problems&lt;/b>&lt;/td>
94	&lt;td>500&lt;/td>
95	&lt;/tr>
96	&lt;tr>
97	&lt;td>&lt;b>Correct Pairs&lt;/b>&lt;/td>
98	&lt;td>250&lt;/td>
99	&lt;/tr>
100	&lt;tr>
101	&lt;td>- &lt;i>human check&lt;/i>&lt;/td>
102	&lt;td>250&lt;/td>
103	&lt;/tr>
104	&lt;tr>
105	&lt;td>&lt;b>Incorrect Pairs&lt;/b>&lt;/td>
106	&lt;td>250&lt;/td>
107	&lt;/tr>
108	&lt;tr>
109	&lt;td>- &lt;i>human/compiler check&lt;/i>&lt;/td>
110	&lt;td>200/50&lt;/td>
111	&lt;/tr>
112	&lt;tr>
113	&lt;td>&lt;b>Question Tokens Length&lt;/b>&lt;/td>
114	&lt;td>&lt;/td>
115	&lt;/tr>
116	&lt;tr>
117	&lt;td>- &lt;i>max/min/avg&lt;/i>&lt;/td>
118	&lt;td>1,583/495/700.94&lt;/td>
119	&lt;/tr>
120	&lt;/tbody>
121	&lt;/table>
122	
123	&lt;table border="1">
124	&lt;thead>
125	&lt;tr>
126	&lt;th>Benchmark&lt;/th>
127	&lt;th>Critic&lt;/th>
128	&lt;th>Lean&lt;/th>
129	&lt;th>Test&lt;/th>
130	&lt;/tr>
131	&lt;/thead>
132	&lt;tbody>
133	&lt;tr>
134	&lt;td>CriticBench&lt;/td>
135	&lt;td>✓&lt;/td>
136	&lt;td>✗&lt;/td>
137	&lt;td>✓&lt;/td>
138	&lt;/tr>
139	&lt;tr>
140	&lt;td>CodeCriticBench&lt;/td>
141	&lt;td>✓&lt;/td>
142	&lt;td>✗&lt;/td>
143	&lt;td>✓&lt;/td>
144	&lt;/tr>
145	&lt;tr>
146	&lt;td>LLaVA-Critic&lt;/td>
147	&lt;td>✓&lt;/td>
148	&lt;td>✗&lt;/td>
149	&lt;td>✗&lt;/td>
150	&lt;/tr>
151	&lt;tr>
152	&lt;td>&lt;b>CriticLeanBench (ours)&lt;/b>&lt;/td>
153	&lt;td>✓&lt;/td>
154	&lt;td>✓&lt;/td>
155	&lt;td>✓&lt;/td>
156	&lt;/tr>
157	&lt;/tbody>
158	&lt;/table>
159	
160	**Table 1** Dataset statistics and comparison of various code benchmark datasets.
161	
162	Table 1 (left) presents the dataset statistics for CriticLeanBench. The dataset contains a total of 500 problems, comprising 250 correct and 250 incorrect Q/GT (Question and GT label) pairs distributed across the collection. The questions exhibit a notable variation in length, with a maximum token count of 1,583 and a minimum of 495 tokens, calculated using the Qwen2.5 [4] tokenizer. On average, each question contains approximately 700.94 tokens. This characteristic distinguishes CriticLeanBench as a complex evaluation benchmark that requires models to process relatively lengthy inputs compared to those in standard datasets.
163	
164	### 3.1.5 Comparison to Other Benchmarks
165	
166	In Table 1 (right), CriticLeanBench has the following features: (1) We focus on a modest data size of 500 samples, acknowledging the expensive manual annotation costs (ranging from tens to hundreds of dollars per instance) and prioritizing efficiency without compromising evaluation rigor; (2) We integrate both Critic and Lean functionalities, distinguishing ourselves from benchmarks like CriticBench [27] and CodeCriticBench [71] that lack Lean capabilities, and LLaVA-Critic [63] that omits both Lean capabilities and test evaluation components; (3) We incorporate a test component focused on translating mathematical statements into formally verified theorem declarations in Lean 4, offering a fine-grained evaluation framework to assess the correctness of model transformations. This aspect of evaluative completeness remains unmatched by existing datasets.
167	
168	## 4 CriticLeanInstruct
169	
170	To enhance the CriticLeanGPT model’s efficacy in critically evaluating the successful transformation of mathematical statements into Lean code, we construct a comprehensive training dataset comprising 48,000 samples. This dataset consists of three high-quality components, designed to comprehensively improve the model’s critical thinking and reasoning capabilities.
171	
172	To significantly broaden the CriticLeanGPT model’s knowledge coverage, we also integrates three times additional code and math [18] datasets, enabling it to more comprehensively understand mathematical concepts and Lean code structures.Specifically, the Seed Data, with a 1:3 mix of math and code, is termed **CriticLeanInstruct(16K)**. When combined with data augmentation while retaining the same ratio, it forms the full **CriticLeanInstruct** dataset.
173	
174	## 4.1 Seed Data
175	
176	The seed data comprises 4,000 samples evenly split into 2,000 correct and 2,000 incorrect instances. For both correct and incorrect samples, human experts provided critical feedback [F](#). Additionally, the incorrect samples include compiler error messages generated by the Lean 4 Compiler as supplementary feedback. Then, we adopt the Gemini2.5-Pro [\[9\]](#) to extend the critical feedback to detailed Chain-of-Thought (CoT) explanations.
177	
178	**Figure 3** Distribution of Different Error Types.
179	
180	To understand the primary failure modes, we analyzed the error distribution across the 2,000 incorrect samples in our seed data as illustrated in Figure 3. The analysis reveals two primary challenges: (1) Syntactic Barriers: The most frequent obstacles are syntactic, such as Type Error and Syntax Errors. These issues typically prevent the code from compiling, indicating a fundamental difficulty in mastering the formal language. (2) Semantic Gaps: Beyond syntax, these errors stem from a failure to interpret the natural language scenario and accurately model its key information. This is evident in high rates of errors when translating a problem’s core logical components—including its premises, goal, and mathematical representation. This semantic challenge is particularly acute in application-style "word problems," where difficulty comprehending complex contexts leads to a fundamentally flawed formalization.
181	
182	Drawing from the error taxonomy (detailed in Appendix D) and building upon our initial annotation standards (detailed in Appendix C), we established a fine-grained checklist, which is provided in full in Appendix E. This checklist formalizes the observed error paradigms, providing the foundational framework for methodically constructing the negative samples used throughout our study.
183	
184	## 4.2 Data Augmentation
185	
186	### 4.2.1 Correct Samples
187	
188	We selected **5560** correct mathematical statements and Lean code pairs from the FormalMATH [\[67\]](#) dataset and used the Gemini-2.5-Pro model to generate Critical Chain-of-Thought for initial assessment. To ensure data quality, we kept these samples where the model’s judgment is “correct.”## 4.2.2 Incorrect Samples
189	
190	We provide two strategies to obtain the incorrect samples as follows:
191	
192	- • Based on OmniMath, we adopt the Kimina-Autoformalizer-7B [54] to generate the Lean 4 code statements, and we kept 2,000 Lean code snippets that failed to compile due to syntactic or logical issues during automated formalization processes. For each detected error, a detailed Chain-of-Thought (CoT) explanation was generated to elucidate the error’s cause, enabling the model to recognize common compilation error patterns and thereby enhance its understanding of Lean 4 code syntax.
193	- • Based on correct mathematical statements and Lean 4 code from the FormalMATH [67] dataset, we implemented a three-step collaborative process to generate negative samples, aiming to enhance the CriticLeanGPT model’s ability to identify subtle errors and logical flaws. First, a checklist of various potential issues, refined by human experts, was established as shown in Appendix E. Second, the Gemini 2.5 Pro model was invoked to randomly select error types from this checklist and modify correct Lean code accordingly, generating incorrect samples (detailed in Appendix H). Then, we adopt the Gemini model to generate the critical Chain-of-Thought explanation.
194	
195	## 4.3 Training Paradigm
196	
197	*Supervised fine-tuning (SFT).* These models are instruction-tuned versions based on their respective pre-trained Qwen2.5 checkpoints, with a focus on improving their ability to interpret and formalize complex mathematical statements expressed in natural language. The CriticLeanInstruct 4 dataset includes Critic data consisting of mathematical statements converted into formally verified theorem declarations in Lean 4, along with three times as much code and mathematics data for SFT (Supervised Fine-Tuning). We used the LLaMA-Factory [77] framework to facilitate the fine-tuning process and optimize model performance.
198	
199	*Reinforcement Learning Optimization (RL).* The recent success of R1-style methods has demonstrated the effectiveness of online RL using discrete, rule-based rewards [45]. In our pipeline, Qwen2.5 series and Qwen3 [52] series are further refined using reinforcement learning signals derived from both format validation of the generated critic data and consistency checking between model predictions and expert-labeled ground truth (GT) labels. Specifically, the RL training data consists of 4,000 Seed Data 4.1, where each example transforms a mathematical statement into a corresponding formal proof in Lean 4. Based on this dataset, we apply a rule-based RL approach to optimize the model’s capability in judgment reasoning. More specifically, we mainly utilize the GRPO [46] algorithm within the VeRL [47] reinforcement learning framework, whose optimization objective is:
200	
201	$$J_{\text{online}}(\pi_{\theta}; \mathcal{D}) = \mathbb{E}_{x \sim \mathcal{D}, \{y_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}(y|x)} \left[ \frac{1}{G} \sum_{i=1}^G \min \left( \frac{\pi_{\theta}(y_i|x)}{\pi_{\theta_{\text{old}}}(y_i|x)} A_i, \text{clip} \left( \frac{\pi_{\theta}(y_i|x)}{\pi_{\theta_{\text{old}}}(y_i|x)}, 1 - \epsilon, 1 + \epsilon \right) A_i \right) - \beta D_{\text{KL}}(\pi_{\theta} || \pi_{\text{ref}}) \right] \quad (1)$$
202	
203	where  $G$  is group size, and  $A_i$  is advantage. The reward function is designed as follows&lt;sup>1&lt;/sup>:
204	
205	$$r_{\text{accuracy}} = \begin{cases} 1, & \text{if judgement} = \text{label} \\ 0, & \text{if judgement} \neq \text{label} \end{cases} \quad (2)$$
206	
207	$$r_{\text{format}} = \begin{cases} 1, & \text{if format is right} \\ 0, & \text{if format is wrong} \end{cases} \quad (3)$$
208	
209	$$r_{\text{final}} = \min(r_{\text{accuracy}}, r_{\text{format}}) \quad (4)$$
210	
211	
212	---
213	
214	&lt;sup>1&lt;/sup>We do not include a length penalty in rewards to encourage longer thinking.## 5 Experiments
215	
216	### 5.1 Experimental Setup
217	
218	**Baseline Models.** For the closed-sourced API models, we select the following models: Claude35\_Sonnet2 [2], Doubao-1.5-pro-32k [12], Gemini 2.5 Pro [50], GPT-4o-2024-11-20 [42]. We select a group of the most advanced open-source LLMs to serve as critic models for evaluation, which includes various reasoning models (DeepSeek-R1 [11], QwQ-32B [53], Qwen3-8B [52], Qwen3-14B [52], Qwen3-32B [52]), DeepSeek-Prover models [62] (DeepSeek-Prover-V1.5-RL, DeepSeek-Prover-V1.5-SFT), Llama-3.3-70B-Instruct [10] and several Qwen models (Qwen2.5-Coder-7B-Instruct [19], Qwen2.5-Coder-32B-Instruct [19], Qwen2.5-7B-Instruct [51], Qwen2.5-14B-Instruct [51] and Qwen2.5-32B-Instruct [51]).
219	
220	**CriticLeanGPT Models.** We further evaluate three variants from the Qwen2.5 series and Qwen3 series. These are instruction-based models fine-tuned specifically on either the CriticLeanInstruct 4 dataset or the RL-based clean critic Seed Data 4.1. All open-source models are inferred using the vLLM [21] framework with default inference parameters.
221	
222	### 5.2 Main Results
223	
224	#### 5.2.1 Evaluation of Critic Capability
225	
226	As indicated in Table 2, the experimental results clearly demonstrate the effectiveness of the CriticLeanGPT models trained on our CriticLeanInstruct, in converting natural language mathematical statements into Lean 4 formal theorem declarations. Within the CriticLeanBench benchmark, our CriticLeanGPT models trained via supervised fine-tuning (SFT) and reinforcement learning (RL), along with their enhanced variants—outperform a range of closed-source API models, open-source models, and baseline models, highlighting distinct advantages. These outcomes yield several key insights: (1) Reasoning models excel in critical tasks, with Gemini 2.5 Pro, QwQ-32B, Qwen3-32B, and DeepSeek-R1 all attaining scores above 80. When compared to baseline models, our Qwen3-32B-RL model, optimized through RL, achieves a strong accuracy level, underscoring the efficacy of both our training methodology and dataset. (3) Our innovative mixed SFT strategy substantially boosts the performance of the Qwen2.5 family, with notable improvements observed across the 7B, 14B, and 32B models. (4) Additionally, SFT and RL significantly strengthen the models’ capacity to identify erroneous samples, as evidenced by higher true negative rates (TNR) and lower false negative rates (FNR)—a critical enhancement for accurate detection of incorrect formalizations, which is indispensable for effective critical tasks.
227	
228	### 5.3 Ablation Study
229	
230	#### 5.3.1 Effect of Reasoning Data
231	
232	We conduct an ablation study on CriticLeanBench to evaluate the impact of different training strategies. As shown in Table 3, incorporating code and math reasoning data significantly improves performance across all model sizes compared to using Seed Data 4.1. Specifically, using the CriticLeanInstruct 4, which samples Critic and non-Critic data at a ratio of 1:3, leads to substantial gains, demonstrating that integrating diverse reasoning tasks enhances the critical reasoning capabilities of the model. This suggests that multi-task learning with math and code data improves the critique abilities of mathematical formalization.
233	
234	#### 5.3.2 Effect of SFT Dataset Size
235	
236	Figure 6 highlights a notable parameter-dependent relationship between the size of the SFT dataset and key reasoning performance. Across all model scales, performance improvements are observed through SFT, albeit with varying degrees of fluctuation depending on the training set size. Smaller models (e.g., 7B) exhibit more pronounced gains as the dataset expands, whereas larger models (e.g., 32B) demonstrate a less consistent trend, with marginal improvements at lower data volumes but substantial gains at higher data volumes. These findings align with prior studies [39, 78], underscoring the interplay between model capacity, data scale, and performance optimization in SFT scenarios. The results emphasize the need for tailored strategies to balance data efficiency and model generalization, particularly for large-scale architectures.&lt;table border="1">
237	&lt;thead>
238	&lt;tr>
239	&lt;th>Model&lt;/th>
240	&lt;th>ACC&lt;/th>
241	&lt;th>TPR&lt;/th>
242	&lt;th>FPR&lt;/th>
243	&lt;th>TNR&lt;/th>
244	&lt;th>FNR&lt;/th>
245	&lt;th>Reasoning&lt;/th>
246	&lt;th>Open-source&lt;/th>
247	&lt;/tr>
248	&lt;/thead>
249	&lt;tbody>
250	&lt;tr>
251	&lt;td colspan="8" style="text-align: center;">&lt;b>SOTA LLMs&lt;/b>&lt;/td>
252	&lt;/tr>
253	&lt;tr>
254	&lt;td>Gemini-2.5-Pro&lt;/td>
255	&lt;td>&lt;u>89.2&lt;/u>&lt;/td>
256	&lt;td>&lt;u>95.6&lt;/u>&lt;/td>
257	&lt;td>&lt;u>4.4&lt;/u>&lt;/td>
258	&lt;td>&lt;u>82.8&lt;/u>&lt;/td>
259	&lt;td>&lt;u>17.2&lt;/u>&lt;/td>
260	&lt;td>✓&lt;/td>
261	&lt;td>✗&lt;/td>
262	&lt;/tr>
263	&lt;tr>
264	&lt;td>QwQ-32B&lt;/td>
265	&lt;td>&lt;u>86.4&lt;/u>&lt;/td>
266	&lt;td>93.6&lt;/td>
267	&lt;td>6.4&lt;/td>
268	&lt;td>79.2&lt;/td>
269	&lt;td>20.8&lt;/td>
270	&lt;td>✓&lt;/td>
271	&lt;td>✓&lt;/td>
272	&lt;/tr>
273	&lt;tr>
274	&lt;td>Qwen3-32B&lt;/td>
275	&lt;td>85.6&lt;/td>
276	&lt;td>&lt;b>96.0&lt;/b>&lt;/td>
277	&lt;td>&lt;b>4.0&lt;/b>&lt;/td>
278	&lt;td>75.2&lt;/td>
279	&lt;td>24.8&lt;/td>
280	&lt;td>✓&lt;/td>
281	&lt;td>✓&lt;/td>
282	&lt;/tr>
283	&lt;tr>
284	&lt;td>Qwen3-235B-A22B&lt;/td>
285	&lt;td>84.8&lt;/td>
286	&lt;td>90.4&lt;/td>
287	&lt;td>9.6&lt;/td>
288	&lt;td>79.2&lt;/td>
289	&lt;td>20.8&lt;/td>
290	&lt;td>✓&lt;/td>
291	&lt;td>✓&lt;/td>
292	&lt;/tr>
293	&lt;tr>
294	&lt;td>DeepSeek-R1&lt;/td>
295	&lt;td>84.0&lt;/td>
296	&lt;td>90.8&lt;/td>
297	&lt;td>9.2&lt;/td>
298	&lt;td>77.2&lt;/td>
299	&lt;td>22.8&lt;/td>
300	&lt;td>✓&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "883cc291-59c3-478a-9d13-9d82eb6be7ec",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "9284ee5d-7996-40ce-b888-07982eef5b90",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/toolu_017tNQR36VFz5t8HzkqpKgwp.txt",
      "content": "# CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization\n\nByteDance Seed      Nanjing University\n\nFull author list in Contributions\n\n## Abstract\n\nTranslating natural language mathematical statements into formal, executable code is a fundamental challenge in automated theorem proving. While prior work has focused on generation and compilation success, little attention has been paid to the *critic phase*—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. In this paper, we introduce **CriticLean**, a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. Specifically, first, we propose the **CriticLeanGPT**, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Then, we introduce **CriticLeanBench**, a benchmark designed to measure models’ ability to distinguish semantically correct from incorrect formalizations, and demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines. Building on the CriticLean framework, we construct **FineLeanCorpus**, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation. Overall, our findings highlight that optimizing the critic phase is essential for producing reliable formalizations and we hope our CriticLean will provide valuable insights for future advances in formal mathematical reasoning.\n\n**Date:** July 8, 2025\n\n**Correspondence:** [liujiaheng@nju.edu.cn](mailto:liujiaheng@nju.edu.cn), [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)\n\n**Project Page:** &lt;https://github.com/multimodal-art-projection/CriticLean>\n\n## 1 Introduction\n\nThe formalization of mathematical statements [64] is a critical task in modern mathematical computation, particularly in the context of theorem provers like Lean 4 [22]. The translation of natural language mathematical problems into formal, executable code remains a significant challenge, as it requires not only syntactical accuracy but also a deep understanding of the problem’s semantics [44, 49]. Existing approaches have shown progress, but they often face limitations in accuracy, especially in the context of complex, high-level problems that involve sophisticated mathematical reasoning [3, 23, 58, 59, 75]. In contrast to existing works, we argue that the *critic* phase—the step where the semantic correctness of generated formalizations is evaluated—is not only underexplored but also fundamentally essential to the success of mathematical autoformalization.\n\nTherefore, in this paper, we systematically investigate and optimize the critic component and introduce **CriticLean**, a comprehensive framework that places the critic model at the center of the formalization pipeline. Unlike prior work that primarily focuses on generation quality or compiler validity, CriticLean introduces the reinforcement learning-based **CriticLeanGPT** models explicitly trained to evaluate whether the Lean 4 output truly reflects the intent of the original mathematical statement., and we present a full methodology forThe diagram illustrates the CriticLean framework for mathematics autoformalization. It starts with a **Natural Language Statement** box containing a mathematical problem about permutations. This statement is processed by an **AutoFormalizer**. The AutoFormalizer's output is then evaluated by two verification steps: a **Verify** box for syntax checking and name resolution, and another **Verify** box for semantic meaning and logical consistency. The **Verify** boxes are supported by a **Lean Compiler** and **CriticLeanGPT** respectively. If a **Compilation Error** or **Critique Error** occurs, the AutoFormalizer receives feedback and iterates. If successful, the final output is a **Lean Formal Language Statement** box showing the formalized theorem.\n\n**Figure 1** Illustration of CriticLean framework based on Critic-Guided Reinforcement Learning for Mathematics Autoformalization.\n\ntraining, and evaluating CriticLeanGPT model. Specifically, as shown in Figure 1, for each natural language statement, we apply the autoformalization iteratively based on the feedback from the Lean compiler and the CriticLeanGPT models, which is trained to critically assess whether a generated formalization accurately represents the semantics of the original mathematical statement. In each iteration, the feedback provides valuable signals that drive an iterative refinement process, further improving the quality of the final Lean code output.\n\nAdditionally, we present **CriticLeanBench**, a benchmark designed to evaluate the performance of CriticLeanGPT models, which contain 500 natural language and Lean 4 language statement pairs (i.e., 250 correct and 250 incorrect pairs). Through extensive experiments, we demonstrate that our trained CriticLeanGPT models outperform the SOTA open-source models [4, 10, 11] and many closed-source API models [9, 12, 42] greatly.\n\nFurthermore, building upon our critic-centric CriticLean pipeline, we propose the high-quality open-source Lean 4 statement dataset **FineLeanCorpus**, comprising 285,957 fully verified entries. When compared to the previous related datasets (e.g., LeanWorkBook [65]), FineLeanCorpus is distinguished by its diversity in mathematical domains, difficulty distribution, and strict semantic validation via critical feedback loops. Notably, its difficulty distribution and targeted domain enrichment create a more structurally balanced training environment, mitigating overfitting and transforming sparse topics into well-supported sub-domains. Furthermore, to foster research into the upper echelons of mathematical reasoning, we have curated the specialized subset called FineLeanCorpus-Diamond, comprising over 36,000 high-difficulty problems.\n\n## 2 Related Works\n\n### 2.1 Autoformalization\n\nAutoformalization [48, 60, 68] refers to the process by which AI systems parse natural language (NL) contents and translate them into machine-verifiable formal representations, such as those in theorem provers like Lean4 [38] or Isabelle [40]. Recent advances leverage large language models (LLMs) [72] to tackle this problem through two primary paradigms: (1) In-context learning [57], where models utilize annotated examples [28, 33, 60] to generate formalizations without explicit fine-tuning, (2) Supervised fine-tuning (e.g., [26, 61, 67]), which adapts general-purpose LLMs into domain-specific autoformalization experts. To assess correctness, prior works [26, 61, 67] employ LLM-as-judge [76] to verify semantic alignment between formal and informal statements. We advance this by training the first open-sourced, domain-specific light LLM on top of Qwen [52] family for critiquing Lean4 statement alignment via reinforcement learning [46], enhancingboth critique capability and formalization robustness.\n\n## 2.2 RL for LLM Reasoning\n\nThe exploration of complex reasoning capabilities in Large Language Models (LLMs) has achieved significant advancements [14, 17, 29–31, 55], with Reinforcement Learning (RL) establishing itself as a critical paradigm for transcending the constraints inherent to Supervised Fine-Tuning (SFT) [29, 32, 56, 66, 70]. Notable methodologies, including GRPO [11, 46], DAPO [66] have demonstrated substantial gains in mathematical reasoning and intricate problem-solving domains. However, the underlying mechanisms by which RL enhances reasoning capabilities remain insufficiently characterized. Empirical analyses increasingly indicate that RL primarily functions to activate, refine, or optimize the sampling of latent reasoning competencies rather than generating entirely novel cognitive frameworks de novo. For example, Yue et al. [69] interrogate whether current reinforcement learning frameworks incorporating verifiable rewards (RLVR) genuinely expand the frontier of reasoning performance or merely enhance the efficiency of retrieving pre-existing solutions.\n\n## 3 CriticLeanGPT\n\n### 3.1 CriticLeanBench\n\n#### 3.1.1 Overview of CriticLeanBench\n\nCriticLeanBench aims to evaluate the critical reasoning of LLMs in key aspects such as translating natural language mathematical statements into formally verified theorem declarations in Lean 4, including critique and correction. By integrating these core dimensions, CriticLeanBench can comprehensively measure the performance of models in Formalization tasks. In this section, we will elaborate on the construction principles and processes of CriticLeanBench; the construction process is shown in Figure 2.\n\nCriticLeanBench is constructed following the following principles: (1) It covers various types of errors, aiming to thoroughly evaluate the comprehensive capabilities of LLMs in capturing the semantic intent of formalized statements, using Template G for systematic assessment; (2) It incorporates diverse data sources to enhance the diversity and representativeness of evaluation data; and (3) It ensures the reliability and validity of the evaluation benchmark through a combination of expert review and automated verification.\n\n#### 3.1.2 Automatically verified\n\nThis section outlines the methodology employed to apply the Automatic Validation Filter, guided by predefined criteria for compiler and model-based verification.\n\n**Data Collection** We selected Math Statements from data sources [1, 16, 24, 36, 41, 43, 66], such as Omni-MATH [8], AIME [75], U-MATH [5], DEMI-MathAnalysis [6], HARDMath [7], OlympiadBench [13], and BlueMO [73], along with their corresponding Lean 4 Statements from public dataset [67].\n\n**Compiler Verified** We submitted the Lean 4 statements from the above dataset to the Lean 4 compiler. If the compilation succeeded, the results were passed to the DeepSeek R1 [11] model for further processing.\n\n- • **Compile false:** For statements that failed to compile, we randomly sampled 50 entries and retained the compiler feedback messages, which were included as part of our CriticLeanBench benchmark.\n\n**LLM Verified** For the data that has passed compilation, we utilize a template G to process each sample’s Math Statement and its corresponding Lean 4 Code Statement through the DeepSeek R1 large language model. The model is tasked with determining whether the Lean 4 Code Statement is consistent with the Math Statement, producing for each sample a tag indicating consistency or inconsistency along with a reasoning statement. To extract structured outputs from the model’s responses, we employ regular expression-based pattern matching. The results are then submitted to human reviewers for further validation.**Figure 2** An overview for the CriticLeanBench construction.\n\n### 3.1.3 Human Validation Filter\n\nThis section outlines the methodology employed to apply the Human Validation Filter, guided by predefined criteria (detailed in Appendix C).\n\nWe categorize the data into two groups based on whether the **Lean-compiled** autoformalization output semantically aligns with the refined statement. Therefore, a Lean-compiled autoformalization falls into the following:\n\n- • **Human Check right:** If the autoformalized statement both compiles and accurately captures the mathematical meaning, logic, and intended behavior of the original problem, it satisfies the semantic consistency criteria.\n- • **Human Check false:** If the autoformalized statement compiles but fails to accurately represent the original mathematical problem’s semantics. It violates one or more of the semantic consistency criteria, despite being syntactically valid Lean code. This often happens when there’s a mismatch between the code’s logic and the intended mathematical meaning.\n\nWithin the two categories, we select representative samples that mirror the characteristics of the original autoformalization statements while maximizing diversity within each subset and capturing the full spectrum of observed error types in the negative samples. This is achieved by balancing several factors:\n\n**Stratified Representation:** The selected samples should maintain a similar distribution across different strata of the original dataset. These strata are defined by:\n\n- • **Problem Complexity:** This encompasses factors like the number of variables, quantifiers, logical connectives, and the depth of nested mathematical structures.\n- • **Mathematical Branches:** The samples should represent the various mathematical domains present in the original data.\n- • **Statement Well-Formedness:** This refers to the degree to which the original mathematical statementsadhere to standard mathematical notation and conventions. This stratification ensures that the subsets reflect the variability in the quality of the original problem statements.\n\n**Comprehensive Error Coverage:** The negative samples are specifically chosen to exemplify the full range of typical errors observed in the autoformalization process. This range includes fundamental semantic and logical issues, such as Premise Translation Errors (e.g., incorrect domains or missing conditions), Mathematical Representation Errors (e.g., faulty expressions or definitions), and Goal Translation Errors. The set also covers issues such as Incorrect Assumptions, logical flaws like Operator & Parenthesis Errors (e.g., misplaced quantifiers), and high-level structural problems like Incomplete Formalization, where crucial context is omitted (detailed in figure 9).\n\n### 3.1.4 Data Statistics\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Statistics&lt;/th>\n&lt;th>Number&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;b>#Problems&lt;/b>&lt;/td>\n&lt;td>500&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Correct Pairs&lt;/b>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>human check&lt;/i>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Incorrect Pairs&lt;/b>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>human/compiler check&lt;/i>&lt;/td>\n&lt;td>200/50&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Question Tokens Length&lt;/b>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>max/min/avg&lt;/i>&lt;/td>\n&lt;td>1,583/495/700.94&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Critic&lt;/th>\n&lt;th>Lean&lt;/th>\n&lt;th>Test&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>CriticBench&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>CodeCriticBench&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>LLaVA-Critic&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>CriticLeanBench (ours)&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 1** Dataset statistics and comparison of various code benchmark datasets.\n\nTable 1 (left) presents the dataset statistics for CriticLeanBench. The dataset contains a total of 500 problems, comprising 250 correct and 250 incorrect Q/GT (Question and GT label) pairs distributed across the collection. The questions exhibit a notable variation in length, with a maximum token count of 1,583 and a minimum of 495 tokens, calculated using the Qwen2.5 [4] tokenizer. On average, each question contains approximately 700.94 tokens. This characteristic distinguishes CriticLeanBench as a complex evaluation benchmark that requires models to process relatively lengthy inputs compared to those in standard datasets.\n\n### 3.1.5 Comparison to Other Benchmarks\n\nIn Table 1 (right), CriticLeanBench has the following features: (1) We focus on a modest data size of 500 samples, acknowledging the expensive manual annotation costs (ranging from tens to hundreds of dollars per instance) and prioritizing efficiency without compromising evaluation rigor; (2) We integrate both Critic and Lean functionalities, distinguishing ourselves from benchmarks like CriticBench [27] and CodeCriticBench [71] that lack Lean capabilities, and LLaVA-Critic [63] that omits both Lean capabilities and test evaluation components; (3) We incorporate a test component focused on translating mathematical statements into formally verified theorem declarations in Lean 4, offering a fine-grained evaluation framework to assess the correctness of model transformations. This aspect of evaluative completeness remains unmatched by existing datasets.\n\n## 4 CriticLeanInstruct\n\nTo enhance the CriticLeanGPT model’s efficacy in critically evaluating the successful transformation of mathematical statements into Lean code, we construct a comprehensive training dataset comprising 48,000 samples. This dataset consists of three high-quality components, designed to comprehensively improve the model’s critical thinking and reasoning capabilities.\n\nTo significantly broaden the CriticLeanGPT model’s knowledge coverage, we also integrates three times additional code and math [18] datasets, enabling it to more comprehensively understand mathematical concepts and Lean code structures.Specifically, the Seed Data, with a 1:3 mix of math and code, is termed **CriticLeanInstruct(16K)**. When combined with data augmentation while retaining the same ratio, it forms the full **CriticLeanInstruct** dataset.\n\n## 4.1 Seed Data\n\nThe seed data comprises 4,000 samples evenly split into 2,000 correct and 2,000 incorrect instances. For both correct and incorrect samples, human experts provided critical feedback [F](#). Additionally, the incorrect samples include compiler error messages generated by the Lean 4 Compiler as supplementary feedback. Then, we adopt the Gemini2.5-Pro [\\[9\\]](#) to extend the critical feedback to detailed Chain-of-Thought (CoT) explanations.\n\n**Figure 3** Distribution of Different Error Types.\n\nTo understand the primary failure modes, we analyzed the error distribution across the 2,000 incorrect samples in our seed data as illustrated in Figure 3. The analysis reveals two primary challenges: (1) Syntactic Barriers: The most frequent obstacles are syntactic, such as Type Error and Syntax Errors. These issues typically prevent the code from compiling, indicating a fundamental difficulty in mastering the formal language. (2) Semantic Gaps: Beyond syntax, these errors stem from a failure to interpret the natural language scenario and accurately model its key information. This is evident in high rates of errors when translating a problem’s core logical components—including its premises, goal, and mathematical representation. This semantic challenge is particularly acute in application-style \"word problems,\" where difficulty comprehending complex contexts leads to a fundamentally flawed formalization.\n\nDrawing from the error taxonomy (detailed in Appendix D) and building upon our initial annotation standards (detailed in Appendix C), we established a fine-grained checklist, which is provided in full in Appendix E. This checklist formalizes the observed error paradigms, providing the foundational framework for methodically constructing the negative samples used throughout our study.\n\n## 4.2 Data Augmentation\n\n### 4.2.1 Correct Samples\n\nWe selected **5560** correct mathematical statements and Lean code pairs from the FormalMATH [\\[67\\]](#) dataset and used the Gemini-2.5-Pro model to generate Critical Chain-of-Thought for initial assessment. To ensure data quality, we kept these samples where the model’s judgment is “correct.”## 4.2.2 Incorrect Samples\n\nWe provide two strategies to obtain the incorrect samples as follows:\n\n- • Based on OmniMath, we adopt the Kimina-Autoformalizer-7B [54] to generate the Lean 4 code statements, and we kept 2,000 Lean code snippets that failed to compile due to syntactic or logical issues during automated formalization processes. For each detected error, a detailed Chain-of-Thought (CoT) explanation was generated to elucidate the error’s cause, enabling the model to recognize common compilation error patterns and thereby enhance its understanding of Lean 4 code syntax.\n- • Based on correct mathematical statements and Lean 4 code from the FormalMATH [67] dataset, we implemented a three-step collaborative process to generate negative samples, aiming to enhance the CriticLeanGPT model’s ability to identify subtle errors and logical flaws. First, a checklist of various potential issues, refined by human experts, was established as shown in Appendix E. Second, the Gemini 2.5 Pro model was invoked to randomly select error types from this checklist and modify correct Lean code accordingly, generating incorrect samples (detailed in Appendix H). Then, we adopt the Gemini model to generate the critical Chain-of-Thought explanation.\n\n## 4.3 Training Paradigm\n\n*Supervised fine-tuning (SFT).* These models are instruction-tuned versions based on their respective pre-trained Qwen2.5 checkpoints, with a focus on improving their ability to interpret and formalize complex mathematical statements expressed in natural language. The CriticLeanInstruct 4 dataset includes Critic data consisting of mathematical statements converted into formally verified theorem declarations in Lean 4, along with three times as much code and mathematics data for SFT (Supervised Fine-Tuning). We used the LLaMA-Factory [77] framework to facilitate the fine-tuning process and optimize model performance.\n\n*Reinforcement Learning Optimization (RL).* The recent success of R1-style methods has demonstrated the effectiveness of online RL using discrete, rule-based rewards [45]. In our pipeline, Qwen2.5 series and Qwen3 [52] series are further refined using reinforcement learning signals derived from both format validation of the generated critic data and consistency checking between model predictions and expert-labeled ground truth (GT) labels. Specifically, the RL training data consists of 4,000 Seed Data 4.1, where each example transforms a mathematical statement into a corresponding formal proof in Lean 4. Based on this dataset, we apply a rule-based RL approach to optimize the model’s capability in judgment reasoning. More specifically, we mainly utilize the GRPO [46] algorithm within the VeRL [47] reinforcement learning framework, whose optimization objective is:\n\n$$J_{\\text{online}}(\\pi_{\\theta}; \\mathcal{D}) = \\mathbb{E}_{x \\sim \\mathcal{D}, \\{y_i\\}_{i=1}^G \\sim \\pi_{\\theta_{\\text{old}}}(y|x)} \\left[ \\frac{1}{G} \\sum_{i=1}^G \\min \\left( \\frac{\\pi_{\\theta}(y_i|x)}{\\pi_{\\theta_{\\text{old}}}(y_i|x)} A_i, \\text{clip} \\left( \\frac{\\pi_{\\theta}(y_i|x)}{\\pi_{\\theta_{\\text{old}}}(y_i|x)}, 1 - \\epsilon, 1 + \\epsilon \\right) A_i \\right) - \\beta D_{\\text{KL}}(\\pi_{\\theta} || \\pi_{\\text{ref}}) \\right] \\quad (1)$$\n\nwhere  $G$  is group size, and  $A_i$  is advantage. The reward function is designed as follows&lt;sup>1&lt;/sup>:\n\n$$r_{\\text{accuracy}} = \\begin{cases} 1, & \\text{if judgement} = \\text{label} \\\\ 0, & \\text{if judgement} \\neq \\text{label} \\end{cases} \\quad (2)$$\n\n$$r_{\\text{format}} = \\begin{cases} 1, & \\text{if format is right} \\\\ 0, & \\text{if format is wrong} \\end{cases} \\quad (3)$$\n\n$$r_{\\text{final}} = \\min(r_{\\text{accuracy}}, r_{\\text{format}}) \\quad (4)$$\n\n\n---\n\n&lt;sup>1&lt;/sup>We do not include a length penalty in rewards to encourage longer thinking.## 5 Experiments\n\n### 5.1 Experimental Setup\n\n**Baseline Models.** For the closed-sourced API models, we select the following models: Claude35\\_Sonnet2 [2], Doubao-1.5-pro-32k [12], Gemini 2.5 Pro [50], GPT-4o-2024-11-20 [42]. We select a group of the most advanced open-source LLMs to serve as critic models for evaluation, which includes various reasoning models (DeepSeek-R1 [11], QwQ-32B [53], Qwen3-8B [52], Qwen3-14B [52], Qwen3-32B [52]), DeepSeek-Prover models [62] (DeepSeek-Prover-V1.5-RL, DeepSeek-Prover-V1.5-SFT), Llama-3.3-70B-Instruct [10] and several Qwen models (Qwen2.5-Coder-7B-Instruct [19], Qwen2.5-Coder-32B-Instruct [19], Qwen2.5-7B-Instruct [51], Qwen2.5-14B-Instruct [51] and Qwen2.5-32B-Instruct [51]).\n\n**CriticLeanGPT Models.** We further evaluate three variants from the Qwen2.5 series and Qwen3 series. These are instruction-based models fine-tuned specifically on either the CriticLeanInstruct 4 dataset or the RL-based clean critic Seed Data 4.1. All open-source models are inferred using the vLLM [21] framework with default inference parameters.\n\n### 5.2 Main Results\n\n#### 5.2.1 Evaluation of Critic Capability\n\nAs indicated in Table 2, the experimental results clearly demonstrate the effectiveness of the CriticLeanGPT models trained on our CriticLeanInstruct, in converting natural language mathematical statements into Lean 4 formal theorem declarations. Within the CriticLeanBench benchmark, our CriticLeanGPT models trained via supervised fine-tuning (SFT) and reinforcement learning (RL), along with their enhanced variants—outperform a range of closed-source API models, open-source models, and baseline models, highlighting distinct advantages. These outcomes yield several key insights: (1) Reasoning models excel in critical tasks, with Gemini 2.5 Pro, QwQ-32B, Qwen3-32B, and DeepSeek-R1 all attaining scores above 80. When compared to baseline models, our Qwen3-32B-RL model, optimized through RL, achieves a strong accuracy level, underscoring the efficacy of both our training methodology and dataset. (3) Our innovative mixed SFT strategy substantially boosts the performance of the Qwen2.5 family, with notable improvements observed across the 7B, 14B, and 32B models. (4) Additionally, SFT and RL significantly strengthen the models’ capacity to identify erroneous samples, as evidenced by higher true negative rates (TNR) and lower false negative rates (FNR)—a critical enhancement for accurate detection of incorrect formalizations, which is indispensable for effective critical tasks.\n\n### 5.3 Ablation Study\n\n#### 5.3.1 Effect of Reasoning Data\n\nWe conduct an ablation study on CriticLeanBench to evaluate the impact of different training strategies. As shown in Table 3, incorporating code and math reasoning data significantly improves performance across all model sizes compared to using Seed Data 4.1. Specifically, using the CriticLeanInstruct 4, which samples Critic and non-Critic data at a ratio of 1:3, leads to substantial gains, demonstrating that integrating diverse reasoning tasks enhances the critical reasoning capabilities of the model. This suggests that multi-task learning with math and code data improves the critique abilities of mathematical formalization.\n\n#### 5.3.2 Effect of SFT Dataset Size\n\nFigure 6 highlights a notable parameter-dependent relationship between the size of the SFT dataset and key reasoning performance. Across all model scales, performance improvements are observed through SFT, albeit with varying degrees of fluctuation depending on the training set size. Smaller models (e.g., 7B) exhibit more pronounced gains as the dataset expands, whereas larger models (e.g., 32B) demonstrate a less consistent trend, with marginal improvements at lower data volumes but substantial gains at higher data volumes. These findings align with prior studies [39, 78], underscoring the interplay between model capacity, data scale, and performance optimization in SFT scenarios. The results emphasize the need for tailored strategies to balance data efficiency and model generalization, particularly for large-scale architectures.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>ACC&lt;/th>\n&lt;th>TPR&lt;/th>\n&lt;th>FPR&lt;/th>\n&lt;th>TNR&lt;/th>\n&lt;th>FNR&lt;/th>\n&lt;th>Reasoning&lt;/th>\n&lt;th>Open-source&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"8\" style=\"text-align: center;\">&lt;b>SOTA LLMs&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Gemini-2.5-Pro&lt;/td>\n&lt;td>&lt;u>89.2&lt;/u>&lt;/td>\n&lt;td>&lt;u>95.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>4.4&lt;/u>&lt;/td>\n&lt;td>&lt;u>82.8&lt;/u>&lt;/td>\n&lt;td>&lt;u>17.2&lt;/u>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B&lt;/td>\n&lt;td>&lt;u>86.4&lt;/u>&lt;/td>\n&lt;td>93.6&lt;/td>\n&lt;td>6.4&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-32B&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>&lt;b>96.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>4.0&lt;/b>&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-235B-A22B&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;td>90.8&lt;/td>\n&lt;td>9.2&lt;/td>\n&lt;td>77.2&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>✓&lt;/td>",
      "numLines": 300,
      "startLine": 1,
      "totalLines": 1768
    }
  },
  "sourceToolAssistantUUID": "883cc291-59c3-478a-9d13-9d82eb6be7ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "9284ee5d-7996-40ce-b888-07982eef5b90",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Tool call

_source line 60 · 2026-05-27T20:38:31.110Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JUdGJc4WDofLjJczJNiuce`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/toolu_017tNQR36VFz5t8HzkqpKgwp.txt",
  "offset": 300,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9284ee5d-7996-40ce-b888-07982eef5b90",
  "isSidechain": false,
  "requestId": "req_011CbTibEaNzLhLPZdKuFkqa",
  "type": "assistant",
  "uuid": "0586caa4-e627-47df-a556-2b6603c51939",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnVWmGhAWHVboLhJ4Gs3bV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8363,
      "cache_read_input_tokens": 29464,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 29464,
          "cache_creation_input_tokens": 8363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8363
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

_source line 61 · 2026-05-27T20:38:31.117Z_

<details><summary>↩ Tool result · `toolu_01JUdGJc4WDofLjJczJNiuce`</summary>

```text
300	&lt;td>✓&lt;/td>
301	&lt;td>✓&lt;/td>
302	&lt;/tr>
303	&lt;tr>
304	&lt;td>Qwen3-14B&lt;/td>
305	&lt;td>83.6&lt;/td>
306	&lt;td>92.4&lt;/td>
307	&lt;td>7.6&lt;/td>
308	&lt;td>74.8&lt;/td>
309	&lt;td>25.2&lt;/td>
310	&lt;td>✓&lt;/td>
311	&lt;td>✓&lt;/td>
312	&lt;/tr>
313	&lt;tr>
314	&lt;td>Qwen3-8B&lt;/td>
315	&lt;td>79.8&lt;/td>
316	&lt;td>94.4&lt;/td>
317	&lt;td>5.6&lt;/td>
318	&lt;td>65.2&lt;/td>
319	&lt;td>34.8&lt;/td>
320	&lt;td>✓&lt;/td>
321	&lt;td>✓&lt;/td>
322	&lt;/tr>
323	&lt;tr>
324	&lt;td>Doubao-1.5-pro-32k&lt;/td>
325	&lt;td>78.4&lt;/td>
326	&lt;td>95.2&lt;/td>
327	&lt;td>4.8&lt;/td>
328	&lt;td>61.6&lt;/td>
329	&lt;td>38.4&lt;/td>
330	&lt;td>✗&lt;/td>
331	&lt;td>✗&lt;/td>
332	&lt;/tr>
333	&lt;tr>
334	&lt;td>Claude35-Sonnet&lt;/td>
335	&lt;td>74.2&lt;/td>
336	&lt;td>&lt;u>97.2&lt;/u>&lt;/td>
337	&lt;td>&lt;u>2.8&lt;/u>&lt;/td>
338	&lt;td>51.2&lt;/td>
339	&lt;td>48.8&lt;/td>
340	&lt;td>✗&lt;/td>
341	&lt;td>✗&lt;/td>
342	&lt;/tr>
343	&lt;tr>
344	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
345	&lt;td>73.0&lt;/td>
346	&lt;td>91.6&lt;/td>
347	&lt;td>8.4&lt;/td>
348	&lt;td>54.4&lt;/td>
349	&lt;td>45.6&lt;/td>
350	&lt;td>✗&lt;/td>
351	&lt;td>✓&lt;/td>
352	&lt;/tr>
353	&lt;tr>
354	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
355	&lt;td>71.6&lt;/td>
356	&lt;td>91.6&lt;/td>
357	&lt;td>8.4&lt;/td>
358	&lt;td>51.6&lt;/td>
359	&lt;td>48.4&lt;/td>
360	&lt;td>✗&lt;/td>
361	&lt;td>✓&lt;/td>
362	&lt;/tr>
363	&lt;tr>
364	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
365	&lt;td>68.2&lt;/td>
366	&lt;td>95.2&lt;/td>
367	&lt;td>4.8&lt;/td>
368	&lt;td>41.2&lt;/td>
369	&lt;td>58.8&lt;/td>
370	&lt;td>✗&lt;/td>
371	&lt;td>✓&lt;/td>
372	&lt;/tr>
373	&lt;tr>
374	&lt;td>GPT-4o-2024-11-20&lt;/td>
375	&lt;td>67.8&lt;/td>
376	&lt;td>95.6&lt;/td>
377	&lt;td>4.4&lt;/td>
378	&lt;td>40.0&lt;/td>
379	&lt;td>60.0&lt;/td>
380	&lt;td>✗&lt;/td>
381	&lt;td>✗&lt;/td>
382	&lt;/tr>
383	&lt;tr>
384	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
385	&lt;td>66.6&lt;/td>
386	&lt;td>80.4&lt;/td>
387	&lt;td>19.6&lt;/td>
388	&lt;td>52.8&lt;/td>
389	&lt;td>47.2&lt;/td>
390	&lt;td>✗&lt;/td>
391	&lt;td>✓&lt;/td>
392	&lt;/tr>
393	&lt;tr>
394	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
395	&lt;td>65.4&lt;/td>
396	&lt;td>88.4&lt;/td>
397	&lt;td>11.6&lt;/td>
398	&lt;td>42.4&lt;/td>
399	&lt;td>57.6&lt;/td>
400	&lt;td>✗&lt;/td>
401	&lt;td>✓&lt;/td>
402	&lt;/tr>
403	&lt;tr>
404	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
405	&lt;td>60.8&lt;/td>
406	&lt;td>89.6&lt;/td>
407	&lt;td>10.4&lt;/td>
408	&lt;td>32.0&lt;/td>
409	&lt;td>68.0&lt;/td>
410	&lt;td>✗&lt;/td>
411	&lt;td>✓&lt;/td>
412	&lt;/tr>
413	&lt;tr>
414	&lt;td>DeepSeek-Prover-V1.5-SFT&lt;/td>
415	&lt;td>52.4&lt;/td>
416	&lt;td>78.8&lt;/td>
417	&lt;td>21.2&lt;/td>
418	&lt;td>26.0&lt;/td>
419	&lt;td>74.0&lt;/td>
420	&lt;td>✗&lt;/td>
421	&lt;td>✓&lt;/td>
422	&lt;/tr>
423	&lt;tr>
424	&lt;td>DeepSeek-Prover-V1.5-RL&lt;/td>
425	&lt;td>50.0&lt;/td>
426	&lt;td>76.4&lt;/td>
427	&lt;td>23.6&lt;/td>
428	&lt;td>23.6&lt;/td>
429	&lt;td>76.4&lt;/td>
430	&lt;td>✗&lt;/td>
431	&lt;td>✓&lt;/td>
432	&lt;/tr>
433	&lt;tr>
434	&lt;td colspan="8" style="text-align: center;">&lt;b>CriticLeanGPT (Ours)&lt;/b>&lt;/td>
435	&lt;/tr>
436	&lt;tr>
437	&lt;td>Qwen3-8B-RL&lt;/td>
438	&lt;td>79.8&lt;/td>
439	&lt;td>90.0&lt;/td>
440	&lt;td>10.0&lt;/td>
441	&lt;td>72.0&lt;/td>
442	&lt;td>28.0&lt;/td>
443	&lt;td>✓&lt;/td>
444	&lt;td>✓&lt;/td>
445	&lt;/tr>
446	&lt;tr>
447	&lt;td>Qwen3-14B-RL&lt;/td>
448	&lt;td>84.8&lt;/td>
449	&lt;td>91.6&lt;/td>
450	&lt;td>8.4&lt;/td>
451	&lt;td>78.0&lt;/td>
452	&lt;td>22.0&lt;/td>
453	&lt;td>✓&lt;/td>
454	&lt;td>✓&lt;/td>
455	&lt;/tr>
456	&lt;tr>
457	&lt;td>Qwen3-32B-RL&lt;/td>
458	&lt;td>&lt;b>87.0&lt;/b>&lt;/td>
459	&lt;td>88.4&lt;/td>
460	&lt;td>11.6&lt;/td>
461	&lt;td>&lt;u>85.6&lt;/u>&lt;/td>
462	&lt;td>&lt;u>14.4&lt;/u>&lt;/td>
463	&lt;td>✓&lt;/td>
464	&lt;td>✓&lt;/td>
465	&lt;/tr>
466	&lt;tr>
467	&lt;td>Qwen2.5-7B-Instruct-RL&lt;/td>
468	&lt;td>68.6&lt;/td>
469	&lt;td>85.6&lt;/td>
470	&lt;td>14.4&lt;/td>
471	&lt;td>51.6&lt;/td>
472	&lt;td>48.4&lt;/td>
473	&lt;td>✗&lt;/td>
474	&lt;td>✓&lt;/td>
475	&lt;/tr>
476	&lt;tr>
477	&lt;td>Qwen2.5-14B-Instruct-RL&lt;/td>
478	&lt;td>69.4&lt;/td>
479	&lt;td>85.2&lt;/td>
480	&lt;td>14.8&lt;/td>
481	&lt;td>53.6&lt;/td>
482	&lt;td>46.4&lt;/td>
483	&lt;td>✗&lt;/td>
484	&lt;td>✓&lt;/td>
485	&lt;/tr>
486	&lt;tr>
487	&lt;td>Qwen2.5-32B-Instruct-RL&lt;/td>
488	&lt;td>72.0&lt;/td>
489	&lt;td>60.4&lt;/td>
490	&lt;td>39.6&lt;/td>
491	&lt;td>&lt;b>83.6&lt;/b>&lt;/td>
492	&lt;td>&lt;b>16.4&lt;/b>&lt;/td>
493	&lt;td>✗&lt;/td>
494	&lt;td>✓&lt;/td>
495	&lt;/tr>
496	&lt;tr>
497	&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>
498	&lt;td>69.8&lt;/td>
499	&lt;td>94.4&lt;/td>
500	&lt;td>5.6&lt;/td>
501	&lt;td>45.2&lt;/td>
502	&lt;td>54.8&lt;/td>
503	&lt;td>✗&lt;/td>
504	&lt;td>✓&lt;/td>
505	&lt;/tr>
506	&lt;tr>
507	&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>
508	&lt;td>70.6&lt;/td>
509	&lt;td>83.6&lt;/td>
510	&lt;td>16.4&lt;/td>
511	&lt;td>57.6&lt;/td>
512	&lt;td>42.4&lt;/td>
513	&lt;td>✗&lt;/td>
514	&lt;td>✓&lt;/td>
515	&lt;/tr>
516	&lt;tr>
517	&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>
518	&lt;td>76.2&lt;/td>
519	&lt;td>85.2&lt;/td>
520	&lt;td>14.8&lt;/td>
521	&lt;td>67.2&lt;/td>
522	&lt;td>32.8&lt;/td>
523	&lt;td>✗&lt;/td>
524	&lt;td>✓&lt;/td>
525	&lt;/tr>
526	&lt;tr>
527	&lt;td>Qwen2.5-7B-Instruct-SFT-RL&lt;/td>
528	&lt;td>68.2&lt;/td>
529	&lt;td>90.4&lt;/td>
530	&lt;td>9.6&lt;/td>
531	&lt;td>46.0&lt;/td>
532	&lt;td>54.0&lt;/td>
533	&lt;td>✗&lt;/td>
534	&lt;td>✓&lt;/td>
535	&lt;/tr>
536	&lt;tr>
537	&lt;td>Qwen2.5-14B-Instruct-SFT-RL&lt;/td>
538	&lt;td>74.6&lt;/td>
539	&lt;td>81.6&lt;/td>
540	&lt;td>18.4&lt;/td>
541	&lt;td>67.6&lt;/td>
542	&lt;td>32.4&lt;/td>
543	&lt;td>✗&lt;/td>
544	&lt;td>✓&lt;/td>
545	&lt;/tr>
546	&lt;tr>
547	&lt;td>Qwen2.5-32B-Instruct-SFT-RL&lt;/td>
548	&lt;td>78.6&lt;/td>
549	&lt;td>88.0&lt;/td>
550	&lt;td>12.0&lt;/td>
551	&lt;td>69.2&lt;/td>
552	&lt;td>30.8&lt;/td>
553	&lt;td>✗&lt;/td>
554	&lt;td>✓&lt;/td>
555	&lt;/tr>
556	&lt;/tbody>
557	&lt;/table>
558	
559	**Table 2 Performance on CriticLeanBench.** The best, the second-best and the third-best scores for each indicator are shown in box, **bold** and underlined, respectively.&lt;table border="1">
560	&lt;thead>
561	&lt;tr>
562	&lt;th>Model&lt;/th>
563	&lt;th>ACC&lt;/th>
564	&lt;th>TPR&lt;/th>
565	&lt;th>FPR&lt;/th>
566	&lt;th>TNR&lt;/th>
567	&lt;th>FNR&lt;/th>
568	&lt;/tr>
569	&lt;/thead>
570	&lt;tbody>
571	&lt;tr>
572	&lt;td colspan="6" style="text-align: center;">&lt;b>7B Size Models&lt;/b>&lt;/td>
573	&lt;/tr>
574	&lt;tr>
575	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
576	&lt;td>60.8&lt;/td>
577	&lt;td>89.6&lt;/td>
578	&lt;td>10.4&lt;/td>
579	&lt;td>32.0&lt;/td>
580	&lt;td>68.0&lt;/td>
581	&lt;/tr>
582	&lt;tr>
583	&lt;td>Qwen2.5-7B-Instruct-SFT(Critic Only)&lt;/td>
584	&lt;td>64.0&lt;/td>
585	&lt;td>70.8&lt;/td>
586	&lt;td>29.2&lt;/td>
587	&lt;td>&lt;span style="border: 1px solid black;">57.2&lt;/span>&lt;/td>
588	&lt;td>&lt;span style="border: 1px solid black;">42.8&lt;/span>&lt;/td>
589	&lt;/tr>
590	&lt;tr>
591	&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>
592	&lt;td>&lt;span style="border: 1px solid black;">69.8&lt;/span>&lt;/td>
593	&lt;td>&lt;span style="border: 1px solid black;">94.4&lt;/span>&lt;/td>
594	&lt;td>&lt;span style="border: 1px solid black;">5.6&lt;/span>&lt;/td>
595	&lt;td>45.2&lt;/td>
596	&lt;td>54.8&lt;/td>
597	&lt;/tr>
598	&lt;tr>
599	&lt;td colspan="6" style="text-align: center;">&lt;b>14B Size Models&lt;/b>&lt;/td>
600	&lt;/tr>
601	&lt;tr>
602	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
603	&lt;td>66.6&lt;/td>
604	&lt;td>80.4&lt;/td>
605	&lt;td>19.6&lt;/td>
606	&lt;td>52.8&lt;/td>
607	&lt;td>47.2&lt;/td>
608	&lt;/tr>
609	&lt;tr>
610	&lt;td>Qwen2.5-14B-Instruct-SFT(Critic Only)&lt;/td>
611	&lt;td>67.4&lt;/td>
612	&lt;td>80.8&lt;/td>
613	&lt;td>19.2&lt;/td>
614	&lt;td>54.0&lt;/td>
615	&lt;td>46.0&lt;/td>
616	&lt;/tr>
617	&lt;tr>
618	&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>
619	&lt;td>&lt;span style="border: 1px solid black;">70.6&lt;/span>&lt;/td>
620	&lt;td>&lt;span style="border: 1px solid black;">83.6&lt;/span>&lt;/td>
621	&lt;td>&lt;span style="border: 1px solid black;">16.4&lt;/span>&lt;/td>
622	&lt;td>&lt;span style="border: 1px solid black;">57.6&lt;/span>&lt;/td>
623	&lt;td>&lt;span style="border: 1px solid black;">42.4&lt;/span>&lt;/td>
624	&lt;/tr>
625	&lt;tr>
626	&lt;td colspan="6" style="text-align: center;">&lt;b>32B Size Models&lt;/b>&lt;/td>
627	&lt;/tr>
628	&lt;tr>
629	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
630	&lt;td>73.0&lt;/td>
631	&lt;td>&lt;span style="border: 1px solid black;">91.6&lt;/span>&lt;/td>
632	&lt;td>&lt;span style="border: 1px solid black;">8.4&lt;/span>&lt;/td>
633	&lt;td>54.4&lt;/td>
634	&lt;td>45.6&lt;/td>
635	&lt;/tr>
636	&lt;tr>
637	&lt;td>Qwen2.5-32B-Instruct-SFT(Critic Only)&lt;/td>
638	&lt;td>71.0&lt;/td>
639	&lt;td>72.0&lt;/td>
640	&lt;td>28.0&lt;/td>
641	&lt;td>&lt;span style="border: 1px solid black;">70.0&lt;/span>&lt;/td>
642	&lt;td>&lt;span style="border: 1px solid black;">30.0&lt;/span>&lt;/td>
643	&lt;/tr>
644	&lt;tr>
645	&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>
646	&lt;td>&lt;span style="border: 1px solid black;">76.2&lt;/span>&lt;/td>
647	&lt;td>85.2&lt;/td>
648	&lt;td>14.8&lt;/td>
649	&lt;td>67.2&lt;/td>
650	&lt;td>32.8&lt;/td>
651	&lt;/tr>
652	&lt;/tbody>
653	&lt;/table>
654	
655	**Table 3 Comparison of model performance under different training strategies:** base model, SFT on Critic data only, and SFT on combined Critic, code, and math data. The best score for each indicator is shown in box.
656	
657	## 5.4 Analysis
658	
659	### 5.4.1 Scaling Analysis
660	
661	We evaluate the performance of Qwen series models on CriticLeanBench across different model scales, including Qwen2.5-Coder, Qwen2.5-Instruct, Qwen2.5-Instruct-SFT, Qwen2.5-Instruct-SFT-RL, Qwen3, and Qwen3-RL. The results in Figure 4 show that the performance improves consistently as the model size increases, demonstrating a clear scaling law of LLMs on CriticLeanBench.
662	
663	### 5.4.2 Effect of Pass@k
664	
665	The Pass@k metric serves as a means to identify the highest-quality answers from multi-modal large language models (MLLMs) for final responses, highlighting the models’ potential for enhancement through post-training techniques like Reinforcement Learning from Human Feedback (RLHF [25]) and Gradient Penalty Policy Optimization (GRPO [46]). In this study, Pass@k evaluations were conducted on Qwen2.5-7B-Instruct, Qwen2.5-7B-Instruct-SFT-RL, Qwen3-8B, and Qwen3-8B-RL using CriticLeanBench, with k set to 8 and 32, and evaluation metrics including Accuracy (ACC), True Positive Rate (TPR), and True Negative Rate (TNR).
666	
667	As shown in Figure 5, we observe that models subjected to Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) achieve better overall performance. Considering Pass@32, the Accuracy of Qwen2.5-7B-Instruct is outperformed by that of Qwen2.5-7B-Instruct-SFT-RL, which has undergone SFT and RL processing, leading to a notable improvement in the overall correctness rate. Regarding the True Negative Rate, models without SFT and RL processing are more prone to misclassifying incorrect samples as correct, whereas processed models effectively mitigate such errors; this is evident in the higher TNR of Qwen2.5-7B-Instruct-SFT-RL compared to Qwen2.5-7B-Instruct at Pass@32, reducing the likelihood of
668	
669	**Figure 6 Comparison of model performance under different amounts of SFT data:** base model, CriticLeanInstruct(16K), and CriticLeanInstruct.**Figure 4** Scaling Analysis of LLMs on CriticLeanBench.  $\hat{\square}$  denoted closed-source LLMs.
670	
671	such misclassifications. A similar trend is observed in Qwen3-8B. Additionally, all models exhibit improved performance as  $k$  increases, suggesting that SFT- and RL-optimized models can more effectively select high-quality answers when provided with more candidate responses.
672	
673	## 6 FineLeanCorpus
674	
675	To construct the FineLeanCorpus, we began by aggregating a vast and diverse collection of natural language mathematical problems. Sourcing from a wide array of materials, including high school olympiad datasets (e.g., AoPS, BlueMO), standard high school curricula (e.g., TAL-SCQ5), and undergraduate-level challenges (e.g., Omni-MATH), we ensured an extensive initial distribution in both the mathematical domain and difficulty. The first step in our process was to standardize this heterogeneous collection into a uniform, proof-based format, making each problem compatible with the Lean 4 theorem prover and ready for the subsequent formalization pipeline.
676	
677	These standardized problems were then subjected to a rigorous, gated auto-formalization process powered by our CriticLean framework (Figure 1). The Kimina-Autoformalizer-7B model first generates a candidate formal statement. This statement must pass a syntactic check via the Lean 4 compiler; failure leads to regeneration. A successful compilation is followed by a semantic correctness check from our CriticLeanGPT model, with rejection also triggering a new attempt. This regenerative approach is critical, maximizing the yield from our source corpus by iteratively seeking a valid formalization. Finally, to further enhance precision, we apply a final filtering stage using another,
678	
679	&lt;table border="1">
680	&lt;thead>
681	&lt;tr>
682	&lt;th>Statistics&lt;/th>
683	&lt;th>Number&lt;/th>
684	&lt;/tr>
685	&lt;/thead>
686	&lt;tbody>
687	&lt;tr>
688	&lt;td>#Problems&lt;/td>
689	&lt;td>285957&lt;/td>
690	&lt;/tr>
691	&lt;tr>
692	&lt;td>&lt;b>Length&lt;/b>&lt;/td>
693	&lt;td>&lt;/td>
694	&lt;/tr>
695	&lt;tr>
696	&lt;td>&lt;i>Statement&lt;/i>&lt;/td>
697	&lt;td>&lt;/td>
698	&lt;/tr>
699	&lt;tr>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0586caa4-e627-47df-a556-2b6603c51939",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "f35d4de2-f4c5-4e37-b1d2-8846690ad688",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/toolu_017tNQR36VFz5t8HzkqpKgwp.txt",
      "content": "&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-14B&lt;/td>\n&lt;td>83.6&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>7.6&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>25.2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-8B&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>94.4&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>34.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Doubao-1.5-pro-32k&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>95.2&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Claude35-Sonnet&lt;/td>\n&lt;td>74.2&lt;/td>\n&lt;td>&lt;u>97.2&lt;/u>&lt;/td>\n&lt;td>&lt;u>2.8&lt;/u>&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>48.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>48.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>95.2&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>41.2&lt;/td>\n&lt;td>58.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-2024-11-20&lt;/td>\n&lt;td>67.8&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>4.4&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>19.6&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>65.4&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>57.6&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>60.8&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>10.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V1.5-SFT&lt;/td>\n&lt;td>52.4&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V1.5-RL&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"8\" style=\"text-align: center;\">&lt;b>CriticLeanGPT (Ours)&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-8B-RL&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-14B-RL&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>22.0&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-32B-RL&lt;/td>\n&lt;td>&lt;b>87.0&lt;/b>&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;td>&lt;u>85.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>14.4&lt;/u>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-RL&lt;/td>\n&lt;td>68.6&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>14.4&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>48.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-RL&lt;/td>\n&lt;td>69.4&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-RL&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>60.4&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>&lt;b>83.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>16.4&lt;/b>&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>94.4&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>\n&lt;td>70.6&lt;/td>\n&lt;td>83.6&lt;/td>\n&lt;td>16.4&lt;/td>\n&lt;td>57.6&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT-RL&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT-RL&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>18.4&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT-RL&lt;/td>\n&lt;td>78.6&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 2 Performance on CriticLeanBench.** The best, the second-best and the third-best scores for each indicator are shown in box, **bold** and underlined, respectively.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>ACC&lt;/th>\n&lt;th>TPR&lt;/th>\n&lt;th>FPR&lt;/th>\n&lt;th>TNR&lt;/th>\n&lt;th>FNR&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>7B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>60.8&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>10.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>64.0&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>29.2&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">57.2&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">42.8&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">69.8&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">94.4&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">5.6&lt;/span>&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>14B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>19.6&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>67.4&lt;/td>\n&lt;td>80.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">70.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">83.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">16.4&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">57.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">42.4&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>32B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">91.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">8.4&lt;/span>&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>71.0&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">70.0&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">30.0&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">76.2&lt;/span>&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3 Comparison of model performance under different training strategies:** base model, SFT on Critic data only, and SFT on combined Critic, code, and math data. The best score for each indicator is shown in box.\n\n## 5.4 Analysis\n\n### 5.4.1 Scaling Analysis\n\nWe evaluate the performance of Qwen series models on CriticLeanBench across different model scales, including Qwen2.5-Coder, Qwen2.5-Instruct, Qwen2.5-Instruct-SFT, Qwen2.5-Instruct-SFT-RL, Qwen3, and Qwen3-RL. The results in Figure 4 show that the performance improves consistently as the model size increases, demonstrating a clear scaling law of LLMs on CriticLeanBench.\n\n### 5.4.2 Effect of Pass@k\n\nThe Pass@k metric serves as a means to identify the highest-quality answers from multi-modal large language models (MLLMs) for final responses, highlighting the models’ potential for enhancement through post-training techniques like Reinforcement Learning from Human Feedback (RLHF [25]) and Gradient Penalty Policy Optimization (GRPO [46]). In this study, Pass@k evaluations were conducted on Qwen2.5-7B-Instruct, Qwen2.5-7B-Instruct-SFT-RL, Qwen3-8B, and Qwen3-8B-RL using CriticLeanBench, with k set to 8 and 32, and evaluation metrics including Accuracy (ACC), True Positive Rate (TPR), and True Negative Rate (TNR).\n\nAs shown in Figure 5, we observe that models subjected to Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) achieve better overall performance. Considering Pass@32, the Accuracy of Qwen2.5-7B-Instruct is outperformed by that of Qwen2.5-7B-Instruct-SFT-RL, which has undergone SFT and RL processing, leading to a notable improvement in the overall correctness rate. Regarding the True Negative Rate, models without SFT and RL processing are more prone to misclassifying incorrect samples as correct, whereas processed models effectively mitigate such errors; this is evident in the higher TNR of Qwen2.5-7B-Instruct-SFT-RL compared to Qwen2.5-7B-Instruct at Pass@32, reducing the likelihood of\n\n**Figure 6 Comparison of model performance under different amounts of SFT data:** base model, CriticLeanInstruct(16K), and CriticLeanInstruct.**Figure 4** Scaling Analysis of LLMs on CriticLeanBench.  $\\hat{\\square}$  denoted closed-source LLMs.\n\nsuch misclassifications. A similar trend is observed in Qwen3-8B. Additionally, all models exhibit improved performance as  $k$  increases, suggesting that SFT- and RL-optimized models can more effectively select high-quality answers when provided with more candidate responses.\n\n## 6 FineLeanCorpus\n\nTo construct the FineLeanCorpus, we began by aggregating a vast and diverse collection of natural language mathematical problems. Sourcing from a wide array of materials, including high school olympiad datasets (e.g., AoPS, BlueMO), standard high school curricula (e.g., TAL-SCQ5), and undergraduate-level challenges (e.g., Omni-MATH), we ensured an extensive initial distribution in both the mathematical domain and difficulty. The first step in our process was to standardize this heterogeneous collection into a uniform, proof-based format, making each problem compatible with the Lean 4 theorem prover and ready for the subsequent formalization pipeline.\n\nThese standardized problems were then subjected to a rigorous, gated auto-formalization process powered by our CriticLean framework (Figure 1). The Kimina-Autoformalizer-7B model first generates a candidate formal statement. This statement must pass a syntactic check via the Lean 4 compiler; failure leads to regeneration. A successful compilation is followed by a semantic correctness check from our CriticLeanGPT model, with rejection also triggering a new attempt. This regenerative approach is critical, maximizing the yield from our source corpus by iteratively seeking a valid formalization. Finally, to further enhance precision, we apply a final filtering stage using another,\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Statistics&lt;/th>\n&lt;th>Number&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>#Problems&lt;/td>\n&lt;td>285957&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Length&lt;/b>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;i>Statement&lt;/i>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>",
      "numLines": 400,
      "startLine": 300,
      "totalLines": 1768
    }
  },
  "sourceToolAssistantUUID": "0586caa4-e627-47df-a556-2b6603c51939",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-27T20:38:37.005Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PBxS8UvdUCZznkYvYpfJzR`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/toolu_017tNQR36VFz5t8HzkqpKgwp.txt",
  "offset": 700,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f35d4de2-f4c5-4e37-b1d2-8846690ad688",
  "isSidechain": false,
  "requestId": "req_011CbTibe5Vpia3ff7cpyR2S",
  "type": "assistant",
  "uuid": "157a4d86-a86e-47b2-b257-d791c1fe01c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X51BzKBjojnBUTWcCBUeCG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5889,
      "cache_read_input_tokens": 37827,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 37827,
          "cache_creation_input_tokens": 5889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5889
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

_source line 63 · 2026-05-27T20:38:37.017Z_

<details><summary>↩ Tool result · `toolu_01PBxS8UvdUCZznkYvYpfJzR`</summary>

```text
700	&lt;td>maximum length&lt;/td>
701	&lt;td>2980 tokens&lt;/td>
702	&lt;/tr>
703	&lt;tr>
704	&lt;td>minimum length&lt;/td>
705	&lt;td>9 tokens&lt;/td>
706	&lt;/tr>
707	&lt;tr>
708	&lt;td>avg length&lt;/td>
709	&lt;td>78.4 tokens&lt;/td>
710	&lt;/tr>
711	&lt;tr>
712	&lt;td>&lt;i>Lean Result(success)&lt;/i>&lt;/td>
713	&lt;td>&lt;/td>
714	&lt;/tr>
715	&lt;tr>
716	&lt;td>maximum length&lt;/td>
717	&lt;td>768 tokens&lt;/td>
718	&lt;/tr>
719	&lt;tr>
720	&lt;td>minimum length&lt;/td>
721	&lt;td>14 tokens&lt;/td>
722	&lt;/tr>
723	&lt;tr>
724	&lt;td>avg length&lt;/td>
725	&lt;td>87.8 tokens&lt;/td>
726	&lt;/tr>
727	&lt;/tbody>
728	&lt;/table>
729	
730	**Table 5** Dataset statistics of FineLeanCorpus.**Figure 5** Performance on CriticLeanBench using **Pass@k** metrics, where **k = 8** (left) and **k = 32** (right).
731	
732	&lt;table border="1">
733	&lt;thead>
734	&lt;tr>
735	&lt;th>Dataset&lt;/th>
736	&lt;th>Difficulty Level&lt;/th>
737	&lt;th>Size&lt;/th>
738	&lt;/tr>
739	&lt;/thead>
740	&lt;tbody>
741	&lt;tr>
742	&lt;td>AOPs [35]&lt;/td>
743	&lt;td>High School Olympiad&lt;/td>
744	&lt;td>199982&lt;/td>
745	&lt;/tr>
746	&lt;tr>
747	&lt;td>DeepMath-103k [15]&lt;/td>
748	&lt;td>Diverse&lt;/td>
749	&lt;td>28538&lt;/td>
750	&lt;/tr>
751	&lt;tr>
752	&lt;td>NuminaMath-TIR [24]&lt;/td>
753	&lt;td>High School&lt;/td>
754	&lt;td>22847&lt;/td>
755	&lt;/tr>
756	&lt;tr>
757	&lt;td>DeepTheorem [74]&lt;/td>
758	&lt;td>High School Olympiad&lt;/td>
759	&lt;td>15131&lt;/td>
760	&lt;/tr>
761	&lt;tr>
762	&lt;td>DeepScaleR [34]&lt;/td>
763	&lt;td>High School Olympiad&lt;/td>
764	&lt;td>11544&lt;/td>
765	&lt;/tr>
766	&lt;tr>
767	&lt;td>DAPO-Math-17k [66]&lt;/td>
768	&lt;td>High School&lt;/td>
769	&lt;td>4078&lt;/td>
770	&lt;/tr>
771	&lt;tr>
772	&lt;td>Omni-MATH [8]&lt;/td>
773	&lt;td>Undergraduate&lt;/td>
774	&lt;td>1176&lt;/td>
775	&lt;/tr>
776	&lt;tr>
777	&lt;td>IneqMath [20]&lt;/td>
778	&lt;td>High School Olympiad&lt;/td>
779	&lt;td>963&lt;/td>
780	&lt;/tr>
781	&lt;tr>
782	&lt;td>BlueMO [73]&lt;/td>
783	&lt;td>High School Olympiad&lt;/td>
784	&lt;td>616&lt;/td>
785	&lt;/tr>
786	&lt;tr>
787	&lt;td>TAL-SCQ5K [37]&lt;/td>
788	&lt;td>High School&lt;/td>
789	&lt;td>393&lt;/td>
790	&lt;/tr>
791	&lt;tr>
792	&lt;td>OnlineMathContest&lt;/td>
793	&lt;td>High School&lt;/td>
794	&lt;td>70&lt;/td>
795	&lt;/tr>
796	&lt;tr>
797	&lt;td>Multi-Source Math Competition&lt;/td>
798	&lt;td>High School Olympiad&lt;/td>
799	&lt;td>619&lt;/td>
800	&lt;/tr>
801	&lt;/tbody>
802	&lt;/table>
803	
804	**Table 4** Overview of different sources for FineLeanCorpus.
805	
806	higher-performance CriticLeanGPT model. Manual validation indicates that this step is expected to eliminate 74.7% of the remaining incorrect formalizations. The resulting corpus is characterized by its expressive range: natural language statements vary from a concise 9 tokens to a complex 2,980 tokens (avg. 78.4), while their corresponding Lean formalizations span from 14 to 768 tokens (avg. 87.8), reflecting the deep spectrum of complexity successfully captured by our pipeline.
807	
808	To further analyze the differences between our FineLeanCorpus dataset and the Lean-Workbook, we employed the templates from Appendix J and Appendix I to assess the difficulty levels and classify the mathematical domains of the datasets using Doubao-1.5-pro [12]. A comparative analysis of our proposed FineLeanCorpus against Lean-Workbook (Figure 7, Figure 8, Table 4 and Table 5) reveals two fundamental advancements: (1) Scale and Coverage: Our corpus provides a significant quantitative expansion in both problem difficulty and domain coverage. This expansion is evident not only across nearly the entire difficulty spectrum—offering a much richer data pool for training foundational skills—but also in the substantial augmentation of high-volume domains like Intermediate Algebra and Elementary Number Theory. (2) FineLeanCorpus exhibits a more diverse and structurally balanced profile, achieved by collecting natural language statements from numerous sources. From a difficulty perspective, it features a multimodal distribution with substantial problem counts at several distinct complexity points, in stark contrast to the unimodal distribution of Lean-Workbook. This characteristic is crucial for mitigating model overfitting to a narrow complexity band. From a domain perspective, it substantially reinforces previously underrepresented areas. For instance, categories such as Analytic Geometry and Integral Calculus are significantly expanded, while niche topics like Algorithms and Graph Theory are also robustly augmented. This targeted enrichment transforms sparsely sampled topics into well-supported, learnable sub-domains, yielding a more comprehensive dataset designed to fosterholistic reasoning capabilities. More details regarding our FineLeanCorpus dataset, including its fine-grained mathematical domain distribution (see Appendix A), are provided for further analysis.
809	
810	Furthermore, to push the boundaries of current models and foster research into the upper echelons of mathematical reasoning, we have curated a specialized training subset from FineLeanCorpus, which we designate as Diamond. This subset comprises 36,033 problems with a difficulty rating exceeding 5. The purpose of this high-difficulty training set is to create a demanding training environment that fosters the development of the sophisticated, multi-step reasoning required to tackle the most formidable mathematical problems. A detailed breakdown of the mathematical domain distribution within this subset is provided in table 11.
811	
812	&lt;table border="1">
813	&lt;thead>
814	&lt;tr>
815	&lt;th>Dataset&lt;/th>
816	&lt;th>Source&lt;/th>
817	&lt;th>Theorems&lt;/th>
818	&lt;th>Level&lt;/th>
819	&lt;th>Detailed Critic Process&lt;/th>
820	&lt;th>Difficulty Profile&lt;/th>
821	&lt;th>Topic Diversity&lt;/th>
822	&lt;/tr>
823	&lt;/thead>
824	&lt;tbody>
825	&lt;tr>
826	&lt;td>Lean-Workbook [65]&lt;/td>
827	&lt;td>Synthetic&lt;/td>
828	&lt;td>140K&lt;/td>
829	&lt;td>Undergraduate&lt;/td>
830	&lt;td>Opaque&lt;/td>
831	&lt;td>Avg: 3.70&lt;br/>Top-tier (&lt;math>\geq 6&lt;/math>): 7.81%&lt;/td>
832	&lt;td>Highly Skewed&lt;/td>
833	&lt;/tr>
834	&lt;tr>
835	&lt;td>FineLeanCorpus (ours)&lt;/td>
836	&lt;td>Synthetic&lt;/td>
837	&lt;td>285K&lt;/td>
838	&lt;td>Diverse&lt;/td>
839	&lt;td>Transparent&lt;/td>
840	&lt;td>Avg: 3.24&lt;br/>Top-tier (&lt;math>\geq 6&lt;/math>): 11.10%&lt;/td>
841	&lt;td>Balanced &amp; Diverse&lt;/td>
842	&lt;/tr>
843	&lt;/tbody>
844	&lt;/table>
845	
846	**Table 6** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.
847	
848	**Figure 7** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.
849	
850	## 6.1 Analysis on CriticLean Pipeline
851	
852	As shown in Table 7, our autoformalization pipeline significantly improves accuracy. We selected 50 problems from the Omni-MATH and applied the following three formalization strategies, with the correctness of all outputs confirmed by manual human inspection.
853	
854	Our baseline model, Kimina-Autoformalizer-7B, is used in each strategy: (1) a **Single Pass** baseline (38.0% accuracy); (2) a **Compiler Feedback** loop, where the model regenerates formalizations until they successfully compile (54.0% accuracy); (3) our **CriticLean Pipeline**, which extends this process, regenerating formalizations until they both compile successfully and are validated by our integrated **CriticLeanGPT Model** (84.0% accuracy).
855	
856	While compiler feedback resolves syntactical errors, it fails to detect logical flaws. Our pipeline addresses this gap. The integration of critic model, which performs deeper semantic and logical validation, is directly
857	
858	&lt;table border="1">
859	&lt;thead>
860	&lt;tr>
861	&lt;th>Model&lt;/th>
862	&lt;th>AVG&lt;/th>
863	&lt;/tr>
864	&lt;/thead>
865	&lt;tbody>
866	&lt;tr>
867	&lt;td>Kimina-Autoformalizer-7B&lt;/td>
868	&lt;td>38.0&lt;/td>
869	&lt;/tr>
870	&lt;tr>
871	&lt;td>Kimina-Autoformalizer-7B (Compiler)&lt;/td>
872	&lt;td>54.0&lt;/td>
873	&lt;/tr>
874	&lt;tr>
875	&lt;td>Kimina-Autoformalizer-7B (CriticLean)&lt;/td>
876	&lt;td>84.0&lt;/td>
877	&lt;/tr>
878	&lt;/tbody>
879	&lt;/table>
880	
881	**Table 7** Human evaluation accuracy results for autoformalization performance: The best score is highlighted in *box*.**Figure 8** Math Domain Distributions: FineLeanCorpus vs. Lean-Workbook.
882	
883	&lt;table border="1">
884	&lt;thead>
885	&lt;tr>
886	&lt;th># Attempt&lt;/th>
887	&lt;th>1&lt;/th>
888	&lt;th>5&lt;/th>
889	&lt;th>10&lt;/th>
890	&lt;th>50&lt;/th>
891	&lt;th>100&lt;/th>
892	&lt;th>200&lt;/th>
893	&lt;/tr>
894	&lt;/thead>
895	&lt;tbody>
896	&lt;tr>
897	&lt;td>Count / Ratio&lt;/td>
898	&lt;td>63 / 12.6%&lt;/td>
899	&lt;td>137 / 27.4%&lt;/td>
900	&lt;td>170 / 34.0%&lt;/td>
901	&lt;td>229 / 45.8%&lt;/td>
902	&lt;td>245 / 49.0%&lt;/td>
903	&lt;td>264 / 52.8%&lt;/td>
904	&lt;/tr>
905	&lt;/tbody>
906	&lt;/table>
907	
908	**Table 8 Effectiveness of the Multi-Attempt Strategy on Formalization Yield.** The table shows the cumulative number of successfully formalized problems retained by the critic model as the attempt limit increases. Statistics are from a 500-problem sample.
909	
910	&lt;table border="1">
911	&lt;thead>
912	&lt;tr>
913	&lt;th>Dataset&lt;/th>
914	&lt;th>Accuracy&lt;/th>
915	&lt;th>Dataset&lt;/th>
916	&lt;th>Accuracy&lt;/th>
917	&lt;th>Dataset&lt;/th>
918	&lt;th>Accuracy&lt;/th>
919	&lt;/tr>
920	&lt;/thead>
921	&lt;tbody>
922	&lt;tr>
923	&lt;td>NuminaMath-TIR [24]&lt;/td>
924	&lt;td>78%&lt;/td>
925	&lt;td>IneqMath [20]&lt;/td>
926	&lt;td>96%&lt;/td>
927	&lt;td>BlueMO [73]&lt;/td>
928	&lt;td>86%&lt;/td>
929	&lt;/tr>
930	&lt;tr>
931	&lt;td>DeepMath-103k [16]&lt;/td>
932	&lt;td>84%&lt;/td>
933	&lt;td>DAPO-Math-17k [66]&lt;/td>
934	&lt;td>69%&lt;/td>
935	&lt;td>OnlineMathContest&lt;/td>
936	&lt;td>88%&lt;/td>
937	&lt;/tr>
938	&lt;tr>
939	&lt;td>AOPs [35]&lt;/td>
940	&lt;td>73%&lt;/td>
941	&lt;td>TAL-SCQ5K [37]&lt;/td>
942	&lt;td>75%&lt;/td>
943	&lt;td>Omni-MATH [8]&lt;/td>
944	&lt;td>84%&lt;/td>
945	&lt;/tr>
946	&lt;tr>
947	&lt;td>DeepTheorem [74]&lt;/td>
948	&lt;td>100%&lt;/td>
949	&lt;td>DeepScaleR [34]&lt;/td>
950	&lt;td>100%&lt;/td>
951	&lt;td>&lt;/td>
952	&lt;td>&lt;/td>
953	&lt;/tr>
954	&lt;/tbody>
955	&lt;/table>
956	
957	**Table 9** Human evaluation results of different sources.
958	
959	responsible for the accuracy increase from 54.0% to 84.0%. By filtering out plausible but incorrect formalizations, our method provides a more robust path toward reliable autoformalization. These manually-verified results present strong empirical evidence for the efficacy of our approach.
960	
961	Table 8 shows our pipeline achieved a 52.8% success rate across 500 problems, where success required passing both syntactic validation and our critic model’s semantic check. The value of our multi-attempt strategy is evident: while only 12.6% of samples passed on the first try, the pipeline successfully recovered an additional 40.2% that would be discarded by single-pass systems. Conversely, the 47.2% failure rate within the 200-attempt limit highlights a fundamental bottleneck: the pipeline’s performance is ultimately constrained by the base auto-formalization model’s ability to produce a candidate our critic can approve.
962	
963	Moreover, as shown in Table 9, we also provide the human evaluation results of different sources. We observe that the accuracy varies across different sources, a discrepancy we attribute primarily to the differing domain and difficulty distributions of the respective datasets.&lt;sup>2&lt;/sup>
964	
965	&lt;sup>2&lt;/sup>Our human evaluation standard is particularly stringent. To calibrate our criteria, we inspected a random sample of 50## 7 Conclusion
966	
967	This paper presents CriticLean, a comprehensive framework that positions the critic as a central component in the autoformalization of mathematical statements. Through the development of CriticLeanGPT and the construction of CriticLeanBench, we demonstrate that explicitly modeling and training the critic yields significant improvements in formalization quality. Our pipeline not only refines the translation process through semantic validation, but also enables the construction of FineLeanCorpus, which is validated by both compiler and critic.
968	
969	---
970	
971	entries from the Lean-Workbook, which yielded an accuracy of 84%.## **8 Contributions and Acknowledgments**
972	
973	### **Co-First Authors**
974	
975	Zhongyuan Peng, Yifan Yao, Kaijing Ma
976	
977	### **Co-Authors**
978	
979	Shuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, Minghao Liu, Yihang Xia, Jiawei Shen, Yuchen Wu, Yixin Cao, Zhaoxiang Zhang, Wenhao Huang
980	
981	### **Corresponding Authors**
982	
983	Jiaheng Liu, Ge Zhang## References
984	
985	- [1] AI Research Group of TAL Education Group. K-12 handwritten mathematical expressions dataset (hme100k). &lt;https://ai.100tal.com/dataset>. Accessed: 2025-04-05.
986	- [2] Anthropic. Claude 3.5 sonnet model card addendum, 2024. URL &lt;https://www.paperswithcode.com/paper/claude-3-5-sonnet-model-card-addendum>. Accessed: 2024-09-21.
987	- [3] Zhangir Azerbayev, Bartosz Piotrowski, Hailey Schoelkopf, Edward W Ayers, Dragomir Radev, and Jeremy Avigad. Proofnet: Autoformalizing and formally proving undergraduate-level mathematics. [arXiv preprint arXiv:2302.12433](#), 2023.
988	- [4] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report. [arXiv preprint arXiv:2309.16609](#), 2023.
989	- [5] Konstantin Chernyshev, Vitaliy Polshkov, Ekaterina Artemova, Alex Myasnikov, Vlad Stepanov, Alexei Miasnikov, and Sergei Tilga. U-math: A university-level benchmark for evaluating mathematical skills in llms. [arXiv preprint arXiv:2412.03205](#), 2024.
990	- [6] B.P. Demidovich. Problems in Mathematical Analysis. Edited by B. Demidovich. Translated From the Russian by G. Yankovsky. Russian Monographs and Texts on Advanced Mathematics and Physics. Mir Publishers, 1964. URL &lt;https://books.google.com/books?id=XdmpwgEACA AJ>.
991	- [7] J Fan, S Martinson, EY Wang, K Hausknecht, J Brenner, D Liu, N Peng, C Wang, and MP Brenner. Hardmath: A benchmark dataset for challenging problems in applied mathematics. arxiv 2024. [arXiv preprint arXiv:2410.09988](#).
992	- [8] Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. [arXiv preprint arXiv:2410.07985](#), 2024.
993	- [9] Google. Gemini: A family of highly capable multimodal models, 2023.
994	- [10] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. [arXiv preprint arXiv:2407.21783](#), 2024.
995	- [11] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. [arXiv preprint arXiv:2501.12948](#), 2025.
996	- [12] Dong Guo, Faming Wu, Feida Zhu, Fuxing Leng, Guang Shi, Haobin Chen, Haoqi Fan, Jian Wang, Jianyu Jiang, Jiawei Wang, et al. Seed1. 5-vl technical report. [arXiv preprint arXiv:2505.07062](#), 2025.
997	- [13] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024.
998	- [14] Yancheng He, Shilong Li, Jiaheng Liu, Weixun Wang, Xingyuan Bu, Ge Zhang, Zhongyuan Peng, Zhaoxiang Zhang, Zhicheng Zheng, Wenbo Su, and Bo Zheng. Can large language models detect errors in long chain-of-thought reasoning?, 2025. URL &lt;https://arxiv.org/abs/2502.19361>.
999	- [15] Zhiwei He, Tian Liang, Jiahao Xu, Qiuzhi Liu, Xingyu Chen, Yue Wang, Linfeng Song, Dian Yu, Zhenwen Liang, Wenxuan Wang, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. Deepmath-103k: A large-scale, challenging, decontaminated, and verifiable mathematical dataset for advancing reasoning. 2025. URL &lt;https://arxiv.org/abs/2504.11456>.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "157a4d86-a86e-47b2-b257-d791c1fe01c6",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "2d08a24a-cef3-416c-9904-c7bff38ea64d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/toolu_017tNQR36VFz5t8HzkqpKgwp.txt",
      "content": "&lt;td>maximum length&lt;/td>\n&lt;td>2980 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>minimum length&lt;/td>\n&lt;td>9 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>avg length&lt;/td>\n&lt;td>78.4 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;i>Lean Result(success)&lt;/i>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>maximum length&lt;/td>\n&lt;td>768 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>minimum length&lt;/td>\n&lt;td>14 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>avg length&lt;/td>\n&lt;td>87.8 tokens&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 5** Dataset statistics of FineLeanCorpus.**Figure 5** Performance on CriticLeanBench using **Pass@k** metrics, where **k = 8** (left) and **k = 32** (right).\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Difficulty Level&lt;/th>\n&lt;th>Size&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>AOPs [35]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>199982&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepMath-103k [15]&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>28538&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>NuminaMath-TIR [24]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>22847&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepTheorem [74]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>15131&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepScaleR [34]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>11544&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DAPO-Math-17k [66]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>4078&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Omni-MATH [8]&lt;/td>\n&lt;td>Undergraduate&lt;/td>\n&lt;td>1176&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>IneqMath [20]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>963&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>BlueMO [73]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>616&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>TAL-SCQ5K [37]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>393&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>70&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Multi-Source Math Competition&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>619&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 4** Overview of different sources for FineLeanCorpus.\n\nhigher-performance CriticLeanGPT model. Manual validation indicates that this step is expected to eliminate 74.7% of the remaining incorrect formalizations. The resulting corpus is characterized by its expressive range: natural language statements vary from a concise 9 tokens to a complex 2,980 tokens (avg. 78.4), while their corresponding Lean formalizations span from 14 to 768 tokens (avg. 87.8), reflecting the deep spectrum of complexity successfully captured by our pipeline.\n\nTo further analyze the differences between our FineLeanCorpus dataset and the Lean-Workbook, we employed the templates from Appendix J and Appendix I to assess the difficulty levels and classify the mathematical domains of the datasets using Doubao-1.5-pro [12]. A comparative analysis of our proposed FineLeanCorpus against Lean-Workbook (Figure 7, Figure 8, Table 4 and Table 5) reveals two fundamental advancements: (1) Scale and Coverage: Our corpus provides a significant quantitative expansion in both problem difficulty and domain coverage. This expansion is evident not only across nearly the entire difficulty spectrum—offering a much richer data pool for training foundational skills—but also in the substantial augmentation of high-volume domains like Intermediate Algebra and Elementary Number Theory. (2) FineLeanCorpus exhibits a more diverse and structurally balanced profile, achieved by collecting natural language statements from numerous sources. From a difficulty perspective, it features a multimodal distribution with substantial problem counts at several distinct complexity points, in stark contrast to the unimodal distribution of Lean-Workbook. This characteristic is crucial for mitigating model overfitting to a narrow complexity band. From a domain perspective, it substantially reinforces previously underrepresented areas. For instance, categories such as Analytic Geometry and Integral Calculus are significantly expanded, while niche topics like Algorithms and Graph Theory are also robustly augmented. This targeted enrichment transforms sparsely sampled topics into well-supported, learnable sub-domains, yielding a more comprehensive dataset designed to fosterholistic reasoning capabilities. More details regarding our FineLeanCorpus dataset, including its fine-grained mathematical domain distribution (see Appendix A), are provided for further analysis.\n\nFurthermore, to push the boundaries of current models and foster research into the upper echelons of mathematical reasoning, we have curated a specialized training subset from FineLeanCorpus, which we designate as Diamond. This subset comprises 36,033 problems with a difficulty rating exceeding 5. The purpose of this high-difficulty training set is to create a demanding training environment that fosters the development of the sophisticated, multi-step reasoning required to tackle the most formidable mathematical problems. A detailed breakdown of the mathematical domain distribution within this subset is provided in table 11.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Source&lt;/th>\n&lt;th>Theorems&lt;/th>\n&lt;th>Level&lt;/th>\n&lt;th>Detailed Critic Process&lt;/th>\n&lt;th>Difficulty Profile&lt;/th>\n&lt;th>Topic Diversity&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Lean-Workbook [65]&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>140K&lt;/td>\n&lt;td>Undergraduate&lt;/td>\n&lt;td>Opaque&lt;/td>\n&lt;td>Avg: 3.70&lt;br/>Top-tier (&lt;math>\\geq 6&lt;/math>): 7.81%&lt;/td>\n&lt;td>Highly Skewed&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>FineLeanCorpus (ours)&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>285K&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>Transparent&lt;/td>\n&lt;td>Avg: 3.24&lt;br/>Top-tier (&lt;math>\\geq 6&lt;/math>): 11.10%&lt;/td>\n&lt;td>Balanced &amp; Diverse&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 6** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.\n\n**Figure 7** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.\n\n## 6.1 Analysis on CriticLean Pipeline\n\nAs shown in Table 7, our autoformalization pipeline significantly improves accuracy. We selected 50 problems from the Omni-MATH and applied the following three formalization strategies, with the correctness of all outputs confirmed by manual human inspection.\n\nOur baseline model, Kimina-Autoformalizer-7B, is used in each strategy: (1) a **Single Pass** baseline (38.0% accuracy); (2) a **Compiler Feedback** loop, where the model regenerates formalizations until they successfully compile (54.0% accuracy); (3) our **CriticLean Pipeline**, which extends this process, regenerating formalizations until they both compile successfully and are validated by our integrated **CriticLeanGPT Model** (84.0% accuracy).\n\nWhile compiler feedback resolves syntactical errors, it fails to detect logical flaws. Our pipeline addresses this gap. The integration of critic model, which performs deeper semantic and logical validation, is directly\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>AVG&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B&lt;/td>\n&lt;td>38.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B (Compiler)&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B (CriticLean)&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 7** Human evaluation accuracy results for autoformalization performance: The best score is highlighted in *box*.**Figure 8** Math Domain Distributions: FineLeanCorpus vs. Lean-Workbook.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th># Attempt&lt;/th>\n&lt;th>1&lt;/th>\n&lt;th>5&lt;/th>\n&lt;th>10&lt;/th>\n&lt;th>50&lt;/th>\n&lt;th>100&lt;/th>\n&lt;th>200&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Count / Ratio&lt;/td>\n&lt;td>63 / 12.6%&lt;/td>\n&lt;td>137 / 27.4%&lt;/td>\n&lt;td>170 / 34.0%&lt;/td>\n&lt;td>229 / 45.8%&lt;/td>\n&lt;td>245 / 49.0%&lt;/td>\n&lt;td>264 / 52.8%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 8 Effectiveness of the Multi-Attempt Strategy on Formalization Yield.** The table shows the cumulative number of successfully formalized problems retained by the critic model as the attempt limit increases. Statistics are from a 500-problem sample.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>NuminaMath-TIR [24]&lt;/td>\n&lt;td>78%&lt;/td>\n&lt;td>IneqMath [20]&lt;/td>\n&lt;td>96%&lt;/td>\n&lt;td>BlueMO [73]&lt;/td>\n&lt;td>86%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepMath-103k [16]&lt;/td>\n&lt;td>84%&lt;/td>\n&lt;td>DAPO-Math-17k [66]&lt;/td>\n&lt;td>69%&lt;/td>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>88%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AOPs [35]&lt;/td>\n&lt;td>73%&lt;/td>\n&lt;td>TAL-SCQ5K [37]&lt;/td>\n&lt;td>75%&lt;/td>\n&lt;td>Omni-MATH [8]&lt;/td>\n&lt;td>84%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepTheorem [74]&lt;/td>\n&lt;td>100%&lt;/td>\n&lt;td>DeepScaleR [34]&lt;/td>\n&lt;td>100%&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 9** Human evaluation results of different sources.\n\nresponsible for the accuracy increase from 54.0% to 84.0%. By filtering out plausible but incorrect formalizations, our method provides a more robust path toward reliable autoformalization. These manually-verified results present strong empirical evidence for the efficacy of our approach.\n\nTable 8 shows our pipeline achieved a 52.8% success rate across 500 problems, where success required passing both syntactic validation and our critic model’s semantic check. The value of our multi-attempt strategy is evident: while only 12.6% of samples passed on the first try, the pipeline successfully recovered an additional 40.2% that would be discarded by single-pass systems. Conversely, the 47.2% failure rate within the 200-attempt limit highlights a fundamental bottleneck: the pipeline’s performance is ultimately constrained by the base auto-formalization model’s ability to produce a candidate our critic can approve.\n\nMoreover, as shown in Table 9, we also provide the human evaluation results of different sources. We observe that the accuracy varies across different sources, a discrepancy we attribute primarily to the differing domain and difficulty distributions of the respective datasets.&lt;sup>2&lt;/sup>\n\n&lt;sup>2&lt;/sup>Our human evaluation standard is particularly stringent. To calibrate our criteria, we inspected a random sample of 50## 7 Conclusion\n\nThis paper presents CriticLean, a comprehensive framework that positions the critic as a central component in the autoformalization of mathematical statements. Through the development of CriticLeanGPT and the construction of CriticLeanBench, we demonstrate that explicitly modeling and training the critic yields significant improvements in formalization quality. Our pipeline not only refines the translation process through semantic validation, but also enables the construction of FineLeanCorpus, which is validated by both compiler and critic.\n\n---\n\nentries from the Lean-Workbook, which yielded an accuracy of 84%.## **8 Contributions and Acknowledgments**\n\n### **Co-First Authors**\n\nZhongyuan Peng, Yifan Yao, Kaijing Ma\n\n### **Co-Authors**\n\nShuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, Minghao Liu, Yihang Xia, Jiawei Shen, Yuchen Wu, Yixin Cao, Zhaoxiang Zhang, Wenhao Huang\n\n### **Corresponding Authors**\n\nJiaheng Liu, Ge Zhang## References\n\n- [1] AI Research Group of TAL Education Group. K-12 handwritten mathematical expressions dataset (hme100k). &lt;https://ai.100tal.com/dataset>. Accessed: 2025-04-05.\n- [2] Anthropic. Claude 3.5 sonnet model card addendum, 2024. URL &lt;https://www.paperswithcode.com/paper/claude-3-5-sonnet-model-card-addendum>. Accessed: 2024-09-21.\n- [3] Zhangir Azerbayev, Bartosz Piotrowski, Hailey Schoelkopf, Edward W Ayers, Dragomir Radev, and Jeremy Avigad. Proofnet: Autoformalizing and formally proving undergraduate-level mathematics. [arXiv preprint arXiv:2302.12433](#), 2023.\n- [4] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report. [arXiv preprint arXiv:2309.16609](#), 2023.\n- [5] Konstantin Chernyshev, Vitaliy Polshkov, Ekaterina Artemova, Alex Myasnikov, Vlad Stepanov, Alexei Miasnikov, and Sergei Tilga. U-math: A university-level benchmark for evaluating mathematical skills in llms. [arXiv preprint arXiv:2412.03205](#), 2024.\n- [6] B.P. Demidovich. Problems in Mathematical Analysis. Edited by B. Demidovich. Translated From the Russian by G. Yankovsky. Russian Monographs and Texts on Advanced Mathematics and Physics. Mir Publishers, 1964. URL &lt;https://books.google.com/books?id=XdmpwgEACA AJ>.\n- [7] J Fan, S Martinson, EY Wang, K Hausknecht, J Brenner, D Liu, N Peng, C Wang, and MP Brenner. Hardmath: A benchmark dataset for challenging problems in applied mathematics. arxiv 2024. [arXiv preprint arXiv:2410.09988](#).\n- [8] Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. [arXiv preprint arXiv:2410.07985](#), 2024.\n- [9] Google. Gemini: A family of highly capable multimodal models, 2023.\n- [10] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. [arXiv preprint arXiv:2407.21783](#), 2024.\n- [11] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. [arXiv preprint arXiv:2501.12948](#), 2025.\n- [12] Dong Guo, Faming Wu, Feida Zhu, Fuxing Leng, Guang Shi, Haobin Chen, Haoqi Fan, Jian Wang, Jianyu Jiang, Jiawei Wang, et al. Seed1. 5-vl technical report. [arXiv preprint arXiv:2505.07062](#), 2025.\n- [13] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024.\n- [14] Yancheng He, Shilong Li, Jiaheng Liu, Weixun Wang, Xingyuan Bu, Ge Zhang, Zhongyuan Peng, Zhaoxiang Zhang, Zhicheng Zheng, Wenbo Su, and Bo Zheng. Can large language models detect errors in long chain-of-thought reasoning?, 2025. URL &lt;https://arxiv.org/abs/2502.19361>.\n- [15] Zhiwei He, Tian Liang, Jiahao Xu, Qiuzhi Liu, Xingyu Chen, Yue Wang, Linfeng Song, Dian Yu, Zhenwen Liang, Wenxuan Wang, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. Deepmath-103k: A large-scale, challenging, decontaminated, and verifiable mathematical dataset for advancing reasoning. 2025. URL &lt;https://arxiv.org/abs/2504.11456>.",
      "numLines": 300,
      "startLine": 700,
      "totalLines": 1768
    }
  },
  "sourceToolAssistantUUID": "157a4d86-a86e-47b2-b257-d791c1fe01c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "2d08a24a-cef3-416c-9904-c7bff38ea64d",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Assistant

_source line 66 · 2026-05-27T20:38:40.520Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of CriticLean. Let me also search for ICLR 2027 deadline dates and search for any more recent relevant work on Lean compilation costs at scale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d08a24a-cef3-416c-9904-c7bff38ea64d",
  "isSidechain": false,
  "requestId": "req_011CbTic5Hodnw8UEfWRKxNG",
  "type": "assistant",
  "uuid": "a20b6701-903a-4bbd-b021-4f56b811d122",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RjNujAAYjzewGiNWHU8j2L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6062,
      "cache_read_input_tokens": 43716,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 43716,
          "cache_creation_input_tokens": 6062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6062
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

_source line 67 · 2026-05-27T20:38:40.542Z_

Now let me search for a few more things to complete my research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a20b6701-903a-4bbd-b021-4f56b811d122",
  "isSidechain": false,
  "requestId": "req_011CbTic5Hodnw8UEfWRKxNG",
  "type": "assistant",
  "uuid": "90a26bb0-d0ec-4938-a69a-8f59e91b656e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RjNujAAYjzewGiNWHU8j2L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6062,
      "cache_read_input_tokens": 43716,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 43716,
          "cache_creation_input_tokens": 6062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6062
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

_source line 68 · 2026-05-27T20:38:41.082Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NfqUXY4J4z3ESHkFJskZyg`</summary>

```json
{
  "query": "ICLR 2027 submission deadline dates call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90a26bb0-d0ec-4938-a69a-8f59e91b656e",
  "isSidechain": false,
  "requestId": "req_011CbTic5Hodnw8UEfWRKxNG",
  "type": "assistant",
  "uuid": "0de8cf56-d4bf-40a0-b2c1-8216ab637fa2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RjNujAAYjzewGiNWHU8j2L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6062,
      "cache_read_input_tokens": 43716,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 43716,
          "cache_creation_input_tokens": 6062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6062
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

_source line 69 · 2026-05-27T20:38:45.673Z_

<details><summary>↩ Tool result · `toolu_01NfqUXY4J4z3ESHkFJskZyg`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline dates call for papers"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"}]

Based on the search results, I found information about ICLR but limited specific details about ICLR 2027 submission deadlines. Here's what I found:

ICLR 2027 is predicted to be held April 24-28, 2027, but the specific dates note that this is predicted based on previous year schedule and should be verified on the official conference website.

Unfortunately, the search results do not contain the official submission deadline dates for ICLR 2027. The most detailed information available is for ICLR 2026, which shows that there is a mandatory abstract deadline on September 27, 2025 (for the 2026 conference).

Since the official ICLR 2027 call for papers has likely not yet been published, I recommend checking the official ICLR website (iclr.cc) directly for the most up-to-date information on ICLR 2027 submission deadlines once they are announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0de8cf56-d4bf-40a0-b2c1-8216ab637fa2",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "d0a2c38c-386b-4ecd-85ba-08c6c986d15a",
  "toolUseResult": {
    "query": "ICLR 2027 submission deadline dates call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MC6hm4P4zSHd6wDaQhxx1R",
        "content": [
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://iclr.cc/Conferences/2026/Dates"
          },
          {
            "title": "International Conference on Learning Representations ICLR in August 2027 in Sydney",
            "url": "https://waset.org/learning-representations-conference-in-august-2027-in-sydney"
          },
          {
            "title": "ICLR 2026 Call for Papers",
            "url": "https://iclr.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Key deadlines in AI and ML conferences",
            "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"
          },
          {
            "title": "Year-Round Deadlines - Imranur Rahman",
            "url": "https://imranur-rahman.github.io/deadlines/"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          },
          {
            "title": "Call for Papers",
            "url": "https://iclr.cc/Conferences/2025/CallForPapers"
          }
        ]
      },
      "Based on the search results, I found information about ICLR but limited specific details about ICLR 2027 submission deadlines. Here's what I found:\n\nICLR 2027 is predicted to be held April 24-28, 2027, but the specific dates note that this is predicted based on previous year schedule and should be verified on the official conference website.\n\nUnfortunately, the search results do not contain the official submission deadline dates for ICLR 2027. The most detailed information available is for ICLR 2026, which shows that there is a mandatory abstract deadline on September 27, 2025 (for the 2026 conference).\n\nSince the official ICLR 2027 call for papers has likely not yet been published, I recommend checking the official ICLR website (iclr.cc) directly for the most up-to-date information on ICLR 2027 submission deadlines once they are announced."
    ],
    "durationSeconds": 4.582972199999989,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0de8cf56-d4bf-40a0-b2c1-8216ab637fa2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-27T20:38:49.434Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XFuND3i4Wi5aK3jTx8kPzh`</summary>

```json
{
  "url": "https://trybibby.com/conference-deadlines",
  "prompt": "Find the ICLR 2027 submission deadline dates. Also find any other AI/ML conference deadlines for late 2026 that would be relevant (NeurIPS 2027, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0a2c38c-386b-4ecd-85ba-08c6c986d15a",
  "isSidechain": false,
  "requestId": "req_011CbTici39iBKytqpyUrn2c",
  "type": "assistant",
  "uuid": "a3711a5b-248a-4679-90b2-c30bb82d59e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qpq6y3XHh888z83xnbuVrR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 49778,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 49778,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 71 · 2026-05-27T20:38:55.052Z_

<details><summary>↩ Tool result · `toolu_01XFuND3i4Wi5aK3jTx8kPzh`</summary>

```text
# ICLR 2027 and Related ML Conference Deadlines

## ICLR 2027

Based on the deadline registry, **ICLR 2027** has two submission phases:

- **Abstract deadline:** September 19, 2026, 11:59 AM UTC
- **Full paper deadline:** September 24, 2026, 11:59 AM UTC

The conference is scheduled for April/May 2027 at a location still to be determined.

## Other Major ML Conferences in Late 2026

Several significant machine learning venues have earlier deadlines:

- **AAAI 2027** (Abstract): July 26, 2026
- **AAAI 2027** (Full Paper): August 2, 2026
- **AISTATS 2027**: October 10, 2026

## Late 2027 ML Events

Looking further ahead, you'll also want to track:

- **ICML 2027**: January 29, 2027 deadline
- **NeurIPS 2027**: May 16, 2027 deadline

The registry notes that tentative entries marked "[EST.]" are "projected from prior-year schedules where the official CFP has not yet posted," so verify directly with each conference before submitting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3711a5b-248a-4679-90b2-c30bb82d59e4",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "b42a4290-949a-4307-a5d2-e9fb56de17f9",
  "toolUseResult": {
    "bytes": 444260,
    "code": 200,
    "codeText": "OK",
    "result": "# ICLR 2027 and Related ML Conference Deadlines\n\n## ICLR 2027\n\nBased on the deadline registry, **ICLR 2027** has two submission phases:\n\n- **Abstract deadline:** September 19, 2026, 11:59 AM UTC\n- **Full paper deadline:** September 24, 2026, 11:59 AM UTC\n\nThe conference is scheduled for April/May 2027 at a location still to be determined.\n\n## Other Major ML Conferences in Late 2026\n\nSeveral significant machine learning venues have earlier deadlines:\n\n- **AAAI 2027** (Abstract): July 26, 2026\n- **AAAI 2027** (Full Paper): August 2, 2026\n- **AISTATS 2027**: October 10, 2026\n\n## Late 2027 ML Events\n\nLooking further ahead, you'll also want to track:\n\n- **ICML 2027**: January 29, 2027 deadline\n- **NeurIPS 2027**: May 16, 2027 deadline\n\nThe registry notes that tentative entries marked \"[EST.]\" are \"projected from prior-year schedules where the official CFP has not yet posted,\" so verify directly with each conference before submitting.",
    "durationMs": 5616,
    "url": "https://trybibby.com/conference-deadlines"
  },
  "sourceToolAssistantUUID": "a3711a5b-248a-4679-90b2-c30bb82d59e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-27T20:39:04.913Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting - that page shows AAAI 2027 abstract July 26 and paper Aug 2, but the official AAAI website showed July 21 and July 28. The official site should be more authoritative. Let me verify the AAAI dates from the official site more carefully.

From my earlier search, the official AAAI site (aaai.org/conference/aaai/aaai-27/) clearly showed:
- July 21, 2026: Abstracts due at 11:59 PM UTC-12


- July 28, 2026: Full papers due at 11:59 PM UTC-12

For ICLR 2027, trybibby shows Sep 19/24 which aligns with the original proposal, though the official CFP probably hasn't been released yet since we're still in May 2026. Now I need to look into CPU costs for running Lean instances at scale and search for recent work on gaming-aware evaluation frameworks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b42a4290-949a-4307-a5d2-e9fb56de17f9",
  "isSidechain": false,
  "requestId": "req_011CbTidQnMTwttQpYnb1j8v",
  "type": "assistant",
  "uuid": "7eac4fa8-033f-4712-bc30-d10d07f774b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpQJbNDTCBgprK1KZ82A63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 50522,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 50522,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
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

_source line 73 · 2026-05-27T20:39:04.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0157AHMdc8iNygqppBpxqmQS`</summary>

```json
{
  "query": "cloud CPU instance cost 2026 c7i.16xlarge 64 vCPU spot price AWS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eac4fa8-033f-4712-bc30-d10d07f774b9",
  "isSidechain": false,
  "requestId": "req_011CbTidQnMTwttQpYnb1j8v",
  "type": "assistant",
  "uuid": "e4f8a421-2163-4287-a57b-1b73f820619c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpQJbNDTCBgprK1KZ82A63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 50522,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 50522,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
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

_source line 74 · 2026-05-27T20:39:09.763Z_

<details><summary>↩ Tool result · `toolu_0157AHMdc8iNygqppBpxqmQS`</summary>

```text
Web search results for query: "cloud CPU instance cost 2026 c7i.16xlarge 64 vCPU spot price AWS"

Links: [{"title":"c7i.16xlarge specs and pricing | AWS | CloudPrice","url":"https://cloudprice.net/aws/ec2/instances/c7i.16xlarge"},{"title":"c7i.16xlarge pricing and specs - Vantage Instances","url":"https://instances.vantage.sh/aws/ec2/c7i.16xlarge"},{"title":"Amazon EC2 Instance Comparison","url":"https://instances.vantage.sh/"},{"title":"Compare AWS EC2 C7I Instance Pricing","url":"https://www.economize.cloud/resources/aws/pricing/ec2/family/c7i/"},{"title":"c7i.16xlarge - Amazon EC2 Instance Type","url":"https://aws-pricing.com/c7i.16xlarge.html"},{"title":"c7i.16xlarge pricing and specs - AWS | Holori","url":"https://calculator.holori.com/aws/ec2/c7i.16xlarge"},{"title":"Amazon EC2 C7i Instances","url":"https://aws.amazon.com/ec2/instance-types/c7i/"},{"title":"c7i.16xlarge Pricing and Specs: AWS EC2","url":"https://costcalc.cloudoptimo.com/aws-pricing-calculator/ec2/c7i.16xlarge"},{"title":"c7i.large pricing and specs - Vantage Instances","url":"https://instances.vantage.sh/aws/ec2/c7i.large"},{"title":"SpotPrice - Amazon Elastic Compute Cloud","url":"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotPrice.html"}]

Based on the search results, here's what I found about the c7i.16xlarge instance pricing in 2026:

## Instance Specifications
The c7i.16xlarge is an Amazon EC2 instance with 64 vCPUs and 128 GiB RAM.

## Pricing Information

**On-Demand Pricing:**
The c7i.16xlarge instance starts at $2.856 per hour, which equates to approximately $2,043.30 per month.

**Spot Instance Pricing:**
The search results don't provide specific current spot price information for the c7i.16xlarge. Spot prices vary dynamically based on region, availability zone, and current demand. To get the most current spot pricing for this instance type, you would need to:

1. Check the AWS EC2 pricing console directly
2. Use AWS pricing APIs
3. Visit one of the pricing aggregator sites found in the results (CloudPrice.net, Vantage Instances, etc.), which may have regional spot price data

The results indicate that these pricing sites track spot pricing across regions, but the specific spot prices aren't displayed in the search results returned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4f8a421-2163-4287-a57b-1b73f820619c",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "9ebf38c9-2a4a-43bf-a54d-7bb603bfccf7",
  "toolUseResult": {
    "query": "cloud CPU instance cost 2026 c7i.16xlarge 64 vCPU spot price AWS",
    "results": [
      {
        "tool_use_id": "srvtoolu_017R4WGYBj1WbsddAHV7d9yd",
        "content": [
          {
            "title": "c7i.16xlarge specs and pricing | AWS | CloudPrice",
            "url": "https://cloudprice.net/aws/ec2/instances/c7i.16xlarge"
          },
          {
            "title": "c7i.16xlarge pricing and specs - Vantage Instances",
            "url": "https://instances.vantage.sh/aws/ec2/c7i.16xlarge"
          },
          {
            "title": "Amazon EC2 Instance Comparison",
            "url": "https://instances.vantage.sh/"
          },
          {
            "title": "Compare AWS EC2 C7I Instance Pricing",
            "url": "https://www.economize.cloud/resources/aws/pricing/ec2/family/c7i/"
          },
          {
            "title": "c7i.16xlarge - Amazon EC2 Instance Type",
            "url": "https://aws-pricing.com/c7i.16xlarge.html"
          },
          {
            "title": "c7i.16xlarge pricing and specs - AWS | Holori",
            "url": "https://calculator.holori.com/aws/ec2/c7i.16xlarge"
          },
          {
            "title": "Amazon EC2 C7i Instances",
            "url": "https://aws.amazon.com/ec2/instance-types/c7i/"
          },
          {
            "title": "c7i.16xlarge Pricing and Specs: AWS EC2",
            "url": "https://costcalc.cloudoptimo.com/aws-pricing-calculator/ec2/c7i.16xlarge"
          },
          {
            "title": "c7i.large pricing and specs - Vantage Instances",
            "url": "https://instances.vantage.sh/aws/ec2/c7i.large"
          },
          {
            "title": "SpotPrice - Amazon Elastic Compute Cloud",
            "url": "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotPrice.html"
          }
        ]
      },
      "Based on the search results, here's what I found about the c7i.16xlarge instance pricing in 2026:\n\n## Instance Specifications\nThe c7i.16xlarge is an Amazon EC2 instance with 64 vCPUs and 128 GiB RAM.\n\n## Pricing Information\n\n**On-Demand Pricing:**\nThe c7i.16xlarge instance starts at $2.856 per hour, which equates to approximately $2,043.30 per month.\n\n**Spot Instance Pricing:**\nThe search results don't provide specific current spot price information for the c7i.16xlarge. Spot prices vary dynamically based on region, availability zone, and current demand. To get the most current spot pricing for this instance type, you would need to:\n\n1. Check the AWS EC2 pricing console directly\n2. Use AWS pricing APIs\n3. Visit one of the pricing aggregator sites found in the results (CloudPrice.net, Vantage Instances, etc.), which may have regional spot price data\n\nThe results indicate that these pricing sites track spot pricing across regions, but the specific spot prices aren't displayed in the search results returned."
    ],
    "durationSeconds": 4.835476599000016,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e4f8a421-2163-4287-a57b-1b73f820619c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-27T20:39:12.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018AxSfbhLRJGLjMEy17zDcv`</summary>

```json
{
  "query": "Lean 4 compilation memory per instance Mathlib import RAM requirements benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ebf38c9-2a4a-43bf-a54d-7bb603bfccf7",
  "isSidechain": false,
  "requestId": "req_011CbTieV5M9V2SAnJM3wdeW",
  "type": "assistant",
  "uuid": "e11c20e6-ca08-4e6d-9f2f-b79bbd3ad1c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoqphTemtCWitjcpuqDmyR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 50954,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1079,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 50954,
          "cache_creation_input_tokens": 1079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1079
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

_source line 76 · 2026-05-27T20:39:18.134Z_

<details><summary>↩ Tool result · `toolu_018AxSfbhLRJGLjMEy17zDcv`</summary>

```text
Web search results for query: "Lean 4 compilation memory per instance Mathlib import RAM requirements benchmark"

Links: [{"title":"Topic: Memory consumption of mathlib","url":"https://leanprover-community.github.io/archive/stream/113489-new-members/topic/Memory.20consumption.20of.20mathlib.html"},{"title":"GitHub - gebner/lean4-mathlib-import","url":"https://github.com/gebner/lean4-mathlib-import"},{"title":"Topic: Importing mathlib into Lean 4","url":"https://leanprover-community.github.io/archive/stream/113488-general/topic/Importing.20mathlib.20into.20Lean.204.html"},{"title":"Topic: memory usage with vscode, lean and mathlib","url":"https://leanprover-community.github.io/archive/stream/113489-new-members/topic/memory.20usage.20with.20vscode.2C.20lean.20and.20mathlib.html"},{"title":"Lean Tips and Tricks","url":"https://leanprover-community.github.io/lean3/tips_and_tricks.html"},{"title":"Excessive memory consumption for processing simple file. · Issue #5321 · leanprover/lean4","url":"https://github.com/leanprover/lean4/issues/5321"},{"title":"lean-interact · PyPI","url":"https://pypi.org/project/lean-interact/"},{"title":"GitHub - leanprover-community/mathlib4: The math library of Lean 4 · GitHub","url":"https://github.com/leanprover-community/mathlib4"}]

Based on the search results, here's what I found regarding Lean 4 compilation memory requirements for Mathlib imports:

## Memory Requirements for Mathlib Compilation

Importing the Mathlib export file takes about 6 minutes and 13.5 gigabytes of RAM for earlier versions. However, more recent optimizations have improved this significantly.

With improvements to the compiler, the importer only requires 2 gigabytes of RAM, resulting in a more efficient process.

## Performance After Import

Once compiled, importing a 3.2 gigabyte Mathlib file is surprisingly snappy: it only takes 1.8 seconds on a machine.

## Practical Recommendations

Rather than recompiling Mathlib locally, the recommended approach is to use precompiled files: To obtain precompiled olean files, run `lake exe cache get` (Skipping this step means the next step will be very slow).

The memory requirements can vary significantly depending on your specific imports and proof complexity. If you encounter memory issues, you can adjust the memory limit in VS Code by searching for "Lean Memory Limit" in the settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e11c20e6-ca08-4e6d-9f2f-b79bbd3ad1c0",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "5bbda850-de64-4e81-bf5c-b4baae5394e2",
  "toolUseResult": {
    "query": "Lean 4 compilation memory per instance Mathlib import RAM requirements benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_014hjox8UXqxdB5hLf97Hcmp",
        "content": [
          {
            "title": "Topic: Memory consumption of mathlib",
            "url": "https://leanprover-community.github.io/archive/stream/113489-new-members/topic/Memory.20consumption.20of.20mathlib.html"
          },
          {
            "title": "GitHub - gebner/lean4-mathlib-import",
            "url": "https://github.com/gebner/lean4-mathlib-import"
          },
          {
            "title": "Topic: Importing mathlib into Lean 4",
            "url": "https://leanprover-community.github.io/archive/stream/113488-general/topic/Importing.20mathlib.20into.20Lean.204.html"
          },
          {
            "title": "Topic: memory usage with vscode, lean and mathlib",
            "url": "https://leanprover-community.github.io/archive/stream/113489-new-members/topic/memory.20usage.20with.20vscode.2C.20lean.20and.20mathlib.html"
          },
          {
            "title": "Lean Tips and Tricks",
            "url": "https://leanprover-community.github.io/lean3/tips_and_tricks.html"
          },
          {
            "title": "Excessive memory consumption for processing simple file. · Issue #5321 · leanprover/lean4",
            "url": "https://github.com/leanprover/lean4/issues/5321"
          },
          {
            "title": "lean-interact · PyPI",
            "url": "https://pypi.org/project/lean-interact/"
          },
          {
            "title": "GitHub - leanprover-community/mathlib4: The math library of Lean 4 · GitHub",
            "url": "https://github.com/leanprover-community/mathlib4"
          }
        ]
      },
      "Based on the search results, here's what I found regarding Lean 4 compilation memory requirements for Mathlib imports:\n\n## Memory Requirements for Mathlib Compilation\n\nImporting the Mathlib export file takes about 6 minutes and 13.5 gigabytes of RAM for earlier versions. However, more recent optimizations have improved this significantly.\n\nWith improvements to the compiler, the importer only requires 2 gigabytes of RAM, resulting in a more efficient process.\n\n## Performance After Import\n\nOnce compiled, importing a 3.2 gigabyte Mathlib file is surprisingly snappy: it only takes 1.8 seconds on a machine.\n\n## Practical Recommendations\n\nRather than recompiling Mathlib locally, the recommended approach is to use precompiled files: To obtain precompiled olean files, run `lake exe cache get` (Skipping this step means the next step will be very slow).\n\nThe memory requirements can vary significantly depending on your specific imports and proof complexity. If you encounter memory issues, you can adjust the memory limit in VS Code by searching for \"Lean Memory Limit\" in the settings."
    ],
    "durationSeconds": 5.266748847999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e11c20e6-ca08-4e6d-9f2f-b79bbd3ad1c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-27T20:39:20.863Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016QJekxkttoXwgrrGPPBniZ`</summary>

```json
{
  "query": "reward hacking detection framework evaluation methodology RL formal verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bbda850-de64-4e81-bf5c-b4baae5394e2",
  "isSidechain": false,
  "requestId": "req_011CbTif6qfFbq1HeB6eyXQz",
  "type": "assistant",
  "uuid": "68329704-a4dd-4acb-ab62-9bbf7fa165d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01754uGX41nNzP99SxRKJJak",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 52033,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 755,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 52033,
          "cache_creation_input_tokens": 755,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 755
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

_source line 78 · 2026-05-27T20:39:29.823Z_

<details><summary>↩ Tool result · `toolu_016QJekxkttoXwgrrGPPBniZ`</summary>

```text
Web search results for query: "reward hacking detection framework evaluation methodology RL formal verification 2025 2026"

Links: [{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Reward Hacking in RLVR Systems","url":"https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr"},{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://udspace.udel.edu/bitstreams/11090db0-25e3-40a9-834d-1625ab1e4050/download"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Reward Hacking in RLVR","url":"https://www.emergentmind.com/topics/reward-hacking-in-rlvr"},{"title":"Reward Hacking Mitigation using Verifiable Composite ...","url":"https://dl.acm.org/doi/pdf/10.1145/3765612.3767230"},{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/pdf/2601.20103"},{"title":"Verifiable Rewards (RLVR) Framework","url":"https://www.emergentmind.com/topics/verifiable-rewards-rlvr"},{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://www.arxiv.org/pdf/2509.15557"}]

Based on the search results, here's what I found regarding reward hacking detection framework evaluation methodology for RL with formal verification approaches from 2025-2026:

## Detection Framework Performance

Integrated, ensemble-based detection frameworks achieve precision near 78% and recall near 82% in diverse RL environments, with computational cost below 5% of training time according to research from July 2025.

## Detection Methodology

Automated detection algorithms span statistical divergence checks (e.g., KL divergence between current and baseline proxy/true reward ratios), time-series anomaly detection (Isolation Forests over reward statistics), correlation decay of proxy to true rewards, Markov chain perplexity of action sequences, robust IQR-based outlier analysis, and integrity monitoring (cryptographic checks on reward signal integrity).

## Empirical Evaluation

Empirical deployment of these detectors across 15 environments (Atari, MuJoCo, custom RLVR domains) and five RL algorithms yields 78.4% precision and 81.7% recall, with overhead below 5%.

## Formal Verification Component

A robust Reward Hacking Defense Rubric combines: formal proxy-trueness verifications; diverse, dynamic, and causally-aligned reward signals; vigilant detection and ongoing evaluation protocols; and dynamically updated, functional mitigations—across both RL and RLHF systems.

## Mitigation Effectiveness

Mitigation techniques based on detection findings can reduce reward hacking occurrence up to 54.6%, although this often involves trade-offs in legitimate performance and increased computational cost.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68329704-a4dd-4acb-ab62-9bbf7fa165d3",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "d3b8d836-8f82-4855-9c51-0f08aca320a5",
  "toolUseResult": {
    "query": "reward hacking detection framework evaluation methodology RL formal verification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YS1g7ic6gPt6PqfmdGEDWy",
        "content": [
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Reward Hacking in RLVR Systems",
            "url": "https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr"
          },
          {
            "title": "Reward Hacking Mitigation using Verifiable Composite Rewards",
            "url": "https://udspace.udel.edu/bitstreams/11090db0-25e3-40a9-834d-1625ab1e4050/download"
          },
          {
            "title": "Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study",
            "url": "https://arxiv.org/html/2507.05619v1"
          },
          {
            "title": "Reward Hacking in RLVR",
            "url": "https://www.emergentmind.com/topics/reward-hacking-in-rlvr"
          },
          {
            "title": "Reward Hacking Mitigation using Verifiable Composite ...",
            "url": "https://dl.acm.org/doi/pdf/10.1145/3765612.3767230"
          },
          {
            "title": "Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis",
            "url": "https://arxiv.org/pdf/2601.20103"
          },
          {
            "title": "Verifiable Rewards (RLVR) Framework",
            "url": "https://www.emergentmind.com/topics/verifiable-rewards-rlvr"
          },
          {
            "title": "Reward Hacking Mitigation using Verifiable Composite Rewards",
            "url": "https://www.arxiv.org/pdf/2509.15557"
          }
        ]
      },
      "Based on the search results, here's what I found regarding reward hacking detection framework evaluation methodology for RL with formal verification approaches from 2025-2026:\n\n## Detection Framework Performance\n\nIntegrated, ensemble-based detection frameworks achieve precision near 78% and recall near 82% in diverse RL environments, with computational cost below 5% of training time according to research from July 2025.\n\n## Detection Methodology\n\nAutomated detection algorithms span statistical divergence checks (e.g., KL divergence between current and baseline proxy/true reward ratios), time-series anomaly detection (Isolation Forests over reward statistics), correlation decay of proxy to true rewards, Markov chain perplexity of action sequences, robust IQR-based outlier analysis, and integrity monitoring (cryptographic checks on reward signal integrity).\n\n## Empirical Evaluation\n\nEmpirical deployment of these detectors across 15 environments (Atari, MuJoCo, custom RLVR domains) and five RL algorithms yields 78.4% precision and 81.7% recall, with overhead below 5%.\n\n## Formal Verification Component\n\nA robust Reward Hacking Defense Rubric combines: formal proxy-trueness verifications; diverse, dynamic, and causally-aligned reward signals; vigilant detection and ongoing evaluation protocols; and dynamically updated, functional mitigations—across both RL and RLHF systems.\n\n## Mitigation Effectiveness\n\nMitigation techniques based on detection findings can reduce reward hacking occurrence up to 54.6%, although this often involves trade-offs in legitimate performance and increased computational cost."
    ],
    "durationSeconds": 8.956034455999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "68329704-a4dd-4acb-ab62-9bbf7fa165d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 79 · 2026-05-27T20:39:29.827Z_

```json
{
  "parentUuid": "d3b8d836-8f82-4855-9c51-0f08aca320a5",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e9e2945e-5d63-414b-bc77-7f6ab636f8a6",
  "timestamp": "2026-05-27T20:39:29.827Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 80_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "e9e2945e-5d63-414b-bc77-7f6ab636f8a6",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Tool call

_source line 82 · 2026-05-27T20:39:33.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SPbjiMMNdZd3u7vMcPV1Gf`</summary>

```json
{
  "query": "FormaRL GRPO Lean compilation rollout time latency autoformalization training cost GPU hours"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9e2945e-5d63-414b-bc77-7f6ab636f8a6",
  "isSidechain": false,
  "requestId": "req_011CbTifxnW5PVwtrozBwF5d",
  "type": "assistant",
  "uuid": "eeaeaeb7-de55-4027-bf82-38d99e730dcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6sn7SPodMybcg8bJH9azG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 52788,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 52788,
          "cache_creation_input_tokens": 1003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1003
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

_source line 83 · 2026-05-27T20:39:42.628Z_

<details><summary>↩ Tool result · `toolu_01SPbjiMMNdZd3u7vMcPV1Gf`</summary>

```text
Web search results for query: "FormaRL GRPO Lean compilation rollout time latency autoformalization training cost GPU hours"

Links: [{"title":"FormaRL: RL-Driven Autoformalization for Lean 4","url":"https://www.emergentmind.com/topics/formarl"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data | OpenReview","url":"https://openreview.net/forum?id=Z2El1U94bq"},{"title":"[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/abs/2508.18914"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"},{"title":"Keep the Tokens Flowing: Lessons from 16 Open-Source RL Libraries","url":"https://huggingface.co/blog/async-rl-training-landscape"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"}]

Based on the search results, here's what I found about FormaRL's approach and performance characteristics:

## FormaRL Overview

FormaRL is a reinforcement learning framework for autoformalization which requires only a small amount of unlabeled data. It integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer.

## Performance Results

FormaRL can increase the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4–6x (4.04% → 26.15% on ProofNet and 2.4% → 9.6% on uproof) with merely 859 unlabeled data.

## Latency Considerations

Regarding latency concerns with Lean compilation, the search results indicate that one approach adopts GRPO with a soft (embedding-based) reward, which avoids the latency cost of a Lean4 REPL while still providing a semantic signal. This shows there's awareness in the field about Lean compilation latency as a training bottleneck.

## GRPO Training

GRPO is a policy-gradient algorithm that avoids a separate critic model by normalising rewards within groups of sampled completions. It has been applied to mathematical reasoning with verifiable rewards (compiler or symbolic checker).

Unfortunately, the search results don't contain specific information about the exact GPU hours, training cost, or rollout time latency metrics for FormaRL's training. For those detailed computational metrics, you may need to consult the full FormaRL paper on arXiv (2508.18914).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eeaeaeb7-de55-4027-bf82-38d99e730dcb",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "6baa0e11-c185-473f-8127-78ecb502e878",
  "toolUseResult": {
    "query": "FormaRL GRPO Lean compilation rollout time latency autoformalization training cost GPU hours",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FR6uGe4XW7963ZYQuGZKso",
        "content": [
          {
            "title": "FormaRL: RL-Driven Autoformalization for Lean 4",
            "url": "https://www.emergentmind.com/topics/formarl"
          },
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data | OpenReview",
            "url": "https://openreview.net/forum?id=Z2El1U94bq"
          },
          {
            "title": "[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/abs/2508.18914"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project",
            "url": "https://arxiv.org/html/2603.24372"
          },
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/pdf/2508.18914"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning",
            "url": "https://arxiv.org/pdf/2603.24372"
          },
          {
            "title": "Keep the Tokens Flowing: Lessons from 16 Open-Source RL Libraries",
            "url": "https://huggingface.co/blog/async-rl-training-landscape"
          },
          {
            "title": "Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics",
            "url": "https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"
          }
        ]
      },
      "Based on the search results, here's what I found about FormaRL's approach and performance characteristics:\n\n## FormaRL Overview\n\nFormaRL is a reinforcement learning framework for autoformalization which requires only a small amount of unlabeled data. It integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer.\n\n## Performance Results\n\nFormaRL can increase the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4–6x (4.04% → 26.15% on ProofNet and 2.4% → 9.6% on uproof) with merely 859 unlabeled data.\n\n## Latency Considerations\n\nRegarding latency concerns with Lean compilation, the search results indicate that one approach adopts GRPO with a soft (embedding-based) reward, which avoids the latency cost of a Lean4 REPL while still providing a semantic signal. This shows there's awareness in the field about Lean compilation latency as a training bottleneck.\n\n## GRPO Training\n\nGRPO is a policy-gradient algorithm that avoids a separate critic model by normalising rewards within groups of sampled completions. It has been applied to mathematical reasoning with verifiable rewards (compiler or symbolic checker).\n\nUnfortunately, the search results don't contain specific information about the exact GPU hours, training cost, or rollout time latency metrics for FormaRL's training. For those detailed computational metrics, you may need to consult the full FormaRL paper on arXiv (2508.18914)."
    ],
    "durationSeconds": 9.575033177000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eeaeaeb7-de55-4027-bf82-38d99e730dcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-27T20:39:47.725Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013HYwsm6Q4diMkVa4MaKct7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.18914",
  "prompt": "Extract: (1) Training compute details - how many GPU hours? What GPUs were used? (2) How many rollouts per training step? (3) What was the Lean compilation latency? (4) How many Lean REPL instances were used in parallel? (5) Training dataset size and duration. (6) Any CPU resource estimates mentioned. (7) How many training epochs/steps?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6baa0e11-c185-473f-8127-78ecb502e878",
  "isSidechain": false,
  "requestId": "req_011CbTiguanreSLxXQbaBpyx",
  "type": "assistant",
  "uuid": "e1917bcd-8003-41f5-ad0b-5a5d8b5e2adb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9YnzXHLCpcbPyW56JKzMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 53791,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 53791,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 896
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

_source line 85 · 2026-05-27T20:39:51.417Z_

<details><summary>↩ Tool result · `toolu_013HYwsm6Q4diMkVa4MaKct7`</summary>

```text
# FormaRL Paper - Resource & Training Details

Based on the provided webpage content, I cannot extract the requested technical specifications. The page contains only the abstract and metadata for the arXiv paper "FormaRL: Enhancing Autoformalization with no Labeled Data."

## What's Available:
The abstract mentions: "FormaRL can increase the pass@1 autoformalization accuracy...with merely 859 unlabeled data" and references the GRPO algorithm, but does not include:

- GPU specifications or compute hours
- Rollout counts per training step
- Lean compilation latency measurements
- Parallel REPL instance counts
- CPU resource estimates
- Training epoch/step counts

## Recommendation:
To find these implementation details, you would need to access the full PDF paper (available via the "View PDF" link on the arXiv page) rather than relying on the abstract alone. Technical papers typically reserve such computational specifics for the methods or appendix sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1917bcd-8003-41f5-ad0b-5a5d8b5e2adb",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "ab01193a-b8a6-4829-aaaa-61ddaef64f47",
  "toolUseResult": {
    "bytes": 46154,
    "code": 200,
    "codeText": "OK",
    "result": "# FormaRL Paper - Resource & Training Details\n\nBased on the provided webpage content, I cannot extract the requested technical specifications. The page contains only the abstract and metadata for the arXiv paper \"FormaRL: Enhancing Autoformalization with no Labeled Data.\"\n\n## What's Available:\nThe abstract mentions: \"FormaRL can increase the pass@1 autoformalization accuracy...with merely 859 unlabeled data\" and references the GRPO algorithm, but does not include:\n\n- GPU specifications or compute hours\n- Rollout counts per training step\n- Lean compilation latency measurements\n- Parallel REPL instance counts\n- CPU resource estimates\n- Training epoch/step counts\n\n## Recommendation:\nTo find these implementation details, you would need to access the full PDF paper (available via the \"View PDF\" link on the arXiv page) rather than relying on the abstract alone. Technical papers typically reserve such computational specifics for the methods or appendix sections.",
    "durationMs": 3687,
    "url": "https://arxiv.org/abs/2508.18914"
  },
  "sourceToolAssistantUUID": "e1917bcd-8003-41f5-ad0b-5a5d8b5e2adb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-27T20:39:56.583Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SEJnVvpyura253pArQj32s`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2508.18914",
  "prompt": "Extract ALL training details from the full paper: (1) How many GPU hours were used? What GPUs? (2) How many rollouts per training step? Group size for GRPO? (3) Lean compilation latency per sample. (4) How many parallel Lean REPL instances? (5) Training dataset size (859 unlabeled). (6) How many training epochs/steps total? (7) Any mention of CPU compute costs. (8) Batch size, learning rate, KL penalty coefficient. (9) How long did training take wall-clock? (10) How was the Lean interaction handled - what tool/library?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab01193a-b8a6-4829-aaaa-61ddaef64f47",
  "isSidechain": false,
  "requestId": "req_011CbTihZ8WehoRUPeqbS6ub",
  "type": "assistant",
  "uuid": "6cfe0b75-0306-4c4b-80fe-97542bed4521",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ixR1gB6Rk4uEcytp5QuDD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 54687,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 54687,
          "cache_creation_input_tokens": 394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 394
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

_source line 87 · 2026-05-27T20:40:01.582Z_

<details><summary>↩ Tool result · `toolu_01SEJnVvpyura253pArQj32s`</summary>

```text
# FormaRL Training Details Extraction

Based on the provided PDF content, I found limited explicit training details. Here's what is available:

## Key Training Specifications Found

**Dataset Size:** The paper mentions 859 unlabeled examples for training the autoformalization model.

**GPU Compute:** Specific GPU hour counts and GPU types are not explicitly stated in the extracted content.

**Rollouts & GRPO Parameters:** The group size for GRPO (Group Relative Policy Optimization) and rollouts per training step are not detailed in the visible sections.

**Lean Compilation:** Latency measurements per sample during Lean interaction are not provided.

**Parallel REPL Instances:** The number of concurrent Lean REPL instances is not specified.

**Training Duration:** Wall-clock training time is not mentioned in the available excerpt.

**Hyperparameters:** Batch size, learning rate, and KL penalty coefficient values are not visible in this PDF section.

**Training Epochs/Steps:** Total training iterations are not explicitly stated.

**CPU Costs:** No mention of CPU compute requirements.

**Lean Integration Tool:** The mechanism for Lean interaction (whether using a specific library or custom tooling) is not detailed in the extracted content.

## Recommendation
To obtain complete training details, consulting the full paper's appendix (particularly subsection A.1 on case studies or A.6 on additional experimental results) would be necessary, as these sections are referenced but not fully visible in the provided excerpt.

[Binary content (application/pdf, 825.8KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/webfetch-1779914396596-nj3lo5.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cfe0b75-0306-4c4b-80fe-97542bed4521",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "378051e5-23df-4176-8654-47c8765d4e17",
  "toolUseResult": {
    "bytes": 845666,
    "code": 200,
    "codeText": "OK",
    "result": "# FormaRL Training Details Extraction\n\nBased on the provided PDF content, I found limited explicit training details. Here's what is available:\n\n## Key Training Specifications Found\n\n**Dataset Size:** The paper mentions 859 unlabeled examples for training the autoformalization model.\n\n**GPU Compute:** Specific GPU hour counts and GPU types are not explicitly stated in the extracted content.\n\n**Rollouts & GRPO Parameters:** The group size for GRPO (Group Relative Policy Optimization) and rollouts per training step are not detailed in the visible sections.\n\n**Lean Compilation:** Latency measurements per sample during Lean interaction are not provided.\n\n**Parallel REPL Instances:** The number of concurrent Lean REPL instances is not specified.\n\n**Training Duration:** Wall-clock training time is not mentioned in the available excerpt.\n\n**Hyperparameters:** Batch size, learning rate, and KL penalty coefficient values are not visible in this PDF section.\n\n**Training Epochs/Steps:** Total training iterations are not explicitly stated.\n\n**CPU Costs:** No mention of CPU compute requirements.\n\n**Lean Integration Tool:** The mechanism for Lean interaction (whether using a specific library or custom tooling) is not detailed in the extracted content.\n\n## Recommendation\nTo obtain complete training details, consulting the full paper's appendix (particularly subsection A.1 on case studies or A.6 on additional experimental results) would be necessary, as these sections are referenced but not fully visible in the provided excerpt.\n\n[Binary content (application/pdf, 825.8KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/webfetch-1779914396596-nj3lo5.pdf]",
    "durationMs": 4995,
    "url": "https://arxiv.org/pdf/2508.18914"
  },
  "sourceToolAssistantUUID": "6cfe0b75-0306-4c4b-80fe-97542bed4521",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-27T20:40:04.914Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SaguFyQTCHBaJXNbnVGXsB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/webfetch-1779914396596-nj3lo5.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "378051e5-23df-4176-8654-47c8765d4e17",
  "isSidechain": false,
  "requestId": "req_011CbTiiJagKhv3b2AXe5NG8",
  "type": "assistant",
  "uuid": "516f8e11-d8bb-4f4b-a604-f12678224f39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwgNMhv724UKcPXoMKL6H8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 55081,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 55081,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 89 · 2026-05-27T20:40:05.439Z_

<details><summary>↩ Tool result · `toolu_01SaguFyQTCHBaJXNbnVGXsB`</summary>

```text
PDF pages extracted: 10 page(s) from /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/webfetch-1779914396596-nj3lo5.pdf (825.8KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "516f8e11-d8bb-4f4b-a604-f12678224f39",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "uuid": "4bce5da9-54c4-4257-bb47-1dc5b56d17d0",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/webfetch-1779914396596-nj3lo5.pdf",
      "originalSize": 845666,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/82f99182-f825-4b58-b9e8-01598f230d91/tool-results/pdf-ccc67189-aef4-41f5-a1fe-6bbcccac2128",
      "count": 10
    }
  },
  "sourceToolAssistantUUID": "516f8e11-d8bb-4f4b-a604-f12678224f39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

9 recorded events

### User

_source line 90 · 2026-05-27T20:40:05.437Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bce5da9-54c4-4257-bb47-1dc5b56d17d0",
  "isSidechain": false,
  "promptId": "aaa25d18-bbae-470e-b41d-94e880da1a3c",
  "type": "user",
  "isMeta": true,
  "uuid": "103076e1-9d90-45b5-aa6c-9709ad8c0acf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 91_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "4bce5da9-54c4-4257-bb47-1dc5b56d17d0",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Assistant

_source line 93 · 2026-05-27T20:43:26.867Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have extensive information. Let me synthesize what I've learned and address each reviewer issue:

1. **AAAI 2027 dates**: Official AAAI site confirms July 21 (abstract) and July 28 (paper), not Jul 26/Aug 2. The reviewer was right.

2. **Lean compilation CPU costs**: From my research:
   - Each Lean REPL instance with Mathlib imports needs ~2GB RAM (with optimizations)
   - Kimina Lean Server achieves ~1.5-2x speedup over baseline with LRU caching, ~29% speedup from caching
   - LeanInteract uses AutoLeanServer with one instance per process, and a c7i.16xlarge machine (64 vCPU, 128GB RAM) at ~$2.856/hr on-demand or ~$0.85-1.00/hr spot could theoretically run ~60 parallel instances at 2GB each. Working through the math: 7 configs × 2 models × 80K rollouts × 16 samples per rollout gives roughly 17.9M total compilations, which at ~10 seconds average per compilation translates to about 179M CPU-seconds or roughly 49 hours of compute time.

With 64 parallel instances running on a single machine, that's about 780 wall-clock hours per config, or 10,920 total. But I need to reconsider what the reviewer meant—they said "per configuration," which actually refers to each of the 14 config-model pairs individually. So recalculating: each pair involves 80K rollouts × 16 samples = 1.28M compilations × 10 seconds = 12.8M CPU-seconds = 3,556 CPU-hours. Dividing by 64 parallel instances gives roughly 56 wall-clock hours per pair, and multiplying by 14 pairs yields 780 wall-clock hours total, not per configuration as I initially thought.

Let me verify this is correct. Per config: 1.28M compilations at 10 seconds each equals 3,556 hours of serial CPU time, which becomes about 55.5 wall-clock hours with 64 parallel instances—roughly 2.3 days. Across all 14 configs, that's 777 wall-clock hours or about 32 days. The cost breaks down to $2,219 on-demand or around $777 at spot pricing. Though I'm realizing the sampling strategy in GRPO might not require all 16 samples to go through compilation—I need to think through whether each sample actually needs its own compilation pass.

Using something like Kimina Lean Server with LRU caching could give us a meaningful speedup, around 29%, which would help offset some of these costs. The real takeaway is that CPU expenses are substantial enough to warrant serious budget planning.

The human gaming audit is where things get expensive in a different way. With 14 config-model pairs and 200 samples each, that's 2,800 audits at 5-10 minutes per audit—translating to 233-467 hours of expert time. That's a significant hidden labor cost. I could reduce the sample size to 100, use stratified sampling to be smarter about which ones to audit, or implement a hybrid approach where an automated critic pre-filters and humans only audit the disagreements.

Now I'm diving into the CriticLean details.  The approach trains a critic model on Qwen's series using SFT and GRPO to evaluate whether Lean 4 formalizations are semantically faithful. They built CriticLeanBench with 500 samples and achieved 87% accuracy with Qwen3-32B-RL versus GPT-4o's 67.8%. The full pipeline—formalize, compile, critic check, iterate—reaches 84% accuracy on their 285K problem corpus, which is substantially better than compiler-only feedback at 54% or a single-pass approach at 38%. The critic provides a binary reward signal based on whether its judgment matches the ground truth label, and this learned signal is exactly what we'd need to improve our own iteration loop.

The key distinction is that CriticLean trains a specialized critic for semantic fidelity while our R_judge relies on a frozen general-purpose LLM, so we could either incorporate their trained critic as a reward component or use it as a comparison baseline. For the negative result scenario, we can frame cheap embedding rewards as a cost-effectiveness insight or highlight the surprising sufficiency of semantic signals for gaming-resistant autoformalization, and potentially publish the gaming-aware evaluation framework separately. The online RL work is confirmed for the MAR Workshop at NeurIPS 2025, not MATH.

The deeper issue is that this risks being just an ablation study, so I need to reframe it as the first gaming-aware reward composition study. Beyond empirical comparison, I could propose a principled method for selecting reward compositions, add an automated gaming detection metric that avoids manual auditing, or even formalize gaming-resistance as a property and demonstrate which compositions are Pareto-optimal. Looking at the FormaRL training details, they use 859 unlabeled statements from miniF2F and ProofNet as their base dataset.

Now examining the reward ablation results: FormaRL uses GRPO without KL divergence and a binary reward that only fires when both syntax and consistency checks pass. The consistency check relies on DeepSeek-V3 as the judge. Table 5 reveals the gaming problem clearly—removing the consistency check gives 100% syntax pass but 0% consistency, while removing syntax gives 74.66% consistency but only 0.27% syntax pass. With both checks, they get 35.58% syntax, 57.14% consistency, and 26.15% on the final metric. Interestingly, FormaRL already demonstrates that compilation-only rewards lead to gaming, and their manual review shows 38.8% accuracy versus 25.0% for RAutoformalizer.

This observation about reward hacking in FormaRL actually validates the core problem we're addressing. For the revision, I need to make several structural changes: elevate gaming-aware evaluation as a co-primary contribution by formalizing it as a framework with automated gaming detection metrics, add CriticLean as both related work and an experimental condition to create a three-way comparison between formally-grounded rewards, semantic rewards, and trained-critic rewards, and significantly rework the resource budget and contribution framing since this is a major revision rather than just an ablation study.

I should also reduce the manual audit burden by using CriticLeanGPT as an automated pre-filter to only audit disagreements, which cuts the workload from 2800 to around 500-800 cases, explicitly budget CPU resources at roughly 50K hours, and introduce a formal Gaming Resistance Score metric along with an algorithm for selecting reward compositions. I'll need to fix the AAAI dates to July 21/28, confirm the MAR Workshop, and prepare a framing for null results in RQ2 around cost-effectiveness principles.

Now I'm working through the Lean compilation budget more carefully—calculating the total CPU hours needed across all training runs with different reward configurations and accounting for caching optimizations.

I need to reconsider the parallelization constraints: while the c7i.16xlarge instance has 64 vCPUs, memory becomes the limiting factor when running multiple Lean processes simultaneously, each requiring around 2GB of RAM.

The real bottleneck emerges when interleaving RL training with compilation—the GPU sits idle during Lean compilation while the CPU handles verification, and vice versa during model generation. A more practical approach would be to run Kimina Lean Server on a separate CPU cluster, batching all 1024 compilations (64 prompts × 16 samples) across 128 parallel instances, which takes roughly 64 seconds per training step. This compilation time actually dominates the GPU compute time of 10-20 seconds, making it the critical constraint for the overall training pipeline.

Working through the actual numbers more carefully: using FormaRL's 859 training samples with GRPO over multiple epochs, each epoch generates about 13,744 compilations, and scaling across 50 epochs per run gives roughly 687K compilations per run, totaling around 9.6M compilations across all 14 configuration runs.

If I expand to larger datasets like ProofNet and FormalMATH-Lite with around 2K training prompts, running 40 epochs per configuration yields about 1.28M compilations per run, which scales to 17.9M total compilations. At 8 seconds per compilation, that's roughly 144M CPU-seconds or about 40K CPU-hours. Using spot instances on c7i.16xlarge machines at $0.90/hour with 60 parallel compilations per machine, the practical cost comes to around $600 on spot pricing or roughly $1,900 on-demand.

To keep wall-clock training time reasonable, I'd need 4-8 machines running in parallel to match GPU throughput, which brings the total CPU cost to somewhere between $600-1,500 depending on how much parallelism I actually need. This is a meaningful expense but not nearly as dramatic as the reviewer suggested.

Let me work through the reviewer's calculation more carefully. With 179 million CPU-seconds total and 64 parallel Lean instances, that's about 777 wall-clock hours on a single 64-vCPU machine. The key insight is that this translates to roughly $700 on spot pricing or $2,200 on-demand for that one machine, not the inflated figure I was initially calculating—I was conflating CPU-hours with machine-hours. So with 49,778 CPU-hours needed, a c7i.16xlarge with 64 vCPUs running one Lean instance per core means I need about 778 machine-hours total—$700 on spot pricing or $2,222 on-demand. The real constraint is wall-clock time though; a single machine would take 32 days, so I'd need at least 4 machines to keep it under a week. Now I'm reconsidering whether the 80K rollouts per config is realistic—FormaRL actually used around 859 samples, so the training budget might be significantly smaller than that estimate.

Let me work through a more concrete GRPO training scenario with 2K prompts, 30 epochs, and a group size of 16, which gives me about 960K compilations per run. Across 14 runs that's roughly 13.4M total compilations, and at 8 seconds average with caching, that's around 30K CPU-hours—translating to about 467 machine-hours or $420 in spot costs, finishing in roughly 5 days on 4 machines. But the original proposal included that 80K rollout number for a reason, so I should probably stick closer to it while just adding proper CPU budgeting.

Now I'm ready to draft the revised proposal with several key updates: fixing the AAAI dates to July 21/28, adding an explicit CPU budget in the $700-1,500 range, reducing the human audit to 100 stratified samples per config with CriticLeanGPT pre-filtering, incorporating CriticLean into related work and as a baseline comparison, framing negative results upfront, and elevating the gaming-aware evaluation as a co-primary contribution with a formal Gaming Resistance Score. I should also confirm the MAR Workshop venue and address the "fundamentally ablation" concern by highlighting the methodological contributions like the GRS metric and reward composition selection. The level should probably stay at "solid+" given these improvements, though I'll note the mitigation strategies for the ablation worry.

Writing the revised JSON proposal...

For the infrastructure, I'm considering whether to use Kimina Lean Server alongside LeanInteract—Kimina offers 1.5-2x speedup with LRU caching and is purpose-built for RL training loops, while LeanInteract provides the Python interface and crash recovery. I could leverage Kimina as the compilation backend for throughput while keeping LeanInteract's message parsing for error classification.

On the "fundamentally an ablation study" concern, the real way to address this is by proposing a formal Gaming Resistance Score as an automated metric that goes beyond just comparing reward signals under GRPO—this becomes a methodological contribution that elevates the work beyond pure ablation.

The stronger move though is proposing Adaptive Gaming-Resistant Reward Composition, where the reward weights adjust dynamically during training based on detected gaming signals rather than staying fixed, which would be genuinely novel and address the reviewer's core concern about novelty.

I can structure this as three phases: first run the ablation across eight fixed compositions including a trained critic, then design and test the adaptive method based on what I learn, and finally introduce a Gaming Resistance Score metric for automated evaluation. That gives me three solid contributions—a systematic comparison of reward sources, the adaptive composition method itself, and the evaluation metric—which transforms this from a pure ablation study into something with real methodological innovation.

Now I need to check if this fits the timeline. From late May to the ICLR deadline in September is about seventeen weeks, and I can allocate eight weeks for the pipeline and fixed ablation, four weeks for the adaptive composition, and five weeks for evaluation and writing. It's tight but workable with the auto_research framework.

For the human audit bottleneck, I can use CriticLeanGPT as an automated pre-filter to handle all compilable outputs at 87% accuracy, then focus manual audits on just a stratified sample of a hundred per model rather than per configuration, concentrating effort on cases where the automated and manual judgments disagree. I'm settling on using automated metrics across all outputs, then manually auditing a stratified sample of 50 per model plus 100 adversarially-selected disagreement cases—200 audits total at 17-33 hours. But I realize the gaming audit needs sufficient samples per configuration to get meaningful statistics, so 50 per config-model pair (700 total) is more appropriate despite the higher time cost of 58-117 hours. The real solution is to apply the automated GRS metric comprehensively across all compilable outputs and use that as the foundation.

For the key configurations—baseline, formal-only, full hybrid, and trained critic—I'll do targeted manual audits of 50 per pair across just those 4 configs and 2 models, bringing it down to 400 audits and roughly 50 hours of work. That's a reasonable scope for the research. Now I'm ready to write out the complete revised proposal and make sure the AAAI deadline is corrected.

I've identified the main changes: fixing the conference dates, adding explicit CPU budgets for Lean compilation, bringing in Kimina as the compilation backend, restructuring the human audit to combine automated GRS scoring with stratified manual sampling, adding CriticLean to related work and as a config variant, pre-committing to a cost-effectiveness framing if results are negative, elevating gaming-resistant evaluation as a co-primary contribution with the GRS metric, introducing AGRC as a methodological contribution, and confirming the NeurIPS 2025 MAR Workshop as the venue.

Now I'm recalculating the resource budgets more carefully—the GPU allocation comes to around 1,680 H100-hours at $4,200 total, and I'm working through the CPU requirements for the 19.2 million compilations across all training runs.

I'm realizing that compilation actually happens during training rather than as a separate phase, so the wall-clock time overlaps with GPU training. The real question is whether compilation becomes the bottleneck during a single training step.

With the GPU generating 512 samples in about 20-30 seconds, the CPU can only compile those samples in roughly 68 seconds with 60 parallel instances, which means compilation is indeed the limiting factor. To keep pace with GPU throughput, I'd need around 120-180 parallel instances, which translates to 2-3 dedicated CPU machines per training run.

For the budget breakdown, this works out to roughly 40,000 CPU-hours total across all training runs, costing around $700-1,500 with spot pricing, requiring 2-3 CPU machines running alongside the GPU setup for compilation to keep up.

Now I'm setting up the ablation study matrix with ten different configurations to test, ranging from individual components like binary compilation, formal signals, embedding similarity, and LLM judging, through various hybrid combinations, up to the full adaptive gaming-resistant composition approach. I'm realizing I need to focus on strengthening the methodology rather than expanding the config count. The ablation study should demonstrate clear methodological contributions, so I'll stick with these 8 core configurations plus AGRC, which gives me a solid experimental design without unnecessary complexity.

Now I'm calculating the computational budget—running all 9 configs on the 7B model plus AGRC, then selectively testing the top performers on the 30B model to keep costs manageable while still validating scalability.

I'm also reconsidering whether to use CriticLeanGPT as a reward signal during training. It would add significant overhead since the 14B or 32B model would need to run inference alongside the policy model, but comparing a general LLM judge against a specialized trained critic could be a genuinely interesting contribution.

For the Gaming Resistance Score, I'm defining it as a metric that captures the gap between reward and faithfulness—if a model achieves high reward but low faithfulness, the score drops, but when they track together, it stays high.

I'm reconsidering the approach: instead of a simple ratio, I'll use Spearman rank correlation between the reward signal and faithfulness scores. This avoids arbitrary thresholds and directly measures whether the reward is gaming-resistant by checking if it correlates with actual faithfulness. A high correlation means the reward is aligned with what matters; low or negative correlation indicates gaming.

Now I'm putting together the full revised JSON specification.

Let me also verify the CriticLean paper details—it's a July 2025 arXiv preprint with models available on HuggingFace, so I'll cite it accordingly.

I'm rethinking the reviewer's feedback about this being an ablation study. To strengthen the contribution, I'm introducing AGRC (Adaptive Gaming-Resistant Reward Composition), a dynamic reward weighting scheme that monitors...

Writing the methodology section...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "103076e1-9d90-45b5-aa6c-9709ad8c0acf",
  "isSidechain": false,
  "requestId": "req_011CbTiibCK4AhuX87zNmFWG",
  "type": "assistant",
  "uuid": "517d2e0c-6fc6-4d5f-b184-52d2652edd0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBVtjiqwkiPYGcgze852Bu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12665,
      "cache_read_input_tokens": 55733,
      "output_tokens": 16651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12665,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 16651,
          "cache_read_input_tokens": 55733,
          "cache_creation_input_tokens": 12665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12665
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

_source line 94 · 2026-05-27T20:46:03.183Z_

Now I have thorough research on all reviewer issues. Let me synthesize my findings and construct the revised proposal.

**Key findings from research:**
1. **AAAI 2027 dates confirmed**: Jul 21 abstract / Jul 28 paper (from official aaai.org)
2. **CriticLean (arXiv Jul 2025)**: Trains CriticLeanGPT via SFT+GRPO on Qwen2.5/Qwen3 to evaluate semantic fidelity. Best model Qwen3-32B-RL achieves 87.0% accuracy on CriticLeanBench (vs GPT-4o's 67.8%). Pipeline lifts autoformalization accuracy from 54% (compiler-only) to 84% (compiler+critic). Uses binary reward matching expert labels. Includes FineLeanCorpus (285K problems) and CriticLeanBench (500 samples).
3. **Online RL for Autoformalization venue CONFIRMED**: MAR Workshop (Multimodal Algorithmic Reasoning) at NeurIPS 2025, paper #12 in poster list.
4. **Lean compilation costs**: ~2GB RAM per Lean instance with Mathlib. Kimina Lean Server achieves 1.5-2x speedup with LRU caching (~29% improvement). c7i.16xlarge (64 vCPU, 128GB) at ~$0.90/hr spot can run ~60 parallel instances.
5. **FormaRL details**: Uses 859 unlabeled samples, binary reward (SC∧CC), GRPO without KL. Already shows gaming: w/o CC yields 100% SC but 0% CC. Manual audit rate: 38.8% accuracy.
6. **ICLR 2027**: Sep 19 abstract / Sep 24 paper (estimated, CFP not yet published).

Now constructing the comprehensive revision:

```json
{
  "change_type": "major",
  "changes_made": [
    "Fixed AAAI 2027 deadline dates to Jul 21 (abstract) / Jul 28 (paper) per official aaai.org, from incorrect Jul 26 / Aug 2",
    "Added explicit CPU resource budget for Lean compilation: ~40,000 CPU-hours on c7i.16xlarge instances ($700-1,500 spot), requiring 2-3 dedicated CPU machines per concurrent training run to match GPU throughput",
    "Introduced Kimina Lean Server as compilation backend for ~1.5-2x throughput improvement via LRU caching of Mathlib imports, reducing avg compilation latency from ~10s to ~7s",
    "Added CriticLean (arXiv July 2025) as related work: trains CriticLeanGPT via SFT+GRPO to evaluate semantic fidelity of Lean 4 formalizations, achieving 87.0% accuracy on CriticLeanBench vs GPT-4o's 67.8%. Lifts pipeline accuracy from 54% (compiler-only) to 84% (compiler+critic). Added CriticLeanGPT-based reward (R_critic) as C5 in ablation matrix, testing trained-critic signals vs general-purpose LLM judge vs formally-grounded signals",
    "Restructured human gaming audit from infeasible 2800 manual audits to tiered approach: (a) automated Gaming Resistance Score (GRS) computed on ALL compilable outputs via CriticLeanGPT + roundtrip consistency, (b) stratified manual expert audit of 50 samples per config on 8 key config-model pairs = 400 total audits (~50 expert-hours), with focus on gaming-specific behaviors (axiom fabrication, premise mistranslation, semantic vacuity)",
    "Elevated gaming-aware evaluation from diagnostic tool to co-primary methodological contribution: introduced Gaming Resistance Score (GRS) = Spearman rank correlation between reward signal and faithfulness score, computable automatically without human audit. GRS provides a principled, scalable gaming metric that can serve as a standard evaluation tool beyond this paper",
    "Added Adaptive Gaming-Resistant Reward Composition (AGRC) as second methodological contribution: during training, monitor GRS on held-out validation set every K steps and dynamically re-weight reward components to maximize GRS-weighted performance. This transforms the paper from pure ablation to method + framework + ablation",
    "Pre-committed negative result framing for RQ2: if formally-grounded signals ≈ semantic signals on faithfulness, position as 'the cost-effectiveness principle for autoformalization rewards'—cheap embedding rewards achieve comparable gaming resistance to expensive error classification pipelines, with implications for practical deployment. The GRS metric and AGRC method remain valid contributions regardless",
    "Expanded ablation matrix from 7 to 9 configurations (adding trained-critic C5 and AGRC C9), with tiered model strategy: all 9 configs on Qwen2.5-Coder-7B-Instruct, top 4 configs + AGRC on Qwen3-Coder-30B-A3B-Instruct, reducing total runs from 20 to 14 while maintaining key comparisons",
    "Confirmed Online RL for Autoformalization venue attribution as MAR Workshop (Multimodal Algorithmic Reasoning) at NeurIPS 2025—verified in accepted papers list at marworkshop.github.io/neurips25/",
    "Reframed paper contribution structure from 'ablation study' to three-pronged: (1) GRS as automated gaming-resistance evaluation metric, (2) AGRC as adaptive reward composition method, (3) first systematic multi-source reward comparison as empirical foundation. Paper is viable at ICLR 2027 even if ablation results are inconclusive, because GRS and AGRC are independent contributions",
    "Updated resource estimates with CPU costs, reduced human audit budget, and tiered model training strategy"
  ],
  "title": "Beyond Compilation: Adaptive Gaming-Resistant Reward Composition for Autoformalization RL",
  "core_problem": "RL-based autoformalization has progressed from binary compilation rewards (FormaRL, COLM 2025) to composite rewards combining type-checking with embedding similarity (Online RL for Autoformalization, MAR @ NeurIPS 2025) and from frozen LLM judges to trained critic models (CriticLean, arXiv July 2025). Yet three critical questions remain unanswered. First, what SOURCE of reward signal—compiler-derived, embedding-based, or learned-critic—produces the most FAITHFUL formalizations? 'Do LLMs Game Formalization?' (VerifAI-2 @ ICLR 2026) demonstrates that 87-99% compilation success masks significant unfaithfulness, while FormaRL's own ablation shows syntax-only RL yields 100% compilation but 0% semantic consistency—confirming that models aggressively game any single-source reward. Second, how should we MEASURE gaming resistance without expensive manual audits? Current evaluation relies on manual faithfulness annotation (200+ expert-hours for comprehensive assessment), creating an unsustainable bottleneck. Third, can reward composition be made ADAPTIVE during training to resist gaming as it emerges, rather than relying on fixed compositions chosen a priori? Process-Verified RL for Theorem Proving (NeurIPS 2025) shows formally-grounded signals outperform binary rewards for proof search, but no work has tested whether this advantage transfers to autoformalization or whether cheap semantic signals suffice.",
  "opportunity": "Four converging trends create a unique opportunity: (1) Process reward models are proven effective for reasoning (ThinkPRM, FOVER, Process-Verified RL), but no work systematically compares reward signal SOURCES (compiler vs. embedding vs. learned critic) for autoformalization RL; (2) The formalization gaming problem is newly identified (VerifAI-2 @ ICLR 2026, LLMs Gaming Verifiers @ ICLR 2026) but no automated metric exists for gaming resistance—evaluation still requires expensive manual audits; (3) CriticLean (July 2025) demonstrates that trained critic models can assess semantic fidelity at 87% accuracy, creating a new reward signal category (learned-critic) that is neither purely formal nor purely semantic—but has not been tested as an RL reward signal for training autoformalizers; (4) Kimina Lean Server (2025) and LeanInteract v0.11.3 provide the infrastructure for high-throughput compilation with LRU caching, making large-scale RL with compiler feedback practical. The key novelty is not just comparing reward signals, but introducing (a) an automated Gaming Resistance Score (GRS) for scalable evaluation and (b) Adaptive Gaming-Resistant Reward Composition (AGRC) that dynamically adjusts signal weights during training. These methodological contributions transcend the specific ablation, providing tools applicable to any RL-from-verifier setting.",
  "landscape": "FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency reward (SC∧CC), achieving 26.15% pass@1 on ProofNet from Qwen2.5-Coder-7B-Instruct using only 859 unlabeled samples; its own ablation reveals aggressive gaming—syntax-only RL yields 100% compilation but 0% consistency, consistency-only yields 0.27% compilation but 74.66% consistency. Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025) extends this with composite rewards combining type-check + exact-match (BEq/BEq+) + continuous embedding similarity, using GRPO with KL penalty; type-check rate improves from 17.29% to 26.01% but semantic gains remain modest, confirming that multi-signal composition alone doesn't solve faithfulness. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite via SFT+RLVR with knowledge-reasoning fusion. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO on Qwen2.5/Qwen3 series to assess semantic fidelity of Lean 4 formalizations, achieving 87.0% accuracy on CriticLeanBench (vs GPT-4o's 67.8%); its pipeline lifts autoformalization accuracy from 38% (single-pass) to 54% (compiler feedback) to 84% (compiler+critic)—but CriticLeanGPT is used only for iterative rejection filtering, not as a direct RL reward signal during GRPO training. CriticLean also provides FineLeanCorpus (285K problems) and CriticLeanBench (500 annotated pairs). Monotonic Reference-Free Refinement (January 2026) uses masked composite objectives across Formal Validity, Logical Preservation, Mathematical Consistency, and Formal Quality using LLM judges. Do LLMs Game Formalization? (VerifAI-2 @ ICLR 2026) shows frontier models achieve 87-99% compilation while exhibiting systematic unfaithfulness: GPT-5 fabricates axioms, DeepSeek-R1 mistranslates premises. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR-trained models systematically abandon genuine reasoning for shortcut strategies. Process-Verified RL for Theorem Proving (NeurIPS 2025) extracts tactic-level process rewards from Lean for GRPO, showing formally-grounded signals outperform binary rewards—but targets tactic sequences, not whole-statement autoformalization. Process-Driven Autoformalization (arXiv 2024) uses Lean compiler feedback for process-supervised best-of-N selection via SFT. ReForm (ICLR 2026) proposes reflective autoformalization with PBSO using position-dependent rewards. Autoformalizer with Tool Feedback (October 2025) classifies Lean error messages into categories for iterative repair, demonstrating feasibility of error classification. Faithful Autoformalization via Roundtrip Verification (April 2026) uses formalize→backtranslate→re-formalize→check equivalence as a faithfulness metric. Cycle Consistency Fine-tuning (March 2026) applies GRPO with embedding-based cycle consistency reward. FormalEvolve (March 2026) uses compilation-gated evolutionary search. Kimina Lean Server (2025) provides high-performance Lean verification with LRU caching, achieving 1.5-2x speedup over baseline tools. The gap: no work (a) systematically compares reward signal SOURCES (compiler-derived vs. embedding vs. learned-critic) for autoformalization RL, (b) proposes automated gaming resistance metrics, or (c) adaptively composes rewards based on gaming detection during training.",
  "inspired_by": "Convergence of four threads: (1) Process-Verified RL (NeurIPS 2025) proving formally-grounded process rewards help proof search—but untested for autoformalization; (2) CriticLean (July 2025) demonstrating that trained critic models assess semantic fidelity at 87% accuracy and lift pipeline quality from 54% to 84%—but only used for rejection filtering, not as RL reward signals; (3) Formalization gaming literature (VerifAI-2, LLMs Gaming Verifiers, both ICLR 2026) revealing compilation-optimized models game verifiers, plus FormaRL's own ablation showing syntax-only RL yields 100% compilation, 0% consistency—demanding gaming-resistant reward design with automated detection; (4) Online RL for Autoformalization (MAR @ NeurIPS 2025) showing composite type-check + embedding rewards yield modest semantic gains—suggesting the COMPOSITION DYNAMICS matter more than just adding signals. The deeper insight: the field treats reward composition as a static design choice, but gaming is a dynamic phenomenon that emerges during training. Adaptive composition that responds to gaming indicators during training could fundamentally change the reward design paradigm.",
  "approach": "We introduce two methodological contributions—Gaming Resistance Score (GRS) and Adaptive Gaming-Resistant Reward Composition (AGRC)—grounded in the first systematic multi-source reward comparison for autoformalization RL.\n\n**Phase 1: Multi-Source Reward Signal Extraction**\n\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's structured Message objects (severity, position, content), we classify compiler diagnostics via regex-based pattern matching into an ordered error hierarchy: parse errors → name resolution failures → type-level errors → clean compilation. This yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} based on highest elaboration stage reached, plus density bonus for fraction of error-free declarations. Compilation throughput via Kimina Lean Server with LRU caching of Mathlib imports (~7s avg vs ~10s uncached).\n\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL statement and backtranslation of generated formal statement (reference-free, following Online RL for Autoformalization's approach but with backtranslation).\n\n(c) LLM judge R_judge: binary faithfulness judgment from frozen general-purpose LLM (following FormaRL's consistency check).\n\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT (Qwen3-8B-RL variant for inference efficiency), used as reward signal during GRPO training. This is the first use of CriticLean's trained critic as a direct RL reward rather than rejection filter.\n\n**Phase 2: Systematic Ablation (9 Configurations)**\n  C1: Binary compilation only (FormaRL reproduction)\n  C2: Graded formal signal only (R_formal)\n  C3: Embedding similarity only (R_embed)\n  C4: LLM judge only (R_judge)\n  C5: Trained critic only (R_critic via CriticLeanGPT)\n  C6: Formal + embedding hybrid (R_formal + R_embed)\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\n  C8: Full hybrid (R_formal + R_embed + R_critic)\n  C9: AGRC (adaptive, see below)\n  Tiered model strategy: all 9 configs on Qwen2.5-Coder-7B-Instruct; top 4 configs by GRS + AGRC on Qwen3-Coder-30B-A3B-Instruct.\n\n**Phase 3: Gaming Resistance Score (GRS) — Contribution 1**\nWe introduce GRS as an automated, scalable metric for reward gaming resistance:\n  GRS(R) = ρ_s(R(x), F(x)) over a held-out evaluation set\nwhere ρ_s is Spearman rank correlation, R(x) is the reward signal value, and F(x) is a faithfulness score combining roundtrip consistency (formalize→backtranslate→re-formalize→check equivalence) and CriticLeanGPT judgment. GRS ∈ [-1, 1]: high GRS means reward tracks faithfulness; low/negative GRS indicates gaming (high reward, low faithfulness). Key properties: (i) fully automated—no manual audit required; (ii) decomposable—can compute GRS for each signal component independently; (iii) comparable across compositions. We validate GRS against manual faithfulness audits on 400 samples.\n\n**Phase 4: Adaptive Gaming-Resistant Reward Composition (AGRC) — Contribution 2**\nInstead of fixed reward weights, AGRC dynamically adjusts composition during training:\n  R_AGRC(x, t) = Σ_k w_k(t) · R_k(x)\nEvery K training steps (K=500), compute GRS_k for each signal component on a held-out validation batch. Re-weight: w_k(t+1) ∝ w_k(t) · exp(η · GRS_k(t)), then normalize. Signals exhibiting high reward but low faithfulness correlation (low GRS) get downweighted; gaming-resistant signals get upweighted. This creates an online defense against gaming as it emerges during training.\n\n**Training:** GRPO with KL penalty, training Qwen2.5-Coder-7B-Instruct (for FormaRL comparison at 26.15% pass@1 on ProofNet) and Qwen3-Coder-30B-A3B-Instruct (for SOTA pursuit). Training on ProofNet + FormalMATH-Lite datasets.\n\n**Gaming-Aware Evaluation Framework — Contribution 3:**\n  (1) Standard: BEq@1, pass@1, ASSESS structural similarity\n  (2) Automated faithfulness: Roundtrip consistency rate + CriticLeanGPT agreement rate\n  (3) GRS per configuration (automated, computed on full output sets)\n  (4) Stratified manual expert audit: 50 samples × 8 key config-model pairs = 400 total audits, targeting axiom fabrication, premise mistranslation, and semantic vacuity. Used to validate GRS against human judgment.\n  (5) Signal-quality correlation: Spearman rank correlation between each reward component and human-judged faithfulness on 400 samples\n  (6) GRS-accuracy Pareto analysis: which compositions achieve best tradeoff between gaming resistance (GRS) and autoformalization accuracy (BEq@1)?\n\n**Research Questions:**\n  RQ1: Does graded formal signaling (C2) outperform binary compilation (C1)?\n  RQ2: Do formally-grounded signals (C2) outperform semantic signals (C3, C4) and learned-critic signals (C5) on faithfulness metrics? [Pre-committed framing: if null, report as cost-effectiveness principle]\n  RQ3: Does hybrid composition (C6-C8) yield additive faithfulness gains over individual signals?\n  RQ4: Which static compositions produce the highest GRS?\n  RQ5: Does AGRC (C9) outperform the best static composition on both accuracy and GRS?\n  RQ6: Does GRS reliably predict human-judged gaming rates? (GRS validation)",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1400 H100 (9 configs on 7B = 9×70 + top 4+AGRC on 30B = 5×70 + 100 grid search + 100 baseline + 80 evaluation)",
      "cpu_hours": "~40,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server (14 training runs × ~960K compilations × 8s avg with LRU caching)",
      "human_audit_hours": "~50 expert-hours for 400 stratified manual gaming audits (50 samples × 8 key config-model pairs, 5-10 min per audit)",
      "timeline": "15-17 weeks (4 wks pipeline + error classification + GRS implementation, 6 wks RL training across configs, 3 wks AGRC development/training, 4 wks evaluation/gaming audit/writing)",
      "estimated_gpu_cost": "$3,500 (at ~$2.50/hr H100 spot)",
      "estimated_cpu_cost": "$700-1,500 (c7i.16xlarge spot at ~$0.90/hr, requiring 2-3 machines per concurrent training run for compilation throughput)"
    },
    "human_in_loop": {
      "gpu_hours": "1100 H100 (Claude accelerates pipeline, hyperparameter search, AGRC tuning, and GRS validation analysis)",
      "cpu_hours": "~35,000 CPU-hours",
      "human_audit_hours": "~40 expert-hours (Claude assists with audit pre-filtering and analysis)",
      "timeline": "12-14 weeks",
      "claude_api_cost": "$500 (code generation, error classification pipeline, AGRC implementation, GRS analysis, paper drafting)",
      "estimated_gpu_cost": "$2,750",
      "estimated_cpu_cost": "$600-1,200"
    },
    "auto_research": {
      "gpu_hours": "1100 H100",
      "cpu_hours": "~35,000 CPU-hours",
      "human_audit_hours": "~30 expert-hours (automated pre-filtering reduces manual load to disagreement cases)",
      "timeline": "9-11 weeks",
      "claude_api_cost": "$700 (end-to-end experiment orchestration, automated ablation sweeps, AGRC development, GRS computation, gaming audit support, paper drafting)",
      "estimated_gpu_cost": "$2,750",
      "estimated_cpu_cost": "$600-1,200",
      "speed_bottleneck": "Lean 4 compilation latency remains primary bottleneck despite Kimina Lean Server caching (~7s avg per sample). With 120-180 parallel Lean instances (2-3 c7i.16xlarge machines), compilation throughput approximately matches GPU generation throughput during GRPO. CriticLeanGPT inference for R_critic adds ~15% overhead per rollout batch (mitigated by running Qwen3-8B-RL variant on separate GPU)."
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, paper Sep 24, 2026) — PRIMARY, ~17 weeks available. Three-contribution structure (GRS metric + AGRC method + systematic comparison) makes paper viable even if ablation results are inconclusive",
    "AAAI 2027 (abstract Jul 21, paper Jul 28, 2026) — STRETCH, ~8 weeks, only feasible if limiting to 7B model and 5 core configs with GRS but without AGRC",
    "ARR July 2026 cycle (Jul 30) — committable to EMNLP 2026 or NAACL 2027"
  ],
  "level": "solid+",
  "key_references": [
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (VerifAI-2 @ ICLR 2026)",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)",
    "Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)",
    "Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)",
    "Process-Driven Autoformalization in Lean 4 (arXiv 2024)",
    "Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)",
    "ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Autoformalizer with Tool Feedback (arXiv October 2025)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)",
    "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv March 2026)",
    "FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv March 2026)",
    "Process Reward Models That Think [ThinkPRM] (arXiv 2025)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)",
    "Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems (arXiv July 2025)"
  ],
  "description": "We address the open problem of gaming-resistant reward design for autoformalization RL through three contributions. First, we introduce the Gaming Resistance Score (GRS), an automated metric that measures the Spearman rank correlation between a reward signal and faithfulness (via roundtrip consistency + CriticLeanGPT judgment), providing scalable gaming evaluation without expensive manual audits. Second, we propose Adaptive Gaming-Resistant Reward Composition (AGRC), which dynamically re-weights reward components during training based on their GRS on a held-out validation set—upweighting gaming-resistant signals and downweighting gamed ones as gaming emerges. Third, we ground these contributions in the first systematic comparison of reward signal SOURCES for autoformalization: formally-grounded (graded error-category classification from Lean compiler diagnostics via LeanInteract), semantic (embedding similarity, frozen LLM judge), and learned-critic (CriticLeanGPT, the first use of trained critic models as direct RL rewards for autoformalization rather than rejection filters). Our 9-configuration ablation under GRPO training includes the novel CriticLeanGPT reward signal and AGRC, evaluated not just on standard BEq@1 and ASSESS metrics but also on automated GRS and validated against 400 stratified manual gaming audits. We address five research questions: whether graded formal signals outperform binary compilation (RQ1), whether signal source matters for faithfulness (RQ2, with pre-committed cost-effectiveness framing for null results), whether hybrid compositions yield additive gains (RQ3), which compositions maximize GRS (RQ4), and whether AGRC outperforms static compositions (RQ5). Compilation throughput is handled via Kimina Lean Server with LRU caching on dedicated CPU clusters. We train Qwen2.5-Coder-7B-Instruct (for FormaRL comparison) and Qwen3-Coder-30B-A3B-Instruct (for SOTA pursuit), targeting ICLR 2027. The paper is designed to be publishable under any outcome: if formally-grounded signals dominate, we advance reward design; if they don't, we establish the cost-effectiveness principle; regardless, GRS and AGRC are independent methodological contributions.",
  "project_name": "reward_comp_autoform",
  "source": "web_research"
}
```

**Summary of changes (major revision):**

| Issue | Resolution |
|---|---|
| **AAAI dates wrong** | Fixed to Jul 21/28 per official aaai.org |
| **CPU costs unbudgeted** | Added ~40K CPU-hours, $700-1,500 spot, via Kimina Lean Server with LRU caching on 2-3 c7i.16xlarge machines per concurrent training run |
| **Human audit infeasible (2800)** | Reduced to 400 stratified audits (~50 expert-hours) on 8 key config-model pairs, with automated GRS on all outputs |
| **CriticLean missing** | Added as related work AND as novel C5 reward signal (first use of trained critic as RL reward for autoformalization, not just rejection filter) |
| **No negative-result mitigation** | Pre-committed "cost-effectiveness principle" framing; GRS and AGRC are valid contributions regardless of ablation outcome |
| **MAR Workshop unverified** | Confirmed: paper #12 in MAR poster list at marworkshop.github.io/neurips25/ |
| **Fundamentally an ablation** | Elevated to three-contribution paper: (1) GRS automated metric, (2) AGRC adaptive method, (3) systematic comparison as empirical foundation. Tiered model strategy reduces runs while maintaining rigor |

Sources:
- [AAAI-27 Official Dates](https://aaai.org/conference/aaai/aaai-27/)
- [CriticLean Paper](https://arxiv.org/abs/2507.06181)
- [CriticLeanGPT on HuggingFace](https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL)
- [MAR Workshop NeurIPS 2025 - Accepted Papers](https://marworkshop.github.io/neurips25/)
- [Kimina Lean Server](https://arxiv.org/html/2504.21230v1)
- [LeanInteract GitHub](https://github.com/augustepoiroux/LeanInteract)
- [FormaRL Paper](https://arxiv.org/abs/2508.18914)
- [MATH-AI Workshop NeurIPS 2025](https://mathai2025.github.io/papers/)
- [AWS c7i.16xlarge Pricing](https://instances.vantage.sh/aws/ec2/c7i.16xlarge)
- [Conference Deadlines](https://trybibby.com/conference-deadlines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "517d2e0c-6fc6-4d5f-b184-52d2652edd0e",
  "isSidechain": false,
  "requestId": "req_011CbTiibCK4AhuX87zNmFWG",
  "type": "assistant",
  "uuid": "1db79680-5145-42c0-8ff3-ae058c180d3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBVtjiqwkiPYGcgze852Bu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12665,
      "cache_read_input_tokens": 55733,
      "output_tokens": 16651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12665,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 16651,
          "cache_read_input_tokens": 55733,
          "cache_creation_input_tokens": 12665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12665
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

_source line 95_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "1db79680-5145-42c0-8ff3-ae058c180d3c",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 96_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 97_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"Reframed core research question from 'replace binary with…",
  "leafUuid": "1db79680-5145-42c0-8ff3-ae058c180d3c",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---

### Runtime record

_source line 98_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization reward composition study based on reviewer feedback",
  "sessionId": "82f99182-f825-4b58-b9e8-01598f230d91"
}
```

---
