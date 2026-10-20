# Exp-009: SICA Pipeline Overhead Analysis

**Source**: exp-001 (sica_expanded_14b), 804 problems, Qwen2.5-14B via vLLM, K=12  
**Total wall time**: 49,559s (826 min / 13.8h)  
**All 804 problems have complete per-stage timing data.**

## Stage Breakdown

| Stage | Mean | Median | P95 | Total | % of Total |
|-------|------|--------|-----|-------|------------|
| Trace Generation (vLLM, K=12) | 31.6s | 31.2s | 46.7s | 25,420s (423.7min) | 51.3% |
| Constraint Extraction (LLM) | 29.0s | 29.3s | 46.9s | 23,295s (388.3min) | 47.0% |
| Deduplication (embeddings) | 1.0s | 0.8s | 2.3s | 805s (13.4min) | 1.6% |
| MaxSAT Solving (Z3) | 0.003s | 0.003s | 0.004s | 2.1s | ~0% |

## Key Finding: Overhead Ratio

- **SC baseline** (trace generation only): **423.7 min**
- **SICA extra overhead** (extraction + dedup + MaxSAT): **401.7 min**
- **Overhead ratio**: **+94.8%** wall time over SC baseline
- Per-problem overhead: mean 30.0s, median 30.3s, P95 47.7s

## Is the Overhead Worth It?

**Cost**: SICA nearly doubles wall time (+94.8%) vs. SC.

**Benefit**: SICA accuracy 76.49% vs. SC 76.24% = **+0.25pp** on this benchmark. Only 2 net problems flipped (615 vs 613 correct).

**Verdict**: At current accuracy gain, the overhead is **not justified** for this benchmark/model combination. The constraint extraction stage (47% of total time) dominates the overhead — it's essentially another full inference pass. The symbolic stages (dedup + MaxSAT) are negligible (<2%).

## Optimization Opportunities

1. **Constraint extraction is the bottleneck** — uses same LLM for extraction as for trace generation. Batching or a smaller extraction model could cut this ~50%.
2. **Dedup + MaxSAT are already fast** — no optimization needed (1.6% combined).
3. **Pipeline parallelism** — extraction could start as soon as each trace completes, overlapping with trace generation. Theoretical speedup: ~30% if extraction runs in parallel with later traces.

## Per-Dataset Breakdown

| Dataset | N | Mean Total | Mean Overhead | Overhead % |
|---------|---|-----------|---------------|------------|
| ProofWriter (D5) | 600 | 65.6s | 33.6s | 51.3% |
| FOLIO | 204 | 49.8s | 19.2s | 38.6% |

ProofWriter has higher overhead because longer traces produce more constraints to extract. FOLIO's shorter traces yield less extraction work.

## Time Distribution

**Per-problem total time** (83% of problems fall in 40-100s):
- 0-20s: 4 (0.5%)
- 20-40s: 125 (15.5%)
- 40-60s: 231 (28.7%)
- 60-80s: 268 (33.3%)
- 80-100s: 172 (21.4%)
- 100-150s: 4 (0.5%)

**Per-problem overhead** (extraction+dedup+maxsat):
- 0-10s: 56 (7.0%)
- 10-20s: 152 (18.9%)
- 20-30s: 188 (23.4%)
- 30-50s: 406 (50.5%)
- 50-100s: 2 (0.2%)

## Validation

- 804/804 problems have timing data (0 missing)
- Sum of per-problem `total_s` = 49,522s ≈ reported wall time 49,559s (0.07% difference — within tolerance)
