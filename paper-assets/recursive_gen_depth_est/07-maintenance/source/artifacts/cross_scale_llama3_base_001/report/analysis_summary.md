# cross_scale_llama3_base_001 Analysis

## Experiment Info
- **Model**: Meta-Llama-3.1-8B (BASE, NOT Instruct)
- **Model path**: `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3.1-8B`
- **Strategy**: nucleus_p0.95
- **Data**: 500 samples/depth, d0-d5, seed=42
- **Duration**: ~3.48 hours (22:01 - 00:32 CST, May 16-17 2026)
- **W&B**: None
- **Note**: summary.json incorrectly labels model as "Meta-Llama-3.1-8B-Instruct" (script bug, confirmed BASE from log)

## Key Metrics

### Classification Accuracy
| Task | Accuracy | 95% CI |
|------|----------|--------|
| 4-class (d0-d3) | 0.599 | [0.578, 0.6215] |
| 6-class (d0-d5) | 0.4953 | [0.4773, 0.5133] |

### Consecutive Pairwise Binary AUC (Critical)
| Pair | AUC | Acc | Acc CI |
|------|-----|-----|--------|
| d0v1 | 0.9175 | 0.845 | [0.821, 0.867] |
| d1v2 | 0.7936 | 0.722 | [0.695, 0.749] |
| d2v3 | 0.6815 | 0.644 | [0.615, 0.673] |
| d3v4 | **0.730** | 0.665 | [0.635, 0.692] |
| d4v5 | 0.595 | 0.570 | [0.539, 0.597] |

### EDD Estimate: >5

## Monotonicity Analysis

**AUC sequence**: 0.9175 → 0.7936 → 0.6815 → **0.730** → 0.595

**NOT monotonically decreasing.** d3v4 AUC (0.730) > d2v3 AUC (0.6815), a bump of +0.0485.

## Comparison with Instruct (cross_scale_llama3_8b_003)

| Pair | BASE AUC | Instruct AUC | Δ (I - B) |
|------|----------|--------------|-----------|
| d0v1 | 0.9175 | 0.9494 | +0.032 |
| d1v2 | 0.7936 | 0.8768 | +0.083 |
| d2v3 | 0.6815 | 0.7706 | +0.089 |
| d3v4 | 0.730 | 0.716 | -0.014 |
| d4v5 | 0.595 | 0.6183 | +0.023 |

| Metric | BASE | Instruct |
|--------|------|----------|
| 4-class acc | 0.599 | 0.702 |
| 6-class acc | 0.4953 | 0.554 |
| EDD | >5 | >5 |

**Monotonicity comparison**:
- **Instruct**: 0.9494 > 0.8768 > 0.7706 > 0.716 > 0.6183 — **strictly monotonic** (no U-shape)
- **BASE**: 0.9175 > 0.7936 > 0.6815 < 0.730 > 0.595 — **non-monotonic** bump at d3v4

## Hypothesis Evaluation

**Hypothesis**: "BASE model AUC decay should be monotonic (no U-shape), confirming instruction-tuning causes U-shape in Instruct models."

**Result: CONTRADICTED.**

The data shows the opposite pattern:
1. The Instruct model has strictly monotonic AUC decay (no U-shape)
2. The BASE model has a mild non-monotonic bump at d3v4

However:
- The BASE non-monotonicity (Δ=0.05) is small and may not be statistically significant (no AUC CIs available)
- Neither model shows a "classic U-shape" where late depths become more distinguishable than early-middle depths
- The bump is localized to one pair (d3v4) and the overall trend is still decreasing

## Interpretation

1. **Instruction-tuning does NOT cause U-shape** — Instruct is actually more monotonic than BASE
2. **Instruction-tuning improves depth separability** — Instruct has higher AUC at almost every pair (except d3v4), likely because instruction-tuning produces more structured/distinguishable text at each recursive depth
3. **BASE model shows slight non-monotonicity** — possibly because BASE text at depths 3-4 diverges in different statistical properties (BASE repetition increases non-linearly: rep_4gram goes from 0.165 at d4 to 0.385 at d5, while d3→d4 transition introduces distinctive degeneration patterns)
4. **Both models have EDD >5** — the recursive generation depth estimation framework works for both BASE and Instruct, though BASE has lower absolute separability

## Conclusion

**Classification: NEGATIVE** (hypothesis not supported)

The original hypothesis that instruction-tuning causes U-shaped AUC curves is not supported. In fact, the Instruct model shows cleaner monotonic decay while the BASE model exhibits mild non-monotonicity. The experiment is informative but does not validate the proposed mechanism. The BASE vs Instruct difference is better explained by instruction-tuning producing more structured text that degrades more predictably with recursive depth.
