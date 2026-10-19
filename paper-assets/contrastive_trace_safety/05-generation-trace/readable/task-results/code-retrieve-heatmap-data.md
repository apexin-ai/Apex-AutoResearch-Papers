# code retrieve heatmap data

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_retrieve_heatmap_data_20260520T165655_result.json`
- **Structured JSON:** [`ee8a76c21bbcad98ae9a.json`](../../sessions/ee/ee8a76c21bbcad98ae9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's what I found:

**`layer_metric_ablation.json` does not exist** — not on the server (`cqa1-21977`, the only available server), nor locally. The directory `exp_r3_layer_ablation/` doesn't exist anywhere.

**`qwq_alt_layers.json`** — also does not exist.

**`plot_layer_heatmap.py`** — does not exist.

**What does exist:**

**Server (`cqa1-21977`):**
- `/root/autodl-tmp/artifacts/` only contains: `fig_calibration.pdf`, `fig_calibration.png`
- No `contrastive_trace_safety` project directory on this server at all

**Local (`artifacts/`):**
- Closest match: `artifacts/diag_d1_layer_sweep/report/d1_layer_sweep_results.md` and `artifacts/exp_gru256_multilayer/data/gru256_ablation.log`
- No `exp_r3_layer_ablation` directory

**Forest plot script (local):**
- `scripts/plot_forest_precision.py` exists
- `docs/paper/figures/fig_forest_precision.pdf` and `.png` exist

**All local scripts:**
```
scripts/run_threshold_sensitivity.py
scripts/run_7b8b_residualization.py
scripts/run_a7_random_projection.py
scripts/random_cp_control_qwq32b.py
scripts/sf3_quadratic_residual.py
scripts/n6_multi_metric_ensemble.py
scripts/advbench_hs_exploratory.py
scripts/heuristic_cp.py
scripts/advbench_preliminary_sweep.py
scripts/advbench_preliminary_sweep_no_pca.py
scripts/advbench_phase4_layer_sweep.py
scripts/annotate_cp_llm.py
scripts/annotate_cp_llm_qwen3.py
scripts/annotate_cp_llm_gpt4omini.py
scripts/plot_forest_precision.py
```

The `contrastive_trace_safety` project was never deployed to this server instance. The data files you're looking for either haven't been generated yet, or were on a previous server instance that's no longer available. Want me to read the layer sweep results from `diag_d1_layer_sweep` or `advbench_phase4_layer_sweep.py` instead?

---
