# code r9 qwq hs vs position bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r9_qwq_hs_vs_position_bootstrap_20260518T083619_result.json`
- **Structured JSON:** [`aa2515c42099d6bcc309.json`](../../sessions/aa/aa2515c42099d6bcc309.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Aggregates now match exactly (HS precision=0.5640, FPR=0.2165; Position precision=0.5192, FPR=0.2414). Results saved.

```
QwQ-32B HS vs Position (L60, W=3) - Paired Bootstrap (10k resamples, n=19):
| Metric    | HS     | Position | Δ       | 95% CI              | p-value |
|-----------|--------|----------|---------|---------------------|---------|
| precision | 0.5640 | 0.5192   | +0.0448 | [-0.0321, +0.1275]  | 0.1325  |
| FPR       | 0.2165 | 0.2414   | +0.0249 | [-0.0606, +0.1104]  | 0.2792  |
```

Both differences are **not statistically significant** (precision p=0.133, FPR p=0.279). The 95% CIs span zero in both cases. With only 19 test traces, the HS probe's +4.5pp precision advantage and +2.5pp FPR advantage over position-only are directionally consistent but lack statistical power to reject the null.

Saved to `artifacts/exp_r9_qwq_hs_vs_position/results.json` (includes per-trace arrays for further analysis).

---
