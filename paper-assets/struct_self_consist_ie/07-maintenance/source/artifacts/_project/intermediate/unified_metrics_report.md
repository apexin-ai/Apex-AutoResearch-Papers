## Unified Metrics Fix Complete

### Created
- `code/unified_metrics.py` — canonical F1/degeneracy/data loading
- `code/regression_test_unified_metrics.py`
- `output/unified_metrics_regression/regression_report.json`

### Modified (5 scripts)
1. diagnostic_calibration.py
2. entity_consensus.py
3. ccs_selection.py
4. analysis_dgs_gold_filter.py
5. adaptive_temperature_analysis.py

### Canonical Numbers (SciERC, 529 inst, gold_filter=True)
| Metric | Value | 95% CI |
|--------|-------|--------|
| Greedy F1 | 0.6439 | [0.6180, 0.6692] |
| LP-all F1 | 0.6501 | [0.6246, 0.6750] |
| DGS F1 | 0.6513 | [0.6259, 0.6760] |
| Oracle F1 | 0.7758 | [0.7541, 0.7969] |
| Degeneracy | 17.77% | 94/529 |
| DGS-Greedy | +0.74pp | [-0.60, +2.11] |