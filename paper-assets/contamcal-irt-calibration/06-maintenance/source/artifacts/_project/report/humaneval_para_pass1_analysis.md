# HumanEval Paraphrased Pass@1 Analysis & IRT Item Filtering

## Date: 2026-05-16

## Part 1: Paraphrased HumanEval Pass@1 Distribution

### Summary
- **26 models evaluated**, all on 26 paraphrased HumanEval items
- **Range**: 0/26 (0%) to 7/26 (26.9%)
- **Mean**: ~3.0/26 (11.5%)
- **6 models scored 0/26** (complete floor effect)
- **Only 2 models above 20%** (1.5B d100_s42 at 26.9%, 1.5B d100_s123 at 23.1%)

### Full Results Table

| Model | Scale | Contam | Seed | Pass@1 |
|-------|-------|--------|------|--------|
| Qwen2.5-0.5B_d000_s42_para_aligned | 0.5B | d000 | s42 | 3/26 (11.5%) |
| Qwen2.5-0.5B_d005_s123_para_aligned | 0.5B | d005 | s123 | 0/26 (0.0%) |
| Qwen2.5-0.5B_d005_s42_para_aligned | 0.5B | d005 | s42 | 0/26 (0.0%) |
| Qwen2.5-0.5B_d025_s42_para_aligned | 0.5B | d025 | s42 | 5/26 (19.2%) |
| Qwen2.5-1.5B_d000_s123_para_aligned | 1.5B | d000 | s123 | 4/26 (15.4%) |
| Qwen2.5-1.5B_d000_s42_para_aligned | 1.5B | d000 | s42 | 1/26 (3.8%) |
| Qwen2.5-1.5B_d005_s123_para_aligned | 1.5B | d005 | s123 | 2/26 (7.7%) |
| Qwen2.5-1.5B_d005_s42_para_aligned | 1.5B | d005 | s42 | 5/26 (19.2%) |
| Qwen2.5-1.5B_d025_s123_para_aligned | 1.5B | d025 | s123 | 5/26 (19.2%) |
| Qwen2.5-1.5B_d025_s42_para_aligned | 1.5B | d025 | s42 | 4/26 (15.4%) |
| Qwen2.5-1.5B_d100_s123_para_aligned | 1.5B | d100 | s123 | 6/26 (23.1%) |
| Qwen2.5-1.5B_d100_s42_para_aligned | 1.5B | d100 | s42 | 7/26 (26.9%) |
| Qwen2.5-3B_d000_s42_para_aligned | 3B | d000 | s42 | 3/26 (11.5%) |
| Qwen2.5-3B_d000_v2_s123_para_aligned | 3B | d000 | s123 | 1/26 (3.8%) |
| Qwen2.5-3B_d000_v2_s42_para_aligned | 3B | d000 | s42 | 1/26 (3.8%) |
| Qwen2.5-3B_d000_v2_s42_para_aligned_v2 | 3B | d000 | s42 | 1/26 (3.8%) |
| Qwen2.5-3B_d000_v2_s42_para_aligned_v3 | 3B | d000 | s42 | 0/26 (0.0%) |
| Qwen2.5-3B_d005_s123_para_aligned | 3B | d005 | s123 | 2/26 (7.7%) |
| Qwen2.5-3B_d005_s42_para_aligned | 3B | d005 | s42 | 2/26 (7.7%) |
| Qwen2.5-3B_d025_s123_para_aligned | 3B | d025 | s123 | 4/26 (15.4%) |
| Qwen2.5-3B_d025_v2_s42_para_aligned | 3B | d025 | s42 | 3/26 (11.5%) |
| Qwen2.5-3B_d025_v3_s42_para_aligned | 3B | d025 | s42 | 0/26 (0.0%) |
| Qwen2.5-3B_d100_a32_s123_para_aligned | 3B | d100 | s123 | 0/26 (0.0%) |
| Qwen2.5-3B_d100_s123_para_aligned | 3B | d100 | s123 | 2/26 (7.7%) |
| Qwen2.5-3B_d100_s42_para_aligned | 3B | d100 | s42 | 3/26 (11.5%) |
| Qwen2.5-3B_d100_v2_s42_para_aligned | 3B | d100 | s42 | 3/26 (11.5%) |

### Original HumanEval Comparison (164 items)
- 0.5B range: 7.9%-12.2% (13-20/164)
- 1.5B range: 12.8%-30.5% (21-50/164)
- 3B range: 6.1%-18.3% (10-30/164)

## Part 2: IRT Item Pool Confirmation

**File**: `artifacts/exp006_irt_calibration/run_irt_stan.py`

The IRT pipeline already excludes paraphrased data via `skip_para=True` (line 39 in `load_eval_results()`). Paraphrased HumanEval items do NOT enter the IRT response matrix.

However, there was no item-level variance filtering — items with all-correct or all-wrong responses across models (zero variance) would still enter the matrix, causing IRT estimation issues.

## Part 3: Item Variance Filter Added

**Modified file**: `artifacts/exp006_irt_calibration/run_irt_stan.py`

Added `filter_low_variance_items()` function (lines 113-151) that:
1. Computes per-item response variance across valid models
2. Removes items with variance < threshold (default 0.01)
3. Returns filtered matrix + metadata (excluded indices, keep mask)
4. Properly aligns exposure scores after item removal

Integration point: called in `run_real_data()` loop (line 442-443) before building exposure matrix.

CLI argument added: `--min-item-variance` (default: 0.01)

### Threshold Justification
- variance=0.01 → items with ≤1% response heterogeneity (practically all-same)
- For binary responses with N models: var = p*(1-p), so var<0.01 means p<0.01 or p>0.99
- This is conservative: only removes items where essentially all models agree
