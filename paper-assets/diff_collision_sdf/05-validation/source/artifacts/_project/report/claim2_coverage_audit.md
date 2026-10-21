# Claim 2 Evidence Coverage Audit (2026-05-25)

## Coverage Matrix

| Model Family | TSR | CAR | real_CAR | fake_rate | displacement | Episodes | Status |
|---|---|---|---|---|---|---|---|
| Pi0 (A1-SDF) | 0% | 91.5% | ≈0.4% | 99.6% | 0.0027 | 800 | ✅ Complete |
| Pi0 (LoRA baseline) | 0% | 82% | — | Not quantified | 0.01 | 200 | ⚠️ Missing fake_rate |
| Pi0 (Full-FT baseline) | 0.5% | 83% | — | Not quantified | 0.027 | 200 | ⚠️ Missing fake_rate |
| Pi0.5 (baseline) | 73-76% | 25-28% | 0.5% | 98.2% | 0.15 | 600 (3-seed) | ✅ Complete |
| Pi0.5+A1 | ? | ? | ? | ? | ? | — | ⏳ 4 evals RUNNING |
| OpenVLA (base) | — | — | — | — | — | 0 | ❌ No data |

## Critical Gaps (P0)
1. OpenVLA zero-shot eval (in progress, ~5h)
2. Pi0 baseline fake_rate explicit quantification (reanalyze existing data, ~30min)

## Key Weakness
Pi0 and Pi0.5 are same model family (Physical Intelligence). Reviewer can argue this is PI-specific, not universal VLA problem. OpenVLA (7B ViT+LLM, different architecture) is essential.

## Minimum Path
1. Pi0 baseline fake_rate reanalysis (30min, CPU)
2. OpenVLA base eval 200ep (5h, 1 GPU)
3. Unified comparison table script (1-2h, CPU)
