# experiment d135 gemini launch

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d135-gemini-launch_20260521T143259_result.json`
- **Structured JSON:** [`c8861cffeb3f86330edc.json`](../../sessions/c8/c8861cffeb3f86330edc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment is stable. Here's the status report:

## Gemini-2.5-Pro FOLIO-204 SCB Status

| Item | Value |
|------|-------|
| **PID** | 19972 (westd-25068) |
| **API** | `http://47.94.22.126/v1` — confirmed working |
| **Progress** | 2/204 done, both **correct** |
| **Yield** | 83–100% (avg ~92%) — vastly improved from earlier 17–42% |
| **SC@12 Accuracy** | 100% (2/2) |
| **Finish reasons** | 22/24 traces = `stop`, 2 = `unknown` (no truncation) |
| **Per-problem time** | ~185–226s (avg ~206s) |
| **ETA** | ~693 min (~11.5 hours) → completion ~10:30 AM |
| **o3** | No o3 processes running |

**Note**: Script launched with `sem=5` instead of your requested `sem=10`. With sem=10 the rolling window would process 12 traces in ~2 rounds instead of ~3, cutting ETA by ~33% to ~7.5 hours. Want me to kill and restart with `--semaphore 10 --resume`? The `--resume` flag will pick up from where it left off (results are checkpointed every 5 problems).

---
