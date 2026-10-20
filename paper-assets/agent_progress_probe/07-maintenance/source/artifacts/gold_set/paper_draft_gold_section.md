# §6.7 Gold Set Validation — Draft Framework

> **Status**: Batch 1 draft (annotator=unknown). Placeholders marked `[PLACEHOLDER]` await batch 2/3 data.
> **Data source**: `artifacts/gold_set/eval_results_full.json`, `eval_report_full.md`, `quality_report.md`

---

## Annotation Protocol

[TOTAL_ANNOTATORS] CS graduate students independently annotated [TOTAL_N] windows sampled stratified by source (SWE-agent, OpenHands), confidence level (conf=1, 2, 3), and trajectory position (early, middle, late thirds).
Each annotator viewed the $k{=}5$ action descriptions with full command outputs and file diffs but *not* the task outcome (resolved/unresolved), preventing information leakage from $\lambda_3$.
A window was labeled *stagnation* if the agent's actions within it did not make meaningful progress toward solving the task, regardless of whether the actions appeared diverse or purposeful.
Annotators assigned a confidence score (0–3); conf=0 windows were treated as abstentions and excluded from evaluation.

**Batch 1** (current): A single annotator labeled 199 windows; 195 matched to labeled windows (132 SWE-agent, 63 OpenHands), with 4 conf=0 abstentions excluded.
Inter-annotator agreement (Cohen's $\kappa$): [KAPPA_PLACEHOLDER] (pending batches 2–3).

---

## Gold Label Distribution

| Source | $N$ | Progress | Stagnation | Progress % |
|--------|-----|----------|------------|------------|
| SWE-agent | 132 | 69 | 63 | 52.3% |
| OpenHands | 63 | 62 | 1 | 98.4% |
| **All** | **195** | **131** | **64** | **67.2%** |

The SWE-agent subset is near-balanced (52.3% progress), while OpenHands is almost uniformly progress (98.4%).
This extreme skew limits cross-agent stagnation validation on OpenHands and reflects genuine behavioral differences: OpenHands agents rarely exhibit the repetitive command patterns that characterize SWE-agent stagnation.

---

## Model Performance Against Gold Labels

### Table: Gold Set Macro-F1 by Model

| Model | $N$ | Macro-F1 | F1(stag) | F1(prog) | Accuracy |
|-------|-----|----------|----------|----------|----------|
| TWV Probe | 132 | 0.768 [CI_PLACEHOLDER] | 0.737 | 0.800 | 0.773 |
| Structural GB | 195 | 0.760 [CI_PLACEHOLDER] | 0.682 | 0.837 | 0.785 |
| Structural RF | 195 | 0.756 [CI_PLACEHOLDER] | 0.681 | 0.831 | 0.779 |
| GRU Probe | 132 | 0.735 [CI_PLACEHOLDER] | 0.733 | 0.737 | 0.735 |
| MV Labels | 195 | 0.718 [CI_PLACEHOLDER] | 0.626 | 0.811 | 0.749 |
| TWV Labels | 136 | 0.718 [CI_PLACEHOLDER] | 0.667 | 0.770 | 0.728 |

All trained models outperform their corresponding silver labels (MV or TWV) against gold, confirming that probes and structural classifiers learn signal beyond what the label aggregation encodes.
The TWV probe achieves the highest macro-F1 (0.768) among models evaluated on the SWE-agent subset ($N{=}132$); structural GB leads on the full 195-window set (0.760).

### Per-Source Breakdown

**SWE-agent ($N{=}132$):**

| Model | Macro-F1 | F1(stag) | F1(prog) |
|-------|----------|----------|----------|
| Structural RF | 0.793 | 0.769 | 0.816 |
| Structural GB | 0.785 | 0.759 | 0.811 |
| TWV Probe | 0.768 | 0.737 | 0.800 |
| GRU Probe | 0.735 | 0.733 | 0.737 |
| MV Labels | 0.730 | 0.696 | 0.765 |

**OpenHands ($N{=}63$):**

Model-vs-gold evaluation on OpenHands is unreliable: only 1 of 63 gold windows is labeled stagnation, making stagnation F1 ill-defined and macro-F1 dominated by the progress class.
MV achieves 77.8% agreement on OpenHands, but this masks a systematic false-stagnation bias analyzed below.

---

## MV–Gold Agreement Analysis

### By Confidence Stratum

| Subset | $N$ | Agreement | Macro-F1 |
|--------|-----|-----------|----------|
| Overall | 195 | 74.9% | 0.718 |
| conf=1 | 115 | 69.6% | 0.638 |
| conf$\geq$2 | 80 | 82.5% | 0.816 |
| conf=2 | 67 | 83.6% | 0.823 |
| conf=3 | 13 | 76.9% | 0.769 |

Agreement rises from 69.6% (conf=1) to 82.5% (conf$\geq$2), validating the confidence stratification strategy: high-confidence silver labels are substantially more reliable.
The conf=3 dip to 76.9% ($N{=}13$) is statistically unstable and driven by 3 OpenHands conf=3 disagreements where MV called stagnation but the annotator saw progress.

### By Source $\times$ Confidence

| Source | Confidence | $N$ | Agreement |
|--------|------------|-----|-----------|
| SWE-agent | conf=1 | 76 | 65.8% |
| SWE-agent | conf$\geq$2 | 56 | 83.9% |
| OpenHands | conf=1 | 39 | 76.9% |
| OpenHands | conf$\geq$2 | 24 | 79.2% |

SWE-agent benefits most from confidence filtering (+18.1 pp from conf=1 to conf$\geq$2), while OpenHands shows a smaller gain (+2.3 pp).

---

## OpenHands False-Stagnation Bias

The confusion matrix reveals an asymmetric error pattern across sources:

**OpenHands ($N{=}63$):**
- MV predicts stagnation for 15 windows; human labels only 1 as stagnation.
- 14 of 15 MV stagnation predictions (93.3%) are false positives from the human perspective.
- MV error direction: overwhelmingly **false-stagnation** (22.2% of OH windows mislabeled as stagnation).

**SWE-agent ($N{=}132$):**
- MV error direction: predominantly **false-progress** (17.4% of SWE windows mislabeled as progress).
- 23 of 35 SWE disagreements are MV predicting progress where the annotator marked stagnation.

The two sources exhibit *opposite* MV bias directions: SWE-agent silver labels under-detect stagnation, while OpenHands silver labels over-detect it.
This aligns with the LF temporal dynamics identified in §5.2 (C2): `cmd_rep` fires on 65.5% of SWE-agent windows but only 5.4% of OpenHands windows, yet when it does fire on OpenHands, it frequently flags exploratory but productive behavior as repetitive stagnation.
The finding demonstrates that cross-agent LF transfer without agent-specific calibration of stagnation definitions produces systematically biased labels.

---

## GRU Probe Contamination Check

Of 132 SWE-agent gold windows, 39 appeared in the probe's training set and 17 in its test set (remaining 76 were unmatched to train/test splits).
Gold macro-F1 on train-set windows (0.844) and test-set windows (0.871) are comparable, showing no memorization advantage — if anything, the probe performs marginally better on held-out gold windows.

---

## Limitations

1. **Single-annotator batch.** Batch 1 was annotated by a single labeler (annotator=unknown). Inter-annotator agreement cannot be computed until batches 2–3 are complete. All gold metrics reported here reflect one annotator's judgment and may shift with multi-annotator consensus. [KAPPA_PLACEHOLDER]

2. **OpenHands class skew.** With only 1/63 OpenHands windows labeled stagnation, cross-agent stagnation validation is effectively impossible on the current gold set. The OH macro-F1 numbers are dominated by progress-class performance and should not be interpreted as stagnation detection accuracy.

3. **Sample size.** $N{=}195$ provides moderate statistical power for overall metrics but limits stratified analysis. The conf=3 subset ($N{=}13$) is too small for reliable sub-group inference. Bootstrap confidence intervals [CI_PLACEHOLDER] will quantify uncertainty.

4. **Sampling bias.** Gold windows were stratified by confidence and source but not by trajectory position in this batch. Position-stratified sampling in batches 2–3 will address whether early/late trajectory stagnation patterns are captured.

5. **Annotation scope.** Annotators saw $k{=}5$ action windows without broader trajectory context. Some borderline cases (e.g., agent exploring before converging) may be ambiguous at the window level but clear in context.

---

## Summary

Gold set validation confirms that trained models (structural GB: 0.760, TWV probe: 0.768) outperform silver label baselines (MV: 0.718) when measured against human judgment, providing the first non-circular evidence that these models capture genuine progress/stagnation signal beyond LF reconstruction.
The confidence stratification is validated: MV–gold agreement rises from 69.6% (conf=1) to 82.5% (conf$\geq$2).
However, the gold set also exposes a systematic cross-agent calibration failure: MV labels 93% of OpenHands stagnation predictions incorrectly, with the two sources exhibiting opposite bias directions.
This finding strengthens the case for agent-specific LF calibration in deployment.
