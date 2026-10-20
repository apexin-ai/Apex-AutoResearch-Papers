# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # TTRA: Critic-Guided Test-Time Ret

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/29610d22-ae32-421a-8d2b-c4122dd5c431.jsonl`
- **Structured JSON:** [`f163ff232094d36e11ca.json`](../../sessions/f1/f163ff232094d36e11ca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:58:00.403Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:58:00.403Z",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization\n\n## Core Problem\n\nCurrent autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in multi-tier reward settings; and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation.\n\nA key structural asymmetry motivates our approach: in informal math reasoning, TTRL obtains only binary correct/incorrect signals with no information about *why* a solution failed or *what knowledge is missing*—and binary rewards create a fundamental degeneracy for policy gradient methods, leading to diversity collapse (Dymetman, arXiv:2605.02375). In contrast, Lean 4's compiler produces machine-parseable error messages that precisely identify missing identifiers, type mismatches, and unresolved typeclass instances—constituting a graded hierarchy of structured feedback signals. Critically, these signals are not merely \"richer rewards\": when a compilation error reports `unknownIdentifier \"Finset.sum_bij\"`, it provides an oracle-quality, token-level retrieval training signal that directly specifies which Mathlib dependency is needed. Such signals are unavailable during pre-training or SFT (no compilation feedback), discarded by inference-time search methods like FormalEvolve (which uses only compile success/failure), and unexploited by static retrieval pipelines like Aria (whose retriever cannot adapt). Only during test-time RL can these structured error signals be continuously collected and used to co-adapt the retriever—making co-adaptive retrieval an emergent capability uniquely enabled by TTRL in formal language settings.\n\nFor domains where model performance is extremely low (MathAtlas MA-Hard: 2.6%), inference-time scaling alone is insufficient: the fixed model's output space may not contain correct formalizations for truly OOD domains, so no amount of sampling can find what the model cannot generate. Weight adaptation is necessary, and it produces compounding improvement—better formalizations yield more informative compilation errors, which improve the retriever, which enables even better formalizations in subsequent rounds.\n\n## Research Opportunity\n\nFour independently validated capabilities have never been combined, and their integration is enabled by the structured feedback properties unique to formal languages.\n\n(1) **Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode.** R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv:2601.11443, Jan 2026) shows test-time retrieval adaptation via self-supervised prediction. The prevalence of identifier hallucination is established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math stem from hallucination of non-existent theorems/definitions. DDR (arXiv:2511.11990) quantifies Hall_m=0.21-0.39 across frontier LLMs, reduced to <0.02 with retrieval. The RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as a primary error class. MathAtlas (arXiv:2605.14061, May 2026) shows a 66% advantage for Mathlib-grounded definitions (27.9% vs 16.8%, p<0.001). Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL—where Lean's structured error taxonomy provides graded, machine-parseable signals for retriever training.\n\n(2) **TTRL with debiasing has advanced but remains limited to binary rewards in informal settings.** DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed ±1 advantages, and consensus-based off-policy refinement (19.0% relative improvement over ETMR on AIME 2024; 4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B), but assumes binary rewards with 'more expressive advantage formulations' left as future work. GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization but does not address debiasing. T³RL (arXiv:2603.02203, Mar 2026) introduces tool-verified rewards into TTRL, using code execution output to upweight verified rollouts—but collapses all tool feedback into a single binary bit (verified/unverified), discarding the internal structure of tool output. SCOPE (arXiv:2512.15146, Dec 2025) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, but remains within the homogeneous binary-reward paradigm. The combination of DDRL's debiasing with GDPO's multi-reward normalization for heterogeneous reward components (hard binary gate + noisy soft critic + drifting population statistic) has not been attempted.\n\n(3) **CriticLean provides the missing semantic reward signal.** CriticLeanGPT-14B-RL (arXiv:2507.06181, July 2025) achieves 84.8% accuracy on balanced CriticLeanBench (87.0% for 32B), but CriticLeanBench's 250/250 balanced distribution differs from OOD TTRL's heavily skewed distribution (<10% compilable). This distributional shift gap motivates our Phase 0 calibration protocol.\n\n(4) **Online RL for autoformalization validated at training time only.** Wang et al. (NeurIPS 2025 MAR Workshop) achieves TC1: 17.29%→26.01% on RLMEval using GRPO with BEq + embedding rewards, but operates at training time on in-distribution problems without retrieval, test-time adaptation, or a trained semantic critic.\n\nRecent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.\n\n## Research Landscape\n\n**(1) RL for autoformalization.** FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards (pass@1: 4%→26% on ProofNet). Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with BEq + embedding similarity (TC1: 17.29%→26.01%, TC50: 76.41%→85.46% on RLMEval)—closest prior work but training-time, no retrieval, no test-time adaptation. ReForm (arXiv:2510.24592) applies PBSO position-aware RL rewards for reflective autoformalization; ReForm-8B (Qwen3-8B) achieves +18.0pp average improvement.\n\n**(2) Semantic critics and iterative refinement.** CriticLean (July 2025) introduces CriticLeanGPT (32B-RL: 87.0%, 14B-RL: 84.8% on balanced CriticLeanBench). ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO. Monotonic Refinement achieves 90.27% on miniF2F through multi-model ensemble orchestration. These cannot adapt model weights to new domains.\n\n**(3) Debiased RL, multi-reward optimization, and TTRL reward improvements.** DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification exclusively with binary rewards; GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward normalization. Binary Rewards and RL (Dymetman, arXiv:2605.02375, May 2026) proves binary rewards create fundamental degeneracy (diversity collapse). T³RL (arXiv:2603.02203, Mar 2026) introduces external tool verification into TTRL, upweighting verified rollouts via verification-aware voting—but treats tool output as a single binary signal (verified/unverified), discarding the structured content of tool feedback. SCOPE (arXiv:2512.15146) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, remaining within the homogeneous binary-reward paradigm. All these improvements assume homogeneous reward signals. TTRA addresses a qualitatively different problem: heterogeneous reward components (hard compilation gate, noisy critic signal, policy-drifting BEq statistic) requiring a two-layer binarize-then-enrich adaptation.\n\n**(4) Retrieval-augmented autoformalization and co-adaptive retrieval.** Aria (ICLR 2026, arXiv:2510.04520) achieves ProofNet 91.6% compilation / 68.5% accuracy and 42.9% on homological conjectures (vs. 0% for all others) via dependency graph + iterative formalization + AriaScorer—current frontier of retrieval-augmented autoformalization, but a fixed inference pipeline: retriever does not adapt to formalizer's evolving behavior and model weights are not updated. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF. DDR builds a 500K-sample dataset (Hall_m reduced from 0.21-0.39 to <0.02). CRAMF indexes 26K+ Mathlib definitions. ProofBridge (ICLR 2026, arXiv:2510.15681) uses joint embeddings + retrieval-augmented fine-tuning. On co-adaptive retrieval: R3 (NeurIPS 2025, arXiv:2510.24652) optimizes RAG retrieval via reinforced contrastive learning; Reinforced-IR (ACL 2025) alternates RLRF/RLGF; TTARAG (arXiv:2601.11443) demonstrates test-time retrieval adaptation. None applied to autoformalization or Lean 4.\n\n**(5) Test-time compute for autoformalization.** FormalEvolve (arXiv:2603.19828, Mar 2026) formulates autoformalization as budgeted evolutionary search (SH@100=58.0% CombiBench, 84.9% ProofNet) using LLM-driven mutation/crossover with AST rewrites. This is orthogonal to TTRA: FormalEvolve searches a fixed model's output space without weight adaptation or retriever co-adaptation, discarding compilation error structure. TEMPO (arXiv:2604.19295, Apr 2026) formalizes test-time training as EM (policy refinement = M-step, critic recalibration = E-step), proving that omitting recalibration leads to ELBO degradation and diversity collapse—a conceptual parallel to TTRA's dual-loop where omitting retriever co-adaptation (= static retrieval TTRL) accumulates retriever-formalizer distribution mismatch.\n\n**(6) Error analysis and identifier hallucination.** The AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are identifier hallucination (32.7% competence, 15.2% incomplete, 4.8% syntax). RAutoformalizer (ICLR 2025 Spotlight) categorizes errors into 'Hallucination' vs 'Others'. MathAtlas (arXiv:2605.14061) introduces 52K graduate-level problems (best: 2.6% on MA-Hard).\n\nAfter exhaustive search through May 2026, no work combines co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, a calibrated semantic critic with distributional shift analysis, principled adaptation of binary-reward debiased RL to heterogeneous multi-tier rewards, and test-time adaptation on unlabeled OOD domains. Existing retrieval methods (Aria, DRIFT, DDR) use static retrievers; existing RL methods (FormaRL, Wang et al., ReForm) operate at training time; existing test-time methods (FormalEvolve) search without learning; existing TTRL improvements (T³RL, SCOPE, DDRL) assume homogeneous binary rewards.\n\n## Proposed Approach\n\nWe propose TTRA (Test-Time Retrieval-Augmented autoformalization), making TTRL viable for autoformalization through three technical innovations unified by a single insight: formal languages' structured compilation feedback creates a graded hierarchy of adaptation signals unavailable in informal reasoning, enabling co-adaptive test-time learning as a new scaling axis for formal mathematics—complementing training-time compute (more data, larger models) and inference-time compute (more samples, longer search). Drawing a conceptual parallel with TEMPO's EM formalization of TTT, TTRA's dual-loop design ensures the retriever co-adapts with the formalizer (analogous to not omitting the E-step), preventing the retriever-formalizer distribution mismatch that would degrade a static-retrieval TTRL.\n\n**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Quantify Lean 4 error taxonomy coverage on OOD domains. Compile 500 candidate formalizations on Con-NF and 500 on MathAtlas MA-Hard, classify errors into: Tier 1 (direct identifier: `lean.unknownIdentifier`, `unknown namespace`), Tier 2 (type-based: `type mismatch`, `failed to synthesize instance`), Tier 3 (indirect: tactic/elaboration/syntax errors). Thresholds: Tier 1 ≥40% → co-adaptive retrieval well-supported; 20-40% → rely on Tier 1+2; <20% → fall back to Tier 2 with type-signature matching. Prior evidence strongly supports ≥40% (AMBER: 47.3%; DDR: Hall_m=0.21-0.39; RAutoformalizer treats 'Hallucination' as primary class; CRAMF documents systematic fabrication). Phase -1 validates on our specific model/domain. Simultaneously verify MathAtlas MA-Hard gold formalization coverage; if <50%, downgrade to secondary benchmark and activate IndiMathBench (arXiv:2512.00997) as contingency OOD benchmark. Resource: ~8 A100-hours generation, ~10 CPU-hours parsing.\n\n**Phase 0 — Minimal Pilot with Critic Calibration (De-risking).** FormaRL's GRPO pipeline with CriticLean-14B replacing LLM-consistency reward. 200 Con-NF + 200 FormalMATH number theory problems. Primary hypothesis: ≥3pp BEq@1 over compilation-only GRPO on Con-NF. Critic calibration under distributional shift: measure precision/recall separately on skewed distribution (<10% compilable); report calibration curves; if precision <80%, introduce confidence gating >0.8. Go/no-go: proceed only if primary hypothesis confirmed AND precision ≥80%. Additionally, establish critic calibration monitoring protocol: during subsequent TTRL phases, checkpoint critic precision every ~100 GRPO steps; if precision drops >10pp from Phase 0 baseline, adjust confidence threshold (periodic recalibration, motivated by TEMPO's finding that reward signal drift without recalibration leads to performance plateaus). Resource: ~50 A100-hours, 2-3 weeks.\n\n**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune Qwen3-8B using DDR's 500K-sample dataset and GRPO with R(y, x) = r_compile × (α·r_critic + β·r_beq). r_compile ∈ {0,1} (Kimina Lean Server, 128 parallel workers); r_critic ∈ {0,1} (CriticLeanGPT-Qwen3-14B-RL, gated by Phase 0 threshold); r_beq ∈ [0,1] (BEq consensus density). α=0.7, β=0.3. Fallback: when <4 of K=32 compile, R = r_compile × r_critic.\n\n**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever (DDR-style dense encoder) is explicitly updated during TTRL. This exploits Lean 4's unique structural property: compilation errors provide oracle-quality, token-level retrieval training signals that directly specify which Mathlib dependencies are needed—signals unavailable during pre-training, discarded by inference-time search, and unexploited by static retrieval pipelines.\n\n  Loop 1 — Formalizer GRPO (every step): K=32 candidates, compile, multi-tier rewards, debiased GRPO.\n\n  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Graded error hierarchy:\n    (a) Tier 1 (highest confidence): `lean.unknownIdentifier` names missing constant → hard negatives from retrieved set; constant from CRAMF/DDR index = positive. `unknown namespace` → coarser module-level positive.\n    (b) Tier 2 (moderate): `type mismatch` → type signatures matched against Mathlib type index, 0.5× weight. `failed to synthesize instance` → typeclass instances as positives.\n    (c) Tier 3: tactic/elaboration/syntax → negatives only.\n    (d) Compilation success → all retrieved dependencies in compiled output = confirmed positives.\n    (e) Weighted InfoNCE: L = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), w_k = 1.0 (Tier 1/confirmed), 0.5 (Tier 2), τ=0.07.\n    (f) Decoupled optimization (per R3 and Reinforced-IR): retriever gradient does not flow through formalizer. FAISS rebuild after each update.\n\n  Signal density: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle.\n\n**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** Autoformalization's reward components are fundamentally heterogeneous: compilation is a hard binary gate (non-negotiable), the critic is a noisy soft signal (calibrated but imperfect), BEq is a population statistic (drifts with policy). This heterogeneity distinguishes TTRA from all existing TTRL reward improvements (DDRL, T³RL, SCOPE, GDPO), which assume homogeneous reward signals. Neither DDRL alone (cannot handle multi-tier) nor GDPO alone (does not address spurious amplification) suffices:\n\n  (a) Binarization layer: r_accept = I(r_compile=1 AND r_critic=1). Balanced sampling (exclude 30-70% ambiguity zone per DDRL). Fixed advantages: +1 (accepted), -1 (rejected). Consensus off-policy refinement: M=128, rejection-sample >80% acceptance, SFT 5 epochs.\n  (b) GDPO-style enrichment: among accepted candidates, per-reward decoupled normalization for BEq. Additive bonus δ·norm(r_beq) to +1 advantage, δ=0.3.\n\n**Phase 4 — Progressive Domain Curriculum.** (a) Near-distribution warm-start: compilation ≥40%, critic approval ≥60%, BEq@32 ≥3pp above baseline. Timeout: 500 steps. (b) Retrieval bootstrapping: Tier 1/2 errors feed retriever updates. Transition: recall@10 ≥30%, compilation ≥25%. Early transition: plateau <2pp over 200 steps. (c) Far-OOD: algebraic geometry, condensed mathematics, MathAtlas MA-Hard with adaptive fallback.\n\n**Contribution Floor Analysis.** (1) Co-adaptive retrieval + CriticLean TTRL alone: first co-adaptive retrieval for autoformalization + first TTRL for formal math with calibrated critic. (2) Binarize-then-enrich alone: addresses DDRL's explicit future work on multi-tier rewards. (3) Curriculum: droppable. (4) Essential floor: CriticLean TTRL outperforms compilation-only (Phase 0 gate) AND ≥1 of co-adaptive retrieval / binarize-then-enrich shows statistically significant improvement.\n\n**Evaluation.**\n\n  *Benchmarks:* In-distribution: miniF2F-test (244), ProofNet (~371). Multi-domain: FormalMATH (5,560). OOD stress tests: Con-NF, CombiBench, MathAtlas MA-Hard (700 entities, best: 2.6%; contingency: IndiMathBench if gold coverage <50%).\n\n  *Metrics:* BEq@K, BEq+@K (per DRIFT), pass@K (K=1,32), compilation@K on all benchmarks. GTED (arXiv:2507.07399, continuous [0,1] similarity with better precision-recall balance than BEq) on OOD benchmarks. Hall_m (DDR's hallucination rate) in retriever ablation. Human evaluation: 100-150 samples on Con-NF + 200 samples on MathAtlas MA-Hard (inter-annotator agreement reported).\n\n  *Same-scale primary baselines (~7-8B):* (1) FormaRL (Qwen2.5-Coder-7B, COLM 2025); (2) Online RL for Autoformalization (Wang et al., faithfully reimplemented if code unavailable); (3) DRIFT with Qwen3-8B (ICLR 2026); (4) Aria (ICLR 2026, reimplemented on shared benchmarks or reported numbers annotated); (5) StepFun-Formalizer-7B (AAAI 2026, open-source); (6) ReForm-8B (Qwen3-8B, arXiv:2510.24592); (7) compilation-only TTRL and critic-only TTRL ablations.\n\n  *Cross-paradigm reference:* FormalEvolve (arXiv:2603.19828, reported SH@100 on CombiBench/ProofNet).\n\n  *Compute-matched baseline:* Best-of-N (matched FLOPs) + CriticLean filtering: allocate equivalent test-time compute to sampling more candidates from base formalizer, filter with CriticLean-14B, report BEq@1 and compilation@1. Directly tests whether TTRA's weight adaptation provides value beyond inference-time scaling.\n\n  *Ablations:* (a) Standard GRPO vs. DDRL vs. binarize-then-enrich (component-wise); (b) frozen vs. co-adaptive retriever; (c) Tier 1-only vs. Tier 1+2 vs. all-tier error signals; (d) no curriculum vs. progressive; (e) CriticLean-14B reward vs. embedding-based similarity reward (isolating trained critic value).\n\n  *Sensitivity:* N_ret ∈ {25, 50, 100}; δ ∈ {0.0, 0.1, 0.3, 0.5} (δ=0.0 = pure DDRL); ambiguity zone ∈ {[20%-80%], [30%-70%], [40%-60%]}; critic confidence threshold ∈ {0.6, 0.7, 0.8, 0.9}; K ∈ {16, 32, 64} (test-time compute scaling behavior).\n\n  *Cross-scale references:* ATF-32B, ATLAS (NeurIPS 2025), Monotonic Refinement (multi-model ensemble). All tables annotate scale and compute.\n\n  *Statistical rigor:* Key comparisons ≥3 seeds, mean ± std, bootstrap CI (p<0.05).\n\n## Detailed Description\n\nTTRA makes TTRL viable for autoformalization by exploiting a structural asymmetry: Lean 4's compiler provides oracle-quality, token-level feedback (identifier names, type signatures, typeclass requirements) that serves simultaneously as retriever training signal, multi-tier reward components, and domain adaptation indicators—signals unavailable in informal reasoning and unexploited by existing methods. The dual-loop architecture co-adapts the retriever during test-time RL via weighted InfoNCE over Lean 4's error hierarchy, addressing the limitation that static retrievers (Aria, DRIFT, DDR) cannot track formalizer evolution. CriticLean-14B integration includes distributional shift calibration and periodic drift monitoring (motivated by TEMPO's EM analysis of reward signal degradation). Binarize-then-enrich addresses the specific gap between DDRL (binary debiasing) and GDPO (multi-reward normalization) for formal verification's heterogeneous reward landscape—a qualitatively different problem from the homogeneous-reward improvements in T³RL and SCOPE. Compute-matched evaluation against best-of-N + critic filtering directly tests whether weight adaptation provides value beyond inference-time scaling. The framework positions test-time learning as a third scaling axis for formal mathematics alongside training-time and inference-time compute.\n\n## Key References\n\n- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)\n- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)\n- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, NVIDIA, January 2026)\n- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv:2507.06181, ByteDance/Nanjing)\n- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)\n- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv:2510.24652)\n- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)\n- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv:2601.11443, January 2026)\n- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv:2602.01291, February 2026)\n- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)\n- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\n- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)\n- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)\n- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\n- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)\n- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv:2511.11990)\n- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)\n- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)\n- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)\n- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\n- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv:2505.02735)\n- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)\n- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\n- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026, arXiv:2510.04520)\n- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026, arXiv:2510.15681)\n- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv:2510.24592)\n- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv:2512.00997, Microsoft Research)\n- FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv:2603.19828, March 2026)\n- Binary Rewards and Reinforcement Learning: Fundamental Challenges (Dymetman, arXiv:2605.02375, May 2026)\n- TEMPO: Scaling Test-time Training for Large Reasoning Models (arXiv:2604.19295, April 2026)\n- T³RL: Tool Verification for Test-Time Reinforcement Learning (arXiv:2603.02203, March 2026)\n- SCOPE: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning (arXiv:2512.15146, December 2025)\n- GTED: Generalized Tree Edit Distance: A Faithful Evaluation Metric for Statement Autoformalization (arXiv:2507.07399)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1400-1900 A100-80GB hours (Phase -1 micro-analysis + MathAtlas coverage: ~10h; Phase 0 pilot + calibration: ~50h; Phase 1 base GRPO: ~300h; DDR retriever + co-adaptive updates: ~100h; Phase 4 progressive TTRL + ablations: ~400h; CriticLean-14B inference all phases: ~200-300h; N_ret/δ/ambiguity/critic-threshold/K sensitivity: ~100h; baseline evaluation (Aria reimpl + StepFun + ReForm): ~100-120h; compute-matched best-of-N baseline: ~30h; CriticLean vs embedding ablation: ~25h; multi-seed (3 seeds × key ablations): ~200h; human eval annotation: ~60-80h; miniF2F/ProofNet + remaining eval: ~80h) + 15,000-20,000 CPU-hours Lean verification (Kimina Lean Server), timeline: 14-18 weeks (0.5 wk Phase -1; 2-3 wk Phase 0 + go/no-go; 3 wk Phase 1; 2 wk retriever infrastructure; 4 wk TTRL experiments; 3 wk ablations + sensitivity + multi-seed; 2 wk writing), estimated_gpu_cost: $2,800-$4,700 + $750-$1,000 CPU + ~$1,500-$2,500 human annotation. GPU architecture: policy (8B) + ref (8B) on 4×A100 tensor parallel, CriticLean-14B on dedicated 2×A100 with vLLM batch inference, retriever + FAISS on CPU/1×A100; async pipeline.\n- **human_in_loop**: gpu_hours: 1100-1500 A100-80GB hours (~25% reduction), timeline: 11-14 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,200-$3,700 + $600-$800 CPU + ~$1,200-$2,000 annotation\n- **auto_research**: gpu_hours: 2000-2700 A100-80GB hours (full sweep), timeline: 8-11 weeks, claude_api_cost: $800-$1,200, estimated_gpu_cost: $4,000-$6,700 + $1,000-$1,350 CPU + ~$1,500-$2,500 annotation, speed_bottleneck: Lean 4 compilation (~3.65s/statement warm cache, ~0.10s amortized at 64 workers). CriticLean-14B ~0.5s/candidate (→~0.1-0.2s with vLLM). Retriever co-adaptation ~15 min/cycle (re-encode 26K constants, rebuild FAISS)."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:58:00.444Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:58:00.444Z",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-28T05:58:00.549Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization

