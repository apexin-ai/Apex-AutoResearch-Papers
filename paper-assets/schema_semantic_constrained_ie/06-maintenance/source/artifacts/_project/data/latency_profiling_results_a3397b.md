## Latency Profiling Results

Controlled benchmark: 100 SciERC samples, Qwen3-8B FT checkpoint, single GPU (westd-16980 cuda:0, RTX PRO 6000), CUDA sync precise timing.

| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |
|------|---|----------|---------|---------|---------|----------|-------|
| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |
| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |
| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |
| full_s1 | 100 | 2.655 | 2.416 | 6.162 | 8.449 | +2.3% | 56.4 |

All differences statistically significant (p < 0.0001, paired t-test).

Key findings:
- Full constrained decoding (grammar + semantic) adds only 2.3% latency overhead (61ms/sample)
- Each constraint layer independently contributes ~1-2%
- Combined overhead is sub-additive (1.7% + 1.2% → 2.3%, not 2.9%)
- Practically negligible for production use
