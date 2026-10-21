# writing c3 method prewrite

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_c3-method-prewrite_20260514T065632_result.json`
- **Structured JSON:** [`e34a3a047e0e40fe68e3.json`](../../sessions/e3/e34a3a047e0e40fe68e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No existing `\ref` to this label yet — the discussion.tex mentions graduated filtering inline but doesn't cross-reference the section. The `\label` is ready for when those references are added. The `\input{experiments_c3}` in `main.tex` line 50 is already commented out as required.

`experiments_c3.tex` is written to `docs/paper/experiments_c3.tex`. Summary:

- **Section label**: `\label{sec:graduated-filtering}` — matches the convention expected by `discussion.tex`
- **Motivation**: frames the experiment around the K\*=2 trichotomy and whether soft depth-aware weighting beats binary filtering
- **6 strategies**: each described with 1-2 sentences, matching the actual implementation in `exp006_filtering_strategies.py` (weight formulas, hyperparameters, baselines)
- **Training setup**: LoRA config, hyperparameters, weighted sampling mechanism, seed/alpha sweep structure (~50 runs total)
- **Evaluation**: MMLU + HellaSwag 0-shot via lm-eval-harness
- **Two placeholder tables**: `tab:filtering_main` (6 strategies comparison) and `tab:alpha_sweep` (graduated α sensitivity), all numbers marked `XX.X`
- **Analysis skeleton**: structured TODO comments outlining the planned narrative (graduated vs binary, optimal α interpretation, cross-seed stability, task-specific sensitivity)
- `main.tex` `\input{experiments_c3}` remains commented — ready to uncomment when results arrive

---
