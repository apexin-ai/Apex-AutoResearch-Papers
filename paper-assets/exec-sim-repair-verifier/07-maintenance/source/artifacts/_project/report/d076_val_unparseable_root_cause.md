# D076 Val Unparseable Root Cause Analysis

## Root Cause
Val 20.2% unparseable is caused by prompt truncation on exactly 2 problem_ids:

| Problem ID | Samples | Token Length | @2048 | @4096 | @5120 |
|---|---|---|---|---|---|
| sympy__sympy-14248 | 1406 | ~4947 | truncated | truncated | fits |
| pytest-dev__pytest-5787 | 477 | ~2352 | truncated | fits | fits |

1406 + 477 = 1883 = exact unparseable count at @2048
1406 = exact unparseable count at @4096 (15.1%)

## Why Test Set Unaffected
Val and test have zero problem_id overlap. Test's longest problem (xarray-6992) tokenizes to 2034-2047 — barely fits at 2048.

## Truncation Mechanism
Truncated prompt → model sees incomplete diff → continues code completion instead of answering pass/fail → marked unparseable. Even "parseable" truncated samples have 35.8% accuracy (random guessing).

## Fix
Use `--max_seq_length 5120` at eval time. Val max is 4947 tokens, so 5120 covers all. May need batch_size 16→8. No code changes needed.
