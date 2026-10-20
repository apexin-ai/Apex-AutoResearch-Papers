# fix fewnerd degeneracy calc v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fewnerd_degeneracy_calc_v2_20260518T130227_result.json`
- **Structured JSON:** [`e2ab2464ebf3fb1a63fa.json`](../../sessions/e2/e2ab2464ebf3fb1a63fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，验证通过。

- **改动**: `code/analyze_fewnerd_results.py` 第 163 行，`len(set(key_sets)) == 1` → `len(set(sample_f1s)) == 1`
- **验证**: F1-based degeneracy = 13.75% (4479/32565)，与预期一致；旧 keyset-based = 10.13%

---
