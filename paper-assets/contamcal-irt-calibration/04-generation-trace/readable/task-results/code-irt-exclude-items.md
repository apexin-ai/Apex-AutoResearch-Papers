# code irt exclude items

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_irt-exclude-items_20260516T051153_result.json`
- **Structured JSON:** [`65c4718cd129cd3d6455.json`](../../sessions/65/65c4718cd129cd3d6455.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tests pass. Summary of changes to `artifacts/run_pooled_4bench_irt.py`:

**New CLI args** (via `argparse`):
- `--exclude-items &lt;path.json>` — JSON file containing a list of `item_id` strings (e.g. `["mmlu_42", "mmlu_103"]`). Items matching `{benchmark}_{column_index}` are masked out before Stan fitting.
- `--min-item-variance &lt;float>` — Items with cross-model variance below this threshold are excluded (default 0.0 = disabled). Addresses the HumanEval-para all-zeros problem.

**New function** `filter_items()` (line 115) — removes items by exclusion set and/or low variance, returns filtered response matrix + stats.

**Integration points**:
- `run_single_benchmark_fit` — filters items after model exclusions, before exposure matrix construction (line 170)
- `run_joint_fit` — filters per-benchmark items before concatenation (line 276)
- `main()` — loads exclude JSON, records filter config in output metadata

Backward compatible: no args = identical behavior to before.

Sync to remote needed before running on the server.

---
