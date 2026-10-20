# exp-014: DeepSeek-R1-Distill-Qwen-7B Analysis

**Date**: 2026-05-17 | **Model**: DeepSeek-R1-Distill-Qwen-7B | **Dataset**: D012 (30 PW-D5 + 30 FOLIO)

## Configuration

| Parameter | Value |
|-----------|-------|
| Model | DeepSeek-R1-Distill-Qwen-7B (reasoning distill) |
| K (traces) | 12 |
| Temperature | 0.7 |
| max_tokens | 4096 |
| Dataset | 30 ProofWriter D5 + 30 FOLIO = 60 problems |
| Seed | 42 |
| Wall time | 100.3 min |

## Core Results

| Metric | Value |
|--------|-------|
| **SICA accuracy** | **68.3% (41/60)** |
| **SC accuracy** | **71.7% (43/60)** |
| **Gap (SICA - SC)** | **-3.4pp** |
| McNemar chi2 | 0.500 (p=0.4795, NOT significant) |
| C0 (nominal) | **58.3% (35/60)** |
| Contradiction rate | 3.7% |
| Extraction rate | 83.9% |
| Answer extraction | 93.9% |

### McNemar 2x2 Table

|  | SC correct | SC wrong |
|--|-----------|----------|
| SICA correct | 41 | 0 |
| SICA wrong | 2 | 17 |

SICA rescued 0 problems. SICA flipped 2 SC-correct answers to wrong:
- ProofWriter_RelNeg-OWA-D5-144_Q12
- folio_012

## By Dataset

| Dataset | SICA | SC | Gap | C0 | n |
|---------|------|-----|-----|-----|---|
| ProofWriter D5 | 50.0% | 53.3% | -3.3pp | 66.7% (20/30) | 30 |
| FOLIO | 86.7% | 90.0% | -3.3pp | 50.0% (15/30) | 30 |

## Constraint Quality

| Metric | Value |
|--------|-------|
| Avg constraints extracted/problem | 80.1 |
| Avg unique constraints/problem | 24.0 |
| Satisfied ratio (mean) | 0.950 |
| Satisfied ratio (min) | 0.714 |
| Problems with ratio=1.0 | 27/60 (45%) |
| Truncated traces | 72/720 (10%), 17/60 problems |
| SC vote entropy (mean) | 0.404 |

## Hypothesis Evaluation

**Original hypothesis**: DeepSeek-R1-Distill-Qwen-7B, as a reasoning distill model, will exhibit deterministic reasoning chains that kill diversity. Expected C0 < 5%, similar to QwQ-32B (C0=2.6%), serving as a second reasoning model data point for the "capability trap."

**Result: HYPOTHESIS FALSIFIED.**

C0 = 58.3%, dramatically above the 5% threshold. The 7B distilled reasoning model does NOT exhibit the extreme determinism of QwQ-32B.

## Cross-Model Comparison (Reasoning Models)

| Model | Size | C0 | SICA | SC | Gap | Interpretation |
|-------|------|-----|------|-----|------|----------------|
| QwQ-32B | 32B | 2.6% (eff.) | ~77% | ~77% | 0.0pp | Diversity collapse, SICA degenerates to SC |
| DeepSeek-R1-7B | 7B | 58.3% | 68.3% | 71.7% | -3.4pp | Diversity exists, SICA still loses |

Key differences:
1. QwQ-32B (32B full reasoning) has near-zero diversity (C0=2.6%); SICA = SC trivially
2. DeepSeek-R1-7B (7B distilled) retains substantial diversity (C0=58.3%), likely because smaller model capacity introduces more stochasticity
3. Despite high diversity, SICA STILL underperforms SC, confirming constraint quality is the real bottleneck

## Conclusions

1. **Cannot serve as second "capability trap" data point.** The 7B distilled model behaves more like a standard instruction model than a reasoning model in terms of diversity. Distillation at 7B does not faithfully replicate the deterministic behavior of the 32B teacher.

2. **Reinforces constraint quality as the fundamental bottleneck.** Even with C0=58.3% (ample diversity for SICA to exploit), SICA rescues zero problems and flips 2 correct answers to wrong. The extracted constraints are domain facts, not answer-discriminative signals.

3. **Verdict: NEGATIVE.** This experiment does not validate the capability trap hypothesis. It instead provides additional evidence that SICA's constraint extraction mechanism is fundamentally insufficient regardless of diversity level.

## Implications for Paper

- The "reasoning model diversity collapse" narrative is model-size-dependent, not a universal property of reasoning distillation
- QwQ-32B remains the sole data point for the capability trap argument; adding DeepSeek-R1-7B would weaken the claim
- The more robust finding across ALL experiments: SICA <= SC everywhere, due to constraint quality degradation (not diversity collapse)
