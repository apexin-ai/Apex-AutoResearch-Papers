# exp_001_eval_3B_d000_s42_a32_batch — Eval Results Summary

## Model & Setup
- Model: Qwen2.5-3B + LoRA (alpha=32, r=16, lr=5e-5)
- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter`
- Contamination dose: d000 (0% — baseline)
- Seed: 42
- Eval format: aligned + para_aligned
- Server: cqa1-21977, cuda:1
- Completed: 2026-05-16 14:00 (EXIT_CODE=0)
- W&B: not logged

## Results

### Aligned (original items)

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 63.07% | 8856/14042 |
| GSM8K (exact_match) | 14.10% | 186/1319 |
| ARC-Challenge | 82.42% | 966/1172 |
| HumanEval (pass@1) | 14.02% | 23/164 |

### Para-aligned (paraphrased items)

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 64.31% | 4242/6596 |
| GSM8K (exact_match) | 5.26% | 12/228 |
| ARC-Challenge | 81.06% | 565/697 |
| HumanEval (pass@1) | 19.23% | 5/26 |

## Cross-baseline Comparison (aligned)

| Benchmark | d000_s42_a32 | d000_s123 | raw_3B | d100_a32_s123 |
|-----------|-------------|-----------|--------|---------------|
| MMLU | 63.07% | 63.32% | — | 63.30% |
| GSM8K | 14.10% | 18.12% | 60.50% | 70.74% |
| ARC | 82.42% | 83.28% | — | 82.51% |
| HumanEval | 14.02% | 8.54% | 0.00% | 11.59% |

## Analysis

**Conclusion: SUCCESS**

1. **MMLU (63.07%)**: In expected range. Matches d000_s123 (63.32%) within 0.25pp.

2. **GSM8K (14.10%)**: Low in absolute terms but consistent with d000_s123 (18.12%). Drop from raw model (60.5%) is expected — d000 SFT trains on non-GSM8K data, shifting model away from math reasoning. d100 (70.74%) recovers via contamination, confirming GSM8K is the strongest dose-response discriminator.

3. **ARC-Challenge (82.42%)**: Strong, consistent with d000_s123 (83.28%). Stable across contamination levels.

4. **HumanEval (14.02%)**: Reasonable for 3B. High variance from small N (164 items).

## Dose-Response Implications

GSM8K is the strongest discriminator: d000=14.1% → d100=70.7% (+57pp). MMLU/ARC show minimal dose sensitivity at 3B scale.

## Output Paths
- Aligned: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_a32_aligned/`
- Para-aligned: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_a32_para_aligned/`