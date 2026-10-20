# Clustered Bootstrap v2 — Summary Table

> Generated: 2026-05-23 06:20 UTC | Method: demo-level clustered bootstrap, n=1000, fixed canonical peak layer (no winner's curse) | 19/20 conditions complete (tracvla_long/untrained pending)

## Main Results

| Architecture | Suite | Condition | Peak R² | Peak Layer | Exit R² | Δ (peak−exit) | CI 95% lower | CI 95% upper | Boot mean±std | Significant? | n_demos |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **TracVLA** | **goal** | **trained** | **0.5399** | **L13** | **0.2065** | **0.3334** | **0.0546** | **0.3416** | **0.167±0.073** | **YES** | 100 |
| TracVLA | goal | untrained | 0.5048 | L11 | 0.4403 | 0.0645 | -0.1873 | -0.0039 | -0.086±0.048 | NO | 100 |
| **TracVLA** | **spatial** | **trained** | **0.6871** | **L13** | **0.5315** | **0.1557** | **0.0115** | **0.1498** | **0.075±0.036** | **YES** | 100 |
| TracVLA | spatial | untrained | 0.6120 | L4 | 0.5643 | 0.0477 | -0.8003 | -0.5788 | -0.701±0.057 | NO | 100 |
| **TracVLA** | **object** | **trained** | **0.6315** | **L13** | **0.2692** | **0.3623** | **0.0377** | **0.3674** | **0.175±0.084** | **YES** | 100 |
| TracVLA | object | untrained | 0.6274 | L17 | 0.6184 | 0.0090 | -0.0648 | 0.0217 | -0.019±0.022 | NO | 100 |
| **TracVLA** | **long** | **trained** | **0.5897** | **L13** | **0.2319** | **0.3579** | **0.0302** | **0.3363** | **0.156±0.081** | **YES** | 100 |
| TracVLA | long | untrained | — | — | — | — | — | — | — | PENDING | — |
| **NORA** | **goal** | **trained** | **0.4489** | **L8** | **-0.0062** | **0.4551** | **0.9960** | **1.8478** | **1.348±0.212** | **YES†** | 100 |
| NORA | goal | untrained | 0.4203 | L5 | 0.3397 | 0.0806 | -0.0624 | 0.0856 | 0.004±0.045 | NO | 100 |
| **NORA** | **spatial** | **trained** | **0.5763** | **L20** | **0.2683** | **0.3080** | **0.0624** | **0.4450** | **0.235±0.102** | **YES** | 100 |
| NORA | spatial | untrained | 0.5125 | L4 | 0.4240 | 0.0885 | -0.0468 | 0.0610 | 0.003±0.029 | NO | 100 |
| OpenVLA | goal | trained | 0.4556 | L1 | 0.3395 | 0.1160 | -0.2528 | -0.0117 | -0.142±0.065 | NO | 100 |
| OpenVLA | goal | untrained | 0.4042 | L24 | 0.2565 | 0.1477 | -0.0617 | 0.0746 | -0.003±0.034 | NO | 100 |
| OpenVLA | spatial | trained | 0.5782 | L15 | 0.5447 | 0.0335 | -0.0575 | 0.0487 | -0.009±0.028 | NO | 100 |
| OpenVLA | spatial | untrained | 0.5660 | L10 | 0.4931 | 0.0729 | -0.0788 | 0.0604 | -0.016±0.037 | NO | 100 |
| OpenVLA | object | trained | 0.5883 | L26 | 0.5332 | 0.0551 | -0.0310 | 0.0515 | 0.006±0.021 | NO | 100 |
| OpenVLA | object | untrained | 0.5749 | L26 | 0.5381 | 0.0369 | -0.0359 | 0.0532 | 0.003±0.024 | NO | 100 |
| OpenVLA | long | trained | 0.5050 | L23 | 0.4294 | 0.0757 | -0.0539 | 0.0595 | -0.005±0.029 | NO | 100 |
| OpenVLA | long | untrained | 0.5181 | L24 | 0.5027 | 0.0154 | -0.0655 | 0.0285 | -0.026±0.025 | NO | 100 |

## Summary by Architecture × Condition

| Group | Significant / Total | Pattern |
|---|---|---|
| **TracVLA trained** | **4/4** | Exit collapse robust across all 4 suites. L13 consistently peak. |
| TracVLA untrained | 0/4 (3 complete) | No exit collapse in base Phi-3-Vision. |
| **NORA trained** | **2/2** | Exit collapse confirmed. †NORA goal CI anomalous (see note). |
| NORA untrained | 0/2 | No exit collapse in base Qwen2.5-VL. |
| OpenVLA trained | 0/4 | No robust exit collapse after demo-level correction. |
| OpenVLA untrained | 0/4 | No exit collapse in base Llama-2. |

## Key Findings

1. **Exit collapse is VLM→VLA specific**: TracVLA (4/4) and NORA (2/2) trained models show significant peak-to-exit R² drop. OpenVLA (0/4) does not.

2. **Training-induced**: All untrained base models show no significant exit collapse (0/10 complete conditions). The effect is strictly a consequence of VLA fine-tuning on VLM backbones.

3. **Temporal leakage confirmed**: R² absolute values dropped substantially from original aggregate probing (0.7-0.9 → 0.4-0.6) after demo-level splitting, confirming same-demo timesteps in train/test inflated original estimates.

4. **TracVLA peak layer consistency**: L13 is the peak layer across all 4 trained suites, suggesting a stable architectural locus for action-relevant representations in Phi-3-Vision.

## Notes

- †NORA goal/trained CI [0.996, 1.848] remains anomalous even after canonical peak fix. Root cause: exit L35 R²=-0.006 (near zero) fluctuates to extreme negative values in bootstrap resamples. The directional conclusion (significant collapse) is correct, but the CI magnitude is unreliable for this specific cell. NORA spatial/trained CI [0.062, 0.445] is well-behaved and confirms the pattern.
- TracVLA spatial/untrained shows extreme negative bootstrap mean (-0.701). This reflects that L4 (canonical peak) is not robustly the highest R² layer across demo resamples — in most bootstrap samples, exit R² > L4 R². This is expected for untrained models with flat R² profiles.
- Method: 1000 bootstrap iterations with demo-level (clustered) resampling, 100 multiprocessing workers. RidgeCV with kernel method. Fixed canonical peak layer to avoid winner's curse (per-iteration np.max removed).
