# Diagnosis: exp-062 & exp-065 false failure

**Date**: 2026-05-19  
**Server**: westd-25068  
**Verdict**: Both experiments completed successfully. Cron monitoring false positive.

## exp-062 (Gemma-3-27B-IT, FOLIO 204, cuda:3)

**Status**: COMPLETED  
**Results**:
- SICA accuracy: **80.4%** (164/204)
- SC accuracy: **80.9%** (165/204)
- Extraction rate: 99.8%
- Contradiction rate: 1.1% (45/204 problems)
- Total wall time: 357.4 min

**Log tail** (`exp062_gemma27b_folio204.log`):
```
SICA: True (X)
  Constraints: 75 extracted -> 25 unique
  MaxSAT: 25 sat, 0 excl, solve=0.67ms
  Timing: trace=18.4s extract=72.8s total=91.5s
SC:   True (X) -- votes: 12/12
Time: 91.5s

================================================================================
FULL MVP EXPERIMENT RESULTS
================================================================================
Problems: 204
SICA accuracy: 80.4% (164/204)
SC accuracy:   80.9% (165/204)
...
Total wall time: 357.4 min
Results saved to results/exp062_gemma27b_folio204/exp062_results.json
FULL_MVP_DONE
```

**Output files**:
- `exp062_results.json` (294KB)
- `exp062_gemma27b_folio204.log` (657KB)
- `intermediates/` directory populated
- `per_trace_constraints/` directory populated

## exp-065 (Qwen2.5-7B-Instruct, ProofWriter 600, cuda:0)

**Status**: COMPLETED  
**Results**:
- SICA accuracy: **68.0%** (408/600)
- SC accuracy: **72.0%** (432/600)
- Extraction rate: 99.7%
- Contradiction rate: 2.3% (288/600 problems)
- Total wall time: 340.4 min

**Log tail** (`exp065_run.log`):
```
SICA: Unknown (X)
  Constraints: 114 extracted -> 28 unique
  MaxSAT: 26 sat, 2 excl, solve=0.99ms
  Timing: trace=6.5s extract=18.0s total=25.0s
SC:   False (V) -- votes: 5/12
Time: 25.0s

================================================================================
FULL MVP EXPERIMENT RESULTS
================================================================================
Problems: 600
SICA accuracy: 68.0% (408/600)
SC accuracy:   72.0% (432/600)
...
Total wall time: 340.4 min
Results saved to results/exp065_qwen7b_pw600/exp065_results.json
FULL_MVP_DONE
```

**Output files**:
- `exp065_results.json` (1MB)
- `exp065_run.log` (1.9MB)

## Root Cause of False Failure

Cron monitoring detected both `exp062_run` and `exp065_run` tmux sessions as dead (5 consecutive checks). However:

1. The sessions exited **normally** after the experiments completed (`FULL_MVP_DONE` printed)
2. No sentinel files were written by the experiment code
3. No W&B logging was configured

The cron relied on process liveness + sentinel/W&B as completion signals. Since only the vLLM server sessions persist after completion (and `exp065_vllm` was already cleaned up), the run sessions' natural exit was misinterpreted as failure.

## GPU State at Diagnosis Time (22:59 UTC)

| GPU | Status | Memory | Process |
|-----|--------|--------|---------|
| 0 | Idle | 0MiB / 97887MiB | - |
| 1 | Active | 90241MiB / 97887MiB | exp071 vLLM |
| 2 | Idle | 0MiB / 97887MiB | - |
| 3 | Residual | 88115MiB / 97887MiB | exp062 vLLM (stale) |

## Action Items

1. Correct exp-062 and exp-065 registry status from `failed` to `completed`
2. Kill stale `exp062_vllm` tmux session to free GPU 3
3. Future experiments should write a sentinel file on completion to prevent false failure detection
