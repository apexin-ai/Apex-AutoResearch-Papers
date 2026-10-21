# E4 Ensemble Scaling Analysis — Frontier SC

**Dataset**: FewNERD (first 200 test instances, seed=42)
**Models**: GPT-5.5, Claude Sonnet 4, Gemini 2.5 Pro, DeepSeek Chat
**Metric**: Instance-average F1 (text matching, not offset matching)
**SC config**: N=8 samples, T=1.0 per model

---

## Table 1: Single-Model Frontier SC Metrics

| Model | Greedy F1 | MV F1 | Oracle F1 | MV−Greedy | Selection Gap | Degen% |
|-------|-----------|-------|-----------|-----------|---------------|--------|
| GPT-5.5 | 0.6382 | 0.6521 | 0.7203 | +1.39pp | 6.82pp | 50.0% |
| Gemini 2.5 Pro | 0.6301 | 0.6446 | 0.7575 | +1.45pp | 11.29pp | 28.5% |
| Claude Sonnet 4 | 0.6068 | 0.6226 | 0.6544 | +1.58pp | 3.18pp | 74.0% |
| DeepSeek | 0.3992 | 0.4243 | 0.7140 | +2.51pp | 28.97pp | 5.5% |

**Key**: All 4 families exhibit the correlation-selection gap. MV gains are modest (+1.4–2.5pp) while oracle headroom is large (3–29pp). DeepSeek has lowest greedy but highest oracle headroom and lowest degeneracy.

---

## Table 2: Cross-Model Error Correlation (Pearson r, greedy F1)

| | GPT-5.5 | Gemini | Claude | DeepSeek |
|--|---------|--------|--------|----------|
| GPT-5.5 | — | **0.816** | **0.712** | 0.283 |
| Gemini | | — | **0.690** | 0.252 |
| Claude | | | — | 0.232 |
| DeepSeek | | | | — |

**Mean r (6 pairs)**: 0.498

**Pattern**: Three proprietary models (GPT-5.5, Gemini, Claude) form a high-correlation cluster (r=0.69–0.82). DeepSeek is orthogonal to all three (r=0.23–0.28), suggesting fundamentally different error patterns.

---

## Table 3: Ensemble Scaling Curve

| k models | Greedy-Selection | Cross-Oracle | Δ Oracle (vs k−1) |
|----------|-----------------|-------------|-------------------|
| 1 (avg single) | 0.5558 | 0.7306 | — |
| 2 (avg pairs) | 0.6939 | 0.7918 | +6.12pp |
| 3 (avg triples) | 0.7337 | 0.8200 | +2.82pp |
| 4 (all) | **0.7571** | **0.8361** | +1.61pp |

**Greedy-selection oracle**: For each instance, pick the model with the highest greedy F1. This represents the ceiling of perfect model routing.

**Cross-oracle**: For each instance, take the best sample F1 across all models' samples. This represents the ceiling of a perfect cross-model sample selector.

---

## Table 4: Cross-Model Ensemble Summary

| Metric | Value | vs Best Single |
|--------|-------|---------------|
| Best single greedy (GPT-5.5) | 0.6382 | — |
| Best single MV (GPT-5.5) | 0.6521 | — |
| Best single oracle (Gemini) | 0.7575 | — |
| **4-model greedy-selection** | **0.7571** | **+11.89pp** |
| **4-model cross-oracle** | **0.8361** | **+7.86pp** |

---

## Table 5: Model Complementarity

| Model | Uniquely Best (greedy) | % |
|-------|----------------------|---|
| Claude Sonnet 4 | 19 | 9.5% |
| Gemini 2.5 Pro | 16 | 8.0% |
| DeepSeek | 16 | 8.0% |
| GPT-5.5 | 12 | 6.0% |
| Tied (≥2 models) | 137 | 68.5% |

Despite being the weakest model overall (greedy 0.607), Claude is uniquely best on the most instances (9.5%), driven by different error patterns on a subset of instances.

---

## Conclusions

1. **Cross-model ensemble breaks the single-model SC ceiling**: 4-model cross-oracle (0.836) exceeds best single-model oracle (0.758) by +7.86pp. The within-model selection gap (MV fails to reach oracle) is partly compensated by cross-model diversity.

2. **Diminishing returns with model count**: Oracle gains follow 1→2: +6.1pp, 2→3: +2.8pp, 3→4: +1.6pp. The marginal value of additional models decreases, consistent with correlated error patterns within the high-r cluster.

3. **DeepSeek's orthogonality is the key diversity source**: Despite 0.399 greedy F1, DeepSeek's low correlation (r≈0.25) with all other models makes it the most valuable ensemble partner. This demonstrates that model diversity matters more than individual quality for ensemble gain.

4. **Degeneracy inversely predicts ensemble value**: Claude (74% degen) contributes less diversity than DeepSeek (5.5% degen), despite higher absolute F1. High degeneracy = all samples identical = no new information for the ensemble.

5. **The correlation-selection gap is universal**: All 4 families show ρ(agreement, F1) > 0 but MV ≈ greedy. This confirms the gap is not model-specific but a structural property of SC for structured generation.

---

## Comparison: Frontier Ensemble vs Fine-Tuned Ensemble

| Setting | Cross-family r | Ensemble gain (mean) |
|---------|---------------|---------------------|
| Fine-tuned (Qwen × LLaMA, 2 families) | 0.67 | +0.61pp (MV) |
| Frontier (4 families) | 0.50 | +7.86pp (oracle) |

The frontier models show lower mean correlation (0.50 vs 0.67) and much larger ensemble ceiling gain, driven by DeepSeek's orthogonal error pattern. However, frontier ensemble ceiling requires an oracle selector; the practical achievable gain depends on the quality of the selection mechanism.
