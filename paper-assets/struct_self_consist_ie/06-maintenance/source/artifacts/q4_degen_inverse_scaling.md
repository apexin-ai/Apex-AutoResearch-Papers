# Q4: Degeneracy × Inverse Scaling Analysis

## Method
- **Data**: 6 dataset-setting combinations (SciERC/CoNLL/FewNERD × Finetuned/Pretrained)
- **N values**: Truncation from max-N file (up to N=64 for SciERC/CoNLL, N=16 for FewNERD-FT, N=8 for FewNERD-PT)
- **Degeneracy**: Binary per instance at source N — all N samples produce identical (start, end, type) entity set
- **Inverse scaling**: F1(N_large) < F1(N_small) for a given N→N' transition
- **MV**: Strict majority voting with (start, end, type) matching, threshold > N/2
- **Test**: Fisher exact test on 2×2 table (degenerate/non-degenerate × inverse/non-inverse)

## Results

### Aggregate (all 6 datasets)

| Group | Transitions | Inverse | Rate | OR | p |
|-------|------------|---------|------|-----|---|
| Degenerate | 54,411 | 725 | **1.3%** | — | — |
| Non-degenerate | 141,264 | 15,625 | **11.1%** | — | — |
| **Fisher** | — | — | — | **0.109** | **<1e-300** |

**Conclusion**: Degenerate instances are ~9× less likely to exhibit inverse scaling (OR=0.109, p≈0). This strongly supports the diagnostic framework — degeneracy signals model certainty, and inverse scaling is concentrated in non-degenerate (uncertain) instances.

### By Setting

| Setting | Degen inv% | Non-degen inv% | OR | p |
|---------|-----------|---------------|-----|---|
| Finetuned | 1.5% (452/31,039) | 8.2% (6,775/83,081) | 0.166 | <1e-300 |
| Pretrained | 1.2% (273/23,372) | 15.2% (8,850/58,183) | 0.066 | <1e-300 |

Pretrained models show even stronger effect (OR=0.066 vs 0.166) — consistent with higher overall inverse scaling rate in pretrained models creating more room for the degeneracy protective effect.

## Per-dataset breakdown

### SciERC Finetuned (529 instances, N=2→64)

| Group | Transitions | Inverse | Rate |
|-------|------------|---------|------|
| Degenerate | 485 | 4 | 0.8% |
| Non-degenerate | 2,160 | 207 | 9.6% |

Fisher: OR=0.078, p<1e-6 (***)

### CoNLL Finetuned (2,756 instances, N=2→64)

| Group | Transitions | Inverse | Rate |
|-------|------------|---------|------|
| Degenerate | 8,256 | 21 | 0.3% |
| Non-degenerate | 5,524 | 224 | 4.1% |

Fisher: OR=0.060, p<1e-6 (***)

### FewNERD Finetuned (32,565 instances, N=2→16)

| Group | Transitions | Inverse | Rate |
|-------|------------|---------|------|
| Degenerate | 22,298 | 427 | 1.9% |
| Non-degenerate | 75,397 | 6,344 | 8.4% |

Fisher: OR=0.213, p<1e-6 (***)

### SciERC Pretrained (529 instances, N=2→64)

| Group | Transitions | Inverse | Rate |
|-------|------------|---------|------|
| Degenerate | 81 | 3 | 3.7% |
| Non-degenerate | 2,564 | 254 | 9.9% |

Fisher: OR=0.350, p=0.083 (n.s.) — underpowered due to very few degenerate instances (pretrained SciERC has low degeneracy: 0–10%)

### CoNLL Pretrained (2,756 instances, N=2→64)

| Group | Transitions | Inverse | Rate |
|-------|------------|---------|------|
| Degenerate | 5,284 | 15 | 0.3% |
| Non-degenerate | 8,496 | 670 | 7.9% |

Fisher: OR=0.033, p<1e-6 (***)

### FewNERD Pretrained (32,565 instances, N=2→8)

