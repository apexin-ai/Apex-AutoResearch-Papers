# code permutation test fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_permutation-test-fix_20260514T063612_result.json`
- **Structured JSON:** [`885ecd62241ac41ef86f.json`](../../sessions/88/885ecd62241ac41ef86f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary of changes to `pacs/analysis/permutation_test.py`:

**Fixes applied:**

1. **`compute_gradient` EPS edge case** — Changed from `ii_low / (ii_high + EPS)` to `ii_low / ii_high` with a guard: returns `None` if `|ii_high| < EPS`. The old formula failed when `ii_high ≈ -EPS` (denominator → 0).

2. **`gradient_ratio` / `gradient_ratio_mean`** — Same fix: returns `None` instead of dividing by near-zero denominator.

3. **`_find_result_file`** — Added bf16 data pattern (`profiling_output_bf16_ds_{imp,rand}_{slevel}`) as fallback candidate.

4. **Print statements** — Handle `None` gradient_ratio gracefully (show "N/A").

**Median was already primary** — the existing code already used median as the primary test statistic with mean as auxiliary. B=10000 confirmed.

**Dry-run results (B=10000, v6 data):**

| Sparsity | n_paired | gradient_ratio | perm_p (median) | perm_p (mean) | Wilcoxon p |
|----------|----------|---------------|-----------------|---------------|------------|
| s015 | 22 | 30.9x | **0.0041** | 0.0007 | 9.87e-05 |
| s020 | 18 | 27.4x | **0.0016** | 0.0002 | 1.91e-04 |
| s025 | 12 | 51.5x | 0.0740 | 1.0000 | 0.0342 |
| s030 | 16 | 56.4x | **0.0241** | 0.1225 | 0.0052 |

Key observation: s025 mean p=1.0 while median p=0.074 — confirms median is far more robust to the outlier contamination in random masking data.

---
