# A2: LLaMA-8B TOST Feasibility Check

## Data Structure
- **54 batches** across **2 count levels** (count=8: 27, count=16: 27)
- Per count: 1 low_bcs + 1 high_bcs (designed extremes) + 25 random
- BCS range: random 0.65–0.90 (narrow); with controlled 0.47–0.97

## TOST Verdict: UNDERPOWERED — NOT FEASIBLE

Three factors make standalone TOST uninformative:
1. Only 2 count levels (vs Qwen3's 7) → interaction = single slope-difference, 1 df
2. Narrow BCS range in random batches → per-count slopes n.s. (count=8: p=0.25; count=16: p=0.59)
3. N=54 too small (Qwen3 N=375 was already inconclusive at p_TOST=0.684)

Approximate TOST: interaction ~34.5pp (SE=27.7pp), 95% CI [-19.9, 88.9]pp, p_TOST=0.87

## BCS Slope Replication (MEANINGFUL)

| Metric | LLaMA-8B | Qwen3-32B |
|--------|----------|-----------|
| Overall Pearson r | -0.39 (p=0.004) | ~-0.60 |
| Overall Spearman ρ | -0.43 (p=0.001) | — |
| count=8 extreme Δ | -27.1pp | -31.2pp |
| count=16 extreme Δ | -24.0pp | -31.8pp |
| Effect ratio | ~87% of Qwen3 | baseline |

## Recommendation
Do not add standalone LLaMA TOST to paper. Present as cross-model BCS slope replication (already in paper). If reviewer insists on cross-model TOST, consider combined LLaMA+Qwen3 analysis with model as random effect.