## Core Problem

Current autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in multi-tier reward settings; and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation.

A key structural asymmetry motivates our approach: in informal math reasoning, TTRL obtains only binary correct/incorrect signals with no information about *why* a solution failed or *what knowledge is missing*—and binary rewards create a fundamental degeneracy for policy gradient methods, leading to diversity collapse (Dymetman, arXiv:2605.02375). In contrast, Lean 4's compiler produces machine-parseable error messages that precisely identify missing identifiers, type mismatches, and unresolved typeclass instances—constituting a graded hierarchy of structured feedback signals. Critically, these signals are not merely "richer rewards": when a compilation error reports `unknownIdentifier "Finset.sum_bij"`, it provides an oracle-quality, token-level retrieval training signal that directly specifies which Mathlib dependency is needed. Such signals are unavailable during pre-training or SFT (no compilation feedback), discarded by inference-time search methods like FormalEvolve (which uses only compile success/failure), and unexploited by static retrieval pipelines like Aria (whose retriever cannot adapt). Only during test-time RL can these structured error signals be continuously collected and used to co-adapt the retriever—making co-adaptive retrieval an emergent capability uniquely enabled by TTRL in formal language settings.

For domains where model performance is extremely low (MathAtlas MA-Hard: 2.6%), inference-time scaling alone is insufficient: the fixed model's output space may not contain correct formalizations for truly OOD domains, so no amount of sampling can find what the model cannot generate. Weight adaptation is necessary, and it produces compounding improvement—better formalizations yield more informative compilation errors, which improve the retriever, which enables even better formalizations in subsequent rounds.

## Research Opportunity

Four independently validated capabilities have never been combined, and their integration is enabled by the structured feedback properties unique to formal languages.

(1) **Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode.** R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv:2601.11443, Jan 2026) shows test-time retrieval adaptation via self-supervised prediction. The prevalence of identifier hallucination is established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math stem from hallucination of non-existent theorems/definitions. DDR (arXiv:2511.11990) quantifies Hall_m=0.21-0.39 across frontier LLMs, reduced to <0.02 with retrieval. The RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as a primary error class. MathAtlas (arXiv:2605.14061, May 2026) shows a 66% advantage for Mathlib-grounded definitions (27.9% vs 16.8%, p<0.001). Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL—where Lean's structured error taxonomy provides graded, machine-parseable signals for retriever training.

(2) **TTRL with debiasing has advanced but remains limited to binary rewards in informal settings.** DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed ±1 advantages, and consensus-based off-policy refinement (19.0% relative improvement over ETMR on AIME 2024; 4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B), but assumes binary rewards with 'more expressive advantage formulations' left as future work. GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization but does not address debiasing. T³RL (arXiv:2603.02203, Mar 2026) introduces tool-verified rewards into TTRL, using code execution output to upweight verified rollouts—but collapses all tool feedback into a single binary bit (verified/unverified), discarding the internal structure of tool output. SCOPE (arXiv:2512.15146, Dec 2025) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, but remains within the homogeneous binary-reward paradigm. The combination of DDRL's debiasing with GDPO's multi-reward normalization for heterogeneous reward components (hard binary gate + noisy soft critic + drifting population statistic) has not been attempted.

(3) **CriticLean provides the missing semantic reward signal.** CriticLeanGPT-14B-RL (arXiv:2507.06181, July 2025) achieves 84.8% accuracy on balanced CriticLeanBench (87.0% for 32B), but CriticLeanBench's 250/250 balanced distribution differs from OOD TTRL's heavily skewed distribution (<10% compilable). This distributional shift gap motivates our Phase 0 calibration protocol.

(4) **Online RL for autoformalization validated at training time only.** Wang et al. (NeurIPS 2025 MAR Workshop) achieves TC1: 17.29%→26.01% on RLMEval using GRPO with BEq + embedding rewards, but operates at training time on in-distribution problems without retrieval, test-time adaptation, or a trained semantic critic.

Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.

## Research Landscape

**(1) RL for autoformalization.** FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards (pass@1: 4%→26% on ProofNet). Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with BEq + embedding similarity (TC1: 17.29%→26.01%, TC50: 76.41%→85.46% on RLMEval)—closest prior work but training-time, no retrieval, no test-time adaptation. ReForm (arXiv:2510.24592) applies PBSO position-aware RL rewards for reflective autoformalization; ReForm-8B (Qwen3-8B) achieves +18.0pp average improvement.

**(2) Semantic critics and iterative refinement.** CriticLean (July 2025) introduces CriticLeanGPT (32B-RL: 87.0%, 14B-RL: 84.8% on balanced CriticLeanBench). ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO. Monotonic Refinement achieves 90.27% on miniF2F through multi-model ensemble orchestration. These cannot adapt model weights to new domains.

**(3) Debiased RL, multi-reward optimization, and TTRL reward improvements.** DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification exclusively with binary rewards; GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward normalization. Binary Rewards and RL (Dymetman, arXiv:2605.02375, May 2026) proves binary rewards create fundamental degeneracy (diversity collapse). T³RL (arXiv:2603.02203, Mar 2026) introduces external tool verification into TTRL, upweighting verified rollouts via verification-aware voting—but treats tool output as a single binary signal (verified/unverified), discarding the structured content of tool feedback. SCOPE (arXiv:2512.15146) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, remaining within the homogeneous binary-reward paradigm. All these improvements assume homogeneous reward signals. TTRA addresses a qualitatively different problem: heterogeneous reward components (hard compilation gate, noisy critic signal, policy-drifting BEq statistic) requiring a two-layer binarize-then-enrich adaptation.

