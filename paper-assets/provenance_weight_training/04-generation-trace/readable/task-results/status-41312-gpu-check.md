# status 41312 gpu check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_41312_gpu_check_20260518T093040_result.json`
- **Structured JSON:** [`0ef79ec18f5123c272d0.json`](../../sessions/0e/0ef79ec18f5123c272d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results Summary

### GPU Status (4x NVIDIA RTX PRO 6000 Blackwell, 98GB each)

| GPU | Utilization | Memory | Process PID | Experiment |
|-----|------------|--------|-------------|------------|
| 0 | 94% | 46.5/97.9 GB | 181818 | contamination_60_ess_only_seed123 |
| 1 | 97% | 46.5/97.9 GB | 182193 | contamination_60_ess_only_seed456 |
| 2 | 100% | 46.5/97.9 GB | 183255 | contamination_60_random_seed123 |
| 3 | 100% | 46.5/97.9 GB | 183337 | contamination_60_random_seed456 |

### Running Experiments (ρ=0.6 cross-seed, 6103 total steps)

| Experiment | GPU | Step | Progress | CPU Time | Started | ETA |
|------------|-----|------|----------|----------|---------|-----|
| contamination_60_ess_only_seed123 | 0 | 5424/6103 | **88.9%** | 191 min | 14:19 | ~24 min |
| contamination_60_ess_only_seed456 | 1 | 5427/6103 | **88.9%** | 191 min | 14:20 | ~24 min |
| contamination_60_random_seed123 | 2 | 4922/6103 | **80.6%** | 173 min | 14:38 | ~42 min |
| contamination_60_random_seed456 | 3 | 4919/6103 | **80.6%** | 173 min | 14:38 | ~42 min |

Speed: ~2.11 s/step. The ess_only experiments started ~19 min earlier and are accordingly further ahead.

**Tmux sessions:** `contamination_60_random_seed123`, `contamination_60_random_seed456` (the ess_only runs were launched via nohup, not tmux).

### Old Experiments Status

| Experiment | Status | Final Checkpoint | Completed |
|------------|--------|-----------------|-----------|
| qwen06b_uniform_seed42 | **Not found** at expected path. `qwen06b_uniform_seed42_v2` exists instead | checkpoint-6103 + `final/` + `eval_results.json` | **Yes** (finished ~05:57 May 18) |
| ess_only_seed123 | checkpoint-6103 + `final/` | **Yes** (finished ~07:25 May 18) |
| ess_only_seed456 | checkpoint-6103 + `final/` | **Yes** (finished ~07:07 May 18) |
| random_reweight_seed456 | checkpoint-6103 + `final/` | **Yes** (finished ~08:29 May 18) |

All 4 old experiments completed successfully (all reached step 6103 with `final/` directory). The uniform experiment directory is named `qwen06b_uniform_seed42_v2` (not `qwen06b_uniform_seed42`), and it additionally has `eval_results.json`.

### Estimated Completion

- **ess_only seed123/456**: ~17:55 UTC (about 25 min from now)
- **random seed123/456**: ~18:13 UTC (about 43 min from now)

---
