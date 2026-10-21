# D157 Shuffled-ISR s44 Eval Results

**Experiment:** d157-shuffled-isr-s44
**Checkpoint:** /root/autodl-tmp/outputs/d157_shuffled_isr_s44/checkpoint-500
**Eval data:** data/proofwriter_fol_100.jsonl (C008 compliant)
**Training:** 500/500 steps completed, Qwen3-4B, seed=44, config=grpo_shuffled_isr_b01.yaml
**Wall clock:** 4327s (~1h12m)
**Final train stats:** prove_rate=0.12325, mean_isr=0.06143, parse_rate=1.0
**Eval date:** 2026-05-21

## Eval Metrics

| Metric | s44 | s43 (ref) | s42 (ref) |
|--------|-----|-----------|-----------|
| prove_rate | 0.15 (15/100) | 0.16 (16/100) | 0.15 (15/100) |
| mean_isr | 0.0813 | 0.0908 | 0.0851 |
| isr_std | 0.2225 | 0.2314 | 0.2265 |
| median_isr | 0.0000 | 0.0000 | 0.0000 |
| max_isr | 0.8889 | 0.8889 | — |
| proved_only_isr | 0.5423 | 0.5675 | 0.5673 |

## By Answer Type (s44)

| Type | n | proved | ISR |
|------|---|--------|-----|
| true | 34 | 12 | 0.1852 |
| unknown | 41 | 2 | 0.0302 |
| false | 25 | 1 | 0.0240 |

## Hacking Classification (s44)

| Category | Count | % of proved |
|----------|-------|-------------|
| TS (tautology shortcut) | 1 | 6.7% |
| CE (conclusion embedding) | 1 | 6.7% |
| PG (premise gathering) | 0 | 0.0% |
| CI (content-independent) | 0 | 0.0% |
| **Genuine** | **13** | **86.7%** |

## Cross-seed Comparison (all 3 seeds)

| Metric | s42 | s43 | s44 | Mean | Std |
|--------|-----|-----|-----|------|-----|
| prove_rate | 0.15 | 0.16 | 0.15 | 0.153 | 0.006 |
| mean_isr | 0.0851 | 0.0908 | 0.0813 | 0.0857 | 0.0048 |
| proved_only_isr | 0.5673 | 0.5675 | 0.5423 | 0.5590 | 0.0145 |
| genuine_rate | 86.7% | 87.5% | 86.7% | 86.9% | 0.5pp |
| genuine_count | 13 | 14 | 13 | 13.3 | 0.6 |
| TS | 1 | 1 | 1 | 1.0 | 0.0 |
| CE | 1 | 1 | 1 | 1.0 | 0.0 |

**Conclusion:** All 3 seeds are highly consistent. Shuffled-ISR produces stable results across seeds with ~15% prove rate, ~0.55 proved-only ISR, and ~87% genuine rate. The hypothesis holds: shuffling ISR (breaking semantic alignment while preserving distribution) does not degrade performance, confirming ISR acts as distributional noise rather than a semantic signal during training.

## Paths

- Checkpoint: `/root/autodl-tmp/outputs/d157_shuffled_isr_s44/checkpoint-500`
- Training log: `~/runs/solver-trace-ablation/d157-shuffled-isr-s44.log`
- Eval results: `/root/autodl-tmp/outputs/d157_shuffled_isr_s44/eval_sta_results.json`
- Classify results: `/root/autodl-tmp/outputs/d157_shuffled_isr_s44/classify_h7_results.json`
