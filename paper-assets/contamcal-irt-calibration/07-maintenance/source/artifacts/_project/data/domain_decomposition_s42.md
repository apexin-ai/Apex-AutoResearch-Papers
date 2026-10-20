Per-domain accuracy decomposition (seed=42, d100 vs d000)

| Family | STEM | Humanities | Social Sci | Other |
|--------|------|------------|------------|-------|
| Phi-4 (Immune) | +0.20 | +0.43 | -0.97 | -0.74 |
| Qwen-14B (U-collapse) | -6.79 | -10.05 | -11.18 | -9.40 |
| Qwen-7B (V-recovery) | -1.70 | +0.28 | -3.41 | -3.52 |
| Gemma-2 (Benefit) | +2.66 | +3.93 | +5.04 | +3.41 |
| OLMo-2 (Benefit-sat) | +2.87 | +2.76 | +5.10 | +2.32 |

Key findings:
1. STEM most resilient across all families (smallest |delta|)
2. Social Sciences most sensitive (largest |delta|)
3. Direction by archetype, not domain (no STEM↑/non-STEM↓ crossover)
4. High-baseline models' STEM even more resilient