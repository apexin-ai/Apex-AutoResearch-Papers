# diagnose exp 002 signals 3B d100 s123 v9

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_3B_d100_s123_v9_20260516T060411_result.json`
- **Structured JSON:** [`b18991c89b45bf36110e.json`](../../sessions/b1/b18991c89b45bf36110e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

| Item | Status |
|------|--------|
| PID 689315 | Dead (completed mmlu s4 normally) |
| PID 712011 | **Alive**, running gsm8k all signals on cuda:4 |
| mmlu s4 self-critique | **Done** — 14042/14042 items, all 15 chunks saved |
| gsm8k signals | **In progress** — ~2min elapsed, s1 embedding phase |
| cuda:4 | In use (576MiB) |
| Failure? | **No** — false alarm from PID rotation in batch job |
| Action needed | None — let it run. Registry updated with new PID 712011 |

---
