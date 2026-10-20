# D157 Shuffled-ISR s43 Eval Results

**Experiment:** d157-shuffled-isr-s43
**Checkpoint:** /root/autodl-tmp/outputs/d157_shuffled_isr_s43/checkpoint-500
**Eval data:** data/proofwriter_fol_100.jsonl (C008 compliant)
**Training:** 500/500 steps completed, Qwen3-4B, seed=43
**Eval date:** 2026-05-21

## Eval Metrics

| Metric | s43 | s42 (ref) |
|--------|-----|-----------|
| prove_rate | 0.16 (16/100) | 0.15 (15/100) |
| mean_isr | 0.0908 | 0.0851 |
| isr_std | 0.2314 | — |
| proved_only_isr | 0.5675 | 0.5673 |

## By Answer Type (s43)

| Type | n | proved | ISR |
|------|---|--------|-----|
| true | 34 | 12 | 0.1962 |
| unknown | 41 | 3 | 0.0441 |
| false | 25 | 1 | 0.0240 |

## Hacking Classification (s43)

| Category | Count | % of proved |
|----------|-------|-------------|
| TS (tautology shortcut) | 1 | 6.2% |
| CE (conclusion embedding) | 1 | 6.2% |
| PG (premise gathering) | 0 | 0.0% |
| CI (content-independent) | 0 | 0.0% |
| **Genuine** | **14** | **87.5%** |

## Cross-seed Comparison

| Metric | s42 | s43 | Delta |
|--------|-----|-----|-------|
| prove_rate | 0.15 | 0.16 | +0.01 |
| mean_isr | 0.0851 | 0.0908 | +0.0057 |
| proved_only_isr | 0.5673 | 0.5675 | +0.0002 |
| genuine_rate | 86.7% | 87.5% | +0.8pp |
| TS | 1 | 1 | 0 |
| CE | 1 | 1 | 0 |

**Conclusion:** s42 and s43 are highly consistent. Shuffled-ISR produces stable results across seeds with ~15-16% prove rate, ~0.57 proved-only ISR, and ~87% genuine rate.
