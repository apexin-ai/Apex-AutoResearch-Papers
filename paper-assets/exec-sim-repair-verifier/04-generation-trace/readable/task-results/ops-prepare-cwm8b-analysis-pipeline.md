# ops prepare cwm8b analysis pipeline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-cwm8b-analysis-pipeline_20260515T220320_result.json`
- **Structured JSON:** [`da436004ee0ab2bf7383.json`](../../sessions/da/da436004ee0ab2bf7383.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report:

## GPU Status (as of ~06:04 UTC May 16)

| GPU | Task | Progress | ETA (UTC) |
|-----|------|----------|-----------|
| **cuda:0** | CLS 8B s42 val sweep (21 ckpts) | 11/21 done, on ckpt-3800 (9170/9335) | ~10:20 |
| **cuda:1** | CLS 8B s42 val sweep GPU1 (10 ckpts) | 8/10 done, on ckpt-5400 (5770/9335) | ~07:10 |
| **cuda:2** | CWM 8B training v5 (resume) | 5846/6633 steps (88%), ~12.3s/it | ~08:50 |
| **cuda:3** | **CWM 8B ckpt-400 test eval** | **4176/9784 (42.7%)**, running_acc=**64.7%** | **~17:00** |

### CWM 8B Test Eval — ETA Revised
Original ETA was 09:15 UTC, but **actual throughput averaged lower** than projected (likely due to intermittent stalls). Current rate is ~8.5 samples/min with 5608 remaining → **revised ETA: ~17:00 UTC May 16** (~11h from now).

### Preliminary 8B-8B Gap (at 42.7% completion)
- CLS 8B s42 test: **83.52%**
- CWM 8B running_acc: **64.7%**
- **Current gap: ~18.8pp** (close to the 20pp C1 threshold, but only 42.7% through — final number may shift)

### Analysis Tooling
- `analyze_cwm_eval.py` exists **locally** with full metrics pipeline (accuracy, F1, unparseable breakdown, truncation analysis, CLS comparison, gen-length buckets)
- Output file: `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/results_incremental.jsonl`
- JSONL format per record: `{index, problem_id, label, pred, correct, truncated, gen_text, unparseable}`
- The default CLS comparison values in the script have a typo: `CLS_8B_s42: 84.52` should be `83.52`

### Note on the script
The `analyze_cwm_eval.py` needs to be:
1. Synced to server (only exists locally), OR run locally after downloading the results JSONL
2. Default CLS values updated — I can fix the `84.52 → 83.52` typo and add CLS 8B s123 (85.60%) and full metric breakdowns from registry now if you want

Want me to fix the script defaults and prepare it for immediate use when the eval completes?

---
