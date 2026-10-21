# Framework Diagnostic Summary

Cross-environment comparison demonstrating the framework diagnoses different routing mechanisms in different environments.

## Summary Table

| Metric | ScienceWorld | ALFWorld | MATH |
|--------|-------------|----------|------|
| Environment type | Text sim (irreversible failure) | Text sim (no death) | Static reasoning |
| Death mechanism | Yes (P=-100) | No | No |
| N episodes | 245 | 135 | 300 |
| Internal DR | 42.9% | 0% | N/A |
| Deterministic DR | 16.3% | 0% | N/A |
| ΔDR (pp) | +26.5 | 0 | N/A |
| DAF | 90.4% [81.1, 99.0] | 0% (no deaths) | N/A |
| Death-asymmetry labels | 78.9% | 0% | 0% |
| Det-preferred % | 35.1% (86/245) | 25.9% (35/135) | 3.0% (9/300) |
| Int-preferred % | 3.7% (9/245) | 1.5% (2/135) | 8.3% (25/300) |
| No-preference % | 61.2% (150/245) | 72.6% (98/135) | 88.7% (266/300) |
| Dominant routing mechanism | Death avoidance | Information asymmetry | No signal (p=0.81) |
| Model | Qwen2.5-7B-Instruct | Qwen2.5-7B-Instruct | Qwen2.5-7B-Instruct |

## Interpretation

The framework correctly identifies:
1. **ScienceWorld**: Death avoidance accounts for 90.4% of routing signal. The deterministic strategy's advantage comes almost entirely from avoiding fatal actions.
2. **ALFWorld**: With no death mechanism, routing signal (25.9% det-preferred) comes entirely from information asymmetry — deterministic mode provides admissible action lists that resolve vocabulary mismatch.
3. **MATH**: No significant routing signal exists (McNemar p=0.81). Internal (chain-of-thought) slightly outperforms deterministic (code execution), but the difference is not directionally consistent enough to train a router.

## Cross-Model Replication (ScienceWorld only)

| Model | N | Int DR | Det DR | ΔDR | DAF |
|-------|---|--------|--------|-----|-----|
| Qwen2.5-7B | 245 | 42.9% | 16.3% | +26.5pp | 90.4% |
| Llama-3.1-8B | 220 | 41.4% | 11.4% | +30.0pp | 88.2% |
| Qwen2.5-72B | 255 | 30.6% | 2.75% | +27.8pp | 92.4% |
