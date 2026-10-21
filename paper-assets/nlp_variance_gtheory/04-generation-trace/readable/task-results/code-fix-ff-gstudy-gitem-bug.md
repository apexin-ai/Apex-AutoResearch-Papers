# code fix ff gstudy gitem bug

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_ff_gstudy_gitem_bug_20260522T000548_result.json`
- **Structured JSON:** [`1adc37f595259a8805b3.json`](../../sessions/1a/1adc37f595259a8805b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**MATH G_item = 0.888941** — matches expected ~0.888 (within ±0.005).

Both values verified:
- GSM8K G_item = 0.862852 (expected ~0.863) ✓
- MATH G_item = 0.888941 (expected ~0.888) ✓

Fix complete. The MATH bootstrap is now running (~10 min) but the core G_item values are confirmed correct. 

**Summary**: Changed `divisor = 1` to `divisor = prod(n_levels[f] for f in n_levels if f != "item_id")` on lines 118 and 138 of `scripts/exp004_ff_gstudy.py`. The residual variance component now correctly divides by the product of all non-item facet levels (2304 for GSM8K with 8 models, 2016 for MATH with 7 models) instead of 1.

---
