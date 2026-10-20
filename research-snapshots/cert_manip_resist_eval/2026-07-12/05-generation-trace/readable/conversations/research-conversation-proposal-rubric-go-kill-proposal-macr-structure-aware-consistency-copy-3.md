# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # MACR: Structure-Aware Consistency

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/cf239bc9-74d6-4639-b18d-cd448bba6fc9.jsonl`
- **Structured JSON:** [`d7850b2a108ee9baacbc.json`](../../sessions/d7/d7850b2a108ee9baacbc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:32:25.555Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:32:25.555Z",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL\n\n## Core Problem\n\nRL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface perturbations: open-weight reasoning models drop up to 55% (Robust Reasoning Benchmark, arXiv 2604.08571), and VAR-MATH (arXiv 2507.12885) documents 47-73% drops concentrated in sub-frontier models on competition-level problems. Binary reward provides no gradient against surface-form-dependent strategies.\n\nExisting augmentation methods (TA-GRPO, arXiv 2601.22478; PrAg-PO, arXiv 2602.03190) pool rewards across equivalent variants but optimize reward, not strategy invariance. Critically, in the \"both-correct regime\" (both original and perturbed variants solved), pooled advantage yields identical signals—zero differential gradient—leaving surface-dependent reasoning strategies unrectified. This regime becomes increasingly prevalent as training progresses and model accuracy rises, meaning augmentation-only methods suffer diminishing corrective power precisely when fine-grained strategy refinement matters most. Can structure-aware consistency regularization during GRPO enforce perturbation-invariant reasoning strategies, especially in this late-training regime?\n\n## Key Insight: Augmentation Optimizes Reward, Consistency Optimizes Strategy\n\nTA-GRPO's pooled advantage provides effective learning signal when one variant is solved and the other is not (early training, lower accuracy). But as training progresses and accuracy increases, the both-correct regime dominates, and TA-GRPO's signal diminishes. MACR's explicit consistency loss fills this gap: it provides gradient even when both variants are correct, enforcing not just correct answers but structurally similar reasoning. This creates a natural phase complementarity—augmentation drives initial learning, consistency drives late-stage refinement from \"getting it right\" to \"getting it right for the right reasons.\"\n\n## Critical Technical Challenge: Math ≠ Vision for Consistency\n\nROMA (arXiv 2605.09262) achieves visual robustness via token-level KL between corrupted and clean trajectories under teacher forcing. This works because visual perturbation (blur, noise) preserves the correct answer—the same reasoning trace is valid for both views. In math, numerical substitution (2x+3=7 → 5x+2=12) changes the answer and intermediate computations. Naively applying ROMA's token-level divergence would penalize correct numerical differences alongside genuine strategy divergence.\n\nWe propose **Trajectory-Translated Teacher Forcing (T3F)** as the core mechanism for Structure-Aware Consistency (SAC):\n\n1. For original problem x, select a correct rollout trajectory τ_x from GRPO sampling.\n2. Using SymPy's known perturbation mapping M (e.g., {a=2→a=5, variable x→variable y}), mechanically translate τ_x into τ_translated by substituting corresponding numerical values and variable names. Since SymPy controls the perturbation, the mapping is exact and deterministic. τ_translated has identical length and structure to τ_x—only problem-specific values change.\n3. Teacher-force the model on perturbed input x' with prefix from τ_translated, collecting per-token logit distributions.\n4. Teacher-force the model on original input x with prefix from τ_x, collecting per-token logit distributions.\n5. Compute token-level JS divergence between the two logit distribution sequences, with numerical-token masking as secondary noise reduction.\n\nT3F resolves the alignment problem: trajectory translation creates exact position correspondence, making token-level divergence well-defined without requiring step-level alignment algorithms (e.g., DTW). The divergence directly measures: \"Given structurally identical reasoning contexts (differing only in problem-specific values), does the model assign similar probabilities to structurally corresponding next tokens?\"\n\n**Why token-level, not step-type-level?** A coarser alternative would compare only reasoning step types (e.g., \"set up equation → simplify → solve\"). But step-type consistency cannot distinguish between correct algebraic manipulation and pattern-matching shortcuts within the same step type. Token-level granularity captures intra-step strategy differences—the fine-grained signal that matters for eliminating surface heuristics.\n\n**Masking policy and boundary conditions.** Numerical token identification uses regex matching against SymPy's perturbation mapping (problem-copied values and their direct derivatives). Mathematical constants (π, e), step indices, and tokens not traceable to problem-specific values are retained in the JS computation. This conservative masking policy is sound because SymPy-controlled perturbations guarantee that only mapped values differ between τ_x and τ_translated; unmapped numerical tokens (e.g., mathematical constants shared across variants) should indeed be consistent. Limitation: for perturbation types beyond token-level substitution (e.g., expression rewriting \"a+b\" → \"b+a\"), trajectory translation may introduce structural shifts; for these, we fall back to rollout-level outcome consistency (JS over correctness distributions across K rollouts) as a coarser but robust signal.\n\n## Research Landscape\n\n**Diagnostic-only (no training fix):** VAR-MATH (arXiv 2507.12885): 47-73% drops, sub-frontier models on competition math. MATH-Perturb (ICML 2025, arXiv 2502.06453): 279 MATH level-5 problems, distinguishes solution-preserving (Simple) vs. solution-changing (Hard) perturbation. GSM-Symbolic (ICLR 2025): performance variance across instantiations, 25 models evaluated. Robust Reasoning Benchmark (arXiv 2604.08571): 14 encoding/structural perturbation types on AIME 2024, orthogonal to semantic-preserving perturbation.\n\n**Augmentation-only (no invariance objective):** TA-GRPO (arXiv 2601.22478): +9.84pp competition math via cross-variant pooled advantage, no consistency loss, no robustness evaluation. PrAg-PO (arXiv 2602.03190): prompt augmentation stabilizes GRPO, mitigates entropy collapse, no invariance objective.\n\n**Structural RL (different mechanism):** AbstRaL (ICLR 2026, arXiv 2506.07751): input-side mechanism—teaches models to abstract GSM problems into symbolic representations before solving. Achieves near-full robustness recovery on GSM variants but untested on competition-level math. MACR is output-side (constrains reasoning strategy consistency). These are orthogonal: abstraction changes how the model reads problems, consistency changes how it reasons. Potentially complementary. MathForge/DGPO (ICLR 2026): difficulty-aware GRPO, no robustness evaluation.\n\n**Causal/consistency RL (different target):** GC²PO (arXiv 2602.06475): episodic causal counterfactual reward evaluating whether reasoning steps remain stable under within-problem counterfactual perturbations—focuses on step-level causal robustness within a single problem. MACR targets cross-problem strategy invariance across semantically equivalent perturbations—a complementary but distinct objective. GRPO-CARE (arXiv 2506.16141): consistency-aware RL for video reasoning (step-answer coherence, not cross-perturbation invariance). CC-LEARN (arXiv 2506.15662): cohort consistency RL for NLU tasks. COPO (arXiv 2508.04138): consistency-entropy for zero-advantage training efficiency—addresses the same upstream problem (gradient vanishing in all-correct groups) but through advantage redesign rather than cross-perturbation consistency. DPH-RL: JS for diversity, not invariance.\n\n**Consistency regularization (different domain/setting):** ROMA (arXiv 2605.09262): correctness-conditioned token-level KL for visual corruption robustness, closest methodological cousin but operates where perturbation preserves answers. F2C (arXiv 2510.14242)/PPCL: JS-based consistency, SFT-only, NLU-only.\n\n**Gap:** No work combines math-equivalence-aware perturbation with trajectory-translated structure-aware consistency during RL training. The T3F mechanism—which resolves the fundamental math-vs-vision consistency gap via SymPy-guided trajectory translation—is the core technical novelty.\n\n## Proposed Approach\n\nMACR integrates perturbation-invariance into GRPO training on Qwen3-8B via four components:\n\n**(1) SymPy-Verified Symbolic Perturbation Generator.** Creates equivalent variants through: numerical substitution, variable renaming, expression rewriting (a+b → b+a), constraint reformulation (\"A exceeds B by 3\" → \"B is 3 less than A\"). All variants SymPy-verified for answer equivalence. Inspired by Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187). Coverage limitation: SymPy handles algebra/equation problems well but has limited coverage for geometry, combinatorics, and number theory. For non-coverable problems, LLM-based perturbation with majority-vote verification serves as fallback. We report per-topic perturbation coverage rates.\n\n**(2) Structure-Aware Consistency (SAC) via T3F.** For each (original, perturbed) pair where both are correctly solved in GRPO rollouts: apply Trajectory-Translated Teacher Forcing (detailed above) to compute token-level JS divergence over reasoning structure. Correctness-conditioning (à la ROMA) restricts enforcement to successful pairs, avoiding systematically wrong invariance. For perturbation types where trajectory translation is imprecise (expression rewriting, constraint reformulation), fall back to rollout-level outcome consistency.\n\n**(3) Contrastive Discrimination Loss.** Prevents degenerate invariance by training the model to distinguish surface-similar but semantically-different problems. Hard negatives constructed via SymPy answer-changing perturbation: modifying a coefficient/constraint so the answer changes while surface similarity is preserved. Automatically verifiable via SymPy.\n\n**(4) verl/DAPO Infrastructure.** Built on DAPO (arXiv 2025) for scalable GRPO training.\n\n## Theoretical Positioning\n\nMACR provides a lightweight process-level quality signal without step-level annotation. By requiring structurally similar reasoning on equivalent problems, SAC implicitly penalizes heuristic shortcuts: a model relying on surface pattern matching cannot consistently produce similar reasoning structures across numerically different but structurally identical problems. This positions MACR as complementary to PRM (explicit process supervision) and ORM (outcome-only)—offering process-quality pressure at zero annotation cost. This claim is offered as a secondary insight; the primary contribution is perturbation robustness.\n\n## Experimental Design\n\n**Training Data:** MATH training split (~7.5K problems) + NuminaMath-TIR subset, aligned with TA-GRPO's data regime for fair comparison. We report SymPy perturbation success rate on this training set (expected: high for algebra/equations, lower for geometry/combinatorics).\n\n**Baselines (7 tiers):**\n1. Vanilla Qwen3-8B (no RL)\n2. Standard GRPO (verl/DAPO, no augmentation or consistency)\n3. COPO (consistency-entropy advantage redesign—isolates \"fix zero-advantage\" from \"enforce cross-perturbation consistency\")\n4. TA-GRPO / PrAg-PO (augmentation-only GRPO—isolates SAC contribution)\n5. AbstRaL (abstraction + RL—direct competitor; reproduce on Qwen3-8B if feasible, otherwise use published results on shared benchmarks with explicit model-gap discussion since AbstRaL uses Llama-3/Qwen2)\n6. F2C-style generic JS consistency applied to GRPO (no math-specific perturbation or T3F—isolates math-aware design value)\n7. Full MACR\n\n**Compute-normalized comparison:** Standard GRPO with 2-3x compute budget (matched to MACR's additional forward passes) as fairness control.\n\n**Evaluation Benchmarks:**\n- Robustness (core): VAR-MATH, MATH-P-Simple (ICML 2025), GSM-Symbolic (ICLR 2025), GSM-Plus\n- Robustness (supplementary, out-of-scope for MACR): MATH-P-Hard, Robust Reasoning Benchmark (arXiv 2604.08571) — reported for completeness, no expected gains\n- Clean accuracy: MATH500, GSM8K, AIME 2024\n- OOD generalization: Minerva, OlympiadBench\n- Stratified analysis: per-topic breakdown (algebra, number theory, geometry, combinatorics) to assess SymPy coverage impact\n\n**Evaluation Metrics:**\n- Clean Accuracy: Pass@1 on standard benchmarks\n- Robust Accuracy: Pass@1 on perturbation benchmarks\n- Relative Performance Drop (RPD): (Clean − Robust) / Clean × 100%\n- Consistency Rate: fraction of templates where all instantiations correct (VAR-MATH strict)\n- Performance Variance: accuracy variance across instantiations (GSM-Symbolic style)\n- All metrics: mean ± std over 3 seeds (sensitivity analyses on 1 seed)\n\n**Ablation Study:**\n- A1: GRPO only (no augmentation, no consistency)\n- A2: GRPO + perturbation augmentation only (no consistency loss)\n- A3: GRPO + perturbation + unconditional JS (no correctness conditioning)\n- A4: GRPO + perturbation + correctness-conditioned JS without T3F (naive token-level JS, no trajectory translation)\n- A5: GRPO + perturbation + correctness-conditioned SAC via T3F (no contrastive)\n- A6: Full MACR (T3F-SAC + contrastive discrimination)\n- A7: λ sensitivity for consistency loss weight (1 seed)\n- A8: Perturbation type contribution: numerical-only vs. variable-only vs. expression-rewriting vs. all (1 seed)\n- A9: T3F teacher-forcing vs. rollout-level outcome consistency (coarse fallback)\n- A10: Masking granularity: conservative (problem-value-only) vs. aggressive (all digits) vs. no masking\n\n**Compute Estimate:** Single GRPO run on Qwen3-8B ≈ 40-80 GPU-hours on 8×A100. Core baselines (7 configs × 3 seeds = 21 runs) + key ablations (A3-A6 × 3 seeds = 12 runs) + sensitivity analyses (A7-A10 × 1 seed = 4 runs) = ~37 runs ≈ 1,500-3,000 A100 GPU-hours total. Ablation reduction strategy: A7, A8, A10 run on 1 seed for initial screening, scale to 3 seeds only for significant findings.\n\n## Key References\n\n- ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (arXiv 2605.09262, 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2507.12885, 2025)\n- AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking (ICLR 2026, arXiv 2506.07751)\n- MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations (ICML 2025, arXiv 2502.06453)\n- Robust Reasoning Benchmark (arXiv 2604.08571, 2026)\n- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478)\n- PrAg-PO: Prompt Augmentation Scales up GRPO Training (arXiv 2602.03190)\n- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)\n- DAPO: Open-Source LLM RL System at Scale (arXiv 2025)\n- F2C: Flip-Flop Consistency for Prompt Perturbation Robustness (arXiv 2510.14242, 2025)\n- GSM-Symbolic: Understanding Limitations of Math Reasoning (ICLR 2025)\n- GSM-Plus: Evaluating Robustness of LLMs as Mathematical Problem Solvers\n- GC²PO: Group Causal Counterfactual Policy Optimization (arXiv 2602.06475, 2026)\n- GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (arXiv 2506.16141)\n- COPO: Consistency-Entropy Policy Optimization (arXiv 2508.04138)\n- CC-LEARN: Cohort-based Consistency Learning (arXiv 2506.15662)\n- DPH-RL / PPCL\n- Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, 2026)\n- NuminaMath-TIR"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:32:25.558Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:32:25.558Z",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-29T06:32:25.614Z_

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
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "eadbb870-ad70-4f75-9927-6683f103aa0e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:32:25.613Z_

```json
{
  "parentUuid": "eadbb870-ad70-4f75-9927-6683f103aa0e",
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
  "uuid": "93901a73-34e9-4531-b1ad-0ecbab2766c9",
  "timestamp": "2026-05-29T06:32:25.613Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:32:25.613Z_

```json
{
  "parentUuid": "93901a73-34e9-4531-b1ad-0ecbab2766c9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0994212d-eadb-42c8-80dc-d72ba68ea79a",
  "timestamp": "2026-05-29T06:32:25.613Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
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
  "leafUuid": "0994212d-eadb-42c8-80dc-d72ba68ea79a",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:32:29.539Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. Let me first do the required web searches to understand the field, then provide my assessment.

Let me search for the key topics and papers mentioned in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0994212d-eadb-42c8-80dc-d72ba68ea79a",
  "isSidechain": false,
  "requestId": "req_011CbWPhKk9fiFtpdv9HuSXN",
  "type": "assistant",
  "uuid": "45901f46-c3a7-490b-a20d-859fdf5ad0f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUNFDoFan7ECoUdaqwWTBa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19131,
      "output_tokens": 172,
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
          "output_tokens": 172,
          "cache_read_input_tokens": 19131,
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

_source line 9 · 2026-05-29T06:32:30.623Z_

I'll start by conducting the required literature search to understand the current landscape before making any assessments. Let me run several targeted searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45901f46-c3a7-490b-a20d-859fdf5ad0f2",
  "isSidechain": false,
  "requestId": "req_011CbWPhKk9fiFtpdv9HuSXN",
  "type": "assistant",
  "uuid": "fa2739f0-2f72-4b53-b078-bb8255788e40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUNFDoFan7ECoUdaqwWTBa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19131,
      "output_tokens": 172,
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
          "output_tokens": 172,
          "cache_read_input_tokens": 19131,
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

_source line 10 · 2026-05-29T06:32:30.670Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012eN2Q7v52wojX3eYfHjZNk`</summary>

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
  "parentUuid": "fa2739f0-2f72-4b53-b078-bb8255788e40",
  "isSidechain": false,
  "requestId": "req_011CbWPhKk9fiFtpdv9HuSXN",
  "type": "assistant",
  "uuid": "67ff892d-0e4b-4219-ab65-d124c726831a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUNFDoFan7ECoUdaqwWTBa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19131,
      "output_tokens": 172,
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
          "output_tokens": 172,
          "cache_read_input_tokens": 19131,
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

_source line 11 · 2026-05-29T06:32:30.678Z_

<details><summary>↩ Tool result · `toolu_012eN2Q7v52wojX3eYfHjZNk`</summary>

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
  "parentUuid": "67ff892d-0e4b-4219-ab65-d124c726831a",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "f38e4e10-132f-4d6e-9d64-8bd78031c5c4",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "67ff892d-0e4b-4219-ab65-d124c726831a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-29T06:32:33.239Z_

Now let me run the targeted searches in parallel to understand the field:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f38e4e10-132f-4d6e-9d64-8bd78031c5c4",
  "isSidechain": false,
  "requestId": "req_011CbWPhidKB5mJ2cka44v3V",
  "type": "assistant",
  "uuid": "05ad27e4-4920-4fa0-90bc-848369dd6d61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwU6FdFpArX6AFmj27ff3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 19131,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 303,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 13 · 2026-05-29T06:32:34.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GWRUPnp4e7t6JRNUnToWrx`</summary>

```json
{
  "query": "RL math reasoning robustness perturbation GRPO consistency 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05ad27e4-4920-4fa0-90bc-848369dd6d61",
  "isSidechain": false,
  "requestId": "req_011CbWPhidKB5mJ2cka44v3V",
  "type": "assistant",
  "uuid": "e97d97ec-9004-40f1-9da6-a9d3d4ccd966",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwU6FdFpArX6AFmj27ff3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 19131,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 303,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 14 · 2026-05-29T06:32:34.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ArJfyKv9fbocT3ZhVJHYTm`</summary>

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
  "parentUuid": "e97d97ec-9004-40f1-9da6-a9d3d4ccd966",
  "isSidechain": false,
  "requestId": "req_011CbWPhidKB5mJ2cka44v3V",
  "type": "assistant",
  "uuid": "60b24751-b6f4-4d4d-84d0-d90bbaaa8b0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwU6FdFpArX6AFmj27ff3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 19131,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 303,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 15 · 2026-05-29T06:32:35.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UxDVua3nY1ywcomm1VbFqH`</summary>

```json
{
  "query": "AbstRaL abstract thinking reinforcement learning math reasoning ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60b24751-b6f4-4d4d-84d0-d90bbaaa8b0f",
  "isSidechain": false,
  "requestId": "req_011CbWPhidKB5mJ2cka44v3V",
  "type": "assistant",
  "uuid": "39376427-c288-45da-86e1-bb65d7fe65c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwU6FdFpArX6AFmj27ff3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 19131,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 303,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 16 · 2026-05-29T06:32:36.177Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D56gDYAQKGrMa411QV1fKP`</summary>

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
  "parentUuid": "39376427-c288-45da-86e1-bb65d7fe65c6",
  "isSidechain": false,
  "requestId": "req_011CbWPhidKB5mJ2cka44v3V",
  "type": "assistant",
  "uuid": "a7e69a52-e749-4b2f-aa99-95f567d5c14a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwU6FdFpArX6AFmj27ff3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 19131,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 303,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 17 · 2026-05-29T06:32:36.334Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CbLvw2RXCrbdrWt8QPaAqN`</summary>

```json
{
  "query": "COPO consistency entropy policy optimization zero advantage arXiv 2508.04138"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7e69a52-e749-4b2f-aa99-95f567d5c14a",
  "isSidechain": false,
  "requestId": "req_011CbWPhidKB5mJ2cka44v3V",
  "type": "assistant",
  "uuid": "09190394-dda3-43fd-a8f5-2c8f0301d40a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwU6FdFpArX6AFmj27ff3n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 19131,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 303,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 18 · 2026-05-29T06:32:42.051Z_

<details><summary>↩ Tool result · `toolu_01ArJfyKv9fbocT3ZhVJHYTm`</summary>

```text
Web search results for query: "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262"

Links: [{"title":"[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/abs/2605.09262"},{"title":"Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/pdf/2605.09262"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/html/2509.23322v2"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/html/2512.17532"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/pdf/2512.17532"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/pdf/2509.23322"}]

Based on the search results, here's what I found about the arXiv paper 2605.09262:

## ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation

ROMA is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance.

### Problem Address
While Reinforcement Learning has significantly advanced the reasoning capabilities of Multimodal Large Language Models (MLLMs), the resulting policies remain brittle against real-world visual degradations such as blur, compression artifacts, and low-resolution scans. Naively injecting degraded views during rollout induces reward poisoning, where perceptual occlusions trigger hallucinated trajectories and destabilize optimization.

### Key Technical Approach
A dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs. The method applies a token-level surrogate KL penalty against the worst-case augmentation, uses an auxiliary policy gradient loss anchored to clean-image advantages to prevent policy collapse, and applies correctness-conditioned regularization to restrict enforcement to successful trajectories.

### Results
On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, ROMA improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60b24751-b6f4-4d4d-84d0-d90bbaaa8b0f",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "1d1f956b-9186-40d3-b441-a042a24a8e8b",
  "toolUseResult": {
    "query": "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GN9LWd27qvrzgvCVyxUYA2",
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
      "Based on the search results, here's what I found about the arXiv paper 2605.09262:\n\n## ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation\n\nROMA is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance.\n\n### Problem Address\nWhile Reinforcement Learning has significantly advanced the reasoning capabilities of Multimodal Large Language Models (MLLMs), the resulting policies remain brittle against real-world visual degradations such as blur, compression artifacts, and low-resolution scans. Naively injecting degraded views during rollout induces reward poisoning, where perceptual occlusions trigger hallucinated trajectories and destabilize optimization.\n\n### Key Technical Approach\nA dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs. The method applies a token-level surrogate KL penalty against the worst-case augmentation, uses an auxiliary policy gradient loss anchored to clean-image advantages to prevent policy collapse, and applies correctness-conditioned regularization to restrict enforcement to successful trajectories.\n\n### Results\nOn Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, ROMA improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy."
    ],
    "durationSeconds": 7.2957353860000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "60b24751-b6f4-4d4d-84d0-d90bbaaa8b0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T06:32:42.684Z_

<details><summary>↩ Tool result · `toolu_01D56gDYAQKGrMa411QV1fKP`</summary>

```text
Web search results for query: "TA-GRPO transform augmented GRPO math reasoning arXiv 2601.22478"

Links: [{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/html/2601.22478"},{"title":"(PDF) Transform-Augmented GRPO Improves Pass@k","url":"https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/html/2602.03190v1"}]

Based on the search results, here's what I found about TA-GRPO:

## Transform-Augmented GRPO (TA-GRPO)

TA-GRPO generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.

### Problem It Addresses

GRPO suffers from two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.

### How It Works

This pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies.

### Theoretical and Empirical Results

TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift. Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).

The paper was submitted on January 30, 2026, and revised on February 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7e69a52-e749-4b2f-aa99-95f567d5c14a",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "950dd805-fd63-4852-a7c2-3d414dab71f9",
  "toolUseResult": {
    "query": "TA-GRPO transform augmented GRPO math reasoning arXiv 2601.22478",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SXVpPnZUWvJYA1VdR1Vskq",
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
      "Based on the search results, here's what I found about TA-GRPO:\n\n## Transform-Augmented GRPO (TA-GRPO)\n\nTA-GRPO generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.\n\n### Problem It Addresses\n\nGRPO suffers from two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.\n\n### How It Works\n\nThis pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies.\n\n### Theoretical and Empirical Results\n\nTA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift. Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).\n\nThe paper was submitted on January 30, 2026, and revised on February 11, 2026."
    ],
    "durationSeconds": 6.504816612999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a7e69a52-e749-4b2f-aa99-95f567d5c14a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T06:32:43.280Z_

<details><summary>↩ Tool result · `toolu_01CbLvw2RXCrbdrWt8QPaAqN`</summary>

```text
Web search results for query: "COPO consistency entropy policy optimization zero advantage arXiv 2508.04138"

Links: [{"title":"[2508.04138v1] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138v1"},{"title":"[2508.04138] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138"},{"title":"COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/html/2508.04138v1"},{"title":"COPO: Consistency-Aware Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=JkmKzsMaAu"},{"title":"COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,","url":"https://arxiv.org/pdf/2508.04138"},{"title":"COPO: Consistency-Aware Policy Optimization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/copo-consistency-aware-policy-optimization"},{"title":"Artificial Intelligence 2025","url":"https://www.arxiv.org/list/cs.AI/2025?skip=29800&show=500"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=2200&show=25"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=21075&show=25"}]

I found the paper! Here's what I found about arXiv 2508.04138:

**COPO: Consistency-Aware Policy Optimization**

The paper addresses challenges that emerged following the introduction of DeepSeek R1, which inspired interest in leveraging rule-based rewards as a low-cost alternative for computing advantage functions and guiding policy optimization.

The core problem the paper addresses is that when multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero, leading to vanishing gradients and rendering the corresponding samples ineffective for learning, ultimately limiting training efficiency and downstream performance.

**Proposed Solution:**

The authors propose a consistency-aware policy optimization framework that introduces a structured global reward based on outcome consistency, ensuring that even when model outputs show high intra-group consistency, the training process still receives meaningful learning signals. Additionally, they incorporate an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization, enabling dynamic transitions between exploration and convergence throughout training.

The paper demonstrates performance improvement of COPO over GRPO methods in mathematical reasoning tasks and conducts extensive ablation studies on various existing improvements to GRPO training schemes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09190394-dda3-43fd-a8f5-2c8f0301d40a",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "513d3a74-b8cc-4bf7-98ac-6e07f33b56d1",
  "toolUseResult": {
    "query": "COPO consistency entropy policy optimization zero advantage arXiv 2508.04138",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F94q4Z1cCShmJSLovcfQ5F",
        "content": [
          {
            "title": "[2508.04138v1] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138v1"
          },
          {
            "title": "[2508.04138] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/html/2508.04138v1"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=JkmKzsMaAu"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,",
            "url": "https://arxiv.org/pdf/2508.04138"
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
      "I found the paper! Here's what I found about arXiv 2508.04138:\n\n**COPO: Consistency-Aware Policy Optimization**\n\nThe paper addresses challenges that emerged following the introduction of DeepSeek R1, which inspired interest in leveraging rule-based rewards as a low-cost alternative for computing advantage functions and guiding policy optimization.\n\nThe core problem the paper addresses is that when multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero, leading to vanishing gradients and rendering the corresponding samples ineffective for learning, ultimately limiting training efficiency and downstream performance.\n\n**Proposed Solution:**\n\nThe authors propose a consistency-aware policy optimization framework that introduces a structured global reward based on outcome consistency, ensuring that even when model outputs show high intra-group consistency, the training process still receives meaningful learning signals. Additionally, they incorporate an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization, enabling dynamic transitions between exploration and convergence throughout training.\n\nThe paper demonstrates performance improvement of COPO over GRPO methods in mathematical reasoning tasks and conducts extensive ablation studies on various existing improvements to GRPO training schemes."
    ],
    "durationSeconds": 6.943222934999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "09190394-dda3-43fd-a8f5-2c8f0301d40a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-29T06:32:43.332Z_

<details><summary>↩ Tool result · `toolu_01UxDVua3nY1ywcomm1VbFqH`</summary>

```text
Web search results for query: "AbstRaL abstract thinking reinforcement learning math reasoning ICLR 2026"

Links: [{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/html/2506.07751v4"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"ABSTRAL: AUGMENTING LLMS' REASONING BY ...","url":"https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"},{"title":"International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-iclr-2026"},{"title":"[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/abs/2506.07751"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | OpenReview","url":"https://openreview.net/forum?id=49vo7D9LbI"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/abstral"},{"title":"Published in Transactions on Machine Learning Research (10/2025)","url":"https://openreview.net/pdf?id=Gz5HMiJLqv"}]

Based on the search results, here's what I found about AbstRaL:

## Overview

AbstRaL is a method that promotes abstract reasoning in LLMs using reinforcement learning (RL) on granular abstraction data and significantly mitigates performance degradation on recent GSM perturbation benchmarks.

## Key Approach

AbstRaL first teaches LLMs to generate mathematical abstraction of input GSM problem, and then connects the abstraction with symbolic tools to stably derive the output solution, regardless of the specific input contexts. The learning of abstraction relies on Granularly-decomposed Abstract Reasoning (GranulAR) data distilled from an oracle LLM, which integrates symbolic reasoning within socratic problem decomposition and chain-of-thought (CoT) explanations.

## Effectiveness

The abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability.

## ICLR 2026 Presentation

The paper was presented as a poster at ICLR 2026 (Poster Session 3, Pavilion 4, #4615) by Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39376427-c288-45da-86e1-bb65d7fe65c6",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "15a3424c-cf62-44b4-87f1-87b46324bfcd",
  "toolUseResult": {
    "query": "AbstRaL abstract thinking reinforcement learning math reasoning ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014gak8wQkFTdErW3jmMW1fT",
        "content": [
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/html/2506.07751v4"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/pdf/2506.07751"
          },
          {
            "title": "ABSTRAL: AUGMENTING LLMS' REASONING BY ...",
            "url": "https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"
          },
          {
            "title": "International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/updates/apple-at-iclr-2026"
          },
          {
            "title": "[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/abs/2506.07751"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | OpenReview",
            "url": "https://openreview.net/forum?id=49vo7D9LbI"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/abstral"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (10/2025)",
            "url": "https://openreview.net/pdf?id=Gz5HMiJLqv"
          }
        ]
      },
      "Based on the search results, here's what I found about AbstRaL:\n\n## Overview\n\nAbstRaL is a method that promotes abstract reasoning in LLMs using reinforcement learning (RL) on granular abstraction data and significantly mitigates performance degradation on recent GSM perturbation benchmarks.\n\n## Key Approach\n\nAbstRaL first teaches LLMs to generate mathematical abstraction of input GSM problem, and then connects the abstraction with symbolic tools to stably derive the output solution, regardless of the specific input contexts. The learning of abstraction relies on Granularly-decomposed Abstract Reasoning (GranulAR) data distilled from an oracle LLM, which integrates symbolic reasoning within socratic problem decomposition and chain-of-thought (CoT) explanations.\n\n## Effectiveness\n\nThe abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability.\n\n## ICLR 2026 Presentation\n\nThe paper was presented as a poster at ICLR 2026 (Poster Session 3, Pavilion 4, #4615) by Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe."
    ],
    "durationSeconds": 8.179930237,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "39376427-c288-45da-86e1-bb65d7fe65c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
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
  "leafUuid": "15a3424c-cf62-44b4-87f1-87b46324bfcd",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Tool result

_source line 24 · 2026-05-29T06:32:45.422Z_

<details><summary>↩ Tool result · `toolu_01GWRUPnp4e7t6JRNUnToWrx`</summary>

```text
Web search results for query: "RL math reasoning robustness perturbation GRPO consistency 2025 2026"

Links: [{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/html/2505.09655v4"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"},{"title":"Uncalibrated Reasoning: GRPO Induces Overconfidence for Stochastic Outcomes","url":"https://arxiv.org/pdf/2508.11800"},{"title":"Mitigating Think-Answer Mismatch in LLM Reasoning Through Noise-Aware Advantage Reweighting","url":"https://arxiv.org/pdf/2508.05928"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?","url":"https://arxiv.org/pdf/2602.07470"},{"title":"Geometric-Mean Policy Optimization","url":"https://arxiv.org/pdf/2507.20673"},{"title":"CoRPO: Adding a Correctness Bias to GRPO Improves Generalization","url":"https://arxiv.org/pdf/2511.04439"},{"title":"Reinforcement Learning for Reasoning in Large","url":"https://arxiv.org/pdf/2504.20571"}]

I found several highly relevant research papers on this topic. Here's a summary of the search results:

## Key Research Papers Found:

**1. DRA-GRPO: Diverse Reasoning Paths for Mathematical Reasoning**
DRA-GRPO applies across distinct model backbones and demonstrates consistent effectiveness with significant performance gains over strong baselines on five mathematical reasoning benchmarks. The paper identifies a "Diversity-Quality Inconsistency" problem where scalar correctness rewards fail to reflect diverse reasoning paths leading to the same solution.

**2. Uncalibrated Reasoning: GRPO Induces Overconfidence**
This research shows that removing group standard normalization in GRPO fixes its miscalibration and provides theoretical explanation for why normalization causes overconfidence.

**3. Mitigating Think-Answer Mismatch**
Despite GRPO's empirical success, its reliance on final-answer correctness as a proxy for reasoning quality presents a critical vulnerability, as a correct answer does not necessarily imply valid or logically sound reasoning.

**4. Transform-Augmented GRPO**
Research empirically demonstrates that RLVR primarily sharpens pre-existing capabilities rather than developing new reasoning skills, with diversity collapse being a key mechanism, and transform augmentation can counteract this by ensuring diverse correct answers appear in training rollouts.

**5. Geometric-Mean Policy Optimization (GMPO)**
GMPO improves Pass@1 accuracy by 4.1% on five mathematical reasoning benchmarks with DeepSeek-R1-Distill-Qwen-7B compared to GRPO.

**6. CoRPO: Correctness-Relative Policy Optimization**
CoRPO-trained models improve cross-domain reasoning and generalize more consistently to out-of-domain tasks, outperforming GRPO when trained on coding tasks for math problems and vice versa.

**7. Robustness to Chain-of-Thought Interventions**
Research shows that reasoning LLMs struggle to recover when the initial part of their CoT is misleading.

These papers represent recent work (2025-2026) focused on improving GRPO's robustness, consistency, and mathematical reasoning capabilities through various techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e97d97ec-9004-40f1-9da6-a9d3d4ccd966",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "094a82cc-e157-401e-9902-6c750b05207b",
  "toolUseResult": {
    "query": "RL math reasoning robustness perturbation GRPO consistency 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LujRwh3TBXr5h9RxC79qrE",
        "content": [
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2505.09655v4"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
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
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/pdf/2601.22478"
          },
          {
            "title": "Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?",
            "url": "https://arxiv.org/pdf/2602.07470"
          },
          {
            "title": "Geometric-Mean Policy Optimization",
            "url": "https://arxiv.org/pdf/2507.20673"
          },
          {
            "title": "CoRPO: Adding a Correctness Bias to GRPO Improves Generalization",
            "url": "https://arxiv.org/pdf/2511.04439"
          },
          {
            "title": "Reinforcement Learning for Reasoning in Large",
            "url": "https://arxiv.org/pdf/2504.20571"
          }
        ]
      },
      "I found several highly relevant research papers on this topic. Here's a summary of the search results:\n\n## Key Research Papers Found:\n\n**1. DRA-GRPO: Diverse Reasoning Paths for Mathematical Reasoning**\nDRA-GRPO applies across distinct model backbones and demonstrates consistent effectiveness with significant performance gains over strong baselines on five mathematical reasoning benchmarks. The paper identifies a \"Diversity-Quality Inconsistency\" problem where scalar correctness rewards fail to reflect diverse reasoning paths leading to the same solution.\n\n**2. Uncalibrated Reasoning: GRPO Induces Overconfidence**\nThis research shows that removing group standard normalization in GRPO fixes its miscalibration and provides theoretical explanation for why normalization causes overconfidence.\n\n**3. Mitigating Think-Answer Mismatch**\nDespite GRPO's empirical success, its reliance on final-answer correctness as a proxy for reasoning quality presents a critical vulnerability, as a correct answer does not necessarily imply valid or logically sound reasoning.\n\n**4. Transform-Augmented GRPO**\nResearch empirically demonstrates that RLVR primarily sharpens pre-existing capabilities rather than developing new reasoning skills, with diversity collapse being a key mechanism, and transform augmentation can counteract this by ensuring diverse correct answers appear in training rollouts.\n\n**5. Geometric-Mean Policy Optimization (GMPO)**\nGMPO improves Pass@1 accuracy by 4.1% on five mathematical reasoning benchmarks with DeepSeek-R1-Distill-Qwen-7B compared to GRPO.\n\n**6. CoRPO: Correctness-Relative Policy Optimization**\nCoRPO-trained models improve cross-domain reasoning and generalize more consistently to out-of-domain tasks, outperforming GRPO when trained on coding tasks for math problems and vice versa.\n\n**7. Robustness to Chain-of-Thought Interventions**\nResearch shows that reasoning LLMs struggle to recover when the initial part of their CoT is misleading.\n\nThese papers represent recent work (2025-2026) focused on improving GRPO's robustness, consistency, and mathematical reasoning capabilities through various techniques."
    ],
    "durationSeconds": 11.187239059999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e97d97ec-9004-40f1-9da6-a9d3d4ccd966",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T06:32:48.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CTf8yCsrqGMnDk9SjJLo7k`</summary>

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
  "parentUuid": "094a82cc-e157-401e-9902-6c750b05207b",
  "isSidechain": false,
  "requestId": "req_011CbWPinN4ui4W9P1SNxM2o",
  "type": "assistant",
  "uuid": "4f5ff75b-eacf-4857-9d40-6b63e2eb2143",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eKdGwjHmAnj29HKhV6QFs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2799,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 19831,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2799,
          "output_tokens": 180,
          "cache_read_input_tokens": 19831,
          "cache_creation_input_tokens": 1261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1261
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

_source line 26 · 2026-05-29T06:32:49.086Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F6PUb88RosjpkpcYV5CNTa`</summary>

```json
{
  "query": "GC2PO group causal counterfactual policy optimization math reasoning arXiv 2602.06475"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f5ff75b-eacf-4857-9d40-6b63e2eb2143",
  "isSidechain": false,
  "requestId": "req_011CbWPinN4ui4W9P1SNxM2o",
  "type": "assistant",
  "uuid": "cbd5dccc-70bd-4161-b5b4-e2768f616728",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eKdGwjHmAnj29HKhV6QFs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2799,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 19831,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2799,
          "output_tokens": 180,
          "cache_read_input_tokens": 19831,
          "cache_creation_input_tokens": 1261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1261
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

_source line 27 · 2026-05-29T06:32:49.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Sc5tTZ9dXFkbZSj9VKvRy`</summary>

```json
{
  "query": "math reasoning LLM robustness consistency regularization training 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbd5dccc-70bd-4161-b5b4-e2768f616728",
  "isSidechain": false,
  "requestId": "req_011CbWPinN4ui4W9P1SNxM2o",
  "type": "assistant",
  "uuid": "7f551847-eb98-4bc8-a0b8-6570245b0137",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eKdGwjHmAnj29HKhV6QFs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2799,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 19831,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2799,
          "output_tokens": 180,
          "cache_read_input_tokens": 19831,
          "cache_creation_input_tokens": 1261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1261
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

_source line 28 · 2026-05-29T06:32:56.389Z_

<details><summary>↩ Tool result · `toolu_01CTf8yCsrqGMnDk9SjJLo7k`</summary>

```text
Web search results for query: "VAR-MATH symbolic benchmark math reasoning robustness arXiv 2507.12885"

Links: [{"title":"[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/abs/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885v1"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in ...","url":"https://arxiv.org/pdf/2507.12885"},{"title":"MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.06430"},{"title":"I-RAVEN-X: Benchmarking Generalization and Robustness of Analogical and Mathematical Reasoning in Large Language and Reasoning Models","url":"https://arxiv.org/pdf/2510.17496"}]

Based on the search results, here's what I found about VAR-MATH:

## Overview

VAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.

## Purpose and Design

The framework converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each, enforcing consistency across structurally equivalent variants, mitigating contamination, and enhancing robustness through bootstrapped metrics.

## Key Findings

When RL-fine-tuned models are re-evaluated on these transformed benchmarks, their performance drops substantially. For example, several 7B-parameter models that previously achieved scores ranging from 36.9 to 78.6 on AMC23 drop to only 2.5 to 56.4 when evaluated on VAR-AMC23.

This sharp decline indicates that much of their apparent success under conventional evaluation may stem from overfitting to benchmark-specific artifacts.

State-of-the-art models such as DeepSeek-R1 and SEED-THINK maintain strong performance on AMC23, with drops below 5%, but even these frontier systems experience notable degradation on the more difficult AIME24 and AIME25 variants, with relative drops up to 28.1%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f5ff75b-eacf-4857-9d40-6b63e2eb2143",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "2404bca2-8d4a-4ef0-bf40-5cf9de65d6a0",
  "toolUseResult": {
    "query": "VAR-MATH symbolic benchmark math reasoning robustness arXiv 2507.12885",
    "results": [
      {
        "tool_use_id": "srvtoolu_013o3JhH9cUNmp3c7DUdh2c8",
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
      "Based on the search results, here's what I found about VAR-MATH:\n\n## Overview\n\nVAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.\n\n## Purpose and Design\n\nThe framework converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each, enforcing consistency across structurally equivalent variants, mitigating contamination, and enhancing robustness through bootstrapped metrics.\n\n## Key Findings\n\nWhen RL-fine-tuned models are re-evaluated on these transformed benchmarks, their performance drops substantially. For example, several 7B-parameter models that previously achieved scores ranging from 36.9 to 78.6 on AMC23 drop to only 2.5 to 56.4 when evaluated on VAR-AMC23.\n\nThis sharp decline indicates that much of their apparent success under conventional evaluation may stem from overfitting to benchmark-specific artifacts.\n\nState-of-the-art models such as DeepSeek-R1 and SEED-THINK maintain strong performance on AMC23, with drops below 5%, but even these frontier systems experience notable degradation on the more difficult AIME24 and AIME25 variants, with relative drops up to 28.1%."
    ],
    "durationSeconds": 7.779086119,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4f5ff75b-eacf-4857-9d40-6b63e2eb2143",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-29T06:32:57.310Z_

<details><summary>↩ Tool result · `toolu_01F6PUb88RosjpkpcYV5CNTa`</summary>

```text
Web search results for query: "GC2PO group causal counterfactual policy optimization math reasoning arXiv 2602.06475"

Links: [{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLMs","url":"https://arxiv.org/html/2602.06475v2"},{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning","url":"https://arxiv.org/pdf/2602.06475"},{"title":"Counterfactual Policy Optimization","url":"https://www.emergentmind.com/topics/counterfactual-policy-optimization"},{"title":"Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization","url":"https://arxiv.org/pdf/2602.09331"},{"title":"[2602.09331] Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization","url":"https://arxiv.org/abs/2602.09331"},{"title":"Causally-Enhanced Reinforcement Policy Optimization","url":"https://arxiv.org/pdf/2509.23095"}]

Based on the search results, I found detailed information about the paper you're looking for:

## Summary of GC²PO Paper (arXiv 2602.06475)

The paper proposes Group Causal Counterfactual Policy Optimization (GC²PO) to explicitly train LLMs to learn generalizable reasoning patterns.

### Key Problem
Existing reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization.

### Core Approach
The core innovation is an episodic causal counterfactual reward that instead of merely rewarding a trajectory that happens to be correct (which may rely on spurious shortcuts), evaluates whether the underlying reasoning pattern is truly generalizable.

### Method Overview
It proposes an episodic causal counterfactual reward that jointly captures (i) robustness, encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations; and (ii) effectiveness, enforcing sufficient variability so that the learned reasoning strategy can transfer across questions.

The paper was published on February 9, 2026, and aims to improve how LLMs develop reasoning capabilities by focusing on generalizable reasoning patterns rather than just getting correct answers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbd5dccc-70bd-4161-b5b4-e2768f616728",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "203cd79d-bf05-4abc-a99c-ba3eba00b861",
  "toolUseResult": {
    "query": "GC2PO group causal counterfactual policy optimization math reasoning arXiv 2602.06475",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PQWUZeScM3h15imXvwoyfD",
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
      "Based on the search results, I found detailed information about the paper you're looking for:\n\n## Summary of GC²PO Paper (arXiv 2602.06475)\n\nThe paper proposes Group Causal Counterfactual Policy Optimization (GC²PO) to explicitly train LLMs to learn generalizable reasoning patterns.\n\n### Key Problem\nExisting reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization.\n\n### Core Approach\nThe core innovation is an episodic causal counterfactual reward that instead of merely rewarding a trajectory that happens to be correct (which may rely on spurious shortcuts), evaluates whether the underlying reasoning pattern is truly generalizable.\n\n### Method Overview\nIt proposes an episodic causal counterfactual reward that jointly captures (i) robustness, encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations; and (ii) effectiveness, enforcing sufficient variability so that the learned reasoning strategy can transfer across questions.\n\nThe paper was published on February 9, 2026, and aims to improve how LLMs develop reasoning capabilities by focusing on generalizable reasoning patterns rather than just getting correct answers."
    ],
    "durationSeconds": 8.220066200000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cbd5dccc-70bd-4161-b5b4-e2768f616728",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-29T06:32:57.386Z_

<details><summary>↩ Tool result · `toolu_016Sc5tTZ9dXFkbZSj9VKvRy`</summary>

```text
Web search results for query: "math reasoning LLM robustness consistency regularization training 2026"

Links: [{"title":"How Math Training Creates LLMs That Actually Think - blog.exascale-ai.in 2026","url":"https://blog.exascale-ai.in/llms-that-actually-think/"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2509.24210"},{"title":"Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges","url":"https://arxiv.org/html/2605.19723v1"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v2"},{"title":"Preprint. Under review DOES MATH REASONING IMPROVE GENERAL LLM","url":"https://arxiv.org/pdf/2507.00432"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/pdf/2508.08833"},{"title":"enhancing llm reasoning with adversarial reinforce","url":"https://arxiv.org/pdf/2512.16917"}]

I've found several relevant research papers and articles on math reasoning in LLMs, robustness, consistency, and regularization training from 2026. Here are the key findings:

## Recent Developments (2026)

**Math Reasoning Training Approaches:**
Math-RL training boosts the capacity of LLMs to think clearly, plan, explain, and adapt. Tools like Principal Component Analysis and KL Divergence reveal that RL-trained models preserve more stable internal representations—a critical trait for knowledge retention and versatility.

**Robustness and Consistency Evaluation:**
LLMs exhibit noticeable variance when responding to different instantiations of the same question. To further test robustness and consistency, works like MetaMath and ConsisEval generate question variants via fixed rewrite rules or prompt-driven reviews.

State-of-the-art LLMs show inconsistent performance under semantics-preserving transformations and appear sensitive to superficial cues.

**Regularization and Training Paradigms:**
Curricula that randomize both symbol identities and numeric parameters during fine-tuning should become standard practice for models targeting formal reasoning domains. Additionally, alignment regularization is used to curb reward hacking in adversarial reinforcement learning approaches.

**Evaluation Challenges:**
Evaluation consistency presents challenges, as LLMs may generate different reasoning paths or error localization patterns for the same problem across multiple runs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f551847-eb98-4bc8-a0b8-6570245b0137",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "0882245a-01bc-4b16-a39b-e6540b81038b",
  "toolUseResult": {
    "query": "math reasoning LLM robustness consistency regularization training 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wnvfvhodg4xJcuNJViokHu",
        "content": [
          {
            "title": "How Math Training Creates LLMs That Actually Think - blog.exascale-ai.in 2026",
            "url": "https://blog.exascale-ai.in/llms-that-actually-think/"
          },
          {
            "title": "Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/html/2506.05038"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2509.24210"
          },
          {
            "title": "Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges",
            "url": "https://arxiv.org/html/2605.19723v1"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v2"
          },
          {
            "title": "Preprint. Under review DOES MATH REASONING IMPROVE GENERAL LLM",
            "url": "https://arxiv.org/pdf/2507.00432"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/pdf/2508.08833"
          },
          {
            "title": "enhancing llm reasoning with adversarial reinforce",
            "url": "https://arxiv.org/pdf/2512.16917"
          }
        ]
      },
      "I've found several relevant research papers and articles on math reasoning in LLMs, robustness, consistency, and regularization training from 2026. Here are the key findings:\n\n## Recent Developments (2026)\n\n**Math Reasoning Training Approaches:**\nMath-RL training boosts the capacity of LLMs to think clearly, plan, explain, and adapt. Tools like Principal Component Analysis and KL Divergence reveal that RL-trained models preserve more stable internal representations—a critical trait for knowledge retention and versatility.\n\n**Robustness and Consistency Evaluation:**\nLLMs exhibit noticeable variance when responding to different instantiations of the same question. To further test robustness and consistency, works like MetaMath and ConsisEval generate question variants via fixed rewrite rules or prompt-driven reviews.\n\nState-of-the-art LLMs show inconsistent performance under semantics-preserving transformations and appear sensitive to superficial cues.\n\n**Regularization and Training Paradigms:**\nCurricula that randomize both symbol identities and numeric parameters during fine-tuning should become standard practice for models targeting formal reasoning domains. Additionally, alignment regularization is used to curb reward hacking in adversarial reinforcement learning approaches.\n\n**Evaluation Challenges:**\nEvaluation consistency presents challenges, as LLMs may generate different reasoning paths or error localization patterns for the same problem across multiple runs."
    ],
    "durationSeconds": 7.662056665999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7f551847-eb98-4bc8-a0b8-6570245b0137",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-29T06:32:57.390Z_

```json
{
  "parentUuid": "0882245a-01bc-4b16-a39b-e6540b81038b",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3e342394-cebf-43c8-a332-f94e6d5d1a3f",
  "timestamp": "2026-05-29T06:32:57.390Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-29T06:33:00.637Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do a couple more searches to understand specific aspects better, particularly around trajectory-level consistency methods and the novelty of the T3F mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e342394-cebf-43c8-a332-f94e6d5d1a3f",
  "isSidechain": false,
  "requestId": "req_011CbWPjfUrWzHHrTSS9PVvY",
  "type": "assistant",
  "uuid": "c70fd82a-6c68-48e0-94e2-b6825687b699",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRvNGFrs83osG75oPFCb6s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 21092,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 21092,
          "cache_creation_input_tokens": 5135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5135
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

_source line 33 · 2026-05-29T06:33:01.119Z_

Let me do two more targeted searches to fully understand the competitive landscape:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c70fd82a-6c68-48e0-94e2-b6825687b699",
  "isSidechain": false,
  "requestId": "req_011CbWPjfUrWzHHrTSS9PVvY",
  "type": "assistant",
  "uuid": "e9ed29d6-aa21-467c-9aed-e56e551507fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRvNGFrs83osG75oPFCb6s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 21092,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 21092,
          "cache_creation_input_tokens": 5135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5135
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

_source line 34 · 2026-05-29T06:33:02.072Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K5jzRtK6Z43PSGsVznDw2h`</summary>

```json
{
  "query": "trajectory translation teacher forcing consistency math reasoning RL token-level divergence 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9ed29d6-aa21-467c-9aed-e56e551507fc",
  "isSidechain": false,
  "requestId": "req_011CbWPjfUrWzHHrTSS9PVvY",
  "type": "assistant",
  "uuid": "9d9bd125-01fd-475f-8159-dd96a085aaf0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRvNGFrs83osG75oPFCb6s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 21092,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 21092,
          "cache_creation_input_tokens": 5135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5135
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

_source line 35 · 2026-05-29T06:33:02.754Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015iXPWGGk3i9Z7YW4UP5FcJ`</summary>

```json
{
  "query": "F2C flip flop consistency prompt perturbation robustness JS divergence arXiv 2510.14242"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d9bd125-01fd-475f-8159-dd96a085aaf0",
  "isSidechain": false,
  "requestId": "req_011CbWPjfUrWzHHrTSS9PVvY",
  "type": "assistant",
  "uuid": "12580a83-aae6-457a-b119-545e487f4be0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRvNGFrs83osG75oPFCb6s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5135,
      "cache_read_input_tokens": 21092,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 21092,
          "cache_creation_input_tokens": 5135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5135
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "12580a83-aae6-457a-b119-545e487f4be0",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Tool result

_source line 38 · 2026-05-29T06:33:09.893Z_

<details><summary>↩ Tool result · `toolu_015iXPWGGk3i9Z7YW4UP5FcJ`</summary>

```text
Web search results for query: "F2C flip flop consistency prompt perturbation robustness JS divergence arXiv 2510.14242"

Links: [{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/html/2510.14242v1"},{"title":"[2510.14242] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/abs/2510.14242"},{"title":"[2510.14242v1] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/abs/2510.14242v1"},{"title":"Flip-Flop Consistency: Unsupervised Training for ...","url":"https://arxiv.org/pdf/2510.14242"},{"title":"Evaluating Semantic Fragility in Text-to-Audio Generation Systems Under Controlled Prompt Perturbations","url":"https://arxiv.org/html/2603.13824"},{"title":"Auto-Prompt Generation is Not Robust: Prompt Optimization Driven by Pseudo Gradient","url":"https://arxiv.org/pdf/2412.18196"},{"title":"Small Edits, Big Consequences: Telling Good from Bad Robustness in Large Language Models","url":"https://arxiv.org/pdf/2507.15868"},{"title":"Generalized Jensen-Shannon Divergence Loss for Learning with Noisy   Labels","url":"https://arxiv.org/pdf/2105.04522"}]

Based on the search results, here's information about the paper arXiv 2510.14242:

## Flip-Flop Consistency (F2C): Unsupervised Training for Robustness to Prompt Perturbations in LLMs

Large Language Models (LLMs) often produce inconsistent answers when faced with different phrasings of the same prompt. The paper proposes Flip-Flop Consistency (F²C), an unsupervised training method that improves robustness to such perturbations.

### Key Components

The first component, Consensus Cross-Entropy (CCE), uses a majority vote across prompt variations to create a hard pseudo-label. The second is a representation alignment loss that pulls lower-confidence and non-majority predictors toward the consensus established by high-confidence, majority-voting variations. The method minimizes the JS divergence among datapoints within the high-confidence consensus group, and the KL divergence between all other datapoints and that group.

### Evaluation Results

The method was evaluated on 11 datasets spanning four NLP tasks, with 4-15 prompt variations per dataset. On average, F²C raises observed agreement by 11.62%, improves mean F1 by 8.94%, and reduces performance variance across formats by 3.29%. When trained on only a subset of prompt perturbations and evaluated on held-out formats, F2C consistently improves both performance and agreement while reducing variance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12580a83-aae6-457a-b119-545e487f4be0",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "eed448e9-8010-45fe-83a9-0a1a1d36d52b",
  "toolUseResult": {
    "query": "F2C flip flop consistency prompt perturbation robustness JS divergence arXiv 2510.14242",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EcCLpFnQBj5LxuihAuSvoJ",
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
            "title": "Flip-Flop Consistency: Unsupervised Training for ...",
            "url": "https://arxiv.org/pdf/2510.14242"
          },
          {
            "title": "Evaluating Semantic Fragility in Text-to-Audio Generation Systems Under Controlled Prompt Perturbations",
            "url": "https://arxiv.org/html/2603.13824"
          },
          {
            "title": "Auto-Prompt Generation is Not Robust: Prompt Optimization Driven by Pseudo Gradient",
            "url": "https://arxiv.org/pdf/2412.18196"
          },
          {
            "title": "Small Edits, Big Consequences: Telling Good from Bad Robustness in Large Language Models",
            "url": "https://arxiv.org/pdf/2507.15868"
          },
          {
            "title": "Generalized Jensen-Shannon Divergence Loss for Learning with Noisy   Labels",
            "url": "https://arxiv.org/pdf/2105.04522"
          }
        ]
      },
      "Based on the search results, here's information about the paper arXiv 2510.14242:\n\n## Flip-Flop Consistency (F2C): Unsupervised Training for Robustness to Prompt Perturbations in LLMs\n\nLarge Language Models (LLMs) often produce inconsistent answers when faced with different phrasings of the same prompt. The paper proposes Flip-Flop Consistency (F²C), an unsupervised training method that improves robustness to such perturbations.\n\n### Key Components\n\nThe first component, Consensus Cross-Entropy (CCE), uses a majority vote across prompt variations to create a hard pseudo-label. The second is a representation alignment loss that pulls lower-confidence and non-majority predictors toward the consensus established by high-confidence, majority-voting variations. The method minimizes the JS divergence among datapoints within the high-confidence consensus group, and the KL divergence between all other datapoints and that group.\n\n### Evaluation Results\n\nThe method was evaluated on 11 datasets spanning four NLP tasks, with 4-15 prompt variations per dataset. On average, F²C raises observed agreement by 11.62%, improves mean F1 by 8.94%, and reduces performance variance across formats by 3.29%. When trained on only a subset of prompt perturbations and evaluated on held-out formats, F2C consistently improves both performance and agreement while reducing variance."
    ],
    "durationSeconds": 7.135352722999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "12580a83-aae6-457a-b119-545e487f4be0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-29T06:33:10.574Z_

<details><summary>↩ Tool result · `toolu_01K5jzRtK6Z43PSGsVznDw2h`</summary>

```text
Web search results for query: "trajectory translation teacher forcing consistency math reasoning RL token-level divergence 2025 2026"

Links: [{"title":"Preprint. A Survey of On-Policy Distillation for Large Language Models","url":"https://arxiv.org/pdf/2604.00626"},{"title":"From Expert Trajectories to Step-wise Reasoning","url":"https://arxiv.org/pdf/2510.25992"},{"title":"Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM Reasoning","url":"https://arxiv.org/html/2507.00432v1"},{"title":"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning","url":"https://arxiv.org/pdf/2602.04391"},{"title":"Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs","url":"https://arxiv.org/pdf/2603.22446"},{"title":"Entropy-Aware On-Policy Distillation of Language Models","url":"https://arxiv.org/pdf/2603.07079"},{"title":"Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models","url":"https://arxiv.org/pdf/2601.18734"},{"title":"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals","url":"https://arxiv.org/pdf/2604.05655"}]

I found several relevant research papers from 2025-2026 related to your search query. Here's a summary of the key findings:

**Token-Level Divergence and RL Fine-Tuning:**

Recent research provides token-level analysis of distributional shifts in RLVR fine-tuning, examining how RLVR reshapes the token-level predictive distributions of a base model. RL fine-tuning induces sparse distributional shifts where divergence between base and RL token distributions remains near zero at most positions, with only a small subset of tokens exhibiting substantial changes.

**Teacher Forcing and Consistency:**

White-box logit access enables exact token-level divergence computation, supporting methods such as DistiLLM, G-OPD, and cross-tokenizer approaches. Reverse KL is a mode-seeking objective that reduces student diversity and yields unstable learning signals at positions where the teacher distribution has high entropy, which is particularly problematic in reasoning tasks where high-entropy tokens often represent key decision points.

**Trajectory Translation and Math Reasoning:**

Large language models have made progress through supervised fine-tuning on high-quality solution trajectories using rejection sampling, which performs supervised training on filtered sets of correct trajectories. DAPO introduces a token-level loss and relaxes the policy update constraint.

**RL vs. SFT Approaches:**

Models fine-tuned using reinforcement learning exhibit much stronger generalization to non-math tasks than those trained with supervised fine-tuning, which often show signs of catastrophic forgetting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d9bd125-01fd-475f-8159-dd96a085aaf0",
  "isSidechain": false,
  "promptId": "c33d28b7-7ba6-4b68-95ec-622079951989",
  "type": "user",
  "uuid": "36d4b9e3-43ac-4d77-8527-779a79b413c7",
  "toolUseResult": {
    "query": "trajectory translation teacher forcing consistency math reasoning RL token-level divergence 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WeJXL9BnGkj3zrLVKzGL6n",
        "content": [
          {
            "title": "Preprint. A Survey of On-Policy Distillation for Large Language Models",
            "url": "https://arxiv.org/pdf/2604.00626"
          },
          {
            "title": "From Expert Trajectories to Step-wise Reasoning",
            "url": "https://arxiv.org/pdf/2510.25992"
          },
          {
            "title": "Does Math Reasoning Improve General LLM Capabilities? Understanding Transferability of LLM Reasoning",
            "url": "https://arxiv.org/html/2507.00432v1"
          },
          {
            "title": "Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2602.04391"
          },
          {
            "title": "Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs",
            "url": "https://arxiv.org/pdf/2603.22446"
          },
          {
            "title": "Entropy-Aware On-Policy Distillation of Language Models",
            "url": "https://arxiv.org/pdf/2603.07079"
          },
          {
            "title": "Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models",
            "url": "https://arxiv.org/pdf/2601.18734"
          },
          {
            "title": "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals",
            "url": "https://arxiv.org/pdf/2604.05655"
          }
        ]
      },
      "I found several relevant research papers from 2025-2026 related to your search query. Here's a summary of the key findings:\n\n**Token-Level Divergence and RL Fine-Tuning:**\n\nRecent research provides token-level analysis of distributional shifts in RLVR fine-tuning, examining how RLVR reshapes the token-level predictive distributions of a base model. RL fine-tuning induces sparse distributional shifts where divergence between base and RL token distributions remains near zero at most positions, with only a small subset of tokens exhibiting substantial changes.\n\n**Teacher Forcing and Consistency:**\n\nWhite-box logit access enables exact token-level divergence computation, supporting methods such as DistiLLM, G-OPD, and cross-tokenizer approaches. Reverse KL is a mode-seeking objective that reduces student diversity and yields unstable learning signals at positions where the teacher distribution has high entropy, which is particularly problematic in reasoning tasks where high-entropy tokens often represent key decision points.\n\n**Trajectory Translation and Math Reasoning:**\n\nLarge language models have made progress through supervised fine-tuning on high-quality solution trajectories using rejection sampling, which performs supervised training on filtered sets of correct trajectories. DAPO introduces a token-level loss and relaxes the policy update constraint.\n\n**RL vs. SFT Approaches:**\n\nModels fine-tuned using reinforcement learning exhibit much stronger generalization to non-math tasks than those trained with supervised fine-tuning, which often show signs of catastrophic forgetting."
    ],
    "durationSeconds": 8.498128820999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9d9bd125-01fd-475f-8159-dd96a085aaf0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-29T06:33:39.177Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient information to do a thorough assessment. Let me synthesize everything I've learned and provide a comprehensive evaluation.

Let me think through the key dimensions:

**Research Problem:**
The problem of RL-trained math reasoners being brittle to surface perturbations is well-documented (VAR-MATH, MATH-Perturb, GSM-Symbolic, Robust Reasoning Benchmark). The proposal correctly identifies that existing augmentation methods (TA-GRPO, PrAg-PO) don't explicitly optimize for strategy invariance. This is a real and timely problem.
 
**Core Novelty - T3F (Trajectory-Translated Teacher Forcing):**
The key insight here is that math problems differ fundamentally from vision tasks—perturbations change the actual answer, so simple token-level consistency approaches fail. T3F leverages SymPy to automatically map correct trajectories from original problems to perturbed ones, enabling precise token-level divergence measurement. This is genuinely novel compared to prior work like ROMA, which only handles answer-preserving perturbations, or F2C, which applies JS divergence only in supervised settings.

**Method Soundness:**
T3F is elegant but has real limitations. SymPy's coverage is restricted to algebra and equations, with a weaker LLM-based fallback for other domains. The assumption that solution structure stays identical across perturbations holds for numerical substitution but breaks down with expression rewriting. The numerical token masking is sensible in theory but could be finicky in practice. The contrastive discrimination loss helps avoid trivial solutions, which is a solid safeguard.

**Experimental Design:**
The evaluation is comprehensive with seven baselines including compute-normalized comparisons.

The ablations span A1-A10, multiple benchmarks test robustness and out-of-distribution performance, and they're running three seeds with stratified per-topic analysis. The baseline selection is solid—vanilla RL, standard GRPO, COPO, TA-GRPO, AbstRaL, and generic JS variants give good coverage.

**Potential Weaknesses:**
SymPy's domain restriction is a genuine constraint that could limit applicability beyond algebra. The "both-correct regime" is the paper's core claim but remains empirically unvalidated—how prevalent is this regime actually? The method adds computational cost through extra teacher-forcing passes, and while trajectory translation is deterministic given the perturbation mapping, there's an open question about robustness when the mapping itself is uncertain.

**Strengths:**
The problem is well-motivated and the insight about the both-correct regime is compelling. T3F introduces a genuinely novel mechanism addressing a real technical gap. The experimental setup is thorough with strong baselines and comprehensive ablations. The positioning against ROMA, TA-GRPO, and AbstRaL is clear.

**Assessment:**
This is a solid proposal with real motivation and a technically sound method, though the main concerns are whether SymPy coverage limits generality, whether gains over TA-GRPO plus COPO combined will be meaningful, and whether the added complexity is justified.

I'm placing this around 35-45% probability. The proposal is well-constructed with genuine novelty and the experimental design is a major strength, but the SymPy limitations and method complexity are real concerns. The ablation study will be critical to demonstrate that all four components are actually necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36d4b9e3-43ac-4d77-8527-779a79b413c7",
  "isSidechain": false,
  "requestId": "req_011CbWPkdu8sq5L2Hu3RxpbV",
  "type": "assistant",
  "uuid": "676cdf72-3b76-42ba-93e7-0fe6f6422124",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qaod9RNM5iVyfmPT8s5XtB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 801,
      "cache_creation_input_tokens": 952,
      "cache_read_input_tokens": 26227,
      "output_tokens": 5812,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 952,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 801,
          "output_tokens": 5812,
          "cache_read_input_tokens": 26227,
          "cache_creation_input_tokens": 952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 952
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

_source line 41 · 2026-05-29T06:35:23.446Z_

Now I have sufficient information to provide a thorough assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [VAR-MATH (arXiv 2507.12885)](https://arxiv.org/abs/2507.12885) (2025): 核心诊断基准，7B模型在AMC23上从36.9-78.6骤降至2.5-56.4，DeepSeek-R1在AIME上相对下降达28.1%。直接验证了proposal所述问题的严重性。
- [TA-GRPO (arXiv 2601.22478)](https://arxiv.org/abs/2601.22478) (2026): 最直接的前置工作。通过跨变体pooled advantage实现+9.84pp竞赛数学提升，但无一致性损失、无鲁棒性评估。Proposal正确指出其在"both-correct regime"下梯度信号消失的局限性。
- [AbstRaL (arXiv 2506.07751, ICLR 2026)](https://arxiv.org/abs/2506.07751): 输入侧机制——教模型先抽象再求解，在GSM变体上接近完全恢复。ICLR 2026 poster，Apple/EPFL合作。但仅在GSM级别验证，未测试竞赛数学。Proposal正确将其定位为正交互补方法。
- [ROMA (arXiv 2605.09262)](https://arxiv.org/abs/2605.09262) (2026): 方法论上最近的"表亲"。视觉退化场景下的token-level KL一致性+teacher forcing双前向传播。在Qwen3-VL上鲁棒性+2.4%。Proposal的T3F直接回应了"数学≠视觉"的核心技术挑战。
- [COPO (arXiv 2508.04138)](https://arxiv.org/abs/2508.04138) (2025): 通过consistency-entropy重设计advantage解决零梯度问题。与MACR解决同一上游问题（all-correct group梯度消失），但通过advantage redesign而非跨扰动一致性。Proposal将其作为baseline是合理的。
- [GC²PO (arXiv 2602.06475)](https://arxiv.org/abs/2602.06475) (2026): 因果反事实奖励，评估推理步骤在问题内反事实扰动下的稳定性。关注单问题内因果鲁棒性，与MACR的跨问题策略不变性互补但不同。
- [F2C (arXiv 2510.14242)](https://arxiv.org/abs/2510.14242) (2025): JS-based一致性，SFT-only，NLU任务。Agreement提升11.62%，F1提升8.94%。仅限分类/NLU，未涉及生成式推理或RL训练。
- [DRA-GRPO (arXiv 2505.09655)](https://arxiv.org/abs/2505.09655) (2025): 识别GRPO的"Diversity-Quality Inconsistency"问题，通过多样推理路径改善。关注多样性而非鲁棒性，但揭示了GRPO训练的另一个failure mode。

- **调研总结**: 数学推理鲁棒性是2025-2026年的热点问题，诊断工具（VAR-MATH, MATH-Perturb, GSM-Symbolic）已经成熟，但训练端的修复方案仍处于早期阶段。TA-GRPO/PrAg-PO提供了增强但无不变性目标；AbstRaL走输入抽象路线但仅限GSM；COPO解决零梯度但不针对跨扰动一致性。Proposal的T3F机制——通过SymPy引导的轨迹翻译实现数学场景下的token-level一致性——在已有工作中没有直接竞争者，novelty claim基本成立。

【整体印象】: 
作为审稿人，我的第一反应是**cautious positive**。这是一篇问题定义清晰、技术路线有独创性、实验设计全面的proposal。核心贡献T3F（Trajectory-Translated Teacher Forcing）巧妙地解决了"数学扰动改变答案因此不能直接做token-level一致性"这个真实的技术难题，且与ROMA（视觉场景）形成了清晰的方法论对比。research landscape的梳理非常扎实，positioning准确。

但我会有几个关键担忧：(1) SymPy覆盖率限制使方法在几何、组合、数论上的适用性存疑；(2) "both-correct regime dominates as training progresses"这个核心动机需要实验验证而非仅靠推理论证；(3) 四个组件的系统较为复杂，ablation需要清晰证明每个都不可或缺。整体而言，如果实验结果达到预期（在竞赛数学上相对TA-GRPO有显著鲁棒性提升），这篇论文有接收潜力。

【核心贡献】: 
核心贡献是T3F（Trajectory-Translated Teacher Forcing）机制及其在GRPO训练中的集成。T3F通过SymPy的确定性扰动映射将原题的正确推理轨迹机械翻译为扰动题的对应轨迹，使得token-level JS散度可以直接衡量"在结构相同的推理上下文中，模型是否对结构对应的下一个token赋予相似概率"。这解决了数学一致性正则化中答案变化导致的position alignment问题，是相对于ROMA（视觉，答案不变）和F2C（SFT，NLU）的明确技术推进。

对领域的价值：中等偏高。如果方法有效，它填补了"增强驱动学习 → 一致性驱动精细化"的phase complementarity空白，且零标注成本的过程级质量信号是一个吸引人的附加价值。但价值受限于SymPy的问题覆盖范围。

【方法合理性】: 
方法总体合理，逻辑链条清晰：SymPy生成等价变体 → 正确轨迹翻译 → teacher-forcing收集logit → masked JS散度 → 梯度信号。

**合理之处：**
- Teacher forcing避免了在扰动输入上重新rollout（避免reward poisoning，与ROMA同思路）
- 正确性条件（correctness-conditioning）限制在双正确对上执行，避免强制错误的不变性
- 对比辨别损失防止退化不变性（表面相似但语义不同的问题）
- Fallback机制（expression rewriting用rollout-level outcome consistency）承认了T3F的适用边界

**需要关注的问题：**
- T3F隐含假设：同一解题策略应产生结构相同的推理轨迹。但对于某些问题，不同数值可能导致合理的不同解法路径（如某些值允许特殊化简）。这时T3F可能会惩罚合理的策略适应。
- 数值token masking的regex策略在复杂推理链中可能不够鲁棒（嵌套计算的中间值追踪）
- 能否有更简单的替代方案？例如：仅在rollout层面要求跨变体的正确率一致性（proposal中的A9 ablation），如果这已经足够有效，T3F的额外复杂度就不justified。这是ablation必须回答的关键问题。

【5 维度打分】:

  1. 研究问题: 【强】 — 数学推理鲁棒性是经VAR-MATH、MATH-Perturb、GSM-Symbolic等多个独立基准证实的真实问题。RL训练的7B-14B模型在表面扰动下准确率下降47-73%（VAR-MATH），这对模型的实际可靠部署构成严重障碍。Proposal进一步细化到"both-correct regime下现有增强方法的梯度信号消失"这个具体gap，问题定义精准。

  2. 方法与创新: 【中偏强】 — T3F机制是genuinely novel的：调研中未发现任何工作将SymPy引导的轨迹翻译与token-level一致性结合用于RL训练。与ROMA（视觉，答案不变）的对比清晰地说明了为什么需要trajectory translation。但创新主要是技术层面的（"如何在数学场景下实现token-level一致性"），而非概念层面的突破（一致性正则化本身是已有思路）。SymPy覆盖率限制也削弱了方法的通用性。与TA-GRPO相比，MACR增加了显著的方法复杂度，需要实验验证这种复杂度是否justified。

  3. 实验设计: 【强】 — 这是proposal的一大亮点。7层baseline设计极为全面，特别是包含了COPO（同一上游问题的不同解法）、compute-normalized control（公平性控制）、和F2C-style generic JS（隔离math-aware设计的价值）。10项ablation覆盖了几乎所有关键设计选择。评测基准覆盖鲁棒性（VAR-MATH, MATH-P-Simple, GSM-Symbolic）、清洁准确率（MATH500, GSM8K, AIME）和OOD泛化（Minerva, OlympiadBench），且明智地将MATH-P-Hard和Robust Reasoning Benchmark标注为supplementary。3 seeds + 1 seed敏感性分析的策略务实合理。

  4. 可行性: 【中】 — 1,500-3,000 A100 GPU-hours的计算需求合理（约2-4周8×A100）。但有几个实施风险：(a) SymPy轨迹翻译在复杂推理链上的可靠性需要验证——中间计算值的映射可能在长链推理中出错；(b) AbstRaL baseline的复现可能有困难（不同模型架构、数据regime），proposal也承认了这一点；(c) 数值token masking的regex策略在实际CoT中可能需要大量工程调试。总体可行但有moderate实施风险。

  5. 写作与呈现: 【强】 — Proposal的写作质量很高。问题动机的论证有逻辑层次（诊断 → 现有方案的局限 → 具体gap → 解决方案）；"Math ≠ Vision for Consistency"这个framing非常有效；research landscape的分类（diagnostic-only / augmentation-only / structural RL / causal-consistency RL / consistency regularization）清晰且全面；方法的四个组件有明确的分工。limitation的讨论（SymPy覆盖率、表达式改写的fallback）也体现了学术诚实。

【概率估计】: [30% - 45%] 中位 37%

【估计理由】: 
这是一篇在问题定义、方法新颖性、实验设计三个维度上都达到solid水平的proposal。T3F机制确实填补了一个有意义的技术空白（数学场景下的token-level一致性），且实验设计的全面性（7 baselines, 10 ablations, compute-normalized control）远超一般投稿。

将中位估计定在37%而非更高的原因：
(1) **核心novelty是"技术解决方案"而非"概念突破"**——一致性正则化是已有思路，T3F是使其在数学场景下可行的工程性创新，审稿人可能认为conceptual contribution有限；
(2) **SymPy覆盖率天花板**——方法的核心依赖SymPy的确定性映射，在几何/组合/数论上的适用性受限，这显著限制了方法的generality，而AAAI审稿人通常重视方法的通用性；
(3) **竞争激烈且时间窗口紧**——AbstRaL（ICLR 2026）、TA-GRPO、COPO、GC²PO等近期工作快速推进，到提交时可能出现更多竞争者；
(4) **实验结果的不确定性**——T3F相对于更简单替代方案（仅rollout-level一致性）的增量效果未知，如果ablation中A9（无T3F的outcome consistency）已经很强，T3F的marginal gain可能不足以justify其复杂度。

上界45%的条件：实验显示T3F在竞赛数学上相对TA-GRPO取得显著鲁棒性提升（RPD降低>10pp），且ablation清晰证明T3F不可替代。下界30%的情景：T3F增量效果有限，或SymPy覆盖率问题导致方法仅在algebra子集上有效。

【主要风险】: 
1. **T3F的marginal value不确定**: 如果更简单的rollout-level outcome consistency（ablation A9）已能提供足够的一致性信号，T3F的复杂度（轨迹翻译、数值masking、teacher forcing开销）将被审稿人质疑为over-engineering。这是最大的实验风险。
2. **SymPy覆盖率限制generality**: 方法的核心机制只在SymPy可处理的代数/方程问题上完整运作，几何/组合/数论退回到粗粒度fallback。审稿人可能认为这不是一个general-purpose solution而仅是一个domain-specific trick，从而降低评价。

【实施评估】:
  - 计算资源: ~1,500-3,000 A100 GPU-hours（≈8×A100运行2-4周），含37次训练run。中等规模，对大多数研究组可行。
  - 数据需求: MATH训练集（~7.5K）+ NuminaMath-TIR子集，均为公开数据。SymPy扰动生成需要工程实现但无额外数据采集。
  - 人工介入: 低。SymPy扰动自动生成，评测基准公开，pipeline高度自动化。主要人工成本在数值token masking策略的调试和SymPy perturbation generator的工程实现。
  - 训练需求: 需要从头训练/微调Qwen3-8B的GRPO。每次run约40-80 GPU-hours。不需要预训练但需要完整的RL训练loop。
  - 新 Benchmark: 不需要构建新benchmark，使用现有VAR-MATH、MATH-Perturb、GSM-Symbolic等。需要为训练集构建SymPy扰动变体（工程工作但非新benchmark）。
  - 预估周期: 6-10周（2-3周基础设施搭建含SymPy generator和verl/DAPO集成 + 3-5周训练runs + 1-2周分析和写作）。关键路径在SymPy轨迹翻译的工程实现可靠性验证。
```

Sources:
- [VAR-MATH: Probing True Mathematical Reasoning](https://arxiv.org/abs/2507.12885)
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation](https://arxiv.org/abs/2605.09262)
- [COPO: Consistency-Aware Policy Optimization](https://arxiv.org/abs/2508.04138)
- [GC²PO: Towards Generalizable Reasoning](https://arxiv.org/abs/2602.06475)
- [F2C: Flip-Flop Consistency](https://arxiv.org/abs/2510.14242)
- [DRA-GRPO: Diverse Reasoning Paths](https://arxiv.org/abs/2505.09655)
- [MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations](https://arxiv.org/abs/2502.06453)
- [GSM-Symbolic: Understanding Limitations of Math Reasoning](https://arxiv.org/abs/2410.05229)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "676cdf72-3b76-42ba-93e7-0fe6f6422124",
  "isSidechain": false,
  "requestId": "req_011CbWPkdu8sq5L2Hu3RxpbV",
  "type": "assistant",
  "uuid": "8938a914-35c6-4cd1-ae12-509112058c64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qaod9RNM5iVyfmPT8s5XtB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 801,
      "cache_creation_input_tokens": 952,
      "cache_read_input_tokens": 26227,
      "output_tokens": 5812,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 952,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 801,
          "output_tokens": 5812,
          "cache_read_input_tokens": 26227,
          "cache_creation_input_tokens": 952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 952
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "8938a914-35c6-4cd1-ae12-509112058c64",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "8938a914-35c6-4cd1-ae12-509112058c64",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for math reasoning robustness",
  "sessionId": "cf239bc9-74d6-4639-b18d-cd448bba6fc9"
}
```

---