**(4) Retrieval-augmented autoformalization and co-adaptive retrieval.** Aria (ICLR 2026, arXiv:2510.04520) achieves ProofNet 91.6% compilation / 68.5% accuracy and 42.9% on homological conjectures (vs. 0% for all others) via dependency graph + iterative formalization + AriaScorer—current frontier of retrieval-augmented autoformalization, but a fixed inference pipeline: retriever does not adapt to formalizer's evolving behavior and model weights are not updated. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF. DDR builds a 500K-sample dataset (Hall_m reduced from 0.21-0.39 to <0.02). CRAMF indexes 26K+ Mathlib definitions. ProofBridge (ICLR 2026, arXiv:2510.15681) uses joint embeddings + retrieval-augmented fine-tuning. On co-adaptive retrieval: R3 (NeurIPS 2025, arXiv:2510.24652) optimizes RAG retrieval via reinforced contrastive learning; Reinforced-IR (ACL 2025) alternates RLRF/RLGF; TTARAG (arXiv:2601.11443) demonstrates test-time retrieval adaptation. None applied to autoformalization or Lean 4.

**(5) Test-time compute for autoformalization.** FormalEvolve (arXiv:2603.19828, Mar 2026) formulates autoformalization as budgeted evolutionary search (SH@100=58.0% CombiBench, 84.9% ProofNet) using LLM-driven mutation/crossover with AST rewrites. This is orthogonal to TTRA: FormalEvolve searches a fixed model's output space without weight adaptation or retriever co-adaptation, discarding compilation error structure. TEMPO (arXiv:2604.19295, Apr 2026) formalizes test-time training as EM (policy refinement = M-step, critic recalibration = E-step), proving that omitting recalibration leads to ELBO degradation and diversity collapse—a conceptual parallel to TTRA's dual-loop where omitting retriever co-adaptation (= static retrieval TTRL) accumulates retriever-formalizer distribution mismatch.

**(6) Error analysis and identifier hallucination.** The AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are identifier hallucination (32.7% competence, 15.2% incomplete, 4.8% syntax). RAutoformalizer (ICLR 2025 Spotlight) categorizes errors into 'Hallucination' vs 'Others'. MathAtlas (arXiv:2605.14061) introduces 52K graduate-level problems (best: 2.6% on MA-Hard).

After exhaustive search through May 2026, no work combines co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, a calibrated semantic critic with distributional shift analysis, principled adaptation of binary-reward debiased RL to heterogeneous multi-tier rewards, and test-time adaptation on unlabeled OOD domains. Existing retrieval methods (Aria, DRIFT, DDR) use static retrievers; existing RL methods (FormaRL, Wang et al., ReForm) operate at training time; existing test-time methods (FormalEvolve) search without learning; existing TTRL improvements (T³RL, SCOPE, DDRL) assume homogeneous binary rewards.

## Proposed Approach

We propose TTRA (Test-Time Retrieval-Augmented autoformalization), making TTRL viable for autoformalization through three technical innovations unified by a single insight: formal languages' structured compilation feedback creates a graded hierarchy of adaptation signals unavailable in informal reasoning, enabling co-adaptive test-time learning as a new scaling axis for formal mathematics—complementing training-time compute (more data, larger models) and inference-time compute (more samples, longer search). Drawing a conceptual parallel with TEMPO's EM formalization of TTT, TTRA's dual-loop design ensures the retriever co-adapts with the formalizer (analogous to not omitting the E-step), preventing the retriever-formalizer distribution mismatch that would degrade a static-retrieval TTRL.

**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Quantify Lean 4 error taxonomy coverage on OOD domains. Compile 500 candidate formalizations on Con-NF and 500 on MathAtlas MA-Hard, classify errors into: Tier 1 (direct identifier: `lean.unknownIdentifier`, `unknown namespace`), Tier 2 (type-based: `type mismatch`, `failed to synthesize instance`), Tier 3 (indirect: tactic/elaboration/syntax errors). Thresholds: Tier 1 ≥40% → co-adaptive retrieval well-supported; 20-40% → rely on Tier 1+2; <20% → fall back to Tier 2 with type-signature matching. Prior evidence strongly supports ≥40% (AMBER: 47.3%; DDR: Hall_m=0.21-0.39; RAutoformalizer treats 'Hallucination' as primary class; CRAMF documents systematic fabrication). Phase -1 validates on our specific model/domain. Simultaneously verify MathAtlas MA-Hard gold formalization coverage; if <50%, downgrade to secondary benchmark and activate IndiMathBench (arXiv:2512.00997) as contingency OOD benchmark. Resource: ~8 A100-hours generation, ~10 CPU-hours parsing.

**Phase 0 — Minimal Pilot with Critic Calibration (De-risking).** FormaRL's GRPO pipeline with CriticLean-14B replacing LLM-consistency reward. 200 Con-NF + 200 FormalMATH number theory problems. Primary hypothesis: ≥3pp BEq@1 over compilation-only GRPO on Con-NF. Critic calibration under distributional shift: measure precision/recall separately on skewed distribution (<10% compilable); report calibration curves; if precision <80%, introduce confidence gating >0.8. Go/no-go: proceed only if primary hypothesis confirmed AND precision ≥80%. Additionally, establish critic calibration monitoring protocol: during subsequent TTRL phases, checkpoint critic precision every ~100 GRPO steps; if precision drops >10pp from Phase 0 baseline, adjust confidence threshold (periodic recalibration, motivated by TEMPO's finding that reward signal drift without recalibration leads to performance plateaus). Resource: ~50 A100-hours, 2-3 weeks.

**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune Qwen3-8B using DDR's 500K-sample dataset and GRPO with R(y, x) = r_compile × (α·r_critic + β·r_beq). r_compile ∈ {0,1} (Kimina Lean Server, 128 parallel workers); r_critic ∈ {0,1} (CriticLeanGPT-Qwen3-14B-RL, gated by Phase 0 threshold); r_beq ∈ [0,1] (BEq consensus density). α=0.7, β=0.3. Fallback: when <4 of K=32 compile, R = r_compile × r_critic.

**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever (DDR-style dense encoder) is explicitly updated during TTRL. This exploits Lean 4's unique structural property: compilation errors provide oracle-quality, token-level retrieval training signals that directly specify which Mathlib dependencies are needed—signals unavailable during pre-training, discarded by inference-time search, and unexploited by static retrieval pipelines.

  Loop 1 — Formalizer GRPO (every step): K=32 candidates, compile, multi-tier rewards, debiased GRPO.

  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Graded error hierarchy:
    (a) Tier 1 (highest confidence): `lean.unknownIdentifier` names missing constant → hard negatives from retrieved set; constant from CRAMF/DDR index = positive. `unknown namespace` → coarser module-level positive.
    (b) Tier 2 (moderate): `type mismatch` → type signatures matched against Mathlib type index, 0.5× weight. `failed to synthesize instance` → typeclass instances as positives.
    (c) Tier 3: tactic/elaboration/syntax → negatives only.
    (d) Compilation success → all retrieved dependencies in compiled output = confirmed positives.
    (e) Weighted InfoNCE: L = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), w_k = 1.0 (Tier 1/confirmed), 0.5 (Tier 2), τ=0.07.
    (f) Decoupled optimization (per R3 and Reinforced-IR): retriever gradient does not flow through formalizer. FAISS rebuild after each update.

  Signal density: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle.

**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** Autoformalization's reward components are fundamentally heterogeneous: compilation is a hard binary gate (non-negotiable), the critic is a noisy soft signal (calibrated but imperfect), BEq is a population statistic (drifts with policy). This heterogeneity distinguishes TTRA from all existing TTRL reward improvements (DDRL, T³RL, SCOPE, GDPO), which assume homogeneous reward signals. Neither DDRL alone (cannot handle multi-tier) nor GDPO alone (does not address spurious amplification) suffices:

  (a) Binarization layer: r_accept = I(r_compile=1 AND r_critic=1). Balanced sampling (exclude 30-70% ambiguity zone per DDRL). Fixed advantages: +1 (accepted), -1 (rejected). Consensus off-policy refinement: M=128, rejection-sample >80% acceptance, SFT 5 epochs.
  (b) GDPO-style enrichment: among accepted candidates, per-reward decoupled normalization for BEq. Additive bonus δ·norm(r_beq) to +1 advantage, δ=0.3.

**Phase 4 — Progressive Domain Curriculum.** (a) Near-distribution warm-start: compilation ≥40%, critic approval ≥60%, BEq@32 ≥3pp above baseline. Timeout: 500 steps. (b) Retrieval bootstrapping: Tier 1/2 errors feed retriever updates. Transition: recall@10 ≥30%, compilation ≥25%. Early transition: plateau <2pp over 200 steps. (c) Far-OOD: algebraic geometry, condensed mathematics, MathAtlas MA-Hard with adaptive fallback.

**Contribution Floor Analysis.** (1) Co-adaptive retrieval + CriticLean TTRL alone: first co-adaptive retrieval for autoformalization + first TTRL for formal math with calibrated critic. (2) Binarize-then-enrich alone: addresses DDRL's explicit future work on multi-tier rewards. (3) Curriculum: droppable. (4) Essential floor: CriticLean TTRL outperforms compilation-only (Phase 0 gate) AND ≥1 of co-adaptive retrieval / binarize-then-enrich shows statistically significant improvement.

**Evaluation.**

  *Benchmarks:* In-distribution: miniF2F-test (244), ProofNet (~371). Multi-domain: FormalMATH (5,560). OOD stress tests: Con-NF, CombiBench, MathAtlas MA-Hard (700 entities, best: 2.6%; contingency: IndiMathBench if gold coverage <50%).

  *Metrics:* BEq@K, BEq+@K (per DRIFT), pass@K (K=1,32), compilation@K on all benchmarks. GTED (arXiv:2507.07399, continuous [0,1] similarity with better precision-recall balance than BEq) on OOD benchmarks. Hall_m (DDR's hallucination rate) in retriever ablation. Human evaluation: 100-150 samples on Con-NF + 200 samples on MathAtlas MA-Hard (inter-annotator agreement reported).

  *Same-scale primary baselines (~7-8B):* (1) FormaRL (Qwen2.5-Coder-7B, COLM 2025); (2) Online RL for Autoformalization (Wang et al., faithfully reimplemented if code unavailable); (3) DRIFT with Qwen3-8B (ICLR 2026); (4) Aria (ICLR 2026, reimplemented on shared benchmarks or reported numbers annotated); (5) StepFun-Formalizer-7B (AAAI 2026, open-source); (6) ReForm-8B (Qwen3-8B, arXiv:2510.24592); (7) compilation-only TTRL and critic-only TTRL ablations.

  *Cross-paradigm reference:* FormalEvolve (arXiv:2603.19828, reported SH@100 on CombiBench/ProofNet).

  *Compute-matched baseline:* Best-of-N (matched FLOPs) + CriticLean filtering: allocate equivalent test-time compute to sampling more candidates from base formalizer, filter with CriticLean-14B, report BEq@1 and compilation@1. Directly tests whether TTRA's weight adaptation provides value beyond inference-time scaling.

  *Ablations:* (a) Standard GRPO vs. DDRL vs. binarize-then-enrich (component-wise); (b) frozen vs. co-adaptive retriever; (c) Tier 1-only vs. Tier 1+2 vs. all-tier error signals; (d) no curriculum vs. progressive; (e) CriticLean-14B reward vs. embedding-based similarity reward (isolating trained critic value).

  *Sensitivity:* N_ret ∈ {25, 50, 100}; δ ∈ {0.0, 0.1, 0.3, 0.5} (δ=0.0 = pure DDRL); ambiguity zone ∈ {[20%-80%], [30%-70%], [40%-60%]}; critic confidence threshold ∈ {0.6, 0.7, 0.8, 0.9}; K ∈ {16, 32, 64} (test-time compute scaling behavior).

  *Cross-scale references:* ATF-32B, ATLAS (NeurIPS 2025), Monotonic Refinement (multi-model ensemble). All tables annotate scale and compute.

  *Statistical rigor:* Key comparisons ≥3 seeds, mean ± std, bootstrap CI (p<0.05).

## Detailed Description

TTRA makes TTRL viable for autoformalization by exploiting a structural asymmetry: Lean 4's compiler provides oracle-quality, token-level feedback (identifier names, type signatures, typeclass requirements) that serves simultaneously as retriever training signal, multi-tier reward components, and domain adaptation indicators—signals unavailable in informal reasoning and unexploited by existing methods. The dual-loop architecture co-adapts the retriever during test-time RL via weighted InfoNCE over Lean 4's error hierarchy, addressing the limitation that static retrievers (Aria, DRIFT, DDR) cannot track formalizer evolution. CriticLean-14B integration includes distributional shift calibration and periodic drift monitoring (motivated by TEMPO's EM analysis of reward signal degradation). Binarize-then-enrich addresses the specific gap between DDRL (binary debiasing) and GDPO (multi-reward normalization) for formal verification's heterogeneous reward landscape—a qualitatively different problem from the homogeneous-reward improvements in T³RL and SCOPE. Compute-matched evaluation against best-of-N + critic filtering directly tests whether weight adaptation provides value beyond inference-time scaling. The framework positions test-time learning as a third scaling axis for formal mathematics alongside training-time and inference-time compute.

## Key References

- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)
- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)
- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, NVIDIA, January 2026)
- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv:2507.06181, ByteDance/Nanjing)
- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)
- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv:2510.24652)
- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)
- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv:2601.11443, January 2026)
- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv:2602.01291, February 2026)
- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)
- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)
- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)
- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)
- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)
- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)
- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv:2511.11990)
- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)
- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)
- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)
- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)
- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv:2505.02735)
- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)
- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)
- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026, arXiv:2510.04520)
- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026, arXiv:2510.15681)
- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv:2510.24592)
- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv:2512.00997, Microsoft Research)
- FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv:2603.19828, March 2026)
- Binary Rewards and Reinforcement Learning: Fundamental Challenges (Dymetman, arXiv:2605.02375, May 2026)
- TEMPO: Scaling Test-time Training for Large Reasoning Models (arXiv:2604.19295, April 2026)
- T³RL: Tool Verification for Test-Time Reinforcement Learning (arXiv:2603.02203, March 2026)
- SCOPE: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning (arXiv:2512.15146, December 2025)
- GTED: Generalized Tree Edit Distance: A Faithful Evaluation Metric for Statement Autoformalization (arXiv:2507.07399)

