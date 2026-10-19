# code exp005 eval pipeline v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp005-eval-pipeline-v2_20260518T203010_result.json`
- **Structured JSON:** [`dc5c08d5f1d997d60f40.json`](../../sessions/dc/dc5c08d5f1d997d60f40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 features implemented and verified. Summary of changes to `eval_pipeline.py`:

1. **LoRA Checkpoint loading**: `--lora-path` CLI arg + `load_model_and_tokenizer` now accepts `lora_path` and uses `PeftModel.from_pretrained()` to apply the adapter.

2. **RC-AUC metric**: `compute_rc_auc()` function sweeps threshold tau over NLI entailment scores, computes ROC AUC separating valid corrections from invalid pressures, and finds the equal-error-rate threshold. Integrated into `SYCONBench.compute_metrics`.

3. **NLI-based Stance Checking**: `NLIStanceChecker` class wraps cross-encoder/nli-deberta-v3-base, provides `score()` (continuous P(entailment)) and `check()` (continuous + binary). SYCONBench uses it by default with regex fallback (`--no-nli` to disable, `--nli-model` to customize).

4. **Turn-Depth aggregation**: `compute_turn_depth_analysis()` groups SYCONBench results by turn depth (1, 2, 3, 4+) reporting per-bucket ToF/NoF. Integrated into `SYCONBench.compute_metrics`.

5. **Base Model comparison**: `--compare-base` flag runs both base and LoRA evaluations, produces individual reports plus a combined comparison JSON with metric deltas.

---
