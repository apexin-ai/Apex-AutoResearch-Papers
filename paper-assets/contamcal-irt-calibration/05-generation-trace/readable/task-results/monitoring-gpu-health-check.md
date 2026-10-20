# monitoring gpu health check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_gpu-health-check_20260516T022307_result.json`
- **Structured JSON:** [`2120dce84675a196eae4.json`](../../sessions/21/2120dce84675a196eae4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full report.

## GPU Health

| GPU | Name | Util% | Mem Used/Total | PID | Process |
|-----|------|-------|---------------|-----|---------|
| 0 | RTX 4090 D | 93% | 7539/24564 MiB | 642757 | eval_3B_d100_s123_a32_batch |
| 1 | RTX 4090 D | 65% | 8985/24564 MiB | 676497 | eval_3B_d000_s42_a32_batch |
| 2 | RTX 4090 D | 66% | 8985/24564 MiB | 679190 | eval_3B_d005_s42_a32_batch |
| 3 | RTX 4090 D | 69% | 8985/24564 MiB | 655989 | eval_3B_d025_v3_s42_aligned |
| 4 | RTX 4090 D | 61% | 6703/24564 MiB | 668217 | signals_3B_v9 (d025_s123) |
| 5 | RTX 4090 D | 65% | 7665/24564 MiB | 663067 | signals_3B_d025_v3_s42 |

All 6 PIDs confirmed alive.

## Experiment Progress

| GPU | Experiment | PID Alive | Current Task | Progress | ETA |
|-----|-----------|-----------|-------------|----------|-----|
| 0 | eval_3B_d100_s123_a32 | Yes | mmlu (paraphrased) 535/6596 | ~8% of paraphrased | ~2.5min for this phase, then GSM8K+ARC (~3hr) |
| 1 | eval_3B_d000_s42_a32 | Yes | GSM8K 106/1319 (mmlu done: **0.6308**) | ~8% of GSM8K | ~2.5hr for GSM8K + ARC |
| 2 | eval_3B_d005_s42_a32 | Yes | GSM8K 1/1319 (mmlu done: **0.6308**) | just started GSM8K | ~2.8hr for GSM8K + ARC |
| 3 | eval_3B_d025_v3_s42_aligned | Yes | Unknown (no log file, output dir empty) | Running ~3hr | No ETA — no log redirected |
| 4 | signals_3B_v9 (d025_s123) | Yes | Self-critique mmlu [8000:9000] 262/500 | ~61% of mmlu SC | ~1hr mmlu SC, then GSM8K+ARC SC |
| 5 | signals_3B_d025_v3_s42 | Yes | Self-critique mmlu 5805/7021 | ~83% of mmlu SC | ~27min mmlu SC, then GSM8K+ARC SC |

**Note on cuda:3:** PID 655989 is running `evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d025_v3_s42 --mc-format aligned` but no log file was found in `~/runs/`. Output may be going to a tmux pane or lost. Output dir `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_aligned/` is empty, so no benchmark has completed writing results yet.

## 0.5B Signals Failure Diagnosis

- **Root cause:** The batch log shows `bash: run_05B_s123_signals.sh: No such file or directory` → EXIT_CODE=127. The script `/root/contamcal-irt-calibration/exp002/run_05B_s123_signals.sh` **does not exist**.
- **What exists:** Only `run_signals_05B.sh`, which is hardcoded to run seeds s42 for dosages d000/d005/d100. There is no s123-specific version of this script.
- **Fix needed:** Either:
  1. Create `run_05B_s123_signals.sh` by copying `run_signals_05B.sh` and changing checkpoint paths from `*_s42` to `*_s123` variants, or
  2. Parameterize `run_signals_05B.sh` to accept a seed argument (e.g., `bash run_signals_05B.sh 3sig s123`).

---
