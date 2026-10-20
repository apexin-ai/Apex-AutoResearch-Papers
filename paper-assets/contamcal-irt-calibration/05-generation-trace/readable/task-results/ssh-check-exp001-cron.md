# ssh check exp001 cron

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp001-cron_20260513T190217_result.json`
- **Structured JSON:** [`c4597842a6c335cf15ef.json`](../../sessions/c4/c4597842a6c335cf15ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp-001 Phase 1 Status ===

Old PID 186841: KILLED (expected)
  Log stops at transformers 40/439 batches (9%), no crash traceback — clean kill.

New MMLU vLLM: PID 196320 + EngineCore 197417 — STUCK
  vLLM EngineCore loaded on GPU 0 (22334 MiB), but dataset download
  is failing: HuggingFace connection timeout, retry 4/5.
  Root cause: likely missing `source /etc/network_turbo`.

GSM8K:    IN PROGRESS — transformers fallback, 19/42 batches (45%), PID 189375
ARC:      IN PROGRESS — transformers fallback, 15/37 batches (41%), PID 190717
HumanEval: IN PROGRESS — transformers fallback, 0/6 batches (just started), PID 191459
           vLLM failed (GPU memory insufficient), some params offloaded to CPU.

Paraphrases completed: NONE (output dir empty)

GPU utilization:
  GPU 0: vLLM EngineCore 22334 MiB — MMLU (blocked on HF download)
  GPU 1: 95%, 15040 MiB — GSM8K
  GPU 2: 95%, 15094 MiB — ARC
  GPU 3:  0%, ~22098 MiB — HumanEval (15134) + MMLU main (6964), shared
  GPU 4-5: idle
```

**3 issues need attention:**

1. **MMLU download stuck** — HuggingFace unreachable. Needs `source /etc/network_turbo` or use cached dataset. Will exhaust retries and fail soon.

2. **vLLM broken everywhere** — all 4 benchmarks hit `duplicate template name` pydantic assertion or memory errors and fell back to transformers (~50s/batch vs vLLM's ~2s/batch). The "vLLM is fixed" assumption doesn't hold.

3. **GPU 3 overloaded** — HumanEval + MMLU main sharing one GPU, HumanEval has model params offloaded to CPU, will be extremely slow.

---
