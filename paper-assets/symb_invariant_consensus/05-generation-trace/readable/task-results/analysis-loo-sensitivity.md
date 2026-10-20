# analysis loo sensitivity

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loo-sensitivity_20260521T220615_result.json`
- **Structured JSON:** [`37857f0b93754158e735.json`](../../sessions/37/37857f0b93754158e735.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整输出：

```
=== Leave-One-Out Sensitivity Analysis ===
Full (n=5): rho=-1.000, p=0.0000

Drop R1-Distill   (k=0.248, d=+2.45): n=4 rho=-1.000, p=0.0000 (one-tailed=0.0000)
Drop gpt-5.5      (k=0.563, d=+0.49): n=4 rho=-1.000, p=0.0000 (one-tailed=0.0000)
Drop o3           (k=0.596, d=+0.00): n=4 rho=-1.000, p=0.0000 (one-tailed=0.0000)
Drop Gemini*      (k=0.790, d=-1.05): n=4 rho=-1.000, p=0.0000 (one-tailed=0.0000)
Drop gpt-4.1      (k=0.792, d=-1.47): n=4 rho=-1.000, p=0.0000 (one-tailed=0.0000)

=== Gemini vs gpt-4.1 swap test (kappa diff=0.002) ===
After kappa swap: rho=-0.900, p=0.0374

=== Gemini delta sensitivity ===
  Gemini delta=-2.0: rho=-0.900, p=0.0374
  Gemini delta=-1.5: rho=-0.900, p=0.0374
  Gemini delta=-1.0: rho=-1.000, p=0.0000
  Gemini delta=-0.5: rho=-1.000, p=0.0000
  Gemini delta=+0.0: rho=-0.975, p=0.0048
  Gemini delta=+0.5: rho=-0.700, p=0.1881
  Gemini delta=+1.0: rho=-0.700, p=0.1881
```

---
