# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # TTRA: Critic-Guided Test-Time Ret

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/40328dc9-f852-4865-9336-216d513967f9.jsonl`
- **Structured JSON:** [`7c35e43a560d8a64ecc8.json`](../../sessions/7c/7c35e43a560d8a64ecc8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:58:00.193Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:58:00.193Z",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization\n\n## Core Problem\n\nCurrent autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in multi-tier reward settings; and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation.\n\nA key structural asymmetry motivates our approach: in informal math reasoning, TTRL obtains only binary correct/incorrect signals with no information about *why* a solution failed or *what knowledge is missing*—and binary rewards create a fundamental degeneracy for policy gradient methods, leading to diversity collapse (Dymetman, arXiv:2605.02375). In contrast, Lean 4's compiler produces machine-parseable error messages that precisely identify missing identifiers, type mismatches, and unresolved typeclass instances—constituting a graded hierarchy of structured feedback signals. Critically, these signals are not merely \"richer rewards\": when a compilation error reports `unknownIdentifier \"Finset.sum_bij\"`, it provides an oracle-quality, token-level retrieval training signal that directly specifies which Mathlib dependency is needed. Such signals are unavailable during pre-training or SFT (no compilation feedback), discarded by inference-time search methods like FormalEvolve (which uses only compile success/failure), and unexploited by static retrieval pipelines like Aria (whose retriever cannot adapt). Only during test-time RL can these structured error signals be continuously collected and used to co-adapt the retriever—making co-adaptive retrieval an emergent capability uniquely enabled by TTRL in formal language settings.\n\nFor domains where model performance is extremely low (MathAtlas MA-Hard: 2.6%), inference-time scaling alone is insufficient: the fixed model's output space may not contain correct formalizations for truly OOD domains, so no amount of sampling can find what the model cannot generate. Weight adaptation is necessary, and it produces compounding improvement—better formalizations yield more informative compilation errors, which improve the retriever, which enables even better formalizations in subsequent rounds.\n\n## Research Opportunity\n\nFour independently validated capabilities have never been combined, and their integration is enabled by the structured feedback properties unique to formal languages.\n\n(1) **Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode.** R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv:2601.11443, Jan 2026) shows test-time retrieval adaptation via self-supervised prediction. The prevalence of identifier hallucination is established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math stem from hallucination of non-existent theorems/definitions. DDR (arXiv:2511.11990) quantifies Hall_m=0.21-0.39 across frontier LLMs, reduced to <0.02 with retrieval. The RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as a primary error class. MathAtlas (arXiv:2605.14061, May 2026) shows a 66% advantage for Mathlib-grounded definitions (27.9% vs 16.8%, p<0.001). Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL—where Lean's structured error taxonomy provides graded, machine-parseable signals for retriever training.\n\n(2) **TTRL with debiasing has advanced but remains limited to binary rewards in informal settings.** DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed ±1 advantages, and consensus-based off-policy refinement (19.0% relative improvement over ETMR on AIME 2024; 4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B), but assumes binary rewards with 'more expressive advantage formulations' left as future work. GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization but does not address debiasing. T³RL (arXiv:2603.02203, Mar 2026) introduces tool-verified rewards into TTRL, using code execution output to upweight verified rollouts—but collapses all tool feedback into a single binary bit (verified/unverified), discarding the internal structure of tool output. SCOPE (arXiv:2512.15146, Dec 2025) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, but remains within the homogeneous binary-reward paradigm. The combination of DDRL's debiasing with GDPO's multi-reward normalization for heterogeneous reward components (hard binary gate + noisy soft critic + drifting population statistic) has not been attempted.\n\n(3) **CriticLean provides the missing semantic reward signal.** CriticLeanGPT-14B-RL (arXiv:2507.06181, July 2025) achieves 84.8% accuracy on balanced CriticLeanBench (87.0% for 32B), but CriticLeanBench's 250/250 balanced distribution differs from OOD TTRL's heavily skewed distribution (<10% compilable). This distributional shift gap motivates our Phase 0 calibration protocol.\n\n(4) **Online RL for autoformalization validated at training time only.** Wang et al. (NeurIPS 2025 MAR Workshop) achieves TC1: 17.29%→26.01% on RLMEval using GRPO with BEq + embedding rewards, but operates at training time on in-distribution problems without retrieval, test-time adaptation, or a trained semantic critic.\n\nRecent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.\n\n## Research Landscape\n\n**(1) RL for autoformalization.** FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards (pass@1: 4%→26% on ProofNet). Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with BEq + embedding similarity (TC1: 17.29%→26.01%, TC50: 76.41%→85.46% on RLMEval)—closest prior work but training-time, no retrieval, no test-time adaptation. ReForm (arXiv:2510.24592) applies PBSO position-aware RL rewards for reflective autoformalization; ReForm-8B (Qwen3-8B) achieves +18.0pp average improvement.\n\n**(2) Semantic critics and iterative refinement.** CriticLean (July 2025) introduces CriticLeanGPT (32B-RL: 87.0%, 14B-RL: 84.8% on balanced CriticLeanBench). ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO. Monotonic Refinement achieves 90.27% on miniF2F through multi-model ensemble orchestration. These cannot adapt model weights to new domains.\n\n**(3) Debiased RL, multi-reward optimization, and TTRL reward improvements.** DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification exclusively with binary rewards; GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward normalization. Binary Rewards and RL (Dymetman, arXiv:2605.02375, May 2026) proves binary rewards create fundamental degeneracy (diversity collapse). T³RL (arXiv:2603.02203, Mar 2026) introduces external tool verification into TTRL, upweighting verified rollouts via verification-aware voting—but treats tool output as a single binary signal (verified/unverified), discarding the structured content of tool feedback. SCOPE (arXiv:2512.15146) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, remaining within the homogeneous binary-reward paradigm. All these improvements assume homogeneous reward signals. TTRA addresses a qualitatively different problem: heterogeneous reward components (hard compilation gate, noisy critic signal, policy-drifting BEq statistic) requiring a two-layer binarize-then-enrich adaptation.\n\n**(4) Retrieval-augmented autoformalization and co-adaptive retrieval.** Aria (ICLR 2026, arXiv:2510.04520) achieves ProofNet 91.6% compilation / 68.5% accuracy and 42.9% on homological conjectures (vs. 0% for all others) via dependency graph + iterative formalization + AriaScorer—current frontier of retrieval-augmented autoformalization, but a fixed inference pipeline: retriever does not adapt to formalizer's evolving behavior and model weights are not updated. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF. DDR builds a 500K-sample dataset (Hall_m reduced from 0.21-0.39 to <0.02). CRAMF indexes 26K+ Mathlib definitions. ProofBridge (ICLR 2026, arXiv:2510.15681) uses joint embeddings + retrieval-augmented fine-tuning. On co-adaptive retrieval: R3 (NeurIPS 2025, arXiv:2510.24652) optimizes RAG retrieval via reinforced contrastive learning; Reinforced-IR (ACL 2025) alternates RLRF/RLGF; TTARAG (arXiv:2601.11443) demonstrates test-time retrieval adaptation. None applied to autoformalization or Lean 4.\n\n**(5) Test-time compute for autoformalization.** FormalEvolve (arXiv:2603.19828, Mar 2026) formulates autoformalization as budgeted evolutionary search (SH@100=58.0% CombiBench, 84.9% ProofNet) using LLM-driven mutation/crossover with AST rewrites. This is orthogonal to TTRA: FormalEvolve searches a fixed model's output space without weight adaptation or retriever co-adaptation, discarding compilation error structure. TEMPO (arXiv:2604.19295, Apr 2026) formalizes test-time training as EM (policy refinement = M-step, critic recalibration = E-step), proving that omitting recalibration leads to ELBO degradation and diversity collapse—a conceptual parallel to TTRA's dual-loop where omitting retriever co-adaptation (= static retrieval TTRL) accumulates retriever-formalizer distribution mismatch.\n\n**(6) Error analysis and identifier hallucination.** The AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are identifier hallucination (32.7% competence, 15.2% incomplete, 4.8% syntax). RAutoformalizer (ICLR 2025 Spotlight) categorizes errors into 'Hallucination' vs 'Others'. MathAtlas (arXiv:2605.14061) introduces 52K graduate-level problems (best: 2.6% on MA-Hard).\n\nAfter exhaustive search through May 2026, no work combines co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, a calibrated semantic critic with distributional shift analysis, principled adaptation of binary-reward debiased RL to heterogeneous multi-tier rewards, and test-time adaptation on unlabeled OOD domains. Existing retrieval methods (Aria, DRIFT, DDR) use static retrievers; existing RL methods (FormaRL, Wang et al., ReForm) operate at training time; existing test-time methods (FormalEvolve) search without learning; existing TTRL improvements (T³RL, SCOPE, DDRL) assume homogeneous binary rewards.\n\n## Proposed Approach\n\nWe propose TTRA (Test-Time Retrieval-Augmented autoformalization), making TTRL viable for autoformalization through three technical innovations unified by a single insight: formal languages' structured compilation feedback creates a graded hierarchy of adaptation signals unavailable in informal reasoning, enabling co-adaptive test-time learning as a new scaling axis for formal mathematics—complementing training-time compute (more data, larger models) and inference-time compute (more samples, longer search). Drawing a conceptual parallel with TEMPO's EM formalization of TTT, TTRA's dual-loop design ensures the retriever co-adapts with the formalizer (analogous to not omitting the E-step), preventing the retriever-formalizer distribution mismatch that would degrade a static-retrieval TTRL.\n\n**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Quantify Lean 4 error taxonomy coverage on OOD domains. Compile 500 candidate formalizations on Con-NF and 500 on MathAtlas MA-Hard, classify errors into: Tier 1 (direct identifier: `lean.unknownIdentifier`, `unknown namespace`), Tier 2 (type-based: `type mismatch`, `failed to synthesize instance`), Tier 3 (indirect: tactic/elaboration/syntax errors). Thresholds: Tier 1 ≥40% → co-adaptive retrieval well-supported; 20-40% → rely on Tier 1+2; <20% → fall back to Tier 2 with type-signature matching. Prior evidence strongly supports ≥40% (AMBER: 47.3%; DDR: Hall_m=0.21-0.39; RAutoformalizer treats 'Hallucination' as primary class; CRAMF documents systematic fabrication). Phase -1 validates on our specific model/domain. Simultaneously verify MathAtlas MA-Hard gold formalization coverage; if <50%, downgrade to secondary benchmark and activate IndiMathBench (arXiv:2512.00997) as contingency OOD benchmark. Resource: ~8 A100-hours generation, ~10 CPU-hours parsing.\n\n**Phase 0 — Minimal Pilot with Critic Calibration (De-risking).** FormaRL's GRPO pipeline with CriticLean-14B replacing LLM-consistency reward. 200 Con-NF + 200 FormalMATH number theory problems. Primary hypothesis: ≥3pp BEq@1 over compilation-only GRPO on Con-NF. Critic calibration under distributional shift: measure precision/recall separately on skewed distribution (<10% compilable); report calibration curves; if precision <80%, introduce confidence gating >0.8. Go/no-go: proceed only if primary hypothesis confirmed AND precision ≥80%. Additionally, establish critic calibration monitoring protocol: during subsequent TTRL phases, checkpoint critic precision every ~100 GRPO steps; if precision drops >10pp from Phase 0 baseline, adjust confidence threshold (periodic recalibration, motivated by TEMPO's finding that reward signal drift without recalibration leads to performance plateaus). Resource: ~50 A100-hours, 2-3 weeks.\n\n**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune Qwen3-8B using DDR's 500K-sample dataset and GRPO with R(y, x) = r_compile × (α·r_critic + β·r_beq). r_compile ∈ {0,1} (Kimina Lean Server, 128 parallel workers); r_critic ∈ {0,1} (CriticLeanGPT-Qwen3-14B-RL, gated by Phase 0 threshold); r_beq ∈ [0,1] (BEq consensus density). α=0.7, β=0.3. Fallback: when <4 of K=32 compile, R = r_compile × r_critic.\n\n**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever (DDR-style dense encoder) is explicitly updated during TTRL. This exploits Lean 4's unique structural property: compilation errors provide oracle-quality, token-level retrieval training signals that directly specify which Mathlib dependencies are needed—signals unavailable during pre-training, discarded by inference-time search, and unexploited by static retrieval pipelines.\n\n  Loop 1 — Formalizer GRPO (every step): K=32 candidates, compile, multi-tier rewards, debiased GRPO.\n\n  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Graded error hierarchy:\n    (a) Tier 1 (highest confidence): `lean.unknownIdentifier` names missing constant → hard negatives from retrieved set; constant from CRAMF/DDR index = positive. `unknown namespace` → coarser module-level positive.\n    (b) Tier 2 (moderate): `type mismatch` → type signatures matched against Mathlib type index, 0.5× weight. `failed to synthesize instance` → typeclass instances as positives.\n    (c) Tier 3: tactic/elaboration/syntax → negatives only.\n    (d) Compilation success → all retrieved dependencies in compiled output = confirmed positives.\n    (e) Weighted InfoNCE: L = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), w_k = 1.0 (Tier 1/confirmed), 0.5 (Tier 2), τ=0.07.\n    (f) Decoupled optimization (per R3 and Reinforced-IR): retriever gradient does not flow through formalizer. FAISS rebuild after each update.\n\n  Signal density: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle.\n\n**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** Autoformalization's reward components are fundamentally heterogeneous: compilation is a hard binary gate (non-negotiable), the critic is a noisy soft signal (calibrated but imperfect), BEq is a population statistic (drifts with policy). This heterogeneity distinguishes TTRA from all existing TTRL reward improvements (DDRL, T³RL, SCOPE, GDPO), which assume homogeneous reward signals. Neither DDRL alone (cannot handle multi-tier) nor GDPO alone (does not address spurious amplification) suffices:\n\n  (a) Binarization layer: r_accept = I(r_compile=1 AND r_critic=1). Balanced sampling (exclude 30-70% ambiguity zone per DDRL). Fixed advantages: +1 (accepted), -1 (rejected). Consensus off-policy refinement: M=128, rejection-sample >80% acceptance, SFT 5 epochs.\n  (b) GDPO-style enrichment: among accepted candidates, per-reward decoupled normalization for BEq. Additive bonus δ·norm(r_beq) to +1 advantage, δ=0.3.\n\n**Phase 4 — Progressive Domain Curriculum.** (a) Near-distribution warm-start: compilation ≥40%, critic approval ≥60%, BEq@32 ≥3pp above baseline. Timeout: 500 steps. (b) Retrieval bootstrapping: Tier 1/2 errors feed retriever updates. Transition: recall@10 ≥30%, compilation ≥25%. Early transition: plateau <2pp over 200 steps. (c) Far-OOD: algebraic geometry, condensed mathematics, MathAtlas MA-Hard with adaptive fallback.\n\n**Contribution Floor Analysis.** (1) Co-adaptive retrieval + CriticLean TTRL alone: first co-adaptive retrieval for autoformalization + first TTRL for formal math with calibrated critic. (2) Binarize-then-enrich alone: addresses DDRL's explicit future work on multi-tier rewards. (3) Curriculum: droppable. (4) Essential floor: CriticLean TTRL outperforms compilation-only (Phase 0 gate) AND ≥1 of co-adaptive retrieval / binarize-then-enrich shows statistically significant improvement.\n\n**Evaluation.**\n\n  *Benchmarks:* In-distribution: miniF2F-test (244), ProofNet (~371). Multi-domain: FormalMATH (5,560). OOD stress tests: Con-NF, CombiBench, MathAtlas MA-Hard (700 entities, best: 2.6%; contingency: IndiMathBench if gold coverage <50%).\n\n  *Metrics:* BEq@K, BEq+@K (per DRIFT), pass@K (K=1,32), compilation@K on all benchmarks. GTED (arXiv:2507.07399, continuous [0,1] similarity with better precision-recall balance than BEq) on OOD benchmarks. Hall_m (DDR's hallucination rate) in retriever ablation. Human evaluation: 100-150 samples on Con-NF + 200 samples on MathAtlas MA-Hard (inter-annotator agreement reported).\n\n  *Same-scale primary baselines (~7-8B):* (1) FormaRL (Qwen2.5-Coder-7B, COLM 2025); (2) Online RL for Autoformalization (Wang et al., faithfully reimplemented if code unavailable); (3) DRIFT with Qwen3-8B (ICLR 2026); (4) Aria (ICLR 2026, reimplemented on shared benchmarks or reported numbers annotated); (5) StepFun-Formalizer-7B (AAAI 2026, open-source); (6) ReForm-8B (Qwen3-8B, arXiv:2510.24592); (7) compilation-only TTRL and critic-only TTRL ablations.\n\n  *Cross-paradigm reference:* FormalEvolve (arXiv:2603.19828, reported SH@100 on CombiBench/ProofNet).\n\n  *Compute-matched baseline:* Best-of-N (matched FLOPs) + CriticLean filtering: allocate equivalent test-time compute to sampling more candidates from base formalizer, filter with CriticLean-14B, report BEq@1 and compilation@1. Directly tests whether TTRA's weight adaptation provides value beyond inference-time scaling.\n\n  *Ablations:* (a) Standard GRPO vs. DDRL vs. binarize-then-enrich (component-wise); (b) frozen vs. co-adaptive retriever; (c) Tier 1-only vs. Tier 1+2 vs. all-tier error signals; (d) no curriculum vs. progressive; (e) CriticLean-14B reward vs. embedding-based similarity reward (isolating trained critic value).\n\n  *Sensitivity:* N_ret ∈ {25, 50, 100}; δ ∈ {0.0, 0.1, 0.3, 0.5} (δ=0.0 = pure DDRL); ambiguity zone ∈ {[20%-80%], [30%-70%], [40%-60%]}; critic confidence threshold ∈ {0.6, 0.7, 0.8, 0.9}; K ∈ {16, 32, 64} (test-time compute scaling behavior).\n\n  *Cross-scale references:* ATF-32B, ATLAS (NeurIPS 2025), Monotonic Refinement (multi-model ensemble). All tables annotate scale and compute.\n\n  *Statistical rigor:* Key comparisons ≥3 seeds, mean ± std, bootstrap CI (p<0.05).\n\n## Detailed Description\n\nTTRA makes TTRL viable for autoformalization by exploiting a structural asymmetry: Lean 4's compiler provides oracle-quality, token-level feedback (identifier names, type signatures, typeclass requirements) that serves simultaneously as retriever training signal, multi-tier reward components, and domain adaptation indicators—signals unavailable in informal reasoning and unexploited by existing methods. The dual-loop architecture co-adapts the retriever during test-time RL via weighted InfoNCE over Lean 4's error hierarchy, addressing the limitation that static retrievers (Aria, DRIFT, DDR) cannot track formalizer evolution. CriticLean-14B integration includes distributional shift calibration and periodic drift monitoring (motivated by TEMPO's EM analysis of reward signal degradation). Binarize-then-enrich addresses the specific gap between DDRL (binary debiasing) and GDPO (multi-reward normalization) for formal verification's heterogeneous reward landscape—a qualitatively different problem from the homogeneous-reward improvements in T³RL and SCOPE. Compute-matched evaluation against best-of-N + critic filtering directly tests whether weight adaptation provides value beyond inference-time scaling. The framework positions test-time learning as a third scaling axis for formal mathematics alongside training-time and inference-time compute.\n\n## Key References\n\n- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)\n- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)\n- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, NVIDIA, January 2026)\n- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv:2507.06181, ByteDance/Nanjing)\n- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)\n- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv:2510.24652)\n- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)\n- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv:2601.11443, January 2026)\n- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv:2602.01291, February 2026)\n- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)\n- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\n- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)\n- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)\n- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\n- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)\n- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv:2511.11990)\n- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)\n- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)\n- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)\n- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\n- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv:2505.02735)\n- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)\n- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\n- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026, arXiv:2510.04520)\n- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026, arXiv:2510.15681)\n- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv:2510.24592)\n- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv:2512.00997, Microsoft Research)\n- FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv:2603.19828, March 2026)\n- Binary Rewards and Reinforcement Learning: Fundamental Challenges (Dymetman, arXiv:2605.02375, May 2026)\n- TEMPO: Scaling Test-time Training for Large Reasoning Models (arXiv:2604.19295, April 2026)\n- T³RL: Tool Verification for Test-Time Reinforcement Learning (arXiv:2603.02203, March 2026)\n- SCOPE: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning (arXiv:2512.15146, December 2025)\n- GTED: Generalized Tree Edit Distance: A Faithful Evaluation Metric for Statement Autoformalization (arXiv:2507.07399)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1400-1900 A100-80GB hours (Phase -1 micro-analysis + MathAtlas coverage: ~10h; Phase 0 pilot + calibration: ~50h; Phase 1 base GRPO: ~300h; DDR retriever + co-adaptive updates: ~100h; Phase 4 progressive TTRL + ablations: ~400h; CriticLean-14B inference all phases: ~200-300h; N_ret/δ/ambiguity/critic-threshold/K sensitivity: ~100h; baseline evaluation (Aria reimpl + StepFun + ReForm): ~100-120h; compute-matched best-of-N baseline: ~30h; CriticLean vs embedding ablation: ~25h; multi-seed (3 seeds × key ablations): ~200h; human eval annotation: ~60-80h; miniF2F/ProofNet + remaining eval: ~80h) + 15,000-20,000 CPU-hours Lean verification (Kimina Lean Server), timeline: 14-18 weeks (0.5 wk Phase -1; 2-3 wk Phase 0 + go/no-go; 3 wk Phase 1; 2 wk retriever infrastructure; 4 wk TTRL experiments; 3 wk ablations + sensitivity + multi-seed; 2 wk writing), estimated_gpu_cost: $2,800-$4,700 + $750-$1,000 CPU + ~$1,500-$2,500 human annotation. GPU architecture: policy (8B) + ref (8B) on 4×A100 tensor parallel, CriticLean-14B on dedicated 2×A100 with vLLM batch inference, retriever + FAISS on CPU/1×A100; async pipeline.\n- **human_in_loop**: gpu_hours: 1100-1500 A100-80GB hours (~25% reduction), timeline: 11-14 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,200-$3,700 + $600-$800 CPU + ~$1,200-$2,000 annotation\n- **auto_research**: gpu_hours: 2000-2700 A100-80GB hours (full sweep), timeline: 8-11 weeks, claude_api_cost: $800-$1,200, estimated_gpu_cost: $4,000-$6,700 + $1,000-$1,350 CPU + ~$1,500-$2,500 annotation, speed_bottleneck: Lean 4 compilation (~3.65s/statement warm cache, ~0.10s amortized at 64 workers). CriticLean-14B ~0.5s/candidate (→~0.1-0.2s with vLLM). Retriever co-adaptation ~15 min/cycle (re-encode 26K constants, rebuild FAISS)."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:58:00.269Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:58:00.269Z",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-28T05:58:00.628Z_

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
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "46c42566-53a2-44be-970a-39bca489d772",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:58:00.626Z_

