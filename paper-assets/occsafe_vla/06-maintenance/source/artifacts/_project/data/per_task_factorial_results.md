## Per-Task 2×2 Factorial Analysis Results (v2 only)
## Generated: 2026-05-27 22:28 UTC

### Constrained Tasks Identified (mean CAR < 0.85, SD > 0.05)
- T3: bowl_on_cookie_box (mean=0.363, sd=0.215)
- T5: bowl_on_ramekin (mean=0.111, sd=0.080)
- T6: bowl_next_to_cookie_box (mean=0.453, sd=0.164)

### T3: bowl_on_cookie_box
| Cell | n | Mean | SD |
|------|---|------|----|
| Cell1 GradON+BN | 3 | 0.193 | 0.269 |
| Cell2 GradON+LN | 3 | 0.447 | 0.189 |
| Cell3 GradOFF+BN | 4 | 0.360 | 0.232 |
| Cell4 GradOFF+LN | 1 | 0.700 | N/A |
| Vanilla | 3 | 0.340 | 0.035 |

- gradient_flow: d=-0.165 [CI: -1.43, +1.10]
- norm_type: d=-0.687 [CI: -2.07, +0.70] (LN > BN, medium)
- Interaction: +0.087
- Best OCC vs Vanilla: Cell4=0.700 vs 0.340 (Δ=+0.360)

### T5: bowl_on_ramekin
| Cell | n | Mean | SD |
|------|---|------|----|
| Cell1 GradON+BN | 3 | 0.153 | 0.110 |
| Cell2 GradON+LN | 3 | 0.187 | 0.070 |
| Cell3 GradOFF+BN | 4 | 0.080 | 0.043 |
| Cell4 GradOFF+LN | 1 | 0.100 | N/A |
| Vanilla | 3 | 0.040 | 0.035 |

- gradient_flow: d=+1.251 [CI: -0.13, +2.63] (ON > OFF, large)
- norm_type: d=-0.962 [CI: -2.38, +0.46] (LN > BN, large)
- Interaction: -0.013
- Best OCC vs Vanilla: Cell2=0.187 vs 0.040 (d=+2.648)

### T6: bowl_next_to_cookie_box
| Cell | n | Mean | SD |
|------|---|------|----|
| Cell1 GradON+BN | 3 | 0.340 | 0.216 |
| Cell2 GradON+LN | 3 | 0.500 | 0.092 |
| Cell3 GradOFF+BN | 4 | 0.495 | 0.194 |
| Cell4 GradOFF+LN | 1 | 0.680 | N/A |
| Vanilla | 3 | 0.387 | 0.070 |

- gradient_flow: d=-0.415 [CI: -1.69, +0.86]
- norm_type: d=-0.393 [CI: -1.76, +0.97]
- Interaction: +0.025
- Best OCC vs Vanilla: Cell4=0.680 vs 0.387 (Δ=+0.293)

### Summary
| Task | d(grad) | d(norm) | Interaction | BestOCC | Vanilla | Δ |
|------|---------|---------|-------------|---------|---------|---|
| T3 | -0.16 | -0.69 | +0.087 | 0.700 | 0.340 | +0.360 |
| T5 | +1.25 | -0.96 | -0.013 | 0.187 | 0.040 | +0.147 |
| T6 | -0.41 | -0.39 | +0.025 | 0.680 | 0.387 | +0.293 |

### Constrained Tasks Aggregate
| Cell | Mean |
|------|------|
| Cell4 GradOFF+LN | 0.493 |
| Cell2 GradON+LN | 0.378 |
| Cell3 GradOFF+BN | 0.312 |
| Vanilla | 0.256 |
| Cell1 GradON+BN | 0.229 |
