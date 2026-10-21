# ε Sensitivity Analysis — LP Compression Threshold

Dataset: FewNERD finetuned 3-epoch (mf4v2_s42_v3), N=8, seed=42
Server: autodl-5090, output/fewnerd_mf4v2_seed42_v3/epsilon_sensitivity.json

## Core Table: ε vs LP Compression

| ε | compressed% | ρ(LP,F1) non-comp | ρ(LP,F1) all | MV F1 | LP-best F1 |
|---|---|---|---|---|---|
| 0.01 | 9.3% | 0.6824 | 0.6325 | 0.7587 | 0.7927 |
| 0.03 | 19.9% | 0.6945 | 0.6325 | 0.7587 | 0.7927 |
| **0.05** | **34.5%** | **0.7095** | **0.6325** | **0.7587** | **0.7927** |
| 0.10 | 60.2% | 0.7328 | 0.6325 | 0.7587 | 0.7927 |
| 0.15 | 75.9% | 0.7228 | 0.6325 | 0.7587 | 0.7927 |
| 0.20 | 92.5% | 0.7196 | 0.6325 | 0.7587 | 0.7927 |

## LP-best Selection Advantage by LP Range Bucket

| LP range bucket | n | MV F1 | LP F1 | LP-MV gap |
|---|---|---|---|---|
| [0.00, 0.01) | 3018 | 0.8180 | 0.8257 | +0.8pp |
| [0.01, 0.03) | 3457 | 0.8119 | 0.8271 | +1.5pp |
| [0.03, 0.05) | 4744 | 0.7862 | 0.8090 | +2.3pp |
| [0.05, 0.10) | 8374 | 0.7398 | 0.7827 | +4.3pp |
| [0.10, 0.20) | 10537 | 0.7006 | 0.7586 | +5.8pp |
| [0.20, inf) | 2435 | 0.7714 | 0.8072 | +3.6pp |

## Conclusion

ε=0.05 is at the elbow point where delta-compression-% begins to flatten.
LP-best advantage in compressed region (range<0.05): +0.8~2.3pp
LP-best advantage in non-compressed region (range≥0.05): +3.6~5.8pp
ρ improvement by filtering compressed: 0.6325 → 0.7095 (+12.2%)

Files:
- Script: code/epsilon_sensitivity.py
- Results: output/epsilon_sensitivity_results.txt
- JSON: output/fewnerd_mf4v2_seed42_v3/epsilon_sensitivity.json