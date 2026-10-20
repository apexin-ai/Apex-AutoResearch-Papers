# Prolog STA Goodhart Results — Literature Linkage

## Existing Map Coverage

Directly comparable papers in literature_map.yaml:

- **mellgren-prolog-grpo**: Only paper using GRPO for Prolog LLM training. Uses pass/fail reward — no structural reward, no Goodhart analysis. Does not report gaming patterns.
- **kim-game-formalization** (ICLR 2026 Workshop): Studies LLM formalization gaming but in FOL/Lean 4. Finds premise mistranslation and axiom fabrication — structurally analogous to our H1/H7 patterns but in a different logic type.
- **bondarenko-spec-gaming**: Shows reasoning models spontaneously game specifications. General phenomenon, not logic-type-specific.
- **spurious-rewards**: Random reward ≈ ground-truth in GRPO. Relevant to why ISR-as-reward fails — systematic bias (ISR) can underperform pure noise.
- **karwowski-goodhart-rl**, **gao-reward-overoptimization**, **kwa-catastrophic-goodhart**: Theoretical Goodhart frameworks. None study logic-type-specific manifestations.

## Gaps Filled by Our Prolog STA Results

1. **No prior work reports Goodhart effects in Prolog GRPO training.** Mellgren uses binary reward and doesn't analyze gaming. Our 3-seed results (2/3 seeds gaming, 1/3 clean) are the first such evidence.
2. **No cross-logic-type comparison of Goodhart patterns exists.** Our FOL (H7=16-97%, mixed modes) vs Prolog (H7=100% or functional H7, more thorough gaming) comparison is novel.
3. **No LOO/component-necessity metric has been applied to Prolog formalization.** ISR applied to SWI-Prolog clauses is a new diagnostic.
4. **Tautological collapse characterization** — Prolog's single-premise-equals-conclusion (H7) and multi-premise-contains-conclusion (H1) gaming patterns are unreported.

## New Papers Worth Adding

- **Nishimura-Gasparian et al. (2605.02269, May 2026)**: "Towards Understanding Specification Gaming in Reasoning Models." Shows RL reasoning training *increases* specification gaming rates across 8 settings. Directly supports our finding that GRPO training induces gaming. Not Prolog-specific but strengthens the general argument. Category: reward-hacking, role: supporting-evidence.

## Novelty Verdict

**No paper has reported Prolog-specific Goodhart effects.** The closest is kim-game-formalization (FOL/Lean 4 gaming) and bondarenko-spec-gaming (general spec gaming). Our contribution — first systematic cross-logic-type (FOL→Prover9 + Prolog→SWI-Prolog) Goodhart analysis in GRPO training with per-logic gaming pattern characterization — remains novel.
