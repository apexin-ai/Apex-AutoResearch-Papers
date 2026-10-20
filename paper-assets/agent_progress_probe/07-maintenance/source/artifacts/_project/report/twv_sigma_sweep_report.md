# TWV Sigma Sensitivity Sweep

## Results Table

| σ  | MV agree% | conf1 flip% | conf2 flip% | conf3 flip% | mean flips | stag% |
|----|-----------|-------------|-------------|-------------|------------|-------|
|  1 |     85.9% |       17.2% |        6.6% |        0.4% |      0.602 | 27.9% |
|  2 |     88.5% |       14.1% |        5.2% |        0.1% |      0.346 | 26.5% |
|  3 |     88.8% |       13.6% |        5.2% |        0.1% |      0.204 | 25.2% |
|  5 |     88.9% |       13.7% |        4.6% |        0.0% |      0.125 | 24.4% |
| 10 |     88.5% |       13.9% |        5.5% |        0.1% |      0.060 | 24.0% |

MV baseline smoothness: 0.962 mean flips/traj

## Smoothness vs MV-Agreement Tradeoff

- σ=1: agreement=85.9%, smoothness reduction +37.5% vs MV
- σ=2: agreement=88.5%, smoothness reduction +64.0% vs MV
- σ=3: agreement=88.8%, smoothness reduction +78.8% vs MV
- σ=5: agreement=88.9%, smoothness reduction +87.0% vs MV (peak agreement)
- σ=10: agreement=88.5%, smoothness reduction +93.8% vs MV

## Key Findings

1. **Sweet spot at σ=5**: Peak MV agreement (88.9%) with 87% smoothness reduction
2. **Diminishing returns σ>5**: Agreement slightly drops at σ=10 (over-smoothing washes out temporal signal)
3. **σ=1 too narrow**: Agreement drops to 85.9% — kernel too tight to aggregate temporal info
4. **σ=2-5 plateau**: Agreement is stable at 88.5-88.9%, main difference is smoothness
5. **stag% monotonically decreases** with σ: larger kernel → more temporal averaging → slightly more "progress" labels
