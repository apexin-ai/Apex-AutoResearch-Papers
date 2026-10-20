# Qwen Cross-Model Experiment Status Check

**Time**: 2026-05-14 ~15:20 UTC (processes running ~2.5 hours)
**Server**: westd-22162

## Process Status

| Experiment | PID | GPU | Status | Problems | Uptime |
|------------|-----|-----|--------|----------|--------|
| s015 (sparsity=0.15) | 68738 | cuda:0 | **ALIVE** | 4/50 started (on #4) | 02:27 |
| s020 (sparsity=0.20) | 68880 | cuda:1 | **ALIVE** | 4/50 started (on #4) | 02:25 |
| s025 (sparsity=0.25) | 69023 | cuda:2 | **ALIVE** | 2/50 started (on #2) | 02:23 |
| s030 (sparsity=0.30) | 69272 | cuda:3 | **ALIVE** | 2/50 started (on #2) | 02:21 |

## GPU Utilization

| GPU | Model | Utilization | Memory Used | Memory Total |
|-----|-------|-------------|-------------|--------------|
| 0 | RTX PRO 6000 Blackwell | 78% | 26,687 MiB | 97,887 MiB |
| 1 | RTX PRO 6000 Blackwell | 80% | 26,687 MiB | 97,887 MiB |
| 2 | RTX PRO 6000 Blackwell | 90% | 58,644 MiB | 97,887 MiB |
| 3 | RTX PRO 6000 Blackwell | 90% | 55,932 MiB | 97,887 MiB |

## Observations

- **All 4 experiments alive and actively computing** (high GPU utilization confirms).
- **Output directories empty** — no result files written yet (likely writes at end or per-batch).
- **Progress is extremely slow**: ~1-1.5 problems/hour. At this rate:
  - s015/s020: ~33-40 hours to complete 50 problems
  - s025/s030: ~50-100 hours to complete 50 problems
- **GPU 2/3 use 2x more memory** than GPU 0/1 (58-59 GB vs 27 GB), possibly due to higher sparsity computation overhead.
- **NaN attention layer 27** warning appears for all experiments (non-fatal, skipped automatically).
- Registry stuck at ALLOCATED status is cosmetic — processes are actually running fine.

## Concern

The per-problem processing time (~30-75 min) means 50 problems will take **1.5-4 days** per experiment. The importance masking method on Qwen2.5-7B-Instruct is far more expensive than expected. Consider whether `max_problems` can be reduced or if the computation can be optimized.
