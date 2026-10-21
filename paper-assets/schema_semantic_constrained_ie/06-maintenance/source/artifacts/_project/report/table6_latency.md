# Table 6: Latency Profiling — OntoCoDec Decoding Overhead

Hardware: NVIDIA RTX PRO 6000 (98GB), Qwen3-8B LoRA-merged checkpoint.
Protocol: 100 samples, 5-sample warmup, `torch.cuda.synchronize()` + `time.perf_counter()`, same process sequential runs.

## SciERC (avg output ~150 tokens/sample)

| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |
|------|---|----------|---------|---------|---------|----------|-------|
| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |
| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |
| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |
| **full (OntoCoDec)** | 100 | 2.655 | 2.416 | 6.162 | 8.449 | **+2.3%** | 56.4 |

## DocRED (avg output ~1200 tokens/sample, includes max_tokens=4096 truncations)

| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |
|------|---|----------|---------|---------|---------|----------|-------|
| unconstrained | 100 | 21.023 | 15.588 | 72.882 | 73.522 | — | 56.8 |
| grammar_only | 100 | 21.366 | 15.793 | 74.089 | 74.349 | +1.6% | 55.9 |
| semantic_only | 100 | 21.912 | 15.827 | 75.517 | 75.650 | +4.2% | 55.4 |
| **full (OntoCoDec)** | 100 | 22.147 | 15.993 | 76.289 | 76.418 | **+5.3%** | 54.9 |

## Summary

| Dataset | Full OntoCoDec Overhead | Absolute Cost/Sample |
|---------|------------------------|---------------------|
| SciERC | +2.3% | +61 ms |
| DocRED | +5.3% | +1.12 s |

- Grammar compile time: 44ms (one-time, amortized over all samples)
- All overhead differences statistically significant (p < 0.0001, paired t-test)
- Grammar layer: +1.6–1.7% (token-level FSM constraint check)
- Semantic layer: +1.2–4.2% (DR/CF validation per generated triple)
- Combined overhead sub-additive on SciERC (1.7+1.2→2.3%), near-additive on DocRED (1.6+4.2→5.3%)
- DocRED higher semantic overhead due to larger ontology (96 relation types, complex DR rules) vs SciERC (7 types)
- Practically negligible for both datasets — constraint enforcement costs <6% throughput
