# ML Classifier Baseline vs lz* — Analysis Report

## Experiment Setup

- **Task**: Binary classification — clean vs contaminated response vectors
- **Benchmarks**: MMLU (14042 items), HellaSwag (10042), GSM8K (1319), ARC-C (295), HumanEval (164)
- **Contamination mechanism**: Randomly select π% of items and set to correct (1), matching the simulation protocol
- **Samples**: 500 per class, 80/20 train/test split
- **Classifiers**: Logistic Regression (L-BFGS), Random Forest (100 trees, sqrt features)
- **Feature sets**: (a) response vectors only, (b) response vectors + summary stats (accuracy, lz*, outfit, infit)
- **Baseline**: lz* score (negated, unsupervised — no training data needed)

## Results at 25% Contamination

### Main comparison: lz* vs ML (binary response vector only)

This is the fair comparison — ML classifiers receive only the binary response vector (same information as lz* minus the IRT model structure).

| Benchmark | lz* | LR (resp only) | RF (resp only) |
|-----------|-----|----------------|----------------|
| MMLU | 0.973 | 1.000 | 0.979 |
| HellaSwag | 0.976 | 0.997 | 0.935 |
| GSM8K | 0.936 | 0.965 | 0.930 |
| ARC-C | 0.625 | 0.676 | 0.728 |
| HumanEval | 0.791 | 0.858 | 0.853 |
| **Average** | **0.860** | **0.899** | **0.885** |

### Information upper bound: ML (response vector + summary statistics including lz*)

These results include lz* itself as a feature, so they represent an upper bound on what ML can achieve with all available information — not a fair comparison with lz* alone.

| Benchmark | LR (+summ incl. lz*) | RF (+summ incl. lz*) |
|-----------|----------------------|----------------------|
| MMLU | 1.000 | 1.000 |
| HellaSwag | 0.998 | 0.975 |
| GSM8K | 0.985 | 0.981 |
| ARC-C | 0.689 | 0.743 |
| HumanEval | 0.872 | 0.869 |
| **Average** | **0.909** | **0.913** |

## Key Finding: lz* Outperforms ML Classifiers at Low Contamination

The most important result is at **low contamination levels (5–10%)**, which are the most practically relevant scenarios. All ML results below use **response vector only** (fair comparison):

| Contamination | lz* (avg) | Best ML resp-only (avg) | lz* advantage |
|:---:|:---:|:---:|:---:|
| **5%** | **0.675** | 0.575 (LR) | **+0.100** |
| **10%** | **0.763** | 0.712 (LR) | **+0.051** |
| 15% | 0.823 | 0.819 (LR) | +0.004 |
| 25% | 0.860 | 0.899 (LR) | −0.039 |
| 50% | 0.826 | 0.987 (RF) | −0.161 |

At 5% contamination, lz* outperforms the best supervised ML classifier by **+0.10 AUROC** across all five benchmarks. This advantage narrows as contamination increases, with ML classifiers overtaking only at 25%+ contamination.

## Per-Benchmark Analysis

**Large benchmarks (MMLU, HellaSwag, GSM8K ≥ 1000 items):**
- lz* dominates at 5–15% contamination (avg AUROC advantage: +0.06 to +0.12)
- ML classifiers catch up at 25% but require labeled training data
- At 25% contamination, lz* still achieves 0.93–0.98 AUROC, which is highly practical

**Small benchmarks (ARC-C: 295, HumanEval: 164 items):**
- Both lz* and ML classifiers struggle at low contamination (AUROC 0.5–0.6)
- At 25%, lz* (0.63–0.79) < ML classifiers (0.73–0.87)
- Low item count limits both methods, but especially lz* since lz* power is directly proportional to item count

## Feature Importance

RF feature importances are **diffuse across items**: even the top-ranked item accounts for < 1% of total importance on large benchmarks. This confirms that no small item subset drives detection — consistent with lz*'s holistic likelihood approach, which aggregates weak signals across all items.

## Conclusion

1. **lz* outperforms supervised ML classifiers at the most practically relevant low contamination levels (5–10%)**, precisely where detection is hardest and matters most.

2. ML classifiers only gain an advantage at moderate-to-high contamination (≥ 25%), where the contamination signal is already strong enough that even unsupervised methods achieve high AUROC.

3. **lz* requires zero labeled training data** — it needs no examples of contaminated responses and makes no assumption about the contamination mechanism. ML classifiers require labeled data from the *exact same contamination mechanism* they will encounter, which is unavailable in practice.

4. Even when ML classifiers are given oracle knowledge (exact contamination mechanism + labeled examples at the correct contamination level), their advantage over lz* at 25% contamination is modest (+0.04 AUROC on average for response-vector-only; +0.05 with summary features that include lz* itself).

5. **Note on +summary results**: The ML(+summary) variant includes lz* as an input feature, making it an information upper bound rather than a fair baseline. These results are reported for completeness but should not be cited as evidence that ML "outperforms" lz* — they demonstrate that adding IRT-derived features to ML further improves detection, which is expected.

**Bottom line**: For real-world contamination detection where the contamination level and mechanism are unknown, lz* is the more practical and robust choice. It matches or outperforms supervised approaches at low contamination without requiring any training data.

**Scope limitation**: These results are from simulation with known contamination mechanism. They should not be generalized to claim "all binary-only ML methods are inferior to IRT" — real-world contamination patterns may differ from the random-item-flip model used here.