| Group | Transitions | Inverse | Rate |
|-------|------------|---------|------|
| Degenerate | 18,007 | 255 | 1.4% |
| Non-degenerate | 47,123 | 7,926 | 16.8% |

Fisher: OR=0.071, p<1e-6 (***)

## Per-transition breakdown (selected)

### SciERC Finetuned
| Transition | Degen inv% | Non-degen inv% | OR | p |
|-----------|-----------|---------------|------|------|
| 2→4 | 1.7% (4/236) | 20.1% (59/293) | 0.068 | <0.001 |
| 4→8 | 0.0% (0/117) | 17.0% (70/412) | 0.000 | <0.001 |
| 8→16 | 0.0% (0/74) | 7.7% (35/455) | 0.000 | 0.009 |
| 16→32 | 0.0% (0/38) | 5.5% (27/491) | 0.000 | 0.247 |
| 32→64 | 0.0% (0/20) | 3.1% (16/509) | 0.000 | 1.000 |

### CoNLL Finetuned
| Transition | Degen inv% | Non-degen inv% | OR | p |
|-----------|-----------|---------------|------|------|
| 2→4 | 1.0% (21/2176) | 10.3% (60/580) | 0.084 | <0.001 |
| 4→8 | 0.0% (0/1915) | 7.4% (62/841) | 0.000 | <0.001 |
| 8→16 | 0.0% (0/1656) | 4.0% (44/1100) | 0.000 | <0.001 |
| 16→32 | 0.0% (0/1381) | 2.4% (33/1375) | 0.000 | <0.001 |
| 32→64 | 0.0% (0/1128) | 1.5% (25/1628) | 0.000 | <0.001 |

### FewNERD Finetuned
| Transition | Degen inv% | Non-degen inv% | OR | p |
|-----------|-----------|---------------|------|------|
| 2→4 | 3.3% (420/12879) | 8.6% (1687/19686) | 0.360 | <0.001 |
| 4→8 | 0.1% (7/6452) | 9.8% (2565/26113) | 0.010 | <0.001 |
| 8→16 | 0.0% (0/2967) | 7.1% (2092/29598) | 0.000 | <0.001 |

### CoNLL Pretrained
| Transition | Degen inv% | Non-degen inv% | OR | p |
|-----------|-----------|---------------|------|------|
| 2→4 | 0.9% (15/1739) | 19.8% (201/1017) | 0.035 | <0.001 |
| 4→8 | 0.0% (0/1291) | 10.7% (157/1465) | 0.000 | <0.001 |
| 8→16 | 0.0% (0/1002) | 8.2% (144/1754) | 0.000 | <0.001 |
| 16→32 | 0.0% (0/715) | 5.1% (105/2041) | 0.000 | <0.001 |
| 32→64 | 0.0% (0/537) | 2.8% (63/2219) | 0.000 | <0.001 |

### FewNERD Pretrained
| Transition | Degen inv% | Non-degen inv% | OR | p |
|-----------|-----------|---------------|------|------|
| 2→4 | 2.1% (251/11762) | 19.7% (4103/20803) | 0.089 | <0.001 |
| 4→8 | 0.1% (4/6245) | 14.5% (3823/26320) | 0.004 | <0.001 |

## Key Patterns

1. **For N≥4, degenerate instances show near-zero inverse scaling** (0.0–0.1%). The only non-trivial inverse scaling in degenerate instances occurs at the 2→4 transition (1–5%), where degeneracy at N=2 is a weak signal (only 2 samples need to agree).

2. **Non-degenerate inverse scaling decreases with N**: as N grows, the non-degenerate inverse rate drops (e.g., CoNLL-FT: 10.3% at 2→4 → 1.5% at 32→64). MV stabilizes with more samples even for uncertain instances.

3. **Pretrained models show higher non-degenerate inverse rates** than finetuned (15.2% vs 8.2% overall), consistent with pretrained models having more diverse/uncertain outputs. But the protective effect of degeneracy is equally strong.

4. **SciERC-PT is the only non-significant result** (p=0.083) — explained by extremely low degeneracy rate (0–10%) yielding too few degenerate transitions (81 total) for adequate power.
