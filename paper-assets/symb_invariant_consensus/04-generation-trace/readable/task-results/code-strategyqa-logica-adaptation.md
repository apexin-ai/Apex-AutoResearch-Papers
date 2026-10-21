# code strategyqa logica adaptation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_strategyqa-logica-adaptation_20260518T171744_result.json`
- **Structured JSON:** [`3f4f45bdef28995a4688.json`](../../sessions/3f/3f4f45bdef28995a4688.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications pass. Here's a summary of all changes:

### Part 1: StrategyQA Extraction Prompt Fix

**`sica/constraint_extractor.py`**:
- Added `COMMONSENSE_EXTRACTION_PROMPT` (line 95) with claim/causal/conclusion constraint types for Yes/No commonsense reasoning
- Added `_COMMONSENSE_TYPES = {"claim", "causal", "conclusion"}` (line 133)
- Updated `_build_prompt()` to route `domain == "commonsense"` to the new prompt
- Updated `_parse_response()` valid_types to accept commonsense constraint types

**`sica/trace_generator.py`**:
- Added `COMMONSENSE_SOLVE_PROMPT` (Yes/No format with `\boxed{Yes}`/`\boxed{No}`)
- Added `MULTICHOICE_SOLVE_PROMPT` (for 4-choice with `\boxed{A}`)
- Added `extract_yesno_answer()` and `extract_choice_answer()` helper functions
- Added `domain` property to `TraceGenerator` base class
- Updated `VLLMGenerator` and `APIGenerator` to use domain-aware prompt selection and answer extraction

**`sica/pipeline.py`**: Added `"strategyqa"` to datasets that get logic answer normalization (Yes/No -> True/False)

**`run_full_mvp.py`**: 
- Added `--strategyqa-data` argument and loading logic
- Updated domain classification: `strategyqa` -> `commonsense`, `logiqa` -> `logic`+`multichoice`

### Part 2: LogiQA 2.0

- **`data/prepare_logiqa.py`**: Downloads from GitHub, converts to pipeline format
- **`data/logiqa_200.json`**: 200 test problems ready
- **`run_logiqa.py`**: Full run script with SICA vs SC, resume support, checkpointing
- **`scripts/run_logiqa200.sh`**: Shell launch script (vLLM startup + pipeline)

### Part 3: Dry-run

- StrategyQA: prompt generates correctly (commonsense types, no math equations), answer extractors pass all tests
- LogiQA: full mock pipeline runs end-to-end on 2 problems without errors

---