## Resource Estimate

- **manual**: gpu_hours: 1400-1900 A100-80GB hours (Phase -1 micro-analysis + MathAtlas coverage: ~10h; Phase 0 pilot + calibration: ~50h; Phase 1 base GRPO: ~300h; DDR retriever + co-adaptive updates: ~100h; Phase 4 progressive TTRL + ablations: ~400h; CriticLean-14B inference all phases: ~200-300h; N_ret/δ/ambiguity/critic-threshold/K sensitivity: ~100h; baseline evaluation (Aria reimpl + StepFun + ReForm): ~100-120h; compute-matched best-of-N baseline: ~30h; CriticLean vs embedding ablation: ~25h; multi-seed (3 seeds × key ablations): ~200h; human eval annotation: ~60-80h; miniF2F/ProofNet + remaining eval: ~80h) + 15,000-20,000 CPU-hours Lean verification (Kimina Lean Server), timeline: 14-18 weeks (0.5 wk Phase -1; 2-3 wk Phase 0 + go/no-go; 3 wk Phase 1; 2 wk retriever infrastructure; 4 wk TTRL experiments; 3 wk ablations + sensitivity + multi-seed; 2 wk writing), estimated_gpu_cost: $2,800-$4,700 + $750-$1,000 CPU + ~$1,500-$2,500 human annotation. GPU architecture: policy (8B) + ref (8B) on 4×A100 tensor parallel, CriticLean-14B on dedicated 2×A100 with vLLM batch inference, retriever + FAISS on CPU/1×A100; async pipeline.
- **human_in_loop**: gpu_hours: 1100-1500 A100-80GB hours (~25% reduction), timeline: 11-14 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,200-$3,700 + $600-$800 CPU + ~$1,200-$2,000 annotation
- **auto_research**: gpu_hours: 2000-2700 A100-80GB hours (full sweep), timeline: 8-11 weeks, claude_api_cost: $800-$1,200, estimated_gpu_cost: $4,000-$6,700 + $1,000-$1,350 CPU + ~$1,500-$2,500 annotation, speed_bottleneck: Lean 4 compilation (~3.65s/statement warm cache, ~0.10s amortized at 64 workers). CriticLean-14B ~0.5s/candidate (→~0.1-0.2s with vLLM). Retriever co-adaptation ~15 min/cycle (re-encode 26K constants, rebuild FAISS).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "02227946-3903-41e6-bd0f-572926fd98ea",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:58:00.542Z_

```json
{
  "parentUuid": "02227946-3903-41e6-bd0f-572926fd98ea",
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
  "uuid": "e2122cd1-1c27-4a44-919e-df74d5c11069",
  "timestamp": "2026-05-28T05:58:00.542Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:58:00.542Z_

```json
{
  "parentUuid": "e2122cd1-1c27-4a44-919e-df74d5c11069",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "eaa1cded-9450-4f58-9333-6b75e0425b0a",
  "timestamp": "2026-05-28T05:58:00.542Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
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
  "leafUuid": "eaa1cded-9450-4f58-9333-6b75e0425b0a",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate test-time retrieval-augmented autoformalization proposal",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Assistant

_source line 8 · 2026-05-28T05:58:09.448Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed proposal for TTRA (Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization). I need to evaluate it as the "入口评审 agent" following the specified rubric. 

Let me first conduct research on the field to understand the current landscape before making my assessment. I need to search for:
1. Recent work on autoformalization and test-time RL
2. Co-adaptive retrieval methods
3. The specific papers cited in this proposal to verify their existence and claims


4. Background on the key technical components and their current state of development

Now I'm beginning my literature search on these core topics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaa1cded-9450-4f58-9333-6b75e0425b0a",
  "isSidechain": false,
  "requestId": "req_011CbUTGC7XaRj8vfzuDFsKd",
  "type": "assistant",
  "uuid": "618a7c1b-95b1-493a-87aa-038ed595be41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiDdzqtdDXEVQnaCQmKbjC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9782,
      "cache_read_input_tokens": 13968,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 13968,
          "cache_creation_input_tokens": 9782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9782
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

_source line 9 · 2026-05-28T05:58:09.453Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RanokhD4SsJtVoTmsbJkA2`</summary>

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
  "parentUuid": "618a7c1b-95b1-493a-87aa-038ed595be41",
  "isSidechain": false,
  "requestId": "req_011CbUTGC7XaRj8vfzuDFsKd",
  "type": "assistant",
  "uuid": "468bd70d-7cc3-431f-a69a-c0d8e81e7872",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiDdzqtdDXEVQnaCQmKbjC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9782,
      "cache_read_input_tokens": 13968,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 13968,
          "cache_creation_input_tokens": 9782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9782
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

_source line 10 · 2026-05-28T05:58:09.462Z_

<details><summary>↩ Tool result · `toolu_01RanokhD4SsJtVoTmsbJkA2`</summary>

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
  "parentUuid": "468bd70d-7cc3-431f-a69a-c0d8e81e7872",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "e2869933-a2c5-46df-8e29-6b66bf772fce",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "468bd70d-7cc3-431f-a69a-c0d8e81e7872",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-28T05:58:16.040Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required research. I need to search for:
1. Recent work on test-time RL (TTRL) for math reasoning and autoformalization
2. Co-adaptive retrieval methods in formal mathematics
3. CriticLean and semantic critics for autoformalization
4. DDRL and debiased RL methods
5. The current state of autoformalization (Aria, DRIFT, DDR, etc.)

Let me do 5 targeted searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2869933-a2c5-46df-8e29-6b66bf772fce",
  "isSidechain": false,
  "requestId": "req_011CbUTGrYa9uq7fVVbjKyXo",
  "type": "assistant",
  "uuid": "62eb87d5-3c07-4416-8178-e46cf7b46cd5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5J7ABiUqx4Ca56imtDHAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 23750,
      "output_tokens": 430,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 430,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 12 · 2026-05-28T05:58:17.047Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cm8Uck5W4sy7mcAwdR8ee2`</summary>

```json
{
  "query": "TTRL test-time reinforcement learning autoformalization Lean 4 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62eb87d5-3c07-4416-8178-e46cf7b46cd5",
  "isSidechain": false,
  "requestId": "req_011CbUTGrYa9uq7fVVbjKyXo",
  "type": "assistant",
  "uuid": "085221ce-9f24-4c58-86dd-f758d9288e3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5J7ABiUqx4Ca56imtDHAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 23750,
      "output_tokens": 430,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 430,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 13 · 2026-05-28T05:58:17.555Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0184ngwEq9i3tpwDzamGK1s6`</summary>

```json
{
  "query": "CriticLean CriticLeanGPT mathematical formalization critic reward 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "085221ce-9f24-4c58-86dd-f758d9288e3b",
  "isSidechain": false,
  "requestId": "req_011CbUTGrYa9uq7fVVbjKyXo",
  "type": "assistant",
  "uuid": "77650b65-9c24-4cc9-9555-8e443304e925",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5J7ABiUqx4Ca56imtDHAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 23750,
      "output_tokens": 430,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 430,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 14 · 2026-05-28T05:58:18.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S1nkdVc46R9xpDdjxUtGmX`</summary>

```json
{
  "query": "DDRL debiased test-time reinforcement learning GRPO spurious signal amplification ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77650b65-9c24-4cc9-9555-8e443304e925",
  "isSidechain": false,
  "requestId": "req_011CbUTGrYa9uq7fVVbjKyXo",
  "type": "assistant",
  "uuid": "2691a3b5-4bf8-4581-bae1-d9c19809ff89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5J7ABiUqx4Ca56imtDHAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 23750,
      "output_tokens": 430,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 430,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 15 · 2026-05-28T05:58:19.007Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TRpbGrYqo29c9414eE1a7A`</summary>

```json
{
  "query": "co-adaptive retrieval RAG reinforcement learning R3 Reinforced-IR 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2691a3b5-4bf8-4581-bae1-d9c19809ff89",
  "isSidechain": false,
  "requestId": "req_011CbUTGrYa9uq7fVVbjKyXo",
  "type": "assistant",
  "uuid": "254a5e12-1a05-404b-8cae-fecf72c71541",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5J7ABiUqx4Ca56imtDHAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 23750,
      "output_tokens": 430,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 430,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 16 · 2026-05-28T05:58:19.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wj98j3kJHYJGfqti3Hkj2x`</summary>

```json
{
  "query": "Aria ICLR 2026 autoformalization retrieval dependency graph Lean MathAtlas 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "254a5e12-1a05-404b-8cae-fecf72c71541",
  "isSidechain": false,
  "requestId": "req_011CbUTGrYa9uq7fVVbjKyXo",
  "type": "assistant",
  "uuid": "27d11ff9-4840-48a3-a6f5-0dd757b20983",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5J7ABiUqx4Ca56imtDHAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 23750,
      "output_tokens": 430,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 430,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 17 · 2026-05-28T05:58:24.378Z_

<details><summary>↩ Tool result · `toolu_0184ngwEq9i3tpwDzamGK1s6`</summary>

```text
Web search results for query: "CriticLean CriticLeanGPT mathematical formalization critic reward 2025"

Links: [{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"},{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"},{"title":"m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face","url":"https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | Nanjing University Large-scale Intelligence and Knowledge Laboratory","url":"https://www.nju-link.com/en/publication/peng-2025-criticleancriticguidedreinforcementlearning/"}]

Based on the search results, here's what I found about CriticLean and CriticLeanGPT:

## Overview

CriticLean addresses the challenge of translating natural language mathematical statements into formal, executable code, with a focus on the critic phase—evaluating whether generated formalizations truly capture the semantic intent of the original problem.

## Key Components

CriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component.

**CriticLeanGPT**: This model is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations. CriticLeanGPT models outperform strong baselines in distinguishing semantically correct from incorrect formalizations.

**CriticLeanBench**: A benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.

**FineLeanCorpus**: A dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.

## Significance

The findings highlight that optimizing the critic phase is essential for producing reliable formalizations. The paper was published on July 8, 2025, with authors including Zhongyuan Peng and 18 others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77650b65-9c24-4cc9-9555-8e443304e925",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "79aff91c-a13d-487b-804c-8fbae809076e",
  "toolUseResult": {
    "query": "CriticLean CriticLeanGPT mathematical formalization critic reward 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H2F1EuW2hswDgLZc2Mj7Su",
        "content": [
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
          },
          {
            "title": "[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181v1"
          },
          {
            "title": "[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181"
          },
          {
            "title": "(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"
          },
          {
            "title": "m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face",
            "url": "https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | Nanjing University Large-scale Intelligence and Knowledge Laboratory",
            "url": "https://www.nju-link.com/en/publication/peng-2025-criticleancriticguidedreinforcementlearning/"
          }
        ]
      },
      "Based on the search results, here's what I found about CriticLean and CriticLeanGPT:\n\n## Overview\n\nCriticLean addresses the challenge of translating natural language mathematical statements into formal, executable code, with a focus on the critic phase—evaluating whether generated formalizations truly capture the semantic intent of the original problem.\n\n## Key Components\n\nCriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component.\n\n**CriticLeanGPT**: This model is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations. CriticLeanGPT models outperform strong baselines in distinguishing semantically correct from incorrect formalizations.\n\n**CriticLeanBench**: A benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.\n\n**FineLeanCorpus**: A dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.\n\n## Significance\n\nThe findings highlight that optimizing the critic phase is essential for producing reliable formalizations. The paper was published on July 8, 2025, with authors including Zhongyuan Peng and 18 others."
    ],
    "durationSeconds": 6.819299565999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "77650b65-9c24-4cc9-9555-8e443304e925",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T05:58:25.359Z_

<details><summary>↩ Tool result · `toolu_01Cm8Uck5W4sy7mcAwdR8ee2`</summary>

```text
Web search results for query: "TTRL test-time reinforcement learning autoformalization Lean 4 2025 2026"

Links: [{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"[2504.16084] TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2504.16084"},{"title":"TTRL: Test-Time Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=VuVhgEiu20"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372v1"},{"title":"(PDF) Online Reinforcement Learning for Autoformalization","url":"https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"},{"title":"GitHub - PRIME-RL/TTRL: [NeurIPS 2025] TTRL: Test-Time Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/TTRL"},{"title":"arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084"}]

Based on the search results, here's what I found about TTRL (Test-Time Reinforcement Learning) and its application to autoformalization in Lean 4:

## Overview of TTRL

TTRL is a novel method for training LLMs using reinforcement learning on unlabeled data. TTRL enables self-evolution of LLMs by utilizing the priors in the pre-trained models. Common practices in Test-Time Scaling (TTS), such as majority voting, yield surprisingly effective rewards suitable for driving RL training.

## Performance Results

The technique has shown impressive results: TTRL boosts the pass@1 performance of Qwen-2.5-Math-7B by approximately 211% on the AIME 2024 with only unlabeled test data. The TTRL paper was accepted to NeurIPS 2025.

## Application to Lean 4 Autoformalization

For the most difficult problems, TTRL is used as a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation. TTRL enables discovery, combination, and reuse of intermediate lemmas autonomously and achieved 92.2% on MiniF2F with full Test-Time RL (TTRL) search framework.

Additionally, online reinforcement learning is being studied for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "085221ce-9f24-4c58-86dd-f758d9288e3b",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "1c694e3b-cb07-4680-ba5b-19ebd8ae6239",
  "toolUseResult": {
    "query": "TTRL test-time reinforcement learning autoformalization Lean 4 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015espw88ixUNfgeQ1VRC5YN",
        "content": [
          {
            "title": "Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics",
            "url": "https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"
          },
          {
            "title": "[2504.16084] TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/abs/2504.16084"
          },
          {
            "title": "TTRL: Test-Time Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=VuVhgEiu20"
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
            "title": "GitHub - PRIME-RL/TTRL: [NeurIPS 2025] TTRL: Test-Time Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/TTRL"
          },
          {
            "title": "arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2504.16084"
          }
        ]
      },
      "Based on the search results, here's what I found about TTRL (Test-Time Reinforcement Learning) and its application to autoformalization in Lean 4:\n\n## Overview of TTRL\n\nTTRL is a novel method for training LLMs using reinforcement learning on unlabeled data. TTRL enables self-evolution of LLMs by utilizing the priors in the pre-trained models. Common practices in Test-Time Scaling (TTS), such as majority voting, yield surprisingly effective rewards suitable for driving RL training.\n\n## Performance Results\n\nThe technique has shown impressive results: TTRL boosts the pass@1 performance of Qwen-2.5-Math-7B by approximately 211% on the AIME 2024 with only unlabeled test data. The TTRL paper was accepted to NeurIPS 2025.\n\n## Application to Lean 4 Autoformalization\n\nFor the most difficult problems, TTRL is used as a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation. TTRL enables discovery, combination, and reuse of intermediate lemmas autonomously and achieved 92.2% on MiniF2F with full Test-Time RL (TTRL) search framework.\n\nAdditionally, online reinforcement learning is being studied for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4."
    ],
    "durationSeconds": 8.307605851,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "085221ce-9f24-4c58-86dd-f758d9288e3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T05:58:26.056Z_

<details><summary>↩ Tool result · `toolu_01S1nkdVc46R9xpDdjxUtGmX`</summary>

```text
Web search results for query: "DDRL debiased test-time reinforcement learning GRPO spurious signal amplification ACL 2026"

