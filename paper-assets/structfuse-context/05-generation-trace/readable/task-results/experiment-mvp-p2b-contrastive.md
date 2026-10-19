# experiment mvp p2b contrastive

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_p2b_contrastive_20260512T115900_result.json`
- **Structured JSON:** [`a6d1e1a2547e1caa6153.json`](../../sessions/a6/a6d1e1a2547e1caa6153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training is running. Summary of what's in progress:

- **9 training runs** (3 strategies × 3 seeds) executing sequentially on GPU 4
- Run 1/9 (`p2b_random_s42`) at step 100, loss decreasing from 0.36→0.09
- Estimated total time: ~11-12 hours
- Each run: 3 epochs × ~253 steps, eval every 50 steps, checkpoint every 200 steps
- When complete, `collect_p2b_results.py` will aggregate training-time metrics
- `eval_p2b.py` is ready for full 25-candidate-pool evaluation on final checkpoints
- Pass condition: dataflow recall@5 > random recall@5 by ≥2pp in ≥2/3 seeds

---
