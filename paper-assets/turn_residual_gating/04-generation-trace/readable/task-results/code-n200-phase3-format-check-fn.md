# code n200 phase3 format check fn

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n200_phase3_format_check_fn_20260522T104803_result.json`
- **Structured JSON:** [`41c0df1be25eba67dcd1.json`](../../sessions/41/41c0df1be25eba67dcd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**200/200 passed.** All prompts resolve and pass positive/negative correctness tests.

Summary of changes made:

**`src/eval_instruction_retention.py`** (production code):
- Added `make_sentence_word_count(n, tolerance=0)` factory — checks every sentence has exactly n words (±tolerance)
- Registered `"sentence_word_count"` in `CHECK_FACTORIES`

**`data/instruction_retention_prompts_200.json`**:
- Fixed `content_style_each_sent_exactly`: changed `check_type` from `"regex_match"` (with invalid pattern `"sentence_word_count_10"`) to `"sentence_word_count"` with `{"n": 10}`

**`scripts/validate_ir_prompts.py`** (validation script):
- Added `_REGEX_MATCH_EXAMPLES` dict for `should_match=false` regex patterns (first-person, passive voice)
- Fixed regex_match handler to properly handle `min_matches` (repeat text) and `per_sentence` (join without extra periods)
- Added `sentence_word_count` test generator
- Used double-newline separator for `\n\n` patterns

Final result:
```
Resolve: 200/200 OK, 0 FAILED
Pos/Neg: 200/200 OK, 0 FAILED
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "n": 10
  }
}
```

</details>

---