Links: [{"title":"Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/html/2604.21327"},{"title":"[2604.21327] Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/abs/2604.21327"},{"title":"What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time","url":"https://arxiv.org/html/2603.19880"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Dual Consensus: Escaping from Spurious Majority in Unsupervised RLVR via Two-Stage Vote Mechanism","url":"https://arxiv.org/html/2603.16223"},{"title":"What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time","url":"https://arxiv.org/pdf/2603.19880"}]

Based on the search results, I found relevant information about DDRL and spurious signal amplification in test-time reinforcement learning:

## Key Findings

DDRL (Debiased and Denoised test-time Reinforcement Learning) is a framework designed to mitigate spurious signals in test-time reinforcement learning for math reasoning.

### The Problem with GRPO

GRPO's normalization mechanism disproportionately amplifies spurious rewards in low-consensus regimes. More specifically, majority voting can produce false-positive supervision by promoting a wrong answer, which is further amplified under GRPO due to group normalization.

### DDRL's Solution

DDRL first applies a frequency-based sampling strategy to exclude ambiguous samples while maintaining a balanced set of positive and negative examples. It then adopts a debiased advantage estimation with fixed advantages, removing the bias introduced by group-relative policy optimization. Finally, DDRL incorporates a consensus-based off-policy refinement stage, which leverages the rejection-sampled dataset to enable efficient and stable model updates.

### Results

Experiments on three large language models across multiple mathematical reasoning benchmarks demonstrate that DDRL consistently outperforms existing TTRL baselines. The paper was published in Findings of the Association for Computational Linguistics: ACL 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2691a3b5-4bf8-4581-bae1-d9c19809ff89",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "c75eb5c9-1c9b-4ce3-81d8-3c1ab0618b7d",
  "toolUseResult": {
    "query": "DDRL debiased test-time reinforcement learning GRPO spurious signal amplification ACL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R1ekMXRAdAorFxqudPysB3",
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
            "title": "What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time",
            "url": "https://arxiv.org/html/2603.19880"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/pdf/2503.06639"
          },
          {
            "title": "Dual Consensus: Escaping from Spurious Majority in Unsupervised RLVR via Two-Stage Vote Mechanism",
            "url": "https://arxiv.org/html/2603.16223"
          },
          {
            "title": "What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time",
            "url": "https://arxiv.org/pdf/2603.19880"
          }
        ]
      },
      "Based on the search results, I found relevant information about DDRL and spurious signal amplification in test-time reinforcement learning:\n\n## Key Findings\n\nDDRL (Debiased and Denoised test-time Reinforcement Learning) is a framework designed to mitigate spurious signals in test-time reinforcement learning for math reasoning.\n\n### The Problem with GRPO\n\nGRPO's normalization mechanism disproportionately amplifies spurious rewards in low-consensus regimes. More specifically, majority voting can produce false-positive supervision by promoting a wrong answer, which is further amplified under GRPO due to group normalization.\n\n### DDRL's Solution\n\nDDRL first applies a frequency-based sampling strategy to exclude ambiguous samples while maintaining a balanced set of positive and negative examples. It then adopts a debiased advantage estimation with fixed advantages, removing the bias introduced by group-relative policy optimization. Finally, DDRL incorporates a consensus-based off-policy refinement stage, which leverages the rejection-sampled dataset to enable efficient and stable model updates.\n\n### Results\n\nExperiments on three large language models across multiple mathematical reasoning benchmarks demonstrate that DDRL consistently outperforms existing TTRL baselines. The paper was published in Findings of the Association for Computational Linguistics: ACL 2026."
    ],
    "durationSeconds": 7.537883043000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2691a3b5-4bf8-4581-bae1-d9c19809ff89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T05:58:26.776Z_

<details><summary>↩ Tool result · `toolu_01Wj98j3kJHYJGfqti3Hkj2x`</summary>

```text
Web search results for query: "Aria ICLR 2026 autoformalization retrieval dependency graph Lean MathAtlas 2026"

Links: [{"title":"Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph | OpenReview","url":"https://openreview.net/forum?id=CPxZClPMiy"},{"title":"ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://iclr.cc/virtual/2026/poster/10010860"},{"title":"[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251004520W/abstract"},{"title":"[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520v1"},{"title":"[Literature Review] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://www.themoonlight.io/en/review/aria-an-agent-for-retrieval-and-iterative-auto-formalization-via-dependency-graph"},{"title":"(PDF) Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://www.researchgate.net/publication/396250696_Aria_An_Agent_For_Retrieval_and_Iterative_Auto-Formalization_via_Dependency_Graph"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE","url":"https://arxiv.org/pdf/2510.04520"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE ...","url":"https://openreview.net/pdf/388a385b7ad068290351f90757bd3af8bb6e5515.pdf"}]

Based on the search results, here's what I found about your query:

## Aria: An Agent for Retrieval and Iterative Auto-Formalization

Aria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.

### Key Components

The system addresses the challenges that make auto-formalization a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.

To ensure semantic correctness, the paper introduces AriaScorer, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.

### Performance Results

On ProofNet, Aria achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods.

### Conference Information

This work is an ICLR 2026 Conference submission, presented as both a paper submission and conference poster at ICLR 2026.

Note: The search results don't contain specific information about MathAtlas in connection with Aria, though the work does utilize Mathlib for definition retrieval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27d11ff9-4840-48a3-a6f5-0dd757b20983",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "d4376f89-758d-4ee2-8bb5-59999debef97",
  "toolUseResult": {
    "query": "Aria ICLR 2026 autoformalization retrieval dependency graph Lean MathAtlas 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AsNfZAdiuNXyCtSCAffeHa",
        "content": [
          {
            "title": "Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph | OpenReview",
            "url": "https://openreview.net/forum?id=CPxZClPMiy"
          },
          {
            "title": "ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://iclr.cc/virtual/2026/poster/10010860"
          },
          {
            "title": "[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/abs/2510.04520"
          },
          {
            "title": "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251004520W/abstract"
          },
          {
            "title": "[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/abs/2510.04520v1"
          },
          {
            "title": "[Literature Review] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://www.themoonlight.io/en/review/aria-an-agent-for-retrieval-and-iterative-auto-formalization-via-dependency-graph"
          },
          {
            "title": "(PDF) Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://www.researchgate.net/publication/396250696_Aria_An_Agent_For_Retrieval_and_Iterative_Auto-Formalization_via_Dependency_Graph"
          },
          {
            "title": "ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE",
            "url": "https://arxiv.org/pdf/2510.04520"
          },
          {
            "title": "ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE ...",
            "url": "https://openreview.net/pdf/388a385b7ad068290351f90757bd3af8bb6e5515.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about your query:\n\n## Aria: An Agent for Retrieval and Iterative Auto-Formalization\n\nAria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.\n\n### Key Components\n\nThe system addresses the challenges that make auto-formalization a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.\n\nTo ensure semantic correctness, the paper introduces AriaScorer, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.\n\n### Performance Results\n\nOn ProofNet, Aria achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods.\n\n### Conference Information\n\nThis work is an ICLR 2026 Conference submission, presented as both a paper submission and conference poster at ICLR 2026.\n\nNote: The search results don't contain specific information about MathAtlas in connection with Aria, though the work does utilize Mathlib for definition retrieval."
    ],
    "durationSeconds": 7.099155607999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "27d11ff9-4840-48a3-a6f5-0dd757b20983",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
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
  "leafUuid": "d4376f89-758d-4ee2-8bb5-59999debef97",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate test-time retrieval-augmented autoformalization proposal",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Tool result

_source line 23 · 2026-05-28T05:58:27.461Z_

<details><summary>↩ Tool result · `toolu_01TRpbGrYqo29c9414eE1a7A`</summary>

```text
Web search results for query: "co-adaptive retrieval RAG reinforcement learning R3 Reinforced-IR 2025 2026"

