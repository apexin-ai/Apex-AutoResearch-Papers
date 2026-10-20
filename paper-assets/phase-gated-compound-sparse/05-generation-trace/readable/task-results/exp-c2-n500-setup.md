# exp c2 n500 setup

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_c2-n500-setup_20260514T133447_result.json`
- **Structured JSON:** [`7850d142067814b1523a.json`](../../sessions/78/7850d142067814b1523a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments running and processing problems:
- **GPU 0** (importance): [2/500], 36GB VRAM used  
- **GPU 1** (random): [4/500], 18GB VRAM used

Summary of what was done:

1. **Code exploration**: Found actual package at `pacs/pacs/profiling/run_profiling.py` (not the outer copy). Already has bf16, `per_problem_ii`, `--max_problems`.

2. **Code modifications** to `pacs/pacs/profiling/run_profiling.py`:
   - Fixed data loading: when `--max_problems > 50`, bypasses `stratified_sample_math500()` and uses all 500 problems
   - Added `--gpu` arg for CUDA device selection
   - Device selection uses `cuda:{gpu}` when specified

3. **Pre-registration** created at `PRE_REGISTRATION_C2.md` with hypothesis, decision rule (QW s015 CI crossing zero → threshold narrative), and analysis plan.

4. **Launched 8 conditions** across 2 GPUs:
   - tmux `c2_n500_gpu0`: importance × {s015, s020, s025, s030} sequential on cuda:0
   - tmux `c2_n500_gpu1`: random × {s015, s020, s025, s030} sequential on cuda:1

5. **Registry** updated: `c2_n500_deepseek` → RUNNING

Estimated wall clock: ~20 hours total (4 conditions × ~5h each per GPU, 2 GPUs parallel).

---
