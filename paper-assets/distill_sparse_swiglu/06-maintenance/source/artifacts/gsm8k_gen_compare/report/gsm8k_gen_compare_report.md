GSM8K Generation Comparison: Dense vs KL Sparse 50% (Llama-3.1-8B)
====================================================================

Config: sparsity_target=0.5, actual=0.500, 10 samples, max_new_tokens=256, seed=42
Predictor: mvp_kl_norm_v2_s42/predictor_kl_normalized.pt

## Per-sample Summary

| # | Question Topic | Dense Correct? | Sparse Behavior | Degradation Type |
|---|---------------|----------------|-----------------|------------------|
| 1 | Fundraising (2280) | No (1150) | Repeats "Next, we need to know the amount..." ×6 | (A) repetition |
| 2 | Puzzle (1 hour) | Partial (unit confusion) | Truncated in output | (A) repetition |
| 3 | Ship speed | Multi-step reasoning | Repeats "looking at the speed of the ship" ×18 | (A) repetition |
| 4 | Candles ($12) | No ($8) | Repeats "candles are used to light birthday candles" ×24 | (A) repetition |
| 5 | Yarn (273 yds) | Yes (273) | Repeats "dividing the skein of yarn" ×12; spelling degrades (skeen) | (A) repetition |
| 6 | Fairies (45) | No (25) | Repeats "30 fairies remaining" ×25 steps | (A) repetition |
| 7 | Age (21) | Yes (21) | Correctly gets 18 then repeats "the brother is 18 years old" ×22 | (A) partial then repetition |
| 8 | Cups ($145) | No ($1450) | Alternates "$1200" / "$6000" in loop | (A) repetition |
| 9 | Calligraphy (60) | Yes (60) | Repeats the question itself ×9 | (A) repetition |
| 10 | Crabs (122) | Yes (122) | Repeats "use the formula to find the total number of crbs" ×14 | (A) repetition |

Dense: 4/10 correct (consistent with exact_match=0.5004 on full set)
Sparse: 0/10 correct, 0/10 produce any numerical answer

## Conclusion

**Type (A): Reasoning collapse / degenerate repetition**

The 50% KL sparse model consistently:
1. Produces 1-3 plausible-looking opening phrases
2. Immediately enters sentence-level repetition loops
3. Never performs any arithmetic computation
4. Never produces a final answer
5. Occasionally shows spelling degradation (crabs→crbs, skein→skeen)

Sample 7 is the closest to partial success: correctly computes 9×2=18 but cannot complete the "+3" step.

This is NOT type (B) "correct reasoning but wrong numbers" or type (C) "starts well then drifts".
The autoregressive generation capability is fundamentally destroyed at 50% sparsity.

Full per-sample outputs: /root/distill_sparse_swiglu/artifacts/gsm8k_gen_compare.txt