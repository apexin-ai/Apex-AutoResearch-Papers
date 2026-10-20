# Research conversation: MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL ## Core Problem RL-trained

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/0e0543e7-e1f4-48a2-b8f4-05aecae274a4.jsonl`
- **Structured JSON:** [`fb337b4708e79ec576ac.json`](../../sessions/fb/fb337b4708e79ec576ac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:17:39.799Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:17:39.799Z",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "content": "# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL\n\n## Core Problem\n\nRL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface perturbations: open-weight reasoning models drop up to 55% (Robust Reasoning Benchmark, arXiv 2604.08571), and VAR-MATH (arXiv 2507.12885) documents 47-73% drops concentrated in sub-frontier models on competition-level problems. Binary reward provides no gradient against surface-form-dependent strategies.\n\nExisting augmentation methods (TA-GRPO, arXiv 2601.22478; PrAg-PO, arXiv 2602.03190) pool rewards across equivalent variants but optimize reward, not strategy invariance. Critically, in the \"both-correct regime\" (both original and perturbed variants solved), pooled advantage yields identical signals—zero differential gradient—leaving surface-dependent reasoning strategies unrectified. This regime becomes increasingly prevalent as training progresses and model accuracy rises, meaning augmentation-only methods suffer diminishing corrective power precisely when fine-grained strategy refinement matters most. Can structure-aware consistency regularization during GRPO enforce perturbation-invariant reasoning strategies, especially in this late-training regime?\n\n## Key Insight: Augmentation Optimizes Reward, Consistency Optimizes Strategy\n\nTA-GRPO's pooled advantage provides effective learning signal when one variant is solved and the other is not (early training, lower accuracy). But as training progresses and accuracy increases, the both-correct regime dominates, and TA-GRPO's signal diminishes. MACR's explicit consistency loss fills this gap: it provides gradient even when both variants are correct, enforcing not just correct answers but structurally similar reasoning. This creates a natural phase complementarity—augmentation drives initial learning, consistency drives late-stage refinement from \"getting it right\" to \"getting it right for the right reasons.\"\n\n## Critical Technical Challenge: Math ≠ Vision for Consistency\n\nROMA (arXiv 2605.09262) achieves visual robustness via token-level KL between corrupted and clean trajectories under teacher forcing. This works because visual perturbation (blur, noise) preserves the correct answer—the same reasoning trace is valid for both views. In math, numerical substitution (2x+3=7 → 5x+2=12) changes the answer and intermediate computations. Naively applying ROMA's token-level divergence would penalize correct numerical differences alongside genuine strategy divergence.\n\nWe propose **Trajectory-Translated Teacher Forcing (T3F)** as the core mechanism for Structure-Aware Consistency (SAC):\n\n1. For original problem x, select a correct rollout trajectory τ_x from GRPO sampling.\n2. Using SymPy's known perturbation mapping M (e.g., {a=2→a=5, variable x→variable y}), mechanically translate τ_x into τ_translated by substituting corresponding numerical values and variable names. Since SymPy controls the perturbation, the mapping is exact and deterministic. τ_translated has identical length and structure to τ_x—only problem-specific values change.\n3. Teacher-force the model on perturbed input x' with prefix from τ_translated, collecting per-token logit distributions.\n4. Teacher-force the model on original input x with prefix from τ_x, collecting per-token logit distributions.\n5. Compute token-level JS divergence between the two logit distribution sequences, with numerical-token masking as secondary noise reduction.\n\nT3F resolves the alignment problem: trajectory translation creates exact position correspondence, making token-level divergence well-defined without requiring step-level alignment algorithms (e.g., DTW). The divergence directly measures: \"Given structurally identical reasoning contexts (differing only in problem-specific values), does the model assign similar probabilities to structurally corresponding next tokens?\"\n\n**Why token-level, not step-type-level?** A coarser alternative would compare only reasoning step types (e.g., \"set up equation → simplify → solve\"). But step-type consistency cannot distinguish between correct algebraic manipulation and pattern-matching shortcuts within the same step type. Token-level granularity captures intra-step strategy differences—the fine-grained signal that matters for eliminating surface heuristics.\n\n**Masking policy and boundary conditions.** Numerical token identification uses regex matching against SymPy's perturbation mapping (problem-copied values and their direct derivatives). Mathematical constants (π, e), step indices, and tokens not traceable to problem-specific values are retained in the JS computation. This conservative masking policy is sound because SymPy-controlled perturbations guarantee that only mapped values differ between τ_x and τ_translated; unmapped numerical tokens (e.g., mathematical constants shared across variants) should indeed be consistent. Limitation: for perturbation types beyond token-level substitution (e.g., expression rewriting \"a+b\" → \"b+a\"), trajectory translation may introduce structural shifts; for these, we fall back to rollout-level outcome consistency (JS over correctness distributions across K rollouts) as a coarser but robust signal.\n\n## Research Landscape\n\n**Diagnostic-only (no training fix):** VAR-MATH (arXiv 2507.12885): 47-73% drops, sub-frontier models on competition math. MATH-Perturb (ICML 2025, arXiv 2502.06453): 279 MATH level-5 problems, distinguishes solution-preserving (Simple) vs. solution-changing (Hard) perturbation. GSM-Symbolic (ICLR 2025): performance variance across instantiations, 25 models evaluated. Robust Reasoning Benchmark (arXiv 2604.08571): 14 encoding/structural perturbation types on AIME 2024, orthogonal to semantic-preserving perturbation.\n\n**Augmentation-only (no invariance objective):** TA-GRPO (arXiv 2601.22478): +9.84pp competition math via cross-variant pooled advantage, no consistency loss, no robustness evaluation. PrAg-PO (arXiv 2602.03190): prompt augmentation stabilizes GRPO, mitigates entropy collapse, no invariance objective.\n\n**Structural RL (different mechanism):** AbstRaL (ICLR 2026, arXiv 2506.07751): input-side mechanism—teaches models to abstract GSM problems into symbolic representations before solving. Achieves near-full robustness recovery on GSM variants but untested on competition-level math. MACR is output-side (constrains reasoning strategy consistency). These are orthogonal: abstraction changes how the model reads problems, consistency changes how it reasons. Potentially complementary. MathForge/DGPO (ICLR 2026): difficulty-aware GRPO, no robustness evaluation.\n\n**Causal/consistency RL (different target):** GC²PO (arXiv 2602.06475): episodic causal counterfactual reward evaluating whether reasoning steps remain stable under within-problem counterfactual perturbations—focuses on step-level causal robustness within a single problem. MACR targets cross-problem strategy invariance across semantically equivalent perturbations—a complementary but distinct objective. GRPO-CARE (arXiv 2506.16141): consistency-aware RL for video reasoning (step-answer coherence, not cross-perturbation invariance). CC-LEARN (arXiv 2506.15662): cohort consistency RL for NLU tasks. COPO (arXiv 2508.04138): consistency-entropy for zero-advantage training efficiency—addresses the same upstream problem (gradient vanishing in all-correct groups) but through advantage redesign rather than cross-perturbation consistency. DPH-RL: JS for diversity, not invariance.\n\n**Consistency regularization (different domain/setting):** ROMA (arXiv 2605.09262): correctness-conditioned token-level KL for visual corruption robustness, closest methodological cousin but operates where perturbation preserves answers. F2C (arXiv 2510.14242)/PPCL: JS-based consistency, SFT-only, NLU-only.\n\n**Gap:** No work combines math-equivalence-aware perturbation with trajectory-translated structure-aware consistency during RL training. The T3F mechanism—which resolves the fundamental math-vs-vision consistency gap via SymPy-guided trajectory translation—is the core technical novelty.\n\n## Proposed Approach\n\nMACR integrates perturbation-invariance into GRPO training on Qwen3-8B via four components:\n\n**(1) SymPy-Verified Symbolic Perturbation Generator.** Creates equivalent variants through: numerical substitution, variable renaming, expression rewriting (a+b → b+a), constraint reformulation (\"A exceeds B by 3\" → \"B is 3 less than A\"). All variants SymPy-verified for answer equivalence. Inspired by Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187). Coverage limitation: SymPy handles algebra/equation problems well but has limited coverage for geometry, combinatorics, and number theory. For non-coverable problems, LLM-based perturbation with majority-vote verification serves as fallback. We report per-topic perturbation coverage rates.\n\n**(2) Structure-Aware Consistency (SAC) via T3F.** For each (original, perturbed) pair where both are correctly solved in GRPO rollouts: apply Trajectory-Translated Teacher Forcing (detailed above) to compute token-level JS divergence over reasoning structure. Correctness-conditioning (à la ROMA) restricts enforcement to successful pairs, avoiding systematically wrong invariance. For perturbation types where trajectory translation is imprecise (expression rewriting, constraint reformulation), fall back to rollout-level outcome consistency.\n\n**(3) Contrastive Discrimination Loss.** Prevents degenerate invariance by training the model to distinguish surface-similar but semantically-different problems. Hard negatives constructed via SymPy answer-changing perturbation: modifying a coefficient/constraint so the answer changes while surface similarity is preserved. Automatically verifiable via SymPy.\n\n**(4) verl/DAPO Infrastructure.** Built on DAPO (arXiv 2025) for scalable GRPO training.\n\n## Theoretical Positioning\n\nMACR provides a lightweight process-level quality signal without step-level annotation. By requiring structurally similar reasoning on equivalent problems, SAC implicitly penalizes heuristic shortcuts: a model relying on surface pattern matching cannot consistently produce similar reasoning structures across numerically different but structurally identical problems. This positions MACR as complementary to PRM (explicit process supervision) and ORM (outcome-only)—offering process-quality pressure at zero annotation cost. This claim is offered as a secondary insight; the primary contribution is perturbation robustness.\n\n## Experimental Design\n\n**Training Data:** MATH training split (~7.5K problems) + NuminaMath-TIR subset, aligned with TA-GRPO's data regime for fair comparison. We report SymPy perturbation success rate on this training set (expected: high for algebra/equations, lower for geometry/combinatorics).\n\n**Baselines (7 tiers):**\n1. Vanilla Qwen3-8B (no RL)\n2. Standard GRPO (verl/DAPO, no augmentation or consistency)\n3. COPO (consistency-entropy advantage redesign—isolates \"fix zero-advantage\" from \"enforce cross-perturbation consistency\")\n4. TA-GRPO / PrAg-PO (augmentation-only GRPO—isolates SAC contribution)\n5. AbstRaL (abstraction + RL—direct competitor; reproduce on Qwen3-8B if feasible, otherwise use published results on shared benchmarks with explicit model-gap discussion since AbstRaL uses Llama-3/Qwen2)\n6. F2C-style generic JS consistency applied to GRPO (no math-specific perturbation or T3F—isolates math-aware design value)\n7. Full MACR\n\n**Compute-normalized comparison:** Standard GRPO with 2-3x compute budget (matched to MACR's additional forward passes) as fairness control.\n\n**Evaluation Benchmarks:**\n- Robustness (core): VAR-MATH, MATH-P-Simple (ICML 2025), GSM-Symbolic (ICLR 2025), GSM-Plus\n- Robustness (supplementary, out-of-scope for MACR): MATH-P-Hard, Robust Reasoning Benchmark (arXiv 2604.08571) — reported for completeness, no expected gains\n- Clean accuracy: MATH500, GSM8K, AIME 2024\n- OOD generalization: Minerva, OlympiadBench\n- Stratified analysis: per-topic breakdown (algebra, number theory, geometry, combinatorics) to assess SymPy coverage impact\n\n**Evaluation Metrics:**\n- Clean Accuracy: Pass@1 on standard benchmarks\n- Robust Accuracy: Pass@1 on perturbation benchmarks\n- Relative Performance Drop (RPD): (Clean − Robust) / Clean × 100%\n- Consistency Rate: fraction of templates where all instantiations correct (VAR-MATH strict)\n- Performance Variance: accuracy variance across instantiations (GSM-Symbolic style)\n- All metrics: mean ± std over 3 seeds (sensitivity analyses on 1 seed)\n\n**Ablation Study:**\n- A1: GRPO only (no augmentation, no consistency)\n- A2: GRPO + perturbation augmentation only (no consistency loss)\n- A3: GRPO + perturbation + unconditional JS (no correctness conditioning)\n- A4: GRPO + perturbation + correctness-conditioned JS without T3F (naive token-level JS, no trajectory translation)\n- A5: GRPO + perturbation + correctness-conditioned SAC via T3F (no contrastive)\n- A6: Full MACR (T3F-SAC + contrastive discrimination)\n- A7: λ sensitivity for consistency loss weight (1 seed)\n- A8: Perturbation type contribution: numerical-only vs. variable-only vs. expression-rewriting vs. all (1 seed)\n- A9: T3F teacher-forcing vs. rollout-level outcome consistency (coarse fallback)\n- A10: Masking granularity: conservative (problem-value-only) vs. aggressive (all digits) vs. no masking\n\n**Compute Estimate:** Single GRPO run on Qwen3-8B ≈ 40-80 GPU-hours on 8×A100. Core baselines (7 configs × 3 seeds = 21 runs) + key ablations (A3-A6 × 3 seeds = 12 runs) + sensitivity analyses (A7-A10 × 1 seed = 4 runs) = ~37 runs ≈ 1,500-3,000 A100 GPU-hours total. Ablation reduction strategy: A7, A8, A10 run on 1 seed for initial screening, scale to 3 seeds only for significant findings.\n\n## Key References\n\n- ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (arXiv 2605.09262, 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2507.12885, 2025)\n- AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking (ICLR 2026, arXiv 2506.07751)\n- MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations (ICML 2025, arXiv 2502.06453)\n- Robust Reasoning Benchmark (arXiv 2604.08571, 2026)\n- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478)\n- PrAg-PO: Prompt Augmentation Scales up GRPO Training (arXiv 2602.03190)\n- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)\n- DAPO: Open-Source LLM RL System at Scale (arXiv 2025)\n- F2C: Flip-Flop Consistency for Prompt Perturbation Robustness (arXiv 2510.14242, 2025)\n- GSM-Symbolic: Understanding Limitations of Math Reasoning (ICLR 2025)\n- GSM-Plus: Evaluating Robustness of LLMs as Mathematical Problem Solvers\n- GC²PO: Group Causal Counterfactual Policy Optimization (arXiv 2602.06475, 2026)\n- GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (arXiv 2506.16141)\n- COPO: Consistency-Entropy Policy Optimization (arXiv 2508.04138)\n- CC-LEARN: Cohort-based Consistency Learning (arXiv 2506.15662)\n- DPH-RL / PPCL\n- Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, 2026)\n- NuminaMath-TIR"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:17:39.804Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:17:39.804Z",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-29T06:17:39.824Z_

# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL

## Core Problem

RL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface perturbations: open-weight reasoning models drop up to 55% (Robust Reasoning Benchmark, arXiv 2604.08571), and VAR-MATH (arXiv 2507.12885) documents 47-73% drops concentrated in sub-frontier models on competition-level problems. Binary reward provides no gradient against surface-form-dependent strategies.

Existing augmentation methods (TA-GRPO, arXiv 2601.22478; PrAg-PO, arXiv 2602.03190) pool rewards across equivalent variants but optimize reward, not strategy invariance. Critically, in the "both-correct regime" (both original and perturbed variants solved), pooled advantage yields identical signals—zero differential gradient—leaving surface-dependent reasoning strategies unrectified. This regime becomes increasingly prevalent as training progresses and model accuracy rises, meaning augmentation-only methods suffer diminishing corrective power precisely when fine-grained strategy refinement matters most. Can structure-aware consistency regularization during GRPO enforce perturbation-invariant reasoning strategies, especially in this late-training regime?

## Key Insight: Augmentation Optimizes Reward, Consistency Optimizes Strategy

TA-GRPO's pooled advantage provides effective learning signal when one variant is solved and the other is not (early training, lower accuracy). But as training progresses and accuracy increases, the both-correct regime dominates, and TA-GRPO's signal diminishes. MACR's explicit consistency loss fills this gap: it provides gradient even when both variants are correct, enforcing not just correct answers but structurally similar reasoning. This creates a natural phase complementarity—augmentation drives initial learning, consistency drives late-stage refinement from "getting it right" to "getting it right for the right reasons."

## Critical Technical Challenge: Math ≠ Vision for Consistency

ROMA (arXiv 2605.09262) achieves visual robustness via token-level KL between corrupted and clean trajectories under teacher forcing. This works because visual perturbation (blur, noise) preserves the correct answer—the same reasoning trace is valid for both views. In math, numerical substitution (2x+3=7 → 5x+2=12) changes the answer and intermediate computations. Naively applying ROMA's token-level divergence would penalize correct numerical differences alongside genuine strategy divergence.

We propose **Trajectory-Translated Teacher Forcing (T3F)** as the core mechanism for Structure-Aware Consistency (SAC):

1. For original problem x, select a correct rollout trajectory τ_x from GRPO sampling.
2. Using SymPy's known perturbation mapping M (e.g., {a=2→a=5, variable x→variable y}), mechanically translate τ_x into τ_translated by substituting corresponding numerical values and variable names. Since SymPy controls the perturbation, the mapping is exact and deterministic. τ_translated has identical length and structure to τ_x—only problem-specific values change.
3. Teacher-force the model on perturbed input x' with prefix from τ_translated, collecting per-token logit distributions.
4. Teacher-force the model on original input x with prefix from τ_x, collecting per-token logit distributions.
5. Compute token-level JS divergence between the two logit distribution sequences, with numerical-token masking as secondary noise reduction.

T3F resolves the alignment problem: trajectory translation creates exact position correspondence, making token-level divergence well-defined without requiring step-level alignment algorithms (e.g., DTW). The divergence directly measures: "Given structurally identical reasoning contexts (differing only in problem-specific values), does the model assign similar probabilities to structurally corresponding next tokens?"

**Why token-level, not step-type-level?** A coarser alternative would compare only reasoning step types (e.g., "set up equation → simplify → solve"). But step-type consistency cannot distinguish between correct algebraic manipulation and pattern-matching shortcuts within the same step type. Token-level granularity captures intra-step strategy differences—the fine-grained signal that matters for eliminating surface heuristics.

**Masking policy and boundary conditions.** Numerical token identification uses regex matching against SymPy's perturbation mapping (problem-copied values and their direct derivatives). Mathematical constants (π, e), step indices, and tokens not traceable to problem-specific values are retained in the JS computation. This conservative masking policy is sound because SymPy-controlled perturbations guarantee that only mapped values differ between τ_x and τ_translated; unmapped numerical tokens (e.g., mathematical constants shared across variants) should indeed be consistent. Limitation: for perturbation types beyond token-level substitution (e.g., expression rewriting "a+b" → "b+a"), trajectory translation may introduce structural shifts; for these, we fall back to rollout-level outcome consistency (JS over correctness distributions across K rollouts) as a coarser but robust signal.

## Research Landscape

**Diagnostic-only (no training fix):** VAR-MATH (arXiv 2507.12885): 47-73% drops, sub-frontier models on competition math. MATH-Perturb (ICML 2025, arXiv 2502.06453): 279 MATH level-5 problems, distinguishes solution-preserving (Simple) vs. solution-changing (Hard) perturbation. GSM-Symbolic (ICLR 2025): performance variance across instantiations, 25 models evaluated. Robust Reasoning Benchmark (arXiv 2604.08571): 14 encoding/structural perturbation types on AIME 2024, orthogonal to semantic-preserving perturbation.

**Augmentation-only (no invariance objective):** TA-GRPO (arXiv 2601.22478): +9.84pp competition math via cross-variant pooled advantage, no consistency loss, no robustness evaluation. PrAg-PO (arXiv 2602.03190): prompt augmentation stabilizes GRPO, mitigates entropy collapse, no invariance objective.

**Structural RL (different mechanism):** AbstRaL (ICLR 2026, arXiv 2506.07751): input-side mechanism—teaches models to abstract GSM problems into symbolic representations before solving. Achieves near-full robustness recovery on GSM variants but untested on competition-level math. MACR is output-side (constrains reasoning strategy consistency). These are orthogonal: abstraction changes how the model reads problems, consistency changes how it reasons. Potentially complementary. MathForge/DGPO (ICLR 2026): difficulty-aware GRPO, no robustness evaluation.

**Causal/consistency RL (different target):** GC²PO (arXiv 2602.06475): episodic causal counterfactual reward evaluating whether reasoning steps remain stable under within-problem counterfactual perturbations—focuses on step-level causal robustness within a single problem. MACR targets cross-problem strategy invariance across semantically equivalent perturbations—a complementary but distinct objective. GRPO-CARE (arXiv 2506.16141): consistency-aware RL for video reasoning (step-answer coherence, not cross-perturbation invariance). CC-LEARN (arXiv 2506.15662): cohort consistency RL for NLU tasks. COPO (arXiv 2508.04138): consistency-entropy for zero-advantage training efficiency—addresses the same upstream problem (gradient vanishing in all-correct groups) but through advantage redesign rather than cross-perturbation consistency. DPH-RL: JS for diversity, not invariance.

**Consistency regularization (different domain/setting):** ROMA (arXiv 2605.09262): correctness-conditioned token-level KL for visual corruption robustness, closest methodological cousin but operates where perturbation preserves answers. F2C (arXiv 2510.14242)/PPCL: JS-based consistency, SFT-only, NLU-only.

**Gap:** No work combines math-equivalence-aware perturbation with trajectory-translated structure-aware consistency during RL training. The T3F mechanism—which resolves the fundamental math-vs-vision consistency gap via SymPy-guided trajectory translation—is the core technical novelty.

## Proposed Approach

MACR integrates perturbation-invariance into GRPO training on Qwen3-8B via four components:

**(1) SymPy-Verified Symbolic Perturbation Generator.** Creates equivalent variants through: numerical substitution, variable renaming, expression rewriting (a+b → b+a), constraint reformulation ("A exceeds B by 3" → "B is 3 less than A"). All variants SymPy-verified for answer equivalence. Inspired by Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187). Coverage limitation: SymPy handles algebra/equation problems well but has limited coverage for geometry, combinatorics, and number theory. For non-coverable problems, LLM-based perturbation with majority-vote verification serves as fallback. We report per-topic perturbation coverage rates.

**(2) Structure-Aware Consistency (SAC) via T3F.** For each (original, perturbed) pair where both are correctly solved in GRPO rollouts: apply Trajectory-Translated Teacher Forcing (detailed above) to compute token-level JS divergence over reasoning structure. Correctness-conditioning (à la ROMA) restricts enforcement to successful pairs, avoiding systematically wrong invariance. For perturbation types where trajectory translation is imprecise (expression rewriting, constraint reformulation), fall back to rollout-level outcome consistency.

**(3) Contrastive Discrimination Loss.** Prevents degenerate invariance by training the model to distinguish surface-similar but semantically-different problems. Hard negatives constructed via SymPy answer-changing perturbation: modifying a coefficient/constraint so the answer changes while surface similarity is preserved. Automatically verifiable via SymPy.

**(4) verl/DAPO Infrastructure.** Built on DAPO (arXiv 2025) for scalable GRPO training.

## Theoretical Positioning

MACR provides a lightweight process-level quality signal without step-level annotation. By requiring structurally similar reasoning on equivalent problems, SAC implicitly penalizes heuristic shortcuts: a model relying on surface pattern matching cannot consistently produce similar reasoning structures across numerically different but structurally identical problems. This positions MACR as complementary to PRM (explicit process supervision) and ORM (outcome-only)—offering process-quality pressure at zero annotation cost. This claim is offered as a secondary insight; the primary contribution is perturbation robustness.

## Experimental Design

**Training Data:** MATH training split (~7.5K problems) + NuminaMath-TIR subset, aligned with TA-GRPO's data regime for fair comparison. We report SymPy perturbation success rate on this training set (expected: high for algebra/equations, lower for geometry/combinatorics).

**Baselines (7 tiers):**
1. Vanilla Qwen3-8B (no RL)
2. Standard GRPO (verl/DAPO, no augmentation or consistency)
3. COPO (consistency-entropy advantage redesign—isolates "fix zero-advantage" from "enforce cross-perturbation consistency")
4. TA-GRPO / PrAg-PO (augmentation-only GRPO—isolates SAC contribution)
5. AbstRaL (abstraction + RL—direct competitor; reproduce on Qwen3-8B if feasible, otherwise use published results on shared benchmarks with explicit model-gap discussion since AbstRaL uses Llama-3/Qwen2)
6. F2C-style generic JS consistency applied to GRPO (no math-specific perturbation or T3F—isolates math-aware design value)
7. Full MACR

**Compute-normalized comparison:** Standard GRPO with 2-3x compute budget (matched to MACR's additional forward passes) as fairness control.

**Evaluation Benchmarks:**
- Robustness (core): VAR-MATH, MATH-P-Simple (ICML 2025), GSM-Symbolic (ICLR 2025), GSM-Plus
- Robustness (supplementary, out-of-scope for MACR): MATH-P-Hard, Robust Reasoning Benchmark (arXiv 2604.08571) — reported for completeness, no expected gains
- Clean accuracy: MATH500, GSM8K, AIME 2024
- OOD generalization: Minerva, OlympiadBench
- Stratified analysis: per-topic breakdown (algebra, number theory, geometry, combinatorics) to assess SymPy coverage impact

**Evaluation Metrics:**
- Clean Accuracy: Pass@1 on standard benchmarks
- Robust Accuracy: Pass@1 on perturbation benchmarks
- Relative Performance Drop (RPD): (Clean − Robust) / Clean × 100%
- Consistency Rate: fraction of templates where all instantiations correct (VAR-MATH strict)
- Performance Variance: accuracy variance across instantiations (GSM-Symbolic style)
- All metrics: mean ± std over 3 seeds (sensitivity analyses on 1 seed)

**Ablation Study:**
- A1: GRPO only (no augmentation, no consistency)
- A2: GRPO + perturbation augmentation only (no consistency loss)
- A3: GRPO + perturbation + unconditional JS (no correctness conditioning)
- A4: GRPO + perturbation + correctness-conditioned JS without T3F (naive token-level JS, no trajectory translation)
- A5: GRPO + perturbation + correctness-conditioned SAC via T3F (no contrastive)
- A6: Full MACR (T3F-SAC + contrastive discrimination)
- A7: λ sensitivity for consistency loss weight (1 seed)
- A8: Perturbation type contribution: numerical-only vs. variable-only vs. expression-rewriting vs. all (1 seed)
- A9: T3F teacher-forcing vs. rollout-level outcome consistency (coarse fallback)
- A10: Masking granularity: conservative (problem-value-only) vs. aggressive (all digits) vs. no masking

**Compute Estimate:** Single GRPO run on Qwen3-8B ≈ 40-80 GPU-hours on 8×A100. Core baselines (7 configs × 3 seeds = 21 runs) + key ablations (A3-A6 × 3 seeds = 12 runs) + sensitivity analyses (A7-A10 × 1 seed = 4 runs) = ~37 runs ≈ 1,500-3,000 A100 GPU-hours total. Ablation reduction strategy: A7, A8, A10 run on 1 seed for initial screening, scale to 3 seeds only for significant findings.

## Key References

- ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (arXiv 2605.09262, 2026)
- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2507.12885, 2025)
- AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking (ICLR 2026, arXiv 2506.07751)
- MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations (ICML 2025, arXiv 2502.06453)
- Robust Reasoning Benchmark (arXiv 2604.08571, 2026)
- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478)
- PrAg-PO: Prompt Augmentation Scales up GRPO Training (arXiv 2602.03190)
- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)
- DAPO: Open-Source LLM RL System at Scale (arXiv 2025)
- F2C: Flip-Flop Consistency for Prompt Perturbation Robustness (arXiv 2510.14242, 2025)
- GSM-Symbolic: Understanding Limitations of Math Reasoning (ICLR 2025)
- GSM-Plus: Evaluating Robustness of LLMs as Mathematical Problem Solvers
- GC²PO: Group Causal Counterfactual Policy Optimization (arXiv 2602.06475, 2026)
- GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (arXiv 2506.16141)
- COPO: Consistency-Entropy Policy Optimization (arXiv 2508.04138)
- CC-LEARN: Cohort-based Consistency Learning (arXiv 2506.15662)
- DPH-RL / PPCL
- Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, 2026)
- NuminaMath-TIR

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "41dea716-4dd0-4d21-ad81-3bbdb33f4dbd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:17:39.823Z_

```json
{
  "parentUuid": "41dea716-4dd0-4d21-ad81-3bbdb33f4dbd",
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
  "uuid": "fdba01e5-991a-4273-ab22-043c5a6b67aa",
  "timestamp": "2026-05-29T06:17:39.823Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:17:39.823Z_

```json
{
  "parentUuid": "fdba01e5-991a-4273-ab22-043c5a6b67aa",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e7487a9d-de78-4483-b181-923010246472",
  "timestamp": "2026-05-29T06:17:39.823Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
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
  "lastPrompt": "# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem  RL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface pe…",
  "leafUuid": "e7487a9d-de78-4483-b181-923010246472",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "MACR: Math reasoning robustness via consistency regularization",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:17:43.905Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal as the 补救 agent (remediation agent), focusing strictly on experimental design and technical execution completeness. I need to first do thorough literature research to understand the current experimental standards in this field before making any suggestions.

Let me search for the key papers mentioned and understand the experimental landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7487a9d-de78-4483-b181-923010246472",
  "isSidechain": false,
  "requestId": "req_011CbWNa2huXTekJxCZtf5Ph",
  "type": "assistant",
  "uuid": "73821e9f-9053-4a5e-8ea7-544bb0dd3c6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ugijaqin7gBT5BQMPRb8CG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5555,
      "cache_read_input_tokens": 14080,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 5555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5555
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

_source line 9 · 2026-05-29T06:17:44.934Z_

I need to do thorough literature research before evaluating the experimental design. Let me search for the key papers and understand current experimental standards in this field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73821e9f-9053-4a5e-8ea7-544bb0dd3c6c",
  "isSidechain": false,
  "requestId": "req_011CbWNa2huXTekJxCZtf5Ph",
  "type": "assistant",
  "uuid": "e4ca6848-c3b3-46e7-b247-c1e94e505a05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ugijaqin7gBT5BQMPRb8CG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5555,
      "cache_read_input_tokens": 14080,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 5555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5555
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

_source line 10 · 2026-05-29T06:17:45.291Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Lcx65oDGEpdpYYVJEZeoqZ`</summary>

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
  "parentUuid": "e4ca6848-c3b3-46e7-b247-c1e94e505a05",
  "isSidechain": false,
  "requestId": "req_011CbWNa2huXTekJxCZtf5Ph",
  "type": "assistant",
  "uuid": "9a52cda8-b3c7-46f7-979e-728306d1177f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ugijaqin7gBT5BQMPRb8CG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5555,
      "cache_read_input_tokens": 14080,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 5555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5555
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

_source line 11 · 2026-05-29T06:17:45.298Z_

<details><summary>↩ Tool result · `toolu_01Lcx65oDGEpdpYYVJEZeoqZ`</summary>

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
  "parentUuid": "9a52cda8-b3c7-46f7-979e-728306d1177f",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "825d44c8-573b-445b-adbc-3b78516dbc85",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "9a52cda8-b3c7-46f7-979e-728306d1177f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-29T06:17:48.494Z_

Now let me conduct my pre-research. I'll search for the key papers and experimental standards in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "825d44c8-573b-445b-adbc-3b78516dbc85",
  "isSidechain": false,
  "requestId": "req_011CbWNaSDGjui8GwfC8BxpE",
  "type": "assistant",
  "uuid": "a61d6f06-673b-4350-b8d0-f5a5a86fdace",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqoJC2P9ZEGWvaP85s5P1N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 19635,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 19635,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 13 · 2026-05-29T06:17:48.899Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DdbXQ6U5F1o6KjgQrfPKNj`</summary>

```json
{
  "query": "TA-GRPO arXiv 2601.22478 experimental design baselines evaluation math reasoning robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a61d6f06-673b-4350-b8d0-f5a5a86fdace",
  "isSidechain": false,
  "requestId": "req_011CbWNaSDGjui8GwfC8BxpE",
  "type": "assistant",
  "uuid": "eac0a829-4032-4251-ab7a-8fac6026a494",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqoJC2P9ZEGWvaP85s5P1N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 19635,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 19635,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 14 · 2026-05-29T06:17:56.531Z_

<details><summary>↩ Tool result · `toolu_01DdbXQ6U5F1o6KjgQrfPKNj`</summary>

```text
Web search results for query: "TA-GRPO arXiv 2601.22478 experimental design baselines evaluation math reasoning robustness"

Links: [{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/html/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"Why Tree-Style Branching Matters for Thought Advantage Estimation in GRPO","url":"https://arxiv.org/pdf/2509.24494"},{"title":"Synchronization in Epidemic Growth and the Impossibility of Selective Containment","url":"https://www.medrxiv.org/content/10.1101/2020.11.06.20226894.full.pdf"}]

Based on the search results, here's what I found about TA-GRPO arXiv 2601.22478:

## Overview

TA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.

## Problem and Motivation

Large language models trained via next-token prediction are fundamentally pattern-matchers: sensitive to superficial phrasing variations even when the underlying problem is identical. Group Relative Policy Optimization (GRPO) was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.

## Solution

The pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies.

## Evaluation Results

Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).

## Theoretical Justification

The paper provides theoretical justification showing that TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eac0a829-4032-4251-ab7a-8fac6026a494",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "6ef17cf9-e6fa-4777-aa97-4201eaef3d1a",
  "toolUseResult": {
    "query": "TA-GRPO arXiv 2601.22478 experimental design baselines evaluation math reasoning robustness",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NCCVmgxgzPEoJHHNdiueNm",
        "content": [
          {
            "title": "[2601.22478] Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/abs/2601.22478"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/html/2601.22478"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/pdf/2601.22478"
          },
          {
            "title": "Why Tree-Style Branching Matters for Thought Advantage Estimation in GRPO",
            "url": "https://arxiv.org/pdf/2509.24494"
          },
          {
            "title": "Synchronization in Epidemic Growth and the Impossibility of Selective Containment",
            "url": "https://www.medrxiv.org/content/10.1101/2020.11.06.20226894.full.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about TA-GRPO arXiv 2601.22478:\n\n## Overview\n\nTA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.\n\n## Problem and Motivation\n\nLarge language models trained via next-token prediction are fundamentally pattern-matchers: sensitive to superficial phrasing variations even when the underlying problem is identical. Group Relative Policy Optimization (GRPO) was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.\n\n## Solution\n\nThe pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies.\n\n## Evaluation Results\n\nExperiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).\n\n## Theoretical Justification\n\nThe paper provides theoretical justification showing that TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift."
    ],
    "durationSeconds": 7.624878881000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eac0a829-4032-4251-ab7a-8fac6026a494",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-29T06:17:59.360Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014fSBmfQ7QoWb96vWZGXkZR`</summary>

```json
{
  "query": "AbstRaL arXiv 2506.07751 ICLR 2026 experimental setup baselines GSM robustness evaluation ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ef17cf9-e6fa-4777-aa97-4201eaef3d1a",
  "isSidechain": false,
  "requestId": "req_011CbWNbG6qwinLjgtTDC13h",
  "type": "assistant",
  "uuid": "46e02f9e-24e3-43d8-96f4-7aa632126acc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3dx8qeSg2veejcH6gCh44",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 20352,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 20352,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 16 · 2026-05-29T06:18:07.691Z_

<details><summary>↩ Tool result · `toolu_014fSBmfQ7QoWb96vWZGXkZR`</summary>

```text
Web search results for query: "AbstRaL arXiv 2506.07751 ICLR 2026 experimental setup baselines GSM robustness evaluation ablation"

Links: [{"title":"[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/abs/2506.07751"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/html/2506.07751"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | OpenReview","url":"https://openreview.net/forum?id=49vo7D9LbI"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"}]

Based on the search results, here's what I found about the AbstRaL paper (arXiv 2506.07751):

## Overview
AbstRaL promotes abstract reasoning in LLMs using RL on granular abstraction data and significantly mitigates performance degradation on recent GSM perturbation benchmarks. The paper is accepted to ICLR 2026.

## Robustness Evaluation & Baselines
The work tested AbstRaL on two benchmarks that evaluate the robustness of GSM reasoning: GSM-Symbolic and GSM-Plus. Results show average accuracy across the original GSM8K testing set, testing sets with numerical variations (digit expansion, integer-decimal-fraction conversion and numerical substitution), testing sets with problem rephrasing, and testing sets with distractor insertion.

## Experimental Setup
On top of supervised fine-tuning (SFT), AbstRaL uses reinforcement learning (RL) with a new set of model-free rewards to further improve the faithfulness of generated abstraction.

## Results & Generalization
AbstRaL almost reverts the performance drop of LLMs caused by variations of relevant input conditions and significantly mitigates the interference of distracting conditions added to the perturbed testing samples. LLMs trained with AbstRaL demonstrate improved zero-shot performances on a wide range of OOD tasks within and beyond the math domain, such as AIME and BBH.

The paper appears to focus on abstract reasoning as a strategy to improve LLM robustness on grade school math problems rather than relying solely on data augmentation approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46e02f9e-24e3-43d8-96f4-7aa632126acc",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "b68175cd-fab0-47bd-ad7d-0b86909d8326",
  "toolUseResult": {
    "query": "AbstRaL arXiv 2506.07751 ICLR 2026 experimental setup baselines GSM robustness evaluation ablation",
    "results": [
      {
        "tool_use_id": "srvtoolu_013A4iXxui1DY5MMbZf29iBs",
        "content": [
          {
            "title": "[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/abs/2506.07751"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/html/2506.07751"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/pdf/2506.07751"
          },
          {
            "title": "Artificial Intelligence Jun 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | OpenReview",
            "url": "https://openreview.net/forum?id=49vo7D9LbI"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "ICLR 2026 Author Guide",
            "url": "https://iclr.cc/Conferences/2026/AuthorGuide"
          }
        ]
      },
      "Based on the search results, here's what I found about the AbstRaL paper (arXiv 2506.07751):\n\n## Overview\nAbstRaL promotes abstract reasoning in LLMs using RL on granular abstraction data and significantly mitigates performance degradation on recent GSM perturbation benchmarks. The paper is accepted to ICLR 2026.\n\n## Robustness Evaluation & Baselines\nThe work tested AbstRaL on two benchmarks that evaluate the robustness of GSM reasoning: GSM-Symbolic and GSM-Plus. Results show average accuracy across the original GSM8K testing set, testing sets with numerical variations (digit expansion, integer-decimal-fraction conversion and numerical substitution), testing sets with problem rephrasing, and testing sets with distractor insertion.\n\n## Experimental Setup\nOn top of supervised fine-tuning (SFT), AbstRaL uses reinforcement learning (RL) with a new set of model-free rewards to further improve the faithfulness of generated abstraction.\n\n## Results & Generalization\nAbstRaL almost reverts the performance drop of LLMs caused by variations of relevant input conditions and significantly mitigates the interference of distracting conditions added to the perturbed testing samples. LLMs trained with AbstRaL demonstrate improved zero-shot performances on a wide range of OOD tasks within and beyond the math domain, such as AIME and BBH.\n\nThe paper appears to focus on abstract reasoning as a strategy to improve LLM robustness on grade school math problems rather than relying solely on data augmentation approaches."
    ],
    "durationSeconds": 8.325930207,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "46e02f9e-24e3-43d8-96f4-7aa632126acc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-29T06:18:10.308Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012WQYUzXFzN4ZxKArC9tCL6`</summary>

```json
{
  "query": "ROMA arXiv 2605.09262 reinforcing multimodal reasoning visual degradation experimental design token-level KL consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b68175cd-fab0-47bd-ad7d-0b86909d8326",
  "isSidechain": false,
  "requestId": "req_011CbWNc5g4TamDbFgdGm1Ln",
  "type": "assistant",
  "uuid": "30392622-81f1-4ef6-bf7f-eac56e743948",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013dvbxban12sZfPbyGGrEbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 21075,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 21075,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 823
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

_source line 18 · 2026-05-29T06:18:17.597Z_

<details><summary>↩ Tool result · `toolu_012WQYUzXFzN4ZxKArC9tCL6`</summary>

```text
Web search results for query: "ROMA arXiv 2605.09262 reinforcing multimodal reasoning visual degradation experimental design token-level KL consistency"

Links: [{"title":"[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/abs/2605.09262"},{"title":"Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/html/2605.09262.pdf"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/html/2509.23322v2"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/html/2512.17532"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/pdf/2512.17532"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/pdf/2509.23322"}]

Based on the search results, I found the paper you're looking for. Here's the information about arXiv paper 2605.09262:

**Title:** Reinforcing Multimodal Reasoning Against Visual Degradation

**Core Problem:** Reinforcement Learning has significantly advanced the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet the resulting policies remain brittle against real-world visual degradations such as blur, compression artifacts, and low-resolution scans.

**Proposed Method (ROMA):** ROMA is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance.

**Key Technical Components:** A dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs. Additionally, a token-level surrogate KL penalty is applied against the worst-case augmentation; an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and correctness-conditioned regularization restricts enforcement to successful trajectories.

**Results:** On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30392622-81f1-4ef6-bf7f-eac56e743948",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "8db066f3-c496-4179-a899-e626c899fb20",
  "toolUseResult": {
    "query": "ROMA arXiv 2605.09262 reinforcing multimodal reasoning visual degradation experimental design token-level KL consistency",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PZ5w3S9bUUSH8d97Vd4q1s",
        "content": [
          {
            "title": "[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/abs/2605.09262"
          },
          {
            "title": "Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/html/2605.09262.pdf"
          },
          {
            "title": "Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework",
            "url": "https://arxiv.org/html/2509.23322v2"
          },
          {
            "title": "Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding",
            "url": "https://arxiv.org/html/2512.17532"
          },
          {
            "title": "Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding",
            "url": "https://arxiv.org/pdf/2512.17532"
          },
          {
            "title": "Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework",
            "url": "https://arxiv.org/pdf/2509.23322"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's the information about arXiv paper 2605.09262:\n\n**Title:** Reinforcing Multimodal Reasoning Against Visual Degradation\n\n**Core Problem:** Reinforcement Learning has significantly advanced the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet the resulting policies remain brittle against real-world visual degradations such as blur, compression artifacts, and low-resolution scans.\n\n**Proposed Method (ROMA):** ROMA is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance.\n\n**Key Technical Components:** A dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs. Additionally, a token-level surrogate KL penalty is applied against the worst-case augmentation; an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and correctness-conditioned regularization restricts enforcement to successful trajectories.\n\n**Results:** On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy."
    ],
    "durationSeconds": 7.2855434520000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "30392622-81f1-4ef6-bf7f-eac56e743948",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-29T06:18:20.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FWJk5KhuifXCZJKBBkoRE6`</summary>

```json
{
  "query": "COPO arXiv 2508.04138 consistency entropy policy optimization zero-advantage GRPO experimental baselines ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8db066f3-c496-4179-a899-e626c899fb20",
  "isSidechain": false,
  "requestId": "req_011CbWNcp2k6TbCrvHmK7opK",
  "type": "assistant",
  "uuid": "6c16f284-e74a-479c-8a84-45b991b021b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rUvoekdW7x7W1SQbakwMb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 21898,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 21898,
          "cache_creation_input_tokens": 722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 722
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

_source line 20 · 2026-05-29T06:18:28.254Z_

<details><summary>↩ Tool result · `toolu_01FWJk5KhuifXCZJKBBkoRE6`</summary>

```text
Web search results for query: "COPO arXiv 2508.04138 consistency entropy policy optimization zero-advantage GRPO experimental baselines ablation"

Links: [{"title":"COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,","url":"https://arxiv.org/pdf/2508.04138"},{"title":"COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/html/2508.04138v1"},{"title":"[2508.04138v1] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138v1"},{"title":"[2508.04138] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138"},{"title":"Artificial Intelligence 2025","url":"https://www.arxiv.org/list/cs.AI/2025?skip=29800&show=500"},{"title":"COPO: Consistency-Aware Policy Optimization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/copo-consistency-aware-policy-optimization"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=2200&show=25"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=21075&show=25"}]

I found the paper! Here's information about COPO (arXiv 2508.04138):

## Paper Overview

COPO is a consistency-entropy-based policy optimization framework that theoretically addresses the sample wastage and gradient vanishing problem under extreme samples observed in GRPO methods.

## The Problem Addressed

The paper identifies a common challenge where when multiple sampled responses under a single prompt converge to identical outcomes (whether correct or incorrect), the group-based advantage degenerates to zero, leading to vanishing gradients and rendering the corresponding samples ineffective for learning.

## Key Technical Contributions

The main contribution is a novel consistency-entropy-based policy optimization method that introduces the concept of joint optimization across both intra-group and inter-group samples to fully leverage available training data.

The framework specifically introduces a structured global reward based on outcome consistency and incorporates an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization.

The consistency entropy evaluates the consistency of the model's responses to a given prompt, and the soft blending mechanism smoothly interpolates between objectives—when response diversity is high, local optimization dominates; when response uniformity is high, global optimization dominates.

## Experimental Results

The paper demonstrates performance improvement of COPO over GRPO methods in mathematical reasoning tasks and conducts extensive ablation studies on various existing improvements to GRPO training schemes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c16f284-e74a-479c-8a84-45b991b021b4",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "ab4c1fa5-0af5-43b9-ab31-fd11eb9eb81f",
  "toolUseResult": {
    "query": "COPO arXiv 2508.04138 consistency entropy policy optimization zero-advantage GRPO experimental baselines ablation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MTeGw9wATM9TXMNjWiNDCG",
        "content": [
          {
            "title": "COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,",
            "url": "https://arxiv.org/pdf/2508.04138"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/html/2508.04138v1"
          },
          {
            "title": "[2508.04138v1] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138v1"
          },
          {
            "title": "[2508.04138] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138"
          },
          {
            "title": "Artificial Intelligence 2025",
            "url": "https://www.arxiv.org/list/cs.AI/2025?skip=29800&show=500"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/copo-consistency-aware-policy-optimization"
          },
          {
            "title": "Computer Science Aug 2025",
            "url": "https://arxiv.org/list/cs/2025-08?skip=2200&show=25"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=21075&show=25"
          }
        ]
      },
      "I found the paper! Here's information about COPO (arXiv 2508.04138):\n\n## Paper Overview\n\nCOPO is a consistency-entropy-based policy optimization framework that theoretically addresses the sample wastage and gradient vanishing problem under extreme samples observed in GRPO methods.\n\n## The Problem Addressed\n\nThe paper identifies a common challenge where when multiple sampled responses under a single prompt converge to identical outcomes (whether correct or incorrect), the group-based advantage degenerates to zero, leading to vanishing gradients and rendering the corresponding samples ineffective for learning.\n\n## Key Technical Contributions\n\nThe main contribution is a novel consistency-entropy-based policy optimization method that introduces the concept of joint optimization across both intra-group and inter-group samples to fully leverage available training data.\n\nThe framework specifically introduces a structured global reward based on outcome consistency and incorporates an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization.\n\nThe consistency entropy evaluates the consistency of the model's responses to a given prompt, and the soft blending mechanism smoothly interpolates between objectives—when response diversity is high, local optimization dominates; when response uniformity is high, global optimization dominates.\n\n## Experimental Results\n\nThe paper demonstrates performance improvement of COPO over GRPO methods in mathematical reasoning tasks and conducts extensive ablation studies on various existing improvements to GRPO training schemes."
    ],
    "durationSeconds": 7.334276852999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6c16f284-e74a-479c-8a84-45b991b021b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
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
  "lastPrompt": "# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem  RL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface pe…",
  "leafUuid": "ab4c1fa5-0af5-43b9-ab31-fd11eb9eb81f",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "MACR: Math reasoning robustness via consistency regularization",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Tool call

_source line 23 · 2026-05-29T06:18:31.401Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DEENRSHunvQG1VdZw4TVg2`</summary>

```json
{
  "query": "VAR-MATH arXiv 2507.12885 evaluation protocol metrics consistency rate performance variance math reasoning robustness 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab4c1fa5-0af5-43b9-ab31-fd11eb9eb81f",
  "isSidechain": false,
  "requestId": "req_011CbWNdbfdgnRc2DdYtQo5y",
  "type": "assistant",
  "uuid": "8edb74bb-51ec-419d-b590-626bd21fae95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDt6QUCNBgvkenUSJnXaZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 22620,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 22620,
          "cache_creation_input_tokens": 791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 791
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

_source line 24 · 2026-05-29T06:18:37.388Z_

<details><summary>↩ Tool result · `toolu_01DEENRSHunvQG1VdZw4TVg2`</summary>

```text
Web search results for query: "VAR-MATH arXiv 2507.12885 evaluation protocol metrics consistency rate performance variance math reasoning robustness 2025"

Links: [{"title":"[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/abs/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885v1"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in ...","url":"https://arxiv.org/pdf/2507.12885"},{"title":"Quantifying Ranking Instability Across Evaluation Protocol Axes in Gene Regulatory Network Benchmarking","url":"https://arxiv.org/pdf/2603.03493"},{"title":"Anomaly Detection: How to Artificially Increase your F1-Score with a   Biased Evaluation Protocol","url":"https://arxiv.org/pdf/2106.16020"},{"title":"Reliable Evaluation Protocol for Low-Precision Retrieval","url":"https://arxiv.org/pdf/2508.03306"}]

Based on the search results, here's what I found about VAR-MATH (arXiv 2507.12885):

## Overview

VAR-MATH is a symbolic evaluation framework that converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each.

## Key Problems It Addresses

The paper identifies two critical shortcomings in existing evaluation protocols for mathematical reasoning in LLMs:

1. **Benchmark Contamination**: Test problems are publicly available, thereby increasing the risk of data leakage.

2. **Evaluation Fragility**: Single-instance assessments are sensitive to stochastic outputs and fail to capture reasoning consistency.

## Evaluation Approach and Metrics

The framework converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each, which enforces consistency across structurally equivalent variants, mitigates contamination, and enhances robustness through bootstrapped metrics.

The paper was published in January 2026 and represents an evaluation-centric approach designed to probe true mathematical reasoning in large language models by going beyond single-instance success and addressing memorization concerns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8edb74bb-51ec-419d-b590-626bd21fae95",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "20d7335c-86cb-4235-99e3-31821cca4e11",
  "toolUseResult": {
    "query": "VAR-MATH arXiv 2507.12885 evaluation protocol metrics consistency rate performance variance math reasoning robustness 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D6VGtzPXcDpdiuDte4Ui6b",
        "content": [
          {
            "title": "[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/abs/2507.12885"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/html/2507.12885v1"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/html/2507.12885"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in ...",
            "url": "https://arxiv.org/pdf/2507.12885"
          },
          {
            "title": "Quantifying Ranking Instability Across Evaluation Protocol Axes in Gene Regulatory Network Benchmarking",
            "url": "https://arxiv.org/pdf/2603.03493"
          },
          {
            "title": "Anomaly Detection: How to Artificially Increase your F1-Score with a   Biased Evaluation Protocol",
            "url": "https://arxiv.org/pdf/2106.16020"
          },
          {
            "title": "Reliable Evaluation Protocol for Low-Precision Retrieval",
            "url": "https://arxiv.org/pdf/2508.03306"
          }
        ]
      },
      "Based on the search results, here's what I found about VAR-MATH (arXiv 2507.12885):\n\n## Overview\n\nVAR-MATH is a symbolic evaluation framework that converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each.\n\n## Key Problems It Addresses\n\nThe paper identifies two critical shortcomings in existing evaluation protocols for mathematical reasoning in LLMs:\n\n1. **Benchmark Contamination**: Test problems are publicly available, thereby increasing the risk of data leakage.\n\n2. **Evaluation Fragility**: Single-instance assessments are sensitive to stochastic outputs and fail to capture reasoning consistency.\n\n## Evaluation Approach and Metrics\n\nThe framework converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each, which enforces consistency across structurally equivalent variants, mitigates contamination, and enhances robustness through bootstrapped metrics.\n\nThe paper was published in January 2026 and represents an evaluation-centric approach designed to probe true mathematical reasoning in large language models by going beyond single-instance success and addressing memorization concerns."
    ],
    "durationSeconds": 5.982248739000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8edb74bb-51ec-419d-b590-626bd21fae95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T06:18:40.494Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JsCyDqGMZmGMJapUjes5g3`</summary>

```json
{
  "query": "GC2PO arXiv 2602.06475 causal counterfactual policy optimization math reasoning experimental setup 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20d7335c-86cb-4235-99e3-31821cca4e11",
  "isSidechain": false,
  "requestId": "req_011CbWNeGhtQv2tpTPyCwVP2",
  "type": "assistant",
  "uuid": "af94e81f-64bc-426b-bfa1-c12348a17fa2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pG4QJnYNJ3FDpvy9vzZiG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 23411,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 23411,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 26 · 2026-05-29T06:18:53.765Z_

<details><summary>↩ Tool result · `toolu_01JsCyDqGMZmGMJapUjes5g3`</summary>

```text
Web search results for query: "GC2PO arXiv 2602.06475 causal counterfactual policy optimization math reasoning experimental setup 2026"

Links: [{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLMs","url":"https://arxiv.org/html/2602.06475v2"},{"title":"Counterfactual Policy Optimization","url":"https://www.emergentmind.com/topics/counterfactual-policy-optimization"},{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning","url":"https://arxiv.org/pdf/2602.06475"},{"title":"Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization","url":"https://arxiv.org/pdf/2602.09331"},{"title":"Towards Causal Model-Based Policy Optimization","url":"https://arxiv.org/pdf/2503.09719"},{"title":"Online Causal Kalman Filtering for Stable and Effective Policy Optimization","url":"https://arxiv.org/html/2602.10609"}]

Based on the web search results, I found the arXiv paper you're looking for. Here's what I found:

## Paper Overview

The paper proposes Group Causal Counterfactual Policy Optimization (GC²PO) to explicitly train LLMs to learn generalizable reasoning patterns.

## The Problem Addressed

Existing reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization.

## Core Methodology

The approach proposes an episodic causal counterfactual reward that jointly captures (i) robustness, encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations; and (ii) effectiveness, enforcing sufficient variability so that the learned reasoning strategy can transfer across questions.

## How It Works

The method automatically segments each question-solution pair into distinct episodes via prompt design, computes a causal counterfactual reward for each episode consisting of two terms that jointly measure the robustness and effectiveness of the reasoning step, and leverages these rewards with the outcome reward to construct token-level advantages, optimizing the LLM to internalize generalizable reasoning strategies.

Extensive experiments on diverse benchmarks demonstrate its advantages. The paper was published on February 9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af94e81f-64bc-426b-bfa1-c12348a17fa2",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "1b16f425-c4ba-40ee-a9aa-9ba6154370af",
  "toolUseResult": {
    "query": "GC2PO arXiv 2602.06475 causal counterfactual policy optimization math reasoning experimental setup 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CvpHu4kRXn2Q6g23Gezq9r",
        "content": [
          {
            "title": "Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLMs",
            "url": "https://arxiv.org/html/2602.06475v2"
          },
          {
            "title": "Counterfactual Policy Optimization",
            "url": "https://www.emergentmind.com/topics/counterfactual-policy-optimization"
          },
          {
            "title": "Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.06475"
          },
          {
            "title": "Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization",
            "url": "https://arxiv.org/pdf/2602.09331"
          },
          {
            "title": "Towards Causal Model-Based Policy Optimization",
            "url": "https://arxiv.org/pdf/2503.09719"
          },
          {
            "title": "Online Causal Kalman Filtering for Stable and Effective Policy Optimization",
            "url": "https://arxiv.org/html/2602.10609"
          }
        ]
      },
      "Based on the web search results, I found the arXiv paper you're looking for. Here's what I found:\n\n## Paper Overview\n\nThe paper proposes Group Causal Counterfactual Policy Optimization (GC²PO) to explicitly train LLMs to learn generalizable reasoning patterns.\n\n## The Problem Addressed\n\nExisting reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization.\n\n## Core Methodology\n\nThe approach proposes an episodic causal counterfactual reward that jointly captures (i) robustness, encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations; and (ii) effectiveness, enforcing sufficient variability so that the learned reasoning strategy can transfer across questions.\n\n## How It Works\n\nThe method automatically segments each question-solution pair into distinct episodes via prompt design, computes a causal counterfactual reward for each episode consisting of two terms that jointly measure the robustness and effectiveness of the reasoning step, and leverages these rewards with the outcome reward to construct token-level advantages, optimizing the LLM to internalize generalizable reasoning strategies.\n\nExtensive experiments on diverse benchmarks demonstrate its advantages. The paper was published on February 9, 2026."
    ],
    "durationSeconds": 13.268042769,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "af94e81f-64bc-426b-bfa1-c12348a17fa2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-29T06:18:56.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013mmnRKuETxe55M9pVeTmJ1`</summary>

```json
{
  "query": "MATH-Perturb ICML 2025 arXiv 2502.06453 benchmarking perturbation types evaluation protocol baselines tested"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b16f425-c4ba-40ee-a9aa-9ba6154370af",
  "isSidechain": false,
  "requestId": "req_011CbWNfUfVvtNA1BCM6HRun",
  "type": "assistant",
  "uuid": "7736fbc1-2920-4104-9bac-471e4ba09418",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUky8coU6TBdT5Q3u9tUi8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 24131,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 24131,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 702
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

_source line 28 · 2026-05-29T06:19:04.334Z_

<details><summary>↩ Tool result · `toolu_013mmnRKuETxe55M9pVeTmJ1`</summary>

```text
Web search results for query: "MATH-Perturb ICML 2025 arXiv 2502.06453 benchmarking perturbation types evaluation protocol baselines tested"

Links: [{"title":"[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/abs/2502.06453"},{"title":"GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://github.com/Kaffaljidhmah2/MATH-Perturb"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.06453"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities","url":"https://arxiv.org/pdf/2502.06453"},{"title":"ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://icml.cc/virtual/2025/poster/45435"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/html/2502.06453"},{"title":"Modeling and predicting single-cell multi-gene perturbation responses with scLAMBDA","url":"https://www.biorxiv.org/content/10.1101/2024.12.04.626878.full.pdf"},{"title":"Geometry-informed irreversible perturbations for accelerated convergence of Langevin dynamics","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9485103/"}]

Based on the search results, I can provide you with information about MATH-Perturb:

## Overview

MATH-Perturb investigates whether large language models' impressive performance on challenging mathematical reasoning tasks is achieved by true reasoning capability or memorization. Prior work has constructed mathematical benchmarks when questions undergo simple perturbations—modifications that preserve the underlying reasoning patterns of solutions—however no work has explored hard perturbations, which fundamentally change the nature of the problem so that the original solution steps do not apply.

## Benchmark Components

The research constructs MATH-P-Simple and MATH-P-Hard via simple perturbation and hard perturbation, respectively, each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.

## Key Results

Significant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).

## Publication Details

The paper is accepted to ICML 2025 and is available as arXiv preprint arXiv:2502.06453. The corresponding GitHub repository contains evaluation code and the dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7736fbc1-2920-4104-9bac-471e4ba09418",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "070238d9-2a3d-4ad3-ad2a-c6f0f6c118e7",
  "toolUseResult": {
    "query": "MATH-Perturb ICML 2025 arXiv 2502.06453 benchmarking perturbation types evaluation protocol baselines tested",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TX96gX1cTkqEVqUwNbdkau",
        "content": [
          {
            "title": "[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/abs/2502.06453"
          },
          {
            "title": "GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://github.com/Kaffaljidhmah2/MATH-Perturb"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2502.06453"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities",
            "url": "https://arxiv.org/pdf/2502.06453"
          },
          {
            "title": "ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://icml.cc/virtual/2025/poster/45435"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/html/2502.06453"
          },
          {
            "title": "Modeling and predicting single-cell multi-gene perturbation responses with scLAMBDA",
            "url": "https://www.biorxiv.org/content/10.1101/2024.12.04.626878.full.pdf"
          },
          {
            "title": "Geometry-informed irreversible perturbations for accelerated convergence of Langevin dynamics",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9485103/"
          }
        ]
      },
      "Based on the search results, I can provide you with information about MATH-Perturb:\n\n## Overview\n\nMATH-Perturb investigates whether large language models' impressive performance on challenging mathematical reasoning tasks is achieved by true reasoning capability or memorization. Prior work has constructed mathematical benchmarks when questions undergo simple perturbations—modifications that preserve the underlying reasoning patterns of solutions—however no work has explored hard perturbations, which fundamentally change the nature of the problem so that the original solution steps do not apply.\n\n## Benchmark Components\n\nThe research constructs MATH-P-Simple and MATH-P-Hard via simple perturbation and hard perturbation, respectively, each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.\n\n## Key Results\n\nSignificant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).\n\n## Publication Details\n\nThe paper is accepted to ICML 2025 and is available as arXiv preprint arXiv:2502.06453. The corresponding GitHub repository contains evaluation code and the dataset."
    ],
    "durationSeconds": 7.549983827000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7736fbc1-2920-4104-9bac-471e4ba09418",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-29T06:19:04.339Z_

```json
{
  "parentUuid": "070238d9-2a3d-4ad3-ad2a-c6f0f6c118e7",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "720a4fe0-cbf0-498a-bea5-b5bee230a203",
  "timestamp": "2026-05-29T06:19:04.339Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-29T06:19:07.660Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0172ny3sS9Gm6bLgCf51xw2W`</summary>

```json
{
  "query": "F2C arXiv 2510.14242 flip-flop consistency JS divergence prompt perturbation robustness NLU experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "720a4fe0-cbf0-498a-bea5-b5bee230a203",
  "isSidechain": false,
  "requestId": "req_011CbWNgGazoaYqyL46p7Km8",
  "type": "assistant",
  "uuid": "5ddb6488-211b-4bae-b86e-c7d6a05f622e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Su1a4CveKTC4zExoVanNAY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 997,
      "cache_read_input_tokens": 24833,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 997,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 24833,
          "cache_creation_input_tokens": 997,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 997
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

_source line 31 · 2026-05-29T06:19:16.331Z_

<details><summary>↩ Tool result · `toolu_0172ny3sS9Gm6bLgCf51xw2W`</summary>

```text
Web search results for query: "F2C arXiv 2510.14242 flip-flop consistency JS divergence prompt perturbation robustness NLU experimental design"

Links: [{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/html/2510.14242v1"},{"title":"[2510.14242] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/abs/2510.14242"},{"title":"[2510.14242v1] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/abs/2510.14242v1"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs | Request PDF","url":"https://www.researchgate.net/publication/396541005_Flip-Flop_Consistency_Unsupervised_Training_for_Robustness_to_Prompt_Perturbations_in_LLMs"},{"title":"Flip-Flop Consistency: Unsupervised Training for ...","url":"https://arxiv.org/pdf/2510.14242"},{"title":"A non-negative expansion for small Jensen-Shannon Divergences","url":"https://arxiv.org/pdf/0810.5117"},{"title":"On the Jensen–Shannon Symmetrization of Distances Relying on Abstract Means","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7514974/"},{"title":"The Representation Jensen-Shannon Divergence","url":"https://arxiv.org/pdf/2305.16446"},{"title":"Dual-edge-triggered flip-flop","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12218669"}]

Based on the search results, I found the paper you're looking for. Here's what I found about arXiv 2510.14242:

## Flip-Flop Consistency (F2C) - arXiv 2510.14242

The paper addresses how Large Language Models often produce inconsistent answers when faced with different phrasings of the same prompt, and proposes Flip-Flop Consistency (F²C), an unsupervised training method that improves robustness to such perturbations.

**Method Overview:**

F²C is composed of two key components: the first, Consensus Cross-Entropy (CCE), uses a majority vote across prompt variations to create a hard pseudo-label, and the second is a representation alignment loss that pulls lower-confidence and non-majority predictors toward the consensus established by high-confidence, majority-voting variations.

The method minimizes the JS divergence among datapoints within the high-confidence consensus group, and the KL divergence between all other datapoints and that group.

**Experimental Results:**

The authors evaluate their method on 11 datasets spanning four NLP tasks, with 4-15 prompt variations per dataset, finding that on average, F²C raises observed agreement by 11.62%, improves mean F₁ by 8.94%, and reduces performance variance across formats by 3.29%.

When trained on only a subset of prompt perturbations and evaluated on held-out formats, F2C consistently improves both performance and agreement while reducing variance.

The paper was published on October 16, 2025, and code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ddb6488-211b-4bae-b86e-c7d6a05f622e",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "8fccdcac-d282-43a4-b5ec-92fe30014074",
  "toolUseResult": {
    "query": "F2C arXiv 2510.14242 flip-flop consistency JS divergence prompt perturbation robustness NLU experimental design",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GPakCEmnB7XbExkcpAd3YY",
        "content": [
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/html/2510.14242v1"
          },
          {
            "title": "[2510.14242] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/abs/2510.14242"
          },
          {
            "title": "[2510.14242v1] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/abs/2510.14242v1"
          },
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/396541005_Flip-Flop_Consistency_Unsupervised_Training_for_Robustness_to_Prompt_Perturbations_in_LLMs"
          },
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for ...",
            "url": "https://arxiv.org/pdf/2510.14242"
          },
          {
            "title": "A non-negative expansion for small Jensen-Shannon Divergences",
            "url": "https://arxiv.org/pdf/0810.5117"
          },
          {
            "title": "On the Jensen–Shannon Symmetrization of Distances Relying on Abstract Means",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7514974/"
          },
          {
            "title": "The Representation Jensen-Shannon Divergence",
            "url": "https://arxiv.org/pdf/2305.16446"
          },
          {
            "title": "Dual-edge-triggered flip-flop",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12218669"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found about arXiv 2510.14242:\n\n## Flip-Flop Consistency (F2C) - arXiv 2510.14242\n\nThe paper addresses how Large Language Models often produce inconsistent answers when faced with different phrasings of the same prompt, and proposes Flip-Flop Consistency (F²C), an unsupervised training method that improves robustness to such perturbations.\n\n**Method Overview:**\n\nF²C is composed of two key components: the first, Consensus Cross-Entropy (CCE), uses a majority vote across prompt variations to create a hard pseudo-label, and the second is a representation alignment loss that pulls lower-confidence and non-majority predictors toward the consensus established by high-confidence, majority-voting variations.\n\nThe method minimizes the JS divergence among datapoints within the high-confidence consensus group, and the KL divergence between all other datapoints and that group.\n\n**Experimental Results:**\n\nThe authors evaluate their method on 11 datasets spanning four NLP tasks, with 4-15 prompt variations per dataset, finding that on average, F²C raises observed agreement by 11.62%, improves mean F₁ by 8.94%, and reduces performance variance across formats by 3.29%.\n\nWhen trained on only a subset of prompt perturbations and evaluated on held-out formats, F2C consistently improves both performance and agreement while reducing variance.\n\nThe paper was published on October 16, 2025, and code is available on GitHub."
    ],
    "durationSeconds": 8.666465992000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5ddb6488-211b-4bae-b86e-c7d6a05f622e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-29T06:19:19.797Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019sUH3D9sJLsKY1DBMpQCH2`</summary>

```json
{
  "query": "math reasoning RL robustness GRPO consistency regularization 2026 latest methods baselines experimental comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fccdcac-d282-43a4-b5ec-92fe30014074",
  "isSidechain": false,
  "requestId": "req_011CbWNh9Qvm5eix9Bjcn3rD",
  "type": "assistant",
  "uuid": "773ae7f2-0923-48ed-b050-e03027ba4ecf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GS2foXJiUaK4qYNWwuCBUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 25830,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 25830,
          "cache_creation_input_tokens": 993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 993
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

_source line 33 · 2026-05-29T06:19:29.382Z_

<details><summary>↩ Tool result · `toolu_019sUH3D9sJLsKY1DBMpQCH2`</summary>

```text
Web search results for query: "math reasoning RL robustness GRPO consistency regularization 2026 latest methods baselines experimental comparison"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.17508"},{"title":"Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization","url":"https://arxiv.org/html/2509.21854"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=GP5RHZnEsw"},{"title":"Preprint. Under review DOES MATH REASONING IMPROVE GENERAL LLM","url":"https://arxiv.org/pdf/2507.00432"},{"title":"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/pdf/2601.03661"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models","url":"https://arxiv.org/pdf/2504.09696"},{"title":"CoRPO: Adding a Correctness Bias to GRPO Improves Generalization","url":"https://arxiv.org/pdf/2511.04439"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"},{"title":"VRPO: Rethinking Value Modeling for Robust RL Training under Noisy Supervision","url":"https://arxiv.org/html/2508.03058v1"}]

Based on the web search results, here are the latest methods, baselines, and experimental comparisons for math reasoning with RL, GRPO, consistency regularization, and robustness as of 2026:

## Key Latest Methods (2026)

**GRPO-Based Variants:**
AMIR-GRPO augments GRPO with an implicit DPO-style contrastive regularizer and consistently outperforms strong GRPO baselines across multiple mathematical reasoning benchmarks. CoRPO is a simple modification to the GRPO objective that clips the minimum baseline to a fixed correctness threshold, and empirically improves cross-domain reasoning for out-of-domain tasks.

DRA-GRPO demonstrates that diversity calibration is critical in data-efficient alignment, achieving 58.2% accuracy on DeepSeek-R1-Distill-Qwen-1.5B with only 7,000 training samples.

**Consistency & Robustness Methods:**
CapPO introduces caption-based consistency regularization, and both the caption-based KL regularization and KL-weighted advantage mechanism independently enhance reasoning capability. VRPO consistently outperforms both standard PPO and GRPO baselines in noisy supervision scenarios across math reasoning, science QA, and multi-turn dialogue tasks.

**Efficient Reasoning:**
DRPO decouples learning signals of correct and incorrect answers and integrates an optimized positive data distribution under KL regularization.

## Experimental Comparisons

Standard comparisons are conducted against baselines including GRPO, DAPO, and REINFORCE++. On-policy methods outperform off-policy methods across both evaluation categories, and when KL regularization is applied to RL, on-policy RL yields superior transferability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "773ae7f2-0923-48ed-b050-e03027ba4ecf",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "866a39ad-627a-4ee8-8693-d1d069de7f3b",
  "toolUseResult": {
    "query": "math reasoning RL robustness GRPO consistency regularization 2026 latest methods baselines experimental comparison",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BxVuWNoz8Kis3dxusiv33M",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2505.17508"
          },
          {
            "title": "Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization",
            "url": "https://arxiv.org/html/2509.21854"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=GP5RHZnEsw"
          },
          {
            "title": "Preprint. Under review DOES MATH REASONING IMPROVE GENERAL LLM",
            "url": "https://arxiv.org/pdf/2507.00432"
          },
          {
            "title": "AMIR-GRPO: Inducing Implicit Preference Signals into GRPO",
            "url": "https://arxiv.org/pdf/2601.03661"
          },
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2504.09696"
          },
          {
            "title": "CoRPO: Adding a Correctness Bias to GRPO Improves Generalization",
            "url": "https://arxiv.org/pdf/2511.04439"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          },
          {
            "title": "VRPO: Rethinking Value Modeling for Robust RL Training under Noisy Supervision",
            "url": "https://arxiv.org/html/2508.03058v1"
          }
        ]
      },
      "Based on the web search results, here are the latest methods, baselines, and experimental comparisons for math reasoning with RL, GRPO, consistency regularization, and robustness as of 2026:\n\n## Key Latest Methods (2026)\n\n**GRPO-Based Variants:**\nAMIR-GRPO augments GRPO with an implicit DPO-style contrastive regularizer and consistently outperforms strong GRPO baselines across multiple mathematical reasoning benchmarks. CoRPO is a simple modification to the GRPO objective that clips the minimum baseline to a fixed correctness threshold, and empirically improves cross-domain reasoning for out-of-domain tasks.\n\nDRA-GRPO demonstrates that diversity calibration is critical in data-efficient alignment, achieving 58.2% accuracy on DeepSeek-R1-Distill-Qwen-1.5B with only 7,000 training samples.\n\n**Consistency & Robustness Methods:**\nCapPO introduces caption-based consistency regularization, and both the caption-based KL regularization and KL-weighted advantage mechanism independently enhance reasoning capability. VRPO consistently outperforms both standard PPO and GRPO baselines in noisy supervision scenarios across math reasoning, science QA, and multi-turn dialogue tasks.\n\n**Efficient Reasoning:**\nDRPO decouples learning signals of correct and incorrect answers and integrates an optimized positive data distribution under KL regularization.\n\n## Experimental Comparisons\n\nStandard comparisons are conducted against baselines including GRPO, DAPO, and REINFORCE++. On-policy methods outperform off-policy methods across both evaluation categories, and when KL regularization is applied to RL, on-policy RL yields superior transferability."
    ],
    "durationSeconds": 9.58037752400001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "773ae7f2-0923-48ed-b050-e03027ba4ecf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem  RL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface pe…",
  "leafUuid": "866a39ad-627a-4ee8-8693-d1d069de7f3b",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "MACR: Math reasoning robustness via consistency regularization",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Tool call

_source line 36 · 2026-05-29T06:19:32.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016euTSF3WASKkRzkgcygbsh`</summary>

```json
{
  "query": "Qwen3-8B GRPO training compute cost GPU hours math reasoning reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "866a39ad-627a-4ee8-8693-d1d069de7f3b",
  "isSidechain": false,
  "requestId": "req_011CbWNi6zbfE2iMbCbodj7h",
  "type": "assistant",
  "uuid": "6381f539-e847-43db-bdb4-ec8c4554307e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kqJotS7xaSTsMRsb7UZeh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 26823,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 927,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26823,
          "cache_creation_input_tokens": 927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 927
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

_source line 37 · 2026-05-29T06:19:40.024Z_

<details><summary>↩ Tool result · `toolu_016euTSF3WASKkRzkgcygbsh`</summary>

```text
Web search results for query: "Qwen3-8B GRPO training compute cost GPU hours math reasoning reinforcement learning 2026"

Links: [{"title":"Qwen3-8b-base SFT+GRPO Training Report | My Blog","url":"https://dtianyou.com/en/notes/qwen3-8b-base-training/"},{"title":"Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models","url":"https://arxiv.org/pdf/2507.18014"},{"title":"Post Training Qwen3 for Math Reasoning Using GRPO - PyImageSearch","url":"https://pyimagesearch.com/2025/09/08/post-training-qwen3-for-math-reasoning-using-grpo/"},{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"Can A Gamer Train A Mathematical Reasoning Model?","url":"https://arxiv.org/html/2506.08935v1"},{"title":"The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU","url":"https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"}]

Based on the search results, here's what I found about Qwen3-8B GRPO training for math reasoning:

## Training Overview

The Qwen3-8b-base model has been trained with both SFT (Supervised Fine-tuning) and GRPO (Group-wise Reward Policy Optimization) to enhance performance on mathematical problem-solving, especially for the GSM8K and AIME24 datasets.

## GRPO Training Efficiency

Research across open-source models including Qwen has shown that GRPO reward curves display consistent three-phase patterns: slow initial progress, rapid improvement, and saturation. A key finding is that training beyond roughly 80% of a single epoch yields negligible reward gains while consuming substantial computation, and using scaling laws can help practitioners forecast phase transitions early and reduce GRPO compute without sacrificing final performance.

## Cost Perspective

GRPO optimizes LLMs more efficiently than traditional supervised fine-tuning by grouping training samples into batches and using a reward model to guide gradient updates, reducing GPU-hour requirements by orders of magnitude compared to conventional methods.

## Related Models

For context, DeepSeek-R1-Distill-Qwen3-8B was created by distilling chain-of-thought reasoning from the full DeepSeek-R1 model and applying it to fine-tune Qwen3-8B, using approximately 800,000 high-quality reasoning samples.

The search results don't contain specific GPU hour or exact cost figures for Qwen3-8B GRPO training, but they indicate that GRPO provides substantial efficiency gains over traditional methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6381f539-e847-43db-bdb4-ec8c4554307e",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "36c1c328-f572-452b-9c0f-6e829d8ea6ae",
  "toolUseResult": {
    "query": "Qwen3-8B GRPO training compute cost GPU hours math reasoning reinforcement learning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PXv1sHR1muEgJooj5eRetn",
        "content": [
          {
            "title": "Qwen3-8b-base SFT+GRPO Training Report | My Blog",
            "url": "https://dtianyou.com/en/notes/qwen3-8b-base-training/"
          },
          {
            "title": "Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2507.18014"
          },
          {
            "title": "Post Training Qwen3 for Math Reasoning Using GRPO - PyImageSearch",
            "url": "https://pyimagesearch.com/2025/09/08/post-training-qwen3-for-math-reasoning-using-grpo/"
          },
          {
            "title": "Top 10 Open-source Reasoning Models in 2026",
            "url": "https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"
          },
          {
            "title": "Can A Gamer Train A Mathematical Reasoning Model?",
            "url": "https://arxiv.org/html/2506.08935v1"
          },
          {
            "title": "The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU",
            "url": "https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl"
          },
          {
            "title": "Qwen/Qwen3-8B · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen3-8B"
          }
        ]
      },
      "Based on the search results, here's what I found about Qwen3-8B GRPO training for math reasoning:\n\n## Training Overview\n\nThe Qwen3-8b-base model has been trained with both SFT (Supervised Fine-tuning) and GRPO (Group-wise Reward Policy Optimization) to enhance performance on mathematical problem-solving, especially for the GSM8K and AIME24 datasets.\n\n## GRPO Training Efficiency\n\nResearch across open-source models including Qwen has shown that GRPO reward curves display consistent three-phase patterns: slow initial progress, rapid improvement, and saturation. A key finding is that training beyond roughly 80% of a single epoch yields negligible reward gains while consuming substantial computation, and using scaling laws can help practitioners forecast phase transitions early and reduce GRPO compute without sacrificing final performance.\n\n## Cost Perspective\n\nGRPO optimizes LLMs more efficiently than traditional supervised fine-tuning by grouping training samples into batches and using a reward model to guide gradient updates, reducing GPU-hour requirements by orders of magnitude compared to conventional methods.\n\n## Related Models\n\nFor context, DeepSeek-R1-Distill-Qwen3-8B was created by distilling chain-of-thought reasoning from the full DeepSeek-R1 model and applying it to fine-tune Qwen3-8B, using approximately 800,000 high-quality reasoning samples.\n\nThe search results don't contain specific GPU hour or exact cost figures for Qwen3-8B GRPO training, but they indicate that GRPO provides substantial efficiency gains over traditional methods."
    ],
    "durationSeconds": 7.856976781000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6381f539-e847-43db-bdb4-ec8c4554307e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-29T06:19:43.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015GocoiyTPeZt8EmNAdnfEh`</summary>

```json
{
  "query": "SymPy symbolic perturbation math problem generation coverage limitations geometry combinatorics number theory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36c1c328-f572-452b-9c0f-6e829d8ea6ae",
  "isSidechain": false,
  "requestId": "req_011CbWNiteUif76KUtWYHh4N",
  "type": "assistant",
  "uuid": "53904991-90ef-4cc2-9c05-c84059dbf68a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TS9YxyYGfkLtebduduCb87",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 27750,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 27750,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
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

_source line 39 · 2026-05-29T06:19:52.697Z_

<details><summary>↩ Tool result · `toolu_015GocoiyTPeZt8EmNAdnfEh`</summary>

```text
Web search results for query: "SymPy symbolic perturbation math problem generation coverage limitations geometry combinatorics number theory"

Links: [{"title":"SymPy: A Complete Guide to Symbolic Mathematics in Python | DataCamp","url":"https://www.datacamp.com/tutorial/sympy"},{"title":"Sympy — MEM T680: Fall 2022: Data Analysis and Machine Learning","url":"https://courses.coe.drexel.edu/MEM/MEMT680/Topic_5/SymPy/SymPy.html"},{"title":"SymPy - Symbolic Computation","url":"https://www.tutorialspoint.com/sympy/sympy_symbolic_computation.htm"},{"title":"Introduction - SymPy 1.14.0 documentation","url":"https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html"},{"title":"SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation","url":"https://arxiv.org/pdf/2510.25975"},{"title":"SymPy - Quick Guide","url":"https://www.tutorialspoint.com/sympy/sympy_quick_guide.htm"},{"title":"PeerJ SymPy: symbolic computing in Python","url":"https://peerj.com/articles/cs-103/"},{"title":"Towards Generating Controllable and Solvable Geometry Problem by Leveraging Symbolic Deduction Engine","url":"https://arxiv.org/pdf/2506.02565"},{"title":"(PDF) SymPy: Symbolic computing in Python","url":"https://www.researchgate.net/publication/345840132_SymPy_Symbolic_computing_in_Python"},{"title":"A deterministic pseudorandom perturbation scheme for arbitrary   polynomial predicates","url":"https://arxiv.org/pdf/1308.1986"}]

Based on the web search results, here's what I found regarding SymPy and its capabilities across different mathematical domains:

## SymPy's Coverage

SymPy includes modules for plotting, printing (like 2D pretty printed output of math formulas, or LaTeX), code generation, physics, statistics, combinatorics, number theory, geometry, logic, and more.

More specifically:

**Combinatorics and Number Theory:** SymPy has several utilities that enable it to handle combinatorial and number-theoretic problems. For example, the binomial(5, 2) function calculates the number of ways to choose 2 items from 5 (a combination problem), factorial(6) computes 6!, a common operation in permutations.

**Geometry:** Supported facilities include discrete math, concrete math, plotting, geometry, statistics, sets, series, vectors, combinatorics, group theory, code generation, tensors, Lie algebras, cryptography, and special functions.

**Advanced Capabilities:** SymPy can simplify expressions, compute derivatives, integrals, and limits, solve equations, work with matrices, and much, much more, and do it all symbolically.

## Math Problem Generation

The search results do reference a framework called Symbolic Deduction Engine-based Geometry Problem Generation (SDE-GPG), which leverages a symbolic deduction engine and contains four main steps: searching a predefined mapping table from knowledge points to extended definitions, sampling extended definitions and performing symbolic deduction, filtering out unqualified problems, and generating textual problems and diagrams.

However, the search results do not contain specific information about coverage limitations of SymPy for symbolic perturbation methods in math problem generation across these domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53904991-90ef-4cc2-9c05-c84059dbf68a",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "06cb41a8-811b-4f25-a5a9-b46315cb29d4",
  "toolUseResult": {
    "query": "SymPy symbolic perturbation math problem generation coverage limitations geometry combinatorics number theory",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WqJX38MAPsUYgAic63Rg3Q",
        "content": [
          {
            "title": "SymPy: A Complete Guide to Symbolic Mathematics in Python | DataCamp",
            "url": "https://www.datacamp.com/tutorial/sympy"
          },
          {
            "title": "Sympy — MEM T680: Fall 2022: Data Analysis and Machine Learning",
            "url": "https://courses.coe.drexel.edu/MEM/MEMT680/Topic_5/SymPy/SymPy.html"
          },
          {
            "title": "SymPy - Symbolic Computation",
            "url": "https://www.tutorialspoint.com/sympy/sympy_symbolic_computation.htm"
          },
          {
            "title": "Introduction - SymPy 1.14.0 documentation",
            "url": "https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html"
          },
          {
            "title": "SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation",
            "url": "https://arxiv.org/pdf/2510.25975"
          },
          {
            "title": "SymPy - Quick Guide",
            "url": "https://www.tutorialspoint.com/sympy/sympy_quick_guide.htm"
          },
          {
            "title": "PeerJ SymPy: symbolic computing in Python",
            "url": "https://peerj.com/articles/cs-103/"
          },
          {
            "title": "Towards Generating Controllable and Solvable Geometry Problem by Leveraging Symbolic Deduction Engine",
            "url": "https://arxiv.org/pdf/2506.02565"
          },
          {
            "title": "(PDF) SymPy: Symbolic computing in Python",
            "url": "https://www.researchgate.net/publication/345840132_SymPy_Symbolic_computing_in_Python"
          },
          {
            "title": "A deterministic pseudorandom perturbation scheme for arbitrary   polynomial predicates",
            "url": "https://arxiv.org/pdf/1308.1986"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding SymPy and its capabilities across different mathematical domains:\n\n## SymPy's Coverage\n\nSymPy includes modules for plotting, printing (like 2D pretty printed output of math formulas, or LaTeX), code generation, physics, statistics, combinatorics, number theory, geometry, logic, and more.\n\nMore specifically:\n\n**Combinatorics and Number Theory:** SymPy has several utilities that enable it to handle combinatorial and number-theoretic problems. For example, the binomial(5, 2) function calculates the number of ways to choose 2 items from 5 (a combination problem), factorial(6) computes 6!, a common operation in permutations.\n\n**Geometry:** Supported facilities include discrete math, concrete math, plotting, geometry, statistics, sets, series, vectors, combinatorics, group theory, code generation, tensors, Lie algebras, cryptography, and special functions.\n\n**Advanced Capabilities:** SymPy can simplify expressions, compute derivatives, integrals, and limits, solve equations, work with matrices, and much, much more, and do it all symbolically.\n\n## Math Problem Generation\n\nThe search results do reference a framework called Symbolic Deduction Engine-based Geometry Problem Generation (SDE-GPG), which leverages a symbolic deduction engine and contains four main steps: searching a predefined mapping table from knowledge points to extended definitions, sampling extended definitions and performing symbolic deduction, filtering out unqualified problems, and generating textual problems and diagrams.\n\nHowever, the search results do not contain specific information about coverage limitations of SymPy for symbolic perturbation methods in math problem generation across these domains."
    ],
    "durationSeconds": 8.749850932999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "53904991-90ef-4cc2-9c05-c84059dbf68a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-29T06:19:55.443Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A8hL72A3je61TUNwJdgryD`</summary>

```json
{
  "query": "\"teacher forcing\" trajectory translation math reasoning consistency loss token-level divergence perturbation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06cb41a8-811b-4f25-a5a9-b46315cb29d4",
  "isSidechain": false,
  "requestId": "req_011CbWNjpgdZ9GxuXKrrTTPw",
  "type": "assistant",
  "uuid": "645ede68-2c13-48ad-8751-1cba40695224",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwyTgDC5TkVxBSBHM11XK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 28605,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 943,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 28605,
          "cache_creation_input_tokens": 943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 943
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

_source line 41 · 2026-05-29T06:20:08.164Z_

<details><summary>↩ Tool result · `toolu_01A8hL72A3je61TUNwJdgryD`</summary>

```text
Web search results for query: ""teacher forcing" trajectory translation math reasoning consistency loss token-level divergence perturbation 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2507.07982"},{"title":"Contrastive Student-Forcing Loss (CSFL)","url":"https://www.emergentmind.com/topics/contrastive-student-forcing-loss-csfl"},{"title":"Published as a conference paper at ICLR 2025 LEARNING TO DISCRETIZE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/750046157471c56235a781f2eff6e226-Paper-Conference.pdf"},{"title":"Mixed Cross Entropy Loss for Neural Machine Translation","url":"https://arxiv.org/pdf/2106.15880"},{"title":"Elucidating the Preconditioning in Consistency Distillation","url":"https://arxiv.org/pdf/2502.02922"},{"title":"generalized consistency trajectory models","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/986e0caad271b59417287737416d8594-Paper-Conference.pdf"}]

The web search found some relevant recent papers from 2025-2026. Let me search more specifically for the mathematical reasoning and token-level divergence aspects you mentioned.

Links: [{"title":"Preprint. Under review DOES MATH REASONING IMPROVE GENERAL LLM","url":"https://arxiv.org/pdf/2507.00432"},{"title":"Preprint DISTILLING REASONING INTO STUDENT LLMS: LO-","url":"https://www.arxiv.org/pdf/2510.03988"},{"title":"Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM Reasoning","url":"https://arxiv.org/html/2507.00432v1"},{"title":"Looking beyond the next token","url":"https://arxiv.org/html/2504.11336v1"},{"title":"Beyond Multi-Token Prediction: Pretraining LLMs with Future Summaries","url":"https://arxiv.org/html/2510.14751"},{"title":"R2R: Efficiently Navigating Divergent Reasoning Paths ...","url":"https://arxiv.org/pdf/2505.21600"},{"title":"When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning","url":"https://arxiv.org/html/2605.21606"},{"title":"BEYOND MULTI-TOKEN PREDICTION: PRETRAINING LLMS ...","url":"https://openreview.net/pdf/2365655cddc93c8a064e077a9da6948d8b5e76e6.pdf"}]

I've conducted web searches on your query about teacher forcing, trajectory translation, math reasoning, consistency loss, and token-level divergence perturbation in recent 2025-2026 research. Here's what I found:

## Key Research Areas

**Teacher Forcing and Trajectory Consistency:**
Recent work has introduced Contrastive Student-Forcing Loss (CSFL) which ties student-forced and teacher-forced outputs together by retrospectively aligning SF outputs with their TF counterparts, thus maintaining consistency along student-generated contexts.

**Math Reasoning and Token-Level Analysis:**
Research has conducted token-level analyses to examine the distribution shift of RL and SFT models trained on mathematical reasoning data, employing token-distribution analyses to assess the model distribution shift from a token-space perspective. These analyses specifically employ KL-divergence and token rank shift metrics to analyze distribution shifts between models.

**Teacher Forcing Perturbation:**
Recent methods proposed to alleviate teacher forcing issues include multi-token prediction approaches and methods that modify the training objective to predict both the next token for a prefix and the previous token for a suffix. Some approaches reduce teacher forcing by requiring the model to reason about rich, global properties of the target trajectory.

**Advanced Distillation Techniques:**
Recent privileged distillation methods include EOPD which applies forward KL on high-teacher-entropy tokens while retaining reverse KL elsewhere in on-policy distillation, and REOPOLD which interprets on-policy distillation as policy optimization with a teacher-student log-likelihood-ratio token reward.

These represent the most recent research (2025-2026) addressing the interconnected topics of teacher forcing, trajectory consistency, and token-level analysis in the context of math reasoning and model distillation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "645ede68-2c13-48ad-8751-1cba40695224",
  "isSidechain": false,
  "promptId": "25d3d564-a8b0-481b-ad43-ae2fa7ca8e44",
  "type": "user",
  "uuid": "f1a72424-7b7b-4ed3-9642-c128030aca9a",
  "toolUseResult": {
    "query": "\"teacher forcing\" trajectory translation math reasoning consistency loss token-level divergence perturbation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XvwfjwHHGBhUPk2JecugZb",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2507.07982"
          },
          {
            "title": "Contrastive Student-Forcing Loss (CSFL)",
            "url": "https://www.emergentmind.com/topics/contrastive-student-forcing-loss-csfl"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 LEARNING TO DISCRETIZE",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/750046157471c56235a781f2eff6e226-Paper-Conference.pdf"
          },
          {
            "title": "Mixed Cross Entropy Loss for Neural Machine Translation",
            "url": "https://arxiv.org/pdf/2106.15880"
          },
          {
            "title": "Elucidating the Preconditioning in Consistency Distillation",
            "url": "https://arxiv.org/pdf/2502.02922"
          },
          {
            "title": "generalized consistency trajectory models",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/986e0caad271b59417287737416d8594-Paper-Conference.pdf"
          }
        ]
      },
      "The web search found some relevant recent papers from 2025-2026. Let me search more specifically for the mathematical reasoning and token-level divergence aspects you mentioned.",
      {
        "tool_use_id": "srvtoolu_01UBMayAt8etLu9h1n9nxwBR",
        "content": [
          {
            "title": "Preprint. Under review DOES MATH REASONING IMPROVE GENERAL LLM",
            "url": "https://arxiv.org/pdf/2507.00432"
          },
          {
            "title": "Preprint DISTILLING REASONING INTO STUDENT LLMS: LO-",
            "url": "https://www.arxiv.org/pdf/2510.03988"
          },
          {
            "title": "Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM Reasoning",
            "url": "https://arxiv.org/html/2507.00432v1"
          },
          {
            "title": "Looking beyond the next token",
            "url": "https://arxiv.org/html/2504.11336v1"
          },
          {
            "title": "Beyond Multi-Token Prediction: Pretraining LLMs with Future Summaries",
            "url": "https://arxiv.org/html/2510.14751"
          },
          {
            "title": "R2R: Efficiently Navigating Divergent Reasoning Paths ...",
            "url": "https://arxiv.org/pdf/2505.21600"
          },
          {
            "title": "When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning",
            "url": "https://arxiv.org/html/2605.21606"
          },
          {
            "title": "BEYOND MULTI-TOKEN PREDICTION: PRETRAINING LLMS ...",
            "url": "https://openreview.net/pdf/2365655cddc93c8a064e077a9da6948d8b5e76e6.pdf"
          }
        ]
      },
      "I've conducted web searches on your query about teacher forcing, trajectory translation, math reasoning, consistency loss, and token-level divergence perturbation in recent 2025-2026 research. Here's what I found:\n\n## Key Research Areas\n\n**Teacher Forcing and Trajectory Consistency:**\nRecent work has introduced Contrastive Student-Forcing Loss (CSFL) which ties student-forced and teacher-forced outputs together by retrospectively aligning SF outputs with their TF counterparts, thus maintaining consistency along student-generated contexts.\n\n**Math Reasoning and Token-Level Analysis:**\nResearch has conducted token-level analyses to examine the distribution shift of RL and SFT models trained on mathematical reasoning data, employing token-distribution analyses to assess the model distribution shift from a token-space perspective. These analyses specifically employ KL-divergence and token rank shift metrics to analyze distribution shifts between models.\n\n**Teacher Forcing Perturbation:**\nRecent methods proposed to alleviate teacher forcing issues include multi-token prediction approaches and methods that modify the training objective to predict both the next token for a prefix and the previous token for a suffix. Some approaches reduce teacher forcing by requiring the model to reason about rich, global properties of the target trajectory.\n\n**Advanced Distillation Techniques:**\nRecent privileged distillation methods include EOPD which applies forward KL on high-teacher-entropy tokens while retaining reverse KL elsewhere in on-policy distillation, and REOPOLD which interprets on-policy distillation as policy optimization with a teacher-student log-likelihood-ratio token reward.\n\nThese represent the most recent research (2025-2026) addressing the interconnected topics of teacher forcing, trajectory consistency, and token-level analysis in the context of math reasoning and model distillation."
    ],
    "durationSeconds": 12.71597114400001,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "645ede68-2c13-48ad-8751-1cba40695224",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-29T06:21:06.605Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have gathered sufficient research context. Let me synthesize my findings and evaluate the experimental design of this proposal.

Key findings from my research:

1. **TA-GRPO**: Uses cross-variant pooled advantages, evaluates on competition math (AMC12, AIME24) and GPQA-Diamond. No explicit robustness evaluation protocol.

2. **AbstRaL**: Evaluates on GSM-Symbolic and GSM-Plus for robustness. Uses SFT + RL pipeline. Tested on GSM8K variants but not competition-level math perturbation benchmarks like VAR-MATH.
   
3. **ROMA**: Applies token-level KL regularization between corrupted and clean trajectories, tested across seven multimodal reasoning benchmarks with correctness-conditioned constraints.

4. **COPO**: Tackles the zero-advantage problem through a consistency-entropy mechanism on math reasoning tasks.

5. **VAR-MATH**: Uses parameterized templates with multiple instantiations and tracks consistency rate as the primary metric.

6. **MATH-Perturb**: Contains 279 level-5 problems with separate simple and hard perturbation variants.

7. **GC²PO**: Employs episodic causal counterfactual rewards for reasoning generation.

8. **F2C**: Measures JavaScript-based consistency for NLU tasks using SFT-only training, tracking agreement and F1 scores.

Looking at the experimental design, I'm seeing solid coverage with seven baseline tiers, compute-normalized comparisons, and thorough ablations across ten components. The evaluation spans multiple benchmarks for robustness and out-of-distribution performance, with stratified per-topic analysis accounting for SymPy limitations. Three-seed evaluation with sensitivity checks seems reasonable. But I'm flagging a concern about baseline reproduction—the proposal mentions reproducing AbstRaL on Qwen3-8B only "if feasible," which is problematic since this is a key baseline.

The bigger issue is that AbstRaL was originally tested on Llama-3 and Qwen2, not Qwen3-8B, so if they can't reproduce it, comparing across different model families weakens the comparison significantly. COPO is listed as a baseline but needs clearer specification on how it's adapted for perturbation augmentation—COPO was designed for vanilla GRPO's zero-advantage problem, not cross-perturbation consistency, so the proposal should explicitly detail whether COPO receives the same augmented data. Most critically, T3F is the core novelty but there's no validation plan for whether trajectory translation is actually producing high-quality results—they need a concrete metric or validation step to verify this.

For the perturbation types where T3F doesn't work well, like expression rewriting and constraint reformulation, the proposal falls back to rollout-level outcome consistency, which represents a significant portion of the training data. The ablation comparing T3F versus rollout-level exists, but there's no clear experimental protocol showing what fraction of training uses each approach or whether the fallback signal is strong enough. The contrastive discrimination loss uses hard negatives from SymPy answer-changing perturbations, but the ablation studies only compare with and without the contrastive component without deeper analysis of its contribution.

I'm also noticing there's no explicit evaluation of whether the contrastive loss actually prevents the degenerate invariance problem it's designed to address—I'd need a specific metric or test to measure that. The vanilla consistency baseline using F2C-style generic JavaScript consistency applied to GRPO is useful for isolating the value of math-aware design, but the specific adaptation of F2C to GRPO needs clearer specification since F2C was originally SFT-only. The compute estimate of 40-80 GPU-hours per run on 8×A100 for Qwen3-8B GRPO seems reasonable, but that's a wide range, and with T3F adding extra forward passes, I should estimate the compute overhead for MACR more precisely.

The proposal mentions a "2-3x compute budget" for the compute-normalized baseline without justifying it—I need to count exactly how many additional forward passes T3F requires. Beyond that, reporting mean ± std across 3 seeds is standard, but the key claims, especially around the "both-correct regime" advantage, should have explicit statistical testing like paired t-tests or bootstrap confidence intervals rather than just summary statistics. Most critically, the core claim that TA-GRPO's signal diminishes in the both-correct regime while MACR's SAC provides gradient needs direct empirical validation—I should measure what fraction of training pairs actually fall into the both-correct regime at different training stages and quantify the actual gradient signal in each case.

For the OlympiadBench and Minerva evaluations, the proposal is vague about which specific subsets are used and what the evaluation protocol looks like. I'm also noticing that several recent GRPO variants like CoRPO and DRA-GRPO appear relevant but aren't discussed as baselines—the proposal should either include them or explicitly justify why the current baseline selection is sufficient.

Actually, I need to step back here. MACR's core contribution is about perturbation robustness specifically, not general math reasoning improvement, so I should evaluate baselines through that lens rather than treating all recent methods as equally relevant. Looking at the seven-tier baseline structure—from no RL up through standard RL, zero-advantage fixes, augmentation approaches, structural abstraction, generic consistency methods, and finally the full approach—it actually covers the robustness space quite comprehensively.

GC²PO could potentially fill a gap as a counterfactual-based baseline, but its focus on within-problem causal robustness is fundamentally different from cross-problem perturbation invariance, so it might not be a direct apples-to-apples comparison.

On feasibility, the compute budget of 1,500-3,000 A100 GPU-hours is substantial but realistic for a well-resourced team—roughly 6-12 days on an 8×A100 cluster running continuously. The real challenge is engineering the SymPy perturbation generator to achieve broad coverage across MATH problem types, which the proposal acknowledges but doesn't fully quantify in terms of engineering effort.

The T3F implementation pipeline with trajectory translation and teacher forcing is novel and untested, which introduces real risks around handling variable-length sequences, ensuring the regex-based masking works correctly, and managing edge cases in the SymPy mapping. None of these feel fatal, but they're all potential friction points that need careful validation.

The core issue I keep coming back to is that the "both-correct regime" claim—the paper's central motivating insight—lacks direct empirical validation. Without demonstrating that this regime actually exists and matters in practice, the entire argument rests on an unproven assumption.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1a72424-7b7b-4ed3-9642-c128030aca9a",
  "isSidechain": false,
  "requestId": "req_011CbWNkxnZsHxwxquRHKDMw",
  "type": "assistant",
  "uuid": "90795fa1-5eba-4da2-bebd-fd1457829aab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QUgYb9aTJp1KfS3GysmJ1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 29548,
      "output_tokens": 7394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7394,
          "cache_read_input_tokens": 29548,
          "cache_creation_input_tokens": 1186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1186
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

_source line 43 · 2026-05-29T06:22:56.453Z_

Now I have sufficient research context. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **TA-GRPO (arXiv 2601.22478)**: 使用跨变体池化advantage，评估指标为Pass@k（AMC12, AIME24, GPQA-Diamond），未做显式鲁棒性评估（无RPD/consistency rate），无ablation隔离augmentation vs. invariance贡献。
- **AbstRaL (ICLR 2026, arXiv 2506.07751)**: 在GSM-Symbolic和GSM-Plus上评估robustness（数值变体、问题改写、干扰项插入），基座模型为Llama-3/Qwen2（非Qwen3），仅在GSM级别验证，未测试competition-level math。
- **ROMA (arXiv 2605.09262)**: 双forward-pass + teacher forcing，correctness-conditioned token-level KL，在Qwen3-VL 4B/8B上评估7个多模态benchmark，报告seen/unseen corruption的增益。实验中包含了compute overhead分析。
- **COPO (arXiv 2508.04138)**: consistency-entropy advantage重设计，解决zero-advantage问题，在数学推理任务上做了extensive ablation（包括与多种GRPO改进的交叉对比）。
- **VAR-MATH (arXiv 2507.12885)**: 参数化模板 + 多实例评估，核心指标为consistency rate和bootstrapped metrics，评估25个模型，发现sub-frontier模型47-73%下降。
- **MATH-Perturb (ICML 2025, arXiv 2502.06453)**: 279道Level-5题，区分Simple（保solution）和Hard（改solution）扰动，提供了GitHub评测代码。
- **GC²PO (arXiv 2602.06475)**: episodic因果反事实奖励，评估reasoning step的robustness和effectiveness，使用token-level advantage。
- **F2C (arXiv 2510.14242)**: JS-based consistency，SFT-only，11个NLU数据集，指标包括observed agreement、mean F1、performance variance。
- **GRPO compute scaling (arXiv 2507.18014)**: GRPO训练呈三阶段模式，超过约80% epoch后收益递减；Qwen3-8B GRPO训练实践已有开源教程参考。

- **调研总结**: 该领域当前实验设计标准要求：(1) 多层级baseline对比（vanilla → standard RL → augmentation → full method）；(2) 在多个robustness benchmark上报告RPD和consistency rate（不仅仅是clean accuracy）；(3) compute-normalized fairness control；(4) 细粒度ablation隔离每个组件贡献。审稿人普遍期望看到：核心claim有直接的实证支撑（不仅仅是end-to-end数字），以及对方法局限性的诚实量化。

---

【缺陷 1】
- 类别: 实验设计不足
- 问题: Proposal的核心motivating claim是"both-correct regime下TA-GRPO的advantage信号趋近于零，而MACR的SAC loss仍提供有效梯度"。这是整篇论文最关键的差异化论点，但实验设计中**没有任何直接验证该claim的实验**。当前设计只有end-to-end的accuracy/robustness对比（A2 vs. A5/A6），无法证明改进确实来源于both-correct regime的信号补充，而非其他因素（如regularization的泛化效果）。
- 严重度: 可补救
- 补救方案: 增加一组**训练动态分析实验**（training dynamics analysis），具体包括：(1) 在训练过程中track "both-correct pairs"占所有pair的比例随训练步数的变化曲线（预期应单调上升）；(2) 对比TA-GRPO和MACR在both-correct regime下的有效梯度范数（TA-GRPO应≈0，MACR的SAC loss应>0）；(3) 将验证集按"both-correct"和"mixed-correctness"分层，分别报告两组方法在各层的robustness改进幅度。如果MACR的优势确实集中在both-correct层，该claim即获得直接支撑。此实验无需额外训练run，只需在现有训练过程中插入logging。
- 调研依据: COPO (arXiv 2508.04138) 在其实验中专门分析了zero-advantage样本比例及其对训练信号的影响，这种training dynamics分析在该领域是审稿人期望看到的实证标准。

【缺陷 2】
- 类别: baseline 不足或过时
- 问题: AbstRaL (tier 5) 的baseline处理方式存在显著不确定性。Proposal写"reproduce on Qwen3-8B if feasible, otherwise use published results on shared benchmarks with explicit model-gap discussion"。AbstRaL原文使用Llama-3/Qwen2，而MACR使用Qwen3-8B——跨model family的published results对比在审稿中几乎不被接受为公平比较（不同model family的base capability差异可能远大于方法本身的差异）。这是7个baseline tier中唯一一个可能无法实现同模型对比的tier，而它恰恰是最直接的competitor（同样声称解决perturbation robustness问题）。
- 严重度: 可补救
- 补救方案: 将AbstRaL复现定为**必选项**而非optional。AbstRaL的核心机制（训练模型先抽象再求解）并不依赖特定model architecture，技术上应可在Qwen3-8B上复现。建议：(1) 在实验计划中预留AbstRaL复现的compute budget（约3 runs × 3 seeds = 9 runs ≈ 360-720 A100 GPU-hours）；(2) 如果完全复现其RL pipeline有困难，至少实现其核心机制（abstraction prompt + RL reward for abstraction quality）的simplified version on Qwen3-8B；(3) 同时报告AbstRaL在competition-level robustness benchmarks（VAR-MATH, MATH-P-Simple）上的结果——这是AbstRaL原文未覆盖的场景，如果MACR在此处显著优于AbstRaL，将是一个很强的differentiator。
- 调研依据: AbstRaL原文 (arXiv 2506.07751) 仅在GSM级别验证robustness，未测试competition-level math benchmarks，存在evaluation gap可供MACR利用。

【缺陷 3】
- 类别: 实验设计不足
- 问题: T3F（Trajectory-Translated Teacher Forcing）是本文的**核心技术创新**，但实验设计中缺少对trajectory translation质量本身的验证。Translation的假设是：SymPy mapping可以精确地将正确的原始trajectory转化为对perturbed问题同样合理的trajectory。但这个假设可能在多种情况下失效——例如当original trajectory的推理路径依赖于特定数值的性质（如2是质数、7是奇数等），translation后的数值可能不再具有相同性质，导致translated trajectory逻辑上不再成立。
- 严重度: 可补救
- 补救方案: 增加**T3F translation quality audit**：(1) 随机抽样100-200对translated trajectories，检查translation后trajectory的逻辑正确性（可用模型自动判断+人工抽检）；(2) 报告translation success rate（translated trajectory导致正确答案的比例）作为方法前提的验证；(3) 在ablation中加入一个variant：只在translation验证成功的pair上应用SAC loss（vs. 在所有pair上应用），量化translation质量对最终性能的影响。此审计可以在正式训练前在一个small batch上完成。
- 调研依据: ROMA (arXiv 2605.09262) 的teacher forcing方法之所以work，是因为visual perturbation保证了同一trajectory对两种view都valid。Math setting下这个保证不存在，需要显式验证。基于领域实验规范判断，审稿人对novel mechanism的validity要求有direct evidence，不能仅靠assumption。

【缺陷 4】
- 类别: ablation 不完整
- 问题: 当前ablation A5 vs. A6 比较的是"有contrastive loss"和"无contrastive loss"，但**没有实验验证contrastive loss实际解决了它声称要解决的问题（degenerate invariance）**。即：如果不加contrastive loss，模型是否真的会学到degenerate invariance（对语义不同的问题也产生相同reasoning）？这需要直接的实证，否则contrastive component的motivation是hollow的。
- 严重度: 可补救
- 补救方案: 增加**degenerate invariance测试**：(1) 构造一个diagnostic test set，包含surface-similar但answer-different的问题对（可直接复用contrastive loss的hard negative构造方法）；(2) 对比A5（无contrastive）和A6（有contrastive）在此test set上的"错误一致性率"（模型对两个semantically different问题给出相同错误答案的比例）；(3) 如果A5确实表现出更高的degenerate invariance，contrastive loss的contribution就有了直接实证支撑。这个diagnostic test不需要额外training，只需要inference。
- 调研依据: 基于领域实验规范判断。在consistency regularization文献中（F2C, ROMA等），通常需要证明regularization不会导致over-regularization或collapse，审稿人对"防止什么问题"的claim普遍要求direct evidence。

【缺陷 5】
- 类别: compute 公平性问题
- 问题: Compute-normalized comparison设计为"Standard GRPO with 2-3x compute budget"，但"2-3x"是一个较大的范围，且没有明确说明MACR相对于standard GRPO的实际compute overhead是多少。T3F需要两次额外的teacher-forced forward pass（对original和perturbed），contrastive loss需要额外的hard negative构造和forward pass。Proposal应该精确计算overhead multiplier，然后给standard GRPO匹配相同的compute（不是一个模糊的范围）。
- 严重度: 可补救
- 补救方案: (1) 精确计算MACR的compute overhead：额外的forward pass次数 × 每次forward pass相对于一次rollout的cost比例。T3F的teacher-forced forward pass（无autoregressive generation）比rollout cheap很多（因为无序列生成，只需要一次前向传播），应明确这一点；(2) 将compute-normalized baseline调整为精确匹配的multiplier（如MACR总compute是standard GRPO的1.6x，则给standard GRPO也1.6x compute，通过增加training steps或增加rollout数量实现）；(3) 考虑两种compute-matching strategy（more steps vs. more rollouts per step），报告两者中的best result作为fairness baseline。
- 调研依据: ROMA (arXiv 2605.09262) 在实验中包含了compute overhead分析，这是consistency regularization方法的审稿人常见质疑点。

【缺陷 6】
- 类别: 评估方案缺陷
- 问题: Proposal中列出了多个评估benchmark和指标，但缺少**统计显著性检验**的计划。当前只提到"mean ± std over 3 seeds"，但对于核心claim（MACR vs. TA-GRPO, MACR vs. AbstRaL），3个seed的mean ± std在robustness metrics上可能不足以区分显著性——尤其是VAR-MATH (279个template × multiple instantiations) 和 MATH-P-Simple (279 problems) 这种中等规模test set上，variance可能较大。
- 严重度: 可补救
- 补救方案: (1) 对核心baseline对比（尤其是MACR vs. TA-GRPO, MACR vs. COPO, MACR vs. AbstRaL）使用paired bootstrap test或paired permutation test报告p-value；(2) 对于seed数量有限的情况，利用benchmark本身的template/problem级别variance做bootstrap（e.g., VAR-MATH的每个template有多个instantiation，可以做template-level bootstrap）；(3) 在结果表格中标注统计显著性（* p<0.05, ** p<0.01）。这是reviewer的standard要求，不增加实验cost。
- 调研依据: GSM-Symbolic (ICLR 2025) 和 VAR-MATH (arXiv 2507.12885) 都使用了bootstrapped metrics来确保评估可靠性，该领域审稿人对统计显著性有明确期望。

【缺陷 7】
- 类别: 可行性问题
- 问题: SymPy perturbation generator的**覆盖率不确定性**是一个实际执行风险。Proposal承认SymPy对geometry/combinatorics/number theory覆盖有限，并提出LLM-based perturbation + majority-vote verification作为fallback。但：(a) LLM-based perturbation的质量和equivalence保证远弱于SymPy（majority vote不能保证mathematical equivalence，只能做probabilistic verification）；(b) 如果SymPy覆盖率低于预期（如MATH训练集中algebra/equations只占40-50%），则大量训练数据无法应用T3F，方法的实际影响力大打折扣。
- 严重度: 可补救
- 补救方案: (1) **在实验启动前**先运行SymPy perturbation generator在完整训练集上做一次coverage audit，报告per-topic coverage rate（这个可以在1天内完成，应作为go/no-go gate）；(2) 如果coverage低于60%，需要考虑更aggressive的LLM perturbation strategy或者缩小训练集到high-coverage topics（但需要分析这是否引入topic bias）；(3) 明确实验中的fallback策略：对于LLM-generated perturbations，不应用T3F（因为translation mapping不精确），只应用rollout-level outcome consistency——但要在论文中量化这两种信号的质量差异。(4) 考虑增加一个pilot experiment：在一个小规模训练集（如500题）上先跑完整pipeline，验证T3F在SymPy-covered和non-covered问题上的实际行为差异。
- 调研依据: AbstRaL (arXiv 2506.07751) 在GSM级别有较好的覆盖率，但competition-level math的topic diversity更高，SymPy覆盖不确定性是MACR特有的风险。基于领域实验规范判断。

【缺陷 8】
- 类别: baseline 不足或过时
- 问题: 近期出现了多个与MACR部分目标重叠的GRPO变体（如CoRPO arXiv 2511.04439，通过correctness bias改善泛化；DRA-GRPO arXiv 2505.09655，通过diverse reasoning paths改善鲁棒性），但这些并未被纳入baseline或discussed in landscape。虽然它们不是直接的robustness方法，但审稿人可能会要求至少discuss它们为什么不需要作为baseline，或者作为supplementary comparison。
- 严重度: 可补救
- 补救方案: (1) 在research landscape中增加一个段落简要讨论recent GRPO variants (CoRPO, DRA-GRPO, AMIR-GRPO等)，说明它们的目标（general reasoning improvement）与MACR的目标（perturbation robustness）的区别，论证为什么当前7-tier baseline已经充分覆盖了robustness-relevant的方法空间；(2) 如果compute允许，选择其中一个（如CoRPO或DRA-GRPO）作为supplementary baseline，在1个seed上测试其robustness表现，验证"general reasoning improvement ≠ perturbation robustness"的论点。此为锦上添花，非必须。
- 调研依据: 调研中发现CoRPO (arXiv 2511.04439) 和 DRA-GRPO (arXiv 2505.09655) 是2025-2026年较有影响力的GRPO变体，审稿人可能期望看到discussion。

Sources:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation](https://arxiv.org/abs/2605.09262)
- [COPO: Consistency-Aware Policy Optimization](https://arxiv.org/abs/2508.04138)
- [VAR-MATH: Probing True Mathematical Reasoning](https://arxiv.org/abs/2507.12885)
- [MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations](https://arxiv.org/abs/2502.06453)
- [GC²PO: Towards Generalizable Reasoning](https://arxiv.org/abs/2602.06475)
- [F2C: Flip-Flop Consistency](https://arxiv.org/abs/2510.14242)
- [Predictive Scaling Laws for Efficient GRPO Training](https://arxiv.org/pdf/2507.18014)
- [CoRPO: Adding a Correctness Bias to GRPO](https://arxiv.org/pdf/2511.04439)
- [DRA-GRPO: Diverse Reasoning Paths for Mathematical Reasoning](https://arxiv.org/pdf/2505.09655)
- [AMIR-GRPO: Inducing Implicit Preference Signals into GRPO](https://arxiv.org/pdf/2601.03661)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90795fa1-5eba-4da2-bebd-fd1457829aab",
  "isSidechain": false,
  "requestId": "req_011CbWNkxnZsHxwxquRHKDMw",
  "type": "assistant",
  "uuid": "3f153ec9-4ec6-44d4-9d4a-b9ba253fa637",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QUgYb9aTJp1KfS3GysmJ1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 29548,
      "output_tokens": 7394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7394,
          "cache_read_input_tokens": 29548,
          "cache_creation_input_tokens": 1186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1186
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
  "lastPrompt": "# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem  RL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface pe…",
  "leafUuid": "3f153ec9-4ec6-44d4-9d4a-b9ba253fa637",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "MACR: Math reasoning robustness via consistency regularization",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem  RL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface pe…",
  "leafUuid": "3f153ec9-4ec6-44d4-9d4a-b9ba253fa637",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "MACR: Math reasoning robustness via consistency regularization",
  "sessionId": "0e0543e7-e1f4-48a2-b8f4-05aecae274a4"
}
```

---
