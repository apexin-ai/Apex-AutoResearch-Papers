# ssh cron check exp001 phase1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cron-check-exp001-phase1_20260513T191049_result.json`
- **Structured JSON:** [`b74dbbba5302c005495f.json`](../../sessions/b7/b74dbbba5302c005495f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the status:

```
=== Phase 1 Complete Status ===
MMLU:          FAILED — vLLM init failed on GPU 0 (OOM: 8.36/23.52 GiB free from old process),
               fell back to transformers (attempt 1), then retried vLLM (attempt 2) which started
               but crashed at batch 16/220 (7%). No output file generated.
GSM8K:         IN PROGRESS — 76% (32/42 batches), transformers fallback, GPU 1, ~7 min remaining
ARC-Challenge: IN PROGRESS — 70% (26/37 batches), transformers fallback, GPU 2, ~9 min remaining
HumanEval:     DONE — 164 items, 26/164 QC pass (15.9%), vLLM succeeded

Completed: 1/4 benchmarks
Still running PIDs: 189375 (GSM8K, 22h20m), 190717 (ARC, 21h00m)
Failed: PID 200967 (MMLU) — crashed during vLLM retry attempt 2

GPU Status:
  GPU 0: 0% util, 22951 MiB used ← leaked from crashed MMLU process
  GPU 1: 96% util, 15049 MiB (GSM8K active)
  GPU 2: 94% util, 15103 MiB (ARC active)
  GPU 3-5: idle

QC Summary (completed):
  HumanEval: 164 items, 15.9% pass (26/164), 3 generation attempts

Notes:
  - All 4 benchmarks hit vLLM "duplicate template name" validation error,
    GSM8K/ARC/old-MMLU fell back to transformers successfully
  - MMLU restart (PID 200967) hit GPU 0 OOM on vLLM init (old process memory),
    fell back to transformers for attempt 1, then retried vLLM for attempt 2
    (GPU freed by then) but process died at 7%
  - HumanEval QC pass rate (15.9%) is very low — may need to investigate
    paraphrase prompt quality
  - GPU 0 holds ~23 GiB leaked memory — needs cleanup before MMLU restart
```

**Next steps needed:**
1. Wait ~10 min for GSM8K and ARC to finish
2. Clean GPU 0 leaked memory (kill zombie process or `nvidia-smi -r`)
3. Restart MMLU with `CUDA_VISIBLE_DEVICES=0` after GPU 0 is freed
4. Investigate the 15.9% QC pass rate on HumanEval — may need prompt tuning

---
