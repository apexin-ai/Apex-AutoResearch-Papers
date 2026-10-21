# VOTA vs Exception_only: Paired Bootstrap + McNemar (3-seed)

## Per-seed Results

| Seed | exc_only | VOTA | Diff | Bootstrap p | McNemar χ² | McNemar p | Discordant (exc>vota : vota>exc) |
|------|----------|------|------|-------------|------------|-----------|----------------------------------|
| 42 | 99.83% | 99.41% | +0.42pp | 0.0629 | 2.78 | 0.0956 | 7:2 |
| 123 | 99.83% | 98.66% | +1.18pp | **0.0002** | 10.89 | **0.0010** | 16:2 |
| 456 | 99.83% | 99.08% | +0.76pp | **0.0047** | 6.23 | **0.0126** | 11:2 |

## Aggregate
- Mean diff: **+0.78pp ± 0.31pp**
- Range: [0.42, 1.18]pp
- 2/3 seeds significant at p<0.05
- seed42 marginal (p=0.063) due to ceiling effect — only 9 discordant pairs
- All 3 seeds directionally consistent: exception_only > VOTA
