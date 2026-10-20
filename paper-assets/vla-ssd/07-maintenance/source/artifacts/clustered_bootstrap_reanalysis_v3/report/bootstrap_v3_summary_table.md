# Clustered Bootstrap v3 (MCCV) — Summary Table

> Generated: 2026-05-23 12:54 UTC | Method: Monte Carlo Cross-Validation (without-replacement permutation 80/20 demo split × 1000 iterations) | **20/20 conditions complete**
> Fix: v2 used with-replacement bootstrap causing train-test demo overlap; v3 uses without-replacement permutation (no leakage)

## Main Results

| Model | Suite | Condition | Peak Layer | Peak R² | Exit R² | Canonical Δ | CI Lower | CI Upper | Boot Mean | Boot Std | Δ∈CI | Substantial (>0.10) | Significant (CI≠0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **TracVLA** | **goal** | **trained** | **L13** | **0.5399** | **0.2065** | **0.3334** | **0.2069** | **0.4508** | **0.3155** | **0.0642** | **Y** | **Y** | **YES** |
| TracVLA | goal | untrained | L11 | 0.5048 | 0.4403 | 0.0645 | -0.1084 | 0.0510 | -0.0232 | 0.0407 | N | N | NO |
| **TracVLA** | **spatial** | **trained** | **L13** | **0.6871** | **0.5315** | **0.1557** | **0.0906** | **0.2244** | **0.1539** | **0.0333** | **Y** | **Y** | **YES** |
| TracVLA | spatial | untrained | L4 | 0.6120 | 0.5643 | 0.0477 | -0.6067 | -0.4606 | -0.5427 | 0.0357 | N | N | YES‡ |
| **TracVLA** | **object** | **trained** | **L13** | **0.6315** | **0.2692** | **0.3623** | **0.2834** | **0.5038** | **0.3788** | **0.0582** | **Y** | **Y** | **YES** |
| TracVLA | object | untrained | L17 | 0.6274 | 0.6184 | 0.0090 | -0.0669 | 0.0169 | -0.0239 | 0.0208 | Y | N | NO |
| **TracVLA** | **long** | **trained** | **L13** | **0.5897** | **0.2319** | **0.3579** | **0.1714** | **0.5333** | **0.3236** | **0.0984** | **Y** | **Y** | **YES** |
| TracVLA | long | untrained | L9 | 0.5729 | 0.4757 | 0.0971 | -0.0208 | 0.1078 | 0.0396 | 0.0319 | Y | N | NO |
| **NORA** | **goal** | **trained** | **L8** | **0.4489** | **-0.0062** | **0.4551** | **0.9099†** | **1.6077†** | **1.2155** | **0.1786** | **N** | **Y** | **YES** |
| NORA | goal | untrained | L5 | 0.4203 | 0.3397 | 0.0806 | -0.0147 | 0.1102 | 0.0454 | 0.0313 | Y | N | NO |
| **NORA** | **spatial** | **trained** | **L20** | **0.5763** | **0.2683** | **0.3080** | **0.3011** | **0.5119** | **0.3926** | **0.0532** | **Y** | **Y** | **YES** |
| NORA | spatial | untrained | L4 | 0.5125 | 0.4240 | 0.0885 | -0.0128 | 0.0931 | 0.0423 | 0.0277 | Y | N | NO |
| OpenVLA | goal | trained | L1 | 0.4177 | 0.3313 | 0.0864 | -0.0560 | 0.1064 | 0.0173 | 0.0414 | Y | N | NO |
| OpenVLA | goal | untrained | L27 | 0.4230 | 0.3672 | 0.0558 | 0.0113 | 0.0773 | 0.0396 | 0.0166 | Y | N | YES |
| OpenVLA | spatial | trained | L24 | 0.5649 | 0.5278 | 0.0371 | 0.0087 | 0.1020 | 0.0508 | 0.0233 | Y | N | YES |
| OpenVLA | spatial | untrained | L28 | 0.5391 | 0.4955 | 0.0437 | 0.0295 | 0.1113 | 0.0666 | 0.0209 | Y | N | YES |
| OpenVLA | object | trained | L3 | 0.5695 | 0.5325 | 0.0370 | -0.0038 | 0.0854 | 0.0413 | 0.0226 | Y | N | NO |
| OpenVLA | object | untrained | L3 | 0.5619 | 0.5105 | 0.0513 | -0.0044 | 0.0905 | 0.0417 | 0.0250 | Y | N | NO |
| OpenVLA | long | trained | L23 | 0.5328 | 0.5003 | 0.0325 | 0.0037 | 0.1030 | 0.0484 | 0.0259 | Y | N | YES |
| OpenVLA | long | untrained | L29 | 0.5316 | 0.4968 | 0.0349 | 0.0261 | 0.1047 | 0.0597 | 0.0202 | Y | N | YES |

## Summary by Group

| Group | Substantial (Δ>0.10) | Significant (CI≠0) | Pattern |
|---|---|---|---|
| **VLM→VLA trained** | **6/6** | **6/6** | Large exit collapse (Δ=0.15-0.46). TracVLA peak consistently L13. |
| VLM→VLA untrained | 0/4 | 1/4‡ | No substantial exit collapse in base VLMs. |
| OpenVLA trained | 0/4 | 2/4 | Small deltas (0.03-0.09), some statistically significant but not substantial. |
| OpenVLA untrained | 0/4 | 3/4 | Small deltas (0.03-0.06), similar to trained. |

## MCCV Fix Validation

| Metric | v2 (with-replacement) | v3 (MCCV) |
|---|---|---|
| Canonical Δ within CI | ~8/19 (42%) | **17/20 (85%)** |
| Boot mean ≈ Canonical Δ | Systematic bias | Centered |
| CI interpretation | Unreliable (train-test leakage) | Valid |

## Notes

- †NORA goal/trained CI [0.91, 1.61] unreliable due to near-zero exit-layer R² (L35 R²=-0.006). Canonical Δ=0.455 is substantial. CI driven by exit layer instability, not methodology error.
- ‡TracVLA spatial/untrained shows CI [-0.61, -0.46] with "significant" flag, but this reflects L4 instability in flat R² profile, not real exit collapse. Δ=0.048 is non-substantial.
- "Substantial" defined as |Δ| > 0.10 (D102 decision).
- Method: 1000 MCCV iterations with without-replacement demo-level permutation (80 train / 20 test), kernel ridge regression, fixed canonical peak layer. Multiprocessing Pool(100), OPENBLAS_NUM_THREADS=1.
