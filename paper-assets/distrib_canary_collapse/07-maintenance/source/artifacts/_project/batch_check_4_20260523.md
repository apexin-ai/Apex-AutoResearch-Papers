# Batch Check #4 — 2026-05-23

## 1. scale_14b_t15_a045_s43_fp32 (westd-17855)

- **Status**: DONE (EXIT_CODE=0)
- **PID**: 762806 (exited)
- **Generations**: gen_0 — gen_15 (16/16 complete)
- **Registry**: updated to DONE/success

### Metrics trajectory (key)

| Gen | token_entropy | ece    | distinct_3 | perplexity |
|-----|--------------|--------|------------|------------|
| 0   | 2.9731       | 0.0081 | 0.8167     | 19.83      |
| 5   | 2.1745       | 0.1354 | 0.5636     | 28.18      |
| 10  | 2.2337       | 0.1432 | 0.4877     | 31.37      |
| 15  | 2.2626       | 0.1494 | 0.4643     | 34.18      |

- distinct_3 drift: 0.817 → 0.464 (−43.2%)
- perplexity drift: 19.83 → 34.18 (+72.3%)

### D102 analysis (distinct_3 downstream)

| Pair                    | K   | Methods              |
|-------------------------|-----|----------------------|
| token_entropy<distinct_3 | 3/5 | diff, perm, ty       |
| ece<distinct_3           | 3/5 | diff, perm, ty       |

- **robust_pairs (K≥3)**: 2/2
- threshold_onset: 0/2 (no 3σ onset detected — gradual degradation at low α)
- naive_xcorr D111: 0/2 (peak_lag not < 0)
- Artifact: `artifacts/D102_14b_t15_a045_s43_fp32_d3.json`

## 2. scale_14b_t10_a045_s44_fp32 (westd-17855)

- **Status**: RUNNING
- **PID**: 796624 (elapsed: 9h 46m)
- **Generations**: gen_0 — gen_9 (10 dirs present, expected 11: gen_0–gen_10)
- Likely on gen_10 or finishing post-processing

## 3. scale_14b_t15_a075_s43_fp32 (westd-19828)

- **Status**: RUNNING
- **PID**: 857058 (elapsed: 15h 37m)
- **Generations**: gen_0 — gen_14 (15 dirs present, expected 16: gen_0–gen_15)
- Likely on gen_15 (final generation)

## Actions taken

1. Registry: `scale_14b_t15_a045_s43_fp32` → DONE/success
2. D102 analysis run on westd-17855, output saved to server + local artifacts
3. Artifact registered: `D102_14b_t15_a045_s43_fp32_d3`

## Next steps

- Wait for t10_a045_s44 and t15_a075_s43 to complete
- Run D102 for both once done
- t10_a045_s44 should finish within ~1h; t15_a075_s43 should finish within ~1-2h
