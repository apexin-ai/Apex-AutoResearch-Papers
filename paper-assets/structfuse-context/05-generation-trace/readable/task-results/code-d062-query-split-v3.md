# code d062 query split v3

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d062_query_split_v3_20260516T074549_result.json`
- **Structured JSON:** [`99a9d99dd082672db29c.json`](../../sessions/99/99a9d99dd082672db29c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All infrastructure is already fully implemented. Here's the summary:

---

**D062 Query Split — Already Complete**

Everything was implemented by a previous Worker. Here's what exists:

| Component | Path | Status |
|-----------|------|--------|
| Split script | `/root/structfuse/scripts/generate_query_split.py` | Done, stratified by repo, seed=42 |
| Split outputs | `/root/autodl-tmp/structfuse/d062_splits/selection_indices.txt` (504 lines) | Generated |
| | `/root/autodl-tmp/structfuse/d062_splits/test_indices.txt` (2476 lines) | Generated |
| Eval script | `/root/structfuse/scripts/evaluate_pool50.py` | Supports `--selection-set` / `--test-set` flags |
| Orchestrator | `/root/structfuse/scripts/run_d062_eval.py` | Dry-run passes, finds 14 checkpoints |

**Split**: 504 selection + 2476 test = 2980 total (from `val_random_s42.jsonl`). Uses line-index-based filtering to handle duplicate query_ids.

**Eval command template** (for future Workers):
```bash
# Full pipeline (selection → pick best → test eval):
python /root/structfuse/scripts/run_d062_eval.py

# Single checkpoint eval on test set:
python /root/structfuse/scripts/evaluate_pool50.py \
  --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
  --test-set /root/autodl-tmp/structfuse/d062_splits/test_indices.txt \
  --output /root/autodl-tmp/structfuse/d062_results/test_random_s42_best_by_recall_at_1.json
```

**Next step**: Run `python scripts/run_d062_eval.py` when GPU is free (14 checkpoints × 2 phases = 28 eval runs on pool=50). Results dir is currently empty — no eval has been executed yet.

---
