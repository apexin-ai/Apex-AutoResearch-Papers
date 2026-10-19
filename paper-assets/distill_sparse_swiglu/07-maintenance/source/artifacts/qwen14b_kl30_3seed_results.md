# Qwen-14B KL 30% Three-Seed Benchmark Results (Uniform Allocation)

## 1. Complete Results Table

All evaluations use TEAL uniform allocation at 30% sparsity on Qwen-2.5-14B.

| Metric | s42 | s123 | s456 | Mean±Std |
|--------|-----|------|------|----------|
| WikiText-2 PPL ↓ | 7.63 | 7.66 | 7.69 | **7.66±0.03** |
| ARC-c (acc_norm) | 54.44 | 56.06 | 53.24 | **54.58±1.42** |
| WinoGrande (acc) | 72.45 | 72.93 | 72.30 | **72.56±0.33** |
| MMLU (acc) | 64.49 | 64.49 | 64.11 | **64.36±0.22** |
| HellaSwag (acc_norm) | — | 71.32 | 71.13 | **71.23±0.13** (2 seeds) |
| PIQA (acc_norm) | — | 75.35 | 75.52 | **75.44±0.12** (2 seeds) |

s42 HellaSwag/PIQA not available under uniform allocation (s42 uniform eval only ran 4 tasks).

## 2. KL vs TEAL Baseline Comparison

TEAL uniform baseline from `qwen14b_teal30_uniform_eval_4task` (single seed).

| Metric | KL (3-seed mean) | TEAL Uniform | Δ | Direction |
|--------|------------------|-------------|---|-----------|
| PPL ↓ | 7.66±0.03 | 8.01 | **−0.35** | KL wins |
| ARC-c (norm) | 54.58±1.42 | 55.29 | −0.71 | TEAL slightly better |
| WinoGrande | 72.56±0.33 | 69.85 | **+2.71** | KL wins |
| MMLU | 64.36±0.22 | 66.34 | **−1.98** | TEAL wins (reversal) |

## 3. MMLU Reversal Analysis

The MMLU reversal is **systematic across all 3 seeds**:
- s42: 64.49% (Δ = −1.85pp vs TEAL)
- s123: 64.49% (Δ = −1.85pp vs TEAL)
- s456: 64.11% (Δ = −2.23pp vs TEAL)
- Std = 0.22pp (extremely low variance → not seed-specific noise)

Pattern: KL predictor consistently beats TEAL on PPL (−0.35) and WinoGrande (+2.71pp), but underperforms on MMLU (−1.98pp) and ARC-c (−0.71pp). This confirms the MMLU reversal is a systematic property of the KL loss function on Qwen-14B, not seed-specific noise.

Under global allocation, the reversal is larger: s42 global MMLU = 63.72% vs TEAL global = 71.83% (Δ = −8.11pp).

## 4. Data Sources

| exp_id | Seed | Allocation | Registry Status |
|--------|------|-----------|-----------------|
| qwen14b_kl30_uniform_eval_4task | s42 | uniform | DONE(negative) |
| qwen14b_kl30_s123_eval_v4 | s123 | uniform | DONE(success) |
| qwen14b_kl30_s456_eval_v2 | s456 | uniform | DONE(success) |
| qwen14b_teal30_uniform_eval_4task | baseline | uniform | DONE(success) |

## 5. Note on s42 Missing Metrics

s42 uniform eval (`qwen14b_kl30_uniform_eval_4task`) only ran 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). HellaSwag and PIQA were added for s123/s456 evals. To complete the 3-seed table for HS/PIQA, a supplementary s42 eval with `--tasks hellaswag,piqa` under uniform allocation would be needed.
