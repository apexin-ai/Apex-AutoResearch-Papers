# monitor progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress_check_20260514T204145_result.json`
- **Structured JSON:** [`9fa1b966651ca87314b1.json`](../../sessions/9f/9fa1b966651ca87314b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### Sessions & GPU

| GPU | Session | Process | PID | GPU Util | VRAM |
|-----|---------|---------|-----|----------|------|
| 0 | c2_n500_gpu0 (tmux) | ds_imp_s020 | 156554 | 77% | 30.1/97.9 GB |
| 1 | c2_n500_gpu1 (tmux) | ds_rand_s020 | 154305 | 76% | 30.6/97.9 GB |
| 2 | c2_qw_gpu2 (screen) | qw_imp_s020 | 159269 | 77% | 30.8/97.9 GB |
| 3 | c2_qw_gpu3 (screen) | qw_rand_s020 | 159794 | 79% | 31.4/97.9 GB |

All 4 processes **ALIVE**, 100% CPU each.

### Pipeline: s015 → s020 → s025 → s030 (each 500 problems)

**s015: ALL DONE** (results saved to disk)

**s020: IN PROGRESS**

| Process | GPU | Progress | Elapsed | Rate | s020 ETA |
|---------|-----|----------|---------|------|----------|
| ds_imp | 0 | **256/500** (51%) | 2h11m | 1.95/min | ~06:47 |
| ds_rand | 1 | **302/500** (60%) | 2h37m | 1.92/min | ~06:25 |
| qw_imp | 2 | **243/500** (49%) | 1h40m | 2.43/min | ~06:28 |
| qw_rand | 3 | **226/500** (45%) | 1h31m | 2.48/min | ~06:32 |

s020 output directories exist but are still empty (results written only on completion).

### 全局 ETA（全部 8 conditions 完成）

Each sparsity level takes ~4-5h per GPU. With s015 done and s020 ~50%, still need to finish s020 + run s025 + s030.

| Experiment | Bottleneck GPU | Remaining Work | ETA (all done) |
|------------|---------------|----------------|----------------|
| DeepSeek (GPU 0/1) | GPU 0 (imp) | 244 + 1000 problems | **~May 15 15:00-16:00** |
| Qwen (GPU 2/3) | GPU 3 (rand) | 274 + 1000 problems | **~May 15 13:00-15:00** |

**Overall: expect all 16 conditions done by ~May 15 16:00 (UTC+8)**, roughly 11 hours from now.

---
