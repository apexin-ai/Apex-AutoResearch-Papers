# code gen length ablation c

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gen_length_ablation_c_20260517T045550_result.json`
- **Structured JSON:** [`938dd0d990b8219e08f0.json`](../../sessions/93/938dd0d990b8219e08f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job is running correctly. Generation for 128-token length is progressing at ~1.4s/batch (63 batches for 1000 samples at batch_size=16).

**Status:**
- `gen_length_ablation_001` submitted to `cuda:0` on `gpu-6000pro-2`, status RUNNING
- Currently generating 128-token passages for depth 1
- Estimated timeline: ~1.4s/batch × 63 batches × 3 depths × 3 lengths for generation, plus feature extraction and classification
- Output will be at `results/gen_length_ablation/summary.json`

Estimated total runtime: ~2-3 hours (generation is the bottleneck; 128-token generation is faster than 512-token).

---
