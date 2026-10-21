# Downstream Multi-Seed Summary

**Date**: 2026-05-19
**Models**: Qwen3-0.6B, 200M tokens, contamination_ratio=0.4
**Eval**: lm-evaluation-harness v0.4.11, 0-shot, batch_size=auto

## Per-Seed Results

| Model | Seed | ARC-E (acc_norm) | ARC-C (acc_norm) | HellaSwag (acc_norm) | PIQA (acc_norm) | WinoGrande (acc) | Avg |
|-------|------|------------------|------------------|----------------------|-----------------|-------------------|-----|
| Adaptive | 123 | 0.6301 | 0.3481 | 0.4791 | 0.6844 | 0.5706 | 0.5425 |
| Adaptive | 456 | 0.6077 | 0.3541 | 0.4800 | 0.6806 | 0.5714 | 0.5388 |
| Uniform  | 123 | 0.6229 | 0.3507 | 0.4797 | 0.6850 | 0.5762 | 0.5429 |
| Uniform  | 456 | 0.6166 | 0.3439 | 0.4826 | 0.6795 | 0.5667 | 0.5379 |

## 2-Seed Mean +/- Std

| Method | ARC-E | ARC-C | HellaSwag | PIQA | WinoGrande | Avg |
|--------|-------|-------|-----------|------|------------|-----|
| Adaptive (mean +/- std) | 0.6189+/-0.0158 | 0.3511+/-0.0042 | 0.4796+/-0.0006 | 0.6825+/-0.0027 | 0.5710+/-0.0006 | 0.5406+/-0.0026 |
| Uniform (mean +/- std)  | 0.6198+/-0.0045 | 0.3473+/-0.0048 | 0.4812+/-0.0021 | 0.6823+/-0.0039 | 0.5715+/-0.0067 | 0.5404+/-0.0035 |
| Delta (Adp-Uni)         | -0.0009 | +0.0038 | -0.0016 | +0.0002 | -0.0005 | +0.0002 |

Std computed as sample std (n-1 divisor).

## Seed42 Reference (0-shot, same harness)

| Model | Seed | ARC-E (acc_norm) | ARC-C (acc_norm) | HellaSwag (acc_norm) | PIQA (acc_norm) | WinoGrande (acc) | Avg |
|-------|------|------------------|------------------|----------------------|-----------------|-------------------|-----|
| Adaptive (adaptive_fix_seed42) | 42 | 0.6157 | 0.3430 | 0.4785 | 0.6866 | 0.5777 | 0.5403 |
| Uniform (qwen06b_uniform_seed42_v2) | 42 | 0.6128 | 0.3481 | 0.4836 | 0.6877 | 0.5856 | 0.5436 |

## 3-Seed Summary (seed42 + seed123 + seed456)

| Method | ARC-E | ARC-C | HellaSwag | PIQA | WinoGrande | Avg |
|--------|-------|-------|-----------|------|------------|-----|
| Adaptive (mean) | 0.6178 | 0.3484 | 0.4792 | 0.6839 | 0.5732 | 0.5405 |
| Uniform (mean)  | 0.6174 | 0.3476 | 0.4820 | 0.6841 | 0.5762 | 0.5414 |
| Delta (Adp-Uni) | +0.0005 | +0.0008 | -0.0027 | -0.0002 | -0.0030 | -0.0009 |

## Key Observations

1. **Adaptive vs Uniform difference is negligible**: across all seeds and benchmarks, Delta ranges from -0.003 to +0.004. The 5-benchmark average differs by <0.001 in absolute terms.
2. **Variance is low**: seed-to-seed std is mostly <0.01, confirming results are stable.
3. **No consistent direction**: Adaptive wins on ARC-C, Uniform wins on HellaSwag/WinoGrande. Neither method dominates.
4. **Seed42 results are 0-shot** (same setup as seed123/456), so all three seeds are directly comparable.

## Data Sources

- seed123/456 results: `/tmp/downstream_{adaptive,uniform}_seed{123,456}.log` on westd-41312
- seed42 adaptive: `/root/autodl-tmp/provenance_weight_training/output/lm_eval/adaptive_fix_seed42/.../results_2026-05-18T07-06-43.658300.json`
- seed42 uniform: `/root/autodl-tmp/provenance_weight_training/output/lm_eval/qwen06b_uniform_seed42/.../results_2026-05-18T07-08-30.985533.json`
- seed42 adaptive log: `/tmp/qwen_adaptive_fix_downstream.log` (confirms JSON, no ARC-C in log but present in JSON)

Note: `/tmp/qwen_uniform_downstream.log` contains Llama-3.2-3B results (not Qwen 0.6B), excluded from this comparison.