```json
{
  "parentUuid": "46c42566-53a2-44be-970a-39bca489d772",
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
  "uuid": "245cbcb4-75eb-4079-8f36-d6275701be8f",
  "timestamp": "2026-05-28T05:58:00.626Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:58:00.626Z_

```json
{
  "parentUuid": "245cbcb4-75eb-4079-8f36-d6275701be8f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1967ecb9-1ff3-45b3-bc87-2f281635d997",
  "timestamp": "2026-05-28T05:58:00.626Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
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
  "leafUuid": "1967ecb9-1ff3-45b3-bc87-2f281635d997",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal objective acceptance likelihood",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Assistant

_source line 8 · 2026-05-28T05:58:08.695Z_

<details><summary>Logged reasoning block</summary>

```text
This is a complex research proposal about Test-Time Retrieval-Augmented RL for Autoformalization. I need to evaluate it as the "入口评审 agent" (Entry Triage Agent). Let me first do the required web searches to understand the field before making any assessments.

Let me search for:
1. Recent work on TTRL (Test-Time Reinforcement Learning) and autoformalization
2. Co-adaptive retrieval in RAG settings
3. CriticLean and semantic critics for formal math
4. DDRL and debiased RL methods
5. The key competing works mentioned (Aria, FormalEvolve, etc.)


6. I'll need to load the WebSearch tool to start gathering information on these topics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1967ecb9-1ff3-45b3-bc87-2f281635d997",
  "isSidechain": false,
  "requestId": "req_011CbUTGCFhxcfCUd5bwGpis",
  "type": "assistant",
  "uuid": "bae3baa5-f175-43a8-8c48-6efb911d1ace",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcC44Z9QyH6aiKcqqWuuD9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9782,
      "cache_read_input_tokens": 13968,
      "output_tokens": 253,
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
          "output_tokens": 253,
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

_source line 9 · 2026-05-28T05:58:08.697Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LpgqNFL9K1VGqoAgxRfRq9`</summary>

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
  "parentUuid": "bae3baa5-f175-43a8-8c48-6efb911d1ace",
  "isSidechain": false,
  "requestId": "req_011CbUTGCFhxcfCUd5bwGpis",
  "type": "assistant",
  "uuid": "2a0d7490-7028-4147-a3ac-6968d2307a21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcC44Z9QyH6aiKcqqWuuD9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9782,
      "cache_read_input_tokens": 13968,
      "output_tokens": 253,
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
          "output_tokens": 253,
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

_source line 10 · 2026-05-28T05:58:08.706Z_

<details><summary>↩ Tool result · `toolu_01LpgqNFL9K1VGqoAgxRfRq9`</summary>

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
  "parentUuid": "2a0d7490-7028-4147-a3ac-6968d2307a21",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "45d716d4-4f36-4cc9-958c-aa264373b131",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "2a0d7490-7028-4147-a3ac-6968d2307a21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-28T05:58:27.494Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required 3-5 web searches to understand the field before making any assessments. I'll search for:

1. TTRL (Test-Time Reinforcement Learning) for math reasoning - recent advances
2. Autoformalization with RL - recent work (FormaRL, TTRL for formal math)
3. Co-adaptive retrieval in RAG - R3, Reinforced-IR, TTARAG
4. CriticLean for mathematical formalization
5. DDRL debiased GRPO and multi-reward RL

Let me run these searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45d716d4-4f36-4cc9-958c-aa264373b131",
  "isSidechain": false,
  "requestId": "req_011CbUTGygh8PBkEpZo7rNAg",
  "type": "assistant",
  "uuid": "78fc37ee-874f-40d9-88cf-22502c42df2d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEtDPchGga2ysnmP7tHHsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 23750,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 12 · 2026-05-28T05:58:28.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EhP4J4HzA6r5wuPM3ah5kx`</summary>

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
  "parentUuid": "78fc37ee-874f-40d9-88cf-22502c42df2d",
  "isSidechain": false,
  "requestId": "req_011CbUTGygh8PBkEpZo7rNAg",
  "type": "assistant",
  "uuid": "d3f1bda7-61a8-42b3-8072-8d9571e8370f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEtDPchGga2ysnmP7tHHsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 23750,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 13 · 2026-05-28T05:58:29.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R4GnmjTRvf8W8QV8sjYtnN`</summary>

```json
{
  "query": "DDRL debiased GRPO test-time RL spurious signal amplification ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f1bda7-61a8-42b3-8072-8d9571e8370f",
  "isSidechain": false,
  "requestId": "req_011CbUTGygh8PBkEpZo7rNAg",
  "type": "assistant",
  "uuid": "a4af96bb-bf29-4e4b-a10e-1ae006ac8e2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEtDPchGga2ysnmP7tHHsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 23750,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 14 · 2026-05-28T05:58:29.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VxzxhW6XjxQsWVnAZTDoD7`</summary>

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
  "parentUuid": "a4af96bb-bf29-4e4b-a10e-1ae006ac8e2b",
  "isSidechain": false,
  "requestId": "req_011CbUTGygh8PBkEpZo7rNAg",
  "type": "assistant",
  "uuid": "61cd1312-533d-438c-9b6e-d82d9bce1940",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEtDPchGga2ysnmP7tHHsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 23750,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 15 · 2026-05-28T05:58:31.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018kMigik2CCfJ9DCJ19EDYT`</summary>

```json
{
  "query": "co-adaptive retrieval RAG reinforcement learning R3 Reinforced-IR TTARAG 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61cd1312-533d-438c-9b6e-d82d9bce1940",
  "isSidechain": false,
  "requestId": "req_011CbUTGygh8PBkEpZo7rNAg",
  "type": "assistant",
  "uuid": "3950d2dd-8d8c-4807-91e6-af20a9e59968",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEtDPchGga2ysnmP7tHHsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 23750,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 16 · 2026-05-28T05:58:31.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VYPz9kYJ947p9gnXXATs9a`</summary>

```json
{
  "query": "Aria ICLR 2026 autoformalization retrieval dependency graph FormalEvolve evolutionary search"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3950d2dd-8d8c-4807-91e6-af20a9e59968",
  "isSidechain": false,
  "requestId": "req_011CbUTGygh8PBkEpZo7rNAg",
  "type": "assistant",
  "uuid": "3b6d500c-4016-49f5-9682-9810bac890e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEtDPchGga2ysnmP7tHHsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 23750,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 17 · 2026-05-28T05:58:35.448Z_

<details><summary>↩ Tool result · `toolu_01EhP4J4HzA6r5wuPM3ah5kx`</summary>

```text
Web search results for query: "TTRL test-time reinforcement learning autoformalization Lean 4 2025 2026"

Links: [{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"(PDF) Online Reinforcement Learning for Autoformalization","url":"https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"},{"title":"TTRL: Test-Time Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=VuVhgEiu20"},{"title":"[2504.16084] TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2504.16084"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/html/2406.01940v1"},{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Kimina-Prover: Applying Test-time RL Search on Large Formal Reasoning Models","url":"https://huggingface.co/blog/AI-MO/kimina-prover"},{"title":"Olympiad-level formal mathematical reasoning with reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09833-y"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"}]

I found several relevant results about TTRL (Test-Time Reinforcement Learning) and autoformalization in Lean 4. Here's what the search revealed:

## TTRL (Test-Time Reinforcement Learning)

TTRL is a novel method for training LLMs using RL on unlabeled data, and it enables self-evolution of LLMs by utilizing the priors in the pre-trained models. Common practices in Test-Time Scaling (TTS), such as majority voting, yield surprisingly effective rewards suitable for driving RL training.

## TTRL and Autoformalization in Lean 4

For the most difficult problems, TTRL is a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation. The Test-Time Reinforcement Learning (TTRL) search framework enables the model to discover, combine, and reuse multiple intermediate lemmas autonomously.

## Recent Achievements (2025-2026)

Recent systems achieved 92.2% on MiniF2F with full Test-Time RL, and in 2025, multiple independent systems achieved gold-medal equivalent performance with formally verified Lean 4 proofs.

Recent work has studied online reinforcement learning for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4, with approaches addressing the challenges of reward formulation in this domain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3f1bda7-61a8-42b3-8072-8d9571e8370f",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "e21bfa90-a0a9-4320-b80f-2bd3c734782d",
  "toolUseResult": {
    "query": "TTRL test-time reinforcement learning autoformalization Lean 4 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011MTkjiE1rukbHZiPLvnheX",
        "content": [
          {
            "title": "Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics",
            "url": "https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"
          },
          {
            "title": "(PDF) Online Reinforcement Learning for Autoformalization",
            "url": "https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"
          },
          {
            "title": "TTRL: Test-Time Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=VuVhgEiu20"
          },
          {
            "title": "[2504.16084] TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/abs/2504.16084"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/html/2406.01940v1"
          },
          {
            "title": "[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning",
            "url": "https://arxiv.org/abs/2603.24372"
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
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          }
        ]
      },
      "I found several relevant results about TTRL (Test-Time Reinforcement Learning) and autoformalization in Lean 4. Here's what the search revealed:\n\n## TTRL (Test-Time Reinforcement Learning)\n\nTTRL is a novel method for training LLMs using RL on unlabeled data, and it enables self-evolution of LLMs by utilizing the priors in the pre-trained models. Common practices in Test-Time Scaling (TTS), such as majority voting, yield surprisingly effective rewards suitable for driving RL training.\n\n## TTRL and Autoformalization in Lean 4\n\nFor the most difficult problems, TTRL is a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation. The Test-Time Reinforcement Learning (TTRL) search framework enables the model to discover, combine, and reuse multiple intermediate lemmas autonomously.\n\n## Recent Achievements (2025-2026)\n\nRecent systems achieved 92.2% on MiniF2F with full Test-Time RL, and in 2025, multiple independent systems achieved gold-medal equivalent performance with formally verified Lean 4 proofs.\n\nRecent work has studied online reinforcement learning for autoformalization: translating informal mathematical conjectures into formal statements in Lean 4, with approaches addressing the challenges of reward formulation in this domain."
    ],
    "durationSeconds": 6.988772214000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d3f1bda7-61a8-42b3-8072-8d9571e8370f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T05:58:35.644Z_

<details><summary>↩ Tool result · `toolu_01R4GnmjTRvf8W8QV8sjYtnN`</summary>

```text
Web search results for query: "DDRL debiased GRPO test-time RL spurious signal amplification ACL 2026"

Links: [{"title":"Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/html/2604.21327"},{"title":"Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients","url":"https://arxiv.org/pdf/2510.18924"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Dual Consensus: Escaping from Spurious Majority in Unsupervised RLVR via Two-Stage Vote Mechanism","url":"https://arxiv.org/html/2603.16223"},{"title":"Mitigating Selection Bias in Large Language Models via Permutation-Aware GRPO","url":"https://arxiv.org/pdf/2603.21016"},{"title":"Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts","url":"https://arxiv.org/pdf/2603.21177"}]

Based on the web search results, I found relevant information about your query:

DDRL (Debiased and Denoised test-time Reinforcement Learning) is a framework designed to mitigate spurious signals in test-time RL for math reasoning. 

The research addresses how GRPO's normalization mechanism disproportionately amplifies spurious rewards in low-consensus regimes, which introduces a systematic bias in unsupervised settings.

DDRL proposes three key components: (1) a balanced confidence-aware sampling strategy that selects rollout samples based on their reliability while maintaining balanced positive and negative examples, (2) replacing group-relative advantage estimation with a bias-corrected scheme to eliminate the amplification effect, and (3) a consensus-based off-policy refinement stage after the RL phase using rejection sampling.

The paper appears to be from April 2026 based on the metadata from the arXiv source, which aligns with the ACL 2026 timeframe you mentioned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4af96bb-bf29-4e4b-a10e-1ae006ac8e2b",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "9c95f1f5-06af-4d60-bc64-118896cf65e5",
  "toolUseResult": {
    "query": "DDRL debiased GRPO test-time RL spurious signal amplification ACL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Yu8WsQhLzsw6VZM5invEA",
        "content": [
          {
            "title": "Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning",
            "url": "https://arxiv.org/html/2604.21327"
          },
          {
            "title": "Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients",
            "url": "https://arxiv.org/pdf/2510.18924"
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
            "title": "Mitigating Selection Bias in Large Language Models via Permutation-Aware GRPO",
            "url": "https://arxiv.org/pdf/2603.21016"
          },
          {
            "title": "Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts",
            "url": "https://arxiv.org/pdf/2603.21177"
          }
        ]
      },
      "Based on the web search results, I found relevant information about your query:\n\nDDRL (Debiased and Denoised test-time Reinforcement Learning) is a framework designed to mitigate spurious signals in test-time RL for math reasoning. \n\nThe research addresses how GRPO's normalization mechanism disproportionately amplifies spurious rewards in low-consensus regimes, which introduces a systematic bias in unsupervised settings.\n\nDDRL proposes three key components: (1) a balanced confidence-aware sampling strategy that selects rollout samples based on their reliability while maintaining balanced positive and negative examples, (2) replacing group-relative advantage estimation with a bias-corrected scheme to eliminate the amplification effect, and (3) a consensus-based off-policy refinement stage after the RL phase using rejection sampling.\n\nThe paper appears to be from April 2026 based on the metadata from the arXiv source, which aligns with the ACL 2026 timeframe you mentioned."
    ],
    "durationSeconds": 6.089412640000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a4af96bb-bf29-4e4b-a10e-1ae006ac8e2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T05:58:36.426Z_

<details><summary>↩ Tool result · `toolu_01VxzxhW6XjxQsWVnAZTDoD7`</summary>

```text
Web search results for query: "CriticLean CriticLeanGPT mathematical formalization critic reward 2025"

Links: [{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"},{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"},{"title":"m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face","url":"https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | Nanjing University Large-scale Intelligence and Knowledge Laboratory","url":"https://www.nju-link.com/en/publication/peng-2025-criticleancriticguidedreinforcementlearning/"}]

Based on the search results, here's what I found about CriticLean and CriticLeanGPT:

## Overview

CriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. The research addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code, noting that while prior work has focused on generation and compilation success, little attention has been paid to the critic phase-the evaluation of whether generated formalizations truly capture the semantic intent of the original problem.

## Key Components

**CriticLeanGPT**: CriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations.

**CriticLeanBench**: CriticLeanBench is a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations, and the trained CriticLeanGPT models significantly outperform strong open- and closed-source baselines.

**FineLeanCorpus**: Building on the CriticLean framework, FineLeanCorpus is a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.

## Publication

The paper was published on July 8, 2025, with authors including Zhongyuan Peng and 18 other researchers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61cd1312-533d-438c-9b6e-d82d9bce1940",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "4aad33fc-c356-4fda-a5bb-cdf8d4acf68e",
  "toolUseResult": {
    "query": "CriticLean CriticLeanGPT mathematical formalization critic reward 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0161yC7SvF3iJpni4yHWcfqX",
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
      "Based on the search results, here's what I found about CriticLean and CriticLeanGPT:\n\n## Overview\n\nCriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. The research addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code, noting that while prior work has focused on generation and compilation success, little attention has been paid to the critic phase-the evaluation of whether generated formalizations truly capture the semantic intent of the original problem.\n\n## Key Components\n\n**CriticLeanGPT**: CriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations.\n\n**CriticLeanBench**: CriticLeanBench is a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations, and the trained CriticLeanGPT models significantly outperform strong open- and closed-source baselines.\n\n**FineLeanCorpus**: Building on the CriticLean framework, FineLeanCorpus is a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.\n\n## Publication\n\nThe paper was published on July 8, 2025, with authors including Zhongyuan Peng and 18 other researchers."
    ],
    "durationSeconds": 6.453544420000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "61cd1312-533d-438c-9b6e-d82d9bce1940",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T05:58:38.491Z_

<details><summary>↩ Tool result · `toolu_01VYPz9kYJ947p9gnXXATs9a`</summary>

```text
Web search results for query: "Aria ICLR 2026 autoformalization retrieval dependency graph FormalEvolve evolutionary search"

Links: [{"title":"Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph | OpenReview","url":"https://openreview.net/forum?id=CPxZClPMiy"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE ...","url":"https://openreview.net/pdf/388a385b7ad068290351f90757bd3af8bb6e5515.pdf"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://iclr.cc/virtual/2026/poster/10010860"},{"title":"[Literature Review] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://www.themoonlight.io/en/review/aria-an-agent-for-retrieval-and-iterative-auto-formalization-via-dependency-graph"},{"title":"[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520"},{"title":"[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520v1"},{"title":"(PDF) Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://www.researchgate.net/publication/396250696_Aria_An_Agent_For_Retrieval_and_Iterative_Auto-Formalization_via_Dependency_Graph"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE","url":"https://arxiv.org/pdf/2510.04520"}]

Based on the search results, I found comprehensive information about Aria. Here's what I found:

## Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph

Aria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.

### Problem Being Addressed
Accurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.

### Key Components
To ensure semantic correctness, the system introduces AriaScorer, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.

### Results
On ProofNet, it achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods.

The paper was submitted to ICLR 2026 and is now available in the conference proceedings. Note that while your search query mentioned "FormalEvolve" and "evolutionary search," those terms did not appear in the results about Aria itself.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b6d500c-4016-49f5-9682-9810bac890e6",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "b73ca318-d93a-4f92-a10f-8ecb0301d4e7",
  "toolUseResult": {
    "query": "Aria ICLR 2026 autoformalization retrieval dependency graph FormalEvolve evolutionary search",
    "results": [
      {
        "tool_use_id": "srvtoolu_016BWFdPBPUU6Qm35YK39Zdo",
        "content": [
          {
            "title": "Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph | OpenReview",
            "url": "https://openreview.net/forum?id=CPxZClPMiy"
          },
          {
            "title": "ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE ...",
            "url": "https://openreview.net/pdf/388a385b7ad068290351f90757bd3af8bb6e5515.pdf"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://iclr.cc/virtual/2026/poster/10010860"
          },
          {
            "title": "[Literature Review] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://www.themoonlight.io/en/review/aria-an-agent-for-retrieval-and-iterative-auto-formalization-via-dependency-graph"
          },
          {
            "title": "[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/abs/2510.04520"
          },
          {
            "title": "[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/abs/2510.04520v1"
          },
          {
            "title": "(PDF) Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://www.researchgate.net/publication/396250696_Aria_An_Agent_For_Retrieval_and_Iterative_Auto-Formalization_via_Dependency_Graph"
          },
          {
            "title": "ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE",
            "url": "https://arxiv.org/pdf/2510.04520"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about Aria. Here's what I found:\n\n## Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph\n\nAria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.\n\n### Problem Being Addressed\nAccurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.\n\n### Key Components\nTo ensure semantic correctness, the system introduces AriaScorer, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.\n\n### Results\nOn ProofNet, it achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods.\n\nThe paper was submitted to ICLR 2026 and is now available in the conference proceedings. Note that while your search query mentioned \"FormalEvolve\" and \"evolutionary search,\" those terms did not appear in the results about Aria itself."
    ],
    "durationSeconds": 6.642897550000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3b6d500c-4016-49f5-9682-9810bac890e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
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
  "leafUuid": "b73ca318-d93a-4f92-a10f-8ecb0301d4e7",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal objective acceptance likelihood",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Tool result

_source line 23 · 2026-05-28T05:58:39.323Z_

<details><summary>↩ Tool result · `toolu_018kMigik2CCfJ9DCJ19EDYT`</summary>

```text
Web search results for query: "co-adaptive retrieval RAG reinforcement learning R3 Reinforced-IR TTARAG 2025 2026"

Links: [{"title":"[2510.24652] Optimizing Retrieval for RAG via Reinforcement Learning","url":"https://arxiv.org/abs/2510.24652"},{"title":"Optimizing Retrieval for RAG via Reinforced Contrastive Learning","url":"https://arxiv.org/html/2510.24652v1"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2505.23794v2"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2505.23794"},{"title":"[2505.23794] R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2505.23794"},{"title":"Towards Faithful Industrial RAG: A Reinforced Co-adaptation...","url":"https://arxiv.org/abs/2602.22584"},{"title":"GitHub - DavidZWZ/Awesome-RAG-Reasoning: [EMNLP 2025] Awesome RAG Reasoning Resources · GitHub","url":"https://github.com/DavidZWZ/Awesome-RAG-Reasoning"}]

Based on the search results, here's what I found regarding these research topics:

## R3 (Optimizing Retrieval for RAG via Reinforcement Learning)

R3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. Unlike prior approaches that rely on annotated or synthetic data for supervised fine-tuning, R3 enables the retriever to dynamically explore and optimize relevance within the RAG environment. R3 improves RAG performance by 5.2% over the original retriever and surpasses state-of-the-art retrievers by 4.9%. It is both efficient and practical, requiring only 4 GPUs and completing training within a single day.

## R3-RAG (Learning Step-by-Step Reasoning and Retrieval)

R3-RAG uses Reinforcement learning to enable the LLM to learn to Reason and Retrieve step-by-step, thereby retrieving comprehensive external knowledge and generating a factual answer. The framework first uses cold start to make the model learn the manner of iteratively interleaving reasoning and retrieval.

## Reinforced Co-adaptation Framework

A reinforced co-adaptation framework jointly optimizes retrieval and generation through Graph-aware Retrieval (GraphRAG) and evidence-constrained reinforcement learning via Group Relative Policy Optimization (GRPO) with multi-dimensional rewards covering faithfulness, style compliance, safety, and URL validity. The framework showed consistent gains in accuracy and completeness while reducing hallucination rate by 72%, and a two-week online A/B test demonstrated a 28.6% increase in like rate and 46.2% decrease in dislike rate.

I did not find specific search results for "Reinforced-IR" or "TTARAG" in the results returned. These concepts may be either emerging research or alternative naming conventions in the RAG and reinforcement learning literature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3950d2dd-8d8c-4807-91e6-af20a9e59968",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "f3dd1177-939a-45dd-95bc-a6c7bcf27360",
  "toolUseResult": {
    "query": "co-adaptive retrieval RAG reinforcement learning R3 Reinforced-IR TTARAG 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013CkdzC55s392AWJFWf1ZzX",
        "content": [
          {
            "title": "[2510.24652] Optimizing Retrieval for RAG via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2510.24652"
          },
          {
            "title": "Optimizing Retrieval for RAG via Reinforced Contrastive Learning",
            "url": "https://arxiv.org/html/2510.24652v1"
          },
          {
            "title": "R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.23794v2"
          },
          {
            "title": "R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2505.23794"
          },
          {
            "title": "[2505.23794] R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.23794"
          },
          {
            "title": "Towards Faithful Industrial RAG: A Reinforced Co-adaptation...",
            "url": "https://arxiv.org/abs/2602.22584"
          },
          {
            "title": "GitHub - DavidZWZ/Awesome-RAG-Reasoning: [EMNLP 2025] Awesome RAG Reasoning Resources · GitHub",
            "url": "https://github.com/DavidZWZ/Awesome-RAG-Reasoning"
          }
        ]
      },
      "Based on the search results, here's what I found regarding these research topics:\n\n## R3 (Optimizing Retrieval for RAG via Reinforcement Learning)\n\nR3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. Unlike prior approaches that rely on annotated or synthetic data for supervised fine-tuning, R3 enables the retriever to dynamically explore and optimize relevance within the RAG environment. R3 improves RAG performance by 5.2% over the original retriever and surpasses state-of-the-art retrievers by 4.9%. It is both efficient and practical, requiring only 4 GPUs and completing training within a single day.\n\n## R3-RAG (Learning Step-by-Step Reasoning and Retrieval)\n\nR3-RAG uses Reinforcement learning to enable the LLM to learn to Reason and Retrieve step-by-step, thereby retrieving comprehensive external knowledge and generating a factual answer. The framework first uses cold start to make the model learn the manner of iteratively interleaving reasoning and retrieval.\n\n## Reinforced Co-adaptation Framework\n\nA reinforced co-adaptation framework jointly optimizes retrieval and generation through Graph-aware Retrieval (GraphRAG) and evidence-constrained reinforcement learning via Group Relative Policy Optimization (GRPO) with multi-dimensional rewards covering faithfulness, style compliance, safety, and URL validity. The framework showed consistent gains in accuracy and completeness while reducing hallucination rate by 72%, and a two-week online A/B test demonstrated a 28.6% increase in like rate and 46.2% decrease in dislike rate.\n\nI did not find specific search results for \"Reinforced-IR\" or \"TTARAG\" in the results returned. These concepts may be either emerging research or alternative naming conventions in the RAG and reinforcement learning literature."
    ],
    "durationSeconds": 8.190836062000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3950d2dd-8d8c-4807-91e6-af20a9e59968",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-28T05:58:44.326Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have initial search results. Let me do a few more targeted searches to fill in gaps:

1. FormalEvolve for autoformalization
2. MathAtlas benchmark
3. TEMPO test-time training EM formalization
4. T³RL tool-verified TTRL
5. Whether anyone has already combined TTRL with retrieval for autoformalization
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3dd1177-939a-45dd-95bc-a6c7bcf27360",
  "isSidechain": false,
  "requestId": "req_011CbUTK3MGBNkbiSGiFN1TN",
  "type": "assistant",
  "uuid": "c8f41a8e-8e4e-4b96-8061-5a2ba8a1b3ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJKHEd2tbee8bYK9XBaEYQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 874,
      "cache_creation_input_tokens": 3573,
      "cache_read_input_tokens": 24531,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 874,
          "output_tokens": 292,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 3573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3573
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

_source line 25 · 2026-05-28T05:58:45.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DqYPH7fbjkKtuMrmRPHZHD`</summary>

```json
{
  "query": "FormalEvolve neuro-symbolic evolutionary autoformalization CombiBench 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8f41a8e-8e4e-4b96-8061-5a2ba8a1b3ca",
  "isSidechain": false,
  "requestId": "req_011CbUTK3MGBNkbiSGiFN1TN",
  "type": "assistant",
  "uuid": "3ac16045-d68f-4b60-9487-8d839a881d0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJKHEd2tbee8bYK9XBaEYQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 874,
      "cache_creation_input_tokens": 3573,
      "cache_read_input_tokens": 24531,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 874,
          "output_tokens": 292,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 3573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3573
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

_source line 26 · 2026-05-28T05:58:45.828Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GC8roKBRJ8dxyBXcNnAn5t`</summary>

```json
{
  "query": "MathAtlas autoformalization benchmark graduate-level 2026 arXiv:2605.14061"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ac16045-d68f-4b60-9487-8d839a881d0e",
  "isSidechain": false,
  "requestId": "req_011CbUTK3MGBNkbiSGiFN1TN",
  "type": "assistant",
  "uuid": "1cd6557e-9817-4cca-9d5f-4454a726581f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJKHEd2tbee8bYK9XBaEYQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 874,
      "cache_creation_input_tokens": 3573,
      "cache_read_input_tokens": 24531,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 874,
          "output_tokens": 292,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 3573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3573
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

_source line 27 · 2026-05-28T05:58:46.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019gvF9GM3fWKcxBvM3r8Zmd`</summary>

```json
{
  "query": "TEMPO test-time training reasoning models EM formalization 2026 arXiv:2604.19295"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cd6557e-9817-4cca-9d5f-4454a726581f",
  "isSidechain": false,
  "requestId": "req_011CbUTK3MGBNkbiSGiFN1TN",
  "type": "assistant",
  "uuid": "fd06cfeb-610e-41ee-b0d1-1df526ced561",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJKHEd2tbee8bYK9XBaEYQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 874,
      "cache_creation_input_tokens": 3573,
      "cache_read_input_tokens": 24531,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 874,
          "output_tokens": 292,
          "cache_read_input_tokens": 24531,
          "cache_creation_input_tokens": 3573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3573
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

_source line 28 · 2026-05-28T05:58:52.410Z_

<details><summary>↩ Tool result · `toolu_019gvF9GM3fWKcxBvM3r8Zmd`</summary>

```text
Web search results for query: "TEMPO test-time training reasoning models EM formalization 2026 arXiv:2604.19295"

Links: [{"title":"Paper page - TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://huggingface.co/papers/2604.19295"},{"title":"[2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/abs/2604.19295"},{"title":"April 22, 2026 TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/pdf/2604.19295"},{"title":"TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/html/2604.19295v1"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"The Surprising Effectiveness of Test-Time Training for Abstract Reasoning","url":"https://arxiv.org/html/2411.07279v1"},{"title":"[2411.07279] The Surprising Effectiveness of Test-Time Training for Few-Shot Learning","url":"https://arxiv.org/abs/2411.07279"}]

Based on the search results, here's what I found about TEMPO (arXiv:2604.19295):

## Overview

TEMPO is a test-time training (TTT) framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on a labeled dataset.

## Key Innovation: EM Formalization

The method formalizes this alternating procedure through the Expectation-Maximization (EM) algorithm, revealing that prior methods can be interpreted as incomplete variants that omit the crucial recalibration step. Reintroducing this step tightens the evidence lower bound (ELBO) and enables sustained improvement.

## Problem Being Addressed

Existing TTT methods for large reasoning models (LRMs) plateau quickly and do not benefit from additional test-time compute. Without external calibration, the self-generated reward signal increasingly drifts as the policy model evolves, leading to both performance plateaus and diversity collapse.

## Results

Across diverse model families (Qwen3 and OLMO3) and reasoning tasks, TEMPO improves OLMO3-7B on AIME 2024 from 33.0% to 51.1% and Qwen3-14B from 42.3% to 65.8%, while maintaining high diversity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd06cfeb-610e-41ee-b0d1-1df526ced561",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "745e8cef-d9e5-4c83-b521-45a0dcb55d1e",
  "toolUseResult": {
    "query": "TEMPO test-time training reasoning models EM formalization 2026 arXiv:2604.19295",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HXSAzbb7sjn8ztu7q6bVCE",
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
            "title": "The Surprising Effectiveness of Test-Time Training for Abstract Reasoning",
            "url": "https://arxiv.org/html/2411.07279v1"
          },
          {
            "title": "[2411.07279] The Surprising Effectiveness of Test-Time Training for Few-Shot Learning",
            "url": "https://arxiv.org/abs/2411.07279"
          }
        ]
      },
      "Based on the search results, here's what I found about TEMPO (arXiv:2604.19295):\n\n## Overview\n\nTEMPO is a test-time training (TTT) framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on a labeled dataset.\n\n## Key Innovation: EM Formalization\n\nThe method formalizes this alternating procedure through the Expectation-Maximization (EM) algorithm, revealing that prior methods can be interpreted as incomplete variants that omit the crucial recalibration step. Reintroducing this step tightens the evidence lower bound (ELBO) and enables sustained improvement.\n\n## Problem Being Addressed\n\nExisting TTT methods for large reasoning models (LRMs) plateau quickly and do not benefit from additional test-time compute. Without external calibration, the self-generated reward signal increasingly drifts as the policy model evolves, leading to both performance plateaus and diversity collapse.\n\n## Results\n\nAcross diverse model families (Qwen3 and OLMO3) and reasoning tasks, TEMPO improves OLMO3-7B on AIME 2024 from 33.0% to 51.1% and Qwen3-14B from 42.3% to 65.8%, while maintaining high diversity."
    ],
    "durationSeconds": 5.780475535999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fd06cfeb-610e-41ee-b0d1-1df526ced561",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-28T05:58:52.620Z_

<details><summary>↩ Tool result · `toolu_01GC8roKBRJ8dxyBXcNnAn5t`</summary>

```text
Web search results for query: "MathAtlas autoformalization benchmark graduate-level 2026 arXiv:2605.14061"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data","url":"https://arxiv.org/pdf/2502.05567"},{"title":"(PDF) FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://www.researchgate.net/publication/403308231_FormalProofBench_Can_Models_Write_Graduate_Level_Math_Proofs_That_Are_Formally_Verified"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"},{"title":"FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://arxiv.org/pdf/2603.26996"}]

Based on the search results, here's what I found about MathAtlas:

MathAtlas is the first large-scale autoformalization benchmark of graduate-level mathematics in the wild, containing approximately 52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

Current autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored, which MathAtlas aims to address.

MathAtlas is enriched with a mathematical dependency graph containing approximately 178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

Regarding the difficulty of the benchmark, strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions, showing that MathAtlas is high quality but extremely challenging.

The paper (arXiv:2605.14061) was submitted on May 13, 2026, and is authored by Nilay Patel, Noah Arias, Davit Babayan, Victoria Cochran, Timothy Libman, Hafsah Mahmood, Liam McCarty, Soli Munoz, Laurel Willey, and Jeffrey Flanigan from the University of California, Santa Cruz.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cd6557e-9817-4cca-9d5f-4454a726581f",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "b050a59c-1920-457d-aa70-b0288903a79a",
  "toolUseResult": {
    "query": "MathAtlas autoformalization benchmark graduate-level 2026 arXiv:2605.14061",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FoM6nXgdWAsXbMPpvtsi92",
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
            "title": "(PDF) FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://www.researchgate.net/publication/403308231_FormalProofBench_Can_Models_Write_Graduate_Level_Math_Proofs_That_Are_Formally_Verified"
          },
          {
            "title": "A New Approach Towards Autoformalization",
            "url": "https://arxiv.org/pdf/2310.07957"
          },
          {
            "title": "Reliable Evaluation and Benchmarks for Statement Autoformalization",
            "url": "https://arxiv.org/pdf/2406.07222"
          },
          {
            "title": "FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://arxiv.org/pdf/2603.26996"
          }
        ]
      },
      "Based on the search results, here's what I found about MathAtlas:\n\nMathAtlas is the first large-scale autoformalization benchmark of graduate-level mathematics in the wild, containing approximately 52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.\n\nCurrent autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored, which MathAtlas aims to address.\n\nMathAtlas is enriched with a mathematical dependency graph containing approximately 178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.\n\nRegarding the difficulty of the benchmark, strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions, showing that MathAtlas is high quality but extremely challenging.\n\nThe paper (arXiv:2605.14061) was submitted on May 13, 2026, and is authored by Nilay Patel, Noah Arias, Davit Babayan, Victoria Cochran, Timothy Libman, Hafsah Mahmood, Liam McCarty, Soli Munoz, Laurel Willey, and Jeffrey Flanigan from the University of California, Santa Cruz."
    ],
    "durationSeconds": 6.7889301500000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1cd6557e-9817-4cca-9d5f-4454a726581f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T05:58:54.001Z_

<details><summary>↩ Tool result · `toolu_01DqYPH7fbjkKtuMrmRPHZHD`</summary>

```text
Web search results for query: "FormalEvolve neuro-symbolic evolutionary autoformalization CombiBench 2026 arXiv"

Links: [{"title":"[2603.19828] FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/abs/2603.19828"},{"title":"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/pdf/2603.19828"},{"title":"arXiv preprint AUTOFORMALIZER WITH TOOL FEEDBACK","url":"https://arxiv.org/pdf/2510.06857"},{"title":"Neuro-Symbolic Autoformalization Framework","url":"https://www.emergentmind.com/topics/neuro-symbolic-autoformalization-framework"},{"title":"Neuro-Symbolic Artificial Intelligence: Towards Improving the Reasoning Abilities of Large Language Models","url":"https://arxiv.org/html/2508.13678v1"}]

I found the research paper you're looking for! Here are the key findings:

FormalEvolve is a compilation-gated neuro-symbolic evolutionary framework that formulates autoformalization as a budgeted, test-time search for semantically consistent repertoires.

Autoformalization aims to translate natural-language mathematics into compilable, machine-checkable statements. However, semantic consistency does not imply prover effectiveness: even semantically consistent formalizations can differ substantially in proof-search cost and success rate.

**Key Technical Features:**

FormalEvolve generates diverse candidates via LLM-driven mutation and crossover with bounded patch repair, while symbolic Abstract Syntax Tree (AST) rewrite operations further inject structural diversity.

**Performance Results:**

On CombiBench and ProofNet, under a strict generator-call budget of T = 100, FormalEvolve reaches semantic hit rates (SH@100) of 58.0% and 84.9%, and reduces cross-problem concentration of semantic successes (lower Gini). Additionally, under a fixed prover budget, FormalEvolve also improves downstream proving performance on CombiBench.

The paper was published on arXiv on March 23, 2026 with the identifier 2603.19828.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ac16045-d68f-4b60-9487-8d839a881d0e",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "2585778c-fc5b-44ba-ae23-2374565edeae",
  "toolUseResult": {
    "query": "FormalEvolve neuro-symbolic evolutionary autoformalization CombiBench 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JkzYHAcDr8fZLUKJy7JmLp",
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
            "title": "Neuro-Symbolic Autoformalization Framework",
            "url": "https://www.emergentmind.com/topics/neuro-symbolic-autoformalization-framework"
          },
          {
            "title": "Neuro-Symbolic Artificial Intelligence: Towards Improving the Reasoning Abilities of Large Language Models",
            "url": "https://arxiv.org/html/2508.13678v1"
          }
        ]
      },
      "I found the research paper you're looking for! Here are the key findings:\n\nFormalEvolve is a compilation-gated neuro-symbolic evolutionary framework that formulates autoformalization as a budgeted, test-time search for semantically consistent repertoires.\n\nAutoformalization aims to translate natural-language mathematics into compilable, machine-checkable statements. However, semantic consistency does not imply prover effectiveness: even semantically consistent formalizations can differ substantially in proof-search cost and success rate.\n\n**Key Technical Features:**\n\nFormalEvolve generates diverse candidates via LLM-driven mutation and crossover with bounded patch repair, while symbolic Abstract Syntax Tree (AST) rewrite operations further inject structural diversity.\n\n**Performance Results:**\n\nOn CombiBench and ProofNet, under a strict generator-call budget of T = 100, FormalEvolve reaches semantic hit rates (SH@100) of 58.0% and 84.9%, and reduces cross-problem concentration of semantic successes (lower Gini). Additionally, under a fixed prover budget, FormalEvolve also improves downstream proving performance on CombiBench.\n\nThe paper was published on arXiv on March 23, 2026 with the identifier 2603.19828."
    ],
    "durationSeconds": 8.649211552,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3ac16045-d68f-4b60-9487-8d839a881d0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-28T05:58:58.329Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more targeted searches to check if anyone has already combined TTRL with co-adaptive retrieval specifically for autoformalization, and to verify some of the other key claims in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2585778c-fc5b-44ba-ae23-2374565edeae",
  "isSidechain": false,
  "requestId": "req_011CbUTL87Xgr238JhRs4NWg",
  "type": "assistant",
  "uuid": "a4b4cac2-7117-4e21-89b9-bc101f45e4bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYhux9AxUkUakPKijdHps5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1388,
      "cache_creation_input_tokens": 1769,
      "cache_read_input_tokens": 28104,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1388,
          "output_tokens": 187,
          "cache_read_input_tokens": 28104,
          "cache_creation_input_tokens": 1769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1769
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

_source line 32 · 2026-05-28T05:58:59.452Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015DYx2zsd1v7yBu4C8msgHV`</summary>

```json
{
  "query": "test-time reinforcement learning retrieval augmented formal mathematics Lean 4 co-adaptive 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4b4cac2-7117-4e21-89b9-bc101f45e4bb",
  "isSidechain": false,
  "requestId": "req_011CbUTL87Xgr238JhRs4NWg",
  "type": "assistant",
  "uuid": "d6b1e99b-b548-4f19-bb10-771bed43865c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYhux9AxUkUakPKijdHps5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1388,
      "cache_creation_input_tokens": 1769,
      "cache_read_input_tokens": 28104,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1388,
          "output_tokens": 187,
          "cache_read_input_tokens": 28104,
          "cache_creation_input_tokens": 1769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1769
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

_source line 33 · 2026-05-28T05:59:00.347Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M9TyWQbCYZovvVP6bctjUS`</summary>

```json
{
  "query": "GDPO group reward decoupled normalization multi-reward GRPO NVIDIA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6b1e99b-b548-4f19-bb10-771bed43865c",
  "isSidechain": false,
  "requestId": "req_011CbUTL87Xgr238JhRs4NWg",
  "type": "assistant",
  "uuid": "0c650fcf-9664-4bd5-8d57-aa4ffda0725e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYhux9AxUkUakPKijdHps5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1388,
      "cache_creation_input_tokens": 1769,
      "cache_read_input_tokens": 28104,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1388,
          "output_tokens": 187,
          "cache_read_input_tokens": 28104,
          "cache_creation_input_tokens": 1769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1769
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
  "leafUuid": "0c650fcf-9664-4bd5-8d57-aa4ffda0725e",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal objective acceptance likelihood",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Tool result

_source line 36 · 2026-05-28T05:59:07.476Z_

<details><summary>↩ Tool result · `toolu_015DYx2zsd1v7yBu4C8msgHV`</summary>

```text
Web search results for query: "test-time reinforcement learning retrieval augmented formal mathematics Lean 4 co-adaptive 2026"

Links: [{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/html/2605.13137v2"},{"title":"REAL-Prover: Retrieval Augmented Lean ...","url":"https://arxiv.org/pdf/2505.20613"},{"title":"Lean Refactor: Multi-Objective Controllable Proof Optimization via Agentic Strategy Search","url":"https://arxiv.org/html/2605.20244"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/pdf/2507.06181"},{"title":"Olympiad-level formal mathematical reasoning with reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09833-y"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/pdf/2508.06931"},{"title":"DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition","url":"https://arxiv.org/pdf/2504.21801"}]

Based on the search results, here's what I found about test-time reinforcement learning, retrieval-augmented formal mathematics, Lean 4, and related developments in 2026:

## Test-Time Reinforcement Learning

For the most difficult problems, test-time RL uses a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation. Test-Time Reinforcement Learning (TTRL) enables discovery, combination, and reuse of intermediate lemmas autonomously.

## Retrieval-Augmented Approaches

Several systems combine retrieval with theorem proving in Lean 4:

- Real-Prover is a retrieval augmented lean prover for mathematical reasoning.
- CRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, and introduces a framework for automatically constructing a concept-definition knowledge base from Mathlib4, the standard mathematical library for Lean 4.

## Notable Systems and Achievements

AlphaProof is an AlphaZero-inspired agent that learns to find formal proofs through reinforcement learning by training on millions of auto-formalized problems, and for the most difficult problems, it uses Test-Time RL.

## Reinforcement Learning Integration

DeepSeek-Prover-V2 develops a reasoning model for subgoal decomposition using large-scale reinforcement learning, and prompts models to decompose theorems into high-level proof sketches while simultaneously formalizing these proof steps in Lean 4.

The search results show active development in combining reinforcement learning, retrieval augmentation, and Lean 4 formal mathematics as of 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6b1e99b-b548-4f19-bb10-771bed43865c",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "1b31c1a3-379f-4f73-b394-ba1fab46e927",
  "toolUseResult": {
    "query": "test-time reinforcement learning retrieval augmented formal mathematics Lean 4 co-adaptive 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013YESTqsbrQjzuYLJ74hu2S",
        "content": [
          {
            "title": "Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics",
            "url": "https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"
          },
          {
            "title": "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving",
            "url": "https://arxiv.org/html/2605.13137v2"
          },
          {
            "title": "REAL-Prover: Retrieval Augmented Lean ...",
            "url": "https://arxiv.org/pdf/2505.20613"
          },
          {
            "title": "Lean Refactor: Multi-Objective Controllable Proof Optimization via Agentic Strategy Search",
            "url": "https://arxiv.org/html/2605.20244"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/pdf/2507.06181"
          },
          {
            "title": "Olympiad-level formal mathematical reasoning with reinforcement learning | Nature",
            "url": "https://www.nature.com/articles/s41586-025-09833-y"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/pdf/2508.06931"
          },
          {
            "title": "DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition",
            "url": "https://arxiv.org/pdf/2504.21801"
          }
        ]
      },
      "Based on the search results, here's what I found about test-time reinforcement learning, retrieval-augmented formal mathematics, Lean 4, and related developments in 2026:\n\n## Test-Time Reinforcement Learning\n\nFor the most difficult problems, test-time RL uses a method of generating and learning from millions of related problem variants at inference time to enable deep, problem-specific adaptation. Test-Time Reinforcement Learning (TTRL) enables discovery, combination, and reuse of intermediate lemmas autonomously.\n\n## Retrieval-Augmented Approaches\n\nSeveral systems combine retrieval with theorem proving in Lean 4:\n\n- Real-Prover is a retrieval augmented lean prover for mathematical reasoning.\n- CRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, and introduces a framework for automatically constructing a concept-definition knowledge base from Mathlib4, the standard mathematical library for Lean 4.\n\n## Notable Systems and Achievements\n\nAlphaProof is an AlphaZero-inspired agent that learns to find formal proofs through reinforcement learning by training on millions of auto-formalized problems, and for the most difficult problems, it uses Test-Time RL.\n\n## Reinforcement Learning Integration\n\nDeepSeek-Prover-V2 develops a reasoning model for subgoal decomposition using large-scale reinforcement learning, and prompts models to decompose theorems into high-level proof sketches while simultaneously formalizing these proof steps in Lean 4.\n\nThe search results show active development in combining reinforcement learning, retrieval augmentation, and Lean 4 formal mathematics as of 2026."
    ],
    "durationSeconds": 8.019035820999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d6b1e99b-b548-4f19-bb10-771bed43865c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T05:59:07.561Z_

<details><summary>↩ Tool result · `toolu_01M9TyWQbCYZovvVP6bctjUS`</summary>

```text
Web search results for query: "GDPO group reward decoupled normalization multi-reward GRPO NVIDIA 2026"

Links: [{"title":"GDPO Explained: How NVIDIA Fixes GRPO for Multi-Reward LLM Reinforcement Learning - AI Papers Academy","url":"https://aipapersacademy.com/gdpo/"},{"title":"GDPO, not GRPO NVIDIA introduces Group reward-Decoupled Normalization Policy Optimization (GDPO), a new multi-reward RL algorithm that consistently improves per-reward convergence over GRPO across a wide range of tasks. They find that the common practice of applying GRPO to multi-reward optimization normalizes distinct reward combinations into identical advantage values. This collapses the training signal, reduces reward-level resolution, and leads to suboptimal convergence.","url":"https://www.threads.com/@sung.kim.mw/post/DTVU1v1kYZ1/gdpo-not-grpo-nvidia-introduces-group-reward-decoupled-normalization-policy"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://www.emergent-behaviors.com/gdpo-group-reward-decoupled-normalization-policy-optimization-for-multi-reward-rl-optimization/"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://nvlabs.github.io/GDPO/"},{"title":"Paper page - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://huggingface.co/papers/2601.05242"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiviq.substack.com/p/gdpo-group-reward-decoupled-normalization"},{"title":"GitHub - NVlabs/GDPO: Official implementation of GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization · GitHub","url":"https://github.com/NVlabs/GDPO"},{"title":"[2601.05242] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/abs/2601.05242"}]

Based on the search results, here's what I found about GDPO and its relationship to GRPO:

## Overview

GDPO (Group reward-Decoupled Normalization Policy Optimization) is a new multi-reward RL algorithm introduced by NVIDIA that consistently improves per-reward convergence over GRPO across a wide range of tasks.

## The Problem with GRPO for Multi-Reward Learning

The common practice of applying GRPO to multi-reward RL optimization leads to a previously overlooked issue: GRPO inherently collapses reward signals, resulting in information loss in the advantage estimates. More specifically, applying GRPO to multi-reward optimization normalizes distinct reward combinations into identical advantage values, which collapses the training signal, reduces reward-level resolution, and leads to suboptimal convergence.

## How GDPO Works

GDPO performs group-wise normalization on each reward independently prior to aggregation, in contrast with GRPO, which applies group-wise normalization directly to the summed rewards. Each reward type is normalized separately within the group of sampled responses—correctness rewards are normalized relative to other correctness rewards, format rewards relative to other format rewards, and so on.

## Performance Impact

The gap between GDPO and GRPO isn't constant; it widens exponentially as the number of rewards or rollouts increases, with GDPO maintaining 180+ distinct advantage groups compared to GRPO's ~120 at 16 rollouts. Across all settings tested, GDPO consistently outperforms GRPO, demonstrating its effectiveness and generalizability for multi-reward reinforcement learning optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c650fcf-9664-4bd5-8d57-aa4ffda0725e",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "6cee75ab-a67b-4ed6-a8fb-e46fea3abafb",
  "toolUseResult": {
    "query": "GDPO group reward decoupled normalization multi-reward GRPO NVIDIA 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VbkZjkWAJfYm1wvY5i1QyS",
        "content": [
          {
            "title": "GDPO Explained: How NVIDIA Fixes GRPO for Multi-Reward LLM Reinforcement Learning - AI Papers Academy",
            "url": "https://aipapersacademy.com/gdpo/"
          },
          {
            "title": "GDPO, not GRPO NVIDIA introduces Group reward-Decoupled Normalization Policy Optimization (GDPO), a new multi-reward RL algorithm that consistently improves per-reward convergence over GRPO across a wide range of tasks. They find that the common practice of applying GRPO to multi-reward optimization normalizes distinct reward combinations into identical advantage values. This collapses the training signal, reduces reward-level resolution, and leads to suboptimal convergence.",
            "url": "https://www.threads.com/@sung.kim.mw/post/DTVU1v1kYZ1/gdpo-not-grpo-nvidia-introduces-group-reward-decoupled-normalization-policy"
          },
          {
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://www.emergent-behaviors.com/gdpo-group-reward-decoupled-normalization-policy-optimization-for-multi-reward-rl-optimization/"
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
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://arxiviq.substack.com/p/gdpo-group-reward-decoupled-normalization"
          },
          {
            "title": "GitHub - NVlabs/GDPO: Official implementation of GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization · GitHub",
            "url": "https://github.com/NVlabs/GDPO"
          },
          {
            "title": "[2601.05242] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://arxiv.org/abs/2601.05242"
          }
        ]
      },
      "Based on the search results, here's what I found about GDPO and its relationship to GRPO:\n\n## Overview\n\nGDPO (Group reward-Decoupled Normalization Policy Optimization) is a new multi-reward RL algorithm introduced by NVIDIA that consistently improves per-reward convergence over GRPO across a wide range of tasks.\n\n## The Problem with GRPO for Multi-Reward Learning\n\nThe common practice of applying GRPO to multi-reward RL optimization leads to a previously overlooked issue: GRPO inherently collapses reward signals, resulting in information loss in the advantage estimates. More specifically, applying GRPO to multi-reward optimization normalizes distinct reward combinations into identical advantage values, which collapses the training signal, reduces reward-level resolution, and leads to suboptimal convergence.\n\n## How GDPO Works\n\nGDPO performs group-wise normalization on each reward independently prior to aggregation, in contrast with GRPO, which applies group-wise normalization directly to the summed rewards. Each reward type is normalized separately within the group of sampled responses—correctness rewards are normalized relative to other correctness rewards, format rewards relative to other format rewards, and so on.\n\n## Performance Impact\n\nThe gap between GDPO and GRPO isn't constant; it widens exponentially as the number of rewards or rollouts increases, with GDPO maintaining 180+ distinct advantage groups compared to GRPO's ~120 at 16 rollouts. Across all settings tested, GDPO consistently outperforms GRPO, demonstrating its effectiveness and generalizability for multi-reward reinforcement learning optimization."
    ],
    "durationSeconds": 7.210276685000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0c650fcf-9664-4bd5-8d57-aa4ffda0725e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-28T05:59:07.565Z_

```json
{
  "parentUuid": "6cee75ab-a67b-4ed6-a8fb-e46fea3abafb",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6542963b-9852-4c21-baee-73e123ff0ac6",
  "timestamp": "2026-05-28T05:59:07.565Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-28T05:59:16.297Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the field. Let me synthesize what I've found and do my evaluation.

Let me also check if there's any existing work that combines these components that the proposal claims is novel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6542963b-9852-4c21-baee-73e123ff0ac6",
  "isSidechain": false,
  "requestId": "req_011CbUTM85aG52LuZoWBPhUp",
  "type": "assistant",
  "uuid": "b618e367-a6ad-4ffa-81e3-a545e8ad62d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNKuLvWCgkyZ7EXsTP36N4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3529,
      "cache_read_input_tokens": 29873,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 29873,
          "cache_creation_input_tokens": 3529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3529
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

_source line 40 · 2026-05-28T05:59:17.614Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lmu7UZPFhET6rX8cPCmzD8`</summary>

```json
{
  "query": "DDR direct dependency retrieval autoformalization hallucination Lean arXiv:2511.11990"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b618e367-a6ad-4ffa-81e3-a545e8ad62d2",
  "isSidechain": false,
  "requestId": "req_011CbUTM85aG52LuZoWBPhUp",
  "type": "assistant",
  "uuid": "b9fb7b88-fd14-45ee-a60f-375c94864989",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNKuLvWCgkyZ7EXsTP36N4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3529,
      "cache_read_input_tokens": 29873,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 29873,
          "cache_creation_input_tokens": 3529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3529
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

_source line 41 · 2026-05-28T05:59:18.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NomgXPgsjZRmkfuoCFLz6H`</summary>

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
  "parentUuid": "b9fb7b88-fd14-45ee-a60f-375c94864989",
  "isSidechain": false,
  "requestId": "req_011CbUTM85aG52LuZoWBPhUp",
  "type": "assistant",
  "uuid": "e3f139fa-f56f-4e22-b402-82dd60046f63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNKuLvWCgkyZ7EXsTP36N4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3529,
      "cache_read_input_tokens": 29873,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 29873,
          "cache_creation_input_tokens": 3529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3529
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

_source line 42 · 2026-05-28T05:59:24.733Z_

<details><summary>↩ Tool result · `toolu_01Lmu7UZPFhET6rX8cPCmzD8`</summary>

```text
Web search results for query: "DDR direct dependency retrieval autoformalization hallucination Lean arXiv:2511.11990"

Links: [{"title":"[2511.11990] Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/abs/2511.11990"},{"title":"(PDF) Improving Autoformalization Using Direct Dependency Retrieval","url":"https://www.researchgate.net/publication/397701226_Improving_Autoformalization_Using_Direct_Dependency_Retrieval"},{"title":"Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/html/2511.11990"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/html/2510.10815"},{"title":"An Agent For Retrieval and Iterative Auto-Formalization via ...","url":"https://arxiv.org/pdf/2510.04520"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"}]

Based on the search results, here's what I found about arXiv:2511.11990:

**Paper Overview:**
The paper addresses statement autoformalization, which aims to translate informal descriptions into machine-verifiable representations, working with the Lean theorem prover.

**Key Problem:**
Existing methods often suffer from a lack of contextual awareness, leading to hallucination of formal definitions and theorems. Additionally, current retrieval-augmented approaches exhibit poor precision and recall for formal library dependency retrieval, and lack the scalability to effectively leverage ever-growing public datasets.

**Proposed Solution:**
The paper proposes a novel retrieval-augmented framework based on DDR (Direct Dependency Retrieval) for statement autoformalization. The DDR method directly generates candidate library dependencies from natural language mathematical descriptions and subsequently verifies their existence within the formal library.

**Results:**
A high-precision DDR model was fine-tuned on a dependency retrieval dataset of over 500,000 samples and shown to significantly outperform state-of-the-art methods in both retrieval precision and recall. An autoformalizer equipped with DDR shows consistent performance advantages in both single-attempt accuracy and multi-attempt stability compared to models using traditional selection-based RAG methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9fb7b88-fd14-45ee-a60f-375c94864989",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "26ef8c4d-2ce9-46ec-8d07-5cf45658f70e",
  "toolUseResult": {
    "query": "DDR direct dependency retrieval autoformalization hallucination Lean arXiv:2511.11990",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Guav1QtcfAakSfg8LKKPD",
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
            "url": "https://arxiv.org/html/2511.11990"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/html/2508.06931"
          },
          {
            "title": "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://arxiv.org/html/2510.10815"
          },
          {
            "title": "An Agent For Retrieval and Iterative Auto-Formalization via ...",
            "url": "https://arxiv.org/pdf/2510.04520"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv:2511.11990:\n\n**Paper Overview:**\nThe paper addresses statement autoformalization, which aims to translate informal descriptions into machine-verifiable representations, working with the Lean theorem prover.\n\n**Key Problem:**\nExisting methods often suffer from a lack of contextual awareness, leading to hallucination of formal definitions and theorems. Additionally, current retrieval-augmented approaches exhibit poor precision and recall for formal library dependency retrieval, and lack the scalability to effectively leverage ever-growing public datasets.\n\n**Proposed Solution:**\nThe paper proposes a novel retrieval-augmented framework based on DDR (Direct Dependency Retrieval) for statement autoformalization. The DDR method directly generates candidate library dependencies from natural language mathematical descriptions and subsequently verifies their existence within the formal library.\n\n**Results:**\nA high-precision DDR model was fine-tuned on a dependency retrieval dataset of over 500,000 samples and shown to significantly outperform state-of-the-art methods in both retrieval precision and recall. An autoformalizer equipped with DDR shows consistent performance advantages in both single-attempt accuracy and multi-attempt stability compared to models using traditional selection-based RAG methods."
    ],
    "durationSeconds": 7.112650827999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b9fb7b88-fd14-45ee-a60f-375c94864989",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T05:59:25.866Z_

<details><summary>↩ Tool result · `toolu_01NomgXPgsjZRmkfuoCFLz6H`</summary>

```text
Web search results for query: "FormaRL GRPO autoformalization COLM 2025 compilation reward"

Links: [{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data | OpenReview","url":"https://openreview.net/forum?id=Z2El1U94bq"},{"title":"[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/abs/2508.18914"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://openreview.net/pdf?id=Z2El1U94bq"},{"title":"Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs","url":"https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"},{"title":"[PDF] FormaRL: Enhancing Autoformalization with no Labeled Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FormaRL:-Enhancing-Autoformalization-with-no-Data-Huang-Jin/b430d8ac9cf1236314a1273dc7e8fb9769ebae70"},{"title":"Published as a conference paper at COLM 2025","url":"https://par.nsf.gov/servlets/purl/10635650"},{"title":"FormaRL: RL-Driven Autoformalization for Lean 4","url":"https://www.emergentmind.com/topics/formarl"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"}]

Based on the search results, here's what I found about FormaRL, GRPO, and autoformalization at COLM 2025:

## Overview

FormaRL is a reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. The paper was published as a conference paper at COLM 2025.

## Key Technical Details

FormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer.

The reward mechanism works as follows: Only when both SC (syntax check) and CC (consistency check) evaluate positively is a reward signal of 1 assigned; otherwise, the reward is 0.

## Performance Results

FormaRL can increase the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4 to 6x (4.04% → 26.15% on ProofNet and 2.4% → 9.6% on uproof) with merely 859 unlabeled data.

## Dataset Contribution

The authors curated a proof problem dataset from undergraduate-level math materials, named uproof, to facilitate the exploration of autoformalization and theorem proving in advanced math.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3f139fa-f56f-4e22-b402-82dd60046f63",
  "isSidechain": false,
  "promptId": "73004933-2d51-4a7a-bbeb-0165a667d14e",
  "type": "user",
  "uuid": "4b73928f-9337-4c51-9904-42401205708d",
  "toolUseResult": {
    "query": "FormaRL GRPO autoformalization COLM 2025 compilation reward",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A87YYTV4Q5tyLQjYgvR81v",
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
      "Based on the search results, here's what I found about FormaRL, GRPO, and autoformalization at COLM 2025:\n\n## Overview\n\nFormaRL is a reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. The paper was published as a conference paper at COLM 2025.\n\n## Key Technical Details\n\nFormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer.\n\nThe reward mechanism works as follows: Only when both SC (syntax check) and CC (consistency check) evaluate positively is a reward signal of 1 assigned; otherwise, the reward is 0.\n\n## Performance Results\n\nFormaRL can increase the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4 to 6x (4.04% → 26.15% on ProofNet and 2.4% → 9.6% on uproof) with merely 859 unlabeled data.\n\n## Dataset Contribution\n\nThe authors curated a proof problem dataset from undergraduate-level math materials, named uproof, to facilitate the exploration of autoformalization and theorem proving in advanced math."
    ],
    "durationSeconds": 7.624683370999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e3f139fa-f56f-4e22-b402-82dd60046f63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-28T06:00:31.892Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to conduct a thorough evaluation. Let me synthesize my findings.

## Summary of Key Findings

### What the proposal claims to do:
TTRA proposes combining four components:
1. Co-adaptive retrieval during TTRL (exploiting Lean 4's structured error messages)
2. Calibrated CriticLean semantic reward signal for TTRL
3. "Binarize-then-enrich" adaptation of DDRL's debiasing to multi-tier rewards (combining DDRL + GDPO ideas)
4. Test-time adaptation on unlabeled OOD domains for autoformalization
 
### Evaluating novelty:

Looking at the co-adaptive retrieval claim, recent work like R3 and Reinforced-IR have shown co-adaptive retrieval works for general RAG systems, and TTARAG demonstrates test-time retrieval adaptation. However, existing autoformalization work—DDR, Aria, DRIFT, CRAMF—all use static retrievers. So applying co-adaptive retrieval specifically to Lean 4 during RL training appears to be genuinely new.

The key insight here is leveraging Lean 4's structured error messages as direct training signals for the retriever—when it says `unknownIdentifier "Finset.sum_bij"`, that's telling you exactly which dependency is missing. That's a clever observation worth pursuing.

For CriticLean, the contribution is more engineering-focused: it exists but hasn't been used in TTRL settings, and there's a real distributional shift problem when a critic trained on balanced data gets applied to highly skewed compilable/non-compilable distributions.

On the binarize-then-enrich approach, I'm combining DDRL's debiasing for binary rewards with GDPO's multi-reward normalization to handle heterogeneous reward signals—compilation success plus soft critic feedback.

The weakest novelty claim is applying TTRL to autoformalization specifically. FormaRL and Wang et al. both do RL for autoformalization at training time, and TTRL has been applied to informal math reasoning, but nobody's combined them yet.

The real question is whether co-adaptive retrieval with weight adaptation actually beats simpler alternatives—best-of-N with CriticLean filtering, or just static retrieval plus TTRL without the co-adaptation. The proposal includes these as baselines, so if they work well, the added complexity might not be justified.

Looking at the core assumptions: identifier hallucination being a dominant error mode is well-supported by the data. Lean 4's structured errors as retrieval signals makes sense conceptually, though whether InfoNCE training on these signals actually produces a good retriever hasn't been empirically validated. And co-adaptive retrieval improving during TTRL is established in prior work like R3 and Reinforced-IR.

But there are some critical unknowns. Whether this transfers to autoformalization where the retrieval space is Lean 4 library constants is unproven. CriticLean functioning as a reliable reward signal in out-of-distribution TTRL settings is a key risk—if its accuracy degrades significantly on novel domains, the whole reward structure breaks down. And the "binarize-then-enrich" approach for adapting DDRL's debiasing to multi-tier rewards is straightforward in theory but untested in practice.

The core insight about Lean 4's structured error messages providing oracle-quality signals is compelling.

The real tension is that this reads as a combination paper—integrating co-adaptive retrieval with TTRL for autoformalization, which fills a genuine gap in the literature. But the novelty is concentrated in the co-adaptive retrieval piece; the other components feel more incremental. If that central retrieval mechanism doesn't deliver empirically, the contribution weakens significantly.

There's also an intuition problem: using richer structured error signals to improve retrieval doesn't feel surprising in principle, even if the execution is novel. And the system's complexity—four phases, dual loops, multi-tier rewards, curriculum learning—might invite criticism from reviewers who prefer cleaner, more focused contributions. The empirical bar is high too: even a 3-5 percentage point absolute improvement on an already-hard task (2.6% baseline) may not feel compelling enough to justify the architectural overhead.

The core insight about leveraging Lean 4's error taxonomy as co-adaptive training signals is genuinely new and not something prior work achieves directly, but it's really a specific combination of existing techniques—co-adaptive retrieval, TTRL, retrieval-augmented autoformalization, and RL-based approaches—applied to this particular domain. That's real novelty, just not the breakthrough kind. And while autoformalization and OOD generalization matter, the impact is fairly specialized to that community rather than reshaping the broader AI landscape.

Looking at the evidence and positioning, I'm settling around 25-35% acceptance probability, probably closer to 30%. The co-adaptive retrieval idea is compelling, but the paper reads more like a well-executed combination of existing methods than a clean conceptual leap. The hypothesis that structured error feedback beats binary feedback is somewhat intuitive, and there's execution risk with so many moving parts. For an AAAI audience, it might land as too niche for the autoformalization space. That said, the structural insight about formal versus informal language differences does have genuine appeal that could push this higher. The proposal's length shouldn't affect the core idea assessment—what matters is whether combining Lean 4's error signals with co-adaptive retrieval, calibrated critics, and multi-tier rewards genuinely advances autoformalization beyond existing work like FormaRL and TTRL. The novelty is real but the risk remains that reviewers might see it as incremental complexity rather than a surprising breakthrough. Sticking with 25-33%, median 28-29%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b73928f-9337-4c51-9904-42401205708d",
  "isSidechain": false,
  "requestId": "req_011CbUTNUoHdxsMg2EakvN9u",
  "type": "assistant",
  "uuid": "8ddda828-f1db-4bd4-9b61-6edb9903f650",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGNrE3cwoJprz9jNiGjVFb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 33402,
      "output_tokens": 7705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7705,
          "cache_read_input_tokens": 33402,
          "cache_creation_input_tokens": 1668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1668
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

_source line 45 · 2026-05-28T06:02:27.789Z_

Now I have sufficient information to conduct a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **TTRL (NeurIPS 2025, arXiv:2504.16084)**: 提出在无标签数据上用 majority voting 作为伪奖励进行 test-time RL，在 informal 数学推理上取得显著提升。但仅适用于有唯一数值答案的场景，不直接适用于形式化陈述（无法 majority vote）。

2. **DDRL (ACL 2026 Findings, arXiv:2604.21327)**: 识别并修复 GRPO 在 unsupervised 设置下的 spurious signal amplification，提出 balanced sampling + fixed advantages + consensus off-policy refinement。但明确限于 binary rewards，论文自身将 "multi-tier reward" 列为 future work。确认存在。

3. **GDPO (NVIDIA, arXiv:2601.05242)**: 发现 GRPO 在 multi-reward 设置下将不同 reward 组合 normalize 到相同 advantage 值，导致信息坍缩。提出 per-reward decoupled normalization。与 DDRL 解决的是不同问题（debiasing vs multi-reward resolution），确认两者未被统一。

4. **CriticLean (arXiv:2507.06181, ByteDance/Nanjing)**: CriticLeanGPT-14B-RL 在 balanced CriticLeanBench 上达 84.8% 准确率。模型已开源（HuggingFace: m-a-p/CriticLeanGPT-Qwen3-14B-RL）。论文聚焦于 critic 训练和 benchmark 构建，未探索将 CriticLean 作为 TTRL 的 reward 信号。确认存在。

5. **FormaRL (COLM 2025, arXiv:2508.18914)**: 使用 GRPO + compilation reward + LLM consistency check，在 ProofNet 上 pass@1 从 4.04% 提升至 26.15%。但是 training-time RL，非 test-time adaptation。确认存在。

6. **Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop)**: 使用 GRPO + BEq + embedding similarity，training-time。TC1: 17.29%→26.01%。无 retrieval，无 test-time adaptation。确认存在。

7. **Aria (ICLR 2026, arXiv:2510.04520)**: 当前 retrieval-augmented autoformalization 的 SOTA。通过 dependency graph + iterative formalization + AriaScorer 在 ProofNet 上达 91.6% compilation / 68.5% accuracy，homological conjectures 上达 42.9%。关键局限：retriever 是 static 的，不随 formalizer 行为变化而适应。确认存在，确认 ICLR 2026 poster。

8. **DDR (arXiv:2511.11990)**: 构建 500K 依赖检索数据集，将 Hall_m 从 0.21-0.39 降至 <0.02。验证了 identifier hallucination 是重要错误源且 retrieval 可大幅降低。确认存在。

9. **R3 (NeurIPS 2025, arXiv:2510.24652)**: 通过 reinforced contrastive learning 优化 RAG retriever，在通用 QA 任务上验证了 co-adaptive retrieval 可行。未应用于 autoformalization。确认存在。

10. **FormalEvolve (arXiv:2603.19828)**: 将 autoformalization 建模为 budgeted evolutionary search，SH@100=58.0% CombiBench / 84.9% ProofNet。搜索固定模型输出空间，无权重更新，不利用编译错误结构。确认存在。

11. **MathAtlas (arXiv:2605.14061, May 2026)**: 52K graduate-level problems，best baseline 在 MA-Hard 上仅 2.6%。含 178K dependency relations。确认存在，确认其极高难度。

12. **TEMPO (arXiv:2604.19295, Apr 2026)**: 将 TTT 形式化为 EM 过程，证明 omitting critic recalibration 导致 ELBO 退化。OLMO3-7B AIME 2024: 33.0%→51.1%。概念上与 TTRA 的 dual-loop 有平行关系。确认存在。

13. **AMBER / Construction-Verification (arXiv:2602.01291)**: 对 DeepSeek-R1 在 applied math 上的 3189 个编译错误分类，47.3% 为 identifier hallucination。确认存在。

14. **Reinforced Co-adaptation Framework (arXiv:2602.22584)**: 工业 RAG 中通过 GRPO + multi-dimensional rewards 联合优化 retrieval 和 generation，减少 72% hallucination。验证 co-adaptive RAG 方向可行，但在 FAQ/客服场景，非形式化数学。

- **调研总结**: Autoformalization 领域 2025-2026 年处于快速发展期。RL for autoformalization（FormaRL、Wang et al.）、retrieval-augmented autoformalization（Aria、DDR、DRIFT）、test-time RL（TTRL）、co-adaptive retrieval（R3、Reinforced-IR）分别是活跃的研究线。但这四条线尚未交叉：(a) 现有 RL for autoformalization 均为 training-time；(b) 现有 retrieval-augmented autoformalization 均用 static retriever；(c) 现有 TTRL 均面向 informal reasoning 的 binary reward；(d) 现有 co-adaptive retrieval 未应用于 Lean 4。Proposal 的定位——在这四条线的交叉点上——是一个真实存在的 gap。

【Trivial Alternative 检验】:

最直接的 trivial alternative 是 **Best-of-N sampling + CriticLean filtering + static DDR retrieval**：给定同等 test-time compute，从 base formalizer（如已 SFT/RL 训练好的模型）采样大量候选，用 DDR 做 static retrieval 增强，然后用 CriticLean 过滤。这不需要 test-time 权重更新，也不需要 co-adaptive retrieval。

Proposal 的增量价值在两处：
1. **Weight adaptation**：当模型的 output space 根本不包含正确的 OOD formalization 时（MathAtlas MA-Hard 2.6%），任何 inference-time scaling 都无法找到不存在的解。这个论点在概念上成立，但实证强度取决于 OOD 程度——如果 pass@128 或 pass@512 仍然很低，才能证明 weight adaptation 是必要的。
2. **Co-adaptive retrieval**：static retriever 无法跟踪 formalizer 在 TTRL 过程中行为的漂移。但这个论点有一个隐含假设：formalizer 在 50-200 步 TTRL 后行为漂移足够大，以至于 static retriever 的 recall 显著下降。这一点未被验证。

**结论**：Trivial alternative 威胁是 **中等** 的。在 near-OOD 场景下，Best-of-N + static RAG + CriticLean filtering 可能已经足够好。增量价值主要体现在 far-OOD 场景（如 MA-Hard），前提是 inference-time scaling 确实触顶。Proposal 意识到了这一点并包含了 compute-matched baseline，这是正确的。

【前提假设检验】:

核心 claim 的逻辑链条包含以下未经验证的假设：

1. **"Lean 4 的 unknownIdentifier 错误可以作为 oracle-quality retrieval training signal"** — 这是整个 co-adaptive retrieval 的基石。概念上合理（错误确实指名缺失的 identifier），但实际有两个子假设：(a) 错误中提到的 identifier 确实对应 Mathlib 中可检索的常量（而非 locally-defined 变量或 model 自创的名字），(b) 基于这些 positives/negatives 的 InfoNCE 训练在仅 ~240 对/cycle 的信号密度下能有效更新 retriever。假设 (a) 的 Phase -1 micro-analysis 是合理的验证手段；假设 (b) 的低数据量下 contrastive learning 效果存疑。

2. **"CriticLean 在 OOD + 严重 class imbalance (<10% compilable) 下仍可用"** — CriticLean 训练于 balanced 250/250 distribution，在 <10% compilable 的 TTRL distribution 下 precision 可能大幅下降（误将错误 formalization 判为正确）。Phase 0 calibration 是必要的，但如果 precision 不过关，整个 reward structure 需要大幅调整。这是一个 **高风险假设**。

3. **"Binarize-then-enrich 保留 DDRL 的 debiasing 性质"** — 先 binarize（compilation AND critic），然后在 accepted candidates 中加 BEq enrichment。DDRL 的理论分析基于 binary reward 的特定结构；加入连续的 enrichment 是否破坏 debiasing 性质未被分析。这是一个 **中等风险假设**。

4. **"TTRL 过程中 formalizer 行为漂移足以使 static retriever 失效"** — 这是 co-adaptive retrieval 必要性的前提。在 TTRL 的典型步数（几百步）内，8B 模型的权重更新幅度是否足以改变 retrieval 需求模式是未知的。如果漂移很小，co-adaptive retrieval 的增量价值就很小。

5. **"Compilation success rate 在 OOD TTRL 中能从极低 baseline 逐步上升"** — 如果 MA-Hard 的 pass@32 在 TTRL 初期接近 0%，GRPO 几乎收不到 positive signal，可能无法启动学习。Curriculum（Phase 4）部分缓解了这一问题，但 cold-start 风险仍在。

【3 维度打分】:

1. **Novelty: 中（偏强）** — 
   核心 novelty 在于识别并利用 formal language 与 informal reasoning 之间的 **结构性不对称**：Lean 4 的编译错误提供了 oracle-quality、token-level 的 retrieval training signal，这在 informal reasoning 中不存在。这一 insight 是 **genuinely novel** 的——R3 (NeurIPS 2025) 和 Reinforced-IR (ACL 2025) 验证了 co-adaptive retrieval 的可行性，但未在 formal language setting 中利用编译器反馈作为 retrieval signal；Aria (ICLR 2026) 和 DDR 做了 retrieval for autoformalization 但 retriever 是 static 的；FormaRL (COLM 2025) 和 Wang et al. 做了 RL for autoformalization 但在 training time 且无 retrieval adaptation。四条研究线的交叉点确实是空白。
   
   然而，novelty 的限制在于：(a) 这本质上是一篇 **combination paper**——将 DDRL + GDPO + CriticLean + R3/Reinforced-IR 的既有技术应用到新 domain，每个组件的技术贡献是 adaptation 而非 invention；(b) "binarize-then-enrich" 虽填补了 DDRL 论文自述的 future work，但技术深度有限——它是一个 two-layer heuristic 而非有理论支撑的 principled solution；(c) 核心发现如果 positive（"利用结构化反馈比 binary 反馈好"），审稿人可能会说 "intuitive, not surprising"。

2. **Significance: 中** — 
   研究问题本身重要：OOD autoformalization 是实用化形式化数学的关键瓶颈（MathAtlas MA-Hard 2.6% 说明 SOTA 几乎无法处理 graduate-level math）。如果 TTRA 在 far-OOD 上显著提升（如从 2.6% 到 8-10%），这将是有意义的进展。"Test-time learning as a third scaling axis for formal math" 的 framing 也有启发价值（与 TEMPO 的 EM 视角互补）。
   
   但 significance 受限于：(a) autoformalization 目前仍是一个 **相对 niche** 的子领域，对 broader AI community 的直接影响有限；(b) 方法的可推广性存疑——co-adaptive retrieval via compiler error 是 formal language 特有的，不易迁移到其他 domain；(c) 即使所有组件 work，绝对性能提升可能仍然有限（far-OOD autoformalization 的天花板可能本身很低）。

3. **Related Work: 强** — 
   这是 proposal 最强的维度。覆盖了截至 May 2026 的几乎所有相关工作：RL for autoformalization (FormaRL, Wang et al., ReForm)、retrieval-augmented autoformalization (Aria, DDR, DRIFT, CRAMF, ProofBridge)、TTRL 及其改进 (DDRL, GDPO, T³RL, SCOPE)、semantic critics (CriticLean)、test-time compute (FormalEvolve, TEMPO)、error analysis (AMBER)。每篇工作的差异化定位清晰。对 R3、Reinforced-IR、TTARAG 的 co-adaptive retrieval 线引用准确。我调研中发现的所有关键论文均已被覆盖。唯一可补充的是 Reinforced Co-adaptation Framework (arXiv:2602.22584) 作为工业 RAG 中 co-adaptive 的额外验证。

【概率估计】: [23% - 33%] 中位 27%

【估计理由】: 
Idea 的核心 insight（formal language 的结构化编译反馈可作为 co-adaptive retrieval 的 oracle-quality training signal）是 genuinely novel 且 well-motivated 的，支撑了概率下界不低于 23%。Related work 覆盖极为充分，差异化定位清晰。

但概率受到三方面限制：
- **Novelty 的 "combination" 性质限制了上界**：四个组件（co-adaptive retrieval + CriticLean reward + DDRL debiasing + GDPO multi-reward）中每个的技术贡献都是 adaptation-to-new-domain 而非 fundamental innovation。AAAI 审稿人可能认为这是 "well-engineered integration" 而非 "conceptual breakthrough"。
- **"Surprising" 检验未通过**：核心发现如果 positive（"利用编译器结构化反馈比 binary feedback 好"），这是 intuitive 而非 surprising 的。审稿人不太会写 "I would not have expected this"。
- **系统复杂度过高**：4 phases、dual loops、multi-tier rewards、curriculum learning、多个 go/no-go gates——这些增加了实现可靠性，但也让 paper 读起来像 systems paper 而非 idea paper。在 AAAI 这样的综合会议上，过于复杂的 pipeline 可能被要求 "simplify and focus on the core contribution"。

中位 27% 反映了：idea 方向正确、gap 真实存在、but 核心发现偏 incremental、combination nature 是主要扣分项。

【主要风险】:
1. **Combination paper 风险**：审稿人可能认为将 DDRL + GDPO + CriticLean + R3 组合应用到 autoformalization 是 engineering integration 而非 scientific contribution——"the whole is not greater than the sum of its parts"。每个组件的技术深度不足以独立支撑论文，但组合在一起又过于复杂。
2. **Core finding 缺乏 surprise**：如果实验结果是 "structured feedback > binary feedback" 且 "adaptive retrieval > static retrieval"，审稿人可能会说 "I would have guessed this, the interesting question is by how much, and the margin might not be large enough to justify the complexity"。
```

Sources:
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)
- [DDRL: Understanding and Mitigating Spurious Signal Amplification in Test-Time RL](https://arxiv.org/html/2604.21327)
- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242)
- [CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization](https://arxiv.org/abs/2507.06181)
- [CriticLeanGPT-Qwen3-14B-RL on HuggingFace](https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL)
- [FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)](https://arxiv.org/abs/2508.18914)
- [Aria: An Agent For Retrieval and Iterative Auto-Formalization (ICLR 2026)](https://arxiv.org/abs/2510.04520)
- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)
- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652)
- [FormalEvolve: Neuro-Symbolic Evolutionary Search for Autoformalization](https://arxiv.org/abs/2603.19828)
- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)
- [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/abs/2604.19295)
- [Towards Faithful Industrial RAG: Reinforced Co-adaptation](https://arxiv.org/abs/2602.22584)
- [Online Reinforcement Learning for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)
- [AMBER: Construction-Verification Benchmark](https://arxiv.org/abs/2602.01291)
- [GDPO Explained (AI Papers Academy)](https://aipapersacademy.com/gdpo/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ddda828-f1db-4bd4-9b61-6edb9903f650",
  "isSidechain": false,
  "requestId": "req_011CbUTNUoHdxsMg2EakvN9u",
  "type": "assistant",
  "uuid": "7346e163-e3e2-4e66-b442-c55203feb146",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGNrE3cwoJprz9jNiGjVFb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 33402,
      "output_tokens": 7705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7705,
          "cache_read_input_tokens": 33402,
          "cache_creation_input_tokens": 1668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1668
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "7346e163-e3e2-4e66-b442-c55203feb146",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal objective acceptance likelihood",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "7346e163-e3e2-4e66-b442-c55203feb146",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal objective acceptance likelihood",
  "sessionId": "40328dc9-f852-4865-9336-216d513967f9"
}
```

---
