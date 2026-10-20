# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # TTRA: Critic-Guided Test-Time Ret

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/6636e8e6-7680-4dcb-9644-3680077f6940.jsonl`
- **Structured JSON:** [`25b84342af3eb0050af4.json`](../../sessions/25/25b84342af3eb0050af4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:15:23.437Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:15:23.437Z",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization\n\n## Core Problem\n\nCurrent autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning dramatically but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in the multi-tier reward setting (compilation + critic + BEq); and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation, yet no prior work fine-tunes the retriever during test-time RL. Can we make TTRL viable for autoformalization by combining compilation-error-driven co-adaptive retrieval that exploits Lean 4's full structured error taxonomy, a calibrated semantic critic reward, and principled adaptation of binary-reward debiased RL to multi-tier rewards?\n\n## Research Opportunity\n\nFour independently validated capabilities have never been combined: (1) Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode. R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv 2601.11443, Jan 2026) shows test-time retrieval adaptation is achievable via self-supervised prediction. Critically, the prevalence of identifier hallucination as the dominant error class is now established by converging evidence from multiple independent studies: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) provides the strongest quantitative evidence, finding that 47.3% of 3,189 sampled compilation errors from DeepSeek-R1 on applied mathematics domains stem from 'invocation of non-existent theorems or definitions'—directly exceeding Phase -1's ≥40% Tier 1 threshold. DDR (arXiv 2511.11990) quantifies that ICL-based dependency generation produces ~30% hallucinated (non-existent) Mathlib identifiers (Hall_m=0.21-0.39 across frontier LLMs), while retrieval-based DDR reduces hallucination to <2% (Hall_m=0.016). The RAutoformalizer (ICLR 2025 Spotlight) explicitly classifies compilation errors into 'Hallucination' (errors caused by hallucination of identifiers) and 'Others', establishing identifier hallucination as a primary error class. MathAtlas (May 2026) further shows a 66% performance advantage for Mathlib-grounded definitions (27.9% vs 16.8% correct, p<0.001), confirming that dependency availability is the critical bottleneck. Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL-based autoformalization—where Lean's structured error taxonomy (unknownIdentifier, type mismatch with type signatures, failed to synthesize with typeclass names, unknown namespace) provides a graded hierarchy of machine-parseable signals for retriever training. (2) TTRL with debiasing has advanced rapidly. DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed +/-1 advantages, and consensus-based off-policy refinement, achieving up to 19.0% relative improvement over ETMR on AIME 2024 (4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B). But DDRL assumes binary correct/incorrect rewards. GDPO (NVIDIA, arXiv 2601.05242, Jan 2026) addresses multi-reward GRPO through per-reward decoupled normalization, preventing reward signal collapse. The combination—binarize multi-tier rewards for DDRL's debiasing, then enrich with GDPO's per-reward normalization for continuous components—has not been attempted. (3) CriticLean (July 2025) provides the missing reward signal: CriticLeanGPT-14B-RL achieves 84.8% accuracy on CriticLeanBench (87.0% for the 32B variant), raising autoformalization pipeline accuracy from 54% to 84% over compilation-only feedback. However, CriticLeanBench evaluates on a balanced 250-correct/250-incorrect distribution, while OOD TTRL produces heavily skewed distributions (often <10% compilable candidates). This distributional shift gap has not been characterized, motivating our Phase 0 calibration protocol. (4) Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) validates RL for autoformalization (TC1: 17.29% to 26.01% on RLMEval using GRPO with composite BEq + embedding rewards), but operates at training time with labeled/unlabeled data on in-distribution problems, without retrieval, test-time adaptation, or a trained semantic critic. Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.\n\n## Research Landscape\n\nThe landscape spans five relevant lineages. (1) RL for autoformalization: FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards, improving pass@1 from 4% to 26% on ProofNet. Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with composite rewards (BEq + embedding-based similarity) for Lean 4, achieving TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46% on RLMEval—the closest prior work but operates at training time on in-distribution problems, uses embedding similarity rather than a trained semantic critic, and lacks retrieval and test-time adaptation. ReForm (2026) applies position-aware RL rewards for reflective autoformalization (+22.6pp average). (2) Semantic critics and iterative refinement: CriticLean (July 2025) introduces CriticLeanGPT, with the 32B-RL variant achieving 87.0% accuracy and the 14B-RL variant reaching 84.8% on the balanced CriticLeanBench (250 correct, 250 incorrect). The paper reports TPR, FPR, TNR, and FNR metrics but evaluates only on balanced distributions, leaving the heavily skewed OOD regime uncharacterized. ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO with multi-LLM consistency checking. Monotonic Refinement achieves 90.27% composite on miniF2F through multi-model ensemble orchestration. These achieve impressive results but cannot adapt model weights to new domains. (3) Debiased RL and multi-reward optimization: DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification through three components: frequency-based balanced sampling excluding ambiguous samples, fixed +/-1 advantages, and consensus-based off-policy refinement—achieving up to 19.0% relative improvement over ETMR on AIME 2024 (4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B; the TTRL baseline without debiasing scores 15.8, illustrating the severity of signal amplification that DDRL corrects). Critically, DDRL operates exclusively with binary rewards and its authors note that 'more expressive advantage formulations' are left for future work. GDPO (NVIDIA, arXiv 2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization, demonstrating that standard GRPO collapses distinct reward combinations into identical advantage values. (4) Co-adaptive retrieval: R3 (NeurIPS 2025) optimizes retrieval for RAG via reinforced contrastive learning. Reinforced-IR (ACL 2025) alternates RLRF and RLGF for mutual adaptation. TTARAG (arXiv 2601.11443) demonstrates test-time adaptation for RAG. None of these have been applied to autoformalization or Lean 4. (5) Static retrieval, error analysis, and identifier hallucination quantification for autoformalization: The Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) provides the most comprehensive error taxonomy to date: analyzing 3,189 sampled compilation errors from DeepSeek-R1 on applied math (convex analysis, optimization, numerical algebra, high-dimensional probability), they find 47.3% are hallucination of non-existent theorems/definitions, 32.7% are formalization competence errors, 15.2% are incomplete outputs, and 4.8% are formatting/syntax—concluding that 'future improvements should prioritize retrieval-augmented generation or specialized fine-tuning.' DDR builds a 500K-sample dependency dataset and quantifies that ~30% of ICL-generated dependencies are hallucinated identifiers (Hall_m ranging 0.21-0.39 across frontier LLMs), reduced to <2% with retrieval-based DDR. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF but falls short on ProofNet (21.93% vs 27.54%). CRAMF indexes 26K+ Mathlib definitions for concept-level retrieval, documenting that models fabricate identifiers like 'Function.Continuous' instead of 'ContinuousOn' and 'Group.index' instead of 'Subgroup.index'. MathAtlas (May 2026) introduces 52K graduate-level problems where the best model achieves only 2.6% on MA-Hard and adding local context degrades prompted systems' performance. The RAutoformalizer (ICLR 2025 Spotlight) explicitly categorizes compilation errors into 'Hallucination' (identifier hallucination) vs 'Others', establishing that identifier-related errors constitute a major error class. After exhaustive search through May 2026, no work combines (a) co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, (b) a calibrated semantic critic as RL reward with distributional shift analysis, (c) principled adaptation of binary-reward debiased RL to multi-tier rewards, and (d) test-time adaptation on fully unlabeled OOD domains.\n\n## Proposed Approach\n\nWe propose TTRA (Test-Time Retrieval-Augmented autoformalization), a framework that makes TTRL viable for autoformalization through three technical innovations: (1) a dual-loop architecture with co-adaptive retrieval exploiting Lean 4's full structured error taxonomy, (2) integration of CriticLean-14B as semantic RL reward with explicit calibration under distributional shift, and (3) a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards using GDPO's per-reward decoupled normalization.\n\n**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Before committing to the pipeline design, we quantify the retrieval signal coverage that Lean 4's error taxonomy provides on OOD domains. We compile 500 candidate formalizations from an existing model (e.g., FormaRL or Kimina-7B) on Con-NF (OOD) and 500 on MathAtlas MA-Hard, collecting all compilation error messages. We classify each error into the following hierarchy:\n  (a) Tier 1 — Direct identifier signals: `lean.unknownIdentifier` (names the missing constant), `unknown namespace` (names the namespace). These provide direct, machine-parseable mapping from error to needed Mathlib dependency.\n  (b) Tier 2 — Type-based signals: `type mismatch` (contains expected vs actual type signatures), `failed to synthesize instance` (names the typeclass). These provide weaker but still informative retrieval signals—type signatures can be matched against Mathlib's type index, and typeclass names map to specific Mathlib modules.\n  (c) Tier 3 — Indirect signals: tactic failures, elaboration errors, syntax errors. These provide no direct retrieval signal but can serve as negative examples (confirming that retrieved dependencies were insufficient).\n  Quantitative thresholds: If Tier 1 errors constitute ≥40% of compilation failures, the co-adaptive retrieval mechanism is well-supported as designed. If Tier 1 is 20-40%, we rely on both Tier 1 and Tier 2 signals (requiring the type-signature matching extension). If Tier 1 is <20%, we must fall back primarily to Tier 2 signals with type-signature-based retrieval. Prior evidence now strongly supports ≥40%: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291) finds that 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math domains are hallucination of non-existent theorems/definitions—directly exceeding the ≥40% threshold on an OOD domain. DDR shows ~30% of ICL-generated dependencies are hallucinated identifiers (Hall_m=0.21-0.39 across frontier LLMs), the RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' (identifier hallucination) as one of two major error classes, and CRAMF documents systematic fabrication of close-but-wrong identifiers. Phase -1 nonetheless remains essential because AMBER's error distribution is from DeepSeek-R1 on applied math, and our pipeline uses a smaller formalizer on different OOD domains (condensed mathematics, algebraic geometry)—the error distribution may differ. Resource: ~8 A100-hours for generation, ~10 CPU-hours for compilation and error parsing. No model training required.\n\n**Phase 0 — Minimal Pilot Experiment with Critic Calibration (De-risking).** Before committing to the full pipeline, we validate two riskiest assumptions with a minimal experiment. Setup: Take FormaRL's GRPO pipeline, replace its LLM-consistency reward with CriticLean-14B as the sole semantic reward signal (reward = r_compile × r_critic). Data: 200 problems from Con-NF (OOD) + 200 from FormalMATH number theory (near-distribution). No retrieval, no curriculum, no DDRL debiasing—just vanilla GRPO with the critic reward.\n  Primary hypothesis: if CriticLean-14B reward achieves ≥3pp BEq@1 improvement over compilation-only GRPO on Con-NF, the core premise (semantic critic rewards enable OOD adaptation) is validated.\n  Secondary hypothesis — Critic calibration under distributional shift: We explicitly measure CriticLean-14B's precision and recall SEPARATELY on the skewed distribution produced during TTRL. Specifically: (a) Among K=32 candidates per problem, record the number that compile and the number the critic approves. (b) For problems where <10% of candidates compile (the regime expected on hard OOD domains), manually inspect 100 random critic-approved candidates and 100 critic-rejected candidates to compute precision and recall in this hardest regime. (c) Report calibration curves: for each critic confidence bin (if logit-based confidence is available from the critic model), plot the empirical correctness rate. Key concern: on CriticLeanBench's balanced 250/250 distribution, 84.8% accuracy could correspond to very different precision/recall trade-offs. Under OOD TTRL's heavily skewed distribution (90%+ incorrect), even moderate false positive rates could produce substantial noise. Our conservative binarization (requiring BOTH compile AND critic approval) inherently prioritizes precision over recall—a candidate must pass two independent filters. If critic precision on the skewed distribution is <80% (i.e., >20% of critic-approved compilable candidates are semantically wrong), we introduce critic confidence gating: only accept critic judgments with confidence >0.8, trading recall for precision.\n  Resource: ~50 A100-hours (increased from 40 to include calibration analysis), 2-3 weeks. Go/no-go decision: proceed only if primary hypothesis confirmed AND critic precision on the skewed distribution ≥80% (or ≥80% with confidence gating).\n\n**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune a Qwen3-8B base model as a retrieval-augmented autoformalizer using DDR's 500K-sample dependency dataset and GRPO with the multi-tier reward function R(y, x) = r_compile × (α·r_critic + β·r_beq), where: r_compile ∈ {0,1} is the Lean 4 compilation gate (verified via Kimina Lean Server with 128 parallel pre-warmed REPL workers); r_critic ∈ {0,1} is the semantic fidelity judgment from CriticLeanGPT-Qwen3-14B-RL, gated by the confidence threshold established in Phase 0; r_beq ∈ [0,1] is the BEq consensus density (fraction of compilable candidates in the same BEq equivalence class). We set α=0.7, β=0.3 to weight semantic fidelity over syntactic consensus, since BEq has high precision (98.6%) but low recall (~33% on ProofNet). Adaptive reward degradation: when fewer than M=4 candidates out of K=32 compile, BEq becomes degenerate, and the reward falls back to R = r_compile × r_critic.\n\n**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever is a DDR-style dense encoder whose parameters ARE updated during TTRL—not frozen. This exploits a key structural property: Lean 4's type checker produces machine-parseable error messages with a hierarchy of retrieval informativeness.\n\n  Loop 1 — Formalizer GRPO (every step): Generate K=32 candidate formalizations per problem, compile each against Lean 4, compute multi-tier rewards, and perform debiased GRPO updates (Phase 3).\n\n  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Accumulated compilation feedback generates contrastive training data for the retriever using a graded error signal hierarchy:\n    (a) Tier 1 — Direct identifier signals (highest confidence): When a formalization fails with `lean.unknownIdentifier` (tagged with `unknownIdentifierMessageTag`), the error explicitly names the missing Mathlib constant (e.g., 'unknown identifier Finset.sum_comm'). The dependencies that WERE retrieved but did NOT include this constant are hard negatives. The missing constant—looked up in the CRAMF/DDR Mathlib constant index—becomes the positive example. When the error is `unknown namespace`, the namespace maps to a Mathlib module, providing a coarser positive signal.\n    (b) Tier 2 — Type-based signals (moderate confidence): When a formalization fails with `type mismatch`, the error contains expected vs actual type signatures. We match these type signatures against Mathlib's type index (built from DDR's 500K-sample dataset) to identify candidate dependencies that would resolve the mismatch, generating softer positive examples with reduced weight (0.5× in the InfoNCE loss). When `failed to synthesize instance` names a typeclass, we retrieve Mathlib instances of that typeclass as positives.\n    (c) Tier 3 — Negative confirmation from non-identifier errors: Tactic failures, elaboration errors, and syntax errors do not provide positive retrieval signals but confirm that the retrieved dependency set was insufficient for reasons beyond identifier resolution. These contribute only negative examples to the contrastive loss.\n    (d) Positive confirmation from successful compilations: When a formalization compiles successfully, all retrieved Mathlib dependencies that appear in the compiled formalization are confirmed positives.\n    (e) Weighted InfoNCE contrastive loss: L_InfoNCE = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), where w_k = 1.0 for Tier 1 positives, w_k = 0.5 for Tier 2 positives, w_k = 1.0 for compilation-confirmed positives, and τ is the temperature (initialized at 0.07).\n    (f) Decoupled optimization: The retriever's gradient does NOT flow through the formalizer's policy gradient. This alternating optimization prevents instability, following R3 (NeurIPS 2025) and Reinforced-IR (ACL 2025). After each retriever update, the FAISS index over Mathlib dependency embeddings is rebuilt.\n\n  The graded error signal hierarchy ensures the retriever update loop has sufficient signal even on the hardest OOD domains where pure unknownIdentifier errors may be sparse. Phase -1's micro-analysis determines the empirical signal mix, allowing the weighting scheme to be calibrated before full-scale experiments.\n\n**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** DDRL's three-component fix was designed for binary correct/incorrect rewards on informal math. Autoformalization's multi-tier reward has a continuous range. We adapt via binarize-then-enrich:\n\n  (a) Binarization layer (for DDRL compatibility): Define binary acceptance r_accept = I(r_compile=1 AND r_critic=1). Compilation is a non-negotiable binary gate; the critic's precision (characterized in Phase 0 under distributional shift) makes it the most informative signal after compilation.\n    - Balanced sampling: Partition K=32 candidates into 'accepted' (compile + critic approves) and 'rejected' (otherwise). Exclude problems where acceptance frequency is in the ambiguous zone (30-70%, i.e., ~10-22 of 32 accepted), following DDRL's insight that medium-consistency samples are the primary source of reward noise.\n    - Fixed advantages: A_i = +1 for accepted candidates, A_i = -1 for rejected, eliminating GRPO's group-relative normalization that DDRL identifies as the amplification pathway.\n    - Consensus-based off-policy refinement: After each TTRL epoch, sample M=128 formalizations per problem, apply acceptance filtering, perform rejection sampling on high-confidence samples (>80% acceptance rate), and run SFT on this high-quality dataset for 5 epochs.\n  (b) GDPO-style enrichment layer (for BEq signal preservation): Among accepted candidates only, apply per-reward decoupled normalization for the BEq component. The BEq consensus density is normalized independently, preserving its ranking information without collapsing it into the binary acceptance signal. This adds an additive gradient bonus δ·norm(r_beq) to the fixed +1 advantage for accepted candidates, where δ=0.3 scales the enrichment relative to the debiased signal.\n  (c) Methodological contribution: This binarize-then-enrich adaptation from single-reward to multi-tier debiased RL is applicable beyond autoformalization to any multi-tier reward where one component is continuous and others are binary.\n\n**Phase 4 — Progressive Domain Curriculum for Test-Time Adaptation.** To break the bootstrapping problem (poor OOD retrieval → bad formalizations → noisy rewards → failed adaptation), we apply a progressive curriculum with quantitative transition criteria:\n\n  (a) Near-distribution warm-start: TTRL on domains close to training data where retrieval coverage is high. Transition criterion (a)→(b): compilation rate ≥40%, critic approval rate ≥60% among compilable candidates, BEq@32 improves ≥3pp over pre-adaptation baseline. Timeout: T_max=500 GRPO steps.\n  (b) Retrieval bootstrapping: Use the adapted model to generate improved formalization attempts on moderately OOD domains. Failed attempts with structured error signals (Tier 1 and Tier 2) feed the retriever's contrastive updates (Phase 2). Transition criterion (b)→(c): retrieval recall@10 ≥30% on bootstrapped queries, compilation rate on moderate-OOD ≥25%. Early transition: compilation rate plateaus (<2pp improvement over 200 consecutive steps).\n  (c) Far-OOD adaptation: TTRL on truly OOD domains (algebraic geometry, condensed mathematics, MathAtlas MA-Hard) using the bootstrapped retriever and adaptive reward fallback (R = r_compile × r_critic when <4 candidates compile).\n\n**Contribution Floor Analysis.** The three innovations are designed to be synergistic but are independently valuable, ensuring the paper makes a publishable contribution even under partial success:\n  (1) Co-adaptive retrieval alone (Phase 2) + CriticLean TTRL (Phase 0-1): If binarize-then-enrich (Phase 3) provides only marginal gains over vanilla GRPO or plain DDRL, the paper still contributes the first co-adaptive retrieval mechanism for autoformalization exploiting Lean 4's structured error taxonomy, and the first application of TTRL to formal mathematics with a calibrated semantic critic. The co-adaptive retriever is an independent module that can be integrated into any RL-based autoformalization pipeline.\n  (2) Binarize-then-enrich alone (Phase 3): If co-adaptive retrieval provides marginal gains (e.g., because static retrieval is already sufficient for near-OOD domains), the binarize-then-enrich adaptation of DDRL to multi-tier rewards is a standalone methodological contribution applicable to any domain with mixed binary/continuous rewards—not limited to autoformalization.\n  (3) Progressive curriculum alone (Phase 4): If both innovations work but the curriculum provides marginal improvement over direct OOD adaptation, dropping Phase 4 simplifies the pipeline without losing the core contributions.\n  (4) Essential floor: The minimal publishable contribution requires that CriticLean-guided TTRL outperforms compilation-only TTRL on OOD domains (validated in Phase 0) AND at least one of co-adaptive retrieval or binarize-then-enrich provides statistically significant improvement over the CriticLean TTRL baseline. Phase 0's go/no-go gate ensures we do not invest in the full pipeline unless the foundational premise holds.\n\n**Evaluation.** Measure BEq@K and compilation success on FormalMATH's 5,560-problem multi-domain benchmark, Con-NF, CombiBench, and MathAtlas's MA-Hard (700 entities, average dependency depth 30, best current model: 2.6%).\n  Same-scale comparisons (primary, all ~7-8B parameter models): (1) FormaRL (Qwen2.5-Coder-7B) as RL-without-retrieval baseline, (2) Online RL for Autoformalization (Wang et al.) as training-time RL baseline with composite rewards, (3) DRIFT with Qwen3-8B as strongest static retrieval baseline, (4) compilation-only TTRL and critic-only TTRL ablations, (5) standard GRPO vs. DDRL debiased vs. binarize-then-enrich (with separate ablations for each DDRL component and the GDPO enrichment layer), (6) frozen retriever vs. co-adaptive retriever during TTRL (isolating the value of compilation-error-driven retriever updates from natural query improvement), (7) Tier 1-only vs. Tier 1+2 vs. all-tier error signals (isolating the value of the graded error hierarchy), (8) no curriculum vs. progressive curriculum.\n  Cross-scale reference points (for contextualizing absolute performance, NOT for claiming superiority): (9) ATF-32B as iterative refinement SOTA (94.51%/65.38% FormalMath-Lite/CombiBench), (10) ATLAS as SFT-only reference (70.08% pass@1 miniF2F), (11) Monotonic Refinement as inference-time orchestration upper bound (90.27% miniF2F, multi-model ensemble with GPT-4+ level models). All evaluation tables explicitly annotate model scale and compute budget to ensure fair interpretation.\n  Sensitivity analysis: Dedicated ablation for N_ret ∈ {25, 50, 100} (retriever update frequency), as this controls the retriever-formalizer alternation and is critical for stability.\n\n## Detailed Description\n\nCurrent autoformalization models achieve strong in-distribution results but collapse on unfamiliar mathematical domains due to missing domain-specific Mathlib dependencies and fixed inference-time behavior. We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a framework making TTRL viable for autoformalization through three technical innovations. First, a dual-loop co-adaptive retrieval architecture where a DDR-style dense retriever is explicitly fine-tuned during test-time RL using a graded hierarchy of Lean 4 compilation error signals: Tier 1 signals from `lean.unknownIdentifier` errors (which explicitly name the missing Mathlib constant, providing direct hard negatives for InfoNCE training), Tier 2 signals from type mismatches and failed typeclass synthesis (providing softer retrieval signals via type-signature matching), and Tier 3 negative confirmation from other errors. This graded hierarchy addresses the key concern that not all OOD errors produce clean identifier signals—the prevalence of identifier errors is now established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are hallucination of non-existent theorems/definitions, DDR shows ~30% of ICL-generated dependencies are hallucinated identifiers, and the RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as one of two primary error classes. A Phase -1 micro-analysis (2-3 days, ~8 A100-hours) validates the error distribution on our specific OOD benchmarks before committing to the pipeline. Second, integration of CriticLean-14B (84.8% accuracy on balanced CriticLeanBench) as semantic RL reward, with explicit calibration under distributional shift: Phase 0 measures the critic's precision and recall SEPARATELY on the heavily skewed distribution expected during OOD TTRL (where >90% of candidates may be incorrect), reports calibration curves, and establishes a confidence gating threshold to maintain precision ≥80%—the conservative binarization (requiring BOTH compile AND critic approval) inherently prioritizes precision over recall. Third, a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards: binary acceptance (compile AND critic approval) provides DDRL's frequency-based balanced sampling and fixed ±1 advantages for debiasing, while GDPO-style per-reward decoupled normalization preserves BEq consensus density as a secondary ranking bonus among accepted candidates—this adaptation is itself a methodological contribution applicable beyond autoformalization. A progressive domain curriculum with quantitative transition criteria breaks the bootstrapping problem on OOD domains. Crucially, the three innovations are independently valuable: if binarize-then-enrich provides marginal gains, the paper still contributes the first co-adaptive retrieval for autoformalization and the first TTRL application to formal math with a calibrated semantic critic; if co-adaptive retrieval is marginal, binarize-then-enrich stands as a general methodology for multi-tier debiased RL. This contribution floor ensures publishable results even under partial success, with Phase 0's go/no-go gate preventing wasted effort on the foundational premise. Evaluation spans FormalMATH, Con-NF, CombiBench, and MathAtlas MA-Hard (best current: 2.6%), with same-scale comparisons (FormaRL, Online RL, DRIFT, ablations on error tiers and N_ret sensitivity) explicitly separated from cross-scale reference points (ATF-32B, Monotonic Refinement) to ensure fair interpretation. N_ret=50 GRPO steps between retriever updates is justified by signal accumulation: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle, sufficient for stable InfoNCE learning.\n\n## Key References\n\n- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)\n- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)\n- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv 2601.05242, NVIDIA, January 2026)\n- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv 2507.06181, ByteDance/Nanjing)\n- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)\n- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv 2510.24652)\n- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)\n- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv 2601.11443, January 2026)\n- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv 2602.01291, February 2026)\n- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)\n- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\n- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)\n- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)\n- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\n- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)\n- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv 2025)\n- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)\n- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)\n- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)\n- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\n- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\n- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2605.14061, May 2026)\n- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\n- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\n- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\n- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025)\n- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv 2512.00997, Microsoft Research)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 950-1400 A100-80GB hours (Phase -1 error micro-analysis: ~8h; Phase 0 pilot with critic calibration: ~50h; base formalizer GRPO training with multi-tier reward: ~300h on 8 GPUs; DDR retriever fine-tuning + co-adaptive contrastive updates: ~100h on 4 GPUs; TTRL progressive adaptation across 3 curriculum stages with binarize-then-enrich DDRL and ablations: ~400h on 4 GPUs; CriticLean-14B inference during training: ~60h on 2 GPUs; N_ret sensitivity analysis: ~50h; error tier ablation: ~40h; evaluation: ~80h) + 10,000-15,000 CPU-hours for Lean 4 verification (128 parallel workers via Kimina Lean Server), timeline: 12-16 weeks (0.5 wk Phase -1 micro-analysis, 2-3 wk Phase 0 pilot + critic calibration + go/no-go, 3 wk base training + critic integration, 2 wk retriever co-adaptation infrastructure, 4 wk progressive TTRL experiments, 2-3 wk ablations including N_ret sensitivity and error tier analysis, 2 wk writing), estimated_gpu_cost: $1,900-$3,500 at ~$2.00/A100-hr + ~$500-$750 CPU verification costs\n- **human_in_loop**: gpu_hours: 750-1100 A100-80GB hours (Claude handles Phase -1 analysis, Phase 0 calibration analysis, experiment scheduling; reduced ablation overhead ~25%) + 8,000-12,000 CPU-hours for Lean verification, timeline: 9-12 weeks (0.5 wk Phase -1; 2 wk Phase 0 with Claude-assisted calibration analysis; 3 wk base training + co-adaptive retriever; 3 wk progressive TTRL; 2-3 wk ablations + writing), claude_api_cost: $400-$700 (critic reward calibration, Phase -1/0 analysis, automated curriculum scheduling, ablation analysis), estimated_gpu_cost: $1,500-$2,700 + ~$400-$600 CPU costs\n- **auto_research**: gpu_hours: 1600-2200 A100-80GB hours (automated hyperparameter sweeps over N_ret ∈ {25,50,100}, InfoNCE temperature τ, Tier 1/2 weighting, DDRL binarization ambiguity zone, GRPO group sizes K ∈ {16,32,64}, curriculum transition thresholds, enrichment weight δ, critic confidence threshold, plus multi-seed evaluation) + 20,000-30,000 CPU-hours for Lean verification at scale, timeline: 6-9 weeks (highly parallelized; Phase -1 in day 1-2 with automatic error taxonomy analysis; Phase 0 pilot in week 1-2 with automatic go/no-go gate and calibration analysis; wall-clock bottleneck is Lean 4 verification, mitigated by 128+ Kimina Lean Server workers), claude_api_cost: $800-$1,200 (automated experiment design, Phase -1/0 analysis, reward function ablation, curriculum optimization, paper drafting), estimated_gpu_cost: $3,200-$5,500 + ~$1,000-$1,500 CPU costs, speed_bottleneck: Lean 4 compilation latency (~3.65s per statement with warm LRU cache; ~0.10s amortized at 64 workers) dominates reward computation. CriticLean-14B inference adds ~0.5s per candidate on A100. Retriever co-adaptation adds ~15 min per update cycle (every N_ret GRPO steps) for re-encoding 26K Mathlib constants and rebuilding FAISS index.\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:15:23.444Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:15:23.444Z",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-28T05:15:23.466Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization

## Core Problem

Current autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning dramatically but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in the multi-tier reward setting (compilation + critic + BEq); and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation, yet no prior work fine-tunes the retriever during test-time RL. Can we make TTRL viable for autoformalization by combining compilation-error-driven co-adaptive retrieval that exploits Lean 4's full structured error taxonomy, a calibrated semantic critic reward, and principled adaptation of binary-reward debiased RL to multi-tier rewards?

## Research Opportunity

Four independently validated capabilities have never been combined: (1) Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode. R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv 2601.11443, Jan 2026) shows test-time retrieval adaptation is achievable via self-supervised prediction. Critically, the prevalence of identifier hallucination as the dominant error class is now established by converging evidence from multiple independent studies: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) provides the strongest quantitative evidence, finding that 47.3% of 3,189 sampled compilation errors from DeepSeek-R1 on applied mathematics domains stem from 'invocation of non-existent theorems or definitions'—directly exceeding Phase -1's ≥40% Tier 1 threshold. DDR (arXiv 2511.11990) quantifies that ICL-based dependency generation produces ~30% hallucinated (non-existent) Mathlib identifiers (Hall_m=0.21-0.39 across frontier LLMs), while retrieval-based DDR reduces hallucination to <2% (Hall_m=0.016). The RAutoformalizer (ICLR 2025 Spotlight) explicitly classifies compilation errors into 'Hallucination' (errors caused by hallucination of identifiers) and 'Others', establishing identifier hallucination as a primary error class. MathAtlas (May 2026) further shows a 66% performance advantage for Mathlib-grounded definitions (27.9% vs 16.8% correct, p<0.001), confirming that dependency availability is the critical bottleneck. Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL-based autoformalization—where Lean's structured error taxonomy (unknownIdentifier, type mismatch with type signatures, failed to synthesize with typeclass names, unknown namespace) provides a graded hierarchy of machine-parseable signals for retriever training. (2) TTRL with debiasing has advanced rapidly. DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed +/-1 advantages, and consensus-based off-policy refinement, achieving up to 19.0% relative improvement over ETMR on AIME 2024 (4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B). But DDRL assumes binary correct/incorrect rewards. GDPO (NVIDIA, arXiv 2601.05242, Jan 2026) addresses multi-reward GRPO through per-reward decoupled normalization, preventing reward signal collapse. The combination—binarize multi-tier rewards for DDRL's debiasing, then enrich with GDPO's per-reward normalization for continuous components—has not been attempted. (3) CriticLean (July 2025) provides the missing reward signal: CriticLeanGPT-14B-RL achieves 84.8% accuracy on CriticLeanBench (87.0% for the 32B variant), raising autoformalization pipeline accuracy from 54% to 84% over compilation-only feedback. However, CriticLeanBench evaluates on a balanced 250-correct/250-incorrect distribution, while OOD TTRL produces heavily skewed distributions (often <10% compilable candidates). This distributional shift gap has not been characterized, motivating our Phase 0 calibration protocol. (4) Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) validates RL for autoformalization (TC1: 17.29% to 26.01% on RLMEval using GRPO with composite BEq + embedding rewards), but operates at training time with labeled/unlabeled data on in-distribution problems, without retrieval, test-time adaptation, or a trained semantic critic. Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.

## Research Landscape

The landscape spans five relevant lineages. (1) RL for autoformalization: FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards, improving pass@1 from 4% to 26% on ProofNet. Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with composite rewards (BEq + embedding-based similarity) for Lean 4, achieving TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46% on RLMEval—the closest prior work but operates at training time on in-distribution problems, uses embedding similarity rather than a trained semantic critic, and lacks retrieval and test-time adaptation. ReForm (2026) applies position-aware RL rewards for reflective autoformalization (+22.6pp average). (2) Semantic critics and iterative refinement: CriticLean (July 2025) introduces CriticLeanGPT, with the 32B-RL variant achieving 87.0% accuracy and the 14B-RL variant reaching 84.8% on the balanced CriticLeanBench (250 correct, 250 incorrect). The paper reports TPR, FPR, TNR, and FNR metrics but evaluates only on balanced distributions, leaving the heavily skewed OOD regime uncharacterized. ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO with multi-LLM consistency checking. Monotonic Refinement achieves 90.27% composite on miniF2F through multi-model ensemble orchestration. These achieve impressive results but cannot adapt model weights to new domains. (3) Debiased RL and multi-reward optimization: DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification through three components: frequency-based balanced sampling excluding ambiguous samples, fixed +/-1 advantages, and consensus-based off-policy refinement—achieving up to 19.0% relative improvement over ETMR on AIME 2024 (4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B; the TTRL baseline without debiasing scores 15.8, illustrating the severity of signal amplification that DDRL corrects). Critically, DDRL operates exclusively with binary rewards and its authors note that 'more expressive advantage formulations' are left for future work. GDPO (NVIDIA, arXiv 2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization, demonstrating that standard GRPO collapses distinct reward combinations into identical advantage values. (4) Co-adaptive retrieval: R3 (NeurIPS 2025) optimizes retrieval for RAG via reinforced contrastive learning. Reinforced-IR (ACL 2025) alternates RLRF and RLGF for mutual adaptation. TTARAG (arXiv 2601.11443) demonstrates test-time adaptation for RAG. None of these have been applied to autoformalization or Lean 4. (5) Static retrieval, error analysis, and identifier hallucination quantification for autoformalization: The Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) provides the most comprehensive error taxonomy to date: analyzing 3,189 sampled compilation errors from DeepSeek-R1 on applied math (convex analysis, optimization, numerical algebra, high-dimensional probability), they find 47.3% are hallucination of non-existent theorems/definitions, 32.7% are formalization competence errors, 15.2% are incomplete outputs, and 4.8% are formatting/syntax—concluding that 'future improvements should prioritize retrieval-augmented generation or specialized fine-tuning.' DDR builds a 500K-sample dependency dataset and quantifies that ~30% of ICL-generated dependencies are hallucinated identifiers (Hall_m ranging 0.21-0.39 across frontier LLMs), reduced to <2% with retrieval-based DDR. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF but falls short on ProofNet (21.93% vs 27.54%). CRAMF indexes 26K+ Mathlib definitions for concept-level retrieval, documenting that models fabricate identifiers like 'Function.Continuous' instead of 'ContinuousOn' and 'Group.index' instead of 'Subgroup.index'. MathAtlas (May 2026) introduces 52K graduate-level problems where the best model achieves only 2.6% on MA-Hard and adding local context degrades prompted systems' performance. The RAutoformalizer (ICLR 2025 Spotlight) explicitly categorizes compilation errors into 'Hallucination' (identifier hallucination) vs 'Others', establishing that identifier-related errors constitute a major error class. After exhaustive search through May 2026, no work combines (a) co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, (b) a calibrated semantic critic as RL reward with distributional shift analysis, (c) principled adaptation of binary-reward debiased RL to multi-tier rewards, and (d) test-time adaptation on fully unlabeled OOD domains.

## Proposed Approach

We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a framework that makes TTRL viable for autoformalization through three technical innovations: (1) a dual-loop architecture with co-adaptive retrieval exploiting Lean 4's full structured error taxonomy, (2) integration of CriticLean-14B as semantic RL reward with explicit calibration under distributional shift, and (3) a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards using GDPO's per-reward decoupled normalization.

**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Before committing to the pipeline design, we quantify the retrieval signal coverage that Lean 4's error taxonomy provides on OOD domains. We compile 500 candidate formalizations from an existing model (e.g., FormaRL or Kimina-7B) on Con-NF (OOD) and 500 on MathAtlas MA-Hard, collecting all compilation error messages. We classify each error into the following hierarchy:
  (a) Tier 1 — Direct identifier signals: `lean.unknownIdentifier` (names the missing constant), `unknown namespace` (names the namespace). These provide direct, machine-parseable mapping from error to needed Mathlib dependency.
  (b) Tier 2 — Type-based signals: `type mismatch` (contains expected vs actual type signatures), `failed to synthesize instance` (names the typeclass). These provide weaker but still informative retrieval signals—type signatures can be matched against Mathlib's type index, and typeclass names map to specific Mathlib modules.
  (c) Tier 3 — Indirect signals: tactic failures, elaboration errors, syntax errors. These provide no direct retrieval signal but can serve as negative examples (confirming that retrieved dependencies were insufficient).
  Quantitative thresholds: If Tier 1 errors constitute ≥40% of compilation failures, the co-adaptive retrieval mechanism is well-supported as designed. If Tier 1 is 20-40%, we rely on both Tier 1 and Tier 2 signals (requiring the type-signature matching extension). If Tier 1 is <20%, we must fall back primarily to Tier 2 signals with type-signature-based retrieval. Prior evidence now strongly supports ≥40%: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291) finds that 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math domains are hallucination of non-existent theorems/definitions—directly exceeding the ≥40% threshold on an OOD domain. DDR shows ~30% of ICL-generated dependencies are hallucinated identifiers (Hall_m=0.21-0.39 across frontier LLMs), the RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' (identifier hallucination) as one of two major error classes, and CRAMF documents systematic fabrication of close-but-wrong identifiers. Phase -1 nonetheless remains essential because AMBER's error distribution is from DeepSeek-R1 on applied math, and our pipeline uses a smaller formalizer on different OOD domains (condensed mathematics, algebraic geometry)—the error distribution may differ. Resource: ~8 A100-hours for generation, ~10 CPU-hours for compilation and error parsing. No model training required.

**Phase 0 — Minimal Pilot Experiment with Critic Calibration (De-risking).** Before committing to the full pipeline, we validate two riskiest assumptions with a minimal experiment. Setup: Take FormaRL's GRPO pipeline, replace its LLM-consistency reward with CriticLean-14B as the sole semantic reward signal (reward = r_compile × r_critic). Data: 200 problems from Con-NF (OOD) + 200 from FormalMATH number theory (near-distribution). No retrieval, no curriculum, no DDRL debiasing—just vanilla GRPO with the critic reward.
  Primary hypothesis: if CriticLean-14B reward achieves ≥3pp BEq@1 improvement over compilation-only GRPO on Con-NF, the core premise (semantic critic rewards enable OOD adaptation) is validated.
  Secondary hypothesis — Critic calibration under distributional shift: We explicitly measure CriticLean-14B's precision and recall SEPARATELY on the skewed distribution produced during TTRL. Specifically: (a) Among K=32 candidates per problem, record the number that compile and the number the critic approves. (b) For problems where <10% of candidates compile (the regime expected on hard OOD domains), manually inspect 100 random critic-approved candidates and 100 critic-rejected candidates to compute precision and recall in this hardest regime. (c) Report calibration curves: for each critic confidence bin (if logit-based confidence is available from the critic model), plot the empirical correctness rate. Key concern: on CriticLeanBench's balanced 250/250 distribution, 84.8% accuracy could correspond to very different precision/recall trade-offs. Under OOD TTRL's heavily skewed distribution (90%+ incorrect), even moderate false positive rates could produce substantial noise. Our conservative binarization (requiring BOTH compile AND critic approval) inherently prioritizes precision over recall—a candidate must pass two independent filters. If critic precision on the skewed distribution is <80% (i.e., >20% of critic-approved compilable candidates are semantically wrong), we introduce critic confidence gating: only accept critic judgments with confidence >0.8, trading recall for precision.
  Resource: ~50 A100-hours (increased from 40 to include calibration analysis), 2-3 weeks. Go/no-go decision: proceed only if primary hypothesis confirmed AND critic precision on the skewed distribution ≥80% (or ≥80% with confidence gating).

**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune a Qwen3-8B base model as a retrieval-augmented autoformalizer using DDR's 500K-sample dependency dataset and GRPO with the multi-tier reward function R(y, x) = r_compile × (α·r_critic + β·r_beq), where: r_compile ∈ {0,1} is the Lean 4 compilation gate (verified via Kimina Lean Server with 128 parallel pre-warmed REPL workers); r_critic ∈ {0,1} is the semantic fidelity judgment from CriticLeanGPT-Qwen3-14B-RL, gated by the confidence threshold established in Phase 0; r_beq ∈ [0,1] is the BEq consensus density (fraction of compilable candidates in the same BEq equivalence class). We set α=0.7, β=0.3 to weight semantic fidelity over syntactic consensus, since BEq has high precision (98.6%) but low recall (~33% on ProofNet). Adaptive reward degradation: when fewer than M=4 candidates out of K=32 compile, BEq becomes degenerate, and the reward falls back to R = r_compile × r_critic.

**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever is a DDR-style dense encoder whose parameters ARE updated during TTRL—not frozen. This exploits a key structural property: Lean 4's type checker produces machine-parseable error messages with a hierarchy of retrieval informativeness.

  Loop 1 — Formalizer GRPO (every step): Generate K=32 candidate formalizations per problem, compile each against Lean 4, compute multi-tier rewards, and perform debiased GRPO updates (Phase 3).

  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Accumulated compilation feedback generates contrastive training data for the retriever using a graded error signal hierarchy:
    (a) Tier 1 — Direct identifier signals (highest confidence): When a formalization fails with `lean.unknownIdentifier` (tagged with `unknownIdentifierMessageTag`), the error explicitly names the missing Mathlib constant (e.g., 'unknown identifier Finset.sum_comm'). The dependencies that WERE retrieved but did NOT include this constant are hard negatives. The missing constant—looked up in the CRAMF/DDR Mathlib constant index—becomes the positive example. When the error is `unknown namespace`, the namespace maps to a Mathlib module, providing a coarser positive signal.
    (b) Tier 2 — Type-based signals (moderate confidence): When a formalization fails with `type mismatch`, the error contains expected vs actual type signatures. We match these type signatures against Mathlib's type index (built from DDR's 500K-sample dataset) to identify candidate dependencies that would resolve the mismatch, generating softer positive examples with reduced weight (0.5× in the InfoNCE loss). When `failed to synthesize instance` names a typeclass, we retrieve Mathlib instances of that typeclass as positives.
    (c) Tier 3 — Negative confirmation from non-identifier errors: Tactic failures, elaboration errors, and syntax errors do not provide positive retrieval signals but confirm that the retrieved dependency set was insufficient for reasons beyond identifier resolution. These contribute only negative examples to the contrastive loss.
    (d) Positive confirmation from successful compilations: When a formalization compiles successfully, all retrieved Mathlib dependencies that appear in the compiled formalization are confirmed positives.
    (e) Weighted InfoNCE contrastive loss: L_InfoNCE = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), where w_k = 1.0 for Tier 1 positives, w_k = 0.5 for Tier 2 positives, w_k = 1.0 for compilation-confirmed positives, and τ is the temperature (initialized at 0.07).
    (f) Decoupled optimization: The retriever's gradient does NOT flow through the formalizer's policy gradient. This alternating optimization prevents instability, following R3 (NeurIPS 2025) and Reinforced-IR (ACL 2025). After each retriever update, the FAISS index over Mathlib dependency embeddings is rebuilt.

  The graded error signal hierarchy ensures the retriever update loop has sufficient signal even on the hardest OOD domains where pure unknownIdentifier errors may be sparse. Phase -1's micro-analysis determines the empirical signal mix, allowing the weighting scheme to be calibrated before full-scale experiments.

**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** DDRL's three-component fix was designed for binary correct/incorrect rewards on informal math. Autoformalization's multi-tier reward has a continuous range. We adapt via binarize-then-enrich:

  (a) Binarization layer (for DDRL compatibility): Define binary acceptance r_accept = I(r_compile=1 AND r_critic=1). Compilation is a non-negotiable binary gate; the critic's precision (characterized in Phase 0 under distributional shift) makes it the most informative signal after compilation.
    - Balanced sampling: Partition K=32 candidates into 'accepted' (compile + critic approves) and 'rejected' (otherwise). Exclude problems where acceptance frequency is in the ambiguous zone (30-70%, i.e., ~10-22 of 32 accepted), following DDRL's insight that medium-consistency samples are the primary source of reward noise.
    - Fixed advantages: A_i = +1 for accepted candidates, A_i = -1 for rejected, eliminating GRPO's group-relative normalization that DDRL identifies as the amplification pathway.
    - Consensus-based off-policy refinement: After each TTRL epoch, sample M=128 formalizations per problem, apply acceptance filtering, perform rejection sampling on high-confidence samples (>80% acceptance rate), and run SFT on this high-quality dataset for 5 epochs.
  (b) GDPO-style enrichment layer (for BEq signal preservation): Among accepted candidates only, apply per-reward decoupled normalization for the BEq component. The BEq consensus density is normalized independently, preserving its ranking information without collapsing it into the binary acceptance signal. This adds an additive gradient bonus δ·norm(r_beq) to the fixed +1 advantage for accepted candidates, where δ=0.3 scales the enrichment relative to the debiased signal.
  (c) Methodological contribution: This binarize-then-enrich adaptation from single-reward to multi-tier debiased RL is applicable beyond autoformalization to any multi-tier reward where one component is continuous and others are binary.

**Phase 4 — Progressive Domain Curriculum for Test-Time Adaptation.** To break the bootstrapping problem (poor OOD retrieval → bad formalizations → noisy rewards → failed adaptation), we apply a progressive curriculum with quantitative transition criteria:

  (a) Near-distribution warm-start: TTRL on domains close to training data where retrieval coverage is high. Transition criterion (a)→(b): compilation rate ≥40%, critic approval rate ≥60% among compilable candidates, BEq@32 improves ≥3pp over pre-adaptation baseline. Timeout: T_max=500 GRPO steps.
  (b) Retrieval bootstrapping: Use the adapted model to generate improved formalization attempts on moderately OOD domains. Failed attempts with structured error signals (Tier 1 and Tier 2) feed the retriever's contrastive updates (Phase 2). Transition criterion (b)→(c): retrieval recall@10 ≥30% on bootstrapped queries, compilation rate on moderate-OOD ≥25%. Early transition: compilation rate plateaus (<2pp improvement over 200 consecutive steps).
  (c) Far-OOD adaptation: TTRL on truly OOD domains (algebraic geometry, condensed mathematics, MathAtlas MA-Hard) using the bootstrapped retriever and adaptive reward fallback (R = r_compile × r_critic when <4 candidates compile).

**Contribution Floor Analysis.** The three innovations are designed to be synergistic but are independently valuable, ensuring the paper makes a publishable contribution even under partial success:
  (1) Co-adaptive retrieval alone (Phase 2) + CriticLean TTRL (Phase 0-1): If binarize-then-enrich (Phase 3) provides only marginal gains over vanilla GRPO or plain DDRL, the paper still contributes the first co-adaptive retrieval mechanism for autoformalization exploiting Lean 4's structured error taxonomy, and the first application of TTRL to formal mathematics with a calibrated semantic critic. The co-adaptive retriever is an independent module that can be integrated into any RL-based autoformalization pipeline.
  (2) Binarize-then-enrich alone (Phase 3): If co-adaptive retrieval provides marginal gains (e.g., because static retrieval is already sufficient for near-OOD domains), the binarize-then-enrich adaptation of DDRL to multi-tier rewards is a standalone methodological contribution applicable to any domain with mixed binary/continuous rewards—not limited to autoformalization.
  (3) Progressive curriculum alone (Phase 4): If both innovations work but the curriculum provides marginal improvement over direct OOD adaptation, dropping Phase 4 simplifies the pipeline without losing the core contributions.
  (4) Essential floor: The minimal publishable contribution requires that CriticLean-guided TTRL outperforms compilation-only TTRL on OOD domains (validated in Phase 0) AND at least one of co-adaptive retrieval or binarize-then-enrich provides statistically significant improvement over the CriticLean TTRL baseline. Phase 0's go/no-go gate ensures we do not invest in the full pipeline unless the foundational premise holds.

**Evaluation.** Measure BEq@K and compilation success on FormalMATH's 5,560-problem multi-domain benchmark, Con-NF, CombiBench, and MathAtlas's MA-Hard (700 entities, average dependency depth 30, best current model: 2.6%).
  Same-scale comparisons (primary, all ~7-8B parameter models): (1) FormaRL (Qwen2.5-Coder-7B) as RL-without-retrieval baseline, (2) Online RL for Autoformalization (Wang et al.) as training-time RL baseline with composite rewards, (3) DRIFT with Qwen3-8B as strongest static retrieval baseline, (4) compilation-only TTRL and critic-only TTRL ablations, (5) standard GRPO vs. DDRL debiased vs. binarize-then-enrich (with separate ablations for each DDRL component and the GDPO enrichment layer), (6) frozen retriever vs. co-adaptive retriever during TTRL (isolating the value of compilation-error-driven retriever updates from natural query improvement), (7) Tier 1-only vs. Tier 1+2 vs. all-tier error signals (isolating the value of the graded error hierarchy), (8) no curriculum vs. progressive curriculum.
  Cross-scale reference points (for contextualizing absolute performance, NOT for claiming superiority): (9) ATF-32B as iterative refinement SOTA (94.51%/65.38% FormalMath-Lite/CombiBench), (10) ATLAS as SFT-only reference (70.08% pass@1 miniF2F), (11) Monotonic Refinement as inference-time orchestration upper bound (90.27% miniF2F, multi-model ensemble with GPT-4+ level models). All evaluation tables explicitly annotate model scale and compute budget to ensure fair interpretation.
  Sensitivity analysis: Dedicated ablation for N_ret ∈ {25, 50, 100} (retriever update frequency), as this controls the retriever-formalizer alternation and is critical for stability.

## Detailed Description

Current autoformalization models achieve strong in-distribution results but collapse on unfamiliar mathematical domains due to missing domain-specific Mathlib dependencies and fixed inference-time behavior. We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a framework making TTRL viable for autoformalization through three technical innovations. First, a dual-loop co-adaptive retrieval architecture where a DDR-style dense retriever is explicitly fine-tuned during test-time RL using a graded hierarchy of Lean 4 compilation error signals: Tier 1 signals from `lean.unknownIdentifier` errors (which explicitly name the missing Mathlib constant, providing direct hard negatives for InfoNCE training), Tier 2 signals from type mismatches and failed typeclass synthesis (providing softer retrieval signals via type-signature matching), and Tier 3 negative confirmation from other errors. This graded hierarchy addresses the key concern that not all OOD errors produce clean identifier signals—the prevalence of identifier errors is now established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are hallucination of non-existent theorems/definitions, DDR shows ~30% of ICL-generated dependencies are hallucinated identifiers, and the RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as one of two primary error classes. A Phase -1 micro-analysis (2-3 days, ~8 A100-hours) validates the error distribution on our specific OOD benchmarks before committing to the pipeline. Second, integration of CriticLean-14B (84.8% accuracy on balanced CriticLeanBench) as semantic RL reward, with explicit calibration under distributional shift: Phase 0 measures the critic's precision and recall SEPARATELY on the heavily skewed distribution expected during OOD TTRL (where >90% of candidates may be incorrect), reports calibration curves, and establishes a confidence gating threshold to maintain precision ≥80%—the conservative binarization (requiring BOTH compile AND critic approval) inherently prioritizes precision over recall. Third, a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards: binary acceptance (compile AND critic approval) provides DDRL's frequency-based balanced sampling and fixed ±1 advantages for debiasing, while GDPO-style per-reward decoupled normalization preserves BEq consensus density as a secondary ranking bonus among accepted candidates—this adaptation is itself a methodological contribution applicable beyond autoformalization. A progressive domain curriculum with quantitative transition criteria breaks the bootstrapping problem on OOD domains. Crucially, the three innovations are independently valuable: if binarize-then-enrich provides marginal gains, the paper still contributes the first co-adaptive retrieval for autoformalization and the first TTRL application to formal math with a calibrated semantic critic; if co-adaptive retrieval is marginal, binarize-then-enrich stands as a general methodology for multi-tier debiased RL. This contribution floor ensures publishable results even under partial success, with Phase 0's go/no-go gate preventing wasted effort on the foundational premise. Evaluation spans FormalMATH, Con-NF, CombiBench, and MathAtlas MA-Hard (best current: 2.6%), with same-scale comparisons (FormaRL, Online RL, DRIFT, ablations on error tiers and N_ret sensitivity) explicitly separated from cross-scale reference points (ATF-32B, Monotonic Refinement) to ensure fair interpretation. N_ret=50 GRPO steps between retriever updates is justified by signal accumulation: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle, sufficient for stable InfoNCE learning.

## Key References

- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)
- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)
- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv 2601.05242, NVIDIA, January 2026)
- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv 2507.06181, ByteDance/Nanjing)
- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)
- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv 2510.24652)
- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)
- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv 2601.11443, January 2026)
- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv 2602.01291, February 2026)
- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)
- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)
- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)
- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)
- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)
- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)
- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv 2025)
- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)
- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)
- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)
- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)
- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)
- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2605.14061, May 2026)
- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)
- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)
- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)
- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025)
- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv 2512.00997, Microsoft Research)

## Resource Estimate

- **manual**: gpu_hours: 950-1400 A100-80GB hours (Phase -1 error micro-analysis: ~8h; Phase 0 pilot with critic calibration: ~50h; base formalizer GRPO training with multi-tier reward: ~300h on 8 GPUs; DDR retriever fine-tuning + co-adaptive contrastive updates: ~100h on 4 GPUs; TTRL progressive adaptation across 3 curriculum stages with binarize-then-enrich DDRL and ablations: ~400h on 4 GPUs; CriticLean-14B inference during training: ~60h on 2 GPUs; N_ret sensitivity analysis: ~50h; error tier ablation: ~40h; evaluation: ~80h) + 10,000-15,000 CPU-hours for Lean 4 verification (128 parallel workers via Kimina Lean Server), timeline: 12-16 weeks (0.5 wk Phase -1 micro-analysis, 2-3 wk Phase 0 pilot + critic calibration + go/no-go, 3 wk base training + critic integration, 2 wk retriever co-adaptation infrastructure, 4 wk progressive TTRL experiments, 2-3 wk ablations including N_ret sensitivity and error tier analysis, 2 wk writing), estimated_gpu_cost: $1,900-$3,500 at ~$2.00/A100-hr + ~$500-$750 CPU verification costs
- **human_in_loop**: gpu_hours: 750-1100 A100-80GB hours (Claude handles Phase -1 analysis, Phase 0 calibration analysis, experiment scheduling; reduced ablation overhead ~25%) + 8,000-12,000 CPU-hours for Lean verification, timeline: 9-12 weeks (0.5 wk Phase -1; 2 wk Phase 0 with Claude-assisted calibration analysis; 3 wk base training + co-adaptive retriever; 3 wk progressive TTRL; 2-3 wk ablations + writing), claude_api_cost: $400-$700 (critic reward calibration, Phase -1/0 analysis, automated curriculum scheduling, ablation analysis), estimated_gpu_cost: $1,500-$2,700 + ~$400-$600 CPU costs
- **auto_research**: gpu_hours: 1600-2200 A100-80GB hours (automated hyperparameter sweeps over N_ret ∈ {25,50,100}, InfoNCE temperature τ, Tier 1/2 weighting, DDRL binarization ambiguity zone, GRPO group sizes K ∈ {16,32,64}, curriculum transition thresholds, enrichment weight δ, critic confidence threshold, plus multi-seed evaluation) + 20,000-30,000 CPU-hours for Lean verification at scale, timeline: 6-9 weeks (highly parallelized; Phase -1 in day 1-2 with automatic error taxonomy analysis; Phase 0 pilot in week 1-2 with automatic go/no-go gate and calibration analysis; wall-clock bottleneck is Lean 4 verification, mitigated by 128+ Kimina Lean Server workers), claude_api_cost: $800-$1,200 (automated experiment design, Phase -1/0 analysis, reward function ablation, curriculum optimization, paper drafting), estimated_gpu_cost: $3,200-$5,500 + ~$1,000-$1,500 CPU costs, speed_bottleneck: Lean 4 compilation latency (~3.65s per statement with warm LRU cache; ~0.10s amortized at 64 workers) dominates reward computation. CriticLean-14B inference adds ~0.5s per candidate on A100. Retriever co-adaptation adds ~15 min per update cycle (every N_ret GRPO steps) for re-encoding 26K Mathlib constants and rebuilding FAISS index.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "6ef15cba-e143-43a8-bcb2-6ca9362221ec",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:15:23.464Z_

```json
{
  "parentUuid": "6ef15cba-e143-43a8-bcb2-6ca9362221ec",
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
  "uuid": "df6c5b9e-1f5f-421e-93b8-0a1ebe018cae",
  "timestamp": "2026-05-28T05:15:23.464Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:15:23.464Z_

```json
{
  "parentUuid": "df6c5b9e-1f5f-421e-93b8-0a1ebe018cae",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3b544881-3b2c-4712-8c94-c01cf0934f66",
  "timestamp": "2026-05-28T05:15:23.464Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "3b544881-3b2c-4712-8c94-c01cf0934f66",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Critic-guided test-time retrieval-augmented autoformalization",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Assistant

_source line 8 · 2026-05-28T05:15:30.734Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed proposal for TTRA (Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization). I need to evaluate it as the "入口评审 agent" following the rubric provided. Let me first do the required web searches to understand the current landscape before making any judgments.

Let me search for:
1. Recent work on test-time RL for autoformalization
2. Co-adaptive retrieval for formal mathematics
3. DDRL and debiased RL for math reasoning
4. CriticLean and semantic critics for autoformalization


5. The current state of autoformalization research

I'll need to load the WebSearch tool to gather this information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b544881-3b2c-4712-8c94-c01cf0934f66",
  "isSidechain": false,
  "requestId": "req_011CbUQ1h5Y74wUahjCs64eo",
  "type": "assistant",
  "uuid": "1316dc8d-3109-4b19-ab13-6e6dfd4152dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SLm8yjrZAumjgsyNevybM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14245,
      "cache_read_input_tokens": 11014,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 246,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14245
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

_source line 9 · 2026-05-28T05:15:30.743Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016tsCDYdvvC1mgFu2jzcv37`</summary>

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
  "parentUuid": "1316dc8d-3109-4b19-ab13-6e6dfd4152dd",
  "isSidechain": false,
  "requestId": "req_011CbUQ1h5Y74wUahjCs64eo",
  "type": "assistant",
  "uuid": "0d6cdfca-4fa7-45ea-ab08-923ed5179306",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SLm8yjrZAumjgsyNevybM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14245,
      "cache_read_input_tokens": 11014,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 246,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14245
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

_source line 10 · 2026-05-28T05:15:30.753Z_

<details><summary>↩ Tool result · `toolu_016tsCDYdvvC1mgFu2jzcv37`</summary>

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
  "parentUuid": "0d6cdfca-4fa7-45ea-ab08-923ed5179306",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "19b027ab-955a-45a5-9503-2deac36f6bf0",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "0d6cdfca-4fa7-45ea-ab08-923ed5179306",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-28T05:15:33.917Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required 3-5 web searches to understand the current landscape before making any judgments. I'll search for the key topics in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19b027ab-955a-45a5-9503-2deac36f6bf0",
  "isSidechain": false,
  "requestId": "req_011CbUQ2EJ1BhxniWquDmaoH",
  "type": "assistant",
  "uuid": "1b110f5d-791d-4382-af8f-1a1dc527756b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194KnhVe24ekvUxPtmKqNns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 25259,
      "output_tokens": 367,
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
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 25259,
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

### Assistant

_source line 12 · 2026-05-28T05:15:34.951Z_

Let me conduct the required pre-scoring research. I'll run multiple searches in parallel to cover the key aspects of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b110f5d-791d-4382-af8f-1a1dc527756b",
  "isSidechain": false,
  "requestId": "req_011CbUQ2EJ1BhxniWquDmaoH",
  "type": "assistant",
  "uuid": "b5464649-7921-4264-91e5-3d9f93525031",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194KnhVe24ekvUxPtmKqNns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 25259,
      "output_tokens": 367,
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
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 25259,
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

### Tool call

_source line 13 · 2026-05-28T05:15:35.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018g6dtLmDKzW67GoyWnAwRz`</summary>

```json
{
  "query": "test-time reinforcement learning autoformalization Lean 4 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5464649-7921-4264-91e5-3d9f93525031",
  "isSidechain": false,
  "requestId": "req_011CbUQ2EJ1BhxniWquDmaoH",
  "type": "assistant",
  "uuid": "d14f6778-8b3c-4f06-ac72-3699163ee872",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194KnhVe24ekvUxPtmKqNns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 25259,
      "output_tokens": 367,
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
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 25259,
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

### Tool call

_source line 14 · 2026-05-28T05:15:36.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01THqwb15w4DFjwV3hV8wSmS`</summary>

```json
{
  "query": "DDRL debiased test-time RL GRPO spurious signal amplification math reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d14f6778-8b3c-4f06-ac72-3699163ee872",
  "isSidechain": false,
  "requestId": "req_011CbUQ2EJ1BhxniWquDmaoH",
  "type": "assistant",
  "uuid": "b5739323-908f-43f0-b0aa-84553669d796",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194KnhVe24ekvUxPtmKqNns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 25259,
      "output_tokens": 367,
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
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 25259,
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

### Tool call

_source line 15 · 2026-05-28T05:15:36.953Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GKYFrV8PWxwdJ9rt5qspTE`</summary>

```json
{
  "query": "CriticLean semantic critic autoformalization reward 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5739323-908f-43f0-b0aa-84553669d796",
  "isSidechain": false,
  "requestId": "req_011CbUQ2EJ1BhxniWquDmaoH",
  "type": "assistant",
  "uuid": "bb239675-4c33-4665-9676-a7e66aaa532e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194KnhVe24ekvUxPtmKqNns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 25259,
      "output_tokens": 367,
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
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 25259,
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

### Tool call

_source line 16 · 2026-05-28T05:15:37.953Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G8ApLQN6AQJUDB1fb32yvm`</summary>

```json
{
  "query": "co-adaptive retrieval augmented generation reinforcement learning R3 Reinforced-IR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb239675-4c33-4665-9676-a7e66aaa532e",
  "isSidechain": false,
  "requestId": "req_011CbUQ2EJ1BhxniWquDmaoH",
  "type": "assistant",
  "uuid": "4f9da6ac-554e-4725-b1c1-08550567d078",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194KnhVe24ekvUxPtmKqNns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 25259,
      "output_tokens": 367,
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
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 25259,
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

### Tool call

_source line 17 · 2026-05-28T05:15:39.017Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012HH4DaU5CcDBx8zXr4R7wB`</summary>

```json
{
  "query": "GDPO group reward decoupled normalization multi-reward RL NVIDIA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f9da6ac-554e-4725-b1c1-08550567d078",
  "isSidechain": false,
  "requestId": "req_011CbUQ2EJ1BhxniWquDmaoH",
  "type": "assistant",
  "uuid": "9b0b55b4-91f0-47b3-a820-63af4b806d8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194KnhVe24ekvUxPtmKqNns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 25259,
      "output_tokens": 367,
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
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 25259,
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

_source line 18 · 2026-05-28T05:15:43.740Z_

<details><summary>↩ Tool result · `toolu_018g6dtLmDKzW67GoyWnAwRz`</summary>

```text
Web search results for query: "test-time reinforcement learning autoformalization Lean 4 2025 2026"

Links: [{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372v1"},{"title":"(PDF) Online Reinforcement Learning for Autoformalization","url":"https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"},{"title":"Goedel-Prover: Open-Source ATP in Lean 4","url":"https://www.emergentmind.com/topics/goedel-prover"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"Towards Formalizing Reinforcement Learning Theory","url":"https://arxiv.org/pdf/2511.03618"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://openreview.net/pdf?id=k8KsI84Ds7"}]

Based on the web search results, here are the key findings related to test-time reinforcement learning, autoformalization, and Lean 4 developments in 2025-2026:

## Test-Time Reinforcement Learning (TTRL)

Test-Time RL is a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation. This approach enables discovery, combination, and reuse of intermediate lemmas autonomously.

## Performance Breakthroughs

In 2025, multiple independent systems achieved gold-medal equivalent performance on the International Mathematical Olympiad with formally verified Lean 4 proofs. More specifically, systems achieved 92.2% on MiniF2F with full Test-Time RL (TTRL) search framework.

## Autoformalization with Reinforcement Learning

FormaRL is a reinforcement learning framework for autoformalization that requires only a small amount of unlabeled data—addressing the critical data scarcity problem in formal verification. This approach showed 4-6× improvement in pass@1 autoformalization accuracy.

Recent work has studied online reinforcement learning for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4.

## Notable Applications

Math Inc. completed a challenge set by Fields Medallist Terence Tao and Alex Kontorovich in January 2024 to formalize the strong Prime Number Theorem (PNT) in Lean, which had stalled after 18+ months of human expert effort, in just three weeks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d14f6778-8b3c-4f06-ac72-3699163ee872",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "8ecf2806-ee08-4f52-860b-1949eca7a2c3",
  "toolUseResult": {
    "query": "test-time reinforcement learning autoformalization Lean 4 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J3VA55FH81uMEYXeBcdGrQ",
        "content": [
          {
            "title": "Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics",
            "url": "https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project",
            "url": "https://arxiv.org/html/2603.24372v1"
          },
          {
            "title": "(PDF) Online Reinforcement Learning for Autoformalization",
            "url": "https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"
          },
          {
            "title": "Goedel-Prover: Open-Source ATP in Lean 4",
            "url": "https://www.emergentmind.com/topics/goedel-prover"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4 | OpenReview",
            "url": "https://openreview.net/forum?id=k8KsI84Ds7"
          },
          {
            "title": "Towards Formalizing Reinforcement Learning Theory",
            "url": "https://arxiv.org/pdf/2511.03618"
          },
          {
            "title": "An Evaluation Benchmark for Autoformalization in Lean4",
            "url": "https://arxiv.org/pdf/2406.06555"
          },
          {
            "title": "PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4",
            "url": "https://openreview.net/pdf?id=k8KsI84Ds7"
          }
        ]
      },
      "Based on the web search results, here are the key findings related to test-time reinforcement learning, autoformalization, and Lean 4 developments in 2025-2026:\n\n## Test-Time Reinforcement Learning (TTRL)\n\nTest-Time RL is a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation. This approach enables discovery, combination, and reuse of intermediate lemmas autonomously.\n\n## Performance Breakthroughs\n\nIn 2025, multiple independent systems achieved gold-medal equivalent performance on the International Mathematical Olympiad with formally verified Lean 4 proofs. More specifically, systems achieved 92.2% on MiniF2F with full Test-Time RL (TTRL) search framework.\n\n## Autoformalization with Reinforcement Learning\n\nFormaRL is a reinforcement learning framework for autoformalization that requires only a small amount of unlabeled data—addressing the critical data scarcity problem in formal verification. This approach showed 4-6× improvement in pass@1 autoformalization accuracy.\n\nRecent work has studied online reinforcement learning for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4.\n\n## Notable Applications\n\nMath Inc. completed a challenge set by Fields Medallist Terence Tao and Alex Kontorovich in January 2024 to formalize the strong Prime Number Theorem (PNT) in Lean, which had stalled after 18+ months of human expert effort, in just three weeks."
    ],
    "durationSeconds": 8.222617161999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d14f6778-8b3c-4f06-ac72-3699163ee872",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T05:15:44.188Z_

<details><summary>↩ Tool result · `toolu_01GKYFrV8PWxwdJ9rt5qspTE`</summary>

```text
Web search results for query: "CriticLean semantic critic autoformalization reward 2025"

Links: [{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/html/2510.24592"},{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"},{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"},{"title":"M-A-P CriticLean: Critic-Guided Reinforcement Learning for","url":"https://arxiv.org/pdf/2507.06181"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"}]

Based on the search results, here's what I found about CriticLean:

## CriticLean Overview

CriticLean is a novel framework that elevates the critic from a passive validator to an active learning component, placing it at the center of the formalization pipeline and creating a feedback loop that drives iterative refinement of generated Lean 4 code.

## The Semantic Critic Component

CriticLean introduces reinforcement learning-based CriticLeanGPT models explicitly trained to evaluate whether the Lean 4 output truly reflects the intent of the original mathematical statement, rather than focusing primarily on generation quality or compiler validity.

## Key Components

CriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations, with CriticLeanBench serving as a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.

## Dataset and Results

The framework includes FineLeanCorpus, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.

## Integration with Reward Models

In autoformalization reward design, a positive reward is assigned to the final formal statement only when it achieves both syntactic and semantic correctness, where the semantic consistency is assessed between the formalization and the original question using an LLM-based judge evaluated by CriticLean-14B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb239675-4c33-4665-9676-a7e66aaa532e",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "7965f656-d818-4d78-8708-0bca2df0b8e3",
  "toolUseResult": {
    "query": "CriticLean semantic critic autoformalization reward 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NpY9C63HuK5aBcBAA5w5cP",
        "content": [
          {
            "title": "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization",
            "url": "https://arxiv.org/html/2510.24592"
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
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"
          },
          {
            "title": "[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181v1"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
          },
          {
            "title": "M-A-P CriticLean: Critic-Guided Reinforcement Learning for",
            "url": "https://arxiv.org/pdf/2507.06181"
          },
          {
            "title": "MathAtlas: A Benchmark for Autoformalization in the Wild",
            "url": "https://arxiv.org/html/2605.14061"
          }
        ]
      },
      "Based on the search results, here's what I found about CriticLean:\n\n## CriticLean Overview\n\nCriticLean is a novel framework that elevates the critic from a passive validator to an active learning component, placing it at the center of the formalization pipeline and creating a feedback loop that drives iterative refinement of generated Lean 4 code.\n\n## The Semantic Critic Component\n\nCriticLean introduces reinforcement learning-based CriticLeanGPT models explicitly trained to evaluate whether the Lean 4 output truly reflects the intent of the original mathematical statement, rather than focusing primarily on generation quality or compiler validity.\n\n## Key Components\n\nCriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations, with CriticLeanBench serving as a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.\n\n## Dataset and Results\n\nThe framework includes FineLeanCorpus, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.\n\n## Integration with Reward Models\n\nIn autoformalization reward design, a positive reward is assigned to the final formal statement only when it achieves both syntactic and semantic correctness, where the semantic consistency is assessed between the formalization and the original question using an LLM-based judge evaluated by CriticLean-14B."
    ],
    "durationSeconds": 7.232261354,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bb239675-4c33-4665-9676-a7e66aaa532e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T05:15:44.797Z_

<details><summary>↩ Tool result · `toolu_01THqwb15w4DFjwV3hV8wSmS`</summary>

```text
Web search results for query: "DDRL debiased test-time RL GRPO spurious signal amplification math reasoning 2026"

Links: [{"title":"Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/html/2604.21327"},{"title":"[2604.21327] Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/abs/2604.21327"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"},{"title":"Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients","url":"https://arxiv.org/pdf/2510.18924"},{"title":"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/pdf/2601.03661"},{"title":"[Literature Review] TTRL: Test-Time Reinforcement Learning","url":"https://www.themoonlight.io/en/review/ttrl-test-time-reinforcement-learning"},{"title":"Uncalibrated Reasoning: GRPO Induces Overconfidence for Stochastic Outcomes","url":"https://arxiv.org/pdf/2508.11800"},{"title":"Mitigating Think-Answer Mismatch in LLM Reasoning Through Noise-Aware Advantage Reweighting","url":"https://arxiv.org/pdf/2508.05928"},{"title":"Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts","url":"https://arxiv.org/pdf/2603.21177"}]

I found relevant results about DDRL and the issues with GRPO in test-time RL for math reasoning. Here's what the search revealed:

## Main Research Finding

Debiased and Denoised test-time Reinforcement Learning (DDRL) is a framework designed to mitigate spurious signals. The research addresses a critical problem in test-time RL where spurious rewards are amplified during training.

## The Problem Identified

GRPO's advantage estimation introduces a systematic bias in unsupervised settings, where its normalization mechanism disproportionately amplifies spurious rewards in low-consensus regimes. Responses with medium consistency form an ambiguity region and constitute the primary source of reward noise.

## DDRL's Solution

The framework employs three key strategies:

1. A frequency-based sampling strategy to exclude ambiguous samples while maintaining a balanced set of positive and negative examples.

2. A debiased advantage estimation with fixed advantages, removing the bias introduced by group-relative policy optimization.

3. A consensus-based off-policy refinement stage after the RL phase, where a rejection sampling dataset is constructed to enable efficient and stable post-RL optimization.

This research was published in April 2026 on arXiv and addresses a significant challenge in using test-time reinforcement learning for mathematical reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5739323-908f-43f0-b0aa-84553669d796",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "b4b3ae1c-4f10-4079-bf2b-99b2fe325d4b",
  "toolUseResult": {
    "query": "DDRL debiased test-time RL GRPO spurious signal amplification math reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GKMnRTvDzE7FjG9zJyRW4R",
        "content": [
          {
            "title": "Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning",
            "url": "https://arxiv.org/html/2604.21327"
          },
          {
            "title": "[2604.21327] Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning",
            "url": "https://arxiv.org/abs/2604.21327"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          },
          {
            "title": "Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients",
            "url": "https://arxiv.org/pdf/2510.18924"
          },
          {
            "title": "AMIR-GRPO: Inducing Implicit Preference Signals into GRPO",
            "url": "https://arxiv.org/pdf/2601.03661"
          },
          {
            "title": "[Literature Review] TTRL: Test-Time Reinforcement Learning",
            "url": "https://www.themoonlight.io/en/review/ttrl-test-time-reinforcement-learning"
          },
          {
            "title": "Uncalibrated Reasoning: GRPO Induces Overconfidence for Stochastic Outcomes",
            "url": "https://arxiv.org/pdf/2508.11800"
          },
          {
            "title": "Mitigating Think-Answer Mismatch in LLM Reasoning Through Noise-Aware Advantage Reweighting",
            "url": "https://arxiv.org/pdf/2508.05928"
          },
          {
            "title": "Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts",
            "url": "https://arxiv.org/pdf/2603.21177"
          }
        ]
      },
      "I found relevant results about DDRL and the issues with GRPO in test-time RL for math reasoning. Here's what the search revealed:\n\n## Main Research Finding\n\nDebiased and Denoised test-time Reinforcement Learning (DDRL) is a framework designed to mitigate spurious signals. The research addresses a critical problem in test-time RL where spurious rewards are amplified during training.\n\n## The Problem Identified\n\nGRPO's advantage estimation introduces a systematic bias in unsupervised settings, where its normalization mechanism disproportionately amplifies spurious rewards in low-consensus regimes. Responses with medium consistency form an ambiguity region and constitute the primary source of reward noise.\n\n## DDRL's Solution\n\nThe framework employs three key strategies:\n\n1. A frequency-based sampling strategy to exclude ambiguous samples while maintaining a balanced set of positive and negative examples.\n\n2. A debiased advantage estimation with fixed advantages, removing the bias introduced by group-relative policy optimization.\n\n3. A consensus-based off-policy refinement stage after the RL phase, where a rejection sampling dataset is constructed to enable efficient and stable post-RL optimization.\n\nThis research was published in April 2026 on arXiv and addresses a significant challenge in using test-time reinforcement learning for mathematical reasoning tasks."
    ],
    "durationSeconds": 8.323716208000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b5739323-908f-43f0-b0aa-84553669d796",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "b4b3ae1c-4f10-4079-bf2b-99b2fe325d4b",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Critic-guided test-time retrieval-augmented autoformalization",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Tool result

_source line 23 · 2026-05-28T05:15:46.355Z_

<details><summary>↩ Tool result · `toolu_01G8ApLQN6AQJUDB1fb32yvm`</summary>

```text
Web search results for query: "co-adaptive retrieval augmented generation reinforcement learning R3 Reinforced-IR 2025"

Links: [{"title":"Optimizing Retrieval for RAG via Reinforced Contrastive Learning","url":"https://arxiv.org/html/2510.24652v1"},{"title":"Optimizing Retrieval for RAG via Reinforcement Learning Jiawei Zhou Lei Chen","url":"https://openreview.net/pdf/74b57081a9a2db071d310000acfd1692aa247047.pdf"},{"title":"R3AG 2025: Workshop on Refined and Reliable Retrieval-Augmented Generation | Proceedings of the 2025 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region","url":"https://dl.acm.org/doi/10.1145/3767695.3769524"},{"title":"[2510.24652] Optimizing Retrieval for RAG via Reinforcement Learning","url":"https://arxiv.org/abs/2510.24652"},{"title":"Reinforced Information Retrieval","url":"https://arxiv.org/pdf/2502.11562"},{"title":"[2505.23794] R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2505.23794"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval ...","url":"https://aclanthology.org/2025.findings-emnlp.554.pdf"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2505.23794"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2505.23794v2"}]

Based on the search results, I found relevant information about these research topics:

## R3: Optimizing Retrieval for RAG via Reinforcement Learning

R3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. Unlike prior approaches that rely on annotated or synthetic data for supervised fine-tuning, R3 enables the retriever to dynamically explore and optimize relevance within the RAG environment.

The approach adopts an RL training paradigm that enables the retriever to explore and self-improve within given RAG environments, automating the learning process with minimal manual experimentation or tuning effort. R3 enables retrievers to effectively adapt from IR to RAG, achieving an average 5.2% improvement in 1-shot accuracy and consistently outperforming SOTA retrievers as well as LLM-empowered retrieval methods. It is both efficient and practical, requiring only 4 GPUs and completing training within a single day.

## Reinforced-IR

A key innovation of Reinforced-IR is its Self-Boosting framework, which enables retriever and generator to learn from each other's feedback. Specifically, the generator is reinforced to generate query augmentations that enhance the retriever's performance, while the retriever is trained to better discriminate the relevant documents identified by the generator. This iterative process allows the end-to-end retrieval performance to be progressively optimized using an unlabeled corpus from the target domain.

Both of these methods represent recent advances in co-adaptive approaches where retrieval and generation components learn from each other through reinforcement learning mechanisms in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f9da6ac-554e-4725-b1c1-08550567d078",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "40e9c90e-5bef-4664-94e9-f1bb6721a9e9",
  "toolUseResult": {
    "query": "co-adaptive retrieval augmented generation reinforcement learning R3 Reinforced-IR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GYMrJpf9YsSBXm2EcoYeZJ",
        "content": [
          {
            "title": "Optimizing Retrieval for RAG via Reinforced Contrastive Learning",
            "url": "https://arxiv.org/html/2510.24652v1"
          },
          {
            "title": "Optimizing Retrieval for RAG via Reinforcement Learning Jiawei Zhou Lei Chen",
            "url": "https://openreview.net/pdf/74b57081a9a2db071d310000acfd1692aa247047.pdf"
          },
          {
            "title": "R3AG 2025: Workshop on Refined and Reliable Retrieval-Augmented Generation | Proceedings of the 2025 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region",
            "url": "https://dl.acm.org/doi/10.1145/3767695.3769524"
          },
          {
            "title": "[2510.24652] Optimizing Retrieval for RAG via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2510.24652"
          },
          {
            "title": "Reinforced Information Retrieval",
            "url": "https://arxiv.org/pdf/2502.11562"
          },
          {
            "title": "[2505.23794] R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.23794"
          },
          {
            "title": "R3-RAG: Learning Step-by-Step Reasoning and Retrieval ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.554.pdf"
          },
          {
            "title": "R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2505.23794"
          },
          {
            "title": "R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.23794v2"
          }
        ]
      },
      "Based on the search results, I found relevant information about these research topics:\n\n## R3: Optimizing Retrieval for RAG via Reinforcement Learning\n\nR3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. Unlike prior approaches that rely on annotated or synthetic data for supervised fine-tuning, R3 enables the retriever to dynamically explore and optimize relevance within the RAG environment.\n\nThe approach adopts an RL training paradigm that enables the retriever to explore and self-improve within given RAG environments, automating the learning process with minimal manual experimentation or tuning effort. R3 enables retrievers to effectively adapt from IR to RAG, achieving an average 5.2% improvement in 1-shot accuracy and consistently outperforming SOTA retrievers as well as LLM-empowered retrieval methods. It is both efficient and practical, requiring only 4 GPUs and completing training within a single day.\n\n## Reinforced-IR\n\nA key innovation of Reinforced-IR is its Self-Boosting framework, which enables retriever and generator to learn from each other's feedback. Specifically, the generator is reinforced to generate query augmentations that enhance the retriever's performance, while the retriever is trained to better discriminate the relevant documents identified by the generator. This iterative process allows the end-to-end retrieval performance to be progressively optimized using an unlabeled corpus from the target domain.\n\nBoth of these methods represent recent advances in co-adaptive approaches where retrieval and generation components learn from each other through reinforcement learning mechanisms in 2025."
    ],
    "durationSeconds": 8.399684904,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4f9da6ac-554e-4725-b1c1-08550567d078",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T05:15:46.393Z_

<details><summary>↩ Tool result · `toolu_012HH4DaU5CcDBx8zXr4R7wB`</summary>

```text
Web search results for query: "GDPO group reward decoupled normalization multi-reward RL NVIDIA 2025 2026"

Links: [{"title":"[Podcast] GDPO: Group Reward-Decoupled Normalization for Multi-Reward RL Optimization - YouTube","url":"https://www.youtube.com/watch?v=2Abej7NG09I"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiviq.substack.com/p/gdpo-group-reward-decoupled-normalization"},{"title":"GDPO, not GRPO NVIDIA introduces Group reward-Decoupled Normalization Policy Optimization (GDPO), a new multi-reward RL algorithm that consistently improves per-reward convergence over GRPO across a wide range of tasks. They find that the common practice of applying GRPO to multi-reward optimization normalizes distinct reward combinations into identical advantage values. This collapses the training signal, reduces reward-level resolution, and leads to suboptimal convergence.","url":"https://www.threads.com/@sung.kim.mw/post/DTVU1v1kYZ1/gdpo-not-grpo-nvidia-introduces-group-reward-decoupled-normalization-policy"},{"title":"GitHub - NVlabs/GDPO: Official implementation of GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization · GitHub","url":"https://github.com/NVlabs/GDPO"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://www.emergent-behaviors.com/gdpo-group-reward-decoupled-normalization-policy-optimization-for-multi-reward-rl-optimization/"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/pdf/2601.05242"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://nvlabs.github.io/GDPO/"},{"title":"Paper page - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://huggingface.co/papers/2601.05242"},{"title":"[2601.05242] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/abs/2601.05242"}]

I found comprehensive information about GDPO. Here's what the research reveals:

## GDPO Overview

GDPO (Group Reward-Decoupled Normalization Policy Optimization) is a drop-in replacement for GRPO that consistently improves per-reward convergence in multi-reward RL training across tasks.

## The Problem GDPO Solves

Directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence. This issue is known as reward signal collapse, where different combinations of raw rewards result in identical advantage estimates, blinding the policy to improvements in specific objectives.

## How GDPO Works

GDPO performs group-wise normalization on each reward independently prior to aggregation, which contrasts with GRPO, which applies group-wise normalization directly to the summed rewards.

## Evaluation and Results

GDPO was compared with GRPO across three tasks: tool calling, math reasoning, and coding reasoning, evaluating both correctness metrics (accuracy, bug ratio) and constraint adherence metrics (format, length), with GDPO consistently outperforming GRPO across all settings.

## Research Team and Publication

The paper was authored by researchers from NVIDIA including Shih-Yang Liu, Xin Dong, Ximing Lu, and others, and was published in 2026 (arXiv ID: 2601.05242). The official implementation is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b0b55b4-91f0-47b3-a820-63af4b806d8f",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "c7c3e448-b847-445a-988a-19190d56c59f",
  "toolUseResult": {
    "query": "GDPO group reward decoupled normalization multi-reward RL NVIDIA 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NxXeGXerF8qCDmhACN6HkC",
        "content": [
          {
            "title": "[Podcast] GDPO: Group Reward-Decoupled Normalization for Multi-Reward RL Optimization - YouTube",
            "url": "https://www.youtube.com/watch?v=2Abej7NG09I"
          },
          {
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://arxiviq.substack.com/p/gdpo-group-reward-decoupled-normalization"
          },
          {
            "title": "GDPO, not GRPO NVIDIA introduces Group reward-Decoupled Normalization Policy Optimization (GDPO), a new multi-reward RL algorithm that consistently improves per-reward convergence over GRPO across a wide range of tasks. They find that the common practice of applying GRPO to multi-reward optimization normalizes distinct reward combinations into identical advantage values. This collapses the training signal, reduces reward-level resolution, and leads to suboptimal convergence.",
            "url": "https://www.threads.com/@sung.kim.mw/post/DTVU1v1kYZ1/gdpo-not-grpo-nvidia-introduces-group-reward-decoupled-normalization-policy"
          },
          {
            "title": "GitHub - NVlabs/GDPO: Official implementation of GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization · GitHub",
            "url": "https://github.com/NVlabs/GDPO"
          },
          {
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://www.emergent-behaviors.com/gdpo-group-reward-decoupled-normalization-policy-optimization-for-multi-reward-rl-optimization/"
          },
          {
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://arxiv.org/pdf/2601.05242"
          },
          {
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://nvlabs.github.io/GDPO/"
          },
          {
            "title": "Paper page - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://huggingface.co/papers/2601.05242"
          },
          {
            "title": "[2601.05242] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://arxiv.org/abs/2601.05242"
          }
        ]
      },
      "I found comprehensive information about GDPO. Here's what the research reveals:\n\n## GDPO Overview\n\nGDPO (Group Reward-Decoupled Normalization Policy Optimization) is a drop-in replacement for GRPO that consistently improves per-reward convergence in multi-reward RL training across tasks.\n\n## The Problem GDPO Solves\n\nDirectly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence. This issue is known as reward signal collapse, where different combinations of raw rewards result in identical advantage estimates, blinding the policy to improvements in specific objectives.\n\n## How GDPO Works\n\nGDPO performs group-wise normalization on each reward independently prior to aggregation, which contrasts with GRPO, which applies group-wise normalization directly to the summed rewards.\n\n## Evaluation and Results\n\nGDPO was compared with GRPO across three tasks: tool calling, math reasoning, and coding reasoning, evaluating both correctness metrics (accuracy, bug ratio) and constraint adherence metrics (format, length), with GDPO consistently outperforming GRPO across all settings.\n\n## Research Team and Publication\n\nThe paper was authored by researchers from NVIDIA including Shih-Yang Liu, Xin Dong, Ximing Lu, and others, and was published in 2026 (arXiv ID: 2601.05242). The official implementation is available on GitHub."
    ],
    "durationSeconds": 7.369423284000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9b0b55b4-91f0-47b3-a820-63af4b806d8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-28T05:15:49.145Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have initial results. Let me now search for more specific topics to complete my research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7c3e448-b847-445a-988a-19190d56c59f",
  "isSidechain": false,
  "requestId": "req_011CbUQ3NuhVhnkpN3wGGprz",
  "type": "assistant",
  "uuid": "75d1c477-40f9-41c5-86df-5c7101e6416c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZj5TDbqB5QrCjUnST4wte",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4727,
      "cache_read_input_tokens": 26032,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 4727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4727
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

_source line 26 · 2026-05-28T05:15:49.644Z_

Good, I have initial results. Let me search for additional specific topics to complete the landscape analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75d1c477-40f9-41c5-86df-5c7101e6416c",
  "isSidechain": false,
  "requestId": "req_011CbUQ3NuhVhnkpN3wGGprz",
  "type": "assistant",
  "uuid": "4bdd521f-cc31-4b74-b0c7-095d6c9d8c90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZj5TDbqB5QrCjUnST4wte",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4727,
      "cache_read_input_tokens": 26032,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 4727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4727
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

_source line 27 · 2026-05-28T05:15:50.638Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UAxeonuGtj8hqLazFdkmmK`</summary>

```json
{
  "query": "DDR direct dependency retrieval autoformalization identifier hallucination Mathlib 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bdd521f-cc31-4b74-b0c7-095d6c9d8c90",
  "isSidechain": false,
  "requestId": "req_011CbUQ3NuhVhnkpN3wGGprz",
  "type": "assistant",
  "uuid": "d1058cbe-1b34-419c-b646-d2ee945fdd50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZj5TDbqB5QrCjUnST4wte",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4727,
      "cache_read_input_tokens": 26032,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 4727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4727
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

_source line 28 · 2026-05-28T05:15:51.696Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ViczmfWRanRAU1YvU9y8rT`</summary>

```json
{
  "query": "FormaRL GRPO autoformalization COLM 2025 compilation reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1058cbe-1b34-419c-b646-d2ee945fdd50",
  "isSidechain": false,
  "requestId": "req_011CbUQ3NuhVhnkpN3wGGprz",
  "type": "assistant",
  "uuid": "d230dd73-a18a-4cdd-9f33-e3db569add51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZj5TDbqB5QrCjUnST4wte",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4727,
      "cache_read_input_tokens": 26032,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 4727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4727
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

_source line 29 · 2026-05-28T05:15:52.324Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HZqZXc68HUDTuCPK7LhLLV`</summary>

```json
{
  "query": "MathAtlas benchmark autoformalization wild graduate-level 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d230dd73-a18a-4cdd-9f33-e3db569add51",
  "isSidechain": false,
  "requestId": "req_011CbUQ3NuhVhnkpN3wGGprz",
  "type": "assistant",
  "uuid": "951415aa-89f3-4d9c-9030-0c18637d355c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZj5TDbqB5QrCjUnST4wte",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4727,
      "cache_read_input_tokens": 26032,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 4727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4727
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

_source line 30 · 2026-05-28T05:15:58.104Z_

<details><summary>↩ Tool result · `toolu_01HZqZXc68HUDTuCPK7LhLLV`</summary>

```text
Web search results for query: "MathAtlas benchmark autoformalization wild graduate-level 2026"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"[2601.03017] MMFormalizer: Multimodal Autoformalization in the Wild","url":"https://arxiv.org/abs/2601.03017"},{"title":"LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics","url":"https://arxiv.org/html/2602.24173v1"},{"title":"(PDF) FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://www.researchgate.net/publication/403308231_FormalProofBench_Can_Models_Write_Graduate_Level_Math_Proofs_That_Are_Formally_Verified"},{"title":"ProofNet: Autoformalizing and Formally Proving Undergraduate-Level   Mathematics","url":"https://arxiv.org/pdf/2302.12433"}]

Based on the search results, here's what I found about the MathAtlas benchmark:

MathAtlas is released as a benchmark set for large-scale autoformalization of graduate-level mathematics in the wild. It is the first large-scale autoformalization benchmark of graduate-level mathematics, containing approximately 52,000 theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

MathAtlas is enriched with a mathematical dependency graph containing approximately 178,000 relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

In terms of performance, MathAtlas is high quality but extremely challenging: strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "951415aa-89f3-4d9c-9030-0c18637d355c",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "39fe2d68-a2b3-490a-9fed-bd0de32bd84a",
  "toolUseResult": {
    "query": "MathAtlas benchmark autoformalization wild graduate-level 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012Su4vX6KxYAFNHiSYqXyTn",
        "content": [
          {
            "title": "[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild",
            "url": "https://arxiv.org/abs/2605.14061"
          },
          {
            "title": "MathAtlas: A Benchmark for Autoformalization in the Wild",
            "url": "https://arxiv.org/html/2605.14061"
          },
          {
            "title": "[2601.03017] MMFormalizer: Multimodal Autoformalization in the Wild",
            "url": "https://arxiv.org/abs/2601.03017"
          },
          {
            "title": "LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics",
            "url": "https://arxiv.org/html/2602.24173v1"
          },
          {
            "title": "(PDF) FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://www.researchgate.net/publication/403308231_FormalProofBench_Can_Models_Write_Graduate_Level_Math_Proofs_That_Are_Formally_Verified"
          },
          {
            "title": "ProofNet: Autoformalizing and Formally Proving Undergraduate-Level   Mathematics",
            "url": "https://arxiv.org/pdf/2302.12433"
          }
        ]
      },
      "Based on the search results, here's what I found about the MathAtlas benchmark:\n\nMathAtlas is released as a benchmark set for large-scale autoformalization of graduate-level mathematics in the wild. It is the first large-scale autoformalization benchmark of graduate-level mathematics, containing approximately 52,000 theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.\n\nMathAtlas is enriched with a mathematical dependency graph containing approximately 178,000 relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.\n\nIn terms of performance, MathAtlas is high quality but extremely challenging: strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others."
    ],
    "durationSeconds": 5.776556591,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "951415aa-89f3-4d9c-9030-0c18637d355c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T05:15:58.477Z_

<details><summary>↩ Tool result · `toolu_01UAxeonuGtj8hqLazFdkmmK`</summary>

```text
Web search results for query: "DDR direct dependency retrieval autoformalization identifier hallucination Mathlib 2025"

Links: [{"title":"[2511.11990] Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/abs/2511.11990"},{"title":"(PDF) Improving Autoformalization Using Direct Dependency Retrieval","url":"https://www.researchgate.net/publication/397701226_Improving_Autoformalization_Using_Direct_Dependency_Retrieval"},{"title":"Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/html/2511.11990v2"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/html/2510.10815"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"towards a faithful metric and a dependency retrieval","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/html/2512.00997"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/pdf/2510.04520"}]

Based on the search results, here's what I found about DDR (Direct Dependency Retrieval) and related topics in autoformalization with Mathlib 2025:

## Overview

DDR (Direct Dependency Retrieval) directly generates candidate library dependencies from natural language mathematical descriptions and subsequently verifies their existence within the formal library via an efficient suffix array check.

## The Problem It Addresses

The core difficulty in autoformalization lies in the fact that existing methods often suffer from a lack of contextual awareness, leading to hallucination of formal definitions and theorems. Current retrieval-augmented approaches exhibit poor precision and recall for formal library dependency retrieval, and lack the scalability to effectively leverage ever-growing public datasets.

## Key Features and Results

A dependency retrieval dataset of over 500,000 samples was constructed and a high-precision DDR model was fine-tuned. Experimental results demonstrate that the DDR model significantly outperforms state-of-the-art methods in both retrieval precision and recall.

## Context with Mathlib

Lean 4's mathlib contains over 240,000 entries, including many with similar descriptions and usage. The DDR method was designed to address the challenge of retrieving the correct dependencies from such large formal libraries to reduce hallucination in autoformalization tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1058cbe-1b34-419c-b646-d2ee945fdd50",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "99affb7e-e48d-4370-b804-c998340b2d5f",
  "toolUseResult": {
    "query": "DDR direct dependency retrieval autoformalization identifier hallucination Mathlib 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015AyCHhYq2oo8X1b28cE93o",
        "content": [
          {
            "title": "[2511.11990] Improving Autoformalization Using Direct Dependency Retrieval",
            "url": "https://arxiv.org/abs/2511.11990"
          },
          {
            "title": "(PDF) Improving Autoformalization Using Direct Dependency Retrieval",
            "url": "https://www.researchgate.net/publication/397701226_Improving_Autoformalization_Using_Direct_Dependency_Retrieval"
          },
          {
            "title": "Improving Autoformalization Using Direct Dependency Retrieval",
            "url": "https://arxiv.org/html/2511.11990v2"
          },
          {
            "title": "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://arxiv.org/html/2510.10815"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/html/2508.06931"
          },
          {
            "title": "towards a faithful metric and a dependency retrieval",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/html/2512.00997"
          },
          {
            "title": "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/pdf/2510.04520"
          }
        ]
      },
      "Based on the search results, here's what I found about DDR (Direct Dependency Retrieval) and related topics in autoformalization with Mathlib 2025:\n\n## Overview\n\nDDR (Direct Dependency Retrieval) directly generates candidate library dependencies from natural language mathematical descriptions and subsequently verifies their existence within the formal library via an efficient suffix array check.\n\n## The Problem It Addresses\n\nThe core difficulty in autoformalization lies in the fact that existing methods often suffer from a lack of contextual awareness, leading to hallucination of formal definitions and theorems. Current retrieval-augmented approaches exhibit poor precision and recall for formal library dependency retrieval, and lack the scalability to effectively leverage ever-growing public datasets.\n\n## Key Features and Results\n\nA dependency retrieval dataset of over 500,000 samples was constructed and a high-precision DDR model was fine-tuned. Experimental results demonstrate that the DDR model significantly outperforms state-of-the-art methods in both retrieval precision and recall.\n\n## Context with Mathlib\n\nLean 4's mathlib contains over 240,000 entries, including many with similar descriptions and usage. The DDR method was designed to address the challenge of retrieving the correct dependencies from such large formal libraries to reduce hallucination in autoformalization tasks."
    ],
    "durationSeconds": 7.833453198999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d1058cbe-1b34-419c-b646-d2ee945fdd50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "99affb7e-e48d-4370-b804-c998340b2d5f",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Critic-guided test-time retrieval-augmented autoformalization",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Tool result

_source line 34 · 2026-05-28T05:16:00.159Z_

<details><summary>↩ Tool result · `toolu_01ViczmfWRanRAU1YvU9y8rT`</summary>

```text
Web search results for query: "FormaRL GRPO autoformalization COLM 2025 compilation reward"

Links: [{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data | OpenReview","url":"https://openreview.net/forum?id=Z2El1U94bq"},{"title":"[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/abs/2508.18914"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://openreview.net/pdf?id=Z2El1U94bq"},{"title":"Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs","url":"https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"},{"title":"[PDF] FormaRL: Enhancing Autoformalization with no Labeled Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FormaRL:-Enhancing-Autoformalization-with-no-Data-Huang-Jin/b430d8ac9cf1236314a1273dc7e8fb9769ebae70"},{"title":"Published as a conference paper at COLM 2025","url":"https://par.nsf.gov/servlets/purl/10635650"},{"title":"FormaRL: RL-Driven Autoformalization for Lean 4","url":"https://www.emergentmind.com/topics/formarl"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"}]

Based on the search results, here's what I found about FormaRL, GRPO, and autoformalization:

## FormaRL Overview

FormaRL is a reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. The work was published at COLM 2025.

## Reward Structure with Compilation

FormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer. More specifically, during RL training, 16 proofs for each problem were generated and verified through compilation, with correct proofs receiving a reward of +8.

## Performance Results

FormaRL increased the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4-6x (4.04% → 26.15% on ProofNet and 2.4% → 9.6% on uproof) with merely 859 unlabeled data. Additionally, on uproof the method achieved improvements in out-of-distribution performance compared to existing open-source state-of-the-art autoformalizers on both pass@1 accuracy (6.2% → 9.6%) and pass@16 accuracy (24.4% → 33.6%).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d230dd73-a18a-4cdd-9f33-e3db569add51",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "2e90e928-d3e0-4dac-814a-d6ce79f093aa",
  "toolUseResult": {
    "query": "FormaRL GRPO autoformalization COLM 2025 compilation reward",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N7XkMJj7BpVunVAkUKcwBR",
        "content": [
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data | OpenReview",
            "url": "https://openreview.net/forum?id=Z2El1U94bq"
          },
          {
            "title": "[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/abs/2508.18914"
          },
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://openreview.net/pdf?id=Z2El1U94bq"
          },
          {
            "title": "Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs",
            "url": "https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"
          },
          {
            "title": "[PDF] FormaRL: Enhancing Autoformalization with no Labeled Data | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/FormaRL:-Enhancing-Autoformalization-with-no-Data-Huang-Jin/b430d8ac9cf1236314a1273dc7e8fb9769ebae70"
          },
          {
            "title": "Published as a conference paper at COLM 2025",
            "url": "https://par.nsf.gov/servlets/purl/10635650"
          },
          {
            "title": "FormaRL: RL-Driven Autoformalization for Lean 4",
            "url": "https://www.emergentmind.com/topics/formarl"
          },
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/pdf/2508.18914"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project",
            "url": "https://arxiv.org/html/2603.24372"
          }
        ]
      },
      "Based on the search results, here's what I found about FormaRL, GRPO, and autoformalization:\n\n## FormaRL Overview\n\nFormaRL is a reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. The work was published at COLM 2025.\n\n## Reward Structure with Compilation\n\nFormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer. More specifically, during RL training, 16 proofs for each problem were generated and verified through compilation, with correct proofs receiving a reward of +8.\n\n## Performance Results\n\nFormaRL increased the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4-6x (4.04% → 26.15% on ProofNet and 2.4% → 9.6% on uproof) with merely 859 unlabeled data. Additionally, on uproof the method achieved improvements in out-of-distribution performance compared to existing open-source state-of-the-art autoformalizers on both pass@1 accuracy (6.2% → 9.6%) and pass@16 accuracy (24.4% → 33.6%)."
    ],
    "durationSeconds": 8.459439776000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d230dd73-a18a-4cdd-9f33-e3db569add51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-28T05:16:00.164Z_

```json
{
  "parentUuid": "2e90e928-d3e0-4dac-814a-d6ce79f093aa",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9913f72c-a183-4de8-8672-5509e1adef8d",
  "timestamp": "2026-05-28T05:16:00.164Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-28T05:16:02.327Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for additional key papers to validate the proposal's references and check for any existing work that might closely overlap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9913f72c-a183-4de8-8672-5509e1adef8d",
  "isSidechain": false,
  "requestId": "req_011CbUQ4Pq3VcL7hSe1VvfXL",
  "type": "assistant",
  "uuid": "1bafc978-2385-4e2b-aef7-d5a7565e0598",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FzwhKZU34T4M3vTZiF4UC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 30759,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 590,
          "output_tokens": 184,
          "cache_read_input_tokens": 30759,
          "cache_creation_input_tokens": 1892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1892
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

_source line 37 · 2026-05-28T05:16:03.284Z_

Let me do two more targeted searches to check for direct competitors and validate key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bafc978-2385-4e2b-aef7-d5a7565e0598",
  "isSidechain": false,
  "requestId": "req_011CbUQ4Pq3VcL7hSe1VvfXL",
  "type": "assistant",
  "uuid": "9276074d-9066-4766-83b4-3ddea55e0f90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FzwhKZU34T4M3vTZiF4UC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 30759,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 590,
          "output_tokens": 184,
          "cache_read_input_tokens": 30759,
          "cache_creation_input_tokens": 1892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1892
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

_source line 38 · 2026-05-28T05:16:04.293Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B3hQU5NVEd8ryzXH21xuSL`</summary>

```json
{
  "query": "TTRL test-time reinforcement learning formal mathematics theorem proving 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9276074d-9066-4766-83b4-3ddea55e0f90",
  "isSidechain": false,
  "requestId": "req_011CbUQ4Pq3VcL7hSe1VvfXL",
  "type": "assistant",
  "uuid": "a9884ddd-978e-4bb9-95c5-f62c5df85aff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FzwhKZU34T4M3vTZiF4UC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 30759,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 590,
          "output_tokens": 184,
          "cache_read_input_tokens": 30759,
          "cache_creation_input_tokens": 1892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1892
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

_source line 39 · 2026-05-28T05:16:05.359Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTj2iikUBjkXxS9CmcMed1`</summary>

```json
{
  "query": "Construction-Verification AMBER benchmark Lean 4 compilation error taxonomy identifier hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9884ddd-978e-4bb9-95c5-f62c5df85aff",
  "isSidechain": false,
  "requestId": "req_011CbUQ4Pq3VcL7hSe1VvfXL",
  "type": "assistant",
  "uuid": "4b4413cf-e89f-426e-bfec-4774f237856d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FzwhKZU34T4M3vTZiF4UC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 30759,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 590,
          "output_tokens": 184,
          "cache_read_input_tokens": 30759,
          "cache_creation_input_tokens": 1892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1892
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

_source line 40 · 2026-05-28T05:16:16.020Z_

<details><summary>↩ Tool result · `toolu_01KTj2iikUBjkXxS9CmcMed1`</summary>

```text
Web search results for query: "Construction-Verification AMBER benchmark Lean 4 compilation error taxonomy identifier hallucination 2026"

Links: [{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291v1"},{"title":"[2602.01291] Construction-Verification: A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/abs/2602.01291"},{"title":"Construction-Verification: A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/pdf/2602.01291"},{"title":"AMBER: An LLM-free Multi-dimensional Benchmark for MLLMs Hallucination   Evaluation","url":"https://arxiv.org/pdf/2311.07397"},{"title":"Why the open-source programming language is becoming a key tool to inject rigor and certainty into AI systems.","url":"https://venturebeat.com/ai/lean4-how-the-theorem-prover-works-and-why-its-the-new-competitive-edge-in"}]

I found relevant results for your search query. The search returned information about the Construction-Verification AMBER benchmark research paper, which appears to be a February 2026 preprint.

## Key Findings:

AMBER (Applied Mathematics BEnchmark for Reasoning) is a comprehensive benchmark spanning core domains of applied mathematics, including convex analysis, optimization, numerical algebra, and high-dimensional probability.

### Lean 4 Compilation Error Taxonomy and Identifier Hallucination

The research identifies specific compilation error categories in Lean 4:

**Hallucination (47.3% of failures):** The most prevalent source of error, accounting for 47.3% (1,512 cases), is the invocation of non-existent theorems or definitions, where the model hallucinates plausible-sounding Mathlib identifiers (e.g., convexHull_eq_sInter) that do not exist in the actual library.

**Formalization Competence (32.7% of failures):** The second largest category comprises 32.7% of errors, stemming from insufficient formalization skills, occurring when the model utilizes valid theorems and tactics but misapplies them.

**Output Formatting (4.8% of failures):** A minor fraction of 4.8% (154 cases) is attributed to basic output formatting errors, such as failing to encapsulate code within standard markdown blocks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b4413cf-e89f-426e-bfec-4774f237856d",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "b4d39f86-cf23-4955-9e61-6fd5ecb741a3",
  "toolUseResult": {
    "query": "Construction-Verification AMBER benchmark Lean 4 compilation error taxonomy identifier hallucination 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016t8ELCFmydnSCWRS7UcvnZ",
        "content": [
          {
            "title": "Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4",
            "url": "https://arxiv.org/html/2602.01291v1"
          },
          {
            "title": "[2602.01291] Construction-Verification: A Benchmark for Applied Mathematics in Lean 4",
            "url": "https://arxiv.org/abs/2602.01291"
          },
          {
            "title": "Construction-Verification: A Benchmark for Applied Mathematics in Lean 4",
            "url": "https://arxiv.org/pdf/2602.01291"
          },
          {
            "title": "AMBER: An LLM-free Multi-dimensional Benchmark for MLLMs Hallucination   Evaluation",
            "url": "https://arxiv.org/pdf/2311.07397"
          },
          {
            "title": "Why the open-source programming language is becoming a key tool to inject rigor and certainty into AI systems.",
            "url": "https://venturebeat.com/ai/lean4-how-the-theorem-prover-works-and-why-its-the-new-competitive-edge-in"
          }
        ]
      },
      "I found relevant results for your search query. The search returned information about the Construction-Verification AMBER benchmark research paper, which appears to be a February 2026 preprint.\n\n## Key Findings:\n\nAMBER (Applied Mathematics BEnchmark for Reasoning) is a comprehensive benchmark spanning core domains of applied mathematics, including convex analysis, optimization, numerical algebra, and high-dimensional probability.\n\n### Lean 4 Compilation Error Taxonomy and Identifier Hallucination\n\nThe research identifies specific compilation error categories in Lean 4:\n\n**Hallucination (47.3% of failures):** The most prevalent source of error, accounting for 47.3% (1,512 cases), is the invocation of non-existent theorems or definitions, where the model hallucinates plausible-sounding Mathlib identifiers (e.g., convexHull_eq_sInter) that do not exist in the actual library.\n\n**Formalization Competence (32.7% of failures):** The second largest category comprises 32.7% of errors, stemming from insufficient formalization skills, occurring when the model utilizes valid theorems and tactics but misapplies them.\n\n**Output Formatting (4.8% of failures):** A minor fraction of 4.8% (154 cases) is attributed to basic output formatting errors, such as failing to encapsulate code within standard markdown blocks."
    ],
    "durationSeconds": 10.655375263000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4b4413cf-e89f-426e-bfec-4774f237856d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-28T05:16:28.902Z_

<details><summary>↩ Tool result · `toolu_01B3hQU5NVEd8ryzXH21xuSL`</summary>

```text
Web search results for query: "TTRL test-time reinforcement learning formal mathematics theorem proving 2025 2026"

Links: [{"title":"TTRL: Test-Time Reinforcement Learning","url":"https://mail.bycloud.ai/p/ttrl-test-time-reinforcement-learning"},{"title":"Test-Time Reinforcement Learning","url":"https://www.emergentmind.com/topics/test-time-reinforcement-learning-ttrl"},{"title":"Kimina-Prover: Applying Test-time RL Search on Large Formal Reasoning Models","url":"https://huggingface.co/blog/AI-MO/kimina-prover"},{"title":"Olympiad-level formal mathematical reasoning with reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09833-y"},{"title":"TTRL: Test-Time Reinforcement Learning | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/ttrl-test-time-reinforcement-learning-d78a74e78a28"},{"title":"AI Research Review 25.04.25 – DAM and Reasoning","url":"https://patmcguinness.substack.com/p/ai-research-review-250425-dam-and"},{"title":"arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084"},{"title":"Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience","url":"https://arxiv.org/pdf/2512.17260"},{"title":"ETTRL: Balancing Exploration and Exploitation in LLM Test-Time Reinforcement Learning Via Entropy Mechanism","url":"https://arxiv.org/pdf/2508.11356"}]

Based on the search results, here's what I found about TTRL (Test-Time Reinforcement Learning) and its applications to formal mathematics and theorem proving in 2025-2026:

## Overview of TTRL

TTRL is a novel method for training LLMs using RL on unlabeled data. Instead of relying on external labels, the model samples multiple responses to a problem, votes on the best answer internally, and uses that consensus to guide its own learning.

## Performance on Mathematical Benchmarks

Researchers tested TTRL on mathematical benchmarks like AIME 2024 and MATH-500 and it performed remarkably well. Specifically, when TTRL was applied to the Qwen2.5-Math-7B model, the model's performance on the AIME 2024 task increased by 159.3%, with pass@1 accuracy going up from 16.7% to 43.3%.

## Applications to Formal Theorem Proving

Extension to agentic, continual, and multimodal domains is ongoing, with initial results in video reasoning, planning, and theorem proving suggesting strong promise. 

A prominent example is Kimina-Prover, which applying the full Test-Time Reinforcement Learning (TTRL) search framework yields a final pass rate of 92.2% on the miniF2F benchmark. Additionally, test-time RL is used by some systems to generate and learn from millions of related problem variants at inference time to enable deep, problem-specific adaptation.

## Future Research Directions

While empirical evidence is robust, formal guarantees of convergence in large-scale or online unsupervised TTRL are a target for future research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9884ddd-978e-4bb9-95c5-f62c5df85aff",
  "isSidechain": false,
  "promptId": "77ace666-bac9-4520-af5b-f7ddaf657f79",
  "type": "user",
  "uuid": "dae3cc92-5cdc-487d-904c-eea8237cbdcf",
  "toolUseResult": {
    "query": "TTRL test-time reinforcement learning formal mathematics theorem proving 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RizdhJ3JN2HDK17utekmbB",
        "content": [
          {
            "title": "TTRL: Test-Time Reinforcement Learning",
            "url": "https://mail.bycloud.ai/p/ttrl-test-time-reinforcement-learning"
          },
          {
            "title": "Test-Time Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/test-time-reinforcement-learning-ttrl"
          },
          {
            "title": "Kimina-Prover: Applying Test-time RL Search on Large Formal Reasoning Models",
            "url": "https://huggingface.co/blog/AI-MO/kimina-prover"
          },
          {
            "title": "Olympiad-level formal mathematical reasoning with reinforcement learning | Nature",
            "url": "https://www.nature.com/articles/s41586-025-09833-y"
          },
          {
            "title": "TTRL: Test-Time Reinforcement Learning | by Eleventh Hour Enthusiast | Medium",
            "url": "https://medium.com/@EleventhHourEnthusiast/ttrl-test-time-reinforcement-learning-d78a74e78a28"
          },
          {
            "title": "AI Research Review 25.04.25 – DAM and Reasoning",
            "url": "https://patmcguinness.substack.com/p/ai-research-review-250425-dam-and"
          },
          {
            "title": "arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2504.16084"
          },
          {
            "title": "Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience",
            "url": "https://arxiv.org/pdf/2512.17260"
          },
          {
            "title": "ETTRL: Balancing Exploration and Exploitation in LLM Test-Time Reinforcement Learning Via Entropy Mechanism",
            "url": "https://arxiv.org/pdf/2508.11356"
          }
        ]
      },
      "Based on the search results, here's what I found about TTRL (Test-Time Reinforcement Learning) and its applications to formal mathematics and theorem proving in 2025-2026:\n\n## Overview of TTRL\n\nTTRL is a novel method for training LLMs using RL on unlabeled data. Instead of relying on external labels, the model samples multiple responses to a problem, votes on the best answer internally, and uses that consensus to guide its own learning.\n\n## Performance on Mathematical Benchmarks\n\nResearchers tested TTRL on mathematical benchmarks like AIME 2024 and MATH-500 and it performed remarkably well. Specifically, when TTRL was applied to the Qwen2.5-Math-7B model, the model's performance on the AIME 2024 task increased by 159.3%, with pass@1 accuracy going up from 16.7% to 43.3%.\n\n## Applications to Formal Theorem Proving\n\nExtension to agentic, continual, and multimodal domains is ongoing, with initial results in video reasoning, planning, and theorem proving suggesting strong promise. \n\nA prominent example is Kimina-Prover, which applying the full Test-Time Reinforcement Learning (TTRL) search framework yields a final pass rate of 92.2% on the miniF2F benchmark. Additionally, test-time RL is used by some systems to generate and learn from millions of related problem variants at inference time to enable deep, problem-specific adaptation.\n\n## Future Research Directions\n\nWhile empirical evidence is robust, formal guarantees of convergence in large-scale or online unsupervised TTRL are a target for future research."
    ],
    "durationSeconds": 24.604928264,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a9884ddd-978e-4bb9-95c5-f62c5df85aff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-28T05:17:19.797Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the research landscape. Let me synthesize my findings and provide the evaluation.

Let me think carefully about this proposal:

## Summary of the proposal
TTRA proposes combining four independently validated capabilities for test-time adaptation of autoformalization:
1. Co-adaptive retrieval using Lean 4's structured error taxonomy during TTRL
2. CriticLean-14B as a calibrated semantic RL reward
3. A "binarize-then-enrich" adaptation of DDRL's binary debiasing to multi-tier rewards using GDPO


4. Progressive domain curriculum for OOD adaptation

## Key Questions:

### Trivial Alternative Check
The core question is whether the full machinery of co-adaptive retrieval, DDRL debiasing, and GDPO enrichment delivers meaningful improvements over a simpler baseline—just static retrieval plus CriticLean as the reward signal with vanilla GRPO. FormaRL already demonstrates 4→26% on ProofNet with vanilla GRPO and compilation rewards, so adding a better reward model seems like a natural next step. The real test is whether all these components together justify the added complexity.

The co-adaptive retrieval mechanism is genuinely necessary though. On out-of-distribution domains, the retriever must adapt because the distribution of required Mathlib dependencies shifts. I could try a simpler iterative approach—generate, fail, parse errors, update the retriever offline, regenerate—but that lacks the tight feedback loop of the RL formulation.

### Novelty Assessment
The co-adaptive retrieval for autoformalization using Lean 4 error signals is the genuinely novel contribution here. No prior work combines co-adaptive retrieval with autoformalization, and using Lean 4's structured error taxonomy—unknownIdentifier, type mismatch, and others—as graded signals for training the retriever is a novel technical approach. The tiered hierarchy of error signals is well-motivated by the structural properties of the language.

The binarize-then-enrich adaptation of DDRL to multi-tier rewards feels more incremental—it's essentially binarizing the rewards so DDRL works, then adding back the continuous component as a bonus. Once you know both DDRL and GDPO exist, the idea is fairly straightforward. Using CriticLean as a TTRL reward with calibration analysis under distributional shift is a thoughtful engineering contribution, but it's more practical than conceptually novel. Applying TTRL to autoformalization rather than theorem proving is a meaningful application novelty, though.

### Significance Assessment
Autoformalization is an important problem for AI in mathematics, and OOD generalization is a real bottleneck. The identifier hallucination problem dominates at 47.3% according to AMBER, so targeting it with co-adaptive retrieval is well-motivated. The practical impact ultimately hinges on whether the approach actually delivers results.

### Core Concerns
The proposal integrates 4+ existing techniques in a new configuration, so the novelty is primarily in the combination and adaptation to autoformalization rather than in individual components. There's a risk of this reading as a "combination paper" lacking a single deep insight, especially with 4 phases, 3 claimed innovations, and multiple ablations. The justification that TTRL cannot be naively applied to autoformalization—based on majority voting, advantage normalization, and static retrieval issues—needs to be more convincing.

The "binarize-then-enrich" contribution feels like a natural engineering fix rather than a surprising insight, and once you know DDRL works with binary rewards and GDPO handles multi-reward, combining them this way is almost obvious. CriticLean's calibration under distributional shift is a valid and nice contribution, but it's more of an empirical characterization study than a novel method.

### What's genuinely strong
The co-adaptive retrieval mechanism exploiting Lean 4's error taxonomy stands out as the strongest novel contribution, with its graded hierarchy of error tiers well-motivated and specific to autoformalization. The Phase -1 and Phase 0 de-risking design also demonstrates strong thinking.

The "contribution floor" analysis is honest and thoughtful, and the problem itself is real and quantifiably important given the 47.3% identifier hallucination rate. The related work coverage is extremely thorough, showing deep field knowledge.

### My assessment:

Novelty is medium—the co-adaptive retrieval for autoformalization is genuinely novel, but the rest is competent combination work where "binarize-then-enrich" feels somewhat obvious once you know the building blocks. Significance is medium to strong since autoformalization OOD generalization is an important practical problem. The key limiting factor is novelty depth—while the combination is novel in execution, the individual contributions aside from co-adaptive retrieval are relatively straightforward applications.

A reviewer might critique this as well-executed engineering with limited core insights, though the problem importance, solid motivation, and thorough experimental design could make it compelling if results are strong. I'm estimating around 25-38%, with a median of 30%.

But reconsidering for a top venue like AAAI, the paper needs to stand out. The real question is whether co-adaptive retrieval during TTRL significantly outperforms static retrieval—that would be moderately surprising. The binarize-then-enrich beating vanilla GRPO is expected, not surprising. What matters is whether the full pipeline enables meaningful improvements that justify the added complexity.

The paper's real strength lies in being the first to combine TTRL with autoformalization, implement co-adaptive retrieval for this task, and adapt multi-tier rewards—these "firsts" have value at AAAI, especially if results are strong. The risk is being perceived as a systems paper that combines existing components without a single deep insight, though AAAI is generally more receptive to systems-level contributions than some other venues. I'm settling on 25-35%, median 30%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dae3cc92-5cdc-487d-904c-eea8237cbdcf",
  "isSidechain": false,
  "requestId": "req_011CbUQ6WwUtMh1tiGvfoUup",
  "type": "assistant",
  "uuid": "9ee1fbb9-4f8a-4394-a7ba-6c34192cbbbd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtNZiLaJPGiLySbY97H3PF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 32651,
      "output_tokens": 7221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 643,
          "output_tokens": 7221,
          "cache_read_input_tokens": 32651,
          "cache_creation_input_tokens": 1677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1677
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

_source line 43 · 2026-05-28T05:19:09.375Z_

Now I have sufficient information to provide my evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084) (NeurIPS 2025): 在无标签数据上通过多数投票伪标签进行 GRPO 训练，Qwen2.5-Math-7B 在 AIME 2024 上从 16.7%→43.3%。本 proposal 的基础框架，但 TTRL 仅用于非形式化数学推理，依赖数值答案的多数投票——这正是 proposal 要解决的问题之一（形式化语句无法直接做 majority voting）。

- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327) (ACL 2026 Findings): 诊断并修复 GRPO 在 TTRL 中的 spurious signal amplification，提出 frequency-based balanced sampling + fixed ±1 advantages + consensus-based off-policy refinement。在 AIME 2024 上相对 TTRL baseline（15.8→25.0 for Qwen2.5-Math-1.5B）提升显著。**但仅支持 binary rewards**，其作者明确将 multi-reward 扩展留作 future work。proposal 的 "binarize-then-enrich" 正是回应这一 gap。

- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242) (NVIDIA, Jan 2026): 发现 GRPO 在 multi-reward 场景下会将不同 reward 组合 collapse 成相同 advantage 值，提出 per-reward decoupled normalization。已在 tool calling、math reasoning、coding 上验证。proposal 借用其 per-reward normalization 作为 enrichment layer。

- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181) (ByteDance/Nanjing, July 2025): 训练 CriticLeanGPT-14B-RL 达到 84.8% accuracy（32B 版本 87.0%），将 autoformalization pipeline 准确率从 54%→84%。但仅在 balanced 250/250 分布上评估，OOD 场景下的 skewed distribution 表现未知。proposal 的 Phase 0 calibration 正是针对此 gap。

- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914) (COLM 2025): 首个将 GRPO+compilation reward 用于 autoformalization，Qwen2.5-Coder-7B 在 ProofNet 上从 4%→26%。但使用 LLM consistency 作为语义 reward（而非 trained critic），且无 retrieval，仅在 in-distribution 场景。

- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization) (Wang et al., NeurIPS 2025 MAR Workshop): 使用 GRPO + composite BEq+embedding rewards 在 Lean 4 上做 autoformalization RL，TC1: 17.29%→26.01%。**最近的 baseline**，但属于 training-time RL，使用 embedding similarity 而非 trained critic，无 retrieval 和 test-time adaptation。

- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990) (2025): 构建 500K 样本依赖数据集，量化 ICL 生成的依赖中~30% 为 hallucinated identifiers（Hall_m=0.21-0.39），retrieval-based DDR 将 hallucination 降至 <2%。proposal 使用其数据集和 retriever 架构作为起点。

- [Construction-Verification/AMBER Benchmark](https://arxiv.org/abs/2602.01291) (Yang et al., Feb 2026): 在 applied math 领域分析 3,189 个编译错误，发现 47.3% 为 hallucination of non-existent theorems/definitions。这是 proposal 关于 "identifier hallucination 是 dominant error mode" 的最强实证支撑。

- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652) (NeurIPS 2025): 通过 trial-and-feedback reinforced contrastive learning 优化 RAG 环境中的 retriever。proposal 的 co-adaptive retrieval 借鉴其 contrastive learning 框架，但应用到完全不同的 domain（Lean 4 dependency retrieval）。

- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061) (May 2026): 52K graduate-level 问题，最佳模型仅 9.8% correctness on theorems，MA-Hard 上 2.6%。验证了 OOD autoformalization 仍是极具挑战性的开放问题。

- 调研总结: Autoformalization 领域在 2025-2026 经历快速发展：RL-based 方法（FormaRL, Online RL）已初步验证，semantic critic（CriticLean）提供了编译之外的 reward 信号，static retrieval（DDR, DRIFT, CRAMF）大幅降低了 identifier hallucination，TTRL 在非形式化数学推理中取得突破。但**尚无工作将 TTRL 应用于 autoformalization，尚无工作在 RL 过程中对 retriever 做 co-adaptive 更新，尚无工作将 DDRL 的 binary debiasing 扩展到 multi-tier rewards**。Proposal 定位在这三个 gap 的交叉点上。

【Trivial Alternative 检验】:

最直接的 trivial alternative 是：**static DDR retrieval + CriticLean reward + vanilla GRPO（不做 co-adaptive retrieval，不做 DDRL debiasing）**。这基本上是把 FormaRL 的 reward 换成更好的 CriticLean，再加上 DDR 提供的 Mathlib 依赖。

这个 trivial baseline 的关键弱点在于：
1. **Static retrieval 在 OOD 域会失效**：DDR 的 retriever 在训练数据分布上训练，面对 condensed mathematics 或 algebraic geometry 等 far-OOD 域，retrieval recall 会显著下降，因为 query distribution 发生了 shift。这是 co-adaptive retrieval 的核心增量价值——retriever 随 formalizer 的行为变化而适应。
2. **Vanilla GRPO 在低 consensus 场景会放大噪声**：DDRL 已经实证证明了这一点（AIME 2024 上 TTRL baseline 仅 15.8 vs DDRL 的 25.0）。在 autoformalization 的 OOD 场景中，compilable rate 很低，consensus 更差，噪声放大问题会更严重。

但也必须承认：**在 near-OOD 域，static retrieval + CriticLean + vanilla GRPO 可能已经足够好**。Proposal 的增量价值主要体现在 far-OOD 场景。如果实验发现大多数 benchmark 属于 near-OOD，co-adaptive retrieval 和 DDRL debiasing 的 marginal gain 可能很小。

**增量价值判断**：co-adaptive retrieval 是最有说服力的增量贡献（问题明确、机制新颖、利用了 Lean 4 独特的结构化错误信息）。Binarize-then-enrich 的增量价值较弱（在 DDRL 和 GDPO 都已存在的前提下，这一步近乎 obvious）。

【前提假设检验】:

核心 claim 的逻辑链中，以下环节是未经验证的假设：

1. **"CriticLean-14B 在 OOD skewed distribution 下仍能保持足够的 precision"**：CriticLeanBench 仅在 balanced 250/250 分布上评估（84.8% accuracy）。在 TTRL 的 OOD 场景下，>90% 的 candidate 可能不正确，critic 的 false positive rate 可能会显著恶化。Proposal 的 Phase 0 calibration 试图验证这一假设，但这也意味着**如果这个假设不成立，整个 pipeline 的基础就会动摇**。这是最关键的风险点。

2. **"Lean 4 的 unknownIdentifier 等 Tier 1 错误在 OOD 域占比足够高（≥40%）以支撑 co-adaptive retrieval"**：AMBER 的 47.3% 来自 DeepSeek-R1 on applied math，但 proposal 使用更小的 formalizer 在不同 OOD 域上。Proposal 承认了这一点（Phase -1 就是为了验证），但如果 Tier 1 比例很低（如 <20%），co-adaptive retrieval 的 core mechanism 会大打折扣。

3. **"co-adaptive retriever 更新不会 destabilize RL training"**：交替优化 retriever 和 formalizer 在理论上可能导致不稳定——retriever 变化改变 input context → formalizer 的 reward landscape 发生 shift → GRPO 的 advantage estimation 受到干扰。Proposal 借鉴 R3 和 Reinforced-IR 的 decoupled optimization，但这些工作是在 text QA 领域验证的，autoformalization 场景的 reward 更加 sparse 和 noisy，是否同样稳定未经验证。

4. **"Binarize-then-enrich 的 DDRL 扩展在 multi-tier reward 场景下能保持 DDRL 的 debiasing 效果"**：DDRL 的理论分析基于 binary reward 的简洁结构（correct/incorrect）。加入 GDPO enrichment layer 后，fixed ±1 advantages 被 BEq bonus 打破，debiasing 的理论保证是否仍然成立是一个开放问题。

【3 维度打分】:

1. **Novelty: 中** — 
   Co-adaptive retrieval exploiting Lean 4's structured error taxonomy 是最强的新颖贡献：没有先前工作在 RL-based autoformalization 过程中对 retriever 做 online adaptation，利用 unknownIdentifier/type mismatch 等结构化错误信号构建 graded contrastive training data 的设计是 domain-specific 且有新意的。这一点与 R3 (NeurIPS 2025) 和 Reinforced-IR (ACL 2025) 在 text QA 上的 co-adaptive retrieval 形成清晰区分——后者不涉及编译器的结构化错误信号。

   但整体而言，proposal 的 novelty 分布不均匀。"Binarize-then-enrich" 的贡献较薄：一旦知道 DDRL 处理 binary rewards、GDPO 处理 multi-reward normalization，将二者组合（先 binarize 使 DDRL 适用，再用 GDPO 对 continuous component 做 enrichment）是一个**几乎 obvious 的工程决策**，缺乏深层 insight。CriticLean 作为 TTRL reward 也是自然的应用延伸（CriticLean 论文本身就在 RL pipeline 中使用了 critic reward）。

   此外，TTRL 应用于 autoformalization 虽然是"首次"，但 Online RL for Autoformalization (Wang et al.) 已经做了 training-time RL for autoformalization with composite rewards，从 training-time 到 test-time 的跨越虽有价值但不构成根本性 novelty 突破。

   **总体判断**：有一个扎实的新贡献点（co-adaptive retrieval with error taxonomy），其余贡献是competent combination work。对于 AAAI，这处于中等水平——不是 trivial incremental，但也达不到 "surprising insight"。

2. **Significance: 中偏强** — 
   Autoformalization 的 OOD generalization 是一个真实且重要的问题。MathAtlas (2026) 显示最佳模型在 MA-Hard 上仅 2.6%，AMBER (2026) 量化了 47.3% 的编译错误来自 identifier hallucination——**问题的重要性和 urgency 是有充分实证支撑的**。

   如果 proposal 的方法在 far-OOD 域（condensed mathematics, algebraic geometry）上实现显著提升，这对 AI for mathematics 社区有实际价值。Co-adaptive retrieval 机制如果成功，可以推广到其他涉及编译器反馈的形式化任务（proof generation, code synthesis）。Binarize-then-enrich 虽然 insight 有限，但作为通用方法论确实有跨领域适用性。

   限制 significance 的因素：autoformalization 仍是一个相对小众的子领域。虽然在 AI for math 热潮中受到更多关注，但与 LLM reasoning、code generation 等热门方向相比，直接受众有限。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。覆盖了 5 个相关研究脉络，引用了 25+ 篇论文，包括最新的 2026 年工作（DDRL, GDPO, MathAtlas, Construction-Verification/AMBER）。关键对比点清晰：
   - 与 FormaRL: 使用 trained critic 而非 LLM consistency，加入 retrieval 和 test-time adaptation
   - 与 Online RL for Autoformalization: test-time 而非 training-time，trained critic 而非 embedding similarity
   - 与 DDR/DRIFT: dynamic co-adaptive 而非 static retrieval
   - 与 DDRL: multi-tier reward 而非 binary
   
   调研中确认的引用（DDR 的 500K 数据集、AMBER 的 47.3% hallucination rate、CriticLean 的 84.8% accuracy、DDRL 的 AIME 结果）均与原始论文一致。差异化定位清晰且准确。唯一的轻微不足是：对 ATLAS (NeurIPS 2025) 和 Monotonic Refinement 的讨论主要作为 reference point，没有深入分析它们的 inference-time refinement 策略是否能部分替代 TTRL 的功能。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty 是中等水平（一个扎实的新贡献 + 若干 obvious combination），这限制了概率的上界——一个审稿人可能会写 "the co-adaptive retrieval idea is interesting, but the binarize-then-enrich and critic integration feel like natural engineering choices rather than research contributions"。Significance 中偏强但受限于子领域的受众规模。Related work 是真正的强项，降低了被 "missing related work" 拒稿的风险。

从 rubric 锚点来看：proposal 有真实的 novelty delta（co-adaptive retrieval with error taxonomy），方向正确，问题重要，但核心发现如果 positive（"co-adaptive retrieval + debiased RL 在 OOD autoformalization 上优于 static retrieval + vanilla GRPO"），审稿人更可能说 "this makes sense, I would have expected retrieval adaptation to help" 而非 "this is surprising"。这将其定位在 25-35% 区间。

上界被 novelty 深度限制：proposal 的创新主要在 combination 层面，单个贡献的 insight 深度有限。下界被 related work 覆盖度和 Phase 0 de-risking 设计支撑：这是一个 well-crafted proposal，不太可能因为"方向不对"或"遗漏关键工作"而被直接拒绝。

【主要风险】:
1. **"Kitchen sink" / combination paper 质疑**：Proposal 集成了 4+ 个现有技术（TTRL, DDRL, GDPO, co-adaptive retrieval, CriticLean, progressive curriculum），审稿人可能认为没有任何一个单独贡献有足够的深度，整体是 "competent systems work" 而非 "research contribution"。Binarize-then-enrich 尤其容易被认为 trivial。
2. **核心前提（CriticLean 在 OOD skewed distribution 下的可靠性）未经验证**：如果 Phase 0 calibration 发现 critic precision 在 skewed distribution 下显著低于 80%，整个 pipeline 的 reward signal 基础就会受到质疑。即使 proposal 设计了 confidence gating 作为 fallback，审稿人可能会认为这是在 patch 一个根本性的 weakness。
```

Sources:
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)
- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327)
- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242)
- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181)
- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)
- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)
- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)
- [Construction-Verification/AMBER Benchmark](https://arxiv.org/abs/2602.01291)
- [R3: Optimizing Retrieval for RAG via Reinforcement Learning](https://arxiv.org/abs/2510.24652)
- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)
- [NVIDIA GDPO Official Page](https://nvlabs.github.io/GDPO/)
- [Kimina-Prover: Test-time RL on Formal Reasoning](https://huggingface.co/blog/AI-MO/kimina-prover)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ee1fbb9-4f8a-4394-a7ba-6c34192cbbbd",
  "isSidechain": false,
  "requestId": "req_011CbUQ6WwUtMh1tiGvfoUup",
  "type": "assistant",
  "uuid": "17a81aac-3bd5-4e48-906d-0fba3766d65d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtNZiLaJPGiLySbY97H3PF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 32651,
      "output_tokens": 7221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 643,
          "output_tokens": 7221,
          "cache_read_input_tokens": 32651,
          "cache_creation_input_tokens": 1677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1677
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "17a81aac-3bd5-4e48-906d-0fba3766d65d",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Critic-guided test-time retrieval-augmented autoformalization",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "17a81aac-3bd5-4e48-906d-0fba3766d65d",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Critic-guided test-time retrieval-augmented autoformalization",
  "sessionId": "6636e8e6-7680-4dcb-9644-3680077f6940"
}
```

---
