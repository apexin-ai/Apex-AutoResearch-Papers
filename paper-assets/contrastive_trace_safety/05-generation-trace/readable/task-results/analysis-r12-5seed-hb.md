# analysis r12 5seed hb

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r12_5seed_hb_20260518T132721_result.json`
- **Structured JSON:** [`4e0c55d120829945d8b0.json`](../../sessions/4e/4e0c55d120829945d8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Complete. Here are the results:

## Table 1: Per-seed results

| Model   | Seed |  BA p  | Prec p | FPR p  | 3/3 HB |
|---------|------|--------|--------|--------|--------|
| R1-8B   |   42 | 0.0040 | 0.0140 | 0.0140 | PASS   |
| R1-8B   |  123 | 0.0070 | 0.0030 | 0.2620 | FAIL   |
| R1-8B   |  456 | 0.0010 | 0.0700 | 0.9520 | FAIL   |
| R1-8B   |  789 | 0.0010 | 0.0000 | 0.0340 | PASS   |
| R1-8B   | 1024 | 0.0000 | 0.0000 | 0.0090 | PASS   |
| OT-7B   |   42 | 0.0000 | 0.0000 | 0.0000 | PASS   |
| OT-7B   |  123 | 0.0000 | 0.0000 | 0.0000 | PASS   |
| OT-7B   |  456 | 0.0000 | 0.0000 | 0.0000 | PASS   |
| OT-7B   |  789 | 0.0000 | 0.0000 | 0.0000 | PASS   |
| OT-7B   | 1024 | 0.0000 | 0.0000 | 0.0000 | PASS   |
| R1-32B  |   42 | 0.0000 | 0.0010 | 0.0120 | PASS   |
| R1-32B  |  123 | 0.0000 | 0.0000 | 0.0000 | PASS   |
| R1-32B  |  456 | 0.0060 | 0.0000 | 0.0000 | PASS   |
| R1-32B  |  789 | 0.0030 | 0.0000 | 0.0020 | PASS   |
| R1-32B  | 1024 | 0.0000 | 0.0010 | 0.0010 | PASS   |
| QwQ-32B |   42 | 0.0000 | 0.0000 | 0.0010 | PASS   |
| QwQ-32B |  123 | 0.0120 | 0.0080 | 0.0010 | PASS   |
| QwQ-32B |  456 | 0.0120 | 0.0010 | 0.0000 | PASS   |
| QwQ-32B |  789 | 0.0000 | 0.0000 | 0.0000 | PASS   |
| QwQ-32B | 1024 | 0.0020 | 0.0010 | 0.0000 | PASS   |

## Table 2: Summary

| Model   | Pass | Mean DPrec (pp)   | Mean DBA (pp)     |
|---------|------|-------------------|-------------------|
| R1-8B   |  3/5 | +14.62 +/- 4.49   | +9.41 +/- 2.37    |
| OT-7B   |  5/5 | +20.90 +/- 1.27   | +11.34 +/- 1.48   |
| R1-32B  |  5/5 | +13.71 +/- 1.99   | +11.83 +/- 2.41   |
| QwQ-32B |  5/5 | +19.85 +/- 2.50   | +11.44 +/- 3.18   |

**18/20 (90%) pass 3/3 HB.** OT-7B, R1-32B, QwQ-32B all 5/5. R1-8B 3/5, with 2 failures driven by FPR instability (seeds 123, 456: the pre-CP FPR difference is not significant on those splits). Full JSON at `artifacts/r12_5seed_hb/full_results.json`.

---
