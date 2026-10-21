# Degeneracy-Gated Selection Results

## Method

For each instance with N=8 samples:
1. Compute span-based entity F1 (start, end, type) for each sample vs gold
2. If all 8 sample F1 scores are identical (degenerate) -> use greedy decoding output
3. Otherwise -> use LP-best selection (sample with highest mean_logprob)

## Summary Table

| Dataset | N | Degen% | Greedy | LP-all | Gated | Oracle | G-Greedy | G-LP |
|---------|---:|-------:|-------:|-------:|------:|-------:|---------:|-----:|
| SciERC | 551 | 18.7% | 0.6436 | 0.6495 | 0.6507 | 0.7775 | +0.0071 | +0.0012 |
| CoNLL | 3453 | 62.0% | 0.9087 | 0.8985 | 0.8985 | 0.9520 | -0.0102 | +0.0000 |
| FewNERD | 5000 | 23.1% | 0.7713 | 0.7800 | 0.7805 | 0.8831 | +0.0092 | +0.0004 |

## Degenerate vs Non-degenerate Breakdown

### SciERC
- Degenerate (103, 18.7%): Greedy=Gated=0.6207, Oracle=0.6142
- Non-degenerate (448, 81.3%): Greedy=0.6489, LP=0.6576, Oracle=0.8150, LP-Greedy=+0.0087

### CoNLL
- Degenerate (2141, 62.0%): Greedy=Gated=0.9431, Oracle=0.9431
- Non-degenerate (1312, 38.0%): Greedy=0.8524, LP=0.8255, Oracle=0.9666, LP-Greedy=-0.0269

### FewNERD
- Degenerate (1156, 23.1%): Greedy=Gated=0.7790, Oracle=0.7772
- Non-degenerate (3844, 76.9%): Greedy=0.7690, LP=0.7809, Oracle=0.9149, LP-Greedy=+0.0119

## Analysis

### Gated vs LP-all
Gated selection provides marginal improvement over LP-all:
- SciERC: +0.12pp (small positive)
- CoNLL: +0.00pp (no change, because on degenerate instances greedy F1 matches sample F1)
- FewNERD: +0.04pp (negligible)

The improvement is minimal because on degenerate instances, LP-all already picks a sample with the same F1 as any other sample (by definition of degeneracy). The only gain comes when greedy decoding differs from all samples on degenerate instances.

### Gated vs Greedy
- SciERC: +0.71pp (positive, LP helps on non-degen)
- CoNLL: -1.02pp (negative! LP hurts on non-degenerate instances: LP=0.8255 vs Greedy=0.8524)
- FewNERD: +0.92pp (positive, LP helps on non-degen)

### Key Insight: CoNLL LP Failure on Non-degenerate Instances
On CoNLL non-degenerate instances, LP-best (0.8255) is worse than Greedy (0.8524) by -2.69pp. This means higher mean_logprob does not correlate with better entity F1 on CoNLL, so any method using LP for selection (including Gated) will underperform Greedy on those instances.

### Conclusion
Degeneracy-gated selection provides only marginal improvement over LP-all (+0.00 to +0.12pp). The core issue is not that LP fails on degenerate instances (where it is harmless since all samples have equal F1), but that LP itself is a weak signal for selection quality. The gating mechanism addresses a theoretical concern (LP noise on degenerate instances) that has minimal practical impact.

## Data Sources
- SciERC: `output/exp_012_rerun_1024/samples.jsonl` (N=8, 551 instances)
- CoNLL: `output/exp_002_conll_n16_r1024/samples.jsonl` (first 8 of 16 samples, 3453 instances)
- FewNERD: `output/exp_027_fewnerd_n16/samples.jsonl` (first 8 of 16 samples, 5000 instances)

## Script
`code/analysis_degen_gated_selection.py`
