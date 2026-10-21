# code plan014 eval impl

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan014-eval-impl_20260514T021241_result.json`
- **Structured JSON:** [`41a73adde2d319de8e84.json`](../../sessions/41/41a73adde2d319de8e84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Aggregation logic works correctly. All components verified:

**Summary of what was done:**

1. **`scripts/eval_downstream.py`** — complete rewrite with:
   - **Phase 1**: GPU inference generating K=8 formalizations per sample (temperature=0.7, top_p=0.9)
   - **Phase 2**: Full STA ISR computation for each formalization via `run_sta` + `compute_isr`
   - **Phase 3**: 3-way NLI classification (prove conclusion → true, prove ¬conclusion → false, neither → unknown)
   - **Aggregation**: overall accuracy, by gold label, by ISR bucket (high/mid/low), by ISR quartile, Best-of-N (Oracle/ISR-best/Random/Prove-first)
   - **Multiprocessing**: `--workers N` for parallel CPU-bound solver evaluation
   - **Output**: JSON with per-sample details and aggregated statistics

2. **`data/test_held_out.jsonl`** — symlink to `test_100.jsonl` (100 samples, 0 overlap with training, labels: true=40, false=29, unknown=31)

3. **Dry-run verified**: negation logic, 3-way classification for all three label types, parse error handling, and aggregation all pass.

**To run the full eval** (once a checkpoint is available):
```bash
export CUDA_VISIBLE_DEVICES=0
python scripts/eval_downstream.py \
  --checkpoint_path outputs/&lt;checkpoint_dir> \
  --data_path data/test_held_out.jsonl \
  --output_path results/plan014_downstream.json \
  --num_generations 8 --workers 4
```

---
