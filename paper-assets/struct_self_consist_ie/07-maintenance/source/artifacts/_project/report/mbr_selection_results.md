# MBR Selection for NER: Results

## Method

Minimum Bayes Risk (MBR) selection picks the sample whose entity set has highest average overlap with all other samples. For each instance with N=8 samples:

```
MBR_score(si) = mean_{j!=i} Jaccard(E(si), E(sj))
```

where `Jaccard(A, B) = |A ∩ B| / |A ∪ B|` over entity sets `E = {(text, type)}`. Empty-set pairs score 1.0.

F1 evaluation uses span-based matching `(start, end, type)` against gold.

## Results

| Dataset | Greedy | LP Sel | MBR Sel | Oracle | MBR-Greedy | MBR-LP |
|---------|--------|--------|---------|--------|------------|--------|
| SciERC  | 0.6439 | 0.6501 | 0.6444  | 0.7758 | +0.0005    | -0.0057 |
| CoNLL   | 0.9087 | 0.8985 | 0.9043  | 0.9520 | -0.0043    | +0.0059 |
| FewNERD | 0.7478 | 0.7610 | 0.7208  | 0.8686 | -0.0269    | -0.0402 |

Instance counts: SciERC=529 (gold-filtered), CoNLL=3453, FewNERD=4351 (gold-filtered). All use first 8 samples per instance.

## MBR vs LP Comparison

- **SciERC**: MBR marginally above Greedy (+0.0005) but below LP (-0.0057). Negligible difference.
- **CoNLL**: MBR below Greedy (-0.0043) but above LP (+0.0059). On this high-accuracy dataset, LP sometimes picks a confident but incorrect outlier.
- **FewNERD**: MBR significantly underperforms both Greedy (-0.0269) and LP (-0.0402). Worst case for MBR.

## Degeneracy-Grouped MBR Performance

Instances grouped by sample diversity (unique (text,type) entity sets / N):
- **Low diversity** (1-2 unique sets out of 8): near-degenerate, all samples agree
- **Medium** (3-5 unique): moderate variation
- **High diversity** (6-8 unique): high disagreement across samples

### SciERC

| Group | Count | Greedy | LP | MBR | Oracle | MBR-Greedy |
|-------|-------|--------|----|-----|--------|------------|
| Low diversity | 186 | 0.7110 | 0.7101 | 0.7011 | 0.8031 | -0.0099 |
| Medium | 280 | 0.6235 | 0.6359 | 0.6268 | 0.7684 | +0.0033 |
| High diversity | 63 | 0.5366 | 0.5358 | 0.5549 | 0.7281 | +0.0183 |

MBR helps most on high-diversity instances (+0.0183), where consensus selection has informative signal.

### CoNLL

| Group | Count | Greedy | LP | MBR | Oracle | MBR-Greedy |
|-------|-------|--------|----|-----|--------|------------|
| Low diversity | 2764 | 0.9502 | 0.9448 | 0.9470 | 0.9640 | -0.0032 |
| Medium | 626 | 0.7495 | 0.7252 | 0.7430 | 0.9127 | -0.0065 |
| High diversity | 63 | 0.6676 | 0.5860 | 0.6345 | 0.8184 | -0.0331 |

MBR consistently below Greedy across all groups. On high-diversity instances, MBR beats LP (+0.05) but still loses to Greedy.

### FewNERD

| Group | Count | Greedy | LP | MBR | Oracle | MBR-Greedy |
|-------|-------|--------|----|-----|--------|------------|
| Low diversity | 1436 | 0.7949 | 0.8211 | 0.7871 | 0.8699 | -0.0077 |
| Medium | 2197 | 0.7464 | 0.7587 | 0.7071 | 0.8831 | -0.0393 |
| High diversity | 718 | 0.6576 | 0.6478 | 0.6302 | 0.8219 | -0.0274 |

MBR hurts across all groups, worst on medium-diversity (-0.0393).

## Conclusion

Output-level MBR selection with entity-set Jaccard as the utility function is not effective for NER sample selection. MBR fails to improve over Greedy on 2/3 datasets and underperforms LP on 2/3 datasets.

The key failure mode: MBR with (text,type) Jaccard favors samples with common entity subsets, but this consensus signal does not reliably indicate higher quality. In NER, a sample that includes only "easy" entities (high consensus) may miss harder entities that fewer samples detect correctly. LP selection, which picks the most confident complete output, remains the stronger single-sample selection baseline.

The one scenario where MBR shows promise is SciERC high-diversity instances (+0.0183), where samples diverge significantly and consensus can filter noise. But this benefit is too small and narrow to justify MBR as a general strategy.
