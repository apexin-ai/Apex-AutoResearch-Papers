# ssh poll 5epoch and mf4 completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_poll_5epoch_and_mf4_completion_20260522T132228_result.json`
- **Structured JSON:** [`007d403d1be3f007abfa.json`](../../sessions/00/007d403d1be3f007abfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the status:

**1. 5-epoch LP (PID 137900, cuda:3)** — Still running (elapsed 1h51m). GPU 3 active (PID 138176, 30,610 MiB). Output dir `fewnerd_5epoch_lp_seed42/` is empty — no files written yet. No log file in `~/runs/` (was launched as direct `python -u`, stdout goes to the launching terminal). Can't determine current progress from here.

**2. MF4 s123v2 (PID 136358, cuda:2)** — Still running (elapsed 1h54m). GPU 2 active (PID 136811, 30,914 MiB). Currently in what appears to be a second processing phase: **29% (11,059/37,648)**, ~16 min remaining at ~30 it/s. The first phase (301,184 prompts = 37,648 × 8 samples) has completed. Output dir `fewnerd_mf4_seed123_v2/` also empty — results not written yet.

Both are further from completion than expected. The 5-epoch LP "96%" may have been a phase that completed, with the process now in a subsequent phase (possibly the same 37k rendering step). Neither experiment has written output files yet — they both appear to write results only at the end.

---
