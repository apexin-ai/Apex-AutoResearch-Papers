# Q3: Trace Component Decomposition — Scale Effect Analysis

## Main Comparison: Qwen-7B vs Qwen-1.5B

| Condition | Qwen-7B | Qwen-1.5B | Δ (7B−1.5B) | Seeds |
|-----------|---------|-----------|-------------|-------|
| exception_only | 99.83 | 99.83 | **0.00** | 3/3 |
| ae_only | 99.92 | 98.83 | +1.09 | 1/2 |
| loop_only | 85.63 | 79.54 | **+6.09** | 1/3 |
| vota (all components) | 99.25 | 99.54 | −0.29 | 2/2 |
| full_trace (raw) | 81.43 | 77.06 | +4.37 | 3/1 |
| no_trace | 75.13 | 72.35 | +2.78 | 1/3 |

> Qwen-1.5B no_trace seed variance large: 67.31/75.88/73.87 (σ≈3.6pp). Other conditions stable.

## Cross-Model Component Comparison (seed42 or best available)

| Condition | Qwen-7B | DeepSeek-6.7B | Qwen-1.5B | CodeLlama-13B |
|-----------|---------|---------------|-----------|---------------|
| exception_only | 99.83 | 99.33 | 99.83 | 99.89 |
| ae_only | 99.92 | 98.74 | 99.08 | 99.08 |
| loop_only | 85.63 | 81.26 | 79.54 | 77.06 |
| no_trace | 75.13 | 73.36 | 72.35 | 76.50 |

## Key Findings

1. **Tier 1 ceiling confirmed across scales**: exception_only (≥99.3%) and ae_only (≥98.7%) are essentially solved for all 4 models. Scale has negligible impact on high-information-density components.

2. **Scale effect concentrates on loop_only**: The only component where scale matters is loop_only — 7B leads at 85.63%, followed by DeepSeek-6.7B (81.26%), Qwen-1.5B (79.54%), CodeLlama-13B (77.06%). Note: CodeLlama-13B (13B params) underperforms Qwen-1.5B, indicating architecture/pretraining matters more than raw parameter count.

3. **Information density hierarchy preserved at 1.5B**: exception(99.83) ≈ ae(98.83) >> loop(79.54) >> no_trace(72.35). The tier structure is scale-invariant; only the gap between tiers changes.

4. **vota neutralizes scale**: With all structured components combined, 1.5B (99.54%) matches 7B (99.25%). The structured representation eliminates the capacity advantage.

## Missing Data

- Qwen-1.5B full_trace: single seed only (77.06%)
- Qwen-1.5B vota: 2 seeds (vs 7B's 2 seeds)
- No full_trace multi-seed for cross-model comparison
