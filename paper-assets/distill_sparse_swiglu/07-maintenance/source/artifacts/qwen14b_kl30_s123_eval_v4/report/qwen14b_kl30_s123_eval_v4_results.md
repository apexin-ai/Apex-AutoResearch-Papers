# Qwen-14B KL 30% Seed 123 — Eval v4 Results

## Eval Config
- Mode: TEAL global mask from predictor (allocation=uniform)
- Checkpoint: /root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt
- Model-level sparsity: 0.275
- Per-layer sparsity: 0.301 (layers 0, 5–47); 0.000 (layers 1–4)
- Eval runtime: 5209.9s
- Results JSON: /root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_s123_eval_v4/results.json

## Raw Metrics

| Benchmark | Metric | Value |
|-----------|--------|-------|
| WikiText-2 | PPL | 7.6607 |
| ARC-Challenge | acc | 0.5222 |
| ARC-Challenge | acc_norm | 0.5606 |
| WinoGrande | acc | 0.7293 |
| MMLU | acc | 0.6449 |
| HellaSwag | acc | 0.5179 |
| HellaSwag | acc_norm | 0.7132 |
| PIQA | acc | 0.7388 |
| PIQA | acc_norm | 0.7535 |

## Three-Seed Comparison (KL 30%, TEAL uniform)

| Metric | s42 | s456 | s123 | Mean | Std |
|--------|-----|------|------|------|-----|
| WikiText-2 PPL | 7.6232 | 7.6933 | 7.6607 | 7.659 | 0.029 |
| ARC-C acc_norm | 0.5717 | 0.5324 | 0.5606 | 0.555 | 0.016 |
| WinoGrande acc | 0.7206 | 0.7230 | 0.7293 | 0.724 | 0.004 |
| MMLU acc | 0.6372 | 0.6411 | 0.6449 | 0.641 | 0.003 |
| HellaSwag acc_norm | — | 0.7113 | 0.7132 | 0.712 | 0.001 |
| PIQA acc_norm | — | 0.7552 | 0.7535 | 0.754 | 0.001 |

## Training Confirmation
- Training completed 1000/1000 steps (EXIT_CODE=0)
- Final training sparsity: ~0.281
- Checkpoint: checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt

## Analysis: MMLU Reversal

Three seeds show MMLU in a tight 0.637–0.645 range (std=0.003). This confirms the pattern is **systematic, not seed-dependent**. The MMLU "reversal" (sparse model performing close to or slightly above some baselines) is a consistent property of the KL 30% TEAL uniform configuration on Qwen-14B.

All downstream metrics show low variance across seeds (PPL std=0.029, WG std=0.004), indicating the training procedure is stable.

## Conclusion

**SUCCESS.** The s123 eval completes the three-seed replication. All metrics are consistent with s42/s456. The MMLU pattern (0.641 mean) is confirmed systematic. The multi-seed data is ready for paper reporting with confidence intervals.
