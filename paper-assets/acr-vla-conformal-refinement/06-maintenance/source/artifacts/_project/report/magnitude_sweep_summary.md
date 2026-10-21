# Magnitude Sweep Summary (2026-05-16)

## Spatial Benchmark (DONE points only)

| norm | obs_only | perdof | gap | obs_only status | perdof status |
|------|----------|--------|-----|-----------------|---------------|
| 0.03 | — | 30.0% | — | 7/10 RUNNING | 10/10 DONE |
| 0.05 | 35.0% | 31.0% | +4.0pp | 10/10 DONE | 10/10 DONE |
| 0.10 | 35.0% | 35.0% | 0pp | 10/10 DONE | 10/10 DONE |
| 0.20 | 35.0% | — | — | 10/10 DONE | killed (6/10 partial 28.3%) |
| 0.30 | 36.0% | 26.0% | +10pp | 10/10 DONE | 10/10 DONE |

**Key finding**: obs_only stable 35-36% across [0.05, 0.30]. perdof peaks at 0.10 (35%) and collapses to 26% at 0.30 (-9pp).

Baselines: argmin 34%, VLA-only 30%, VLA-mean 32%.

## Object Benchmark (in progress)

| norm | obs_only | perdof | status |
|------|----------|--------|--------|
| 0.03 | RUNNING (2/10) | RUNNING (1/10) | bjb1-32546, bjb2-28827 |
| 0.05 | RUNNING (2/10) | RUNNING (1/10) | bjb2-28827 |
| 0.10 | **19.0% FINAL** | **11.0% FINAL** | from main eval experiments |
| 0.20 | **22.0% FINAL** | RUNNING (2/10) | obs_only done, perdof on bjb1-32546 |
| 0.30 | RUNNING (2/10) | RUNNING (0/10) | bjb2-28827 |

Baselines: argmin 12%, VLA-only 12%, VLA-mean 12%.

**obs_only 0.2 > obs_only 0.1** (22% vs 19%, +3pp): suggests moderate correction magnitude may be optimal for object.

## Narrative for Paper

1. **obs_only is robust to norm scaling**: spatial 35-36% across 6× range [0.05, 0.30]; object 19-22% at [0.1, 0.2]
2. **perdof is fragile**: spatial peaks at 0.10 (35%), drops to 26% at 0.30; object 11% at 0.10
3. **Unbounded correction (norm≈1.42) is catastrophic for perdof (0% SR), while obs_only remains robust at 17%, still above the argmin baseline (12%)**: this contrast is the strongest evidence that obs_only's learned correction is inherently safe even without norm clipping
4. **Safe operating range**: ε ∈ [0.05, 0.2] for obs_only; ε = 0.1 only for perdof
