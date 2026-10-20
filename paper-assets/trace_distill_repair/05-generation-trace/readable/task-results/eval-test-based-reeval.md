# eval test based reeval

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_test_based_reeval_20260515T114100_result.json`
- **Structured JSON:** [`3577ba896cd8bccab1ad.json`](../../sessions/35/3577ba896cd8bccab1ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No register_artifact tool available. Here's the complete analysis:

---

## Re-evaluation Results: 4 Instances × 4 Conditions

### Oracle Baseline
**Ground truth patch pass rate: 4/4 (100%)** — test infrastructure fully functional for all 4 instances after dependency fixes.

### Per-Instance × Per-Condition Results

| Instance | Condition | Pass | Judge | Overlap | Fix Len | Failure Reason |
|---|---|---|---|---|---|---|
| **black_1** | no_trace | N | 1 | 0.094 | 5000 (trunc) | SyntaxError |
| | full_trace | N | 0 | 0.088 | 5000 (trunc) | SyntaxError |
| | structural_filtered | N | 5 | 0.065 | 5000 (trunc) | SyntaxError |
| | line_filtered | N | 0 | 0.033 | 3829 (trunc) | SyntaxError |
| **fastapi_1** | no_trace | N | 4 | 0.413 | 4581 (trunc) | SyntaxError |
| | full_trace | N | 5 | 0.588 | 5000 (trunc) | SyntaxError |
| | structural_filtered | N | 1 | 0.913 | 5000 (trunc) | SyntaxError |
| | line_filtered | N | 5 | 0.913 | 5000 (trunc) | SyntaxError |
| **fastapi_2** | no_trace | N | 2 | 0.306 | 5000 (trunc) | SyntaxError |
| | full_trace | N | 0 | 0.075 | 1519 (trunc) | SyntaxError |
| | structural_filtered | N | 0 | 0.747 | 5000 (trunc) | SyntaxError |
| | line_filtered | N | 5 | 0.761 | 5000 (trunc) | SyntaxError |
| **httpie_2** | no_trace | N | 4 | 0.975 | 4544 | AssertionError (wrong fix) |
| | full_trace | N | 2 | 0.992 | 4337 | AssertionError (wrong fix) |
| | structural_filtered | N | 1 | 0.983 | 4339 | AssertionError (wrong fix) |
| | line_filtered | N | 0 | 0.983 | 4355 | AssertionError (wrong fix) |

### Condition Pass Rates
| Condition | Pass Rate |
|---|---|
| structural_filtered | 0/4 |
| line_filtered | 0/4 |
| full_trace | 0/4 |
| no_trace | 0/4 |
| **ground_truth** | **4/4** |

### Failure Categories
- **SyntaxError (12/16)**: black_1 + fastapi_1 + fastapi_2 — LLM output capped at 4096 tokens (`max_tokens`), then checkpoint truncated to 5000 chars. For files of 27K–221K chars, this produces partial files. Even smart-diff extraction creates invalid Python.
- **AssertionError (4/16)**: httpie_2 — the only instance with complete (non-truncated) fixes. File is small (4338 chars) and LLM reproduced it fully. But **none of the 4 conditions included the key fix** (`requests_session.max_redirects = args.max_redirects`). The "fixes" are essentially identical to the buggy code (overlap 0.97–0.99).

### Conclusions

1. **Structural filtering shows no advantage in test-based evaluation** — all conditions equally fail at 0/4. However, this is **not a fair comparison** because the evaluation is confounded by two systemic issues:

2. **Primary confound: output truncation** (affects 12/16 entries). The repair LLM's `max_tokens=4096` is far too small for files >5K chars. black.py (221K), applications.py (27K), and routing.py (40K) cannot be reproduced within this budget. The "output ONLY the fixed Python code" prompt forces the LLM to regenerate the entire file, which is impossible for large files. A **diff-based repair prompt** would fix this.

3. **Secondary confound: wrong target file** (fastapi_1). The repair targeted `changed_files[0]` = `fastapi/applications.py`, but the test checks `exclude_defaults` in `fastapi/encoders.py`. Even a perfect fix to applications.py wouldn't pass this test.

4. **httpie_2 is the only clean signal**: complete, non-truncated fixes where all 4 conditions failed equally because the LLM didn't identify the actual bug. High line_overlap (0.97+) confirms the "fixes" barely changed anything.

5. **LLM judge scores are unreliable**: judge=5 was given to fixes that produce SyntaxError (black_1/structural_filtered), while judge=0 was given to others that are structurally identical. The judge evaluated code similarity, not functional correctness.

---
