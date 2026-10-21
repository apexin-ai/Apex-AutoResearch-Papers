# Retry Dose-Response Per-Trial Analysis

## Death Definition
- is_death = (score <= -100)
- Episode-level DR(N) = P(all first N trials are death)
- Each trial is a complete restart (retry: no reflection; reflexion: with reflection)

## Dose-Response Table (death-prone tasks, 200 episodes)

| N | Retry DR | 95% CI | Reflexion DR | 95% CI |
|---|----------|--------|--------------|--------|
| 1 | 0.4650 | [0.397, 0.534] | 0.4600 | [0.392, 0.529] |
| 2 | 0.4450 | [0.378, 0.514] | 0.3400 | [0.278, 0.408] |
| 3 | 0.4150 | [0.349, 0.484] | 0.2700 | [0.213, 0.335] |

## Key Findings
- Retry N=1→N=3: only -5pp (flat curve, ~2pp/trial marginal improvement)
- Reflexion N=1→N=3: -19pp (steep curve, reflection mechanism is key)
- N=1 baselines nearly identical (~46%), confirming same starting point
- Blind retry ineffective for death avoidance; reflexion's benefit comes from self-correction, not retry opportunity

## Source
- Data: results/retry_dose_response_analysis.json on westb-14838
- Method: Extracted from existing retry-control-baseline and reflexion per-trial JSON data
- No new GPU experiments needed for N=1,2,3