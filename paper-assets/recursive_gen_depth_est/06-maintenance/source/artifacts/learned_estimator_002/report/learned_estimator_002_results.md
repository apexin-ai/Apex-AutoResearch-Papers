# learned_estimator_002 Results Summary

## Experiment: NaN-fixed Learned Estimators Full Sweep
- Server: westd-48862, cuda:0
- Data: 9 feature files (3 models x 3 strategies), 120k train / 60k test per split
- Baseline: RF = 66.4% accuracy

## Results Table (Accuracy %)

| Method          | Pythia | OLMo    | GPT2-XL | Mean   |
|-----------------|--------|---------|---------|--------|
| XGBoost         | 63.72  | **69.76** | **68.05** | 67.18  |
| Ordinal MLP     | 62.52  | **69.69** | **67.90** | 66.70  |
| Prototypical    | 61.55  | **70.01** | **68.35** | 66.64  |

Bold = exceeds RF baseline of 66.4%

## Key Findings
1. NaN fix works: Prototypical network runs without crashes (was NaN-crashing in _001)
2. All 3 methods beat baseline on olmo and gpt2xl holdouts
3. Pythia holdout is hardest for all methods (61-64%)
4. Best single result: Prototypical on olmo = 70.01% (AUC=0.9004)
5. XGBoost is strongest overall (avg 67.18%)
6. Mean pairwise AUC consistently 0.84-0.90 across methods

## AUC Results

| Method          | Pythia | OLMo   | GPT2-XL |
|-----------------|--------|--------|---------|
| XGBoost         | 0.8501 | 0.8969 | 0.8930  |
| Ordinal MLP     | 0.8391 | 0.8947 | 0.8668  |
| Prototypical    | 0.8415 | 0.9004 | 0.8926  |

## Runtime
- XGBoost: ~7s per holdout
- Ordinal MLP: ~100s per holdout (150 epochs, early stopping at ~15)
- Prototypical: ~107s per holdout (150 epochs, early stopping)
- Total: ~694s (11.6 min)
