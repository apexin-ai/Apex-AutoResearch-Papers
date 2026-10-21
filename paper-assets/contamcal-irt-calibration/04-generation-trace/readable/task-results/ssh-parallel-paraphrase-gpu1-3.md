# ssh parallel paraphrase gpu1 3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_parallel-paraphrase-gpu1-3_20260513T184649_result.json`
- **Structured JSON:** [`42b1e95510a735be0991.json`](../../sessions/42/42b1e95510a735be0991.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GSM8K entered retry round 1 (38 batches) — 92% of items failed QC, similar to HumanEval's high BLEU issue. This retry will take ~26 min in transformers mode. ARC will be similar.

Here's the current summary:

---

### === Paraphrase Parallel Launch Summary ===

| GPU | Benchmark | PID | Mode | Status | Notes |
|-----|-----------|-----|------|--------|-------|
| GPU 0 | MMLU | **204467** (v3) | vLLM | **RUNNING** 64/878 (7%) | Restarted with bs=16 after 2 prior crashes (orphaned EngineCore held GPU memory). ETA ~60 min |
| GPU 1 | GSM8K | **189361** | Transformers | **RUNNING** - Retry 1 (3/38) | Initial gen done (42/42, 29min). Now retrying ~1200 failed QC items. ETA ~25 min for retry 1 |
| GPU 2 | ARC-Challenge | **190712** | Transformers | **RUNNING** - QC phase | Generation done (37/37, ~30min). Now in QC/retry phase |
| GPU 4 | HumanEval | (201097) | vLLM | **COMPLETED** | Output: `/root/autodl-tmp/exp001/paraphrases/humaneval_paraphrases.json` (500KB) |

**HumanEval QC Results:**
- Total items: 164
- QC passed: 26/164 (15.9%)
- Main failure reason: BLEU score too high (paraphrases not diverse enough from originals)
- Cosine similarity threshold (>0.85): mostly met
- BLEU threshold (<0.3): most items fail — model generates near-copies

**MMLU Crash Root Cause:** Parent python process dies silently (no traceback — likely system OOM killer), leaving `VLLM::EngineCore` child as orphan (PPID=1) holding 22.9 GiB GPU memory. Fixed by killing orphan (PID 201376) and restarting with smaller batch size (16 vs 32).

**Key Issue:** All benchmarks have low QC pass rate due to high BLEU scores — the model produces paraphrases too similar to originals. This is a prompt/strategy problem that will need addressing after all generation completes.

---
