# exp advbench phase4 layer sweep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_advbench_phase4_layer_sweep_20260520T063330_result.json`
- **Structured JSON:** [`abc0d7474fb3e2c25083.json`](../../sessions/ab/abc0d7474fb3e2c25083.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job submitted.

- **exp_id**: `advbench_phase4_layer_sweep`
- **tmux session**: `advbench_phase4_layer_sweep`
- **log**: `~/runs/contrastive_trace_safety/advbench_phase4_layer_sweep.log`
- **GPU**: cuda:0

Key changes from the pseudo-CP version:
1. Reads LLM CP annotations (`llm_cp_annotations_qwen3.json`) instead of heuristic pseudo-CP
2. Filters for `is_jailbreak=True` only → 52 traces
3. Allows CP=0 (removed `cp < 1` filter) — 47/52 traces have CP=0
4. `crossing_rate` denominator uses only traces with CP>0 (avoids division by traces where early crossing is undefined)
5. Output → `artifacts/advbench_layer_sweep/`
6. `--dry-run` CLI flag added

25 layers × 4 windows × bootstrap 1000 on 52 traces — estimated ~1-2 hours.

---
