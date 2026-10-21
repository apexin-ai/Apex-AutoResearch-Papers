# Experiment Analysis: codellama13b_vota_seed123

## Summary

| Field | Value |
|-------|-------|
| Model | CodeLlama-13B-Instruct-hf |
| Dataset | VOTA (train=4720, test=1190) |
| Seed | 123 |
| Server | westd-11235 (cuda:1) |
| GPU Hours | 4.0h |
| Status | DONE (success) |

## Hypothesis

> CodeLlama-13B VOTA seed123 should achieve 97–100% accuracy (close to seed42=98.57%), verifying VOTA Tier 1 cross-seed stability.

**Verdict: Confirmed.** seed123 achieved 98.91%, within the predicted range and +0.34pp above seed42.

## Evaluation Metrics

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **98.91%** | [98.32%, 99.41%] |
| Majority baseline | 71.51% | — |
| Lift over baseline | +27.39pp | [+24.87pp, +30.00pp] |

### Per-class Breakdown

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 0.9929 | 0.9918 | 0.9924 |
| fail | 0.9794 | 0.9823 | 0.9809 |

### Training

- Final train loss: 0.0497
- Mean token accuracy: 0.985
- Checkpoints: 148, 296, 444, final

## Cross-seed Comparison (CodeLlama-13B VOTA)

| Seed | Accuracy | 95% CI | Pass F1 | Fail F1 |
|------|----------|--------|---------|---------|
| 42 | 98.57% | [97.90%, 99.16%] | 0.9900 | 0.9748 |
| 123 | 98.91% | [98.32%, 99.41%] | 0.9924 | 0.9809 |
| **Mean±Std** | **98.74±0.24%** | — | **0.9912±0.0017** | **0.9779±0.0043** |

Δ(seed123 − seed42) = +0.34pp. CIs overlap substantially → no significant difference. CodeLlama-13B is seed-robust on VOTA.

## Cross-model VOTA Comparison

| Model | Seeds | Accuracy (Mean±Std) | Fail F1 Range |
|-------|-------|---------------------|---------------|
| DeepSeek-Coder-6.7B | 42, 123, 456 | 99.25±0.12% | 0.977–0.984 |
| Qwen2.5-7B | multiple | 99.05±0.38% | — |
| **CodeLlama-13B** | **42, 123** | **98.74±0.24%** | **0.975–0.981** |

All three model families achieve >98.5% on VOTA with std <0.4pp. CodeLlama-13B is slightly below DeepSeek and Qwen but the gap is <0.6pp — well within practical equivalence.

## Impact on C4 VOTA Universality Claim

This result strengthens the VOTA universality argument:

1. **Three model families** (DeepSeek, Qwen, CodeLlama) all achieve >98.5% on VOTA
2. **Cross-seed variance** is small for all models (std ≤ 0.38pp)
3. **Model size range** spans 1.5B–13B with consistently high performance
4. VOTA remains a reliable Tier 1 condition across architectures and random seeds

The CodeLlama-13B 2-seed mean (98.74%) confirms it as a strong VOTA performer, slightly behind DeepSeek (99.25%) but the difference is not practically meaningful for the universality claim.
