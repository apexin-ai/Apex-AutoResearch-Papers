# Error Analysis Initial Results (SFT Baselines)

Script: `/root/autodl-tmp/freige/scripts/error_analysis.py`
Output: `/root/autodl-tmp/analysis/error_analysis/`

## Key Findings (3 SFT baselines: 1.7B / 8B-Qwen / 8B-LLaMA)

### FP Classification
- Hallucinated relation: ~89% (pred (h,t) pair not in gold)
- Relation confusion: ~11% ((h,t) exists but wrong relation)

### FN Classification
- Cross-sentence miss and truncation loss dominate
- Rare relation miss relatively low

### Evidence Quality (TP triples only)
- Exact match: 65-70%
- Over-citation: ~15%
- Under-citation: ~15%
- Evidence shift: <2%

### Scale Effects
- Duplicates: 4538 (1.7B) → 4075 (8B-Q) → 2624 (8B-L)
- Truncation loss also decreases with scale

## Next Steps
- Run on RSFT predictions for SFT→RSFT comparison (P0)
- Run on d102 k=1 predictions
- Generate LaTeX tables for paper
