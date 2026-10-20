# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # TTRA: Critic-Guided Test-Time Ret

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/f293bf8a-8e22-4fc3-9edb-c980c35f7fc1.jsonl`
- **Structured JSON:** [`05554e1654fa363a20b3.json`](../../sessions/05/05554e1654fa363a20b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T06:01:43.142Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T06:01:43.142Z",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization\n\n## Core Problem\n\nCurrent autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in multi-tier reward settings; and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation.\n\nA key structural asymmetry motivates our approach: in informal math reasoning, TTRL obtains only binary correct/incorrect signals with no information about *why* a solution failed or *what knowledge is missing*—and binary rewards create a fundamental degeneracy for policy gradient methods, leading to diversity collapse (Dymetman, arXiv:2605.02375). In contrast, Lean 4's compiler produces machine-parseable error messages that precisely identify missing identifiers, type mismatches, and unresolved typeclass instances—constituting a graded hierarchy of structured feedback signals. Critically, these signals are not merely \"richer rewards\": when a compilation error reports `unknownIdentifier \"Finset.sum_bij\"`, it provides an oracle-quality, token-level retrieval training signal that directly specifies which Mathlib dependency is needed. Such signals are unavailable during pre-training or SFT (no compilation feedback), discarded by inference-time search methods like FormalEvolve (which uses only compile success/failure), and unexploited by static retrieval pipelines like Aria (whose retriever cannot adapt). Only during test-time RL can these structured error signals be continuously collected and used to co-adapt the retriever—making co-adaptive retrieval an emergent capability uniquely enabled by TTRL in formal language settings.\n\nFor domains where model performance is extremely low (MathAtlas MA-Hard: 2.6%), inference-time scaling alone is insufficient: the fixed model's output space may not contain correct formalizations for truly OOD domains, so no amount of sampling can find what the model cannot generate. Weight adaptation is necessary, and it produces compounding improvement—better formalizations yield more informative compilation errors, which improve the retriever, which enables even better formalizations in subsequent rounds.\n\n## Research Opportunity\n\nFour independently validated capabilities have never been combined, and their integration is enabled by the structured feedback properties unique to formal languages.\n\n(1) **Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode.** R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv:2601.11443, Jan 2026) shows test-time retrieval adaptation via self-supervised prediction. The prevalence of identifier hallucination is established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math stem from hallucination of non-existent theorems/definitions. DDR (arXiv:2511.11990) quantifies Hall_m=0.21-0.39 across frontier LLMs, reduced to <0.02 with retrieval. The RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as a primary error class. MathAtlas (arXiv:2605.14061, May 2026) shows a 66% advantage for Mathlib-grounded definitions (27.9% vs 16.8%, p<0.001). Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL—where Lean's structured error taxonomy provides graded, machine-parseable signals for retriever training.\n\n(2) **TTRL with debiasing has advanced but remains limited to binary rewards in informal settings.** DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed ±1 advantages, and consensus-based off-policy refinement (19.0% relative improvement over ETMR on AIME 2024; 4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B), but assumes binary rewards with 'more expressive advantage formulations' left as future work. GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization but does not address debiasing. T³RL (arXiv:2603.02203, Mar 2026) introduces tool-verified rewards into TTRL, using code execution output to upweight verified rollouts—but collapses all tool feedback into a single binary bit (verified/unverified), discarding the internal structure of tool output. SCOPE (arXiv:2512.15146, Dec 2025) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, but remains within the homogeneous binary-reward paradigm. The combination of DDRL's debiasing with GDPO's multi-reward normalization for heterogeneous reward components (hard binary gate + noisy soft critic + drifting population statistic) has not been attempted.\n\n(3) **CriticLean provides the missing semantic reward signal.** CriticLeanGPT-14B-RL (arXiv:2507.06181, July 2025) achieves 84.8% accuracy on balanced CriticLeanBench (87.0% for 32B), but CriticLeanBench's 250/250 balanced distribution differs from OOD TTRL's heavily skewed distribution (<10% compilable). This distributional shift gap motivates our Phase 0 calibration protocol.\n\n(4) **Online RL for autoformalization validated at training time only.** Wang et al. (NeurIPS 2025 MAR Workshop) achieves TC1: 17.29%→26.01% on RLMEval using GRPO with BEq + embedding rewards, but operates at training time on in-distribution problems without retrieval, test-time adaptation, or a trained semantic critic.\n\nRecent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.\n\n## Research Landscape\n\n**(1) RL for autoformalization.** FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards (pass@1: 4%→26% on ProofNet). Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with BEq + embedding similarity (TC1: 17.29%→26.01%, TC50: 76.41%→85.46% on RLMEval)—closest prior work but training-time, no retrieval, no test-time adaptation. ReForm (arXiv:2510.24592) applies PBSO position-aware RL rewards for reflective autoformalization; ReForm-8B (Qwen3-8B) achieves +18.0pp average improvement.\n\n**(2) Semantic critics and iterative refinement.** CriticLean (July 2025) introduces CriticLeanGPT (32B-RL: 87.0%, 14B-RL: 84.8% on balanced CriticLeanBench). ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO. Monotonic Refinement achieves 90.27% on miniF2F through multi-model ensemble orchestration. These cannot adapt model weights to new domains.\n\n**(3) Debiased RL, multi-reward optimization, and TTRL reward improvements.** DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification exclusively with binary rewards; GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward normalization. Binary Rewards and RL (Dymetman, arXiv:2605.02375, May 2026) proves binary rewards create fundamental degeneracy (diversity collapse). T³RL (arXiv:2603.02203, Mar 2026) introduces external tool verification into TTRL, upweighting verified rollouts via verification-aware voting—but treats tool output as a single binary signal (verified/unverified), discarding the structured content of tool feedback. SCOPE (arXiv:2512.15146) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, remaining within the homogeneous binary-reward paradigm. All these improvements assume homogeneous reward signals. TTRA addresses a qualitatively different problem: heterogeneous reward components (hard compilation gate, noisy critic signal, policy-drifting BEq statistic) requiring a two-layer binarize-then-enrich adaptation.\n\n**(4) Retrieval-augmented autoformalization and co-adaptive retrieval.** Aria (ICLR 2026, arXiv:2510.04520) achieves ProofNet 91.6% compilation / 68.5% accuracy and 42.9% on homological conjectures (vs. 0% for all others) via dependency graph + iterative formalization + AriaScorer—current frontier of retrieval-augmented autoformalization, but a fixed inference pipeline: retriever does not adapt to formalizer's evolving behavior and model weights are not updated. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF. DDR builds a 500K-sample dataset (Hall_m reduced from 0.21-0.39 to <0.02). CRAMF indexes 26K+ Mathlib definitions. ProofBridge (ICLR 2026, arXiv:2510.15681) uses joint embeddings + retrieval-augmented fine-tuning. On co-adaptive retrieval: R3 (NeurIPS 2025, arXiv:2510.24652) optimizes RAG retrieval via reinforced contrastive learning; Reinforced-IR (ACL 2025) alternates RLRF/RLGF; TTARAG (arXiv:2601.11443) demonstrates test-time retrieval adaptation. None applied to autoformalization or Lean 4.\n\n**(5) Test-time compute for autoformalization.** FormalEvolve (arXiv:2603.19828, Mar 2026) formulates autoformalization as budgeted evolutionary search (SH@100=58.0% CombiBench, 84.9% ProofNet) using LLM-driven mutation/crossover with AST rewrites. This is orthogonal to TTRA: FormalEvolve searches a fixed model's output space without weight adaptation or retriever co-adaptation, discarding compilation error structure. TEMPO (arXiv:2604.19295, Apr 2026) formalizes test-time training as EM (policy refinement = M-step, critic recalibration = E-step), proving that omitting recalibration leads to ELBO degradation and diversity collapse—a conceptual parallel to TTRA's dual-loop where omitting retriever co-adaptation (= static retrieval TTRL) accumulates retriever-formalizer distribution mismatch.\n\n**(6) Error analysis and identifier hallucination.** The AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are identifier hallucination (32.7% competence, 15.2% incomplete, 4.8% syntax). RAutoformalizer (ICLR 2025 Spotlight) categorizes errors into 'Hallucination' vs 'Others'. MathAtlas (arXiv:2605.14061) introduces 52K graduate-level problems (best: 2.6% on MA-Hard).\n\nAfter exhaustive search through May 2026, no work combines co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, a calibrated semantic critic with distributional shift analysis, principled adaptation of binary-reward debiased RL to heterogeneous multi-tier rewards, and test-time adaptation on unlabeled OOD domains. Existing retrieval methods (Aria, DRIFT, DDR) use static retrievers; existing RL methods (FormaRL, Wang et al., ReForm) operate at training time; existing test-time methods (FormalEvolve) search without learning; existing TTRL improvements (T³RL, SCOPE, DDRL) assume homogeneous binary rewards.\n\n## Proposed Approach\n\nWe propose TTRA (Test-Time Retrieval-Augmented autoformalization), making TTRL viable for autoformalization through three technical innovations unified by a single insight: formal languages' structured compilation feedback creates a graded hierarchy of adaptation signals unavailable in informal reasoning, enabling co-adaptive test-time learning as a new scaling axis for formal mathematics—complementing training-time compute (more data, larger models) and inference-time compute (more samples, longer search). Drawing a conceptual parallel with TEMPO's EM formalization of TTT, TTRA's dual-loop design ensures the retriever co-adapts with the formalizer (analogous to not omitting the E-step), preventing the retriever-formalizer distribution mismatch that would degrade a static-retrieval TTRL.\n\n**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Quantify Lean 4 error taxonomy coverage on OOD domains. Compile 500 candidate formalizations on Con-NF and 500 on MathAtlas MA-Hard, classify errors into: Tier 1 (direct identifier: `lean.unknownIdentifier`, `unknown namespace`), Tier 2 (type-based: `type mismatch`, `failed to synthesize instance`), Tier 3 (indirect: tactic/elaboration/syntax errors). Thresholds: Tier 1 ≥40% → co-adaptive retrieval well-supported; 20-40% → rely on Tier 1+2; <20% → fall back to Tier 2 with type-signature matching. Prior evidence strongly supports ≥40% (AMBER: 47.3%; DDR: Hall_m=0.21-0.39; RAutoformalizer treats 'Hallucination' as primary class; CRAMF documents systematic fabrication). Phase -1 validates on our specific model/domain. Simultaneously verify MathAtlas MA-Hard gold formalization coverage; if <50%, downgrade to secondary benchmark and activate IndiMathBench (arXiv:2512.00997) as contingency OOD benchmark. Resource: ~8 A100-hours generation, ~10 CPU-hours parsing.\n\n**Phase 0 — Minimal Pilot with Critic Calibration (De-risking).** FormaRL's GRPO pipeline with CriticLean-14B replacing LLM-consistency reward. 200 Con-NF + 200 FormalMATH number theory problems. Primary hypothesis: ≥3pp BEq@1 over compilation-only GRPO on Con-NF. Critic calibration under distributional shift: measure precision/recall separately on skewed distribution (<10% compilable); report calibration curves; if precision <80%, introduce confidence gating >0.8. Go/no-go: proceed only if primary hypothesis confirmed AND precision ≥80%. Additionally, establish critic calibration monitoring protocol: during subsequent TTRL phases, checkpoint critic precision every ~100 GRPO steps; if precision drops >10pp from Phase 0 baseline, adjust confidence threshold (periodic recalibration, motivated by TEMPO's finding that reward signal drift without recalibration leads to performance plateaus). Resource: ~50 A100-hours, 2-3 weeks.\n\n**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune Qwen3-8B using DDR's 500K-sample dataset and GRPO with R(y, x) = r_compile × (α·r_critic + β·r_beq). r_compile ∈ {0,1} (Kimina Lean Server, 128 parallel workers); r_critic ∈ {0,1} (CriticLeanGPT-Qwen3-14B-RL, gated by Phase 0 threshold); r_beq ∈ [0,1] (BEq consensus density). α=0.7, β=0.3. Fallback: when <4 of K=32 compile, R = r_compile × r_critic.\n\n**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever (DDR-style dense encoder) is explicitly updated during TTRL. This exploits Lean 4's unique structural property: compilation errors provide oracle-quality, token-level retrieval training signals that directly specify which Mathlib dependencies are needed—signals unavailable during pre-training, discarded by inference-time search, and unexploited by static retrieval pipelines.\n\n  Loop 1 — Formalizer GRPO (every step): K=32 candidates, compile, multi-tier rewards, debiased GRPO.\n\n  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Graded error hierarchy:\n    (a) Tier 1 (highest confidence): `lean.unknownIdentifier` names missing constant → hard negatives from retrieved set; constant from CRAMF/DDR index = positive. `unknown namespace` → coarser module-level positive.\n    (b) Tier 2 (moderate): `type mismatch` → type signatures matched against Mathlib type index, 0.5× weight. `failed to synthesize instance` → typeclass instances as positives.\n    (c) Tier 3: tactic/elaboration/syntax → negatives only.\n    (d) Compilation success → all retrieved dependencies in compiled output = confirmed positives.\n    (e) Weighted InfoNCE: L = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), w_k = 1.0 (Tier 1/confirmed), 0.5 (Tier 2), τ=0.07.\n    (f) Decoupled optimization (per R3 and Reinforced-IR): retriever gradient does not flow through formalizer. FAISS rebuild after each update.\n\n  Signal density: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle.\n\n**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** Autoformalization's reward components are fundamentally heterogeneous: compilation is a hard binary gate (non-negotiable), the critic is a noisy soft signal (calibrated but imperfect), BEq is a population statistic (drifts with policy). This heterogeneity distinguishes TTRA from all existing TTRL reward improvements (DDRL, T³RL, SCOPE, GDPO), which assume homogeneous reward signals. Neither DDRL alone (cannot handle multi-tier) nor GDPO alone (does not address spurious amplification) suffices:\n\n  (a) Binarization layer: r_accept = I(r_compile=1 AND r_critic=1). Balanced sampling (exclude 30-70% ambiguity zone per DDRL). Fixed advantages: +1 (accepted), -1 (rejected). Consensus off-policy refinement: M=128, rejection-sample >80% acceptance, SFT 5 epochs.\n  (b) GDPO-style enrichment: among accepted candidates, per-reward decoupled normalization for BEq. Additive bonus δ·norm(r_beq) to +1 advantage, δ=0.3.\n\n**Phase 4 — Progressive Domain Curriculum.** (a) Near-distribution warm-start: compilation ≥40%, critic approval ≥60%, BEq@32 ≥3pp above baseline. Timeout: 500 steps. (b) Retrieval bootstrapping: Tier 1/2 errors feed retriever updates. Transition: recall@10 ≥30%, compilation ≥25%. Early transition: plateau <2pp over 200 steps. (c) Far-OOD: algebraic geometry, condensed mathematics, MathAtlas MA-Hard with adaptive fallback.\n\n**Contribution Floor Analysis.** (1) Co-adaptive retrieval + CriticLean TTRL alone: first co-adaptive retrieval for autoformalization + first TTRL for formal math with calibrated critic. (2) Binarize-then-enrich alone: addresses DDRL's explicit future work on multi-tier rewards. (3) Curriculum: droppable. (4) Essential floor: CriticLean TTRL outperforms compilation-only (Phase 0 gate) AND ≥1 of co-adaptive retrieval / binarize-then-enrich shows statistically significant improvement.\n\n**Evaluation.**\n\n  *Benchmarks:* In-distribution: miniF2F-test (244), ProofNet (~371). Multi-domain: FormalMATH (5,560). OOD stress tests: Con-NF, CombiBench, MathAtlas MA-Hard (700 entities, best: 2.6%; contingency: IndiMathBench if gold coverage <50%).\n\n  *Metrics:* BEq@K, BEq+@K (per DRIFT), pass@K (K=1,32), compilation@K on all benchmarks. GTED (arXiv:2507.07399, continuous [0,1] similarity with better precision-recall balance than BEq) on OOD benchmarks. Hall_m (DDR's hallucination rate) in retriever ablation. Human evaluation: 100-150 samples on Con-NF + 200 samples on MathAtlas MA-Hard (inter-annotator agreement reported).\n\n  *Same-scale primary baselines (~7-8B):* (1) FormaRL (Qwen2.5-Coder-7B, COLM 2025); (2) Online RL for Autoformalization (Wang et al., faithfully reimplemented if code unavailable); (3) DRIFT with Qwen3-8B (ICLR 2026); (4) Aria (ICLR 2026, reimplemented on shared benchmarks or reported numbers annotated); (5) StepFun-Formalizer-7B (AAAI 2026, open-source); (6) ReForm-8B (Qwen3-8B, arXiv:2510.24592); (7) compilation-only TTRL and critic-only TTRL ablations.\n\n  *Cross-paradigm reference:* FormalEvolve (arXiv:2603.19828, reported SH@100 on CombiBench/ProofNet).\n\n  *Compute-matched baseline:* Best-of-N (matched FLOPs) + CriticLean filtering: allocate equivalent test-time compute to sampling more candidates from base formalizer, filter with CriticLean-14B, report BEq@1 and compilation@1. Directly tests whether TTRA's weight adaptation provides value beyond inference-time scaling.\n\n  *Ablations:* (a) Standard GRPO vs. DDRL vs. binarize-then-enrich (component-wise); (b) frozen vs. co-adaptive retriever; (c) Tier 1-only vs. Tier 1+2 vs. all-tier error signals; (d) no curriculum vs. progressive; (e) CriticLean-14B reward vs. embedding-based similarity reward (isolating trained critic value).\n\n  *Sensitivity:* N_ret ∈ {25, 50, 100}; δ ∈ {0.0, 0.1, 0.3, 0.5} (δ=0.0 = pure DDRL); ambiguity zone ∈ {[20%-80%], [30%-70%], [40%-60%]}; critic confidence threshold ∈ {0.6, 0.7, 0.8, 0.9}; K ∈ {16, 32, 64} (test-time compute scaling behavior).\n\n  *Cross-scale references:* ATF-32B, ATLAS (NeurIPS 2025), Monotonic Refinement (multi-model ensemble). All tables annotate scale and compute.\n\n  *Statistical rigor:* Key comparisons ≥3 seeds, mean ± std, bootstrap CI (p<0.05).\n\n## Detailed Description\n\nTTRA makes TTRL viable for autoformalization by exploiting a structural asymmetry: Lean 4's compiler provides oracle-quality, token-level feedback (identifier names, type signatures, typeclass requirements) that serves simultaneously as retriever training signal, multi-tier reward components, and domain adaptation indicators—signals unavailable in informal reasoning and unexploited by existing methods. The dual-loop architecture co-adapts the retriever during test-time RL via weighted InfoNCE over Lean 4's error hierarchy, addressing the limitation that static retrievers (Aria, DRIFT, DDR) cannot track formalizer evolution. CriticLean-14B integration includes distributional shift calibration and periodic drift monitoring (motivated by TEMPO's EM analysis of reward signal degradation). Binarize-then-enrich addresses the specific gap between DDRL (binary debiasing) and GDPO (multi-reward normalization) for formal verification's heterogeneous reward landscape—a qualitatively different problem from the homogeneous-reward improvements in T³RL and SCOPE. Compute-matched evaluation against best-of-N + critic filtering directly tests whether weight adaptation provides value beyond inference-time scaling. The framework positions test-time learning as a third scaling axis for formal mathematics alongside training-time and inference-time compute.\n\n## Key References\n\n- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)\n- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)\n- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, NVIDIA, January 2026)\n- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv:2507.06181, ByteDance/Nanjing)\n- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)\n- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv:2510.24652)\n- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)\n- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv:2601.11443, January 2026)\n- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv:2602.01291, February 2026)\n- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)\n- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\n- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)\n- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)\n- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\n- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)\n- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv:2511.11990)\n- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)\n- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)\n- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)\n- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\n- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv:2505.02735)\n- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)\n- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\n- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026, arXiv:2510.04520)\n- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026, arXiv:2510.15681)\n- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv:2510.24592)\n- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv:2512.00997, Microsoft Research)\n- FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv:2603.19828, March 2026)\n- Binary Rewards and Reinforcement Learning: Fundamental Challenges (Dymetman, arXiv:2605.02375, May 2026)\n- TEMPO: Scaling Test-time Training for Large Reasoning Models (arXiv:2604.19295, April 2026)\n- T³RL: Tool Verification for Test-Time Reinforcement Learning (arXiv:2603.02203, March 2026)\n- SCOPE: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning (arXiv:2512.15146, December 2025)\n- GTED: Generalized Tree Edit Distance: A Faithful Evaluation Metric for Statement Autoformalization (arXiv:2507.07399)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1400-1900 A100-80GB hours (Phase -1 micro-analysis + MathAtlas coverage: ~10h; Phase 0 pilot + calibration: ~50h; Phase 1 base GRPO: ~300h; DDR retriever + co-adaptive updates: ~100h; Phase 4 progressive TTRL + ablations: ~400h; CriticLean-14B inference all phases: ~200-300h; N_ret/δ/ambiguity/critic-threshold/K sensitivity: ~100h; baseline evaluation (Aria reimpl + StepFun + ReForm): ~100-120h; compute-matched best-of-N baseline: ~30h; CriticLean vs embedding ablation: ~25h; multi-seed (3 seeds × key ablations): ~200h; human eval annotation: ~60-80h; miniF2F/ProofNet + remaining eval: ~80h) + 15,000-20,000 CPU-hours Lean verification (Kimina Lean Server), timeline: 14-18 weeks (0.5 wk Phase -1; 2-3 wk Phase 0 + go/no-go; 3 wk Phase 1; 2 wk retriever infrastructure; 4 wk TTRL experiments; 3 wk ablations + sensitivity + multi-seed; 2 wk writing), estimated_gpu_cost: $2,800-$4,700 + $750-$1,000 CPU + ~$1,500-$2,500 human annotation. GPU architecture: policy (8B) + ref (8B) on 4×A100 tensor parallel, CriticLean-14B on dedicated 2×A100 with vLLM batch inference, retriever + FAISS on CPU/1×A100; async pipeline.\n- **human_in_loop**: gpu_hours: 1100-1500 A100-80GB hours (~25% reduction), timeline: 11-14 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,200-$3,700 + $600-$800 CPU + ~$1,200-$2,000 annotation\n- **auto_research**: gpu_hours: 2000-2700 A100-80GB hours (full sweep), timeline: 8-11 weeks, claude_api_cost: $800-$1,200, estimated_gpu_cost: $4,000-$6,700 + $1,000-$1,350 CPU + ~$1,500-$2,500 annotation, speed_bottleneck: Lean 4 compilation (~3.65s/statement warm cache, ~0.10s amortized at 64 workers). CriticLean-14B ~0.5s/candidate (→~0.1-0.2s with vLLM). Retriever co-adaptation ~15 min/cycle (re-encode 26K constants, rebuild FAISS)."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T06:01:43.146Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T06:01:43.146Z",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