Links: [{"title":"Optimizing Retrieval for RAG via Reinforced Contrastive Learning | OpenReview","url":"https://openreview.net/forum?id=yZzhaHygWW"},{"title":"Optimizing Retrieval for RAG via Reinforced Contrastive Learning","url":"https://arxiv.org/html/2510.24652v1"},{"title":"Optimizing Retrieval for RAG via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2510.24652"},{"title":"Optimizing Retrieval for RAG via Reinforcement Learning Jiawei Zhou Lei Chen","url":"https://arxiv.org/pdf/2510.24652"},{"title":"[2510.24652v1] Optimizing Retrieval for RAG via Reinforced Contrastive Learning","url":"https://arxiv.org/abs/2510.24652v1"},{"title":"[2510.24652] Optimizing Retrieval for RAG via Reinforcement Learning","url":"https://arxiv.org/abs/2510.24652"},{"title":"Reinforced Information Retrieval","url":"https://arxiv.org/html/2502.11562"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2505.23794v2"},{"title":"[2505.23794] R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2505.23794"}]

Based on the search results, here's what I found:

## R3: Reinforced Contrastive Learning for RAG

R3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. Unlike prior works that learn pre-defined relevance via supervised fine-tuning through annotation or synthetic data, R3 aims to explore relevance via reinforcement learning within the RAG environment through reinforced contrastive learning, where contrastive relational data are explored during training rather than pre-annotated.

R3 follows the standard RAG workflow by retrieving documents and incorporating them as context for LLM generation, and based on the generation outcomes, the retrieved documents are labeled as positive or negative with respect to the query for contrastive learning optimization.

R3 achieves an average 5.2% improvement in 1-shot accuracy and consistently outperforms state-of-the-art retrievers as well as LLM-empowered retrieval methods.

## Reinforced-IR: Co-adaptive Framework

Reinforced-IR is a novel domain adaptation framework which jointly adapts the retriever and LLM-based generator using an unlabeled corpus. The method features a self-boosting algorithm where the LLM-based generator is reinforced through Reinforcement Learning of generator with Retriever's Feedback (RLRF), and the retriever is reinforced through Reinforcement Learning of retriever with Generator's Feedback (RLGF).

Both frameworks represent recent advances (2025-2026) in using reinforcement learning to improve retrieval and generation in RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "254a5e12-1a05-404b-8cae-fecf72c71541",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "27350cb8-93bf-4d74-b16b-7a4de93d2fbe",
  "toolUseResult": {
    "query": "co-adaptive retrieval RAG reinforcement learning R3 Reinforced-IR 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GApqEYfR3GiuL8QDDRvpsP",
        "content": [
          {
            "title": "Optimizing Retrieval for RAG via Reinforced Contrastive Learning | OpenReview",
            "url": "https://openreview.net/forum?id=yZzhaHygWW"
          },
          {
            "title": "Optimizing Retrieval for RAG via Reinforced Contrastive Learning",
            "url": "https://arxiv.org/html/2510.24652v1"
          },
          {
            "title": "Optimizing Retrieval for RAG via Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2510.24652"
          },
          {
            "title": "Optimizing Retrieval for RAG via Reinforcement Learning Jiawei Zhou Lei Chen",
            "url": "https://arxiv.org/pdf/2510.24652"
          },
          {
            "title": "[2510.24652v1] Optimizing Retrieval for RAG via Reinforced Contrastive Learning",
            "url": "https://arxiv.org/abs/2510.24652v1"
          },
          {
            "title": "[2510.24652] Optimizing Retrieval for RAG via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2510.24652"
          },
          {
            "title": "Reinforced Information Retrieval",
            "url": "https://arxiv.org/html/2502.11562"
          },
          {
            "title": "R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.23794v2"
          },
          {
            "title": "[2505.23794] R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.23794"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## R3: Reinforced Contrastive Learning for RAG\n\nR3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. Unlike prior works that learn pre-defined relevance via supervised fine-tuning through annotation or synthetic data, R3 aims to explore relevance via reinforcement learning within the RAG environment through reinforced contrastive learning, where contrastive relational data are explored during training rather than pre-annotated.\n\nR3 follows the standard RAG workflow by retrieving documents and incorporating them as context for LLM generation, and based on the generation outcomes, the retrieved documents are labeled as positive or negative with respect to the query for contrastive learning optimization.\n\nR3 achieves an average 5.2% improvement in 1-shot accuracy and consistently outperforms state-of-the-art retrievers as well as LLM-empowered retrieval methods.\n\n## Reinforced-IR: Co-adaptive Framework\n\nReinforced-IR is a novel domain adaptation framework which jointly adapts the retriever and LLM-based generator using an unlabeled corpus. The method features a self-boosting algorithm where the LLM-based generator is reinforced through Reinforcement Learning of generator with Retriever's Feedback (RLRF), and the retriever is reinforced through Reinforcement Learning of retriever with Generator's Feedback (RLGF).\n\nBoth frameworks represent recent advances (2025-2026) in using reinforcement learning to improve retrieval and generation in RAG systems."
    ],
    "durationSeconds": 8.451589101999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "254a5e12-1a05-404b-8cae-fecf72c71541",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-28T05:58:32.393Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've verified several key papers. Let me do a few more targeted searches to verify additional claims and check for competing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27350cb8-93bf-4d74-b16b-7a4de93d2fbe",
  "isSidechain": false,
  "requestId": "req_011CbUTJAd37whqAerHMnpTE",
  "type": "assistant",
  "uuid": "0691a4bc-5285-4126-8c20-d3fa473be4d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vy2oNj8Uxbn1pc7acXL7k2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 3549,
      "cache_read_input_tokens": 24504,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 901,
          "output_tokens": 214,
          "cache_read_input_tokens": 24504,
          "cache_creation_input_tokens": 3549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3549
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

_source line 25 · 2026-05-28T05:58:32.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AVEEyEzBogg34m6j5vFEvQ`</summary>

```json
{
  "query": "FormalEvolve autoformalization evolutionary search CombiBench 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0691a4bc-5285-4126-8c20-d3fa473be4d9",
  "isSidechain": false,
  "requestId": "req_011CbUTJAd37whqAerHMnpTE",
  "type": "assistant",
  "uuid": "61ad7052-903d-4e89-8027-b366c4c4f9b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vy2oNj8Uxbn1pc7acXL7k2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 3549,
      "cache_read_input_tokens": 24504,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 901,
          "output_tokens": 214,
          "cache_read_input_tokens": 24504,
          "cache_creation_input_tokens": 3549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3549
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

_source line 26 · 2026-05-28T05:58:33.876Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BFMFBzBwtN4pwrx7LBVzuj`</summary>

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
  "parentUuid": "61ad7052-903d-4e89-8027-b366c4c4f9b0",
  "isSidechain": false,
  "requestId": "req_011CbUTJAd37whqAerHMnpTE",
  "type": "assistant",
  "uuid": "72b26f58-e6dc-4b7e-98c3-c83fb48226b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vy2oNj8Uxbn1pc7acXL7k2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 3549,
      "cache_read_input_tokens": 24504,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 901,
          "output_tokens": 214,
          "cache_read_input_tokens": 24504,
          "cache_creation_input_tokens": 3549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3549
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

_source line 27 · 2026-05-28T05:58:34.367Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lqr9XsuNTk8GS3AzMz1KV6`</summary>

```json
{
  "query": "TEMPO test-time training EM framework reasoning models 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72b26f58-e6dc-4b7e-98c3-c83fb48226b2",
  "isSidechain": false,
  "requestId": "req_011CbUTJAd37whqAerHMnpTE",
  "type": "assistant",
  "uuid": "c527525c-1413-483d-8c39-a4f8335c3879",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vy2oNj8Uxbn1pc7acXL7k2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 3549,
      "cache_read_input_tokens": 24504,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 901,
          "output_tokens": 214,
          "cache_read_input_tokens": 24504,
          "cache_creation_input_tokens": 3549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3549
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

_source line 28 · 2026-05-28T05:58:40.006Z_

<details><summary>↩ Tool result · `toolu_01BFMFBzBwtN4pwrx7LBVzuj`</summary>

```text
Web search results for query: "FormaRL GRPO autoformalization COLM 2025 compilation reward"

Links: [{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data | OpenReview","url":"https://openreview.net/forum?id=Z2El1U94bq"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/abs/2508.18914"},{"title":"FormaRL: RL-Driven Autoformalization for Lean 4","url":"https://www.emergentmind.com/topics/formarl"},{"title":"[PDF] FormaRL: Enhancing Autoformalization with no Labeled Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FormaRL:-Enhancing-Autoformalization-with-no-Data-Huang-Jin/b430d8ac9cf1236314a1273dc7e8fb9769ebae70"},{"title":"Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs","url":"https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"},{"title":"GitHub - THUNLP-MT/FormaRL: [COLM25] Enhancing Autoformalization with no Labeled Data · GitHub","url":"https://github.com/THUNLP-MT/FormaRL"},{"title":"Yang Liu's Homepage at Tsinghua University","url":"https://nlp.csai.tsinghua.edu.cn/~ly/pub.html"},{"title":"Published as a conference paper at COLM 2025","url":"https://par.nsf.gov/servlets/purl/10635650"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"}]

Based on the search results, here's what I found about FormaRL, GRPO, autoformalization, and COLM 2025:

## Overview

FormaRL is a reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. The paper was published at COLM 2025.

## Compilation Reward Mechanism

FormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer. This dual-reward approach combines:
- **Syntax checking**: Validation through the Lean compiler
- **Semantic checking**: Consistency evaluation using a large language model

## GRPO Algorithm

The GRPO algorithm is used as the optimization method to update the formalizer model based on the combined rewards from compilation and semantic checking.

## Key Contributions

The authors also curated a proof problem dataset from undergraduate-level math materials, named **uproof**.

## Performance

The method improved autoformalizers on both pass@1 accuracy (6.2% → 9.6%) and pass@16 accuracy (24.4% → 33.6%).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72b26f58-e6dc-4b7e-98c3-c83fb48226b2",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "e7244d1e-bfd3-404c-ada4-4f7dd0fb477c",
  "toolUseResult": {
    "query": "FormaRL GRPO autoformalization COLM 2025 compilation reward",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EJ6yY5gaLxQW3A8BpWkakB",
        "content": [
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data | OpenReview",
            "url": "https://openreview.net/forum?id=Z2El1U94bq"
          },
          {
            "title": "Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics",
            "url": "https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"
          },
          {
            "title": "[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/abs/2508.18914"
          },
          {
            "title": "FormaRL: RL-Driven Autoformalization for Lean 4",
            "url": "https://www.emergentmind.com/topics/formarl"
          },
          {
            "title": "[PDF] FormaRL: Enhancing Autoformalization with no Labeled Data | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/FormaRL:-Enhancing-Autoformalization-with-no-Data-Huang-Jin/b430d8ac9cf1236314a1273dc7e8fb9769ebae70"
          },
          {
            "title": "Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs",
            "url": "https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"
          },
          {
            "title": "GitHub - THUNLP-MT/FormaRL: [COLM25] Enhancing Autoformalization with no Labeled Data · GitHub",
            "url": "https://github.com/THUNLP-MT/FormaRL"
          },
          {
            "title": "Yang Liu's Homepage at Tsinghua University",
            "url": "https://nlp.csai.tsinghua.edu.cn/~ly/pub.html"
          },
          {
            "title": "Published as a conference paper at COLM 2025",
            "url": "https://par.nsf.gov/servlets/purl/10635650"
          },
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/pdf/2508.18914"
          }
        ]
      },
      "Based on the search results, here's what I found about FormaRL, GRPO, autoformalization, and COLM 2025:\n\n## Overview\n\nFormaRL is a reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. The paper was published at COLM 2025.\n\n## Compilation Reward Mechanism\n\nFormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer. This dual-reward approach combines:\n- **Syntax checking**: Validation through the Lean compiler\n- **Semantic checking**: Consistency evaluation using a large language model\n\n## GRPO Algorithm\n\nThe GRPO algorithm is used as the optimization method to update the formalizer model based on the combined rewards from compilation and semantic checking.\n\n## Key Contributions\n\nThe authors also curated a proof problem dataset from undergraduate-level math materials, named **uproof**.\n\n## Performance\n\nThe method improved autoformalizers on both pass@1 accuracy (6.2% → 9.6%) and pass@16 accuracy (24.4% → 33.6%)."
    ],
    "durationSeconds": 6.125584883999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "72b26f58-e6dc-4b7e-98c3-c83fb48226b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-28T05:58:40.317Z_

<details><summary>↩ Tool result · `toolu_01AVEEyEzBogg34m6j5vFEvQ`</summary>

```text
Web search results for query: "FormalEvolve autoformalization evolutionary search CombiBench 2026"

Links: [{"title":"[2603.19828] FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/abs/2603.19828"},{"title":"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/pdf/2603.19828"},{"title":"arXiv preprint AUTOFORMALIZER WITH TOOL FEEDBACK","url":"https://arxiv.org/pdf/2510.06857"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion","url":"https://arxiv.org/html/2508.04440v2"},{"title":"(PDF) FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://www.researchgate.net/publication/403308231_FormalProofBench_Can_Models_Write_Graduate_Level_Math_Proofs_That_Are_Formally_Verified"}]

Based on the search results, here's what I found about FormalEvolve:

FormalEvolve is a compilation-gated neuro-symbolic evolutionary framework that formulates autoformalization as a budgeted, test-time search for semantically consistent repertoires. Autoformalization aims to translate natural-language mathematics into compilable, machine-checkable statements.

FormalEvolve generates diverse candidates via LLM-driven mutation and crossover with bounded patch repair, while symbolic Abstract Syntax Tree (AST) rewrite operations further inject structural diversity.

The framework was evaluated on benchmark datasets: On CombiBench and ProofNet, under a strict generator-call budget of T = 100, FormalEvolve reaches semantic hit rates (SH@100) of 58.0% and 84.9%, and reduces cross-problem concentration of semantic successes (lower Gini). Additionally, under a fixed prover budget, FormalEvolve also improves downstream proving performance on CombiBench.

The paper was published on arXiv on March 23, 2026, with the full reference: "FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization" (arXiv:2603.19828).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61ad7052-903d-4e89-8027-b366c4c4f9b0",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "35bae74b-d657-4f1a-86d2-0fc9155a9f7b",
  "toolUseResult": {
    "query": "FormalEvolve autoformalization evolutionary search CombiBench 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A8VcTBtsJVsLzvctXq19C4",
        "content": [
          {
            "title": "[2603.19828] FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization",
            "url": "https://arxiv.org/abs/2603.19828"
          },
          {
            "title": "FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization",
            "url": "https://arxiv.org/pdf/2603.19828"
          },
          {
            "title": "arXiv preprint AUTOFORMALIZER WITH TOOL FEEDBACK",
            "url": "https://arxiv.org/pdf/2510.06857"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/html/2508.04440v2"
          },
          {
            "title": "(PDF) FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://www.researchgate.net/publication/403308231_FormalProofBench_Can_Models_Write_Graduate_Level_Math_Proofs_That_Are_Formally_Verified"
          }
        ]
      },
      "Based on the search results, here's what I found about FormalEvolve:\n\nFormalEvolve is a compilation-gated neuro-symbolic evolutionary framework that formulates autoformalization as a budgeted, test-time search for semantically consistent repertoires. Autoformalization aims to translate natural-language mathematics into compilable, machine-checkable statements.\n\nFormalEvolve generates diverse candidates via LLM-driven mutation and crossover with bounded patch repair, while symbolic Abstract Syntax Tree (AST) rewrite operations further inject structural diversity.\n\nThe framework was evaluated on benchmark datasets: On CombiBench and ProofNet, under a strict generator-call budget of T = 100, FormalEvolve reaches semantic hit rates (SH@100) of 58.0% and 84.9%, and reduces cross-problem concentration of semantic successes (lower Gini). Additionally, under a fixed prover budget, FormalEvolve also improves downstream proving performance on CombiBench.\n\nThe paper was published on arXiv on March 23, 2026, with the full reference: \"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization\" (arXiv:2603.19828)."
    ],
    "durationSeconds": 7.448781808,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "61ad7052-903d-4e89-8027-b366c4c4f9b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T05:58:45.611Z_

<details><summary>↩ Tool result · `toolu_01Lqr9XsuNTk8GS3AzMz1KV6`</summary>

```text
Web search results for query: "TEMPO test-time training EM framework reasoning models 2026 arXiv"

Links: [{"title":"Paper page - TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://huggingface.co/papers/2604.19295"},{"title":"[2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/abs/2604.19295"},{"title":"April 22, 2026 TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/pdf/2604.19295"},{"title":"TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/html/2604.19295v1"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"[2510.07745] Parallel Test-Time Scaling for Latent Reasoning Models","url":"https://arxiv.org/abs/2510.07745"}]

I found relevant information about TEMPO. Here's what the search revealed:

## TEMPO: Scaling Test-Time Training for Large Reasoning Models

TEMPO is a test-time training (TTT) framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on a labeled dataset.

**Key Innovation:** By formalizing this alternating procedure through the Expectation-Maximization (EM) algorithm, the framework reveals that prior methods can be interpreted as incomplete variants that omit the crucial recalibration step.

**Problem Addressed:** Existing TTT methods for large reasoning models (LRMs) plateau quickly and do not benefit from additional test-time compute, as the self-generated reward signal increasingly drifts without external calibration, leading to both performance plateaus and diversity collapse.

**How It Works:** TEMPO operates in two stages: (i) Policy Refinement, where the actor generates reasoning trajectories on unlabeled test prompts and optimizes against rewards from a critic model; and (ii) Critic Recalibration, where the critic is periodically updated using verifiable rewards from a labeled dataset.

**Results:** Across diverse model families (Qwen3 and OLMO3), TEMPO improves OLMO3-7B on AIME 2024 from 33.0% to 51.1% and Qwen3-14B from 42.3% to 65.8%, while maintaining high diversity.

The paper was posted to arXiv in April 2026 (arXiv ID: 2604.19295).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c527525c-1413-483d-8c39-a4f8335c3879",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "dd77b07e-2c94-4eef-bf0d-e79b01e0b5e9",
  "toolUseResult": {
    "query": "TEMPO test-time training EM framework reasoning models 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_012HWuEwoMYQzcKWXuMh1PKM",
        "content": [
          {
            "title": "Paper page - TEMPO: Scaling Test-time Training for Large Reasoning Models",
            "url": "https://huggingface.co/papers/2604.19295"
          },
          {
            "title": "[2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models",
            "url": "https://arxiv.org/abs/2604.19295"
          },
          {
            "title": "April 22, 2026 TEMPO: Scaling Test-time Training for Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2604.19295"
          },
          {
            "title": "TEMPO: Scaling Test-time Training for Large Reasoning Models",
            "url": "https://arxiv.org/html/2604.19295v1"
          },
          {
            "title": "GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"
          },
          {
            "title": "[2510.07745] Parallel Test-Time Scaling for Latent Reasoning Models",
            "url": "https://arxiv.org/abs/2510.07745"
          }
        ]
      },
      "I found relevant information about TEMPO. Here's what the search revealed:\n\n## TEMPO: Scaling Test-Time Training for Large Reasoning Models\n\nTEMPO is a test-time training (TTT) framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on a labeled dataset.\n\n**Key Innovation:** By formalizing this alternating procedure through the Expectation-Maximization (EM) algorithm, the framework reveals that prior methods can be interpreted as incomplete variants that omit the crucial recalibration step.\n\n**Problem Addressed:** Existing TTT methods for large reasoning models (LRMs) plateau quickly and do not benefit from additional test-time compute, as the self-generated reward signal increasingly drifts without external calibration, leading to both performance plateaus and diversity collapse.\n\n**How It Works:** TEMPO operates in two stages: (i) Policy Refinement, where the actor generates reasoning trajectories on unlabeled test prompts and optimizes against rewards from a critic model; and (ii) Critic Recalibration, where the critic is periodically updated using verifiable rewards from a labeled dataset.\n\n**Results:** Across diverse model families (Qwen3 and OLMO3), TEMPO improves OLMO3-7B on AIME 2024 from 33.0% to 51.1% and Qwen3-14B from 42.3% to 65.8%, while maintaining high diversity.\n\nThe paper was posted to arXiv in April 2026 (arXiv ID: 2604.19295)."
    ],
    "durationSeconds": 11.240912641000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c527525c-1413-483d-8c39-a4f8335c3879",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-28T05:58:52.093Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me also check a few more things - the MathAtlas benchmark and DDR, and whether any existing work has already combined co-adaptive retrieval with TTRL for autoformalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd77b07e-2c94-4eef-bf0d-e79b01e0b5e9",
  "isSidechain": false,
  "requestId": "req_011CbUTKWRSFWnRXYpCzdndJ",
  "type": "assistant",
  "uuid": "f78f864b-dc3f-4f33-967d-db16a72eaa87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2cFzeP6xBvDQjCU7w6WCT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3360,
      "cache_read_input_tokens": 28053,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 28053,
          "cache_creation_input_tokens": 3360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3360
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

_source line 32 · 2026-05-28T05:58:53.353Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PfdM4ERApUeeawyjJ58xGG`</summary>

```json
{
  "query": "MathAtlas benchmark autoformalization graduate-level 2026 arXiv:2605.14061"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f78f864b-dc3f-4f33-967d-db16a72eaa87",
  "isSidechain": false,
  "requestId": "req_011CbUTKWRSFWnRXYpCzdndJ",
  "type": "assistant",
  "uuid": "c351632c-f5e7-492e-bab9-fd780f424b8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2cFzeP6xBvDQjCU7w6WCT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3360,
      "cache_read_input_tokens": 28053,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 28053,
          "cache_creation_input_tokens": 3360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3360
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

_source line 33 · 2026-05-28T05:58:53.537Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017YwFzg8KXLe2GwT46ZrE3X`</summary>

```json
{
  "query": "test-time RL formal mathematics autoformalization co-adaptive retrieval weight adaptation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c351632c-f5e7-492e-bab9-fd780f424b8f",
  "isSidechain": false,
  "requestId": "req_011CbUTKWRSFWnRXYpCzdndJ",
  "type": "assistant",
  "uuid": "cdddcf4e-e46f-4d15-8684-48ae42409831",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2cFzeP6xBvDQjCU7w6WCT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3360,
      "cache_read_input_tokens": 28053,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 28053,
          "cache_creation_input_tokens": 3360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3360
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "cdddcf4e-e46f-4d15-8684-48ae42409831",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate test-time retrieval-augmented autoformalization proposal",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Tool result

_source line 36 · 2026-05-28T05:58:59.771Z_

<details><summary>↩ Tool result · `toolu_01PfdM4ERApUeeawyjJ58xGG`</summary>

```text
Web search results for query: "MathAtlas benchmark autoformalization graduate-level 2026 arXiv:2605.14061"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data","url":"https://arxiv.org/pdf/2502.05567"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"ProofNet: Autoformalizing and Formally Proving Undergraduate-Level   Mathematics","url":"https://arxiv.org/pdf/2302.12433"},{"title":"FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://arxiv.org/pdf/2603.26996"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"}]

Based on the search results, here's what I found about MathAtlas:

MathAtlas is the first large-scale autoformalization benchmark of in the wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

Strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions.

The paper (arXiv:2605.14061) was authored by researchers from the University of California, Santa Cruz, with the paper submitted on 13 May 2026. The research addresses an important gap, as current autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c351632c-f5e7-492e-bab9-fd780f424b8f",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "5492c752-4514-4b84-a9ab-c861a2e5a7ae",
  "toolUseResult": {
    "query": "MathAtlas benchmark autoformalization graduate-level 2026 arXiv:2605.14061",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GDSdfD99cQjGDNGToUNepx",
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
            "title": "ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data",
            "url": "https://arxiv.org/pdf/2502.05567"
          },
          {
            "title": "A New Approach Towards Autoformalization",
            "url": "https://arxiv.org/pdf/2310.07957"
          },
          {
            "title": "ProofNet: Autoformalizing and Formally Proving Undergraduate-Level   Mathematics",
            "url": "https://arxiv.org/pdf/2302.12433"
          },
          {
            "title": "FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://arxiv.org/pdf/2603.26996"
          },
          {
            "title": "Reliable Evaluation and Benchmarks for Statement Autoformalization",
            "url": "https://arxiv.org/pdf/2406.07222"
          },
          {
            "title": "An Evaluation Benchmark for Autoformalization in Lean4",
            "url": "https://arxiv.org/pdf/2406.06555"
          }
        ]
      },
      "Based on the search results, here's what I found about MathAtlas:\n\nMathAtlas is the first large-scale autoformalization benchmark of in the wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.\n\nMathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.\n\nStrong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions.\n\nThe paper (arXiv:2605.14061) was authored by researchers from the University of California, Santa Cruz, with the paper submitted on 13 May 2026. The research addresses an important gap, as current autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored."
    ],
    "durationSeconds": 6.413330294,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c351632c-f5e7-492e-bab9-fd780f424b8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T05:59:05.696Z_

<details><summary>↩ Tool result · `toolu_017YwFzg8KXLe2GwT46ZrE3X`</summary>

```text
Web search results for query: "test-time RL formal mathematics autoformalization co-adaptive retrieval weight adaptation 2026"

Links: [{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/pdf/2510.10815"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/pdf/2510.04520"},{"title":"[2510.24592] ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/abs/2510.24592"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"Rango: Adaptive Retrieval-Augmented Proving for Automated Software Verification","url":"https://people.cs.umass.edu/~brun/pubs/pubs/Thompson25icse.pdf"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"}]

Based on the search results, I found several recent research papers addressing aspects of your query related to formal mathematics and autoformalization from 2025-2026:

**Key Findings:**

1. **FormaRL** - A RL-based training framework to enhance model ability of autoformalization with far less training data. The researchers created a benchmark named "uproof" bridging the gap of evaluation of out-of-distribution autoformalization for advanced math problems.

2. **DRIFT Framework** - Analysis shows that retrieval effectiveness in mathematical autoformalization depends heavily on model-specific knowledge boundaries, highlighting the need for adaptive retrieval strategies aligned with each model's capabilities. DRIFT enhances retrieval-augmented autoformalization by adapting query decomposition and context augmentation, first decomposing statements into simpler atomic sub-queries where each sub-query targets a single mathematical concept.

3. **Aria Agent** - A system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.

4. **ReForm** - Addresses reflective autoformalization, as LLMs can generate syntactically correct formal statements but often fail to preserve the original problem's semantic intent due to treating autoformalization as a simplistic translation task lacking mechanisms for self-reflection and iterative refinement.

These papers address co-adaptive retrieval strategies and weight adaptation mechanisms for autoformalization tasks in formal mathematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdddcf4e-e46f-4d15-8684-48ae42409831",
  "isSidechain": false,
  "promptId": "5e565207-5480-4dc8-93db-6a9e1a01f022",
  "type": "user",
  "uuid": "4aff14b4-7382-4c53-84d7-94497cb367c9",
  "toolUseResult": {
    "query": "test-time RL formal mathematics autoformalization co-adaptive retrieval weight adaptation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UiGo7eRhQWNszga9YcbvJZ",
        "content": [
          {
            "title": "FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/pdf/2508.18914"
          },
          {
            "title": "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://arxiv.org/pdf/2510.10815"
          },
          {
            "title": "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/pdf/2510.04520"
          },
          {
            "title": "[2510.24592] ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization",
            "url": "https://arxiv.org/abs/2510.24592"
          },
          {
            "title": "Consistent Autoformalization for Constructing Mathematical Libraries",
            "url": "https://arxiv.org/pdf/2410.04194"
          },
          {
            "title": "Rango: Adaptive Retrieval-Augmented Proving for Automated Software Verification",
            "url": "https://people.cs.umass.edu/~brun/pubs/pubs/Thompson25icse.pdf"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning ...",
            "url": "https://arxiv.org/pdf/2512.00997"
          }
        ]
      },
      "Based on the search results, I found several recent research papers addressing aspects of your query related to formal mathematics and autoformalization from 2025-2026:\n\n**Key Findings:**\n\n1. **FormaRL** - A RL-based training framework to enhance model ability of autoformalization with far less training data. The researchers created a benchmark named \"uproof\" bridging the gap of evaluation of out-of-distribution autoformalization for advanced math problems.\n\n2. **DRIFT Framework** - Analysis shows that retrieval effectiveness in mathematical autoformalization depends heavily on model-specific knowledge boundaries, highlighting the need for adaptive retrieval strategies aligned with each model's capabilities. DRIFT enhances retrieval-augmented autoformalization by adapting query decomposition and context augmentation, first decomposing statements into simpler atomic sub-queries where each sub-query targets a single mathematical concept.\n\n3. **Aria Agent** - A system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.\n\n4. **ReForm** - Addresses reflective autoformalization, as LLMs can generate syntactically correct formal statements but often fail to preserve the original problem's semantic intent due to treating autoformalization as a simplistic translation task lacking mechanisms for self-reflection and iterative refinement.\n\nThese papers address co-adaptive retrieval strategies and weight adaptation mechanisms for autoformalization tasks in formal mathematics."
    ],
    "durationSeconds": 12.156086224,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cdddcf4e-e46f-4d15-8684-48ae42409831",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-28T05:59:05.703Z_

```json
{
  "parentUuid": "4aff14b4-7382-4c53-84d7-94497cb367c9",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "006716b6-5f36-4e85-a245-9055cc0d50ea",
  "timestamp": "2026-05-28T05:59:05.703Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-28T06:00:12.927Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient information to do my evaluation. Let me synthesize what I've found.

**Summary of field research:**

1. **TTRL** (NeurIPS 2025) - Validated for informal math reasoning with majority voting. Shows 211% improvement on AIME 2024. No application to autoformalization yet.

2. **CriticLean** (arXiv:2507.06181) - Real paper, trains critic models for semantic evaluation of formalizations. CriticLeanGPT-14B-RL achieves 84.8% accuracy on balanced CriticLeanBench.


3. **DDRL** (ACL 2026 Findings) - Addresses the spurious signal amplification problem that TTRL encounters, using binary rewards instead.

4. **R3** (NeurIPS 2025) - Applies reinforced contrastive learning to optimize RAG retrieval systems.

5. **Reinforced-IR** - A framework enabling co-adaptive updates between retrievers and generators.

6. **Aria** (ICLR 2026) - Achieves state-of-the-art results on retrieval-augmented autoformalization using dependency graphs, though it relies on a static pipeline without weight adaptation.

7. **FormalEvolve** (arXiv:2603.19) - Still examining this one.

8. **FormaRL** (COLM 2025) - Applies RL to autoformalization with compilation and LLM consistency rewards.

9. **TEMPO** (arXiv:2604.19295) - Formalizes test-time training through an EM framework with critic recalibration.

10. **MathAtlas** (arXiv:2605.14061) - A very recent benchmark from May 2026 containing 52K graduate-level problems.

11. **DDR** - A dependency retrieval approach that reduces hallucination.

Now I'm assessing the novelty of combining these threads: applying TTRL to autoformalization is new, and layering co-adaptive retrieval on top of TTRL during inference creates another novel angle.

The real innovation here is recognizing that Lean 4's structured error messages can serve as graded training signals for retrieval during test-time learning—something no existing work exploits. FormaRL does RL for autoformalization but only at training time without retrieval or weight adaptation, Aria uses retrieval but statically without RL, TTRL applies test-time RL to informal math with binary rewards, and FormalEvolve adds test-time compute but doesn't adapt weights. The gap is genuine, though the combination introduces real technical hurdles like handling majority voting for formal statements, managing heterogeneous rewards, and preventing retriever drift.

The problem itself is well-motivated—MathAtlas's 2.6% performance on MA-Hard shows how severely OOD degradation affects autoformalization. The core insight about compilation errors as oracle-quality retriever training signals feels reasonably novel and non-obvious, but the overall direction of combining retrieval, RL, and test-time adaptation reads more like an integration effort than a fundamental conceptual breakthrough. I'm wondering whether reviewers would find this surprising or whether it feels like a natural next step. The proposal does explicitly address the simpler alternative of best-of-N with CriticLean filtering as a baseline comparison.

Now I'm checking the key assumptions underlying the approach: whether Lean 4's error messages will be structured enough to hit the 40% Tier 1 threshold, whether CriticLean's precision holds up under distribution shift, whether the co-adaptive retriever actually improves formalization performance, and whether GRPO can effectively handle multi-tier rewards. The proposal is thorough in identifying these assumptions and has already built in validation steps like Phase 0 calibration to address distributional shift concerns.

The core strength here is that the structured compilation errors as graded signals for retrieval is genuinely novel and fills a real gap in the literature—no one's combined these threads before. The de-risking strategy with explicit go/no-go gates is well-designed, and the structural asymmetry argument about formal versus informal feedback is compelling. That said, this reads more as an integration of four existing ideas rather than a single breakthrough insight, which might make AAAI reviewers hesitant to view it as conceptual novelty versus engineering novelty.

The system itself is quite complex—dual-loop architecture, multi-tier rewards, critic calibration, progressive curriculum—and that complexity becomes a liability if results are mixed since it's hard to isolate what's actually driving improvements. The binarize-then-enrich piece addresses a real gap in DDRL but feels somewhat incremental, and the co-adaptive retrieval, while novel to autoformalization, is largely applying existing reinforced IR techniques to a new domain. Reviewers will likely push back with the standard "you're just combining existing techniques" critique, and the heavy computational requirements might raise concerns about reproducibility and accessibility.

Weighing everything—the genuine novelty of using structured compilation errors as retrieval signals, the importance of the problem, the thorough execution—I'd estimate this lands around 30-40%. The core insight is solid and the problem matters, but it's fundamentally a well-motivated combination of existing techniques applied to a new setting rather than a conceptual breakthrough. The proposal is extremely well-crafted, but that might not be enough to overcome the integration-focused nature of the contribution. me be more precise: I'd say 28-38%, mid 33%.

Actually, let me reconsider. The structural asymmetry argument is quite strong - the insight that formal languages uniquely enable co-adaptive retrieval during TTRL because of their structured error signals is genuinely novel. This isn't just "apply X to Y" - it's identifying a fundamental capability gap between formal and informal settings and exploiting it. That pushes the novelty up.

On the other hand, the proposal is so long and complex that it risks being perceived as a "kitchen sink" paper. AAAI reviewers typically have limited time and may not fully appreciate the subtleties.

The challenge is that autoformalization is still somewhat niche within AAAI's broad scope, and finding reviewers who grasp both TTRL and this domain could be difficult. Specialists would likely see the depth, but generalists might struggle with the technical density. That uncertainty keeps me at 28-38%, with 33% as my central estimate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "006716b6-5f36-4e85-a245-9055cc0d50ea",
  "isSidechain": false,
  "requestId": "req_011CbUTM1LGUt7qFDDGNCA1u",
  "type": "assistant",
  "uuid": "67e93f6c-ff95-4694-bd0d-6d0313bbebe6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpAv2krJZju4aRNjxcrukX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 31413,
      "output_tokens": 5947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1621,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5947,
          "cache_read_input_tokens": 31413,
          "cache_creation_input_tokens": 1621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1621
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

_source line 40 · 2026-05-28T06:01:41.772Z_

Now I have sufficient research data. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- TTRL (arXiv:2504.16084, NeurIPS 2025): 奠基性工作，在无标注数据上用 majority voting 做 pseudo reward 驱动 RL，Qwen-2.5-Math-7B 在 AIME 2024 上 pass@1 提升约 211%。仅适用于有明确数值答案的 informal math，不处理 formal statement。
- DDRL (arXiv:2604.21327, ACL 2026 Findings): 发现 GRPO 在低共识域放大 spurious reward，提出频率平衡采样 + 固定 ±1 advantage + consensus off-policy refinement。明确指出"更丰富的 advantage 公式"为 future work，仅处理 binary reward。确认 proposal 对其描述准确。
- CriticLean (arXiv:2507.06181, 2025): 训练 CriticLeanGPT 模型判断 Lean 4 formalization 的语义正确性，14B-RL 在 balanced CriticLeanBench 上 84.8%。开源模型在 HuggingFace 可用。Proposal 对其 balanced vs. skewed 分布差异的担忧是合理的。
- R3 (arXiv:2510.24652, NeurIPS 2025): 用 RL 环境反馈训练 retriever 的 contrastive learning，1-shot accuracy 平均 +5.2%。验证了"RAG 环境反馈可训练 retriever"这一前提。
- Reinforced-IR (ACL 2025): 交替 RLRF/RLGF 实现 retriever-generator 共适应。验证了 co-adaptive retrieval 的可行性。
- Aria (arXiv:2510.04520, ICLR 2026): 当前 retrieval-augmented autoformalization 的 SOTA，ProofNet 91.6% compilation / 68.5% accuracy，dependency graph + iterative formalization。关键局限：静态 pipeline，retriever 不随 formalizer 演化而更新，模型权重不更新。
- FormaRL (COLM 2025): GRPO + compilation + LLM consistency reward 用于 autoformalization，pass@1 4%→26% on ProofNet。Training-time RL，无 retrieval，无 test-time adaptation。
- FormalEvolve (arXiv:2603.19828, 2026): 将 autoformalization 建模为 budgeted evolutionary search，SH@100=58.0% CombiBench。Test-time compute 但无 weight adaptation，丢弃 compilation error 结构。
- TEMPO (arXiv:2604.19295, 2026): 将 TTT 形式化为 EM 框架，证明省略 critic recalibration 导致 ELBO degradation 和 diversity collapse。概念上支持 proposal 的 dual-loop 设计。
- MathAtlas (arXiv:2605.14061, May 2026): 52K graduate-level 问题 + 178K dependency relations，MA-Hard 最佳仅 2.6%。验证了 OOD autoformalization 的严峻挑战。
- AMBER/Construction-Verification (arXiv:2602.01291, 2026): 47.3% compilation errors 来自 identifier hallucination。支持 proposal 对 Tier 1 error 占比 ≥40% 的预期。

**调研总结**: Autoformalization 领域正在沿三条轴线快速发展：(1) RL-based training (FormaRL, Wang et al.)、(2) retrieval augmentation (Aria, DDR, DRIFT)、(3) test-time compute (FormalEvolve, TTRL)。这三条轴线目前是独立的——没有工作将 test-time RL 应用于 autoformalization，也没有工作在 TTRL 中实现 co-adaptive retrieval。Proposal 定位在三者的交叉点，gap 是真实的。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是 **Best-of-N + CriticLean 过滤**：给基础模型分配等量 test-time compute 采样更多候选，用 CriticLean-14B 过滤，不做任何 weight adaptation。Proposal 已将其纳入 compute-matched baseline，这是好的。

第二个 trivial alternative 是 **static retrieval + TTRL**：直接在 autoformalization 上跑 TTRL，用 compilation-only reward，retriever 固定不更新。这实际上是 proposal 的一个 ablation。

Proposal 对这两个 trivial alternative 有明确的应对。增量价值的核心论证是：(a) weight adaptation 能产生 inference-time scaling 无法到达的 OOD 泛化（因为固定模型的输出空间可能根本不包含正确 formalization），(b) co-adaptive retrieval 利用 compilation error 的结构化信息实现 retriever-formalizer 协同进化。论证逻辑上是通的，但 (a) 的实证支撑依赖于 MathAtlas MA-Hard 2.6% 这个极端数据点，在 moderate OOD 场景下 Best-of-N 可能就够了。

**结论**: Trivial alternative 威胁在 moderate OOD 场景下存在，但在 extreme OOD 场景下 proposal 的论证成立。Proposal 意识到了这一点并设计了 compute-matched baseline。

【前提假设检验】:
核心 claim 的逻辑链有几个关键假设：

1. **"Lean 4 的 structured error 能提供 oracle-quality retrieval training signal"** — 这是最核心的假设。AMBER 的 47.3% identifier hallucination 数据和 DDR 的 Hall_m=0.21-0.39 提供了间接支撑，但这些数据来自不同模型（DeepSeek-R1 / frontier LLMs）、不同设置。在 TTRL 过程中，随着模型权重更新，error 分布会变化——proposal 的 Phase -1 micro-analysis 旨在验证这一假设，这是合理的。此假设有中等程度的实证支撑，但尚未在 TTRL 动态场景下验证。

2. **"CriticLean 在 skewed OOD 分布下仍能保持足够精度"** — CriticLeanBench 是 250/250 balanced，而 OOD TTRL 下 <10% compilable，分布偏移巨大。Proposal 用 Phase 0 calibration + confidence gating 来应对，但这仍是未经验证的假设。如果 CriticLean 在 OOD skewed 分布下 precision 不达标，整个 multi-tier reward 体系的核心组件就不成立。

3. **"Binarize-then-enrich 能有效处理 heterogeneous reward"** — 这是对 DDRL + GDPO 的嫁接，逻辑上合理但完全是未经实验验证的组合。特别是 binarization 层丢弃了 critic 的 soft signal 信息（30-70% ambiguity zone 被排除），这可能在数据稀缺的 OOD 场景下浪费宝贵的训练信号。

4. **"Co-adaptive retrieval 的收益会超过其引入的复杂性和不稳定性"** — 同时更新 formalizer 权重和 retriever 权重是一个 non-trivial 的双优化问题。R3 和 Reinforced-IR 在 QA 场景验证了可行性，但 autoformalization + TTRL 场景的 signal density 更低（50 steps × 32 candidates × ~15% compile rate ≈ 240 对/cycle），retriever 更新的样本效率是个问号。

**结论**: 假设 1 和 2 有 partial evidence 但需要 proposal 中的 de-risking phases 验证；假设 3 和 4 是更强的未验证假设。但 proposal 的 phased design 和 go/no-go gates 表明作者清楚这些风险。

【3 维度打分】:

1. **Novelty: 中偏强** —
理由：核心 insight——"formal languages 的 structured compilation errors 构成一个 graded hierarchy of adaptation signals，使得 co-adaptive retrieval 成为 TTRL 在 formal setting 中独有的 emergent capability"——是真正的 novelty。这不仅仅是"把 A 应用到 B"，而是识别了 formal vs. informal reasoning 之间的一个 structural asymmetry 并系统性地利用它。调研确认无现有工作做到这一点：Aria (ICLR 2026) 是 static retrieval，FormaRL (COLM 2025) 是 training-time RL without retrieval，FormalEvolve 丢弃 error structure，TTRL 仅处理 informal math。Gap 是真实的。

但我必须指出两个 novelty 折扣：(a) 这是一个 **combination paper**——四个独立验证的组件的首次整合。每个组件单独看（co-adaptive retrieval, TTRL, critic reward, debiased RL）都已有前人工作，novelty 来自组合而非单个突破。AAAI 审稿人可能以"engineering novelty"而非"conceptual novelty"定性。(b) "Binarize-then-enrich"这个贡献虽然填补了 DDRL 的 explicit future work gap，但本身较为 incremental——本质是在 DDRL 的 binary framework 上叠加 GDPO 的 per-reward normalization。

2. **Significance: 中偏强** —
理由：OOD autoformalization 是一个重要且日益突出的问题。MathAtlas MA-Hard 2.6%（arXiv:2605.14061）量化了现有方法在 graduate-level 数学上的惨淡表现。如果 TTRA 能在 OOD 域上显著提升 autoformalization 质量，对 formal mathematics、AI for math、proof assistants 社区都有实际影响。

Test-time adaptation 作为 formal math 的"第三 scaling axis"（complementing training-time 和 inference-time compute）的 framing 具有概念上的吸引力，并与 TEMPO (arXiv:2604.19295) 的 TTT 叙事相呼应。

但 significance 的上限受限于：autoformalization 仍是一个相对 niche 的子领域。虽然 AAAI 作为综合 AI 会议接受范围很广，但 reviewer pool 中深度理解 Lean 4 + TTRL + retrieval 这个交叉点的人有限。如果 reviewer 不具备足够背景，可能低估 contribution。

3. **Related Work: 强** —
理由：Proposal 对 related work 的覆盖在我调研范围内是全面且准确的。所有我查证的关键论文（TTRL、CriticLean、DDRL、R3、Reinforced-IR、Aria、FormaRL、FormalEvolve、TEMPO、MathAtlas、AMBER）均真实存在，描述准确，差异化定位清晰。Proposal 不仅列出了竞争工作，还精确指出了每个工作的局限性与 TTRA 的差异。对 6 个子方向（RL for autoformalization, semantic critics, debiased RL, retrieval-augmented autoformalization, test-time compute, error analysis）的分类组织清晰。

特别值得肯定的是：proposal 将最近的工作（TEMPO April 2026, MathAtlas May 2026, Dymetman May 2026）也纳入了 landscape 分析，说明作者持续跟踪领域动态。唯一的小缺陷是部分引用密度过高，可能在实际论文中需要精简以保持可读性。

【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
Novelty 是"中偏强"而非"强"，因为这本质是一个 combination/integration paper。核心 insight（structural asymmetry enabling co-adaptive retrieval as emergent TTRL capability）是真正的 novelty，但四个组件的整合属于 system-level contribution。AAAI 审稿人对 combination novelty 的接受度因人而异。Significance 在 autoformalization 社区内是强的，但受限于子领域的 niche 程度。Related work 覆盖出色，不构成扣分因素。

上界受限于 **Novelty 的 combination 性质**：如果审稿人认为"each piece exists, you just put them together"，evaluation 无论多精致都无法拯救。下界受支撑于 **gap 的真实性和 insight 的原创性**：no existing work exploits structured compilation errors for co-adaptive retrieval during TTRL，这一点在领域调研中得到了确认。

【主要风险】:
1. **"Lego novelty" 批评**：审稿人可能认为 TTRA 是四个现有技术（TTRL + co-adaptive retrieval + CriticLean + DDRL/GDPO）的工程整合，而非概念突破。Proposal 对 structural asymmetry 的论述需要在论文中更加突出以对冲这一批评。
2. **系统复杂性与可归因性**：dual-loop + multi-tier reward + progressive curriculum + critic calibration 的复杂度极高。如果实验结果是 moderate improvement，审稿人难以判断哪个组件真正起作用；如果是 negative 或 mixed result，复杂性本身成为攻击面（"too many moving parts, unclear what matters"）。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67e93f6c-ff95-4694-bd0d-6d0313bbebe6",
  "isSidechain": false,
  "requestId": "req_011CbUTM1LGUt7qFDDGNCA1u",
  "type": "assistant",
  "uuid": "7ceb6d62-58b6-4807-9dc0-29cb69065c86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpAv2krJZju4aRNjxcrukX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 31413,
      "output_tokens": 5947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1621,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5947,
          "cache_read_input_tokens": 31413,
          "cache_creation_input_tokens": 1621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1621
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "7ceb6d62-58b6-4807-9dc0-29cb69065c86",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate test-time retrieval-augmented autoformalization proposal",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "7ceb6d62-58b6-4807-9dc0-29cb69065c86",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate test-time retrieval-augmented autoformalization proposal",
  "sessionId": "29610d22-ae32-421a-8d2b-c4122dd5c431"
}
```

---
