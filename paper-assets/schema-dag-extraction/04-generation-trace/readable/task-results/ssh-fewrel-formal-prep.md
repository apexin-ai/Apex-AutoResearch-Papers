# ssh fewrel formal prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-formal-prep_20260515T083006_result.json`
- **Structured JSON:** [`0f606326a9c77cc75fe6.json`](../../sessions/0f/0f606326a9c77cc75fe6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 tasks complete. Summary of deliverables:

**Scripts (deployed + dry-run validated on cqa1-38874):**
- `src/run_fewrel_formal.py` — exp1 (count curve, 110 batches) + exp2 (BCS controlled, 54 batches), with PID→name auto-remap for Qwen3 embeddings
- `src/analyze_fewrel_results.py` — 3-layer analysis (pairwise SCS-confusion, per-type accuracy vs BCS, batch-level accuracy vs BCS)

**Bug fix applied this session:**
- Added PID→relation name key remapping in embedding loading (lines 203-207). `compute_type_embeddings.py` outputs PID-keyed embeddings but `fewrel_utils` data uses relation names — the remap bridges this mismatch automatically.

**Launch commands:** `artifacts/fewrel_formal/LAUNCH_COMMANDS.md`
- Step 0: Qwen3 embedding computation (~2 min GPU)
- Step 1-2: exp1/exp2 full runs with nohup
- Step 3: analysis pipeline
- Execution order: embeddings → dry-run → exp1 (~5.5h) → exp2 → analyze

---
