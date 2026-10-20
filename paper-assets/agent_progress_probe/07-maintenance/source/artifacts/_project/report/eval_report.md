# Gold Set Evaluation Report

**Date**: 2026-05-15  
**Annotation file**: `annotation_unknown_2026-05-15.csv` (annotator 1 of 3)  
**Total annotations**: 199 | **Matched for evaluation**: 132 (swe-agent only)

---

## 1. Coverage

| Subset | Count | Notes |
|--------|-------|-------|
| Total gold annotations | 199 | 136 swe-agent + 63 openhands |
| Matched in `windows_labeled.jsonl` | 132 | All swe-agent |
| Unmatched | 67 | 63 openhands + 4 swe-agent |

OpenHands windows are absent from `windows_labeled.jsonl`, so **all evaluation below is swe-agent only**.

Matched gold distribution: **63 stagnation (47.7%)**, **69 progress (52.3%)** — well-balanced, in contrast to the full 199-sample set where openhands inflates progress to 66.3%.

---

## 2. Model Performance vs Gold Labels (N=132)

| Model | Macro-F1 | F1(stag) | F1(prog) | Prec(stag) | Rec(stag) | Accuracy |
|-------|----------|----------|----------|------------|-----------|----------|
| **Structural RF** | **0.7928** | **0.7692** | **0.8163** | 0.8333 | 0.7143 | **0.7955** |
| Structural GB | 0.7847 | 0.7586 | 0.8108 | **0.8302** | 0.6984 | 0.7879 |
| TWV Probe | 0.7684 | 0.7368 | 0.8000 | 0.8235 | 0.6667 | 0.7727 |
| GRU Probe | 0.7348 | 0.7328 | 0.7368 | 0.7059 | **0.7619** | 0.7348 |
| MV Labels | 0.7304 | 0.6957 | 0.7651 | 0.7692 | 0.6349 | 0.7348 |
| TWV Labels | 0.7184 | 0.6667 | 0.7702 | 0.8222 | 0.5606 | 0.7279 |

**Best**: Structural RF (macro-F1 0.7928). Structural baselines outperform both probe models when evaluated against human labels.

**GRU Probe sub-split analysis** (N is small — interpret cautiously):
- Gold windows that fell in train split (N=39): macro-F1 = 0.8436
- Gold windows that fell in test split (N=17): macro-F1 = 0.8712

---

## 3. MV–Gold Agreement (Critical Result)

### Overall
- **Agreement rate: 73.5%** (97/132)
- **35 disagreements**: 23 where MV=progress but gold=stagnation, 12 where MV=stagnation but gold=progress
- **MV bias**: Over-predicts progress (65.7% of disagreements are false-progress)

### Confusion Matrix (MV vs Gold)

|  | Pred Stagnation | Pred Progress |
|--|-----------------|---------------|
| **Gold Stagnation** | 40 | 23 |
| **Gold Progress** | 12 | 57 |

### By Confidence Level

| Confidence | N | Agreement | Macro-F1 | F1(stag) | F1(prog) | Disagree % |
|-----------|---|-----------|----------|----------|----------|------------|
| 1 | 76 | 50/76 = **65.8%** | 0.6420 | 0.5667 | 0.7174 | 34.2% |
| 2 | 48 | 39/48 = **81.3%** | 0.8118 | 0.8000 | 0.8235 | 18.8% |
| 3 | 8 | 8/8 = **100.0%** | 1.0000 | 1.0000 | 1.0000 | 0.0% |
| **≥2** | **56** | **47/56 = 83.9%** | **0.8392** | 0.8364 | 0.8421 | 16.1% |

**Key finding**: Confidence level is a strong predictor of silver label quality. At conf≥2, MV–gold agreement rises to 83.9%; at conf=3, it is 100%. But conf=1 windows (57.6% of matched data) have only 65.8% agreement — substantial noise.

---

## 4. TWV–Gold Agreement

| Confidence | N | Agreement |
|-----------|---|-----------|
| Overall | 132 | 99/132 = **75.0%** |
| 1 | 76 | 53/76 = **69.7%** |
| 2 | 48 | 38/48 = **79.2%** |
| 3 | 8 | 8/8 = **100.0%** |

TWV slightly outperforms MV overall (75.0% vs 73.5%) and at conf=1 (69.7% vs 65.8%), but is slightly worse at conf=2 (79.2% vs 81.3%).

---

## 5. Interpretation

### Silver label noise is substantial but structured
- ~26.5% of MV silver labels disagree with human judgment (on swe-agent data)
- The noise is concentrated in low-confidence windows (conf=1): 34.2% error rate
- High-confidence windows (conf≥2) have ≤18.8% error, and conf=3 is perfect (though N=8)

### MV has a progress bias
- 23/35 disagreements are "MV says progress, human says stagnation"
- This means some genuinely stagnating agents get mislabeled as making progress by the labeling functions
- Downstream: models trained on MV labels may under-detect stagnation

### Structural baselines are surprisingly robust
- RF achieves the highest macro-F1 (0.7928) against gold labels
- This suggests hand-crafted features capture genuine behavioral patterns rather than just fitting silver label noise
- The gap between RF (0.793) and MV ceiling (0.735) means RF meaningfully improves over just using the silver labels directly

### GRU Probe is calibrated but not best
- Probe macro-F1 (0.7348) matches MV accuracy exactly — it learned the silver label distribution faithfully
- On its own test split (N=17), probe achieves 0.8712 macro-F1, suggesting it generalizes better than the silver labels themselves

### Statistical caveats
- N=132 (swe-agent only) — no openhands coverage
- conf=3 has only 8 samples — 100% agreement is not statistically meaningful
- This is 1 of 3 annotators — inter-annotator agreement not yet computable
- The matched subset has different class balance (47.7%/52.3%) than the full gold set (33.7%/66.3%)

---

## 6. Implications for Paper

1. **The MV silver labels are a noisy proxy**: 73.5% agreement with gold is the baseline ceiling for any model trained on MV labels alone.

2. **Confidence stratification works**: conf≥2 gives 83.9% agreement, validating the paper's strategy of using confidence-stratified evaluation.

3. **Structural RF outperforms on gold**: The result that structural baselines (RF 0.793) beat the GRU probe (0.735) on gold labels is different from the silver-label evaluation ranking. This warrants discussion — the probe may be overfitting to silver label noise.

4. **Progress bias in MV**: 2:1 ratio of false-progress to false-stagnation in disagreements. The labeling functions may be too lenient in classifying windows as progress.

5. **Openhands gap**: 63 openhands windows are unevaluable. The annotator labeled 62/63 as progress — if this reflects ground truth, openhands agents stagnate far less than swe-agent agents. But we cannot validate this against model predictions until openhands data is added to `windows_labeled.jsonl`.
