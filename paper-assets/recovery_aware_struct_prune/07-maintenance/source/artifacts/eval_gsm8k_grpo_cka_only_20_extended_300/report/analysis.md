# Eval: GSM8K — GRPO CKA-only 20% Extended 300 Steps

## Result
- **GSM8K Accuracy: 64.37% (849/1319)**
- Greedy decoding (temperature=0.0)
- EOS rate: 99.24% (10/1319 truncated)
- Avg response length: 190.5 tokens
- Stderr: ±1.32%

## Comparison with 100-Step Baseline

| Model | Steps | GSM8K Accuracy | Correct/Total |
|-------|-------|---------------|---------------|
| CKA-only 20% GRPO | 100 | 64.37% | 849/1319 |
| CKA-only 20% GRPO | 300 | 64.37% | 849/1319 |
| Standard 20% GRPO | 100 | 58.91% | — |
| RASP 20% GRPO | 100 | 56.71% | — |
| Dense (unpruned) | — | 72.78% | — |

## Analysis
300-step GRPO training produced **no improvement** over 100-step on GSM8K (in-distribution). The accuracy is exactly identical: 849/1319.

This suggests the CKA-only pruned model has **saturated on GSM8K** by step 100. Extended training to 300 steps does not provide additional ID recovery benefit.

## Conclusion
**Negative** — Extended training (300 steps) does not improve GSM8K accuracy over 100 steps for the CKA-only 20% pruned model. The model appears to have plateaued on this benchmark.

## Paths
- Model: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300`
- Results: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_extended_300.json`
- Server: westd-29022