# Qwen3-4B Dose-Response Summary

## Per-condition aggregates (mean ± std across seeds)

| Condition | β | N seeds | Prove Rate | Mean ISR | Genuine Rate (of proved) |
|-----------|---|---------|------------|----------|--------------------------|
| SFT | — | 3 | 0.130 ± 0.020 | 0.0774 ± 0.0098 | 0.922 ± 0.012 |
| exec-only | 0.0 | 4 | 0.955 ± 0.048 | 0.2893 ± 0.2667 | 0.043 ± 0.046 |
| ISR | 0.05 | 1 | 0.550 ± 0.000 | 0.4175 ± 0.0000 | — |
| ISR | 0.1 | 2 | 0.850 ± 0.057 | 0.5697 ± 0.3299 | — |
| ISR | 0.2 | 3 | 0.967 ± 0.031 | 0.6791 ± 0.1996 | 0.000 ± 0.000 |
| ISR | 0.3 | 2 | 0.905 ± 0.064 | 0.4938 ± 0.3398 | 0.134 ± 0.189 |
| random | 0.1 | 2 | 0.840 ± 0.071 | 0.0829 ± 0.0296 | 0.067 ± 0.000 |

## Notes

- **Missing data**: plan002-additive-b01-s43, plan018-random-b01-s43 — checkpoints cleaned, no eval available
- **Step mismatch**: exec-only s42 = 500 steps, s43/s44 = 1000 steps; ISR β=0.3 s42 = 1000 steps, s43 = 500 steps
- **ISR calculation**: mean_isr is computed over all 100 samples (unproved samples get ISR=0)
- **Taxonomy rates**: h7/h1/h8/genuine rates are relative to n_proved
- **C013 standard**: genuine = proved − H7 − H1_exact − H8
- **Exec-only s42 vs s45**: very different taxonomy despite similar prove_rate — s42 has H1-dominant hacking, s45 has H7-dominant hacking

## Raw data source files

| Experiment | Eval source | Taxonomy source |
|-----------|------------|-----------------|
| plan001-exec-only-s42-r2 | eval_sta_plan001_r2.json | h8_retroactive_audit.json / d086_missed_classify_h7.json |
| plan001-exec-only-s43-1000-r2 | plan001_exec_only_s43_1000_r2/eval_sta_results.json | MISSING |
| plan001-exec-only-s44-1000-r2 | plan001_exec_only_s44_1000_r2/eval_sta_results.json | MISSING |
| sweep-exec-only-s45 | sweep_exec_only_s45/eval_sta_results.json | sweep_exec_only_s45/classify_h7_results.json |
| sweep-isr-b005-s42 | eval_sta_sweep_isr_b005_s42.json | MISSING |
| plan002-additive-b01-s42 | eval_results_backup/plan002_additive_b01_s42_eval_sta_results.json | MISSING (1000-step taxonomy available separately) |
| plan002-additive-b01-s43 | MISSING | MISSING |
| plan002-additive-b01-s44 | eval_results_backup/plan002_additive_b01_s44_eval.json | MISSING |
| sweep-isr-b02-s42 | sweep_isr_b02_s42_v2/eval/eval_sta_results.json | sweep_isr_b02_s42_v2/eval/hacking_taxonomy.json |
| sweep-isr-b02-s43 | sweep_isr_b02_s43/eval_results.json | sweep_isr_b02_s43/hacking_taxonomy.json |
| sweep-isr-b02-s44 | sweep_isr_b02_s44/eval/eval_results.json | sweep_isr_b02_s44/eval/taxonomy.json |
| exp1-isr-b03-s42 | exp1_isr_b03_s42_1000/eval_results.json | h7_results.json + h8_retroactive_audit.json |
| exp1-isr-b03-s43-r3 | eval_sta_exp1_isr_b03_s43_r3.json | h8_retroactive_audit.json |
| plan018-random-b01-s42 | eval_sta_plan018_additive_random_b01_s42.json | plan018_random_s42_taxonomy_verification.json (partial) |
| plan018-random-b01-s43 | MISSING | MISSING |
| plan018-random-b01-s44-r2 | plan018_additive_random_b01_s44_r2/eval_sta_results.json | plan018_additive_random_b01_s44_r2/taxonomy.json |
| plan009-sft-s42 | plan009_sft_baseline_s42_1000/eval_sta_results.json | sft_1000_taxonomy_summary.json |
| plan009-sft-s43 | plan009_sft_baseline_s43_1000/eval_sta_results.json | sft_1000_taxonomy_summary.json |
| plan009-sft-s44 | plan009_sft_baseline_s44_1000/eval_sta_results.json | sft_1000_taxonomy_summary.json |
