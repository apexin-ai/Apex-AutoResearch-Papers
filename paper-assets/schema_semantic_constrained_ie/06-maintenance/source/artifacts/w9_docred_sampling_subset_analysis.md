# W9 DocRED Sampling r3 Subset Analysis

## Kill Confirmation

- PID 384608 killed successfully (SIGTERM, no force needed)
- tmux session `w9_docred_sampling_r3` cleaned
- GPU (cuda:1) freed — no compute processes remaining

## Output Summary

- File: `outputs/w9_qwen_docred_zs_sampling_r3.jsonl`
- Lines: 114 (1 sample per doc, 114 unique docs)
- Parse failures: 2 (1.8%)
- Mode: `full_s1` (sampling, zero-shot)
- Avg inference time: 20.99s/doc, total 39.9 min

## Violation Metrics

| Metric | Sampling r3 (114 docs) | Greedy baseline (998 docs) | Delta |
|--------|----------------------|---------------------------|-------|
| ET     | 0.00%                | 0.00%                     | —     |
| RV     | 0.00%                | 0.03%                     | −0.03pp |
| DR     | 10.31%               | 10.21%                    | +0.10pp |
| CF     | 12.63%               | 2.57%                     | +10.06pp |

## F1 Metrics

| Metric | Sampling r3 | Greedy baseline | Delta |
|--------|------------|-----------------|-------|
| E_P    | 55.85      | —               | —     |
| E_R    | 58.31      | —               | —     |
| E_F1   | 57.05      | 59.37           | −2.32 |
| R_P    | 6.88       | —               | —     |
| R_R    | 9.34       | —               | —     |
| R_F1   | 7.92       | 8.23            | −0.31 |

## CF Violation Analysis

Sampling causes significantly more cross-field inconsistency (12.63% vs 2.57%). Root cause: entities get typed differently in the `entities` list vs `relations` head_type/tail_type fields. Examples:

- "Greek" → {MISC, LOC}
- "Emancipation Proclamation" → {TIME, MISC}
- "2016 Summer Olympics" → {LOC, MISC}

Temperature introduces randomness in type assignments, making the model less self-consistent across the two output sections.

## Conclusions

1. **DR unchanged**: 10.31% vs 10.21% (±0.1pp). Sampling does NOT reduce domain-range violations — the model's structural errors are systematic, not stochastic.
2. **ET/RV remain 0%**: Schema vocabulary compliance is robust regardless of decoding strategy.
3. **CF significantly worse**: 12.63% vs 2.57%. Sampling degrades cross-field consistency by ~5x.
4. **F1 slightly lower**: Both entity and relation F1 drop modestly (−2.32 / −0.31), consistent with sampling adding noise without improving coverage.
5. **Verdict**: Sampling offers no benefit over greedy for this task. The DR violations are a structural problem (model doesn't internalize ontology constraints), not a search problem that sampling could solve.
