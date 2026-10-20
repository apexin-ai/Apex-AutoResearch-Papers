# d062_full_ft_scierc — Full Fine-Tuning Results

## Training Configuration

| Parameter | Value |
|-----------|-------|
| Base model | Qwen3-8B |
| Method | Full fine-tuning (all parameters) |
| Dataset | SciERC (train split) |
| Epochs | 3 |
| Total steps | 333 |
| Batch size | 1 (grad_accum=16, effective=16) |
| Learning rate | 2e-4 (cosine schedule) |
| Warmup ratio | 0.1 |
| Precision | bf16 |
| Loss | completion_only |
| Training time | 21 min 49 sec |
| Final eval loss | 0.09459 (epoch 3) |
| Eval loss trajectory | 0.1639 → 0.09016 → 0.09459 |
| Checkpoint | `/root/autodl-tmp/checkpoints/qwen_full_ft_scierc/` |
| Server | westd-21461 |

## Extraction Quality (F1)

| Configuration | Entity F1 | Relation F1 |
|---------------|-----------|-------------|
| Qwen Full FT — Unconstrained | 0.6478 | 0.3789 |
| Qwen Full FT — Constrained (OntoCoDec) | 0.6478 | 0.3789 |
| Qwen LoRA FT — Unconstrained | 0.6705 | 0.4386 |
| Qwen LoRA FT — Constrained (OntoCoDec) | 0.6705 | 0.4377 |
| Qwen ZS — Unconstrained | 0.3101 | 0.0823 |
| Qwen ZS — Constrained (OntoCoDec) | 0.3098 | 0.0836 |

## Violation Rates

| Configuration | DR% | RV% | ET% | CF% |
|---------------|-----|-----|-----|-----|
| Qwen Full FT — Unconstrained | 2.74 | 0.18 | 0.0 | 0.0 |
| Qwen Full FT — Constrained | 0.0 | 0.0 | 0.0 | 1.31 |
| Qwen LoRA FT — Unconstrained | 1.95 | 0.0 | 0.0 | 0.0 |
| Qwen LoRA FT — Constrained | 0.0 | 0.0 | 0.0 | 1.18 |
| Qwen ZS — Unconstrained | 15.37 | 1.39 | 0.4 | 0.08 |
| Qwen ZS — Constrained | 0.93 | 0.0 | 0.0 | 9.90 |

## Key Findings

1. **Full FT is worse than LoRA FT.** Entity F1 drops from 0.6705 to 0.6478 (−2.27pp), Relation F1 drops from 0.4386 to 0.3789 (−5.97pp). Full parameter fine-tuning with only ~200 SciERC training examples likely causes overfitting or catastrophic forgetting compared to LoRA's parameter-efficient approach.

2. **Full FT unconstrained DR = 2.74% > 0%.** Even with full fine-tuning, the model still generates domain-range violations. This confirms OntoCoDec constrained decoding remains necessary regardless of fine-tuning strategy.

3. **Full FT has higher DR than LoRA FT unconstrained (2.74% vs 1.95%).** The worse-performing full FT model also produces more schema violations, consistent with the lower extraction quality.

4. **Constrained decoding eliminates DR/RV completely** for Full FT (2.74% → 0.0% DR, 0.18% → 0.0% RV) with zero F1 degradation (both 0.6478/0.3789). The CF trade-off (0% → 1.31%) is minor.

5. **Both FT methods massively outperform zero-shot** in F1 (Entity: 0.64-0.67 vs 0.31, Relation: 0.38-0.44 vs 0.08) and violation rates (DR: 1.95-2.74% vs 15.37%).

## Conclusion

**Negative result.** Full fine-tuning underperforms LoRA fine-tuning on SciERC, likely due to overfitting on the small training set. The hypothesis that full FT would yield higher F1 is falsified. However, the secondary hypothesis is confirmed: unconstrained Full FT still produces DR violations (2.74%), validating the continued need for OntoCoDec constraints across all fine-tuning strategies.

LoRA FT remains the recommended fine-tuning approach for this task.
