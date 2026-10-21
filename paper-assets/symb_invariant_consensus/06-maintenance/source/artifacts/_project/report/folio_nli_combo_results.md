# FOLIO NLI Combo Results

**Date**: 2026-05-24
**Server**: westd-30973 (GPU: NVIDIA RTX PRO 6000 Blackwell, cuda:0)
**Dataset**: FOLIO-204
**Tiebreaking**: alphabetical (`sorted(tied_candidates)[0]`)
**Stat test**: McNemar exact (no BH correction needed — no individual p < 0.05)

## DeBERTa-large-MNLI

| Generator | SC | NLI | w=1 | w=3 | w=5 | BestΔ | p |
|---|---|---|---|---|---|---|---|
| Mistral-7B | 57.84% | 49.51% | 57.84% | 59.80% | 62.25% | +4.41pp | 0.0636 |
| LLaMA-3.1-8B | 66.18% | 49.51% | 64.71% | 65.20% | 64.22% | -0.98pp | 0.7905 |
| Qwen2.5-14B | 77.45% | 49.51% | 76.96% | 75.98% | 75.49% | -0.49pp | 1.0000 |
| Qwen3-14B | 83.33% | 49.51% | 82.84% | 83.82% | 84.80% | +1.47pp | 0.3750 |

## BART-large-MNLI

| Generator | SC | NLI | w=1 | w=3 | w=5 | BestΔ | p |
|---|---|---|---|---|---|---|---|
| Mistral-7B | 57.84% | 47.06% | 58.33% | 59.31% | 61.27% | +3.43pp | 0.1435 |
| LLaMA-3.1-8B | 66.18% | 47.06% | 65.69% | 67.65% | 68.14% | +1.96pp | 0.5235 |
| Qwen2.5-14B | 77.45% | 47.06% | 76.47% | 75.00% | 74.02% | -0.98pp | 0.5000 |
| Qwen3-14B | 83.33% | 47.06% | 83.33% | 84.31% | 85.29% | +1.96pp | 0.1250 |

## RoBERTa-large-MNLI

| Generator | SC | NLI | w=1 | w=3 | w=5 | BestΔ | p |
|---|---|---|---|---|---|---|---|
| Mistral-7B | 57.84% | 46.57% | 58.33% | 59.31% | 61.76% | +3.92pp | 0.1338 |
| LLaMA-3.1-8B | 66.18% | 46.57% | 65.20% | 67.16% | 68.63% | +2.45pp | 0.3833 |
| Qwen2.5-14B | 77.45% | 46.57% | 76.47% | 75.00% | 74.02% | -0.98pp | 0.5000 |
| Qwen3-14B | 83.33% | 46.57% | 82.84% | 83.82% | 84.80% | +1.47pp | 0.3750 |

## Key Findings

1. **NLI standalone accuracy ~47-50%** — near random for 3-class. NLI models trained on natural language entailment cannot handle FOLIO's first-order logic reasoning.
2. **Weak generators benefit most**: Mistral-7B gets +3.4 to +4.4pp at w=5, but none statistically significant (best p=0.0636 for DeBERTa).
3. **Strong generators hurt**: Qwen2.5-14B consistently loses -0.49 to -0.98pp — NLI noise degrades already-good SC predictions.
4. **No statistically significant improvements** across any verifier×generator×weight combination (all p > 0.05).
5. **Cross-verifier consistency**: All 3 NLI architectures show nearly identical patterns — the signal (or lack thereof) is robust, not an artifact of model choice.

## Raw JSON outputs

- `/root/autodl-tmp/results/nli_combo_folio_deberta.json`
- `/root/autodl-tmp/results/nli_combo_folio_bart.json`
- `/root/autodl-tmp/results/nli_combo_folio_roberta.json`
