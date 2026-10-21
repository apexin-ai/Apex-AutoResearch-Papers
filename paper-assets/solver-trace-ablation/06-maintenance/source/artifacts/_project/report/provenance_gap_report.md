# Provenance Completeness Report

**Date:** 2026-05-15
**Scope:** All DONE experiments with conclusion=success (24 total)

## Result: 24/24 complete (was 18/24)

### Fixed (6 experiments)

**Pattern 1: Missing spec.data_path/data_count/model_name/seed (5 SFT experiments)**

Root cause: `submit_training_job` SFT path doesn't auto-populate semantic spec fields.

| Experiment | seed | Filled values |
|---|---|---|
| plan009-sft-baseline-s43 | 43 | data_path, data_count=500, model_name=Qwen3-4B, seed=43 |
| plan009-sft-baseline-s44 | 44 | data_path, data_count=500, model_name=Qwen3-4B, seed=44 |
| plan009-sft-baseline-s43-1000 | 43 | data_path, data_count=500, model_name=Qwen3-4B, seed=43 |
| plan009-sft-baseline-s44-1000 | 44 | data_path, data_count=500, model_name=Qwen3-4B, seed=44 |
| plan009-sft-baseline-s44-1000-r3 | 44 | data_path, data_count=500, model_name=Qwen3-4B, seed=44 |

All values extracted from `reproduce.command` / `spec.command`.

**Pattern 2: Missing log_path (1 GRPO experiment)**

| Experiment | Filled value | Note |
|---|---|---|
| exp1-isr-b03-s43 | ~/runs/solver-trace-ablation/exp1-isr-b03-s43.log | Inferred from sibling experiments' log_path pattern. Experiment invalidated (D062/D063), retrained as r4. |

### Non-success experiments (not in scope)

42 additional DONE experiments (failed/killed/negative) have various provenance gaps. These are not paper-relevant and were not patched.
