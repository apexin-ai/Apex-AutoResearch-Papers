# Cross-dataset OOD Signal Analysis

## Exp 1: SciERC model → CoNLL (NER only)
- Instances: 3453, Parsed: 3453, Valid NER: 2756
- Parse rate: 100.0%
- Greedy NER F1: 0.5221

| Signal | ρ | p-value | AUROC | In-domain ρ | Δρ |
|--------|---|---------|-------|-------------|-----|
| SJ | +0.3777 *** | 3.48e-94 | 0.6920 | 0.364 | +0.0137 |
| FK | +0.2852 *** | 9.51e-53 | 0.6423 | 0.254 | +0.0312 |
| VC | +0.4689 *** | 1.00e-150 | 0.7366 | 0.386 | +0.0829 |
| LP | +0.2458 *** | 3.30e-39 | 0.6324 | 0.217 | +0.0288 |
| EM | +0.2996 *** | 2.89e-58 | 0.6549 | 0.307 | -0.0074 |

## Exp 2: CoNLL model → SciERC (NER+RE)
- Instances: 551, Parsed: 551, Valid NER: 529
- Parse rate: 100.0%
- Greedy NER F1: 0.0093
- Greedy RE F1: 0.0008

| Signal | ρ | p-value | AUROC | In-domain ρ | Δρ |
|--------|---|---------|-------|-------------|-----|
| SJ | -0.1857 *** | 1.71e-05 | N/A | 0.364 | -0.5497 |
| FK | -0.0695 | 0.1105 | N/A | 0.254 | -0.3235 |
| VC | +0.1051 * | 0.0156 | N/A | 0.386 | -0.2809 |
| LP | -0.1521 *** | 4.47e-04 | N/A | 0.217 | -0.3691 |
| EM | -0.2015 *** | 3.00e-06 | N/A | 0.307 | -0.5085 |

## Key Findings

### SciERC→CoNLL
- Best structural signal: VC (ρ=+0.4689)
- LogProb (LP): ρ=+0.2458
- Structural > LP by Δρ=+0.2231
- Structural signals ALL significant (p<0.05)
- LP significant (p=3.30e-39)

### CoNLL→SciERC
- Best structural signal: VC (ρ=+0.1051)
- LogProb (LP): ρ=-0.1521
- Structural > LP by Δρ=+0.2572
- Structural signals NOT all significant
- LP significant (p=4.47e-04)

### Overall: Do structural signals remain effective under OOD?

- **SciERC→CoNLL**: avg structural ρ = 0.3773 (in-domain avg = 0.3347, Δ = +0.0426), LP ρ = +0.2458 (in-domain = 0.217, Δ = +0.0288)
- **CoNLL→SciERC**: avg structural ρ = -0.0500 (in-domain avg = 0.3347, Δ = -0.3847), LP ρ = -0.1521 (in-domain = 0.217, Δ = -0.3691)
