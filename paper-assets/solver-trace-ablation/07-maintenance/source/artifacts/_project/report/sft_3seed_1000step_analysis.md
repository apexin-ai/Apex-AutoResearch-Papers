# SFT 1000-step 3-seed Analysis

## Per-seed Results

| Metric | s42 | s43 | s44 |
|--------|-----|-----|-----|
| prove_rate | 0.13 | 0.11 | 0.15 |
| n_proved | 13 | 11 | 15 |
| mean_isr | 0.0738 | 0.0699 | 0.0884 |
| proved_only_mean_isr | 0.5677 | 0.6352 | 0.5892 |
| genuine_count | 12 | 10 | 14 |
| genuine_rate | 0.9231 | 0.9091 | 0.9333 |
| h7_strict | 0 | 0 | 0 |
| h1_strict | 1 | 1 | 1 |
| h8_conj_collapse | 0 | 0 | 0 |
| conclusion_in_premise | 1 | 1 | 1 |
| content_independent | 0 | 0 | 0 |
| isr_1_count | 0 | 1 | 0 |
| train_final_loss | 0.0168 | 0.0167 | 0.0171 |

## 3-seed Summary (mean +/- std)

| Metric | Mean | Std |
|--------|------|-----|
| prove_rate | 0.130 | 0.016 |
| mean_isr | 0.077 | 0.008 |
| genuine_count | 12.0 | 1.63 |
| genuine_rate | 0.922 | 0.010 |
| train_final_loss | 0.0169 | 0.0002 |

## Key Observations

- genuine_rate extremely stable: 90.9%-93.3% across seeds (all >90%)
- h1_strict_count = 1 in ALL seeds (same folio_167 sample)
- Zero h7_strict, h8, content_independent hacking across all seeds
- prove_rate moderate variance (11-15%) typical for SFT with small eval set
