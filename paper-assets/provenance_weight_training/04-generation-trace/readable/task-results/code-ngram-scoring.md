# code ngram scoring

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ngram_scoring_20260518T114901_result.json`
- **Structured JSON:** [`3b9ccc041d3bed30a447.json`](../../sessions/3b/3b9ccc041d3bed30a447.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

N-gram PPL scoring complete.

**Results:**
- **Total samples scored:** 371,499
- **5-gram model:** 574,866 unique contexts (trained on 50K sample)
- **PPL statistics:** mean=4.46, min=1.03, max=2901.06
- **Output file:** `/root/provenance_weight_training/data/scored_data_ngram.jsonl` (944MB)
- **New field:** `ngram_ppl` added to each sample
- **Runtime:** ~18 minutes on CPU

Output is ready. Each sample now has the `ngram_ppl` field alongside existing `text`, `q_score`, and metadata fields.

---
