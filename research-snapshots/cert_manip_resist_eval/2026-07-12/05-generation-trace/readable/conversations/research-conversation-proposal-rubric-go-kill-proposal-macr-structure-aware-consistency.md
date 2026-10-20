# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # MACR: Structure-Aware Consistency

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/5652111f-4828-4e18-b653-ec09b9c576d1.jsonl`
- **Structured JSON:** [`4b4101aab0fe66c0fd47.json`](../../sessions/4b/4b4101aab0fe66c0fd47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:29:16.317Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:29:16.317Z",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL\n\n## Core Problem\n\nRL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface perturbations: open-weight reasoning models drop up to 55% (Robust Reasoning Benchmark, arXiv 2604.08571), and VAR-MATH (arXiv 2507.12885) documents 47-73% drops concentrated in sub-frontier models on competition-level problems. Binary reward provides no gradient against surface-form-dependent strategies.\n\nExisting augmentation methods (TA-GRPO, arXiv 2601.22478; PrAg-PO, arXiv 2602.03190) pool rewards across equivalent variants but optimize reward, not strategy invariance. Critically, in the \"both-correct regime\" (both original and perturbed variants solved), pooled advantage yields identical signals—zero differential gradient—leaving surface-dependent reasoning strategies unrectified. This regime becomes increasingly prevalent as training progresses and model accuracy rises, meaning augmentation-only methods suffer diminishing corrective power precisely when fine-grained strategy refinement matters most. Can structure-aware consistency regularization during GRPO enforce perturbation-invariant reasoning strategies, especially in this late-training regime?\n\n## Key Insight: Augmentation Optimizes Reward, Consistency Optimizes Strategy\n\nTA-GRPO's pooled advantage provides effective learning signal when one variant is solved and the other is not (early training, lower accuracy). But as training progresses and accuracy increases, the both-correct regime dominates, and TA-GRPO's signal diminishes. MACR's explicit consistency loss fills this gap: it provides gradient even when both variants are correct, enforcing not just correct answers but structurally similar reasoning. This creates a natural phase complementarity—augmentation drives initial learning, consistency drives late-stage refinement from \"getting it right\" to \"getting it right for the right reasons.\"\n\n## Critical Technical Challenge: Math ≠ Vision for Consistency\n\nROMA (arXiv 2605.09262) achieves visual robustness via token-level KL between corrupted and clean trajectories under teacher forcing. This works because visual perturbation (blur, noise) preserves the correct answer—the same reasoning trace is valid for both views. In math, numerical substitution (2x+3=7 → 5x+2=12) changes the answer and intermediate computations. Naively applying ROMA's token-level divergence would penalize correct numerical differences alongside genuine strategy divergence.\n\nWe propose **Trajectory-Translated Teacher Forcing (T3F)** as the core mechanism for Structure-Aware Consistency (SAC):\n\n1. For original problem x, select a correct rollout trajectory τ_x from GRPO sampling.\n2. Using SymPy's known perturbation mapping M (e.g., {a=2→a=5, variable x→variable y}), mechanically translate τ_x into τ_translated by substituting corresponding numerical values and variable names. Since SymPy controls the perturbation, the mapping is exact and deterministic. τ_translated has identical length and structure to τ_x—only problem-specific values change.\n3. Teacher-force the model on perturbed input x' with prefix from τ_translated, collecting per-token logit distributions.\n4. Teacher-force the model on original input x with prefix from τ_x, collecting per-token logit distributions.\n5. Compute token-level JS divergence between the two logit distribution sequences, with numerical-token masking as secondary noise reduction.\n\nT3F resolves the alignment problem: trajectory translation creates exact position correspondence, making token-level divergence well-defined without requiring step-level alignment algorithms (e.g., DTW). The divergence directly measures: \"Given structurally identical reasoning contexts (differing only in problem-specific values), does the model assign similar probabilities to structurally corresponding next tokens?\"\n\n**Why token-level, not step-type-level?** A coarser alternative would compare only reasoning step types (e.g., \"set up equation → simplify → solve\"). But step-type consistency cannot distinguish between correct algebraic manipulation and pattern-matching shortcuts within the same step type. Token-level granularity captures intra-step strategy differences—the fine-grained signal that matters for eliminating surface heuristics.\n\n**Masking policy and boundary conditions.** Numerical token identification uses regex matching against SymPy's perturbation mapping (problem-copied values and their direct derivatives). Mathematical constants (π, e), step indices, and tokens not traceable to problem-specific values are retained in the JS computation. This conservative masking policy is sound because SymPy-controlled perturbations guarantee that only mapped values differ between τ_x and τ_translated; unmapped numerical tokens (e.g., mathematical constants shared across variants) should indeed be consistent. Limitation: for perturbation types beyond token-level substitution (e.g., expression rewriting \"a+b\" → \"b+a\"), trajectory translation may introduce structural shifts; for these, we fall back to rollout-level outcome consistency (JS over correctness distributions across K rollouts) as a coarser but robust signal.\n\n## Research Landscape\n\n**Diagnostic-only (no training fix):** VAR-MATH (arXiv 2507.12885): 47-73% drops, sub-frontier models on competition math. MATH-Perturb (ICML 2025, arXiv 2502.06453): 279 MATH level-5 problems, distinguishes solution-preserving (Simple) vs. solution-changing (Hard) perturbation. GSM-Symbolic (ICLR 2025): performance variance across instantiations, 25 models evaluated. Robust Reasoning Benchmark (arXiv 2604.08571): 14 encoding/structural perturbation types on AIME 2024, orthogonal to semantic-preserving perturbation.\n\n**Augmentation-only (no invariance objective):** TA-GRPO (arXiv 2601.22478): +9.84pp competition math via cross-variant pooled advantage, no consistency loss, no robustness evaluation. PrAg-PO (arXiv 2602.03190): prompt augmentation stabilizes GRPO, mitigates entropy collapse, no invariance objective.\n\n**Structural RL (different mechanism):** AbstRaL (ICLR 2026, arXiv 2506.07751): input-side mechanism—teaches models to abstract GSM problems into symbolic representations before solving. Achieves near-full robustness recovery on GSM variants but untested on competition-level math. MACR is output-side (constrains reasoning strategy consistency). These are orthogonal: abstraction changes how the model reads problems, consistency changes how it reasons. Potentially complementary. MathForge/DGPO (ICLR 2026): difficulty-aware GRPO, no robustness evaluation.\n\n**Causal/consistency RL (different target):** GC²PO (arXiv 2602.06475): episodic causal counterfactual reward evaluating whether reasoning steps remain stable under within-problem counterfactual perturbations—focuses on step-level causal robustness within a single problem. MACR targets cross-problem strategy invariance across semantically equivalent perturbations—a complementary but distinct objective. GRPO-CARE (arXiv 2506.16141): consistency-aware RL for video reasoning (step-answer coherence, not cross-perturbation invariance). CC-LEARN (arXiv 2506.15662): cohort consistency RL for NLU tasks. COPO (arXiv 2508.04138): consistency-entropy for zero-advantage training efficiency—addresses the same upstream problem (gradient vanishing in all-correct groups) but through advantage redesign rather than cross-perturbation consistency. DPH-RL: JS for diversity, not invariance.\n\n**Consistency regularization (different domain/setting):** ROMA (arXiv 2605.09262): correctness-conditioned token-level KL for visual corruption robustness, closest methodological cousin but operates where perturbation preserves answers. F2C (arXiv 2510.14242)/PPCL: JS-based consistency, SFT-only, NLU-only.\n\n**Gap:** No work combines math-equivalence-aware perturbation with trajectory-translated structure-aware consistency during RL training. The T3F mechanism—which resolves the fundamental math-vs-vision consistency gap via SymPy-guided trajectory translation—is the core technical novelty.\n\n## Proposed Approach\n\nMACR integrates perturbation-invariance into GRPO training on Qwen3-8B via four components:\n\n**(1) SymPy-Verified Symbolic Perturbation Generator.** Creates equivalent variants through: numerical substitution, variable renaming, expression rewriting (a+b → b+a), constraint reformulation (\"A exceeds B by 3\" → \"B is 3 less than A\"). All variants SymPy-verified for answer equivalence. Inspired by Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187). Coverage limitation: SymPy handles algebra/equation problems well but has limited coverage for geometry, combinatorics, and number theory. For non-coverable problems, LLM-based perturbation with majority-vote verification serves as fallback. We report per-topic perturbation coverage rates.\n\n**(2) Structure-Aware Consistency (SAC) via T3F.** For each (original, perturbed) pair where both are correctly solved in GRPO rollouts: apply Trajectory-Translated Teacher Forcing (detailed above) to compute token-level JS divergence over reasoning structure. Correctness-conditioning (à la ROMA) restricts enforcement to successful pairs, avoiding systematically wrong invariance. For perturbation types where trajectory translation is imprecise (expression rewriting, constraint reformulation), fall back to rollout-level outcome consistency.\n\n**(3) Contrastive Discrimination Loss.** Prevents degenerate invariance by training the model to distinguish surface-similar but semantically-different problems. Hard negatives constructed via SymPy answer-changing perturbation: modifying a coefficient/constraint so the answer changes while surface similarity is preserved. Automatically verifiable via SymPy.\n\n**(4) verl/DAPO Infrastructure.** Built on DAPO (arXiv 2025) for scalable GRPO training.\n\n## Theoretical Positioning\n\nMACR provides a lightweight process-level quality signal without step-level annotation. By requiring structurally similar reasoning on equivalent problems, SAC implicitly penalizes heuristic shortcuts: a model relying on surface pattern matching cannot consistently produce similar reasoning structures across numerically different but structurally identical problems. This positions MACR as complementary to PRM (explicit process supervision) and ORM (outcome-only)—offering process-quality pressure at zero annotation cost. This claim is offered as a secondary insight; the primary contribution is perturbation robustness.\n\n## Experimental Design\n\n**Training Data:** MATH training split (~7.5K problems) + NuminaMath-TIR subset, aligned with TA-GRPO's data regime for fair comparison. We report SymPy perturbation success rate on this training set (expected: high for algebra/equations, lower for geometry/combinatorics).\n\n**Baselines (7 tiers):**\n1. Vanilla Qwen3-8B (no RL)\n2. Standard GRPO (verl/DAPO, no augmentation or consistency)\n3. COPO (consistency-entropy advantage redesign—isolates \"fix zero-advantage\" from \"enforce cross-perturbation consistency\")\n4. TA-GRPO / PrAg-PO (augmentation-only GRPO—isolates SAC contribution)\n5. AbstRaL (abstraction + RL—direct competitor; reproduce on Qwen3-8B if feasible, otherwise use published results on shared benchmarks with explicit model-gap discussion since AbstRaL uses Llama-3/Qwen2)\n6. F2C-style generic JS consistency applied to GRPO (no math-specific perturbation or T3F—isolates math-aware design value)\n7. Full MACR\n\n**Compute-normalized comparison:** Standard GRPO with 2-3x compute budget (matched to MACR's additional forward passes) as fairness control.\n\n**Evaluation Benchmarks:**\n- Robustness (core): VAR-MATH, MATH-P-Simple (ICML 2025), GSM-Symbolic (ICLR 2025), GSM-Plus\n- Robustness (supplementary, out-of-scope for MACR): MATH-P-Hard, Robust Reasoning Benchmark (arXiv 2604.08571) — reported for completeness, no expected gains\n- Clean accuracy: MATH500, GSM8K, AIME 2024\n- OOD generalization: Minerva, OlympiadBench\n- Stratified analysis: per-topic breakdown (algebra, number theory, geometry, combinatorics) to assess SymPy coverage impact\n\n**Evaluation Metrics:**\n- Clean Accuracy: Pass@1 on standard benchmarks\n- Robust Accuracy: Pass@1 on perturbation benchmarks\n- Relative Performance Drop (RPD): (Clean − Robust) / Clean × 100%\n- Consistency Rate: fraction of templates where all instantiations correct (VAR-MATH strict)\n- Performance Variance: accuracy variance across instantiations (GSM-Symbolic style)\n- All metrics: mean ± std over 3 seeds (sensitivity analyses on 1 seed)\n\n**Ablation Study:**\n- A1: GRPO only (no augmentation, no consistency)\n- A2: GRPO + perturbation augmentation only (no consistency loss)\n- A3: GRPO + perturbation + unconditional JS (no correctness conditioning)\n- A4: GRPO + perturbation + correctness-conditioned JS without T3F (naive token-level JS, no trajectory translation)\n- A5: GRPO + perturbation + correctness-conditioned SAC via T3F (no contrastive)\n- A6: Full MACR (T3F-SAC + contrastive discrimination)\n- A7: λ sensitivity for consistency loss weight (1 seed)\n- A8: Perturbation type contribution: numerical-only vs. variable-only vs. expression-rewriting vs. all (1 seed)\n- A9: T3F teacher-forcing vs. rollout-level outcome consistency (coarse fallback)\n- A10: Masking granularity: conservative (problem-value-only) vs. aggressive (all digits) vs. no masking\n\n**Compute Estimate:** Single GRPO run on Qwen3-8B ≈ 40-80 GPU-hours on 8×A100. Core baselines (7 configs × 3 seeds = 21 runs) + key ablations (A3-A6 × 3 seeds = 12 runs) + sensitivity analyses (A7-A10 × 1 seed = 4 runs) = ~37 runs ≈ 1,500-3,000 A100 GPU-hours total. Ablation reduction strategy: A7, A8, A10 run on 1 seed for initial screening, scale to 3 seeds only for significant findings.\n\n## Key References\n\n- ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (arXiv 2605.09262, 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2507.12885, 2025)\n- AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking (ICLR 2026, arXiv 2506.07751)\n- MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations (ICML 2025, arXiv 2502.06453)\n- Robust Reasoning Benchmark (arXiv 2604.08571, 2026)\n- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478)\n- PrAg-PO: Prompt Augmentation Scales up GRPO Training (arXiv 2602.03190)\n- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)\n- DAPO: Open-Source LLM RL System at Scale (arXiv 2025)\n- F2C: Flip-Flop Consistency for Prompt Perturbation Robustness (arXiv 2510.14242, 2025)\n- GSM-Symbolic: Understanding Limitations of Math Reasoning (ICLR 2025)\n- GSM-Plus: Evaluating Robustness of LLMs as Mathematical Problem Solvers\n- GC²PO: Group Causal Counterfactual Policy Optimization (arXiv 2602.06475, 2026)\n- GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (arXiv 2506.16141)\n- COPO: Consistency-Entropy Policy Optimization (arXiv 2508.04138)\n- CC-LEARN: Cohort-based Consistency Learning (arXiv 2506.15662)\n- DPH-RL / PPCL\n- Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, 2026)\n- NuminaMath-TIR"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:29:16.322Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:29:16.322Z",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-29T06:29:16.394Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
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
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "9c83044e-38ba-4c11-a4c9-0ef7086c4271",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:29:16.393Z_

```json
{
  "parentUuid": "9c83044e-38ba-4c11-a4c9-0ef7086c4271",
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
  "uuid": "9154d89a-d36d-4503-89b7-584692b770bb",
  "timestamp": "2026-05-29T06:29:16.393Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:29:16.393Z_

```json
{
  "parentUuid": "9154d89a-d36d-4503-89b7-584692b770bb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9f19d096-3a16-4107-9b97-832dbc0265fb",
  "timestamp": "2026-05-29T06:29:16.393Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "9f19d096-3a16-4107-9b97-832dbc0265fb",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:29:20.888Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. Let me first do thorough web searches to understand the field, then provide my assessment.

Let me search for the key related works and the current state of the field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f19d096-3a16-4107-9b97-832dbc0265fb",
  "isSidechain": false,
  "requestId": "req_011CbWPTNoZHrQXMwLeqZMfh",
  "type": "assistant",
  "uuid": "1e1b3cc7-6079-4d0c-ad05-47ad514336ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRKq9b3Z6YBGha72EVfxNy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 11014,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8117
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

_source line 9 · 2026-05-29T06:29:21.446Z_

I'll start by conducting thorough web searches to understand the current research landscape before evaluating this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e1b3cc7-6079-4d0c-ad05-47ad514336ff",
  "isSidechain": false,
  "requestId": "req_011CbWPTNoZHrQXMwLeqZMfh",
  "type": "assistant",
  "uuid": "ac584939-a6eb-403b-a406-f44c2c737d78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRKq9b3Z6YBGha72EVfxNy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 11014,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8117
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

_source line 10 · 2026-05-29T06:29:21.839Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RUEydyAjq8hjTg46sAPKAa`</summary>

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
  "parentUuid": "ac584939-a6eb-403b-a406-f44c2c737d78",
  "isSidechain": false,
  "requestId": "req_011CbWPTNoZHrQXMwLeqZMfh",
  "type": "assistant",
  "uuid": "718b06a4-5fdc-4ce3-a92e-3d2912606702",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRKq9b3Z6YBGha72EVfxNy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 11014,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8117
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

_source line 11 · 2026-05-29T06:29:21.851Z_

<details><summary>↩ Tool result · `toolu_01RUEydyAjq8hjTg46sAPKAa`</summary>

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
  "parentUuid": "718b06a4-5fdc-4ce3-a92e-3d2912606702",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "1ff8e0fd-d267-4e0b-9a00-4b36ff8e691c",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "718b06a4-5fdc-4ce3-a92e-3d2912606702",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-29T06:29:25.066Z_

Now let me conduct the required research searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ff8e0fd-d267-4e0b-9a00-4b36ff8e691c",
  "isSidechain": false,
  "requestId": "req_011CbWPTnJBKY7c5FerzFCnp",
  "type": "assistant",
  "uuid": "1889b748-5577-4e6e-bf68-09997ebd7eb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWLvaz9P2JHsqAriwuQARr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 19131,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 13 · 2026-05-29T06:29:26.108Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BEZa8pbGHGK4bSr22XA8MQ`</summary>

```json
{
  "query": "RL math reasoning robustness perturbation 2025 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1889b748-5577-4e6e-bf68-09997ebd7eb8",
  "isSidechain": false,
  "requestId": "req_011CbWPTnJBKY7c5FerzFCnp",
  "type": "assistant",
  "uuid": "d7177d0e-4a14-462d-bf5f-92ac95b364d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWLvaz9P2JHsqAriwuQARr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 19131,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 14 · 2026-05-29T06:29:26.584Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JcRRBLsy7955u93uFBdALY`</summary>

```json
{
  "query": "TA-GRPO transform augmented GRPO math reasoning arXiv 2601.22478"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7177d0e-4a14-462d-bf5f-92ac95b364d5",
  "isSidechain": false,
  "requestId": "req_011CbWPTnJBKY7c5FerzFCnp",
  "type": "assistant",
  "uuid": "4384b75d-000e-46e7-b335-79b6424a7afe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWLvaz9P2JHsqAriwuQARr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 19131,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 15 · 2026-05-29T06:29:27.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RipWzeebPNziwRMVLLpEEc`</summary>

```json
{
  "query": "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4384b75d-000e-46e7-b335-79b6424a7afe",
  "isSidechain": false,
  "requestId": "req_011CbWPTnJBKY7c5FerzFCnp",
  "type": "assistant",
  "uuid": "d4244a6f-26b0-4e52-b59b-ac71c32bfda7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWLvaz9P2JHsqAriwuQARr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 19131,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 16 · 2026-05-29T06:29:28.046Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XQH5NfxfD6JV4dXm2zwTnZ`</summary>

```json
{
  "query": "AbstRaL abstract thinking reinforcement learning math ICLR 2026 arXiv 2506.07751"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4244a6f-26b0-4e52-b59b-ac71c32bfda7",
  "isSidechain": false,
  "requestId": "req_011CbWPTnJBKY7c5FerzFCnp",
  "type": "assistant",
  "uuid": "1d7ca1b9-8662-499d-b615-7ccc12bd495a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWLvaz9P2JHsqAriwuQARr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 19131,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 17 · 2026-05-29T06:29:28.123Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y9mCUr7QgHi2UoTLpaZrAm`</summary>

```json
{
  "query": "COPO consistency entropy policy optimization arXiv 2508.04138 zero advantage GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d7ca1b9-8662-499d-b615-7ccc12bd495a",
  "isSidechain": false,
  "requestId": "req_011CbWPTnJBKY7c5FerzFCnp",
  "type": "assistant",
  "uuid": "e70fae8c-a3eb-4bb2-8ff7-41e881761ab1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWLvaz9P2JHsqAriwuQARr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 19131,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 18 · 2026-05-29T06:29:33.433Z_

<details><summary>↩ Tool result · `toolu_01JcRRBLsy7955u93uFBdALY`</summary>

```text
Web search results for query: "TA-GRPO transform augmented GRPO math reasoning arXiv 2601.22478"

Links: [{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/html/2601.22478"},{"title":"(PDF) Transform-Augmented GRPO Improves Pass@k","url":"https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/html/2602.03190v1"}]

Based on the search results, here's what I found about TA-GRPO:

## Overview
TA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.

## Problem It Addresses
Group Relative Policy Optimization (GRPO) has two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.

## Key Benefits
The pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies. TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.

## Experimental Results
Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).

The paper was submitted on January 30, 2026, with a revision on February 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4384b75d-000e-46e7-b335-79b6424a7afe",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "5fab8f06-117f-4876-b2f1-2e2edd7212e9",
  "toolUseResult": {
    "query": "TA-GRPO transform augmented GRPO math reasoning arXiv 2601.22478",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xjh5xXtcpv1HsKbocfs3ov",
        "content": [
          {
            "title": "[2601.22478] Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/abs/2601.22478"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/pdf/2601.22478"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/html/2601.22478"
          },
          {
            "title": "(PDF) Transform-Augmented GRPO Improves Pass@k",
            "url": "https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/html/2602.03190v1"
          }
        ]
      },
      "Based on the search results, here's what I found about TA-GRPO:\n\n## Overview\nTA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.\n\n## Problem It Addresses\nGroup Relative Policy Optimization (GRPO) has two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.\n\n## Key Benefits\nThe pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies. TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.\n\n## Experimental Results\nExperiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).\n\nThe paper was submitted on January 30, 2026, with a revision on February 11, 2026."
    ],
    "durationSeconds": 6.845873029999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4384b75d-000e-46e7-b335-79b6424a7afe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T06:29:33.906Z_

<details><summary>↩ Tool result · `toolu_01BEZa8pbGHGK4bSr22XA8MQ`</summary>

```text
Web search results for query: "RL math reasoning robustness perturbation 2025 2026 survey"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://www.arxiv.org/pdf/2602.07470"},{"title":"Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges","url":"https://arxiv.org/html/2605.19723v1"},{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571v2"},{"title":"May 7, 2026 Rethinking RL for LLM Reasoning:","url":"https://arxiv.org/pdf/2605.06241"},{"title":"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2511.08022"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview","url":"https://openreview.net/forum?id=OZy70UggXr"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/pdf/2508.08833"}]

Based on the search results, here's what I found on RL math reasoning robustness and perturbation research from 2025-2026:

## Key Research Areas

**Robustness Benchmarking and Perturbations:**

The Robust Reasoning Benchmark (RRB) introduces a pipeline of 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025, with findings showing that current open-weights architectures and RL paradigms can memorize and execute standard mathematical heuristics, but their reasoning pathways are overfit to standard textual formatting and sequential presentation.

MATH-Perturb constructs MATH-P-Simple and MATH-P-Hard via simple and hard perturbations, each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset, with significant performance drops on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).

**RL for Mathematical Reasoning:**

RL's useful effect on math reasoning is a sparse, predictable, and low-dimensional correction, and this correction can be obtained without RL at all. Existing research shows that the reasoning process of current LLMs essentially relies on complex pattern matching rather than formal mathematical reasoning.

**Robustness Evaluation Methods:**

Four LLMs obtain 48.04% and 31.35% less averaged accuracy on GSM8K and MATH-500 evaluation variants, respectively, and Generalization-and-Perturbation (GAP) is a novel evaluation strategy that addresses both leakage and robustness by stress-testing models on mathematically equivalent versions of the same problem.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7177d0e-4a14-462d-bf5f-92ac95b364d5",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "b218f24e-0f15-43a4-b65a-b79c4ba05469",
  "toolUseResult": {
    "query": "RL math reasoning robustness perturbation 2025 2026 survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NinvJq1CQumXA3ZnZSVkQ5",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://www.arxiv.org/pdf/2602.07470"
          },
          {
            "title": "Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges",
            "url": "https://arxiv.org/html/2605.19723v1"
          },
          {
            "title": "Robust Reasoning Benchmark",
            "url": "https://arxiv.org/html/2604.08571v2"
          },
          {
            "title": "May 7, 2026 Rethinking RL for LLM Reasoning:",
            "url": "https://arxiv.org/pdf/2605.06241"
          },
          {
            "title": "Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2511.08022"
          },
          {
            "title": "Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/html/2506.05038"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v1"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=OZy70UggXr"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/pdf/2508.08833"
          }
        ]
      },
      "Based on the search results, here's what I found on RL math reasoning robustness and perturbation research from 2025-2026:\n\n## Key Research Areas\n\n**Robustness Benchmarking and Perturbations:**\n\nThe Robust Reasoning Benchmark (RRB) introduces a pipeline of 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025, with findings showing that current open-weights architectures and RL paradigms can memorize and execute standard mathematical heuristics, but their reasoning pathways are overfit to standard textual formatting and sequential presentation.\n\nMATH-Perturb constructs MATH-P-Simple and MATH-P-Hard via simple and hard perturbations, each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset, with significant performance drops on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).\n\n**RL for Mathematical Reasoning:**\n\nRL's useful effect on math reasoning is a sparse, predictable, and low-dimensional correction, and this correction can be obtained without RL at all. Existing research shows that the reasoning process of current LLMs essentially relies on complex pattern matching rather than formal mathematical reasoning.\n\n**Robustness Evaluation Methods:**\n\nFour LLMs obtain 48.04% and 31.35% less averaged accuracy on GSM8K and MATH-500 evaluation variants, respectively, and Generalization-and-Perturbation (GAP) is a novel evaluation strategy that addresses both leakage and robustness by stress-testing models on mathematically equivalent versions of the same problem."
    ],
    "durationSeconds": 7.793674005000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d7177d0e-4a14-462d-bf5f-92ac95b364d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T06:29:34.869Z_

<details><summary>↩ Tool result · `toolu_01RipWzeebPNziwRMVLLpEEc`</summary>

```text
Web search results for query: "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262"

Links: [{"title":"[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/abs/2605.09262"},{"title":"Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/pdf/2605.09262"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/html/2509.23322v2"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/html/2512.17532"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/pdf/2512.17532"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/pdf/2509.23322"}]

I found the paper! Here's what I found about the arXiv paper 2605.09262:

**Title:** Reinforcing Multimodal Reasoning Against Visual Degradation

**Summary:** The paper proposes ROMA, an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance. Reinforcement Learning has significantly advanced the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet the resulting policies remain brittle against real-world visual degradations such as blur, compression artifacts, and low-resolution scans.

**Key Technical Approach:** A dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs. The method applies a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories.

**Results:** On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4244a6f-26b0-4e52-b59b-ac71c32bfda7",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "744e5abd-8765-41b4-9dd8-c621b64b8573",
  "toolUseResult": {
    "query": "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RbL51FBxLJPnSibsycLCpK",
        "content": [
          {
            "title": "[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/abs/2605.09262"
          },
          {
            "title": "Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/pdf/2605.09262"
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
      "I found the paper! Here's what I found about the arXiv paper 2605.09262:\n\n**Title:** Reinforcing Multimodal Reasoning Against Visual Degradation\n\n**Summary:** The paper proposes ROMA, an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance. Reinforcement Learning has significantly advanced the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet the resulting policies remain brittle against real-world visual degradations such as blur, compression artifacts, and low-resolution scans.\n\n**Key Technical Approach:** A dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs. The method applies a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories.\n\n**Results:** On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy."
    ],
    "durationSeconds": 7.813189876,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d4244a6f-26b0-4e52-b59b-ac71c32bfda7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-29T06:29:35.598Z_

<details><summary>↩ Tool result · `toolu_01Y9mCUr7QgHi2UoTLpaZrAm`</summary>

```text
Web search results for query: "COPO consistency entropy policy optimization arXiv 2508.04138 zero advantage GRPO"

Links: [{"title":"COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/html/2508.04138v1"},{"title":"[2508.04138v1] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138v1"},{"title":"COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,","url":"https://arxiv.org/pdf/2508.04138"},{"title":"[2508.04138] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138"},{"title":"COPO: Consistency-Aware Policy Optimization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/copo-consistency-aware-policy-optimization"},{"title":"Artificial Intelligence 2025","url":"https://www.arxiv.org/list/cs.AI/2025?skip=29800&show=500"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=2200&show=25"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=21075&show=25"}]

Based on the search results, here's what I found about COPO and the arXiv paper 2508.04138:

## Overview

COPO is a consistency-entropy-based policy optimization framework that theoretically addresses the sample wastage and gradient vanishing problem under extreme samples observed in GRPO methods.

## The Problem COPO Addresses

When multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero, which leads to vanishing gradients and renders the corresponding samples ineffective for learning, ultimately limiting training efficiency and downstream performance.

## Solution

COPO introduces a structured global reward based on outcome consistency; the global loss ensures that even when model outputs show high intra-group consistency, the training process still receives meaningful learning signals, and incorporates an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization.

## Consistency Entropy

The consistency entropy evaluates the consistency of the model's responses to a given prompt, serving as an indicator of the determinism in its output behavior. When consistency entropy is high (indicating high diversity), local optimization dominates to reinforce higher-quality responses; when it is low (indicating high response uniformity), global optimization dominates to maintain correctness and consistency across prompts.

The paper was submitted to arXiv on August 6, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e70fae8c-a3eb-4bb2-8ff7-41e881761ab1",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "bbf5beff-2a77-47c0-963c-7b1223080b9e",
  "toolUseResult": {
    "query": "COPO consistency entropy policy optimization arXiv 2508.04138 zero advantage GRPO",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TAKvUDQbQ1nG6wqu4x8wiu",
        "content": [
          {
            "title": "COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/html/2508.04138v1"
          },
          {
            "title": "[2508.04138v1] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138v1"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,",
            "url": "https://arxiv.org/pdf/2508.04138"
          },
          {
            "title": "[2508.04138] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/copo-consistency-aware-policy-optimization"
          },
          {
            "title": "Artificial Intelligence 2025",
            "url": "https://www.arxiv.org/list/cs.AI/2025?skip=29800&show=500"
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
      "Based on the search results, here's what I found about COPO and the arXiv paper 2508.04138:\n\n## Overview\n\nCOPO is a consistency-entropy-based policy optimization framework that theoretically addresses the sample wastage and gradient vanishing problem under extreme samples observed in GRPO methods.\n\n## The Problem COPO Addresses\n\nWhen multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero, which leads to vanishing gradients and renders the corresponding samples ineffective for learning, ultimately limiting training efficiency and downstream performance.\n\n## Solution\n\nCOPO introduces a structured global reward based on outcome consistency; the global loss ensures that even when model outputs show high intra-group consistency, the training process still receives meaningful learning signals, and incorporates an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization.\n\n## Consistency Entropy\n\nThe consistency entropy evaluates the consistency of the model's responses to a given prompt, serving as an indicator of the determinism in its output behavior. When consistency entropy is high (indicating high diversity), local optimization dominates to reinforce higher-quality responses; when it is low (indicating high response uniformity), global optimization dominates to maintain correctness and consistency across prompts.\n\nThe paper was submitted to arXiv on August 6, 2025."
    ],
    "durationSeconds": 7.472962595000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e70fae8c-a3eb-4bb2-8ff7-41e881761ab1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "bbf5beff-2a77-47c0-963c-7b1223080b9e",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---

### Tool result

_source line 24 · 2026-05-29T06:29:40.169Z_

<details><summary>↩ Tool result · `toolu_01XQH5NfxfD6JV4dXm2zwTnZ`</summary>

```text
Web search results for query: "AbstRaL abstract thinking reinforcement learning math ICLR 2026 arXiv 2506.07751"

Links: [{"title":"[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/abs/2506.07751"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/html/2506.07751"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"[PDF] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AbstRaL:-Augmenting-LLMs'-Reasoning-by-Reinforcing-Gao-Bosselut/db59c2208185f3711705387c5baf2aa47ec648c5"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=24150&show=25"},{"title":"arXiv:2506.07751v2 [cs.CL] 11 Jun 2025 AbstRaL: Augmenting LLMs’ Reasoning by","url":"https://bengio.abracadoudou.com/cv/publications/pdf/gao_2025_arxiv.pdf"}]

Based on the search results, I found information about the AbstRaL paper:

## AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking

The paper addresses the problem that large language models (LLMs), especially smaller ones, often lack robustness in grade school math (GSM) reasoning. In particular, they tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses.

The work focuses on the strategy of "abstracting" reasoning problems, which not only helps counteract distribution shifts but also facilitates the connection to symbolic tools for deriving solutions. The abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions.

The reinforced AbstRaction Learning framework (AbstRaL) first teaches LLMs to generate mathematical abstraction of input GSM problems, and then connects the abstraction with symbolic tools to stably derive the output solution, regardless of the specific input contexts. On top of supervised fine-tuning (SFT), AbstRaL uses reinforcement learning (RL) with a new set of model-free rewards to further improve the faithfulness of generated abstraction.

The method was tested on two benchmarks that evaluate the robustness of GSM reasoning: GSM-Symbolic and GSM-Plus. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability.

The paper is accepted to ICLR 2026 and was authored by Silin Gao, Antoine Bosselut, Samy Bengio, and Emmanuel Abbe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d7ca1b9-8662-499d-b615-7ccc12bd495a",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "f30edb1e-71ed-4355-8bbd-e32c19dcd4d9",
  "toolUseResult": {
    "query": "AbstRaL abstract thinking reinforcement learning math ICLR 2026 arXiv 2506.07751",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Hi4KGErvZd4WF3LZ7iDgPi",
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
            "title": "[PDF] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/AbstRaL:-Augmenting-LLMs'-Reasoning-by-Reinforcing-Gao-Bosselut/db59c2208185f3711705387c5baf2aa47ec648c5"
          },
          {
            "title": "Artificial Intelligence Jun 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"
          },
          {
            "title": "Artificial Intelligence 2025",
            "url": "https://arxiv.org/list/cs.AI/2025?skip=24150&show=25"
          },
          {
            "title": "arXiv:2506.07751v2 [cs.CL] 11 Jun 2025 AbstRaL: Augmenting LLMs’ Reasoning by",
            "url": "https://bengio.abracadoudou.com/cv/publications/pdf/gao_2025_arxiv.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the AbstRaL paper:\n\n## AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking\n\nThe paper addresses the problem that large language models (LLMs), especially smaller ones, often lack robustness in grade school math (GSM) reasoning. In particular, they tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses.\n\nThe work focuses on the strategy of \"abstracting\" reasoning problems, which not only helps counteract distribution shifts but also facilitates the connection to symbolic tools for deriving solutions. The abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions.\n\nThe reinforced AbstRaction Learning framework (AbstRaL) first teaches LLMs to generate mathematical abstraction of input GSM problems, and then connects the abstraction with symbolic tools to stably derive the output solution, regardless of the specific input contexts. On top of supervised fine-tuning (SFT), AbstRaL uses reinforcement learning (RL) with a new set of model-free rewards to further improve the faithfulness of generated abstraction.\n\nThe method was tested on two benchmarks that evaluate the robustness of GSM reasoning: GSM-Symbolic and GSM-Plus. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability.\n\nThe paper is accepted to ICLR 2026 and was authored by Silin Gao, Antoine Bosselut, Samy Bengio, and Emmanuel Abbe."
    ],
    "durationSeconds": 12.121269937999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1d7ca1b9-8662-499d-b615-7ccc12bd495a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-29T06:29:46.597Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have initial research results. Let me do a few more targeted searches to better understand the landscape and verify key claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f30edb1e-71ed-4355-8bbd-e32c19dcd4d9",
  "isSidechain": false,
  "requestId": "req_011CbWPV8NCZexqyiZ7BxXD4",
  "type": "assistant",
  "uuid": "1696e2d5-a66e-4f9d-b672-a764452250cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3gyFNLJnqjU1diwMCGkJ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 724,
      "cache_creation_input_tokens": 3313,
      "cache_read_input_tokens": 19825,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 724,
          "output_tokens": 245,
          "cache_read_input_tokens": 19825,
          "cache_creation_input_tokens": 3313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3313
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

_source line 26 · 2026-05-29T06:29:46.973Z_

Good. Let me do a few more targeted searches to verify specific claims and understand the competitive landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1696e2d5-a66e-4f9d-b672-a764452250cd",
  "isSidechain": false,
  "requestId": "req_011CbWPV8NCZexqyiZ7BxXD4",
  "type": "assistant",
  "uuid": "c74108d4-8a95-48b3-a95e-6b5ec0aecd5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3gyFNLJnqjU1diwMCGkJ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 724,
      "cache_creation_input_tokens": 3313,
      "cache_read_input_tokens": 19825,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 724,
          "output_tokens": 245,
          "cache_read_input_tokens": 19825,
          "cache_creation_input_tokens": 3313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3313
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

_source line 27 · 2026-05-29T06:29:47.328Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017i2xNJpBuqCncvmkWiuxrP`</summary>

```json
{
  "query": "VAR-MATH symbolic benchmark math reasoning robustness arXiv 2507.12885"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c74108d4-8a95-48b3-a95e-6b5ec0aecd5a",
  "isSidechain": false,
  "requestId": "req_011CbWPV8NCZexqyiZ7BxXD4",
  "type": "assistant",
  "uuid": "2dad57ff-d6eb-4a95-abf1-f5e8561f4490",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3gyFNLJnqjU1diwMCGkJ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 724,
      "cache_creation_input_tokens": 3313,
      "cache_read_input_tokens": 19825,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 724,
          "output_tokens": 245,
          "cache_read_input_tokens": 19825,
          "cache_creation_input_tokens": 3313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3313
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

_source line 28 · 2026-05-29T06:29:47.559Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Efv5aQTekkHGE8GfSuhmPN`</summary>

```json
{
  "query": "GC2PO group causal counterfactual policy optimization arXiv 2602.06475 math reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dad57ff-d6eb-4a95-abf1-f5e8561f4490",
  "isSidechain": false,
  "requestId": "req_011CbWPV8NCZexqyiZ7BxXD4",
  "type": "assistant",
  "uuid": "f830ec8a-66f7-4be0-b293-890dab7ad8ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3gyFNLJnqjU1diwMCGkJ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 724,
      "cache_creation_input_tokens": 3313,
      "cache_read_input_tokens": 19825,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 724,
          "output_tokens": 245,
          "cache_read_input_tokens": 19825,
          "cache_creation_input_tokens": 3313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3313
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

_source line 29 · 2026-05-29T06:29:47.877Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013VZAktRVA5wSKN7Q2LCmLS`</summary>

```json
{
  "query": "consistency regularization reinforcement learning LLM reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f830ec8a-66f7-4be0-b293-890dab7ad8ac",
  "isSidechain": false,
  "requestId": "req_011CbWPV8NCZexqyiZ7BxXD4",
  "type": "assistant",
  "uuid": "6f80aaa6-2879-413c-b129-c2f5fe5a1bb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3gyFNLJnqjU1diwMCGkJ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 724,
      "cache_creation_input_tokens": 3313,
      "cache_read_input_tokens": 19825,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 724,
          "output_tokens": 245,
          "cache_read_input_tokens": 19825,
          "cache_creation_input_tokens": 3313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3313
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

_source line 30 · 2026-05-29T06:29:54.842Z_

<details><summary>↩ Tool result · `toolu_01Efv5aQTekkHGE8GfSuhmPN`</summary>

```text
Web search results for query: "GC2PO group causal counterfactual policy optimization arXiv 2602.06475 math reasoning"

Links: [{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLMs","url":"https://arxiv.org/html/2602.06475v2"},{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning","url":"https://arxiv.org/pdf/2602.06475"},{"title":"Counterfactual Policy Optimization","url":"https://www.emergentmind.com/topics/counterfactual-policy-optimization"},{"title":"Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization","url":"https://arxiv.org/pdf/2602.09331"},{"title":"[2602.09331] Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization","url":"https://arxiv.org/abs/2602.09331"},{"title":"Causally-Enhanced Reinforcement Policy Optimization","url":"https://arxiv.org/pdf/2509.23095"}]

Based on the search results, I found detailed information about the GC²PO paper:

## Overview

Group Causal Counterfactual Policy Optimization (GC²PO) is proposed to explicitly train LLMs to learn generalizable reasoning patterns.

## The Core Problem

Existing reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization.

## Key Innovation

The core innovation is an episodic causal counterfactual reward that evaluates whether the underlying reasoning pattern is truly generalizable, rather than merely rewarding a trajectory that happens to be correct (which may rely on spurious shortcuts).

## How It Works

GC²PO operates by automatically segmenting each question-solution pair into distinct episodes, then computing a causal counterfactual reward for each episode that measures the robustness and effectiveness of the reasoning step, and finally leveraging these rewards with the outcome reward to construct token-level advantages that optimize the LLM to internalize generalizable reasoning strategies.

## The Reward Components

The episodic causal counterfactual reward jointly captures robustness (encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations) and effectiveness (enforcing sufficient variability so that the learned reasoning strategy can transfer across questions).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f830ec8a-66f7-4be0-b293-890dab7ad8ac",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "866f8e66-b57d-4002-ab15-e8ea7fc2b6d6",
  "toolUseResult": {
    "query": "GC2PO group causal counterfactual policy optimization arXiv 2602.06475 math reasoning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KCjDxpPuZMbRX9xqsANvRT",
        "content": [
          {
            "title": "Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLMs",
            "url": "https://arxiv.org/html/2602.06475v2"
          },
          {
            "title": "Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.06475"
          },
          {
            "title": "Counterfactual Policy Optimization",
            "url": "https://www.emergentmind.com/topics/counterfactual-policy-optimization"
          },
          {
            "title": "Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization",
            "url": "https://arxiv.org/pdf/2602.09331"
          },
          {
            "title": "[2602.09331] Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization",
            "url": "https://arxiv.org/abs/2602.09331"
          },
          {
            "title": "Causally-Enhanced Reinforcement Policy Optimization",
            "url": "https://arxiv.org/pdf/2509.23095"
          }
        ]
      },
      "Based on the search results, I found detailed information about the GC²PO paper:\n\n## Overview\n\nGroup Causal Counterfactual Policy Optimization (GC²PO) is proposed to explicitly train LLMs to learn generalizable reasoning patterns.\n\n## The Core Problem\n\nExisting reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization.\n\n## Key Innovation\n\nThe core innovation is an episodic causal counterfactual reward that evaluates whether the underlying reasoning pattern is truly generalizable, rather than merely rewarding a trajectory that happens to be correct (which may rely on spurious shortcuts).\n\n## How It Works\n\nGC²PO operates by automatically segmenting each question-solution pair into distinct episodes, then computing a causal counterfactual reward for each episode that measures the robustness and effectiveness of the reasoning step, and finally leveraging these rewards with the outcome reward to construct token-level advantages that optimize the LLM to internalize generalizable reasoning strategies.\n\n## The Reward Components\n\nThe episodic causal counterfactual reward jointly captures robustness (encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations) and effectiveness (enforcing sufficient variability so that the learned reasoning strategy can transfer across questions)."
    ],
    "durationSeconds": 7.279535456000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f830ec8a-66f7-4be0-b293-890dab7ad8ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-29T06:29:55.809Z_

<details><summary>↩ Tool result · `toolu_017i2xNJpBuqCncvmkWiuxrP`</summary>

```text
Web search results for query: "VAR-MATH symbolic benchmark math reasoning robustness arXiv 2507.12885"

Links: [{"title":"[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/abs/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885v1"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in ...","url":"https://arxiv.org/pdf/2507.12885"},{"title":"MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.06430"},{"title":"I-RAVEN-X: Benchmarking Generalization and Robustness of Analogical and Mathematical Reasoning in Large Language and Reasoning Models","url":"https://arxiv.org/pdf/2510.17496"}]

Based on the search results, here's what I found about VAR-MATH:

## Overview

VAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.

## Key Problem It Addresses

The framework addresses two critical shortcomings in existing evaluation protocols: benchmark contamination (because test problems are publicly available, increasing data leakage risk) and evaluation fragility (from reliance on single-instance assessments, which are sensitive to stochastic outputs and fail to capture reasoning consistency).

## Methodology

VAR-MATH converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each, enforcing consistency across structurally equivalent variants, mitigating contamination, and enhancing robustness through bootstrapped metrics.

## Key Findings

When tested on the transformed benchmarks, several 7B-parameter models that previously achieved scores ranging from 36.9 to 78.6 on AMC23 dropped to only 2.5 to 56.4 when evaluated on VAR-AMC23, indicating that much of their apparent success under conventional evaluation may stem from overfitting to benchmark-specific artifacts.

State-of-the-art models like DeepSeek-R1 and SEED-THINK maintain strong performance on AMC23 with drops below 5%, but experience notable degradation on the more difficult AIME24 and AIME25 variants, with relative drops up to 28.1%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dad57ff-d6eb-4a95-abf1-f5e8561f4490",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "5814953b-9254-439a-a170-46514d86d2c2",
  "toolUseResult": {
    "query": "VAR-MATH symbolic benchmark math reasoning robustness arXiv 2507.12885",
    "results": [
      {
        "tool_use_id": "srvtoolu_014YgxQ9pHx7eEKn8HpKxhSq",
        "content": [
          {
            "title": "[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/abs/2507.12885"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/html/2507.12885"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/html/2507.12885v1"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in ...",
            "url": "https://arxiv.org/pdf/2507.12885"
          },
          {
            "title": "MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2510.06430"
          },
          {
            "title": "I-RAVEN-X: Benchmarking Generalization and Robustness of Analogical and Mathematical Reasoning in Large Language and Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.17496"
          }
        ]
      },
      "Based on the search results, here's what I found about VAR-MATH:\n\n## Overview\n\nVAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.\n\n## Key Problem It Addresses\n\nThe framework addresses two critical shortcomings in existing evaluation protocols: benchmark contamination (because test problems are publicly available, increasing data leakage risk) and evaluation fragility (from reliance on single-instance assessments, which are sensitive to stochastic outputs and fail to capture reasoning consistency).\n\n## Methodology\n\nVAR-MATH converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each, enforcing consistency across structurally equivalent variants, mitigating contamination, and enhancing robustness through bootstrapped metrics.\n\n## Key Findings\n\nWhen tested on the transformed benchmarks, several 7B-parameter models that previously achieved scores ranging from 36.9 to 78.6 on AMC23 dropped to only 2.5 to 56.4 when evaluated on VAR-AMC23, indicating that much of their apparent success under conventional evaluation may stem from overfitting to benchmark-specific artifacts.\n\nState-of-the-art models like DeepSeek-R1 and SEED-THINK maintain strong performance on AMC23 with drops below 5%, but experience notable degradation on the more difficult AIME24 and AIME25 variants, with relative drops up to 28.1%."
    ],
    "durationSeconds": 8.475937611,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2dad57ff-d6eb-4a95-abf1-f5e8561f4490",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-29T06:29:57.237Z_

<details><summary>↩ Tool result · `toolu_013VZAktRVA5wSKN7Q2LCmLS`</summary>

```text
Web search results for query: "consistency regularization reinforcement learning LLM reasoning 2025 2026"

Links: [{"title":"Reinforcement Learning for LLM Reasoning","url":"https://www.emergentmind.com/topics/reinforcement-learning-for-llm-reasoning"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS","url":"https://www.arxiv.org/pdf/2512.21852"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Answer-Consistent Chain-of-thought Reinforcement Learning For Multi-modal Large Langauge Models","url":"https://arxiv.org/pdf/2510.10104"},{"title":"Published as a conference paper at ICLR 2025 CREAM: CONSISTENCY REGULARIZED","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8f9d459c19b59b5400ce396e0f8c23e0-Paper-Conference.pdf"}]

Based on the search results, here are the key findings related to consistency regularization, reinforcement learning, and LLM reasoning in 2025-2026:

## Consistency in Self-Rewarding RL Frameworks

Self-rewarding RL frameworks like CoVo operationalize correctness as consistency and stability across intermediate alternatives within a trajectory, with methods that measure intra-trajectory alignment and support self-supervised RL that matches or exceeds traditional supervised RL on multiple benchmarks (from June 2025).

## Regularization in RL for LLMs

Off-policy algorithms like EM Policy Gradient alternate between diverse rationale sampling and reward-guided updates, eliminating the complexity of importance weights and achieving interpretable reasoning. Additionally, token-efficient methods restrict RL updates to informative output subsequences, acting as implicit regularization and stabilizing low-parameter regime training (from April 2025).

## CREAM: Consistency Regularized Approach

A consistency regularized approach (CREAM) published at ICLR 2025 uses reference models for KL divergence regularization, representing a structured method for managing policy drift during training.

## Recent Progress in Reasoning RL

Reinforcement learning has become an indispensable component of present-day post-training pipelines for LLMs, and has played a critical role in reasoning-oriented post-training, with recent work showing that training LLMs as RL policies on verifiable reasoning tasks such as mathematics and coding leads to substantial performance improvements.

## Emerging Questions

A NeurIPS 2025 paper examining Reinforcement Learning with Verifiable Rewards (RLVR) found that while it has demonstrated notable success in enhancing reasoning performance in mathematics and programming tasks, it does not elicit fundamentally new reasoning patterns, revealing a gap between the potential of RL and actual impact of current methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f80aaa6-2879-413c-b129-c2f5fe5a1bb2",
  "isSidechain": false,
  "promptId": "099b70c8-57b9-4106-9d79-39f37ac67cd1",
  "type": "user",
  "uuid": "d59e3cb7-b9ce-4c40-b712-0264f8be0c90",
  "toolUseResult": {
    "query": "consistency regularization reinforcement learning LLM reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FdgX59SQMrNebBBTE13gXY",
        "content": [
          {
            "title": "Reinforcement Learning for LLM Reasoning",
            "url": "https://www.emergentmind.com/topics/reinforcement-learning-for-llm-reasoning"
          },
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS",
            "url": "https://www.arxiv.org/pdf/2512.21852"
          },
          {
            "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview",
            "url": "https://openreview.net/forum?id=4OsgYD7em5"
          },
          {
            "title": "The State Of LLMs 2025: Progress, Progress, and Predictions",
            "url": "https://magazine.sebastianraschka.com/p/state-of-llms-2025"
          },
          {
            "title": "Answer-Consistent Chain-of-thought Reinforcement Learning For Multi-modal Large Langauge Models",
            "url": "https://arxiv.org/pdf/2510.10104"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 CREAM: CONSISTENCY REGULARIZED",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8f9d459c19b59b5400ce396e0f8c23e0-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, here are the key findings related to consistency regularization, reinforcement learning, and LLM reasoning in 2025-2026:\n\n## Consistency in Self-Rewarding RL Frameworks\n\nSelf-rewarding RL frameworks like CoVo operationalize correctness as consistency and stability across intermediate alternatives within a trajectory, with methods that measure intra-trajectory alignment and support self-supervised RL that matches or exceeds traditional supervised RL on multiple benchmarks (from June 2025).\n\n## Regularization in RL for LLMs\n\nOff-policy algorithms like EM Policy Gradient alternate between diverse rationale sampling and reward-guided updates, eliminating the complexity of importance weights and achieving interpretable reasoning. Additionally, token-efficient methods restrict RL updates to informative output subsequences, acting as implicit regularization and stabilizing low-parameter regime training (from April 2025).\n\n## CREAM: Consistency Regularized Approach\n\nA consistency regularized approach (CREAM) published at ICLR 2025 uses reference models for KL divergence regularization, representing a structured method for managing policy drift during training.\n\n## Recent Progress in Reasoning RL\n\nReinforcement learning has become an indispensable component of present-day post-training pipelines for LLMs, and has played a critical role in reasoning-oriented post-training, with recent work showing that training LLMs as RL policies on verifiable reasoning tasks such as mathematics and coding leads to substantial performance improvements.\n\n## Emerging Questions\n\nA NeurIPS 2025 paper examining Reinforcement Learning with Verifiable Rewards (RLVR) found that while it has demonstrated notable success in enhancing reasoning performance in mathematics and programming tasks, it does not elicit fundamentally new reasoning patterns, revealing a gap between the potential of RL and actual impact of current methods."
    ],
    "durationSeconds": 9.357986094,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6f80aaa6-2879-413c-b129-c2f5fe5a1bb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-29T06:29:57.241Z_

```json
{
  "parentUuid": "d59e3cb7-b9ce-4c40-b712-0264f8be0c90",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "88b12ac8-6a6b-4f8b-aacb-25c850c2f4bb",
  "timestamp": "2026-05-29T06:29:57.241Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "88b12ac8-6a6b-4f8b-aacb-25c850c2f4bb",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---

### Assistant

_source line 36 · 2026-05-29T06:30:26.259Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the landscape. Let me synthesize my findings and evaluate this proposal.

Key observations from my research:

1. **The problem is well-documented and timely**: VAR-MATH, MATH-Perturb, GSM-Symbolic, and Robust Reasoning Benchmark all document significant performance drops (up to 55-73%) under surface perturbations. This is a recognized problem.

2. **TA-GRPO is the closest augmentation-only baseline**: It pools rewards across variants but doesn't explicitly enforce consistency. The proposal correctly identifies the "both-correct regime" limitation.


3. **ROMA shares the token-level consistency approach but operates in vision where perturbations preserve answers**, whereas the proposal's T3F mechanism directly addresses the math-specific challenge where answers actually change. **AbstRaL tackles this through input-side abstraction on simpler problems, while MACR works on the output side**, making them complementary rather than competing approaches. **COPO and GC²PO address related issues**—one through advantage redesign and the other through a related but distinct mechanism—but neither directly enforces cross-perturbation consistency the way this proposal does.

Now evaluating the proposal itself: the positioning is exceptionally strong, particularly the insight about the "both-correct regime" and the clear gap it identifies. T3F is a genuine technical innovation that solves the core math-specific problem, and the experimental rigor is impressive—seven baseline comparisons, ten ablations, and normalized compute analysis. The SymPy-verified perturbations are principled, and the contrastive discrimination loss prevents the model from learning trivial invariances.

The main limitation is that T3F's effectiveness depends on SymPy's ability to generate meaningful trajectory translations, which may break down on complex problems beyond simple algebra. The proposal acknowledges this but the fallback strategy seems underdeveloped.

There's also a deeper concern: the "both-correct regime" assumes models will reach sufficient accuracy for this regime to dominate, but at the 7B-14B scale on competition-level math like AIME, that might not happen. The practical implementation is also fragile—SymPy needs to track all intermediate values, not just final answers, across multi-step problems. And there's an unresolved tension: enforcing trajectory consistency could suppress legitimate reasoning diversity when the model finds different valid paths for original versus perturbed problems. Finally, the comparison with AbstRaL is somewhat circular—if AbstRaL is untested on competition math, that's precisely where T3F's SymPy mechanism is weakest too.

Despite these limitations, the proposal is well-structured with a novel mechanism and an exceptionally rigorous experimental plan—seven baseline tiers, compute-normalized comparisons, ten ablations, multi-seed runs. The core insight about augmentation versus consistency optimization is compelling. The main risks are whether trajectory translation holds up in practice beyond simple algebra, whether the "both-correct regime" actually materializes at this scale, and whether improvements will be meaningful given that similar augmentation approaches have shown modest gains. For AAAI 2026, the problem is timely, the method is novel, and the experimental rigor is strong, though execution risk remains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88b12ac8-6a6b-4f8b-aacb-25c850c2f4bb",
  "isSidechain": false,
  "requestId": "req_011CbWPWPM8ohd6UxkATCHJL",
  "type": "assistant",
  "uuid": "72009e32-fd43-4e8c-b0c4-d8b82b719c9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAsFqqvyhZNM7gW6YFkgZv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3298,
      "cache_read_input_tokens": 23138,
      "output_tokens": 6860,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6860,
          "cache_read_input_tokens": 23138,
          "cache_creation_input_tokens": 3298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3298
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

_source line 37 · 2026-05-29T06:32:27.632Z_

Now I have sufficient research context. Let me compile my comprehensive evaluation.

```
【阶段】: Triage

【领域调研】:
- [TA-GRPO (arXiv 2601.22478)](https://arxiv.org/abs/2601.22478) (2026): 最直接的 augmentation-only baseline。通过 cross-variant pooled advantage 获得 +9.84pp 竞赛数学提升，但无显式 consistency loss，亦无 robustness evaluation。Proposal 正确指出其 "both-correct regime" 零梯度盲区。
- [ROMA (arXiv 2605.09262)](https://arxiv.org/abs/2605.09262) (2026): 方法论最近亲。在视觉退化场景下使用 correctness-conditioned token-level KL + teacher forcing dual-forward-pass，Qwen3-VL 4B/8B 上 robustness 提升 +2.4% (seen) / +2.3% (unseen)。关键差异：视觉扰动保持答案不变，数学扰动改变答案——Proposal 的 T3F 正是为解决这一根本差异而设计。
- [AbstRaL (ICLR 2026, arXiv 2506.07751)](https://arxiv.org/abs/2506.07751): 主要竞争者。输入端机制，教模型将 GSM 问题抽象为符号表示再求解，在 GSM-Symbolic/GSM-Plus 上接近完全恢复 robustness。但仅在 GSM 级别验证，未测试竞赛级数学。Proposal 定位为输出端（约束推理策略一致性），与 AbstRaL 正交。
- [VAR-MATH (arXiv 2507.12885)](https://arxiv.org/abs/2507.12885) (2025): 诊断性 benchmark，7B 模型在 AMC23 上从 36.9-78.6 骤降至 2.5-56.4；DeepSeek-R1 在 AIME24/25 上 relative drop 高达 28.1%。证实问题的严重性与普遍性。
- [COPO (arXiv 2508.04138)](https://arxiv.org/abs/2508.04138) (2025): 通过 consistency-entropy 全局奖励解决 zero-advantage 问题，但机制是 advantage redesign 而非 cross-perturbation consistency。与 MACR 解决同一上游问题（全 correct group 梯度消失），但路径完全不同。Proposal 将其列为 baseline 是恰当的。
- [GC²PO (arXiv 2602.06475)](https://arxiv.org/abs/2602.06475) (2026): 针对 episodic causal counterfactual reward，关注单问题内推理步骤的因果鲁棒性，而非跨问题扰动不变性。互补但目标不同。
- [MATH-Perturb (ICML 2025)](https://openreview.net/forum?id=OZy70UggXr): 279 道 MATH level-5 问题的 Simple/Hard 扰动，o1-mini -16.49%，gemini-2.0-flash-thinking -12.9%。标准化的 robustness 评测协议。
- [Robust Reasoning Benchmark (arXiv 2604.08571)](https://arxiv.org/html/2604.08571v2) (2026): 14 种编码/结构扰动，发现开源模型推理路径过拟合于标准文本格式。
- [NeurIPS 2025 "Does RL Really Incentivize Reasoning?"](https://openreview.net/forum?id=4OsgYD7em5): 发现 RLVR 不产生根本性新推理模式，揭示当前 RL 方法的局限性——这对 MACR 既是挑战（RL 本身可能收益有限）也是机遇（说明需要更精细的训练信号）。

- **调研总结**: 数学推理的 perturbation robustness 是 2025-2026 年的活跃方向，诊断性工作充分（VAR-MATH、MATH-Perturb、GSM-Symbolic），但训练端修复方案稀缺——TA-GRPO/PrAg-PO 只做 augmentation，AbstRaL 只在 GSM 级别验证。"在 RL 训练中同时结合数学等价扰动和结构感知一致性正则"这一 gap 确实存在。MACR 的 T3F 机制在方法论上有清晰的 novelty claim，关键问题在于能否在竞赛级数学上实际 work。

【整体印象】:
作为审稿人，第一反应是 **borderline accept 偏向 weak accept**。这是一篇方向精准、gap identification 极为清晰、实验设计异常完备的 proposal。"Augmentation optimizes reward, consistency optimizes strategy" 的核心 insight 简洁有力且理论上站得住。T3F 机制是真正的技术创新——不是对 ROMA 的简单搬运，而是对 math ≠ vision 这一根本差异的原则性解决方案。文献定位几乎无懈可击，每个相关工作都有明确的差异化说明。实验设计的 7 层 baseline + 10 项 ablation + compute-normalized comparison 远超该领域平均水准。

但我有两个核心顾虑：(1) T3F 的实际工程鲁棒性——SymPy 对多步复杂推理的 trajectory translation 能否可靠工作？(2) "both-correct regime" 在 7B-14B 模型做竞赛级数学时是否真的 dominant——如果模型准确率本身就不高，这个 regime 可能并不常见，削弱了核心 motivation。

【核心贡献】:
1. **T3F (Trajectory-Translated Teacher Forcing)**：首次将 consistency regularization 适配到数学推理场景——通过 SymPy 引导的轨迹翻译解决答案变化下的 token-level 对齐问题。这是一个非 trivial 的技术贡献，解决了 ROMA 直接搬用到数学场景时的根本障碍。
2. **"Both-correct regime" 的分析框架**：揭示了 augmentation-only 方法（TA-GRPO）随训练推进其纠正能力递减的机制性原因，并提出 phase complementarity 作为理论解释。
3. **完整的训练框架**：SAC + contrastive discrimination + SymPy perturbation generator 构成了一个相对完整的解决方案。

贡献对领域的价值：**中等偏高**。如果 T3F 实验验证成功，这将成为 math reasoning robustness 从"诊断"到"治疗"的关键工作之一。

【方法合理性】:
整体方法设计合理，各组件有明确的技术 justification：
- **T3F 的设计动机清晰**：直接解决 naive token-level divergence 在数学场景下会惩罚正确数值差异的问题。使用 SymPy 的确定性映射实现精确位置对应，避免 DTW 等复杂对齐算法。
- **Correctness-conditioning** 借鉴 ROMA 是合理的防御性设计，避免强制"一致地错误"。
- **Contrastive discrimination loss** 防止退化不变性（模型对所有看起来相似的问题给出相同答案），设计上有必要。

**潜在替代方案的考量**：
- 更简单替代 1：直接在 TA-GRPO 基础上加 rollout-level outcome consistency（不做 T3F），即只要求相同正确率分布。这更简单，但 proposal 已经在 A9 ablation 中规划了此对比。关键是 token-level 能否比 rollout-level 提供更强的信号——这是需要实验验证的。
- 更简单替代 2：用 COPO 的 advantage redesign 解决 zero-advantage 问题，不引入 consistency loss。Proposal 也已将 COPO 列为 baseline，这是正确的。
- **T3F 的脆弱性**：对于多步推理，SymPy 需要追踪所有中间计算值（不仅是输入和输出），这在实际中可能非常脆弱。例如，当推理轨迹包含"让我先计算 2×3=6，然后..."时，trajectory translation 需要正确地将 6 映射为新问题中的对应值，这要求 SymPy 能完整追踪所有派生数值。Proposal 提到"direct derivatives"但对此追踪的具体实现细节讨论不足。

【5 维度打分】:

1. **研究问题: 强** — 数学推理的 perturbation robustness 是一个已被 VAR-MATH（7B 模型骤降至 2.5-56.4）、MATH-Perturb（o1-mini -16.49%）、Robust Reasoning Benchmark（开源模型 up to 55% drop）充分记录的严重问题。现有训练端修复仅停留在 augmentation 层面（TA-GRPO、PrAg-PO），"both-correct regime" 的分析指出了 augmentation-only 的结构性盲区。问题的重要性和时效性毋庸置疑。唯一小瑕疵：研究问题的 scope 可能受限于 SymPy 可处理的问题类型（algebra/equations），对 geometry/combinatorics 的覆盖率是一个已知但被明确承认的限制。

2. **方法与创新: 中偏强** — T3F 是真正的新机制，不是对已有方法的简单改进。它解决了将 ROMA 的 consistency regularization 从视觉搬到数学时的核心技术障碍。与 AbstRaL（输入端抽象，ICLR 2026）的正交定位清晰。与 COPO（advantage redesign）的差异化明确。**但有两个技术风险**：(a) trajectory translation 对复杂多步推理的鲁棒性未充分讨论——SymPy 追踪所有中间派生值的可行性存疑；(b) 对 expression rewriting 等非 token-level 替换的 fallback 机制（rollout-level outcome consistency）信号显著弱化，可能导致这些扰动类型下效果有限。

3. **实验设计: 强** — 这是本 proposal 最突出的优势之一。7 层 baseline（从 vanilla 到 full MACR，逐层隔离贡献）设计严谨，特别是：(a) 将 COPO 作为"解决同一上游问题但路径不同"的 baseline 体现了深入的竞品理解；(b) compute-normalized comparison（标准 GRPO 2-3x compute）直接回应了"额外 forward pass 的收益是否来自更多计算"的公平性质疑；(c) 10 项 ablation 逐步拆解每个组件贡献（T3F vs. naive JS、correctness conditioning、masking granularity），覆盖了审稿人可能提出的几乎所有 ablation 要求。分层种子策略（核心 3 seeds，sensitivity 1 seed）也是务实的。唯一不足：未规划 scaling analysis（如 14B 模型上的验证），这在 AAAI 审稿中可能被追问。

4. **可行性: 中** — 
   - SymPy perturbation generator 对 algebra/equations 是可行的，但 proposal 自己承认对 geometry/combinatorics 覆盖率有限。LLM-based fallback 的质量和效率需要额外验证。
   - T3F 中 trajectory translation 的实际实现可能比描述的更复杂——多步推理中的中间值追踪、变量重命名对代数表达式的递归替换等工程挑战不容小觑。
   - 计算预算 1,500-3,000 A100 GPU-hours 对于学术团队而言偏高但在 8×A100 集群上可管理（约 8-16 天连续运行）。
   - 依赖 verl/DAPO 基础设施是合理的，降低了基础工程风险。
   - **最大可行性风险**：T3F 在实际训练中可能因 trajectory translation 的累积误差（长推理链上的数值追踪）而需要大量调试，可能延长开发周期。

5. **写作与呈现: 强** — Proposal 的逻辑链极为清晰：问题（perturbation drops）→ 现有方案不足（augmentation only）→ 核心 insight（reward vs. strategy optimization）→ 技术挑战（math ≠ vision）→ 解决方案（T3F）→ 完整实验设计。每个组件都有明确的设计动机和 justification。Related work 的定位准确且全面，每项工作都有清晰的差异化分析。对 limitations 的主动讨论（SymPy 覆盖率、expression rewriting fallback、ROMA 差异）增强了可信度。少数可改进之处：T3F 中间值追踪的具体实现细节可更详细；"both-correct regime" 在竞赛级数学上的实际占比缺乏量化估计。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
**上行因素 (→42%)**：(1) 问题时效性极强，2025-2026 年多篇 benchmark 工作铺路但训练端修复几乎空白；(2) T3F 是真正的 novelty，不是增量改进，解决了从 vision 到 math 的核心技术障碍；(3) 实验设计远超平均水准，compute-normalized comparison 和细粒度 ablation 覆盖了主要审稿质疑；(4) 写作和定位几乎无可挑剔。

**下行因素 (→28%)**：(1) T3F 的工程复杂性可能导致实际效果不及预期——trajectory translation 在长推理链上的可靠性是未验证的假设；(2) "both-correct regime" 核心动机在 7B 模型+竞赛级数学场景下可能不成立（模型准确率本身较低，该 regime 可能不 dominant），这会削弱核心 narrative；(3) ROMA 在视觉场景下仅 +2.4% 的改善幅度暗示 consistency regularization 的实际收益可能有限，reviewers 可能质疑这是否值得额外复杂度；(4) SymPy 覆盖率限制意味着相当比例的训练数据无法使用 T3F，削弱了方法的通用性；(5) 如果 AbstRaL 在其 codebase 上的复现效果很强（虽然原文仅在 GSM 上测试），MACR 的相对优势可能被压缩。

**中位数 35% 的定位**：这是一篇方向正确、insight 清晰、实验设计完备的 solid 投稿。在 AAAI 的评审中，它有足够的 novelty 和 rigor 获得认可，但最终中稿概率取决于实验结果能否支撑 narrative——如果 T3F 相比 naive JS 和 TA-GRPO 有 clear margin（>3-5pp），概率向 42%+ 移动；如果改善 marginal（<2pp），概率向 25% 下滑。Proposal 本身（不含实验结果）处于 "solid but needs empirical validation" 的位置。

【主要风险】:
1. **T3F 的实际收益可能有限**：ROMA 在视觉场景下 consistency regularization 仅带来 +2.4% 提升。在数学场景下，由于 SymPy 覆盖率限制和 trajectory translation 的工程脆弱性，实际改善幅度可能更小。如果 ablation 显示 T3F 相比 naive JS 或 rollout-level consistency 无显著优势，核心贡献将被大幅削弱。
2. **核心 motivation 的量化缺失**："both-correct regime dominates as training progresses" 是整个方法的理论基础，但 proposal 未提供任何量化估计（例如，在 MATH 7.5K 上训练 Qwen3-8B 时，训练后期 both-correct 占比实际是多少？）。审稿人可能要求 empirical evidence 支撑这一核心假设。如果 7B 模型在竞赛级问题上准确率始终不高，both-correct regime 可能永远不会 dominant，整个 motivation 就会被质疑。

【实施评估】:
  - 计算资源: 1,500-3,000 A100 GPU-hours（约 8-16 天 8×A100 连续运行），对学术团队偏高但可管理。T3F 的 dual-forward-pass 增加约 30-50% 计算开销。
  - 数据需求: MATH train (~7.5K) + NuminaMath-TIR 子集，公开可获取。SymPy perturbation 生成需要额外工程但不需要外部数据。
  - 人工介入: 中等。SymPy perturbation generator 和 trajectory translation 的实现需要较强的符号计算工程能力。masking policy 的调试可能需要大量 case study。不需要人工标注。
  - 训练需求: 需要完整的 GRPO 训练流程 + SAC 正则化。依赖 verl/DAPO 基础设施。Qwen3-8B 单次训练 40-80 GPU-hours，总计约 37 次运行。
  - 新 Benchmark: 不需要构建新 benchmark，使用已有的 VAR-MATH、MATH-P-Simple、GSM-Symbolic 等。需要构建 SymPy perturbation pipeline 和 contrastive hard negatives。
  - 预估周期: 4-6 个月。Phase 1（SymPy perturbation + T3F 实现，6-8 周），Phase 2（核心 baseline + ablation 训练，4-6 周），Phase 3（补充实验 + 论文撰写，4-6 周）。主要不确定性在 Phase 1——T3F 的 trajectory translation 工程可能比预期更耗时。
```

Sources:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation](https://arxiv.org/abs/2605.09262)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs](https://arxiv.org/abs/2507.12885)
- [COPO: Consistency-Aware Policy Optimization](https://arxiv.org/abs/2508.04138)
- [GC²PO: Group Causal Counterfactual Policy Optimization](https://arxiv.org/abs/2602.06475)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations](https://openreview.net/forum?id=OZy70UggXr)
- [Robust Reasoning Benchmark](https://arxiv.org/html/2604.08571v2)
- [Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://openreview.net/forum?id=4OsgYD7em5)
- [Mathematical Reasoning in LLMs: Benchmarks, Architectures, Evaluation](https://arxiv.org/html/2605.19723v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72009e32-fd43-4e8c-b0c4-d8b82b719c9e",
  "isSidechain": false,
  "requestId": "req_011CbWPWPM8ohd6UxkATCHJL",
  "type": "assistant",
  "uuid": "ea8a8d6c-dcb9-4401-b009-d74773038632",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAsFqqvyhZNM7gW6YFkgZv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3298,
      "cache_read_input_tokens": 23138,
      "output_tokens": 6860,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6860,
          "cache_read_input_tokens": 23138,
          "cache_creation_input_tokens": 3298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3298
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "ea8a8d6c-dcb9-4401-b009-d74773038632",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "5652111f-4828-4e18-b653-ec09b9c576d1"
}
```

---
