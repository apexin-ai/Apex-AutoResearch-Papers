# code gsm8k profiling

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k_profiling_20260515T141151_result.json`
- **Structured JSON:** [`d653d7c8db2449ae5852.json`](../../sessions/d6/d653d7c8db2449ae5852.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 GSM8K profiling jobs are running in parallel across GPUs 0-3. Here's the status:

**Jobs submitted:**
| GPU | Job | PID | Script |
|-----|-----|-----|--------|
| 0 | DeepSeek importance (s=0.15,0.20,0.25,0.30) | 242762 | `run_gsm8k_ds_gpu0.sh` |
| 1 | DeepSeek random (s=0.15,0.20,0.25,0.30) | 243045 | `run_gsm8k_ds_gpu1.sh` |
| 2 | Qwen importance (s=0.15,0.20,0.25,0.30) | 243297 | `run_gsm8k_qw_gpu2.sh` |
| 3 | Qwen random (s=0.15,0.20,0.25,0.30) | 243552 | `run_gsm8k_qw_gpu3.sh` |

**What was done:**
1. Created `/root/autodl-tmp/pacs/data/gsm8k.json` — 50 random GSM8K test problems (seed=42)
2. Modified `pacs/profiling/run_profiling.py`:
   - Added `--save_generations` flag to save generated texts for accuracy evaluation
   - Fixed stratified sampling bypass for datasets without `level` field (GSM8K)
3. Created `compute_gsm8k_accuracy.py` — extracts `#### NUMBER` from ground truth and model outputs (handles DeepSeek `&lt;think>` format)
4. Created `aggregate_gsm8k_results.py` — aggregates all 16 conditions into `analysis_output/gsm8k_profiling_results.json` + CSV tables
5. Created 4 run scripts with `--max_new_tokens 2048 --min_phase_length 5`

**Estimated completion:** ~2-3 hours (all 4 GPUs in parallel, ~1 min/problem × 200 problems each). Monitoring cron set up every 10 minutes. No errors in any log so far.

---
