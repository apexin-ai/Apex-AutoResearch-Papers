# code baseline launch scripts

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline-launch-scripts_20260513T081913_result.json`
- **Structured JSON:** [`5199a2a5f8fd7bc3befe.json`](../../sessions/51/5199a2a5f8fd7bc3befe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All syntax checks pass. Summary of changes:

**`config.py`** — added `fixed_ratio: float | None = None` field

**`data_utils.py`** — added `mix_datasets(real_dataset, synth_dataset, ratio, seed)` function that samples `ratio * N` real + `(1-ratio) * N` synthetic sequences, shuffles, returns `PackedDataset`

**`pilot_pipeline.py`** — 
- Added `--fixed-ratio` CLI argument
- Updated `run_pilot()` data selection: `None` = original behavior, `1.0` = pure real every gen, `0.0` = pure synth (G1+), `0<w<1` = mixed via `mix_datasets`
- Passes `fixed_ratio` through to `PilotConfig`

**`launch_baseline_w0.sh`** / **`launch_baseline_w1.sh`** — baseline launch scripts with 20M tokens/gen, 5M checkpoint interval, `--fixed-ratio 0.0` and `1.0` respectively

---
