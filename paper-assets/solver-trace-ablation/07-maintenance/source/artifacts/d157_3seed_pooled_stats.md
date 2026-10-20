# D157 Shuffled-ISR: 3-Seed Pooled Statistics

Date: 2026-05-20

## Per-Seed Results

| Seed | PR (n/100) | Genuine | TS | CE | PG | CI | Genuine% | ISR* (proved-only) |
|------|-----------|---------|----|----|----|----|----------|-------------------|
| s42  | 0.15 (15) | 13      | 1  | 1  | 0  | 0  | 86.7%    | 0.5673            |
| s43  | 0.16 (16) | 14      | 1  | 1  | 0  | 0  | 87.5%    | 0.5680            |
| s44  | 0.15 (15) | 13      | 1  | 1  | 0  | 0  | 86.7%    | 0.5423            |

## 3-Seed Aggregated Statistics

| Metric | Mean | Std | Notes |
|--------|------|-----|-------|
| Prove Rate | 0.153 | 0.006 | 15.3% |
| Genuine% (per-seed) | 86.9% | 0.5% | |
| ISR* (proved-only) | 0.559 | 0.015 | |

## Pooled Totals (N=300)

| Metric | Value |
|--------|-------|
| Total proved | 46/300 |
| Total genuine | 40/46 |
| Total TS | 3 |
| Total CE | 3 |
| Total PG | 0 |
| Total CI | 0 |
| Pooled genuine% | 86.96% (40/46) |
| Wilson 95% CI | [74.3%, 93.9%] |

## Cross-Condition Comparison

| Condition | Seeds | Mean PR | Mean Genuine% | Notes |
|-----------|-------|---------|--------------|-------|
| **Shuffled-ISR β=0.1** | **3** | **15.3±0.6%** | **86.9±0.5%** | This experiment (D157) |
| Exec-only | 3 | 68.0±4.7% | 5.9% | High PR, very low genuine |
| ISR β=0.1 | 5 | ~15% | 15.8±17.6% | High variance |
| Random β=0.1 | 5 | ~13% | 9.4±7.9% | |

## Key Finding

Shuffled-ISR achieves dramatically higher genuine rate (86.9%) compared to standard ISR (15.8%) and Random (9.4%) at similar prove rates (~15%). The shuffled ablation order breaks the Goodhart signal while preserving the formal verification training, producing proofs where ~87% withstand clause-level ablation — i.e., every clause contributes to the proof.

Wilson 95% CI for pooled genuine rate: [74.3%, 93.9%] (n=46 proved, 40 genuine).
