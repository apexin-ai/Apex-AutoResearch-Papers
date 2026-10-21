# code plan006 asv calibration

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-asv-calibration_20260520T210016_result.json`
- **Structured JSON:** [`3799ef6d0a0dbbe55a5b.json`](../../sessions/37/3799ef6d0a0dbbe55a5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run complete. Summary:

**Deployment & execution: all passed.**

| Check | Result |
|-------|--------|
| File deployed | 1047 lines, md5 verified |
| All 6 modules ran | Yes |
| JSON output valid | Yes — 0 NaN, 0 Infinity |
| Null values | 348 (expected: ASV entries where no threshold found, e.g. no sign flip) |
| Runtime | 18.3s |

**Key numbers from mock dry-run:**
- **ASV magnitude**: 0.134–3.769, median 0.577 (173/189 non-None)
- **ASV sign-flip**: 1.956–7.218, median 3.646 (41/189 non-None) — many topologies don't flip sign
- **ASV significance**: 1.863–6.931, median 2.911 (21/189 non-None)
- **Type I/II**: ASV-unsafe 113/189 (59.8%) → PPI++ recommended for those
- **F1 vs bias**: F1>0.93 with |bias|>0.05 = 0% (mock data doesn't trigger Baumann disconnect)
- **Inter-model correlation**: agreement 0.53–0.87, kappa 0.44–0.73, error correlations near 0 (independent mock errors)
- **K=10 (humaid)**: all topologies ran cleanly, no numerical issues

---
