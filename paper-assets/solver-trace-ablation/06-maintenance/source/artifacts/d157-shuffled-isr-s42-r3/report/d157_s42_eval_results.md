# D157 Shuffled-ISR s42-r3: Eval + Classify Results

**Date**: 2026-05-20
**Experiment**: d157-shuffled-isr-s42-r3
**Hypothesis**: Batch-internal ISR permutation preserves ISR distribution but breaks sample↔ISR semantic link.

## Training Summary
- **Model**: Qwen3-4B
- **Steps**: 500/500 completed
- **Seed**: 42
- **Config**: grpo_shuffled_isr_b01.yaml
- **Data**: train_500_seed42.jsonl
- **Wall clock**: ~73 min (1.22 GPU-hours)
- **Training end behavior**: prove_rate highly sparse in final 20 steps (mostly 0, occasional 0.25-0.5)

## Eval Results (eval_sta.py on proofwriter_fol_100.jsonl)

| Metric | Value |
|--------|-------|
| n_problems | 100 |
| n_proved | 15 |
| prove_rate | 0.15 |
| mean_isr | 0.0851 |
| proved_only_mean_isr | 0.5673 |
| isr_std | 0.2265 |
| median_isr | 0.0 |
| max_isr | 0.889 |

### By answer type
| Type | Count | Proved | Prove Rate | Mean ISR |
|------|-------|--------|------------|----------|
| true | 34 | 12 | 0.353 | 0.196 |
| false | 25 | 1 | 0.040 | 0.024 |
| unknown | 41 | 2 | 0.049 | 0.030 |

## Hacking Classification (classify_h7.py)

| Category | Count | % of Proved |
|----------|-------|-------------|
| TS (H7 tautology-shortcut) | 1 | 6.7% |
| CE (H1 conclusion-in-premise) | 1 | 6.7% |
| PG (H8 conjunction-collapse) | 0 | 0.0% |
| CI (content-independent) | 0 | 0.0% |
| **Genuine** | **13** | **86.7%** |

### Hacking details
- TS example: folio_212 (1 premise, ISR=0.667)
- CE example: folio_167 (6 premises, ISR=0.143)
- No PG/CI instances

## Paths
- Checkpoint: `/root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/`
- Eval results: `/root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/eval_sta_results.json`
- Classify results: `/root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/classify_h7_results.json`
- Training log: `/root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/reward_log.jsonl`
