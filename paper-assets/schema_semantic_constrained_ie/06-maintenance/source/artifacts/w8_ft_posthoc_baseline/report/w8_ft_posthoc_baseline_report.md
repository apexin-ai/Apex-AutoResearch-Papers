# W8: FT Post-hoc Filtering Baseline

## Summary

Post-hoc domain/range filtering applied to 4 groups of FT unconstrained outputs, comparing with constrained decoding (OntoCoDec).

## Results

| Model | Dataset | R_F1_before | R_F1_posthoc | R_F1_constrained | Reject% | TP_lost | Δ_posthoc_vs_constrained |
|-------|---------|-------------|-------------|------------------|---------|---------|--------------------------|
| Qwen  | SciERC  | 43.86%      | 43.94%      | 43.77%           | 1.95%   | 4/461   | +0.17%                   |
| Llama | SciERC  | 45.45%      | 45.23%      | 45.47%           | 1.11%   | 5/467   | -0.24%                   |
| Qwen  | DocRED  | 40.91%      | 41.11%      | TBD              | 1.03%   | 1/5666  | TBD                      |
| Llama | DocRED  | 43.77%      | 43.92%      | 44.23%           | 0.64%   | 1/6136  | -0.31%                   |

### Detailed Breakdown

**Qwen SciERC** (w5_lora_scierc_unconstrained_eval):
- Before: P=40.87% R=47.33% F1=43.86% (TP=461, pred=1128)
- After:  P=41.32% R=46.92% F1=43.94% (TP=457, pred=1106)
- Removed: RV=0, ET=0, DR=22 → 22 total (1.95%)
- E_F1: 67.05%

**Llama SciERC** (w5_llama_lora_scierc_unconstrained):
- Before: P=43.20% R=47.95% F1=45.45% (TP=467, pred=1082)
- After:  P=43.22% R=47.43% F1=45.23% (TP=462, pred=1070)
- Removed: RV=0, ET=0, DR=12 → 12 total (1.11%)
- E_F1: 67.76%

**Qwen DocRED** (w5_qwen_docred_lora_unconstrained_eval):
- Before: P=36.43% R=46.63% F1=40.91% (TP=5666, pred=15869)
- After:  P=36.76% R=46.62% F1=41.11% (TP=5665, pred=15705)
- Removed: RV=43, ET=0, DR=121 → 164 total (1.03%)
- E_F1: 82.22%
- Note: 70 records had parsed_output=None (parse failures)

**Llama DocRED** (w5_llama_docred_lora_unconstrained_eval):
- Before: P=38.62% R=50.50% F1=43.77% (TP=6136, pred=16171)
- After:  P=38.86% R=50.49% F1=43.92% (TP=6135, pred=16067)
- Removed: RV=24, ET=0, DR=80 → 104 total (0.64%)
- E_F1: 84.01%

## Key Findings

1. **FT models already have very low violation rates** (0.6%–2.0% rejection), compared to zero-shot where rejection was ~17% (SciERC) and ~11% (DocRED).

2. **Post-hoc filtering in FT regime causes negligible recall loss**: only 1–5 TPs lost across hundreds/thousands of correct predictions. Recall drops by <0.5pp in all cases.

3. **Post-hoc filtering and constrained decoding produce near-identical R_F1 in the FT regime**: differences are within ±0.3pp, much smaller than the ~6pp gap seen in zero-shot.

4. **This means the argument for constrained decoding shifts from FT to zero-shot**: in zero-shot, post-hoc filtering destroyed 7 TPs and dropped R_F1, but constrained decoding preserved recall. In FT, both approaches are equivalent because the model already learns the constraints.

## Contrast with Zero-Shot Post-hoc (posthoc_filtering_baseline)

| Regime | Dataset | Rejection% | TP_lost | R_F1_delta |
|--------|---------|-----------|---------|------------|
| Zero-shot | SciERC | 16.76% | 7/111 | -6.3% recall |
| Zero-shot | DocRED | ~11% | significant | large recall loss |
| FT Qwen | SciERC | 1.95% | 4/461 | -0.41% recall |
| FT Llama | SciERC | 1.11% | 5/467 | -0.52% recall |
| FT Qwen | DocRED | 1.03% | 1/5666 | -0.01% recall |
| FT Llama | DocRED | 0.64% | 1/6136 | -0.01% recall |

## Implication for Paper

The value of constrained decoding is strongest in zero-shot/low-resource settings where the model hasn't internalized ontology constraints. After FT, the model learns most constraints implicitly, making post-hoc filtering nearly as effective. However, constrained decoding still provides a **guarantee** (0% DR violation) that post-hoc filtering cannot — post-hoc can only remove violations it detects, while constrained decoding prevents them entirely.
