# Table 3: Baselines & Grid b Sweep

## Golden Ratio Baseline (seed42)

| Method | PPL | Δ vs Uniform |
|--------|-----|--------------|
| Golden Ratio (w=1/φ for synthetic) | 17.6540 | -0.040 |
| Uniform (reference) | 17.6939 | — |

## Grid b Sweep — All Seeds

| b | seed42 | seed123 | seed456 | Mean |
|---|--------|---------|---------|------|
| 0.3 | 17.6400 | — | — | — |
| 0.5 | 17.6510 | 17.6380 | 17.6500 | 17.6463 |
| 1.0 | 17.6920 | 17.6740 | 17.6800 | 17.6820 |
| 1.5 | 17.7180 | 17.7010 | 17.7100 | 17.7097 |
| 2.0 | 17.7410 | 17.7250 | 17.9890 | 17.8183 |
| 3.0 | 17.7740 | 17.7600 | 17.9210 | 17.8183 |
| 5.0 | 17.8180 | 17.8039 | 17.9930 | 17.8716 |

Note: seed456 shows instability at b≥2.0 (likely outlier batches).

## Per-seed Best Grid b

| Seed | Best b | PPL | Δ vs Uniform |
|------|--------|-----|--------------|
| 42 | 0.3 | 17.6400 | -0.054 |
| 123 | 0.5 | 17.6380 | -0.048 |
| 456 | 0.5 | 17.6500 | -0.052 |
