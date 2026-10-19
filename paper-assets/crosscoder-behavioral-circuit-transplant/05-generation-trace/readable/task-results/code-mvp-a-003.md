# code mvp A 003

**crosscoder behavioral circuit transplant** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-A-003_20260510T132700_result.json`
- **Structured JSON:** [`5ad3c454a4bc09f157d3.json`](../../sessions/5a/5ad3c454a4bc09f157d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
WORKER_RESULT:
status: completed
exp_id: mvp-A-003
script: /home/sonny/crosscoder-bct/mvp_a003_bias_injection.py
log: /home/sonny/crosscoder-bct/run_a003.log
result: H2 NOT CONFIRMED — bias injection also fails
  - All 5 alphas fail Gate 3 (movement threshold ≥50%)
  - Best: alpha=2.0, movement=2.84%, ppl_ratio=1.0109
  - Alpha=5.0 also breaks Gate 4 (ppl_ratio=1.0827)
  - Feature k=1353 (same as mvp-A-001), ratio=6.93
  - Conclusion: problem is NOT the surgery site — both W_out rank-1 and residual bias injection produce <8% movement
```

---
