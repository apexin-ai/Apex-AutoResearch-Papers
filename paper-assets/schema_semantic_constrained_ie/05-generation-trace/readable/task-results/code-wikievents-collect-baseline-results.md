# code wikievents collect baseline results

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_collect_baseline_results_20260517T190117_result.json`
- **Structured JSON:** [`8740989626f5be5fe850.json`](../../sessions/87/8740989626f5be5fe850.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three baselines are still in progress. Here's the status:

---

**Model: Qwen (unconstrained)**
- Server: westd-16980
- Docs: 172/246 (70%)
- Last write: 19s ago (actively running)
- Session: `wikievents_unconstrained` / `qwen_wikievents` (started ~01:42)
- Rate: ~2.1 docs/min
- ETA: ~35 min

**Model: Llama (unconstrained)**
- Server: westd-16980
- Docs: 171/246 (70%)
- Last write: 37s ago (actively running)
- Session: `llama_wikievents_full` (started ~01:47)
- Rate: ~2.3 docs/min
- ETA: ~33 min

**Model: Mistral (unconstrained)**
- Server: westd-21461
- Docs: 93/246 (38%)
- Last write: ~19 min ago (may be on a long document)
- Session: `mistral_wikievents` (started ~00:50)
- Rate: ~0.7 docs/min
- ETA: ~3.5 hours

**Constrained dry-run (Qwen, westd-21461):**
- Docs: 10/20
- Log shows model still loading weights (Fetching 5 files, Loading weights 100%)

---

GPU utilization:
- westd-16980: GPU0 19.9GB/89%, GPU1 21.7GB/87% (both active)
- westd-21461: GPU0 0MB/0%, GPU1 18.9GB/82% (only GPU1 active)

Qwen and Llama should finish in ~30-35 min. Mistral is significantly slower. I can re-check and run evaluations once the first two complete.

---
