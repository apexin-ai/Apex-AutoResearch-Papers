# eval hellaswag seed43

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_hellaswag_seed43_20260520T092756_result.json`
- **Structured JSON:** [`a10205c75a15dbb63c60.json`](../../sessions/a1/a10205c75a15dbb63c60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All seed43 HellaSwag evaluations complete. Here are the results:

## exp_010 (seed43, pure collapse) — HellaSwag 0-shot (acc_norm)

```
Gen  0: HeSw = 0.4130  (pretrained baseline, shared across seeds)
Gen  2: HeSw = 0.3809
Gen  5: HeSw = 0.3384
Gen  7: HeSw = 0.3187
Gen 10: HeSw = 0.2900
```

Full precision from JSON:
- gen_2: 0.3809
- gen_5: 0.3384
- gen_7: 0.3187
- gen_10: 0.2900

**Cross-seed comparison (seed42 vs seed43):**

| Gen | seed42 | seed43 | Δ |
|-----|--------|--------|---|
| 0 | 0.4130 | 0.4130 | — |
| 2 | 0.3760 | 0.3809 | +0.0049 |
| 5 | 0.3440 | 0.3384 | −0.0056 |
| 7 | 0.3190 | 0.3187 | −0.0003 |
| 10 | 0.2950 | 0.2900 | −0.0050 |

Very tight agreement between the two seeds — differences are all within ±0.005. Monotonic degradation trend confirmed for both.

**seed44 (exp_013):** Only gen_0 exists; training still in progress. Cannot run evals yet.

---
