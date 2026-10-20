# Accumulation Experiment Results Summary

## Full-Replacement Baselines (Table 1, 5-fold CV, 20k samples)

| Model | Strategy | 4-class Acc | d1d3 Bal Acc |
|-------|----------|-------------|--------------|
| GPT-2 XL | nucleus | 84.28% | 79.55% |
| Pythia-1.4B | nucleus | 78.70% | 71.83% |
| OLMo-1B | temp0.9 | 82.27% | 76.60% |

Source: table2_rerun_5foldcv.json (5-fold CV, 200 trees, 5000 samples/depth)

## Accumulation Results

| Model | Strategy | Mix | 4-class Acc | d1d3 Bal | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD(T=0.70) | Δ vs Full |
|-------|----------|-----|-------------|----------|----------|----------|----------|-------------|-----------|
| GPT-2 XL | nucleus | 25% | 70.08% | 60.30% | 0.9995 | 0.8168 | 0.7258 | 3 | -14.20pp |
| GPT-2 XL | nucleus | 50% | 69.05% | 58.95% | 0.9995 | 0.8314 | **0.6903** | **2** | -15.23pp |
| Pythia-1.4B | nucleus | 25% | 70.77% | 61.15% | 0.9998 | 0.8090 | 0.7486 | 3 | -7.93pp |
| Pythia-1.4B | nucleus | 50% | 68.65% | 58.34% | 0.9998 | 0.7915 | 0.7133 | 3 | -10.05pp |
| OLMo-1B | temp0.9 | 25% | 73.47% | 64.72% | 1.0000 | 0.8481 | 0.7585 | 3 | -8.80pp |
| OLMo-1B | temp0.9 | 50% | 70.23% | 60.39% | 0.9999 | 0.8162 | 0.7223 | 3 | -12.04pp |

## Per-Class Recall

| Model | Mix | d0 | d1 | d2 | d3 |
|-------|-----|------|------|------|------|
| GPT-2 XL | 25% | 99.4% | 73.3% | 42.8% | 64.7% |
| GPT-2 XL | 50% | 99.4% | 73.0% | 42.0% | 61.8% |
| Pythia-1.4B | 25% | 99.6% | 70.6% | 43.9% | 69.0% |
| Pythia-1.4B | 50% | 99.6% | 69.2% | 41.7% | 64.1% |
| OLMo-1B | 25% | 99.7% | 75.7% | 48.2% | 70.3% |
| OLMo-1B | 50% | 99.7% | 72.5% | 41.2% | 67.4% |

## Mix25 → Mix50 Degradation

| Model | mix25 Acc | mix50 Acc | Δ | d2v3 AUC drop |
|-------|-----------|-----------|------|---------------|
| GPT-2 XL | 70.08% | 69.05% | -1.03pp | 0.726→0.690 (-0.036) |
| Pythia-1.4B | 70.77% | 68.65% | -2.12pp | 0.749→0.713 (-0.035) |
| OLMo-1B | 73.47% | 70.23% | -3.24pp | 0.759→0.722 (-0.036) |

## Key Findings

1. **EDD robustness**: 5/6 experiments maintain EDD=3 at T=0.70; only GPT-2 XL mix50 drops to EDD=2 (d2v3 AUC=0.690, marginally below threshold)
2. **4-class accuracy degradation**: -7.93pp to -15.23pp vs full-replacement, with larger models (by absolute acc) showing larger absolute drops
3. **Consistent mix25→mix50 pattern**: All models show monotonic degradation; d2v3 AUC drop is remarkably uniform (~0.036 across all models)
4. **d0v1 AUC immune to mixing**: Near-perfect (≥0.9995) in all conditions — d0↔d1 boundary is robustly detectable even with 50% human contamination
5. **d2 remains hardest class**: Recall 41-48% across all conditions, consistent with full-replacement pattern
6. **OLMo temp09 dominates**: Highest absolute accuracy in both mix conditions (73.47%, 70.23%) but also largest mix25→mix50 drop (-3.24pp)

## Data Locations

- GPT-2 XL: results/accumulation_v2/{mix25,mix50}/
- Pythia-1.4B: results/accumulation_v3/pythia_nucleus/{mix25,mix50}/
- OLMo-1B: results/accumulation_v3/olmo_temp09/{mix25,mix50}/
- Pairwise AUC: results/accumulation_pairwise_auc.json

## Note on Baselines

The full-replacement baselines are from table2_rerun_5foldcv.json which uses the same methodology (5-fold CV, 200 trees, 5000 samples/depth) as the accumulation experiments, ensuring fair comparison. Earlier accumulation experiments stored different "full_replacement_baseline" values in their summary.json files — those were computed with different pipelines and should not be used for cross-experiment comparison.
