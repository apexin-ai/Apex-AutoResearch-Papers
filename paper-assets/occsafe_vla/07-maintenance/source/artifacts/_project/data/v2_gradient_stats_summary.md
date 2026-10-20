V2 Gradient Analysis Results (5 conditions, 10894:cuda:3, 2026-05-27)

| Condition | Action Loss | OCC Loss | Action Grad Norm | OCC Grad Norm | OCC/Action Ratio | Mean Cosine | Cosine Range | Conflict Rate |
|-----------|-----------|----------|-----------------|--------------|-----------------|-------------|-------------|---------------|
| Vanilla v2 | 0.2285 | 0.0000 | 0.1716 | N/A | N/A | N/A | N/A | N/A |
| Full OCC BN v2 | 0.2541 | 0.0108 | 0.1410 | 0.0210 | 14.9% | +0.0065 | [-0.0006, +0.021] | 45.6% |
| Full OCC LN v2 | 0.2318 | 0.0102 | 0.1340 | 0.0187 | 13.9% | +0.0045 | [-0.002, +0.013] | 45.7% |
| Detach BN v2 | 0.2473 | 0.0121 | 0.1419 | 0 (detached) | N/A | N/A | N/A | N/A |
| Detach LN v2 | 0.2428 | 0.0109 | 0.1346 | 0 (detached) | N/A | N/A | N/A | N/A |

Key conclusions:
1. Cosine ≈ 0: Confirms gradient orthogonality (action vs auxiliary)
2. Conflict rate ~46%: No directional conflict (near 50% random baseline)
3. Full OCC ≈ Detach action grad norm: No gradient amplification from auxiliary head
4. OCC grad norm ~14% of action: Auxiliary task does not dominate backbone updates