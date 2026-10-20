## Per-turn GAR-ours 衰减（N=45）

| Turn | Base | TG | UG | LoRA |
|------|------|-----|-----|------|
| T1 | 0.049±0.021 | 0.547±0.038 | 0.551±0.042 | 0.553±0.050 |
| T2 | 0.018±0.008 | 0.511±0.040 | 0.511±0.046 | 0.511±0.048 |
| T3 | 0.013±0.006 | 0.509±0.034 | 0.511±0.033 | 0.503±0.039 |
| T4 | 0.010±0.004 | 0.498±0.041 | 0.501±0.050 | 0.495±0.054 |
| T5 | 0.009±0.004 | 0.447±0.156 | 0.447±0.158 | 0.447±0.158 |

## Normalized decay (clean N=39)
Base: T1→T5 loses 80%. TG/UG/LoRA: only 7-8%.

## Paired t-test T1 vs T5
Base: t=14.12, p<0.000001. TG: t=3.75, p=0.00052. UG: t=3.84, p=0.00039. LoRA: t=3.90, p=0.00033.

## Conversation length correlation (N=39, turns 5-7)
All |ρ|<0.2, p>0.2. Not significant due to narrow turn range.

## Data quality: 5/50 truncated, 6/50 last-turn collapse (consistent across all models = data artifact).