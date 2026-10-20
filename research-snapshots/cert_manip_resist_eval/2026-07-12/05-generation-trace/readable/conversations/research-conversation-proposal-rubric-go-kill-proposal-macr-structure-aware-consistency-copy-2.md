# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # MACR: Structure-Aware Consistency

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/93b40c1c-70c3-4300-8789-dd9ef02b9c73.jsonl`
- **Structured JSON:** [`35589d248a8103157cb0.json`](../../sessions/35/35589d248a8103157cb0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:29:16.327Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:29:16.327Z",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL\n\n## Core Problem\n\nRL-trained math reasoners (7B-14B scale) suffer severe accuracy drops under surface perturbations: open-weight reasoning models drop up to 55% (Robust Reasoning Benchmark, arXiv 2604.08571), and VAR-MATH (arXiv 2507.12885) documents 47-73% drops concentrated in sub-frontier models on competition-level problems. Binary reward provides no gradient against surface-form-dependent strategies.\n\nExisting augmentation methods (TA-GRPO, arXiv 2601.22478; PrAg-PO, arXiv 2602.03190) pool rewards across equivalent variants but optimize reward, not strategy invariance. Critically, in the \"both-correct regime\" (both original and perturbed variants solved), pooled advantage yields identical signals—zero differential gradient—leaving surface-dependent reasoning strategies unrectified. This regime becomes increasingly prevalent as training progresses and model accuracy rises, meaning augmentation-only methods suffer diminishing corrective power precisely when fine-grained strategy refinement matters most. Can structure-aware consistency regularization during GRPO enforce perturbation-invariant reasoning strategies, especially in this late-training regime?\n\n## Key Insight: Augmentation Optimizes Reward, Consistency Optimizes Strategy\n\nTA-GRPO's pooled advantage provides effective learning signal when one variant is solved and the other is not (early training, lower accuracy). But as training progresses and accuracy increases, the both-correct regime dominates, and TA-GRPO's signal diminishes. MACR's explicit consistency loss fills this gap: it provides gradient even when both variants are correct, enforcing not just correct answers but structurally similar reasoning. This creates a natural phase complementarity—augmentation drives initial learning, consistency drives late-stage refinement from \"getting it right\" to \"getting it right for the right reasons.\"\n\n## Critical Technical Challenge: Math ≠ Vision for Consistency\n\nROMA (arXiv 2605.09262) achieves visual robustness via token-level KL between corrupted and clean trajectories under teacher forcing. This works because visual perturbation (blur, noise) preserves the correct answer—the same reasoning trace is valid for both views. In math, numerical substitution (2x+3=7 → 5x+2=12) changes the answer and intermediate computations. Naively applying ROMA's token-level divergence would penalize correct numerical differences alongside genuine strategy divergence.\n\nWe propose **Trajectory-Translated Teacher Forcing (T3F)** as the core mechanism for Structure-Aware Consistency (SAC):\n\n1. For original problem x, select a correct rollout trajectory τ_x from GRPO sampling.\n2. Using SymPy's known perturbation mapping M (e.g., {a=2→a=5, variable x→variable y}), mechanically translate τ_x into τ_translated by substituting corresponding numerical values and variable names. Since SymPy controls the perturbation, the mapping is exact and deterministic. τ_translated has identical length and structure to τ_x—only problem-specific values change.\n3. Teacher-force the model on perturbed input x' with prefix from τ_translated, collecting per-token logit distributions.\n4. Teacher-force the model on original input x with prefix from τ_x, collecting per-token logit distributions.\n5. Compute token-level JS divergence between the two logit distribution sequences, with numerical-token masking as secondary noise reduction.\n\nT3F resolves the alignment problem: trajectory translation creates exact position correspondence, making token-level divergence well-defined without requiring step-level alignment algorithms (e.g., DTW). The divergence directly measures: \"Given structurally identical reasoning contexts (differing only in problem-specific values), does the model assign similar probabilities to structurally corresponding next tokens?\"\n\n**Why token-level, not step-type-level?** A coarser alternative would compare only reasoning step types (e.g., \"set up equation → simplify → solve\"). But step-type consistency cannot distinguish between correct algebraic manipulation and pattern-matching shortcuts within the same step type. Token-level granularity captures intra-step strategy differences—the fine-grained signal that matters for eliminating surface heuristics.\n\n**Masking policy and boundary conditions.** Numerical token identification uses regex matching against SymPy's perturbation mapping (problem-copied values and their direct derivatives). Mathematical constants (π, e), step indices, and tokens not traceable to problem-specific values are retained in the JS computation. This conservative masking policy is sound because SymPy-controlled perturbations guarantee that only mapped values differ between τ_x and τ_translated; unmapped numerical tokens (e.g., mathematical constants shared across variants) should indeed be consistent. Limitation: for perturbation types beyond token-level substitution (e.g., expression rewriting \"a+b\" → \"b+a\"), trajectory translation may introduce structural shifts; for these, we fall back to rollout-level outcome consistency (JS over correctness distributions across K rollouts) as a coarser but robust signal.\n\n## Research Landscape\n\n**Diagnostic-only (no training fix):** VAR-MATH (arXiv 2507.12885): 47-73% drops, sub-frontier models on competition math. MATH-Perturb (ICML 2025, arXiv 2502.06453): 279 MATH level-5 problems, distinguishes solution-preserving (Simple) vs. solution-changing (Hard) perturbation. GSM-Symbolic (ICLR 2025): performance variance across instantiations, 25 models evaluated. Robust Reasoning Benchmark (arXiv 2604.08571): 14 encoding/structural perturbation types on AIME 2024, orthogonal to semantic-preserving perturbation.\n\n**Augmentation-only (no invariance objective):** TA-GRPO (arXiv 2601.22478): +9.84pp competition math via cross-variant pooled advantage, no consistency loss, no robustness evaluation. PrAg-PO (arXiv 2602.03190): prompt augmentation stabilizes GRPO, mitigates entropy collapse, no invariance objective.\n\n**Structural RL (different mechanism):** AbstRaL (ICLR 2026, arXiv 2506.07751): input-side mechanism—teaches models to abstract GSM problems into symbolic representations before solving. Achieves near-full robustness recovery on GSM variants but untested on competition-level math. MACR is output-side (constrains reasoning strategy consistency). These are orthogonal: abstraction changes how the model reads problems, consistency changes how it reasons. Potentially complementary. MathForge/DGPO (ICLR 2026): difficulty-aware GRPO, no robustness evaluation.\n\n**Causal/consistency RL (different target):** GC²PO (arXiv 2602.06475): episodic causal counterfactual reward evaluating whether reasoning steps remain stable under within-problem counterfactual perturbations—focuses on step-level causal robustness within a single problem. MACR targets cross-problem strategy invariance across semantically equivalent perturbations—a complementary but distinct objective. GRPO-CARE (arXiv 2506.16141): consistency-aware RL for video reasoning (step-answer coherence, not cross-perturbation invariance). CC-LEARN (arXiv 2506.15662): cohort consistency RL for NLU tasks. COPO (arXiv 2508.04138): consistency-entropy for zero-advantage training efficiency—addresses the same upstream problem (gradient vanishing in all-correct groups) but through advantage redesign rather than cross-perturbation consistency. DPH-RL: JS for diversity, not invariance.\n\n**Consistency regularization (different domain/setting):** ROMA (arXiv 2605.09262): correctness-conditioned token-level KL for visual corruption robustness, closest methodological cousin but operates where perturbation preserves answers. F2C (arXiv 2510.14242)/PPCL: JS-based consistency, SFT-only, NLU-only.\n\n**Gap:** No work combines math-equivalence-aware perturbation with trajectory-translated structure-aware consistency during RL training. The T3F mechanism—which resolves the fundamental math-vs-vision consistency gap via SymPy-guided trajectory translation—is the core technical novelty.\n\n## Proposed Approach\n\nMACR integrates perturbation-invariance into GRPO training on Qwen3-8B via four components:\n\n**(1) SymPy-Verified Symbolic Perturbation Generator.** Creates equivalent variants through: numerical substitution, variable renaming, expression rewriting (a+b → b+a), constraint reformulation (\"A exceeds B by 3\" → \"B is 3 less than A\"). All variants SymPy-verified for answer equivalence. Inspired by Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187). Coverage limitation: SymPy handles algebra/equation problems well but has limited coverage for geometry, combinatorics, and number theory. For non-coverable problems, LLM-based perturbation with majority-vote verification serves as fallback. We report per-topic perturbation coverage rates.\n\n**(2) Structure-Aware Consistency (SAC) via T3F.** For each (original, perturbed) pair where both are correctly solved in GRPO rollouts: apply Trajectory-Translated Teacher Forcing (detailed above) to compute token-level JS divergence over reasoning structure. Correctness-conditioning (à la ROMA) restricts enforcement to successful pairs, avoiding systematically wrong invariance. For perturbation types where trajectory translation is imprecise (expression rewriting, constraint reformulation), fall back to rollout-level outcome consistency.\n\n**(3) Contrastive Discrimination Loss.** Prevents degenerate invariance by training the model to distinguish surface-similar but semantically-different problems. Hard negatives constructed via SymPy answer-changing perturbation: modifying a coefficient/constraint so the answer changes while surface similarity is preserved. Automatically verifiable via SymPy.\n\n**(4) verl/DAPO Infrastructure.** Built on DAPO (arXiv 2025) for scalable GRPO training.\n\n## Theoretical Positioning\n\nMACR provides a lightweight process-level quality signal without step-level annotation. By requiring structurally similar reasoning on equivalent problems, SAC implicitly penalizes heuristic shortcuts: a model relying on surface pattern matching cannot consistently produce similar reasoning structures across numerically different but structurally identical problems. This positions MACR as complementary to PRM (explicit process supervision) and ORM (outcome-only)—offering process-quality pressure at zero annotation cost. This claim is offered as a secondary insight; the primary contribution is perturbation robustness.\n\n## Experimental Design\n\n**Training Data:** MATH training split (~7.5K problems) + NuminaMath-TIR subset, aligned with TA-GRPO's data regime for fair comparison. We report SymPy perturbation success rate on this training set (expected: high for algebra/equations, lower for geometry/combinatorics).\n\n**Baselines (7 tiers):**\n1. Vanilla Qwen3-8B (no RL)\n2. Standard GRPO (verl/DAPO, no augmentation or consistency)\n3. COPO (consistency-entropy advantage redesign—isolates \"fix zero-advantage\" from \"enforce cross-perturbation consistency\")\n4. TA-GRPO / PrAg-PO (augmentation-only GRPO—isolates SAC contribution)\n5. AbstRaL (abstraction + RL—direct competitor; reproduce on Qwen3-8B if feasible, otherwise use published results on shared benchmarks with explicit model-gap discussion since AbstRaL uses Llama-3/Qwen2)\n6. F2C-style generic JS consistency applied to GRPO (no math-specific perturbation or T3F—isolates math-aware design value)\n7. Full MACR\n\n**Compute-normalized comparison:** Standard GRPO with 2-3x compute budget (matched to MACR's additional forward passes) as fairness control.\n\n**Evaluation Benchmarks:**\n- Robustness (core): VAR-MATH, MATH-P-Simple (ICML 2025), GSM-Symbolic (ICLR 2025), GSM-Plus\n- Robustness (supplementary, out-of-scope for MACR): MATH-P-Hard, Robust Reasoning Benchmark (arXiv 2604.08571) — reported for completeness, no expected gains\n- Clean accuracy: MATH500, GSM8K, AIME 2024\n- OOD generalization: Minerva, OlympiadBench\n- Stratified analysis: per-topic breakdown (algebra, number theory, geometry, combinatorics) to assess SymPy coverage impact\n\n**Evaluation Metrics:**\n- Clean Accuracy: Pass@1 on standard benchmarks\n- Robust Accuracy: Pass@1 on perturbation benchmarks\n- Relative Performance Drop (RPD): (Clean − Robust) / Clean × 100%\n- Consistency Rate: fraction of templates where all instantiations correct (VAR-MATH strict)\n- Performance Variance: accuracy variance across instantiations (GSM-Symbolic style)\n- All metrics: mean ± std over 3 seeds (sensitivity analyses on 1 seed)\n\n**Ablation Study:**\n- A1: GRPO only (no augmentation, no consistency)\n- A2: GRPO + perturbation augmentation only (no consistency loss)\n- A3: GRPO + perturbation + unconditional JS (no correctness conditioning)\n- A4: GRPO + perturbation + correctness-conditioned JS without T3F (naive token-level JS, no trajectory translation)\n- A5: GRPO + perturbation + correctness-conditioned SAC via T3F (no contrastive)\n- A6: Full MACR (T3F-SAC + contrastive discrimination)\n- A7: λ sensitivity for consistency loss weight (1 seed)\n- A8: Perturbation type contribution: numerical-only vs. variable-only vs. expression-rewriting vs. all (1 seed)\n- A9: T3F teacher-forcing vs. rollout-level outcome consistency (coarse fallback)\n- A10: Masking granularity: conservative (problem-value-only) vs. aggressive (all digits) vs. no masking\n\n**Compute Estimate:** Single GRPO run on Qwen3-8B ≈ 40-80 GPU-hours on 8×A100. Core baselines (7 configs × 3 seeds = 21 runs) + key ablations (A3-A6 × 3 seeds = 12 runs) + sensitivity analyses (A7-A10 × 1 seed = 4 runs) = ~37 runs ≈ 1,500-3,000 A100 GPU-hours total. Ablation reduction strategy: A7, A8, A10 run on 1 seed for initial screening, scale to 3 seeds only for significant findings.\n\n## Key References\n\n- ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (arXiv 2605.09262, 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2507.12885, 2025)\n- AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking (ICLR 2026, arXiv 2506.07751)\n- MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations (ICML 2025, arXiv 2502.06453)\n- Robust Reasoning Benchmark (arXiv 2604.08571, 2026)\n- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478)\n- PrAg-PO: Prompt Augmentation Scales up GRPO Training (arXiv 2602.03190)\n- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)\n- DAPO: Open-Source LLM RL System at Scale (arXiv 2025)\n- F2C: Flip-Flop Consistency for Prompt Perturbation Robustness (arXiv 2510.14242, 2025)\n- GSM-Symbolic: Understanding Limitations of Math Reasoning (ICLR 2025)\n- GSM-Plus: Evaluating Robustness of LLMs as Mathematical Problem Solvers\n- GC²PO: Group Causal Counterfactual Policy Optimization (arXiv 2602.06475, 2026)\n- GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (arXiv 2506.16141)\n- COPO: Consistency-Entropy Policy Optimization (arXiv 2508.04138)\n- CC-LEARN: Cohort-based Consistency Learning (arXiv 2506.15662)\n- DPH-RL / PPCL\n- Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, 2026)\n- NuminaMath-TIR"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:29:16.331Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:29:16.331Z",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-29T06:29:16.345Z_

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
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "e9dc2c6e-926c-4451-ace4-da973141d711",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:29:16.344Z_

```json
{
  "parentUuid": "e9dc2c6e-926c-4451-ace4-da973141d711",
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
  "uuid": "0a6aa28d-59ca-4093-9fe5-65026a763096",
  "timestamp": "2026-05-29T06:29:16.344Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:29:16.344Z_

```json
{
  "parentUuid": "0a6aa28d-59ca-4093-9fe5-65026a763096",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b07c7c55-f9cb-42e4-b261-f3c59b3d25d8",
  "timestamp": "2026-05-29T06:29:16.344Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
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
  "leafUuid": "b07c7c55-f9cb-42e4-b261-f3c59b3d25d8",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for robust math reasoning",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:29:21.292Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. Let me first do thorough web searches to understand the current landscape, then provide my assessment.

Let me search for the key related works and the current state of the field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b07c7c55-f9cb-42e4-b261-f3c59b3d25d8",
  "isSidechain": false,
  "requestId": "req_011CbWPTNfNpuJxtKVtNJTyy",
  "type": "assistant",
  "uuid": "9c1d8c00-94b5-4883-8878-60d7d3a9ea72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFBScZqzgJLW1xyQ2GmnU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 11014,
      "output_tokens": 167,
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
          "output_tokens": 167,
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

_source line 9 · 2026-05-29T06:29:21.834Z_

I'll start by conducting thorough web searches to understand the current research landscape before making any judgments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c1d8c00-94b5-4883-8878-60d7d3a9ea72",
  "isSidechain": false,
  "requestId": "req_011CbWPTNfNpuJxtKVtNJTyy",
  "type": "assistant",
  "uuid": "00ce76bb-d319-4cbd-afa1-1ae3a7a2e615",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFBScZqzgJLW1xyQ2GmnU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 11014,
      "output_tokens": 167,
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
          "output_tokens": 167,
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

_source line 10 · 2026-05-29T06:29:21.867Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TYjfjgbuonqJDT8MnFBkt8`</summary>

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
  "parentUuid": "00ce76bb-d319-4cbd-afa1-1ae3a7a2e615",
  "isSidechain": false,
  "requestId": "req_011CbWPTNfNpuJxtKVtNJTyy",
  "type": "assistant",
  "uuid": "8ad45adb-7432-4198-8326-b842086d376b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFBScZqzgJLW1xyQ2GmnU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 11014,
      "output_tokens": 167,
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
          "output_tokens": 167,
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

_source line 11 · 2026-05-29T06:29:21.876Z_

<details><summary>↩ Tool result · `toolu_01TYjfjgbuonqJDT8MnFBkt8`</summary>

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
  "parentUuid": "8ad45adb-7432-4198-8326-b842086d376b",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "15a05a25-d3f0-498d-94c8-ab11137f49eb",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "8ad45adb-7432-4198-8326-b842086d376b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-29T06:29:25.186Z_

Now let me conduct my research searches in parallel to understand the landscape thoroughly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a05a25-d3f0-498d-94c8-ab11137f49eb",
  "isSidechain": false,
  "requestId": "req_011CbWPTnYKB2rNbDnoR4CHh",
  "type": "assistant",
  "uuid": "70ce041f-41a3-4009-a37e-db5541adb8d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HZAfHunTs6bvJn55CCqK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 19131,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 695
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

_source line 13 · 2026-05-29T06:29:25.407Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017m8DxtjXSeL6KonLvbFX89`</summary>

```json
{
  "query": "RL math reasoning robustness perturbation GRPO consistency regularization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70ce041f-41a3-4009-a37e-db5541adb8d8",
  "isSidechain": false,
  "requestId": "req_011CbWPTnYKB2rNbDnoR4CHh",
  "type": "assistant",
  "uuid": "72a64a59-37ee-4389-b04a-3b5125608c0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HZAfHunTs6bvJn55CCqK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 19131,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 695
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

_source line 14 · 2026-05-29T06:29:25.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EJCVDV2wToFcKbmmCoGxi4`</summary>

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
  "parentUuid": "72a64a59-37ee-4389-b04a-3b5125608c0d",
  "isSidechain": false,
  "requestId": "req_011CbWPTnYKB2rNbDnoR4CHh",
  "type": "assistant",
  "uuid": "2350c73a-d281-49f4-912d-3141e5e69924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HZAfHunTs6bvJn55CCqK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 19131,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 695
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

_source line 15 · 2026-05-29T06:29:26.797Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011ee8uXMQh3iufVhhPggVw6`</summary>

```json
{
  "query": "AbstRaL abstract thinking reinforcement learning math reasoning ICLR 2026 arXiv 2506.07751"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2350c73a-d281-49f4-912d-3141e5e69924",
  "isSidechain": false,
  "requestId": "req_011CbWPTnYKB2rNbDnoR4CHh",
  "type": "assistant",
  "uuid": "acdf1bf4-f668-4540-82da-1eb64af77833",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HZAfHunTs6bvJn55CCqK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 19131,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 695
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

_source line 16 · 2026-05-29T06:29:27.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016k2MJsV81gGN1GsbWk4cyo`</summary>

```json
{
  "query": "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262 consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acdf1bf4-f668-4540-82da-1eb64af77833",
  "isSidechain": false,
  "requestId": "req_011CbWPTnYKB2rNbDnoR4CHh",
  "type": "assistant",
  "uuid": "c026ef26-9c2c-442a-9b17-401dcc8953bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HZAfHunTs6bvJn55CCqK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 19131,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 695
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

_source line 17 · 2026-05-29T06:29:27.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012PVm8eu4y99NcWnBjdRVsh`</summary>

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
  "parentUuid": "c026ef26-9c2c-442a-9b17-401dcc8953bb",
  "isSidechain": false,
  "requestId": "req_011CbWPTnYKB2rNbDnoR4CHh",
  "type": "assistant",
  "uuid": "c16dd383-5561-437b-9317-c5b4c3704349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HZAfHunTs6bvJn55CCqK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 19131,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 19131,
          "cache_creation_input_tokens": 695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 695
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

_source line 18 · 2026-05-29T06:29:33.463Z_

<details><summary>↩ Tool result · `toolu_01EJCVDV2wToFcKbmmCoGxi4`</summary>

```text
Web search results for query: "TA-GRPO transform augmented GRPO math reasoning arXiv 2601.22478"

Links: [{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/html/2601.22478"},{"title":"(PDF) Transform-Augmented GRPO Improves Pass@k","url":"https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/html/2602.03190v1"}]

Based on the search results, here's what I found about TA-GRPO:

## Overview

TA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.

## Problem It Addresses

Group Relative Policy Optimization (GRPO) was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.

## Key Benefits

The pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies. TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.

## Experimental Results

Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).

The paper was submitted to arXiv on January 30, 2026, with a revised version on February 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2350c73a-d281-49f4-912d-3141e5e69924",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "4ab09fd1-9c7c-499a-bbfc-6723d224e80c",
  "toolUseResult": {
    "query": "TA-GRPO transform augmented GRPO math reasoning arXiv 2601.22478",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KYajnnhpRuqzKmUhq7zNhD",
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
      "Based on the search results, here's what I found about TA-GRPO:\n\n## Overview\n\nTA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.\n\n## Problem It Addresses\n\nGroup Relative Policy Optimization (GRPO) was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.\n\n## Key Benefits\n\nThe pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies. TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.\n\n## Experimental Results\n\nExperiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).\n\nThe paper was submitted to arXiv on January 30, 2026, with a revised version on February 11, 2026."
    ],
    "durationSeconds": 7.605556968999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2350c73a-d281-49f4-912d-3141e5e69924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T06:29:34.572Z_

<details><summary>↩ Tool result · `toolu_016k2MJsV81gGN1GsbWk4cyo`</summary>

```text
Web search results for query: "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262 consistency"

Links: [{"title":"[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/abs/2605.09262"},{"title":"Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/pdf/2605.09262"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/html/2509.23322v2"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/html/2512.17532"},{"title":"Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding","url":"https://arxiv.org/pdf/2512.17532"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/pdf/2509.23322"}]

Based on the search results, I found the paper you're looking for:

**ROMA** is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance for Multimodal Large Language Models (MLLMs).

**Key Technical Aspects:**

The challenge is that naively injecting degraded views during rollout induces reward poisoning, where perceptual occlusions trigger hallucinated trajectories and destabilize optimization.

The framework uses a dual-forward-pass strategy with teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs.

**Core Components for Consistency:**

For distributional consistency, ROMA applies a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories.

**Performance:**

On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c026ef26-9c2c-442a-9b17-401dcc8953bb",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "315e1bda-94fc-46ae-911e-d9586741b0e0",
  "toolUseResult": {
    "query": "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262 consistency",
    "results": [
      {
        "tool_use_id": "srvtoolu_016XJuxa5zwDtE5CDknD3Zo8",
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
      "Based on the search results, I found the paper you're looking for:\n\n**ROMA** is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance for Multimodal Large Language Models (MLLMs).\n\n**Key Technical Aspects:**\n\nThe challenge is that naively injecting degraded views during rollout induces reward poisoning, where perceptual occlusions trigger hallucinated trajectories and destabilize optimization.\n\nThe framework uses a dual-forward-pass strategy with teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs.\n\n**Core Components for Consistency:**\n\nFor distributional consistency, ROMA applies a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories.\n\n**Performance:**\n\nOn Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy."
    ],
    "durationSeconds": 7.300781014,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c026ef26-9c2c-442a-9b17-401dcc8953bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T06:29:34.718Z_

<details><summary>↩ Tool result · `toolu_011ee8uXMQh3iufVhhPggVw6`</summary>

```text
Web search results for query: "AbstRaL abstract thinking reinforcement learning math reasoning ICLR 2026 arXiv 2506.07751"

Links: [{"title":"[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/abs/2506.07751"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/html/2506.07751v2"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"[PDF] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AbstRaL:-Augmenting-LLMs'-Reasoning-by-Reinforcing-Gao-Bosselut/db59c2208185f3711705387c5baf2aa47ec648c5"},{"title":"ABSTRAL: AUGMENTING LLMS' REASONING BY ...","url":"https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"},{"title":"arXiv:2506.07751v2 [cs.CL] 11 Jun 2025 AbstRaL: Augmenting LLMs’ Reasoning by","url":"https://bengio.abracadoudou.com/cv/publications/pdf/gao_2025_arxiv.pdf"}]

Based on the search results, here's what I found about the AbstRaL paper:

AbstRaL is a paper addressing how large language models, especially smaller ones, often lack robustness in grade school math (GSM) reasoning. The models tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses.

The researchers propose the reinforced AbstRaction Learning framework, AbstRaL, which first teaches LLMs to generate abstraction of input problems, and then connects the abstraction with symbolic tools to stably derive the output solution, regardless of the specific input contexts.

The learning of abstraction relies on Granularly-decomposed Abstract Reasoning (GranulAR) data distilled from an oracle LLM, which integrates symbolic reasoning within socratic problem decomposition and chain-of-thought explanations. On top of supervised fine-tuning (SFT), AbstRaL uses reinforcement learning (RL) with a new set of model-free rewards to further improve the faithfulness of generated abstraction.

The method significantly mitigates performance degradation on recent GSM perturbation benchmarks. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability.

The paper is authored by Silin Gao, Antoine Bosselut, Samy Bengio, and Emmanuel Abbe, and has been accepted to ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acdf1bf4-f668-4540-82da-1eb64af77833",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "9c9fa56e-f8ba-487b-aab7-feb321ddec68",
  "toolUseResult": {
    "query": "AbstRaL abstract thinking reinforcement learning math reasoning ICLR 2026 arXiv 2506.07751",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AzM4NYziU5E7v7K5doNwRy",
        "content": [
          {
            "title": "[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/abs/2506.07751"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/html/2506.07751v2"
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
            "title": "ABSTRAL: AUGMENTING LLMS' REASONING BY ...",
            "url": "https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"
          },
          {
            "title": "Artificial Intelligence Jun 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"
          },
          {
            "title": "arXiv:2506.07751v2 [cs.CL] 11 Jun 2025 AbstRaL: Augmenting LLMs’ Reasoning by",
            "url": "https://bengio.abracadoudou.com/cv/publications/pdf/gao_2025_arxiv.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about the AbstRaL paper:\n\nAbstRaL is a paper addressing how large language models, especially smaller ones, often lack robustness in grade school math (GSM) reasoning. The models tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses.\n\nThe researchers propose the reinforced AbstRaction Learning framework, AbstRaL, which first teaches LLMs to generate abstraction of input problems, and then connects the abstraction with symbolic tools to stably derive the output solution, regardless of the specific input contexts.\n\nThe learning of abstraction relies on Granularly-decomposed Abstract Reasoning (GranulAR) data distilled from an oracle LLM, which integrates symbolic reasoning within socratic problem decomposition and chain-of-thought explanations. On top of supervised fine-tuning (SFT), AbstRaL uses reinforcement learning (RL) with a new set of model-free rewards to further improve the faithfulness of generated abstraction.\n\nThe method significantly mitigates performance degradation on recent GSM perturbation benchmarks. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability.\n\nThe paper is authored by Silin Gao, Antoine Bosselut, Samy Bengio, and Emmanuel Abbe, and has been accepted to ICLR 2026."
    ],
    "durationSeconds": 7.918572440000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "acdf1bf4-f668-4540-82da-1eb64af77833",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-29T06:29:35.671Z_

<details><summary>↩ Tool result · `toolu_012PVm8eu4y99NcWnBjdRVsh`</summary>

```text
Web search results for query: "COPO consistency entropy policy optimization zero advantage arXiv 2508.04138"

Links: [{"title":"[2508.04138v1] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138v1"},{"title":"[2508.04138] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138"},{"title":"COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/html/2508.04138v1"},{"title":"COPO: Consistency-Aware Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=JkmKzsMaAu"},{"title":"COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,","url":"https://arxiv.org/pdf/2508.04138"},{"title":"COPO: Consistency-Aware Policy Optimization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/copo-consistency-aware-policy-optimization"},{"title":"Artificial Intelligence 2025","url":"https://www.arxiv.org/list/cs.AI/2025?skip=29800&show=500"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=2200&show=25"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=21075&show=25"}]

Based on the search results, here's what I found about arXiv paper 2508.04138:

## COPO: Consistency-Aware Policy Optimization

COPO is a novel consistency-entropy-based policy optimization method that introduces the concept of joint optimization across both intra-group and inter-group samples to fully leverage available training data.

### The Problem It Addresses

The paper identifies a common challenge where when multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero. This leads to vanishing gradients and renders the corresponding samples ineffective for learning, ultimately limiting training efficiency and downstream performance.

### The Proposed Solution

The framework introduces a structured global reward based on outcome consistency, ensuring that even when model outputs show high intra-group consistency, the training process still receives meaningful learning signals, which encourages the generation of correct and self-consistent reasoning paths from a global perspective.

Furthermore, the method incorporates an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization, enabling dynamic transitions between exploration and convergence throughout training.

### Results

The paper demonstrates the performance improvement of COPO over GRPO methods in mathematical reasoning tasks, and conducts extensive ablation studies on various existing improvements to GRPO training schemes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c16dd383-5561-437b-9317-c5b4c3704349",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "6e7dd919-cfcc-499e-a3c4-b52b71c99a2f",
  "toolUseResult": {
    "query": "COPO consistency entropy policy optimization zero advantage arXiv 2508.04138",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AJesqS9wGwgw5Nb8TsnE2v",
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
      "Based on the search results, here's what I found about arXiv paper 2508.04138:\n\n## COPO: Consistency-Aware Policy Optimization\n\nCOPO is a novel consistency-entropy-based policy optimization method that introduces the concept of joint optimization across both intra-group and inter-group samples to fully leverage available training data.\n\n### The Problem It Addresses\n\nThe paper identifies a common challenge where when multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero. This leads to vanishing gradients and renders the corresponding samples ineffective for learning, ultimately limiting training efficiency and downstream performance.\n\n### The Proposed Solution\n\nThe framework introduces a structured global reward based on outcome consistency, ensuring that even when model outputs show high intra-group consistency, the training process still receives meaningful learning signals, which encourages the generation of correct and self-consistent reasoning paths from a global perspective.\n\nFurthermore, the method incorporates an entropy-based soft blending mechanism that adaptively balances local advantage estimation with global optimization, enabling dynamic transitions between exploration and convergence throughout training.\n\n### Results\n\nThe paper demonstrates the performance improvement of COPO over GRPO methods in mathematical reasoning tasks, and conducts extensive ablation studies on various existing improvements to GRPO training schemes."
    ],
    "durationSeconds": 7.912898492999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c16dd383-5561-437b-9317-c5b4c3704349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
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
  "leafUuid": "6e7dd919-cfcc-499e-a3c4-b52b71c99a2f",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for robust math reasoning",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Tool result

_source line 24 · 2026-05-29T06:29:37.455Z_

<details><summary>↩ Tool result · `toolu_017m8DxtjXSeL6KonLvbFX89`</summary>

```text
Web search results for query: "RL math reasoning robustness perturbation GRPO consistency regularization 2025 2026"

Links: [{"title":"Shorter but not Worse: Frugal Reasoning via Easy Samples as Length Regularizers in Math RLVR","url":"https://arxiv.org/html/2511.01937v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=GP5RHZnEsw"},{"title":"May 7, 2026 Rethinking RL for LLM Reasoning:","url":"https://arxiv.org/pdf/2605.06241"},{"title":"Uncalibrated Reasoning: GRPO Induces Overconfidence for Stochastic Outcomes","url":"https://arxiv.org/pdf/2508.11800"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"},{"title":"CoRPO: Adding a Correctness Bias to GRPO Improves Generalization","url":"https://arxiv.org/pdf/2511.04439"},{"title":"Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?","url":"https://arxiv.org/pdf/2602.07470"},{"title":"Geometric-Mean Policy Optimization","url":"https://arxiv.org/pdf/2507.20673"}]

Based on the search results, here's what I found about recent research combining RL, math reasoning, robustness, perturbation, GRPO, and consistency regularization:

## Key Research Areas (2025-2026)

**GRPO Improvements and Refinements:**
Large reasoning models trained via GRPO can autonomously acquire advanced reasoning behaviors such as branching, verification, and backtracking, with recent work investigating its limitations and proposing refinements to enhance reasoning performance.

**Robustness and Perturbations:**
GSM-Plus is a robustness extension of GSM8K with controlled perturbations (e.g., rewording, distractors, numerical changes). Additionally, smaller models especially lack robustness to incorrect few-shot examples and problem perturbations.

**Consistency and Regularization:**
Correctness-Relative Policy Optimization (CoRPO) proposes a modification to the GRPO objective that clips the minimum baseline to a fixed correctness threshold, introducing a protective bias to advantage estimation that mitigates overfitting while preserving effective exploration.

Geometric-Mean Policy Optimization (GMPO) stabilizes the GRPO algorithm by maximizing the geometric mean of token-level rewards, with theoretical and empirical analyses showing improved stability while enhancing exploration.

**Calibration Issues:**
Removing group standard normalization in GRPO fixes its miscalibration and provides a theoretical explanation for why normalization causes overconfidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72a64a59-37ee-4389-b04a-3b5125608c0d",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "0da9e8ee-83f0-44af-bfe3-521aabfa1703",
  "toolUseResult": {
    "query": "RL math reasoning robustness perturbation GRPO consistency regularization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RoMef2oiHCxoQFqPAptf1n",
        "content": [
          {
            "title": "Shorter but not Worse: Frugal Reasoning via Easy Samples as Length Regularizers in Math RLVR",
            "url": "https://arxiv.org/html/2511.01937v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=GP5RHZnEsw"
          },
          {
            "title": "May 7, 2026 Rethinking RL for LLM Reasoning:",
            "url": "https://arxiv.org/pdf/2605.06241"
          },
          {
            "title": "Uncalibrated Reasoning: GRPO Induces Overconfidence for Stochastic Outcomes",
            "url": "https://arxiv.org/pdf/2508.11800"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          },
          {
            "title": "CoRPO: Adding a Correctness Bias to GRPO Improves Generalization",
            "url": "https://arxiv.org/pdf/2511.04439"
          },
          {
            "title": "Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?",
            "url": "https://arxiv.org/pdf/2602.07470"
          },
          {
            "title": "Geometric-Mean Policy Optimization",
            "url": "https://arxiv.org/pdf/2507.20673"
          }
        ]
      },
      "Based on the search results, here's what I found about recent research combining RL, math reasoning, robustness, perturbation, GRPO, and consistency regularization:\n\n## Key Research Areas (2025-2026)\n\n**GRPO Improvements and Refinements:**\nLarge reasoning models trained via GRPO can autonomously acquire advanced reasoning behaviors such as branching, verification, and backtracking, with recent work investigating its limitations and proposing refinements to enhance reasoning performance.\n\n**Robustness and Perturbations:**\nGSM-Plus is a robustness extension of GSM8K with controlled perturbations (e.g., rewording, distractors, numerical changes). Additionally, smaller models especially lack robustness to incorrect few-shot examples and problem perturbations.\n\n**Consistency and Regularization:**\nCorrectness-Relative Policy Optimization (CoRPO) proposes a modification to the GRPO objective that clips the minimum baseline to a fixed correctness threshold, introducing a protective bias to advantage estimation that mitigates overfitting while preserving effective exploration.\n\nGeometric-Mean Policy Optimization (GMPO) stabilizes the GRPO algorithm by maximizing the geometric mean of token-level rewards, with theoretical and empirical analyses showing improved stability while enhancing exploration.\n\n**Calibration Issues:**\nRemoving group standard normalization in GRPO fixes its miscalibration and provides a theoretical explanation for why normalization causes overconfidence."
    ],
    "durationSeconds": 12.044525973999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "72a64a59-37ee-4389-b04a-3b5125608c0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-29T06:29:41.902Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now let me do a couple more targeted searches to fill in gaps, especially about VAR-MATH, GC²PO, and the broader landscape of math reasoning robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0da9e8ee-83f0-44af-bfe3-521aabfa1703",
  "isSidechain": false,
  "requestId": "req_011CbWPUvoBcqV8tXQZEE7ZV",
  "type": "assistant",
  "uuid": "32e5276e-6531-4d20-a843-d48c44369923",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qhChfaMhCoV7Pn3xNMh7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2858,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 19826,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2858,
          "output_tokens": 259,
          "cache_read_input_tokens": 19826,
          "cache_creation_input_tokens": 1073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1073
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

_source line 26 · 2026-05-29T06:29:41.903Z_

Good. Let me do a few more targeted searches to fill remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32e5276e-6531-4d20-a843-d48c44369923",
  "isSidechain": false,
  "requestId": "req_011CbWPUvoBcqV8tXQZEE7ZV",
  "type": "assistant",
  "uuid": "1733a4db-6891-45a5-a129-5a3772ee734c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qhChfaMhCoV7Pn3xNMh7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2858,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 19826,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2858,
          "output_tokens": 259,
          "cache_read_input_tokens": 19826,
          "cache_creation_input_tokens": 1073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1073
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

_source line 27 · 2026-05-29T06:29:42.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EL8gajGn5f5bvJYvmJzp7u`</summary>

```json
{
  "query": "VAR-MATH symbolic benchmark probing mathematical reasoning robustness arXiv 2507.12885"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1733a4db-6891-45a5-a129-5a3772ee734c",
  "isSidechain": false,
  "requestId": "req_011CbWPUvoBcqV8tXQZEE7ZV",
  "type": "assistant",
  "uuid": "b9a4e477-3878-4d04-8ac2-a94203493729",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qhChfaMhCoV7Pn3xNMh7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2858,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 19826,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2858,
          "output_tokens": 259,
          "cache_read_input_tokens": 19826,
          "cache_creation_input_tokens": 1073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1073
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

_source line 28 · 2026-05-29T06:29:43.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AauPZemuopRr9TMNhWyZA3`</summary>

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
  "parentUuid": "b9a4e477-3878-4d04-8ac2-a94203493729",
  "isSidechain": false,
  "requestId": "req_011CbWPUvoBcqV8tXQZEE7ZV",
  "type": "assistant",
  "uuid": "d667140b-fc3b-461f-b6a2-b3cfbbf6ff5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qhChfaMhCoV7Pn3xNMh7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2858,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 19826,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2858,
          "output_tokens": 259,
          "cache_read_input_tokens": 19826,
          "cache_creation_input_tokens": 1073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1073
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

_source line 29 · 2026-05-29T06:29:44.217Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VBETeNo7Hya3cvqd2AzTVS`</summary>

```json
{
  "query": "math reasoning LLM robustness perturbation training methods 2026 consistency invariance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d667140b-fc3b-461f-b6a2-b3cfbbf6ff5d",
  "isSidechain": false,
  "requestId": "req_011CbWPUvoBcqV8tXQZEE7ZV",
  "type": "assistant",
  "uuid": "6f453f8a-385f-4dd0-a3f4-d6b470f9690f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qhChfaMhCoV7Pn3xNMh7H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2858,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 19826,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2858,
          "output_tokens": 259,
          "cache_read_input_tokens": 19826,
          "cache_creation_input_tokens": 1073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1073
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

_source line 30 · 2026-05-29T06:29:50.755Z_

<details><summary>↩ Tool result · `toolu_01EL8gajGn5f5bvJYvmJzp7u`</summary>

```text
Web search results for query: "VAR-MATH symbolic benchmark probing mathematical reasoning robustness arXiv 2507.12885"

Links: [{"title":"[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/abs/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885v1"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in ...","url":"https://arxiv.org/pdf/2507.12885"},{"title":"MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.06430"},{"title":"I-RAVEN-X: Benchmarking Generalization and Robustness of Analogical and Mathematical Reasoning in Large Language and Reasoning Models","url":"https://arxiv.org/pdf/2510.17496"}]

Based on the search results, here's what I found about the paper:

## VAR-MATH: Overview

VAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.

## Key Problems It Addresses

The paper identifies two critical shortcomings in existing evaluation protocols: benchmark contamination arises because test problems are publicly available, thereby increasing the risk of data leakage, and evaluation fragility results from reliance on single-instance assessments, which are sensitive to stochastic outputs and fail to capture reasoning consistency.

## How It Works

VAR-MATH converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each. This design enforces consistency across structurally equivalent variants, mitigates contamination, and enhances robustness through bootstrapped metrics.

## Key Findings

The research reveals significant performance drops when models are re-evaluated on the symbolic variants. Several 7B-parameter models that previously achieved scores ranging from 36.9 to 78.6 on AMC23 drop to only 2.5 to 56.4 when evaluated on VAR-AMC23. This sharp decline indicates that much of their apparent success under conventional evaluation may stem from overfitting to benchmark-specific artifacts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9a4e477-3878-4d04-8ac2-a94203493729",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "103467fb-6a4a-4489-b2ce-e4387fe91189",
  "toolUseResult": {
    "query": "VAR-MATH symbolic benchmark probing mathematical reasoning robustness arXiv 2507.12885",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HMDbXPzk2x8CPGhY4qcdMC",
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
      "Based on the search results, here's what I found about the paper:\n\n## VAR-MATH: Overview\n\nVAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.\n\n## Key Problems It Addresses\n\nThe paper identifies two critical shortcomings in existing evaluation protocols: benchmark contamination arises because test problems are publicly available, thereby increasing the risk of data leakage, and evaluation fragility results from reliance on single-instance assessments, which are sensitive to stochastic outputs and fail to capture reasoning consistency.\n\n## How It Works\n\nVAR-MATH converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each. This design enforces consistency across structurally equivalent variants, mitigates contamination, and enhances robustness through bootstrapped metrics.\n\n## Key Findings\n\nThe research reveals significant performance drops when models are re-evaluated on the symbolic variants. Several 7B-parameter models that previously achieved scores ranging from 36.9 to 78.6 on AMC23 drop to only 2.5 to 56.4 when evaluated on VAR-AMC23. This sharp decline indicates that much of their apparent success under conventional evaluation may stem from overfitting to benchmark-specific artifacts."
    ],
    "durationSeconds": 7.833559669999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b9a4e477-3878-4d04-8ac2-a94203493729",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-29T06:29:51.191Z_

<details><summary>↩ Tool result · `toolu_01AauPZemuopRr9TMNhWyZA3`</summary>

```text
Web search results for query: "GC2PO group causal counterfactual policy optimization math reasoning arXiv 2602.06475"

Links: [{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLMs","url":"https://arxiv.org/html/2602.06475v2"},{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning","url":"https://arxiv.org/pdf/2602.06475"},{"title":"Counterfactual Policy Optimization","url":"https://www.emergentmind.com/topics/counterfactual-policy-optimization"},{"title":"Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization","url":"https://arxiv.org/pdf/2602.09331"},{"title":"[2602.09331] Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization","url":"https://arxiv.org/abs/2602.09331"},{"title":"Causally-Enhanced Reinforcement Policy Optimization","url":"https://arxiv.org/pdf/2509.23095"}]

Based on the search results, here's what I found about the paper:

Group Causal Counterfactual Policy Optimization (GC²PO) is a method proposed to explicitly train LLMs to learn generalizable reasoning patterns.

**The Core Problem:**
Existing reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization.

**The Solution:**
From a causal perspective, the paper interprets multi-candidate reasoning for a fixed question as a family of counterfactual experiments with theoretical supports.

**Key Innovation:**
GC²PO proposes an episodic causal counterfactual reward that jointly captures (i) robustness, encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations; and (ii) effectiveness, enforcing sufficient variability so that the learned reasoning strategy can transfer across questions.

**Implementation:**
The method automatically segments each question-solution pair into distinct episodes via prompt design, computes a causal counterfactual reward for each episode consisting of two terms that jointly measure the robustness and effectiveness of the reasoning step, and leverages these rewards with the outcome reward to construct token-level advantages, optimizing the LLM to internalize generalizable reasoning strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d667140b-fc3b-461f-b6a2-b3cfbbf6ff5d",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "7fe75499-fe18-4156-b450-5e13008c1b81",
  "toolUseResult": {
    "query": "GC2PO group causal counterfactual policy optimization math reasoning arXiv 2602.06475",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AXZXP7u7ZScrYBAR2YrjTn",
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
      "Based on the search results, here's what I found about the paper:\n\nGroup Causal Counterfactual Policy Optimization (GC²PO) is a method proposed to explicitly train LLMs to learn generalizable reasoning patterns.\n\n**The Core Problem:**\nExisting reward mechanisms remain tightly coupled to final correctness and pay little attention to the underlying reasoning process: trajectories with sound reasoning but wrong answers receive low credit, while lucky guesses with flawed logic may be highly rewarded, affecting reasoning generalization.\n\n**The Solution:**\nFrom a causal perspective, the paper interprets multi-candidate reasoning for a fixed question as a family of counterfactual experiments with theoretical supports.\n\n**Key Innovation:**\nGC²PO proposes an episodic causal counterfactual reward that jointly captures (i) robustness, encouraging the answer distribution induced by a reasoning step to remain stable under counterfactual perturbations; and (ii) effectiveness, enforcing sufficient variability so that the learned reasoning strategy can transfer across questions.\n\n**Implementation:**\nThe method automatically segments each question-solution pair into distinct episodes via prompt design, computes a causal counterfactual reward for each episode consisting of two terms that jointly measure the robustness and effectiveness of the reasoning step, and leverages these rewards with the outcome reward to construct token-level advantages, optimizing the LLM to internalize generalizable reasoning strategies."
    ],
    "durationSeconds": 7.320791979000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d667140b-fc3b-461f-b6a2-b3cfbbf6ff5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-29T06:29:51.901Z_

<details><summary>↩ Tool result · `toolu_01VBETeNo7Hya3cvqd2AzTVS`</summary>

```text
Web search results for query: "math reasoning LLM robustness perturbation training methods 2026 consistency invariance"

Links: [{"title":"Learning Perturbations to Extrapolate Your LLM","url":"https://arxiv.org/html/2605.13284"},{"title":"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/html/2511.08022"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview","url":"https://openreview.net/forum?id=OZy70UggXr"},{"title":"Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges","url":"https://arxiv.org/html/2605.19723v1"},{"title":"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2511.08022"},{"title":"MathRobust-LV: Evaluation of Large Language Models’ Robustness to Linguistic Variations in Mathematical Reasoning","url":"https://arxiv.org/html/2510.06430v1"},{"title":"MSCR: Exploring the Vulnerability of LLMs' Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement","url":"https://arxiv.org/pdf/2511.08055"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038v2"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"}]

I found relevant research on mathematical reasoning in LLMs with focus on robustness and perturbation methods. Here are the key findings:

## Recent Developments in Math Reasoning LLM Robustness

**Perturbation-Based Evaluation Methods:**

Researchers have adopted sentence-level perturbation methods, including perturbations with and without numbers, inserting semantically irrelevant redundant sentences into original problems while gradually increasing perturbation intensity.

A methodology called MathRobust-LV evaluates linguistic robustness in math reasoning through minimal but meaning-preserving rewordings.

MATH-P benchmarks consisting of perturbed math problems derived from the MATH dataset show significant performance drops across models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).

**Training Methods for Robustness:**

Different training objectives have been proposed to improve model robustness, such as total variation distance, Earth Mover's distance, and mixed forward-reverse cross-entropies.

Adversarial variants can be repurposed as training data to enhance robustness, aligning with recent efforts on high-quality data augmentation.

A difficulty-evolving perturbation approach using reinforcement learning guides question rewriting across difficulty levels, showing an average 21.73% performance drop across 26 models.

**Consistency and Invariance Issues:**

When minor perturbations are applied to input problems, the performance of models decreases significantly, indicating fragility in model consistency across variations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f453f8a-385f-4dd0-a3f4-d6b470f9690f",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "2fb3fa6f-bad4-40a2-955a-d803a84c030d",
  "toolUseResult": {
    "query": "math reasoning LLM robustness perturbation training methods 2026 consistency invariance",
    "results": [
      {
        "tool_use_id": "srvtoolu_017msGpovovQcTbWoJPuoWxR",
        "content": [
          {
            "title": "Learning Perturbations to Extrapolate Your LLM",
            "url": "https://arxiv.org/html/2605.13284"
          },
          {
            "title": "Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models",
            "url": "https://arxiv.org/html/2511.08022"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=OZy70UggXr"
          },
          {
            "title": "Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges",
            "url": "https://arxiv.org/html/2605.19723v1"
          },
          {
            "title": "Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2511.08022"
          },
          {
            "title": "MathRobust-LV: Evaluation of Large Language Models’ Robustness to Linguistic Variations in Mathematical Reasoning",
            "url": "https://arxiv.org/html/2510.06430v1"
          },
          {
            "title": "MSCR: Exploring the Vulnerability of LLMs' Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement",
            "url": "https://arxiv.org/pdf/2511.08055"
          },
          {
            "title": "Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/html/2506.05038v2"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2511.04120"
          }
        ]
      },
      "I found relevant research on mathematical reasoning in LLMs with focus on robustness and perturbation methods. Here are the key findings:\n\n## Recent Developments in Math Reasoning LLM Robustness\n\n**Perturbation-Based Evaluation Methods:**\n\nResearchers have adopted sentence-level perturbation methods, including perturbations with and without numbers, inserting semantically irrelevant redundant sentences into original problems while gradually increasing perturbation intensity.\n\nA methodology called MathRobust-LV evaluates linguistic robustness in math reasoning through minimal but meaning-preserving rewordings.\n\nMATH-P benchmarks consisting of perturbed math problems derived from the MATH dataset show significant performance drops across models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).\n\n**Training Methods for Robustness:**\n\nDifferent training objectives have been proposed to improve model robustness, such as total variation distance, Earth Mover's distance, and mixed forward-reverse cross-entropies.\n\nAdversarial variants can be repurposed as training data to enhance robustness, aligning with recent efforts on high-quality data augmentation.\n\nA difficulty-evolving perturbation approach using reinforcement learning guides question rewriting across difficulty levels, showing an average 21.73% performance drop across 26 models.\n\n**Consistency and Invariance Issues:**\n\nWhen minor perturbations are applied to input problems, the performance of models decreases significantly, indicating fragility in model consistency across variations."
    ],
    "durationSeconds": 7.681349984999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6f453f8a-385f-4dd0-a3f4-d6b470f9690f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-29T06:29:51.905Z_

```json
{
  "parentUuid": "2fb3fa6f-bad4-40a2-955a-d803a84c030d",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e7f83b92-2f17-4f5a-a6a6-4f57cd87ef31",
  "timestamp": "2026-05-29T06:29:51.905Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-29T06:29:58.773Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the landscape. Let me synthesize my findings and provide a comprehensive evaluation. Let me also do one more search to check if there's any work that directly overlaps with the T3F (Trajectory-Translated Teacher Forcing) mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f83b92-2f17-4f5a-a6a6-4f57cd87ef31",
  "isSidechain": false,
  "requestId": "req_011CbWPVzUU7nRMnhZaqR8mn",
  "type": "assistant",
  "uuid": "80091827-a958-48fa-ad86-82a6ec407986",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ja2P82J2q28iixqjJf7GiR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5374,
      "cache_read_input_tokens": 20899,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 20899,
          "cache_creation_input_tokens": 5374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5374
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

_source line 35 · 2026-05-29T06:29:59.276Z_

Let me do one final search to check for any direct overlaps with the trajectory translation mechanism and to understand the competitive landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80091827-a958-48fa-ad86-82a6ec407986",
  "isSidechain": false,
  "requestId": "req_011CbWPVzUU7nRMnhZaqR8mn",
  "type": "assistant",
  "uuid": "63164966-e1c6-440d-8360-798d30a3eec9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ja2P82J2q28iixqjJf7GiR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5374,
      "cache_read_input_tokens": 20899,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 20899,
          "cache_creation_input_tokens": 5374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5374
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

_source line 36 · 2026-05-29T06:29:59.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V5gactUFLxPshpaooeoyET`</summary>

```json
{
  "query": "trajectory translation teacher forcing consistency regularization reinforcement learning reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63164966-e1c6-440d-8360-798d30a3eec9",
  "isSidechain": false,
  "requestId": "req_011CbWPVzUU7nRMnhZaqR8mn",
  "type": "assistant",
  "uuid": "02abd32c-cf3c-40c6-9144-e61bbb94da42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ja2P82J2q28iixqjJf7GiR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5374,
      "cache_read_input_tokens": 20899,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 20899,
          "cache_creation_input_tokens": 5374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5374
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

_source line 37 · 2026-05-29T06:30:00.818Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DC7YzEfe6GAkJXnXFK2TMk`</summary>

```json
{
  "query": "F2C flip flop consistency prompt perturbation robustness arXiv 2510.14242 JS divergence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02abd32c-cf3c-40c6-9144-e61bbb94da42",
  "isSidechain": false,
  "requestId": "req_011CbWPVzUU7nRMnhZaqR8mn",
  "type": "assistant",
  "uuid": "fc083446-26c1-4fd9-9c86-eb081e86d364",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ja2P82J2q28iixqjJf7GiR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5374,
      "cache_read_input_tokens": 20899,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 20899,
          "cache_creation_input_tokens": 5374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5374
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
  "leafUuid": "fc083446-26c1-4fd9-9c86-eb081e86d364",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for robust math reasoning",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Tool result

_source line 40 · 2026-05-29T06:30:07.644Z_

<details><summary>↩ Tool result · `toolu_01DC7YzEfe6GAkJXnXFK2TMk`</summary>

```text
Web search results for query: "F2C flip flop consistency prompt perturbation robustness arXiv 2510.14242 JS divergence"

Links: [{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/html/2510.14242"},{"title":"[2510.14242v1] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/abs/2510.14242v1"},{"title":"[2510.14242] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/abs/2510.14242"},{"title":"Flip-Flop Consistency: Unsupervised Training for ...","url":"https://arxiv.org/pdf/2510.14242"},{"title":"Auto-Prompt Generation is Not Robust: Prompt Optimization Driven by Pseudo Gradient","url":"https://arxiv.org/pdf/2412.18196"},{"title":"Evaluating Semantic Fragility in Text-to-Audio Generation Systems Under Controlled Prompt Perturbations","url":"https://arxiv.org/html/2603.13824"},{"title":"Evaluating the Robustness of Discrete Prompts","url":"https://arxiv.org/pdf/2302.05619"}]

I found the paper you were looking for! Here are the key details from arXiv paper 2510.14242:

## Flip-Flop Consistency (F2C)

Large Language Models often produce inconsistent answers when faced with different phrasings of the same prompt, and F2C is an unsupervised training method that improves robustness to such perturbations.

### Key Components

The method has two key components: Consensus Cross-Entropy (CCE), which uses a majority vote across prompt variations to create a hard pseudo-label, and a representation alignment loss that pulls lower-confidence and non-majority predictors toward the consensus established by high-confidence, majority-voting variations.

### JS Divergence and KL Divergence

The method minimizes the JS divergence among datapoints within the high-confidence consensus group, and the KL divergence between all other datapoints and that group.

### Results

On average, F2C raises observed agreement by 11.62%, improves mean F1 by 8.94%, and reduces performance variance across formats by 3.29%. When trained on only a subset of prompt perturbations and evaluated on held-out formats, F2C consistently improves both performance and agreement while reducing variance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc083446-26c1-4fd9-9c86-eb081e86d364",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "4e09421f-c589-425c-85e0-80b541a76690",
  "toolUseResult": {
    "query": "F2C flip flop consistency prompt perturbation robustness arXiv 2510.14242 JS divergence",
    "results": [
      {
        "tool_use_id": "srvtoolu_012nGsm4dK17WNUWtR5Wikc3",
        "content": [
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/html/2510.14242"
          },
          {
            "title": "[2510.14242v1] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/abs/2510.14242v1"
          },
          {
            "title": "[2510.14242] Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/abs/2510.14242"
          },
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for ...",
            "url": "https://arxiv.org/pdf/2510.14242"
          },
          {
            "title": "Auto-Prompt Generation is Not Robust: Prompt Optimization Driven by Pseudo Gradient",
            "url": "https://arxiv.org/pdf/2412.18196"
          },
          {
            "title": "Evaluating Semantic Fragility in Text-to-Audio Generation Systems Under Controlled Prompt Perturbations",
            "url": "https://arxiv.org/html/2603.13824"
          },
          {
            "title": "Evaluating the Robustness of Discrete Prompts",
            "url": "https://arxiv.org/pdf/2302.05619"
          }
        ]
      },
      "I found the paper you were looking for! Here are the key details from arXiv paper 2510.14242:\n\n## Flip-Flop Consistency (F2C)\n\nLarge Language Models often produce inconsistent answers when faced with different phrasings of the same prompt, and F2C is an unsupervised training method that improves robustness to such perturbations.\n\n### Key Components\n\nThe method has two key components: Consensus Cross-Entropy (CCE), which uses a majority vote across prompt variations to create a hard pseudo-label, and a representation alignment loss that pulls lower-confidence and non-majority predictors toward the consensus established by high-confidence, majority-voting variations.\n\n### JS Divergence and KL Divergence\n\nThe method minimizes the JS divergence among datapoints within the high-confidence consensus group, and the KL divergence between all other datapoints and that group.\n\n### Results\n\nOn average, F2C raises observed agreement by 11.62%, improves mean F1 by 8.94%, and reduces performance variance across formats by 3.29%. When trained on only a subset of prompt perturbations and evaluated on held-out formats, F2C consistently improves both performance and agreement while reducing variance."
    ],
    "durationSeconds": 6.820271143000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fc083446-26c1-4fd9-9c86-eb081e86d364",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-29T06:30:07.841Z_

<details><summary>↩ Tool result · `toolu_01V5gactUFLxPshpaooeoyET`</summary>

```text
Web search results for query: "trajectory translation teacher forcing consistency regularization reinforcement learning reasoning 2025 2026"

Links: [{"title":"Consistent Paths Lead to Truth: Self-Rewarding Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/pdf/2506.08745"},{"title":"Intra-Trajectory Consistency for Reward Modeling","url":"https://arxiv.org/pdf/2506.09096"},{"title":"Rethinking Expert Trajectory Utilization in LLM Post-training for Mathematical Reasoning","url":"https://arxiv.org/html/2512.11470"},{"title":"Published as a conference paper at ICLR 2026 BENEFITS AND PITFALLS OF","url":"https://arxiv.org/pdf/2509.22613"},{"title":"TraPO: A Semi-Supervised Reinforcement Learning Framework for Boosting LLM Reasoning","url":"https://arxiv.org/pdf/2512.13106"},{"title":"Closing the Modality Reasoning Gap for Speech Large Language Models","url":"https://arxiv.org/pdf/2601.05543"},{"title":"R2PO: Decoupling Training Trajectories from Inference Responses for LLM Reasoning","url":"https://arxiv.org/html/2601.11960"}]

Based on the search results, I found several recent papers (2025-2026) that address aspects of your query related to trajectory consistency, reinforcement learning, and reasoning:

## Key Findings:

**Intra-Trajectory Consistency for Reward Modeling:** This work leverages generation probabilities to establish reward consistency between processes in response trajectories, and develops an intra-trajectory consistency regularization to enforce that adjacent processes with higher next-token generation probability maintain more consistent rewards.

**Trajectory Consistency in Self-Rewarding RL:** A novel self-rewarding reinforcement learning framework leverages the consistency of intermediate reasoning states across different reasoning trajectories, with the insight that correct responses exhibit consistent trajectory patterns where intermediate reasoning states tend to converge toward their final answers with minimal deviation.

**Teacher Forcing and Expert Trajectories:** Recent synchronized SFT-RL paradigms attempt to merge the benefits of SFT and RL by explicitly injecting expert trajectories into the RL optimization loop, with approaches like LUFFY using regularized importance shaping and SRFT balancing SFT, off-policy RL, and likelihood-shaping losses.

**Trajectory Decoupling:** Recent work examines how exploration characterized by entropy affects the depth and diversity of reasoning trajectories from a reasoning-centric perspective.

These papers represent cutting-edge research combining trajectory analysis, consistency regularization, teacher forcing concepts, and reinforcement learning for improving LLM reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02abd32c-cf3c-40c6-9144-e61bbb94da42",
  "isSidechain": false,
  "promptId": "978eff31-4ce2-4496-be60-9df61df02871",
  "type": "user",
  "uuid": "d2bf0f06-cef4-49de-84d0-63462f50bb9c",
  "toolUseResult": {
    "query": "trajectory translation teacher forcing consistency regularization reinforcement learning reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XJT8RD8orTg6HV1JjqUCJy",
        "content": [
          {
            "title": "Consistent Paths Lead to Truth: Self-Rewarding Reinforcement Learning for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2506.08745"
          },
          {
            "title": "Intra-Trajectory Consistency for Reward Modeling",
            "url": "https://arxiv.org/pdf/2506.09096"
          },
          {
            "title": "Rethinking Expert Trajectory Utilization in LLM Post-training for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2512.11470"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 BENEFITS AND PITFALLS OF",
            "url": "https://arxiv.org/pdf/2509.22613"
          },
          {
            "title": "TraPO: A Semi-Supervised Reinforcement Learning Framework for Boosting LLM Reasoning",
            "url": "https://arxiv.org/pdf/2512.13106"
          },
          {
            "title": "Closing the Modality Reasoning Gap for Speech Large Language Models",
            "url": "https://arxiv.org/pdf/2601.05543"
          },
          {
            "title": "R2PO: Decoupling Training Trajectories from Inference Responses for LLM Reasoning",
            "url": "https://arxiv.org/html/2601.11960"
          }
        ]
      },
      "Based on the search results, I found several recent papers (2025-2026) that address aspects of your query related to trajectory consistency, reinforcement learning, and reasoning:\n\n## Key Findings:\n\n**Intra-Trajectory Consistency for Reward Modeling:** This work leverages generation probabilities to establish reward consistency between processes in response trajectories, and develops an intra-trajectory consistency regularization to enforce that adjacent processes with higher next-token generation probability maintain more consistent rewards.\n\n**Trajectory Consistency in Self-Rewarding RL:** A novel self-rewarding reinforcement learning framework leverages the consistency of intermediate reasoning states across different reasoning trajectories, with the insight that correct responses exhibit consistent trajectory patterns where intermediate reasoning states tend to converge toward their final answers with minimal deviation.\n\n**Teacher Forcing and Expert Trajectories:** Recent synchronized SFT-RL paradigms attempt to merge the benefits of SFT and RL by explicitly injecting expert trajectories into the RL optimization loop, with approaches like LUFFY using regularized importance shaping and SRFT balancing SFT, off-policy RL, and likelihood-shaping losses.\n\n**Trajectory Decoupling:** Recent work examines how exploration characterized by entropy affects the depth and diversity of reasoning trajectories from a reasoning-centric perspective.\n\nThese papers represent cutting-edge research combining trajectory analysis, consistency regularization, teacher forcing concepts, and reinforcement learning for improving LLM reasoning capabilities."
    ],
    "durationSeconds": 8.017242974,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "02abd32c-cf3c-40c6-9144-e61bbb94da42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-29T06:30:52.288Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient research to make a thorough evaluation. Let me synthesize everything.

Key findings from my research:

1. **The problem is real and well-documented**: VAR-MATH (47-73% drops), MATH-Perturb, GSM-Symbolic, Robust Reasoning Benchmark all document significant fragility in math reasoning models under perturbation.

2. **Existing solutions are limited**:
   - TA-GRPO: augmentation-only, pools rewards but no invariance objective
   - AbstRaL: input-side abstraction, tested primarily on GSM-level, accepted at ICLR 2026
   - COPO: addresses zero-advantage problem through advantage redesign, not cross-perturbation consistency
   - GC²PO: causal counterfactual within-problem, different objective
   - F2C: JS-based consistency, SFT-only, NLU tasks
   - ROMA: vision domain, answer-preserving perturbations only

3. **The gap claim seems legitimate**: No existing work combines math-equivalence-aware perturbation with trajectory-translated structure-aware consistency during RL training. The T3F mechanism is indeed novel.

4. **Strengths of this proposal**: Very well-articulated problem statement that precisely identifies the "both-correct regime" gap, and the T3F mechanism is a genuinely clever solution bridging math and vision consistency. The experimental design is extremely thorough with seven baselines and ten ablations across multiple benchmarks, and the work honestly acknowledges limitations like SymPy coverage while using the contrastive discrimination loss to prevent degenerate invariance.

5. **Concerns**: The T3F mechanism's reliance on SymPy for exact trajectory translations could be problematic since SymPy has known limitations for geometry and combinatorics problems, potentially affecting a significant portion of the math domain. The "phase complementarity" claim about when to apply augmentation versus consistency lacks formal justification, and AbstRaL from ICLR 2026 is a strong competitor that raises questions about whether input-side abstraction might be more general than the proposed output-side consistency approach. The computational cost is substantial at 1500-3000 A100 GPU-hours, and the fallback to rollout-level outcome consistency for non-translatable perturbations is considerably weaker than T3F itself, which weakens performance on a non-trivial fraction of problems. The token-level JS divergence with masking is intricate, and getting the masking policy right is critical—this could be a fragile component.

6. **Overall assessment**: This is a well-executed proposal that identifies a genuine gap and proposes a technically creative solution with notably comprehensive experimental design, though the main risk is whether the gains from SAC/T

3F over augmentation-only baselines like TA-GRPO will be substantial in practice, especially if the "both-correct regime" signal is weaker than the augmentation signal itself. The novelty is clear but incremental—extending consistency regularization to a new domain with a specific mechanism for the math-versus-vision gap. The positioning against related work is excellent and candid.

Looking at the key factors: the research problem is strong and well-motivated, the method is medium-to-strong with clever ideas but incremental novelty building on ROMA's framework, the experimental design is thorough with good baselines and extensive ablations, feasibility is medium given SymPy coverage limitations and the complex pipeline, and the writing is clear and honest about constraints. The idea is solid with comprehensive experiments, though the practical gains over simpler augmentation approaches remain uncertain.

I'm settling on around 30-42%, with 35-36% as my midpoint estimate. The problem is timely and well-documented across multiple benchmarks, trajectory translation for consistency regularization is genuinely novel, the experimental work is exceptionally thorough, and there's good self-awareness of limitations. But the method's complexity and SymPy constraints present real risks, and whether the empirical gains will be significant enough is the key question. urbation + trajectory translation + teacher forcing + JS divergence + masking + contrastive loss. Many moving parts.
2. SymPy coverage is limited—the method works best for algebra/equations but degrades for geometry/combinatorics/number theory
3. The "both-correct regime" argument, while theoretically sound, may not lead to large practical gains if the late-training regime contributes relatively little to overall performance
4. AbstRaL at ICLR 2026 is a strong competitor that takes a simpler approach (input-side abstraction)
5. No preliminary results—it's all theoretical/proposed

For AAAI 2026, this is a solid proposal. The novelty is real, the experimental design is thorough. I think 30-40% is fair, with midpoint around 35%.

But I need to reconsider—AAAI requires a complete paper with results, not just a proposal. The real acceptance probability depends heavily on whether the experiments actually deliver gains, whether T3F has implementation issues, and the overall paper quality. Given AAAI's ~20-25% acceptance rate, I'm looking at a range where strong results could push this to 40-50%, moderate results land around 25-35%, and disappointing results drop it to 10-20%. The proposal's thoroughness and careful experimental planning are genuine strengths, but SymPy's limited coverage and the risk of marginal improvements over simpler augmentation baselines are real concerns. Settling on 28-40% with a midpoint around 33%.

I'm weighing the complexity of the approach—perturbation, trajectory translation, teacher forcing, JS divergence, masking, contrastive loss all together—against the limited SymPy coverage and uncertain practical gains. AbstRaL's simpler input-side abstraction is a strong competitor. Without preliminary results, this is still theoretical, which adds risk.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2bf0f06-cef4-49de-84d0-63462f50bb9c",
  "isSidechain": false,
  "requestId": "req_011CbWPXAfRTu8PQzdFg4VHN",
  "type": "assistant",
  "uuid": "bb20a4c0-b9f5-4042-ad96-02bde147b242",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrXyatBS1ZjQbAGYqVWiRQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 705,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 26273,
      "output_tokens": 5812,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 705,
          "output_tokens": 5812,
          "cache_read_input_tokens": 26273,
          "cache_creation_input_tokens": 915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 915
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

_source line 43 · 2026-05-29T06:32:24.124Z_

Now I have sufficient information to provide a thorough evaluation. Here is my assessment:

---

```
【阶段】: Triage

【领域调研】:
- [VAR-MATH] (arXiv 2507.12885, 2025): 核心动机来源之一。对AMC23/AIME24/AIME25做符号化参数模板评测，7B模型从36.9-78.6骤降至2.5-56.4，证实sub-frontier模型的fragility是真实且严重的。MACR直接瞄准这一gap。
- [TA-GRPO] (arXiv 2601.22478, 2026): 最直接的augmentation-only baseline。通过跨变体pooled advantage在竞赛数学上+9.84pp，但不含consistency loss，也未做robustness评测。MACR的核心novelty claim——augmentation优化reward而非strategy invariance——需要在实验中与TA-GRPO的直接对比来验证。
- [AbstRaL] (ICLR 2026, arXiv 2506.07751): 最强直接竞争者。输入端抽象化机制，在GSM变体上实现近完全鲁棒性恢复。但仅在GSM级别验证，未测试competition-level math。MACR与之正交（输出端 vs 输入端），但审稿人可能质疑输入端抽象是否已足够。
- [ROMA] (arXiv 2605.09262, 2026): 方法论上最近的"表亲"。视觉领域token-level KL一致性+correctness conditioning。MACR的T3F机制专门解决ROMA无法直接适用于数学场景（perturbation改变答案）的问题，这一差异化是清晰的。
- [COPO] (arXiv 2508.04138, 2025): 解决相同的上游问题（零优势梯度消失），但通过advantage redesign而非cross-perturbation consistency。是验证"both-correct regime"论点的关键ablation对比。
- [GC²PO] (arXiv 2602.06475, 2026): 因果反事实reward，聚焦单问题内step-level因果鲁棒性，与MACR的跨问题strategy invariance互补但不同。
- [F2C] (arXiv 2510.14242, 2025): JS-based consistency，但仅SFT、仅NLU任务，未进入RL训练循环。MACR作为baseline F2C-style generic JS的对比设计合理。
- [MATH-Perturb] (ICML 2025, arXiv 2502.06453): 区分solution-preserving (Simple) vs solution-changing (Hard) perturbation。MACR的评测设计纳入了这一区分。
- [GSM-Symbolic] (ICLR 2025): 跨instantiation性能方差的先驱工作，25个模型评估。
- 调研总结: 数学推理鲁棒性是2025-2026年的热点方向，诊断工具充足但**训练修复方案**明显不足。现有训练方法（TA-GRPO、AbstRaL）要么无invariance objective，要么局限于GSM级别/输入端。MACR定位在"RL训练中的输出端consistency regularization"这一确实空白的细分位置，gap claim基本成立。

【整体印象】: 
作为审稿人，第一反应是"这是一篇方向正确、调研扎实、实验设计极其周全的proposal"。问题动机清晰（both-correct regime的梯度消失），核心机制T3F有genuine technical creativity——用SymPy控制的perturbation mapping做trajectory translation来实现position-exact的token-level consistency，这个idea是elegant的。整体会倾向weak accept，但存在两个隐忧：(1) SymPy覆盖率限制可能大幅缩小方法的有效适用范围，(2) 方法pipeline复杂度较高（perturbation + trajectory translation + teacher forcing + masked JS + contrastive loss），实际增益是否justify这种复杂度需要empirical evidence来回答。

【核心贡献】: 
核心贡献是T3F (Trajectory-Translated Teacher Forcing) 机制——解决了"在数学场景下做token-level consistency regularization"的根本技术障碍（perturbation改变答案和中间计算，naive token-level divergence不可行）。通过SymPy的exact perturbation mapping做trajectory translation，创造position-exact的对应关系，使得token-level JS divergence在数学reasoning场景下变得well-defined。这是对ROMA框架的non-trivial extension，填补了augmentation-only方法在both-correct regime下的梯度信号gap。贡献价值中等偏上——不是paradigm shift，但是一个well-motivated的技术创新，对sub-frontier模型的robustness有实际意义。

【方法合理性】: 
方法整体合理，各组件有清晰的设计动机：
- T3F解决了math-vs-vision的alignment问题，设计逻辑自洽
- Correctness-conditioning（来自ROMA）避免了systematically wrong invariance，合理
- Contrastive discrimination loss防止degenerate invariance，必要
- Fallback to rollout-level outcome consistency for non-translatable perturbations，诚实但显著削弱

**替代方案考量：** 
1. 更简单的替代：step-type-level consistency（只比较推理步骤类型序列）。Proposal已论述了为什么token-level更优（可区分同step-type内的strategy差异），论证合理但需empirical验证。
2. AbstRaL式输入端抽象：可能更general，不受SymPy覆盖率限制。Proposal将其定位为正交/互补，逻辑站得住，但"正交性"需要通过AbstRaL+MACR的组合实验来真正证明。
3. COPO式advantage redesign：解决相同上游问题但机制完全不同。MACR的优势在于直接enforce cross-perturbation invariance而非仅修复梯度信号。

【5 维度打分】:
  1. 研究问题: [强] — 问题真实、重要且有充分的empirical evidence支撑（VAR-MATH 47-73% drops, MATH-Perturb, GSM-Symbolic）。Both-correct regime的梯度消失分析精准，指出了augmentation-only方法的fundamental limitation。这是一个timely的问题，2025-2026年有大量诊断工作但训练修复方案明显不足。

  2. 方法与创新: [中偏强] — T3F是genuine novelty，在ROMA的consistency框架上做了non-trivial的math-specific adaptation。但创新更多是"clever engineering"而非"fundamental insight"——核心idea是用SymPy mapping做trajectory translation来enable已有的token-level consistency方法。与TA-GRPO（arXiv 2601.22478）的差异化清晰（consistency vs. reward pooling），与ROMA（arXiv 2605.09262）的差异化也清晰（math-aware trajectory translation vs. naive token-level KL）。但方法复杂度较高（4个组件），每个组件的边际贡献需要ablation证明。SymPy覆盖率限制（geometry/combinatorics/number theory）是非trivial weakness。

  3. 实验设计: [强] — 这是proposal最突出的亮点。7-tier baseline设计极其周全（vanilla → GRPO → COPO → TA-GRPO → AbstRaL → generic JS → full MACR），每一层isolate一个specific contribution。10个ablation几乎覆盖了所有可能的审稿人质疑（T3F vs. no T3F, masking granularity, perturbation type contribution, etc.）。Compute-normalized comparison是经常被忽视但重要的fairness control。评测benchmark涵盖core robustness + clean accuracy + OOD generalization + stratified per-topic analysis。3-seed统计+1-seed sensitivity的分层策略务实。唯一不足：AbstRaL的reproduction可能有model-gap问题（Llama-3/Qwen2 vs Qwen3-8B），proposal已acknowledge。

  4. 可行性: [中] — Pipeline复杂度是主要风险：SymPy perturbation generator + trajectory translation + teacher forcing + masked JS + contrastive loss + verl/DAPO infrastructure。每一步都有潜在failure point。SymPy覆盖率是hard constraint——algebra/equations之外的数学类别可能无法有效覆盖。1,500-3,000 A100 GPU-hours的计算需求对一般学术组来说偏高但对有资源的组可行。SymPy-based perturbation generation的工程量不小。Trajectory translation的numerical token identification（regex matching against perturbation mapping）可能在复杂推理中遇到edge cases。

  5. 写作与呈现: [强] — Proposal组织清晰，logic flow好：problem → insight → technical challenge → solution → positioning → experiments。对related work的定位精准且诚实（标注了每个方法的具体gap和与MACR的关系）。Limitation acknowledgment主动且具体（SymPy覆盖率、fallback机制、expression rewriting的structural shifts）。"Phase complementarity"的narrative有吸引力。唯一建议：theoretical positioning section的"implicit PRM"claim可能会引起质疑，好在proposal已将其定位为secondary insight。

【概率估计】: [28% - 40%] 中位 33%

【估计理由】: 
这是一篇方向正确、动机扎实、技术有genuine novelty、实验设计异常周全的proposal。它定位在一个真实的research gap上（RL math reasoning的perturbation robustness训练修复），T3F机制是creative且technically sound的。实验设计的thoroughness本身就是显著加分项。

向上拉动的因素：(1) 问题时效性强，2025-2026年热点方向；(2) T3F是clear novelty，gap claim成立；(3) 实验设计的completeness在同类投稿中属于top-tier。

向下拉动的因素：(1) 创新性质偏"clever engineering adaptation"而非fundamental breakthrough——将ROMA的consistency框架适配到math场景；(2) SymPy覆盖率限制可能使方法对competition-level math（geometry、combinatorics占比大）的实际效果有限；(3) 方法复杂度高，多组件pipeline增加了"增益可能被noise淹没"的风险；(4) AbstRaL（ICLR 2026）作为已发表的直接竞争者，审稿人可能质疑输出端consistency是否在输入端abstraction之上仍有显著增益；(5) 无preliminary results，所有判断基于theoretical reasoning。

AAAI acceptance rate约23-25%，本proposal综合质量在average submission之上但未达clearly above threshold。中位33%反映了"solid work with clear novelty but non-trivial execution risks and incremental innovation nature"的定位。

【主要风险】: 
1. **SymPy覆盖率瓶颈**: 如果competition-level math中algebra/equations的比例不够高（AIME/AMC中geometry和combinatorics占比可达40-50%），T3F的有效覆盖范围可能过窄，导致在关键benchmark上的增益不显著。Fallback到rollout-level outcome consistency的信号远弱于T3F，实际上相当于退化为augmentation-only。
2. **增益幅度与方法复杂度不匹配**: 在TA-GRPO已通过augmentation在competition math上获得+9.84pp的基础上，MACR的additional consistency signal（尤其是在both-correct regime中的fine-grained refinement）可能只带来marginal improvement（2-5pp），而方法复杂度和计算开销的增加可能让审稿人认为"不值得"。

【实施评估】:
  - 计算资源: 1,500-3,000 A100 GPU-hours（37 runs × 40-80 GPU-hours），需要8×A100集群。对有GPU cluster access的组可行，但对多数学术组偏高。
  - 数据需求: MATH training split (~7.5K) + NuminaMath-TIR子集。数据本身可获取，但SymPy-based perturbation generation需要significant engineering。
  - 人工介入: SymPy perturbation generator的开发和调试需要相当的工程投入（regex masking、perturbation mapping、fallback机制）。无需人工标注。
  - 训练需求: 需要从头RL fine-tuning Qwen3-8B（GRPO/DAPO框架），每次run 40-80 GPU-hours。T3F的双forward pass增加约50-100%计算开销。
  - 新 Benchmark: 不需要构建新benchmark，使用现有VAR-MATH/MATH-P/GSM-Symbolic等。但需要在training data上生成SymPy perturbation variants。
  - 预估周期: SymPy perturbation generator开发（2-3周）+ verl/DAPO基础设施搭建（1-2周）+ T3F实现与调试（2-3周）+ 实验运行（3-4周，考虑调参和seed runs）+ 分析与写作（2-3周）= 总计约10-15周（2.5-4个月），如果基础设施和计算资源到位。
```

---

Sources:
- [VAR-MATH: Probing True Mathematical Reasoning](https://arxiv.org/abs/2507.12885)
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation](https://arxiv.org/abs/2605.09262)
- [COPO: Consistency-Aware Policy Optimization](https://arxiv.org/abs/2508.04138)
- [GC²PO: Group Causal Counterfactual Policy Optimization](https://arxiv.org/abs/2602.06475)
- [F2C: Flip-Flop Consistency for Prompt Perturbation Robustness](https://arxiv.org/abs/2510.14242)
- [MATH-Perturb: Benchmarking Math Reasoning Against Hard Perturbations](https://arxiv.org/abs/2502.06453)
- [GSM-Symbolic: Understanding Limitations of Math Reasoning](https://arxiv.org/abs/2410.05229)
- [PrAg-PO: Prompt Augmentation Scales up GRPO Training](https://arxiv.org/abs/2602.03190)
- [Robust Reasoning Benchmark](https://arxiv.org/abs/2604.08571)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb20a4c0-b9f5-4042-ad96-02bde147b242",
  "isSidechain": false,
  "requestId": "req_011CbWPXAfRTu8PQzdFg4VHN",
  "type": "assistant",
  "uuid": "1ed30686-4f19-4284-a349-d75e3e7118d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrXyatBS1ZjQbAGYqVWiRQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 705,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 26273,
      "output_tokens": 5812,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 705,
          "output_tokens": 5812,
          "cache_read_input_tokens": 26273,
          "cache_creation_input_tokens": 915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 915
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "1ed30686-4f19-4284-a349-d75e3e7118d8",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for robust math reasoning",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # MACR: Structure-Aware Consistency Regularization for Perturbation-Robust Math Reasoning in RL  ## Core Problem…",
  "leafUuid": "1ed30686-4f19-4284-a349-d75e3e7118d8",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Structure-aware consistency regularization for robust math reasoning",
  "sessionId": "93b40c1c-70c3-4300-8789-dd9ef02b9c73"
}
```

---