## Round 1

51 recorded events

### User

_source line 3 · 2026-05-28T06:01:43.195Z_

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
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "9f2d720a-312d-42a7-8cbd-f5159ce9076b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T06:01:43.193Z_

```json
{
  "parentUuid": "9f2d720a-312d-42a7-8cbd-f5159ce9076b",
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
  "uuid": "0092b707-3e59-42b7-b425-9d2152ffc012",
  "timestamp": "2026-05-28T06:01:43.193Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T06:01:43.193Z_

```json
{
  "parentUuid": "0092b707-3e59-42b7-b425-9d2152ffc012",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b1dbd70f-d882-492a-9090-2366a6b36d59",
  "timestamp": "2026-05-28T06:01:43.193Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
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
  "leafUuid": "b1dbd70f-d882-492a-9090-2366a6b36d59",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal acceptance probability",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Assistant

_source line 8 · 2026-05-28T06:01:50.176Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed proposal for TTRA (Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization). I need to evaluate this as the "入口评审 agent" following the specified rubric. 

Let me first do the required web searches to understand the field landscape before making any judgments.

Let me search for:
1. Recent work on test-time RL for autoformalization
2. Co-adaptive retrieval in formal mathematics
3. DDRL and debiased GRPO methods
4. CriticLean and semantic critics for formal math


5. The current state of autoformalization benchmarks and methods

I'll start with these searches to get a sense of what's already been done in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1dbd70f-d882-492a-9090-2366a6b36d59",
  "isSidechain": false,
  "requestId": "req_011CbUTYbaMqAxxscPe4YGEF",
  "type": "assistant",
  "uuid": "e8eddf3e-942e-4a6f-a148-84252705394b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdoGtvbXC5HWv5YX2BVCyv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 23750,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 280,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-28T06:01:50.187Z_

I need to conduct thorough field research before making any assessment. Let me start with targeted web searches to understand the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8eddf3e-942e-4a6f-a148-84252705394b",
  "isSidechain": false,
  "requestId": "req_011CbUTYbaMqAxxscPe4YGEF",
  "type": "assistant",
  "uuid": "6247ab34-6a2a-403b-9d9b-eeb0c14ab07b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdoGtvbXC5HWv5YX2BVCyv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 23750,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 280,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-28T06:01:50.235Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PLwJR2zN1CM6WzCeVtZWXQ`</summary>

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
  "parentUuid": "6247ab34-6a2a-403b-9d9b-eeb0c14ab07b",
  "isSidechain": false,
  "requestId": "req_011CbUTYbaMqAxxscPe4YGEF",
  "type": "assistant",
  "uuid": "959e65b9-0bd7-4454-9fde-a7a65212d94a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QdoGtvbXC5HWv5YX2BVCyv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 23750,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 280,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-28T06:01:50.243Z_

<details><summary>↩ Tool result · `toolu_01PLwJR2zN1CM6WzCeVtZWXQ`</summary>

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
  "parentUuid": "959e65b9-0bd7-4454-9fde-a7a65212d94a",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "bbcfe03a-9a56-4875-9d6f-8e6d8aad2b74",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "959e65b9-0bd7-4454-9fde-a7a65212d94a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T06:01:53.021Z_

Now let me conduct the required field research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbcfe03a-9a56-4875-9d6f-8e6d8aad2b74",
  "isSidechain": false,
  "requestId": "req_011CbUTZ7rmSC37YSGxzQVpj",
  "type": "assistant",
  "uuid": "e03ef620-c667-4e3e-a584-66e4546245ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177VCcdLA9U9PYHtcABDhPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 23750,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 13 · 2026-05-28T06:01:53.916Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JsX1chij8DHCoGrUTCkqak`</summary>

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
  "parentUuid": "e03ef620-c667-4e3e-a584-66e4546245ae",
  "isSidechain": false,
  "requestId": "req_011CbUTZ7rmSC37YSGxzQVpj",
  "type": "assistant",
  "uuid": "7eb4e073-e54a-4dd5-9526-5852d75b48a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177VCcdLA9U9PYHtcABDhPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 23750,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 14 · 2026-05-28T06:01:54.463Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LAmxs2fQQheuoETvcLE3Fk`</summary>

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
  "parentUuid": "7eb4e073-e54a-4dd5-9526-5852d75b48a3",
  "isSidechain": false,
  "requestId": "req_011CbUTZ7rmSC37YSGxzQVpj",
  "type": "assistant",
  "uuid": "c27265cf-4d5f-4d49-906b-71576b99f025",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177VCcdLA9U9PYHtcABDhPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 23750,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 15 · 2026-05-28T06:01:54.914Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W1oW9ntjwquaUM7ZaQxdZL`</summary>

```json
{
  "query": "CriticLean CriticLeanGPT semantic critic mathematical formalization 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c27265cf-4d5f-4d49-906b-71576b99f025",
  "isSidechain": false,
  "requestId": "req_011CbUTZ7rmSC37YSGxzQVpj",
  "type": "assistant",
  "uuid": "fad8e510-7a8b-4da5-9980-f10fa10fbe43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177VCcdLA9U9PYHtcABDhPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 23750,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 16 · 2026-05-28T06:01:55.848Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011tBjzq3W4aS1cFEYrB9W41`</summary>

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
  "parentUuid": "fad8e510-7a8b-4da5-9980-f10fa10fbe43",
  "isSidechain": false,
  "requestId": "req_011CbUTZ7rmSC37YSGxzQVpj",
  "type": "assistant",
  "uuid": "eb70e44f-e137-4c2d-a04c-bd809d39ec15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177VCcdLA9U9PYHtcABDhPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 23750,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 17 · 2026-05-28T06:01:56.275Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LxxSbVHuUPcuvssn41nsAg`</summary>

```json
{
  "query": "Aria ICLR 2026 autoformalization retrieval dependency graph DDR identifier hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb70e44f-e137-4c2d-a04c-bd809d39ec15",
  "isSidechain": false,
  "requestId": "req_011CbUTZ7rmSC37YSGxzQVpj",
  "type": "assistant",
  "uuid": "9600c28e-e961-488e-adfa-c05936883c5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177VCcdLA9U9PYHtcABDhPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 23750,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 18 · 2026-05-28T06:02:01.892Z_

<details><summary>↩ Tool result · `toolu_01LAmxs2fQQheuoETvcLE3Fk`</summary>

```text
Web search results for query: "DDRL debiased GRPO test-time RL spurious signal amplification ACL 2026"

Links: [{"title":"Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/html/2604.21327"},{"title":"Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients","url":"https://arxiv.org/pdf/2510.18924"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Dual Consensus: Escaping from Spurious Majority in Unsupervised RLVR via Two-Stage Vote Mechanism","url":"https://arxiv.org/html/2603.16223"},{"title":"Mitigating Selection Bias in Large Language Models via Permutation-Aware GRPO","url":"https://arxiv.org/pdf/2603.21016"},{"title":"Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts","url":"https://arxiv.org/pdf/2603.21177"}]

Based on the search results, I found highly relevant information about your query:

Debiased and Denoised test-time Reinforcement Learning (DDRL) is a framework designed to mitigate spurious signals. The research identified that GRPO's normalization mechanism disproportionately amplifies spurious rewards in low-consensus regimes, and GRPO's advantage estimation introduces a systematic bias in the unsupervised setting.

DDRL addresses this through a balanced confidence-aware sampling strategy that selects rollout samples based on their reliability while maintaining a balanced set of positive and negative examples, and replaces group-relative advantage estimation with a bias-corrected scheme that assigns fixed, label-dependent advantages to eliminate the amplification effect. The framework also incorporates a consensus-based off-policy refinement stage after the RL phase, where a rejection sampling dataset is constructed to enable efficient and stable post-RL optimization.

This research appears to be from April 2026 and addresses the problem of spurious signal amplification in test-time reinforcement learning for mathematical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c27265cf-4d5f-4d49-906b-71576b99f025",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "1e87ad2b-81a0-4d08-b2c7-1f207ccabea9",
  "toolUseResult": {
    "query": "DDRL debiased GRPO test-time RL spurious signal amplification ACL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HBcjDQpJPTZTS9VFBpTh6x",
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
      "Based on the search results, I found highly relevant information about your query:\n\nDebiased and Denoised test-time Reinforcement Learning (DDRL) is a framework designed to mitigate spurious signals. The research identified that GRPO's normalization mechanism disproportionately amplifies spurious rewards in low-consensus regimes, and GRPO's advantage estimation introduces a systematic bias in the unsupervised setting.\n\nDDRL addresses this through a balanced confidence-aware sampling strategy that selects rollout samples based on their reliability while maintaining a balanced set of positive and negative examples, and replaces group-relative advantage estimation with a bias-corrected scheme that assigns fixed, label-dependent advantages to eliminate the amplification effect. The framework also incorporates a consensus-based off-policy refinement stage after the RL phase, where a rejection sampling dataset is constructed to enable efficient and stable post-RL optimization.\n\nThis research appears to be from April 2026 and addresses the problem of spurious signal amplification in test-time reinforcement learning for mathematical reasoning."
    ],
    "durationSeconds": 7.425565925999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c27265cf-4d5f-4d49-906b-71576b99f025",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T06:02:02.070Z_

<details><summary>↩ Tool result · `toolu_01JsX1chij8DHCoGrUTCkqak`</summary>

```text
Web search results for query: "test-time reinforcement learning autoformalization Lean 4 2025 2026"

Links: [{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372v1"},{"title":"(PDF) Online Reinforcement Learning for Autoformalization","url":"https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization"},{"title":"Goedel-Prover: Open-Source ATP in Lean 4","url":"https://www.emergentmind.com/topics/goedel-prover"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"Towards Formalizing Reinforcement Learning Theory","url":"https://arxiv.org/pdf/2511.03618"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://openreview.net/pdf?id=k8KsI84Ds7"}]

Based on the search results, here's what I found regarding test-time reinforcement learning, autoformalization, and Lean 4 in 2025-2026:

## Test-Time Reinforcement Learning (TTRL)

Test-Time Reinforcement Learning (TTRL) enables discovery, combination, and reuse of intermediate lemmas autonomously, and for the most difficult problems, it uses Test-Time RL to generate and learn from millions of related problem variants at inference time to enable deep, problem-specific adaptation.

## Recent Breakthroughs in Autoformalization

In 2025, multiple independent systems achieved gold-medal equivalent performance on the International Mathematical Olympiad with formally verified Lean 4 proofs, achieving 80.7% on MiniF2F with pass@8192.

A notable achievement: Using Gauss, Math Inc. completed a challenge set by Fields Medallist Terence Tao to formalize the strong Prime Number Theorem in Lean, which had stalled after 18+ months of human expert effort, in just three weeks.

## Reinforcement Learning Approaches

FormaRL is a reinforcement learning framework for autoformalization that requires only a small amount of unlabeled data, achieving 4-6× improvement in pass@1 autoformalization accuracy.

Online reinforcement learning for autoformalization focuses on translating informal mathematical conjectures into formal statements in Lean 4, addressing the challenge that autoformalization lacks a natural dense reward and using type-check success alone produces syntactically valid but semantically vacuous outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eb4e073-e54a-4dd5-9526-5852d75b48a3",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "2e02b2ed-09b8-468a-bb3e-fe962045b600",
  "toolUseResult": {
    "query": "test-time reinforcement learning autoformalization Lean 4 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011q1YWHX3a6GHr6Rz3zzwGj",
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
      "Based on the search results, here's what I found regarding test-time reinforcement learning, autoformalization, and Lean 4 in 2025-2026:\n\n## Test-Time Reinforcement Learning (TTRL)\n\nTest-Time Reinforcement Learning (TTRL) enables discovery, combination, and reuse of intermediate lemmas autonomously, and for the most difficult problems, it uses Test-Time RL to generate and learn from millions of related problem variants at inference time to enable deep, problem-specific adaptation.\n\n## Recent Breakthroughs in Autoformalization\n\nIn 2025, multiple independent systems achieved gold-medal equivalent performance on the International Mathematical Olympiad with formally verified Lean 4 proofs, achieving 80.7% on MiniF2F with pass@8192.\n\nA notable achievement: Using Gauss, Math Inc. completed a challenge set by Fields Medallist Terence Tao to formalize the strong Prime Number Theorem in Lean, which had stalled after 18+ months of human expert effort, in just three weeks.\n\n## Reinforcement Learning Approaches\n\nFormaRL is a reinforcement learning framework for autoformalization that requires only a small amount of unlabeled data, achieving 4-6× improvement in pass@1 autoformalization accuracy.\n\nOnline reinforcement learning for autoformalization focuses on translating informal mathematical conjectures into formal statements in Lean 4, addressing the challenge that autoformalization lacks a natural dense reward and using type-check success alone produces syntactically valid but semantically vacuous outputs."
    ],
    "durationSeconds": 8.150467506,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7eb4e073-e54a-4dd5-9526-5852d75b48a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T06:02:03.722Z_

<details><summary>↩ Tool result · `toolu_01W1oW9ntjwquaUM7ZaQxdZL`</summary>

```text
Web search results for query: "CriticLean CriticLeanGPT semantic critic mathematical formalization 2025"

Links: [{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"},{"title":"Paper page - CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://huggingface.co/papers/2507.06181"},{"title":"m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face","url":"https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"}]

Based on the search results, here's what I found about CriticLean and CriticLeanGPT:

## Overview

CriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. The paper addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code in automated theorem proving.

## Key Components

**CriticLeanGPT**: CriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations.

**CriticLeanBench**: CriticLeanBench is a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations, and trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines.

**FineLeanCorpus**: FineLeanCorpus is a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.

## Significance

While prior work has focused on generation and compilation success, little attention has been paid to the critic phase—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. The findings highlight that optimizing the critic phase is essential for producing reliable formalizations.

The paper was published on July 8-9, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fad8e510-7a8b-4da5-9980-f10fa10fbe43",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "f8e88d33-249f-4ef3-83ff-ff09dbb21b55",
  "toolUseResult": {
    "query": "CriticLean CriticLeanGPT semantic critic mathematical formalization 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N9UKkCfhcJzWmqz9vnNzAU",
        "content": [
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
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
            "title": "(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"
          },
          {
            "title": "Paper page - CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://huggingface.co/papers/2507.06181"
          },
          {
            "title": "m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face",
            "url": "https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"
          }
        ]
      },
      "Based on the search results, here's what I found about CriticLean and CriticLeanGPT:\n\n## Overview\n\nCriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. The paper addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code in automated theorem proving.\n\n## Key Components\n\n**CriticLeanGPT**: CriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations.\n\n**CriticLeanBench**: CriticLeanBench is a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations, and trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines.\n\n**FineLeanCorpus**: FineLeanCorpus is a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.\n\n## Significance\n\nWhile prior work has focused on generation and compilation success, little attention has been paid to the critic phase—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. The findings highlight that optimizing the critic phase is essential for producing reliable formalizations.\n\nThe paper was published on July 8-9, 2025."
    ],
    "durationSeconds": 8.80490228,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fad8e510-7a8b-4da5-9980-f10fa10fbe43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T06:02:07.559Z_

<details><summary>↩ Tool result · `toolu_011tBjzq3W4aS1cFEYrB9W41`</summary>

```text
Web search results for query: "co-adaptive retrieval augmented generation reinforcement learning R3 Reinforced-IR 2025"

Links: [{"title":"Optimizing Retrieval for RAG via Reinforced Contrastive Learning","url":"https://arxiv.org/html/2510.24652v1"},{"title":"Optimizing Retrieval for RAG via Reinforcement Learning Jiawei Zhou Lei Chen","url":"https://openreview.net/pdf/74b57081a9a2db071d310000acfd1692aa247047.pdf"},{"title":"R3AG 2025: Workshop on Refined and Reliable Retrieval-Augmented Generation | Proceedings of the 2025 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region","url":"https://dl.acm.org/doi/10.1145/3767695.3769524"},{"title":"[2510.24652] Optimizing Retrieval for RAG via Reinforcement Learning","url":"https://arxiv.org/abs/2510.24652"},{"title":"Reinforced Information Retrieval","url":"https://arxiv.org/pdf/2502.11562"},{"title":"[2505.23794] R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2505.23794"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval ...","url":"https://aclanthology.org/2025.findings-emnlp.554.pdf"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2505.23794"},{"title":"R3-RAG: Learning Step-by-Step Reasoning and Retrieval for LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2505.23794v2"}]

Based on the search results, I found information about the approaches you asked about. Here's what the research reveals:

## R3: Optimizing Retrieval for RAG via Reinforcement Learning

R3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. Unlike prior approaches that rely on annotated or synthetic data for supervised fine-tuning, R3 enables the retriever to dynamically explore and optimize relevance within the RAG environment. Based on the generation outcomes, the retrieved documents are labeled as positive or negative with respect to the query, and contrastive learning objective is applied to optimize the retriever accordingly.

Extensive experiments across diverse tasks demonstrate that R3 improves RAG performance by 5.2% over the original retriever and surpasses state-of-the-art retrievers by 4.9%, while achieving comparable results to LLM-augmented retrieval and RAG systems built on post-trained or instruction-tuned LLMs. It is both efficient and practical, requiring only 4 GPUs and completing training within a single day.

## Reinforced-IR: Co-Adaptive Learning Framework

A key innovation of Reinforced-IR is its Self-Boosting framework, which enables retriever and generator to learn from each other's feedback. Specifically, the generator is reinforced to generate query augmentations that enhance the retriever's performance, while the retriever is trained to better discriminate the relevant documents identified by the generator. This iterative process allows the end-to-end retrieval performance to be progressively optimized using an unlabeled corpus from the target domain.

Both approaches represent recent advances in using reinforcement learning to improve retrieval-augmented generation systems, with R3 focusing on contrastive learning optimization and Reinforced-IR emphasizing co-adaptive learning between retriever and generator components.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb70e44f-e137-4c2d-a04c-bd809d39ec15",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "fe787fd3-6b33-4306-b56c-37623709723f",
  "toolUseResult": {
    "query": "co-adaptive retrieval augmented generation reinforcement learning R3 Reinforced-IR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KHHzpgXzdfb1bayoUXd9SS",
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
      "Based on the search results, I found information about the approaches you asked about. Here's what the research reveals:\n\n## R3: Optimizing Retrieval for RAG via Reinforcement Learning\n\nR3 is a Retrieval framework optimized for RAG through trial-and-feedback Reinforced contrastive learning. Unlike prior approaches that rely on annotated or synthetic data for supervised fine-tuning, R3 enables the retriever to dynamically explore and optimize relevance within the RAG environment. Based on the generation outcomes, the retrieved documents are labeled as positive or negative with respect to the query, and contrastive learning objective is applied to optimize the retriever accordingly.\n\nExtensive experiments across diverse tasks demonstrate that R3 improves RAG performance by 5.2% over the original retriever and surpasses state-of-the-art retrievers by 4.9%, while achieving comparable results to LLM-augmented retrieval and RAG systems built on post-trained or instruction-tuned LLMs. It is both efficient and practical, requiring only 4 GPUs and completing training within a single day.\n\n## Reinforced-IR: Co-Adaptive Learning Framework\n\nA key innovation of Reinforced-IR is its Self-Boosting framework, which enables retriever and generator to learn from each other's feedback. Specifically, the generator is reinforced to generate query augmentations that enhance the retriever's performance, while the retriever is trained to better discriminate the relevant documents identified by the generator. This iterative process allows the end-to-end retrieval performance to be progressively optimized using an unlabeled corpus from the target domain.\n\nBoth approaches represent recent advances in using reinforcement learning to improve retrieval-augmented generation systems, with R3 focusing on contrastive learning optimization and Reinforced-IR emphasizing co-adaptive learning between retriever and generator components."
    ],
    "durationSeconds": 11.708071266,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eb70e44f-e137-4c2d-a04c-bd809d39ec15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "fe787fd3-6b33-4306-b56c-37623709723f",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal acceptance probability",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Tool result

_source line 24 · 2026-05-28T06:02:09.122Z_

<details><summary>↩ Tool result · `toolu_01LxxSbVHuUPcuvssn41nsAg`</summary>

```text
Web search results for query: "Aria ICLR 2026 autoformalization retrieval dependency graph DDR identifier hallucination"

Links: [{"title":"Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph | OpenReview","url":"https://openreview.net/forum?id=CPxZClPMiy"},{"title":"ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://iclr.cc/virtual/2026/poster/10010860"},{"title":"Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/html/2511.11990"},{"title":"[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520"},{"title":"[2511.11990] Improving Autoformalization Using Direct Dependency Retrieval","url":"https://arxiv.org/abs/2511.11990"},{"title":"[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520v1"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE","url":"https://arxiv.org/pdf/2510.04520"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE ...","url":"https://openreview.net/pdf/388a385b7ad068290351f90757bd3af8bb6e5515.pdf"}]

Based on the search results, here's what I found:

## Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph

Aria is an ICLR 2026 conference submission that addresses key challenges in autoformalization.

**Overview:**
Aria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.

**Problem Addressed:**
Accurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.

**Key Component - AriaScorer:**
To ensure semantic correctness, AriaScorer is a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.

**Performance Results:**
On ProofNet, it achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods.

The search results also mention related work on Direct Dependency Retrieval (DDR), which is another approach to addressing hallucination problems in dependency retrieval for autoformalization tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9600c28e-e961-488e-adfa-c05936883c5b",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "db2ce77b-52a3-4d3f-a4ed-00c10e3b5a0f",
  "toolUseResult": {
    "query": "Aria ICLR 2026 autoformalization retrieval dependency graph DDR identifier hallucination",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LokuoKPjxsMrxD9RDYLZUH",
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
            "title": "Improving Autoformalization Using Direct Dependency Retrieval",
            "url": "https://arxiv.org/html/2511.11990"
          },
          {
            "title": "[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/abs/2510.04520"
          },
          {
            "title": "[2511.11990] Improving Autoformalization Using Direct Dependency Retrieval",
            "url": "https://arxiv.org/abs/2511.11990"
          },
          {
            "title": "[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/abs/2510.04520v1"
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
      "Based on the search results, here's what I found:\n\n## Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph\n\nAria is an ICLR 2026 conference submission that addresses key challenges in autoformalization.\n\n**Overview:**\nAria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.\n\n**Problem Addressed:**\nAccurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.\n\n**Key Component - AriaScorer:**\nTo ensure semantic correctness, AriaScorer is a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.\n\n**Performance Results:**\nOn ProofNet, it achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods.\n\nThe search results also mention related work on Direct Dependency Retrieval (DDR), which is another approach to addressing hallucination problems in dependency retrieval for autoformalization tasks."
    ],
    "durationSeconds": 12.843555353,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9600c28e-e961-488e-adfa-c05936883c5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-28T06:02:11.974Z_

<details><summary>Logged reasoning block</summary>

```text
Good, let me continue with more targeted searches to get a complete picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2ce77b-52a3-4d3f-a4ed-00c10e3b5a0f",
  "isSidechain": false,
  "requestId": "req_011CbUTaWJuo9BdAM5rXQs8W",
  "type": "assistant",
  "uuid": "eeca141f-d6d9-4301-a930-02a7ab59c3be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVY3o2RerhSoVuaPotysQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 24558,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 24558,
          "cache_creation_input_tokens": 4271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4271
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

_source line 26 · 2026-05-28T06:02:12.471Z_

Good, let me do a few more targeted searches to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeca141f-d6d9-4301-a930-02a7ab59c3be",
  "isSidechain": false,
  "requestId": "req_011CbUTaWJuo9BdAM5rXQs8W",
  "type": "assistant",
  "uuid": "1de4dd3a-446b-4d9c-9a72-a15fc5ece9bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVY3o2RerhSoVuaPotysQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 24558,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 24558,
          "cache_creation_input_tokens": 4271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4271
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

_source line 27 · 2026-05-28T06:02:13.396Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vky74SxbcbT7NsmvF1Kyip`</summary>

```json
{
  "query": "FormalEvolve autoformalization evolutionary search test-time compute 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1de4dd3a-446b-4d9c-9a72-a15fc5ece9bb",
  "isSidechain": false,
  "requestId": "req_011CbUTaWJuo9BdAM5rXQs8W",
  "type": "assistant",
  "uuid": "f81acb91-caf6-47c1-b899-2aa5c49ca309",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVY3o2RerhSoVuaPotysQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 24558,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 24558,
          "cache_creation_input_tokens": 4271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4271
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

_source line 28 · 2026-05-28T06:02:14.338Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012KPjoMv2bzhSxYNBEyBTNR`</summary>

```json
{
  "query": "MathAtlas benchmark autoformalization graduate-level 2026 arXiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f81acb91-caf6-47c1-b899-2aa5c49ca309",
  "isSidechain": false,
  "requestId": "req_011CbUTaWJuo9BdAM5rXQs8W",
  "type": "assistant",
  "uuid": "beaf8449-0496-4e67-bc94-c52be4dacccb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVY3o2RerhSoVuaPotysQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 24558,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 24558,
          "cache_creation_input_tokens": 4271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4271
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

_source line 29 · 2026-05-28T06:02:14.872Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ACd2cDJwDaQpjS1nLr5XYL`</summary>

```json
{
  "query": "TTRL test-time reinforcement learning NeurIPS 2025 majority voting unsupervised"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beaf8449-0496-4e67-bc94-c52be4dacccb",
  "isSidechain": false,
  "requestId": "req_011CbUTaWJuo9BdAM5rXQs8W",
  "type": "assistant",
  "uuid": "c4eb1f22-7d79-45f7-985d-83c25420c48d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVY3o2RerhSoVuaPotysQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 24558,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 24558,
          "cache_creation_input_tokens": 4271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4271
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

_source line 30 · 2026-05-28T06:02:15.809Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015B2iJdAVv1qhmNTEmdWqVf`</summary>

```json
{
  "query": "TEMPO test-time training EM scaling reasoning model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4eb1f22-7d79-45f7-985d-83c25420c48d",
  "isSidechain": false,
  "requestId": "req_011CbUTaWJuo9BdAM5rXQs8W",
  "type": "assistant",
  "uuid": "72280d3e-f85a-4414-b141-b263b2333dcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVY3o2RerhSoVuaPotysQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 24558,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 24558,
          "cache_creation_input_tokens": 4271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4271
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

_source line 31 · 2026-05-28T06:02:16.274Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0156nZLy45Q6rjRt8pN3WENP`</summary>

```json
{
  "query": "FormaRL COLM 2025 autoformalization GRPO compilation reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72280d3e-f85a-4414-b141-b263b2333dcc",
  "isSidechain": false,
  "requestId": "req_011CbUTaWJuo9BdAM5rXQs8W",
  "type": "assistant",
  "uuid": "75ca13d1-3bc8-4fe2-a23d-590f4c098d34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVY3o2RerhSoVuaPotysQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4271,
      "cache_read_input_tokens": 24558,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 24558,
          "cache_creation_input_tokens": 4271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4271
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

_source line 32 · 2026-05-28T06:02:20.230Z_

<details><summary>↩ Tool result · `toolu_01Vky74SxbcbT7NsmvF1Kyip`</summary>

```text
Web search results for query: "FormalEvolve autoformalization evolutionary search test-time compute 2026"

Links: [{"title":"[2603.19828] FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/abs/2603.19828"},{"title":"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization","url":"https://arxiv.org/pdf/2603.19828"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/992cdc768b2a7bfdcbb61ec9da95d61c24fa0827.pdf"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"}]

Based on the search results, here's what I found about FormalEvolve:

FormalEvolve formulates autoformalization as a budgeted, test-time search for semantically consistent repertoires, and proposes a compilation-gated neuro-symbolic evolutionary framework. Autoformalization aims to translate natural-language mathematics into compilable, machine-checkable statements.

Semantic consistency does not imply prover effectiveness: even semantically consistent formalizations can differ substantially in proof-search cost and success rate. To address this, FormalEvolve generates diverse candidates via LLM-driven mutation and crossover with bounded patch repair, while symbolic Abstract Syntax Tree (AST) rewrite operations further inject structural diversity.

In terms of performance, on CombiBench and ProofNet, under a strict generator-call budget of T = 100, FormalEvolve reaches semantic hit rates (SH@100) of 58.0% and 84.9%, and reduces cross-problem concentration of semantic successes.

The paper was submitted to arXiv on March 20, 2026, and appears to be a recent development in the field of automated theorem proving and formalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f81acb91-caf6-47c1-b899-2aa5c49ca309",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "aee506aa-cd9b-47ad-bb1d-4467f6475c37",
  "toolUseResult": {
    "query": "FormalEvolve autoformalization evolutionary search test-time compute 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GcuwEP8JtHT6cSFfWrMR1U",
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
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/992cdc768b2a7bfdcbb61ec9da95d61c24fa0827.pdf"
          },
          {
            "title": "Formalization and autoformalization 2026-2027",
            "url": "https://web.math.utk.edu/~yqing/lean.html"
          },
          {
            "title": "3rd AI for Math Workshop @ ICML 2026",
            "url": "https://ai4math2026.github.io/"
          }
        ]
      },
      "Based on the search results, here's what I found about FormalEvolve:\n\nFormalEvolve formulates autoformalization as a budgeted, test-time search for semantically consistent repertoires, and proposes a compilation-gated neuro-symbolic evolutionary framework. Autoformalization aims to translate natural-language mathematics into compilable, machine-checkable statements.\n\nSemantic consistency does not imply prover effectiveness: even semantically consistent formalizations can differ substantially in proof-search cost and success rate. To address this, FormalEvolve generates diverse candidates via LLM-driven mutation and crossover with bounded patch repair, while symbolic Abstract Syntax Tree (AST) rewrite operations further inject structural diversity.\n\nIn terms of performance, on CombiBench and ProofNet, under a strict generator-call budget of T = 100, FormalEvolve reaches semantic hit rates (SH@100) of 58.0% and 84.9%, and reduces cross-problem concentration of semantic successes.\n\nThe paper was submitted to arXiv on March 20, 2026, and appears to be a recent development in the field of automated theorem proving and formalization."
    ],
    "durationSeconds": 6.8295161400000035,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f81acb91-caf6-47c1-b899-2aa5c49ca309",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T06:02:20.873Z_

<details><summary>↩ Tool result · `toolu_012KPjoMv2bzhSxYNBEyBTNR`</summary>

```text
Web search results for query: "MathAtlas benchmark autoformalization graduate-level 2026 arXiv 2605"

Links: [{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics","url":"https://arxiv.org/html/2602.24173v1"},{"title":"ProofNet: Autoformalizing and Formally Proving Undergraduate-Level   Mathematics","url":"https://arxiv.org/pdf/2302.12433"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/pdf/2512.00997"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"}]

Perfect! I found the paper you were looking for. Here's what I found:

MathAtlas is the first large-scale autoformalization benchmark of in the wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

Strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others.

The paper (arXiv:2605.14061) was submitted on May 13, 2026, and addresses a gap in the field by focusing on graduate and research-level mathematics, which prior autoformalization benchmarks had largely overlooked in favor of olympiad or undergraduate mathematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "beaf8449-0496-4e67-bc94-c52be4dacccb",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "568981cb-b445-44e6-b6ab-d6c94f1ac73f",
  "toolUseResult": {
    "query": "MathAtlas benchmark autoformalization graduate-level 2026 arXiv 2605",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S6zn8iv82WUKcYy5yonJUL",
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
            "title": "A New Approach Towards Autoformalization",
            "url": "https://arxiv.org/pdf/2310.07957"
          },
          {
            "title": "LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics",
            "url": "https://arxiv.org/html/2602.24173v1"
          },
          {
            "title": "ProofNet: Autoformalizing and Formally Proving Undergraduate-Level   Mathematics",
            "url": "https://arxiv.org/pdf/2302.12433"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/pdf/2512.00997"
          },
          {
            "title": "Reliable Evaluation and Benchmarks for Statement Autoformalization",
            "url": "https://arxiv.org/pdf/2406.07222"
          }
        ]
      },
      "Perfect! I found the paper you were looking for. Here's what I found:\n\nMathAtlas is the first large-scale autoformalization benchmark of in the wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.\n\nMathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.\n\nStrong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others.\n\nThe paper (arXiv:2605.14061) was submitted on May 13, 2026, and addresses a gap in the field by focusing on graduate and research-level mathematics, which prior autoformalization benchmarks had largely overlooked in favor of olympiad or undergraduate mathematics."
    ],
    "durationSeconds": 6.531367418000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "beaf8449-0496-4e67-bc94-c52be4dacccb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T06:02:22.834Z_

<details><summary>↩ Tool result · `toolu_01ACd2cDJwDaQpjS1nLr5XYL`</summary>

```text
Web search results for query: "TTRL test-time reinforcement learning NeurIPS 2025 majority voting unsupervised"

Links: [{"title":"TTRL: Test-Time Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=VuVhgEiu20"},{"title":"GitHub - PRIME-RL/TTRL: [NeurIPS 2025] TTRL: Test-Time Reinforcement Learning · GitHub","url":"https://github.com/prime-rl/ttrl"},{"title":"TTRL: Test-Time Reinforcement Learning | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/ttrl-test-time-reinforcement-learning-d78a74e78a28"},{"title":"arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084"},{"title":"arXiv:2504.16084v1 [cs.CL] 22 Apr 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084v1"},{"title":"TTRL: Test-Time Reinforcement Learning","url":"https://www.emergentmind.com/papers/2504.16084"},{"title":"NeurIPS Poster TTRL: Test-Time Reinforcement Learning","url":"https://neurips.cc/virtual/2025/poster/117645"},{"title":"(PDF) TTRL: Test-Time Reinforcement Learning","url":"https://www.researchgate.net/publication/391020470_TTRL_Test-Time_Reinforcement_Learning"},{"title":"Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2512.15146"}]

Based on the search results, here's information about TTRL and its key aspects:

## Overview

TTRL (Test-Time Reinforcement Learning) is a NeurIPS 2025 paper that investigates Reinforcement Learning on data without explicit labels for reasoning tasks in Large Language Models. It is a novel method for training LLMs using RL on unlabeled data.

## Core Mechanism

The method finds that common practices in Test-Time Scaling (TTS), such as majority voting, yield surprisingly effective rewards suitable for driving RL training. TTRL uses majority voting among multiple model predictions to create pseudo-labels, which then serve as reward signals for reinforcement learning during test time.

## Approach

The paper investigates RL on data without explicit labels for reasoning tasks in LLMs, with the core challenge being reward estimation during inference while not having access to ground-truth information.

## Performance Results

TTRL boosts the pass@1 performance of Qwen-2.5-Math-7B by approximately 211% on the AIME 2024 with only unlabeled test data. Additionally, TTRL can surpass the performance achieved by simply using majority voting on the initial model outputs (Maj@N), suggesting the model learns to generate better solutions than its initial capability to form a consensus.

## Code and Implementation

The TTRL paper was accepted to NeurIPS 2025, and code and experimental logs were released.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4eb1f22-7d79-45f7-985d-83c25420c48d",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "909de8cb-c106-4730-b81d-77c8d66ab2f4",
  "toolUseResult": {
    "query": "TTRL test-time reinforcement learning NeurIPS 2025 majority voting unsupervised",
    "results": [
      {
        "tool_use_id": "srvtoolu_011bGQa68PdVRJUowPNXKH69",
        "content": [
          {
            "title": "TTRL: Test-Time Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=VuVhgEiu20"
          },
          {
            "title": "GitHub - PRIME-RL/TTRL: [NeurIPS 2025] TTRL: Test-Time Reinforcement Learning · GitHub",
            "url": "https://github.com/prime-rl/ttrl"
          },
          {
            "title": "TTRL: Test-Time Reinforcement Learning | by Eleventh Hour Enthusiast | Medium",
            "url": "https://medium.com/@EleventhHourEnthusiast/ttrl-test-time-reinforcement-learning-d78a74e78a28"
          },
          {
            "title": "arXiv:2504.16084v3 [cs.CL] 30 Jun 2025 TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2504.16084"
          },
          {
            "title": "arXiv:2504.16084v1 [cs.CL] 22 Apr 2025 TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2504.16084v1"
          },
          {
            "title": "TTRL: Test-Time Reinforcement Learning",
            "url": "https://www.emergentmind.com/papers/2504.16084"
          },
          {
            "title": "NeurIPS Poster TTRL: Test-Time Reinforcement Learning",
            "url": "https://neurips.cc/virtual/2025/poster/117645"
          },
          {
            "title": "(PDF) TTRL: Test-Time Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/391020470_TTRL_Test-Time_Reinforcement_Learning"
          },
          {
            "title": "Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2512.15146"
          }
        ]
      },
      "Based on the search results, here's information about TTRL and its key aspects:\n\n## Overview\n\nTTRL (Test-Time Reinforcement Learning) is a NeurIPS 2025 paper that investigates Reinforcement Learning on data without explicit labels for reasoning tasks in Large Language Models. It is a novel method for training LLMs using RL on unlabeled data.\n\n## Core Mechanism\n\nThe method finds that common practices in Test-Time Scaling (TTS), such as majority voting, yield surprisingly effective rewards suitable for driving RL training. TTRL uses majority voting among multiple model predictions to create pseudo-labels, which then serve as reward signals for reinforcement learning during test time.\n\n## Approach\n\nThe paper investigates RL on data without explicit labels for reasoning tasks in LLMs, with the core challenge being reward estimation during inference while not having access to ground-truth information.\n\n## Performance Results\n\nTTRL boosts the pass@1 performance of Qwen-2.5-Math-7B by approximately 211% on the AIME 2024 with only unlabeled test data. Additionally, TTRL can surpass the performance achieved by simply using majority voting on the initial model outputs (Maj@N), suggesting the model learns to generate better solutions than its initial capability to form a consensus.\n\n## Code and Implementation\n\nThe TTRL paper was accepted to NeurIPS 2025, and code and experimental logs were released."
    ],
    "durationSeconds": 7.958607473999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c4eb1f22-7d79-45f7-985d-83c25420c48d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T06:02:23.266Z_

<details><summary>↩ Tool result · `toolu_0156nZLy45Q6rjRt8pN3WENP`</summary>

```text
Web search results for query: "FormaRL COLM 2025 autoformalization GRPO compilation reward"

Links: [{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data | OpenReview","url":"https://openreview.net/forum?id=Z2El1U94bq"},{"title":"[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/abs/2508.18914"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://openreview.net/pdf?id=Z2El1U94bq"},{"title":"Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs","url":"https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"},{"title":"[PDF] FormaRL: Enhancing Autoformalization with no Labeled Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FormaRL:-Enhancing-Autoformalization-with-no-Data-Huang-Jin/b430d8ac9cf1236314a1273dc7e8fb9769ebae70"},{"title":"Published as a conference paper at COLM 2025","url":"https://par.nsf.gov/servlets/purl/10635650"},{"title":"FormaRL: RL-Driven Autoformalization for Lean 4","url":"https://www.emergentmind.com/topics/formarl"},{"title":"FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/pdf/2508.18914"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"}]

Based on the search results, here's what I found about FormaRL:

## FormaRL Overview

FormaRL is a simple yet efficient reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. It was published as a conference paper at COLM 2025.

## Technical Approach

FormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer. More specifically, only when both syntax check and consistency check evaluate positively is a reward signal of 1 assigned; otherwise, the reward is 0.

## Performance Results

FormaRL can increase the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4-6x (4.04% → 26.15% on ProofNet and 2.4% → 9.6% on uproof) with merely 859 unlabeled data.

## Dataset Contribution

The researchers also curated a proof problem dataset from undergraduate-level math materials, named uproof, in the hope to facilitate the exploration of autoformalization and theorem proving in advanced math.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75ca13d1-3bc8-4fe2-a23d-590f4c098d34",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "d811cc4b-6509-45ec-ad65-304241e8013d",
  "toolUseResult": {
    "query": "FormaRL COLM 2025 autoformalization GRPO compilation reward",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PvCJk4444B7mk6eT4H5PR4",
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
      "Based on the search results, here's what I found about FormaRL:\n\n## FormaRL Overview\n\nFormaRL is a simple yet efficient reinforcement learning framework for autoformalization which only requires a small amount of unlabeled data. It was published as a conference paper at COLM 2025.\n\n## Technical Approach\n\nFormaRL integrates syntax check from Lean compiler and consistency check from large language model to calculate the reward, and adopts GRPO algorithm to update the formalizer. More specifically, only when both syntax check and consistency check evaluate positively is a reward signal of 1 assigned; otherwise, the reward is 0.\n\n## Performance Results\n\nFormaRL can increase the pass@1 autoformalization accuracy of Qwen2.5-Coder-7B-Instruct by 4-6x (4.04% → 26.15% on ProofNet and 2.4% → 9.6% on uproof) with merely 859 unlabeled data.\n\n## Dataset Contribution\n\nThe researchers also curated a proof problem dataset from undergraduate-level math materials, named uproof, in the hope to facilitate the exploration of autoformalization and theorem proving in advanced math."
    ],
    "durationSeconds": 6.989105174999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "75ca13d1-3bc8-4fe2-a23d-590f4c098d34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "d811cc4b-6509-45ec-ad65-304241e8013d",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal acceptance probability",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Tool result

_source line 38 · 2026-05-28T06:02:24.348Z_

<details><summary>↩ Tool result · `toolu_015B2iJdAVv1qhmNTEmdWqVf`</summary>

```text
Web search results for query: "TEMPO test-time training EM scaling reasoning model 2026"

Links: [{"title":"April 22, 2026 TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/pdf/2604.19295"},{"title":"Paper page - TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://huggingface.co/papers/2604.19295"},{"title":"[2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/abs/2604.19295"},{"title":"TEMPO: Scaling Test-time Training for Large Reasoning Models","url":"https://arxiv.org/html/2604.19295v1"},{"title":"GitHub - QingyangZhang/TEMPO: Scaling Test-time Training for LLM Reasoning · GitHub","url":"https://github.com/QingyangZhang/TEMPO"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"(PDF) Test-Time Compute Scaling and Reasoning Models: Foundations, Benchmarks, and Implications","url":"https://www.academia.edu/165704995/Test_Time_Compute_Scaling_and_Reasoning_Models_Foundations_Benchmarks_and_Implications"}]

Based on the search results, here's what I found about TEMPO:

## TEMPO: Scaling Test-time Training for Large Reasoning Models

TEMPO is a test-time training (TTT) framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on a labeled dataset.

**Key Innovation:** By formalizing this alternating procedure through the Expectation-Maximization (EM) algorithm, the research reveals that prior methods can be interpreted as incomplete variants that omit the crucial recalibration step. The EM framework includes an E-step where a value critic is updated on a small labeled dataset to estimate solution quality, and an M-step where the policy is updated on a larger unlabeled dataset using critic-assigned advantages.

**Performance Results:** Across diverse model families (Qwen3 and OLMO3) and reasoning tasks, TEMPO improves OLMO3-7B on AIME 2024 from 33.0% to 51.1% and Qwen3-14B from 42.3% to 65.8%, while maintaining high diversity.

**Problem Addressed:** Existing TTT methods for large reasoning models plateau quickly and do not benefit from additional test-time compute, as the self-generated reward signal increasingly drifts as the policy model evolves, leading to both performance plateaus and diversity collapse.

The paper was published in April 2026 and includes code released on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72280d3e-f85a-4414-b141-b263b2333dcc",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "65198857-0558-4cf1-bd62-23df091c9158",
  "toolUseResult": {
    "query": "TEMPO test-time training EM scaling reasoning model 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014JxSVKLFw73UdURmxifki6",
        "content": [
          {
            "title": "April 22, 2026 TEMPO: Scaling Test-time Training for Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2604.19295"
          },
          {
            "title": "Paper page - TEMPO: Scaling Test-time Training for Large Reasoning Models",
            "url": "https://huggingface.co/papers/2604.19295"
          },
          {
            "title": "[2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models",
            "url": "https://arxiv.org/abs/2604.19295"
          },
          {
            "title": "TEMPO: Scaling Test-time Training for Large Reasoning Models",
            "url": "https://arxiv.org/html/2604.19295v1"
          },
          {
            "title": "GitHub - QingyangZhang/TEMPO: Scaling Test-time Training for LLM Reasoning · GitHub",
            "url": "https://github.com/QingyangZhang/TEMPO"
          },
          {
            "title": "GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"
          },
          {
            "title": "(PDF) Test-Time Compute Scaling and Reasoning Models: Foundations, Benchmarks, and Implications",
            "url": "https://www.academia.edu/165704995/Test_Time_Compute_Scaling_and_Reasoning_Models_Foundations_Benchmarks_and_Implications"
          }
        ]
      },
      "Based on the search results, here's what I found about TEMPO:\n\n## TEMPO: Scaling Test-time Training for Large Reasoning Models\n\nTEMPO is a test-time training (TTT) framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on a labeled dataset.\n\n**Key Innovation:** By formalizing this alternating procedure through the Expectation-Maximization (EM) algorithm, the research reveals that prior methods can be interpreted as incomplete variants that omit the crucial recalibration step. The EM framework includes an E-step where a value critic is updated on a small labeled dataset to estimate solution quality, and an M-step where the policy is updated on a larger unlabeled dataset using critic-assigned advantages.\n\n**Performance Results:** Across diverse model families (Qwen3 and OLMO3) and reasoning tasks, TEMPO improves OLMO3-7B on AIME 2024 from 33.0% to 51.1% and Qwen3-14B from 42.3% to 65.8%, while maintaining high diversity.\n\n**Problem Addressed:** Existing TTT methods for large reasoning models plateau quickly and do not benefit from additional test-time compute, as the self-generated reward signal increasingly drifts as the policy model evolves, leading to both performance plateaus and diversity collapse.\n\nThe paper was published in April 2026 and includes code released on GitHub."
    ],
    "durationSeconds": 8.536876025999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "72280d3e-f85a-4414-b141-b263b2333dcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39 · 2026-05-28T06:02:24.353Z_

```json
{
  "parentUuid": "65198857-0558-4cf1-bd62-23df091c9158",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3a1b0a70-9111-44c4-a121-835a0b71c967",
  "timestamp": "2026-05-28T06:02:24.353Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 40 · 2026-05-28T06:02:27.644Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do a couple more searches to check for any very close existing work that combines these elements, and to verify some of the more specific claims in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a1b0a70-9111-44c4-a121-835a0b71c967",
  "isSidechain": false,
  "requestId": "req_011CbUTbdQaKkTHA2AwCjH3e",
  "type": "assistant",
  "uuid": "460c180c-fd84-4db9-b47c-d28f25177782",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2DvKCrGsFGmSksDSUcu9D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 812,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 28829,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 812,
          "output_tokens": 250,
          "cache_read_input_tokens": 28829,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 41 · 2026-05-28T06:02:28.490Z_

Let me do a couple more targeted searches to check for directly competing work and verify key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "460c180c-fd84-4db9-b47c-d28f25177782",
  "isSidechain": false,
  "requestId": "req_011CbUTbdQaKkTHA2AwCjH3e",
  "type": "assistant",
  "uuid": "296c37de-7196-4c1e-8abd-e70b66d76266",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2DvKCrGsFGmSksDSUcu9D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 812,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 28829,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 812,
          "output_tokens": 250,
          "cache_read_input_tokens": 28829,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 42 · 2026-05-28T06:02:29.201Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011RuTVFnXP7b66LtX2X7yua`</summary>

```json
{
  "query": "T3RL tool verification test-time reinforcement learning 2026 arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "296c37de-7196-4c1e-8abd-e70b66d76266",
  "isSidechain": false,
  "requestId": "req_011CbUTbdQaKkTHA2AwCjH3e",
  "type": "assistant",
  "uuid": "61105ca9-21b1-47b7-af34-9a2f0ecd6977",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2DvKCrGsFGmSksDSUcu9D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 812,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 28829,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 812,
          "output_tokens": 250,
          "cache_read_input_tokens": 28829,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 43 · 2026-05-28T06:02:30.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TYUB7rfhRCYt67AHLxY6vR`</summary>

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
  "parentUuid": "61105ca9-21b1-47b7-af34-9a2f0ecd6977",
  "isSidechain": false,
  "requestId": "req_011CbUTbdQaKkTHA2AwCjH3e",
  "type": "assistant",
  "uuid": "6b37d95d-1fc4-4110-9ef4-4ba2e8ce213f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2DvKCrGsFGmSksDSUcu9D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 812,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 28829,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 812,
          "output_tokens": 250,
          "cache_read_input_tokens": 28829,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 44 · 2026-05-28T06:02:30.731Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X5RwMchMJ1t8D5VAtJZV9S`</summary>

```json
{
  "query": "TTARAG test-time adaptation retrieval augmented generation self-supervised 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b37d95d-1fc4-4110-9ef4-4ba2e8ce213f",
  "isSidechain": false,
  "requestId": "req_011CbUTbdQaKkTHA2AwCjH3e",
  "type": "assistant",
  "uuid": "0593e82a-55f6-44ef-a92a-29e2063caa0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2DvKCrGsFGmSksDSUcu9D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 812,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 28829,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 812,
          "output_tokens": 250,
          "cache_read_input_tokens": 28829,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 45 · 2026-05-28T06:02:36.698Z_

<details><summary>↩ Tool result · `toolu_01X5RwMchMJ1t8D5VAtJZV9S`</summary>

```text
Web search results for query: "TTARAG test-time adaptation retrieval augmented generation self-supervised 2026"

Links: [{"title":"[2601.11443] Predict the Retrieval! Test time adaptation for Retrieval Augmented Generation","url":"https://arxiv.org/abs/2601.11443"},{"title":"Predict the Retrieval! Test Time Adaptation for Retrieval Augmented Generation","url":"https://arxiv.org/html/2601.11443"},{"title":"Predict the Retrieval! Test time adaptation for Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2601.11443"},{"title":"Predict the Retrieval! Test time adaptation for Retrieval Augmented Generation | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2601.11443"},{"title":"Predict the Retrieval! Test Time Adaptation for Retrieval Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=mhMK1QOmU4"},{"title":"Retrieval-Augmented Generation with Covariate Time Series","url":"https://arxiv.org/html/2603.04951"},{"title":"TAdaRAG: Task Adaptive Retrieval-Augmented Generation via On-the-Fly","url":"https://arxiv.org/pdf/2511.12520"}]

Based on the search results, here's what I found about TTARAG:

## TTARAG Overview

TTARAG is a test-time adaptation method that dynamically updates the language model's parameters during inference to improve RAG system performance in specialized domains.

## Key Features

The method uses a simple yet effective approach where the model learns to predict retrieved content, enabling automatic parameter adjustment to the target domain. 

The approach introduces a test-time adaptation mechanism for retrieval-augmented generation that enables model optimization during inference without access to ground truth labels, with the key innovation lying in designing a self-supervised learning objective using retrieved passages as supervision.

## Problem It Addresses

When adapting RAG systems to specialized domains, challenges arise from distribution shifts, resulting in suboptimal generalization performance.

## Results

Through extensive experiments across six specialized domains, TTARAG achieves substantial performance improvements over baseline RAG systems.

The research was published on arXiv on January 16, 2026, with code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0593e82a-55f6-44ef-a92a-29e2063caa0a",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "5cca86c5-d7d4-467d-8a01-22d2511355ea",
  "toolUseResult": {
    "query": "TTARAG test-time adaptation retrieval augmented generation self-supervised 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XDCugYUnvm1pPhzaJA9x8c",
        "content": [
          {
            "title": "[2601.11443] Predict the Retrieval! Test time adaptation for Retrieval Augmented Generation",
            "url": "https://arxiv.org/abs/2601.11443"
          },
          {
            "title": "Predict the Retrieval! Test Time Adaptation for Retrieval Augmented Generation",
            "url": "https://arxiv.org/html/2601.11443"
          },
          {
            "title": "Predict the Retrieval! Test time adaptation for Retrieval Augmented Generation",
            "url": "https://arxiv.org/pdf/2601.11443"
          },
          {
            "title": "Predict the Retrieval! Test time adaptation for Retrieval Augmented Generation | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2601.11443"
          },
          {
            "title": "Predict the Retrieval! Test Time Adaptation for Retrieval Augmented Generation | OpenReview",
            "url": "https://openreview.net/forum?id=mhMK1QOmU4"
          },
          {
            "title": "Retrieval-Augmented Generation with Covariate Time Series",
            "url": "https://arxiv.org/html/2603.04951"
          },
          {
            "title": "TAdaRAG: Task Adaptive Retrieval-Augmented Generation via On-the-Fly",
            "url": "https://arxiv.org/pdf/2511.12520"
          }
        ]
      },
      "Based on the search results, here's what I found about TTARAG:\n\n## TTARAG Overview\n\nTTARAG is a test-time adaptation method that dynamically updates the language model's parameters during inference to improve RAG system performance in specialized domains.\n\n## Key Features\n\nThe method uses a simple yet effective approach where the model learns to predict retrieved content, enabling automatic parameter adjustment to the target domain. \n\nThe approach introduces a test-time adaptation mechanism for retrieval-augmented generation that enables model optimization during inference without access to ground truth labels, with the key innovation lying in designing a self-supervised learning objective using retrieved passages as supervision.\n\n## Problem It Addresses\n\nWhen adapting RAG systems to specialized domains, challenges arise from distribution shifts, resulting in suboptimal generalization performance.\n\n## Results\n\nThrough extensive experiments across six specialized domains, TTARAG achieves substantial performance improvements over baseline RAG systems.\n\nThe research was published on arXiv on January 16, 2026, with code available on GitHub."
    ],
    "durationSeconds": 5.963311105000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0593e82a-55f6-44ef-a92a-29e2063caa0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T06:02:37.662Z_

<details><summary>↩ Tool result · `toolu_011RuTVFnXP7b66LtX2X7yua`</summary>

```text
Web search results for query: "T3RL tool verification test-time reinforcement learning 2026 arXiv 2603"

Links: [{"title":"[2603.02203] Tool Verification for Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2603.02203"},{"title":"Tool Verification for Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2603.02203"},{"title":"Tool Verification for Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2603.02203v1"},{"title":"Paper page - Tool Verification for Test-Time Reinforcement Learning","url":"https://huggingface.co/papers/2603.02203"},{"title":"Meta-TTRL: A Metacognitive Framework for Self-Improving Test-Time Reinforcement Learning in Unified Multimodal Models","url":"https://arxiv.org/html/2603.15724"}]

Based on the search results, I found the paper you're looking for:

T³RL (Tool-Verification for Test-Time Reinforcement Learning) introduces test-time tool verification into reward estimation. Test-time reinforcement learning (TTRL) has emerged as a promising paradigm for self-evolving large reasoning models, enabling online adaptation via self-induced rewards through majority voting, but a spurious yet high-frequency unverified consensus can become a biased reward signal leading to incorrect mode collapse.

A verifier uses an external tool as evidence (e.g., from code execution) to upweight verified rollouts in a verification-aware voting, producing more reliable pseudo-labels for training. Across various math difficulties (MATH-500, AMC, and AIME 2024) and diverse backbone types, T³RL significantly improves over TTRL, with larger gains on harder problems.

The paper was submitted to arXiv on March 2, 2026, with the identifier 2603.02203.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61105ca9-21b1-47b7-af34-9a2f0ecd6977",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "8192906b-d4b7-45f9-9ded-0b99144d2c72",
  "toolUseResult": {
    "query": "T3RL tool verification test-time reinforcement learning 2026 arXiv 2603",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Jom4XC2FTS8ChzH95Uaock",
        "content": [
          {
            "title": "[2603.02203] Tool Verification for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/abs/2603.02203"
          },
          {
            "title": "Tool Verification for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2603.02203"
          },
          {
            "title": "Tool Verification for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.02203v1"
          },
          {
            "title": "Paper page - Tool Verification for Test-Time Reinforcement Learning",
            "url": "https://huggingface.co/papers/2603.02203"
          },
          {
            "title": "Meta-TTRL: A Metacognitive Framework for Self-Improving Test-Time Reinforcement Learning in Unified Multimodal Models",
            "url": "https://arxiv.org/html/2603.15724"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nT³RL (Tool-Verification for Test-Time Reinforcement Learning) introduces test-time tool verification into reward estimation. Test-time reinforcement learning (TTRL) has emerged as a promising paradigm for self-evolving large reasoning models, enabling online adaptation via self-induced rewards through majority voting, but a spurious yet high-frequency unverified consensus can become a biased reward signal leading to incorrect mode collapse.\n\nA verifier uses an external tool as evidence (e.g., from code execution) to upweight verified rollouts in a verification-aware voting, producing more reliable pseudo-labels for training. Across various math difficulties (MATH-500, AMC, and AIME 2024) and diverse backbone types, T³RL significantly improves over TTRL, with larger gains on harder problems.\n\nThe paper was submitted to arXiv on March 2, 2026, with the identifier 2603.02203."
    ],
    "durationSeconds": 8.456784612000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "61105ca9-21b1-47b7-af34-9a2f0ecd6977",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T06:02:41.234Z_

<details><summary>↩ Tool result · `toolu_01TYUB7rfhRCYt67AHLxY6vR`</summary>

```text
Web search results for query: "GDPO group reward decoupled normalization multi-reward GRPO NVIDIA 2026"

Links: [{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiviq.substack.com/p/gdpo-group-reward-decoupled-normalization"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://nvlabs.github.io/GDPO/"},{"title":"2026-1-9 GDPO: Group reward-Decoupled Normalization","url":"https://arxiv.org/pdf/2601.05242"},{"title":"[2601.05242] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/abs/2601.05242"},{"title":"Paper page - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://huggingface.co/papers/2601.05242"},{"title":"Mark Gatere on X: \"GRPO to now GDPO @nvidia just released a new paper - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization GRPO is great, but in multi-reward settings (like mixing accuracy + format constraints), it causes signal collapse where https://t.co/SC9SYpxGuZ\" / X","url":"https://x.com/gatere_mark/status/2009921519393063213"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/html/2601.05242v1"}]

Based on the search results, here's what I found about GDPO:

## Overview

GDPO (Group Reward–Decoupled Normalization Policy Optimization) is a drop-in replacement for GRPO that consistently improves per-reward convergence in multi-reward RL training across tasks.

## The Problem It Solves

Researchers from NVIDIA identified a critical failure mode in Group Relative Policy Optimization (GRPO) when applied to multi-objective reinforcement learning. When directly applying GRPO to normalize distinct rollout reward combinations, they collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure.

## The Solution

GDPO normalizes each reward signal (e.g., correctness, format, brevity) independently within the group before aggregation. By separating the normalization of each reward, GDPO alleviates the training signal collapse problem present in GRPO's advantage estimation.

## Performance Results

Training Qwen2.5-1.5B-Instruct with GDPO attains both higher correctness and format compliance than GRPO on the tool-calling task. Training DeepSeek-R1-1.5B and Qwen3-4B-Instruct with GDPO yields up to 6.3% and 2.3% higher accuracy on AIME compared to GRPO.

The paper and code are available on arXiv (2601.05242), with official resources at the NVIDIA Labs website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b37d95d-1fc4-4110-9ef4-4ba2e8ce213f",
  "isSidechain": false,
  "promptId": "b4f519bb-1575-4563-8896-5eaa2a754ca1",
  "type": "user",
  "uuid": "38835fe8-d5d8-4af9-a80b-fff998089929",
  "toolUseResult": {
    "query": "GDPO group reward decoupled normalization multi-reward GRPO NVIDIA 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0178HTa1a8fHwk5XTg4S1xn8",
        "content": [
          {
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://arxiviq.substack.com/p/gdpo-group-reward-decoupled-normalization"
          },
          {
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://nvlabs.github.io/GDPO/"
          },
          {
            "title": "2026-1-9 GDPO: Group reward-Decoupled Normalization",
            "url": "https://arxiv.org/pdf/2601.05242"
          },
          {
            "title": "[2601.05242] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://arxiv.org/abs/2601.05242"
          },
          {
            "title": "Paper page - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://huggingface.co/papers/2601.05242"
          },
          {
            "title": "Mark Gatere on X: \"GRPO to now GDPO @nvidia just released a new paper - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization GRPO is great, but in multi-reward settings (like mixing accuracy + format constraints), it causes signal collapse where https://t.co/SC9SYpxGuZ\" / X",
            "url": "https://x.com/gatere_mark/status/2009921519393063213"
          },
          {
            "title": "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization",
            "url": "https://arxiv.org/html/2601.05242v1"
          }
        ]
      },
      "Based on the search results, here's what I found about GDPO:\n\n## Overview\n\nGDPO (Group Reward–Decoupled Normalization Policy Optimization) is a drop-in replacement for GRPO that consistently improves per-reward convergence in multi-reward RL training across tasks.\n\n## The Problem It Solves\n\nResearchers from NVIDIA identified a critical failure mode in Group Relative Policy Optimization (GRPO) when applied to multi-objective reinforcement learning. When directly applying GRPO to normalize distinct rollout reward combinations, they collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure.\n\n## The Solution\n\nGDPO normalizes each reward signal (e.g., correctness, format, brevity) independently within the group before aggregation. By separating the normalization of each reward, GDPO alleviates the training signal collapse problem present in GRPO's advantage estimation.\n\n## Performance Results\n\nTraining Qwen2.5-1.5B-Instruct with GDPO attains both higher correctness and format compliance than GRPO on the tool-calling task. Training DeepSeek-R1-1.5B and Qwen3-4B-Instruct with GDPO yields up to 6.3% and 2.3% higher accuracy on AIME compared to GRPO.\n\nThe paper and code are available on arXiv (2601.05242), with official resources at the NVIDIA Labs website."
    ],
    "durationSeconds": 11.027983786999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6b37d95d-1fc4-4110-9ef4-4ba2e8ce213f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-28T06:03:38.577Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a solid understanding of the field. Let me synthesize my analysis.

Let me think carefully about this proposal:

## Key Claims of TTRA:
1. Co-adaptive retrieval during TTRL for autoformalization, exploiting Lean 4's structured error signals
2. Binarize-then-enrich adaptation of DDRL to multi-tier rewards
3. CriticLean integration with distributional shift calibration
4. Test-time adaptation on unlabeled OOD domains

## Trivial Alternative Check:
The most obvious trivial alternative would be: Best-of-N sampling with CriticLean filtering + static retrieval. 

The proposal explicitly includes this as a compute-matched baseline. Another simpler approach would be static retrieval like Aria with more Lean compilation attempts, but the authors argue this fails on truly OOD domains—like the 2.6% hardest examples in MathAtlas—where no amount of sampling from a fixed model can recover correct formalizations. That's a reasonable claim, though it needs empirical support. A more meaningful alternative to consider: could standard supervised fine-tuning on OOD compilation errors work instead of the full TTRL plus co-adaptive retrieval machinery?

## Premise Assumption Check:
1. **"Lean 4's structured errors provide oracle

-quality retrieval training signals"** - This checks out. When compilation fails with `unknownIdentifier "Finset.sum_bij"`, you get direct signal about what's missing. The AMBER benchmark showing 47.3% identifier hallucination in DeepSeek-R1 supports this.

2. **"Identifier hallucination is the dominant error mode for OOD domains"** - The 47.3% figure is specific to DeepSeek-R1 on applied math, and their Phase -1 analysis should validate whether this holds for their model and domain. But the ≥40% threshold might not generalize—for truly novel math areas, errors could stem more from conceptual gaps than just identifier confusion.

3. **"CriticLean-14B will maintain high precision under distributional shift (<10% compilation error rate)"** - Now examining whether this precision claim is realistic...

4. **"Weight adaptation is necessary for truly OOD domains"** - The logic here is sound: if the model's output space genuinely lacks correct formalizations, inference-time scaling won't help. Though there's a bit of circularity—you can't know the output space is insufficient without testing it first.

The novelty really comes down to combining co-adaptive retrieval with test-time RL specifically for autoformalization in Lean 4. Prior work handles co-adaptive retrieval in general RAG, or static retrieval for autoformalization, or test-time RL for informal math, but nobody's put these together. The key insight is that Lean's structured error messages create a natural feedback loop for this approach.

The binarize-then-enrich strategy for handling heterogeneous rewards is incremental—it's essentially merging DDRL's debiasing with multi-reward normalization—but it does address a gap that DDRL explicitly left open. And applying test-time RL to autoformalization itself is new, since majority voting doesn't work for formal statements the way it does for informal reasoning.

That said, I should be honest: this is fundamentally a systems integration paper. Each piece—TTRL, co-adaptive retrieval, debiased GRPO, CriticLean—already exists. The novelty claim rests on whether combining them creates something emergent that's greater than the sum of its parts.

The "structured asymmetry" insight about Lean 4 errors versus binary rewards is compelling, but it's also somewhat obvious in hindsight—of course formal compilers give richer feedback than binary signals. And the binarize-then-enrich mechanism, once you have DDRL and GDPO, is fairly straightforward engineering rather than a deep intellectual contribution.

The real significance hinges on whether this actually works at scale. The problem itself is important and timely—MathAtlas MA-Hard sitting at 2.6% shows there's massive room for improvement. If TTRA succeeds, it establishes test-time learning as a genuine third scaling axis for formal mathematics, which would be conceptually meaningful. But the practical impact ultimately depends on how much improvement we actually see.

The related work coverage is exceptionally thorough, spanning RL approaches for autoformalization, semantic critics, debiased RL methods, retrieval-augmented techniques, test-time compute strategies, and error analysis work. The positioning against each area is clear and specific, showing deep familiarity with the landscape.

Looking at the strengths and weaknesses, the core insight about leveraging Lean 4's structured error signals for co-adaptive retrieval is genuinely novel and well-motivated, addressing a timely problem. The de-risking strategy with phased go/no-go decisions demonstrates research maturity, and each component has empirical grounding. However, this is fundamentally an integration paper where novelty comes from the combination rather than individual components. The approach feels somewhat natural once you recognize the structured feedback advantage of formal languages, and the binarize-then-enrich mechanism is incremental. There's real risk that combining these pieces won't yield emergent benefits beyond what they offer individually. Still, it's a well-crafted proposal that fills a genuine gap, with clear motivation and thoughtful de-risking.

For AAAI 2026, I'm estimating novelty as moderately novel since the combination is new but individual pieces exist, and significance as medium-to-strong given the problem's importance and potential influence. The related work coverage is exceptionally thorough. I'd put the acceptance probability around 30-40%, centered at 33-35%. Actually, reconsidering—the proposal is extremely well-written and comprehensive with clear differentiation from related work. The core insight about exploiting Lean 4's structured error taxonomy for co-adaptive retrieval during TTRL is genuinely non-trivial, and the structural asymmetry argument between formal and informal reasoning is compelling. The de-risking strategy is mature and the whole thing is well-executed, but I need to remember that top-tier venues often expect more surprising or transformative insights.

The real question is whether the core idea itself is strong enough, separate from how well it's presented. The idea is using Lean 4's structured compilation errors as training signals for co-adapting a retriever during test-time RL with a calibrated semantic critic and debiased multi-tier rewards. A skeptical reviewer might argue that it's intuitive that formal language compilers provide richer feedback than binary rewards, or that combining DDRL with GDPO is straightforward engineering—the real test would be whether this produces significant empirical gains. But a supportive reviewer would highlight that identifying compilation error messages as retriever training signals is clever, the framing of test-time learning as a third scaling axis is compelling, and the comprehensive approach demonstrates genuine insight.

For AAAI specifically, this is a well-motivated systems paper combining multiple techniques in a novel way within a growing field, which the venue tends to appreciate. However, AAAI reviewers might worry the paper is too complex, question whether empirical results justify the system complexity, or see it as having too many moving parts. Balancing these considerations, I'm settling on around 32% as my estimate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38835fe8-d5d8-4af9-a80b-fff998089929",
  "isSidechain": false,
  "requestId": "req_011CbUTcsuz2BmARXFj9Lbqc",
  "type": "assistant",
  "uuid": "b98f5424-d93c-41a8-b694-93531a9495cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rfji3RWNDn7SFc1BMACigv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 613,
      "cache_creation_input_tokens": 2410,
      "cache_read_input_tokens": 32018,
      "output_tokens": 7791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 613,
          "output_tokens": 7791,
          "cache_read_input_tokens": 32018,
          "cache_creation_input_tokens": 2410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2410
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

_source line 49 · 2026-05-28T06:05:38.711Z_

Now I have sufficient information to conduct a thorough assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

- TTRL (NeurIPS 2025, arXiv:2504.16084): 首个在无标注数据上通过多数投票产生伪标签进行 test-time RL 的工作。Qwen2.5-Math-7B 在 AIME 2024 上 pass@1 提升 ~211%。仅适用于有确定数值答案的非形式化数学推理——多数投票对形式化语句不适用。TTRA 的出发点正是解决这一局限。

- DDRL (ACL 2026 Findings, arXiv:2604.21327): 识别并修复 GRPO 在低共识区间对伪奖励的放大效应。使用频率感知平衡采样 + 固定 ±1 advantage + 共识离策略精炼。在 AIME 2024 上对 Qwen2.5-Math-1.5B 实现 19% 相对提升。但**明确限于二值奖励**，作者自己将多层级奖励列为 future work。TTRA 的 binarize-then-enrich 直接回应此 gap。

- GDPO (NVIDIA, arXiv:2601.05242): 解决多奖励 GRPO 训练中信号坍缩问题，对每个奖励分量独立归一化。在 AIME 上对 DeepSeek-R1-1.5B 精度提升 6.3%。但不处理伪标签噪声/去偏。TTRA 将 GDPO 的多奖励归一化与 DDRL 的去偏结合。

- CriticLean (arXiv:2507.06181, ByteDance/南京): CriticLeanGPT-14B-RL 在平衡 CriticLeanBench 上达 84.8% 准确率。首个训练专门的语义评判器来评估 Lean 4 形式化是否忠实于原始语义。但**基准分布是 250/250 平衡**的，与 OOD TTRL 中 <10% 可编译的极度偏斜分布不同。TTRA 的 Phase 0 校准协议正是针对此分布偏移。

- FormaRL (COLM 2025, arXiv:2508.18914): 首个用 GRPO 做 autoformalization RL 的工作。编译检查 + LLM 一致性检查作为奖励。Qwen2.5-Coder-7B 在 ProofNet 上 pass@1 从 4.04% 提升至 26.15%。但是**训练时 RL**，无 test-time 适应，无检索。

- Wang et al. (NeurIPS 2025 MAR Workshop): 在线 RL for autoformalization，使用 GRPO + BEq + embedding 奖励。TC1: 17.29%→26.01%。最接近的先前工作，但仍是**训练时、分布内**，无检索，无 test-time 适应，无训练过的语义评判器。

- Aria (ICLR 2026, arXiv:2510.04520): 当前检索增强 autoformalization 的 SOTA。通过依赖图分解 + 迭代形式化 + AriaScorer 在 ProofNet 上达 91.6% 编译 / 68.5% 精度，在同调猜想上 42.9%（其他系统 0%）。关键局限：**检索器是固定的**，不随形式化器行为漂移而适应；**模型权重不更新**。

- DDR (arXiv:2511.11990): 构建 500K 样本依赖数据集。量化前沿 LLM 的标识符幻觉率 Hall_m=0.21-0.39，通过检索降至 <0.02。证实标识符幻觉是可量化的主要错误模式。

- AMBER/Construction-Verification (arXiv:2602.01291): 在 3,189 个编译错误中，47.3% 来自标识符幻觉（DeepSeek-R1 在应用数学上）。为 TTRA 关于 Tier 1 错误占主导的假设提供独立实证。

- FormalEvolve (arXiv:2603.19828): 将 autoformalization 表述为有预算的进化搜索。SH@100 在 CombiBench 58.0%，ProofNet 84.9%。**搜索固定模型的输出空间，不做权重适应或检索器共适应**。与 TTRA 正交。

- TEMPO (arXiv:2604.19295): 将 TTT 形式化为 EM（策略精炼 = M-step，评判器重校准 = E-step）。证明省略重校准导致 ELBO 退化和多样性坍缩。为 TTRA 的双循环设计提供概念支撑。

- T³RL (arXiv:2603.02203): 将外部工具验证引入 TTRL，用代码执行输出加权投票。但**将工具反馈压缩为单个二值信号**（verified/unverified），丢弃工具输出的内部结构。

- R3 (NeurIPS 2025, arXiv:2510.24652): 通过强化对比学习优化 RAG 检索。在通用 RAG 上提升 5.2%。验证了基于环境反馈训练检索器的范式可行性。

- Reinforced-IR (ACL 2025): 交替 RLRF/RLGF 实现检索器-生成器互适应。验证共适应检索的范式，但未应用于 autoformalization。

- MathAtlas (arXiv:2605.14061, May 2026): 52K 研究生级数学问题，178K 依赖关系。最强基线仅 9.8% 定理正确率，MA-Hard 上 2.6%。证实 OOD autoformalization 是未解决的挑战。

- **调研总结**: Autoformalization 领域正处于方法快速演进阶段：训练时 RL（FormaRL, Wang et al.）、检索增强（Aria, DDR, DRIFT）、推理时搜索（FormalEvolve）、语义评判（CriticLean）各自取得显著进展，但**尚无工作将 test-time RL 应用于 autoformalization**，也**无工作在 TTRL 中实现检索器共适应**。TTRA 位于这些独立研究线的交汇处，填补的是一个真实存在的空白。

【Trivial Alternative 检验】:

最直接的 trivial alternative 是 **Best-of-N 采样 + CriticLean 过滤 + 静态检索**（即 Aria 风格的检索 + 大量采样 + CriticLean 打分筛选）。Proposal 已预见到这一点并将其作为 compute-matched baseline。关键问题是：TTRA 的权重适应相对于这个 trivial baseline 的增量价值是什么？

Proposal 的论证是：对于真正的 OOD 领域（MathAtlas MA-Hard: 2.6%），固定模型的输出空间可能根本不包含正确的形式化——无论采样多少次都无法找到模型无法生成的内容。这个论证在概念上是合理的，但其成立程度取决于 OOD 的"远"程度。对于中等 OOD，Best-of-N + 检索可能已经足够。因此 TTRA 的增量价值主要体现在**极端 OOD 场景**，这限制了其适用范围但也提高了其在该场景下的 significance。

另一个 trivial alternative：**标准 SFT/继续预训练在 OOD 领域数据上** + 静态检索。如果有少量 OOD 领域的标注数据，常规微调可能比 TTRL 更简单有效。但 TTRA 的设定是**无标注 OOD 数据**的 test-time 适应，这使得这个 alternative 不完全可比。

**结论**：存在 trivial alternative 威胁，但 proposal 已明确将其纳入实验对比。增量价值的论证在极端 OOD 场景下合理，在中等 OOD 场景下需实验验证。

【前提假设检验】:

1. **"Lean 4 结构化错误信号可以作为检索器训练的 oracle-quality 信号"** — **部分成立，但有过度声称的风险**。当编译器报告 `unknownIdentifier "Finset.sum_bij"` 时，确实直接指出需要的标识符。但"oracle-quality"措辞过强：(a) 模型可能幻觉出不存在的标识符名称，此时错误信号指向一个不存在的目标；(b) 对于 Tier 2 错误（类型不匹配），从错误信息到正确依赖的映射并不总是一对一的。AMBER 的 47.3% 数据支持 Tier 1 错误占主导，但这是 DeepSeek-R1 的数据，TTRA 使用 Qwen3-8B 可能分布不同——Phase -1 旨在验证此点。

2. **"CriticLean-14B 在极度偏斜分布下仍可保持足够精度"** — **未经验证但有合理的去风险策略**。CriticLeanBench 是 250/250 平衡的，而 OOD TTRL 中 <10% 可编译。Phase 0 的 go/no-go gate 是合理的，但如果 CriticLean 在此分布下精度不足，整个框架的核心组件就失效了。

3. **"共适应检索的增量收益足够显著"** — **最关键的未验证假设**。R3 和 Reinforced-IR 在通用 RAG 上验证了共适应检索的价值，但 autoformalization 的检索空间（Mathlib 26K+ 定义）结构非常不同于通用文档检索。FAISS 在高频重建下的性能开销也是实际考量。

4. **"DDRL 的去偏 + GDPO 的多奖励归一化可以直接组合"** — **合理但简化**。两个方法各自被验证，但它们的组合是否引入新的交互效应（如去偏采样改变了多奖励归一化的有效样本分布）未被讨论。

5. **"TTRL 中的政策漂移不会导致检索器训练信号退化"** — Proposal 引用 TEMPO 的 EM 分析，但 TEMPO 处理的是评判器重校准而非检索器。检索器-形式化器共适应可能存在不同的稳定性特征。

【3 维度打分】:

1. **Novelty: 中** — 

TTRA 的核心 novelty 是一个**领域交叉集成创新**：将 co-adaptive retrieval（R3, Reinforced-IR 验证了范式）、test-time RL（TTRL 验证了范式）、debiased multi-tier reward（DDRL + GDPO 各自验证了组件）、semantic critic（CriticLean 验证了工具）四条独立研究线首次组合应用于 autoformalization。

关键创新点：
- **Lean 4 结构化错误 → 检索器训练信号** 的洞察是非平凡的，在我的调研范围内确实无先前工作发现并利用此联系。T³RL 将工具反馈压缩为二值信号丢弃了内部结构，FormalEvolve 仅用编译成功/失败，Aria 的检索器不适应——TTRA 对此的差异化定位清晰。
- **Binarize-then-enrich** 直接回应 DDRL 论文自身声明的 future work，填补真实 gap。

但需要诚实承认：
- 这本质上是一个**系统集成**论文，每个组件独立存在，novelty 在于组合而非单个组件。
- "形式语言提供比二值奖励更丰富的反馈"这一核心洞察，一旦被陈述出来就显得**合理但不令人惊讶**——reviewer 可能会说 "of course compilers give richer feedback"。
- Binarize-then-enrich 的技术贡献相对直接（在 DDRL 的二值化层上叠加 GDPO 的多奖励归一化）。

2. **Significance: 中偏强** — 

问题本身重要：OOD autoformalization 是真实且困难的挑战（MathAtlas MA-Hard 2.6% 证实了这一点）。如果 TTRA 成功，它：
- 建立 test-time learning 作为形式数学的第三个 scaling axis（训练时、推理时之外），这是有影响力的框架性贡献
- 提供首个将 TTRL 扩展到非数值答案领域（形式化语句）的方法，可能推广到其他有结构化编译/验证反馈的任务（如代码生成）
- 解决 static retriever 不适应 policy drift 的已知局限（Aria 的核心瓶颈之一）

但 significance 受限于：
- 实际影响取决于改进幅度——如果在 MathAtlas MA-Hard 上从 2.6% 到 5%，技术上有意义但实用价值有限
- 应用场景相对窄（Lean 4 autoformalization with Mathlib），不是一个通用方法
- 资源需求高（1400-1900 A100-hours），但这不影响 idea 评估

3. **Related Work: 强** — 

这是整个 proposal 最强的维度。覆盖了：
- 6 个相关研究方向的所有核心工作
- 每篇工作的具体数据、局限性和与 TTRA 的差异
- 最新至 2026 年 5 月的工作（MathAtlas, Dymetman binary rewards）
- 明确的差异化定位：对 Aria（静态检索器）、DDRL（二值奖励限制）、T³RL（丢弃工具反馈结构）、FormalEvolve（无权重适应）等逐一清晰区分

我的调研验证了 proposal 中引用的论文均真实存在，描述基本准确。未发现遗漏的重要竞争工作。唯一轻微疏漏：proposal 未充分讨论 **Lean 4 Cycle Consistency Fine-tuning** (arXiv:2603.24372) 等更小规模但相关的工作，但这不影响核心定位。

【概率估计】: [28% - 38%] 中位 32%

【估计理由】: 

Novelty 是限制上界的主要维度。TTRA 是一个高质量的系统集成工作，而非根本性的方法论创新。核心洞察（Lean 4 错误信号 → 检索器训练信号）虽然在调研范围内确认为 novel，但不属于"反直觉"级别——一旦认识到形式语言的结构化反馈优势，方法论自然跟进。审稿人可能会评价为 "well-motivated combination, but the individual pieces are not new"。

Significance 处于中偏强：问题重要（OOD autoformalization 确实困难且未解决），框架性贡献（第三 scaling axis）有价值，但应用面相对窄。

Related Work 是强项，不会成为被拒原因。

综合来看：这个 proposal 的 idea 内核处于 "方向正确 + 有真实 novelty delta + 但核心发现 if positive 审稿人大概率说 'makes sense, well-engineered' 而非 'surprising'" 的区间，对应 rubric 中 25-35% 的锚点。考虑到 related work 极其充分且问题的时效性/重要性，上调至 28-38%，中位 32%。

【主要风险】: 
1. **"组合 vs 创新" 的审稿人争论**：核心贡献是四条研究线的首次组合，每个组件独立存在。审稿人可能认为 "engineering contribution > intellectual contribution"，尤其是如果 binarize-then-enrich 被认为是 DDRL + GDPO 的直接拼接。
2. **核心洞察的 surprise 不足**："形式语言编译器提供比二值奖励更丰富的反馈" 这一洞察，虽然在此前工作中未被利用，但陈述后显得近乎显然，可能被审稿人认为缺乏深度——从而将整体贡献降级为 "a solid system paper" 而非 "a paper with a deep new insight"。
```

Sources:
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/pdf/2504.16084)
- [DDRL: Spurious Signal Amplification in TTRL](https://arxiv.org/html/2604.21327)
- [GDPO: Group reward-Decoupled Normalization](https://arxiv.org/abs/2601.05242)
- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181)
- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)
- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)
- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652)
- [Aria: An Agent for Retrieval and Iterative Auto-Formalization](https://arxiv.org/abs/2510.04520)
- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)
- [FormalEvolve: Neuro-Symbolic Evolutionary Search](https://arxiv.org/abs/2603.19828)
- [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/abs/2604.19295)
- [T³RL: Tool Verification for Test-Time RL](https://arxiv.org/abs/2603.02203)
- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)
- [AMBER/Construction-Verification Benchmark](https://arxiv.org/abs/2602.01291)
- [TTARAG: Test Time Adaptation for RAG](https://arxiv.org/abs/2601.11443)
- [CriticLeanGPT-Qwen3-14B-RL on HuggingFace](https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b98f5424-d93c-41a8-b694-93531a9495cb",
  "isSidechain": false,
  "requestId": "req_011CbUTcsuz2BmARXFj9Lbqc",
  "type": "assistant",
  "uuid": "754be688-1e5b-4a96-805c-ce7439ac0e74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rfji3RWNDn7SFc1BMACigv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 613,
      "cache_creation_input_tokens": 2410,
      "cache_read_input_tokens": 32018,
      "output_tokens": 7791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 613,
          "output_tokens": 7791,
          "cache_read_input_tokens": 32018,
          "cache_creation_input_tokens": 2410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2410
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "754be688-1e5b-4a96-805c-ce7439ac0e74",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal acceptance probability",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization  ## Core Problem  Cur…",
  "leafUuid": "754be688-1e5b-4a96-805c-ce7439ac0e74",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate autoformalization TTRL proposal acceptance probability",
  "sessionId": "f293bf8a-8e22-4fc3-9edb-c980c35f7fc1"
}
```

---
