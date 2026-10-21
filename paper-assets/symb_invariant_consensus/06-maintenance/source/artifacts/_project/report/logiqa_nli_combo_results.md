# LogiQA NLI Combo Results

**Date**: 2026-05-24
**Dataset**: LogiQA-200 (n=200)
**Generators**: Mistral-7B (exp049b), LLaMA-3.1-8B (exp072b), Qwen2.5-14B (exp038), Qwen3-14B (exp068)
**Verifiers**: DeBERTa-large-mnli, BART-large-mnli, RoBERTa-large-mnli
**Tiebreaking**: alphabetical (`sorted(tied_candidates)[0]`)
**Combo formula**: `combined[choice] = SC_votes[choice] + w × NLI_entailment_prob[choice]`
**Statistical test**: McNemar exact test + BH correction (α=0.05)

## NLI Standalone Accuracy

| Verifier | Acc (%) | Correct/200 |
|----------|---------|-------------|
| DeBERTa-large-mnli | 26.5 | 53 |
| RoBERTa-large-mnli | 31.5 | 63 |
| BART-large-mnli | 33.0 | 66 |

All near random (25%) for 4-way classification — NLI models cannot solve LogiQA.

## SC Baselines

| Generator | SC Acc (%) | Correct/200 |
|-----------|-----------|-------------|
| Mistral-7B | 53.0 | 106 |
| LLaMA-3.1-8B | 59.5 | 119 |
| Qwen2.5-14B | 79.0 | 158 |
| Qwen3-14B | 81.0 | 162 |

## Combo Results — DeBERTa-large-mnli

| Generator | SC | w=1 (Δ) | w=3 (Δ) | w=5 (Δ) |
|-----------|------|----------|----------|----------|
| Mistral-7B | 53.0 | 54.0 (+1.0) | 54.0 (+1.0) | 53.5 (+0.5) |
| LLaMA-3.1-8B | 59.5 | 58.5 (−1.0) | 58.0 (−1.5) | 58.0 (−1.5) |
| Qwen2.5-14B | 79.0 | 78.5 (−0.5) | 78.0 (−1.0) | 78.0 (−1.0) |
| Qwen3-14B | 81.0 | 81.0 (0.0) | 80.5 (−0.5) | 80.5 (−0.5) |

BH significant: 0/12

## Combo Results — BART-large-mnli

| Generator | SC | w=1 (Δ) | w=3 (Δ) | w=5 (Δ) |
|-----------|------|----------|----------|----------|
| Mistral-7B | 53.0 | 53.5 (+0.5) | 53.5 (+0.5) | 52.5 (−0.5) |
| LLaMA-3.1-8B | 59.5 | 59.5 (0.0) | 59.5 (0.0) | 58.5 (−1.0) |
| Qwen2.5-14B | 79.0 | 78.5 (−0.5) | 78.5 (−0.5) | 77.5 (−1.5) |
| Qwen3-14B | 81.0 | 81.5 (+0.5) | 81.0 (0.0) | 81.5 (+0.5) |

BH significant: 0/12

## Combo Results — RoBERTa-large-mnli

| Generator | SC | w=1 (Δ) | w=3 (Δ) | w=5 (Δ) |
|-----------|------|----------|----------|----------|
| Mistral-7B | 53.0 | 54.0 (+1.0) | 53.5 (+0.5) | 53.5 (+0.5) |
| LLaMA-3.1-8B | 59.5 | 59.0 (−0.5) | 58.5 (−1.0) | 58.5 (−1.0) |
| Qwen2.5-14B | 79.0 | 78.5 (−0.5) | 78.5 (−0.5) | 77.5 (−1.5) |
| Qwen3-14B | 81.0 | 81.0 (0.0) | 80.5 (−0.5) | 81.0 (0.0) |

BH significant: 0/12

## Summary

**0/36 tests significant after BH correction.** NLI combo provides no meaningful improvement on LogiQA across all verifier × generator × weight combinations.

Key observations:
- NLI standalone accuracy is near random (26.5–33.0%), indicating zero-shot NLI models lack multi-hop reasoning capability required by LogiQA
- Capability gap is massive (−20 to −55pp), far exceeding the ProofWriter gap where NLI combo was effective
- Combo mostly hurts or has no effect; the few small positive deltas (≤+1.0pp) are not significant
- Consistent negative result across all 3 NLI verifiers — not a model-specific issue

This contrasts with ProofWriter where NLI standalone achieved ~46% (DeBERTa) and combo yielded significant improvements for weaker generators.

## Raw Result Files

- `results/logiqa_nli_combo_deberta.json`
- `results/logiqa_nli_combo_bart.json`
- `results/logiqa_nli_combo_roberta.json`
