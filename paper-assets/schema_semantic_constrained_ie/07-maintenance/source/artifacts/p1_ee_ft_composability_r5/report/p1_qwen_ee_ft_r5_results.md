# P1 Qwen3-8B FT WikiEvents EE - Round 5 Results

## Schema Fix
- **Root cause**: `ontology_compiler.py` `compile_event_json_schema()` had `required: ["entities", "events"]`
- **Fix**: Changed to `required: ["events"]` (entities kept as optional property)
- **Effect**: FT model only outputs `{"events": [...]}`, so grammar no longer forces entity generation loop → parse failures eliminated

## Inference Config
- Model: `/root/autodl-tmp/checkpoints/qwen3_8b_lora_wikievents_merged`
- Dataset: WikiEvents test (20 docs)
- `repetition_penalty=1.2`, greedy decoding
- Added `--repetition_penalty` CLI arg to `run_constrained_extraction.py`

## Results Summary

| Metric | Unconstrained | Full S1 (Constrained) |
|--------|:------------:|:---------------------:|
| **Parse Rate** | 85.0% (17/20) | **95.0%** (19/20) |
| Entity F1 | 0.0 | 0.0 |
| **Trigger F1** | **32.08** | 26.72 |
| **Argument F1** | 7.85 | **8.18** |

## Violation Analysis

| Violation Type | Unconstrained | Full S1 (Constrained) |
|---------------|:------------:|:---------------------:|
| EV (event vocab) | 10.82% (21/194) | **0.0%** (0/285) |
| **RoV (role vocab)** | 38.31% (100/261) | **0.0%** (0/339) |
| **AC (arg constraint)** | 2.68% (7/261) | **0.0%** (0/339) |
| CF (cross-field) | 2 instances | 3 instances |
| **Go/NoGo (RoV+AC)** | 41.0% | **0.0%** |
| Total violation rate | 28.57% | **0.48%** |

## Key Findings
1. **Schema fix resolved parse failures**: Constrained parse rate improved from near-0% (pre-fix) to 95%
2. **Constrained decoding eliminates RoV and AC violations**: 0% violation rate vs 41% unconstrained
3. **Trigger F1 slightly lower with constraints** (26.72 vs 32.08): grammar restricts vocabulary, may prevent some valid triggers
4. **Argument F1 slightly better with constraints** (8.18 vs 7.85): valid role/entity type enforcement helps argument matching
5. **Entity F1 = 0 for both**: FT model trained without entity output, only produces events
6. **Remaining 5% parse failure in constrained**: 1 doc still fails (likely max_new_tokens truncation on very long output)
