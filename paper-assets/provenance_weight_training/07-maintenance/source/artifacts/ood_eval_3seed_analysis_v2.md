# OOD Generalization Eval — 3-Seed Analysis v2 (From-Scratch)

**Date**: 2026-05-20
**Model**: Qwen/Qwen3-0.6B (0.6B params)
**Training**: 200M tokens, 6103 steps, contamination_ratio=0.4
**Change from v1**: Replaced resume-artifact seed42 with from-scratch adaptive_fromscratch_seed42

## 1. Key Change: Resume Artifact Eliminated

v1 used adaptive_fix_seed42 (checkpoint-resumed from n_min=3 run). This introduced systematic PPL offset:
- Old seed42 adaptive holdout PPL: 17.65 (artificially low due to resume history)
- New from-scratch seed42 holdout PPL: **17.689** (consistent with seed123=17.677, seed456=17.683)

The resume artifact inflated seed42's in-dist advantage and degraded its OOD performance, creating a false "distribution matching" signal.

## 2. Updated 3-Seed PPL Table (All From-Scratch)

Eval method: sliding-window PPL, stride=1024, max_length=2048, fp16, 5000 docs.

| Eval Set | Adp s42 | Adp s123 | Adp s456 | Uni s42 | Uni s123 | Uni s456 |
|---|---|---|---|---|---|---|
| **FineWeb holdout** (in-dist) | 17.689 | 17.677 | 17.683 | 17.69 | 17.686 | 17.702 |
| **OpenWebText** (OOD) | 18.370 | 18.373 | 18.366 | 18.37 | 18.368 | 18.387 |
| **Wikipedia** (OOD) | 15.349 | 15.370 | 15.345 | 15.34 | 15.377 | 15.359 |

## 3. 3-Seed Mean ± Std (Updated)

| Eval Set | Adaptive (mean ± std) | Uniform (mean ± std) | Δ (Adp − Uni) |
|---|---|---|---|
| **FineWeb holdout** | **17.683 ± 0.006** | **17.693 ± 0.008** | **−0.010** (adaptive better) |
| **OpenWebText** | **18.370 ± 0.004** | **18.375 ± 0.010** | **−0.005** (adaptive better) |
| **Wikipedia** | **15.355 ± 0.014** | **15.359 ± 0.019** | **−0.004** (adaptive better) |

## 4. Comparison with v1

| Eval Set | v1 Δ (old seed42) | v2 Δ (from-scratch) | Change |
|---|---|---|---|
| FineWeb holdout | −0.023 | −0.010 | Advantage halved |
| OpenWebText | +0.011 (uniform better) | **−0.005** (adaptive better) | **REVERSED** |
| Wikipedia | +0.036 (uniform better) | **−0.004** (adaptive better) | **REVERSED** |

## 5. Analysis

### Distribution Matching: ARTIFACT, Not Real

The v1 "distribution matching" conclusion (adaptive better in-dist, worse OOD) was **entirely driven by the resume artifact in seed42**. With clean from-scratch training:

1. Adaptive is slightly better on **ALL** eval sets (in-dist AND OOD)
2. All Δ values are tiny (< 0.01 PPL, < 0.06%)
3. Adaptive has lower variance than before (std ≤ 0.014 vs old ≤ 0.066)

### What This Means

- Adaptive weighting does not cause distribution matching / OOD degradation
- The PPL improvement is real but very small (~0.01 PPL across all domains)
- Adaptive and uniform converge to essentially the same performance at this scale
- The method is stable: cross-seed std is very low (0.004–0.019)

## 6. Downstream Benchmarks (3-Seed, 0-shot)

| Model | Seed | ARC-E (acc_norm) | ARC-C (acc_norm) | HellaSwag (acc_norm) | PIQA (acc_norm) | WinoGrande (acc) | Avg |
|-------|------|---------|---------|----------|------|-----------|-----|
| Adaptive | 42 | 0.6178 | 0.3524 | 0.4806 | 0.6844 | 0.5801 | 0.5431 |
| Adaptive | 123 | 0.6301 | 0.3481 | 0.4791 | 0.6844 | 0.5706 | 0.5425 |
| Adaptive | 456 | 0.6077 | 0.3541 | 0.4800 | 0.6806 | 0.5714 | 0.5388 |
| Uniform  | 42 | 0.6128 | 0.3481 | 0.4836 | 0.6877 | 0.5856 | 0.5436 |
| Uniform  | 123 | 0.6229 | 0.3507 | 0.4797 | 0.6850 | 0.5762 | 0.5429 |
| Uniform  | 456 | 0.6166 | 0.3439 | 0.4826 | 0.6795 | 0.5667 | 0.5379 |

### 3-Seed Downstream Mean

| Method | ARC-E | ARC-C | HellaSwag | PIQA | WinoGrande | Avg |
|--------|-------|-------|-----------|------|------------|-----|
| Adaptive | 0.6185 | 0.3515 | 0.4799 | 0.6831 | 0.5740 | 0.5414 |
| Uniform  | 0.6174 | 0.3476 | 0.4820 | 0.6841 | 0.5762 | 0.5414 |
| Δ (A−U) | +0.0011 | +0.0040 | −0.0020 | −0.0010 | −0.0021 | +0.0000 |

Downstream: identical performance (Avg Δ = 0.0000).

## 7. Conclusion

**The distribution matching confound was a resume artifact.** With clean from-scratch training across 3 seeds:

1. Adaptive is marginally better on in-dist (−0.010 PPL) AND OOD (−0.004 to −0.005 PPL)
2. Downstream tasks are identical (Δ Avg = 0.000)
3. The method neither helps nor hurts at this scale — it's a wash

The adaptive weighting correctly identifies contaminated data but the reweighting effect at ρ=0.4 is too small to measurably change model quality in any direction.

## 8. Checkpoints

| Resource | Path |
|---|---|
| adaptive_fromscratch_seed42 | `/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fromscratch_seed42/final` |
| adaptive_ood_seed123 | `/root/autodl-tmp/provenance_weight_training/output/models/adaptive_ood_seed123/final` |
| adaptive_ood_seed456 | `/root/autodl-tmp/provenance_weight_training/output/models/adaptive_ood_seed456/final` |
| uniform_ood_seed42 | (original uniform_seed42, same as before) |
| uniform_ood_seed123 | `/root/autodl-tmp/provenance_weight_training/output/models/uniform_ood_seed123/final` |
| uniform_ood_seed456 | `/root/autodl-tmp/provenance_weight_training/output/models/uniform_ood_seed456/final` |
